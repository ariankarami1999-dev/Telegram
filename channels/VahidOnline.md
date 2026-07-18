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
<img src="https://cdn1.telesco.pe/file/SSquBBTvUw04d-InRJUInoMvpM4GugKAXU-IbJ7rdmO4TkbrbAEIGbuDVzG-hbfzELZUSk1jjkY4lLvL4fimzF9Erb42y4VAAGYYMQ5ikZUA8QT3TjyfLEhiw1NG4c_mMmKrYDjoSVzBbcABfU5g6RZ3uAqwh2nBkoPihwNJK2nCiDotuCixHjLsy7BC5J_imme9Oj_R3l15zMVYNHns7BSU_PBYqLBTTNfmwPTj5ZRXBFEuTCrkMq741sXifq3H0kjDG11DkTUBEgrU3hzgu2vd7GIsrZDnPHcyRHvjz6G6c0A9ELtw2OKjjoe6U3qcoRvhhbauyQ5v1py9PL_myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 12:13:28</div>
<hr>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWH6__kCB1eihD6VP0ErOsDYglCr2fXz-0ArmbkOb-gPiIqtrHZtq9iqsC7hzJ2dVUjomXzY2EwsEwUA7tFVugO24el-uOxgK8Gh8oUtRNx3KRaDh_8Qr8j6PI9APSJYED4XmcwUhWtoBmVRyMdA6k1O6a_N-NUhhAJTqP6tFdRqDWiUyfbn5o8qo96m0Jl879CKHLVLWpgfg3VfHyvDSxOABVNv7CsGv0Ib3hn16Q-a4ZAtFXZmilB_UoTiYgsQvpKX5YVWz23IkrzKTSX0gWgOaUBp4aCjpIW-j8OSLqIy8YKDetjDVtuSNaMSMnRePfcNdI-xeT_AoB3O1oFp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: پرتاب چند موشک از استان بوشهر
شنبه ۲۷ تیر حدود ساعت ۶:۳۵
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77230" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=eLf7dJTWUXYfe2vTsMZ7P9vyYXptHHyNpy_B2aeU26O9yVryigDWcR30-C6JbnXdlL3715s2YTGG5ddyyf0lOwsS1XuMQKTotuMF9RtpMVHs37tgo8v8YObNjAbDX-RAdr67vjYcBTHMn6HOLzMZTIpE2BJCtogiV3wsUVDquP7DcdEXDSbrbneM55kEFqfEliHVyzsssJw65_J5x7krl027k_g8A4Pfi1TpWgZ8eq17zgXPZYIGLZYr7--sF3BjBf-yIJnuKUQ8YJDb-eaRt5mMBF_ujVKFUlAFWnTCl1ff9xn5cMdqRCBH8nA-E6oXakrikgtuOxWrzKgGXNxm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=eLf7dJTWUXYfe2vTsMZ7P9vyYXptHHyNpy_B2aeU26O9yVryigDWcR30-C6JbnXdlL3715s2YTGG5ddyyf0lOwsS1XuMQKTotuMF9RtpMVHs37tgo8v8YObNjAbDX-RAdr67vjYcBTHMn6HOLzMZTIpE2BJCtogiV3wsUVDquP7DcdEXDSbrbneM55kEFqfEliHVyzsssJw65_J5x7krl027k_g8A4Pfi1TpWgZ8eq17zgXPZYIGLZYr7--sF3BjBf-yIJnuKUQ8YJDb-eaRt5mMBF_ujVKFUlAFWnTCl1ff9xn5cMdqRCBH8nA-E6oXakrikgtuOxWrzKgGXNxm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم با انتشار ویدیویی از محل حادثه گزارش داده است که دو پل در محور بندرعباس–رودان هدف حمله آمریکا قرار گرفته و این مسیر آسیب دیده است.
این خبرگزاری می‌گوید که در این حمله شماری کشته و تعدادی نیز زخمی شده‌اند، اما آمار دقیق تلفات و میزان خسارت هنوز اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77229" target="_blank">📅 06:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VMK2i0vN1xItybqYc_SLuWVvbesiUni8YvFnqpfOt_-zFu1bOJU_kIwO6734nYV9lqNrV0_R8lEwv_mnQc-OmGgfZiZNI6cvlNQyYohxLUgm3UZEfoiGVPaBKebPt8V-euOqMfbtPeYUzfGGdUSpFaM-L_TB_M9yhk71knixoE8VnfWpPeJp35EZPBa7YhALtQxlClZMxjR_IL3jqeJwYFlwkKUb9HuRyCT21wy4oU0-BIQ3TkNVyun7KIFIs0Dzb3YOZRdvROWvzMlCaBIlDVcaneHVU9p2OapzFzNYgJUfU7t_QiJnXk4YD7qcX-Q-zLKN60ekIzGVMBfnORIixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت: نقشه «راه‌های مسدودشده» در نزدیکی تنگه هرمز
شامل دو پل و خروجی تونلی که در حملات هوایی امشب آمریکا هدف قرار گرفتند.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77228" target="_blank">📅 06:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=WftB8Nw3CFWXSoeK8x117yHR8HS_vOHzl8e2JY10BR9Beqw5O1xdM0dh2KO_yGITX3i2wBP4SbO9VbgJMSrCWXM-y9IOY2Uc1jBC76ZDo3PN6pg9bCsyLQTlv8YZO04GosZeUo5ycu-SjIYv3LIUSnmAAoHiivCiTxHkhpjwUwhHlsej-5D-O2IjEdFLITTxZ7Au1JLMj6wEat_3F0gUJn2vu0GHAvQ4gneMgIORUSL_KPIepUahVdzATRrM-nBGaSy9RoKYwl_akorX18UvFaWUNx02W7RttiJ7IupdO-CgdzVrwlFl2VajV_98fwG2A3fNYxUgOvjpYDFL3HfuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=WftB8Nw3CFWXSoeK8x117yHR8HS_vOHzl8e2JY10BR9Beqw5O1xdM0dh2KO_yGITX3i2wBP4SbO9VbgJMSrCWXM-y9IOY2Uc1jBC76ZDo3PN6pg9bCsyLQTlv8YZO04GosZeUo5ycu-SjIYv3LIUSnmAAoHiivCiTxHkhpjwUwhHlsej-5D-O2IjEdFLITTxZ7Au1JLMj6wEat_3F0gUJn2vu0GHAvQ4gneMgIORUSL_KPIepUahVdzATRrM-nBGaSy9RoKYwl_akorX18UvFaWUNx02W7RttiJ7IupdO-CgdzVrwlFl2VajV_98fwG2A3fNYxUgOvjpYDFL3HfuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین موج حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا [۵ صبح به وقت تهران]، به هفتمین شب متوالی حملات علیه ایران پایان دادند.
فرماندهی مرکزی ایالات متحده (سنتکام) تأسیسات نظارتی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی را مورد حمله قرار داد. نیروهای آمریکایی علاوه بر دیگر تجهیزات، از جنگنده‌ها، پهپادهای هوایی و ناوهای جنگی استفاده کردند.
سنتکام به دستور فرمانده کل قوا، همچنان ایران را پاسخ‌گو می‌کند و هم‌زمان محاصره دریایی بنادر ایران را به‌طور کامل به اجرا می‌گذارد.
بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77227" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی:
انفجار شدید همین الان خرم آباد
خرم آباد لرستان ۴:۵۷ بامداد صدای دو انفجار شدید
سلام وحید انفجار در خرم آباد لرستان خونه لرزید
خرم اباد دوباره صدا اومد ۴:۵۷
خرم آباد دو صداي انفجار پشت سر هم
همین الان دوتا انفجار  شدید خرم اباد
درود وحید جان خرم آباد همین الان دوتا صدای انفجار خیلی زیاد بعید میدونم اینا شلیک موشک باشه
خرم آباد دوتا صدای انفجار
سلام
داداش خرم آباد انفجار نبود
دو مرتبه صدای شلیک موشیک بود
[پیش‌تر پیام‌هایی درباره شلیک از استان بوشهر دریافت کرده بودم.
آپدیت: پس‌تر هم ساعت ۶ از داراب]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77226" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rtsR4gqWVCfA9zgiyiiWdQR8m7RQVHBeY_EO_thaApuTivm0rzddiXYJNMVg3lb3ZcA_OoUp1U2W5FhsaEqHOMeTB04IgaJH3h-6xPwu9Dqqtczvzez7RIHidsStwZmQ3yqBoZxGcEtXdcQoeH2wV82X2hiWY_KIbM-KWMR0EN_jOIG_IeWPNYFfLcyJvMlE5iA-q98Pr-5_iLzJBAcNdD84gxJ8ZIlwONFSaIcfa8sTVo-l1OlCyNT0NnrNWS35RSMgI4miiLPeRek7Kn-8FWE_Czy6zkf4FQg09pFfmYFzZCTRTpIWsfVt_QmaAju6tL0PB7cL9_CgZn-E1re7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، خبرگزاری وابسته به سپاه، بامداد شنبه، در جریان حملات موشکی آمریکا به جزیره لارک، دکل مرکز کنترل ترافیک دریایی اداره بنادر و دریانوردی این جزیره هدف اصابت قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77225" target="_blank">📅 04:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4KMXaD54E4M1Cvn5HjXEFvdJlgOnBSBpL8LI-EqIo_zR5mP5CHB9YU_lpDzYYBLTEZYP4YGW7FADLDYMbD3wEo4H2eYmondY9ppOUpPwVHRFoCKCxNV1bU_9IfRVKcQFvCxUOU6ML6P8x3zfeSk_uOnjLIBeNTV0Q_08dUBWOFxYAJ2nPYv8gkTlk6iRYL0MaBBivRRKA_Sd-JKGJRgP1uEEQVKPpOqI1C7HnaOJTHTgaOdFc21L5lqSJjyFyYuN7jJZi-N5JrBPshhcnw0qfsH2No4gOI2WH0B27BhGOu3G7f2RC8NY0o9j2e8cWyr0c26yzoWxRpswHYppJOMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است دو نفتکش پس از برخورد با مین در آبراه بین‌المللی تنگه هرمز منفجر شده‌اند.
✅
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران نادرست است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77224" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی از ۳:۵۰:
بندرعباس دوباره چهارتا انفجار شدید بود
باز داره بندرو میزنه
۴تا انفجار پشت هم
هفت تا بندر
بندرعباس کلی صدای انفجار داره میاد
سلام بندرعباس
از ۳:۴۸ تا ۳:۵۰ حدود هفت بار زدن
همین الان انفجار در قشم 3 انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77223" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرنگار اکسیوس، ترجمه ماشین
:
🚨
مقام آمریکایی: ایران یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد
🚨
چرا اهمیت دارد: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77222" target="_blank">📅 02:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxiS5gtEaK02_cMMjHutJ3v3i7yqByLmTtSNpO9APzIQbrza4-Fln9JmKqRvSx_3WcLEfbnAJcnuUI8kXgEcIDotRakMNzdeZpYntKox5xiTNc_XGGwAB_xOTzASkkFitm9-sos4DilvvQVNbthpZeMHJTD_VCbQ6BB7wtYp_jD_xY3mDPwoQpD9eP9UQWPbdjNFiHsK12I2C64eUBPfoeRVFi-i81lIXMdKZLs0O-7-8dFQJz2fCz1e2eUdaOKyUqedmNwnsQD3ZImUgz-mhyoKYHFaSIX6X6XnYvUGRAAbICGNxzrlphHhAHg6YtvdC9x8XD_xbwo79dVDjpSlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح: پل جاده رودان به بندرعباس
شنبه ۲۷ تیر
Vahid
منابع حکومتی:
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77221" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daa140a498.mp4?token=SK5RPI4j0iGJW2G23mVkod6GTIFAbufox0UvG5hTJIji3ylNR63DRVThLqD1RkSW4kHQVT2kYkIjEj6l48gUsyjCbQ1_1o7eEpPP_bb9H8rE8GVHydO75ZjEFc295s77BFm4KAICK4hoj86joQqLkOBWQ-s7Nxr-3xdTU8Eq4mozFi1N_dTalhtvafDJ7gQc87eNA4v_33qjiH4SQUVgzrWzjSnpTSEcAqoQ6X63frllnT9JfPVsocEFE10VDXGhlellfjcWt--7JABQoeMkdyKBZlNK2tpTT52dujIt7OK8zCIG9uovYZRFz890ech9WYQIkfjFm1qYUoBNQ9RqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daa140a498.mp4?token=SK5RPI4j0iGJW2G23mVkod6GTIFAbufox0UvG5hTJIji3ylNR63DRVThLqD1RkSW4kHQVT2kYkIjEj6l48gUsyjCbQ1_1o7eEpPP_bb9H8rE8GVHydO75ZjEFc295s77BFm4KAICK4hoj86joQqLkOBWQ-s7Nxr-3xdTU8Eq4mozFi1N_dTalhtvafDJ7gQc87eNA4v_33qjiH4SQUVgzrWzjSnpTSEcAqoQ6X63frllnT9JfPVsocEFE10VDXGhlellfjcWt--7JABQoeMkdyKBZlNK2tpTT52dujIt7OK8zCIG9uovYZRFz890ech9WYQIkfjFm1qYUoBNQ9RqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
شلیک از خرم‌آباد و زیر ۵ دقیقه بعدش ۲ تا انفجار
وحید جان صدای دو انفجار در خرم‌آباد
زمین کامل لرزید صداش هم مثل ترکیدن بود
تو کانال استان زدن شلیک موشک نمیدونم صحت داره یا نه
خرم آباد زدن
دوتا شد دوبار انفجار ساعت ۲:۱۵ دقیقه خرم آباد
وحید جان خرم آباد ساعت 2:15 وحشتناک زدن
سلام وحید همین الان خرم اباد۲ صدای انفجار اومد
همین الان ساعت 2:15 خرم آباد دوبار صدای انفجار اومد
خرم آباد۲.۱۶دقیقه انفجار
۲ و ۱۵ خرم آباد صدا انفجار اومد
خرم اباد چند بار صدا انفجار اومد
سلام آقا ما خرم آبادیم مارو همین الان دو بار زدن صدا انفجار اومد
سلام همین الان خرم آباد صدای انفجار
سلام ساعت دو پانزده دقیقه خرم آباد صدای دو انفجار
۲:۱۶ صدای انفجار خرم آباد
خرم آباد ساعت ۲:۱۷  دوتای صدای انفجار  اومد
خرم آباد دوتا انفجار پشت سر هم ساعت ۲:۱۴ صبح
همین الان سه بار خرم اباد صدای انفجار اومد
دوتا زدن تو خرم آباد لرستان خیلی سنگین بود
سلام خرم اباد ۳تا انفجار داد ساعت ۲:۱۵صدا خیلی دور احتمالا پادگان امام علی
[ساعت ۳ هم چند پیام دیگر دریافت کردم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77220" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=UlPN510GXJLjC3yKMs10p0Khj0XPKDYLl-Qjb4FyjxRveQ5pZTUXe_CjGi9ydjsmCkROogebfcYCWQDmlKuIjGRAueEDDW9B4TgyEbEPpCxZCC0DJLKXIchaoeM6AeE2YgCBFmsjf_s2fmmrLste844pxMMoZG5aJO9WxS37o3LwxqiakyKdJcW5LksbQSWd5iVyK5bSHFXnB8wGGFyS9zzyO7iz244-IrXjfjunhVW9MuJ56TW-sB4o4BV97YdkdOZoaWPuVc6XLDuJdAOjyQWueM__lB9S71HoRxJM-tJCWdwgziYbwaaBhRzHhJ6FA86B5dc1hn0WB3Mzl84stg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=UlPN510GXJLjC3yKMs10p0Khj0XPKDYLl-Qjb4FyjxRveQ5pZTUXe_CjGi9ydjsmCkROogebfcYCWQDmlKuIjGRAueEDDW9B4TgyEbEPpCxZCC0DJLKXIchaoeM6AeE2YgCBFmsjf_s2fmmrLste844pxMMoZG5aJO9WxS37o3LwxqiakyKdJcW5LksbQSWd5iVyK5bSHFXnB8wGGFyS9zzyO7iz244-IrXjfjunhVW9MuJ56TW-sB4o4BV97YdkdOZoaWPuVc6XLDuJdAOjyQWueM__lB9S71HoRxJM-tJCWdwgziYbwaaBhRzHhJ6FA86B5dc1hn0WB3Mzl84stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر پیام‌های دریافتی گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند: 'پل گلوگاه بعد گنو
#بندرعباس
و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
شنبه ۲۷ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77219" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/087c286f67.mp4?token=SLoL14GBvKaUm15x6Ym7LZYUxmPbPuCzFxLhzyBiFxlsMYTNQqSyAVoW4LrUAMH31ft-0pcNhbGqyM7G7E9OK-b5-6lo07IQJR6w_HRkV6yBtcu_nljGzGbR-3t7IGQb-woMu9VWDYp9yxL3tmqz1uxmAt-ZM17E7wSF6Aan6SFeD--2TdECl67stQauiIYpudzQsLOn8gKLanGrVkBQZv61l0dnnGaQJa6RqS82LaeB2fq8D7SUvX9XcDrA-pNPu3ytZ3jJt9yTyzedOrjPcxJPEl5KpJWfsKW63jY-P9KO3mnpkDjELjP2_bI3AwHgPwGDCXE48ANdnRL_kz0UzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/087c286f67.mp4?token=SLoL14GBvKaUm15x6Ym7LZYUxmPbPuCzFxLhzyBiFxlsMYTNQqSyAVoW4LrUAMH31ft-0pcNhbGqyM7G7E9OK-b5-6lo07IQJR6w_HRkV6yBtcu_nljGzGbR-3t7IGQb-woMu9VWDYp9yxL3tmqz1uxmAt-ZM17E7wSF6Aan6SFeD--2TdECl67stQauiIYpudzQsLOn8gKLanGrVkBQZv61l0dnnGaQJa6RqS82LaeB2fq8D7SUvX9XcDrA-pNPu3ytZ3jJt9yTyzedOrjPcxJPEl5KpJWfsKW63jY-P9KO3mnpkDjELjP2_bI3AwHgPwGDCXE48ANdnRL_kz0UzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تبریز کلی پیام فرستادند که دو موشک شلیک شده.
و مطابق معمول از ارومیه و خمین و خرم‌آباد زنجان و داراب و... جاهای دیگری هم پیام‌های مشابه میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77218" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر سه تا
شد پنج تا صدا
بوشهر زدن الان ۲؛۳
بوشهر - دو انفجار مهیب با فاصله ی زمانی ۵ ثانیه ۲:۰۴
سومین انفجار مهیب ۲:۰۵
چهارمین انفجار در فاصله ای دورتر ۲:۰۶
سلام اقا وحید بوشهر ساعت ۲:۰۶ صدای انفجار شنیده شد
وحید جان همین الان بوشهر پایگاه زد صدای سه انفجارپشت سرهم
سلام وحید جان همین الان چغادک را زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77217" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه: دو  کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر و دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودک‌کش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
و ماالنصر الا من عندالله العزیز الحکیم
پیش‌تر:
🔹
سپاه: لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77216" target="_blank">📅 01:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=olcpzRixggm9xVNnpa20s_YyEloKM8f1rm0W-jIO47RzveoC6njHkEeMhzTOwxVgMAN4u9PAPMiCyDdM4SmXEvXlPTre9q4WP90PDQpI-Z7HgqxyOohiMqeJBLhGVx49CQtPiXgxgNKuXQxXKP6M-2euwTnfnd7apBx8pRTVRFKPnsfbBo5icCZ6ewvwI1ENcsH1lP2TWZjyum9zbNDfKPduMEvzsLZ8NKokMSSXr-ctMgQMVPFF6iGpiYgUB4B7QtEUpPWYF2zNz7xZO_S32QcnP5n7XfiO--mr7zXc_JlL8-mP6N-2e9jDs0ZFE6NXZ-MWU7_wmnpuJ5Gj0p6LpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=olcpzRixggm9xVNnpa20s_YyEloKM8f1rm0W-jIO47RzveoC6njHkEeMhzTOwxVgMAN4u9PAPMiCyDdM4SmXEvXlPTre9q4WP90PDQpI-Z7HgqxyOohiMqeJBLhGVx49CQtPiXgxgNKuXQxXKP6M-2euwTnfnd7apBx8pRTVRFKPnsfbBo5icCZ6ewvwI1ENcsH1lP2TWZjyum9zbNDfKPduMEvzsLZ8NKokMSSXr-ctMgQMVPFF6iGpiYgUB4B7QtEUpPWYF2zNz7xZO_S32QcnP5n7XfiO--mr7zXc_JlL8-mP6N-2e9jDs0ZFE6NXZ-MWU7_wmnpuJ5Gj0p6LpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیام‌ها میگن در بندرعباس صدای پرواز جنگنده و انفجار می‌شنوند.:
صدای جنگنده بندر
لرزش و صدا انتجار هم  میاد
وحید جان الان سمت بندر رو زدن
بندر عباس دوتاشو شنیدم
۴ صدای انفجار بندرعباس
سلام سه انفجار بندرعباس
صدا جنگنده هم میاد
بندر داره میزنه
سه بار پشت سر هم
4 صدای انفجار بندرعباس
ساعت ۱:۰۵ صدای انفجار بندرعباس
تا الان دو سه تا دیگه اومد
تک انفجار با صدای کم، شاید بندعباس بوده، توی قشم-طولا حس شد ساعت ۱:۰۸
صدای جنگنده بندرعباس
بندرعباس ٥ تا انفجار جنگنده خيلى پايينه
بندرعباس به شدت صدای جنگنده 1.11
ساعت 1:11  صدای جنگنده اسمان بندرعباس ارتفاع پایین
صدای جنگنده میومد بعد از ۲۰ ثانیه صدای انفجار اومد بندرعباس
سایت موشکی خورگو بندرعباس رو‌ زدن ۳تا انفجار بزرگ با جنگده
بندرعباس ساعت ۱:۰۷ صدای انفجار شنیده شد
🔄
این بار پیام‌ها رگباری بودند نه پراکنده:
بندرعباس همین الان انفجار وحشتناک
وحید جان اینجا رو وحشتناک زد بندرعباس
بندرعباس ساعت 01:16 صدای انفجار شدید
انفجار سنگین منطقه ۴ بندرعباس ۰۱:۱۶
بندرعباس دوتا انفجار شدید الان به جز دوتای قبلی
سلام شبتون بخیر آقا وحید
الان صدای انفجار بدی آمد طوری که پنجره ها لرزید
همش صدای جنگنده تو اسمانه
بندر عباس همین الان چند صدای انفجار ۱:۱۵
سلام بندرعباس همین الان صدای یه انفجار شدید خیلی نزدیک بود که همچی لرزید
😭
این شدیدترین صدایی بود که بعد از آتش بس شنیدم
زددد الان زد بندرعباس
سلام وحید جان همین الان ساعت ۱:۱۶ دقیقه ی انفجار شدید  بندرعباس نزدیک پیامبراعظم که خونه ها لرزید
سلام وحید بندرعباس ساعت ۱:۱۶ دوتا انفجار شدید صدای جنگنده هم خیلی میاد
بندرعباس اول صدای جنگنده میاد بعدش انفجار ده دقیقه پیش اینا سه تا با هم زدن چهارمی رو با فاصله ولی شدت خیلی بیشتر زدن چند دقیقه بعد دوباره صدای جنگنده و پنجمی
الانم دوباره داره صدای جنگنده میاد یه بیست سی ثانیه دیگه میزنن
بندرعباس الان بالای ده دقیقه چند جنگنده روی شهر می چرخند
🔄
همین الان ساعت ۱:۱۹ زد بندرعباس
بندرو رگباری میزنهه
برای بار نمیدونم چندم صدای انفجار
انفجار دوباره پشت هم بندر عباس
بندرعباس الان زد وحشتناک
همین الان ۱:۱۹ دوتا صدای انفجار شرق بندرعباس
زدن وحید بندرعباس ۱و ۲۰
الان دو تا صدا انفجار اومد
سلام وحید جان دوباره صدای انفجار دوتا
بندرعباس ۱:۲۰ دقیقه صدای خیلی زیاد انفجار
قشم همین الان صدا انفجار شدید اومد
سلام  وحید بندرعباس ۱:۲۰ فرودگاه انفجار بزرگ از سمت فرودگاه
بندرعباس الان ۱:۱۹ دقیقه صدای انفجار بلند اومد. قبلش هم جنگنده داشت می‌چرخید.
بندرعباس دوباره زدن
فک کنم تپه الله اکبر دوباره
خیلی شدید بود از دیشب هم بسیار بلندتر 1:16
زدن وحید بندرعباس ۱و ۲۰ پایگاه هوایی
همین الان سمت مسکن مهر طرفای بلوار هرمزو زدن صدای خیلییی شدیدی داشت خونه لرزید
سلام آقا وحید من از داراب فارس پیام میدم تو آسمون داراب هم امشب مدام صدای جنگنده میاد
من بندرعباسم صدای بدی اومد ما محدوده بهشت بندر هستیم
وحید صدای جنگنده در بندرعباس قطع نمیشه خیلی پایینه پشت سر هم صدای جنگنده
دکل مخابرات رو تپه الله اکبر رو امشب یه موشک خورد توش همین الان
برعکس دیشب که ۵تا زدن
منابع حکومتی:
استانداری هرمزگان: در ساعت ۰۱:۲۰ نقطه‌ای در بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77215" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=cIrUbTR2bPUXFwZvxM-FWclRIx38XgyIs9-0Xg6WxQ9vj8udernJwlbhn_XSg81HI5URZ2nhyRI4EtY1gOwcK4g2dV8eLdk1M8NUd6Zv3PGd3VXQdrB10_iFAA3FrFI38e43ebToInjILeefzWmf-kqymlQAsjjHYN7ROrUBEGDBvibBrzCX91zj_fUtwlH9jloqGLkAb0mt9snZ8qtAXoW29EMUgulYrxA_OKzWf45eQpORKTIae7G8CstEkNCqPL39Idj9H1n92EsKvbc9ST6uOnJESKscOVCPWqJclwJv6Vs27ruHRFu1pygM_Lp3CQKldR5FpDmSWC7As56YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=cIrUbTR2bPUXFwZvxM-FWclRIx38XgyIs9-0Xg6WxQ9vj8udernJwlbhn_XSg81HI5URZ2nhyRI4EtY1gOwcK4g2dV8eLdk1M8NUd6Zv3PGd3VXQdrB10_iFAA3FrFI38e43ebToInjILeefzWmf-kqymlQAsjjHYN7ROrUBEGDBvibBrzCX91zj_fUtwlH9jloqGLkAb0mt9snZ8qtAXoW29EMUgulYrxA_OKzWf45eQpORKTIae7G8CstEkNCqPL39Idj9H1n92EsKvbc9ST6uOnJESKscOVCPWqJclwJv6Vs27ruHRFu1pygM_Lp3CQKldR5FpDmSWC7As56YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: سمت نیروی هوایی
#لار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77214" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eom5pbtFKmrVwTwYQ2SN5xQCaVsRVdXCuWv9W3ruGtQ_wBAvZmT1IEflhak76AYK81EzY27Lvkla69N8YfBFGTdfJbrVUXMWgMVF69dJRcB6Q4cXZt3RK6Rs2ikunfauHRiqIgGDP-8yAKN1S774ULbIdw55PSBVx53ifq4FGGLVWc7epWvjfwNY63zKyggzoEyM68RMHG5wSJL5SomeKhclm3-kbij5XpjE0t4q5II1c2q3bWWtvowceIb2VUwy7fa37-VFQOrS3ItMONEtS0SbDfemII6rtG14_BcEC3b7cUzm3oIrCP7wSt0DkaOHmD0-MuQ9Cf_hRejcLR1dTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۱۲:۳۰ اهواز رو زدن
صدای انفجار ولی زیاد نزدیک نبود
اهواز رو زدن 00:31
اهواز صدای انفجار ۱۲:۲۹
ساعت  ۰۰٫۳۰  اهواز  ۲ تا انفجار  پشت سر هم
منابع حکومتی:
معاون امنیتی انتظامی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77213" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=sRIBp_XDEaw8Y-_8c-KPz65A7tUzB11W-PmlLN-4QxrJS9baq5mXo8327L-z3ksMty0WDKtPhKzdmRn2W-aubN0n86stx6Y5EnY59wYy_Aury0DUwfJTB7cFLXw1InOieUYR658NA7nwFlZP3qe6TD7zF-ES4_qJ_2s5wHxABNarVW3wAB12WhEyR2qORO03AS_yHQT2cwRNy22k_j0Ye-5xPHy7LTZOzSLzoaa5M0b7bDirqobojO4ykETd1jHZ1Bt_ka7EP5O2CP2-2caKjT7EwO1WBrAMPcYyJUupFh59xDUPLPz25_DBFtcjB5VfVl2fvsuPS8lF3RvxcPvPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=sRIBp_XDEaw8Y-_8c-KPz65A7tUzB11W-PmlLN-4QxrJS9baq5mXo8327L-z3ksMty0WDKtPhKzdmRn2W-aubN0n86stx6Y5EnY59wYy_Aury0DUwfJTB7cFLXw1InOieUYR658NA7nwFlZP3qe6TD7zF-ES4_qJ_2s5wHxABNarVW3wAB12WhEyR2qORO03AS_yHQT2cwRNy22k_j0Ye-5xPHy7LTZOzSLzoaa5M0b7bDirqobojO4ykETd1jHZ1Bt_ka7EP5O2CP2-2caKjT7EwO1WBrAMPcYyJUupFh59xDUPLPz25_DBFtcjB5VfVl2fvsuPS8lF3RvxcPvPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید یزد الان 12:30صدای انفجار میاد
5 مرتبه صدا اومد
من تفت از یزد هستم
تا الان ۵ تا صدای انفجار شنیدم ولی دوره
۵ انفجار شدید پارک کوهستان یزد
یزد الان ساعت ۱۲ و نیم چندین صدای انفجار
وحید جان یزدو بد زدن چهار بار
سلام وحید دارن یزدو میزنن
وحید یزد چند تا صدای انفجار اومد ۱۲:۳۰
صدای ۵ انفجار پیاپی در یزد ۱۲:۲۹ تا ۱۲:۳۰ بامداد
من 4 تا صدا شنیدم
یزد ساعت ۱۲:۳۰
بیش از سه بار صدای انفجار اومد و زمین لرزید
وحید یزد رو زدن، ۴ تاشو من شنیدم، اخریش شدیدتر بود.
آپدیت:
منابع حکومتی:
معاون استاندار یزد: حملات آمریکا به خارج از شهر یزد بود
🔹
نیمه شب با حمله جنگنده‌های آمریکایی، صدای پنج انفجار در خارج از شهر یزد شنیده شد.
🔹
پنج موشک در حاشیه شهر اصابت داشته که تاکنون هیچ‌گونه خسارت جانی در پی نداشته است.
🔹
اکنون آرامش برقرار شده و دیگر صدای جنگنده‌های متخاصم شنیده نمی‌شود و آسمان یزد کاملاً امن است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77212" target="_blank">📅 00:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=cdbrAGC8zanw4R4Qq3z-_4e56SIloG4wUc1KleiAmovNiP4rEowDxbIZh85kM4tir2Wx6fzmn8l8SMaR61iiKqW1uakeIxSJXs3qejvsQUeZ2SJWDr3FVQ7Ha8wGuG3UzpT--fmbdxg_CTSVuKHk4WzyHgTpICUvK5uFUbr_Mm5KhuS6UEqzF7EtvPgysTVA-m94BOroVCQbyqsS5IVXWcytx7gSu8FzFdJPYMpaGQZuzoCmNdJukPjr-WvMMN0PAoP9_FRpOtMyI1D8cK9J4FgrAm1f3dBTro3W7Wh1yKfLIpHgbx1Vz2YqWj6PZcU-4UySvfRNzed7JFq4YJnmpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=cdbrAGC8zanw4R4Qq3z-_4e56SIloG4wUc1KleiAmovNiP4rEowDxbIZh85kM4tir2Wx6fzmn8l8SMaR61iiKqW1uakeIxSJXs3qejvsQUeZ2SJWDr3FVQ7Ha8wGuG3UzpT--fmbdxg_CTSVuKHk4WzyHgTpICUvK5uFUbr_Mm5KhuS6UEqzF7EtvPgysTVA-m94BOroVCQbyqsS5IVXWcytx7gSu8FzFdJPYMpaGQZuzoCmNdJukPjr-WvMMN0PAoP9_FRpOtMyI1D8cK9J4FgrAm1f3dBTro3W7Wh1yKfLIpHgbx1Vz2YqWj6PZcU-4UySvfRNzed7JFq4YJnmpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'حمله به سایت موشکی در جاده گراش
#لار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77211" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
پیام ساعت ۰۰:۰۷: لار داره پشت سر هم صدای انفجار میاد
سمت جاده گراش
حدود ۱۴ تا صدای انفجار
سلام اقا وحید الان لار دوبار صدای وحشتناکی اومد فک کنم سایت موشکی رو زدن
سایت موشکی لار [رو ] ‌بیشتر از ۱۰بار زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77210" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، برای هفتمین شب متوالی دور تازه‌ای از حملات علیه ایران را آغاز کرد. این حملات به دستور فرمانده کل قوا و با هدف ادامه تضعیف توانمندی‌های نظامی ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77209" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=LNNcUM8deDsn-Owj4QNkghFAxaspMH87b2_Gd4L2b7KcZvtC_axXVP4bm-Gxy_6cp92SygBptH9GAqtrOQdEwVwPcZ6nqBKhJb5zhYn7xg9W1nkPIXxx9FbOU_eDIGL6iodNj4n6D1sRWp4iPJEO0eKX-k43kBBuomjv_YDEeNzM8vtAkpiVdOhoMDIloRVkg9vIqoRZRU3CiBlJnG8OnDdqL9p1B30W3U_xWHrbI0JET2uB_K6BbhQ3LXly5y41y_Gzrc0zBrQXJZ0by2LEWsUEdSkHRO4SE4RCFo2vWMhsHLct8OpGEQCHfaGXV3TANMTFyB_3BR5ulp7hZZNNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=LNNcUM8deDsn-Owj4QNkghFAxaspMH87b2_Gd4L2b7KcZvtC_axXVP4bm-Gxy_6cp92SygBptH9GAqtrOQdEwVwPcZ6nqBKhJb5zhYn7xg9W1nkPIXxx9FbOU_eDIGL6iodNj4n6D1sRWp4iPJEO0eKX-k43kBBuomjv_YDEeNzM8vtAkpiVdOhoMDIloRVkg9vIqoRZRU3CiBlJnG8OnDdqL9p1B30W3U_xWHrbI0JET2uB_K6BbhQ3LXly5y41y_Gzrc0zBrQXJZ0by2LEWsUEdSkHRO4SE4RCFo2vWMhsHLct8OpGEQCHfaGXV3TANMTFyB_3BR5ulp7hZZNNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، بهمن ۱۳۸۹:
حکومت وراثتی بود. یکی می‌مرد، یکی را به جای خودش معین می‌کرد. مردم هیچ نقشی نداشتند؛ می‌خواستند، نمی‌خواستند، ناچار باید قبول می‌کردند
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77208" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d59582925b.mp4?token=CG8385vEgzjHCcVjb-PQ4LmysPTfiAB1zhI9TW6pb7gXgFfPDed6E8JslZOVaT-IGn_c14M4LDJ0PAPpky8U3Or9Mo630PJNPVnvKGi0PJx4GMyUnvhnbQ7Cs_m6y-MmjRwzxdDkNXPSoYdFfZTi1kA9TyOTT2jJC4Zq9fM8eQ8JhHnXtPQHOZR9yoqmQ5aLzkYvFpvi1wPt893zKZDhq9FdNQoNyFbnt9GbRbBSbYsqZx_q939U0t5NZh_NM6NsQda9UUMqPrm1ee9escg97docYLwNxrSfC83doSUTD5OOFCWdFUD8Nwlz_qBrhLCuKzXj9Wt88F5wH9UCn-tYig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d59582925b.mp4?token=CG8385vEgzjHCcVjb-PQ4LmysPTfiAB1zhI9TW6pb7gXgFfPDed6E8JslZOVaT-IGn_c14M4LDJ0PAPpky8U3Or9Mo630PJNPVnvKGi0PJx4GMyUnvhnbQ7Cs_m6y-MmjRwzxdDkNXPSoYdFfZTi1kA9TyOTT2jJC4Zq9fM8eQ8JhHnXtPQHOZR9yoqmQ5aLzkYvFpvi1wPt893zKZDhq9FdNQoNyFbnt9GbRbBSbYsqZx_q939U0t5NZh_NM6NsQda9UUMqPrm1ee9escg97docYLwNxrSfC83doSUTD5OOFCWdFUD8Nwlz_qBrhLCuKzXj9Wt88F5wH9UCn-tYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در صدا و سیما گفت: اگر آمریکا دو سه روز دیگر به حملات خود ادامه دهند، وارد فاز تهاجم و انهدام کامل خواهیم شد و هیچ مرز سیاسی‌ای برای حملات خود نمی‌شناسیم.
او ادامه داد سیاست «هم جنگ، هم مذاکره» به طور کامل پایان یافته و اکنون راهبرد ما بر پایه بازدارندگی، مقابله به مثل قاطع و پاسخ «چشم در برابر چشم» به حملات موشکی دشمن استوار است و ما موشک در دهان دشمن می‌زنیم.
@
VahidOOnLine
مشاور نظامی رهبر جمهوری اسلامی می‌گوید هم اسماً و هم عملاً چیزی به نام تفاهم‌نامۀ اسلام‌آباد دیگر وجود ندارد.
محسن رضایی گفت که پیشبینی می‌کند که اگر مذاکرات شروع شود طرف مقابل قصد دارد «اصلاحاتی در متن ایجاد کند و در واقع تفاهم‌نامۀ جدیدی بنویسند». او در ادامه گفت که اوضاع تغییر کرده و چنین چیزی ممکن نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77207" target="_blank">📅 23:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=U6uBVo7O0aIJvBEde8urIDdHC61QMAQr_StGFF8EFS7f520iLETimvC0enjpH0QFrZOB1z5GXtHdOhjyha9cbYm-fty6lZBMazf7Oqefa4z4N2dYvfqNL7kz-9KueOTviTW33mljPGLbOfjoeyOOEmMau5-dE95Vpqea5piaO_esuUFsKttXgTc9nz86cFtXzlJlzVHWB_jprkgg3VtRt6XOMxu33R9qfFJQ2Q3JvNpqm3cSrvMYVBBAfOmXUjGWTF_rGNG5FMEiLKxP_rUgeAYruoBwu1IFKMv4ddbfvzaGUdSe9WCERKYYiz3YIIFhP9EsyURipvB9FrbskgumSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=U6uBVo7O0aIJvBEde8urIDdHC61QMAQr_StGFF8EFS7f520iLETimvC0enjpH0QFrZOB1z5GXtHdOhjyha9cbYm-fty6lZBMazf7Oqefa4z4N2dYvfqNL7kz-9KueOTviTW33mljPGLbOfjoeyOOEmMau5-dE95Vpqea5piaO_esuUFsKttXgTc9nz86cFtXzlJlzVHWB_jprkgg3VtRt6XOMxu33R9qfFJQ2Q3JvNpqm3cSrvMYVBBAfOmXUjGWTF_rGNG5FMEiLKxP_rUgeAYruoBwu1IFKMv4ddbfvzaGUdSe9WCERKYYiz3YIIFhP9EsyURipvB9FrbskgumSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار ویدئویی‌هایی از قرارگاه سپاه پاسداران در راسک نشان می‌دهد که در پی حمله هوایی آمریکا، سقف یک سوله بزرگ در این مجموعه به شدت آسیب دیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77206" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrFlU9n5vxU0-UvDYl3QGZnQTNsiK3XmWxaoEYJ18PhEFb0Y3-lCxx8LoTtU5HpkkeNwlGAlJvUFpGSO5vQZRSXJ8bYDX549UfPBx959TFN7d597ZpHeVUmTl8MRK1OFpQ_-mOvk3Vmj-skd1OT4_JXuK8c7GBxC-889UmeMmGGKAVe5zGbmaupS5hcUw8DoFRvSgli7EERBqJwKKGDN94QHNUzCRyzA5lsZg0LUa-vwwf_CeEZA8HG7iE9mkKBRZ9gtCZTusg2D-5y_2szWp3yGB3-A-SXZ_uMV5E75S7jnyun9Mq8wcArnxNp9bsSPzLGOukTItQSxBuMVeYslBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس روز جمعه به نقل از سه مقام آمریکایی و اسرائیلی خبر داد دولت دونالد ترامپ به اسرائیل اطلاع داده که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند دیگر هواپیمای سوخت‌رسان را به این کشور اعزام می‌کند.
بر اساس این گزارش، سه‌شنبه این هفته در نشست «اتاق وضعیت» کاخ سفید، چندین طرح جدید نظامی به رئیس‌جمهور آمریکا، ارائه شد و او در حال بررسی اجرای یک «حمله گسترده» علیه ایران است؛ حمله‌ای که دامنه آن از حملات کنونی در اطراف تنگه هرمز «فراتر» خواهد رفت.
اکسیوس می‌گوید «زیرساخت‌های ایران مانند نیروگاه‌های برق، انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف دفن هرچه عمیق‌تر ذخایر اورانیوم غنی‌شده، و همچنین بمباران سایت زیرزمینی کوه کلنگ‌گزلا که گمان می‌رود یک تأسیسات هسته‌ای در حال ساخت باشد»، ازجمله گزینه‌های در حال بررسی در دولت آمریکا است.
دونالد ترامپ روز ۲۲ تیر در یک مصاحبه گفته بود که ارتش آمریکا احتمالاً به زودی به کوه کلنگ حمله خواهد کرد.
گزارش اکسیوس در عین حال یادآوری می‌کند که ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد آماده تشدید جنگ باشد تا خسارتی در حدی به ایران وارد شود تا جمهوری اسلامی تنگه هرمز را باز کند و خواسته‌های او دربارهٔ برنامه هسته‌ای ایران را بپذیرد.
در حال حاضر، ایالات متحده حدود ۳۰ فروند هواپیمای سوخت‌رسان نظامی در فرودگاه بین‌المللی بن‌گوریون در نزدیکی تل‌آویو و تقریباً همین تعداد نیز در فرودگاه رامون در جنوب اسرائیل مستقر کرده است.
مقام‌های اسرائیلی به اکسیوس گفته‌اند آمریکا قصد دارد طی روزهای آینده چند ده فروند هواپیمای سوخت‌رسان دیگر نیز به اسرائیل اعزام کند تا شمار این هواپیماها به سطحی برسد که در آغاز جنگ ۴۰ روزه وجود داشت.
به گفته این مقام‌ها، ارتش آمریکا ترجیح می‌دهد هواپیماهای سوخت‌رسان خود را از فرودگاه بن‌گوریون به پرواز درآورد، زیرا سایر پایگاه‌های هوایی منطقه در برابر حملات ایران آسیب‌پذیرتر هستند و امنیت کمتری برای هواپیماهای آمریکایی دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77205" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=XCed5TEmHT-gFjPV6R5Kn1A8NQTQc559o03lv_zlGFNak08n6PUngMRv2JrX60IR_9lfRkiWKdVBd3GEcK6Df9WTo7Q0IPv_inTOMIFem0KDOIk5jv9AzxKm36Qg-b8VdDAdgNm5aOnwKBQAThOFP_kbuFWaWL-BG60BzHpU-p99l72RMYYMFtGyPzZ0N9Ox193Z819Lqrll7stjSFxY8zMvfcTY6tUaizy78zAhpBRaMRYZTFGb5iADGZvkdMl9MztCHdvV_keEaY-b1s8WbZA-_10aNVb_xYGOYIKCeqnfbDztj05mdtWAQD4xIt8xTVIUmaySXjNc5UQeWnoiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=XCed5TEmHT-gFjPV6R5Kn1A8NQTQc559o03lv_zlGFNak08n6PUngMRv2JrX60IR_9lfRkiWKdVBd3GEcK6Df9WTo7Q0IPv_inTOMIFem0KDOIk5jv9AzxKm36Qg-b8VdDAdgNm5aOnwKBQAThOFP_kbuFWaWL-BG60BzHpU-p99l72RMYYMFtGyPzZ0N9Ox193Z819Lqrll7stjSFxY8zMvfcTY6tUaizy78zAhpBRaMRYZTFGb5iADGZvkdMl9MztCHdvV_keEaY-b1s8WbZA-_10aNVb_xYGOYIKCeqnfbDztj05mdtWAQD4xIt8xTVIUmaySXjNc5UQeWnoiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا: برج مراقبت چابهار را منهدم کردیم چون سپاه
...
پست سنتکام ترجمه ماشین:
در ۱۶ ژوئیه، نیروهای آمریکایی برج مراقبت بندر شهید کلانتری چابهار را با موفقیت منهدم کردند. این برج بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود که سپاه پاسداران انقلاب اسلامی دهه‌ها از آن برای ردیابی و هدف قرار دادن کشتی‌های تجاری عبوری از تنگه هرمز استفاده می‌کرد.
انهدام این برج مستقیماً توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی بی‌گناه را تضعیف می‌کند. افزون بر این، این حمله از آزادی کشتیرانی در آب‌های منطقه برای همه شناورها محافظت می‌کند، به‌جز کشتی‌هایی که در تلاش‌اند محاصره دریایی جاری آمریکا علیه ایران را نقض کنند.
CENTCOM
پیش‌تر پیت هگست، وزیر جنگ آمریکا،
این تصویر دریافتی
رو بدون هیچ توضیحی
توییت کرده بود
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77204" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WvtNZhWK7Qy_2p03pg0EW4bwWeGmVk7nmpy32nBd-30yf4O4M6lGNfvIQyV_ZQbX5CpCkwFfPa5CHx0unTgIqN0Qfn--fWuy1Q4-Nf_moCEVNv8shN1JyiKTiUNg9pR6beuulNytWKgvkbBsI8A7hQ6iOSOGAP43x_vk9WTrx2v3Wpn7cFMQxWKEHebJSTJXUn733_ZVM0soCdinBOWX_WYo9eyrOmvrDQuF8CiaYi6W2x-Y0y68gw2Xeqa0SGWnvZT85HRs5mgo4Z6aAGpGoaAPgL8KV6HmAYFk4PW5ITYtX0nYTiPNKvWCwnOxCqSzvRU1LWojGvKsFPPNHHoCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: "پل و خط تخریب شده دیشب ایستگاه انشعاب راه‌آهن
#بندرعباس
"
هم‌زمان با حملات آمریکا در بامداد جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77203" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEDpK10SCGmeAoq5OXiIB_oVaR66lY2DQG67talDMxRAUqCHPwArzmZKu43sMcEKdAJhqBXjj4yn6-En9Quhl1oUpKniAmwOodewfd7h0gbBvClwRp70EZws9ZATa4X4UHcw4zbasYTqlQDreUJv0wZRxPidXxI9Iuv7cpldSYFn_39jNEKnGo9XQO-NSV41p8TgGoGrlj2WtYkC8CsiP7d5I3DLkLUwcfIn1-TZmaJfR9lr9-dgiTA5wSUx6aX-mJfvRqXpJJwk5XVrxTPGSmOPrDSQ1UfpQZ94gug7AOKWY_U7tWtGP-celLPyDyZGwXtRww8t5wpt19HF22v5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYB_JQfpoVp0c1ojTckLcUwar_AhcBA7XZsO3AZbGsq1z7gR8qfo1q0Pv6XauVPb9vgJRNi6xCrAP6_6KOabu_-5EbR9UQGHj2SNftCLFjpX40GcD-Rj4Uq1y4G5g1sXofriRpJg1L8bdORRFdMOQWnFSm39y3vmVXyykNPkypmHRUhGqowNeg760l1mGhACE2iBKWE8uh6ctcE_5Cj9kinDKJT2StgS8oSpI5WNGtL20Z0wtCUxEncPK1jitMav8VnvToZ1Ci3RDCzLty8OggLmVgez30jUvZIcm6yHVkEHCdluLLv45-ZWdM5CmwHfdKGaaS__bhBAE3QRM_MRAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i294-VzGkL5LpALJrPhFYdK-SPS5K2PZlK40kcy7ANCXWsBB6ofvQYev5T4hrpHAbeGn9A6Cx2_YiO9nTTSmCs_8OkDekqRoUHzgqVkdGFNjm-K9APMav2tcorJopZtgFINGPIOs-L5Po-Z2JENUziePyVqDEurVieEIWSrszjuXwr6TwfAveZV4QzOzGHcdt18LUzYPO2dER5HhVRawv9NLbC4h3_kcSYLXXGe9z4P8cEkTQHiJA1a91Z2qBKzb9CiIMuPUgt6pP4YX4BwLabFbOVQM5aQoAHH9nGaMDclRvOf5-Q3i08raSWVbZkIq7Q4-lVXWictAymwYL3mzag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dKIoOU_-xbhYnJzWCErqKCA5dJJcOzyj0mvshYw_BpmLPZTGBVkIz2ohZ56fQWjmXMh4t3pAp4hXZ4bxO5pgWQd8Jqd147DLOlo5bTv1WXMy8pfc3a5jyQrp03HqWjT8S6zVxqArXmM7Pm7Qnx8ccl0mSjd4yBxbVo19XKfVUJ-lGmOZU5XRER45TQrUkoZ7idbQhD13-5-fMDxDf8SmTAdBTYexE1dGixaPe6fCVs75SGyhJyO1usKIF-aWtAD8nt_obScvk_SuTRjZpFF-udGJbWjYrj7EhHVmwUXeKwV1M9K0QtqmE4ogYf0UtERAKW51o9GBp_u9yFySQ6iqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MOgbaj9lzXPUxWSgiBF7IphuvTNOyGHXd7NoYIgG8uT-MMFPXiEvAu-9DJD4DyBtDKGjEy6IBfn78-QbuEYUAVH77H9dEFmmNfzJW8ohID8rURflGgJWjus_aXuf_MkGOiULt_YmwtOonACmcjUxaGkKYlL0NOSUdD2Ma873gc0W6sweAv6wdeoQTN3-AGD3BWH60JoHrub2_Vt8kbYOs1ZVaTWM8snj7vHmTRpDyysTaDb4VXXhP2G3qRfo_9z53FfAa5vQ90q55AR4SinhAe8PFhDeQCPaV8N7SOTS14yP5gvbRDkYVCQA_7hcS7EoSDOFZ9PmecQLR5JW8V7-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BrBYe4nG8nF1gvdSlOfepwVZ1PPfhwGVjoT7xtWaRLDf6Ao-77J6Nu68eB7a0kuEBJVJWGdIUN9_f7lAjoyyaEoom09ySk1YXDR3rQ-OIVtZ-pIVVmCxBG7J7WjWDjzpGcLRn-mXSF3Sd2jR2GiQjUhlCVTVw9rx9KK_gyNjlIYiaYDGX6Td_qNev8XcjlfekCRE6xgjvLBbu9g_q7xPW-RzS_khpDfz98s5FvH9VrJupfsdWK2el1rVlR26rpCn1hCjBbdgYUhlC1doO78OWo5bQc1TG9OIrQdb5H6XUN_Wk-IFQtZyHez-hFNyLK5_pjlfmIf476y6jQVU290Tgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ND3xIB0FErg_fVg89guAmbePqlHrcJLl0A0Bo2V0318mxROdrqckqbp0VIl9tWll1BxlphGKYJTOaSn9Saf5NxTjpKELfPjWUecEIe0Dc4pPYFEr1GhkQS1HEKGgNHkXZofBLvamcoznGNKCEndJoRqr8xyLf7bR-KG6OL0p1-wweHN-Mgi9QRzB6NpKeMqEkj49dwJV5NOf0GlwHHbWRgKVFPYFbNpYrX2cn7NalsWhBxQK48KZzveO2GMKEeu-9dbaSaNNH5JqFD9b-rpnMXryGMuoKUmCYsBRQpqym63Q0L4jG5YzcZZYAPaOd0MDTQ5Kn5ndcu1p0MqDOsr5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rO97QLzbd7k0OIr1s_7esTkFmC_b8yohec2i_aTnZxj-KRe-8kDm_7JG-PkLBAZT86PdgKTIeCT0NVWCL-Mabz1VxCxxkWswtKlk5ylHIgh3BilubYiS8SZWOwnECatUa9_y_oOOO7xvi67cbD_Eem7CiCziwF9U50u8aROciC8Nn8jd1AYMANBUQ-qrSjMpfM8NCJ44EpTQVocSYGfqrpNwCozZBPBwLiPCplifWHStJmXfiV8SqPHeZyEjHj2BxKmddoxkbzMJoKqhoWuwruJZogQ14nWW1LHLYN1sSZeneq2eRwx7h7UfNNJ-IKiEhwcWQ60vXv-uB-TJ2hbbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AKz3MQhSfPAEXdo9zx3OPcy7teN_9r7yjSFWqHaZ3TeWemGA7jL36u0Es7lZrm2IEarPEcnOuz7A4zukVwuhUL6idHFr2YS2PagPamseP2sw0x4zw6kVdJ82jLViUt5daa6R_6Pio2ebXyh3LD-YRf_lqGguGBJ7Yzaqtd7EtLFNFGc--_ByW6rNSm_QMXo_wTlBgqBElFGoFW_BXVAC2hWuCOSnsyFH1eFKJKjpNwvCplTSqEaJ8v1LcQrHuPHkYj-PNN5XevH9Z5tEgclpmILSse7j-k2gm1rqJdVgE56uyjIa-RX2QVLAERAHRKJLbMhNqWtJ-LAMUdfef9vwXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده در منابع حکومتی با شرح:
تصاویر هوایی از حمله آمریکا‌ به پل‌های بندرخمیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77194" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: نیروهای ایرانی مدعی‌اند که به پادگان التنف در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را کشته یا اسیر کرده‌اند. نادرست است.
✅
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77193" target="_blank">📅 17:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GApIkbrR2wqgQTY2EQscQEndCHOIPWLTylVbKhcB3Sc9QRyqc5rWM1HIZ3Ct_S0XcGaemhDc5XPAXbin849KazN8jK1rpg2HDoDueZTIlX9zTgKqh5Sm9_n9vWvmmJSGs06Tr4H2Nii8__MzE7q094FaR95MpQaok0O9g9yIx-jlftjGkdm4NocpaJpM6OUrDRK1z282pN8sZisnFXDnpu0GhNLyQGfeGno-gx1KJusHWBIhPYZaY5wqNeuzQLlxDsq39JKPaV-j8KuoR86IheVPLPMjtFNf3r8zdUoUtaVq74me3Le-lSFtgdBlEIgJKcBvfN0MoYYAkP62PEm9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه دور تازه درگیری‌های نظامی بین ایران و آمریکا در خاورمیانه، روز جمعه ۲۶ تیر قیمت ارزهای خارجی در بازار آزاد ایران بالاتر رفت و نرخ دلار به ۱۹۱ هزار تومان رسید.
وب‌سایت‌های اعلام نرخ ارز همچنین قیمت یورو را بیش از ۲۱۸ هزار تومان نشان می‌دهند و بهای پوند انگلیس نیز از ۲۵۶ هزار تومان گذشته است.
از سوی دیگر، قیمت سکه بهار آزادی در روز جمعه ۱۸۰ میلیون تومان و سکه «طرح امامی» به ۱۸۵ میلیون تومان رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77191" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPheN0SjPI6wtGNXppviBN1Gsaa_PpHdKnr7E9nZ1aCHTVUCYouHV24wowPpNP73XGyYL0GLY3la8vuWhEE-3hsRIcVJxN4E4NjQqxjLqZpzoFSUi1o0NXGN31QboB3OZLZJhSqDE_GFmsSbspsbYcoSEYFR0dt8C4MwkktRCkZ4Qw_Je2Uuc5N702_AGmETZGApXFGe46rSVfVqcuMn0BpcmEq2WmN1ul3X5nsG_8qDPNHR3BAzt-KXFrjdTg77dI3PuqnmdLGJNZN4GOxK9y765CFN-8n17cWD1i9BlTLxZsx-xJh36Sn6WTW1XmrBN9yWMjx5aY_Keu4XJoyO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق، آب و انرژی‌های تجدیدپذیر کویت اعلام کرد در جریان حملات جمهوری اسلامی به این کشور، یکی از نیروگاه‌های تولید برق و تاسیسات آب‌شیرین‌کن هدف قرار گرفت و در پی آن آتش‌سوزی رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77190" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFTs2lqBmd19vbnyjEbc0YieH_BAMHIIeqsXXf4s4GiYDiKCZ_Ti8mL_p4KPFZDojKkcSo0jH9JyquZmlKVYGkTY1c65qHuor8YMAybORXE9Nqe4rX4zLsg3Hw5wvkdN7Dzb8OJaQr2Dg8AemZ0HXcqGXCuhDYZXrj9XVTNh9kif4aTF293pz8FBbaGST54nzUwl697u4AwhnYIje2UpHxVzGBBsNc01TiidOloWNxo8WD6pBMF7fYV1p0kb3RxtjaZsZtLvLmKbY6B_rJJMOY-STlZ_YvvQwzrVlJq4BHeAvDN-Yn98HaSYFxHfdDbtqm8pCD_n_fwsZMHnEYlblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی و امنیتی استانداری هرمزگان می‌گوید که از شب گذشته تاکنون، هشت نفر در حملات آمریکا کشته و ۱۹ نفر زخمی شده‌اند.
پیشتر وزارت بهداشت ایران اعلام کرده بود که تاکنون ۳۸ نفر در ایران در حملات آمریکا در تیرماه کشته شدند.
بنابر این آمار، در همین مدت بیش از ۴۰۰ نفر هم مجروح شدند.
دور جدید حملات آمریکا به ایران از ۱۶ تیرماه و در واکنش به هدف قرار گرفتن چند کشتی در تنگه هرمز آغاز شد؛ از آن زمان، ایران هم حملات تلافی‌جویانه‌ای را انجام داده است که می‌گوید هدفش منافع و پایگاه‌های آمریکا در کشورهای منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77189" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=UA67V4zJxu-1o3Nk7zvEDQ4ZPGzDSD5JT6YfVSqcZpgLmkUZx3aSA4vOhH_WHWokHsjTrXgKdaJPLUbitYxxUWofCF-Tk5AHfr005jOjGLIVdmwdrovkIAsZeVLP7i0BjUAJr0sKkQMf7q_Y8lXNbbAy_aBiAky-R8Clsx2qvV6NauLlB1KFMIM27HZSYQx3aDYzB9--2C67mgNqwyF70az33L0lZV4BkMQdd6qaZ6swnveqWgdt3b7qJGO8lhVJLyEe2NULCj8DA2uvUxZky3tn9w_xKmeQLrwTkR3A6ljJAy8IBKJlxdOG2PFSUAEiNld-V0W3HT64_jID-dPASw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=UA67V4zJxu-1o3Nk7zvEDQ4ZPGzDSD5JT6YfVSqcZpgLmkUZx3aSA4vOhH_WHWokHsjTrXgKdaJPLUbitYxxUWofCF-Tk5AHfr005jOjGLIVdmwdrovkIAsZeVLP7i0BjUAJr0sKkQMf7q_Y8lXNbbAy_aBiAky-R8Clsx2qvV6NauLlB1KFMIM27HZSYQx3aDYzB9--2C67mgNqwyF70az33L0lZV4BkMQdd6qaZ6swnveqWgdt3b7qJGO8lhVJLyEe2NULCj8DA2uvUxZky3tn9w_xKmeQLrwTkR3A6ljJAy8IBKJlxdOG2PFSUAEiNld-V0W3HT64_jID-dPASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: پل تخریب شده در کهورستان شهرستان خمیر استان هرمزگان
بنا بر گزارش‌ها شب گذشته، پنج‌شنبه ۲۵ تیر، در حمله هوایی آمریکا هدف گرفته شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/77188" target="_blank">📅 08:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استانداری هرمزگان:  ۵ پل مورد اصابت قرار گرفتند
خبرگزاری فارس:
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔸
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔸
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
⤴️
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/77187" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hmeS6yVFsfk-jmVaqnPiKyRoJ3WbIXSzPhNoUwIzRlMboVpd9xMapRNzHNycw6IRLBxVtJNo3X6Zcca_oMU2BOI_brn1H6Wj2QcPYb4IrHFJqqKXVsKC1f28ibPGFLo-1uPN8wCGPv_bXYdEPVI-XUZduRqKnEO1DCRhBuIFpPxuJ4qP0evdDiBMv7mKB5InM5vSo843M9dqC_vn3EMUAujneCVbhXUqQjkX0SkagZpMeQH0rj65SogCM57XEra1ch-h87HFFxSlAOj6C_T_niid7mq_wxdJ0Y6OUKipKTDe0i2QATbI5O8UBf8pIYSK1eiWgPbMIcCKmHnequzq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/907635e197.mp4?token=V1GJZ8ilsU3daWKZV57OC19CWk6Q8X4IUl0jbOijA5t5rj-rpXHzrmfek9bJyXiwkAyG3AsJB_3guwt_BUZ7P9WFMWRuWdwAcaJ8oDnEuAlWHf1WO9cMJVmUoD18pMDsB0o8Vca1YgyIyfqDb5IpFVE5yciQhd9ZytRGA3Vi9SHyBxtwpAvdwmYpXwQz3qzH9jrPw5e--l_FtS0U9Pg1zk33d5hB3_lHq87JCI3aWD_-wGiLrXuWg0NtR01-UffbwONSDsfn2KKxaH9kXLPfXQQDQetOFm2QAG_u-91BAXokghHL2LmYRCC1qZF8TwfhYCsUZPoKLObKqZIWulV2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/907635e197.mp4?token=V1GJZ8ilsU3daWKZV57OC19CWk6Q8X4IUl0jbOijA5t5rj-rpXHzrmfek9bJyXiwkAyG3AsJB_3guwt_BUZ7P9WFMWRuWdwAcaJ8oDnEuAlWHf1WO9cMJVmUoD18pMDsB0o8Vca1YgyIyfqDb5IpFVE5yciQhd9ZytRGA3Vi9SHyBxtwpAvdwmYpXwQz3qzH9jrPw5e--l_FtS0U9Pg1zk33d5hB3_lHq87JCI3aWD_-wGiLrXuWg0NtR01-UffbwONSDsfn2KKxaH9kXLPfXQQDQetOFm2QAG_u-91BAXokghHL2LmYRCC1qZF8TwfhYCsUZPoKLObKqZIWulV2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از 'پهپاد دیده شده در آسمان
#چابهار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77185" target="_blank">📅 05:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=gUIZ3nqrJGOy59GRqlMapn7ZbyMOSymCvZ59e1cSOnH8QnMD2oIP9Oauuf85Lqs2LnOQ-x1ZmtZZ-HrooFl7lYrlPPCKRot4ddZlNGb5nxvlQRkDjM25FTmu3QiI00wRjZ4PN3q5VAP5pLmPn1ehuqtJUS6oN5IFyF6nGRG_7_2y_e9qU_aMRpS6aCJBh7qcXnqUAuOEB9TBuAqwxbOJh-nt1tnZQLc0IxHsND7tblGdYK8ORz9e_WaOzjv2T-famy6AnIfIL_JeOVIhv0PGNcrM0f5r3h6x2c9yLBfWvZw1p5DIbK4dNEhxAV7EKF4wBFXYlpIf088w_4LHalhjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=gUIZ3nqrJGOy59GRqlMapn7ZbyMOSymCvZ59e1cSOnH8QnMD2oIP9Oauuf85Lqs2LnOQ-x1ZmtZZ-HrooFl7lYrlPPCKRot4ddZlNGb5nxvlQRkDjM25FTmu3QiI00wRjZ4PN3q5VAP5pLmPn1ehuqtJUS6oN5IFyF6nGRG_7_2y_e9qU_aMRpS6aCJBh7qcXnqUAuOEB9TBuAqwxbOJh-nt1tnZQLc0IxHsND7tblGdYK8ORz9e_WaOzjv2T-famy6AnIfIL_JeOVIhv0PGNcrM0f5r3h6x2c9yLBfWvZw1p5DIbK4dNEhxAV7EKF4wBFXYlpIf088w_4LHalhjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا حملات جدید در ایران را با موفقیت به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا، تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساند.
نیروهای آمریکایی، از جمله جنگنده‌ها، پهپادهای رزمی و ناوهای جنگی، با استفاده از مهمات هدایت‌شونده دقیق، ده‌ها موضع نظامی ایران، از جمله تأسیسات پایش ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی را مورد اصابت قرار دادند. این ششمین شب متوالی حملات آمریکا علیه ایران بود.
سنتکام به دستور فرمانده کل قوا، به تضعیف بیشتر توانمندی‌های نظامی ایران ادامه می‌دهد و این کشور را در قبال حملات اخیر به کشتی‌رانی تجاری پاسخ‌گو می‌کند.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77184" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lcd3RHgqn9VEJnIfKTmMZz7Z3iGzOElSQzjghOOcU8wYBJPLmaV15rTDQe_KUdNiDNScZsNG8oWOzfpbyt_FG3qYDcgwfFwFk7va-4CcxrFvm3qeN93gkZe4f1RXtpkxshLpaRVJnqiArg55ULUFo3H38QDkMRhnBeX3dDzI8Xv0n5CG2ynRbnNYFyTaIR92B9bb3Fj2HtG1qVIEW08-rC2AUqTrfINeDXlMhav-syrzsETg2dPrbrjSh2BDRmMjcrJKR75LIS0jYQUxEOwX7vlC9VHLTQoIO4NZnKVNdeKTRDwucuzj7Nb98-hP1Rt8lAA-YOVVmzRVHkAIJNTXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: 'لحظه انهدام برج مراقبت دریایی چابهار'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77183" target="_blank">📅 05:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RwTfFuTRKEc7sTcWDZ32gqtfummrY8LpjF4Z0wvvTujjFcxoEE5e1tDQPKCFR4qrdH35svBhMFNzGT2Qy4R99S4W5D5N2J9Vja2EFgPH3jz76BInvpdnTzwToCnzXU7szTNIv00BgxvPmV21Q8f9S_iDTnadbcJBhJXCdUv2UFFYoq1PCeoOZCXb89nFJOEzcnMhn5IfxPZFNbK9Vx_QyXIF6fyXP9Bh_kU9EEqXnNjcH_ueqH_J8fXdaviwD8Am9-F5lE6TAkPrfyqozGsMkS4OEFFLqzbusie-D0TlBsYvZBpQmydSuIZg-56jqblUQk-FgHCM3ZaXf6AM-04wNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس و پیام‌های دریافتی: در حمله اخیر آمریکا به چابهار باقی‌مانده ساختمان برج مراقبت دریایی فرو ریخت.
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77182" target="_blank">📅 05:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V30PITXoUS2vhRdv7GTmTE1C9dCHB-lEDjYhnmGLcZbpnYL4RUdYH6JUW4ZDgffS7FCnBfMZvJBXuwi4CTwfavkofLxa_Gid9sq3FpE75gfkmYODQwIc_FTq1keypvkRM0-Yp8DBXL4S-QPEupgAI9ofdyFbYLi2wSBwz_Gl64QUhq5FyQeWTDHHpH5_wi0qiuQ-P7LngBS1xGrjMWD1tzC2I66RHgAbi1ulnFxvl45zJQk7uohkcTljlgW6VDBdekT744uXhvSvAk_snZtVLHphZYPOWPeKolc0WW9x9_Qtx19hotG3UqyvhTK3EzD1siW1u1ve1WFU68K3rvs5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=hyY1hZz-UOSeaYTEK71klTnuAdvDwM9ToJqArC2WFeE9Aj-OFWySfhpy8CIeOfUXyx1c3bmkfdxRwBF-e9Ijqw89O6_GCggyt8n5WmoUuLZ_eCLK3F3SkY2VznJyXYoCUTpknZjdH-u9-ZslpVaXfVumfdRo629OR_bOg-lIT7rg9CU6fz8dh06aSnyAzGNCVd74xfgYIyPHV4ZdXjiwz9qjox_lj4XIw9SJpphP_qWNDfZpxc7M-xiEfnLSlx_ehj352e6TRbRrlS--T2rpX5WlxR6YdwAeKs-qfHtC-37jnpXT4zKFixY4lTEfzmXFTtahI_WEYGPF7-JPlVZweg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=hyY1hZz-UOSeaYTEK71klTnuAdvDwM9ToJqArC2WFeE9Aj-OFWySfhpy8CIeOfUXyx1c3bmkfdxRwBF-e9Ijqw89O6_GCggyt8n5WmoUuLZ_eCLK3F3SkY2VznJyXYoCUTpknZjdH-u9-ZslpVaXfVumfdRo629OR_bOg-lIT7rg9CU6fz8dh06aSnyAzGNCVd74xfgYIyPHV4ZdXjiwz9qjox_lj4XIw9SJpphP_qWNDfZpxc7M-xiEfnLSlx_ehj352e6TRbRrlS--T2rpX5WlxR6YdwAeKs-qfHtC-37jnpXT4zKFixY4lTEfzmXFTtahI_WEYGPF7-JPlVZweg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: دود انفجار حمله به مکانی در چابهار
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77178" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ec77aLYI8pyThg55m_f3TG2B3sLY1TAxXkJy7COLY89cTYkDW6bMuUUOLtH4vsaxGlX9ZDAW3nCggABVojAOIdcCCppb0lo3FPZsncITBwQp1GckuEWwzS0uF0XcLnyRd1sJnlyeMtOfuloTiFGsJuNWov9xowoHoGWKs_SGSwBiydkcjxdMkPW12Ncwers4CiKfjaiyPpCdXnYslvcCyR5oBUhMNK5ABIiJOYrdmTw6_qpR1pVmwv6TGrgxiklDbnHZtdvp8ZuFuhsFgVZYrqmPnrX7lgyQmTpt0yNBmd5N9QoPtczQ5DNm8_-NzCM-FyVObk0ND5IY3JB3pj2EtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری هرمزگان اعلام کرده حمله به پل‌های گریوه و کهورستان در بندر خمیر ۷ کشته و ۹ زخمی برجا گذاشته است.
خبرگزاری تسنیم گزارش داده که پل‌های گریوه و کهورستان که بخشی از مسیر اصلی ارتباطی بندرعباس به شیراز محسوب می‌شوند، هدف قرار گرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77177" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxDO4Ph7y0vRptKHsUSkgVUPYL9DhW1vWWSIPlJOD-1pwZ5wY0ywdYY5cBmerFEDbpxIjFPI6QnWO86lPXDTQFb4fd3sT03MIF4yx--BXd_mXi1QX4_Q0JTgtszBp1MsMPiwyjpnhnIRbwNE9A31Ess3-o-vRho-iomkj-uu3MqNJyIQRIm6pCAEGtCwWEXhoEtPjr4HdBSc2IwT_2j7KM9pnzSL9YUVSqJUpiFwjpzQXIBUutXooYAUqVCz5RJQ8UI_OlxckMctfYtpQ2wKVIEjYWw0zc40MbwSAzomMP2-XGXpWL3D3PH2h9SvGebcBOeC-_hysEM73q8wNVcHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گزارش‌ها درباره دریافت پیامی از جمهوری اسلامی که در آن استیو ویتکاف و جرد کوشنر به سوءاستفاده از مذاکرات و کسب سود از اطلاعات محرمانه متهم شده بودند را تکذیب کرد و گفت هرگز چنین پیامی دریافت نکرده است.
این واکنش پس از انتشار گزارشی مطرح شد که مدعی بود جمهوری اسلامی در پی مذاکرات سوئیس، ویتکاف و کوشنر را متهم کرده بود از نوسانات بازار ۹ میلیارد دلار سود برده‌اند و خواستار اختصاص نیمی از این مبلغ، معادل ۴.۵ میلیارد دلار، به حکومت ایران شده است.
ونس این ادعاها را «کاملا بی‌اساس» خواند و گفت ویتکاف و کوشنر از اعضای مورد اعتماد تیم دونالد ترامپ، رییس‌جمهوری آمریکا، هستند و ادعای سوءاستفاده آن‌ها از اطلاعات محرمانه «مضحک» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77176" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پیام‌های دریافتی:
درود وحید جان چابهار سه چهارتا موج و صدای انفجار و صدای جنگنده
۴:۳۷ دقیقه
۴:۳۸ دیقه چابهارو زد
چابهار زد
سلام وحید جان صدای دو انفجار ساعت ۴:۳۷ دقیقه در چابهار شنیده شد
چابهار ۴:۳۸ پایگاه سپاه امام علی و اسکله سپاه توسط جنگنده ای که خیلی پایین پرواز میکرد بمباران شد.
🔄
باز هم زد
دوباره زد الان ۴:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77175" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام دریافتی 'از قطر':
ده دقیقه پیش صدا انفجار و پدافند، دوحه.
Still no threat cleared message.
آپدیت ۴:۲۳:
Security threat eliminated.
هم‌زمان از تبریز پیام‌هایی درباره شنیده شدن صدای پرتاب موشک دریافت می‌کنم. قبلش هم از شهرهای دیگری پیام مشابه فرستادند
.‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77174" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=jGNAlSufZKw5JHrVwE5HBb5yJ7rJR1BgMNwXNbB4rSGG4YussVvgod-m4qoSlXc--B9u-dU_b3XB3fTHdA26beO7JCG5SDmR9A0LcHcFdOwoMXimOuMj89F37EjGA7zEA1Ar3XSofYOAp-UpCDW26sHMvGe8zLjENlNTlOnP9K1OSg74G3G-eEM0fhvyOBxGdot8-i4izXH7Y3-7h598BKW-6g1CFuwccIxRatIc89ucpyBAJTvm7AEBSQXeaoGX1ACdMvHVrB_4b_Bu2IMQcN3URUmiG3dBL0Vsq8HTnvalmjOBfnXdNNz_d-EpPoz_7yfhbvE1qUBo2amr3IsqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=jGNAlSufZKw5JHrVwE5HBb5yJ7rJR1BgMNwXNbB4rSGG4YussVvgod-m4qoSlXc--B9u-dU_b3XB3fTHdA26beO7JCG5SDmR9A0LcHcFdOwoMXimOuMj89F37EjGA7zEA1Ar3XSofYOAp-UpCDW26sHMvGe8zLjENlNTlOnP9K1OSg74G3G-eEM0fhvyOBxGdot8-i4izXH7Y3-7h598BKW-6g1CFuwccIxRatIc89ucpyBAJTvm7AEBSQXeaoGX1ACdMvHVrB_4b_Bu2IMQcN3URUmiG3dBL0Vsq8HTnvalmjOBfnXdNNz_d-EpPoz_7yfhbvE1qUBo2amr3IsqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منابع حکومتی از
محل حمله آمریکا به پل جاده دسترسی بندرعباس – بندر خمیر و جنوب استان فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77173" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ihj1jika0Ztj9PxG9LYv0-tpyWGwa1Dvv0P13my0DgnQnyiDxd8YN7hQrhAqE1RWtrhDjaI4wR6qZyFlpRgzJhZ3w9JmU4GOVmvs53wr4_iWW_cfOdX2FzxUveMOyhhuWNP-bioVNvhRbTrcLtw4s23WOyph6cPLwWp-b4lkaJ02vhoCUM50dXQ6YuNAFJT7J398uQ3qe1OfDKMxX-IOO5fasE_JUlaWuRW-3xNcCBa87MXiAiDs5tFG_FW58P5Kj8-V9aQsA8L52bX4K1X1skC6f0sdlRuZcoB77vx61MoGCtBomCmapSWKossfif-yPAPcUZeHxUaQHRsuHJB0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به روزنامه وال‌استریت ژورنال گفت ارتش ایالات متحده چندین پل در ایران را هدف قرار داد تا مسیرهای تدارکاتی منتهی به بندرعباس و پایگاه دریایی واقع در تنگه هرمز را قطع کند.
آمریکا می‌گوید جمهوری اسلامی از آن پایگاه دریایی برای حمله به کشتی‌ها و نمایش قدرت استفاده می‌کند.
تلویزیون حکومتی ایران نیز گزارش داد که چندین حمله به پل‌هایی در بندرعباس و مناطق اطراف آن انجام شده و بزرگراه‌های منتهی به بندرعباس از استان‌های همجوار مسدود اعلام شده‌اند.
رئیس‌جمهوری آمریکا، سه‌شنبه ۲۳ تیر در مصاحبه‌ با شبکه فاکس‌نیوز گفته بود دامنه حملات آمریکا به جمهوری اسلامی در روزهای آینده گسترش خواهد یافت. دونالد ترامپ افزود حملات سنگین ادامه خواهد داشت و اگر جمهوری اسلامی وارد مذاکره نشود، هفته آینده نیروگاه‌های برق و پل‌های آن هدف قرار خواهند گرفت. او تصریح کرد: «تمام نیروگاه‌های برق و تمام پل‌های آن‌ها را از کار خواهیم انداخت، مگر اینکه پای میز مذاکره بیایند.»
ترامپ در آن مصاحبه همچنین تاکید کرد عملیات نظامی آمریکا علیه جمهوری اسلامی ادامه دارد و این حملات «تا زمانی که خودم بگویم کافی است» متوقف نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77172" target="_blank">📅 03:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=m06sWA4M92m-zTsdGe49I7J9r_sgj5f-tiZ5e_ZIbvrvKlxubyGEV_PU7EEhCnvWezaXH-aj4Dz3fe1QvbVIgtKsukXIVkHy02LFdBkX119WoPGD78tkZNTr8wyz-jQjO0cU2Xrn6mjuXXaymM4tigy6tn4R_gYXQ7cUBLkYBdy9VGfuEg4g519YfnPuQoUu8qDpvZ82xv9bwcv_9y2xdHRuX5U-ztlW0gHIOMxILQFg6IXejC9OBx2qNTqR8gb4FkjADylP77C-idoeLqUfPd9tzdY6n44TEsCU4fL5oHNoo2y3QOAn1eePzkYpyU97A0ixl69MI7BecIJ84hBTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=m06sWA4M92m-zTsdGe49I7J9r_sgj5f-tiZ5e_ZIbvrvKlxubyGEV_PU7EEhCnvWezaXH-aj4Dz3fe1QvbVIgtKsukXIVkHy02LFdBkX119WoPGD78tkZNTr8wyz-jQjO0cU2Xrn6mjuXXaymM4tigy6tn4R_gYXQ7cUBLkYBdy9VGfuEg4g519YfnPuQoUu8qDpvZ82xv9bwcv_9y2xdHRuX5U-ztlW0gHIOMxILQFg6IXejC9OBx2qNTqR8gb4FkjADylP77C-idoeLqUfPd9tzdY6n44TEsCU4fL5oHNoo2y3QOAn1eePzkYpyU97A0ixl69MI7BecIJ84hBTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام موشک از شهرستان جم استان بوشهر فرستادن
سلام همین الان از جم موشک بلند شد(۲:۵۶)
۵عدد موشک از جم به سمت خلیج ۲/۵۷
سلام وحید جان از جم موشک بلند شد
سلام همین الان پرتاب موشک از جم 2:57
سلام وحیدجان الان ساعت ۲:۵۷ از جم موشک بلند شد نمیدونم به سمت کجا
همین الان ساعت ۲ و ۵۷ دقیقه موشک از جم بلند کردن
ستاد کل ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی جمهوری اسلامی هستند.
ارتش کویت همچنین اعلام کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری اهداف مهاجم توسط سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی صادرشده از سوی مقام‌های ذی‌ربط را رعایت کنند.
@
VahidOOnLine
پیش‌تر:
وزارت کشور بحرین اعلام کرد آژیرهای هشدار در این کشور به صدا درآمده و از شهروندان و ساکنان خواست آرامش خود را حفظ کرده و به نزدیک‌ترین محل امن بروند.
این هشدار در حالی صادر شد که پیش‌تر جمهوری اسلامی اعلام کرده بود پایگاه ناوگان پنجم آمریکا در بحرین را هدف حمله قرار داده است. مقام‌های بحرینی تاکنون درباره علت به صدا درآمدن آژیرها یا وقوع هرگونه حمله جزییات بیشتری منتشر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77171" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce4JML01qZ3kHHxpCunhIxTkJ5ZE2O3a07g795rksxx9uoXGsUogkWMNxL82DdSOirDPRluQfNc1b4ki4SYLcjPgBvVGk9be40jVjK7H2DHvoAwzWgMeKq3HdaRkGJgHPrdaJLEtVq738Es3kqUBrr0WIAW8mQ3fD8NFGwDfe0LK7civ6RPVAOP6Vc2euVc-mG2G2PJ7aZXl8H85HRVjTZc3zaAxTX1BFSoA4nEqg1XiKV7N4R8W5K4EGPXo0RuGGvVaLWqhXCpIuCECjkFNBM3S2DlhwZnATgnfyCyZNLVK3sDfumsmAJ18vuYjD4RgX27CuD1bPYbGOUD9u33I9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی به نقل از استانداری هرمزگان:
در ساعت ۰۱:۳۰ نقاطی در حوالی بندرلنگه مورد حمله آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77170" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=LUosPU_9WhfZFa-W6159OEK1VNv6Hrez28D4IoLnhnf5nzDzSfMGirOLUyk1KX5mUlflbqKQxltVJzXVfQ8W3kyEd7X7uniTQMR9g4Sucz1RKUY_bDkC1DxTuzu8LB3kInEiZubzn2UpB0U5l-nn9hSeTBGqcnBvp_ftVUmIXX3IWY5TKiDRufdWR-iRVvZvEnUoJMaMzCCoGFeGI-PfHaiULDGIhI9Cfp8OaeW84MZ133d_ewV5QMATyfNNYLiUsy2KVQF8tizPqA07xaFkOyzBByVwJlIDF8O2TABF3CMIAch-N0BT4b3-bBmcxjvmK1UW33URl4njwW4CDqrsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=LUosPU_9WhfZFa-W6159OEK1VNv6Hrez28D4IoLnhnf5nzDzSfMGirOLUyk1KX5mUlflbqKQxltVJzXVfQ8W3kyEd7X7uniTQMR9g4Sucz1RKUY_bDkC1DxTuzu8LB3kInEiZubzn2UpB0U5l-nn9hSeTBGqcnBvp_ftVUmIXX3IWY5TKiDRufdWR-iRVvZvEnUoJMaMzCCoGFeGI-PfHaiULDGIhI9Cfp8OaeW84MZ133d_ewV5QMATyfNNYLiUsy2KVQF8tizPqA07xaFkOyzBByVwJlIDF8O2TABF3CMIAch-N0BT4b3-bBmcxjvmK1UW33URl4njwW4CDqrsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
فرماندهی مرکزی ایالات متحده تفنگداران دریایی آمریکا از یگان اعزامی یازدهم تفنگداران دریایی، ۱۶ ژوئیه در خلیج عمان برای راستی‌آزمایی، سوار نفتکش «وِن یائو» شدند.
تا امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش داشتند محاصره را بشکنند تغییر داده‌اند، ۱ کشتی را که از دستورات تبعیت نکرد از کار انداخته‌اند و برای اطمینان از اجرای کامل محاصره دریایی جاری آمریکا علیه ایران، وارد ۱ کشتی شده‌اند.
تنگه هرمز و آب‌های اطراف آن همچنان آزاد و باز است، به‌جز برای کشتی‌هایی که تلاش می‌کنند «دیوار فولادین» محاصره آمریکا را نقض کنند.
🇺🇸
CENTCOM
ویدیوی دیگری رو هم توییت کردند. میشه از ثانیه 00:20 ویدیوی بالا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77169" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=gQetnbZDvwHKKov-sxQqfbBZDpH1s8PvM2x3VVSh6eqb4vAiWuMkGcrqvjZg9QhYdFpvG0-Y_JW33sn_RDondjI78g-I_J2zh8ClI6e6D9xoXbbKnT_jDXYZnzkXNzknUMIOqaIf7XpVr2qkI3psGalf1qEkvob8jRFZcDuw_C0PpHZ8ZP9KQyJaua40S1LFl9z0Gu4fp6Z55cr4uT2eb5vmmnC5pkmCv1VezK22Zbo6Ny9_dL_gokJ_S4LQGwFSYLr3_m-hAUDj5ixLZJtGewCXQPCJpNniJTfz0x2UP7nADg1n1GROHW1La8-6OgNuFGFnH7V1q65Blkl9ekfWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=gQetnbZDvwHKKov-sxQqfbBZDpH1s8PvM2x3VVSh6eqb4vAiWuMkGcrqvjZg9QhYdFpvG0-Y_JW33sn_RDondjI78g-I_J2zh8ClI6e6D9xoXbbKnT_jDXYZnzkXNzknUMIOqaIf7XpVr2qkI3psGalf1qEkvob8jRFZcDuw_C0PpHZ8ZP9KQyJaua40S1LFl9z0Gu4fp6Z55cr4uT2eb5vmmnC5pkmCv1VezK22Zbo6Ny9_dL_gokJ_S4LQGwFSYLr3_m-hAUDj5ixLZJtGewCXQPCJpNniJTfz0x2UP7nADg1n1GROHW1La8-6OgNuFGFnH7V1q65Blkl9ekfWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت چند ساعت بعد: صدای چند تا از انفجارهای در ویدیوی بالا
پیام‌های دریافتی:
وحید جان همین الان بوشهر سه تا انفجار
۴ تا افنجار شدید بوشهر
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
بوشهر سنگین دارن میزنن
سلام وحید عزیز بوشهر همین الان پنج تا انفجار رخ داد
بوشهر 00:55 صدای 4 انفجار
بوووشهررر همین حالا زدنن و دارن میزنن
همین الان بوشهر رو زدن ۲-۳تا شدید
مجدد ۴-۵تا
خیلی شد
حاجی رگبار بستن
سلام بیشتر از ده تا صدای انفجار بوشهر هنوزم دارن می‌زنن
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
۶ تا دیگه پشت سر هم ۰۰:۵۶
بوشهر ۰۰:۵۵ بالای ۱۰ بار پشت سر هم زدن
سلام آقا وحید همین الان ۱۲.۵۵ دقیقه به بوشهر حمله ی  شدیدی شد منطقه بهمنی و من بسیار در خود ترسیده ام.‌
بوشهر صدای خیلی مهیب
۱۰انجار بوشهر الان
۵۶دقیقه
بوشهر
۱۲ تا انفجار شمردم
ساعت ۱۲.۵۵ تا ۱۲.۵۷
سلام وحید جان بوشهر ۶ بار زد خونه لرزید
بوشهر ۱۲:۵۷ چند انفجار خیلی مهیب
بوووشهررر همین حالا زدنن و دارن میزنن
بیش از هشت انفجار
همینجور پشت سر هم دارن میزنن نزدیک ۱۰ تا بود پایگاه دریایی دودش پیداست
بوشهر داره پشت هم میزنه
😭
😭
😭
😭
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام وحید
حداقل ۱۲ تا انفجار پشت سر هم بوشهر
سمت پایگاه دریایی
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام، صدای انفجار شدید بوشهر
ساعت ۵۵ بامداد شهر بوشهر محدوده پایگاه رو داره به شدت میکوبه شاید ده تا دوازده انفجار
سلام آقا وحید ساعت ۱۲ و ۲۶ دقیقه شهر بوشهر ۱۲ بار زدن صدای انفجار شدید بود
۱۲ تا صدای انفجار بوشهر اومد
پایگاه هوایی بود پشت هم رگباری
انفجارهای اولیه نزدیک فرودگاه بود صداش نزدیک بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77168" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gNCuhFqVue_GRaPbneM6ytPpm645h4fCIIDHfrF5p-Fg8zbXMqxG8YSYg4v44luIVqlP7dEIII554khdtqE54zigKCznxP_zauAE7LAr_LV5HT9rNFzcq2_N2uMF7WxMTVHF_9hUc_vTwGRuLxchgdfiE6Ca6buJuXlJykZh739W-W1JrGidVxWRC8DJ5JnthFbtT1sVvoTGWhyV1emfNv1SqLrLztmMX6UYhbR1h4Ndxk8YLQFfVnI3eXKkmns-_xFGx4lP3LivSkFwKxDzQCRVsF3S9Pbb9crEDTcECkCARnC20IT-t6vN9xvQDBs4lb737j7BoQPAWei_9sdP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: 'پل کهورستان در شهرستان خمیر استان هرمزگان'
که گفته میشه با حمله هوایی آمریکا تخریب شده.
پنج‌شنبه ۲۵ تیر
Vahid
فارس به نقل از استانداری هرمزگان:
علاوه بر پل کهورستان، پل گریوه نیز در محورهای ارتباطی استان، مورد اصابت قرار گرفته است. ۲ نفر کشته و ۴ نفر زخمی شدند.
تسنیم:
در شهرستان خمیر به سه پل حمله شده که مهم ترین پل، متصل کننده بندرعباس به لار در استان فارس در محدوده بخش کهورستان است.
صدا و سیما:
استانداری هرمزگان اعلام کرد محور بندرعباس - خمیر - لار و محور کشار - کهورستان نیز مسدود شده است.
📍
میگن یکیش این بود:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77167" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-6fou5Dhv1BeVQ99Med18l5ZfESr_J1UtSbHx9Q7A5yqvYROjrdo__vhxk05sjKfroB-K6voqmEryKNPj2jMB9sSgFqzoGrRQcecezgDBfpqgTwS2pBZ8LKbNyiA_ovTebLV34Bi-T3XBD-tdAkcW-BKgGnUHUr-Pw9w20JbpGw3RQ-1Xb4w-AzJmCiB1e2aiwPeNGbpFwiw3IH1kJ8aLFt8-HtFzmMBQ2wgufgoqt1QDhstYJ3HihiqLZ5yIK2ie2mVBXEw6mmasH6IBmZZcSGAZ90zS2RB0sp5lLGILyKFuapzxZxKbXBOh33ZU3Prz9oniW6m9ZkvimQWIADeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77166" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/713dc65855.mp4?token=M90amSDqBbR1whx4rcPh8t3OA34PitA3iiDtAy9iCXbgYktujG7B6sSpZbxk4YpuDwtpikEjbXB5tpa5SW0vGfbPrTFB4NTvXbiX0yZ7DOYZA0SwoMOjj_hk0r-UM4pZA1MKHUhcFK8Xe5LGZciSru0ssNWyFYpbmUtDT6pA6OctPhCfFwp-TdSQRUzkwgU18_OibGkf5a3VS7yVTFGB5XJYpSacKf89CxdvVMrca1PrUtApFlHzx3nF1uwzZWf3U3b6o837RWjNjLDUxxMw_AszNPoTCFkqTyJZwQaoTjk_INed-NFRWw1BnwDbqLBIxUItLT8yVwFr0tpgK85N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/713dc65855.mp4?token=M90amSDqBbR1whx4rcPh8t3OA34PitA3iiDtAy9iCXbgYktujG7B6sSpZbxk4YpuDwtpikEjbXB5tpa5SW0vGfbPrTFB4NTvXbiX0yZ7DOYZA0SwoMOjj_hk0r-UM4pZA1MKHUhcFK8Xe5LGZciSru0ssNWyFYpbmUtDT6pA6OctPhCfFwp-TdSQRUzkwgU18_OibGkf5a3VS7yVTFGB5XJYpSacKf89CxdvVMrca1PrUtApFlHzx3nF1uwzZWf3U3b6o837RWjNjLDUxxMw_AszNPoTCFkqTyJZwQaoTjk_INed-NFRWw1BnwDbqLBIxUItLT8yVwFr0tpgK85N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: یکی از پل‌های کهورستان شهرستان خمیر
منابع محلی: محور رفت و برگشت
#بندرعباس
به لار مسدود شد.
پنج‌شنبه ۲۵ تیر
Vahid
یک خودرو دیده میشه که احتمالا از روی پل سقوط کرده.
آپدیت:
محتوای ویدیوها به نقل از شاهدان عینی صدا و سیما!
تجاوز هوایی به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77165" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=CHgsS9exdbvBDNyuMY3YEyilaS65pj5clHBbNJ9EN9fNdtCgeVHiFojxWNMEsGopgumHfSndmzVZmyg1uU9H6ELCFK2v_SHNIVNFu0VfRDNuJBI5mMQE62tUhcQNKFweF2cI6FCgOgBJp3H4WoqFBSzod5IFLF9Zx6wBlRQd8iD6BzOchBMnb4GGlZ3QbZcieo_1uAqAGH9InolGVpIIGXLPCCMyEt2cjFwVHt5pSGyKIzQQy82DM3qXDI_xVqwYgpJJzl9NcmwUzDA7uETqtJOm_arNCJUtvw_llT9akuMplJhwCnXXtHS2dloPYF1NV8qd_IfWC6Wc334TCCg1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=CHgsS9exdbvBDNyuMY3YEyilaS65pj5clHBbNJ9EN9fNdtCgeVHiFojxWNMEsGopgumHfSndmzVZmyg1uU9H6ELCFK2v_SHNIVNFu0VfRDNuJBI5mMQE62tUhcQNKFweF2cI6FCgOgBJp3H4WoqFBSzod5IFLF9Zx6wBlRQd8iD6BzOchBMnb4GGlZ3QbZcieo_1uAqAGH9InolGVpIIGXLPCCMyEt2cjFwVHt5pSGyKIzQQy82DM3qXDI_xVqwYgpJJzl9NcmwUzDA7uETqtJOm_arNCJUtvw_llT9akuMplJhwCnXXtHS2dloPYF1NV8qd_IfWC6Wc334TCCg1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: در کهورستان
#بندرعباس
یک پل هدف گرفته شده.
صدای ویدیو: موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
پنج‌شنبه ۲۵ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77164" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=boq2r4wqGmUaS5N5blkE418kW3T-XIYAMoudLYs2xKQIhUY_NqhYPKgygJJs4zxAqrJVo-KkQG5SHSWIBMPzr_CZrbvuKj2mXa75Mf7Sq0aTRvsPYg2ShyfDbyubEj3ay87Fo7sahAZriugaX8G979x2NgkRT1RJdN3IN_KalRxG9ll4RlDBycZggnvbKwKjEstaTK3lexCoWUKswub3_ze9Jb7j_eJICQvtTqX5nudMO-xS76otfy8MBWii5bJN9aLa8iGzK42zdZyiQ4HjuiMFXG2WQP9Ag-N4iI7JPEMqkbK2CntgOjo71TMad1-eLrSiVfD3ZlEDkgNEXA5c7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=boq2r4wqGmUaS5N5blkE418kW3T-XIYAMoudLYs2xKQIhUY_NqhYPKgygJJs4zxAqrJVo-KkQG5SHSWIBMPzr_CZrbvuKj2mXa75Mf7Sq0aTRvsPYg2ShyfDbyubEj3ay87Fo7sahAZriugaX8G979x2NgkRT1RJdN3IN_KalRxG9ll4RlDBycZggnvbKwKjEstaTK3lexCoWUKswub3_ze9Jb7j_eJICQvtTqX5nudMO-xS76otfy8MBWii5bJN9aLa8iGzK42zdZyiQ4HjuiMFXG2WQP9Ag-N4iI7JPEMqkbK2CntgOjo71TMad1-eLrSiVfD3ZlEDkgNEXA5c7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: کهورستان بندرعباس پل زدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77163" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fE6J85WISixTcy7QR8ca21sPvRiKLK9DWimdm04dTngzkG6hshGZMbaQG4BCr4MrIVe_5UP6YmyQrwvM2uefaYAw3tdXtSewCnyDsMXCnEakENNjzwXSbZW6-Fb3ODaSb1dpP2q-_olIPJox5yFVwFZFiVL6T4rjmojOtQiL5FPOmmpbNNrnEFK0fr1yChwVev8UbnBuFfX2SJhwZFYs1R8TG3mxpnCmwWMZSrhuK-hUc-4oQMbahqvAYFGnGOLkg59sl3a-dz9exxvAFcO7uX2EcdHZF8IA46TF5sn1kpOcZtDuDPj4gmu95FRZQG3lHLuXdHKI8T72WfPbJE4k8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J5j-m8eLDFmwDgw10OYKXQIBrPlURc42PlHYcZMl9Ongw3nCvFJ5q_GooBBQit17tsmtlBXP9_bp1THluCCvvaBUeMXKSM40gSjZEHeJQn22Y8jNcRuSwdabyctPro0ivd5Qge2J22l-I9mqgYoV9-ha6gLb7VrajjUFTYFJMZp8qWpDO3b2YsVq5ww92OxzbbZl7DM9bXvKLIiyIdvFRGCCmg4Cge_CN40n0cls-udoYE8p_AaeYafbgNMhexjRd-YpRMunSY84t0dS881I7IRDmVW2_AkPquomnSegp0S0N0ayQBIOCZIPT1kt7LcB8GZs45wIDxZQLSWVQSA-qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=bv6Qgjw5rH3FAKTpCYJSBVIPZa_kFz6JOF_CrhyGXWOKcbx5zCriHBXNPsOlZO0gPwmQ-NgcbTrKcT8BnNHLiF-n5bWCKsqGcrEmcBm4nWdHIMgN3Vl33a43ITwegHFjC4nnQoXSCggDTg48mgEVJsNIS3G04N4d1g3ju20uCzsRyULFiDEGhFh9bZladaL6Hp9kJO26lbOhPCYBWyTSZLgVA7steAc7tN7k4CRbs8boVYgYNwa7slutjOJ7szXjWYi4GzbFOB-YjBeOhKxiZaI1F3GCn_nXGN2YQDV43fRIaKkATD-_lbZBml62X_30JHcHACEf-xsLGwAR9aB57w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=bv6Qgjw5rH3FAKTpCYJSBVIPZa_kFz6JOF_CrhyGXWOKcbx5zCriHBXNPsOlZO0gPwmQ-NgcbTrKcT8BnNHLiF-n5bWCKsqGcrEmcBm4nWdHIMgN3Vl33a43ITwegHFjC4nnQoXSCggDTg48mgEVJsNIS3G04N4d1g3ju20uCzsRyULFiDEGhFh9bZladaL6Hp9kJO26lbOhPCYBWyTSZLgVA7steAc7tN7k4CRbs8boVYgYNwa7slutjOJ7szXjWYi4GzbFOB-YjBeOhKxiZaI1F3GCn_nXGN2YQDV43fRIaKkATD-_lbZBml62X_30JHcHACEf-xsLGwAR9aB57w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: حمله به فرودگاه ایرانشهر در سیستان و بلوچستان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77160" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
سلام داش ایرانشهر فرودگاهشو دوباره زدن ساعت ۲۳:۰۱
پنج دقیقه پیش دوباره فرودگاه ایرانشهرو زدن
سلام  ده دقیقه پیش فرودگاه ایرانشهر رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77159" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9fZ_bRpNeeBqEW2aJzn6ElZzfJrvQAGR5QPOyT2j0hrGP6NUVx5tgn9PTSSa3_r2Fz9nVybEGBM3mcmvxEklJLxweY9k5zXG9Uj8Ul4Lbp_gklshJA-YuuAQ2Q0DD1NNTPEE-_8XoExIMqgcFH0FgcFls7kJbSzrIr4wlEx2aAPzJiI_MAGN-yN34dQ45q0kVqkpZJPdZ48mhzAm2bA4JOqjrUUrTWvHGaEy41R2kmLPVZOXXaEK2sfLvoc6y-L7jhUauuBiBXOVGXamf8lJXRIEfkMCAWG6d4BhoI8PrwTEs85LTdPvF1VGmjzLduhkgMNY-ZtBA7bUwdl8uiOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:
مصدومیت ۷ نفر در حمله دشمن آمریکایی به بندرعباس
🔹
به گزارش خبرنگار خبرگزاری تسنیم: در پی حمله دقایق پیش نیروهای متجاوز آمریکایی به محله مسکونی تپه الله اکبر در شهر بندرعباس، متأسفانه تاکنون ۷ نفر از هموطنان مجروح شده‌اند .
🔹
بلافاصله پس از وقوع این حادثه، کلیه نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته و اقدامات درمانی لازم برای مداوای مصدومین در حال انجام است.
🔹
روابط عمومی دانشگاه علوم پزشکی هرمزگان ضمن محکومیت شدید این اقدام تجاوزکارانه، از عموم مردم شریف بندرعباس می‌خواهد ضمن حفظ آرامش، اخبار را تنها از طریق مراجع رسمی و معتبر دنبال کرده و از هرگونه شایعه‌پراکنی خودداری فرمایند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77158" target="_blank">📅 23:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
‌
بندرعباس صدای انفجار شدید ۴ بار
ساعت ۱۱ شب
همین الان صدای انفجار شدید مرکز شهر بندرعباس اومد
سلاام وحید جان
بندرعباس دوتا انفجارر
شرق بندرعباس پایگاه هوایی ۲۳:۰۰ دارن میزنن
الان دو تا صدای انفجار بد آمد بندرعباس
بندرعباس دو تا انفجار صدای دومی مهیب بود ساعت ۲۳
سمت شرق بود
بندرعباس همین الان صدای انفجار
چند دقیقه قبل تر هم یه صدای انفجار اومد
بندر الان اینقدر شدید بود پنجره‌های اتاقم لرزید ۱۱:۰۱
سلام الان ۴ بار با فاصله چند ثانیه خیلی با شدت بندرعباس رو زدن (ما نزدیکای فرودگاهیم)
وحید جان سلام الان ساعت ۱۱ شب قشم هم صدای جنگنده اومد هم ۴.۵تا انفجار که خونرو لرزوند جنگنده تو اسمون میچرخه
باز هم بندرعباس صدای جنگنده خیلی واضح داره میاد دوتا صدای انفجار اومد بلافاصله برق قطع شدد صدای جنگنده اصلا قطع نمیشه
بندرعباس ساعت ۱۱ فکر کنم سمت پایگاه هوایی باشه.
وحید جان سلام ، قشم سمت دهخدا ۳ تا صدای نسبتا شدید شنیدیم.
بندر عباس همچنان داره میزنههه
صدای زیاد و لرزش
برق هم داره نوسان میده
ی مناطقی هم قطع شده
ساعت یازده شب صدای سه انفجار بندرعباس
الآن سه تا صدای انفجار بندرعباس اومد
بندر عباس تو فاصله چند دقیقه ۴، ۵ تا صدای خیلی بلند خونه لرزید ، آخریش ۱۱:۰۲ دقیقه اینا بود
سلام وحید بندرعباس اول برق اتصالی کرد بعد صدای انفجار شدید
وحید سلام دقیقا ساعت ۲۳:۰۰ صدای انفجار بندرعباس
بندرعباس ساعت ۲۳:۰۰ صدای ۴ انفجار خیلی شدید و سهمگین اومد
بندر دوباره زد. بزرگ ولی نه به بزرگی یکی دو ساعت پیش
انفجارهای امشب تو بندرعباس از شب های قبل خیلی بیشتره
واقعا ترسناک بود
به مرکز شهر و نزدیک گلشهر صداش اومد
بندر رو چند بار زد و برق هم قطع و وصل شد
وحید برق نه تنها بندر نوسان داشت بلکه چندتا از روستاهای بندر هم همینجوری نوسان و قطعی داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77157" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
الان اهواز صدای دو تا انفجار اومد  ۱۰:۳۰
اهواز انفجار دوباره همون ۲۲:۳۱
اهواز ساعت ۱۰:۳۱ دقیقه دوتا صدای انفجار مهیب اومد
وحید جون 10:30 دو انفجار پشت هم اهواز
الان ۲۲ و۳۰ دقه صدای انفجار اومد اهواز
اهواز ساعت ۱۰:۳۰ صدای سه انفجار اومد.
اهواز طبق روال روز های قبل ساعت ۲۲:۳۰ صدای انفجار میاد
صدای سه انفجار شدید
دقت كردين همش سر يه تايمه
😭
😭
😭
😭
دیشب هم دقیقا همین ساعت ۲۲:۳۱ زدن
اهواز ساعت 10:30 زدن سه تا بود
همین الان 22:30 صدای دو انفجار مهیب در اهواز
بازم مثل دیروز راس ساعت 10.31 دقیقه اهواز رو زدن
اهواز ۲۲:۳۰، زدشون از قطعی برق هم آن‌تایم تره
اهواز صدای ۲انفجار ساعت۲۲/۳۱
همین الان اهواز صدای انفجار اومد
ساعت ۱۰/۳۰ شروع شد مثل هرشب
سلام آقا وحید دو انفجار پی در پی اهواز ساعت ۲۲:۳۱
اهواز صدای انفجار دو بار ساعت ۲۲:۳۰
سلام داش وحید اهواز ۲تا انفجار شدید الان
اهواز ساعت ۲۲:۳۱ صدای دو انفجار اومد
دیشب هم دقیقا همین ساعت شروع شد
هر شب راس ساعت ۱۰:۳۰ اهواز میزنن
امشب باز ساعت ۱۰ و نیم و دو تا انفجار شدید
سر ساعت، برنامه زمانبندی خاموشی هم اینقدر دقیق نیست وحید.
🔄
دوبااااررره
وای وحید دوباره دوتا
۲۲:۳۴ دو بار
اهواز ۲۲:۳۴ انفجار مجدد شدید
دوباره دو تا صدا پشت سر هم اهواز ۱۰:۳۵
انفجار ساعت ۲۲:۳۵ اهواز
یه انفجار دیگه 22:34 این یکی شدیدتررر بود.‌یکی دیگه هم دورتر
دوباره الان زدن ۲۲:۳۵ اهواز
اینبار شدیدتر
خیلی وحشتناک بود
سومی و چهارمی الان ساعت ۲۲:۳۵ اهواز باز روی لرزه‌ست
وحید دوتا همین الان اهواز، ساعت ۲۲:۳۵ خیلی صدا بلند بود
اهواز بعد از اون دوتای اول یکی دیگه الان زد ۲۲:۳۵
۱۰:۳۵ یه انفجار مهیب و بزرگ توی اهواز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77156" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzfHd7MHv2D8-FDF42EMXN4PVTtBAiAd06WAXF1YV23i5kDK3xKXLd-Kzl5KsEfHEIVFzgMTT_kff5yG1ixiVJGkzcU3KwMV7VBgJgjV_Wlgy7Ur-aG9UoNeBu-gct2wVrUj83tiMrXwmW7TgJZNpCoHQg0EftBsOaG40cS3J_yv6GYJKAu7ffiSSlbL14EVN9Hh_hu6iRXK0XfBenqBOiVGrsjq3dMpBF4EFXdgzpFwbmYXDi5p0ifYwlhe07e4fhwKltzJ7nxdIXHEyy5PMOWZLudm0b0FYp5C46C7t8ugM7iiy1PHh_p6AiVEcqoBoeGObXrReal47IRC8MMYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ساعت ۲ بعدازظهر امروز به وقت شرق آمریکا [۲۱:۳۰ به وقت تهران]، نیروهای ایالات متحده برای پنجمین شب پیاپی اجرای موج تازه‌ای از حملات علیه ایران را آغاز کردند تا توانمندی‌های نظامی ایران را بیش‌ازپیش تضعیف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77155" target="_blank">📅 22:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=dO_kYhdx8TIi_9755lVpnoffAyutfcL1r0KK9nGTtP1HdJC3U34sY1l5XviVofIA1thLEFXj1aJi8h_pgWJ8XPFVn-gyCd2-GdkxD5Lb-DBEzySlw_xFKezB_iUweGiLkYxti5--L7CMYQz9B5pb_HXE3CIjR5pYljtCVHBk52AlWsIGKKgIdjAwrp-AELbWJY20Jg1icVPgz2e9hWqZ-zsSRgeit2pIjfw2BJFIgGwOEhsMbSf_nq8Rxp2hnnymGQdDNgqjHF231cnqbLANv31io6ZruDL2iTLRXqP_ci7YY7Kpy2hGy0FQDJOoH7p0eYTRSIPzrmaXhKAGesWySA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=dO_kYhdx8TIi_9755lVpnoffAyutfcL1r0KK9nGTtP1HdJC3U34sY1l5XviVofIA1thLEFXj1aJi8h_pgWJ8XPFVn-gyCd2-GdkxD5Lb-DBEzySlw_xFKezB_iUweGiLkYxti5--L7CMYQz9B5pb_HXE3CIjR5pYljtCVHBk52AlWsIGKKgIdjAwrp-AELbWJY20Jg1icVPgz2e9hWqZ-zsSRgeit2pIjfw2BJFIgGwOEhsMbSf_nq8Rxp2hnnymGQdDNgqjHF231cnqbLANv31io6ZruDL2iTLRXqP_ci7YY7Kpy2hGy0FQDJOoH7p0eYTRSIPzrmaXhKAGesWySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود از حملات امشب به بندرعباس است. @
farahmand_alipour
پیام‌های دریافتی:
سلام وحید بندرعباس ۲۱:۴۴ صدای میاد نمیدونم پدافنده یا انفجار
سلام وحید جان سه تا انفجار خیلی خیلی وحشتناک همین الان ساعت ۲۱:۴۲ بندرعباس
بندرعباسم
دارن میزنننننننن پشت هم
۹:۴۲ چندتا انفجار شدید بندرعباس
ساعت ۹ و۴۵
بندرعباس ۳ تا انفجار وحشناکک
جلوی خونمون بود
سلام وحید جان، همین الان ساعت ۲۱.۴۲ سه تا انفجار پشت سر هم بندر عباس
سلام بندرعباس ساعت 21:43‌چهارتا انفجار
بندرعباس همین الان چندتا انفجار وحشتناک رخ داد
سلام آقا وحید غرب بندرعباس منطقه ۴ ترکید ۵ تا انفجار فوق العاده شدید
3 تاانفجاربندرعباس
نیروی دریایی ارتش غرب بندرعباس
و ایستگاه رادیویی بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77154" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw77BVanjA4jFOrAXNJaPX6LJAU6zkUPc7rtS0u4gaIb6B0pjC_kGlPjeO3o4UP1BlXTBQmAtOd98RRmxbLnvRf8tk4YSrZTz23GSPobFSLzCyPxJF_qeD0kM7bFp6m5XIVBPrLMNV8f2o-QLEUmSQQlELKnAAkpGO-ZrzaXRBNppoKAuf2hYye4nMhe5oBSt5RYGHFMlEfwoiJ2xiI1mDQ28YD81mOPAR0diUr-SycKWLIZ6oUKLPC5wU9zp_hpS1Vk4TxUp6OJew6Lj6yGtIK_NYB3HJW5XghkXGajWoyoOdw1xsGJIqPy3Tq_6-OwLcFTDHxcXGBQEAD1JQs8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
بندرعباس:
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشک‌های دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77153" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vNbEG6Ax0V2vvxNA8bdA2Cg0S_17jcFIXFz3BnHBm_J4hfc1FPAZ_zkpsSsWYmfgJpSAhY_c1z5wF1h69y6dlEWthrg-HrylC_PxJntNJ1iNgol1OvRpNCvECz01o8UtrSL8jmtYVPPVvTeqsHGm2UaP1be4m9_plnrPVOtzqK0mG3mGkR3OaI_fJzMWK0MIfPemqnqLqxIJMryaj-Y-CJdgy2WkiLkfUbU6WZLry6FrYZI11fxGHi1cObXuyCVGYvJ517s3AFUQ-4dzLIOWafht_5aZkRQyMb3zbeu2jPYICp-DvP-NDEijuh7ed4wdZ8IrbTNiZAjbF8wNVC9szA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SZd4u0PG2bEygYB0MWgg1Ckx0aD2SuEAOOhdy9tFokJRtDfNj0yMXoP14bTohrQWrAaNsRAPl78VHn8kciko0tPt_8_6_Nljp8uyw2H40YrlD8t2gE5cc8y4sRQ3AAx1GJKjgZaXAFD3n7pq98c1TpORNKe6GdKyx8QRgFG_5xxkjm1nynvenwP-niTznke_dJC7V9HarWFIA1n2xvi06ph6pfnNd9pLpp-9vTFe13TevBxMm89uZk4TYOglu6pnOwIbN-2dX6ZkHmKKZWnxE7U4PyP9trZ0AwUc3oBgsWkv5f_71dLPIeQfcux3iri5Abst4LGNOPb43lFJXPkctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s8L5YQmSQeS4NBZN4HjPriB7VTZUgCVIKG3zdZmjTgWmdufD27bmPYpovdbKOu8TZAUFCnByjMBT-YETWZx3eVz9Lph6N1SG16oWMCQBNOUNbTa95GZdOvIgZDaPEZ6INHJ8okyg_eoVkNR-ZAqLFV3xPP5pdELw3WdgZSQfKMhzy1PlNMpiE495T298WxJNYObc9jKSPvQ8kA1uitIS-R-ZJD4_Sw91RbwhNn2zGURXZZwPLxRlz5WHfSB9LI9-bD2SEGsfSJHiBOrfyTqD02SZvFYk-J_zBmDlkZYZgCPajWcVJMqzYRFh-ZHrbDcYqJTSoEYSQ6O6uGZ_DppqeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=GB6Mkwr5vBYlfCJUrSGe7nYAlZb2ynJK9ue83EpQd9QoviaIaTtA-EibWwm0wWGAyTq0SSCV5VBDF7vg_ysyoG5_FZgcznkBcF2rzKw1_LuhLC_HHJQHb9Xcm-7FW3kLxdSfG2L9A6GCREvWqaK2xfrgdilseIm6-IwLu4Tb219opsmGIiNh3Z7MzyxDIpEAJrsHt-kbJ6xQR7D4_hGsoQ8Zbs_l-7KAhuXD_b0pzjzSwrUIVrp25pcSyyjL7S3Aak_7z7Ha9a9InW_QIWvP15pyloBa3UF0zscBzuTIdK2cFz9nWveu8zk8FIwuWrek80TnesHUR_9Y8TXo00duxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=GB6Mkwr5vBYlfCJUrSGe7nYAlZb2ynJK9ue83EpQd9QoviaIaTtA-EibWwm0wWGAyTq0SSCV5VBDF7vg_ysyoG5_FZgcznkBcF2rzKw1_LuhLC_HHJQHb9Xcm-7FW3kLxdSfG2L9A6GCREvWqaK2xfrgdilseIm6-IwLu4Tb219opsmGIiNh3Z7MzyxDIpEAJrsHt-kbJ6xQR7D4_hGsoQ8Zbs_l-7KAhuXD_b0pzjzSwrUIVrp25pcSyyjL7S3Aak_7z7Ha9a9InW_QIWvP15pyloBa3UF0zscBzuTIdK2cFz9nWveu8zk8FIwuWrek80TnesHUR_9Y8TXo00duxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستنده تصاویر: پلیس گفت اتوبوس خراب شد پیاده شد تعمیر کنه خلاص بود از ایستگاه پله سوم تا پله اول رو رفت.
آتش‌نشانی: یک اتوبوس متوقف‌شده مقابل پارک ساعی با ۵موتورسیکلت و ۲خودروی سواری برخوردکرد.
اتوبوسرانی: بدون مسافر بود و پس از عملیات امدادی و رفع نقص فنی درحال جابه‌جایی بود.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77149" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=aSAWyZ2mA-SxcxZVMBUSiNFhbjHZ9lUC3EpTFA2ifhWg6HYD2qJuydEZ9u_YT9Q_OuIoe9b_NO5nBtvsQ9cLMABA2rgnzxgjTcSZEyHZql2cghbOJoI0rUhZlPiNnf-klKNFz-5B9PygdoWJaL4FcOpinLt-r-cxZKMLXVi-BI-3FZZZ9WgEQX5mSJi3Jsi91UwoQMEVvTeXqHrcBJW5PD7avCVrk2cXI-FtnRWWBNrCawZJbw8HBGhFCTXQDH_Yq2JnYafqhCgr0sOHAoZDt6iceJyTgw0KAHree8S1N_9__jRZmdBnmqE9QoCG9nL2_nR69YAwe9OVqvbFuxqbVQ0Yq5-5SZ4HvEkGMv0xlz4kqDPRlRR5vfj-_jCFdakO9ltPoyA85U88HosLDDrTjj4pGjVcEqiCmimM7Hm0MFUwe3iV8Tw6iqLGogCBM3nWuFMacpjJXeWmI82nnKWWI2ZgyGiTuMOTvfE_TJyY9LwNNKcdVUgs36ifZGQrJ1WmdCOtpMXo-ynxKnfld5wNj1YQePU0LrES-TJB2JzqcfjwNYhRLnHSm8ZpmzzJivRGQrz9GDupk1WXzXCjTOr89oXvpB9v3puSEZxNDqgt9W762_LkR1tStUz9dy3buEAboP3YU3H3xPFfsbfKuHgh9x3Yd24Ahk_Qw2QhNYj8N-U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=aSAWyZ2mA-SxcxZVMBUSiNFhbjHZ9lUC3EpTFA2ifhWg6HYD2qJuydEZ9u_YT9Q_OuIoe9b_NO5nBtvsQ9cLMABA2rgnzxgjTcSZEyHZql2cghbOJoI0rUhZlPiNnf-klKNFz-5B9PygdoWJaL4FcOpinLt-r-cxZKMLXVi-BI-3FZZZ9WgEQX5mSJi3Jsi91UwoQMEVvTeXqHrcBJW5PD7avCVrk2cXI-FtnRWWBNrCawZJbw8HBGhFCTXQDH_Yq2JnYafqhCgr0sOHAoZDt6iceJyTgw0KAHree8S1N_9__jRZmdBnmqE9QoCG9nL2_nR69YAwe9OVqvbFuxqbVQ0Yq5-5SZ4HvEkGMv0xlz4kqDPRlRR5vfj-_jCFdakO9ltPoyA85U88HosLDDrTjj4pGjVcEqiCmimM7Hm0MFUwe3iV8Tw6iqLGogCBM3nWuFMacpjJXeWmI82nnKWWI2ZgyGiTuMOTvfE_TJyY9LwNNKcdVUgs36ifZGQrJ1WmdCOtpMXo-ynxKnfld5wNj1YQePU0LrES-TJB2JzqcfjwNYhRLnHSm8ZpmzzJivRGQrz9GDupk1WXzXCjTOr89oXvpB9v3puSEZxNDqgt9W762_LkR1tStUz9dy3buEAboP3YU3H3xPFfsbfKuHgh9x3Yd24Ahk_Qw2QhNYj8N-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خون در ۲ ثانیه اول)
صدای ویدیو: "اتوبوس ترمز برید، هرچی موتوری بود رو زیر گرفت رفت. خیابون ولی‌عصر"
به خودروهای پلیس هم برخورد کرد.
Vahid
تهران، پنج‌شنبه ۲۵ تیر
via @
iliaen
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77148" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=ISfRu_jojWbIjCHqJfEYRoN-Up_gmPwbP4CihWccozbU3AsUvDDbvVRtGCgMt1NsSIw9w0FHsFAL96GvMPpgCROylWm70n9mrP23ImkfOqYUb4KGGFJh2JFGL_WCk6u5v9nxaeCkwJVpWZDkCGKD6axP-0igqfPqxE7m2AiPT1ML5RZAGuVk1LzE8RPDmO36ArYM6ObnEPt3WBl6DOk-quDHfQeBKpWQELb4j4YtASoJB-CIGRXUu35PSYdcYCunaWJYNaJfTL0q1EX_vppl1sTQc3nYPmn2sMTVnMkfzqHRGM3ItKp_sRmUV6apZXBjJDXO-lsJtMZq_XA8e3jHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=ISfRu_jojWbIjCHqJfEYRoN-Up_gmPwbP4CihWccozbU3AsUvDDbvVRtGCgMt1NsSIw9w0FHsFAL96GvMPpgCROylWm70n9mrP23ImkfOqYUb4KGGFJh2JFGL_WCk6u5v9nxaeCkwJVpWZDkCGKD6axP-0igqfPqxE7m2AiPT1ML5RZAGuVk1LzE8RPDmO36ArYM6ObnEPt3WBl6DOk-quDHfQeBKpWQELb4j4YtASoJB-CIGRXUu35PSYdcYCunaWJYNaJfTL0q1EX_vppl1sTQc3nYPmn2sMTVnMkfzqHRGM3ItKp_sRmUV6apZXBjJDXO-lsJtMZq_XA8e3jHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77147" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XazpjFfdIuZbdN1Ja0PktHTvKXs2c0L5c1SZRgO4Xlo7N2lqjes6EUBAzyjCshsFvQ5e9Z015d7jbf76ds_b-L6C1GJhVbVD3QiKzTz4ssneL30zmqHV-t_dbU59inBVYhpEuJ0IClTpb1I_Xf7Ey9UT5bc3pVSrxy3n6MVARMB9DfRFbDDKLg_pJtIWivJ6Wwe-J9ZSQRd2Qqm87UdAEE2fX-h2unI8Li97tBaFHzfAc4_sUBl7wC5RCIEMZCWKlAgeEngIXt5-lRYCf0TcHP-dPz9PS7uDhqa5S8Q7ilvEn5NATTuB4M49BPlXSGB_59jFgijux3XHPJua3vhk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام استانداری سمنان:‌ در حملات بامداد پنج‌شنبه فرودگاه سمنان نیز هدف حمله هوایی قرار گرفته است.
محمود قدرتی، مدیرکل امنیتی و انتظامی استانداری سمنان، ادعا کرده که در این حمله یک سوله جانبی در محوطه فرودگاه هدف اصابت موشک قرار گرفت و بخشی از شیشه‌های ساختمان اصلی ترمینال نیز آسیب دید.
به گفته او، این حمله در ساعات اولیه بامداد رخ داد و تلفات جانی نداشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77146" target="_blank">📅 18:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6unaW2ztW1V44Uh4tUAKvlJHZLCRk1EK_GfIdKblPGKV-RHSGyjbn3BZxouV8Z3wJmQKdPUuR6jkdo77zk6BS76U4kCEJ4KOtBgy62-ggFQTjsl5bLnNQkUHkNWGgjP4R8VP2oEM4SqoEqe6AK1YoQSl-qglVfxz5RtN3iX-PrueW8WFm3ZMpr4vSYoCUTDCsfjUlrVeAMzLg9lgeFHk257TH17n3KzOaUpV4N8GRH1UeflyBegLYqQeoz0o0HRhIL1GEmwiwbSo_wILntYp8Yl_wzsP2KtehEiQXx-bdCO6GlLMDPWKhst1i6L7svSoDlU9XiIvas48RzPzpX4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی به خبرگزاری فرانسه گفت که روز پنج‌شنبه ۲۵ تیرماه پهپادی به یک کشتی «حامل خودروهای آمریکایی» در نزدیکی یک ترمینال نفتی برخورد کرد. گزارش شده این کشتی از امارات متحده عربی آمده بود.
همزمان چهار منبع نفتی و امنیتی عراق به خبرگزاری رویترز گفتند که روز پنج‌شنبه بارگیری نفت خام در تمام پایانه‌های عراق پس از برخورد یک پهپاد با یک نفتکش در پایانه بصره متوقف شد.
در واکنش به این گزارش‌، سخنگوی وزارت نفت عراق با اعلام این‌که بارگیری نفت خام در پایانه‌های جنوبی عراق همچنان ادامه دارد گفت که در حال بررسی گزارش‌های مربوط به سقوط یک «شیء» نامشخص بر روی یک نفتکش هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77145" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpR44GBpDN0IQ1bhkWkj_t4vpxQ7mXat8bOsSNglc2uAD219HgdrCeLdxe6MVyoCsBIsbX8LrmaYPCFdUz78H99eGL6oFAZ0jciVngxtj6D38CQGD8QYB6C1biU1m-xgkC0e1MsCsDCWZXT3dHp6ltyVK5UuyKnVed-5krLeC8SDXuX35-T8xV9AC7re_B68fNfCDEtip4Zbw0xrXeCuTTmvccKenmThjHtOoIakWGvpSbpKiFTTW3EXIbYqlNmEhtZQ3vzG7FfhUHRtI6dVLI0O2en4NYj-SC4WzJant56c575dIEE7jmRzfYT8me2Xf5OrEJoNm89oYaSKZnPI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی، وزیر خارجه لبنان، می‌گوید تصمیم برای پایان‌دادن به نقش نظامی حزب‌الله در این کشور یک تصمیم حاکمیتی و مستقل لبنان بوده و پیش از توافق اصولی اخیر با اسرائیل اتخاذ شده است.
آقای رجی روز پنجنشبه ۲۵ تیر گفت که این تصمیم زمینه را برای توافقی فراهم کرد که ماه گذشته با میانجی‌گری آمریکا میان لبنان و اسرائیل حاصل شد.
او با تأکید بر این‌که لبنان «تصمیم خود را گرفته است»، گفت دیگر بازگشتی به «دوگانگی حاکمیت» وجود نخواهد داشت و جایی برای سلاح خارج از چارچوب مشروعیت دولت یا تصمیم‌گیری خارج از نهادهای رسمی کشور نیست.
رجی همچنین گفت استقرار ارتش لبنان در سراسر خاک این کشور، موضوعی جدایی‌ناپذیر از خروج کامل نیروهای اسرائیلی از همهٔ مناطق اشغالی لبنان است.
حزب‌الله که تحت حمایت جمهوری اسلامی ایران است، از سوی آمریکا یک سازمان تروریستی شناخته شده اما اتحادیه اروپا تنها شاخهٔ نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77144" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af4Kv9SB9to2LtKZjfQxX_1_vhKLss8coP3fM_TbJTMxV-QSRc7nP5mnZIY_kdHdZOO6Qdey7ouRwZ6JY36bg3rhIrkEMOzV_Uqra01YuViyNmurBTSzUo1Hudmhwbyn4pMPgsi0gpBAWMYFesW78Tsp2dVBt2d_RZ8Jq1pHFRWsFm1uFbHIbPT0gq2vtxMTO-C40WjPg60REQNBfVNJbBu9_krCdqXcgVh3Cx_wv3adydHu-91Zda4Kh_CshYN0fDYHfXjdrmh8V6aks8PCIWTa634dS8H3YT2dNokuDqePEgxp8kIgXE96OlfUZAYnZav7ZlyeXjM8V08kQ5WO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت جورنال به‌نقل از چند مقام آمریکایی گزارش داد که دونالد ترامپ پس از چند جلسهٔ توجیهی با دستیاران ارشد خود، به گسترش عملیات نظامی ایالات متحده در ایران متمایل شده است.
به‌گفتۀ این مقام‌ها که نام‌شان اعلام نشده، گزینه‌های مطرح‌شده شامل افزایش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی در نزدیکی تنگه هرمز و بمباران یک تأسیسات هسته‌ای مستحکم و مخفی است.
به‌نوشتۀ این روزنامه، دونالد ترامپ عصر سه‌شنبه به وقت آمریکا میزبان جلسه‌ای در اتاق وضعیت کاخ سفید بود تا در مورد تصرف احتمالی جزیرهٔ خارگ و سایر مناطق در امتداد تنگهٔ هرمز با استفاده از نیروهای آمریکایی و همچنین بمباران احتمالی یک مجتمع تونل در کوه کلنگ گزلا که به پیکاکس یا کوه کلنگ معروف است، بحث کند.
کوه کلنگ گزلا محل یک تأسیسات هسته‌ای عمیق و مخفی ایران نزدیک نطنز است که تاکنون هدف حملات آمریکا قرار نگرفته است. وال‌استریت جورنال می‌گوید گسترش حملات هوایی علیه اهداف بیشتر در ایران، از جمله نیروگاه‌ها، نیز همچنان محتمل است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77143" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=SNv9ELFkZWw9BEhxbj79N9jQJnQlibYXBhHuiBC9P2LakrUo3SF1_jU2xJQg58HiKJdgUZ1vx8JIP150r8uRncenEJNKJo_lrxTtzx8CK3CUswufvK8wT-zUwcuvfr0xF4tIdk0ConPCMHkJE6nGO5_4gmqHLNIB4LXLXpVepQixlreOc-RCrsUiuMZ1O3_rqG3Iv1a1S5_Hf34bUQp604eVZqhj1ex5IjfikjvALXSyTmmcCkH7_mEla954CQFm2VGK-flRBXyXFdZ0qtKVBNd5QvC82_-uS6LBBfNe_PksJqcEpRMOa8V4KlViJ7NdGTV_UAzrplp1r0tP9JLvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=SNv9ELFkZWw9BEhxbj79N9jQJnQlibYXBhHuiBC9P2LakrUo3SF1_jU2xJQg58HiKJdgUZ1vx8JIP150r8uRncenEJNKJo_lrxTtzx8CK3CUswufvK8wT-zUwcuvfr0xF4tIdk0ConPCMHkJE6nGO5_4gmqHLNIB4LXLXpVepQixlreOc-RCrsUiuMZ1O3_rqG3Iv1a1S5_Hf34bUQp604eVZqhj1ex5IjfikjvALXSyTmmcCkH7_mEla954CQFm2VGK-flRBXyXFdZ0qtKVBNd5QvC82_-uS6LBBfNe_PksJqcEpRMOa8V4KlViJ7NdGTV_UAzrplp1r0tP9JLvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در پاسخ به پرسشی درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش، گفت که به این موضوع «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»
ترامپ افزود این کار را دیگران انجام می دهند و به نظرم در این زمینه عملکرد خوبی دارند و تاکید کرد خودش به این موضوع اصلا فکر نمی‌کند.
@
VahidOOnLine
او همچنین تاکید کرد که می‌تواند سپاه پاسداران را به همان شیوه‌ای از بین ببرد که در دوره نخست ریاست‌جمهوری خود داعش را در عراق و سوریه شکست داد.
ترامپ گفت: «ما در وضعیت خوبی خواهیم بود. آن‌ها تضعیف شده‌اند. تسلیحاتشان ۹۱ درصد کاهش یافته است. توان پهپادی آن‌ها به‌شدت کاهش یافته است. هنوز مقداری دارند، اما زیاد نیست. ظرفیت تولیدشان کاهش یافته است. پرتابگرهای راکتی و پرتابگرهای موشکی آن‌ها به‌شدت کاهش یافته‌اند. موشک‌هایشان هم به‌شدت کاهش یافته‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/77142" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیم ساعت از
سه ساعت
گفت‌وگوی جی‌دی ونس با جو روگن، بخش مرتبط با ایران
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با جو روگن از آنچه «جنگ‌طلبان» در آمریکا و دیگر کشورها خواند، انتقاد کرد و گفت این افراد با صرف هزینه‌های گسترده تلاش می‌کنند مذاکرات دولت دونالد ترامپ با جمهوری اسلامی را به شکست بکشانند و افکار عمومی آمریکا را تغییر دهند.
ونس با دفاع از رویکرد دولت ترامپ، تاکید کرد دیپلماسی برای حل بحران حمله‌ها به کشتی‌رانی در تنگه هرمز ضروری است و گفت در کنار اقدامات نظامی، گفت‌وگو تنها راه رسیدگی به این بحران است.
@
VahidOOnLine
بخش پرواکنش‌تر:
... من دو چیز را از میان سطرها می‌خوانم. فکر می‌کنم بعضی از آن‌ها می‌خواهند حکومت ایران به‌طور کامل تغییر کند؛ روحانیان سرنگون شوند و فردی بسیار دوستانه‌تر جایگزینشان شود.
ببین، تجربهٔ ما از انجام چنین کاری چیست؟ خوب نبوده. خوب نبوده. خوب نبوده.
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، تصمیم با خودشان است؛ اما ما ۱۵۰ هزار نیروی زمینی نمی‌فرستیم تا تغییر یک حکومت را رقم بزنیم، مگر اینکه مردم داخل کشور خودشان خواهان چنین نتیجه‌ای باشند.
در هر صورت قرار نیست نیرو بفرستیم؛ اما پیشنهاد اعزام نیرو یعنی عملاً می‌گویی ارتش آمریکا باید کار مردم ایران را برایشان انجام دهد. ما دیگر در این کار نیستیم. واقعاً نیستیم.
نتیجهٔ دومی که فکر می‌کنم بعضی‌ها خواهانش هستند ــ چه خودشان آگاه باشند چه نه ــ چیزی است که من «نتیجهٔ لیبی» می‌نامم.
اگر به نتیجهٔ نهایی سیاست ما در لیبی پس از کشته‌شدن قذافی به دست دولت اوباما نگاه کنی ــ باز هم تصمیمی بسیار احمقانه ــ چه اتفاقی افتاد؟ لیبی عملاً به کشوری شکست‌خورده تبدیل شد. بحران پناه‌جویان به وجود آمد. مردم به اروپا سرازیر شدند، به بخش‌های دیگر آسیا و آفریقا رفتند. خشونت و تروریسم زیادی از دل آن بیرون آمد.
فکر می‌کنم افرادی هستند که می‌خواهند همین نتیجه در ایران رخ دهد. اما باز می‌پرسم: چه چیزی به سود ماست؟ چطور به سود ایالات متحده است که ۹۴ میلیون انسان درمانده به اروپا و ایالات متحده سرازیر شوند و زیرساخت‌های تروریستی که وقتی تروریست‌ها را در سراسر جهان پراکنده می‌کنی، می‌تواند شکل بگیرد؟
ما قبلاً این آزمایش را انجام داده‌ایم. سیاست کنونی ما و هدفی که دنبال می‌کنیم این است که تنگه را باز نگه داریم و جریان آزاد نفت و گاز را تضمین کنیم. بدیهی است که می‌خواهیم مانع داشتن برنامهٔ تسلیحات هسته‌ای توسط ایران شویم و از ابزارهای دیپلماسی و قدرت نظامی برای رسیدن به آن استفاده کنیم.
بیشتر متن زیرنویس ویدیوی بالا (تا سقف تعداد کاراکتر مجاز):
telegra.ph/Vance-07-16-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/77141" target="_blank">📅 06:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858e125a28.mp4?token=FLUeaV3i17EWu0euXsq_EnIU-zTF0aBryV9hkAZWMK-CZZ5IDEYF9bNovm4npCjdb4xHchSn0Uo-UsNCoW3miR_70VGlhMyV1NK1t6EDvbPoB9QW0Bc9n-LsKK7_kv_2iSJsie6M2nE3sXs4BcGXHwurSYhqyCGwV1Cyl_dMh9Nm3GRAY1LJMitEjJOs6BYCPRiLh2ihRy3UXFOw9CiG4wEiAzF4ZV3rJzAREVsMQEC-aA7pTo3M_FZ4swK5l17K64KEMTDCJLa_mUd4_oGZW1ZTiwqko_Ar4p3jOZetvviMn9rpr_jWdu3GO8hCNyqI4j7YopfzX0m_-txTQ0Yp_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858e125a28.mp4?token=FLUeaV3i17EWu0euXsq_EnIU-zTF0aBryV9hkAZWMK-CZZ5IDEYF9bNovm4npCjdb4xHchSn0Uo-UsNCoW3miR_70VGlhMyV1NK1t6EDvbPoB9QW0Bc9n-LsKK7_kv_2iSJsie6M2nE3sXs4BcGXHwurSYhqyCGwV1Cyl_dMh9Nm3GRAY1LJMitEjJOs6BYCPRiLh2ihRy3UXFOw9CiG4wEiAzF4ZV3rJzAREVsMQEC-aA7pTo3M_FZ4swK5l17K64KEMTDCJLa_mUd4_oGZW1ZTiwqko_Ar4p3jOZetvviMn9rpr_jWdu3GO8hCNyqI4j7YopfzX0m_-txTQ0Yp_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام،‌ ترجمه ماشین:
تازه‌ترین موج حملات آمریکا علیه ایران پایان یافت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) موج حملات شامگاهی علیه ایران را ساعت ۹ شب به وقت شرق آمریکا [۴:۳۰ تهران] در ۱۵ ژوئیه پایان داد.
نیروهای آمریکایی مراکز فرماندهی، مواضع پدافند هوایی، توانمندی‌های موشکی و پهپادی و تأسیسات نظارت ساحلی ایران را مورد حمله قرار دادند تا توانایی ایران برای تهدید دریانوردان بی‌گناهِ خدمه کشتی‌های تجاری عبوری از تنگه هرمز را بیش از پیش تضعیف کنند. سنتکام برای حمله به مواضعی در چندین نقطه، از جمله بندرعباس، از مهمات هدایت‌شونده دقیق استفاده کرد.
پیش‌تر در صبح امروز، نیروهای آمریکایی طی یک موج حملات ۹۰دقیقه‌ای، مواضع دفاع ساحلی و موشک‌های کروز در جزیره تنب بزرگ را هدف قرار دادند.
ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۱۵
🔸
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم غیور و بپاخاسته ایران!
🔹
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
سپاه درباره
صدای پاکدشت
: پدافند بود. هیچ اصابتی نبود
🔸
اطلاعیه سپاه حضرت سیدالشهدا علیه السلام استان تهران درباره صدای شنیده‌شده در پاکدشت؛
روابط عمومی سپاه حضرت سیدالشهدا علیه‌السلام استان تهران:
🔹
دقایقی پیش صدای انفجاری در محدوده شهرستان پاکدشت شنیده شد که بررسی‌های میدانی و نظامی نشان می‌دهد این صدا ناشی از عملکرد سامانه‌های پدافند هوایی در منطقه پارچین بوده است.
🔹
ضمن تکذیب قاطع ادعاهای برخی رسانه‌های معاند و جریان‌های سلطنت‌طلب در خصوص وقوع هرگونه اصابت، هیچ‌گونه حادثه یا اصابتی در منطقه صورت نپذیرفته و فعالیت‌های مذکور در راستای آمادگی و عملکرد پدافند هوایی بوده است.
🔹
از مردم عزیز ضمن حفظ آرامش، اخبار مربوط به این رویداد را تنها از طریق رسانه‌های رسمی دنبال کرده و از توجه به شایعات هدفمندِ رسانه‌های بیگانه که با هدف ایجاد التهاب و ناامنی روانی منتشر می‌شوند، خودداری کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/77140" target="_blank">📅 04:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی از تهران
احتمالا همگی درباره صدای پدافند:
صدای پدافند میاد ساعت ۳:۵۱ یوسف اباد تهران
تهران انفجار 3:50
پدافند تهرن داره کا میکنه ۳و۵۱
تهران یوسف اباد صدای پدافند
نارمک صدای پدافند ۳:۵۱
سلام وحید جان مرکز تهران صدای پدافند میاد الان شروع شد
.
تهران صدای پدافند
همین الان صدای پدافند شرق تهران
سلام خرم اباد صدای یدونه انفجار اومد
تهران مرکز شهر صدای پدافند
۳:۵۰
البته زیاد نبود، چندتا بود
وحید ساعت ۳:۵۱تهران نارمک صدای پدافند
داداش تهران سید خندان صدا پدافند ساعت ۳:۵۰
پدافند تهران میدون شهدا داره کار میکنه
صدای پدافند ساعت 3:51 مرکز تهران
تهران سهروردی صدای انفجار از دور تقریبا
صدایی شبیه پدافند از دور شنیده میشه، اختیاریه، ۳:۵۱
تهران عباس آباد پدافند ساعت ۳:۵۰
پاسداران تهران صدای پدافند
سلام همین الان پدافند سمت میدان امام حسین فعال شد
۳:۵۱ دقیقه
من ميرداماد تهران هستم
الان دارن ميزنن
٢ تا صداي بلند و بعدش ٥-٦ تا  كوچكتر
سلام.تهران پیروزی صدای پدافند ۳:۵۲
وحید سمت سهروردی صدا پدافند شنیدیم 3:52
سلام سمت سیدخندان همین الان صدای انفجار شنیده شد
سلام ! ساعت ۳:۵۱ دقیقه سمنان صدای جنگنده میاد
الان ساعت ۳:۵۱ صدای سه تا انفجار اومد تهران
سمت غرب صدا شنیدم
وحیدجان سلام الان ۳:۵۲ تهران محله نیروهوایی صدای پدافند
مرکز تهران. یه صدای انفجار اومد (دور بود) بعدش صدای پدافند ۳:۵۱
سلام وحید جان شرق تهران سمت فدک ۳:۵۲ صدای پدافند به گوش رسید نمیدونم کجاست
سهروردی سه تا صدای بلند متوالی اومد ولی منشأ رو نمیدونم و دور بود انگار
سلام وحید جان غرب تهران سمت فرودگاه صدا پدافند و جنگنده میاد
فعال شدن پدافند در تهران محله دبستان ساعت ۳:۵۰ بامداد
سلام ۳:۵۲ دقیقه سمت گیشا هم صدای پدافند میاد
من میدان سپاهم
صدای انفجار یا پدافند! من تشخیص نمیدم از دوره
ساعت ۳:۵۰
سلام‌وحید جان سمت امیر آباد شمالی صدا پدافند داره میاد
سلام وحید جان تهران شریعتی سمت میرداماد صدای پدافند اومد نزدیک نبود خیلی
سلام وحید جان ساعت ۳:۵۱ دقیقه میدان شهدا چهار پنج بار صدای پدافند اومد
صدا پدافند بود فکر کنم
تهران محدوده خیابون امام خمینی
ساعت ۳:۵۰
وحید سلام توانیریم، صدای پدافند ونک دو دقیقه پیش
سلام تهران الان ساعت 3:53 هم صدای پدافند میاد هم روی اسمون نورش معلومه
سلام وحیدجان سمت شرق پدافند زدن اما قبلش یه صدای بلندی اومد اما نمیدونم زدن یا نه چیزی دیده نمیشه
3:50صدای پدافند شرق تهران
سلام ، غرب تهران (پونک) صدای انفجارها پشت هم و خفیف از دور میاد
سلام وحید جان
شرق تهران الان انگاار صدای انفجار اومد . مطمئن نیستم چون خواب بودیم ولی شبیه صداهای اسفند ماه بود
ساعت ۳.۵۱ صدای پدافند تهران خ شریعتی
کوتاه بود
سلام وحید جان الان ساعت ۳.۵۴ صبح ۲۵ تیرماه صدای پدافند گیشا
تهران شوش پدافند ٣:٥٣
غرب تهران 3:51 چندتا انفجار پشت سرهم شنیدیم
الان باز شروع شد ساعت 3:56
همین الان ساعت ۳ و ۵۵ دقیقه دوباره صدا اومد سمت هفت تیر
۳:۵۶ دوباره صدای پدافتد یا شلیک سمت نارمک
۳.۵۶ امیراباد شمالی دومین بار پدافند
از اختیاریه، ۳:۵۶؛ چند تا صدا شنیده شد با صدای قبلی فرق داره که پدافند بود [پدافندها انواع متفاوتی هستند با صداهای متفاوت]
وحید ۳:۵۶ شرق تهران صدای پدافند - تو ۱۰ دقیقه گذشته دومین باره
تهران شمس آباد  نزدیک کلانتری مجیدیه همینطور صدای پدافند میاد
سلام مجیدیه شمالی صدای پشت سرهم پدافند میاد  حدود ۴ صبح
سلام وحید جان. مرکز تهران صدای پدافند مکرر اومد.
وحید جان ، ساعت ۳:۵۱ دقیقه بامداد اتوبان حقانی صدای پدافند بسیار کوتاه
داداش همین الان  ۳:۵۵ حدود ۱۰ بار صدا امد  ولی زیاد نزدیک نبود یوسف اباد
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/77139" target="_blank">📅 03:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی:
خرم آباد صدای انفجار
سلام ساعت 3:48 صدای انفجار در خرم آباد
وحیدخان از بروجرد انگار موشک زدن صدای غرش سریع و شدید تو آسمون اومد
خرم آباد ۳.۴۷ صدای انفجار یهویی و نسبتا شدید
خررم آباد به شدت صدای انفجار اومد
کل ساختمونمون لرزید
سلام وحیدجان ۳:۴۷ خرم اباد صدا اومد
سلام وحید جان خرم اباد لرستان ساعت ۳ و ۴۷ دقیقه انفجار
🔄
دوباره زد خرم اباد رو ۳:۵۷
سلام وحید جان همین الان صدای افنجار اومد دوباره خرم اباد
سلام وحید جان بروجرد الان ی صدای مهیب امد. من هدفون داشتم درست متوجه نشدم بعدشم صدا موشک یا جنگنده امد
آقا وحید بروجرد صدای خیلی قوی صدای واقعا عجیب و قوی،واقعا نمی‌دونم انفجار بود یا دوباره شلیک بالستیک،صداش از رعد و برق بدتر بود
خرم آباد دوباره صداي انفجار
دومین انفجار در خرم آباد ساعت 3:57
بروجردو ۳:۵۵ زدن
انفجار خیلییی قوی
سلام وحید جان از بروجرد صدای شدید و یهویی اومد (ساعت ۳:۵۰ صبح)
طبق تجربه، صدای شلیک موشک بود
داداش الشتر لرستان دوبار صدا اومد معمولا از اینجا موشک پرتاب میکنن یبار 3 و 47 دقیقه یبارم حدودا 3و  56 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77138" target="_blank">📅 03:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تو ارومیه صدای انفجار اومد از سمت کوه های اطراف شهر
همین الان یه صدای انفجار با لرزش خارج از شهر اومد (ارومیه) بعدش با صدای بلند مثل صدای موشک یا جنگنده تو هوا
ارومیه صدای انفجار اومد دقایقی پیش با صدای جنگنده [احتمالا صدای موشکه]
خارج از شهر ارومیه نزدیک مرز صدای جنگنده میاد همین الان
سلام وحیدجان، دوباره از تبریز موشک زدن
سلام وحید. الان ۳:۴۶ از تبریز موشک زدن
۳:۴۶ دقیقه همین الان یه موشک از طرفای اسکو آذربایجان شرقی بلند شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77137" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">استان تهران، صدای پدافند:
سلام وحید جان الان ساعت ۰۳:۲۷ صدا انفجار اومد سمت پاکدشت
اقا وحید همین الان پدافند پاکدشت کار کرد بدجور
صدای انفجار پاکدشت ۳:۲۵
۳:۳۰ سمت پاکدشت داره صدا میاد
سلام صدای انفجار و پدافند حدود دو سه دقیقه پیش داخل پاکدشت
پارچین و پاکدشت انفجار سنگین
خیلی صدا شدید بود
فکرکنم پارچینو زد
۳/۳۰ چندین انفجار در پارچین
سلام وحید
ساعت۳:۲۰ پاکدشت صدا پدافند اومد شدید
دوباره الان ساعت ۳:۳۰ داخل پاکدشت صدا انفجار میاد
دارن میزنن پارچین رووووو
صدای پدافند میاد
۸ بار صدا اومد
سلام وحید جان پدافند پارچین فعال شد همین الان و صداش پاکدشت شنیده شد
سلام دوتا ویکی الان3.31دقیقه.صداتا قرچک ورامین امد
البته اول چهارپنجتا انفجار شنیدم که احتمالا انفجار گلوله.های ضدهوایی بود
شریف اباد پشت پارچین صدا شدید پدافند میاد ۳:۱۸
ما صبح امتحان نهایی ریاضی داریم یه دوازدهمی همینجوری از استرس دارم میمیرم
و یه صدای انفجار اومد همین الان پاکدشت چند بار 3:30
صدای پدافند میاد آقا وحید شدید
🔄
همین الان پدافند رگباری سمت پاکدشت ۳:۴۳
همچنان ۳:۴۲ ضد هوایی شدیدا فعاله
ساعت ۳ و۴۳ دوباره فعالیت شدید پدافند توی پاکدشت
🔄
دوباره صدای پدافندا شدید تر شد
از سمت پارچینه
۳:۴۵ شدیدتر
دیگه همینجوری هست
هر موقع تموم شد میگم
😂
صدای جنگنده ساعت ۳ و ۴۶ دقیقه
بازم انفجار شدید خرم آباد ۳.۵۷
سلام وحید  دوباره خرم آباد زدن ساعت ۳:۵۷
خرم آباد بازم صدای انفجار اومد ساعت 3:56
انفجار مجدد خرم آباد خیلی شدید بود
تهران صدای انفجار سمت آزادی الان
وحید جان 3.48صدای شدید خرم آباد دو مرتبه به فاصله 10دقیقه کل ساختمون لرزید
لرستان. الشتر(سلسله)
صدا و لرزش شدید اومد نمیدونم اونا زدن یا ما موشک شلیک کردیم
3.50
دوباره 3.56 همون لرزش و صدا..
لرستان الشتر وحشتناک دارن میزنن
خرم اباد
سلام وحید جان ساعت حوالی 3:55 از بر‌وجرد موشک زدن صداش خیلی بلند بود
آپدیت: منابع حکومتی
فرماندار پاکدشت: صدای دقایقی پیش در شهرستان پاکدشت به علت فعالیت سامانۀ پدافند هوایی بوده است.
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77136" target="_blank">📅 03:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
۳:۱۵ سمت «شهرک صنعتی سمنان» یک تک صدای انفجار بزرگ اومد.
سمنان، دو موج خیلی شدید انفجار اومد
جوری که خونه لرزید
ولی منشاش نا مشخصه
همزمان با پخش اذان از مساجد هم بود وحید جان
سلام وحید جان 3:18 هست ساعت و صدای بلندی در شهر سمنان اومد
آپدیت: منابع حکومتی
مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
استان مرکزی:
خنداب دوتا انفجار
آقا وحید 3تا انفجار سنگین خنداب
آپدیت: منابع حکومتی
معاون استاندار مرکزی: یک منطقه خارج از محدوده شهر خنداب ۲ بار مورد حمله پرتابه‌های دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77135" target="_blank">📅 03:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECoxrcZu4H7Y8jnOg8RmDb2CcUIuUhd_Z2kmzpHNaBjRbDHRfvYByKGvvys_O7FqjMVCqP5X_FbUVsAAHQw2Rv_t3MkYRzwDS5dGmnF2fGse-KKAfqB2Kibnuz2P44UPnVtMNg3rN1jUWAd64VJOUMkRWRw82XwH9kXYpQAzHE3es9af7tg0DwlKmfYqNmFMcbTI0ozdCAph3Nl_KjmGRle6r4AjVWCL5aYukLYlFvlwqdzPQYA2gk77eryL8xZKT7YZhNEAXCJtOHetSXeILE-masejdsC7hTZtopsx7nisJxYLU5cQss0lROx3uk1tT5ZaJW4VLkGzdgVsfzO6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران یک شهروند بازداشت‌شده آمریکایی را آزاد کرد
پست ترامپ، ترجمه ماشین:‌
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴، در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود، به‌ناحق بازداشت شده بود، اجازه داده است کشور را ترک کند.
او اکنون به سلامت از ایران خارج شده و حالش خوب است.
ایالات متحده آمریکا از این حسن‌نیت ایران قدردانی می‌کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
گویا اسمش "دنا کراری" است:
twitter
آپدیت:
جرد گسنر، وکیل حقوق بشری مستقر در واشنگتن، در بیانیه‌ای
گفت
«من خوشحالم و با هیجان اعلام می‌کنم که موکلم، شهروند آمریکایی دنا کراری، که از دسامبر ۲۰۲۴ به دلیل اتهامات بی‌اساس در ایران گرفتار شده بود، اکنون آزاد است.»
او افزود: «این اتفاق بدون تلاش‌های فوق‌العاده و پیگیرانه رئیس‌جمهوری [آمریکا،‌] دونالد ترامپ ممکن نبود. دنا اکنون در امنیت است و در حال بازگشت به ایالات متحده آمریکا است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77134" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس الان ساعت ۱.۲۶ دو تا صدای انفجار
سلام
بندرعباس ۱:۲۷ پایگاه هوایی ۲ تا انفجار شدید
درود وحید جان
همین الان شرق بندرعباس پایگاه هوایی صدای دو تا انفجار اومد
سه تا انفجار بندرعباس
احتمالا یکیش پایگاه هوایی
سلام وحیدجان چند انفجار سنگین در مسن لرزش شدید برقم قطع شد نیم ساعت قبل
جزیره قشم
یکی دیگه الان خورد 1.29
🔄
فعالیت پدافند بندرعباس ساعت ۱.۵۱
لرزش پنجره و صدای پدافند شرق بندرعباس شنیده میشه
فعال شدن پدافند بندرعباس همین الان
درگیری پدافند هوایی تو بندرعباس نزدیک پایگاه هوایی
فعال شدن پدافند بندرعباس همین الان
پدافند توی محله [...] بندرعباس جاساز شده
بین خونه های مردم ، محله [...]
وحید جان اینو کامل بفرست عزیزم
🔄
صدای بسیار بسیار شدید بندرعباس
دیوار صوتی شکست
یه صدای وحشتناکی از آسمون اومد
۱و ۵۸ بندرعباس
همین الان مجددا ارزش و صدای وحشتناک، ۱و ۵۹
نمیدونم انفجار بود یا پدافند ۱:۵۸
صداش شدید بودسمت پایگاه هوایی
وحید جان صدای عجیب تو آسمون شرق شهر بندرعباس عین غرش ولی منبع نا معلوم
وحید سلام بندرعباس ۱:۵۷ ی صدای خیلس بلند طولانی اومد انگار ی چیزی بخورد کنه و تخریب بشه
🔄
انفجار شدید ۲:۲۱
شرق بندرعباس ۰۲:۲۰ زدن شدید
بندرعباس انفجار سنگین
بازم پایگاه هوایی بندرعباسو زدن
شدت انفجار خیلی بالا بود ساعت ۲.۲۰
الان ساعت ۲:۲۱ گلشهر جنوبی بندرعباس صدای انفجار بسیار شدید،مثل غرش
سلام بندرعباس ۲:۲۰ سمت فرودگاه صدای بسیار مهیب
سلام ۲:۲۰ انفجار مهیب بندرعباس
صدای انفجار شدید اومد بندر وحید ۲:۲۱
🔄
۳ ۴ تا انفجار دیگه ۲ و ۲۶
وحید ۲ انفجار سنگین همین الان پایگاه هوایی بندرعباس
سلام ۲:۲۶ انفجار مهیب بندرعباس
بندرعباس پشت سر هم داره صدای انفجار میاد الانم 2 تا 2:27
۲:۲۷ دوباره انفجار
این دفعه دورتر یا ضعیف‌تر
بندرعباس دو صدای دیگه ۲:۲۷ بازم فرودگاه یا پایگاه هوایی
صدای قبلی شدید تر بود
سه تا انفجار پایگاه هوایی بندرعباس
ساعت ۲.۲۷
سلام وحید جان 2:27 بندرعباس صدای دو انفجار
الان بندر دوباره دوتا صدا ۲:۲۶ ، اولی زد دومی انگار پدافند بود
2.26 بندرعباس
دو انفجار شدید به فاصله ۴ثانیه در منطقه گلشهر شنیده شد.
منابع حکومتی:
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77133" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pzm5pY0V2PbAC1g2DtwHKlcUFRYbwQjUQGqAbUKNL_FgwESnCQlgRTRlgspWQYSJBuPyIo9GNOmTLiXLtgNLHSJMEsBu9BT85N0c8zaq9XN4zPLs2XqqGxUZTRAiPG1Tgk_UohX_PqGB6GmI1cc_SPYAtiypdhdHtIy7brflIB6QwboqHfdujPnMyzr74ypl0stgchI0GIi_fYxIILen0PIBc1iPCp2F3evUigL_UbRUO9k4WO_DIwQm3miJsuQ-FkKPixlQ6VYX7aOIjkkuQb6p9BIu7o4KEVE6P0suLrQMjN4BZEmEcM_zfzYa5GVqh_-fTX5oVA5MDDCsgSyNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه ۲۴ تیر در سخنرانی خود در «دانشکده جنگ ارتش ایالات متحده» در کارلایل پنسیلوانیا، گفت ایران «به‌زودی شکست خواهد خورد.»
او با اشاره به حملات اخیر آمریکا علیه ایران گفت با وجود آنچه «عملیات نظامی» خواند، بازار نفت دچار جهش شدید نشده و برخلاف پیش‌بینی‌ها، قیمت‌ها افزایش چشمگیری نداشته است.
ترامپ افزود بسیاری انتظار داشتند قیمت نفت تا ۳۵۰ دلار در هر بشکه افزایش یابد، اما این رقم در حال حاضر حدود ۷۹ دلار است و حتی چند روز پیش به ۶۸ دلار نیز رسیده بود.
رئیس‌جمهوری آمریکا همچنین گفت اقداماتی که به گفته او در واکنش به «عدم پایبندی ایران» انجام شده، محدود بوده و در صورت آرام شدن شرایط، قیمت نفت ممکن است به حدود ۵۵ دلار یا حتی کمتر کاهش یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77132" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=HUCGiGMUdMoUu771F3Ipv8OA-LzMXuXLOh5yB1JVTdgw9TWm3HPo6iDDt1785i3y8qlWtQgeQ0MH1i1TVZb0TQNPHIzIQ9P2fogritZakAhDXxcdW_TlbwNnIW7Hpv4Gpjqr13V-86WarSozi9fEAWz-FvRxHd9fRN1_J3K_39nvlkJLJS5SjFjf1aCFpluADIR4NeTpHLC1_B4WqhyXH7z4v9haxX-ES2sWecX-LBV-r5poECBHP4lzQjiNMRa-734lYmiNXcJHrpZ70E-W19hsutUFZk86Jg4AuCljMSn9Don5HxuWyrmxaNCzWQOCPW0SuuTVVwWnWidtmua1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=HUCGiGMUdMoUu771F3Ipv8OA-LzMXuXLOh5yB1JVTdgw9TWm3HPo6iDDt1785i3y8qlWtQgeQ0MH1i1TVZb0TQNPHIzIQ9P2fogritZakAhDXxcdW_TlbwNnIW7Hpv4Gpjqr13V-86WarSozi9fEAWz-FvRxHd9fRN1_J3K_39nvlkJLJS5SjFjf1aCFpluADIR4NeTpHLC1_B4WqhyXH7z4v9haxX-ES2sWecX-LBV-r5poECBHP4lzQjiNMRa-734lYmiNXcJHrpZ70E-W19hsutUFZk86Jg4AuCljMSn9Don5HxuWyrmxaNCzWQOCPW0SuuTVVwWnWidtmua1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکایی یک شناور متخلف را در خلیج [فارس] از کار انداختند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۵ ژوئیه، در اجرای تدابیر محاصره دریایی علیه ایران، یک نفتکش بدون محموله را که تلاش داشت به‌سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) مشاهده کردند که نفتکش «بلما» (M/T Belma) با پرچم کوراسائو، در آب‌های بین‌المللی به‌سوی جزیره خارک در حرکت است. این شناور تجاری هنگام تلاش برای نقض محاصره آمریکا، چندین هشدار را نادیده گرفت. یک هواپیمای آمریکایی با شلیک موشک‌های هلفایر به دودکش کشتی، آن را از کار انداخت. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی در ساعت ۴ بعدازظهر به وقت شرق آمریکا در ۱۴ ژوئیه، محاصره دریایی شناورهای در حال تردد به بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها را از سر گرفتند. در نخستین ۲۴ ساعت اجرای محاصره، سنتکام مسیر دو شناور تجاریِ مطیع را تغییر داد و یک شناور متخلف را از کار انداخت.
نیروهای آمریکایی همچنان هوشیار و آماده‌اند تا از رعایت کامل محاصره اطمینان حاصل کنند.
CENTCOM
سنتکام به جای «خلیج فارس» چیز دیگری نوشته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77131" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=PTbOlEDrH1mPDNNTxCTmKsACmybxLX-V-DYHyuLmAXjtzJfr3eTBzHii_JlqgUGRNSujH9jaxjjWbYHHa4HvcmFknQMkvZfHGHGPSgWxbXUneHHdKZd_ybqsRkRmfdOdLcWQe-iPaRWJyLV16mlJfYpJoYOSfV9LyUyJlmSF_bgFxbAOLT-uuJ6TWDiZw_ERUjxOOj1kbOGXk_zzdJyJh4zItqZu12v1dy1zva325OFIr5qnxoCWa0J0wZWNFrzYq73NTYIVADhGL6JMsXLpNh5GxuyOEOxryXKeTbqs7y24q1inohMa3kjDFCpxiM-qz4t56qU9g6dGNn1_SHhN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=PTbOlEDrH1mPDNNTxCTmKsACmybxLX-V-DYHyuLmAXjtzJfr3eTBzHii_JlqgUGRNSujH9jaxjjWbYHHa4HvcmFknQMkvZfHGHGPSgWxbXUneHHdKZd_ybqsRkRmfdOdLcWQe-iPaRWJyLV16mlJfYpJoYOSfV9LyUyJlmSF_bgFxbAOLT-uuJ6TWDiZw_ERUjxOOj1kbOGXk_zzdJyJh4zItqZu12v1dy1zva325OFIr5qnxoCWa0J0wZWNFrzYq73NTYIVADhGL6JMsXLpNh5GxuyOEOxryXKeTbqs7y24q1inohMa3kjDFCpxiM-qz4t56qU9g6dGNn1_SHhN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح: 'پاسگاه احمد ریزه
#چابهار
، شهرک بهار ، جاده‌ی رمین و چابهار' در سیستان و بلوچستان
پیش‌تر هم‌زمان با آغاز حملات آمریکا پیام‌هایی از شنیده شدن صدای چند انفجار در این منطقه دریافت کرده بودم.
چهارشنبه ۲۴ تیر ساعت ۲۲:۳۸
#Iran
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77129" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ_0uzQqTfxi5efNYX_rgLj24bLMQB6QaL0KZYesY8Cyy45f2RqoPZMlKdBhgR0hFWuA5KkHmef0SYQLH0uXP3-bkMO-Pdt6iR5ytMB5RIGzafuDyNy1H14yvapcO9N5Y9F7eZbGMJ9ZQKgejHrZb2YKHTkZ8aN5hBezjWi3nNTv5mIK2OQqIpgzJrCfpFc92qsWqPhkI-Z4LypnmUkH_JjrOTlTikcpUDjOHSYI6H3Tx_7jtfuHhJK7JFhow1LcKzLXmotTKQ5JTb8OCgoyNRDaHY4MKMXigxnAuuFqfpuTLszGjDBb42uzQpCfQ0MAEU8OheabNDwZ9sg_8HBK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخلی ایران از شنیده شدن صدای انفجارهایی در اهواز و چابهار خبر داده‌اند، اما تاکنون جزئیاتی درباره علت این انفجارها یا اهداف احتمالی حملات منتشر نشده است.
رسانه‌های ایران به نقل از استانداری هرمزگان از انفجار در شهر بندرعباس خبر داده‌اند. برخی از گزارش‌ها نیز حاکی از اصابت به شهر راسک در نزدیکی چابهار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77128" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ۲۲:۵۷ دوباره انفجار
یکی دیگه وحید 10:57 بازم سمت گلستان
دوباره اهواز رو زد ۲۲:۵۷
بازم سمت گلستان
۲۲:۵۷ گلستان اهواز بازم انفجار کل خونه لرزید
تو خونه میلرزیم خونها میلرزن
همین الانم دوباره زدن ۲۲:۵۷
اهواز ۲۲:۵۷ پشت سر هم ۳ تا سمت گلستان و کوی مجاهد خیلییییی نزدیک
انفجار شدید ۲۲:۵۸ اهواز
اهواز دوباره زد شد پنج تا
همین الان دوباره فکر کنم واسه 7-8 امین بار بود واقعا از همشون خیییلیی شدیدتر بود
اهواز ۲۲:۵۷ این هشتمین صدای انفجاری بود که شنیدم
۲ انفجار خیلی شدید همین الان
اهواز ساعت ۲۲:۵۷
دارن مداوم‌ اهواز  رو میزنن
سلام اهواز و سه چهار بار زدن آخرینش 10/58دقیقهصدای بلند که شیشه هالرزید
اهواز ۲۲:۵۸ یه انفجار دیگه.ما بهارستانیم صدا خیلی بلند بود
از ساعت ۱۰:۳۰ اهواز رو داره میزنه
🔄
الان باز گلستان زدن
بازم صدا انفجار ۱۱:۰۹ گلستان اهوا زشنیده شد
۲۳:۰۹ بازم انفجار گلستان اهواز
همین الان دوباره اهواز ۲ انفجار پشت هم ساعت ۲۳:۰۸
وحییییید ۲۳:۰۸ ۲تا پشت هم داره بقایی رو میزنه اونجا پادگانه
23:09 دقیقه خیلی بد زد
سلام ، اهواز سمت گلستان دوباره  ۲۳:۰۹ زدن
۲۳:۰۹ دوباره انفجار شدید اهواز
اهواز رو زدن دوباره
اهواز ساعت ۲۳:۰۹…سمت کیانپارس صدا شدید احساس شد.
وحید اهواز پشت پادگان بقایی و پادگان ملاشیه رو داره میزنه ۲۳:۰۷
ساعت ۲۳:۰۹ اهواز سمت گلستان صدای انفجار این چهارمین صدای انفجاره که میشنوم
اهواز همین الان دوباره انفجار داشت
نقاط مختلفی بوده و من دیگه نمیتونم تشخیص بدم دقیق که کدوم پایگاه بود، اما انفجار ها زیاده
تا ۲۳:۱۰ بالغ بر شش صدای انفجار شنیده شد. در اهواز هستیم. که جمله از صداهای روز گذشته بلندتر بودن.
اهواز ساعت 11:10 محدوده بهارستان* رو زدن
شش هفت بار دیگه هم از اهواز صدای موج انفجار رو حس کردیم. با سوت شروع مسابقه انفجار ها هم شروع شد
🔄
ساعت ۲۳:۱۶ موج بعدی پیام‌های مشابه درباره انفجاری دیگر رو دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77127" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XtuXWgu4VcuuygWxrWgalCe0bkJ6wfqwnQfqm9kMaShP2G5pRJW_DjXg6GgzGIOu29rgw4LljX_z6IAa2yKrMQ9X5BcXSbR1RZ_GyozfXqPlKkXJ0Afa4wcIb9LPp1zhQV5KcIpTrPnYWX8kLlP5jVcqVp39SzJjjwE5pqT54StgNW_tzDRtNHc2SNC9xI2MXlDx1Ib7LX-5OtRgsWS4RPhDMUT0erKal2FNRAu9PF5dWe_BRHClWuQGwLZTSedM-fPJ2TqbHeIHMptWazvGu1gFFel9zhcxQm7b0FqaB89q-_Y7THnp5fcAxTAKAp2qHHnNktlo_h-3pZnCZcxGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، نیروهای ایالات متحده عملیات دومین موج حملات امروز علیه ایران را آغاز کردند. این حملات توانمندی‌های نظامی ایران را هدف قرار می‌دهند که برای تهدید کشتی‌های در حال عبور آزادانه از تنگه هرمز به کار می‌روند؛ آبراهی بین‌المللی که برای تجارت جهانی حیاتی است. ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77126" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=Ng5aLSpphjc73epOWuhxSHGYXAe4uc9qwUfqJvU44ORo8OwZBWiRBrnqCiM5Ut2lfLIiyJ0bg8GqBgXcgcR18MsaxHglr15uqkyGyMM8dMFt8gpRKlacDZjCtVMdckmF4-e9-4duVUTcrFk8FEZmG863rR-MQ7n3DEAEF9BRpbgTkWCV65yXL8SRCI7ZxnDwlqDts6Vx676d9eOKeI5r4nRdfeA6wRi4VMyUS3Ftvy1JAg9GaC41W0lK4hwDkmdx0CaMQM_mgzwrPKTxGO4JiG3fYA2I1PgZu8Q69Ks6U5lujJ-gHBC9t1g7dw1XJ0nPlznwJTXC6pidiKPD0H7wSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=Ng5aLSpphjc73epOWuhxSHGYXAe4uc9qwUfqJvU44ORo8OwZBWiRBrnqCiM5Ut2lfLIiyJ0bg8GqBgXcgcR18MsaxHglr15uqkyGyMM8dMFt8gpRKlacDZjCtVMdckmF4-e9-4duVUTcrFk8FEZmG863rR-MQ7n3DEAEF9BRpbgTkWCV65yXL8SRCI7ZxnDwlqDts6Vx676d9eOKeI5r4nRdfeA6wRi4VMyUS3Ftvy1JAg9GaC41W0lK4hwDkmdx0CaMQM_mgzwrPKTxGO4JiG3fYA2I1PgZu8Q69Ks6U5lujJ-gHBC9t1g7dw1XJ0nPlznwJTXC6pidiKPD0H7wSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: ویدیوی منتشر شده در منابع محلی
پیام‌های دریافتی:
اهواز ۲۲:۴۸، جنوب اهواز کامل لرزید
وحید جان الان زدن ۲۲ ۴۸ اهواز لشکر
۲۲:۴۸  خیلی شدید تر از قبلی ها صدا انفجار اومد
انفجاری وحشتناک ساعت ۲۲:۴۸ اهواز
وحید اهواز کوی مجاهدیم ۲۲:۴۸ دوتا خیلییییی نزدیک زد
دوباره 22.48 اهواز، این سنگین تر بود.
همین الان سمت گلستان اهواز انفجار
اهواز باز شروع شد این بار صدا از سمت لشکر ۹۲ میاد
انفجار اهواز ۲۲.۴۸
صدای وحشتناک انفجار اهواز
ساعت ۲۲:۴۹
خونه کامل لرزید
دوباره اهواز رو زدن ساعت ۱۱ و ۵۰
اهواز 22.50  دوباره
اهواز بازم زد ۲۲:۵۰
دوباره زدننن خیلییی نزدیک بود 22:48
صداش خیلی زیاد بود
براى دفعه چندم اهواز ساعت ١٠:٤٨ انفجار بسيار شديد، انگار تمومى نداره
سلام شب بخیر
همین الان  اهواز ساعت ۲۲:۴۹  صدا  اینقدر زیاد بود انگاری سنگر شکن بود سمت گلستان
ساعت ۲۲:۵۰
بکی دیگه هم زد همین الان  قشنک خونه ها میلرزه
ولی صدای هیچ جنگنده نمیاد
یکم پیش اهواز رو زدن فکر میکنم ۹۲ زرهی باشه
همین الان سمت گلستان اهواز انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77125" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ56lP0e71dWkWDqPOrK6GGYkCwSzc92c29Bq05OJsnIdIjul_CfUOo4vqmfUtz_yF1MBcI028SXw3jYEYljQmtLtnUamsPn3DDNuv4grm8xKdoXclQw9OR4fGcRbW5tG6RwErcQfczQ2pfqwEbxbmK8X398X3Et3VCy0VfFbxwKGprQ0EB9MHtslBFz_PkkC1wSHzzQUwH4AbHlbEQIgJXcWweuv3heEIXJ7ZyV2fyb2uYAdn1YX-uh5KyaLDxhkmbNeW3uRf_lh6-iwdyQUml-epWPLzL9wP8F7CIgha9BbakExtSoOrYDRJm5_rhgh1-y3FsAWkOqcYioPYjxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه در پاسخ به پرسش خبرنگاران درباره این‌که آیا پیش از آغاز حملات آمریکا به پل‌های ایران، مهلتی برای تهران تعیین شده است، گفت که علاقه‌ای به تعیین ضرب‌الاجل ندارد.
ترامپ گفت: «من دوست ندارم مهلت تعیین کنم، اما آنها تقریباً می‌دانند؛ آنها از ماجرا خبر دارند... بهتر است رفتارشان را اصلاح کنند.»
این در حالی است که رئیس‌جمهور آمریکا ساعاتی پیش حکومت ایران را تهدید کرده بود که اگر تا هفتۀ آینده با واشینگتن به توافق نرسد، نیروگاه‌های این کشور هدف قرار خواهد گرفت.
او به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77124" target="_blank">📅 22:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در لابلای ده‌ها پیام از اهواز این چند پیام رو هم درباره چابهار فرستاده بودند:
همین الان صدای دو انفجار شدید در چابهار ۲۲:۳۸
چابهار ۳ دفعه صدای انفجار شدید اومد
درود
چابهار صدای انفجاری مهیب اومدددد الان
سلام
۲۲:۳۸ دقیقه ۲ بار چابهار زد
هنوزم صدای جنگنده میاد.
همین الان چابهار زدن
چابهار رو الان زد سه انفجار ساعت ۲۲:۳۵
آپدیت:
سلام ، چابهار رو سه بار زدن ، خیلی بد بود ، احتمالا یه پاسگاه مربوط به دریابانی به سمت جاده رمین
ده دقیقه پیش دوتا انفجار چابهار
سلام وحید پاسگاه کنار خونه‌ی مارو زد
چابهار
پاسگاه احمد ریزه
جاده‌ی ساحلی رمین
سلام چابهارم زد
📡
@VahidOnline
آپدیت
:</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77123" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#اهواز
پیام‌های دریافتی:
انفجار اهواز ۲۲.۳۱
سلام اقا وحيد
10:30 اهواز دو انفجار بسيار شدييددددد
اهواز دو انفجار خیلی شدید ساعت ۲۲:۳۱
سلام وحید جان
۲۲:۳۱ اهواز صدای سه تا انفجار اومد
سلام، اهواز ساعت ۲۲:۳۰ صدای چنتا انفجار پیاپی اومد
اهواز ۲۲:۳۱ صداش مهیب بود
ساعت ۲۲:۳۵
صدای انفجار مهیب اهواز
اهواز شروع شد با شروع بازي
یک صدای انفجار خیلی ترسناک با لرزش زیاد اومد تو اهواز ۲۲:۳۰
دقیقا دیشب هم همین موقع بازی زدن
ساعت ۱۰:۳۱ صدای سه انفجار از  اهواز
ااهواز همین الان زدن
اهواز دوباره ساعت 22:31 دو انفجار پشت سر هم
وحید جان سلام
اهواز ساعت ۲۲:۳۰ همزمان سوت شروع بازی فوتبال ۲ تا انفجار
سنگر شکن بود احتمالا
زمین لرزید
سلام وحید جان،
اهواز ساعت ۲۲:۳۰ صدای انفجار اومد
شیشه ها لرزیدن
اهواز صدا انفجار اومد موجش زیاد بود
سلام وحید اهواز رو زد ساعت ۲۲:۳۰
ساعت ۲۲:۳۱ دوباره با شروع بازی اهواز انفجار
اهواز وحشتناک بود
۲ انفجار سنگیننن
ساختمون بد لرزید
🔄
الانم زده ساعت ۲۲:۳۵
دوباره انفجار اهواز ۲۲.۳۵
دوباره زد
دوباره خیلی شدید تر ساعت 22:35
دور بود خیلی اما اینقد سنگین بود خونه لرزید چندبار
صدای دو انفجار همین الان ساعت ۲۲:۳۵
۲۲:۳۵ اهواز بازم زدن بار دومع
۲۲:۳۵ یکی دیگه اهواز زدن
اهواز یه انفجار دیگه ۲۲:۳۵
همین الان یکی دیگه زد. سنگین بود ۲۲:۳۵
پشمام دوباره
زمین میلرزه، اهواز ۲۲:۳۵
دوباره ۲۲:۳۵ انفجار اهواز
سلام وحید جان
همین الان دوباره ۲۲:۳۵
ساعت ۲۲.۳۴ انفجار دوم
اهواز
این یکی شدیدتر بود
دوباره زدن، نمیدونم نزدیک تر بود یا انفجار قوی تر بود، سمت جنوب اهواز ساعت ۲۲:۳۶
۱۰:۳۴ دوباره یه موشک دیگه زدن غیر از اون دوتا این یکی از اون دوتا هم بدتر بود خیلییی بد بود
🔄
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
۲۲:۳۷ الان هم
10:37 اهوازو زدن
بازم انفجار پیاپی اهواز ۲۲.۳۷
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
آقا وحید بد گیر داده
۴ تا دیگه
۲۲:۳۷ باز هم اهواز دو تا صدا پشت سر هم
اهواز دوباره زد الان دو بار ساعت 22.37
اهواز ۲۲:۳۷ بازک زدن صداش بلند بود
سلام دوباره دارن میزنن ساعت 22:36
۳تا دیگه پشت سر هم ۲۲.۳۷ اهواز
خیلی محکم داره میزنه
یا خدا ۳ ۴ تای دیگه زد
یکی از یکی ترسناک‌تر
اهواز ۲۲:۳۸
با سوت شروع بازی ، انفجارهای پیاپی.
اهواز روی لرزه‌ست وحید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77122" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOs0pzcH7tW44k8z-U8IGEzmXDRdZV8yGs1uJKtfelmpA9I-qq6xAjHsWyZynDbGGy8sn5o18Re8yEZTbSuHZHZ5PHqyPTKnQPuEzJD0wCJyZ8LtAPgmqvdYirTY22q344OxYmCBFiDdyw8XhXqoKeOTVXD9KW9KB8x3gdlEsaTrRuSxGnidv5LqZYmMN4lrhNxlrvJ6fa1m0eqSzGF5El_fQkr0cnKTxOywYMVaI3HNOBzIk1_3HHjG3n_Oxn2iwplwgSq7Pc_fqaT5BO-nZyh4rAw2mGe3wm83yWqY_XQ3_8dQ5GS93sCUGBfLnqP-Cwq4IrdKCvToXyNJRGY0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام عارف خوشکار، از بازداشت‌شدگان اعتراضات سراسری ۱۴۰۱، سحرگاه امروز چهارشنبه ۲۴ تیرماه، در زندان قزلحصار کرج اجرا شد.
masoudkazemi81
یک منبع مطلع نزدیک به خانواده این زندانی سیاسی به هرانا گفت: خانواده عارف خوشکار حدود ساعت هشت صبح امروز از اجرای حکم اعدام وی مطلع شدند.
همچنین به خانواده اعلام شده است که برای رویت و تحویل پیکر، صبح پنج‌شنبه ۲۴ تیرماه حدود ساعت ۹ صبح به بهشت زهرا مراجعه کنند.
این منبع مطلع در ادامه افزود: عارف خوشکار روز شنبه ۲۰ تیرماه به سوئیت ۳۵ زندان قزلحصار منتقل شده بود و خانواده‌اش روز یکشنبه ۲۱ تیرماه آخرین ملاقات را با او انجام دادند.
خانواده او با درخواست اعطای مهلت یک‌ماهه و برگزاری جلسه‌ای برای جلب رضایت خانواده مقتول، در تلاش برای توقف اجرای حکم بودند، اما این تلاش‌ها به نتیجه نرسید.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77121" target="_blank">📅 21:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیانیه محمدباقر قالیباف، رئیس مجلس شورای اسلامی
،
به نقل از منابع حکومتی:
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🔹
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🔹
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
🔹
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.
🔹
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد، در غیر این‌صورت اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم و همانطور که این روزها شاهد هستیم، نیروهای مسلح ما مثل همیشه برای مقابله با تهاجم دشمن آزادی عمل کامل دارند.
🔹
ما بر خلاف جنگ 12 روزه، به درستی در جنگ 40 روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
🔹
حالا برای تحقق این موضع ما چه فرایندی را طی کردیم؟ با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند. در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند 5 تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای 4 بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم. حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم، آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود. دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔹
ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است. این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است. جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است. ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔹
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی امام شهید انقلاب و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
🔹
راه پیروزی و احقاق حقوق ملت در این جنگ و شرایط حساس، پیروی از رهنمودهای رهبری و حرکت  براساس یک  نقشه‌راه دقیق بر مبنای مقاومت، عقلانیت و استفاده هوشمند از همه ظرفیت‌های دفاعی و دیپلماسی در جهت تحمیل اراده خود بر دشمن و کم اثر کردن تبعات اقتصادی جنگ به مردم، است.
🔹
مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قوا است و همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند، برای جنگ یا دیپلماسی یا هردو تلاش کنیم.
🔹
بر همین اساس از همه ملت ایران با هر نگاه و سلیقه‌ای می‌خواهم در تبعیت از اوامر رهبر معظم انقلاب وحدت را حفظ کنند، در میدان باشند و این حضور و وحدت را به رخ دشمنان بکشند. همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید.
🔹
همچنین به اخباری که توسط عده‌ای منتشر می شود تا شما را از مسیر طی شده پشیمان و نسبت به آینده ناامید یا نسبت به خادمین ملت بی‌اعتماد کند، نباید توجه کرد. دشمن به ناامیدی، ترس، اختلاف و بی‌اعتمادی‌های متقابل طمع کرده است. حتماً حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند.  مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت خود را به فضل الهی خواهید دید.
🔹
اینکه ما امروز از موضع قدرت در تنگه هرمز سخن می‌گوییم، نتیجه‌ همان قدرت میدانی است که مردم برای ما ایجاد کرده اند، و برای ما مسجل است که انتقام خون آقای شهیدمان را نیز به ثمر خواهیم نشاند و دشمن باید بداند که هیچ کوتاهی در تحقق مطالبات خود نخواهیم داشت.
🔹
بنده به سهم خودم در دوران جنگ تحمیلی سوم، هم در میدان دفاعی و هم در مقابل طراحی دشمن  در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام.
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های رهبری معظم انقلاب است. عمرم را صرف مبارزه با دشمن کرده‌ام و هراسی نیز از جنگ با دشمن یا تهمت و تهدید و تخریب نداشته و آرزو دارم در این راه به رفقا و رهبر شهیدم بپیوندم.
🔹
در انتها به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما، در مهم‌ترین سال‌های جوانی من و خانواده‌ام پای سفره‌های مهمان‌نوازی شما در مناطق عملیاتی جنوب نمک گیر شده‌ایم، گرمای عشق و محبت شما به هموطنان خود و به ایران را هرگز فراموش نمی‌کنم.
🔹
بدانید که ما سرمان برود، پای قولمان هستیم، شاهرگمان را برای دفاع از این مملکت گرو گذاشته ایم. به فضل و منت خدا بدانید که پیروزی ایران عزیز نزدیک است و مقاومت تاریخی شما ماندگار خواهد شد.
🔹
مردم عزیز ایران! ایمان داشته باشید که این بغض‌های فروخورده شما و این وحدت بی‌نظیر تک تک ملت ایران در کف میدان، پیروزی ما را تضمین خواهد کرد. ما نه تنها از تهدیدها و جنگ با دشمن نمی‌هراسیم، بلکه تحت ارشادات رهبر معظم انقلاب، پاسخ قطعی این جنایت‌ها را به دشمن جنایتکار خواهیم داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77120" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77117" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YSvXZn68JwRBfYCPr_GPFgOT2ZablaT3d2qINgpRfP3HUW3DIXc_MDrZga5HyA3RDqMMPo17OFlkxO8EJM98lB_nnEjnlmELuiIYdrf67p2ivQz22fsMeezH53hNVtTEhpZMQ7CfRs_W0k5kr3QnymIsxkmebLHUrFWcTzNHW9a7FnZg6l-Ov3myoMMRxeKe6dQRsN9tKVuUatqpbXepuo2rTaoLNDyE0_Os91dmajTdwc7LV9NH8GMJSie8tCjazxXuTGpswd-OPBcavOgl_Wj_MLQPR4P_H37_j6tD4C0SouJaZFAy26EinuACGRfSnFWbPApcgmoe3fV2qm_Ntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران مدعی شده‌اند که نیروهای آمریکایی در ۱۴ ژوئیه یک تأسیسات غیرنظامی ذخیره‌سازی گندم در هویزه را هدف قرار داده‌اند. این ادعا نادرست است.
✅
واقعیت: نیروهای آمریکایی در ۱۴ ژوئیه اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. هم‌زمان، ایران غیرنظامیان بی‌گناهِ در حال عبور از تنگه و همچنین غیرنظامیان در کشورهای همسایه خلیج فارس را هدف قرار داده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77116" target="_blank">📅 19:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1KKLwbqBbQgAzvTExlePRInH5VFU8qDB-D5TP_WwGsHHC0kPouRR72fvCnHXAqVK5a29OPYlhFFN7PJvGrr0s9FT98apPnYtIu5NT-u6p5Q3z7KDBhbCoyiZNto2aRFOWtlIHwKPvHcge3QIUEhhmLWcB8KI8MSGAj7A06IVLJpokxtCqLsC4qOtthCjJ9yyCJye2fwnqSpM6nTU214M622f2WIwQ4dD79_YctPjlLgGGtyQNgmeKRd9LPv-9qJKagslL3A__xO--a1hOZdUOquVv9GwbVBTgcYSs1crE56DEDYutumlfxudR1y-sx5l_JblxppnNx0-r0sFctq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=ayc7-CfonCLnIkIcttbwrAIwOUjnCCHnNxpqplTWOJUZA_QHpYR0a0iPbQcFnQHEpDPOH3YfFknv6oAWiaKUapFB7cBeDYURGwjcTGm_J9FmncUifoiTMQpxRTON3Ek_MRrxckvfdCy0KHi5u3R2TTUeEQtkf8BvrrjzGECpoJe0-pPKto27DKQaOPONRMEza86HWWRyeIS9_WbO4eSB2TFayY7RtHQWuNLfKpKXYJSMr2zZOICKWjBrDEfbFJqv9g-Of37tKw13uZ8rfJCpY8jVzA22arDsTfjL-cayXOjlSbWxWSDbT87IAQwBzntE3C-SVTjqL5H3IkoyvauV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=ayc7-CfonCLnIkIcttbwrAIwOUjnCCHnNxpqplTWOJUZA_QHpYR0a0iPbQcFnQHEpDPOH3YfFknv6oAWiaKUapFB7cBeDYURGwjcTGm_J9FmncUifoiTMQpxRTON3Ek_MRrxckvfdCy0KHi5u3R2TTUeEQtkf8BvrrjzGECpoJe0-pPKto27DKQaOPONRMEza86HWWRyeIS9_WbO4eSB2TFayY7RtHQWuNLfKpKXYJSMr2zZOICKWjBrDEfbFJqv9g-Of37tKw13uZ8rfJCpY8jVzA22arDsTfjL-cayXOjlSbWxWSDbT87IAQwBzntE3C-SVTjqL5H3IkoyvauV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو پدر سام حسنی از محل واقعه منتشر کرده.
کودکی که در میان جعبه‌های گیلاس کشته شد.
پنج‌شنبه ۱۸ تیر:
نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
@
VahidOnline
در جریان این تیراندازی، گلوله به کودکی که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77114" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱۷:۳۸
[جزیره] هنگام، الان صدای ۲ تا انفجار بزرگ اومد سمت وسط جزیره
جزیره هنگام رو همین چند دقیقه پیش دوبار زدن
📡
@VahidOnline
🔄
ساعت ۱۸:۳۹ خبرگزاری مهر
:</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77113" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rjMGM3QqQKeDy2Ood7KU2Ejs62hLLOSTS3omKbs1Ce0c4ixpiM5v65OAx9vd0VVGbaSzpHiy59KdBQDdCk-5vDNUKTK4cDCdOMMVvJjVlp0uawfeD70tLk0192k_PnHIWZ8RazI5IdwUMFG0-nfOH_QQR7oHy0yIWyXYmmP1mWxa7yuKyGuFUljaTmX5kB-_IY0WsCoJ1r1uaAN6QT8pnEkFjWGoNuo3gLN7LZF4qCrlCap5BjEdUlDgG26wOIzV8NXqrJkAVpkdVydeNBtXVuXHZKn3W3sBNfuXJBcbJTuPRCPkUDJydlxA8LiZfGrgNwCUTZyOtXYgs6PDfzvtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p0yjTXHBQt-fKfhxP1TyxeSCQHIlP2_DIWd4_6vyb-cl4oJdeOxeg5jryvUOpGMxYB9n4M1EgRwPZrzPc592flDjr_sk04f83FCxiubTqxrv7bQkiGwg1uS0F7GvwnJI_RD1BxxCDTa4IVq1llFOi9sZXoUKbodp8syGSUmGwdhGjQzPECYGB73KSzSu_KZg5Q981FBXUV9Ea5Yg7i96q2pAUo5gzRc3QRbxCCpw3ziUxLpFxX40DbhyybEMv92MijF3EfEG5fuEww10Ktdr6_oeVWHKMTudzp5qYRHqUCCf40MCo_LHVMEem09qt5Ft4NjDIpA_m8qpBtvtt85NZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بیانیه فرماندهی مرکزی ایالات متحده (سنتکام) آمده است: از زمان ازسرگیری محاصره دریایی بنادر ایران، ۱۷ ساعت پیش، نیروهای ایالات متحده مسیر حرکت دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند.
@
VahidHeadline
صدا و سیما چهارشنبه ۲۴ تیرماه گزارش داد که در ۲۴ ساعت گذشته دست‌کم دو کشتی که به گفته این رسانه قصد داشتند بدون هماهنگی با ایران و به‌صورت غیرقانونی از تنگه هرمز عبور کنند، پس از بی‌توجهی به هشدارهای اولیه، با شلیک اخطار نیروی دریایی سپاه پاسداران متوقف شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77111" target="_blank">📅 17:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGuS5aSCtDBeVISnJAkzB82T7utXxCxzCShbQpptQX12231b6hkjMdehSfAWiweFY8Xz3mqRclsqbwmSd6moyh-FHfG1c87Qdf2O0mp7fYfNZuWwnf1UQ6djgdbaBRPVmmAHoLyYubwLxVunq_G-3eLZRXKX9ajYV5RkQnjmG4ILcFfmsOVcpTyApo4YJX0W9NlIPlgskzhX3huN7-BYUGaTNMDDGEnBrYxM2QDEP5TJxVFNDN8PBdxhRbu3BBjp0WwM1hs7g_Ltnr-rFvC_nUkIdJGBEnYaiefKlJTtQkX-fxngbHxpWk8U3SHrKkozKXyHASLpvsSPR4AZnkH3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده کریگ فورمن، شهروند بریتانیایی زندانی در ایران، روز چهارشنبه ۲۴ تیر اعلام کردند که او در زندان اوین به دلیل انجام مصاحبه با رسانه‌های خارجی، به دو سال حبس اضافی محکوم شده است.
کریگ فورمن و همسرش، لیندزی فورمن، در جریان سفر زمینی با موتورسیکلت از اروپا به استرالیا، در ایران بازداشت شدند. این زوج اسفندماه سال گذشته از سوی دادگاه انقلاب به اتهام جاسوسی هر کدام به ۱۰ سال زندان محکوم شدند؛ اتهامی که همواره آن را رد کرده‌اند. مقام‌های جمهوری اسلامی نیز تاکنون هیچ مدرکی برای اثبات این اتهام به‌صورت عمومی منتشر نکرده‌اند.
پیش‌تر وب‌سایت حقوق بشری هرانا گزارش داده بود که  این زوج ۵۳ ساله در اعتراض به رد درخواست تبرئه و جلوگیری از آزادی و بازگشت به بریتانیا، اعتصاب غذا کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77110" target="_blank">📅 16:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jL9Qa-m-xA15nex5bDgkt_revlCf-KZDt8cFnvjUmwJQlEDf2XogyIEttIsJghDub8VsImFQqPOXJpvciBWJdSBug-VsZR36FKElitYtGf1OeVvv6tff8u6I02hbXlVylrvNVzX-QfNkGUndXs0dyaCMnXUUF39O71v9nRHE8EBLyccI_cWX70SQFBNXfHLZKN-86sodq4Ez6I4R3J_Kmj9Z2tQGGYtuC0YyvyGVy_uFQfTChb7fzfDW1y3mtyl4MXPFRB-YTwqHTnn3yK87CsocQwGFJcQjYcaXuOuvWM1HD1TomtsPbiNbSbYcgU62B00lXFyEm7cuIu8C07PMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت دولت:
اطلاعیه ستاد عالی آزمون‌ها در خصوص برگزاری امتحانات نهایی در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
ستاد عالی آزمون‌های وزارت آموزش و پرورش در اطلاعیه‌ای اعلام کرد:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در روز پنجشنبه؛ مورخ ۱۴۰۵/۰۴/۲۵ و پایه یازدهم در روز شنبه ۱۴۰۵/۰۴/۲۷ لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🔹
بدیهی است امتحانات نهایی سایر استان‌ها و امتحانات بعدی استان‌های مذکور، بر اساس برنامه ابلاغی در موعد مقرر برگزار خواهد شد.
dolaat.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77109" target="_blank">📅 15:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=MBG_mgcPbCwKYtcLJiDjz_EUdkDGczSERu3rNYdzKtmDD-Ugt1BqKDDun8__ZwZ9zw5hDG6_qH4o9-W27vQNmCfVa0Z_WycPHKVCj44CvbPGPJDwsFiI18pMo9pjXPv_BuwgWfaFdPKZELDgKrKP0d_rrpNBbeaXGj8VZP5dA_Y12m8_pGyLtF64eZO7eUwTgllEciCXMGMTo7GaVk4RPqFXzgY2u5c1UhdynmKV1U-y5t56mVbV4wzFIkStBxqwAJj0isNDPg0BEIMaFOBXET0sPFCnX0f8av4usgTjrxPMALNJ-y-7r30odU-81hOZ68wb1MtAjea8bOEDFUn3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=MBG_mgcPbCwKYtcLJiDjz_EUdkDGczSERu3rNYdzKtmDD-Ugt1BqKDDun8__ZwZ9zw5hDG6_qH4o9-W27vQNmCfVa0Z_WycPHKVCj44CvbPGPJDwsFiI18pMo9pjXPv_BuwgWfaFdPKZELDgKrKP0d_rrpNBbeaXGj8VZP5dA_Y12m8_pGyLtF64eZO7eUwTgllEciCXMGMTo7GaVk4RPqFXzgY2u5c1UhdynmKV1U-y5t56mVbV4wzFIkStBxqwAJj0isNDPg0BEIMaFOBXET0sPFCnX0f8av4usgTjrxPMALNJ-y-7r30odU-81hOZ68wb1MtAjea8bOEDFUn3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از دکل مخابراتی بندرعباس پس از حملات نیمه‌شب سه‌شنبه و بامداد چهارشنبه آمریکا در صبح چهارشنبه ۲۴ تیرماه در شبکه‌های اجتماعی و رسانه‌های داخلی ایران منتشر شده است.
بر اساس این تصاویر، بخشی از تاسیسات مخابراتی در این منطقه آسیب دیده، اما هنوز جزئیات رسمی درباره میزان خسارات، اختلالات احتمالی ارتباطی یا هدف دقیق این حمله اعلام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77108" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
