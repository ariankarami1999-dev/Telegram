<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/boe2X7UN5RONsJZJuHPKkZO2C4VzdlsG3hsiF4Ja4bmrr2tIvFzP3fg8VndXA7UNum7QMN-iS2JAsF6G1UX_Znl4GW_rEUf_fNmNKMkqGDTOyrfsrI7L8B0LQ49La_ilSrL3CKZJpAsIadyWXfcRW_ChghgJyQWdFOu3YFzjr8-xJSV7fg2u9kPtH03_zramCBks3sURp9zDfSXziL0mEKpeOUsVTfUviIxd52EJvEUrJc3TDR_-o1KxiUqBLVKVmh3QTW63U-lrmf79ueS3_HKn4WTXJAnIaLitQXExjf9gBZy2KBOdQ8FE8zpWz3rbqLoynXgb6Zld_0lh8SOW-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">☄️
'شلیک موشک از کرمانشاه'
‌
بعضی از پیام‌های دریافتی:
سلام همین الان صدای موشک از کرمانشاه اومد
سلام صدای جنگنده در کرمانشاه
سلام وحید جان.
همین الان ساعت ده و نیم دو تا موشک از کرمانشاه شلیک شد
صدای غرش  شدید ترسناک ساعت 10.31 شب کرمانشاه میاد
وحید همین الان از کرمانشاه موشک پرتاب شد
از کرمامشاه الان دوتا موشک شلیک کردن
صدای پرتاب موشک از کرمانشاه الان
سلام وحید جان
من کرمانشاهم
الان ۱۰:۳۰ یه صدایی شبیه شلیک موشک اومد
مطمئن نیستم، ولی دقیقا شبیه صدایی بود که زمان جنگ میومد.
🔄
توییت ارتش اسرائیل:
ارتش اسرائیل موشک‌هایی را که از ایران به سمت اسرائیل شلیک شده بود، شناسایی کرد. سیستم‌های دفاعی برای رهگیری این تهدید در حال فعالیت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/VahidOnline/75995" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای جنگنده در تهران که لابد داخلی است:
سلام وحید جان ۲۱:۳۲ شمال غرب تهران صدای شدید جنگنده
درود وحید جان
صدای جنگنده (؟) غرب تهران
۲۱:۳۲
صدای جنگنده غرب تهران ساعت ۹:۳۲
بازهم مرکز تهران صدای جنگنده یا هواپیما رو نمیدونم ولی خیلی پایینه ساعت ۲۱:۳۳
شهرک غرب
صدا جنگنده
صدای جنگنده ساعت ۲۱:۳۵ دقیقه، شمالغرب تهران
مرکز تهران صدای جنگنده میاد شدییید
صدای نامتعارف جنگنده در مرکز تهران از ساعت ۲۱:۳۳
غرب تهران صدا جنگنده داریم 9.32
۹:۳۱ شهرآرا صدای جنگنده میاد وحشتناک خیلی پایینه
سلام الان نیروهوایی صدای خیلی عجیب میاد صدای جنگنده ست انگار خیلی بلنده
سلام وحید . ساعت ۹ و ۳۳ دقیقه شب مرکز تهران صدای جنگنده میومد واضح . ۱۷ خرداد .
سلام ساعت ۲۱ و ۳۳ دقیقه شنیده شدن صدای جنگنده زیاد ، امیرآباد تهران
صدای جنگنده میاد سمت مرکز شهر
آپدیت: کلی پیام مشابه میاد که دیگه نقل نمی‌کنم. درباره صدای هواپیما اهمیتی نداره که در کدوم محله شنیده شده.
بین پیام‌های اولیه دو تا پیام هم بودند که نادرست به نظر می‌رسند:
سلام وحید، اینجا شهریار صدای موشک میاد. احتمالا از بیدگنه جمهوری اسلامی داره موشک میزنه
وحید از بیدگنه موشک زدن ۲۱:۲۸
صداش تا فردیس اومد قشنگ
آپدیت:
در پیام‌های بعدی روی این تاکید می‌کنند که صدا طولانی بود و چند دقیقه طول کشید.
بعضی‌ها هم نوشتند این بار هم هواپیمای مسافربری بوده با رفتاری عجیب و پرواز با ارتفاع کم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/75994" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBwwrpkuXXsNASnIwAFF1BH-hJaNwo7gd_xwN86gwQs-x6_fHVQcGacgudO5LYO5hz8Nll90iGzyHYZMo23YFdgH5yyfAOjnwqQweGrtGFzm3lvbA8OTiNKgQXDLC23zdN0gsWHeZbBKXmTnB6io6o1fS7kSOSQpW9b4HwQcIeYQ660fp8w41vdz_RW2yOduxGXkZOh5ygY0tFQzcVKyhIlIGylTG8P4FqJ-zQlriEO6qlPSWuvV5BL__E5YfI9bmiJ8ygMVrJFLseFxLThJuowHNCdw8n-UCZ1NdIz4vnXmAnT5YVm38VP5ZbrgNcP1shFxWrUsT-_yJY0BrfnSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان علیه صدا و سیما
رئیس دولت در جمهوری اسلامی، تلویزیون حکومتی را در شبکه فیلترشده ایکس تهدید کرد:
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75993" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oUjieCrOn8wEmCIVvsxoRQbQzQXzOF3an0HCiBDh5C8B8uo6gdWNdNF3I5Lmto27KV8VYquFhi8BSCjI4xROpKszMkU14TcmKnaBpGSY9_jolxG1UiWHdI0fH_w6I-zF7QL3F_olnyGNFyTOyGLPNX3QmyetiD047I1ZPJTCMakZnAB1xBvEm6yiuEplHh4h8FGqVAAfa0rGsky8eFhGI7Sf2nPfARjkb_HtMva8zP9Sl5jvUFXpjnv2HMkgW1TAoyZj-ujFUV1I1JNTyjsbLU0mN62w6Vqfi8_0WFv9Lwf2TSBSt84mydQYAINmrqhGhxUtBtxvKFFYGMQGGRYy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvmDaJTf80p1YtAocwYjpfK50iGrdUw-L95WKywX3c7MyYyvsYUgTsq1ApVqPkFz1Un-K078jj52asGfXlvFwuF8nhTUf0y9t12rPy-4wKuWrFKjyCU3HuVH6eb5xsLn_hl6BMc4yFFYFgK8FLC7ZAR62OMHspi5-tGUelbUuqedB2EeFG0f9FdJf6YFwRfn1nlJA8guiQSGHkYlpbY67jHAK_HyU2IQUEFGEeV9NfNWOVnhtsLIDXp-RxDoxV7BXJHH_1ElVvO0g3J96harIEpCTzmipNK1oWqWSjGfajD8YPN3Fwz-KcMxNsF2TDfkHrZXKIo_0ve79xMDiywoZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در واکنش به حمله اسرائیل به بیروت تهدید کرد پایگاه‌های آمریکا هدف قرار می‌گیرند
:
mb_ghalibaf
رئیس مجلس شورای اسلامی که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوها با ایالات متحده است، در شبکه ایکس نوشت که محاصره دریایی علیه ایران و «چراغ سبز امروز آمریکا» به اسرائیل برای حمله به ضاحیه «پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند».
اسرائیل ساعاتی پیش اعلام کرد در واکنش به حملات حزب‌الله به خاک خود، مواضع حزب‌الله در حومه جنوبی بیروت را هدف قرار داده است. از سوی دیگر دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد که قصد دارد نیروهای آمریکایی را تا زمان «تکمیل» روند توافق با ایران در منطقه نگه دارد.
قالیباف در بیانیه خود ایالات متحده و ‏اسرائیل را متهم کرد که «نه به آتش‌بس پایبندند نه به گفتگو باور دارند» و افزود که این کشورها «با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75991" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSPeEgJe9lAxWospZvpQY-KZAEgY5KZD21KieJbgLIinDDUoGD-paNHG3f1MD6TOx1Dnu-gvM2EBjT2D0ATzlCULO9kQ82_zTv7EeDSH0CIiFdEJUqfAdJnDcJ77Z-yjfgHHHfFA3WlH46QhDhAvO-mojiW3EVLesJj0iSU-uR1sP2Z4zfUa9ENWUtCcASVJkzpyWeW_dkQGQuIt_cFli3FZo0BAwxKJHMLaSPLNpvx0Of9r_x7vHU6HVcIzQw3AiSZAYr_AY18w5fOBQx3-_FfL9lwmSnTSZVBfw0-MIhaumz9MsZLoqDnZfz3cfTQGidb10lBIdOAHBx4bkelxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: امشب به اسرائیل پاسخ دردآور خواهیم داد
توییت سخنگوی کمیسیون امنیت ملی مجلس شورای اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75990" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-1BHsoc7LtoUMjzCTDI0nwW3SSg6IMMlVVdFzgb03HL8xTgSAgSz6yXRTx_3dWjU7tH7UqQJHB3dyEBVUCQ4smoPAcl3k47NBhiArFI3ugAV9Wgy9PFHq6SJsskZfyjm8vcENXc8n-7BVEJiUKh-Ist_vnJjMIE863o1ukXfpX0ax71CK0yDHVwSq7LrLEk9F81iHjxhcDJLQ8nkC2sr_sTYSHdMkDsfyl2k6NlYjrO00uVH1l3TxgrCUqZhPBerh-1jVVGc0xTXCAxwxP-nw4EafnKjGjs_fQgGQioRV1yBF5gP4_RaHc9Pzp7-oTjbMAeu9ZCevBgr4cLQ_8Kjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«وحید هاشمی» ۲۶ ساله و تبعه افغانستان، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در خیابان ۲۰۲ فلکه تهرانپارس هدف شلیک گلوله جنگی قرار گرفت و ساعاتی بعد بر اثر شدت جراحات جان خود را از دست داد.
به گفته نزدیکان، گلوله جنگی به ران پای چپ او اصابت کرده بود. وحید هاشمی حدود دو ساعت پس از تیراندازی به بیمارستان تهرانپارس منتقل شد، اما به دلیل خونریزی شدید جان باخت.
خانواده وحید هاشمی پس از ناپدید شدن او به جست‌وجوی او پرداختند و سرانجام پس از شش روز موفق شدند پیکر او را پیدا کنند.
پیکر وحید هاشمی در تاریخ ۲۴ دی‌ماه در قطعه ۹۶ بهشت زهرا به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75989" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KauOIoIwIUKF8PpSx4irAHCkO4JR5MoG_GXySj0qOadexX8_XbfOHPYJSn9hwAMpjynEQWVnJkccPPHcsbJlwKsJNJ2hfNclqO7PcoB57YqmAKVsIHqD3lr8SqXeAfqRDpqI1odwr0e8g6BJJUyQ8qmRgokdMMOM9lGcC3fv3HR4n9gIGyZuMJxex5WCwU59yynRoLWvp3Rdgx5FoZ_JPrXIN9Hl1gJa-kTdxVAo_nsvZYEqn1SZ1eadDGYRcDKdvuRlCUE_ZnhxNtPeMa0c7V_Q7LE0Op98z9TRi3pwvZPjC2mHygkKxUA7hSmet11S2HxjJqA09vB-pY5YLZOwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fgh8ak7i2HwvosRdsy3bj1bXCRsCpB6Ybw1TtuBk9iOypb0RTyJ5HroqZZnQN1UT0SrBZvNsMexcqvkR2zclpmZetnxfTuMQTuQAkH6JtjcxYJ6ZGUDRf8zwa5tWjFjMEVtz4Gi-2Z6eBEvhpvZARavwsdvJvnRX1vYGtMJ7t5pqPa_dCSIT7Z2FTQJ-jH1DpM7MD5jdKq75OWsYCmpyhScUqUXTQy0kOhaBI-wo7Ubxp4Lc_s2filqNPZ5UY2rd3y_G-2jJcQzLD8cMvBNFtY1-JTQHLKvo26ZluSTS_6BcTuFDoInTNVD7DtJRhuaGBU4mOlafgeRWAvEyEPa5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vRIDaFaIAlo6ZjRERWUrHezhoKwpdOltXFpvKWPn88IvKTwUy4fc6GoZRl9Q-M62Rq_9S2VqXrr_cAKSyvKadFdOet4jg7H__3rTXX_braUkN1bKJnz_w8_6EAhOsgiN3kkR8eOWL9z9rL-tdQy-IbwV0e_Qmmlyxc6zf9KD8gnTWYP96vCVO3cu037AJygtgsjk93bbSK6BfpLBnwz_r4gWihKVlIKCDH5lKwzCO8hbioGZ3z5l8jdk3v_ZASlLPxCqwClKR5_nq2OqwrDED2UMTNHkM-gldqjP9BuPn0aSK3Xvc90TXUo-w_E9JpmqfCT8ZFg3gbcsYL9vrP55Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rRDfoCo0GQOGANe63TtrZXfUo9fmARMfW4MWkqKjYE-9m3r3llD3WonAwxSo3fN_doh4P5FeM3Li0www6X4QOGZpfN9VaeEddYF45NGXy-ax-SbcUqX2wqy6qjANYNvW7oQdiosWkuYsfSCoh6ac3Qh3-iD9XPs3ko81-ZKdccfgk-3rY0KRl0WVJcTPRenuyhuwEwb06VIyyP5B7CZbohNwc7CZNtFm3_hzLSUIrjJ9XfSXk82izm9VhfYgX6Ocm1HwkBrpo0C_spaV8Oe5dwjq34Sk1jFOnQafbyG_SG_tv-dLRV0dlMjCeiVVsz4Ylptow2tm3wzJEGDsctBQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYbH1OitQn5w3xOs0-ZjfJAqmvUhK5qE1rdwO6-Awq1XADDqqjFawc1wzi5ePZ-VtQm4DUMILzJyX_OFhyGnKfz7LZxiu_oxbNVMMcmDGp0lT6wZQ8_U3vlVndTFl6D2nBFcYOKYE59M4YtdmLRA6qMpTnYahJB5WZwwOrGD-hPbSESKf6fRV_eTmVOg8AxNGbhh9PdmVeuj2yleG3e9F8PGmStikaIdlZwW6FvSobk0WjOPwTXXbk2xnQO9HtyvM_fXbtif5UD3c-8bVR3apW66VQgPSEcR2uPjQH4OO5ePuV-Sn9PwCj8tfskCffXHs6Ck7DxdBVVVLlGkG_4X9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ: پیش از نهایی شدن توافق، دارایی‌های ایران آزاد نخواهد شد
دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
او افزود که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: «بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.»
رییس‌جمهور آمریکا اضافه کرد اگر بتواند با تهران برای پایان دادن به جنگ سه‌ماهه میان دو کشور به توافق برسد، آمریکا با ایران برای جمع‌آوری و نابودی ذخایر اورانیوم با غنای بالای این کشور همکاری خواهد کرد.
او افزود در صورت عدم دستیابی به توافق، واشینگتن توان نظامی جمهوری اسلامی را بیش از پیش تضعیف خواهد کرد تا نیروهای آمریکایی بتوانند با امنیت کامل این مواد را خودشان جمع‌آوری کنند.
ترامپ افزود که خواهان اضافه شدن بندی جدید به توافق است تا ایران نتواند با خرید سلاح هسته‌ای یا تجهیزات مرتبط، محدودیت‌های توافق را دور بزند.
او گفت: «پرسیدم اگر آنها خودشان سلاح هسته‌ای تولید نکنند اما آن را خریداری یا به هر شکلی به دست آورند چه؟ من می‌خواهم در متن توافق عبارت خرید، تهیه یا کسب سلاح نیز گنجانده شود. آنها نه حق تولید سلاح هسته‌ای را دارند و نه حق خرید یا دستیابی به آن را. تهران در ابتدا کمی با این درخواست مخالفت کرد اما از موضع خود عقب نشست.»
دونالد ترامپ، رییس‌جمهور آمریکا، درباره مجتبی خامنه‌ای و محل اقامت او گفت: «او به‌شدت زخمی شده است. نمی‌خواهم بگویم می‌دانم کجاست یا نه، اما احتمال زیادی وجود دارد که از محل اقامت مجتبی خامنه‌ای مطلع باشم.»
ترامپ همچنین اعلام کرد فعلا قصد خروج نیروهای آمریکایی از منطقه را ندارد؛ حتی با وجود آتش‌بس شکننده و ارزیابی او مبنی بر اینکه توان تهاجمی و دفاعی جمهوری اسلامی به‌شدت آسیب دیده است.
او افزود: «هزینه نگه داشتن حدود ۵۰ هزار نیروی آمریکایی در منطقه بسیار ناچیز است و ممکن است برای اعمال فشار در مذاکرات به آنها نیاز داشته باشیم».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75984" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=hvmfqOIauQZsFCGJ8NliMYLzRboM0NncEwAYyR7ZOTZJ7lIZr9GHc47nc5DZ-Zeh_PTtsaIiPPZ0eaqAQ-BzLmiUYaJ3F7wCqThDnOGIVeeD4YI5Og6rq6cfs4MUz-E70fUchlZCvk_yMGrUOrTVB-jztSTlyew5ADepwErzbrg-kjX6L6Z56x-EN88dVV2f61G-OVIaGmLbwOkKqSdpbHpddH7g9tSDAxl53cr9ecX5RK2wj6W8es_6etQ5y0DaWFsBKLGYR5IFP0ZFzh1flFb5dCfp5qKVWp2oefyGRFhXUZjh69AqnCaCAZcnEs-L0CTZDEpRZOEs8sP2ym8dZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=hvmfqOIauQZsFCGJ8NliMYLzRboM0NncEwAYyR7ZOTZJ7lIZr9GHc47nc5DZ-Zeh_PTtsaIiPPZ0eaqAQ-BzLmiUYaJ3F7wCqThDnOGIVeeD4YI5Og6rq6cfs4MUz-E70fUchlZCvk_yMGrUOrTVB-jztSTlyew5ADepwErzbrg-kjX6L6Z56x-EN88dVV2f61G-OVIaGmLbwOkKqSdpbHpddH7g9tSDAxl53cr9ecX5RK2wj6W8es_6etQ5y0DaWFsBKLGYR5IFP0ZFzh1flFb5dCfp5qKVWp2oefyGRFhXUZjh69AqnCaCAZcnEs-L0CTZDEpRZOEs8sP2ym8dZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز یکشنبه اعلام کرد که ارتش این کشور مراکز فرماندهی نیروهای مسلح را در حومه جنوبی بیروت هدف حمله قرار داده است.
در این بیانیه آمده است: «مطابق دستورهای نخست‌وزیر نتانیاهو و وزیر دفاع کاتز، نیروهای دفاعی اسرائیل دقایقی پیش یک مرکز فرماندهی نیروهای مسلح را در منطقه ضاحیه بیروت هدف قرار دادند. این اقدام در پاسخ به شلیک‌های حزب‌الله به سوی خاک اسرائیل انجام شده است.»
این نخستین حمله به پایگاه اصلی حزب‌الله از زمان برقراری آتش‌بسی است که روز ۱۶ آوریل با میانجی‌گری طرف‌های بین‌المللی حاصل شد. آمریکا هفته گذشته اعلام کرد دولت‌های اسرائیل و لبنان به تمدید آتش‌بس به شکل مشروط دست یافتند.
حزب‌الله، گروه مورد حمایت جمهوری اسلامی، پیشنهادهایی را که برقراری آتش‌بس را به خلع سلاح این گروه مشروط می‌کند رد کرده و تأکید دارد که اسرائیل باید ابتدا حملات خود را متوقف کرده و نیروهایش را از جنوب لبنان خارج کند.
ضاحیه محل اصلی استقرار فرماندهی و نیروهای حزب‌الله است. این گروه از سوی آمریکا تروریستی شناخته می‌شود، اما اتحادیه اروپا تنها شاخه نظامی آن را در فهرست سازمان‌های تروریستی قرار داده است.
ارتش اسرائیل ساعتی پیش گفته بود دو پرتابه شلیک شده از لبنان به سمت خاک اسرائیل را رهگیری کرده است.
ایران که در حال مذاکره با آمریکا برای رسیدن به توافق پایان جنگ است، پیش‌تر تهدید کرده بود در صورت حمله اسرائیل به بیروت، جنگ را ازسرمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75983" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=bHPdBYSm0Dlq8w0aqapnYritTyfYBCIOCNPRre80DKxmqEDwc9xg8qjRGMNZeINtxwf9hGs8AWdIcYjFRpGasQ1ySm0Hho0QfngNLUVaG4PTr-VxH67a-2KKgN03kS6meMBxacIMXfp0A8a7n5u-pAthId5QnZrW4bRuRUiJdOAx4IeMl50Y9vXpkhjB_L14K2omqnMendpO5pEX4BobRXpJHEd5v3lcbkMU2DQd5-O5RyJ13rHmiN5iCf-xv1MILjduQwCMtt6BoeW3wZhSCtMoXncrK9X0OlHeyM4Sw15wXcsx6YKv0BJfU9XIeezxQgo6ZbrtE8omOVTMAen6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=bHPdBYSm0Dlq8w0aqapnYritTyfYBCIOCNPRre80DKxmqEDwc9xg8qjRGMNZeINtxwf9hGs8AWdIcYjFRpGasQ1ySm0Hho0QfngNLUVaG4PTr-VxH67a-2KKgN03kS6meMBxacIMXfp0A8a7n5u-pAthId5QnZrW4bRuRUiJdOAx4IeMl50Y9vXpkhjB_L14K2omqnMendpO5pEX4BobRXpJHEd5v3lcbkMU2DQd5-O5RyJ13rHmiN5iCf-xv1MILjduQwCMtt6BoeW3wZhSCtMoXncrK9X0OlHeyM4Sw15wXcsx6YKv0BJfU9XIeezxQgo6ZbrtE8omOVTMAen6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کشته و دست‌کم پنج زخمی در تیراندازی مرگبار در اسرائیل؛ دو مهاجم کشته شدند
ارتش اسرائیل اعلام کرد دو مهاجم حمله تیراندازی روز یکشنبه در مرکز اسرائیل، پس از عملیات نیروهای امنیتی کشته شدند؛ حمله‌ای که به گفته امدادگران، یک کشته و دست‌کم پنج زخمی برجای گذاشت.
این حمله در چند نقطه در نزدیکی حصار امنیتی کرانه باختری رخ داد. امدادگران اسرائیلی گفتند قربانیان در سه محل جداگانه هدف قرار گرفتند.
به گزارش تایمز اسرائیل، یک مرد ۳۱ ساله که نزدیک تزور ناتان هدف قرار گرفته بود جان باخت و یک مرد حدوداً ۴۰ ساله در وضعیت وخیم به بیمارستان منتقل شد. چند زخمی دیگر نیز با جراحات متوسط یا شدید به مراکز درمانی انتقال یافتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75982" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYabQFFKkzllgmZOsMOBro2GrOI7Cuxeqn_akmMHBH_dVXMmgWZvD-7cYqrufnYEP0BlVyuL87tCGTBZ9DqNzUdPFPG2s8sMsSEXi8vEiUwOhmSBzINyRbnOP54owYHvrMIOZUPZFCcT-2hTfpNuPrn0AelFKT5zmV9cuQh2q-XZ5J2kdwFH3y69lMnPOrsBCmEE2ESEhgNRIRs3eiXG-izxJwvRyU7eGDruTKOb-E0NtaO2aYmkr9idIo0wJ8WIQDrN2IQvVqm_-t3SRdFAwS7uiFLYN9Wh3yMltWPCd6qkGrckh2-Mmybb-cSeOJpU5JmlMlqTm1KE6f9YsqJ9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان که حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است، روز یکشنبه  ۱۷ خردادماه آن را به عباس عراقچی، وزیر خارجه جمهوری اسلامی تحویل داد.
خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه، ۱۷ خردادماه، ویدئویی منتشر کرد که وزیر کشور پاکستان در آن می‌گوید حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است که به عنوان جانشین پدرش، علی خامنه‌ای، معرفی شده است.
در سه ماهی که از آغاز جنگ و معرفی مجتبی خامنه‌ای به عنوان رهبر می‌گذرد، نه فایلی صوتی از او منتشر شده و نه ویدئویی که نشان دهد او از حمله مرگبار به بیت پدرش در روز ۹ اسفندماه جان سالم به در برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75981" target="_blank">📅 17:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUhirIV7-L7MYhRxjfJZljGwvJqguWq0QCRATVJPG3iCzlEqguEPrhzfVBmMt68HDUpXLv9GearopvMiPts_Bgg7LsQwxqwXfhRT6jG6gM61KSKHNe5Qd1Klh4M3xu3tlkPbhRMQUGXKGfMEwNoukhac5Pi09YtdKZRsxEs_5UH3eB_tUVYS_vNxLc78jsnf2SJ6xSvUYL5SRapIS0MkwLkbsZAHNJP40dP9d8LHq3iWqzdGTjc1B3uvkl-gC-njoAuEFIntJnHSn5LRJZy9BZi_vtHj9P-cuD_NubG62GrdN2mxfCj3YBNTZ7SRjdY0jaMsfGdrlJucVBuvAN7Q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف برخی گزارش‌ها درباره ورود و خروج تیم ملی فوتبال ایران به خاک آمریکا، رئیس فدراسیون فوتبال کشور روز یک‌شنبه توضیح داد که تیم ملی یک روز قبل از هر مسابقه اجازه ورود به خاک این کشور را دارد.
پیشتر ابوالفضل پسندیده، سفیر جمهوری اسلامی ایران در مکزیک، گفته بود که بر اساس شرایط تعیین‌شده برای روادید اعضای تیم ملی فوتبال ایران، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک آمریکا را دارند و باید همان روز این کشور را ترک کنند.
به گزارش ایسنا، مهدی تاج که خود نتوانست ویزای آمریکا را دریافت کند روز یک‌شنبه همچنین گفت: «واقعا عجیب است که اینها تا این حد در حوزه اداره فوتبال دخالت می‌کنند. این کار نادر است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75980" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDSa-JBp1iBwHd4V3GQ04EM0F2mY_7_E3i-XlsbvvExIDSJ04nqOU1KbaOI9PQn9O7x-g_7VLELXQnjXZQnSLUiAWVfZU4YquFmKSXmyuhWeu7a-kOXdxr06ZLNNeLgq9i-d6NVB2JYHLAZMhtkGPNGFgFhOjn4aN4GjJHnh7anSCTat4N1mFmwXGuaqn5Y2aArmrVXqEB5vB4oMUOC4CP3AnCwuqfZinua0Iq70CNFxrO7NmZWJ-GjNq4f0TNyfPOemCJZSRPIEpgTrDm6t0s0V8Nyx0QRtaX54UQklUYt7_whoXajQbDQiSsX_DIl0aXnXj_Fse4e0R2F2TWC1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون، روز شنبه ۱۶خرداد ۱۴۰۵ در گزارشی درباره اجرای قریب‌الوقوع حکم اعدام پنج زندانی سیاسی به نام‌های مسعود جامعی، علیرضا مرداسی (حمیداوی)، فرشاد اعتمادی‌فر، حسن مصلاوی و رضا عبدالی هشدار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75979" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4V3yodlu2V3fBcqMru1ETGRrSQwyiJYbaOE_I3aRY2KLU1DiaycsjN_Y63yslQaa7nv28bVJEG0CjpHR4oWtn0X5WWd8Peg75bmsm_4hruEx4A7V4PVVuk-VsOL7_oQSU7_OyGSUaVvovKPw9cv3nbxsZ0CnYVKvOXLGy3-KVkGzhB4_cG1b0iSzGsECqY1YVV7CCdnRcP95toWcPErAVWSmCdEpOC2-qES6ge6RwoSvwqb95MU_kM7c_FmMjKfySaFb-lWphmcXhwL-E0ZWYntSURiCk7JUZXrJvBmBiBPzVvWneo-2iliJ4W2fsFHIR-baqJlNFi5JoA03QYMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، شنبه‌شب به وقت واشنگتن در بیانیه‌ای گفت اوایل امروز، نیروهای ایالات متحده در خاورمیانه دو پهپاد تهاجمی یک‌طرفه ایران را که تهدیدی برای تردد دریایی بین‌المللی در تنگه هرمز محسوب می‌شدند، سرنگون کردند.
سنتکام افزود که نیروهای آمریکایی همچنان آماده در برابر اقدامات تهاجمی جمهوری اسلامی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75978" target="_blank">📅 05:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJih5IIx-j5tyrx_WmyUDZ0-uMyR3kOhG_8t5-LU1BAsxLL020FZbnZSyuHDaPNPRnbK9S0XLV17gmBMkRYrbIOfgCbXavNlOcss2jltkeJ273hJRVmHgIQdvVgWUPj-gT8GOQHyj5x5h35JZoBHSLYqrlreXDiDjG7YhAVdC3T1Q8qgrUHIZZsYY5HNuv_Ro3Z9MTELvAinXAqswno221La6G-JBiBg_AWj5dCsRS9VVhhY8NLoz4JyJ4NEoHtag7_h29R87VrX4gMT2_HLRWxnHAS1fypPcUPJxVYRa0kf2VzcSRHnKrGZ9-w7_Pu8UpdSWe0klIYZJMKoSQb1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فرانسه گزارش داد، ابوالفضل پسندیده، سفیر جمهوری اسلامی در مکزیک به خبرنگاران گفته است بر اساس شروط تعیین‌شده برای ویزای اعضای تیم ملی، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک ایالات متحده را دارند و باید بلافاصله پس از پایان بازی، این کشور را ترک کنند.
این محدودیت سخت‌گیرانه در شرایطی ابلاغ شده است که کاروان تیم ملی ایران روز شنبه، تحت سایه یک بحران دیپلماتیک شدید میان تهران و واشنگتن، اردوی تمرینی خود در ترکیه را به مقصد مقر جدید خود در شهر تیخوانای مکزیک ترک کرد.
براساس این گزارش، با توجه به اینکه هر سه بازی مرحله گروهی ایران قرار است در خاک آمریکا برگزار شود، این اولین بار در تاریخ جام جهانی است که یک کشور میزبان، پذیرای تیم ملی کشوری می‌شود که با آن در وضعیت جنگی قرار دارد.
این دستورالعمل جدید واشنگتن در تضاد کامل با اظهارات قبلی امیرمهدی علوی، سخنگوی تیم ملی قرار دارد که پیش‌تر مدعی شده بود ویزاها «چندبار ورود» هستند و تیم یک یا دو روز پیش از مسابقات به محل بازی‌ها خواهد رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75977" target="_blank">📅 02:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/byIm0fHlF0IDSQ9q605SiaOkxZ3fd5RGz_OYezWqJ8H1BVbBaw0Gkzz89hUOuGP2lz5XKzO7FwwOpHodL6amX9qoFPHFUHGkKaOsgTTJlW4JDVhGSvMHbUaaanJBVJmRbsjvHb12Ur6GfFWRfga7mhyu3Q9V1fcCMDOrK7-ODFgbL9f1Akev6Mbx27oDGMpS0pOj8rE9PMdj2gPX5tmAkT2vF3gmubLlp4tgfS1zckqj8VRfnOn5jgjx71VpKg-mprVUerFMYRwAD4DJtVSJCzOlAkosfR2z6HMF83EbNLNGu-d_5T5onn-9YPP9sddOtT3RxgdfZOgBLcJcR7nS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از منبعی آگاه گزارش داد که آمریکا در حال بررسی تحویل دارایی‌های بلوکه شده ایران به کشورهای خلیج فارس جهت بازسازی و جبران خسارات ناشی از حملات جمهوری اسلامی است
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
رویترز به نقل از یک منبع آگاه خبر داد که آمریکا دارایی‌های ایران را برای حمایت از بازسازی و جبران خسارات آینده ناشی از حملات جمهوری اسلامی را در اختیار کشورهای خلیج فارس قرار خواهد داد
رویترز به نقل از این منبع نوشت که آمریکا همچنین بررسی خواهد کرد که آیا می‌توان از دارایی‌های ایران برای جبران خسارات گذشته نیز استفاده کرد یا نه
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75976" target="_blank">📅 00:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تسنیم،‌ منبع وابسته به سپاه:
"روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75975" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C53DqE8Dd-oTuYH__bdIXdp-cVEa4JpFKxwRjqL_1njo1cvCGvrufQOl_TPsu4mxNAwmTHkJnG_eJhnawvg8LqRnoGJI4f5atDGPktv9_o2rBhFsQR8q7Uf54J_SyPIAsFFq2ue6_NJ-22Uimzh_Zj4ByZGjSvo2UY9tdNJ38WaFfuUN4pzdALrYXQgbC90CipYVuvEvTAfx-c0LfNk_GOG_WEqSM8czAlqfNl2FGgV8_5x1IbL3R7Ish2Tfp_uXEf0kCON2r9rP41cJxL9pflVCgnKuWg1_Nd_Q2B3BF3Aqiu_a35-i5sSMWzEzTbt7uBgldMLbWKxB8r-cACNBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد خاتمی، عضو مجلس خبرگان، در دیدار با اعضای شورای اداری شهرستان سیرجان با اشاره به وضعیت جسمانی مجتبی خامنه‌ای، گفت: در جریان حمله روز نخست جنگ، او از ناحیه پا دچار آسیب‌دیدگی شد؛ به‌گونه‌ای که احتمال قطع پا نیز مطرح بوده، اما این اتفاق رخ نداد و او هم‌اکنون در سلامت به سر می‌برد.
این در حالی است که از روز ۹ اسفند سال ۱۴۰۴ و حمله به دفتر علی خامنه‌ای، هیچ تصویر یا فایل صوتی از مجتبی خامنه‌ای منتشر نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75974" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVEFqTCGHQaM8F3QFFswZn7ju5TdkD341in_wSPkhrtC6KygElvk-oK6bgYcaOF69XpGIGojlZlXBnPR12v4p6S4KmG2fUF9vkS33CarAyuzfEPwmaDRdNzN8RbDo4LRx2o7nGW9585iiOM8XHLkXqDJ4usLy5lI6_C6Nr5DK1Aj_YSo0ZWLLP3u5whuGFt29wbuoDsn8ZSDJW00r3zjxuVrcB67AdWTRACZyHj0KmnX40mZvkejrPyNVJpHzdkbn2NtE6_Hd8E8QHLOjTMyki0sB4NC4vcnSABopBBiOTRNS-4J-XGVLamr5OHoR51N2GPxEw-UXtasYDgpIqqk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا نوشت که محسن نقوی، وزیر کشور پاکستان، در جریان سفر به تهران حامل پیام ویژه‌ای از عاصم منیر، رییس ستاد کل ارتش پاکستان، به مجتبی خامنه‌ای است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز شنبه ۱۶ خرداد ۱۴۰۵، گزارش داد محسن نقوی، وزیر کشور پاکستان، وارد تهران شده و قرار است با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار و گفت‌وگو کند.
بر اساس این گزارش، نقوی پیش از سفر به تهران با شهباز شریف، نخست‌وزیر پاکستان، دیدار کرده و در جریان این ملاقات، دستورالعمل‌هایی درباره سفر به ایران و روند رایزنی‌های مرتبط با مذاکرات جمهوری اسلامی و آمریکا دریافت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75973" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQozMp8DxRKAQpRZsfs3hR6f3fUxqrlwq_eHIcIj_k6WU6yWooHG5dEw5_WjawGE4jHQrMrepfibZVyoro8QHM4TNFGJyoYr3MtwzWVRJoktnXxmi4HsmBycX4YX_fJ-DB9i8FCw5wKSjTM7ZXxcnxuUp9mfUbw3RDicfBgMF_amR4vSHvgSMFfeRkdYxdlAr8u5xfe2WgS1j_miyNL88RjQ12eW6rAtKoAZlloFTB_RxZxNRiXSTI7NPDaqvKkTz60z4_Nt_ID4KP_W3RGqQoRTi2gpapRi6Un6Tmgo6Ww96sgZejaMzO2nLPAOcqwF6ljTsEgk7zzRYrbgsNFOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول مسعود پزشکیان، در بازدید از دانشگاه علم و صنعت گفت: در جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان و مردم به کشور بودیم. باید از ظرفیت ایرانیان علاقه‌مند به خدمت به کشور استفاده کنیم و با طراحی مشوق‌های مناسب، زمینه بازگشت نخبگان و استادانان را فراهم سازیم.
او افزود: نباید دنبال این باشیم چرا استادان مهاجرت کرده‌اند، بلکه باید به بازگرداندن آنان بیندیشیم.
در روزهای اخیر، بینش بلور، معروف به قصیر، خواننده لس‌آنجلسی، با حضور در تهران در تجمع حامیان حکومت در میدان انقلاب ترانه اجرا کرد.
همچنین صدف طاهریان، بلاگر ساکن ترکیه، تمام پستهای صفحه اینستاگرام خود را حذف کرده و با انتشار استوری‌هایی، از حضور خود در ایران خبر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75972" target="_blank">📅 20:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKrZlmoThM-W5HOttifvHzk76UGejGE03Bx7l5k7nXZz3gFsSxPtZyv5_mdoXlF2LhYVO5gyWYOperaXGiG60jztRn5fpsobvcBGd0aac80Dy0cFCVJXDPXOx_kZjA1VEluDc67LS3su4vooh4XzUdP2HbbahLjFbfRlod_eswBLx4gbogph-3OqonvNGstCtgIXjlzM56nS7mjs5Tk2L-1Bs53eTP0cnBVgVzV13JFns5A99HqWf0ze6CKn4JWwko4Pa1vMzIzQlXPHHWMkNxlW32FW-MRvm2idTJGvjN1nIJlR-282NBtxYfbCB1RaUmjBi9cUd6j7S5Ktg_JkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در بیانیه‌ای حمله بامداد شنبه ۱۶ خرداد ۱۴۰۵ ارتش آمریکا به تاسیسات راداری و نظارت ساحلی در منطقه سیریک و جزیره قشم را «نقض آشکار آتش‌بس» و «تجاوز نظامی علیه حاکمیت ملی و تمامیت سرزمینی ایران» خواند و آن را به شدت محکوم کرد.
در این بیانیه آمده است که تاسیسات هدف قرار گرفته، ماموریت حفاظت از امنیت مرزهای کشور و امنیت کشتیرانی در آبراه‌های بین‌المللی را بر عهده داشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75971" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OXh6Bn5oYv_6ZGOEUNWUp28hBlAr0ZdcvtquM4OuQOkSK_vLBpE8bbUEM3ZPCjtzPKrZCmKjGYQcgnKV8PndEbv58mLo73VYTzMdLrIgHTh7WtPKCF7s3Qh_93vPLodWxZn_c0y8YgyKgEcfgi7F_Wx1ALRjk1KhLaBpzPmGyld1P1YWeWGex4z8fQSMWpvp2u9thrmyMmyENY1JmoGR1z8AV5vWj1cLXdUrDcWnD4ePFCmSBYN-M-fhtRKLPSoI9yj2fLNYseLeS0musC7aLfuByJpDbt3NWx5iskFh19JAsAFSZe_7fWhDH6t8-0kgXu8enHUFw909_QqS-YnEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lXy-ZW2pxT_HFt-KcqZ8PG9zfILLRhXq1laojyRIMUqWO8H-4xdNDVumej3_VJWFgvVzpYjDCS52WFrSHpgElk1WOJ7Hq_8m5CWtx6qPf-duKsToaO_PWcpXGX4s_HsFCne8Ejih2mBsgdcMpPUfPP5a-yDRnsSB3sHkbqDyBd7-LXBC5t--VEQSNXR8gd-o8zxyTYGZ1DoKmAXIUaHs0r9gVDWfVwQ35ATu92GgCL0WwIYZNLLcUY0ZBsktEiNSeB5Z00Ou7dOx5lXEJVBeyJmlfe38NPWGaJk90vYTBAM1z7owptj8PbHqr2PB3R9Bb2h8MghfjwjaGNqzYRoFxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز جمعه در شبکه ایکس در پاسخ به انتقاد صریح مقامات عالی‌رتبه لبنان تمام تقصیر را متوجه اسرائیل دانست.
نواف سلام، نخست‌وزیر لبنان، روز جمعه، ۱۵ خردادماه، در یک نشست مطبوعاتی با لحنی صریح رهبران ایران را خطاب قرار داد و گفت: «به جنوب ما رحم کنید؛ از تبدیل کردن آن و مردمش به یک برگۀ معامله دست بردارید.»
ژوزف عون، رئیس‌جمهور لبنان، نیز در مصاحبه با سی‌ان‌ان پیام مشابهی برای ایران داشت. او گفت: «اینجا کشور شما نیست، کشور ماست. مداخله در کشور ما وظیفۀ شما نیست.»
در پاسخ به این انتقادات که مقامات لبنان ماه‌هاست با صراحت مطرح می‌کنند، عراقچی در پیامی نوشت: «اگر لبنان ابزار معامله برای ایران بود، خیلی وقت پیش به توافق رسیده بودیم.»
وزیر خارجه جمهوری اسلامی در ادامه خطاب به عون نوشته است: «آقای رئیس جمهور، لبنان را از دست دشمن واقعی‌تان نجات دهید.»
عراقچی در پیام خود می‌گوید: «بر اساس گفته‌های آقای عون، هر کس باشد فکر می‌کند که ایران است که یک‌پنجم لبنان را اشغال کرده،‌ یک‌چهارم مردمش را آواره کرده و هر روز کشورش را بمباران می‌کند.»
@
VahidHeadline
ساعاتی بعد نیز اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در پیامی به لهجه لبنانی نوشت: «بیبیع اللی واقف حدّو، وبیشتری اللی واقف ضدّو»؛ عبارتی که به معنای «کسی که کنار او ایستاده را می‌فروشد و کسی که مقابل او ایستاده را می‌خرد» است.
رئیس‌جمهوری لبنان همچنین خطاب به ایران و سپاه پاسداران گفته بود: «این کشور، کشور ماست نه کشور شما» و تاکید کرده بود که لبنانی‌ها از جنگ خسته شده‌اند و خواهان زندگی در صلح و ثبات هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75969" target="_blank">📅 19:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=h0YRv1vfhMSxEU9lwwcMWhZ7LclbdGGr3Ku-hegp5nD4u1GE6Kplv3MYxkN5UV67sT7ITY4uYw-tSP1sK_ku6fq8mD5lo3Cb_da57d_8jS60m-cK3w_ltU9RauXbpFHvxUuADC6tbKLMkuk0Sc1PrmsTuE3pPjTEXwuy65OJPTD-T4XNYXO_6CZknoLNU_4T5m_wMoxSjnZiPNgcI0xXc6TbfB0Q_RLINUfLaC6CR7PST3TCU1juoV7-dc_ZfC8SVpZG9nPVNpbBKsEH2blINkx1d8Z9N4QROu-g2Qko38QRVnBV71zRqPwo9pBupidAWDng6N1WzhBoCeVJX4UlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=h0YRv1vfhMSxEU9lwwcMWhZ7LclbdGGr3Ku-hegp5nD4u1GE6Kplv3MYxkN5UV67sT7ITY4uYw-tSP1sK_ku6fq8mD5lo3Cb_da57d_8jS60m-cK3w_ltU9RauXbpFHvxUuADC6tbKLMkuk0Sc1PrmsTuE3pPjTEXwuy65OJPTD-T4XNYXO_6CZknoLNU_4T5m_wMoxSjnZiPNgcI0xXc6TbfB0Q_RLINUfLaC6CR7PST3TCU1juoV7-dc_ZfC8SVpZG9nPVNpbBKsEH2blINkx1d8Z9N4QROu-g2Qko38QRVnBV71zRqPwo9pBupidAWDng6N1WzhBoCeVJX4UlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از دانش‌آموزان اصفهان روز شنبه ۱۶ خرداد در اعتراض به حضوری برگزار شدن امتحانات تجمع کرده و با سر دادن شعار «دانش‌آموز داد بزن، حقتو فریاد بزن» خواستار تغییر نحوه برگزاری آزمون‌ها شدند.
@
VahidOOnLine
صدها دانش‌آموز روز شنبه ۱۶ خرداد در شهرهای مختلف ایران ازجمله تهران، مشهد، اصفهان، شیراز و چندین شهر دیگر تجمع اعتراضی برگزار کردند.
دانش‌آموزان در تهران مقابل دبیرخانه شورایعالی انقلاب فرهنگی و در شهرستان‌ها مقابل ساختمان وزارت آموزش و پرورش تجمع کردند.
آنها به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری معترض هستند.
گزارش‌های غیر رسمی از حضور نیروهای انتظامی و یگان ویژه در اطراف محل تجمع دانش‌آموزان در مشهد حکایت دارد.
پیشتر هم صدها دانش‌آموز روز سه‌شنبه در شهرهای تهران، مشهد، همدان و چندین شهر دیگر با تجمع مقابل ساختمان وزارت آموزش و پرورش به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری باتوجه به تاثیر منفی جنگ بر آمادگی آن‌ها برای آزمون ورود به دانشگاه اعتراض کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75968" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5eFd6ugv-CepkT-PBGxfTcgIkDY-2yJvEr0s4l9xYtS3lkBgo3Vps6QGB2fWdnBaHtoFF2t1YhWE8LefcMA4o_BuULj4xeg2lM3zhkWwKoBE3JZ77MOlWnx8hlmTfLLN2x6zu9teOOUhcl6bxGfP0KKryh_1CUUYf8Ws0afCluDIFXj69_dL7SBvJ19Rvuj3bMGc5l-Q7uW0Zvso2vTAtMfzWOGCJ-F-kRHph1i7aIgrq3nhsMMLENf8u5GPBZvhLFaHwDGz9jv2HVKno5eVcPg4bV1o3IFN00NIx2l4sCmkNpGZjb-Py0E2WrJhb_lTVKkFsX4-jg1eCyHzrAgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رضا کرمی» ۳۴ ساله، ساکن کرج و اصالتا اهل شهرستان طارم در استان زنجان، در تاریخ ۱۹ دی‌ماه ۱۴۰۴ با اصابت گلوله جنگی به ناحیه قلب جان خود را از دست داد.
به گفته منابع مطلع، رضا کرمی به حرفه ماساژ مشغول بود و در کنار آن به طراحی و نقاشی نیز می‌پرداخت.
خانواده او پس از ناپدید شدنش، به مدت حدود یک هفته در جست‌وجوی او بودند و به مراکز مختلف مراجعه کردند، اما اطلاعی از سرنوشتش به دست نیاوردند.
بر اساس این روایت، خانواده در نهایت پیکر او را در بهشت سکینه کرج شناسایی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75967" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu7I_TJmwEp7qwXtL1cSpJWAQUH-6QCQFGkP1N1ZqBv0YhH3Qdl5zDyJHC6lAiBmuiB2asfs9oN5lBDZ26wNz62h1jtvrYtoQo4SjUqgNnQT1x8E9ECSdaM401i4ppFv7kVJAutJFU-RzysPUtWFa9iVe7qfaAY5qV4Gjh5_RaTzY69I9ZhLOJJxLOS9JJ4A3u-ea8u57I9U57koTzuObVKeb6A4zjrx6HWcoTLiC0JM_uSNCSMXOyODx4Db5LoclNwGSQcNFIvTyUvVpY73sr4cilV6gvu0EPM6suLPy4ef3vLHA3yfcw-8Fpu690sWSmYHlms0z6FFvBG3-uYZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که بازیکنان تیم ملی فوتبال ایران پس از ماه‌ها ابهام، برای حضور در جام جهانی آمریکا روادید دریافت کرده‌اند، گزارش شده است که درخواست روادید مهدی تاج، رئیس فدراسیون فوتبال ایران، رد شده است.
به گزارش نیویورک‌تایمز به نقل از چهار مقام ارشد، درخواست همهٔ ۲۶ بازیکن ایران پذیرفته شده، اما بیش از ده نفر از اعضای کادر پشتیبانی و مسئولان فدراسیون که قرار بود تیم را همراهی کنند، اجازه ورود به آمریکا نگرفته‌اند.
یکی از این مقام‌ها گفته است روادید مهدی تاج، که سابقه فرماندهی در سپاه پاسداران انقلاب اسلامی دارد، نیز رد شده است. آمریکا و کانادا سپاه پاسداران را یک نهاد تروریستی معرفی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75966" target="_blank">📅 08:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/262f970692.mp4?token=CsBSNyHjpcYgBmNfqwoT0B6tCWTEBkGfQ3PELpdh7PctGKFMCLpwfr9vFBn4-SJwgpXRd5kAlt3FlHpDHWu7JfpzWD8U8ydtJag4jS-vtEo1q3qjSmLs7FvKyFfTu7VsPE3kbKWOkBvlP969FWlOWNGklMJDOjRU_LKRIfUHolKDZTMX_YfP2lSgy3m_xq0TQUbu3cUfO8Bpf7E5QCLRCYvevUUbhaaAjCqQUeOvAnZwNcC7Aq_YXSX0UcbzL-t2O7Y9bZ8Gg17MP1iRsY0Ukw1ExmVNL6yHMWFRpRVc__c-MYzl8RX2NE_fgjyof3Oxo11LQFQe1Qx-Oxl3Hc7Vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/262f970692.mp4?token=CsBSNyHjpcYgBmNfqwoT0B6tCWTEBkGfQ3PELpdh7PctGKFMCLpwfr9vFBn4-SJwgpXRd5kAlt3FlHpDHWu7JfpzWD8U8ydtJag4jS-vtEo1q3qjSmLs7FvKyFfTu7VsPE3kbKWOkBvlP969FWlOWNGklMJDOjRU_LKRIfUHolKDZTMX_YfP2lSgy3m_xq0TQUbu3cUfO8Bpf7E5QCLRCYvevUUbhaaAjCqQUeOvAnZwNcC7Aq_YXSX0UcbzL-t2O7Y9bZ8Gg17MP1iRsY0Ukw1ExmVNL6yHMWFRpRVc__c-MYzl8RX2NE_fgjyof3Oxo11LQFQe1Qx-Oxl3Hc7Vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده: "نیروهای سنتکام موشک‌ها و پهپادهای پرتاب‌شده از سوی ایران را منهدم کردند"
ترجمه ماشین:
تمپا، فلوریدا — نیروهای آمریکا در تاریخ ۵ ژوئن، چندین موشک بالستیک و پهپاد ایرانی را که از سوی ایران به سمت تنگه هرمز و کشورهای همسایه در خلیج فارس پرتاب شده بودند، رهگیری کردند.
ایران چند ساعت پس از آنکه فرماندهی مرکزی آمریکا، سنتکام، چهار پهپاد تهاجمی یک‌طرفه ایرانی را که به سمت تنگه هرمز پرتاب شده بودند سرنگون کرد، هفت موشک بالستیک به سمت کویت و بحرین شلیک کرد. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه‌ای محسوب می‌شدند. نیروهای آمریکا سپس برای دفاع در برابر حملات دریایی بیشتر، سایت‌های راداری نظارت ساحلی ایران را در گورک و جزیره قشم هدف قرار دادند.
ارزیابی‌های اولیه نشان می‌دهد شش فروند از موشک‌های پرتاب‌شده از سوی ایران رهگیری شده‌اند و موشک هفتم به هدف مورد نظر خود نرسیده است. در حال حاضر هیچ گزارشی از آسیب‌دیدن نیروهای آمریکایی وجود ندارد و ادعاهای ایران مبنی بر واردکردن خسارت به مقر ناوگان پنجم آمریکا در بحرین نادرست است.
نیروهای سنتکام همچنان هوشیار و در آمادگی کامل هستند تا در چارچوب دفاع از خود، به تجاوزات بی‌دلیل ایران پاسخ دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75965" target="_blank">📅 06:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK5iWF1EwHf5JJJarsE2H_W0naL0W9f5jXdh-Sr5rDT8C3oSOyHWx9mj6MB2u2ZLynct_-P9TckOZhoqjQL8y847nrwoP7SkDUpLfdPQtwo0XCI852p1IaxPcHmwxJcwI0GCtCC1Of6us3yWkFEuU0sUY-23jDMb2AS5nAA-gLDjzoZr17xNL17wahm6LhQsOCpcaDDdqOSOH5brQcANrvg0-PVO9tMKhlAXLsGzt8fw0IrcaXJf4A1TCcl68424enhvAul_mmUGIQXfhMmv196ISrNnh0N6a5I0GGDGZ5i6AT45gTOoS_q4oKVlxlypKSLcIwYWGyX-C5SrQBgDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه، بامداد شنبه، با انتشار بیانیه‌ای اعلام کرد: «به دنبال حملات ارتش آمریکا به سیریک و جزیره قشم، پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند».
@
VahidOOnLine
سپاه در بیانیه‌ای با اشاره به اخطار خود در ساعت ۱:۳۰ بامداد شنبه به چهار نفتکش که قصد خروج از تنگه هرمز را داشتند، گفت یکی از این نفتکش‌ها را هدف قرار داده و متوقف کرده است و دیگر شناورها نیز به عقب برگشتند.
طبق این بیانیه، در ساعت ۲:۳۰ بامداد نیز پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک با دو پرتابه هدف قرار دادند که نیروهای هوافضای سپاه متقابلا با موشک‌های بالستیک به پایگاه هوایی علی‌السالم آمریکا در کویت و تاسیسات ناوگان پنجم نیروی دریایی آمریکا در بحرین حمله کردند.
در همین حال، ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای با اشاره به اینکه در حال حاضر گزارشی از آسیب به نیروهای آمریکایی وجود ندارد، اظهارات مقام‌های سپاه درباره آسیب زدن به مقر ناوگان پنجم آمریکا در بحرین را تکذیب کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/75964" target="_blank">📅 05:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lY46ZlMMFF2UBEzEunfJMEcJ5O9QZpUl3_tWID7tVDKbFF4li8hFIT7z_osz_BwFZjFuxXAohZQKgZEhIEiidkmnqY7HNRXQwxdI2NBx4SGqkyP6_ZzxOCBDA8-Hw8qHWeUzQDen3YerZC3bL1jjE3aA83zMuUtUzr2iNMxvciifMxm9yWyqOesBbK2Gj0ZofRAOCOLdgaoyxbsb_OXGc9A4LK-hfImxn0xaB1sF0fDT17V4xZRNnQkkp6fRr94IvmbkFBt0j-VWxRZ7kCEeg6rW1j_vTZuhSiAQvse9lXzu71ohNnK3leukY4Z2ely6gqE8GtR2hLfcvGQLgLPBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LYw8uwtadG-GkXZx4CTn-tMaHcjE5KDlNofAvZ-OzxLdD1CJSlLJiNBL15zsLoa6IK1NpZu6YPZbDXSNHk8ITjwIOA6Snw1lfnFSYL4neC-vbMkS0OqFbTk88JOsg_oum-O1G6FjwvM2QhUmHtsupjjCb4ALzNeSEmIkdgwH2AHtYDQpr7EZdBCRf2hNW8ZOYo_VjExcmhAhu_TKygIMZcGqez20VVLj3j_vDXahKMen6XACiFoZQPl5xYtYKYnIqSvoIXOug374TrTIRd47yxC3XsAA5Mgx428SYeUFI-AGSVRZmO0TvrXhr3vHfz1H0gB9O1gOdwLPepNR1re2Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=eHpriyOduO6jhAf8M1h7TtObtI42TpoAuxgjCup-QKKDJS2bGzHgwS9eV51J7n7zLRwiqLbmhB6obg_fG9SZ0eLUyA3MyIi0y2I5ZgkobahcZHyqwy02ECSn96ImNqBmlH0iurmFV9Cz9nkduDFyk0a_Lb1TLvsY41dDALNDSQnDzTDEyZ1k5gzDYaE4WEDJ7O2dhaRwv15Bbl5SpW5VA9XyVWwnJZR-lMviM90UymB01aFP-oKwWF8I1A7M5aiYIS1TkNOa6S_aLzqtzFLVIhj63NAmi17N1sHYRJ17pc6Z2DRLMf5LoqTGBfy2MCFQAyBIOyF7wU4K4DPJvR0rWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=eHpriyOduO6jhAf8M1h7TtObtI42TpoAuxgjCup-QKKDJS2bGzHgwS9eV51J7n7zLRwiqLbmhB6obg_fG9SZ0eLUyA3MyIi0y2I5ZgkobahcZHyqwy02ECSn96ImNqBmlH0iurmFV9Cz9nkduDFyk0a_Lb1TLvsY41dDALNDSQnDzTDEyZ1k5gzDYaE4WEDJ7O2dhaRwv15Bbl5SpW5VA9XyVWwnJZR-lMviM90UymB01aFP-oKwWF8I1A7M5aiYIS1TkNOa6S_aLzqtzFLVIhj63NAmi17N1sHYRJ17pc6Z2DRLMf5LoqTGBfy2MCFQAyBIOyF7wU4K4DPJvR0rWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'رد موشک‌های شلیک شده از ایران'
تصاویر دریافتی از استان‌های فارس و بوشهر
آپدیت:
وزارت کشور بحرین نیز دقایقی قبل از به صدا در آمدن آژیر خطر خبر داد و از مردم خواست به اماکن امن بروند.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75961" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eaXt-7LtR7GNKbosrbak3sOVSJIYURTbEvL3SQ5Y87Z74-C1xbQiadFb9xZQ3t8bEdFZi52tQjIt9EG-d3rjOXR5p53K6nW5fidBWVxBKk7PIpWVSArrbt5VhvfO9_Qv4Z5OYAdvFzVqfJxKInxYxJXTpt6wgb-Z5Lsu2wADV5MZRjptyUvjG0F4wjpYJkzX6Nc5hRP0UJNBco6tOXtxWPnEO4HpA-LnOfOEzkCKtDTqQelhNuAKntw2IBu-kAEn31R9Ttle4_fHxYYAJMab90vuHscWaTeEkb1UrdeogD0sa1tWu0prYdm3bd5-bU9lRAkWMjZndC2iaHFCt5Ohvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک‌هایی دیگر از ایران همزمان با صدور هشدآری دیگر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75960" target="_blank">📅 04:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unHPzIb4f4IDBDY-OsAs81ZmApugSJvGGIidtl7x2Ttonx2zdIWfGbxlw84BnDzbFBBsz1TBdiahxT5RJDqAsTT3zNywPQw8kpQtX8ff9UO5DxVrjt4yc4KBJH4XW4Fi5h5pE0vry-MaiW3bsAVQq-JAdTNOXv_Bt_bKGCFd4Ud6jwLb8GdjmExe-2EGr4hxCCJwm35PbWmJcQQnzTCslCarq16Mq9cFrnXTBi_-fzwd2v6CfyZ6c_4DTRw0IpLvqcLA75dA4l81N0j5GAgnJHj7QIfnoGNTy07vyzVb5_Aq1Ibf5Rn27_YWVHOyMSQbdj20p2X1LGoispnFLQSa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: اعلام هشدار در کویت
آپدیت:
ارتش کویت دقایقی قبل از فعالیت پدافند هوایی کویت برای مقابله با «حملات موشکی و پهپادی خصمانه» خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75959" target="_blank">📅 04:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtTlN7mp5GDRj2siWHd4WxgpqgmTMABTMD-PGRsmFtRZmvbPAERkw4Ies36NJfA6BEcNM6Y8aBFMf8r4KrwsuivuMbw2aE_9TtyzpQNuQBvASou5s7JV4tqz7oVZMBJPEhyifofcGbYcksEr41scRoHtRuFR-K3IcKWZyVmb1-LkcEJoklgMSg3BpL808WhYWWGKcyDHXPXTLA4j4q5U7B8ac2NcNsoWdSjUOtdOHH5AMQxyYcFszGpnVchN3ecbtpUwhw6fLpTUFq69LOmvQLctodk16iLzhikV5RswB_KgPtqut7FcXdF--2Af9ChEL3wwURW88icKFKPi-nArzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ایالات متحده (سنتکام)، بامداد شنبه، ۱۶ خردادماه، با انتشار بیانیه‌ای رسمی اعلام کرد که نیروهای ارتش آمریکا چهار فروند پهپاد انتحاری (یک‌طرفه) ایران را که به سمت تنگه هرمز پرتاب شده و تهدیدی فوری برای تردد دریایی منطقه به شمار می‌رفتند، سرنگون کرده‌اند. بر اساس این بیانیه، نیروهای آمریکایی متعاقب و با هدف دفاع از خود در برابر حملات بیشتر، سایت‌های راداری نظارت ساحلی ایران را در منطقه «گروک» و «جزیره قشم» هدف حمله قرار دادند. سنتکام در پایان با تاکید بر حفظ آمادگی کامل نیروهای آمریکایی افزود که واشنگتن برای دفاع از خود و پاسخ به «تجاوزات توجیه‌ناپذیر ایران»، در حالت آماده‌باش قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75958" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سیریک در هرمزگان
پیام‌های دریافتی:
پایگاه نیروی دریایی سپاه بندر سیریک  رو همین الان دوباره زدند. همون
لوکیشن چند روز پیش.
شهرستان سیریک صدای لانچ موشک ساعت  ۲:۱۴
سلام ساعت دو ده دیقه
پنج تا انفجار نیرو دریای سپاه سیرک هرمزگان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75957" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFtnfNyW2a-lgStc3tnpVy18yRSb_p5XCSt_gJGg9JbuoOPDZ2peegJXcCNIv27szD-DCHXZilLEcuGAvAJVbvZPtq19NaWjssAAW1C8pvEeQDI5uqn5NAL9VnE-H43Hod1lRv5tjoJbfoOocE_dXbTOCNgoOzyarH_gqWokAhPATasVGYwuAK3IXrPnxSCOc_OjF5ygz1-Xc6N8xhDNHjU1mZSUCU6vIKUb5UrNOjobSNjmMLqSn-7pcGHQQSk59Dg31CEfC36h-oq5uYBga_LliLVweaedOthoAN4QtCPsMKIDSdq3tVe_KPbERJiXQsc6B4TSYzP50n0OENvkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وب‌سایت آکسیوس گزارش داده است که استیو ویتکاف و جرد کوشنر، فرستادگان دونالد ترامپ، روز پنجشنبه برای رایزنی با گروهی از کارشناسان فنی به آزمایشگاه ملی اوک‌ریج در ایالت تنسی سفر کردند.
به نوشته آکسیوس، کاخ سفید در تلاش است با ایران بر سر یک تفاهم‌نامه برای پایان دادن به جنگ و آغاز مذاکرات تفصیلی هسته‌ای «به توافق برسد» و می‌خواهد در صورت آغاز این مذاکرات، تیم کارشناسی لازم را آماده داشته باشد.
به گفته منابع آمریکایی و منطقه‌ای، تهران و واشنگتن همچنان بر سر برخی جزئیات این تفاهم‌نامه اختلاف دارند، اما مذاکرات وارد مراحل پایانی شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75956" target="_blank">📅 02:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxHYTc6Hglv4rBIRQHr6__17VPlONAGKxJ4K3KH0_kgX155H3blKzj92mF76jDEvKJ6g8hYkd1PSaWwlxlsLzqHSHecepwM1y9unJzfVtX76I0Xy4q0xuNs5VR3K2DoqPRatX797c8-2GqztDuK-JCqBr0VOI-2zA6usbpKgVDiPUnTuHi7Nuh-Rf-3UXXY1ZneDbv1l2IPUgt9rmM6twYKkOpO47PIFR-RrwlGrRbQMLhaGY7gYgil0UMKRXRXeZntJwZluZXqinREzRop3id_4GNmyU6iFhvUyUkvPYdHCoMNk4kK1Fml8pSF1s90rlnEMJgSO3k2hnMGZf8lLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام آمریکایی گزارش داد جمهوری اسلامی چندین پهپاد انتحاری را به سمت تنگه هرمز پرتاب کرد که هواپیماهای آمریکا دست‌کم چهار پهپاد را سرنگون کردند.
این مقام گفت مقام‌های آمریکایی گمان می‌کنند این پهپادها کشتی‌های تجاری در حال عبور از آب‌های منطقه یا نیروهای آمریکایی فعال در نزدیکی آن منطقه را هدف قرار داده بودند.
@
VahidOOnLine
ساعتی پیش‌تر اخباری درباره خارک و بندرعباس در بعضی منابع منتشر شده بود، خبرگزاری مهر میگه صحت ندارند:
جمعه شب خبرهایی مبنی بر شنیده شدن صدای انفجار و پدافند در جزیره خارگ منتشر شده است.
پیگیری های خبرنگار مهر مستقر در جزیره خارگ نشان می دهد، چنین خبری صحت ندارد.
بامداد شنبه برخی فعالین فضای مجازی مدعی وقوع درگیری‌ها و حملاتی به شهر بندرعباس شدند که بررسی‌های خبرنگار مهر نشان می‌دهد هیچ‌گونه درگیری در این شهر اتفاق نیفتاده است.
شلیک‌هایی در این منطقه صورت گرفته که جنبه اخطار داشته و کانون تحرکات در دریا و فراتر از جزیره لارک بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75955" target="_blank">📅 01:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=C3AbrbD2YYdSNPVYN5NyHSpuHHRGAekWv96mcajZFKfS-Cl-m0kK1a6y3F8ZD5MJZ6Ih_3JLo414GK9MPesEV5cO8F5zW4FcCqH8gzOZU9-uiFKuG_JEymNWAfiVM4lkkvsVOjWlmDQ6Z_8D4z1StQHRFX0zfavEPOg3RCSS2DU46fopHTw6bsJNTPhjusDyYuMgLXYXgCcrmjijeP7ZoDM-gs7KJWYI6R0rzqJvVxsqUc1KSBxEOOW4MTZMQu7ax_ThDJ6lBRR6zI6m8MYD2ufdde-z6xYeCcqfjK-D58Cjsz-0TUMHnR_cTssFDivl83fEWCeTvYPRGPltdiJtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=C3AbrbD2YYdSNPVYN5NyHSpuHHRGAekWv96mcajZFKfS-Cl-m0kK1a6y3F8ZD5MJZ6Ih_3JLo414GK9MPesEV5cO8F5zW4FcCqH8gzOZU9-uiFKuG_JEymNWAfiVM4lkkvsVOjWlmDQ6Z_8D4z1StQHRFX0zfavEPOg3RCSS2DU46fopHTw6bsJNTPhjusDyYuMgLXYXgCcrmjijeP7ZoDM-gs7KJWYI6R0rzqJvVxsqUc1KSBxEOOW4MTZMQu7ax_ThDJ6lBRR6zI6m8MYD2ufdde-z6xYeCcqfjK-D58Cjsz-0TUMHnR_cTssFDivl83fEWCeTvYPRGPltdiJtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش امشب برنامه «خیابان انقلاب» به خاطر این حرف‌ها لغو شد
beehnam
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75954" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7JPhUBFKtPh4gdG6FanDYDetBLHK-g-RrUvzvSLeTYPRTERUk2aqA1khYUMXdP3T8WFfG8s6h6koRftMewcY1NBJx-xhr5WzOYXWg3cgEqvuf_AROqhw0Xl0IVP7323J2PQC1A9-kYHGZqPe89d8JjXiCQ6gk9GuwwS5Zo3ULmMtluEVita0n6crgsW0mpcqnFf390_i7wfeinOASG0udRuMiciS4cPkRAXL70G5rKL7OaeLfBSOSzGEW5MQpJXN1jPe0fuqNROgXzBurDyCIqwroQg5whZ5_Rww7QSw8WuoIHiaFLk63glQzH19ue8Pp97Dgyhs5vAzbcNmSbFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام کاخ سفید روز جمعه به خبرگزاری رویترز گفت که بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده و شرکت در جام جهانی فوتبال ویزا دریافت کرده‌اند.
تیم ایران قرار است نخستین دیدار خود در جام جهانی را روز ۲۵ خرداد برابر نیوزیلند در لس‌آنجلس برگزار کند. این تیم سپس در همان شهر به مصاف بلژیک خواهد رفت. بازی سوم در سیاتل مقابل مصر انجام خواهد شد.
@
VahidHeadline
آپدیت:
فارس، خبرگزاری وابسته به سپاه گزارش داد که ویزای برخی «اعضای کادر فنی و اجرایی» تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن «خودداری» کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75953" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWh6OyloEqGNRW3TavwbwxOQPhuYkW-EhqMVLLui5eLcVebt16Yyx6tcBYp49CtL_C0Miem3hFlu3yEkEkDfV-5IEJdoOpd3lXTpW4OBSsycXkrsqKuMu0O6NTuj0zB-Xmpomv4DW208agEm23eFAOWFMd9TU2sMezxczQ-XpvPz8pcHKGlmZrb1Opl3Wb8JVrVxE9MMOSDNSTOdKK1eZrzljbKiP3S7ZFvvREW8nJciZuow26FzX__sA4OFbNsE_vJ6QoktUgCnZGBHWIR5RFkGxf-d_wFqVraBP38wAXQItCAd8c_vGdzlNncj0C6zDghpZHs_pnhhVMOSCYFuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسعود نبی‌دوست» خبرنگار خراسانی فعال در حوزه میراث فرهنگی با انتشار تصاویری خبر داد که کلیسای تاریخی انجیلی مشهد، از آثار ثبت‌شده در فهرست میراث ملی ایران، بامداد پنج‌شنبه ۱۴خردادماه۱۴۰۵ به‌طور کامل تخریب شده است.
رسانه‌های ایران از جمله «جماران» نوشته‌اند که تخریب این کلیسا «توسط عوامل ناشناس» و با استفاده از بولدوزر صورت گرفته است.
فعالان میراث فرهنگی می‌گویند این اقدام در سایه غفلت مسوولان میراث فرهنگی رخ داده، عملیاتی که حدود دو ساعت طول کشیده و صبح روز ۱۴خرداد نیز با بستن اطراف این کلیسا از ورود افراد و خبرنگاران جهت عکاسی ممانعت به عمل آمده است.
انگیزه، هویت افراد یا نهاد تخریب‌ کننده، مشخص نیست اما این نخستین بار نیست که یک بنای ثبت ملی شده تاریخی در ایران بدون اینکه نهادی مسوولیت آن را بپذیرد شبانه تخریب می‌شود.
کلیسای تاریخی انجیلی مربوط به دورهٔ پهلوی اول است و در خیابان جنت، کوچهٔ گلستان شهر مشهد واقع شده است. این اثر در تاریخ ۲۵ مرداد ۱۳۸۴ با شمارهٔ ثبت ۱۳۳۷۵ به‌عنوان یکی از آثار ملی ایران به ثبت رسیده‌ است.
پیش از این بارها بناهایی همچون کلیساها، آرامگاه‌ها و بناهای متعلق به اقلیت‌های مذهبی از جمله بهاییان، مسیحیان و یهودیان
تخریب‎ شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75952" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز ۵ ژوئن ۲۰۲۶
قاضی فدرال آمریکا امروز حکم داد که تمام سیاست‌های تعلیقی USCIS غیرقانونی هستند و باید فوراً لغو شوند!
leeleehozak
چه خبر خوشحال کننده‌ای برای دانشجوهای ایرانی آمریکا، امیدوارم بزودی روند بررسی پرونده‌های USCIS شروع بشه و استرس و نگرانی همه تموم بشه
21aban
بلاخرررررره خبری که ماه‌ها منتظرش بودیم، اعلام شد.
طبق حکم دادگاه فدرال، پاز برای همه‌ی‌ افراد در داخل خاک آمریکا برداشته شد، از این لحظه به بعد دیگه
#USCISpause
وجود خارجی نداره، چون این بخشنامه از نظر دادگاه غیرقانونیه.
درود بر استقلال قوه قضاییه که زد کل بخشنامه اداره مهاجرت رو لغو کرد.
درود بر دموکراسی که در اون قدرت، چک سفید امضایی دست دولت نیست.
پی‌نوشت: احتمالا دولت درخواست تجدیدنظر بده و اعتراض کنه به این حکم اما خب دیر یا زود پرونده با پیروزی ما بسته میشه.
BrmTheGreat
این
لینک اصلی و رسمی حکم دادگاه
ه
اینم
لینک جزئیات بیشتر این شکایت خاص
ولی از یه منبع غیر رسمی
mozfang
جزییات تکمیلی:
دادگاه تمامی استدلال‌های دولت را که سعی داشت سیاست‌های جدید USCIS را از شمول بررسی قضایی خارج کند، رد کرد و رأی داد که:
واژه‌ی «امنیت ملی» نمی‌تواند سیاست‌های مهاجرتی قوه مجریه را به‌طور کامل از نظارت و بررسی دادگاه‌ها مصون کند.
قاضی رأی داده که هر چهار سیاست جدید چالش‌برانگیز، ناقض قانون تشریفات اداری (APA) هستند و به دو دلیل عمده غیرقانونی اعلام می‌شوند:
۱. مغایرت با‌ قانون (Contrary to Law): اداره‌ی USCIS از حدود اختیارات قانونی خود فراتر رفته است. دادگاه اشاره کرد که اختیارات مربوط به محدودیت ورود (موضوع بند 212(f) قانون INA) منحصراً متعلق به رئیس‌جمهور و مربوط به مرزهاست، نه مربوط به فرآیند پردازش مزایای داخلی برای غیرشهروندانی که قبلاً وارد خاک ایالات متحده شده‌اند. علاوه‌بر این، سیاست اعمال «عوامل منفی بر اساس کشور مبدا»، به وضوح ناقض اصل منع تبعیض بر اساس ملیت در قانون مهاجرت (موضوع بخش 1152(a)(1)(A)) است.
۲. خودسرانه و دمدمی‌مزاجانه بودن (Arbitrary and Capricious): این آژانس نتوانسته است استدلال منطقی برای اقدامات خود ارائه کند، منافع و انتظارات به‌حق مهاجرانی را که طبق قانون عمل کرده بودند کاملاً نادیده گرفته، و به دلایل ساختگی و بهانه‌جویانه (Pretextual) متوسل شده است. دادگاه به یک «عدم تطابق جدی» میان اهداف اعلام‌شده امنیت ملی و آنچه در واقعیت رخ داده اشاره کرد؛ از جمله اظهارات بیگانه‌ستیزانه همزمان رئیس‌جمهور و کریستی نوم (Kristi Noem) وزیر وقت امنیت میهن در شبکه‌های اجتماعی، و همچنین استثنائات خودسرانه‌ای که آژانس برای ورزشکاران جام جهانی/المپیک و پزشکان در نظر گرفته بود.
🟣
دادگاه رسماً هر چهار سیاست را غیرقانونی اعلام کرد و آن‌ها را به‌طور کامل ابطال و ملغی اثر نمود. از آنجا که این حکم یک دستورالعمل دولتی را ابطال می‌کند، عملاً اثری سراسری و ملی در کل کشور خواهد داشت.
🟣
دادگاه درخواست شاکیان برای صدور دستور منع دائمی را رد کرد و استدلال نمود که حکم ابطال و اعلام غیرقانونی بودن سیاست‌ها به خودی خود برای جبران خسارت شاکیان کافی است و نیازی به این ابزار فوق‌العاده نیست.
🟣
درخواست دولت برای رد ادعاهای اساسی شاکیان (مبنی بر نقض متمم پنجم قانون اساسی در خصوص رفتار برابر و رویه عادلانه) رد شد. دادگاه بر اساس اصل «اجتناب از ورود به مسائل قانون اساسی در صورت امکان»، اعلام کرد که چون پرونده بر اساس دلایل اداری (قانون APA) به‌طور کامل حل شده، نیازی به صدور رای در خصوص بندهای قانون اساسی در حال حاضر نیست.
این حکم به امضای قاضی ارشد، جان جی. مک‌کانل، رسیده و لازم‌الاجرا است.
منبع‌:
کانال مهاجرت به آمریکا
BrmTheGreat
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75951" target="_blank">📅 19:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d2hg9eGRuu60azxr-LQiRC2T9qP6EGkMjDVjVL6VUvMX1sEeDyYUbavbAWYyA51ijzSbOIL5EqC_v6IiAnd6BZOPL4FpSapLg6m-oaWQW_TVZ5z7y6GUUBgTLO14SawLMXXczY4N7zUIod_8CyGe8ow7f7vC1Fvt24cUpUNF85h5zIXpwQNrMXucmJcN05f7UN0a7RpLuSiGu7yntf3e6sxmVyS2SogJ6dmdcCfXvaYYtuKkgH69Y1ROrqxTgexn2SwkGpevkRM7gNrpNenX00Rb8HgP2TXsX7iSnrZcjWGyL9OcOELSBW6-DRe0jWRsef4dYHcqFuDRnktKIWy64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LiRTgtI6mGG-sgpnAaG_4Qx_jcL2-JQWHiX_fHvw0tBXI1_QbH71FviKiKSrGaxJiqEJv806h0Be8shkIm0RQNNxlgBLqaiHgNzdEt72EljSz5zvSbiYGeCM7yRjYT7GmCrLzYhZgQNkZGDLlovtaZHEw-IYRMQfWKRRi6sSEKP8LRRtOnvQONeR1zz1_UHSVNwMCFSSThYXvDtqYzme43cJbcjIKm4MsRAvT6BBYc5uVgG35Oqs2QfyILCbRJE73Xjr1uHVMmR-6KfsFD8uic6iipOCPaL1V-YgbdpdOUhWz6--N-rgNGfEsQl7KqNOQC1L-1p8S7TK8_QQgUpaUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه خبری الحدث، روز جمعه ۱۵ خرداد ماه به نقل از «منابعی آگاه» گزارش کرد تهران موافقتش با انتقال بخشی از ذخایر اورانیوم خود به یک کشور ثالث را به اسلام‌آباد اعلام کرده است.
بر اساس این گزارش، اصلی‌ترین اختلاف باقی‌مانده در مذاکرات میان تهران و واشنگتن به موضوع آزادسازی دارایی‌های بلوکه‌شده ایران مربوط می‌شود و نحوه و سازوکار آزادسازی این اموال همچنان یکی از شکاف‌های مهم میان طرفین به شمار می‌رود.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران،‌ روز جمعه ۱۵ خرداد ماه به نقل از «یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران»، گزارش شبکه العربیه درباره موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده به کشور ثالث را تکذیب کرد.
خبرگزاری فارس به نقل از این منبع گزارش داد ادعای مطرح‌شده از سوی العربیه «نادرست» است و موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد.
به گفته این منبع آگاه، موضوعات مرتبط با پرونده هسته‌ای در مرحله کنونی گفتگوها مطرح نیست و بررسی آنها به مراحل بعدی مذاکرات موکول شده است: «ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و درباره برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
شبکه العربیه پیش‌تر گزارش کرده بود تهران موافقتش با انتقال بخشی از ذخایر اورانیوم غنی‌شده به یک کشور ثالث را به اسلام‌آباد اعلام کرده است و این کشور ثالث با توافق طرف‌های مذاکره‌کننده انتخاب خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75949" target="_blank">📅 18:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGcPZ4t-mDMqFCiP0WymYhQRdWbZzOJw-uq3SWyFqlOSG0iuQAwfuTSW5iFYnNXyzCRlXqdWMh4wUn-NI8q63AShs7GL5H3VJ8ZDC_WEqbSLCq1j9XT7OUSPkyw1nwmUhA-80W98BRT5tRFnaJidVbm7TPquI0CtlEBcBt8aTiAecJ0SU3gIuCc7dat1TSGAO4s6zT3QdO-Nu8eDRaVQ-6CtDSwh257vGZ-uVjD5haKCBWr92fNbxBC2LlsjShiKQyq6_LlLdsjl78sj5HS7ZUIZirk9cMrDaHKl-j97ekqswchRWvPGnCvfd2j_3RgF7OgwIhbBV63pFxL9hlNRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوزف عون، رئیس‌جمهور لبنان، در مصاحبه‌ای که روز جمعه منتشر شد، از ایران خواست در امور لبنان دخالت نکند. او همچنین به گروه حزب‌الله، متحد مورد حمایت تهران، گفت که تنها راه‌حل درگیری با اسرائیل، دیپلماسی است.
او در این گفت‌وگو با شبکه خبری سی‌ان‌ان خطاب به ایران گفت: «این کشور شما نیست، کشورِ ماست... دخالت در کشور ما وظیفه شما نیست.»
آقای عون افزود: «آنها از لبنان به‌عنوان یک اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کنند. این غیرقابل قبول است.»
رئیس‌جمهور لبنان همچنین گفت: «حزب‌الله باید درک کند که هیچ راهی جز نشستن و گفت‌وگو وجود ندارد؛ هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده است، جز از طریق مذاکره و دیپلماسی وجود ندارد.»
حزب‌الله از سوی آمریکا به عنوان سازمان تروریستی شناخته می‌شود اما اتحادیه اروپا تنها شاخه نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75948" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y1w1Gf3w738MlnliqsI8Jx3nYg0rxwkQV3y54mBpGGI2CloPRs6I7p4gX_ZffwkfBbfWASxUrGfqBfwHvPDAloETrnmHW2G_siueC9jMJgw4_QudE4ySm6CSijWZmScv7ArwqER8UYSbW3-2RNPz5zCWTQI53fLovTlumcUI13nEXWIbymk5Va-2dyE5gFos331WAsam2vU6bIHTXQ1IZbO-LuxCLPKzTksBHdMXNiGqLQiDVBbsz2x6Cbt9Wva7mH5eLIed9Hwga9EzJfXOXIFx2li_LIG4UUC7nSxnGqKErnquCqrnFRiHXfsfkFOwRk4YVI7EQSmfpH1CqkMqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=GPkEC8hSFnNxUfp3ptN-fsDrF2u3laEdM1-Z8DfOFLzG_GrSx7gHKDx86Rcf2u1_LuXYL8vjssM6lfv1LdF-ZNmFINxG0LXUtF_NYvM3xcv3SwOjr1AGSx29R3j3DIKKcSAruUgv-zBbjAFgVl6r1oyyFqIOgs707aYo5CwHOXsu0o8CKv1x0bpCRxIGoDEk2RxS2lKAwkOX5KVTbYvTv3hGV04KZdd6VLSrp6ZEuUdzY2GcyepmbBIGibtGticzbezMcnw9K-GPxp_z7mf-ahiYajPZurqngAfnrgl4-R1Kmp9Hg1EPg_fwNhHNcLKQvrv2UtmWKww7Y--tDcmSRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=GPkEC8hSFnNxUfp3ptN-fsDrF2u3laEdM1-Z8DfOFLzG_GrSx7gHKDx86Rcf2u1_LuXYL8vjssM6lfv1LdF-ZNmFINxG0LXUtF_NYvM3xcv3SwOjr1AGSx29R3j3DIKKcSAruUgv-zBbjAFgVl6r1oyyFqIOgs707aYo5CwHOXsu0o8CKv1x0bpCRxIGoDEk2RxS2lKAwkOX5KVTbYvTv3hGV04KZdd6VLSrp6ZEuUdzY2GcyepmbBIGibtGticzbezMcnw9K-GPxp_z7mf-ahiYajPZurqngAfnrgl4-R1Kmp9Hg1EPg_fwNhHNcLKQvrv2UtmWKww7Y--tDcmSRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده، سنتکام، ادعای ارتش جمهوری اسلامی درباره شلیک موشک و پهپاد به سمت ناوشکن‌های آمریکایی در دریای عمان را تکذیب کرد.
رسانه‌های ایران روز جمعه به نقل از ارتش اعلام کردند که نیروی دریایی آن به عنوان «اخطار» به سمت دو ناوشکن آمریکایی «موشک قدیر و پهپادهای تهاجمی جدید» شلیک کرده و این دو ناوشکن دریای عمان را به سمت اقیانوس هند ترک کردند.
سنتکام که فرماندهی نیروهای نظامی آمریکا در خاورمیانه را برعهده دارد، ساعتی بعد در شبکه ایکس اعلام کرد: «نیروهای ایرانی به ناوهای جنگی نیروی دریایی آمریکا حمله نکرده‌اند و به سوی آنها آتش نگشوده‌اند. انجام چنین اقدامی نقض آشکار و فاحش آتش‌بس محسوب می‌شد.
در این اطلاعیه بر ادامه محاصره دریایی ایران که از اواخر فرودین آغاز شد، تأکید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75946" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGYLNM_sGUD7PRljNfaZQcTqVAz7WzUMiQIAFjKjQfBSuUtHoHP0TuQNS9J2iGntBfTQnAUhpTqqzJjFBXHSoaXQmkQhIaJEjL7ZmfRftqMWo_a4JrBGbQ-NSqhJtMwq0kbCPlnRV7LyszKo9OLEymlPs7hnyuhHAyGJJwnapxkaOfET3xaJx6-GzPj7uWZlRoUTnwzDM_lzWY0MI9_vn59HvidrahHBj7mJDaueD1GRpuX5PKdC_84Du0-9Ge9Ln75RFsUCBK2DfyNnhwqoe8x2A2em_ZmgCywMtwMKTUcn3vgFKFrTuQMh5jRxEWLITbYdPxoTUmoPBaLaaGNwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کمالی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه ۲۶ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌است.
رسانه‌ حقوق بشری هرانابا اعلام محکومیت علی کمالی به اعدام، نوشت این حکم در حال حاضر در دیوان عالی کشور تحت بررسی قرار دارد.
به‌گفته هرانا شعبه ۲۶ به ریاست ایمان افشاری در اواسط اردیبهشت سال جاری حکم را صادر کرد. کمالی که دارای اقامت مالزی است، ۲۲ دی‌ماه ۱۴۰۴ در تهران بازداشت
شد و اکنون در زندان تهران بزرگ نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75945" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PfkoAE0Ke0XSTfetM8vr8lV0hJlnEXhQ7Um2JGWWGk16Jhg2ERUIgoeuGFnXdmkl3qfe-mzX4H2v6u4h_GXhDkr8GmnhM4kQVevzzvEiSEgVCKaoB2MjVQXUeUgppuMw0k3-NrX4r5irWcn7lBK-nye-SYV3LdbonPe3hNKudP5t_aofVozlRObI_LdeihD-OC1HmWBdol1vcv917WYMl2RKkLATzquvxuzL8s_1JnUvxkqE-NJzZA9HBnW0GOs9Lcl1Jg5X7YvEbKgUPqtPB9JGGc7U3wDbMKiwIbhMjHra58rkijmz0b1CGxGpWVeRWthDGwYVSguhqZNAkpm7eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع در روز جمعه گزارش داد که پایانه نفتی مینا الفحل در عمان پس از وقوع یک انفجار در نزدیکی اسکله‌ها، عملیات بارگیری نفت را متوقف کرده است. به گفته این منابع، انفجار ظاهراً در پی یک حمله پهپادی رخ داده است.
@
VahidHeadline
AJENews
هنوز مشخص نیست این حمله دقیقا چه زمانی روی داده است.
بر اساس داده‌های کشتیرانی ال‌اس‌ای‌جی، روز جمعه چند نفتکش بسیار بزرگ در نزدیکی این بندر لنگر انداخته بودند.
رویترز در ادامه
نوشته
:‌ رسانه‌های دولتی ایران روز چهارشنبه گزارش دادند جمهوری اسلامی یک کشتی نظامی آمریکا را که «مرکز کنترل و فرماندهی» توصیف شده بود، هنگام نزدیک شدن به آب‌های سرزمینی ایران در دریای عمان هدف قرار داده است، اما ستاد فرماندهی مرکزی آمریکا، سنتکام، این گزارش‌ها را رد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/75944" target="_blank">📅 06:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HCwVwZoDYijGIfPPn_mcBN0eUBgYMl5Tk_q1xikHcR7c4-EG933fcAo53YIOC9BX9lUm2cywsKbOnsZ2-0scdF9Flr_psjmcY0ASIba5S_wayM-nyZjcjSLQYxQifJidwnjyXtOvNG3Pgo2DB-ouVHYGj7itQ2NlQJpJcC770yW0HByVWCql4QItlktXcPbjlGqwtiYoz3Re2k1igZFuOS4Z0NfPnPVxnndCJEnQ1wG9dze9FPQX-bm824qI7ssx49HLBHidlpfE3ilXSKV_n-wOY_5RA7ExBRUb-k_Vd4f87YbRmq4Lv3arLEOLnlVnH2XlwpcDPmTdlG5E-hlD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ایران نباید سلاح اتمی داشته باشد
دونالد ترامپ، رییس‌جمهوری آمریکا، در کاخ سفید در پاسخ به این که اگر حکومت ایران نیروهای آمریکایی را بکشد، آیا جنگ با جمهوری اسلامی را از سر خواهد گرفت، گفت: «این دلیل خوبی برای چنین کاری خواهد بود. اگر آن‌ها نیروهای آمریکایی را بکشند، فکر می‌کنم خیلی سریع دست به این کار بزنم.»
ترامپ درباره جمهوری اسلامی تاکید کرد: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا گفت: «ما برای به‌دست آوردن اورانیوم غنی‌شده آن‌ها به توافقی با ایران نیاز نداریم.»
او درباره کمک ناتو به بازگشایی تنگه هرمز نیز گفت: «ما به آن‌ها فرصت دادیم که کمک کنند، اما نخواستند کمک کنند. این موضوع برای آن‌ها بسیار پرهزینه خواهد شد، چون نباید چنین کاری می‌کردند. باید کمک می‌کردند.»
🔻
ترامپ درباره جنگ: چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد
دونالد ترامپ، رییس‌جمهوری آمریکا درباره جنگ ایران گفت: «چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد. بخش اصلی این است که تنگه فورا باز خواهد شد.»
ترامپ افزود: «آن‌ها (جمهوری اسلامی) هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند. ما آن‌ها را نابود کرده‌ایم.»
او ادامه داد: «رهبری‌شان را از بین برده‌ایم و تقریبا همه آن‌ها را نابود کرده‌ایم. بعد در رسانه‌های جعلی می‌خوانید که آن‌ها در جنگ خیلی خوب عمل می‌کنند. واقعا باورنکردنی است. ما هر چیزی را که می‌شد نابود کرد، از بین بردیم.»
🔻
ترامپ: حکومت ایران درباره توان و اراده آمریکا دچار اشتباه محاسباتی شده است
دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست کابینه در کاخ سفید با اشاره به مذاکرات جاری و وضعیت تنگه هرمز گفت یکی از محورهای اصلی توافق، بازگشایی فوری تنگه هرمز برای عبور و مرور کشتی‌ها است و تأکید کرد آمریکا «هم در میدان نبرد و هم در عرصه دیپلماسی» پیروز خواهد شد.
رئیس‌جمهوری آمریکا مدعی شد توان نظامی جمهوری اسلامی به‌شدت تضعیف شده و گفت: «آن‌ها دیگر نیروی دریایی و نیروی هوایی مؤثری ندارند. ما تقریباً همه توان نظامی و ساختار رهبری آن‌ها را نابود کرده‌ایم.»
او در پاسخ به پرسشی درباره احتمال ازسرگیری جنگ در صورت کشته شدن نیروهای آمریکایی توسط حکومت ایران گفت چنین اقدامی می‌تواند دلیل کافی برای اقدام نظامی جدید باشد و در آن صورت آمریکا «بسیار سریع» واکنش نشان خواهد داد.
ترامپ همچنین درباره ذخایر اورانیوم غنی‌شده ایران گفت آمریکا در مقطعی گزینه خارج کردن این مواد را بررسی کرده بود، اما به دلیل نیاز به حضور طولانی‌تر نیروهای آمریکایی از این طرح صرف‌نظر شد. به گفته او، واشینگتن همچنان توانایی دسترسی به این مواد را دارد.
وی افزود آمریکا با استفاده از سامانه‌های پیشرفته نظارتی و امکانات فضایی، تمامی مناطق مورد نظر را به‌طور کامل زیر نظر دارد و هرگونه تحرک را رصد می‌کند.
ترامپ درباره احتمال دیدار با مجتبی خامنه‌ای نیز گفت شخصاً تمایلی ندارد و چنین پیشنهادی را هم مطرح نکرده است، اما اگر چنین دیداری انجام شود، با احترام برخورد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/75943" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MUTK8tL0ydYq22Ct-ZYkMAksCOmv9g63ebRtu4zrqZJno1JqsQbodUEAmyFbEbsD1_8FxyYvlK__AX9AHPLzrI_BCugr5FIAQWQtfzwWhJg1XhiGAKHcyycxdt3h4VzXUox2tCqjNiyOvZc-mMmLiP79aZ1JANSiu_WIpRykfaup0PhbS_JuEHb5QkcGvaTxvY9LGkWVS6sjnb61LJnx32kKyY8zgZn-UNK6YFvtO9FjaqLCSYKUe1q6R83M8SrFeWiRa56Wbc-fX_5S0uq_QCgacBfhA6m7lZrX99aEin3IledsRoD4hv_WRKKqMBxpCt1fg8xbAUxbegvsr1TRGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه پنجشنبه شب ۱۴ خردادماه، به نقل از منابع اختصاصی گزارش داد محسن نقوی، وزیر کشور پاکستان، برای پیشبرد مذاکرات میان جمهوری اسلامی ایران و آمریکا به تهران سفر می‌کند.
به گفته این منابع، سفر نقوی در چارچوب تلاش‌های میانجی‌گرانه اسلام‌آباد میان تهران و واشنگتن انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75942" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/osQmCYCJYKX4PVGaKohMUSvUnGIGMxfwOln5GS-J-sL96pvKAlrLTg7PYm3SrO0QZlBUX20U2SQM6-2cJf4Z-FEi7yChP3TerTlpyb5agjHI8EnRMdkjX6dnvP34AZH0dfWrsGMF73ISWSiOeKzppM_YaNsnn46ZZzcYU1cEoZ_Tq9avU1M9E-ZrodTmDoeht7kD5xYjOmIyubp2u4_AL5iuIhGwwkdJ-TllLC6EP2HQJmx_bGF2gw88d3Fq4nL7XqGL7B3BM6zNPVJMHI_Jki-7qug9f62f4T4rBpA047rGZVeQozr5WyhGZbialxu8DkwErfnvG5tfE2yGc1sP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت ایالات متحده بر جمهوری اسلامی غلبه می‌کند، یا با توافق یا با عملیات نظامی.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75941" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X25ns2zW88CHRAgqqqVyrXTERIK1L5n4C8olNx9EBKZrYyYhr6RRKACeGP6EP8hWIUTY3dPvtXRsvX8BldnxwJWeQUgsbYFzyYLo51YzsuRkYoQiG0tU590Jo-G8FtYd5ABgWZuGBNwqZpDUztS-sjEVRJjqYjf0hWRKk-V1UE6q4hPqnzqCg4qj5q-hwbfBUlNW6v3JTnKdyDRF5ErPtHtPehZrDmomkrfLFlzGQO9wXFpzVMClFR-AHGl0-OIdxW4PWQhfpd3pWnLADclJgNoWd63YSaKfvXyM-Dq9naiZn1O-0ZkW5SMAGlzUEx9aFcB8VLMDdNKEhK1jCjCFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پنج‌شنبه ۱۴خرداد۱۴۰۵ در گزارشی به کشورهای عضو، بار دیگر از جمهوری اسلامی خواست «به‌طور فوری» درباره سرنوشت ذخایر اورانیوم غنی‌شده خود پس از حملات سال گذشته آمریکا و اسراییل به تاسیسات هسته‌ای این کشور توضیح دهد.
در این گزارش همچنین از مقامات جمهوری اسلامی خواسته شده تا زمینه ازسرگیری کامل بازرسی‌ها را فراهم کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/75940" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/siRVVnpSKghXkF0vMac81QjhgEZDTt0UupMphk1kzctvYH_rq4NblFNKUuN__xGEMMhoeo8fChYo1oDKP3-1ZQ1jXA1xqcl28zd1N7nU4TbuztZld9RFjnyziS9pi3GPKmByBStjul5DR9x8cL2MCFr4g4VPaaMl_HPhXPkXc8xpG1uwNmZSnwtZvnp8cRbJ7ypn1riu1J7q7IOEIV6NdCRqeH3MoF-J_JJnbCy_dpfpQXXLnVkUaCpQSY7lYUFU_sxnTBTMCwGgKxFuKhUL8wZ5TKeeJcfi14tkk3XTDDoSle1J7UJEmQgk74cz6UjCVz0UyZm6yO3C0Af2wkuzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل گروه حزب‌الله طرح آتش‌بسی را که دولت‌های لبنان و اسرائیل در مذاکراتی با میانجی‌گری آمریکا بر سر آن توافق کرده بودند، رد کرد.
ایالات متحده روز چهارشنبه اعلام کرده بود که لبنان و اسرائیل بر سر اجرای یک آتش‌بس به توافق رسیده‌اند؛ توافقی که مشروط به توقف حملات حزب‌الله و خروج نیروهای این گروه از مناطق مرزی جنوب لبنان است.
@
VahidHeadline
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIeORpctnZPXqSr7XkuhxpUgj8XWTffvZfIfUJ2LWKU5EOYGLEcWIvvaplA2hOTnNUfv543aM0Y-sNQB-0GNeSX1Kt5l-jCvG2RjNVUWBKSuvppo3cns3AcoPiTedTikUCqdVP_PoAIV0AuPZTa5gJoMbiK_iYd6_7Lo0B4SbgMPAzPvf6riou0xg8W7uFaFlRds24oeVLXHniG1r0_MdQBY9-2OTKJCta7AtI5eGC9AXcxM8Hz_9CLm0Dr08xmi84WkQLT-E4wfjp5wcQZkv4mSYqVcqbUEWfkYakFQo_55UwutFasohrVYYOEOjHkvOpbufcDulXasIFRxrzCp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران روز پنجشنبه ۱۴ خردادماه و ساعاتی پس از انتشار ویدیوها و تصاویری از برخورد پهپاد سپاه به فرودگاه بین‌المللی کویت، به نقل از یک منبع نظامی، آن‌ها را «تصویرسازی دروغین دشمن» خواند.
این منبع نظامی به تسنیم گفت:‌«پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.»
سپاه پاسداران پیش از انتشار تصاویر برخورد پهپاد با پایانه مسافربری شماره ۱ فرودگاه کویت ادعا کرده بود که موشک‌های سامانه ضدهوایی آمریکا به این محل برخورد کرده بودند.
این منبع نظامی که نامش فاش نشده به تسنیم گفت:‌ «فاصله «هدف» پهپادهای هوافضای سپاه تا فرودگاه کویت بیش از ۴۰ کیلومتر است و این نیز نشان می‌دهد که اصابت به فرودگاه کویت ارتباطی به پهپادهای ایران ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75938" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZiTWPL8nIERSpfqRNyUJBpBS4hav58xBSdZ7hrwSFjYmwVhh0VzUd28Oib1TohxQRflTHK3SeuIYTmexmzl-6S8e0h5BO7sPnsWkZZa3UW6Z-6Ke7z6wBcuTH7yCD9DhbHCVBxrnH9_HZA-tYaPLh1P-hyXtymANxlqUlfexD9ai08ABRLPqVaq7D2LZS6kvCz45u2KvmQ3U8xrvfcnI2chpO_5lLDvsQahEIZKty_cYVGpgdZnvDfytv_zowq0jbCUN7k-4BWpnoiHI3VbbGcFlUhb9cxRSM6uwuBzHDMcHv3Jy-U7KLu8lnwCTWsTNSjHAjulPEerqbGnpxpQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام مکتوب و منسوب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در مراسم سالگرد مرگ روح‌الله خمینی در تهران، خوانده شد.
در این پیام که محمدجواد حاج‌علی‌اکبری، امام جمعه تهران، روز پنجشنبه ۱۴خرداد خواند، رهبر جمهوری اسلامی‌ آمریکا و اسرائیل را به «جنگ ترکیبی» با ایران متهم کرد و گفت این جنگ «بر دو نقطه متمرکز است؛ یکی تاب‌آوری مردم و دیگری ایجاد اخلال در دستگاه محاسباتی مسئولان کشور».
مجتبی خامنه‌ای همچنین هرگونه اقدامی که به‌گفتهٔ او «موجب بدبینی و سرخوردگی» شود را «کمک به دشمن» خواند و خواستار «حفظ وحدت و انسجام و اعتماد متقابل» مردم و مسئولان نظام شد.
مجتبی خامنه‌ای هفتهٔ گذشته نیز به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داده بود که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
در بخش دیگری از این پیام، اسرائیل «پادگانی متعلق به نظام سلطه» توصیف شده و تاکید شده است این کشور از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.
این پیام همچنین اعلام کرده است: «دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است» و افزوده است دشمن پس از آنچه «تحقیری پرمعنا و عمیق» خوانده شده، تمرکز خود را بر تضعیف تاب‌آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولان قرار داده است.
در پایان، در این پیام از همگان خواسته شده است با ایستادگی، روشن‌بینی، حفظ وحدت و انسجام و همصدایی نکردن با دشمن، «نقشه شوم» او را خنثی کنند.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
مراسم سالگرد مرگ روح‌الله خمینی که هر سال ۱۴ خرداد با سخنرانی رهبر جمهوری اسلامی و با حضور پرشمار مقامات و فرماندهان ارشد نظامی برگزار می‌شد، امسال به‌صورت خیلی محدود و بدون حضور مقامات نظام برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75937" target="_blank">📅 16:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGQXTQ5SNSUK7GdxoeOemgKEtSBFvN8yZRoCJQr7dyhDXoWcPPv8zpHhuwfZZMl6_pPJRQIh7TuMq8OnoFB87xUlrNu4gEVvEBIB5M2zvhblJr42zEpreKWHyPBczX-eeYwrqx3cTF10sCR3ETwxVMVQ9hXTbtFT2Diz-7TTFdQPWpn5LfjzMKLJlWDBxlFuZraMrY4Vtz7MrcY5V4-Vx2GEuz4lrwDSvhwhvTLvZ29H7xYBKPXsXiiN_6NpRx7p39aaD5hFMFQQplSAMxlLeCC-39WKSVU6xlvBlj_7efJ4MrnKU-WahG9sUHYB8Flf5sGYJzQanpaLcBXely_FJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس جمهوری آمریکای روز پنجشنبه ۱۴ خردادماه از تصویب قطعنامه «پایان جنگ ترامپ با ایران» به‌شدت انتقاد کرد.
رئیس جمهوری آمریکا در این پیام نوشت:‌ «دیروز، در یک رای‌گیری بی‌معنی، مجلس نمایندگان، چهار جمهوریخواه بد و تمام دموکرات‌ها، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران، به محدود کردن اختیارات جنگی من رای دادند. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آنها می‌دانند مذاکرات در چه مرحله‌ای است.»
ترامپ با انتقاد تند از نمایندگان حامی این طرح نوشت: «دموکرات‌ها از سندرم اختلال روانی [بیماری مخالفت] ترامپ تغذیه می‌شوند. آنها ترجیح می‌دهند کشورمان شکست بخورد تا اینکه به من یک پیروزی دیگر، از پیروزی‌های بسیار، بدهند. چهار نماینده جمهوریخواه، داستان آن‌ها کاملا متفاوت است. آن‌ها خودنما هستند! آن‌ها باید از خودشان خجالت بکشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75936" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AHg_6Bfd_6nyXtyW7mfAkFYssAYwhHX-dm6699zj1gQMsTCTnnQd_LABGFDLhdQvOOqprWHD446PbhJ0aRhQb-gG8xfHQsqKRdPpUX3EpAgR_EFU6rZAK0wDsiUSl8vCmTFRbqnea1g6eel0ahuwUHpIif-vQxpHKA-TaSLtfxUqs57ryv9EKc3CDkw4NTS4DyyeC3ZU3KzN6NzBF-tJZKIOtyT3kCt_rlPwIHt4ZqnCT_Z9lZnSZicAvL55ZnF4RWDX8fe8y_mrJEZQC2_oaUfd-IUIGBwMD9LkjrculjMBj8OJ8u1sSM6BKBIM_wjO1jtJnP6UTXTDaNefSw4Dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی، نویسنده، تصویرگر و فیلمساز ایرانی-فرانسوی و خالق کتاب مصور «پرسپولیس»، در ۵۶ سالگی درگذشت.
به گزارش خبرگزاری فرانسه، نزدیکان ساتراپی اعلام کردند او «کمی بیش از یک سال پس از درگذشت ماتیاس ریپا، همسرش و عشق زندگی‌اش، از غم درگذشت.»
ساتراپی سال گذشته نشان لژیون دونور دولت فرانسه را در اعتراض به ریاکاری دولت فرانسه در قبال مردم ایران و جمهوری اسلامی رد کرد.
مرجان ساتراپی با انتشار «پرسپولیس»، کتابی مصور درباره زندگی خود در ایران و مهاجرت، به شهرت جهانی رسید. این اثر با استقبال گسترده مخاطبان روبه‌رو شد و به یکی از آثار شاخص ادبیات مصور معاصر تبدیل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75935" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca-o7FonTsfzprlwr91SwY_sLpUrbB8OgbIYPV7XN3J03MbuYQiRXO3IC9mE7x_2rIIfmvwHTdQLzGa2mUjFTt8g77wrPxG0ilv4ubhk77ZocFCHtjY7roqt9q6cklVOepDfRBRksxORgqEH-LYPHfaj-JwkjmHZ0Idn-NhPR9uj7UWMP1op-Rr_GXEYZxej-apPZ2pKF-NMX2doGVQIneN8isKhHYxCYLMxvMUaIluOzWCEEgXlOWCTxXCo3DkZMez68B4QhKqgsWmWUY0G6cOjdWXYkw-anTKxe0NGRE1bgaZizBaPHkV3kqwCKAWkJi2-TBPEM8N7M4ysGUvrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هه‌نگاو و سازمان کوییرهای ایرانی سیمرغ با انتشار اطلاعیه‌هایی خبر کشته‌شدن مهشید فلاحی، زن ترنس، در سنندج را تکذیب کردند.
این سازمان‌ها ضمن عذرخواهی درباره انتشار این خبر نادرست، با وجود راستی‌آزمایی‌های قبلی، گفتند اسناد جدید نشان می‌دهد این شهروند زنده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75934" target="_blank">📅 16:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ark2Wc_U4LeXouTQuZfJ3VC-qU6k6GTYQj362HYjk48A_hB81ZUSijTwoIa1hoQtqlF9DBVw5QFC5VeTZbTDdZlF1Nz-aOHA42Fb2vX4GPz-0e04OV0PLIAZqAGNl-7UGbmte2oWOIL1TQ58MTI9Bd0En9GlmR96315n6t5OI5Qj_VMWgTH1rMNAmPWEeP7wc8a7o4Jh4PaQgiVM7RqMo3axzYeVE7h6uyKhavlX8otpJpxta0YHhw2l2sQ6iTnhQDziKO1VTPdoiZbiQ8hAhC9Kg4ee-Wj_-pVLvNJmmUX5ZnVAZHYdWD5lRpqzsyMdOZo0rNNargQwZwpu1sz9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/75933" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rvJJKQ_E5PL_vADDThMUf40iSvV5DeWmm21rEnxVP6sfw8QzhVLRq_Cy13fUDGHK8pmgIg4N8eZWqofMg9ZCthWPvBh_n8Bjx_kzEKmj3-8-v85Bd3f1SogTBDK_foFCphgLAmsYdqW7jMfP-uDJB4dPxLfTCVMj9QLpWJRO-TrAUl2yyHTY6o94eMANpQeXAS8VsEDVy1ehelW90oRSRG0bT3Yc1icEbCmmkJWFyNMgXJlD6EE2LUA39llfsB-XgyCywBizipgLHiIiHafWGPY3qPMic8-k-laROKjD1A40nXgsJK8nTC6HPLZWX7KD8v5oEIIkr55IJ1oWkwK7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد اسرائیل و لبنان بر سر اجرای یک آتش‌بس به توافق رسیده‌اند.
بر اساس بیانیه منتشر شده، اجرای این توافق «منوط به توقف کامل» حملات حزب‌الله و همچنین تحقق چند شرط دیگر است.
این توافق پس از آن اعلام شد که حملات اسرائیل به جنوب لبنان در روز چهارشنبه دست کم ۹ کشته بر جای گذاشت و حزب‌الله نیز راکت هایی را به سوی شمال اسرائیل شلیک کرد.
در بیانیه چهارشنبه شب وزارت خارجه آمریکا آمده است: «همه طرف‌ها بار دیگر تاکید کردند که آینده روابط میان اسرائیل و لبنان باید توسط دو دولت مستقل و حاکم تعیین شود. آنها هرگونه تلاش از سوی دولت‌ها یا بازیگران غیردولتی برای گروگان گرفتن آینده لبنان را رد کردند.»
حزب‌الله تاکنون به صورت رسمی درباره این توافق اظهار نظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75932" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=ali_1F1YC-rL9JcJuib6Ymwtm40f6PI_IBkQWz_XF6CihrJjFgarrEBI9iWspOrwa7TWDoZ1p6yr4FmcmNEFYLcBznwjETEuvccP_Llaz0R73kp3CKWjuv9oC7DPxrVdKILUuSVKoxA44Vpz9HQekHJjhY4lYxSOwbNdiaHwt5hvzcYL3eSOrM-s-CuwO2z8Qsg0X4BaLY4ykB5xfc8OvW5Dk2pwo37InBR0fLbd5-IS7VPdjAKabAGXR9w29s1uztuyEGeI11H1CoI1nFbhuf0BzeIu-S0dNqnMixEQ1Mn4HUAPySkfKV4rTpaP-i71noAhe60XpyzEKyDwaAoI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=ali_1F1YC-rL9JcJuib6Ymwtm40f6PI_IBkQWz_XF6CihrJjFgarrEBI9iWspOrwa7TWDoZ1p6yr4FmcmNEFYLcBznwjETEuvccP_Llaz0R73kp3CKWjuv9oC7DPxrVdKILUuSVKoxA44Vpz9HQekHJjhY4lYxSOwbNdiaHwt5hvzcYL3eSOrM-s-CuwO2z8Qsg0X4BaLY4ykB5xfc8OvW5Dk2pwo37InBR0fLbd5-IS7VPdjAKabAGXR9w29s1uztuyEGeI11H1CoI1nFbhuf0BzeIu-S0dNqnMixEQ1Mn4HUAPySkfKV4rTpaP-i71noAhe60XpyzEKyDwaAoI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری شاهد 136 به ترمینال فرودگاه کویت از دید دوربین مدار بسته.
mohsenreyhani01
سازمان هواپیمایی کشوری کویت با انتشار ویدیویی گزارش کرده که «نخستین تصاویر» حمله پهپادی به فرودگاه بین‌المللی این کشور که از طریق دوربین‌های مداربسته بیرون و داخل فرودگاه ثبت شده را علنی می‌کند.
در این تصاویر که از چند زاویه بیرون و داخل فرودگاه دیده می‌شود یک پرتابه مشابه پهپادهای انتحاری به سقف ترمینال فرودگاه برخورد و موجب انفجاری بزرگ می‌شود.
در ویدیویی دیگر، وزارت کشور کویت با انتشار ویدیویی اعلام کرد که شیخ فهد یوسف سعود الصباح، معاون اول نخست‌وزیر و وزیر کشور نیز ضمن بازدید از ساختمان ترمینال ۱ فرودگاه بین‌المللی کویت، این حمله را «تجاوز فجیع ایران» خواند.
کویت اعلام کرده در جریان این حمله یک نفر کشته و بیش از ۶۰ نفر مجروح شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر این کشور نیز در این حمله زخمی شده‌اند.
سپاه پاسداران که شب گذشته از حملات موشکی و پهپادی خود به پایگاه‌های آمریکایی در کویت و بحرین خبر داده بود، روز چهارشنبه گفت «هیچ شلیکی به سوی فرودگاه کویت» انجام نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75931" target="_blank">📅 01:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xxm8T8PVKrrRfESzfFj-h0YfDjwX8f3AhVOsEiYuUCyrHgBMDD-OrfFlLc0RGINNU-ETkt9V0az7ixSkrpkmG5EmWdoppWeJn1THWkSozY30G77NpYVryJE3ORMHtTKobE2B5u3XmTApvwA7LrbHeczCyrcTdc6T4PB4vfSNVqxuhAtzPTkv8-2lo8RPe9-TsmzXTTi-CvLNug6LHBodMID5rMWjIwvZDR0xpFeQUkfgq5A_mCvNhtH0x8nr2QoZnWezvboQplwr8u8h137XOwCvTd6AePKbE5y-SkGCZS4dhXpEvhB1896WnxIc5yI1hKO_taOG7Yn6OkIa-KdSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا روز چهارشنبه از قطعنامه‌ای به رهبری دموکرات‌ها حمایت کرد که هدف آن متوقف کردن جنگ با حکومت ایران تا زمان صدور مجوز از سوی کنگره است.
به گزارش رویترز این قطعنامه با ۲۱۵ رای موافق در برابر ۲۰۸ رای مخالف تصویب شد و چهار نماینده جمهوری‌خواه نیز به دموکرات‌ها پیوستند.
این رای‌گیری تازه‌ترین شکست سیاسی دونالد ترامپ در کنگره به شمار می‌رود؛ با وجود آنکه جمهوری‌خواهان در هر دو مجلس اکثریت شکننده‌ای دارند.
بنا به این گزارش، این اقدام عمدتا جنبه نمادین دارد، زیرا برای اجرایی شدن باید در سنا نیز تصویب شود و همچنین برای عبور از وتوی احتمالی دونالد ترامپ به حمایت دو سوم اعضای هر دو مجلس نیاز دارد.
با این حال، این رای‌گیری نشان‌دهنده افزایش نگرانی در کنگره درباره جنگ با حکومت ایران است.
سه قطعنامه مشابه پیشین در مجلس نمایندگان شکست خورده بودند، اما با اختلاف آرای کمتر از دفعات قبل.
همچنین سنا ماه گذشته یک قطعنامه مشابه را در یک رای‌گیری رویه‌ای به پیش برد؛ اتفاقی که پس از هفت تلاش ناموفق قبلی رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75930" target="_blank">📅 01:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sMw3CosRlx2L4igsZZIvTKV4_EJZB2JNpkYsCVsqrnySYMUtm4z7MY6o75X9Xx-x2nqedIx1RPVf5Fytf6k9GegqihFlCRIvzhx0kZ40JZJbspvCdtGaDu0xid8OxFHZ2zqaJjQHI7rTj6IW3Ty3pgTl3RXdb-L6Y6Obksb6zca4QqVt1xL7ekAOw7IhlEkn6TKfIhNcsLQx10dxjbegvjGQdCc2mAPd9pQ-ErVnzUGSlvxxQAa1gAL5_-XwuaN3S6m7lxogdutgx8YWTIiH7J9C8p-Aes_xd_s-0-txtxPIeKoybdFVGHhjVQovfcskVf6LeU7s_0c7PyMU8P3cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: می‌توانیم همه را نابود کنیم، اما ترجیح می‌دهم به توافق مکتوبی برسیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۱۳ خرداد در کاخ سفید درباره حمله جمهوری اسلامی به کویت و شکستن آتش‌بس گفت: «ما سه‌شنبه شب حسابی به آن‌ها (جمهوری اسلامی) ضربه زدیم، و در واقع دیشب هم همین‌طور. و وقتی موضوع را برای من توضیح دادند، گفتم بسیار خب، پس همین کار را می‌کنیم، اما ما هم کمی داشتیم شدید به آن‌ها ضربه می‌زدیم.
ترامپ گفت: «بنابراین برای بعضی چیزها دلیلی وجود دارد، و معمولا دلیلی هست که گاهی منطقی به نظر می‌رسد. و خب، آن‌ها کاری انجام دادند که خیلی… مسئلهٔ بزرگی نبود. ما خیلی سریع جلویش را گرفتیم، همان‌طور که با بزرگ‌ترین ارتش جهان این کار را می‌کنیم. اما بعضی‌ها ممکن است بگویند که آن‌ها تا حدی تحریک شده بودند، چون ما به دلیلی دیگر اقدام قاطعی انجام داده بودیم. بنابراین آن‌ها در حال تلافی بودند.»
او در ادامه گفت: «خود مذاکرات بسیار خوب پیش می‌رود. بسیار خوب. اگر اتفاق بیفتد؛ ممکن است اتفاق بیفتد، ممکن هم هست نیفتد، چه کسی می‌داند. اما اگر اتفاق بیفتد، ممکن است همین آخر هفته رخ دهد. تقریبا اوضاع به همین شکل است.
آنجا بخش متفاوتی از جهان است، می‌دانید. من می‌گویم در آن بخش از جهان، آتش‌بس یعنی این‌که به شکلی ملایم‌تر به تیراندازی ادامه بدهید.»
ترامپ افزود: «تحت هیچ‌ شرایطی نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند، هر اتفاقی ممکن است بیفتد وقتی با ایران طرف هستید، اما وقتی با کشورهای دیگر هم طرف هستید، این یک بخش بسیار بی‌ثبات از جهان است، احتمالا بی‌ثبات‌ترین بخش جهان.
رییس‌جمهوری آمریکا تاکید کرد:
«ما از سه تیم رهبری عبور کرده‌ایم. این یک وضعیت نظامی است، و واقعا هیچ ارتشی مثل ارتش ما وجود ندارد. ما می‌توانیم دو، سه هفته دیگر ادامه بدهیم و همه را کاملا نابود کنیم. ترجیح می‌دهم این کار را نکنم. انجامش خیلی آسان است. آن‌ها آماده‌اند که این کار را انجام دهند. می‌خواهند انجام دهند.»
ترامپ گفت: «اما اگر بتوانیم چیزی را مکتوب به دست بیاوریم که همان نتیجه را بدون کشتن همه به‌دست بدهد، من آن را ترجیح می‌دهم. فکر می‌کنم بیشتر افراد من هم همین را می‌خواهند. بعضی‌ها نه، اما بیشترشان بله. یعنی ما بالاترین بازار سهام تاریخ را داریم، با وجود یک درگیری نظامی یا جنگ. بعضی‌ها اسمش را جنگ می‌گذارند، بعضی‌ها درگیری نظامی. برای ما چیز بزرگی نیست.»
🔻
ترامپ: اورانیوم غنی‌شده زیر کوه دفن شده و می‌خواهیم آن را خارج کنیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۳ خرداد درباره خروج اورانیوم غنی‌شده از ایران گفت جمهوری اسلامی در مقاطع مختلف با این موضوع موافقت کرده، اما چند بار نیز نظر خود را تغییر داده است و این مسئله بیش از حد بزرگ‌نمایی شده است.
او گفت: آن‌ها [با خروج اورانیوم غنی‌شده از ایران] موافقت کردند و بعد گاهی هم مخالفت کردند. این یکی از چیزهایی است که درباره‌اش صحبت کردیم. خیلی هم بیش از حد بزرگ‌نمایی شده است. من خودم آن را بیش از حد بزرگ‌نمایی کردم.
ترامپ با اشاره به گزارش آژانس بین‌المللی انرژی اتمی گفت این مواد «نابود شده» و زیر کوهی دفن شده‌اند که تقریبا فروریخته است.
او افزود بیرون آوردن این مواد بسیار دشوار است، اما تاکید کرد: «من می‌خواهم آن را به دست بیاوریم.» به گفته او، آمریکا و احتمالا چین تنها کشورهایی هستند که تجهیزات لازم برای چنین عملیاتی را دارند.
رییس‌جمهوری آمریکا همچنین گفت سه سایت مورد نظر به طور دائمی زیر نظر هستند و در صورت هرگونه تحرک، آمریکا از آن مطلع خواهد شد.
او افزود: «اگر کسی به آنجا برود، دقیقا می‌بینیم چه اتفاقی می‌افتد و کمی هم بیشتر آن را منفجر می‌کنیم.»
رییس‌جمهوری آمریکا درباره مین‌روبی در تنگه هرمز گفت ایالات متحده از مین‌روب‌های زیرآبی استفاده کرده و مین‌ها را پاکسازی کرده است.
او افزود: «تنگه هرمز بلافاصله پس از امضا باز خواهد شد.»
🔻
ترامپ: ایران یک مشکل بزرگ جهانی بود و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند
دونالد ترامپ، رییس‌جمهوری آمریکا درباره گفت‌وگو با حزب‌الله گفت آمریکا برای نخستین بار با این گروه صحبت کرده و سه‌شنبه توافق شده که شلیک انجام نشود.
او افزود اسرائیل نیز قرار نیست شلیک کند و تاکید کرد موضوع‌های مرتبط با تنگه هرمز، برنامه هسته‌ای و لبنان باید از یکدیگر جدا بررسی شوند.
ترامپ گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، برای او «شریک بسیار خوبی» بوده است.
او همچنین با اشاره به نقش آمریکا در تحولات منطقه گفت بدون کمک واشینگتن، اسرائیل قادر به انجام عملیات اخیر نبود.
ترامپ افزود ایران «یک مشکل بزرگ جهانی» بوده و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75929" target="_blank">📅 23:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpUj9Wzv9J3CZp0ZrVv-WZ-UAGHn-yUXcGSOBplxvnkIa6_Ct6BchnihUL7MMpGLGnDhqKLp99hVCx0f9hb9hx2CpCLRzx4e3TIs1jAuv7CxjP0wxXCjdjenV1yg1wSBEazftDRzmNuRPzt-okJrHF94PMXj2MzbkTD8twrJZTooziGTlWwOHo66uTJTWHU2ulbVm3jkMNwVUUM4UjhfVhEHVJi4yzHjT5GgXvX5U0r7CTZ954SJEtah950bBkftU53w_0Jwo2OJjKd9EK1SNgIKaYFxkUNHbcJkMZE6NacEGpJsODnehvn2s5pKZuMEREPWHywdAJ1VFpIbvZySNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجی، وزیر خارجه جمهوری اسلامی، روز چهارشنبه تهدید کرد که حمله احتمالی اسرائیل به بیروت، پایتخت لبنان، باعث «ازسرگیری کامل جنگ» ایران با آمریکا و اسرائیل خواهد شد.
او در گفت‌وگو با شبکه المیادین، نزدیک به حزب‌الله لبنان، همچنین ادعا کرد که بعد از تهدید اسرائیل برای حمله به ضاجیه، حومه جنوبی بیروت و مقر اصلی حزب‌الله، نیروهای نظامی ایران در «وضعیت آماده‌باش کامل» قرار گرفتند.
عباس عراقچی در گفت‌وگوی روز چهارشنبه خود همجنین اعلام کرد که ارتباط با دولت آمریکا «قطع» نشده است، اما افزود که «هیچ پیشرفت ملموسی در روند مذاکرات حاصل نشده است».
ساعتی پیش مارکو روبیو، وزیر خارجه آمریکا، اعلام کرد که ایران هنوز تصمیم نهایی خود برای پایان دادن به جنگ را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75928" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/es_P3-7KQtiQThbSYV1IaZOduKFgOpvVFWKsWzxo3e3sJh2j7cRgERfBDQrsthIQAh7Ez4LtdHyRH_Eu5PtigsOp-2wE-2Dz6nDwoY9vE4URD8zCoycreT2oskYxy1W_o_EX1oucLxmuwlnwtit-XQHJcy1fAmVk95kLmY2SpLSOfdSPlCoEhLT1k_9Ifwh_eCh4XxNrWgh8M5wwrDC6rt4gfRZjBFQZRCfmVCMNUzC18wEhuSpzqCl3t5uanifC_xyfQV4jbvJrglGfYKwzbocdXn_H-2IpYqAWFkSDZH302TPgdzoIQN3E66xTp42Nf2DhBEz9bv97WtUYGOqePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
ادعای جمهوری اسلامی
درباره شلیک به یک ناوشکن آمریکایی رو دروغ خوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75927" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=fWu3rQGDqwMDJSEdtN-5I6mTWzf7E6id9EitQOKt27_3vryHTXMeqd243-VnS2aFcmBC19y9xmZPk1nH60UmahgJsOLlG4Z-4eIdyVz19TJfh0Po9w1mkImnxwztvN7HSpTBazrN6SNYvJLfCA_ae0dU7DVT7SJ6hzo4KKZVbvCepgJgD7Vo8ZYRiJvqXGoPRDv74JPi7kYWHFiaB0sgb0MPVKMEweDgqWO4qAeR8XiV-SieSn4qNXhSXdeIMmBmi-IwsiJRvD2NhqTUfM75yNzSmt5Y-75PP37uks8RG2m4eyLnnZqbNz0H2ualwASV-v9YU5JCO9hqyxkuJt_3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=fWu3rQGDqwMDJSEdtN-5I6mTWzf7E6id9EitQOKt27_3vryHTXMeqd243-VnS2aFcmBC19y9xmZPk1nH60UmahgJsOLlG4Z-4eIdyVz19TJfh0Po9w1mkImnxwztvN7HSpTBazrN6SNYvJLfCA_ae0dU7DVT7SJ6hzo4KKZVbvCepgJgD7Vo8ZYRiJvqXGoPRDv74JPi7kYWHFiaB0sgb0MPVKMEweDgqWO4qAeR8XiV-SieSn4qNXhSXdeIMmBmi-IwsiJRvD2NhqTUfM75yNzSmt5Y-75PP37uks8RG2m4eyLnnZqbNz0H2ualwASV-v9YU5JCO9hqyxkuJt_3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک‌های ارتش به ناوچه آمریکا در دریای عمان
شامگاه چهارشنبه، خبرگزاری فارس نزدیک به سپاه پاسداران به نقل از نیروی دریایی ارتش جمهوری اسلامی از هدف قرار دادن «مرکز فرماندهی و کنترل ارتش آمریکا» خبر داد.
فارس نوشت: «ساعاتی قبل و درپی نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی از سوی ارتش آمریکا، نیروی دریایی ارتش جمهوری اسلامی، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی را هدف قرار داد.»
در رسانه‌های جمهوری اسلامی ویدیوی کوتاهی از لحظه شلیک موشک‌های ارتش به اهداف مورد نظر در دریای عمان منتشر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75926" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W53T-3ANtmPZ9FljBc8vIDN5Gssne7qB-TguPWVF3c4m7a4lAzCtJP0H5z4luSQZ5KbQ8JPFVzmLCqCKAOWAFw6wP6YB-3VMucxhJ_tytHyT5MJTjBnb2mQ13CkJvQtX-7mE-6s8KIxNM4jQtDk62ELbRspior0GjiBGTwen0rs9ZQ-qc8QPBvsu5N3QcjA5UvydTvTUnOLPWUgh4bgNOL95ULCfQ28dRmrNCOgrf6PKAZ3qSRvQ6s4dXA5tBRWKuQ7hcQnU8l_hLLBLEbVAiFOPcchPvdjK3FX0lNqN8rbyZIusstj4XPvEepO7F3c40kXs_dD6HTBCb9465aFwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PjqzPp-elVM9cCkPDthxv8S7KrXtxcHlVDdvDMrkhlpTibEV-37r14ooX6GE3CQClqLmmCwAO9dGFCNqmI8BZhnSFon0X7VZnbYXrPH0sD7YGSimdDAP2YjQ-1FUKrgV1EnyJQbH3Bjl3Zr7YCrsjPyK4I_eFzoT-ktr82EqgCfghGxb5Hlceq92AEKzuQMm0Sj7UqQTy4iq4uZg3tIXRCyydmiIege3z5Pee45oh0LzUCxUNWWnieW0FPtxiprOjfVJAdpvnOmTl2pjolhBek_KbLeEcH7Qey-RWhE7KCrpxycWvnA13mfkTSLeuS1QL6Xrana6sNatldryoieNFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد ادعای جمهوری اسلامی مبنی بر اینکه به ترمینال مسافری فرودگاه بین‌المللی کویت حمله نکرده و خسارت ناشی از یک موشک رهگیر آمریکایی بوده، «کاملا نادرست» است.
سنتکام اعلام کرد جمهوری اسلامی با پهپاد به این فرودگاه غیرنظامی حمله کرده و این اقدام را «عامدانه، محاسبه‌شده و بی‌دلیل» توصیف کرد.
@
VahidOOnLine
پیش‌تر:
حسین محبی، سخنگوی سپاه پاسداران، گفته است که تخریب ترمینال فرودگاه بین‌المللی کویت «ناشی از خطای سامانه‌های پاترویت آمریکایی بوده است.»
به گزارش رسانه‌های داخلی ایران آقای محبی اضافه کرده است که سپاه «هیچ شلیکی» به سمت این فرودگاه نداشته است.
او مدعی شد که بنا به تحقیقات سپاه: « تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.»
در نتیجه فرود آمدن یک موشک در فرودگاه بین‌المللی کویت، دست‌کم یک نفر کشته و چند نفر زخمی شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر هند نیز در این حمله زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75924" target="_blank">📅 22:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RgveWytxbXAV_JOMQtpRvXBBGOOi8wYJsOCGZqdvtvEL0-JJNXICc3KNS1CgXb8YarXtPqg--CdmbTspI9yEhxiZ9CovVSCBPq8SstLbxYJUnwdfO1CNmmYmv5mJVk6umGVSwN6I0lLVK0921Wcb6LUjri8FCCImHH3_iij-FPmo9LOpaHdp2M0BIZ4u1gb-wkAFaiY7UyqmjdfGGEiLr3wnJwpPO0JyaOcLF7pF6LCnMYH1rjhwE2uEzO-nXMXKxj5q7js_8P5PkBNl_DygHgEzQSTokkL7f739QJn1nFcahce-zuRwywYCKrs5c0pkOvHm4mgVFarbDuMNdg-ZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mGlfPijcJWDDP3mqhuLG_ECXhJWmDpSrtzE3ncbsHA7AkNcEXZss25PLEaeZrO_rCAiyjxu_QPWxM3DnS3Bzxisun83KPE-WkoZn5F8SJBgxuScY1jL6QtfYBqgbyaGnYKga12YCy-cpKJdNanHRghFADcPXZimfBbkKNGW32q3cyIQ1vH91w2eoLf5hpR9UcSBGmJMSHuQwdu6BdOFMZ8MOIMT6Q_22sA0SVrdJYzL1nrJK4NPmxO9ulzpC2X--XZbB_pRDQY4JYioRXlAKMy_m75wDA-9sTAsFIqnWgEiUk7BfWgSkugr9Wg3iJ1SRJAqw1szS-mzABYaEJ8UyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DHCiyM_nWwMsogKUy1NnXh2Fn4K5vtwVA1NvDnlNNjUtgl2Cc4_GJTMF9HkC4TJ0bj6EB0NYEYaK7C4giDkG-hv4TkbB5_iE75aj8Gj0ITPAK7FA6m-fqESeiViTgo8_7L6S9QL5rFyd3wnFr4x_ebdaqeVTLeAqssEfeDJWxdUvDAWidf7iL3b58NTylo2h_VpkGVaYXO867Mbt9emI5xNR9FglXaPJ1qD91tw4sqqgXwet_J1iqfCj4rAduVdloXT4RWF01C33eEpF4t8njGZVQdlB3Ej9U1aM5gl9lfK5dDFQpwe7S6ehMTY8cj2CVPn0-6NaMHueniNR_Ct2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HjVULwo8PUaD7RqDMVkhfac6OZqclSrS7dpcsrEVwWsmZ9C8BuoxLbmltMuNU6sEKTMIGO5cJza_Vl5oc61_sQHvMHkprYOcGP1qtNLZYRfPRT0qpRkhOtjmLz3wgMHfLeHIupFRe9LSF6QO4c_U09ctK1S44869vUKL4uHnT2AhoepKuEfzwnIXMaKLxrZuBw_AOwHZ6iFNePV_VdvZXM2SRYFAg1eVncyehQzDlZeiKQ4OumFUtODVqvjw0v4TWaPcJW-KWteFgDWvIPCyfcNSo-br8y_RhSNCH8kLfkK7gAKqQQHx8hXUEQAnC-hfcKNyIRHYPaW2zfKTcMiutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Auiah0FORLOZtDOL3hUB0h_AHVCEF4QPSFMy11Hvyg0ya9TA_ErBf_pUXZtcIEI6ym_ZfhEPg8l__1LkyoQGIE6e9XbNUP8eKYwrJYukpdcgXuRqsYeLZvKsg3tl51GAIdVdDakU1TSY8GkJe6CSuGP-_R58lI23DeGgbTLQpvWnYoXQwPOmU0zjSWHvIoHVtT1iTnt4ORPPmDkURVVa1J3BhuGn96J08G-D_wa6hVyNKScWzr4oAZ6Z3fE2Ll5ljqUgzY-d1_XOzXiDzjHAYpXCJwkO7pVfYDH8Apuppi3o1mb1k-yVmJSmd-nl-rHqNfyoB-0xgfzQw2WxBV78zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f6b_dSsVmPXHwR-VJh2KFaOw9Vl5C7FWAYA-2B_mpupKcKZ-jykE1ywTJAVMVuaRTYNrOsNPPaMZkYK59AmWoFoCKbcdQueIN8VQjdmjOl3ai2RQP7rNrKDa-PGwwz6YGfArqiTUa1LoYlNAIx2WDWFAf85BTMaEu7Tc_qQsmTQi3PFO1RaOw4tuQvaFnyGuucMfuyIcp-8GO_L13Jop-4SoWUVetZVzIr97dPu8LpftUxm4XeqjcAIKkxrlGSrZyLuSClvBrgiy8UX36c5f0vzu7J4x2tIba3LOmSO2pczc00zjYvTzpHB5e4mxGXkyFAH5F7ucbpm1LVsKASEYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HDXBHdLM9YSA8NMO1titmttCWpAwrZJhGkRrNzTsPbxE2fRzMDN9m9NhN9k1MjkwqaSxC6WJHps43OQmWEQeo_yrgrqTLylIU9_NHNVNExrBur4Zi4XJz1XnvC6y5O9Wi_7K5iSjKH5Za5pfE12tbR_X1Iz2IdLqX7D8pqQWWDj_3CMyKwjk48OgYea1jfSwL1p0lX-IxA_nMFJ2YRalS5e-t-IsHjr8YhqVbuXPc0gAeI_79HR0u-zfCrWxBLPda8XZ8g_e05ErXOMrRkRY3-MRhLjyxswrs_qAo-bKI5nIBVqW0EJIRWbe4C7n2mDH4ibeUsWnuCPTX7LoBrQgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S7nd9Wok6tmz00I87nXVX6Whei9yr1-pumK7prq9wqf-gH4C0PPerAGskLqiaDYvFnn_H5YzohIUYOMsNBsaCiX7q4yBflmCuFR9SKSYIPSHk8UCjNIcQBS1OEkuoBvgtpA-MXcBDxhPLCfm9guPgAL2U46qPMSLfa4HSS5adV9kLDnfJq-negoGsO44A9Dcc9ezNNQ2Wxi6Uc1PXEgGEAShah-eNedktWiHMRw5dL5PvcRttauM15Rm-scF8491fUow09NS-SVYm7aGIn0VVuWdzNIwThsoGwLm0J3ovSfh7m4kLUZFmtDfsUM83jlnawBrq_MoY-xkvHAOvsuWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYdfBkLbZEAkM1TwcK2RgsvdctoSAwqmvFvLwxtoMmmzLynbhcTEAncfwDPwh1Oj4q1aUh9Wgeje0s177MHXhB8TNZWUJSGPY92oB9ynolg0GQySQsdsLCQojhGgSPFu4FBPVX_2zALKbFx8sK14EpJkd0C78i_K58gepm9EGYSGHbazYREYCAZPWOGAenbzU8aBhD0OoWRrNcJAiYe_OXZ6Ju42NKxbhHox-lSzTFDRef-hg2sfqV2OUTAboF1AMra9l4xf2wYDE6qTLAFk4FvASUNy6lQYiYRimZgnM_SFRX1tJraXNhFjl7blNwwEc2A5c80VTtqouiwIT3DetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AprA_0GdNia_zd94vb9AVGNd2_wyO3raiTqYZHby7lkuhPW96lKimioeNvEsxgHG79d9quxx4IfbworBnEe3Q96qGrv1Op2FDroWw7QqoVO82M922pTGvCiTHu89zCcBss7vbEiII1YgX3xrfjN7aFRCZdwadFRwbPBBKn7dynsk1DDcL4C8SrU2wZqMwaJZUZwTr-c2Cfh_l9552nZYS2AJgcQ1WpEh_1fCfF9gC4YBC1fzRaAlVz9OEpjksqU2Aa67xFcWpIhwcSf0tCU4xNKg_AVAPCXiCdXyWRECJnowwxhi7HowU0wJ748LlWoMypsx-JUKwCayzbOFuJumbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دادگستری آمریکا روز چهارشنبه اعلام کرد مدیرعامل یک شرکت فناوری در کالیفرنیا به اتهام تأمین تجهیزات آمریکایی برای نهادهای هسته‌ای و نظامی ایران بازداشت شد.
بر اساس بیانیه این وزارتخانه، جمشید قُمی، ۶۳ ساله، شهروند دو تابعیتی ایران و آمریکا و ساکن نیوپورت کوست در ایالت کالیفرنیا، به «تبانی برای نقض قانون اختیارات اقتصادی در شرایط اضطراری بین‌المللی» متهم شده است.
او متهم است که «تجهیزات پیشرفته شبکه، امنیتی و رمزنگاری ساخت آمریکا را برای مشتریان ایرانی، از جمله نهادهای هسته‌ای و نظامی حکومت ایران تهیه کرده است.»
وزارت دادگستری آمریکا همچنین اعلام کرد که جمشید قمی از «شرکت‌های پوششی» در امارات متحده عربی برای پنهان کردن محموله‌های تجهیزات شبکه و رایانه‌ای که مقصد نهایی آنها ایران بود، استفاده می‌کرد و این شرکت‌های واسطه برای مخفی نگه داشتن مقصد واقعی کالاها و دور زدن تحریم‌های ایالات متحده به کار گرفته شده بودند.
جان آیزنبرگ، معاون دادستان کل آمریکا در امور امنیت ملی، در این بیانیه گفت: «طبق آنچه در کیفرخواست آمده، قمی با تأمین فناوری آمریکایی برای سازمان انرژی اتمی ایران و سایر نهادهای تحریم‌شده مرتبط با برنامه هسته‌ای ایران، به ثروت دست یافته است.»
او افزود: «بخش امنیت ملی وزارت دادگستری افرادی را که برای پیشبرد اهداف هسته‌ای ایران قوانین ما را نقض می‌کنند، پاسخگو خواهد کرد.»
به گفته وزارت دادگستری ایالات متحده، متهم بیش از ۱۵ میلیون دلار از ایران به حساب‌های بانکی خود در آمریکا و یک حساب امانی منتقل کرده و به‌دروغ این پول را به سازمان مالیات آمریکا به‌عنوان ارث خارجی اعلام کرده است.
بر اساس این اتهامات، اظهارنامه‌های مالیاتی فدرال او تقریباً هیچ درآمدی را نشان نمی‌داد و بالاترین درآمدی که در هر سال گزارش کرده بود تنها ۲۰٬۶۸۴ دلار بوده است.
وزارت دادگستری آمریکا همچنین مدعی است که او از درآمد حاصل از «طرح دور زدن تحریم‌ها» برای تأمین هزینه ساخت یک عمارت چند میلیون دلاری در اورنج کانتی کالیفرنیا استفاده کرده است.
@
VahidHeadline
دادستانی علاوه بر درخواست مجازات حبس، به دنبال مصادره اموال وی از جمله عمارت گران‌قیمت اوست.
بازپرسان معتقدند او به مدت بیش از یک دهه از طریق شرکت خود در تهران به نام «فراز پرداز رایانه»، بیش از ۲۵۰ تن تجهیزات کنترل‌شده تکنولوژی را به‌صورت مخفیانه خریداری کرده است.
او متهم است که با استفاده از حساب‌های شخصی در eBay و PayPal و از طریق شرکت‌های صوری در امارات کالاها را تهیه و به ایران ارسال می‌کرد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75913" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rObrSoGfm-W-hdVvNlpq1ePAdAAPe7m-W255kC2mhLSzYrdBm9MEeq-FCPcfopq2XIqTieGUxLDcu6TA9C5seyhKOOD62yP0Y8ToCFsFrYv0MUko1TvEVx9GAb0VQygkuiPdtDmDbV6OqrP48wKNMjVjvvXFdlJAF5AE5_UMEJ1YEv1Za1KbABba7_W2nlTOOqJxd50geFmERb0ymIYGJ7waS9b96ycQtLwHe2E1BDRo9NVlb0yiy7JVrhBEEW2KjvXP7uKpt55jELlmbqRVPkL-76SY0o5RtprjUj7uDs9dNsS3gD4efuUgaUUSp6YW9LZCUT7Kdc4TbjSIr4Tr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbaOPg5jF0YFEIMjX6HZmId2aibnwRZai0qLAXdsGz4ZRcfc1xM7-7rQ3BBbCRZ6QG1Qk3pyL--oMaH5yoEzttwAhEP0hpXjGf8VreY1rBO2B7neJtFecv6YIxUcMV0wlkc814POi1cBWG8JKJWgpkuS0Sw0pqxUylg8S0Zh93YW9Wwe-X0zcvF9GmQYo98bqqEBnD1wyL7KFvIOs3o_gEHUtrmfkMQp1vTj78Xyw-2JBpp8H4DkRS-r3YaeshhEvewSfA_RbJRSfZJhRYf2QOjWMr6i8sMn1gUvD5Wa4UFYv7drwmMx4MoWDTCEoV6NoQKwX5DBDMoT2Fq-Pt0f5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌ان‌بی‌سی، ترجمه ماشین:
▪️
نتانیاهو از پاسخ به سوالی در مورد اینکه ترامپ در تماس تلفنی این هفته به او فحاشی رکیک کرده و رئیس جمهور آمریکا گفته است اگر او نبود، نتانیاهو الان زندانی بود، طفره رفت.
نتانیاهو در پاسخ به سوالی در مورد اینکه ترامپ ظاهراً او را «دیوانه» خطاب کرده است، گفت: «وارد جزئیات نمی‌شوم.»
[ولی ترامپ در
مصاحبه با NBC
گزارش آکسیوس رو تایید کرد که بهش گفت دیوانه]
▪️
نتانیاهو می‌گوید او و ترامپ «اختلافات تاکتیکی» دارند اما «در مورد مسائل اصلی اتفاق نظر دارند»
نتانیاهو هرگونه اشاره‌ای به اختلاف با ترامپ را کم‌اهمیت جلوه داد و گفت اگرچه آنها گاهی اوقات «اختلافات تاکتیکی» دارند، اما «در مورد مسائل اصلی اتفاق نظر دارند».
او گفت که این موارد شامل جلوگیری از دستیابی ایران به سلاح هسته‌ای و تهدید اسرائیل با آن می‌شود.
او گفت: «گاهی اوقات، مثل بهترین خانواده‌ها، این اختلافات تاکتیکی را داریم. اما ما همیشه راهی برای حل آنها پیدا می‌کنیم و این کار را به عنوان دوستان خوب انجام می‌دهیم.»
او گفت: «ما می‌توانیم صبح اختلاف نظر داشته باشیم» و تا بعد از ظهر به زمینه مشترک برسیم.
▪️
نتانیاهو در پاسخ به این سوال که آیا واقعاً آتش‌بس با ایران برقرار شده است، گفت: «فکر می‌کنم یک بازی تاکتیکی در حال انجام است.»
نتانیاهو گفت: «و ایران مطمئناً می‌داند [ترامپ] چه گفته است، اینکه در صورت لزوم، بازگشت کامل به اقدام نظامی وجود خواهد داشت. این تصمیم رئیس جمهور است، اسرائیل آماده است، و نیروهای آمریکایی نیز آماده هستند.»
او گفت: «فکر می‌کنم ایران باید این را در نظر بگیرد. فکر می‌کنم آنها دارند این را در نظر می‌گیرند که دارند با آتش بازی می‌کنند، این واضح است.»
▪️
نتانیاهو از اقدام تلافی‌جویانه ترامپ در محاصره بنادر ایران در تنگه هرمز تمجید کرد و آن را «بسیار مؤثر» خواند.
او گفت: «محاصره معکوس، یک حرکت هوشمندانه بوده است.»
▪️
نتانیاهو گفت که «هر دو روز یک بار» با ترامپ صحبت می‌کند.
او گفت که دو رهبر «اهداف مشترکی دارند... ما می‌خواهیم به آنها دست یابیم.»
اما در پاسخ به این سوال که از توافق آتش‌بس احتمالی چه انتظاری دارد، نتانیاهو اذعان کرد که «این یک سوال بی‌پاسخ است که جنگ چگونه باید پایان یابد.»
▪️
نتانیاهو گفت نهادهایی که به نفت ارسالی از طریق تنگه هرمز متکی هستند، در حال حاضر «در حال توسعه مسیرهای جایگزین» هستند که کمبود عرضه انرژی ناشی از بسته شدن مؤثر این آبراه کلیدی در طول جنگ را جبران خواهد کرد.
▪️
نتانیاهو انتظار دارد که تغییر رژیم در ایران رخ دهد زیرا رهبری فعلی «به شدت» تضعیف شده است - اما پیش‌بینی نکرد که این اتفاق چه زمانی رخ خواهد داد.
نتانیاهو گفت: «شما نمی‌توانید دقیقاً پیش‌بینی کنید که چنین رژیمی چه زمانی سقوط می‌کند. شما در بسیاری از موارد آن را پیش‌بینی نکردید: نه در رومانی، و نه در سقوط دیوار برلین، و هیچ‌کس آن را پیش‌بینی نکرد، اما این اتفاق افتاد. چرا؟ چون ترک‌ها از زیر در حال گسترش بودند.»
او گفت: «در واقع، شما همین الان در ایران شکاف‌های عظیمی دارید و نمی‌توانید پیش‌بینی کنید که چه زمانی این اتفاق خواهد افتاد.»
«اما من دیروز در یک نشست عمومی اینجا گفتم... ببینید، من معتقدم که در نهایت این شکاف‌ها گسترش پیدا می‌کنند و رژیم سقوط خواهد کرد و ما تمام تلاشمان را خواهیم کرد.»
نتانیاهو گفت: «من فکر می‌کنم که ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تغییر نکرده است، اما دقیقاً در لحظه‌ای که ما انتخاب می‌کنیم، این اتفاق نخواهد افتاد.»
او گفت: «فکر می‌کنم آنها به شدت تضعیف شده‌اند.»
nbcnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75911" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctDitowIHlGla9IF-nXEbFjeS82TiQHv110k90uro1AF1M0UrDc6839nOvfiMh5EGrtj1e5gpQNtXkOQL8_5awmF86grExbkKLo06cnOIP817ubOSQQj7BLL0u5nCyKgVc4djopb7YeQAegfhJHPk8cSl33hgIzGmcI348JNB4BrLqH6pI6AJMplSmBx8lUVuz-2A7kSoEXQdmVegFDZFUvTogqGWCpcp1RQq7XBOul1DOAPvTW4UxhanXyey4uopSelqC6LovWq4DW0sizrp_H6PzmWeJeVKT33-g4EF8q9qGp9ldK5wRWJFFoOiR4AjixQfFVrMiOfdKf45yl7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه گفت که سرنوشت ذخایر اورانیوم ۶۰ درصدی ایران در مرکز مذاکرات با واشینگتن قرار دارد و تهران هنوز با یک توافق صلح موافقت نکرده است.
روبیو در جلسه کمیته روابط خارجی مجلس نمایندگان آمریکا گفت: «فکر می‌کنم اکنون در برخی از اسنادی که میان دو طرف رد و بدل شده، این موضوع به‌طور واضح مورد توجه قرار گرفته است، اما تا صبح امروز هنوز تأیید نهایی از سوی نظام تصمیم‌گیری آن‌ها را دریافت نکرده‌ایم.»
روبیو در مجلس نمایندگان آمریکا بار دیگر بر اظهارات پیشین خود مبنی بر پایان جنگ با ایران تأکید کرد و گفت: «ما دیگر حملات مستمر در داخل ایران برای تضعیف توان نظامی آن کشور انجام نمی‌دهیم، زیرا عملیات "خشم حماسی" به پایان رسیده است.»
روبیو با تأکید بر اینکه آمریکا به اهداف خود دست یافته، افزود: «ما پیروزی را این‌گونه تعریف می‌کنیم: نابودی زیرساخت‌های صنایع دفاعی ایران، کاهش قابل توجه تعداد پرتابگرهای موشکی که در اختیار دارند و کاهش چشمگیر ذخایر پهپادی آن‌ها.»
او ادامه داد: «ما به همه این اهداف دست یافتیم. علاوه بر آن، آنچه از نیروی هوایی ایران باقی مانده بود را نابود کردیم و کل نیروی دریایی متعارف آن را از بین بردیم.»
با این حال قانونگذاران حزب دموکرات در این نشست موضع آقای روبیو درباره پیروزی آمریکا را به چالش کشیدند.
از سوی دیگر ایران بامداد چهارشنبه کویت را هدف حملات پهپادی و موشکی قرار داد که به گفته مقام‌های کویتی باعث کشته شدن یک نفر و زخمی شدن دست‌کم ۶۳ تن دیگر شد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75910" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۳:۴۵
سلام وحید همین الان بندرو زدن فکر کنم فرودگاه یا پایگاه هوایی بود صداش زیاد بود جوری که تا شهر نمایشو لرزوند
بندرعباس سمت اسلکه صدای انفجار یا بمب
وحید جان بندرعباس صدا انفجار خیلی بلند 13:45
بندرعباس رو زدن خیلی بد بود این دفعه صداش از همیشه بیشتر بود خونه لرزید
سلام ساعت 13:46 بندرعباس صدای انفجار اومد.
غرب بندرعباس
بندرعباس صدای چندین انفجار سنگین همین الان شنیده شد
همین الان بندر رو زد
سلام ، ۱۳:۴۵ صدای ی انفجار با لرزش شدید بندرعباس
سلام 13:46 صدای انفجار بندرعباس
وحید بندرو فکر کنم زدن صدا انفجار اومد
سلام همین الان قشم صدای انفجار شدید اومد
هرمزگان صدا اومد
بعدش این خبر منتشر شد:
"معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان گفت: صدا‌های شنیده شده در شهر بندرعباس ناشی از انفجار‌های کنترل‌شده مهمات دشمن است."
(گزارش درست اینه که: صدا شنیدم.
از روی شنیدن صدا نمیشه گفت "زدند"، "حمله شده" و...)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75909" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRRMPspOf8Cb7hUcgahdQ_24Yys36Dz3eoGPXX5C8UXzLpHZ9fNZE28nXMWPLXaHNqG-jXCnXYp7m6txBvPXexDYK_5CkG_KpigaKvWhVuWYyWS-By4VXM9iSNoMWSdG9Txpc9AN2jpHGFe6cWoajuWb0zUfvb_dHiiXfvQHmZEYalbCqakCB10ROK1lrxRIxDngLwJtsOhagNPA85Bm7cS-qtz2oBrMbZzOAu0xgwv5VSzNnmi9FcC1_2OeFzd0-4CVRBxJRTMqkVILO5pisiqLLuu8ruDlMzMt_mVZi_fAzmWnv7KWoR-JwfziYhEdLyP-qBs9HxShOHWJlcH2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم جلالی، سفیر جمهوری اسلامی در روسیه با اشاره به سفرهای علی لاریجانی دبیر سابق شورای عالی امنیت ملی به مسکو گفت: سفرهای او، به جز دو مورد که خبری کردیم، بقیه محرمانه بود. یعنی هم ما و هم طرف روس، سفرها را رسانه‌ای نکردیم. فقط دو سفر اعلام شد.
جلالی به خبرآنلاین گفت، لاریجانی سفرهای محرمانه زیادی به روسیه داشت و در یک سال‌و‌نیم اخبر، هفت بار به روسیه سفر کرد. جلالی بدون اشاره به دلیل این سفرها و موضوعات مورد مذاکره گفت: «در یکی از این سفرها، طرف روس با من تماس گرفت و ابراز علاقه کرد که سفر رسانه‌ای شود و آقای لاریجانی هم مخالفتی نکردند و خبر آن منتشر شد. اما سفر آخری که در ۱۰ بهمن‌ماه ۱۴۰۴ صورت گرفت، به شکل دیگری رسانه‌ای شد.»
جلالی افزود: «ما دیدیم وقتی هواپیمای ایشان حرکت کرد، سه یا چهار هزار نفر در فلایت‌رادار آن را تماشا می‌کنند. زمانی که هواپیما در مسکو نشست، این رقم به ۳۴ هزار نفر رسیده بود. برای فلایت‌رادار، این عدد بسیار بالایی است. بعد هم یک‌سری شایعات شکل گرفته بود. در ماشینی که ایشان سوار شدند، به ایشان گفتم که این سفر را باید رسانه‌ای کنیم. پرسیدند چرا؟ گفتم با توجه به حوادث ۱۸ و ۱۹ دی، الآن عده‌ای از ضدانقلاب‌ها تلاش می‌کنند این خبر را به شکل دیگری جلوه دهند. برخی نوشته بودند که رهبر نظام به روسیه رفته یا برخی گفتند که پول‌ها را به روسیه برده‌اند و این خبرهای عجیب زیاد شده بود.»
جلالی در ادامه گفت: در ۱۰ بهمن، زمانی که علی لاریجانی با پوتین ملاقات داشت، در پایان جلسه من گفتم اگر اجازه دهید ما یک خبر کوتاه، با هماهنگی، منتشر کنیم. به این ترتیب همان دو سفر رسانه‌ای شد.
سفیر جمهوری اسلامی در روسیه همچنین گفت: پس از کشته شدن علی لاریجانی، پوتین متن پیام تسلیت خود را آماده کرده بود اما گفتیم منتشر نکند تا اول رسانه‌های داخلی خبر مرگ را اعلام کنند. [چون فعلا به مردم کشور خودمون دروغ گفتیم و ضایع میشه!]
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/75908" target="_blank">📅 17:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVZTiHsUSC2Em4QcE385EwnitlEQZwXXMqNCjR1jRsrrom0mKCSvsE0kUcpNrdABwl8Qanwim-SjDLn7yyu77mz7cmBS0joB69zDuWON_A5OyWq5yNXy7wuoW2tPUK2aBn8qntpMGtd5q12Zp7HrARTVeMR9tZsKgX4NhWcIRa6Our3lbc4arRkkeFtnjGCvzn4_NV8FmmyJoTbdGzKcBfhyx4QCPop1xv4Vub7dsBBnxeh8tYncrKAiOBP8Fp4QjCS8U2em9uODR9sQ3PU7RbqX5RneR2Xg3uohJWc4K-t8OKUu3MoywRVNGVnR4eL5gJJLLJ3neUGkorjykNGuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگو با پادکست «پاد فورس وان» متعلق به نیویورک‌پست گفت که جمهوری اسلامی موافقت کرده که سلاح هسته‌ای نداشته باشد، اما همزمان یادآور شد که تهران همچنان می‌تواند «نظر خود را تغییر دهد.»
او در این مصاحبه که روز چهارشنبه منتشر شد، گفت: «ما باید کاری در قبال ایران انجام می‌دادیم، زیرا صرف‌نظر از اینکه وضعیت ما [از نظر اقتصادی] چقدر خوب است، نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.» پرزیدنت ترامپ اما اضافه کرد که «آن‌ها از قبل موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند.»
وقتی در این گفت‌وگو از پرزیدنت ترامپ سؤال شد که آیا رژیم ایران با این شرط موافقت کرده یا خیر، او تصریح کرد که «بله، آن‌ها با این موضوع موافقت کرده‌اند.»
او اضافه کرد: «منظورم این است که آن‌ها اکنون می‌توانند نظر خود را تغییر دهند، اما این یکی از چیزهایی بود که باید با آن موافقت می‌کردند و موافقت کردند، این موضوع اصلی و بزرگ بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75907" target="_blank">📅 17:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxwWiLVxNRlq9lBwKt1qejlqK4CTI-A8deBE9WHpa5Ae26WE9Tm3mCKKbtEfZs9JPrimD4I-VzLZK-hv32zVKyYnA8fwhTK0fbv_JvqFu1CE_t0KHYrZhL0WcejxJFFH11Uikesd7U35DwapToBVfBVxS6zbFTi9gwKrJxT4dB7t6qnQpa7D4viYqdx8qn8qjYzdOvjYey_Dmb4yAtM_w-Bj-wPpnwCzkNu57BTOmDw_E-Tlz7J2JSlyjxHC5hknmP4i6rpO1s4NttT8I5dAFbkdRA0WVFCBVCEjBh1aRhc0DQz2b_JNuY_c7M21uDUvRaEJRHQoYKjMNtknRDNhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید این کشور مصمم است مانع از تلاش ایران برای «جا زدن» افراد مرتبط با سپاه پاسداران در کاروان تیم ملی فوتبال برای شرکت در جام جهانی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75906" target="_blank">📅 17:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ap2bo-k1sHeJtLar_xLLI0CRV3E3dqBwyo3tGaBZC0smgelMzXTSzItibXSfdYkSAqO9lVnq1bJsFT0sPAXXmzSkzucAwfKGsSh6uL-0E8jBVThawC8XVd3gWK3eR5hvsXDWQca_-2TDO8gjO6Z06Q0u4-8uzfWQBGM68oJryWc64hO4CO0Vfywq6Y7IE_87DNnuYkC7O9GtoeP-HjdLyOUkWDRSMqogPcdni4QBgnHAItZcf95JnMZgcKsT5qIm5HeJaoBjXIpiXMtqBm7fBjmlxsWLPyp9sTt5OL_M85OPpDUurCzT7n5id6j7cNww9-OdrSOieGLnwAb1XeIwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RAbZNpXV5bd4_NsigeppEFm6F-TX5uHPJOPXN5oTf_wiuHpRVV1Wh4HhK5ttSADJWudeu6Qw0XImhEcRBd6HaB6wy7f_qiSrfK2fOOtkfbQI9QGaWVF067dhHN0rRH0j7KFNTsCRT-n0VKfkLE0zA-f0EDNMrE8B4QxOdyCEbwHAnxeiSegTdp5A1jGnGn003bY85jWtet40Q-Z3l0N4qqRy7zttZ5ofb2RgWtXwotrcmomicEWMiC9F4ZlOfuC03V0OPyP1PZsuNdV62rRVYa63CNLCVUQR9IjGJ2aqq6GkTwEnXf7M4A2OFX3ntxUbpiwlvLWKLTIjvLR1D0C2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LBTaLuh0soZ2iOjgSrby37w6jdl9Q3BtksIR8sx7w8DIE9lCNMUrvIQT_d5mFbXFyUBasd7f1bSraVAf5v9t0MY-IKj51u13WwNZnNUqsiWYZt0iyfK0cBd7vDyQXXoG4oBifdQac8Kg4yj-JTOiW9_dm4f-bGWoWephJ6BDa1kDRFxLg1dX1ezkPR9yr3tqQJs7ip10bjMyBXZ7xUQPfMEJ3ZJu2-8x7K3DALioIOAFW0fQeIwa-mCPOk73Q-gEM9MV43GSTV07Jh4mfoOICFh_dMzmvk_AoP8t-y6XAUcURUuYbjhfIacfU76_esKQbKERLsCo_fp9vOgLraBOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZkBkpPrnPZADhND4wQYEePk_NAHy93M1izXtvO7WzhAZ-PxBURewSUqT7Nw9bDy2yxrN-nxAPbdELVOhA_x4Ws2cJwQcv_me-GMgkOYfQrSkmqv4HES_M1_-rcCwePni5aCv4PtN8iqhW8mwy1F7zvQFUw7KR4P7qH-cZkK4Hd-2Pfldqn7HqbACv7GwDiVG6gc6zoKANruvYrbQzVy7W1yBZC9uM9g9J1SErmh40V0fXGUO3-b6ufMKIKDFg93zgKtEVRBW2bxXF7U1MQ2PzvRHz5e7o2IQgkTm7cegfg4jGZv0bglNJj3u3yhWeWqyztf5NKEKRu1txOmQkKyuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A5ojSRsUnag_CU1Dl9IoWjo4pNuPOZMhqyXMEV9gK45ax4XoEhImIImTVyxvANxG5c_FR7bJzp-tj-ULarGjFg8c3KEP30AKPuRSfVOdBcMNNfESg3EPjohhhYc-IOuZTtiHzdwwsAkekKtDRDDl0diOFpHMWwMVF_9NB15-no_PQ4SydNmXl42TR5g29Z977_BDTF04hHJ7NYNlv4K_RVdASs4o83D1Sjb9tvgPyvxSoKSubAM6AhAqtbMg5L8kJfzaqkiHGv_6hEUeXgO_yoEs2ksqiT6s_QZWudI8gG_W3JI0fes6e3vyH0cfA5zrHOYslP151kb7FAZo0nCANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OjFZLTYi3-6NgbNvx1CUj9pyn4bKwPI5z7EJYY3juIpa5yz-jRolcoPCbcOs3n1BSsdBlBPN-xb1S_FpbEQJZ0PzJxQaz0W8QKoMx1PetiJ7B2T3TOZGSGRKlYSlEQa09eRrVhrjkBW04CGgCVumRzhEjrHXnD0GzKkCX9G9PIl6Y2okb007lGg0ovtdz-coJDhHCd1fd6VNpFJjUIVLc3qZ0vrIkkxP0hCquU_XL3hAnhRPqjR8VCgcKgYU_BmbZZU5YqHuyxf7g8L9tQKlJwd2x2e1lfZvH71s-QVK4CdPftzwKDE7mkEAuBGAdvEeE4Rhb-kb0tR-6SKY6KmMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sNc3LQuCsoq_mUmY4Qp0Xjj_0RJRSG1csglD_3oxDtdxJrUtONibGgfD2oeh35s94_KY8fRQOdBpqvqYd5RlOwiv-GM5pFGtHSM4O-ICCl8mqX7wT6r9iRYmcDzlxiCxkO7ZvFMHtn1EDGuphRGa5-iGq-HokChbpxSyEZMR-6_ZkPD05_neMToQyDCtnHt3GbOSoWavc7de0PBzO63uvteqYkb981o1EuTeumSPiJ5kavhSI4Vivm90QmMFXUFjDy_Hqn3AWiUycGYKV4_RSSENJ0jcUIhbA3E8OBR9hrst0UZxZlSSZhi3BllwYayL7biLlJU_NYu23f3kOrx2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gv2jOkY65bFAdRB8dOeWIyYo0DiO6I431cbOBQcLechAP5E060UlKz2eFFrbzz7pMFYsKqH2IixfLPdqfExMuw0veXSS_1WcSi5WVwOTztoP2hd5I-Buc6dSTYTMx3us70iz6Fu17n-JxsU3IvdwYtBs540NghHGGLGaOoEPjJ4SnCgDcK802GrEVs5tRC0qXt2J6ErR02QlhE2pshZZPIhz4Ye3EptAP5nm59og2eZQN-TPp7HvdkEGrpmiH5wGrZoOhZZLBr3qdYp1K03VuVP-ME0O-Ro1dbH2tnCLB4GA7SnynYwpwFwBhwshJIO6jtKhvYfNGPxT7r15lsGaRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=j7jnSLKq3555fjICYthdb1VaRZE3Hv-2EkCY_5-v5lS0TTpyjUDV1-ct7O3TL6WNkiLpJbuDp0N8qoJCR7sAXQvb2steJHJw5s-j8l5gCSvMUITemt_VRfZHjL4Oh_e65uYaFV4OQK7UMx9GbY9uFpNMmVKW0nohRAuGyJn1_b872uuYv8PJnpCfENkocBm4B2xMKEgEOZnRfMeui7SYgT23Nh7p870-TnqB3MQYv7TIsC7C5kftWG_uG5bMins2NsC6qx_uhJhtNfAHcJwnM-OE4_iKIREw57iqHTopkOx5TxcHzfVCB8CEYONJS1XpwGhTREMh_seBkzYyyzTqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=j7jnSLKq3555fjICYthdb1VaRZE3Hv-2EkCY_5-v5lS0TTpyjUDV1-ct7O3TL6WNkiLpJbuDp0N8qoJCR7sAXQvb2steJHJw5s-j8l5gCSvMUITemt_VRfZHjL4Oh_e65uYaFV4OQK7UMx9GbY9uFpNMmVKW0nohRAuGyJn1_b872uuYv8PJnpCfENkocBm4B2xMKEgEOZnRfMeui7SYgT23Nh7p870-TnqB3MQYv7TIsC7C5kftWG_uG5bMins2NsC6qx_uhJhtNfAHcJwnM-OE4_iKIREw57iqHTopkOx5TxcHzfVCB8CEYONJS1XpwGhTREMh_seBkzYyyzTqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت خارجه کویت روز چهارشنبه ۱۳ خرداد اعلام کرد در حملهٔ پهپادی ایران به «تأسیسات غیرنظامی» این کشور، از جمله فرودگاه بین‌المللی کویت و برخی نمایندگی‌های دیپلماتیک، یک نفر کشته شده است.
وزارت بهداشت این کشور نیز اعلام کرد در این حمله دست‌کم ۶۳ نفر زخمی شده‌اند.
وزارت خارجه کویت در بیانیه‌ای که ساعاتی پس از گزارش‌های اولیه از حمله منتشر شد، مشخص نکرد که کدام نمایندگی‌های دیپلماتیک در این حمله آسیب دیده‌اند.
ساعتی بعد وزارت دفاع این کشور اعلام کرد که روز چهارشنبه ۳۰ موشک بالستیک و پهپاد را که ایران شلیک کرده بود، شناسایی کرده است.
سعود عبدالعزیز العطوان، سخنگوی این وزارتخانه، گفت: «از بامداد امروز، نیروهای مسلح ۱۳ موشک بالستیک متخاصم را در حریم هوایی کویت شناسایی و با آنها درگیر شدند. این موشک‌ها بر فراز چندین منطقه مسکونی رهگیری شدند که در نتیجه آن، بخشی از بقایای آنها سقوط کرد.»
او خبر داد نیروهای مسلح کویت ۱۷ پهپاد متخاصم را شناسایی و با آنها مقابله کردند و افزود: «این تجاوز شنیع ایران، تأسیسات غیرنظامی و حیاتی را هدف قرار داده بود.»
وزارت امور خارجه هند اعلام کرد که یکی از شهروندان این کشور در فرودگاه کویت کشته شده است و این حمله را محکوم کرد.
این وزارتخانه در بیانیه‌ای اعلام کرد: «ما بار دیگر از همه طرف‌ها می‌خواهیم که به چنین حملاتی علیه اهداف غیرنظامی پایان دهند.»
پیش‌تر، خبرگزاری دولتی کویت گزارش داده بود که حمله بامداد چهارشنبه به فرودگاه بین‌المللی این کشور چندین زخمی بر جا گذاشت، فعالیت فرودگاه را به حالت تعلیق درآورد و برخی پروازها به فرودگاه‌های دیگر هدایت شدند.
اداره کل هوانوردی غیرنظامی کویت هم اعلام کرد ساختمان ترمینال شماره یک فرودگاه در این حمله «به شدت آسیب دیده است».
شرکت هواپیمایی کویت نیز اعلام کرد پروازهای روز چهارشنبه خود را تغییر زمان‌بندی خواهد داد. با این حال، اداره هوانوردی غیرنظامی این کشور ساعاتی بعد خبر داد که پس از ارزیابی خسارت‌ها و اجرای تدابیر ایمنی، پروازهای شرکت هواپیمایی کویت از ترمینال شماره چهار از سر گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75897" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAyZL2a9rNXo8RJjsUfqP7FPZW2CpClftoiS-jKdi2j0NBzAZKxL1vyTMjChWLlM5npcMEzb0TA8YG1rhQMLudybd-gQk1txkqFsO6hKaUnCCHcBAu0cjHouv-jGorLdnsV4m279D3WSmjc_rY-yvv1Ef0Uu3McD4Nc_T4s3kXPPUWWWf5NgVhILbtp4K9FCjf5wB0X932MYGvYF-f73GqQX0qdHruKaEkfA4VIUT0Dsdp8MLbDtz7ultdoKYJpT7lGw5gJrtEWhEw_arBLpb-YOPuFzVJGtxK5xPChlrFwmh7aMqpNICwLWKollzsZIKQ6jCpCV8teWyTxb_MPZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان وابسته به دستگاه قضایی جمهوری اسلامی، از اجرای حکم اعدام فتح‌الله آوری، به اتهام قتل محمدجواد بخشیان، از نیروهای انتظامی در جریان اعتراضات دی ماه ۱۴۰۴ در همدان خبر داد.
خبرگزاری میزان مدعی است که در زمان دستگیری، «آلت قتاله (چاقو)، هودی مشکی و همچنین همان کتانی سفیدرنگی که در تصاویر دوربین‌های مداربسته محل حادثه مشاهده شده بود»، کشف شده است.
خبرگزاری میزان مدعی شد که آقای «آوری» دارای سوابقی چون «آدم‌ربایی»، «ضرب و جرح عمدی»، «تهدید با چاقو» و «شرکت در سرقت مقرون به آزار» بوده است.
اما خبرگزاری مهر در ۲۹ دی ماه ۱۴۰۴ و زمانی که خبر از دستگیری وی در غرب تهران داد،‌ او را «دارای سوابق کیفری و امنیتی» معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75896" target="_blank">📅 16:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/obv3_hrvLC6tj7-R8TzoJ9UuUOiMlbLT4-Ff7pH3HkmQ2e6o8w-398VI3-5T3VyTgPzGJBY08OtZm_I-mqiiEUym072me6YyyD5itWZoV8KMrFQSizXH6kf3GL0Wpk6Dh6JnjnCr69ndxKRAQr8hrQTE1HU0x2rgDtOwWJYb5rzKizqCWVvgF1LY2Zot-fjqpCQaenZQrtPLZgtu8311Ls94WF4eeiYiEyfsmvKAFa1smLI2h69OmmxFyaEHyrDBnX5OvNuhZ3TWGtr5mDRTGI78v3USIwFmwI2ZIZ_SMgV2HE2Y6qyYZR9nW_l7Wh1McIQTVqfGd1NbesDBOnSS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/obv3_hrvLC6tj7-R8TzoJ9UuUOiMlbLT4-Ff7pH3HkmQ2e6o8w-398VI3-5T3VyTgPzGJBY08OtZm_I-mqiiEUym072me6YyyD5itWZoV8KMrFQSizXH6kf3GL0Wpk6Dh6JnjnCr69ndxKRAQr8hrQTE1HU0x2rgDtOwWJYb5rzKizqCWVvgF1LY2Zot-fjqpCQaenZQrtPLZgtu8311Ls94WF4eeiYiEyfsmvKAFa1smLI2h69OmmxFyaEHyrDBnX5OvNuhZ3TWGtr5mDRTGI78v3USIwFmwI2ZIZ_SMgV2HE2Y6qyYZR9nW_l7Wh1McIQTVqfGd1NbesDBOnSS-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75894" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=DtO7vJTNEuxFIszW1rGKp6SEfunpYrqEoZLhBkj9LojHrQqIItzmBeN_wHqIDFusZz26l85j38Z3SecJPU5ARs4Z80QnpxYR_aWbULXPsXLkh8TqJZsbY20mUGUA5QYzEUmV9GahcOLxpDiBR6ygfiYyfE5fCYUc-Z1SHqOjeZRhBto7ouqYFv4Im6RJc8XEIvm4avJ-odi_LFoHBzPGWRZwPop_UaZ9UtOjzeyWfLBgqrNA-B-i1D4Hi4EYZj5IBf60rS1WZPImn0rozPGKw70xnND4nmCcfY67_uRDePHvKm1sy271JqivN36-nVZz-Xgl6WsodqBJQxkWGXDXBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=DtO7vJTNEuxFIszW1rGKp6SEfunpYrqEoZLhBkj9LojHrQqIItzmBeN_wHqIDFusZz26l85j38Z3SecJPU5ARs4Z80QnpxYR_aWbULXPsXLkh8TqJZsbY20mUGUA5QYzEUmV9GahcOLxpDiBR6ygfiYyfE5fCYUc-Z1SHqOjeZRhBto7ouqYFv4Im6RJc8XEIvm4avJ-odi_LFoHBzPGWRZwPop_UaZ9UtOjzeyWfLBgqrNA-B-i1D4Hi4EYZj5IBf60rS1WZPImn0rozPGKw70xnND4nmCcfY67_uRDePHvKm1sy271JqivN36-nVZz-Xgl6WsodqBJQxkWGXDXBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس"
خبرگزاری فارس و تسنیم با انتشار ویدیوهای بالا نوشتند:
سخنگوی سازمان آتش‌نشانی:
در ساعت ۶:۱۴ صبح امروز، وقوع یک مورد انفجار در جایگاه سوخت گاز واقع در بزرگراه یاسینی، مسیر غرب به شرق، بعد از سه‌راه تهرانپارس (نرسیده به پل ۱۲ فروردین) به سامانه ۱۲۵ اعلام شد. بلافاصله نیروهای دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند.
در بررسی‌های اولیه مشخص شد که یک دستگاه خودروی نیسان یخچال‌دار در حال سوخت‌گیری در این جایگاه بوده که به دلایل نامشخص و در حال بررسی، دچار انفجار شده است.
خوشبختانه این انفجار منجر به آتش‌سوزی نشده بود، اما شدت آن باعث وارد آمدن خسارات قابل‌توجهی به بدنه خودروی نیسان و بخش‌هایی از سقف و دیواره‌های جایگاه سوخت شده است.
در این حادثه دو نفر شامل راننده خودروی نیسان (حدوداً ۶۰ ساله) و یکی از متصدیان جایگاه (حدوداً ۴۰ ساله) دچار مصدومیت شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
شرق تهران
تهران نو صدای انفجار شنیده شد
وحید جان ۵:۵۸ صدای تک انفجار شمال شرق تهران، سنگین بود. مثل بمب بود
سمت شرق تهران یه تک صدا اومد ۵:۵۷ وحید جان
ساعت 5:56 تهران شرق یه صدایی مثل انفجار شنیدم دقیق نمیدونم
سلام، ساعت ۵:۵۷
شرق تهرانیم و انگار صدای انفجار از جنوب غربی بود
تهرانپارس صدای انفجار اومد ساعت۶صبح
منم صدای انفجار ساعت ۶ شرق تهران بیدارم کرد ولی چون ادامه نداشت فکر کردم اشتباه کردم تا پیام بقیه رو دیدم
سلام، ساکن شرق تهرانم، تهرانپارس- با صدای انفجار ساعت حدود ۵:۵۶ بیدار شدم اول فکر کردم توهم زدم، الان که پیغام‌های شما رو خوندم گویا بقیه هم شنیدن.
الان حدود ۵ دقیقه ممتد صدای آژیر میاد حالا آمبولانس یا آتش نشانی نمیدونم.
سلام، پردیس چهارشنبه ۱۳ خرداد ۶ صبح صدای مثل بمب اومد
وحید جان من تو نارمک صدای انفجار شنیدم ولی نزدیک نبود  ۵:۵۸
شرق تهران یه صدای خیلی بلند اومد ۵:۵۷
سلام تهرانپارس فلکه اول ساعت ۶ یک صداى انفجار بلند اومد و از  ساعت ۶:۱۹  تا ۶:۲۲ صداى آژیر ماشین هاى امبولانس و اتش نشانى میاد
آپدیت:
دلیل احتمالی انفجار در پست بعدی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6j62oTOdysnxNhK-D1zdzcrImKPOqD-iRQzC6APaViFciazlLdcOWYg5190PIjk878LBgJv4Ydj2S_f6DOiY-jEKUuwWmVtRF4kAN5xcXIgLXz0ZIsTeCL6zQcR4m1zt3LHzx3290kwBqF2vAO9R5h0ozBJibn6ZObrYr36ddLxgxyJJHJfSaQhZUyJ4Uhd2BqxFt38iygJDDiMTG7jZ2sntfK9a5w7t8ShfeKv_2TWvAH48YcokSu3wpaaim0IY_vJUImEfI0eq4rdh8eoz85oVzSMq7OSsJsYTk3_Pwyfdf5mncQiITqcm0tgVQjApk1nqsYrl7ILaGMQ3-YoXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست می‌نویسد، بر اساس گزارشی جدید، یک خلبان جنگنده «اف-۱۵ئی استرایک ایگل» نیروی هوایی آمریکا در جریان جنگ ایران در کمتر از یک ماه دو بار در کویت (آتش خودی) و ایران سرنگون شد، اما هر دو بار زنده ماند.
هویت این خلبان هرگز به‌طور علنی اعلام نشده است. مقام‌های کنونی و سابق نظامی به نشریه «های ساید ساب‌استک» گفتند که او یکی از دشوارترین پنج هفته‌های دوران خدمت یک خلبان نیروی هوایی آمریکا را از زمان جنگ ویتنام پشت سر گذاشته است.
به نوشته نیویورک‌پست، بدبیاری او از دوم مارس آغاز شد؛ زمانی که در یک حادثه آتش خودی در کویت، نیروهای دفاعی این کشور به اشتباه به سوی سه فروند جنگنده اف-۱۵ئی آمریکایی شلیک کردند.
در این حادثه، هر شش خدمه این سه جنگنده مجبور شدند با استفاده از صندلی پران از هواپیما خارج شوند و با چتر در خاک کویت فرود آیند. همه آن‌ها سالم نجات پیدا کردند.
با وجود این حادثه، به گفته پیت هگست، وزیر جنگ آمریکا، خلبانان تنها چهار هفته بعد دوباره به ماموریت بازگشتند و در عملیات بمباران اهدافی در تهران شرکت کردند؛ اقدامی که او آن را نشانه شجاعت و فداکاری این نیروها دانست.
نیویورک‌پست می‌نویسد، اما چند روز پس از آن ماموریت، بدشانسی بار دیگر به سراغ یکی از این خلبانان آمد. یک جنگنده اف-۱۵ئی بر فراز ایران هدف قرار گرفت و دو سرنشین آن در خاک ایران سقوط کردند.
این خلبان در سوم آوریل به‌سرعت نجات داده شد، اما افسر سامانه‌های تسلیحاتی همراه او زخمی شده بود و پس از آنکه ایران برای دستگیری او جایزه تعیین کرد، ناچار شد مخفی شود. او روز بعد در عملیاتی نجات پیدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QcqRGtpMk154LosI8O6rNVxStYghGKkxmqV_gnSd58NOQogfCVmRHPcs8XmmFCz5CRbXFvfJdxGt4zQsRwnLoXa18CgOWq-CQwiG-80nJ2PuU2n4QuOkH1n0AkBVwK8gGg5BThW40bC3U-ms6sdWjroF4QnPqmJMgyFtyO0Ii-3ebxdUCkZobo-jxxj7AQ7sUnt1hAMQRkmQYV5OxojxgeSnBfyDktQktxtBqSbDQOFJvimNqZ8sbuyiPmX_Vcf_hKKKJugG3EuZbLGzg6WTMi8loyaHzSPzpP5AQWcZyrfmQd-Y3Jz8nu6R9bLKEjkhwbkEvpM0THmmfFSKQqCvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا در شبکه‌های اجتماعی اعلام کرد که سپاه پاسداران مدعی شده که در حملات امروز با موشک و پهپاد به مقر ناوگان پنجم آمریکا در بحرین و یک پایگاه هوایی آمریکا در منطقه ضربه زده است.
سنتکام گفت این ادعا نادرست است و تمام حملات جمهوری اسلامی به نیروهای آمریکایی شکست خورد.
@
VahidHeadline
آپدیت:‌
سنتکام توییت دیگری هم منتشر کرد:
ستاد فرماندهی مرکزی آمریکا (سنتکام) دقایقی پیش اعلام کرد که «موج دیگری» از حملات پهپادی جمهوری اسلامی که نیروهای آمریکایی در کویت را هدف گرفته بود، ناکام ماند و پهپادها به اهدافی که داشتند برخورد نکردند.
سنتکام افزود پدافند هوایی ستاد فرماندهی مرکزی ایالات متحده «با موفقیت چندین پهپاد را سرنگون کرد. سنتکام گفت هیچ یک از پرسنل و یا تجهیزات آمریکا آسیبی ندیده است.
@
VahidHeadline
(مثل دو روز گذشته در این ساعت، ده‌ها پیام دیگر از تهران دریافت کردم درباره صدای عجیب پرواز هواپیما که منجر به بیدار شدن خیلی‌ها شد.)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RT74yDRytLxVB-z5USp4zHdaK_rBMLQ7U0_Hw5GS3ZeRJ_mUv3njCvzYneu9tfraY8dM1O3Qa3GOAAqpZUcr0AFK61vAiNbbEN1OKy4VdrniPrFoAypvzT6ldSwPBubajl45Ts0RP37IP6O-kK6H267jymibpAlskr7SlZjT1-nUGyHJTaf_LZQdqk5p_DnMYlrCFbBJo9nDRtZdd4nCJbZJZMpJw8hvPp414lAPgkgx-dkLCliIppNLKn3K72aLTOPwyD7rKFnYddjJeg1HulvQ2l1-37W46fFPQTxr3SXYptIv839rCMTrzmgmQ-TB7XrniJT6KTWZsF4Z187SKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام از حمله به جزیره قشم پس از دفع حملات موشکی جمهوری اسلامی خبر داد
ترجمه ماشین:
نیروهای آمریکا و شرکایش در برابر رفتار تهاجمی ایران دفاع کردند
تامپا، فلوریدا — نیروهای آمریکا در تاریخ ۲ ژوئن با موفقیت چندین موشک بالستیک و پهپاد ایرانی را منهدم کردند و در پاسخ به تلاش‌های ایران برای حمله در سراسر خاورمیانه، حملات دفاع از خود را در جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سوی همسایگان منطقه‌ای شلیک کرد؛ با این حال، هیچ‌کدام به اهداف مورد نظر خود اصابت نکردند.
دو موشک ایرانی که به سوی کویت شلیک شده بودند، پیش از رسیدن به هدف سقوط کردند یا در مسیر متلاشی شدند و سه موشکی که به سوی بحرین شلیک شده بودند، بلافاصله توسط نیروهای پدافند هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش از آن، نیروهای فرماندهی مرکزی آمریکا، سنتکام، سه پهپاد تهاجمی یک‌طرفه را که ایران به سوی دریانوردان غیرنظامی در حال عبور قانونی از آب‌های منطقه‌ای شلیک کرده بود، سرنگون کردند.
نیروهای آمریکایی همچنین حملات دفاع از خود را علیه یک ایستگاه کنترل زمینی نظامی ایران در جزیره قشم انجام دادند.
هیچ‌یک از نیروهای آمریکایی آسیبی ندیدند. نیروهای سنتکام در جریان آتش‌بس جاری، همچنان هوشیار و آماده دفاع در برابر تجاوز بی‌دلیل ایران هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m3I66OjnQOfjuvUVPoNUt55SQB7jfhDYnMrKkDd8wYCHNDfDbxcaCJErOkV_065kKMnEaSYpPU2z1dhexidCUoCCtikSDmYswPuHiZcipR16662h7j_GvidwUntPmT4MuCh2jr6cWAPzOIWLRiiJ9pPhai2NCjgYwfESekLxa-SInMtlOG7MGTRjG9H--mo1zmVABhvMBvuL49O2TqpTNLURpRPjIFyg1wrfRAAxzZOHk4cxGGEzfuUSoEKy3RRWtD9qC59tpbgnxRRQhVNe9G1N_onD-EOkPqeGIrDuTxKIGlS08eAVGWQgQ_5Q-3Kk0H1GWbvFlpeBmzx1jzarWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پس از مخابره گزارش‌های متعدد از حملات موشکی به نقاطی در کویت و بحرین، سپاه پاسداران با انتشار اطلاعیه‌ای رسما از حمله به پایگاه ناوگان پنجم نیروی دریایی آمریکا خبر داد.
@
VahidHeadline
بیانیه سپاه به نقل از منابع جمهوری اسلامی
"بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJXySQAtR9alGA1UVtK-Yfs5MhGNDqa_D40vPV-bZiENIzmUYd05hW_Mk9sIHLErPpkzE03btupYc-CqBW3Lgv5I8hrrZ4MoMCRIVo2Or0Xj37a6SvRTvLY0uV8vjURcGpmd1DShQcAGDFUNedewPRMb9AaJx_pBDgeIHuUzpPYpDmkJyfzUWXbW3ZwTzmE4YUuHqE6kJViKyrQqSS2WUk3079VUP4_vVeJbHtqkLjejv6Soyk5mieW_0LyALBxfBFQxq6el2JTn45dOZciNUTbtO9hUQZVYQokJIY9EJr4QvYgyW7Ok6Cn_RkxdkggxK_MyXB1wrTWgh8zvQ9B6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
عکس بالا: بندر کنگان دو تا موشک شلیک شد سمت کشور های عربی 2.19
ساعت ۲:۲۰ از جم بوشهر موشک زدن
درود همین الان از جم دو عدد موشک شلیک شد به سمت خلیج فارس
از جم ساعت ۲:۲۱
دو تا موشک پرتاب شد
از جم بوشهر هم دو تا زدن
همين الان
شلیک موشک از شهرک موشکی شهید چمران جم هم اکنون
ساعت ۲:۲۳ دقیقه صبح دو موشک همزمان
آپدیت: پرتاب سوم
سومی هم پرتاب شد
یکی دیگه هم همین الان شلیک شد
۲:۲۴ از جم یکی دیگه پرتاب شد
🔄
آپدیت:
وزارت کشور بحرین دقایقی قبل از به صدا در آمدن «آژیر خطر» خبر داد و از ساکنان این کشور خواست به نزدیکترین مکان امن بروند. این هشدار پس از آن است که کویت نیز اعلام کرد مشغول مقابله با حملات هوایی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bC3ic5pUZ5tJ1knNvSavQj2b4by4GbUVXXiWKt1wZ6Ih1uELnabPGkTVgWHAC7Kc12sP3mPjWxutyDcUjmSNdGrMs60lim-JxNaFTXcu9i6cYF1-LEMKeVGloxQXO4hNmXCr4c6V3eAyEGs7RUpfE6nPE3csiPKjBZ1o32ZTp31fFgHgB_5jwnKKCbuBo_wSdzhTD3EVvMnqigT5BFO08C6yenMUKNBeltuE5ck-hvr5Ssg7cD6eXrBd4Tz2ABLWN6Inki644bixc4yS85YOK5fh-4dwFrAY3lXO4a-xnSBVibD2wSbBb5OHQ7scRgBykOPcUp3NA9NV5XeOjn5F1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۲:۰۷ همین چند ثانیه پیش صدای پرتاب موشک از توی خود شهر داراب شنیده شد.
الان دوباره صدای پرتاب موشک اومد
وحید سلام
یکی دیگه هم الان زدن از داراب
۲ دقیقه پیش
۲ تای قبلی هم یکیش تو هوا ترکید
آپدیت: عکس بالا
و پیامی دیگر از کویت: دوباره صدای آژیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PQ7o2WFA9uWQyH_VRkZHmTQGQnQ8rxzSTSKizF0XVtMb1nwCQtXd6gcMpv1PCPcSecDkh2kluV8XIao6bd59JCsoAhRYU63s1PWxYoNXWRgnIaErB0hfKsEms8QJnJEfJgbWi9VWmQidxkdXBKtTK9z95fLCezhrqm-STA35SClXHdFD4sryyCY3JXwnlRKoBjOV-nf9KosCLDhktGvccCDsBcPvLCGSU5L3tglYeO_sewMoMk3gZTYWK0SFMouChobGxM0o0Ga-VjErjS1L7QsW1tOeNHP-KwqXDCin3UVwWJpQ6v9cgbCP4RotvcV63Jk4hd3EM6zpnUN1NH_hoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از داراب در استان فارس پیام‌هایی درباره شلیک موشک دریافت می‌کنم. هم‌زمان اسکرین‌شات‌هایی هم از کویت دریافت می‌کنم که میگن هشدار اعلام شده.
چهارشنبه ۱۳ خرداد
Vahid
ارتش کویت
اعلام کرد
سامانه‌های دفاعی این کشور در حال مقابله با حملات موشکی و پهپادی خصمانه هستند.
VahidOOnLine
ستاد کل نیروهای مسلح کویت با انتشار بیانیه‌ای فوری اعلام کرد که سیستم‌های پدافند هوایی این کشور، بامداد چهارشنبه، ۱۳ خردادماه، مشغول مقابله با حملات موشکی و پهپادهای متخاصم در آسمان کویت هستند. ارتش کویت در این اطلاعیه تاکید کرد که صدای انفجارهای شنیده‌شده در مناطق مختلف، ناشی از عملیات موفقیت‌آمیز سامانه‌های دفاع جوی در رهگیری و انهدام این «اهداف متخاصم» است. مقامات نظامی کویت از تمامی شهروندان و ساکنان این کشور خواسته‌اند تا آرامش خود را حفظ کرده و به طور کامل به دستورالعمل‌های امنیتی و ایمنی صادر شده از سوی مراجع مربوطه پایبند باشند.
@
VahidOOnLine
پیام‌های دریافتی که پیش از اخبار بالا نقل کرده بودم:
سلام همین الان ساعت ۱:۲۳ دقیقه دوتا موشک از داراب استان فارس پرتاب شد
یکیش حین رفتن ترکید
همین الان داراب صدای انفجار شدید اومد و شیشه ها لرزید
کل همسایه ها ریختن تو کوچه ببینن چه خبره
وحيد همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود
سلام آژیر در کویت
۵ انفجار بزرگ در کویت نسبت به روزهای قبل بیشتره
آپدیت:
ما بین فسا و داراب هستیم
یه صدای انفجار وحشتناک اومد ولی نفهمیدیم چیشده
من داراب هستم
ما عروسی بودیم تقریبا ساعت ۱.۴۰ دقیقه بود که یه صدای انفجار اومد و سقف سالن لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=JBgbU4KL3VxjJ8IFHBAtkzv5-7G3GYET7IGLfkUeMWSAJy9FwR1kXt-6x-rdy4fM7Hm3ISsi4if5iW0-WDlk8JKRuqumfPCHP-R5Ivb71kGKYsRooXm87lrAwefRgwf5v32GM2wSwcZI1mCjzn3seO7Je2dUm_PXe6mgwsttcg7fsfH9QGa3jbDsRKfHwrvKS7KoUdYRbmrdDOmxs2ROC1QYMHF9WLTe3TBZwmoUOBgk1IFr53Q09gelpqHAhWsbda3ojEoepYzIWea5U8xIAj456_JPco8OMd7xUkI7ppz009oxfrTxMeOVTmt9Ev_bGF7p3MK50A3oNLAcWGXlmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=JBgbU4KL3VxjJ8IFHBAtkzv5-7G3GYET7IGLfkUeMWSAJy9FwR1kXt-6x-rdy4fM7Hm3ISsi4if5iW0-WDlk8JKRuqumfPCHP-R5Ivb71kGKYsRooXm87lrAwefRgwf5v32GM2wSwcZI1mCjzn3seO7Je2dUm_PXe6mgwsttcg7fsfH9QGa3jbDsRKfHwrvKS7KoUdYRbmrdDOmxs2ROC1QYMHF9WLTe3TBZwmoUOBgk1IFr53Q09gelpqHAhWsbda3ojEoepYzIWea5U8xIAj456_JPco8OMd7xUkI7ppz009oxfrTxMeOVTmt9Ev_bGF7p3MK50A3oNLAcWGXlmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به یک کشتی دیگر شلیک کرد.
بیانه سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
فرماندهی مرکزی آمریکا، سنتکام، تدابیر محاصره را علیه نفتکش M/T Lexie با پرچم بوتسوانا اجرا کرد؛ این کشتی هنگام عبور از آب‌های بین‌المللی به سوی جزیره خارک در حرکت بود. خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از اجرای دستورهای نیروهای آمریکایی سر باز زدند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک هل‌فایر به موتورخانه کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
سنتکام از ۱۳ آوریل اجرای محاصره همه رفت‌وآمدهای دریایی به بنادر ایران و خروج از آن‌ها را آغاز کرده است. با ادامه آتش‌بس با ایران، نیروهای آمریکا تاکنون شش کشتی تجاری را از کار انداخته و مسیر ۱۲۲ کشتی را تغییر داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKSWYHtYKrm7CbVG4eTUHYzQF3Zw62jUHDxMA69HBBeo5P-t9t6vcvVeSFWq1vqOIAhmG286rSUQicxpHgKDnnS4A6Sy8Q_xBsY14mDZIVwlE-jnuC3DaGYiExPQLp2ss9pajyi-_jhPHdSnvbH9inEC5W8RB4dXGgwgu023uvyO9HeQSyYZO04WNJ9q8cMEmmkbCY5eaWrmNfolfIzUqilqqkTyb039V6ky4G_7bh0v4ghopRLWm3dqtKS9qMiqRW3R286VcGbpL1Eyz5tYpq18c7BeBTSOFEBBoN_RdSHnCiVAoI7rD1iD_OAUcZlflqQulqmQ2HtxWVjAJuuQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLtOVCQyFZJAaCIdNYiPsj7-Cfy4YBss25HvHtBUUfYU7DcQwtkeT5ylByrrbLE6jUub4DkU_lVAKA3B9gaEAFy_GjeS10x3OQZJTK9UQLJNKw5VtM1ZnCVQb-dw0UgdFHnz_IGkGHydSMNGPyXcsaLPWJgsWO86VmqXQ_rrdtbg4UbYM5FPxtCOEkn8ZhHZU9TYZRlIoI_-u09TwiH3c8pw2E4T1mgUcGLVpB94OjR9I8ewgXR37pQL6XfPtgFN4BQsqzGcjRfuOOu-Br0qyI9kDXXy3JEzud6qnaEGFOPclWL5-ewDDJJ_B6Ufk1rsvaKIEfpgPp82HZxGnWe8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BLctvQKA_5n97Tuyb_M1HgDpEW1e7wwrf-AlHaIq9mNKEsSZV84U_ONfcbCKkH0cQtAHKR_xIWO34oiY7L9drO4CGGZQkjn-A1m0YF0I8ZuM3F99nKzBmiRIUXIeIWDk27AUQ8552ALzJXE2v7li7653K82yrNPVwQp5KomUlsZzxc3vLry19VIFBT187XitXRLKbHQDF7JgYbGetOSpQVvyhdwQrfLA_Cnr4_ktHN38iVQFUOZ1HbFJtqc6zYgknYJ-eqQ0-Y5cu0e8SUyHdEnq5kzGaKsthLlDRhFWMym_pqUyMo3rPhKK9sjVSPRiCFJ1f6tmq58EmyBhKMqMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/joXn5sWXLXiScyRnw4H62v2l1Kszlv4uqrvrswRoOmIgVZkvqTdNASwg2FX0_pd2UdPdKakTZ1Luh_AyWLwqm2AXIXakuteFEhK3qKoP8z-XjfzkxZblFlRez6soyJvvr16oKSddH59Ad7ZxNtBgTNCSqxsXoc_CBXyFbhRM6on4wejGvrBsXaktCo3cq6mjsv7Ca3bK_Atyrt3kQrgIZOT9OO3gZHQ1e-K88jgoMONAjDJdoGOUjCyzx9VPNcUdDQTpvnlUpvFQhysJqE5ssOpgbcFonf_Vr9Hq2eMJok6ana4YJ_WWPRJRg8cOdz-JUEFbB-VPIEZW2esSvihQxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو در جلسه کمیته روابط خارجی سنا گفت: «چیزی به نام نیروی دریایی جمهوری اسلامی وجود ندارد. آنچه باقی مانده تعدادی قایق کوچک است که روی آن‌ها مسلسل نصب شده و نیروی دریایی واقعی در کف اقیانوس قرار دارد.»
او افزود: جمهوری اسلامی همچنان تعداد زیادی پهپاد در اختیار دارد. توان بازدارندگی متعارف تهران به‌طور قابل توجهی تضعیف شده است.
@
VahidOOnLine
وزیر امور خارجه ایالات متحده در جلسه استماع سنا تاکید کرد که شرط اول آمریکا برای مذاکره با جمهوری اسلامی، بازگشایی کامل و بدون قید و شرط تنگه هرمز است.
او در ادامه تاکید کرد که منظور از بازگشایی، بازگشت شرایط به پیش از جنگ و عبور و مرور آزاد تمام کشتی‌ها از این آبراه راهبردی، بدون محدودیت و مانند سایر آبراه‌های جهان است.
@
VahidOOnLine
او گفت باز کردن تنگه هرمز شرط اول آمریکاست اما صرف این کار باعث برداشته شدن تحریم‌ها نخواهد شد و رفع تحریم منوط به شرایطی خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW6JSWowZ5a-LZq1PLpDC50G3IuEiL1wDujhpgHTMCkrT_aRgSukZ5X209AenSmTWodgWbpHd7f2-ICwK1w2h3PyTiieXxBY_zV9d5y-Fey15phwJerqRKX2Ffo70d8Sod3dhth_4edvxeahWpvc5hyzFk7elQSiucMCqZcCQ4VyzK7bw4SpVPtBQTA74sg-rRLPHbcUImaVir4P9FMQ2RVz_darr08qxc003nViZ89pZkB14rDNtuPJHD3JjIu8Mkmyi_1w_FQBBsZ5OWWTl0qBI2FI1MEy-3BvU4F0abdKitC-dmbLyLAf9dGlnOHYmsnhV0FpuZv_irQxphE7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5EnKwpyMXPOlr6l3SXT2IRjm2JRVdLDL48PW_swxxV_FTKwu_OW8MQyiDs_EgyaR5kYKDfkDpUpKzjRos7vioWCLKQWmOgtyBI_VvOL1yOlNr4lf0B6GOu237yIZ4ZERdXQYguFmeu0BpBHAwTugdS1jA0dG5CkEHDcx9cPJd-onWn-VTOsTsiYxHKQj3o7F6cwPRpTugrH3wBbE0-QWEhpEoramb4hhoyJPIySk9xi-BoxfNNB0dzSPQmWYimuUye--Wvej7yAxUK6zaX-ffGmfuaZ62876tNpIQJjg_iegr2ZBXHRkuCVuwLEr0iXEG-pJGyoT7cgGE1pQa6IDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که جمهوری اسلامی در حال دستیابی به سلاح هسته‌ای بود و اگر عملیات خشم حماسی صورت نمی‌گرفت دیر می‌شد.
آقای روبیو با یادآوری این که توانایی نظامی جمهوری اسلامی به شدت تضعیف شده، افزود که جمهوری اسلامی ایران برای اولین بار در تاریخ، بسیاری از شرایط مدنظر آمریکا برای رسیدن به توافق را پذیرفته است.
به گفته او شکاف در ساختار قدرت سیاسی جمهوری اسلامی و زمان طولانی رسیدن پیام‌ها مذاکرات را طولانی کرده است. اما طبعا اگر مذاکرات به هدف دلخواه آمریکا نرسد، ایالات متحده گزینه‌های دیگری را درپیش خواهد گرفت.
@
VahidHeadline
پیش‌تر ‌خبرگزاری فارس، وابسته به سپاه، به نقل از یک منبع آگاه نوشت که تبادل پیام بین جمهوری اسلامی و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشینگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fpgCFwCEPCIZUCPreTSRZBD_XnW66bzp_DIouLEEs9VtbfPbem_qdykJuvwh9W18gbc8vDKfAxON3u24pzoriNUP9qbdQiGkV48A-oitTXdtN7o4jG5XFSE592DFUkJk85NWjJ1QFehSTG7Qb0bklxi5egjS68hdZcgKa2iDWk9vYbNhYBPmlqpyrznglX8tP3N-5r9IqTdoFEq6YJoLHOwhX9bkG2nROMFM6-uAzm_roeNA-Bt8kiXK1RHPiXeOxVYb77En3Sn3y-nYbrcxMai4zxyyK42h9Lk33omMuW3axx913xJ22G8QrdfnKAprSrnecs1iHUT1Ll1QK477pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=a9hvLLJhXlgHtg_N0Qrl1aINUPnL4TUQMzYZV-ly8ZDguBc0CYu93YcWEFktCzRLyFe0ASsybK3B4qVneIhbtfrKLcQuCtcrWcwZia8May4abgamPqpwArh2lhN-lwHCH0u2ilAIqO3K4oduELaqv4pqpukeH3KO0aHIEapMxZedSWIot_On1oWySxYARpY1rqaywhHOAdiwMKf5WQgT2adosD9lfUVmcZ3ZUyr0BuQmD-dbzCwADlXpKWzrI8muvxSYJ54sDemWcNnW0eLoqtBHKx2Mz2mXa9BYxrvmOYZ-WWy9rONLurWCanTbwqo3wRrF0vub4XiVXekOxGEYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=a9hvLLJhXlgHtg_N0Qrl1aINUPnL4TUQMzYZV-ly8ZDguBc0CYu93YcWEFktCzRLyFe0ASsybK3B4qVneIhbtfrKLcQuCtcrWcwZia8May4abgamPqpwArh2lhN-lwHCH0u2ilAIqO3K4oduELaqv4pqpukeH3KO0aHIEapMxZedSWIot_On1oWySxYARpY1rqaywhHOAdiwMKf5WQgT2adosD9lfUVmcZ3ZUyr0BuQmD-dbzCwADlXpKWzrI8muvxSYJ54sDemWcNnW0eLoqtBHKx2Mz2mXa9BYxrvmOYZ-WWy9rONLurWCanTbwqo3wRrF0vub4XiVXekOxGEYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هما میرافشار، شاعر و ترانه‌سرای نامدار ایرانی، در ۸۹ سالگی در لس‌آنجلس درگذشت.
مرتضی برجسته اشراقی، با نام هنری مرتضی، سه‌شنبه ۱۲ خرداد، در اینستاگرام نوشت که خانم افشار هفته گذشته چشم از جهان فروبست، اما خانوادهٔ او با تأخیر این خبر را منتشر کردند.
این شاعر و ترانه‌سرا، که بر اساس گزارش‌ها، سال‌ها با بیماری آلزایمر دست‌و‌پنجه نرم می‌کرد، از پُرکارترین و محبوب‌ترین ترانه‌سرایان قبل و بعد از انقلاب ۱۳۵۷ بود.
هما افشار با بسیاری از خوانندگان برجسته ایرانی از جمله حمیرا، هایده، مهستی، ستار، ابی، داریوش، معین و عارف همکاری داشت.
او در سال ۱۳۱۵ در تهران متولد شد و در جوانی با علی میرافشار، پسرعموی حمیرا، ازدواج کرد. این پیوند، دوستی نزدیکی بین هما و حمیرا ایجاد کرد که به گفته خود او، جرقهٔ تولید بسیاری از ترانه‌ها و همکاری‌های این دو با هم شد.
@
VahidHeadline
هما میرافشار، روزنامه‌نگار، شاعر و ترانه‌سرای تصنیف‌های عاشقانه موسیقی دستگاهی و آثار به یادماندنی پاپ، در ۸۹ سالگی درگذشت؛ چهره‌های نامدار موسیقی و علاقه‌مندانش در شبکه‌های اجتماعی از مقام هنری او تجلیل کردند.
او در سه مجموعه شعری بیش از هزار سروده دارد که افزون بر ۲۵۰ شعرش در زمره ماندگارترین ترانه‌های ایرانی است و بی‌دلیل نیست که در جامعه موسیقی به «زن هزار ترانه» و یا «ملکه ترانه‌سرایی ایران» معروف شد. از همین روست که ایرج جنتی عطایی، ترانه‌سرای برجسته معاصر، هما میرافشار را پیشکسوت خود می‌‌داند که «پیش از ترانه نو و در کنار آن شهره بود.»
هما پیشگام سرودن اشعاری بود که یک زن برای معشوق می‌خواند و یا حرف‌های عاشقانه‌ یک مرد برای دلبرش، چرا که تصنیف‌سرایان آن دوران به جنسیت ترانه‌ها کمتر می‌پرداختند. او سال‌ها پیش در برنامه «یک‌ حرف و دو حرف» رادیو بی‌بی‌سی به زنده‌یاد محمود خوشنام، پژوهشگر موسیقی، در این باره گفت: «منیر طاها، سیمین بهبهانی یا لعبت والا که کار می‌کردند، من ندیدم که ترانه‌هایشان بوی زنانه بدهد مگر این که از زبان مرد بیرون آمده باشد. اگر خواننده آنها مرد بوده به ناچار باید چیزی را می‌نوشتند که یک مرد به یک زن بگوید.»
«یادم می‌آید که یکی از من پرسید که شما این حالت را چگونه می‌نویسید و من در پاسخ گفتم اگر بخواهم از زبان مرد شعر بگویم، مشتاق شنیدن همان‌هایی هستم که دوست دارم از او بشنوم. آن حرف‌ها را می‌گذاردم در کلام و اکبر گلپا می‌خواند، یا می‌دادم به محمودی خوانساری می‎‌خواند اما گاه طوری می‌نوشتم که مرد یا زن هر کدام بخوانند فرقی نکند.»
....
در ابتدای دهه پنجاه بود که اشعار هما میرافشار و ملودی‌های زیبای محمد حیدری در صدر جدول بهترین‌ ترانه‌ها قرار گرفت و نام هما درخشید؛ مثل ترانه «دیوونتم» با اجرای حمیرا: «بذار بگم دیوونه‏‌تم...آره دیوونه‏‌تم من...نشکن منو به سنگ غم... چراغ خونه‌تم من...» یا ترانه «دلم می‌خواد» با اجرای هایده: «دلم می‏‌خواد که روزی صدهزار بار... بهت بگم دوست دارم عزیزم...» و یا ترانه «میکده» با صدای اکبر گلپایگانی: «هوس میکده داره دل دیوونه‏‌ی من، نمی‌‏دونه بی‏‌تو ایام بهارو چه کنه...»
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdNAkztE7f1nS9ZdctkxTHLyChK6ufHySprY5gFB0S5rGnFzoLHYuZqLHUWrIdJohLyNN3aPINGB34cVUs3W2yJZLVc3yEtfrgk_LpwbVcbbS1xogvS2ZE4kjASj_vsARDfZj2DRrh3KjbPIZ9QcPkcrmuLRyEs-kNX6mnhSR_ebbw7u6VkRt-980UQR38AXylY6EvDRFweTe76Jp6wIGidB63Zqh1Sl1a4XPqpDQRgqph3SBcIYtaOSkk9WpXVGJAZ0qy2S-3z7dgXmtmLHQBNm9LI_19iE_l1X3F0ef2XD5xLEZoW8ewesdXP3gBupKp3pg5o5YzmXKnBf2AKXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBkPsOTv2fPrp1cs2Q9isTfz09lES-IHJGQwWxjK7K1BP0N5MgHwJvon2SfNln9kOQV5YvMykO03QW1GPQR__zRh4V6fADApD3UzOwpMNFUtrfI_4RjX_oaEv_ALanXfq3ZVSBP0RSD4BzWv3Wm25_6FVqGq54RjbBEtyEC9OY86KDSFIyIjdcx4BIva0NsHPe_s0APCAwky7jPLTXz1ExaM-ldPuK_o2CHOI3W8nouiBqZYhG5djuedFsBxqpoCplkJtZZ_uzDJndp3ABNhCFY2M4_aYVlv9XmCfXc1B5k-NQOALBEC79htEsTOfnXjKlS0lEsCpfJmspi4M2F31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام شهرداری تهران می‌گوید که برگزاری «مراسم بدرقه» و تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، در شهرهای قم، مشهد و تهران «قطعی شده است».
به گزارش رسانه‌های ایران، محمدامین توکلی‌زاده معاون اجتماعی شهرداری تهران روز سه‌شنبه ۱۲ خرداد گفت که این نهاد «در حال تدارک برای حضور جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در تهران هستیم».
او به زمان دقیق برگزاری این مراسم اشاره نکرد ولی گفت که احتمالا در پایان ذی‌الحجه و اوایل محرم برگزار شود.
این زمان تقریبا مصادف با اواخر خرداد و اوایل تیرماه است.
علی خامنه‌ای از ۹ اسفند پارسال که در حملات مشترک آمریکا و اسرائیل کشته شد، هنوز دفن نشده است.
معاون اجتماعی شهرداری تهران در ادامه گفت که «مراسم بدرقه» سه روز در نظر گرفته شده و در تهران قرار است ۲۴ ساعت طول بکشد.
به گفته توکلی‌زاده، محل دفن خامنه‌ای «طبق وصیت ایشان و توصیه‌های نزدیکان‌شان» در حرم امام هشتم شیعیان تعیین شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFch8wTQNJRRx3C6bTRpEhUdUhhSM4KjktS89BuLHw8SZ6qwNvbawEfhOQ85o1iIoOvDcv-vEpnblTnQV14l269vY87P56Zt9PLiY2tvpvsHzE54Nt41YG0ZXonmdKOUqeXao1i8hMWW4yi2xh1b0jQLSYUOUxKU_CctPyBLIw_BuMg078_-tpsqGqUPUGF0sCMFX_ZbJgi6D0XSIsiRuI-ZFbS0IxZYnPl3srEOPT814XvDSVQk1_Vf4Xdy1VwnEu3X96HgoKPJfLP0WmQXHagBnz-_-mZXquNgFkX4qms8UOwfdL_fI_lfSrJx5iyHomyU0EgL-JSdpb4bM0G2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از چند روز تاخیر، بانک مرکزی و مرکز آمار ایران به‌طور همزمان گزارش‌های تورمی اردیبهشت‌ماه را منتشر کردند؛ گزارش‌هایی که با وجود تفاوت در ارقام، از تداوم روند صعودی قیمت‌ها و افزایش فشار معیشتی بر خانوارها حکایت دارد.
مرکز آمار ایران تورم ماهانه خانوارهای کشور را ۸.۸ درصد، تورم نقطه‌به‌نقطه را ۸۳.۹ درصد و تورم سالانه را ۵۷.۷ درصد اعلام کرد.
همزمان بانک مرکزی با تمرکز بر مناطق شهری، تورم ماهانه را ۸.۵ درصد، تورم نقطه‌ای را ۷۷.۲ درصد و تورم سالانه را ۵۳.۹ درصد برآورد کرد.
بر اساس گزارش بانک مرکزی، شاخص کالاها در اردیبهشت‌ماه نسبت به ماه قبل ۱۰ درصد و نسبت به مدت مشابه سال گذشته ۱۱۳.۸ درصد افزایش یافته است؛ آماری که از رشد شدید هزینه خرید اقلام روزمره حکایت دارد.
اختلاف ارقام منتشر شده از سوی دو نهاد آماری به تفاوت در جامعه آماری، سال پایه، شیوه نمونه‌گیری و وزن‌دهی کالاها و خدمات بازمی‌گردد. مرکز آمار کل خانوارهای شهری و روستایی را مبنا قرار می‌دهد، در حالی که بانک مرکزی تنها مناطق شهری را بررسی می‌کند.
مقایسه آمارها با ماه‌های گذشته نیز از شتاب گرفتن روند تورمی خبر می‌دهد. تورم نقطه‌به‌نقطه که در فروردین‌ماه ۷۳.۵ درصد اعلام شده بود، در اردیبهشت به ۸۳.۹ درصد رسید؛ افزایشی بیش از ۱۰ واحد درصدی تنها در یک ماه.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=SnXtZVvyQuzt7viEvtuhWXxOFvHpBjGJm68pI23DIMvwD_QZ4PzRJzdjGmrdSab7e4DdQuPnQUBXAdlUZIZways9zwqmu3tBjwEx4G9p7URghB4oiE_tbCE006sSTIFPflLML4t9XQj7dS6aIomFhKCazHbX2QqzJ08mp0ScmY8_kIge-6dfJgTLS5ipH991a47oeEsJVCy80Zb1WstFurlPEYyPBC9M5TY-yqNXwNf6cfNlzTP8RPVWRwqn92EXxd8CiHZ2yPuFUwXGJon1R8XPngBcG5goz_XjaYx9rtQwjGYz5Rfe-r1OxxrpQW8_4vYtdqy178q6gLbpXAvlkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=SnXtZVvyQuzt7viEvtuhWXxOFvHpBjGJm68pI23DIMvwD_QZ4PzRJzdjGmrdSab7e4DdQuPnQUBXAdlUZIZways9zwqmu3tBjwEx4G9p7URghB4oiE_tbCE006sSTIFPflLML4t9XQj7dS6aIomFhKCazHbX2QqzJ08mp0ScmY8_kIge-6dfJgTLS5ipH991a47oeEsJVCy80Zb1WstFurlPEYyPBC9M5TY-yqNXwNf6cfNlzTP8RPVWRwqn92EXxd8CiHZ2yPuFUwXGJon1R8XPngBcG5goz_XjaYx9rtQwjGYz5Rfe-r1OxxrpQW8_4vYtdqy178q6gLbpXAvlkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYsKzzzYOwHxhTl4GzkpJldOjJvwCOwv8sz7sX1QCEKAM0kScaLs2S1Joo2WJIRTULOy8XUqCri_f1k8QXiooVmXjAnu4qAA510Cf3uENldtzWW1uNclnXeDW3hBrdPZ2UtUSeRYHD37hMgWArOaGGkWNkqDcSaFyXFWNWStV9EewO4-j0hN7BUC-ux47oaw3D4byHBXjBQvEPG4sWLM0dj4XwbUIyIoWYHt0FkgmPVmPQ9QBH37zYdxdaZn1YWzIQC9NYlK057vraJ7xADeCl9j5diG4p-JX3E7f99oGXwrUqOi8KQm7o0bZ6z4ybTaXIpvV-w8r_bcqu4HKVOG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q4YWWBk-H3j6dczYY7HX-TcdrrQDNQ-wq2X4x5DNClz-iQXo-PrJ0peBie3HSVZXbO4pc-YLnGJEPmCEbj-jO0E8cNvEW4joPlUyb8yloLlZjLQOEZj2yVwjveh6bVuBY1K-gn12lfWnaESpP69cFz4CjGmkdHssyq473BoG0ClCpu6D5U8XGF7PsgQBdUab9NYj0GWX5gSrmuZM7FLz-oKh-_fDtLz10qy9TWARVb8D660q6va9MjH32bj-rS609PZDIV2Qgh6lahG8GG35QSLYZi1EOfvzU3xtEcLOjJdrCM23dRgH0ZA2ILnpSXFqVfgRVghkzA7aIPjD2JjJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jKJcHnVKMJffT3dVeCwcas_eX5xnhx1l7CL1QpcOT1ZhFac5yiHHgmIvPmuJr1INR9wmJlliLscSPNvbu7CzRiD3oPlp0jXCTsOUG-8aHTfPw_gdcu6WGKJxGSO0xpHvP6JmldRH3LwM1f1RUUkX5dlEdp-ujdYqRqMg3j4UA_V5_MNRdiyUmB6XamwVVFh5mCkSgBDFA02tAuG1CAVc-jLmJXSjg6kw8NivQcPXT82p9btAOiNyp3hU_YVdbSbLR5EmftnmNshwmdfpnHoKFeg61VaMRbNG_SaiU-VgpmeeNj2nT4_K5b0A1uDqhSynRtAhmgOkF3z-sje4kntLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCQOvSQbYcgK0jOdLIa7aHb9x4onN7PwyvGsiIgwV8af-ypZVaj4wuRzwWr-2kZgBN3wtz9R0_0HpfeQOgNeJe-woDp1QLK1EB-sjjAA4svsQM-FqU49Z-hZep99AUv0ABiUapPkhVNh1T3zVyAjjM9y_K2ZuCRwd_9wJaiLc_r2nYOXrdZwGSIKMlDkrIgJ8aNArMm3vENdY3ZI8N3jHjVWguqp_hbRqHq1qZX_8k2milDgQ0KaVhTu6TebaZTNkBASpN7AwsVY67aoj6Ek-RVDY-aRyHGTYg5JJBHHtsWQAO5KkL8eovFqXoePOWtnVSpwLB68B5vW2hxpq_2KUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=B8310OeuJCfajkl97hPLEwNjWLWthkNRFAILVWGbLFyoSrY0MnzJmdA4hu577rKkDPQep_o_vyoUunjpwIx10Lj371_4vVIvGuwOj-QcVReSGP7gz29x03aOyGJ36J9OC3KA1HkMbQIeALClUzz3H_-pHgRyEsw8wu-_hQbAqLNpiVdi52K6Xme8XA1hzCT36juMmhGrNKhYt5FthcPvSyQhhayej6nGQE7QKB97AuSAWZ2m3nh0zUi6nM78SGykLgXwpjrXl1uAdIBoJHcB0EDJRlEgr67ZmZ7ykHuJky9cZZ9JPQ2ImcG7m1ccoxqbjbIOZ0Ltynj_KR8kHrp-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=B8310OeuJCfajkl97hPLEwNjWLWthkNRFAILVWGbLFyoSrY0MnzJmdA4hu577rKkDPQep_o_vyoUunjpwIx10Lj371_4vVIvGuwOj-QcVReSGP7gz29x03aOyGJ36J9OC3KA1HkMbQIeALClUzz3H_-pHgRyEsw8wu-_hQbAqLNpiVdi52K6Xme8XA1hzCT36juMmhGrNKhYt5FthcPvSyQhhayej6nGQE7QKB97AuSAWZ2m3nh0zUi6nM78SGykLgXwpjrXl1uAdIBoJHcB0EDJRlEgr67ZmZ7ykHuJky9cZZ9JPQ2ImcG7m1ccoxqbjbIOZ0Ltynj_KR8kHrp-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qjupaNMYHiu5hAx1_tiaEv84jM8vlmt6__H47M1WbXHQ1-9ijBH6T7fS8zscHJb8eLLX-KAlwx_HWRI4AwUgoauBm9BDC5jljh16BC_qkYLmXX7PJhMLiqcaNuo_19-qdfQnhoJLg7h8g-SsdXOWLF04yeXgL3xCc7mbq2ka6b-L2JuAYMhf2jTVzWphcudv6vfx1whqR5_1FW4U_Z9jVKU2ADUqk4oVr7YEMaGVd-dx6AutlzBIoPgh9MshC0WyTG57mxyAdIspn-6nCrhcyXRsR6hD3Ad0Kkyi3iaSQkAQXJ5hqv4UYsVSSjkBL05VPtfm485lGY-3sPcEEuMgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
