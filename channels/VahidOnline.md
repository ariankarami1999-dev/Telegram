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
<img src="https://cdn1.telesco.pe/file/lpY-ME0Mc0Emf0IIp9JGQz_sjZcxQ3Cy5hDTkskn7j-3EDKyAuwopNDbn0Mn_TYsmfygG5AIC4vrQa1fzSmajUXjmc6EJ8KfVBFkVoNV9pi228104EWKBB3z8T_AX-vGYiP5ylJSDcI-EQQ7XdUBL2ygOmEovjpEOMeNLr8O9soBAmoQVD-sMUxPT_vdHOIFsDSBOfEc23ntHLEkV7dzn1jkBVRLCadR-3lhDPlgNRKOY_OE1aEw-BlKp70FixRiTg3RiqmNYkCbDzKHcfsveMTSmFHSFXS0kY7WdYIu_JIOK0J09t-3Cd3Y7q-Mg1TKitRDj3ABLtc5fW2mM70SvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bccWKMZpKqmMYjCTSDnYabOY2N8EvQtgFy-J0GlnWqL4saIG5FonFnoX6SI9hd89AwGi8MIX9SWvV5PE8-WXawpjjJ-_TQ074FFoKrXtih_QnThQhgFXWmxqm7iFzAkDzF3nDnR0G-d3jPKuyUQZo_oDcbv7ceAJOyXbm51_pVn9XnnqgtS5vd-7BPgPUIK5jZcCmeB9RIza4SNfF9o4AUR41TJ8l_jnE_mbdb1L1ZBgzEOQ4nw9DW2JY7XeuQ6bxP8gxhu2FQa90rkf-sGiPRjO_s39sVn_OkULMsiGMkG_bccG26i6G8MssBBO9SwLKsnE5qfXq_mToFD0wmcC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک نفتکش در تنگه هرمز «هدف قرار گرفته است.»
براساس این گزارش، این نفتکش «هنگام عبور از تنگه هرمز و خروج از آن» هدف قرار گرفته است.
سازمان عملیات تجارت دریایی بریتانیا گفته این حادثه در فاصله ۳۱ کیلومتری شرق منطقه خصب عمان، «هدف اصابت سه پرتابه ناشناس قرار گرفته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/78122" target="_blank">📅 03:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78121" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FX3p9yewFc6DsvYgE_DXDtMgLJO10LBsx0lTexxji7XrQE7zlxOvX4YUzf1B-qfpXJowvoTiJZPb9BwrGDOMEh6yFVSEeQYVfkXvIivzDbykUJ034yX3TCBGeaUh8kMfSzbhn-cKZHI1QpW-Lecy1HukpAgycrLP9bVir_PHkTH5DlYuBQWTBv1-ViWA3ZjxiO4qVgtnx5_VBEOumSX9ddNj_pOI85d67vZFlf5WfmgEECCQ5QX0GAo96r9uH1sTVzuvQDE-lP3On9WJNMb2N1GA1sEY03aBIrbF2scdSsrz5nLmOBw84doToGWakaHC55m98YdR0v4TamX7slN7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه مقام آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهور آمریکا، و مشاوران ارشدش در حال بررسی انجام حملات محدود در تنگه هرمز برای جلوگیری از بازسازی توانمندی‌های راداری و موشکی جمهوری اسلامی جهت حمله به کشتی‌ها هستند.
بر اساس این گزارش، این طرح که طی هفته گذشته توسط فرماندهی مرکزی آمریکا تهیه و از سوی وزیر جنگ، پیت هگست، حمایت شده بود، پیش از تبادل آتش این آخر هفته با ایران به تایید ترامپ نرسیده بود. اما او ممکن است پس از تشدید جدید تنش‌ها با آن موافقت کند.
یکی از مقامات آمریکایی گفت ایده اصلی این طرح، کاهش خطر حملات تهران به نفتکش‌ها، شناورهای نیروی دریایی آمریکا و هواپیماهای نیروی هوایی آمریکا است؛ به گفته این مقام، هدف «کوتاه کردن چمن» است.
یکی از مقامات کاخ سفید گفت: «رییس‌جمهور همه گزینه‌ها را در اختیار دارد. ایرانی‌ها می‌خواهند توافق کنند، اما همیشه یک روز دیر و یک دلار کم می‌آورند.»
ترامپ عصر دوشنبه به فاکس‌نیوز گفت که آمریکا به حملات جمهوری پاسخ خواهد داد و «آنها را به‌شدت هدف قرار خواهد داد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78120" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FurOKp5E-LUKe6XlFcDt4QwLg8VO_nM5MXzUvqjrYvD5_X5sNwsBWUfUgrnWDNpt0gCPReqIfH3f9-ZW945SRvl6vVTABdwSBIRT_DzAMla0oiRRo2sEBQnZteyK2teJaEPUr6LmnkqatjhPcWR2QK80KPKw5EmPqmEwvawmF-RIoT_uqkwQ9It9dmX3qERqEU-ejNGb-INM3jvsJQUbe7zYR1O_APcsFrq-DEOUNPhiO50bPR45fvFrOzceG4RL5Vk_UCkyBELdE-MitUuehykfEIVxix0z068Rie5kTqMaW5BdOC1PUPGo5hd8WkHtxR-miVNxTyVfq7qv-MfHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح جمهوری اسلامی روز دوشنبه در بیانیه‌ای مدعی شد که ایالات متحده از آسمان یا خاک برخی کشورهای خاورمیانه برای استفاده از ایران استفاده می‌کند و هشدار داد آنها را هدف قرار خواهد داد.
این بیانیه ساعاتی بعد از آن منتشر شد که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد ارتش این کشور به حمله شب گذشته ایران به نیروهای آمریکایی در اردن، ایران را به شدت هدف حملات انتقام‌جویانه قرار خواهد داد.
ستادکل نیروهای مسلح ایران در بیانیه خود گفته است «ضمن احترام به حاکمیت ملی همسایگان»، در صورت ادامه حملات آمریکا، نیروهای نظامی جمهوری اسلامی «پاسخی سنگین‌تر» از حملات شب گذشته خواهد داد.
ارتش آمریکا اعلام کرد شامگاه یکشنبه «نیروهای مین‌گذار سپاه» در جزیره لارک را هدف قرار داده است. در پی این حمله، سپاه پاسداران از حمله موشکی به دو پایگاه نظامی در اردن خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78119" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7KEzwDj8Kj3b-X24ZTkksuLZBX8yUxsJhSwB9EkDuokzNodfmJz1GXmh2JQlk2o5PjqDWiLy63C7M1zdp8nnSQ4RvnxYM4vQhFAFXyS6A8YyjXsc2jRh2mpjoXTLxuRZQ4mkCfx4ta1_Sj917UoZnDcKjDxjPrqfKkcw-az9xdS8RafAVfT5-OhQF9qZ9duA5noDCcXi3b4ZGCf_dBa1BiEtrtMq7nF7zNfTsTAd1XtvcupXAB2Kbgc_VnuTOEiL1KoMUclwcau3iseektfFFqRo89yX4oCjyjyXq4Q8bdbfULjcQVjgjlDcZv-OjZfNUjbYH2uvSYYUee5r_GPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه عربستان سعودی روز دوشنبه نهم شهریور در بیانیه‌ای اعلام کرد که کشور‌های عربستان سعودی، ترکیه و پاکستان توافق کرده‌اند در قالب «پیمان دفاعی مشترک مکه»، دبیرخانه‌ای را در عربستان سعودی تاسیس کنند.
بر اساس این بیانیه، ریاست این دبیرخانه در سه سال نخست بر عهده دبیرکلی از کشور پاکستان خواهد بود.
در همین راستا، وزارت امور خارجه ترکیه نیز اعلام کرد که تنظیم سازوکارهایی برای پیوستن سایر کشورها به این پیمان، در دست بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78118" target="_blank">📅 19:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=sj1JlfDNIoQkc4CwE763QFMUmIG3zjpyO9-px7l9Nw5VQk8U6VwgjIPTV27vxBvopsrn_S4SuOhnhK5wU4XipLPpwYywSH8eQd-GqjEWi8kJ1LK2YLxQkiwUi_Avi85KiiPpys87xu13zzeq0QHBDjP-2_-7xULJV41zrc91weZ6zptdSXqwdosOP-0aowPUOLxJwf-k2egJ0glx9WiiBIOQKsBUfduLQziS2oSmWQ4CP5dV0x88qGawYLowj98uEWSrwEWFNlwNyWShnJwRlIfwtYoURKcgU-T4NWt-0irdkf_nPtU8SNBNLa47xc1NcXeBhyAoOv4dQJJD3noa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=sj1JlfDNIoQkc4CwE763QFMUmIG3zjpyO9-px7l9Nw5VQk8U6VwgjIPTV27vxBvopsrn_S4SuOhnhK5wU4XipLPpwYywSH8eQd-GqjEWi8kJ1LK2YLxQkiwUi_Avi85KiiPpys87xu13zzeq0QHBDjP-2_-7xULJV41zrc91weZ6zptdSXqwdosOP-0aowPUOLxJwf-k2egJ0glx9WiiBIOQKsBUfduLQziS2oSmWQ4CP5dV0x88qGawYLowj98uEWSrwEWFNlwNyWShnJwRlIfwtYoURKcgU-T4NWt-0irdkf_nPtU8SNBNLa47xc1NcXeBhyAoOv4dQJJD3noa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا ویدیوهایی ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.  ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»  این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر…</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78117" target="_blank">📅 19:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=DbXVejIyCkQ4JVisXOXo3Ogp1YrGqmEOh7_kDBI-MbLQC9U_ONOX2GhkER7PwvOj3DaT7hTKIxvlqDyYpa0cDgtm9qdUV--rUoJ_MJs8kT0nm6wVZxoaY_6eNNWF_0XKe9Vq8JA4mF15M3P14yIaOR3JPkSZ6j4LEZKW6s6m1LUMgOW1ezRIz_KSYBVFdmLwunbGhAY7qrKEraVjaukV-fonQLJ5ZhmHoGbZMYSvwkhO4E2xsfBNGRlQozTQj8khnD6M1cM7F-XuQudHx2EyKWBvHHLnfSGjkvlOKgGhO8GqeEyjXOjvDAe759RIz7xmgt10ujIOLd5IKK_6Q08VSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=DbXVejIyCkQ4JVisXOXo3Ogp1YrGqmEOh7_kDBI-MbLQC9U_ONOX2GhkER7PwvOj3DaT7hTKIxvlqDyYpa0cDgtm9qdUV--rUoJ_MJs8kT0nm6wVZxoaY_6eNNWF_0XKe9Vq8JA4mF15M3P14yIaOR3JPkSZ6j4LEZKW6s6m1LUMgOW1ezRIz_KSYBVFdmLwunbGhAY7qrKEraVjaukV-fonQLJ5ZhmHoGbZMYSvwkhO4E2xsfBNGRlQozTQj8khnD6M1cM7F-XuQudHx2EyKWBvHHLnfSGjkvlOKgGhO8GqeEyjXOjvDAe759RIz7xmgt10ujIOLd5IKK_6Q08VSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه نهم شهریور ماه در حاشیه نشست «جی ۲۰» در اشویل آمریکا گفت واشنگتن به اعمال فشار اقتصادی بر تهران ادامه خواهد داد و ممکن است نتایج این فشار طی هفته‌ها یا ماه‌های آینده نمایان شود.
بسنت در پاسخ به پرسشی درباره زمان احتمالی فروپاشی اقتصاد ایران گفت: « مسئله این است که ما محاصره را داریم و به اعمال فشار ادامه خواهیم داد. ما همین حالا گفتگوهای بسیار خوبی در اینجا داشته‌ایم و فکر می‌کنم این می‌تواند طی هفته‌ها یا ماه‌ها رخ دهد.»
وزیر خزانه‌داری آمریکا افزود: «اقتصاد لزوما نباید فروبپاشد؛ فقط باید حکومت ایران به خود بیاید.»
این مقام آمریکایی افزود بسنت در حاشیه نشست گروه ۲۰ با همتایان خود دیدار خواهد کرد و برای افزایش فشار اقتصادی و منزوی کردن ایران تلاش خواهد کرد.
اسکات بسنت، در ادامه با اشاره به حمله ایران به پایگاه‌های نظامی آمریکا در اردن گفت: «به نظرم آنها به‌صورت نظامی دست به واکنش می‌زنند، چون از نظر اقتصادی در حال شکست خوردن هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78116" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=k-n7PbUDg9oGQNvbxoh-Nicvclo0egqVeGmi_-AVw1da1OjhTbIb6UYUroXa31sexAHB8TL3w-h-C3UIF-AR7bhxCJughczwiLdZZvrs9rvuEAmVbCod0Xv8Nl1xkXFnmwOukgLvj_7YR8_juE_dehOGisCNINI6GYp3xt9g9p-_DcTYEJAawVX5FWx9AyvKDXTPAbNHzg7RDUutJ0e2UKsHWShA4uigTOr39GpdBsv0sx9nlxSFH9MCrExQY1B9R4wtdNv1_eBVBYTKW8ztdeOLIq6uJSSaY_ebZ6CRLLmNdEnzcu6QLZD-BUpk3EH3lLlH0gAGVl2QBPqgFjHugA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=k-n7PbUDg9oGQNvbxoh-Nicvclo0egqVeGmi_-AVw1da1OjhTbIb6UYUroXa31sexAHB8TL3w-h-C3UIF-AR7bhxCJughczwiLdZZvrs9rvuEAmVbCod0Xv8Nl1xkXFnmwOukgLvj_7YR8_juE_dehOGisCNINI6GYp3xt9g9p-_DcTYEJAawVX5FWx9AyvKDXTPAbNHzg7RDUutJ0e2UKsHWShA4uigTOr39GpdBsv0sx9nlxSFH9MCrExQY1B9R4wtdNv1_eBVBYTKW8ztdeOLIq6uJSSaY_ebZ6CRLLmNdEnzcu6QLZD-BUpk3EH3lLlH0gAGVl2QBPqgFjHugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز دوشنبه ۹ شهریور ۱۴۰۵، شماری از شهروندان جویای کار در شهرستان گچساران در اعتراض به روند استخدام نیرو در پالایشگاه لیشتر تجمع کردند.
در ویدیوی منتشرشده از این تجمع، تیراندازی نیروهای انتظامی برای متفرق‌کردن معترضان دیده می‌شود. برخی گزارش‌ها نیز از زخمی‌شدن یک نفر در جریان این تیراندازی حکایت دارد.
این تجمع در اعتراض به نحوه جذب و استخدام نیرو در پالایشگاه لیشتر برگزار شده است؛ پالایشگاهی که به‌تازگی افتتاح شده است.
@
VahidHeadline
نیروهای امنیتی و پلیس، جوانان عرب معترض به بیکاری در مقابل شرکت نیشکر «دعبل خزاعی» در اهواز را با ضرب‌وشتم و تیراندازی متفرق کرده‌اند.
در این ویدیو، مردی که در حال فیلم‌برداری است می‌گوید: «این جوانان همه گرسنه هستند، هیچ‌کس ما را استخدام نمی‌کند. هیچ‌کس برای ما ارزش نمی‌گذارد. هر کدام از آن‌ها با اسلحه کلاشینکوف به‌دنبال جوانان افتادند. ما کار می‌خواهیم. جوانان گرسنه هستند. ما هیچ آهی در بساط نداریم. ما کار می‌خواهیم.»
سازمان حقوق‌بشر «کارون» روز دوشنبه نهم‌شهریور۱۴۰۵ در گزارشی نوشته است که «جوانان و خانواده‌های معترض که به نمایندگی از ساکنان همجوار این شرکت دست به تجمع زده بودند، با طرح مطالبات خود اعلام کرده‌اند که شرکت نیشکر دعبل خزاعی در زمینی به مساحت حدود ۱۲ هزار هکتار فعالیت می‌کند که بخش قابل‌توجهی از این اراضی متعلق به منطقه و مردم بومی آن است. با این وجود و علی‌رغم حضور جوانان بومی دارای مدارک تحصیلی و تخصص‌های مختلف، مدیریت شرکت اولویت را به جذب نیروهای غیربومی داده و باعث شده تا جوانان منطقه همچنان از فرصت‌های اولیه اشتغال محروم بمانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78114" target="_blank">📅 19:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fz57RryXmwnV8bKXq6kKAXWP_xzZ5BAwht_TqfbO4QGcMPyRPCwkulOrV6Ale-2bnxAq3Oxh7kcFvqTEAwmwsBuB1mlwaYGYiMHrxrr_Kf8Wu1wYIi-cuAISzqqcfdl_yLQX73GI0tB247b6hXHNZ2WTy--ZD7fsIVxEietisCv4j9qn93rfMx2xePaAeYArI2C6ZSzuWPz0moHJze-ZXPuEo_dPQNgBOLLGb26-sIQiKNRxJ9ockmPSgPSnwCEXlqGVtuP-ye9KcyWImS5UonE9sqBZCo0rwUrkYomtrBYM3XUe_18tGr5_F6Pi9Kiw3GugCBIupY8psqhLwbeDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAdOGKhGvBlz9Wi3M6iF5BOD5DdPnZ9He6NQO3fe2d7OkYMBvq7hDfXsVRORS_N7R2sNTI-3fi2w-yzP7xXYvGk75uo32Y0IsQ97tX5Jjfo1ESytsBrEi1pYzcThjGYcnO4PB-44cPT-gK6Vmv2-8GYFAMx0SP3-xdKpiqUnkkBGzgAwcFZ1tXz4wQYT4Y8SqUKr6Zb4SjXAlOr67yjCJl_E0NHUrh2foFHaETXyw2wBuXMed1XJAfD65aFKXXnUiYqzlxzYuRyDz2VoVF8Qc3YzIh-5XFRayQJFuL0ZuDxD64h_eqfM_aRE1o6ghoAa1Dp7nwZkkdrc3hSIsck6bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اژه‌ای معترضان را به برخورد قاطع‌تر تهدید کرد
در پی تشدید بحران اقتصادی و رسیدن دلار آمریکا به مرز ۲۱۰ هزار تومان، رئیس قوه قضائیه جمهوری اسلامی گفت این نهاد برای مجازات «عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است».
این تهدید پس از آن صورت گرفته است که دستگاه‌های حکومتی بروز اعتراضات مردمی را پیش‌بینی کردند.
غلامحسین محسنی اژه‌ای افزود تحکیم امنیت و مقابله قاطع با عناصر ضدامنیتی از مقولاتی است که مردم و مسئولان درباره آن اتفاق‌نظر دارند.
این رویکرد با پیام مکتوب مجتبی خامنه‌ای در هفته دولت تشدید شده است.
خامنه‌ای در این پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با انتشار گزارشی به حضور «شماری از دانشجویان زن بدون حجاب اجباری» در جلسه رییس سازمان امور دانشجویان و مشاور وزیر علوم اعتراض کرد و خواستار «واکنش قاطع و فوری» وزارت علوم و واکنش نهادهای امنیتی و دستگاه‌های قضایی شد.
به نوشته فارس، انتشار تصاویر جلسه‌ای با حضور رییس سازمان امور دانشجویان، مشاور وزیر علوم و شماری از اعضای شوراهای صنفی دانشگاه‌ها که در آن تعدادی از دانشجویان زن بدون حجاب اجباری حضور داشتند، «با اعتراض گروهی از استادان و دانشجویان» مواجه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78112" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78111">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMQ9xxptg-krVOZJMZ3e5XZnGBoAUHfrIjzFCcfekkiFcNgRPMskHn4o1Jh30GPLDIghyfInK2_NrEIb5X0DYUhm0e-AxDPHz0qh2Nhm0Onncvry76dNYF7yU9Y2OAazhce4z1ThssWLqtDoFyd6_Yo-TRxqVMghT45CH_dEr-WQxGfk-gIRIj0Q2eXFTj-TMa_Kz8loxYK-kzPVFr_xYsZUGzluD0zice4s8aQnNo3J4ZO7wQG04RJp5BWaAw4sPcax99KzDVZkSmewi1pEMgQxLDdFSCyir-tR2FoH4l4K448LDISjyKfm7IL-hrvxBQU32dcFEzftOSZQmTPEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا روز دوشنبه اعلام کرد که به همکاری با ایالات متحده و سایر شرکای بین‌المللی و گروه هفت «برای حفظ فشار بر ایران و کمک به کاهش تنش و ثبات منطقه‌ای» ادامه خواهد داد.
در این بیانیه آمده است:‌ «اتحادیه اروپا از تلاش‌ها برای اطمینان از اینکه ایران فعالیت‌های بی‌ثبات‌کننده خود را متوقف کند و با حسن نیت در مذاکرات صلح شرکت کند، از جمله از طریق فشار اقتصادی بیشتر، شامل عملیات طرد اقتصادی به رهبری ایالات متحده، استقبال می‌کند.»
«عملیات طرد اقتصادی» عنوانی است که مقام‌های دولت آمریکا بر برنامه فشار اقتصادی تازه بر جمهوری اسلامی گذاشته‌اند.
بیانیه اتحادیه اروپا در آستانه آغاز نشست گروه ۲۰ به میزبانی آمریکا صادر شده است.
اسکات بسنت، وزیر خزانه‌داری آمریکا به خبرگزاری رویترز گفته است در این نشست از وزیران دارایی و روسای بانک‌های مرکزی کشورهای جهان خواهد خواست تا روابط اقتصادی‌شان را با ایران قطع کنند؛ در غیر این صورت با تحریم‌های ثانویه آمریکا روبه‌رو خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78111" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aGNPdPyDg56u_BSEFa53lbafjT6v-6s4Z_4Kr1yEyIIMSL8g-nDO4W8jTFRgw-lGuv1ZPEqfZi9BiPLRawlR6rn9GucN1KTdEG0twka6fh2mXQK6b-wOl8Klsi9KXCvs7qepEbYDAUbHGwwbbaDY4PJNEuH2UsCQLL1_nOzdaHm9d62DNTezEs7BglZJ0YwGIrSDJXvHtjF9Ly2SYjaxyktIGgxtcgzElRASgr3fwE86FBFcHFnmJhS9aAix5awmGs4EYixsxJP-QaStRabXIqxhkUNNw5k2lMQIe9lLWYrUcn-B35rj2CydDO1cHo5oc6Si077FfnrnNgaVyDVqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روند نزولی ارزش پول ملی در ایران، قیمت دلار آمریکا دوشنبه، نهم شهریور از ۲۱۰ هزار تومان عبور کرد.
همزمان پوند بریتانیا از ۲۸۴ هزار تومان عبور کرد و یورو نیز به مرز ۲۴۳ هزار تومان رسید. قیمت هر سکه طلای طرح جدید، موسوم به «امامی» نیز از ۲۲۳ میلیون تومان فراتر رفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/78110" target="_blank">📅 17:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RopQvgpszTN0m_MqOAHqNo2HFN3muAneokMxjmr8WOHJ_mwaHC494DNHkYZvz2pMQAFPAE_BA-iqt3qOke5P6La3Wnr0AE4fcTYUb4pgyzGizP0RqNdNMMXJROiYb__AWrzQS6aT9ZiB0QwJV3KRQEz10AnuGo63_o9W2B7dhrXsbeeU2fpcwR-uOLmG9z5cgr46rdODTC1KnGfIaABgnJczrGuT4rM38x7sUQFdoQ8wRjemiWslbOnS3_Wopx6td9iOVBgM5Gcx0ayOqe0pOkIfPvZ7S2TD04itDXpORxctMERvHAmhWA5JE4C-zMrzq-YUHuUmHlhcliWUCjpJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران (IRGC) ادعا می‌کند که یک ابرنفتکش هنگام عبور از مسیر جنوبی تنگه هرمز با دو مین برخورد کرده و کاملاً متوقف شده است. این ادعا
نادرست است.
✅
واقعیت:
هیچ کشتی‌ای در تنگه هرمز با مین برخورد نکرده است. این نیز یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه از طریق انتشار اطلاعات نادرست است.
CENTCOM
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78109" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/78108" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GeYHtaJNKtexQm8-IzqoC920MQ7aYbAAOPcBb-bdJYR6yOHo0xpuO8IFknejdgKTfcBWB_awavdKgspb37wS-wYdVzU-2x8DZRyFQJnQuChk8SwjrIWwUWK6WRiZJy7vzmS-Phqu2J1RPl1daUxHqIL0uxlgrAvwut5waU6s_PA08cP_ghQPEJedYsUqioWdlJrKyjvVRB02S7HtPuUFxc7ZSFUkxqzleDJukNFJrlYOxhxkCTxc_VlD2O1MpeRx-MIf-RLZNNOcC2jVJIFRnAGidZcHBAH-eoPliLstZudOv7hIKZc4vjRF3ZH6Yxa3SLUfCk70i8iqhypAa1ffUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه نهم شهریور، در شبکه اجتماعی «تروث سوشال»، جمهوری اسلامی ایران را رسما یک «کشور شکست‌خورده» خواند و خواستار محاکمه بین‌المللی رهبران آن شد.
ترامپ وضعیت ساختارهای اقتصادی و نظامی ایران را «فروپاشی کامل» توصیف کرد و نوشت: «ایران دیگر نه نیروی دریایی دارد و نه نیروی هوایی؛ ارز آن‌ها از دست رفته، حقوق سربازان و نیروهای پلیس پرداخت نمی‌شود و تورم به ۳۰۰ درصد رسیده است. رهبری آن‌ها در آشفتگی مطلق است و توانایی اداره کشور را ندارد.»
رئیس‌جمهوری آمریکا در ادامه با متهم کردن تهران به سرکوب خونین اعتراضات داخلی افزود: «تنها کاری که آن‌ها بلدند کشتار معترضان خود است که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است. مقامات تهران باید به اتهام ارتکاب جنایات جنگی علیه بشریت محاکمه شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78107" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHH7xKG3rswnsnmqEUHHIky9vvw1ByPVP-DgCNEkCLGqueCgj5uTbZjj25_4I-qJOXjxpAMz6gTNsinnAU4zmAL8uMEk6U8IUR7MWgFMiG-Oziffmoomo1rp-bZabskNJVDFaCS6FRNINLrb6t7MjkhcAAepL1QasuGPoHQwC6akKZJAK4tKAdaNxFQYXIzRIcfjRH9uuFkKWNy0E6zi_Y7JO8S7mLN9W0B0YWk83xnqkFYfBYVtXDgb6vAOo4g2RlAm8c6C4TmZLP5tDiOfZAu1SD4tMRMtRvaibtFLOqHprBQ5iaEwoTmZyZ-4C5s0j_ZCokML_Ynv9DIibeJjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی:
نتانیاهو در عبری آشکارا پُز می‌دهد که دولت آمریکا را فریب داده و به جنگ با ایران، به نیابت از اسرائیل، کشانده است.
نتانیاهو صراحتاً با خنده می‌گوید که چگونه با ۱۰۰۰ ساعت حضور در شبکه‌های تلویزیونی آمریکا، بر آمریکا «تأثیر گذاشته» است.
اما به انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78106" target="_blank">📅 16:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=XjfkmK4A3GTXX0IuzHB2dTUcUuax_9GzTC7_FqldymgUnmNbpx4pKNnKQ9PQDarPXRvqQXkAGjjKjGw4lG0Mtxh8051tGkZljthy6ji_h0akdNNMBt0_4KhKxxaLycobdy0aGVPbRkkeRSFVz7waamqJ7EviBEfKN81MxCB6qrBCJxbmpZAHOYRW6o1McTiGVNVmhQrl9Lu9p-WLfUUKBBxW4lEKcWprPTOiIhOO14CT_UcZI6ZcEjwsdeqZ6On26S5Hcz8Ke8CYIUiC5tUUpfjmzuHNbrq1acZdluENBZ6KBT7QjJEbG6EddtGau6oZl_1BpL2MeEYqOYIXkZn4lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=XjfkmK4A3GTXX0IuzHB2dTUcUuax_9GzTC7_FqldymgUnmNbpx4pKNnKQ9PQDarPXRvqQXkAGjjKjGw4lG0Mtxh8051tGkZljthy6ji_h0akdNNMBt0_4KhKxxaLycobdy0aGVPbRkkeRSFVz7waamqJ7EviBEfKN81MxCB6qrBCJxbmpZAHOYRW6o1McTiGVNVmhQrl9Lu9p-WLfUUKBBxW4lEKcWprPTOiIhOO14CT_UcZI6ZcEjwsdeqZ6On26S5Hcz8Ke8CYIUiC5tUUpfjmzuHNbrq1acZdluENBZ6KBT7QjJEbG6EddtGau6oZl_1BpL2MeEYqOYIXkZn4lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، عربستان و پاکستان همراه با فرماندهان نظامی سه کشور روز یکشنبه نهم شهریور در استانبول اولین نشست پیمان دفاعی خود موسوم به پیمان مکه را برگزار کردند.
عربستان سعودی، پاکستان و ترکیه روز جمعه ۱۶ مرداد این توافق را در شهر مکه امضا کردند.
بر اساس بیانیه سه کشور، حمله مسلحانه به هر یک از آنها به‌منزله حمله به همه اعضا تلقی خواهد شد؛ اصلی که شباهت آشکاری با ماده ۵ پیمان آتلانتیک شمالی، ناتو، دارد.
هاکان فیدان روز شنبه ۱۷ مرداد در گفت‌وگو با خبرگزاری دولتی آناتولی توضیح داد که ائتلاف جدید علیه ایران یا هیچ کشور دیگری شکل نگرفته و هدف از آن، ارائه یک تعهد کلی برای حمایت از امنیت سه کشور عضو است.
روز یکشنبه گزارش‌هایی از احتمال پیوستن هفت کشور عربی دیگر به این پیمان منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78105" target="_blank">📅 16:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/suy5UADZyRLOV6lTyuSUiDYX2s5CbXDUcmJ4tuOOw7Q5PpYK-iF4E0ApKS0dLm6zVvoET23FKTtk7HwmtQ1Rv4rmd76jTZlHG9lrRyALA81HNmFhW_6PiEwEKLnjuivOpyyQglmMp2HT_WPHSm9a57FsWrHhYMGuqMLbIiNM4Iej7KSAGg9grymkF0FgxX3x7g_Gmt-CdZ8zhc5GzTbhY1dJzbByOrtVxoO6-0mLs2KvL_5JvL5nZ044Sd3oKXL5ORFybGwBbf-OsqtrTr-tZ0FNLsw-3w5F84T9Gdzo8tLYOoyWlqZbS_wyw-pBLusGBpfRBsczSOOHA_snHCJHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C9zLvQL9xNFPwrgkzH79siIpms9lTkOX4rcz4SJvDVY-eXqeL2pviKpDXUAYSXj2P_7_ffyYD4sRvh89oCxkl-eowdcX0BC6S4wA4Rt8e2402JlcLgOTVT19Mbz6yQhcjbtyku4kvAHfhkUtuAhN1a0xYfMSQtTdjHoqi3PgoFSr7lL8JoIUcjgnRJTzKvW5-p-FvjDONVf-IFdtnC-VJZL8K8H-RBhNoLjOGcCND9QFxefB-O9TJaKsfvXnx2zYhGjMOsTRCTEUGGeLDZhUKKfkqJAXsuCt0_szmCGrT4LNR5WUk4z6ryNJ8DPlvxz2b3WZVs0aASgAJgthd4eFQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دفاع امارات متحده عربی پیش از ظهر دوشنبه ۹ شهریورماه با صدور بیانیه‌ای گزارش‌ رسانه‌ها مبنی بر هدف قرار گرفتن پایگاه هوایی المنهاد با «موشک» را تکذیب کرد.
ارتش جمهوری اسلامی ایران ساعاتی پیش از حمله «پهپادی» به این پایگاه آمریکا در خاک امارات خبر داده بود.
در بیانیه وزارت دفاع امارات آمده است: «نیروهای مسلح همچنان در آمادگی بالایی برای پاسخ به هرگونه تهدید احتمالی هستند، به گونه‌ای که حاکمیت، امنیت و ثبات امارات متحده عربی را حفظ کند.»
@
VahidOOnLine
پیش‌تر:
روابط عمومی ارتش با انتشار ویدیویی از شلیک پهپادها نوشت که در پاسخ به کشته شدن جمعی از نیروهای سپاه و غیرنظامیان در جریان حمله نیمه‌شب آمریکا به جزیره لارک،  «محل های استقرار بالگردها و نیروهای» در پایگاه المنهاد امارات «با شلیک دهها پهپاد انهدامی، هدف قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78103" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEcHO8CJKpp5SyyRY2vQXNggiid_hjsHHcLbrHslKEoXKRfps6DMJ98oh8HahcnppTKfgoAE-6f1P7RiSxrBsZ8rFHZjDY-P4RiDg_p6-UcwjNkukKg21V5V7jp6DCwG3Z62RXrMqLOaUNCVCgaO6-VK6sxZf_mLLmmFZwQTjMp9v2XFEqMgrbNP2Dr0wb0qZpxs1YzaKftSV4DXJ2GQnvy0A8AE8h4ZBnEdjRjnhh9A8asvYnMfy_e-FOfDKbYNJkOkGdfbOaurp5zfkTqKvtSg_Xv3rTeWfR-ZJiUXRksIvq2P_8U6CwPYn74_cK1zPgFIkQAgzPI8pTFL7pNF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.
درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی صادر شده بود.»
این در حالی است که به گفته این وکیل دعاوی «هیچ‌گونه ارتباط سازمانی یا ارتباط دیگری، به هیچ نحو، میان موکل و هیچ‌یک از گروه‌های متخاصم وجود نداشته» و پیغمبری تنها در اعتراضات حضور داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78102" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SFvfmXGSlI4BBWxZiC7ys_sLyf2wRcvTSCkdo29eO7YJAor6Vxhak2PLzEON_xRESkwXHE7YRZXjuNjtrsJbgMrgY1d036VueCOo0UuBWURAKox_GICOrF_wINI4mfVfDMX1pHwIqh4E2hWNBwNflPk8L8oxO1z-9NVxsKT1O39fMtZIpkA7yJzExgjx5RAtfzB5P8wykT9k8c2ZocrYIM8C078rMxk1EFqpJ-Tg-vqZd2gsloEiDkl3iIuK6BiTTbw7DU7p9ofQHq3LgvhfHDkjMGsTjJvl8iIcC6fte1w_xZ7thMcW6D2CkMCHj97lSlkE7-GjQN6k6y0clmmLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز دوشنبه در بیانیه‌ای که از تلویزیون حکومتی در جمهوری اسلامی منتشر شد از برخورد یک نفتکش غول‌پیکر با دو مین دریایی در تنگه هرمز خبر داد و گفت این نفتکش آتش گرفته و کاملا متوقف شده است.
سپاه در بیانیه‌اش مدعی شد که این نفتکش قصد داشته «به طور غیرقانونی» از بخش جنوبی تنگه هرمز عبور کند.
در پی جنگ آمریکا و اسرائیل با ایران، سپاه مدعی است که عبور کشتی‌ها از بخش جنوبی تنگه هرمز یعنی نزدیک به سواحل عمان غیرقانونی است. این ادعای ایران با قوانین بین‌المللی همخوانی ندارد.
در بیانیه نیروی دریایی سپاه به نام نفتکش و خدمه و مالکیت آن و زمان وقوع حادثه برای آن اشاره‌ای نشده است.
این نهاد نظامی به سایر کشتی‌های نظامی هم هشدار داده است که در صورت پیروی نکردن از «مقررات امنیتی» تنگه هرمز، «سرنوشتی جز این نخواهند داشت.»
بیانیه سپاه پس از وقوع درگیری‌های نظامی تازه آمریکا و ایران منتشر شده است.
اما تنها گزارشی که از بروز سانحه برای یک کشتی در تنگه هرمز خبر می‌دهد مربوط به ساعت‌ها پیش از حمله آمریکا به لارک است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78101" target="_blank">📅 08:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=vwFpzSxMj2eJ1gDmtlXDnv6yjNpQd0kihNBW6REuw8TavQRFQuXMjBDqiwSi0miSrmH6Hh9oZFaXBsZRDu0yR0Wx3RddDyAl8HvCQjd8cGlXcJ4PFdaTC-RbvB7g-eyXC5JJDakOuD2yi2sgshUKuClOmFcwYDvexbL_TSdPKCeoasdW86UQR516-X02CxlRmq_M1eeJn9k8oR5HKphbrAYRBXTgJfYyXe0KiDGWeBWBTOW5Crgv56mXrdx4DimQeTxOhHagYBNiwdMNeD06EJHnZhHRA9QMkd6TQbU_n6OVVxC2YvIbio3lXZy8VKPNf5bcVCDtURD1LIHV5QUf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=vwFpzSxMj2eJ1gDmtlXDnv6yjNpQd0kihNBW6REuw8TavQRFQuXMjBDqiwSi0miSrmH6Hh9oZFaXBsZRDu0yR0Wx3RddDyAl8HvCQjd8cGlXcJ4PFdaTC-RbvB7g-eyXC5JJDakOuD2yi2sgshUKuClOmFcwYDvexbL_TSdPKCeoasdW86UQR516-X02CxlRmq_M1eeJn9k8oR5HKphbrAYRBXTgJfYyXe0KiDGWeBWBTOW5Crgv56mXrdx4DimQeTxOhHagYBNiwdMNeD06EJHnZhHRA9QMkd6TQbU_n6OVVxC2YvIbio3lXZy8VKPNf5bcVCDtURD1LIHV5QUf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا
ویدیو
ها
یی
ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.
ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»
این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78100" target="_blank">📅 08:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tB-ZXQW7T7NMaw-aL3pMzORWpRx-aDRi8WlJbeHXG9wQSrIQJqrNmP4uq7jALFAxl-fuVBauLODAcB05DlK86uxcrzJso0viZQAt-FJhP7OZnCrDQ09E0aHKVDUakt_xE2Ldn0eAr3UfkDCQVQymNG0pWLXmHz3t8L0wYtY_b_07pTw1olrtzSkZREktAX8qq2TfOCpfQJ0X8qhfVN80Ywz8ngtKAsWRYyO0R368FH2wQn1VNnMWKYTKE-WWBYYBu-KMJBgL2VzXqRWfNCuOdBwul6ZOh2qr361EbefEFfB2keDNuPnyUwclS-Qtwc0EpeVsbGplSyZXFgI-5QvpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین
تصویر دریافتی: اسکرین‌شاتی از وب‌سایت مرکز لرزه‌نگاری کشوری
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78099" target="_blank">📅 07:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لرزش زمین
بنا بر پیام‌های دریافتی از شرق تهران
سلام و درود همين الان زلزله اومد ٢/٣ ثانيه طول كشيد خونه لرزيد پنجره كوبيده شد من لواسان افجه ام ٧/٢٠ صبح
شرق تهران زلزله حس کردیم
تهرانپارس تهران زلزله شدید
چند ثانیه طول کشید
انقدر قابل حس بود ک من از خواب پریدم
زلزله تهران
یه تکون ناگهانی شدید
ادامه هم نداشت
داداش تهران همین الان لرزید
نمیدونم‌زلزله بود یا چیز دیگه
سمت جنوب غرب
تهران زلزله اومد شدیدهم بود ولی کوتاه.
زلزله اومد تهرانپارس لرزید
زلزله خیلی وحشتناک همین الان حکیمیه
سلامم تهرانپارس غربی لرزید
تهران چنددقیقه پیش زمین لرزید و زلزله اومد
زلزله بود؟؟؟
تهران زلزله
خواب بودم از خواب بیدار شدم، حداقل ۴ ریشتر بود
سلام. یه لرزش شدیدی سمت تهرانپارس تهران حس شد.
اقا وحید نارمک شرق تهران زلزله شد بد لرزید الان ساعت هفت پ بیست و سه دقیقه دوشنبه
سلام تهران علم و صنعت حیدر خانی همین الان زلزله
وحید زلزله شرق تهران کوتاه بود ولی سنگین
من سمت پارچینم
لرزش شدید
یا زلزله بود یا موج انفجار
سلام پردیس لرزید چند دقیقه پیش
شرق تهران ساعت ۷:۲۱ دوتا پس لرزه شدید اومد
سلام وحید جان دو دقیقه پیش به وقت تهران من رو زمین خواب بودم ..جوری زیرم لرزید که بیدار شدم مدتش کم بود و شدتش زیاد
آره وحید زلزله اومد سمت شرق تهران خیلی حس شده
سلام، فکر کنم حدود یکی دو ثانیه زلزله اومد تهران
من غربم :) اینکه گفتی شرق هم لرزیده مطمئنم کرد
تهران  الان  زلزله اومد  شدید و کوتاه بود
زمین لرزید الان
مرکز شهر تهران
من سبلان زندگی میکنم.. متوجه شدم
ماهم تو جنوب شرق مشیریه لرزیدیم
بحدی لرزش شدید بود ک ما تهرانپارس شرقی هستیم خواهرم تهرانپارس غربی
همه از خواب پریدن
لرزش شدید
شمال شرق تهران
همه رو از خواب بیدار کرد
شرق تهران.تهرانپارس
پحید اینقدر تکونه زیاد بود که از خواب پریدیم
حدودا ساعت ۷:۱۹ ۷:۲۰
ببین صدا نداشت ولی قشنگگگ خونه لرزید عین زلزله همه پریدیم
سلام من پاسدارانم از لرزیدن خونه از خواب بیدار شدم
لواسان قشنگ لرزید
سلام من جنوب تهرانم منطقه ۱۷ طبقه پنجم زندگی میکنم کاملا لرزش حس شد و تکون خورد
ما نارمکیم خونه ی ما یجور لرزید که من با وحشت از خواب پریدم
😭
سلام وحید شرق تهرانه چیه
من مهرآباد جنوبی سمت یافت آبادم
قشنگ خونه لرزید
تکون خورد
غرب تهرانم احساس شد
سلام ما دماوند هستیم لرزش احساس شد
من یوسف ابادم
ساعت ۷.۲۰ لحظاتی کوتاه زمین لرزید
تهرانپارس چند دقیقه پیش کوتاه لرزید
سلام صبح بخیر ، ۷:۲۰ دقیقه پردیس لرزید
نارمک هستیم در حد دو سه ثانیه زلزله حس شد ولی خیلی ضعیف بود
سلام وحید جان ، من ستارخان هستم و کاملا لرزش رو حس کردم فقط شرق نیست
وحید جان ما هم مرکز تهرانیم این زلزله رو حس کردیم ساعت ۷:۲۰ بود حدودا
سلام ۷:۲۲ سهروردی خونمون قشنگ لرزید یخچال تکون خورد ولی در حد یک ثانیه بود
تا مرکز شهرم ما لرزیدیم
خیلی کوتاه بود ولی بد لرزید
زمین‌لرزه_تهران‌پارس. شدت خیلی زیاد و کل خونه لرزید
سلام من سمت جنوب غربم خونه طوری لرزید که همه بیدار شدیم
سلام وحید جان سمت مشیریه هم لرزید ولی لرزش عجیبی بود شبیه زلزله های سابق نبود
وحید بد لرزید جوری که من همه رو بیدار کردم گفتم زلزله
اینجا نزدیک دانشگاه امام حسین
قشنگ شبیه موج انفجار بود یه تک لرزه
وای خیلی وحشتناک بود خیلی بدجور لرزید هنوز دستام داره میلرزه همه از خواب پریدیم ما شریعتی معلم هستیم
ما میدون شیخ بهایی هستیم
لرزش زمین اینجا هم حس شد
همه مون فهمیدیم در جا زمین لرزید
ساعت ٧:٢٠ صدای مهیب و لرزش زمین در پردیس شنیده. و احساس شد
مردم اومدن بیرون
سلام، من مرکز تهرانم و متوجه لرزش خفیف زمین شدم.
سلام شهرری خونه شدید لرزید ۷و۲۰ دیقه ۵دیقه پیش ما طبقه ۴م فهمیدیم
ما تهرانپارس هستیم دو تا تکان شدید مثل انفجار بود دومی خیلی شدید بود ، زلزله نبود چون لوسترهامون تکان نخورد
نمی‌دونم انفجار بود یا لرزش ولی ساعت ۷:۲۰ کامل سمت نارمک لرزید
جنت آباد هم لرزید و کوتاه بود
زمین لرزه شدید  شرق تهران   تختم  بد تکون  خورد
یک ثانیه بود ولی تکون خورد
منم رو زمین خواب بودم متوجه شدم ما مرزدارانیم
زمین کامل لرزید
سمت ظفرم
ولی لوستر تکون نمیخوره
سلام وحید جان شمال طهران هستیم اینجا هم زلزله رو حس کردیم ولی خیلی ضعیف تر از شرق طهران
سلام ساعت ۷:۲۶ دقیقه سمت میدان خراسون تهران زلزله حس کردیم به حدی بود که خواب بودیم از خواب پریدیم
نارمک خونه لرزید
انگار یه موج از زیرمون رد شد
حرکتش کاملا معلوم بود
من از رسالت (شرق تهران) یه چیزی ضربه ای خیلی شدید حس کردم شبیه زلزله نبود
منم لرزش رو حس کردم کوتاه بود ولی قوی بود
منم پیروزیم ساعتای ۷:۲۰ دیقه شدید لرزید
سلام خونه ما نیرو هوایی هست چند لحظه خیلی کوتاه لرزید ولی خیلی شدت تکان زیاد بود
ما نيرو هوايي هستيم از شدت زمين لرزه از خواب بيدار شدم
من هم لرزش رو حس کردم توی نارمک
دوتا لرزش بود شدتش زیاد بود ولی زمانش کم
فکر کردم از بالا مثلا همسایه محکم پریده روی زمین تا الان اومدم پیام ها رو دیدم
رودهن هم لرزید
سلام وحید من شرقم علم و صنعت
نمیدونم بگم زلزله بود چی بود
انگار بمب افتاد
خونه ما شرق تهرانه(حکیمیه) و حدود ۷:۱۵ برای سه ثانیه لرزید، نمیدونم زلزله بود یا چی ولی هیچ صدایی هم قبلش نیومد،
خواب بودم تختم عین گهواره شد بیدار شدم. اتوبان بابایی تهران
سلام اقا وحید زلرله ساعت ۷ و بیست دقیقه بومهن و لرزوند شدتش زیاد بود
من نارمکم، زلزله اومد، یه تکون شدید خورد قشنگ، از خواب بیدارم کرد
ساعت ۷:۲۰
سلام .تهران . نارمک شمالی. با زلزله از خواب بیدار شدم. تکون و صدای شدید داشت.
سلام زلزله شدید سمت نارمک میز کامل تکون خورد و لوازم لرزیدن از شدتش بیدار شدم
میرداماد هم حس کردم
به حدی که از خواب پریدم
هروی زلزله رو‌حس کردیم ....
و از خواب پریدیممم
۷:۱۹ صبح
پاسداران زلزله درحد تکون خوردن تختم از خواب پریدم/:
از شدت لرزش از خواب پریدم
خیلی عجیب بود
ساعت ۷:۱۵ ، نارمک هفت حوض
سلام وحید جان،حکیمیه از شدت زلزله از خواب پریدم هم خودم هم خانوادم!!
فرمانیه هم من کاملا متوجه شدم
ولی بیشتر از لرزه موج شدیدی داشت
سه تا موج پشت هم که قشنگ تو پنجره و دیوار پشت سرم احساسش کردم
ما پاسداران سمت حسین آباد هستیم
قشنگ خونه لرزید
پردیس حدود ساعت ۷،۲۱ لرزید
وحید جان افسریه جنوب شرق تهران لرزش زمین بود که از خواب پریدم
سلام ما شیان هستیم خیلی بد لرزید
به خانواده ام گفتن باور نکردن تا کانال شما رو چک کردم فهمید درست بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78098" target="_blank">📅 07:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✅
واقعیت: نیروهای آمریکایی اقدامی محدود و دقیق علیه نیروهای مین‌گذار سپاه پاسداران که تهدیدی قریب‌الوقوع در تنگه هرمز ایجاد کرده بودند، انجام دادند. در اصل، ایران این تهدید را ایجاد کرد و ارتش آمریکا برای حفاظت از دریانوردان غیرنظامی، کشتیرانی تجاری و جریان آزاد تجارت جهانی، آن را از میان برد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78097" target="_blank">📅 05:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oeJWbdK-EA0DIg4JSKMMtGjcSEztmKt7whGbtc2X98p7CGR_9nh4dU9Hs0c5Vm3A0OHHBMiC7RHSbV1he-PwMadJ2Y6XOVgZCoJK7zxXuaqJ0wrMjFgJDjflAuSGwmFG2Zes4OJ1xKNn-vKqVB3EfWjzi65rFj31xyeRn6FSCQAmvJt5J8jyLeiD8xJztpZmo1kKBaTBrrbfrVEjx6J9CKhXEH7A_TlheE4bfgmrj29EnW_xY1gGnr5Frm2dKsfhkVdz9lx4qJfVzSbWli-HKBNRTNTY9HCFegfkVDd-ac7NZ7nuazm6Zm8YmBeJAxEHSn1WRc-ChfeGAXY8bldvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lEY4owAppwokiZGblZwDHWfc8ZL1MuDg8alv_U-Geg-Y0v7ki2_TaMJ768eFe5u_670qvh4GkrzGcNTvlLz3GgMR9GhDM9PS4mXmjNIysLfzSGo7vaRZyTcv__PyQjK6KnCH21C11CXopq0oIdY6MyHPc2G4IZYvGQUNPKOWaG-__g2InSZuNUD9aK1f3-ukFp-pPkACJ8xjFSuWn85sPHGz--XcGJk8nOvwmT57sgIGgzCYtoXFcs_njSDGBOQAfT1k4dBUmk8CqN0RGxzBAh-oCFnydul8g--WOjwwj8I5FbWlKGyeolyXUD4XhtQPHlU7Gdu_o4KSU8QZ5_1Vow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در گفتگو با «فاکس نیوز» بار دیگر حکومت ایران را حامی شماره یک تروریسم در جهان معرفی کرد و گفت هیچ کس نمی‌خواهد آنها سلاح هسته‌ای داشته باشند، حتی مخالفان عملیات نظامی آمریکا در ایران.
ترامپ همچنین گفت که حکومت ایران به سختی خسارت دیده و رهبران و تجهیزات نظامی‌اش را از دست داده و او به دنبال یک امضا روی یک تکه کاغذ نیست.
ترامپ رهبران حکومت ایران را سرسخت و در عین حال «شیطان صفت» خواند و گفت آنها همین اخیرا ۵۲ هزار معترض را کشتند و همچنان در حال کشتن معترضان هستند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه یکشنبه ۸ شهریور گفت جمهوری اسلامی به سلاح هسته‌ای دست نخواهد یافت، و تاکید کرد برای پیروزی در نبرد با رژیم ایران لزوما به امضای توافق با آن نیاز ندارد.
پرزیدنت ترامپ در گفت‌وگو با فاکس نیوز گفت محاصره دریایی و فشارهای مالی آمریکا ضربات سنگینی به جمهوری اسلامی وارد کرده‌اند و این رژیم اکنون در حال فروپاشی است.
او افزود: «در زمان مناسب، یا ما پیروز می‌شویم یا آنها کاری خواهند کرد؛ اما من با صرفا پیروز شدن مشکلی ندارم. نیازی به امضا روی یک تکه کاغذ ندارم.»
رئیس جمهوری آمریکا رژیم ایران را «بزرگ‌ترین حامی دولتی تروریسم» خواند و گفت: «نمی‌توان اجازه داد آنها سلاح هسته‌ای داشته باشند، و سلاح هسته‌ای نخواهند داشت.»
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با «فاکس‌نیوز» با دفاع از اقدامات نظامی و سیاست‌های دولتش در قبال تهران گفت: «اگر من رئیس‌جمهور نشده بودم، اسرائیلی باقی نمانده بود و به احتمال زیاد اساسا خاورمیانه‌ای هم در کار نبود.»
ترامپ با تاکید بر اینکه حکومت ایران در صورت دستیابی به سلاح اتمی از آن استفاده می‌کرد، افزود: «کشورهایی که سال‌ها در موضع بی‌طرف قرار داشتند، با آغاز درگیری‌ها بلافاصله هدف قرار گرفتند. از عربستان سعودی و قطر گرفته تا امارات، بحرین و کویت هدف گرفته شدند و همه از این اقدام شگفت‌زده شدند. همین مسئله باعث شد ایران حمایت و موضع بی‌طرفی آنان را کاملا از دست بدهد.»
رئیس‌جمهوری آمریکا در ادامه با تاکید بر جلوگیری از پیشبرد اهداف هسته‌ای تهران تصریح کرد: «اگر آنها سلاح هسته‌ای داشتند حتما شلیک می‌کردند و پس از نابودی اسرائیل و خاورمیانه، هدف بعدی ما یا اروپا بودیم. شما نمی‌توانید اجازه دهید آن‌ها به سلاح هسته‌ای برسند و هرگز سلاح هسته‌ای نخواهند داشت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78095" target="_blank">📅 05:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZwFoGlfzRYpgSv469V8iGxL4z8UTCCPhloryISzBv7sCW06MS7wJcZmIfqVF6EWHawkPkAWosi3CvpiRKrQolRIEfl1RyPgwZEyDE8IAVZYnPoPq9Odf_m_nEd5pKaGGIlDeqfNcODN42tG03WMGq2b3IqqmHHfgETzhSXhuYg428_cFC6DPLGbo9KZRpPIZTUmPMNZMfCQmFclNHMH8aA6qBlb1X-GrqjIiG853NZ74ulI67N0BZYWFhY0HvAy4XWie9JRMzkJsBMGeLEqWMFh3mI1mmbhd8L58-dZJ1jLCdDDso-25JnYmo5LWZCXEgltUQ_1GTlLlQGJU6cOUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EvHFqwI-WFK0GmofHqK7fhuOE7SizBufVlwOV-h3_vZT13cRPRb6-9Wstc3PXCek5Drqx03OqM05qH7KizJW9Lj87ai7EMwSR5MZgK-nLtLJcwRVpG7kFS9QEyD0OWFdYbhxIow1SRH08i6AwsyEQIxpBHSdz14ZSjY4Qz6fgVUc-KJgwaUPiQh72_C70Tj7GAL8zY3qy_akDZtA8l_715QeWwOxIffbgFgHDn2_BTkVk0IDSPZRQp_040xX_TB2P0k3nV583nGkesuFLBGnCtvgC7EM2nGD5s4n7_5cRSL_Sd9-2BWgNjhVj8HFFPp7fkXOkX1XtSJouwsz2adiMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با گزارش خبرگزاری فارس، مبنی بر اینکه حملات پهپادی آمریکا به جزیره لارک از «مبدا اردن و با پشتیبانی پایگاه‌های این کشور» انجام شده بود، روابط عمومی سپاه پاسداران بامداد دوشنبه با انتشار بیانیه‌ای اعلام کرد: «نیروی هوافضا در پاسخ به حمله به جزیره لارک، در یک عملیات ترکیبی موشکی-پهپادی، زیرساخت‌های فنی، تعمیراتی و محل استقرار جنگنده‌ها در دو پایگاه هوایی ملک حسین و الازرق در اردن را با شلیک موشک‌های بالستیک هدف قرار داد.» در ادامه این بیانیه آمده است: «اقدامات نظامی، تضعیف‌کننده کنترل بر تنگه هرمز نخواهد بود و هرگونه شلیک با پاسخ‌های متقابل جواب داده خواهد شد.»
@
VahidOOnLine
شبکه فاکس‌نیوز به نقل از یک منبع آمریکایی گزارش داد در پی حملات نیروهای ایالات متحده به پرتابگرهای موشکی در جزیره لارک، سپاه پاسداران مواضع نیروهای آمریکایی در اردن را هدف حملات موشکی قرار داد.
به گفته این منبع مطلع، تاکنون هیچ‌گونه خسارت قابل‌توجهی گزارش نشده و سامانه‌های پدافندی موفق شده‌اند تقریبا تمام موشک‌های شلیک‌شده را پیش از اصابت به اهداف رهگیری و منهدم کنند.
پیش از این سپاه با انتشار بیانیه‌ای از هدف قرار دادن دو پایگاه هوایی «ملک حسین» و «الازرق» در اردن خبر داد.
@
VahidOOnLine
رویترز گزارش داد قیمت نفت بیش از دو درصد افزایش یافت و بهای نفت برنت بار دیگر از ۹۰ دلار در هر بشکه فراتر رفت.
این افزایش پس از حمله نیروهای آمریکایی به دو پرتابگر متعلق به سپاه پاسداران در جزیره لارک رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78093" target="_blank">📅 03:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پرتاب موشک از خرم‌آباد
طی ساعت گذشت پیام‌های پراکنده مختلفی دریافت می‌کردم.
ولی در این لحظه یهو کلی پیام از خرم‌آباد اومد درباره دو صدا که خیلی‌ها نوشتند مربوط به پرتاب موشک بوده ولی بعضی‌ها هم تاکید دارند که بیشتر شبیه انفجارهای برخورد یا شکست پرتاب بوده.
هم‌زمان پیام‌های مشابهی از کنگاور در کرمانشاه دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78092" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dwIqd1a9jFGM1nmrPC8hi9IDexHX37y_q2Dzt9gv0B4ixW9wUI1HvKyXP6tgNgpPdl1N17JrmenqfbvsERgG9FwvrlTZXAL6lD2W5ID_2Z0CQX9ObuRJ6LG1jdlyYAyivtiC-UtwJnnz2dcwMJWWAS-WSJ2gAZBIlA05VN6KaesLwBtOMDhWOhz-5Wu0QRXHzDkUb2_FoJ-x-yFuVRJaMcn1Ca7T5ScWI60NqNlJoIjIFbyJ4azxJRahOWE2qD8laMSZ041lm6C4fsvucoBTpngdSz2se0OZ16pKhcIq2OqV747GdMPN0ZzBf3xrxnbHJSemNvcvtuIU51orpEloHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه با تایید کشته‌شدن شماری از نیروهایش در حمله آمریکا به لارک: پاسخ خواهیم داد
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
🔹
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.
پیش‌تر یک مقام آمریکایی اعلام کرده بود که دو پرتابگر سپاه پاسداران که آماده شلیک به کشتی‌ها بودند در جزیره لارک هدف قرار گرفتند: @
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/78091" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/78089" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mkhWHuGw49ArfDcphiaDXxGzzWl4KSG6X7SK3tGGlSoMNn1PF4x7N5yqkKZRg2t99vqPBLMszwCZxGWJIdvgNJ-LiGfwc4bBq0iYYNzeH6uNUFr6HGhpJnu7E8AAXuT3zT-BpTG1rChbQSSwYtuPKRkaxK6uLdIIaX7k_RTxvQB3_r8VlKszhh_FEWniSpmm9G0mXlJ36BYT3RtugR3OprT6Cchhq4Dd1tE8i9n0wKbUbZMxYSIrEnXOgarWW5vw-nh3ReRXcOrmamXIkMGbRnx_jbfxcu4vonh-07WlwmCfcpd-Ajc0aNreR0qsUboB762r9y6WSYC9NdRyPgiERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
یکی از کارهایی که قرار است با نفت ونزوئلا انجام دهم، پر کردن ذخایر راهبردی ملی است؛ ذخایری که به‌خاطر جو بایدنِ خواب‌آلود عملاً خالی شده‌اند. روند «پر کردن تا ظرفیت کامل» به‌زودی آغاز خواهد شد و این هدیه‌ای از سوی ونزوئلا به مردم ایالات متحده است. متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/78088" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jmtJX7mWxWGF5a8lpHg0KEuv-fPPKs-31EkVY5OOjdT1Bc7eLTCkOfi4RubWmpLbvFIKrw0T8KuYFaSKdswcn5qI8FpPnIAnDT7Fu6ierQr5eLmRKTrJ0nLJddP0ZiawvIbiBD4sFXYw8gUSxjo8NxExaL6UytIcPlFNVcmULEyn76rPBFzoI28i4A0Rj2Kosy7hZybQomEktJzw4NSPNwmzLevKa0stW-yBglbUvyM8Qx-xA8QZSKHgOVhHSmB-mus68ftforSqew8XkTk9_7WjTINtcvXALGpw7WzLZ0oFsG1bpuK6TEta3pKF6CACssdoXVW8f87jN1AvacWHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن‌پست به نقل از افراد آگاه گزارش داد چند مقام ارشد نظامی آمریکا به پیت هگست، وزیر جنگ آمریکا، هشدار داده‌اند که ادامه عملیات نظامی گسترده علیه جمهوری اسلامی پایدار نیست و توان ارتش آمریکا را برای مقابله با تهدیدهای دیگر، از جمله دفاع از خاک آمریکا، تضعیف می‌کند.
به گفته این افراد، این هشدارها که روسای ارتش، نیروی دریایی و نیروی هوایی آمریکا، همراه با فرماندهان چهارستاره مسئول عملیات نظامی آمریکا در اروپا، آسیا و آمریکای لاتین، در نسخه ۲۳ مرداد «کتاب دستورات وزیر جنگ» به هگست ارائه کرده‌اند، بخشی از یک سند محرمانه است.
بر اساس این گزارش، با توجه به تاکید ترامپ بر اینکه گزینه نظامی همچنان روی میز است، ستاد فرماندهی مرکزی آمریکا (سنتکام)، که مسئول اداره جنگ با جمهوری اسلامی است، ماه‌هاست بیش از ۵۰ هزار نیرو را در حالت آماده‌باش نگه داشته تا در صورت صدور دستور حملات بیشتر از سوی رییس‌جمهوری وارد عمل شوند.
به گفته افراد آگاه، نسخه ۲۳ مرداد کتاب دستورات وزیر جنگ مقرر کرده است که بخشی از نیروهای مستقر در خاورمیانه تا پایان سپتامبر در منطقه باقی بمانند و ماموریت برخی دیگر تا سال ۲۰۲۷ تمدید شود. احتمال تمدید بیشتر این استقرارها باعث شد فرماندهان نظامی نگرانی‌های خود را آشکارا مطرح کنند.
به گفته این منابع، فرماندهان ارشد فرماندهی اروپا، فرماندهی اقیانوس آرام و فرماندهی جنوبی آمریکا، همراه با فرمانده ارشد نیروی دریایی، در این سند نظر «عدم موافقت» ثبت کرده‌اند؛ به این معنا که با دستور وزیر جنگ برای تمدید استقرار نیروهایشان موافق نیستند، اما آن را اجرا خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78087" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syBFukOQbjliKXtoC7c7DbsIak6163PTKY5_ug5GOk9FtVszoa_1hAEVQ54AT_THhYaENItPDI1asb2fVAC8-2LGtDb0FT532MGeAQzpzZOlRSc9Y7bFPym4t9fHmyXvHvhGxUXxS9IBg6QG93Nu3VbP4WfLofkdhmdQCnXCYXndpWW4hTTO7H2ezoXtqrmwJRXCHf-8ilEeBEE5l8nVLKCdcUJqoYhffGlqZVEWphHzd7ixoJKS0zOuJKtI1YfMIv79rkrbYkQT18it3HoQSBQWSK0z2IDxh1mrLdKUz9AZD30k799Amr_YoOUtGmdCSp2l2Afv_r9qV44JglXCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه اول دادگاه انقلاب اصفهان ۱۰ نفر از متهمان پرونده موسوم به «میدان شهدای اصفهان» را به اعدام محکوم کرده است. شش متهم دیگر این پرونده نیز احکام سنگین زندان گرفته‌اند.
کانال تلگرامی خبرنامه‌ها خبر داد این احکام در مرحله بدوی صادر شده‌اند: @
MahmoudianMehdi
«ترانه رحیمی»، «نوید الیاسی»، «ابوالفضل دادگستر»، «مهدی منصوری»، «احمدرضا سعیدی»، «مهرداد بو‌ئری»، «محمد مهدی اسدی»، «آرمین غلامی»، «پارسا جعفری» و «مهدی جعفری»، معروف به «مهدی خسروی»، ۱۰ متهمی هستند که حکم اعدام گرفته‌اند.
در بخش دیگری از حکم، «رومینا رحیمی» و «میلاد بو‌ئری» هرکدام به ۲۵ سال حبس و «حامد مهرعلیان» به ۱۵ سال زندان محکوم شده‌اند. «ستایش ساعدی»، «سجاد عابدی» و «علی بوئری» نیز هرکدام به پنج سال حبس محکوم شده‌اند.
دادگاه همچنین هر ۱۶ متهم را بابت اتهام «اجتماع و تبانی» به پنج سال، «تحریک» به پنج سال و «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم کرده است.
پرونده «میدان شهدای اصفهان» در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ تشکیل شده است.
متهمان این پرونده از ۱۴ بهمن تا ۲۴ اسفند همان سال در خانه‌هایشان بازداشت شدند. شماری از آن‌ها کارکنان فروشگاه‌های کفش و پوشاک در محدوده خیابان شهدا یا از بستگان صاحبان این فروشگاه‌ها هستند.
بیشتر متهمان این پرونده کمتر از ۲۳ سال دارند. ترانه و رومینا رحیمی، خواهران دوقلو، هنگام بازداشت ۱۹ ساله بودند.
جلسات رسیدگی به اتهام‌های این افراد از ۲۲ تیر ۱۴۰۵ در شعبه اول دادگاه انقلاب اصفهان آغاز شد. اتهام‌های آن‌ها «محاربه»، «معاونت در محاربه»، «تخریب اموال عمومی در حکم محاربه»، «اجتماع و تبانی» و «تبلیغ علیه نظام» اعلام شده بود.
این پرونده پس از کشته‌شدن «عباس کامرانی»، عضو سپاه پاسداران، و یک شهروند بی‌خانمان در اعتراضات ۱۸ دی تشکیل شد. بااین‌حال، در کیفرخواست صادر شده علیه متهمان، اتهام قتل مطرح نشده است.
منابع مطلع پیش‌تر گفته بودند در جلسات دادگاه مدرکی که نقش متهمان در کشته‌شدن این دو نفر را اثبات کند، ارائه نشده‌ و اعترافات گرفته‌شده در دوران بازجویی، مبنای طرح اتهام‌ها قرار گرفته است.
شماری از متهمان در دادگاه گفته‌اند اعترافات آن‌ها با ضرب‌وشتم، استفاده از شوکر و تهدید به تعرض جنسی گرفته شده است. «احمدرضا سعیدی» نیز در حضور قضات اعلام کرده بود که در دوران بازجویی شکنجه شده است.
براساس اطلاعات منتشرشده، یکی از زنان متهم این پرونده نیز از تعرض در زمان بازداشت خبر داده و شکایتی ثبت کرده است. بااین‌حال، دادگاه بدون رسیدگی به این شکایت، حکم او را صادر کرده است.
وکلای متهمان نیز از دسترسی کامل به پرونده محروم بوده‌اند. گزارش‌ها حاکی است دادگاه اجازه نداده است هر متهم از شمار قانونی وکلای مدافع برخوردار باشد.
«محمدرضا توکلی» و «مرتضی براتی»، قضات این پرونده، پیش‌تر نیز در پرونده‌های سیاسی و امنیتی اصفهان حکم اعدام صادر کرده‌اند. توکلی از قضات پرونده‌های «میدان علیخانی» و «توماج صالحی» بوده و براتی نیز در پرونده «خانه اصفهان» برای سه معترض حکم اعدام صادر کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78086" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ljy5Y-ie-E0q8aHwC6XEaTmkMAepjQUR3ckyOhVLAWnEKPi7D82jkdIi2HRcNhVQphTxXWMsSM5xEyQEu89lRoFn1wpRgFUNtxHKtgaKKJA9cubknPYYwItxjMFLsJMoPOChs7i5fB5IIsc0qJ4VgkFvE1nceolZIwu4OWgHJBnit0CzL0q8azdly1dIdAQerivn4lNMecD2MoYg8K2rz6cTVi8kIADVc3G2YE5tcu4ccY0dR0TNwMK7Pbfa6bB3rrw78Z5boprB9UGmQ4USoralxneEyj7KpeUmZ23k1bNl3Sv7bPvtieJh79dQnhBf3mP8PhXLDQfcMGbcL-Y2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو اعلام کرد آزمون زبان این مؤسسه در ایران و برای دارندگان مدارک هویتی ایرانی در دسترس نیست. همزمان گزارش‌هایی از لغو آزمون تافل و عدم اعلام تاریخ‌های تازه برای برگزاری آن در ایران منتشر شده است.
این تحولات چند روز پس از تعلیق یکی از معافیت‌های تحریمی آمریکا در زمینهٔ خدمات آموزشی به ایرانیان رخ می‌دهد.
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک) روز دوم شهریور مجوز عمومی موسوم به «G» را که از سال ۲۰۱۴ برخی تبادلات دانشگاهی و ارائه خدمات آموزشی به ایرانیان را مجاز می‌کرد، برای مدت نامحدود به حالت تعلیق درآورد.
دولینگو، شرکت آمریکایی سازندهٔ اپلیکیشن آموزش زبان که آزمون آنلاین انگلیسی آن از سوی بسیاری از دانشگاه‌ها پذیرفته می‌شود، اکنون در صفحهٔ رسمی پشتیبانی خود اعلام کرده است که این آزمون در ایران و برای افرادی که از مدارک هویتی ایرانی استفاده می‌کنند، در دسترس نیست.
همزمان شماری از کاربران ایرانی در شبکه‌های اجتماعی تصاویری که به‌گفتهٔ آنان مربوط به از پیام‌های لغو آزمون تافل و نبود مرکز یا تاریخ آزمون در سامانه ثبت‌نام ETS (برگزارکنندهٔ آزمون تافل) است، منتشر کرده‌اند. رادیو فردا نمی‌تواند اصالت و منشأ این تصاویر را مستقلاً تأیید کند.
برخی داوطلبان نیز گفته‌اند آزمون‌های تافل تا همین روزهای اخیر در ایران برگزار می‌شده، اما پس از تصمیم تازه اوفک، پیام‌های لغو برای شماری از متقاضیان ارسال شده است.
تا زمان انتشار این گزارش، مؤسسهٔ برگزارکنندهٔ آزمون تافل اطلاعیه‌ای رسمی دربارهٔ توقف برگزاری این آزمون در ایران منتشر نکرده است.
در وب‌سایت این مؤسسه، ایران همچنان در فهرست کشورهای محل ارائهٔ آزمون اینترنتی تافل قرار دارد و اطلاعات تماس ویژهٔ متقاضیان ایرانی نیز در آن دیده می‌شود.
از این رو، هنوز مشخص نیست محدودیت‌های گزارش‌شده چه دامنه‌ای دارند و آیا مستقیماً ناشی از تصمیم اوفک هستند یا نه.
مجوز عمومی G که اوفک در مارس ۲۰۱۴ صادر کرد، از جمله به دانشگاه‌های معتبر آمریکایی اجازه می‌داد با دانشگاه‌های ایران برنامه‌های تبادل دانشگاهی داشته باشند و برخی خدمات آموزشی را به دانشجویان ایرانی ارائه کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78085" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0a8ieo2DlkYqmouKn8JrDMCrDerzupmYcjE87z3-JXDHnCPIXWLWDfzfSqzLFvrSetW3eNTNTC1NJ_PJfHOXYmynSWM5pbIPx2WWKDO7K1J8w5aWX2aKPtyotQfMuk6LERZYDUwTOIDO2OFhFcSuSwaSZ6-3KWPiAeABABvXZg7w6E-b2mDWV21lTmogyNWk3E3g_xGN987jB4pYkJ25O8MS2fxh3J0KYtc4drjIKOdpKjwGEB86yNU56cBT2Zr8Yz8ej-Mfyn1NYiDSjs6PxsDzFTCMYdVglQ1nNsYqpHx3W5wXSAy-x6VJM57ONroEFupgGyT72C-IL7WxiVGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آخرین نرخ‌های ثبت‌شده در بازار آزاد در روز شنبه ۶ شهریور ۱۴۰۵، قیمت دلار آمریکا به حدود ۲۰۵ هزار و ۸۸۰ تومان رسیده است.
نرخ دلار در بازار هرات نیز حدود ۲۰۵ هزار و ۲۳۰ تومان ثبت شده است.
داده‌های لحظه‌ای بازار همچنین قیمت دلار را در ادامه معاملات بالاتر از ۲۰۶ هزار تومان نشان می‌دهد.
در همین حال، هر یورو حدود ۲۳۸ هزار و ۹۱۰ تومان و هر پوند بریتانیا حدود ۲۷۹ هزار و ۹۰ تومان معامله می‌شود.
قیمت دلار کانادا نیز به حدود ۱۴۸ هزار و ۶۵۰ تومان رسیده است.
در بازار طلا نیز هر گرم طلای ۱۸ عیار بر اساس تصویر ثبت‌شده از بازار به حدود ۲۱ میلیون و ۸۱۰ هزار و ۷۹۰ تومان رسیده است.
قیمت هر مثقال طلای آب‌شده نیز حدود ۹۴ میلیون و ۴۸۰ هزار تومان گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78084" target="_blank">📅 19:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=ndS0Wb80xvd_jcXrKQ2BbqzhFty869JUgcvK2AWeNR9VHwz098pcL_ebNBm71Lml42mOkXLLvLRBYj7AcO1d7IBPKb5xq7LZWjoFrbtNipsIiHZZstbixeHxAjbwNgfKF28nkbgPcoqcLgC2k2fCr1pSNIs_ZTiDcRQDw5jMEQq4s5JtKT8_Na5rKEQbOLbcmLgOEj55MUGF_70SnK-nUcnhyUJqJjdvHN--tGi6j2hrG1aek8Ce24CzVoOlnqZWcqipT55uqXsySinqRHYsOHfumnb9JtSzQ6vk4JpeyZKHnYHCwg_wOsVvNcxkR7LBsp4aQvTJpSyepw6vuJ7WZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=ndS0Wb80xvd_jcXrKQ2BbqzhFty869JUgcvK2AWeNR9VHwz098pcL_ebNBm71Lml42mOkXLLvLRBYj7AcO1d7IBPKb5xq7LZWjoFrbtNipsIiHZZstbixeHxAjbwNgfKF28nkbgPcoqcLgC2k2fCr1pSNIs_ZTiDcRQDw5jMEQq4s5JtKT8_Na5rKEQbOLbcmLgOEj55MUGF_70SnK-nUcnhyUJqJjdvHN--tGi6j2hrG1aek8Ce24CzVoOlnqZWcqipT55uqXsySinqRHYsOHfumnb9JtSzQ6vk4JpeyZKHnYHCwg_wOsVvNcxkR7LBsp4aQvTJpSyepw6vuJ7WZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی:
"اعزام نیروهای مردمی به تنگه هرمز در پاسخ به یاوه‌گویی‌های ترامپ"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78083" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlZez2X1YWgMYKqzLpC-DzwnVj-tM0VIYbf86T2oVJ-ebyJVwWPrqljkvYebCD8EbBB20BFmJIyRZPOpD6ZUVXR4mmzPGYEHMHL6UN6IzaZVKPlnWNpZAiagLZ6WNcEEIy_2ins89KONKg_BJ9nxZthn5oQLEWZzNBWqAWBWCzXBTaSDfBnA0VsWKR3HSjKZD9_GCbLUbBdmQoXT9qUWuaxUuS-hjBrKEdLcQOtrVNtRJe8FlxVAPySQTiL8DWyf_VA0Wy9QmvPvwoetRjajxuk8Aydjt2iJbCUI5K2KcpVMmvVSXi6qwnQkQLThpVUSG81ReXSmFt2so4wXLTj2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از ابتدای سال ۲۰۲۶ تاکنون، بنیاد عبدالرحمن برومند ۹۵۰ مورد اعدام را در ایران مستند کرده است. دست‌کم ۲۰ زن و ۳۰ معترض در میان اعدام‌شدگان قرار دارند و تا این لحظه، ۴۵ مورد اعدام در ماه اوت به ثبت رسیده است.
🔸
در نظام قضایی جمهوری اسلامی که بر پایه روندهای ناعادلانه، عدم شفافیت و نفوذ انگیزه‌های سیاسی بنا شده و در آن اصول دادرسی عادلانه به‌طور سیستماتیک نقض می‌شود، استفاده از مجازات اعدام، بر اساس حقوق بین‌الملل، مصداق سلب خودسرانه حیات است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78082" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiEvAfYd8sVsQMA5nhC3DM5GRlJ5Z5ibUhMTdKS_GmggHqFPmcN_lfUmNLO0f_5nWMbrda5pPXTvQYurhr4BzD7cz43mABgFatvyX65-hBz0lFy1dnsnOuKnoEbyr9h4RD2hBv6xMi2_Al6T9msvPqgmr6Cyzo9ZeaEiDrzs32tZkcATmbIb1fHKfRHafrnLAx7mee1yBZnkfJ_-8UO54qoaxBx0QRGyOli0OD8HxBagUoGp9tU2hPfUM8QnS3M824iRQ2s6bj5M6j2dk9APRhda68utW7uet_3YIOlA6VsDW81vD5n4PACp9B9lCE9raKTU-Fj8Zt4hyhbGHjOCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StEAu1GYyF47OFcpkHn2aaKbXqdc_sKeg4Y4iCxiP5WQ_mp79asFwtWCRu0iL1llSrTKWvYeAB7S2IaCGzDBXv60YoyxfdzY5bYvt7YS6g3HkV_5lcdyGtRwA_nfLpYIIIdNaFOgS64iDrlMRcpcIX77fXPRPxIjT6DDpcjUpn1hu9AqGrTOAAb7nH_asUjzygVlpaCxax-1vGTrbRqTgaXcw4wZEZZ3geoLktIvmIWu5oV7NefC70J89xcLDc9IG6qHnZdPY2ELL8NlDN3KWUAHOvvqOPWYq5bVwYuNM2DaszENqaiZDN5GjPUygA-16O0iFHXfDqrnOS1-awmXjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در تروت سوشال اعلام کرد آمریکا با ونزوئلا به توافقی دست یافته که آن را «بزرگ‌ترین توافق نفتی در تاریخ جهان» خواند.
ترامپ گفت بر اساس این توافق و با مشارکت بخش خصوصی، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شده نفت ونزوئلا را بدون تحمیل هزینه به مالیات‌دهندگان آمریکایی در اختیار خواهد گرفت.
او افزود مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ آمریکا، با همکاری دلسی رودریگز، رییس‌جمهوری موقت ونزوئلا، در دستیابی به این توافق نقش داشته‌اند.
ترامپ گفت این توافق ذخایر نفت آمریکا را بیش از دو برابر می‌کند، عرضه نفت را به میزان قابل‌توجهی افزایش می‌دهد و در بلندمدت به کاهش قیمت بنزین برای آمریکایی‌ها کمک خواهد کرد.
@
VahidOOnLine
مارکو روبیو، وزیر امور خارجه ایالات متحده، روز جمعه با اشاره به توافق نفتی جدید میان واشنگتن و کاراکاس اعلام کرد که این توافق علاوه بر تضمین ذخایر پایدار و کاهش بهای بنزین در آمریکا، نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی را به ونزوئلا سرازیر خواهد کرد.
روبیو در اکس نوشت: «برای مردم ونزوئلا، این توافق نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی به همراه خواهد داشت، از هزاران شغل با دستمزد بالا حمایت می‌کند، و پیشران بازسازی اقتصاد ونزوئلا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78080" target="_blank">📅 04:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=lPmvuG2k3P5Ga7qSaVKgippoREoMo5pAioyxjakPcEHhfums5OTOXeFOoOK-HEmNIYgO8rNzVK2h6Oy9lG69qaxW3UdUn0e-P_Pu5Cpk2L3AeVT73uvvRgQL0fOdWdLGagcUMeBNopHFXfhCGONsVaHgWyxE399kA-QQ-tOCcK7pfF_vp-6gTtDGA-ArHQIiXbZAruivfvPsbPq3Rrmj_35zo5h3nlHpGqoQFs7lq-wLmFA8EQZqtAcICvHMWdGvCzJA9f7Yx91wKlK48-bylqZysHOJVbLzRtoUdCFkIfBgRm9MmRrjVU-SUBmHsJ62wlP_hcuRC4wUDFYUvSJAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=lPmvuG2k3P5Ga7qSaVKgippoREoMo5pAioyxjakPcEHhfums5OTOXeFOoOK-HEmNIYgO8rNzVK2h6Oy9lG69qaxW3UdUn0e-P_Pu5Cpk2L3AeVT73uvvRgQL0fOdWdLGagcUMeBNopHFXfhCGONsVaHgWyxE399kA-QQ-tOCcK7pfF_vp-6gTtDGA-ArHQIiXbZAruivfvPsbPq3Rrmj_35zo5h3nlHpGqoQFs7lq-wLmFA8EQZqtAcICvHMWdGvCzJA9f7Yx91wKlK48-bylqZysHOJVbLzRtoUdCFkIfBgRm9MmRrjVU-SUBmHsJ62wlP_hcuRC4wUDFYUvSJAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: نرخ سوم بنزین حدود ۱۰ هزار تومان خواهد شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78079" target="_blank">📅 22:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVBxHUAbM8ueDeCJtrDX1ozuyFwaQHgoPQ7cMVnS-nAXwQqQ6rKT8j4OI2dSnHfHcSiOfbLFpq3yBsoiD92PYfXOVenCoC73_TpIjHaEh2TdKo7rnRtkd4kaQXDKq2WbjH6HuhNv3QO7PTkBi68IJqU0B2V2LXbCpYbsfRayZBX4M5KJXNd9DumTm7fU7R2O-B6tDhedS-_1ZTowSmvU1A2Q5I7BZPjJrbT3HZvusgn6ZDm-bM0t62Tiz6xT9w3D5z-viWetDnhksPB2FR00FBOAMGdGyAmnWMrE-UF2lTLsQ2xkt90zBOCeBFPbHCwSKEOmUOZH6GHCGQz0Lu4vZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.  به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم…</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78078" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود که هر شریان اقتصادیِ باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید رژیم ایران پایان دهد.
همچنین هشدار دادیم که حامیان ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی برخوردار باشند.
بانک مصر امارات تصمیم گرفت این موضوع را به شیوه سخت بفهمد، و امروز نخستین گام را برای پاسخگو کردن آن به‌دلیل حمایت مستمر و فاحشش از رژیم ایران برمی‌داریم.
SecScottBessent
وزارت خزانه‌داری امریکا:
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)،  شبکه اجرای جرایم مالی (FinCEN) قاعده‌ای را پیشنهاد کرد که دسترسی بانک مصر امارات به خدمات بانکداری کارگزاریِ مؤسسات مالی آمریکا را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، را به همراه یک شرکت پوششی مستقر در هنگ‌کنگ که به پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی کمک کرده است، تحریم کرد.
«عملیات طرد اقتصادی» در حال قطع کردن آخرین شریان‌های مالی‌ای است که رژیم ایران را سرپا نگه می‌دارند.
USTreasury
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78077" target="_blank">📅 18:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78075">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ientRbNEXqFPtr2z51qAJkcD1Q_1s2tUCpu1LtLQBCclSMdBpvTXtJkmAeZTiHt0GwsdqNR47W8YEoFtfhxPgkIwpCORr9uRGH0p4x736oE6kGtk89PriQSzVTZwrwFAwLKU8avlBTKctxwPy-2_-clL72ZNSGrWgTUg_HzD-AiZds-o_yIF48HjA4MyvNQw9hkcOU0xqxAzB2BV4rMbk-glcfGHSAvwk7xZH8esqlAhuWZ7j_kEePNQPG4n8yi6oE310KlRUvsbxT8w-xrk6XO2YEI9WeaNraT0xwewh9XiZIqtabSE2k2q8r51k2mg5u5BCJHtaV-v_qUbhlGM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا نوری، امام جمعه بجنورد، در خطبه‌های نماز جمعه این شهر گفت: فشار اقتصادی کمر خود آمریکا را هم دارد می‌شکند و با فشارهای مردم در آمریکا بر علیه خود ترامپ، او که رای اول را در آمریکا داشت امروز محبوبیتش به زیر ۳۰ درصد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78075" target="_blank">📅 16:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tqRfdLPRF7Vw67EB4R-dWSi3mHkuO0HCSEe3E4g-dSpvLt5WkTWGVmHs6lhbDXdAXGEntfx_5JBCl10DrcWtLreFJx5clyHMpR_e3hKpTkdcZHO8fgIKlMjSWzJ13Xw1_RAuVuj69Npc7_jJ9Qb-V6KeI2cSu5R65y-PiXMJiqFCxnaXsz4hB52Dugod6fSklnEp1d-CkCaGdN6i3x6ZP7GUG7FRIqThI33XqDiF6SNBKz3Vym1dxrWm0fIRoNVhQVhgrfFyH9Hgho-kGx3XocOD90ShwxXTJXIgX5HSYpjqVwybzL5S39mc0eKmHo0ZNopHj-jWmePmQTekF7kDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در واکنش به دور تازه فشارهای اقتصادی آمریکا، از کشورهای جهان خواست از اجرای تحریم‌های یک‌جانبه واشینگتن علیه ایران خودداری کنند.
این وزارتخانه روز جمعه، ششم شهریور، در بیانیه‌ای «عملیات طرد اقتصادی» آمریکا را «تروریسم دولتی» خواند و مدعی شد تحریم‌های جدید واشینگتن با منشور سازمان ملل و اصول حقوق بین‌الملل مغایرت دارد.
در این بیانیه، جمهوری اسلامی آمریکا را متهم کرده است که با استفاده از نقش دلار در نظام مالی بین‌المللی، کشورهای دیگر را برای قطع روابط اقتصادی با ایران تحت فشار قرار می‌دهد. وزارت خارجه جمهوری اسلامی این اقدام را نقض حاکمیت ملی کشورها و اصل برابری حاکمیتی دولت‌ها دانسته است.
وزارت خارجه جمهوری اسلامی همچنین به قطعنامه‌های مجمع عمومی سازمان ملل درباره منع مداخله در امور داخلی کشورها و اصول روابط دوستانه میان دولت‌ها استناد کرده و گفته است دولت‌ها نباید آثار تحریم‌های یک‌جانبه آمریکا را به رسمیت بشناسند یا در اجرای آنها مشارکت کنند.
در بخش دیگری از این بیانیه، تهران تحریم‌های تازه آمریکا را ادامه «جنگ اقتصادی» علیه جمهوری اسلامی دانسته و مدعی شده است این اقدامات با هدف تحمیل فشار و آسیب اقتصادی بر مردم ایران انجام می‌شود. وزارت خارجه جمهوری اسلامی همچنین از سازمان ملل و کشورهای عضو به دلیل آنچه «مماشات» در برابر اقدامات آمریکا و اسرائیل خوانده، انتقاد کرده است.
این موضع‌گیری پس از آن صورت گرفت که آمریکا در روز دوشنبه، دوم شهریور، از آغاز کارزار تازه‌ای با عنوان «عملیات طرد اقتصادی» علیه جمهوری اسلامی خبر داد. هدف اعلام‌شده این کارزار، تشدید فشار بر روابط اقتصادی ایران با دیگر کشورها از طریق تهدید به اعمال تحریم‌های ثانویه و محدودیت در دسترسی به نظام مالی آمریکا عنوان شده است.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز در نامه‌ای به آنتونیو گوترش، دبیرکل سازمان ملل، از این سازمان و کشورهای عضو خواسته است در برابر اقدام تازه آمریکا واکنش نشان دهند و واشینگتن را مسئول پیامدهای تحریم‌های یک‌جانبه دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78074" target="_blank">📅 16:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/693aecab40.mp4?token=Icu-LCCbrlQVrppD3IlXXI12WeXdaQ80899ZxFhDUTYCJTLLbNxuz-rrqzTfDKPS1K8Zc6KHVkz5CLmGZl6O7inWZsaNWv28NJgz6LeSfmB8no14CJte04HlbUkqyFjhGfDRzEeuorZMzlGTqB7jy26ilpqL13g2FMDKCyvikbUvgz0rI8EuQB0lxzF43UaL7rp1fkmWBaGsAGkPq1WqJYz8UkPIRq95hAfkr9gAhjbtJgr9aBt6G36Rllvjbb7y-wTmFvALgOx2YNXfxiX6cssNThNmm43aVt3UGUzY0b0DncNoal9M48ZifhtDGIw6KnueEVeTlJLA85cyRvkJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/693aecab40.mp4?token=Icu-LCCbrlQVrppD3IlXXI12WeXdaQ80899ZxFhDUTYCJTLLbNxuz-rrqzTfDKPS1K8Zc6KHVkz5CLmGZl6O7inWZsaNWv28NJgz6LeSfmB8no14CJte04HlbUkqyFjhGfDRzEeuorZMzlGTqB7jy26ilpqL13g2FMDKCyvikbUvgz0rI8EuQB0lxzF43UaL7rp1fkmWBaGsAGkPq1WqJYz8UkPIRq95hAfkr9gAhjbtJgr9aBt6G36Rllvjbb7y-wTmFvALgOx2YNXfxiX6cssNThNmm43aVt3UGUzY0b0DncNoal9M48ZifhtDGIw6KnueEVeTlJLA85cyRvkJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش ایالات متحده در ویدئویی که روز پنجشنبه پنجم شهریور منتشر شد اعلام کرد که نیروهای آمریکایی مین‌های دریایی را از تنگه هرمز پاکسازی کرده‌اند و مسیرهای بین‌المللی کشتیرانی باز هستند.
دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ارتش ایالات متحده، سنتکام در یک پیام ویدئویی که در رسانه‌های اجتماعی منتشر شد، تاکید کرد که «امروز، خطوط کشتیرانی بین‌المللی باز هستند و تردد در حال افزایش است.»
کوپر با اشاره به پاکسازی مین‌ها در تنگه هرمز گفت: «شرایط، می‌توان گفت، چالش‌برانگیز و خطرناک بود. اما ما کار را انجام دادیم.»
پیشتر دونالد ترامپ، رئیس‌جمهور آمریکا، هم از پاکسازی تنگه هرمز از مین‌های کار گذاشته‌شده‌ ایران در تنگه هرمز خبر داده بود. سپاه پاسداران اما با رد این اظهارات بارها تأکید کرده که تنگه هرمز همچنان مسدود است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78073" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AQ262rurKXq3Uancl3v49LzcaPd1A5tiZqstaaq_5julgLx7YtNlUG03CrMQLpIt5Te4A3GhvztKITfh2TJRxUU05606LT0RzqlBItxu03-7e6ddJzMKoS9RNOtlmfS_ZM3Z0zwBD__bc8-XWYv5pNHtvoay9kg9_NRswpwRdaZJabOatVe-p1ezMcGjaabQruYN5kmasoXODbq3MijiTa83Yqjz2g5d5Xtqqu3fLE3nfl7isDzxCGipoQS3pcttm_OesDfypYakI2Y4uTnZgcf7MN3PWnvCgsSXqBFmw0AhY9asG8Vvw810m9PrHmxfAn8B2K2XrTb_z3rp880CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ms-M1m5CXeQklzMyNSGRviwu6IDzpNdXRHt9EcZx_u6BuvMYS05Kj-FmZ91_4x0zWCH395ZxIWO6_PeKhOBBmhYCGfPlXh011BBbc8UoNHKZoIveRIt_ATNJFULuIzLviARyRmletBV-wdXJn-GwryHq5zyNBUBbMLmNu1wkNfPHAJ6dBw4Ftge8Td5ClJ_OPUX4qJg8Sh0BX0E1c3MtY7N1r7I-IxYnjAQHxbOy6PY3sfwyL9znF-ck-tmXPWO385trXnQpDlJnTCpkwbIb-KI7dDiNeGS3Rsoxm3tyHe2inohi_jGdZ7Gp-soXheZJ0LnDRwVeSLgmhJBgksBC5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفت‌وگو با اکسیوس درباره تنگه هرمز تاکید کرد که این تنگه «باز است.»
او گفت: «پاسخ ایران بسیار ملایم است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم. تمام ماجرا همین است. بقیه چیزها اهمیتی ندارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78071" target="_blank">📅 16:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tabW2FV4fqVwy9b57APTNaGkySh_k1Fl1OlFdm-PcqU4dr7c_zaxfNqTCB3ryKM9Z30FsIiNIB586AwSoLjCMNOUvqwMX4r-VCIgwVkcA0YjtKRVFZiWz1x_T_13aejT3X96cGDvvV9CVjsvKC_c2WFQjj6dnmfWc-t0A9Ywe3RNHPraQ9I8QYxNxX1CyBCTN6hxDImHOiJ_OQYKKjfKj1TpSt57Cxp8-Qoht8bgsNhf2N73j0PsdJqNbZ3eH_P6uCY35fRH7dynzFBVaQI73ne8IZiGJ8e4R4Q5ZZij4EjGg_alMfbaBnvEfCE3dpO1pD55BlCgQTbKyWajUS9Wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chIG0Dj5UbOwq6U2nDDMerURODP-w2Hy6DZgBPUygDzI-VjPhzk3N7qYRVXLBQcMV3Mvo54U7dulrNV6WJCirjfIvnYGcqgmCCP9A0VCKlYGvOyVdZDu_Z_C4EW4N101Xl9xIKN883jtAfk3p73HNTePTs_9KdGDiMzC6gwAH7dcVlDvNsYyrSMkmLqPfWwUPaSDJCTFYSgbcKI5QJBNSef6gtxFZAlLTmV1OZKVckIENJJrU2rKF3KXz2miUeHgNVvxmJLFDBThzz3BmoW37KWasBKRcAxQburcLtjGnFaBoCExpfCcHy1Q9kgydyJDlSbyPlx8-jBr9cx3RhKm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع آگاه به رسانه‌های آمریکا گفته‌اند جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، در جریان سفر محرمانه خود به مسکو از مقام‌های اطلاعاتی روسیه خواسته است اطلاعاتی را که می‌تواند به ایران کمک کند، در اختیار تهران قرار ندهند. همچنین گفته می‌شود موضوع حمایت روسیه از ایران از محورهای گفت‌وگوهای او با طرف روس بوده است.
این دیدار در جریان نخستین سفر برملا شده یک رئیس سیا به مسکو از سال ۲۰۲۱ به شمار می‌رود. کرملین تایید کرده است که آقای رتکلیف با مقام‌های اطلاعاتی روسیه دیدار کرده، اما با ولادیمیر پوتین، رئیس‌جمهور روسیه، ملاقات نداشته است.
بر اساس گزارش‌ها، جان رتکلیف علاوه بر موضوع ایران، درباره نگرانی‌های آمریکا نسبت به امنیت کشورهای عضو ناتو نیز با مقام‌های روس گفت‌وگو کرده است. با این حال، مقام‌های آمریکایی و روسی جزئیات رسمی درباره محتوای مذاکرات منتشر نکرده‌اند و سازمان سیا نیز از اظهار نظر درباره این سفر خودداری کرده است.
@
VahidHeadline
وزیر خارجه روسیه می‌گوید مسکو با دریافت عوارض از کشتی‌های عبوری از تنگهٔ هرمز موافق نیست؛ با این همه به گفته او، این موضوع به مذاکرات بیشتر نیاز دارد.
به گزارش خبرگزاری اینترفکس، سرگئی لاوروف در گفت‌وگویی با تلویزیون «آربی‌سی» با اشاره به باز بودن تنگهٔ هرمز تا قبل از آغاز حملات اسرائیل و آمریکا به ایران در ۹ اسفند پارسال، گفت: ایرانی‌ها «تنها برای این‌که تنگه هرمز امروز کاملاً باز باشد، در حال بحث در مورد عوارض عبور هستند. تا زمانی که ایالات متحده و اسرائیل آن قمار را آغاز نکردند، هیچ عوارضی وجود نداشت».
لاوروف تصریح کرد: «آمریکایی‌ها اکنون از ایران می‌خواهند تنگهٔ هرمز را باز کند و ایران می‌گوید که در ازای آن باید تحریم‌ها کاهش یا لغو شوند. و آن‌ها این کار را خواهند کرد».
رئیس‌جمهور آمریکا روز پنجشنبه گفت که دیگر نمی‌خواهد با مقام‌های جمهوری اسلامی مذاکره کند.
ترامپ افزود: روسیه رفتار مناسبی در تنگهٔ هرمز داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78069" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ezz4Xugy6QtmNw6gcdHoDJT-V_1Z5kl_wFHMKZ1iFC2FDwIkOQNI40RENPEI3sjCSCMuMAUr-CgiJ7u1BYvSjHM-29wim7tF4qXyVGel8XUaXSZDuz9_NV-r_vdNjHuDR97t6ne_zvKLGdNXKFmUfGgKdBTwSBn2TqWqE8S-R7aqTKHuuSfbXUvYWp81CKuzJtGlkS-Cj-cfp6JLXABtXTf15uKB8fWMuIGQWtxcok7Z7_FVhsItLgWppLypZMNDqEiMvylMWcDblJhH2sHe-kUMBenz1Kzx50cqPlOFXZxFMUAX-dledtfu_iK8lONBZOZCmC_xekAow-tevMx21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه جهان صنعت بر اساس آمار بانک مرکزی گزارش داد که تورم نقطه‌به‌نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید؛ رقمی که نسبت به ۸۳.۹ درصد در تیرماه افزایش نشان می‌دهد.
براساس این گزارش که صبح پنجشنبه ششم شهریورماه منتشر شده، تورم نقطه‌به‌نقطه در بخش کالا به ۱۲۱.۵ درصد رسیده و از افزایش چشمگیر قیمت اجناس طی یک سال گذشته حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78068" target="_blank">📅 16:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=c4AEkcpr6wP-7wMqC0o9HEGGsP7-MZBiK0o8R6DGlTQpDgKDQnDTW82QNlLrmlTdaBI0oZ2yiDmF8taGmuBOMd-s6y1kwqAlkRJvnBzSis8qJA1MLdEovEIHF3t2pjtPwZWqAzgqAlirR6DVix9s3jZRE-crTkCtovkjsw5MHGU0AQJhyzaqydhsct44rjHtOaHLiW_HRdxlRljTMJNoqsC8YAp_goHFG8gZPJSehM21C8S1tHRzuKmS70xPdo6NvkK35u_xYRvb2yEyJ8g70LdcyHsiLXSID05GS9psuFrs9ExYIQWjqtDD2iwifh0KNQngX21qUC4mbNMVoOoe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=c4AEkcpr6wP-7wMqC0o9HEGGsP7-MZBiK0o8R6DGlTQpDgKDQnDTW82QNlLrmlTdaBI0oZ2yiDmF8taGmuBOMd-s6y1kwqAlkRJvnBzSis8qJA1MLdEovEIHF3t2pjtPwZWqAzgqAlirR6DVix9s3jZRE-crTkCtovkjsw5MHGU0AQJhyzaqydhsct44rjHtOaHLiW_HRdxlRljTMJNoqsC8YAp_goHFG8gZPJSehM21C8S1tHRzuKmS70xPdo6NvkK35u_xYRvb2yEyJ8g70LdcyHsiLXSID05GS9psuFrs9ExYIQWjqtDD2iwifh0KNQngX21qUC4mbNMVoOoe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک زن شاغل در حرفه قصابی با انتشار ویدیویی از وضعیت کساد بازار و تشدید فشار معیشتی مردم می‌گوید مشتریانی به مغازه‌اش می‌آیند و می‌گویند شش ماه یا حتی یک سال است گوشت نخورده‌اند.
مرکز آمار ایران در تازه‌ترین گزارش خود از ادامه جهش قیمت مواد غذایی در مردادماه خبر داده است.
در میان گروه‌های خوراکی شیر، پنیر و تخم‌مرغ و همچنین گوشت و فرآورده‌های آن، از جمله گروه‌هایی هستند که در ماه‌های اخیر افزایش قیمت بالایی را تجربه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78067" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ItXJEsMBnTZhgRMP7Tam0PQboXCKJQCE68z33MKaq_O8e8vR5UPN2f4WsRDKLJZKkGJBJszelvRSep7hPgEOJ6JM3aTUlAO8t2kjFawkLNn600_9myXx6gBE18rVpViL4YxKAZMy1ZttsQ6zSFKE27A-CB6DY18hOKSlW9GuZfmQ2SpX2h_Y17HhjGZJCfa--IipOoJ8mzON4Mpbp4iGCaDLnocKaRkR0MVtRggCJuU8TGePOr4XVXFszNyYAjsF3p3MWTG0LCbHxnr0S479GJmmxayFAYU9swrEV-2TUSR1k24fnR0sCQ8igddwSQaDWuTcm5s6qt5UwBtPyG3bgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رضا زنگنه، جوان ۲۷ ساله اهل روستای کلیل‌آباد ملایر و ساکن کرج، با اتهام «محاربه» به اعدام محکوم شده است.
پرونده او اکنون برای رسیدگی به فرجام‌خواهی به دیوان عالی کشور ارسال شده و در صورت تأیید حکم، این زندانی با خطر اجرای اعدام روبه‌رو خواهد بود.
بر اساس اطلاعات رسیده، رضا زنگنه روز ۱۳ فروردین‌ماه از ملایر به کرج بازگشت و روز بعد، ۱۴ فروردین، هنگامی که مغازه خود را باز کرده بود، مأموران به محل کار او یورش بردند و او را بازداشت کردند. شماری از مغازه‌داران و کسبه اطراف شاهد بازداشت او بوده‌اند.
زنگنه تعمیرکار خودروهای لوکس و خارجی است و هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شود. او از ابتدای پرونده وکیل تسخیری داشته، اما خانواده‌اش در جریان رسیدگی قضایی، وکیل انتخابی نیز برای پیگیری پرونده معرفی کرده‌اند.
@
Tavaana_TavaanaTech
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78066" target="_blank">📅 16:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgvfb_d_-6V0QHVi2mF4U7zBKUZxn3soaPAOJMxPuFoGjIJeqd4hIGGUpQ4j5HvndyRDCGOhRXErX7WNhqXnew7tDjWLeLD5b9Zoco24X63sBc5un2C0-UAzHMC0H5vSJauyMnfmpG0IghKmLUL7CcfREDuA-joxw3z8bCHry9osUS5DSLCoVvuDprUy5lh5uKzs-wzNL7jwZo0wUfqsmX-7jH55EV_WffoI48c1gAA6TixmESRGRo_hp-qiRqCDbMsLPIYpAfJfcEghdT6GtEb0YmnISbRlRZQZLmtioj6VeyCDyh88y8h6Bnq2ylqo3V1RiSCDG3Lsnj9GaVRDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ به میانجی‌ها اعلام کرده است که تمایلی به بازگشت به مفاد توافق اولیه ماه ژوئن با جمهوری اسلامی ندارد.
این موضع تلاش‌های تازه قطر، عمان و پاکستان برای احیای مذاکرات میان واشنگتن و تهران را با مانع روبرو کرده است.
روزنامه وال‌استریت ژورنال روز پنجشنبه پنجم شهریورماه به نقل از افراد مطلع گزارش داد که دولت ترامپ این موضع را بارها به میانجی‌ها منتقل کرده است.
توافق اولیه که با میانجی‌گری پاکستان شکل گرفت، بازگشایی تنگه هرمز و آغاز گفتگو درباره برنامه هسته‌ای جمهوری اسلامی و پایان جنگ را دنبال می‌کرد. در مقابل، کاهش تحریم‌ها و دسترسی تهران به دارایی‌های مسدودشده در نظر گرفته شده بود.
به نوشته وال‌استریت ژورنال، ترامپ اکنون فشار اقتصادی بر جمهوری اسلامی را در اولویت قرار داده و آماده است برای مشخص شدن نتیجه این سیاست صبر کند. آنا کلی، سخنگوی کاخ سفید، نیز گفت هیچ مذاکره‌ای با جمهوری اسلامی در جریان نیست یا برنامه‌ریزی نشده و محاصره دریایی و «عملیات طرد اقتصادی» ادامه خواهد یافت.
این گزارش در حالی منتشر شد که عاصم منیر، فرمانده ارتش پاکستان، اوایل هفته جاری برای گفتگو به تهران سفر کرد. وزیر خارجه عمان نیز برای دستیابی به تفاهمی درباره مسیر عبور کشتی‌ها از تنگه هرمز با مقام‌های جمهوری اسلامی گفتگو کرده است. نخست‌وزیر قطر نیز پنجشنبه پنجم شهریورماه در تهران با مقام‌های جمهوری اسلامی دیدار کرد.
وال‌استریت ژورنال نوشت اختلاف بر سر نحوه تفسیر توافق ژوئن و شرایط بازگشایی تنگه هرمز، دستیابی به چارچوبی برای ازسرگیری مذاکرات را دشوار کرده است. هم‌زمان، تهران بر اجرای مفاد توافق پیشین تاکید دارد، در حالی که واشنگتن مسیر فشار اقتصادی را دنبال می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78065" target="_blank">📅 23:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=thqoOxAAHPQZ4QMx91DewsoKw713eZXSZNW0oBNsbnS8yOs5xxn_N_OW78FVn8BJ8TmNOAY9uc3W_5tWf6RwFVmassTtDDjGVEmWitXkftbSDl34KrHfdlkamyewZNdsuBMALkj6G_l0tmIZS7Mqlk75ibtjiVBNbgpnf2o-tjdVxRldLiZhP3nvdELXRrC0_Bb9AwNuZ1s7XdjfffOBlaJbjnysgRLH15um_Bg_0drH3kPH-pXrVWd7TklFfJOwIm3vkodnRIuOXkx6nVIgnuUCgDIqTlyghkRcErfFnizW9_ERKreF5QRjBXQS3vG328hSUSvySfdBadrHEubudw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=thqoOxAAHPQZ4QMx91DewsoKw713eZXSZNW0oBNsbnS8yOs5xxn_N_OW78FVn8BJ8TmNOAY9uc3W_5tWf6RwFVmassTtDDjGVEmWitXkftbSDl34KrHfdlkamyewZNdsuBMALkj6G_l0tmIZS7Mqlk75ibtjiVBNbgpnf2o-tjdVxRldLiZhP3nvdELXRrC0_Bb9AwNuZ1s7XdjfffOBlaJbjnysgRLH15um_Bg_0drH3kPH-pXrVWd7TklFfJOwIm3vkodnRIuOXkx6nVIgnuUCgDIqTlyghkRcErfFnizW9_ERKreF5QRjBXQS3vG328hSUSvySfdBadrHEubudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در کاخ سفید و پس از امضای فرمان اجرایی تغییر نام «دریاچه اونتاریو» به «دریاچه آمریکا»، به پرسش‌های خبرنگاران درباره نحوه اعمال تحریم‌های ثانویه علیه کشورهایی که با جمهوری اسلامی ایران روابط اقتصادی داشته باشند، پاسخ داد.
ترامپ در واکنش به پرسشی درباره عملکرد روسیه در منطقه و برخورد احتمالی آمریکا در صورت تداوم معاملات با ایران گفت: «تا اینجا رفتار روسیه در رابطه با تنگه هرمز بسیار خوب بوده است.» او با تاکید بر تقابل پایاپای واشنگتن با سایر قدرت‌ها افزود: «باید در نظر داشته باشید در برابر هر کاری که آن‌ها انجام می‌دهند، ما هم انجام می‌دهیم.»
رئیس‌جمهوری آمریکا همچنین در پاسخ به نگران‌کننده‌بودن اقدامات پکن گفت: «یک نفر درباره چین می‌گفت شنیده‌ایم آن‌ها دارند جاسوسی می‌کنند؛ ما هم از آن‌ها جاسوسی می‌کنیم. وضعیت همین‌طور پیش می‌رود.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز پنجشنبه پنجم شهریورماه، فرمان اجرایی جدیدی را امضا کرد که به موجب آن دستور داده شده نام «دریاچه اونتاریو» فورا به «دریاچه آمریکا» تغییر یابد.
ترامپ پیش از امضای این فرمان در دفتر بیضی کاخ سفید اعلام کرد: «ما نام دریاچه اونتاریو را تغییر می‌دهیم و این تصمیم از همین لحظه لازم‌الاجراست.» بر اساس اعلام یکی از مقامات کاخ سفید، این فرمان وزارت کشور آمریکا را موظف می‌سازد پایگاه داده‌های جغرافیایی ایالات متحده را برای بازتاب این نام جدید به‌روزرسانی کند.
این اقدام نمادین پس از شکست مذاکرات تجاری میان واشنگتن و اوتاوا، وضع تعرفه‌های تلافی‌جویانه و تیرگی شدید روابط میان دو کشور همسایه رخ می‌دهد.
با این حال، مقامات کانادایی پیش‌تر صراحتا اعلام کرده‌اند که این تصمیم یک‌جانبه واشنگتن را به رسمیت نخواهند شناخت و نام این دریاچه مرزی مشترک در خاک کانادا همچنان «دریاچه اونتاریو» باقی خواهد ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78064" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L0W_3K4zU1DvBvSV7duRY-p0JhTbtgSyxy335_Jf4rgg4z_mY7Z8OJi7gFk-Yr3leZBbMF4L7UaPmQ96lC-Dp6ERNva8LwLNRMQAm3agwBg0d9rSQsR-akZ68XG_NxlhDS3PdVV56DWYBCgv8hnCnMARx1WEqM3NlYmC7qr-xYOK_-ojMtcTyzS4LCDEoVELr2AGJ7mEKZPbJDAv2HvrYOyQ0V7M8kBawggkvlmawsbHJcrdslrmyp9j0e1EW2DVB34P6hUuBltAEmJ9-fhl9SNSf4C3ebDI6Z2NoxZeKR0oLKDBvBNliKgF6NY434-vrH1xHSoTg7dSZ_ioApM3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان اطلاعات سپاه روز پنجشنبه ۵شهریور۱۴۰۵ با انتشار بیانیه‌ای نسبت به تشدید نارضایتی‌های اجتماعی هشدار داد.
در این بیانیه به ناکامی «دشمنان ایران» در «تلاش برای تغییر حکومت ایران از طریق حملات نظامی» اشاره شده و آمده است: «مخالفان جمهوری اسلامی در حال تغییر راهبرد خود هستند.»
این نهاد نظامی و امنیتی مدعی شد که فعال کردن بحران‌های داخلی، جنگ روانی، فشار اقتصادی و عملیات‌های امنیتی از محورهای این تغییر رویکرد است.
سازمان اطلاعات سپاه در این بیانیه نسبت به افزایش نارضایتی‌های اجتماعی و احتمال اعتراضات خیابانی هشدار داد و گفت مخالفان جمهوری اسلامی بر «برهم زدن ثبات و کاهش تاب‌آوری ملی» از طریق «نبرد شناختی و تولید ترس و ابهام» تمرکز کرده‌اند.
این نهاد همچنین از شناسایی آن‌چه «ساختار محرمانه و اختصاصی» موساد، سازمان اطلاعات اسراییل برای اعمال فشار از داخل ایران خواند، خبر داد و مدعی شد این ساختار از طریق ارتباط با گروه‌های مخالف، انجام عملیات خرابکارانه و به‌کارگیری عوامل محلی فعالیت می‌کند.
در این بیانیه ادعا شده که جمهوری اسلامی از وضعیت «صرفاً پاسخ‌گویی» به حملات خارج شده و در پی افزایش نقش خود در تعیین روند جنگ و دیپلماسی است.
در بخشی از بیانیه منتشر شده آمده است: «ایران دیگر صرفاً در موقعیت پاسخ به حملات طرف مقابل قرار ندارد» و به سوی «افزایش ابتکار عمل راهبردی و اثرگذاری بر زمان، مکان و هزینه جنگ و دیپلماسی» حرکت می‌کند.
سازمان اطلاعات سپاه همچنین ادعای حاکمیت ایران بر تنگه هرمز را تکرار کرد و نوشت توانایی‌های نظامی و «نامتقارن» جمهوری اسلامی حفظ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78063" target="_blank">📅 23:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRqyRoGn1W1A_ScjXMCoNeUG70Y3W59t5k0kGzC8tjnRRJY0uuBCIAMGPAxfZFTal65qL6YVtLbt52McEEmwXnA3jAwsBlp-3pLcePmsLcyIKsQM--BkvGFa3l0I3_8T1ywfcU9xXrSLGJr27VlINmgEOymfRWayZcDUB0Ky4hBascH7HW32Pb2uM_64NREd5e337F9eZeXDWW2mXpWs__liPt5t6mkQoq1pMm4PwedK9UeaM7AvQSMWi97tT-KnqxETZWGGcD51kTCl2SJ9FwQsg9t0Kw3nYIPUqS5HbGZtFw0YmHdDD5sO8wNH1zYSmktOLC9O06rqqbT2HQku9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.
به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم خواند، و در توضیح دلیل آن گفت: «توزیع بنزین عادلانه نیست و تداوم این مسیر غیرممکن است. ضمن این‌که تولید بنزین کفایت نمی‌کند و با محاصرهٔ دریایی آمریکا نمی‌توانیم بنزین وارد کنیم.»
این مقام دولت ایران در عین حال گفت مشخص نیست این تغییرات به چه میزان و چه زمانی انجام می‌شود.
در روزهای اخیر، هم‌زمان با افزایش اظهارنظرهای مقام‌های جمهوری اسلامی دربارهٔ لزوم افزایش قیمت بنزین، گزارش‌های مختلفی از تعطیلی برخی جایگاه‌های عرضهٔ سوخت در تهران و تشکیل صف‌های طولانی مقابل آن‌ها منتشر شده است.
بر اساس آخرین آمار اعلام‌شده، تولید روزانهٔ بنزین در کشور حدود ۱۱۵ میلیون لیتر و مصرف آن حدود ۱۲۹ میلیون لیتر است. به این ترتیب، میزان تولید روزانه روزانه حدود ۱۴ میلیون لیتر کمتر از میزان مصرف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78062" target="_blank">📅 19:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y9Y1Q-PElffIMTjkcoO55KOULqYP3ppbm7a7qvPirg_tdw_E0Fm8vDGniZ-T_alnLE4B5l_QrAEdEpzqwWbd2RD3FvjBM2BuXmPq54aPYw3I6cwqiLJp_aCYJvgdmm6V8jtz-RzrzWmihp7ILnNVbh_RoBgQsyK5Qit5MGpafiwOkjc98-lgw1sy9-AqFR5eVUDRnJ3oOLXcKQdLLs-9NaaObkmIjku_5AnATdj8F891IgmpRVNbGelZj2NK9TXkMHIDrZOjyFkX0z4FMMkqc3Ljnch9xESLjP6uTeyRbUBg9T-WooZpmhMMDBgnn_AGcikxxrw6Dd7F67xnJOMXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KFPXKnGm3heiCC6njdMizJsARDqDBgJok5SqWFM3aFj6vvGmD0eD-lgHT-AjkGYPWFCRbolod439XeK5ihuJCKUsmE7a1VCzYoETfsrRSVubxn173zP8o6BAEM6NrRNmePRVabbojLyRWA6U7yVuwwHbwtbDuhjWW6GtITE24-0CshWhjyHGkxMDs4M0t5AIsbO1HTgW29Q_xQ8A2evvrLx0EjoYeQT8LHX-q2FhydasEHs_mZ_zt0xtr1uCfFeL25z3AehI_h8gB4hi8gK2_4ZDhW0qKj1B1KfRkvl_kty9bs_6FG-BgoU7qZKE3_nsr2DEE3JaC3oYNKimNEw0eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، در سفر به تهران با مسعود پزشکیان دیدار کرد.
وزیر خارجه قطر در این سفر با محمدباقر قالیباف، رییس مجلس شورای اسلامی نیز دیدار کرده و درباره راه‌حل برای از سرگیری مذاکرات میان واشینگتن و تهران گفت‌وگو کرده بود.
@
VahidOOnLine
وزیر خارجه قطر همچنین به قالیباف گفته است که گفت‌وگو بهترین راه برای حل اختلافات و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78060" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apttruYTd8yo8RoOUHAFsnhnmLhOQ2og5y96hjATMZ3PLbkJexjXiC2Lfcuc97JJ2xJLtYV-EdDvSfh9xsVuq53doQhriI2MbYtwio6vv4Qi_OzkpnRdaTenZwPNbipsvmynZfcfnUQaNDQOQeKobbohm1E3dNwDGAOOJe92KUr_1HgJERqDPRGTNwZH5dItw_nrFOglBw00-IDKiJDFe55k3BJXBVfgBCIuGXB0MGN8CUg8quIPSst5rg82EsW8oT32cPwzaWyIZk4ma0BwXkOikEjCPS2wg5FNZO1GT81xp3U_AzcGFYlHCUERuDIlTF_LCulfcp-c-07cwtz5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیه رمضانی، زن ۳۹ ساله و مادر دو فرزند، در جریان سرکوب اعتراضات دی‌ماه ۱۴۰۴ در تهران با شلیک مستقیم نیروهای جمهوری اسلامی کشته شد.
ماموران بامداد جمعه ۱۹ دی ۱۴۰۴، از فاصله‌ای نزدیک و از پشت به رمضانی شلیک کردند. گلوله پس از عبور از پشت و قفسه سینه، به قلب او رسید و جانش را گرفت.
آسیه رمضانی مادر یک دختر نوجوان و یک پسر دبستانی بود.
خانواده‌اش می‌گویند پس از تیراندازی، او را به یک درمانگاه منتقل کردند؛ اما بدون رسیدگی پزشکی موثر، برای حدود پنج ساعت در حال خون‌ریزی رها شد.
خانواده رمضانی پس از بی‌خبر ماندن از سرنوشت او، سه روز میان پزشکی قانونی کهریزک و بهشت زهرا در جست‌وجویش بودند تا سرانجام پیکرش را پیدا کردند.
خانواده، زمانی که پیکر رمضانی را یافتند، گونه‌اش کبود بود و از زیر کاوری که پیکر را در آن قرار داده بودند، همچنان خون دیده می‌شد. آن‌ها گفته‌اند پیکر او در شرایطی «ناشایست و دردناک» نگهداری شده بود.
خانواده رمضانی همچنین می‌گویند لباس‌ها، کفش‌ها و دیگر وسایل شخصی او برداشته شده و به آن‌ها تحویل داده نشده است.
آن‌ها پس از تحویل پیکر متوجه شدند قلب رمضانی که با گلوله شکافته شده بود، بدون اطلاعشان بخیه زده شده است. خانواده آسیه رمضانی در روایت خود نوشته‌اند: «ما آن سه روز را فراموش نمی‌کنیم. آن پنج ساعت، آن خون، آن کاور، آن قلب شکافته‌شده و وسایلی را که باید به خانواده‌اش بازگردانده می‌شدند، فراموش نمی‌کنیم.»
آن‌ها تاکید کرده‌اند که همه واقعیت‌های مربوط به کشته‌شدن او هنوز روشن نشده است و افزوده‌اند: «هزار سال هم که بگذرد، خون عزیزانمان پاک نمی‌شود. نامشان را تکرار می‌کنیم، روایتشان‌ را زنده نگه می‌داریم و دادخواه می‌مانیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78059" target="_blank">📅 17:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2K86osKxwarwGORaEC0Ni4eY11VXleoK9rUmo6X4ejIji6YqNJ9lRNu90YWzGLX-wUImNCVddfaW45kCtyjO209SVOPXl0DOab0Z02k8wDvdyDzwcb5_v3sa55JYNPjOpBLClwKdj9RZ7bLddRypLvyyvEaIgTkaYSBI_a-4jq-0h-bvKwC7pymrX5LubuVZNeOhIs1nmr7XRQ7TEC-e9dlBd03s-Eq1U9gOv5JkFErXXq2104BJlcfSn9zrwv0Os0z5ZXqhDb1VsUBQfCxxCIjU-Fd1wke-782WkbwQtQUMbLHpVz2myUgFUxR_fIk5jT-LAAu01AbeLaAw7sODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با انتشار پیامی در شبکه اجتماعی ایکس، با انتقاد از سیاست‌های مالی جمهوری اسلامی، خواستار اختصاص منابع مالی کشور به مردم ایران شد.
بسنت در پیام خود نوشت: «در حالی که مردم ایران برای تامین نیازهای اولیه خود با مشکلات معیشتی دست‌وپنجه نرم می‌کنند، حکومت فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.»
وزیر خزانه‌داری آمریکا در ادامه افزود: «حکومت ایران به جای تزریق میلیاردها دلار به گروه‌های نیابتی تروریستی خود، باید این پول را صرف مردم کشورش کند.»
این اظهارات هم‌زمان با تشدید کارزار تحریم‌های مالی ایالات متحده برای محدود کردن دسترسی حکومت ایران به منابع ارز خارجی مطرح می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78058" target="_blank">📅 17:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTsMhoORZP_EZi-f_BNo2SBOXtuq2pyUC12JUclvjgfIIQ3JsyGTCf0bIXuSHm8qifACCV6dDcT01H93iH864Mvy8-wBMjsx7PiP1Y8HFasn9dBxVFTL3azDyNmuBI4MAOyWmeohRENv5WhjNmgU3Vn8RTilZvRteaCYIuNP5m0biwm8kHpzt4NTBV_fjZrfEoXSFw3Ip0_BiIJGLDb8eZjFgeTcL7qAAGBp-gZzhdDmrN-a8x-jzWt_j4o9vlU-zaM92AdkJKue59PK-y83vlHrMvnmDBka_J-vnyBk5coiW173w9gMzUdI5gD1mCavfHzVK0CbsdfTIb3rylyJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت شاخص برنت در پی بهبود وضعیت تردد کشتی‌ها از تنگه هرمز و انتظارها درباره مذاکرات مثبت میان ایران و قطر روند نزولی خود را ادامه داد و روز پنج‌شنبه به ۸۶ دلار و ۷۵ سنت رسید.
قیمت نفت طی روز جاری نسب به روز چهارشنبه بیش از یک دلار و نسبت به هفته گذشته حدود هشت دلار افت کرده است.
در پی سفر وزیر خارجه عمان و فرمانده ارتش پاکستان به تهران طی روزهای گذشته، اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، روز چهارشنبه اعلام کرد نخست‌وزیر قطر نیز قرار است به زودی به تهران سفر کند.
هم‌زمان وزیر خارجه قطر در تماس با همتای ایرانی خود بر حمایت دوحه از تمام تلاش‌های دیپلماتیک و اقداماتی تاکید کرد که هدف آن دستیابی به راه‌حلی برای تضمین آزادی کشتیرانی و فراهم کردن زمینه توافقی جامع برای برقراری صلح پایدار در منطقه باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78057" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qz4GfLOyeVgdSsJvr8Sg7APM9Wy8QQRDOggOjjwRC7VCnTYn-rNbARbtt9vJjfkCvDXBXzlshVTjVtnrI4wh984GC98Xo4Lkz5Wdj9vM8pVEF1vyqig_N6U3d0z0aWeNU9xLRbsVcYmtne9n3ck2L8uZQvTISs79w4fm9dNKNQLvmnPmfatJnXhwx10AGJc9aTJ69kIp6UXfqoKN96JdLjXD3SkP9vGwcL543vg45ylBtWxYOx4Ve-LBH5XkMCVs2p4ovUGdBYLWPijy3pS921QR5TYamyMFYoSC8g-9idHdogyEXZnxLpCVqEsK_ibR2eGQypOYcd7MUjyJXUkB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه مدنی، پژوهشگر و متخصص ایرانی حوزه آب و مدیر مؤسسه «آب، محیط‌زیست و سلامت» دانشگاه سازمان ملل در کانادا روز چهارشنبه چهارم شهریور جایزه آب استکهلم ۲۰۲۶، معروف به «نوبل آب»، را از کارل گوستاف شانزدهم، پادشاه سوئد، دریافت کرد.
این جایزه در مراسم رسمی هفته جهانی آب در استکهلم به پاس پژوهش‌ها و فعالیت‌های کاوه مدنی در زمینه مدیریت منابع آب، حکمرانی آب و ارائه دیدگاه‌های نوین برای مواجهه با بحران آب به او اهدا شده است.
کاوه مدنی پیش‌تر در ماه مارس به‌عنوان برنده این جایزه معرفی شده بود و کمیته جایزه، از پژوهش‌های او در مدیریت منابع آب و پیوند دادن علم با سیاست‌گذاری، دیپلماسی و ارتباطات عمومی تقدیر کرده بود.
جایزه آب استکهلم از سال ۱۹۹۱ به صورت سالانه اعطا می‌شود و مراسم آن را بنیاد آب استکهلم با همکاری آکادمی سلطنتی علوم سوئد برگزار می‌کند.
این جایزه که شامل یک میلیون کرون سوئد و یک تندیس کریستالی است به افراد یا سازمان‌هایی اهدا می‌شود که دستاوردهای برجسته‌ای در حفاظت، مدیریت و استفاده پایدار از منابع آب داشته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78056" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_AwzLwUEDFU9WxJmVBPxZn2w9san0ZuC_r9OTtJiP19LdJTm3ucvwBv_ngk9PaQSKbAkESGQOwkc02CERlxsJ7A98tUqwnDH5CwEIOxHkC81bCZKxDsAqhgn44lLR2bk8aZ7aWLYKwnErNKbNQ6hQRMdavBTzwFvjCxpQegxdDveraGdEbQsZcfMxm2CEA1Jpmc-qSUBcsXCzjVxIiz-1W7qC_J1BHsmS3rjnEw6d8NOF33PzIOljX9-BQSUrXEkfxSvpxQx2daZU2ICzkgS3w7KlHQ33f_-lww5AXnfE1om3K-faqjPF1hf_WGl6QKQFtJvtERStIcJbRKIHCfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلا ابوالحسنی، از بازداشت‌شدگان اعتراضات دی۱۴۰۴، به اتهام «محاربه» به اعدام محکوم شده و پرونده او پس از اعتراض به حکم، اکنون در دیوان عالی کشور در حال بررسی است.
لیلا ابوالحسنی، حدودا ۴۳ ساله و مادر دو نوجوان، از ۱۸دی۱۴۰۴ در زندان دولت‌آباد اصفهان نگهداری می‌شود.
یک منبع گفته است که ابوالحسنی روز ۱۸دی در شاهین‌شهر و هنگامی بازداشت شد که در حال عکس گرفتن از آتش‌سوزی یکی از فروشگاه‌های «افق کوروش» بود.
به گفته این منبع، دستگاه قضایی او را به دست داشتن در آتش‌زدن این فروشگاه متهم کرده است؛ اتهامی که به صدور حکم اعدام علیه او منجر شده است.
در حال حاضر، دیوان عالی درباره اعتراض او به حکم اعدام در حال بررسی پرونده است.
لیلا ابوالحسنی از زمان بازداشت تاکنون، بیش از هفت ماه را در زندان دولت‌آباد اصفهان سپری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78055" target="_blank">📅 17:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e5q146Z1xDmwCwsYWjEHRK7TVDfakFAdw6GFGTYs9bqfY9-H_RdzSwHJOS15_uxOg1aZ-W6rWMmsWeBvMz9-q8DrL98Oo6agucnr1EeIiIzHqzKChtCdIdeRI10dlyjdfXgYs4y4nBvaPGCVw8NONsEq2EqrV1TMT-TCSCYUnFVyoiyeFNcOH5cWdL45NrI_HiDTSAMtKMBcDYzWNey4gfZi4yTEpEAxfaKJQP-x7F4jekxYO9wB8YHRC8mbrKajL9CU42KHht_XRlco5YcbGNNMsxSp33oiZif-URaxIda-qHssJNieiWluIEpuZTIBuHMqwY616r_olsordx9VZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=cnafa1L2PrTlaI3c2-zWxZ1dk-6B2PfdZmKUaerH8fj9PZ3ejkSFspz-c0nXW0sTED1O1DhmzQocS1DrUD8BEwTYLmMOWDWVUs_qVFrFeqe9rcQp1CmFFyF9rGE7puvIMKrPAf9cFjdNvh_soYJtV5GISoEywbSOVCQiMN9IRhcWZk_psx0nxMrg2tiOQPLG_d_-EF1NzHw8I-sVgOtNe6hlXLzY2cAazkY38F6PR4vdAmRe7ax_nLpqldbKXRC6ARniYq5LomDWAh9zq3IXcSqk04xKXbaSh-OGD4SIUXzO9KzVuwihKNN31FhAHmJjUUs2PlI4rJLHXdzaofUcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=cnafa1L2PrTlaI3c2-zWxZ1dk-6B2PfdZmKUaerH8fj9PZ3ejkSFspz-c0nXW0sTED1O1DhmzQocS1DrUD8BEwTYLmMOWDWVUs_qVFrFeqe9rcQp1CmFFyF9rGE7puvIMKrPAf9cFjdNvh_soYJtV5GISoEywbSOVCQiMN9IRhcWZk_psx0nxMrg2tiOQPLG_d_-EF1NzHw8I-sVgOtNe6hlXLzY2cAazkY38F6PR4vdAmRe7ax_nLpqldbKXRC6ARniYq5LomDWAh9zq3IXcSqk04xKXbaSh-OGD4SIUXzO9KzVuwihKNN31FhAHmJjUUs2PlI4rJLHXdzaofUcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oPrnyG0FD_Os3a2-9XMAMZ74q5pjFHgWaE7tWJl05gw8WvZHJMjPy5ibY8kdfsWfqBFTfnHtgZUcbLF1BmlDjWClTqOiN7S5WEGWsT6qzi-xpbrhDfrZtPBFTmTrj863ZnylqgJO0c0O6S5EtJKDAN7t4XGk_ejvn1LNWrwSBzweeabbNZhMBZWcQro71gH-9Z5XI-17gAzuT7p0VpBYqmQOY_cFCuGI5-vQeXQEQCRx03J-To6CDV-aTwbumulqKTgqVYBVaYa-sDSSZMxJyNfPBXbHelAkABndSmusOQRU2UiLgfVTTflcfrj1pn-D4LvP1TqRsu0v1rV8g6uXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isiYnxSXG1DGr6cLUSiyoKMlw-I1Y4u7g3WHFc2ya26PR2uTM6so15NXPspBZXBN7KR19uxHSS8vqpNiVXOgUWOtusBy8W-yPZBuzPCGTW3jOweoWb5oRkBR_7rES7XEOslonPOTl4FyOffslF17LRND8pN-1iXpklwYU7Ws3DbIhXKbyS6Z-3FWLWO7lb_j3e2nk8Fvf7JOEVQiOfqJ2URVPwVGQRzmqBLmSyEFMLd1Yca9Z7qNY5uVkwOrc9vMYuu9B3rFaDJGEAOVy5FyhtyF1OLh3wn3JxI75UiHuKX8Bxwn7bFv3vLZJXff_SmfwHX-7CpxI3rwcB5Wkk8siQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bO5uIJ8LtwQeQZxP0kphWPnBktHLXOB6PMzmITtKAQ7s0T-zJUmga9HTYKBylMGeI74kT3knswsM2uuguO9jfisRGdPB0sU1F4XDCgsTPozFlC1WPehExHRV7wgDUfpIHnX_PeDRQL9981dBJ14iYw7cFp7eitCdyPUen8LcvlSvEfJ7XmS6Cd8fRY0TpeMOmmlCzChpvZCmeBtHwqPgY-S6sEEFoWq05N_fX0cT-jnM_BOx5f7m02xGjPBOqSU2OmbK14uQ9BDWZsf4HCzRbL8ohxvJPHiZyek--6E-xC6KxMNnXVHY91KT3EMXiLapooVlh8FOpDTu9JTqIvCTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JMQhq2KeJn27zE2-VXWHiRm41A8AtaqpF8oEg0lM9j0SG-9hU9xaTObmRAO6dbNH9Sd7x0mJlKVC_emaiHyiMERul47P3mQ9_nCmd62w9RqyKhWdnsLkPAiDOydVK0qAcN9mVSvC5_zFs80t3H-ERStmQk5yR5N6jrXijWBLGKTqU5v1QQtAi6xxsDrSYSjWJzkSC3GES9g08xujX7NnisPdW31PQrzsbhFUAWn4z8s5bjUt429S5o82NnyFsWaVOQ4sx5xjyPdUuBJWtt_oFHP3J9MtklB6gzLn7TScT-xSceGVEvwDJAQeIVE0TxTv5GuJIHBsLEYqZob8HuyPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ljVZiCjvY66dPX5-bg6_T98rwiodhcxq1D2uFfc84-GexBghsNa8w0QQl_5-UQmoTQ0VOFM09rpC92qD3i-x_bLvIjmBRo8NZB0sQRkgL8XDS8dPhMFTTdxJrWkBBNie4QQ6KXQ-eoyVGm7qKAxXRW_5uiONqQOPSIpVnyxLkvHleCseO2c89Bkcve02MWdsH_JIC5lSPBmz4qpI3EFZtCHWeEDeFYOv-o5AI5TFX4f-VR2Hg7WBouhy5-0XOCJmldWCnFuHG1sdndyPyTv9MhPm3NFFCkBKglrSQe8YGWo6YDz9U_Mz-KTvykrMPvhj2aNwzEI_nvnQVR_vbMmX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش وب‌سایت‌های اعلام نرخ ارز و طلا در ایران نشان می‌‌دهد که قیمت دلار آمریکا روز چهارشنبه چهارم شهریور کاهش یافت و به زیر ۲۰۰ هزار تومان بازگشت.
در لحظه انتشار این خبر، قیمت دلار ۱۹۸ هزار و ۵۰۰ تومان و قیمت سکه طلای موسوم به «امامی» هم ۲۱۰ میلیون تومان گزارش شد.
این اتفاق پس از چند روز افزایش قابل توجه قیمت ارزهای خارجی و طلا در ایران رخ می‌دهد. قیمت دلار آمریکا در این روزها تا ۲۰۵ هزار تومان افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78048" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=cis6pLOoQgdBDqoXgajLNsx0VFG8qVGstNsEhZ0PIO64OtmXyZiewrleN1wDCDJdeqOJhH4YMXXV_TQm_S9mmr2Y5wJvTqNlg4ir8S8S5bl-B7FoJw69K3uQAzPZ2TmMJgk-ecjfjdfinxWMRBoOVrnJfVLnUgSltQZQhn2r4QZ87FcR1_PFaD4ChpEPvN3LZLMT2iBWIAVO3uv-J3JCydyKHD3ezcBA_voLmGMlcyk4lv2Qautfnk8RcMvaNw7FNIVGl0pYlYb3BjrCI9yNQyJLzqYPbJi4xLbNf2yr6yysAqoPO6QmmF7L1Isy9eKQUpHeIAKmouf5D2Savuottg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=cis6pLOoQgdBDqoXgajLNsx0VFG8qVGstNsEhZ0PIO64OtmXyZiewrleN1wDCDJdeqOJhH4YMXXV_TQm_S9mmr2Y5wJvTqNlg4ir8S8S5bl-B7FoJw69K3uQAzPZ2TmMJgk-ecjfjdfinxWMRBoOVrnJfVLnUgSltQZQhn2r4QZ87FcR1_PFaD4ChpEPvN3LZLMT2iBWIAVO3uv-J3JCydyKHD3ezcBA_voLmGMlcyk4lv2Qautfnk8RcMvaNw7FNIVGl0pYlYb3BjrCI9yNQyJLzqYPbJi4xLbNf2yr6yysAqoPO6QmmF7L1Isy9eKQUpHeIAKmouf5D2Savuottg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: با «وحشی‌های» حاکم بر ایران نمی‌توان به توافق دیپلماتیک رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل شامگاه سه‌شنبه سوم شهریورماه درباره احتمال دستیابی آمریکا به توافق دیپلماتیک با جمهوری اسلامی گفت اسرائیل در اصل مخالفتی با یک «توافق خوب» ندارد، اما نسبت به امکان رسیدن به چنین توافقی با حاکمان تهران تردید جدی دارد.
نتانیاهو در جریان یک سخنرانی با اشاره به گفتگو با دونالد ترامپ گفت: «به او گفتم یک گزینه، البته، رسیدن به یک توافق است؛ یک توافق خوب. ما مخالفتی با آن نداریم.» او سپس با لحنی تند افزود: «اما تردید دارم بتوان با آن گروه، با آن وحشی‌ها، به توافق رسید. به شما می‌گویم: نمی‌توان به توافق رسید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78047" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfsGxMs9Yhz3cZlEyDDGKEqJjovDgKGJ7fErHskv_W3nvOnrIUeGP5doIpnG_YLg0MvOBt0H08n1WuJ9BCtqMO6Op1cMM-wL53IrxgcrziuOH9qJs1rpEGDowdtr9y22ZzLGsLVvTx4JpRwHovQLNjVkbNDFx7GXtz5AYmHFIqU0Dnw8wDOKYNWDYJLjdFFthiG8tJSuz1zqMp3jmnNl6R5_W8D2vaa7utWsehFq2auWjgP4PxWNOd_bzYrfs1dB2_Vjbz646mA2eeeQBNGNUrOFtE84YrgMyjsX5HHVYEDQPeLOleDyqEd2yF-7ou2bmYAFtKz6MZ-AfxzxHAa7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیح شاهوردی، بازیکن پیشین تیم‌های پایه باشگاه سپاهان، در جریان اعتراضات ۱۸دی۱۴۰۴ در منطقه «خانه اصفهان» هدف گلوله جنگی نیروهای حکومتی قرار گرفت و جان باخت.
او ۱۹ سال داشت و تنها دو ماه به پایان دوران سربازی‌اش باقی مانده بود.
مسیح شاهوردی شامگاه ۱۸دی در منطقه خانه اصفهان از ناحیه پهلوی راست و کلیه هدف گلوله قرار گرفت.
اصابت گلوله باعث خون‌ریزی شدید داخلی او شد.
به گفته یک منبع مطلع، فضای امنیتی حاکم بر منطقه و شرایط آن شب امکان انتقال فوری مسیح به مرکز درمانی را از دوستانش گرفت. آن‌ها پس از گذشت چند ساعت، او را با پای پیاده به منزل رساندند.
مسیح شاهوردی حدود ساعت یک بامداد در آغوش برادرش جان باخت.
خانواده او با وجود جان‌باختنش، مسیح را به بیمارستان منتقل کردند؛ چراکه هنوز امیدوار بودند بتوان او را نجات داد. براساس اطلاعات دریافتی، کادر درمان پس از معاینه اعلام کرد که هنگام انتقال به بیمارستان، خون‌ریزی فعالی وجود نداشته و مرگ او پیش‌تر رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78046" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qzAqvsKTa3Mv_hi6E6u3ErYxErPurTvlWSepV3By--_ruZUeFsclotMcu7lnnkJ_Tgw5WXoDvHP2SKb0CV2ebxcoQaQSJyuAX9GNtZ6CSqQXio7US93LFbc3MjuhVO_2nPPaNwQHJ5CiyZjzif8ziSXe3Pzba2kyFiwgwmy5A0Ku_IntdEwX_CyYi138nApdBr55IZ51wChIJGT1oT-ZnZwvzhZkFr11RpjYu3iRmiWaE6WTjOQ4f3EKVWsMb41nL1ywDdkzA81MEyIapo92E29UTyj50hfTt_hrz89HV-8XSQuNKLD0spK4ow8ceSPeKKe7_bc9dzcXdD1S0_1Rag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVkqwlSiwnjnrnIg75_rAqtw9w0GiBRMx-r1I8sTFyNpH-SAT1tf3VFES0p7YG4B0Sqv2nS8ZD0fsBsKp8k8LEZQsOTROgmhd3zcpYO3LuNv8ggCqCWPymkBYCOPrxfLUvULx_w2wfF1LSyzeJill5QG68jOUoihAx0Iu_h9RZSslI3mc3BGUm3wJVT4DFRGi6bwA2O7r5itdMKT9iNokdFoK0Upsu5of-gKfwv8VIPd4g6y1H-yatgmTj2Wcizy2oxdgO_ywjh5wxzpmnUqwKpkIyz2AkdZICFQ33rqT1YiHadiawNTbuwiT3Ub9xMkivG4G3GXqbmiBaaZzlrgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXRPDKV6-s70KXpqn5M81GPlbl3dW249nibBho2jLP-V-grWOi6yF53iGSriC2SXS4IVzaZimjnv0B7bxMGVdesH3dbP747s6IFyr3_fxglwP_1AUh1vteJ0t5Rr_tCNa2k2J9cTNdjPFuaroSvetqzcxozpsjP7VFO3YYeCO2eBsGJWwomWYsxVVfwpm7Fj5Yhba4yXAgZpHLaOW3vIi_w6AuKleNAtNkRUh7H7TzsBSDEOnNo8i593o7AdROnSXiSEry_pJJ5QJ2aFOrdsVuBRK2DykeNPUZpf2V4nP8i3RXMY7baKAGuDr0i-YjZsBaOe8RfxAM7Ez-yjzk99qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PN_kCoVDIYTERqo_3JBzoGn6PuNWcX2LhccdTaPC4vAuVxxJ9zYcE4d0BXO7IIW8I0Kyt-RL-P5-hnA85AsMQKGR9ZSefpnYYEbYIDK_NHjahKYMHB3-RY13HU-ut3B0q6Hu1ZrBCzP0IJl5dhfHXkETSlmEM0nt_26vZ1r5WTAE0RHlQ1a_2imDB2ozqR6OUtia6CNEiWTrecPjCbILflFn7PocSM5POiWsVmgkE90RVCRQFT75gBxHBMEFY5__BkAzaUk01IQe8v0QEf9XkkvFS70OMfFIQiQicDqE8e32YcRkXOa4TzTo45Ctl6FxvWAmUPDW0wr6yitxPqEvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ms8jtbt4xlHFHKNbR2cX3_qOK6OtaE07fi2-_AdF-P8ChFg35hzh9qpwQr75DwZ6sHp1-1Zj8fnYGCWOCtros9NMx4_rCqidIRhx_DYD-yERid6f9Gi4fag7-p1WA2l1WzCDWIFo7KEiqUD3-rNn4gtBXfW3XDYUTNc7B9I4Qk_K2ToCYTBlVVsbqd81t7-MzlnUKEIQ3enHymO_oVUYZ3BrsoI-G-WdD5TEpcWHbJI62akLj9FZXglj0uBelzfg-LgliZHmLKUvahLvETsvlrneHWqf-Gw4iQpCxhfQFhHwDuKibPkjeXE2ZX_wL9BqiSeizSwrXZihAWm4qyInSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gI0D1OHJAaNOdlRfOiq1eIrv_ygiCEDfdp2kqjAzHJmgTZytZaRoS6G4swR9FhvW1vBKZotdetF4i9ViSveNvM5fFYt26oqa-KmhgsTSiXpIAsDUVss9lLygNjQ7ypqupBMimNGLpRsZW4RQYIlv4ANHdTMJg8qpTL-85XcEtH_GryS7-rAY4AVnUyRAvqaiupd8gcWmjNayKVGLaT2RNAGyy1K7yffZvd9jzAWDrMxj2pj48OtkkieU4NAVsSBai64i3v64mc6V4OdM2VMN6DstPbpZSLITYKROuRYFCJXaQ_tMYazt-BiNDcCdWviuxbL0WeQe8f-O3W9AF8hn_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-R0PHbD9y8uMJFpClrsnFKKn4T43cZMK2d-AGtvz5zdZGRWzQsXqcHjX1lTbbSsEzhdKkuUz89z-LreZFwzmEi0ovmj4iAGTyOHsulbbF_xA9vPXrLIMUPx7mw2FgoeFJLV05lxmzcC4Hc5-uP9Q2ujCrjjpKPj0obqT4gpsizcUYiguNQR5e0oOPcYE-JI6ZUuZo1TO2Bk-C_EY7v36vPUTZdlHVByF7YFlXlZpQUo952ErhyYzE_ejMdRu3Ozt8hXdgrqdXm2XzSv2wHDoz6WiYD69ft1WxhbyUM3MEVVU1CWrc5_Yt-3KUXLRJyu0bPUrTqgfqraJPrRAb-HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fIPl8KRHjEsYbOSN6dEJ8Vu46TuSoYybFYIIg7DHVFm7XTnWxVbMgaUiyYFNfE0gztOsTOEtutJX57BprcYbsxjiUIjseUsD22JAQ4oIbMcT54qK7766tMxmrsRWmwhvtPWchRI61zdbTxRqYLOBrkjV_nLALleqVdMG5GLwJdoa9pPq8tE-vBmlOg9rDAdWSdINAGr5blW0zrj53AvY9t8Cx7ftF4oF9y_gzPB9vhkOB0vBWnl_6XRYtW3JFMjFnthAZboqjRPdpRXL7jMVhIfPc83yM6mxdzWcyzPqTwnSghpO85uJnQSMkwIu4hSej7QxAGqpgy0eT5FmOIvr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbWrUtxf7gGfDlx9NJvVdeDR5kQ2isFWy0MI1DwRBOnw3CUFavNE47LgqoQZCwliYLMTw3Bfo_Bs8gB4VxChrDt7iDv-PN7PMoock0LOP_ZrazCKT-f86w-ZrPT2Qc08sjW6Y91_CLFX_YQeePmUxQgf9uP_-85xvjtWUmkm2kQw4Q1PdFreKOhBjsCBKSivhjLeh3onCSPJZTDxX_U1lMUQD-vJhouCvCEqZ6K3603eragXHVgx8MAmzYgrEVezXLMDw4QtQwSqINKwgiIYhW9MtvCHBuWVRUm8ngN6_8CQOCaQbnUzIML7Rc66qsCp7275OmsBD_YmNh6fW-vIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/liPVTDbbvFK0U17k2Cj8y78LjR4WlPxgco53rU11WSfMQPEnhAeNTx3KafiL4-0GzsQ8nqkRNUY46HsKY4MunOKJ6zZH_SP3r2ACdj8l9iJ5uwfnRRRsaUaWD1cqWB6oIpm0laa4Mk-Mzm6QqV8c2Hr5JiXndedEzUEcAkLyHnKEb_LhrLILJeh4yii4nJYexuSNsJjEa23aL9YurzfEGvBmbh0lj9VDp-AEtGp86Pr0f56obgeB47Lp6dTK8CLRphEwwaeQff9hQlmlpkApHhJ8HN4Z1-FKPUzjFQ7UdUNwFLQW7zlxJCVflF5SFZqhNGab1OuFTfsQyBz8He-SOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jn_woIfmtOM2Zznk6QFMUo-Y7RDASEEfIUjpQcQCVMniVemRoABiZz48IhOdO5EcLNunRPnrRlMIFzxX5X_ONREf-kMgfhqkqPi5xDO3yAz1VNiTz740Yqz9WPyhmjL8JqFHnjZYyUHk1duua0D4k6mK33TCviY2JIGRTs7uhq8zIlyqDVMbE3ZNaEf5H_GLF_z12OaueTIVIPNDT9trJOAAaAjDHqy-xcUhrKW67hk_R0Ze63e4YS_BanVtBXCkiBn93vu-rrIUAHojdQLNjpDY4zgTT8ZJ8xWk0-k858LYgZ34nUuoPfWAkFmOo56BUVs4EP8ADnF1Dh8uuPNQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vo63MBQ_rc3ADKWzUIl0WjZETG5fEAeswUw2LKxvYtJ34Mry0Pu4jIlYAj72zryD2X8gAJ_3cUdcVd64MaBXNz6riU--TAKHQe7WC_CNl6XuuIBJ_h18Sm6Jxq0hf4wP_jpgcsomVFiofeBgrEpRyaBcH9p7eGixqKZSGhvhyLRXJUjVuY64693ltIrm5GYCO2NGX6PT_mQzcwcpObaHSB8luF2OxLksONbRDUvnY6lPc5EefX1TQbrwS_gzRmjkqTnw_RHSgVFR_YtEzeLAOyCP30S7eBzPP4isPQxkVSggClVqORujVX1t21Ulbn1UsJKzf_2Hn_x5GB0whqv3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tmeS9rZ8RMTDksD0qSYPg8I8koLPZ4lLdzaXC5ra5PpHT1aXA7JQEK_NM6txoW4PwMvA1SO4ydDMMXy0A-PJYmHnTntW1-cQbjBm977vPeED4q_0KVhdQ6eAtaX_P4E-cbDvDR-enDOYAaM-xtQr-PtZdlTk8zDxMydMw3RZtp-IzG_4i_AmqQ0HQnfpTLqpXsHnsZNFm5o0ASu6NaOZupyPKYpHNYH-d6oQU0s-eYUlFqabHY4V_cyHlSJhmALABzXmEpA1Sh0FHKaj-dMpZNtltHweuWyAps-aroDp0HzxYbvQcKN5X7Yp4ljDYzKJy86zIyEhsQLAEuAB1gdmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jFd___nNGxzY8oh2w8xhReiXJDY6Mvwfok0HCcZfYzQT3ErVp08ExHPUTlU8D2jEXRugVkUPGJ5LOdw0nI9cVe8Q905dEFkhAHEEeNBt85ZLJ1QszmDUnkzlb1fp53Nv2Zll4avMGeFT97WhZlNsYt5N8TT33v3yt1n_ftjy-UePMa4eWeMQh_H8ri6P7BzE-kow9InvKv9JsEWJs8Wu_x1SBJ2zkBUk-Zw3AIUCBYjm816f5fcLNb3QAffxbObQL7bx45N9QfNET6pPC6wFxrzMfRVYteIGTm__gEkuhLgbzaMB9fDneB-3iIWj5aZc13TnTlZKL87TxYsLpa4Msg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHxYxqe4vMN-KS9lxaltygy9O_1kuH7oaUqCwXvyMNlKYJe18hQJu2uhghJjCb-wuhLxSccWknqFHyhUklmwnloffACblC_GJiDc9aoW3V2vcdEq5b74yw0bOGTVfp52hsg3spUb5sUVSJdkgqkMkpSTneZ9wqDg2-OJFHmzeVO2Ozx2boE6ruSUcpVSQTxsMCsWur3xxWZA4MMHz42F18bUNHmS5nxVnsTHURD-nTbHe-qGR5o_SQlbTW0KOc6_1x1XNwYcfNkr3jyrNp3Ci52TdiMVQ9vsxGJuJ9pNOog1lfQNNJhrrTGt8-kH-yl8RzVReEmWt7VIAZ2y9i4Mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLl-simayaIIRTP4JE7PPQpXvUjDgbKnCfX0-UrXwJ_wOUcg-5nk-AbK_nknhtGDHijSbe9j4tixKW4nMcZTyZn9F-wwebnKDtCrc5-A7ocL2seV18IWXeTQejDvXMtwPGRNKGJWIagUXXnKThipVtPn-K6szXwXSkchIAS6G4b678-Z4MnbtEJa3Axvm-oafnVaKA8X_B6iGYMPG7q1IzlsVFerW1I5pjjIJg2uTehQMIswXPcaiKTK_CEVh8ByJFCMs2luI7sEy3Y5bqj6uqtMUR0wuWnP-q3TNSwSf4ooiA2PpTnFno9Yhab7xaEdFDucumdBeXPjR7yAjwrIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xr3ATt3zqr4sAXR5XLM4pjCMwXxuvIru3csJLgZXxAROUIAqw74ks3S0CVGpdFB3OirVf6jzO0YuEwrCUPOPtZW48BruQes-qiyjvQE8hqorOwXCfXzL4pvoPsUI3kpH98Z1tUyKtYrjAegK593xXrSjdkOpqJ5ow45tmHM3u9mpXT6AUrxj5lXJOTjSkOokDTJBXzZrDXxTR5ybvmf1uDigH6xFlV21OSUjOZr7BVsyP6gCcNGiMLVV4GUdvNbmrdxktMUNjmo4v-H01yBqCIp1-kFhFEb-ANVvNNYbzAJI9DsjcfcqjdUOZ55sfjgyFA-cb2fFgO3OeK6MlVkCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=Osz7See32PRERo_cbJM6cAOq9mCXHN9PybIyKQQyVGnnl2XGUjg30U44_074vywuoZgIO_9J0e6pEr7yzypp7NZG2GR5bguRtHqx2i-jp3n6uV9lzTyWd7y8g5yqyjuRDL7QC0BSCdaA8AneoO87_LFy7zVy9OUt4WqvgPaIs8H32j93nkxzGBRoLrn8ZnMbzwlpvWDnBZQXlNlN48hPr1M8Bkq7lzS4llGtyVfyqv66dcS3jpBjEiVUBclo-ozVwObgG3thcRGxJXh_3XOp5Sv2taTTZeJ4NA0RXKkfBJJ1q9YZ5rhrqBgGnDa1Z0FzE0RdPXBTR2N5R4gp1lh3Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=Osz7See32PRERo_cbJM6cAOq9mCXHN9PybIyKQQyVGnnl2XGUjg30U44_074vywuoZgIO_9J0e6pEr7yzypp7NZG2GR5bguRtHqx2i-jp3n6uV9lzTyWd7y8g5yqyjuRDL7QC0BSCdaA8AneoO87_LFy7zVy9OUt4WqvgPaIs8H32j93nkxzGBRoLrn8ZnMbzwlpvWDnBZQXlNlN48hPr1M8Bkq7lzS4llGtyVfyqv66dcS3jpBjEiVUBclo-ozVwObgG3thcRGxJXh_3XOp5Sv2taTTZeJ4NA0RXKkfBJJ1q9YZ5rhrqBgGnDa1Z0FzE0RdPXBTR2N5R4gp1lh3Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nN2M_x04c3cGm1gGasR1RSuZmOpM6tyoqw68pGFaOEnihc05T7JkPtfOJHkp41EKhxPP-SHy5joeCtTqqk-O2cwbI3uykI4ZAGTZaXYHHduqa_mgKs-5vwpa2LblnLFxkxc6i_iAGUlYzYHNaon_Xew1xXCd7L_4pM1Z45kFba4HJeRWwqp4xs0iFavNqJaJoc__QkPtsUBMFfhpjxjParyUHjmvb0UkjBJCjOp5riDnqsKgEs9KRGG-ho9ShVEU6LepFhlub-yzZZ0rgnR0awX7oBO0txhv_pIjZMDOBsEdtrMTwYTprQU9OfoVkm6KSO7DjBtk93brMQGawH88hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UtSepAJIYzBYhOCwZujQ5w3q-sg0tttnriGwR-N40q6vmM9wtgxm-pa2DH5CodwYCYEDsyvfG_Yr2rck3PnBJD2V0i4LGTsnNInQBVCpICQ3jrds2dJklFlDpFc5Y4Q2WRuypuk5nKaAQNje-Zr3ghXxFPG1yWnNaNSgMRLPR8phuuEi-px-sVGr1biaZy9LPtgW_WRFaTjrpHSApXksUrnYTxVx5DfbX5_YE3nBnZFyqzhgYf1AAg858_o2xLKwlt6Wt7r4TfFmQGecz3P6d9JVmU_eZRUnvYUD8AT5RYGnxy1wba_dNKDY_I9xCuhBpC129iMJHp5dr1pNhWX71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=uMhaj1zE7AXW16-2iJwYD8ndPi7uUEHF4cvUWGKWmrivpBaMSKY22yeiEMv1iclrZNCCL2W6Yxjg64yhUPCSF_DnQa6Kt9O6e-xG8CoMij4i-io_Ezxtj8R4zcs-WBrxcuFQuxlJIaWqjnJYCeE214ooWvaQ07UqoYw9nO3SMdDdfslUX6XEnogowCpBJOZw3DHTUC0hAioWy9DuI5Eg9gm5rQJsKqCWPVZeKdmWDBmG4mrc9CuXCQgROfAeO101Oj-a8NwRuWc8bvVcsLFvnvcWuIOv9Z_IcRQhz5tsvMyuReOSwssypx_pOFp7o5Qhrg_PKfnkvTRhxBrmY9cFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=uMhaj1zE7AXW16-2iJwYD8ndPi7uUEHF4cvUWGKWmrivpBaMSKY22yeiEMv1iclrZNCCL2W6Yxjg64yhUPCSF_DnQa6Kt9O6e-xG8CoMij4i-io_Ezxtj8R4zcs-WBrxcuFQuxlJIaWqjnJYCeE214ooWvaQ07UqoYw9nO3SMdDdfslUX6XEnogowCpBJOZw3DHTUC0hAioWy9DuI5Eg9gm5rQJsKqCWPVZeKdmWDBmG4mrc9CuXCQgROfAeO101Oj-a8NwRuWc8bvVcsLFvnvcWuIOv9Z_IcRQhz5tsvMyuReOSwssypx_pOFp7o5Qhrg_PKfnkvTRhxBrmY9cFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iN_3UgjGIMvxJ5pR2Ncfd3rbixczEaf7oEBD99i-zZxMKm6J3NYl4rbJIk_h7uBNaFTloS-rwYn4NUgHt9RZOb4xJH5s1fImlonagj81rSxKKjPjpehQh6WaXletqdUIYZiRBh_OTveYTtFxhMPwwMp-2HyjDZK46JnycnHOcsBola_gQKMbcx4OPp3f2Nmqp6psoe_Y_qFuKM9X73blw25tUgMncELZRKCvcsEWqMNIU0wnmYadkVEeJHUs4CnclPxa5fvv0eGZg5UjmR_tqTJm66RepykUEeQ8OeW4GotTpQOwX7T70Yx9sYxANyaT7LGUFbtM__7eWNGvHH5Cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIdScVCk3Apn_I_xBKuTKkBlKF8yzQBqwMwwV_F0536VW3Ut9SY1RUp2UfHdlP1EvPOIWoZ_F34KiwkpgnVLLSOyJJVhM8hfAMz_zMhG8vP7JFu5vvd3rByGwg2BL6PChATtxycLXuBfLHvzpEiJcEEQRIxDX3EelAbs6lZeDkYrCGTxhmFe6j1EcxSySpZ2lsObxLQ8Q3_gdV6Od4fw1n5MFFhLj8iWuwOO35nvY3pWs1BmVOJXns8PdOhCvu-soj9Bc_WwihGX5U_kokJI2yJkwWQqH60HSj5RTPRcNfTIIC85WoPn1JZJoIH4O-t2yY6ip5RI4F2lXSQ65Db8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V8umPvM-CC7VGfLIOMVR9IT5YIsTlaWKNFes_poVRXgwkk2KaMOSTabVLeV8YfUn5aeb1AuUktE9Sv3jf6e4xd3TG9nkwJox18Uw609PUg6O0GseVSOIeWJ0TkjpavYnW41PS76Fd9IlznZtEayJk9Ue-WOtVR2fMjlJwimn77l13R4eJhTp9c9kcfo0fMZEYdc8xJM37RkiwpW9-nOgjUaSiUcryWYchJ7lKvfMWr7azfy5skPO0JmZlKUwTTbMHnYab6ei7sZG2hjWusZWfFSi92fNDuzmo7hSKtr2kydFAEXNaoyICmYEe5ABSMFOn9c6SjWgWUfJc1ucjBz-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TSfEJUrDw3su5YbrqQRftUkw22QTrsuIhsSX_X44ROxRvNN2Sws4Vsht8_On7O3Awi1jZN3ZnbnCYHkTwiQwsfa2q7mD-5J1f9VoWdGa_dTd3DGeYy_JhAmiifpPxkeMznznIi119DFNUiLwyLSarER12hcZSRCRrSCYbBBMKbDWUQaTabEYj2v6eCTf_1YuFpFPQbwdfGNcHzOD3D6tCIMHh9s22CTXSz2Jrf_jMD_z8TYBaczEimKanXwCSIsGqKnDTaVag_-t6yixONPkqe6sSIacE9XuPNDFQru1KzT85GHy1zm47Y-ginZn17WsHdzfixEzy0ssRorL-R2cDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Th2SYdczqIZrIhYaAONPKxyZim25dR5vvNKJ6Zsbvb6-eURfW03oBNtscLFHNbGXQiNXoENhe5ty65nxUa88asqU2SWP5RWMgveaPK7DJIhCRrHbqmkJgC9v5zFfspfD457jS2GlZrcyq7VSTR7DUgIdi7eQ-dJvK6AWj93Y4GebHwMjH3EFvBnXk87EfPxOMNoMYHPjqLEWJ-MWmQj9FskAqCn-mjKEqXEl4ryX-uxk7cLa98OqJUSFLGoWzNeeMjYBRVU5aO__HSFTKWWXxhvPIRoha2HRmLPAE-SprwN0gVHUepfJYJLjZA5O6GAa1WEclxe-TjM_D1grsDuPPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fa8sGvtyNV666bC-SEnnDpmx2ns0VHg8VHLfuxfibE06tGjWuKuruKzs2d7mqk2UEsCwX7t_zI3i1t9pXC-moUKn68kMPh6AAHl4xsuJC8FbUGAfO6xpopnLGm7S4DXQjMd5NI-MO1AwTE8L1fdw470wJBNCrQlj5nn810pKAdNDjrHi-U__N6HEZBWEjOurfuiiuHD93yJJmyrJ5T5OgxvmHc8oDqQHkMTFc-dhE4D5RMPX3eE-STBoveUjERzMrfaFqkY5w-Wc83Jfbm9PVPBrRVqQpDWM_jEYMC_7eZlKXGY5_-REQzLOwYUuYuslF6fFK2MY2YrtYH1UNQyQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mHgB7Q-CuR7GzlAQjSIDjbfDqxgNdtf9PD-QAY3CD9lEpHq0ukrbB12kZGu_BA8l99A4OpL1lM5VyCSvPrM4AbtYBxqeHvRuC8liNA4BTYHyN2rRHscjxIdfT-siyxRJJEfeuWxp2XUMviLAe6tiCsESrYQeOJgoJqhLFR4M6JNA6aKPDoMYE_hbXRKF2HZTzZOVjI7DmGF71RgQTtKkxE6wvyhv9EsDk--LR2PO9olCQWdmbWxzQRx7PH0dNC6ZkB7g723Weob9gLxjoPE5CQIXIZdJyb0oaTMjHJO0P53rN_VXuItAB2MEpBdgHJsVAP1EoX6XRDrGyXX-ujKWyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=rCrxk6E7krWwVP24QDCgRKJuB7W632NxuFBhtEuyhpWdzw2BIQCd7hcZod6gL7kWbCwE3MxMPWRVNqhUFFl6bp7r0tGfbJBbCbL10VmW-oyg7CYhzRsSAFuiZUTQ_r1NM7-laoCBQiLaBYf07gchvsP99zeAE6exA0lr2gVLtu7GOsTV7FlP9kPlWatsbXtEYROjEfteJs3PGrV70VrdfYhVGVRoMLLql6hDCy5nLkXG1ThgDSxVitiV966jHVl5R5MQEuHbXU64-0sFb6EeN8S8xVM9KN3LzI0aHfgL8JSoPiLutxP3JjJMN-aEVDLaZhtv7qMPOsEx0Mu_3tB23A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=rCrxk6E7krWwVP24QDCgRKJuB7W632NxuFBhtEuyhpWdzw2BIQCd7hcZod6gL7kWbCwE3MxMPWRVNqhUFFl6bp7r0tGfbJBbCbL10VmW-oyg7CYhzRsSAFuiZUTQ_r1NM7-laoCBQiLaBYf07gchvsP99zeAE6exA0lr2gVLtu7GOsTV7FlP9kPlWatsbXtEYROjEfteJs3PGrV70VrdfYhVGVRoMLLql6hDCy5nLkXG1ThgDSxVitiV966jHVl5R5MQEuHbXU64-0sFb6EeN8S8xVM9KN3LzI0aHfgL8JSoPiLutxP3JjJMN-aEVDLaZhtv7qMPOsEx0Mu_3tB23A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vaUmMlD0B45bcBwqTodRMWP4x_eOXP7i6riP8bi-wc7LEZwv077SqQOslK7XeMXuBbpncYq6PubjedXeFeGztwsuXPnt4BMEkpoKqKVCJiCB9SuIUnsjonNLKCVJHTkAlG4pDwr197depo107PrWHFOxKDl5HPYl8ZuUIDIN8FbMPBiIw9R4AtrPaagCWOUnFkKK3MVuL4PuEa0hD_ArS8wwqrpEZXgnZd3r448aeqm2ra3T8Rv6M7v26HrbbzqVloja3losiPdXvPoGPMmIkKQVXwzA6Zdlb4z7Vj4Gw0zxOqF_Jbpry06gAls4b1GjUhSunmaV1-iDxtPDQKJU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxZpw2Kt-LdIpuIALa5f54P_3GtNk7owBdN2imlGWLxy5_ON872F6KiJZKGxdXXsCcPt9w5UwuEV5NKgUzL5L5MkYXBaioN-fGSMNdh582QSm7PLvAO8kDjyfvvAd-n8F4mHN8jFLzYdjqD3pQGc6cRT3SYWdNPeuweC-bTBfW_Gvu3eEVZepUe15jETg0k7yjRbK--j_FelUy3nZ5U6GUXLMP1Ld0VPWfc4Qq1Se5iBiEf2lbHN-qAgtUtdxxuIK1FrIjLZKhyprSwjUthMTP6f269G78LaLY-pG5mVZ22x9LneQFrb-i3KhdM0AOBi9y49taH5VUYJYtWCacbUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2cMZZwR8qhiRFzKSUCT3rkEEiBfwPZUVFpaOqaEanxge7aOXKBPVpLo0cWBDwsAL3FdVHPRse1-tThqS7N2TtIQMw4ivRSclOXoej9JzISWpeUy7koHRGX2WT_l2eaTY5KozYMoU2WBHbcCKuzvCcQmxFgI8lErrd5j81xK1RdVI2S7_yV86VlBnclNGEPGddOhDvHiHLaYfkggQan_ZrxhpUl0oLLz825xnDK4kwuAKMFwO-KPg98Szkm3zytyhLUYRtogTUdErGBeP0qVREfCWhTINrz2xJrlwC41OcAVZv2vmQmS72raRahWv3BW87xH1YT9pBHpVdLUmRqdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTGTppG3CgPHd99WsdEvy15DeB6JVrKMlgtAhGMWpTZLBov3Oj3lKQvY8UMe_7Nqas7SonjOVG-Tr-CUtBu1WAdgkjSPRXM_PEcciwt26XoNKmNTi_56KrAY2R1lNPZ9qQuyfWwHAIdmuRI2sDl5Ze-_gsbsTjFeqi59H7odEOISRKVAjh4eDUhxlGSiXU6aFm0GMUm-JIkBtfwZn11XBLRm9CILOKpN9pEDeJQ4p3jecSXnrcpm8AXpmDxMsq7D35QXCBbJgy1w3jMFtJVtj96Q2_AQcTrq1Y-W_7rvIPgLCQrpzJWv-S-_6YEsmT23l4JuWgM27kh8ZNRn0fcmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mm-E7hh2b2WIFa9P718yTVoQTCuDvNFHyHothvrrRZFgobQVXqVncwfeurjvmnqxJgvhrsIL5rg3VGTBdeWOttqm4HNVGosjFYXV-Knby-e71kXZo4nhmwAGpnTqAgCGH4qpbtLyaMtvqvOvMV6eqbRyp8cUwlZAAAAj39NAeA5ktts-yXAcmzyE46NDoCa_FcKAcYTS06UYaO8NwGs1x5XMMIOmvxq3nTFq79l6YvMlXvtoM7DSyu4LG1NrMNkZsW4489i2tqQPQm27az2bu-avp7USf2YcrB7L52iPj2Z5WBgOtrr7FIJwBki5ej4EKanFMMNmq0OpJz3iVKZAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pv8je2fj7a1Dfy9W89C7jDGzh2iktcmcn9NQ7ZQY4GdugbBuWUYb3f5lkX7TYrtJdFltK3pkKdpv1m71QxGyQdKE8DePo3GaX_ZYOZMCidOVFsPAYECr2cjIoJRmC4oBMylULWEjNRDqgU3h-mNcfTyiZAqREv4PzoqIliGZEsyPqEgB_2toJFjRFifz78LN-xJH89R4o80zcvVzyl37YoptAPnzKRIgzqi3PosFnY16n4i9iM5u5CrKvSncuKZjc5-smU0uoCr29p5fReUDGdBk6y_WTerj_ch-e4mP0J50CZ30EcOnp5nQdTgIZntI3MQ2KuZMLNNi-gWj-zDdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNBahzxMK01cvIgsdso1sc79ecHjiGHTs9oebir7whc13SpXYmq0SQOXSlwxrrAbrxvkbRA9TdmAk9UqdP4oIWmExQy5vKeGlhe280RfgNVfXlIv13Y2OnI-jpUPBr57jvFfkgb7ZeRNbxCgU2WWhzZq1orD6we14aZa0t28OJA_3P0rFZSamoegYY7BnCWbKaUpCs5-DRsRPmpxUXqy4_EeBOtFJ_zq4bctga0hjCkCLrBbzCuOmmer486ItCiNTUE82MdF4x7exhUcszlX5ZiDUrYIpIecg-K0x1zzvq_C0-xSanLTclQScB7-eMhKEjoMlDtZ62vuNTQXTYKDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzNa-mImBsU-DexFkgH6czjt345_FZamprwTotXcryvFaVokt19a9RtC2IEZbn5wrf6UulwmgdZKCvnWXLsFmwL7W_dyXOZ1Z3cKliHUsaRKTDf5GcmTfVu_c02j2Z97BRo2xk-ln_hGjkg28zjzh8f-N4mo-cCHANu2wT2Lfk6cBAhdSNafeJ5JQNzwrEk4nV5vv9rHjFQGKVlvH2cv5PMPxiCyzXKxsCciGXFH7gl9Ai6sK1dAnnhWkx8FvMup1kj8qyo43HrcN-xEmAermfPpCiFnqIIhOyGNqdCVHTSNiME3_XwRJ_w8j2YnTibWUR9qkZ2cTWSrzTfpAZJDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-vfwwbF8ht6OibKy94wExQ15hXxfHQIzss21jfoIzNBLhDZm65a45n3_fCBPut2Wjp_BdsS7wIY3kRahdnUBTm93H1vuZ3Tb6OfUKMBTB8u9hMO5yNOkg-SujIpzdM62NFco4PJwBO4QU8dGgMyhTneHhdi_HS0Dyc8slChcD2T82XWHLvBj8SJMZgyk-8VYVhSF6O9CiJ_SgLNk-eC1LrSF7_gfECNs-gSIJVvL46_rdeoR3GiYtWWTl9DfeayZIPZhw2LYuIPUnmGo2BxodJpUElRwHMbEp8Zb01rx7FYAUBLO-d94sLPqyvXTV9R2pTeRDcye8CLwEcUMYHgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=HwlF3D1OQIWKgALxn7q2YLpsPV0Pj4VrEyYKnwZ9Tu9CibpZ5QFFNK049nkHVMpjteFqLr1bNaSA7QK--84BDFC9lprhNMU5ft_zsAGW1OeD1p-DUc_WaQMsmuK1-vE6EMQ0Ir_dDMIBE6nZEkslo1GFuVkz_6vQDSnyeFRm9E1WE42y6I90WXUmgpNs_hxP0W-_WJJNDPk6hMblUj68kESp3ef_1N0rnn00dqgOzbUWddX9kSrNrVXZPv9sImhg81g47wm0sEcjZl3o2LBmamV_jDi27SyS8KQp9C5VYVM_H6oYTLTLUH25Xjy03bOcQYVQFsL1QgHt-PWuR-ONgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=HwlF3D1OQIWKgALxn7q2YLpsPV0Pj4VrEyYKnwZ9Tu9CibpZ5QFFNK049nkHVMpjteFqLr1bNaSA7QK--84BDFC9lprhNMU5ft_zsAGW1OeD1p-DUc_WaQMsmuK1-vE6EMQ0Ir_dDMIBE6nZEkslo1GFuVkz_6vQDSnyeFRm9E1WE42y6I90WXUmgpNs_hxP0W-_WJJNDPk6hMblUj68kESp3ef_1N0rnn00dqgOzbUWddX9kSrNrVXZPv9sImhg81g47wm0sEcjZl3o2LBmamV_jDi27SyS8KQp9C5VYVM_H6oYTLTLUH25Xjy03bOcQYVQFsL1QgHt-PWuR-ONgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
