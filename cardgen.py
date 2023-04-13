title = input("title:")
desc = input("desc:")
loc = input("loc")
time = input("time")
print()
temp = f"""\
 <div class="item-container">
            <div class="img-container">
                <img src="" alt="{title}">
            </div>

            <div class="body-container">
                <div class="overlay"></div>

                <div class="event-info">
                    <p class="title">{title}</p>
                    <div class="separator"></div>
                    <p class="info">{loc}</p>
                    <p class="price">Free</p>

                    <div class="additional-info">
                        <p class="info">
                            <i class="fas fa-map-marker-alt"></i>
                            {loc}
                        </p>
                        <p class="info">
                            <i class="far fa-calendar-alt"></i>
                            Tue, Aug 18, {time} IST
                        </p>

                        <p class="info description">
                            {desc}

                        </p>
                    </div>
                </div>
                <button class="action">Technical Event</button>
            </div>
        </div>   """

print(temp)