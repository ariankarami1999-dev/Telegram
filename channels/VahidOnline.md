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
<img src="https://cdn1.telesco.pe/file/cK_1IPQgnb8RIQdiZaGcAsZcOB4c2nkdkT3inUgAu9xqBxFliDbaDAsJGf5m8t2UhZLMHuKbSJlW3LjePJExrW9VqsKX2LBB1iNtmaqor_Ofd-7qyjiYXBxemR9nvN3uqNxQ5CR4kRgr7nIEA7aY2l0n8tmGuBbNKNzxStTa49LMT03aRQTWB59MKyJ3ysI-o1rs_2f8-ahXEbfoZwCrkmhqvJbUrPPwHqoQN7Ukx8wDPbND8Rg8AKYYlFKU7795cqBkS2W5Xo-Ch5926sh_vbRRl2GwuoK87d9aHOwpqsccN2Rz5URgeft46iY0jpbJsSEw0ZCAj4ZKdQgwZstgNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.38M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h8K57T34QV3RbQ5ZYLPGLbl5-p87W0y65Yp4zh8o49bbsmNI3F6ct2_ySdZmJIMWsTAZ863kEWUWXVtg8kgBm-cvojWlnqkZUFOTts9j7p2rB5JPYD_1hC1I-M0lpyOKhAo9WLYLK0J48I14PYWNp66ezKMP2Ffvg4Cgco8hFa1C0Ltz4f6AW7aTvFmI3BESBPy_C69XukUkVP4CuoM0qKQNAjY6pnJ6E_KImoehcC5OtX2A24TOdFYt5YhPTBBz5JFzUMkPG7WfsKNJ2A4Y0LmvauaigaRsnbK96OVOdjClBqz3IvvZ_6c58flPqxcF9fbUJ-ATxihdZOzt050cDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sk3YVkPpyd4iuzFL613yYOa9kGZorLkY__UiUkJTymqF85Z1ioby9WYiloU1fFORP-z8i08l4I1Q95ptiASIS1ZHCgbEt5OtPsxd7uwmL57fPu9spsGC-rtYwSXXXo0KAXCy0LdGmf_hXDRV7ABIanhTHfTxwZLMYFilo6-dL4fT1-m8SBdcit-S_fKbjIKb-kLPTEK41eZvdfRXzAWXQh4T9B78tmD9Xmun3Y4oY2I5RhvnLxO87mBJiies3iHD0C9L5sOpLJm_hIcdFAoQLZNxmG73-CcI7zNuE878uS2qaZKQnD1HcXJsT-Zd7oXwVY8SWI1qoGBKNrQFqHaSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eawiXtIbkbyE_7n9G7RqiiTWd1pFuOCobvVeZOGSODtFgfS5-3mOISf4qDaHU0N2n0uTRegs3TSK-m40Uj33jeZg5fpBnLZdKWXvxkgrOeoDajUomPIOEBih-1vlI2f7jhu_wVKIVcYi9kePeZjdnKJTpobukrsH4fC70JUvY1j_TxJIHrteH6ClZ6eIxNmhnOD04K2A569T5jEr_fszsRl4isoB-w_yzCmVuzd2NVHrlvhWjaJx2RSjn2ohiEoMnaiLxUWVOMJoIJeFQq7L__VU4gRj24Xnns3sd_xKi5rPtEclZ6tnSfSGwwfsJ0EroI2iI6jG-eFoBRAb6sJqcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/VahidOnline/77117" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGCo4bjZx-MRHuD-Frxf4xzhrrymcAYFxdIM2C-Jq_lJEFzzF5hO1HusL_TaN3beCccXvoHHLk82_Q2uZJJXowOXJwV_i4izBZWRTJ9WyZqSaPucQh7t8xkoQoCDFiGLFFpY7Z_hTq_NvPYa7M2kk05Odm3nf9tlnEcEb9espPm8Xtyc8u2QwBVaUcBhOCRGTzqpc1f0xL8e16SoYcpf7IIVl4IDGQbyGb9k69GVGClTUeXVD-DrQJR3hA8G7c65KpkYf-t0ZV68qkEODoA4T9VTwH-as7rcrlGHxDUJFNKbauUB1pLtioY-gMaJ54rAvu1FC-fawvIhH7g-SCtxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران مدعی شده‌اند که نیروهای آمریکایی در ۱۴ ژوئیه یک تأسیسات غیرنظامی ذخیره‌سازی گندم در هویزه را هدف قرار داده‌اند. این ادعا نادرست است.
✅
واقعیت: نیروهای آمریکایی در ۱۴ ژوئیه اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. هم‌زمان، ایران غیرنظامیان بی‌گناهِ در حال عبور از تنگه و همچنین غیرنظامیان در کشورهای همسایه خلیج فارس را هدف قرار داده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/77116" target="_blank">📅 19:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYVwaqfZgfWcu2diIiFuPanQll9Csku6H8rXOkI00LV4173sSiijokDaEvFuPOuumM5eVIyU59-TzSZ3CWR_p8kmeIvEBPnv8LnfnLxl7NAkOC0V4y5qWLNy3yxQY469MAqpE81hggKIjo-J1zXmlgfUQoDoBuJQoEAYVqcTlMEmM_RX_fHz1G2PPd3vKjgifVHD1MXcUYzvZix5j1k8bZVhT8kwWeyElTIkb27UtRUT4zUTgKPqtZS4mXtZd7FHke2MSh3IdLDN81iyG5gZcdeMQJ5cjId4-tVIIM1KT6VKnSmhZCrH0zSuxWegmu0T0jpwlH648z69TrwG5-Xz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GIwxk437djYB7no_3DTblXH474XMymU5nomnfY6IpmsJyyYDBxvdRzjrGZ9Ebog-M-YhURn_ZAWtjPo1UGokj_JczRX1vovrK97UuoZQzCh1WP_pCFp1om6RShAQ7-t-dZISpiA_Aq02FQCJ57jcrxZqRnzuHYREQdvgFV16P_RznFx_PD74YIZ6fUpTMZ_NP2B-jB7Hw4SYYV39Lkw66nlFV5ZSEJLdfNtlcxx-HvCSZSsu4ku51zfPLBTwIyd-hIvXQ3j0csan1tsF-PJ7m_K0eFsNJJG3xA_gIiHwcXwaj9IOwfWfVZwWxB1bZKT6BDIhGLEnFdxWPpO7FGCsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GIwxk437djYB7no_3DTblXH474XMymU5nomnfY6IpmsJyyYDBxvdRzjrGZ9Ebog-M-YhURn_ZAWtjPo1UGokj_JczRX1vovrK97UuoZQzCh1WP_pCFp1om6RShAQ7-t-dZISpiA_Aq02FQCJ57jcrxZqRnzuHYREQdvgFV16P_RznFx_PD74YIZ6fUpTMZ_NP2B-jB7Hw4SYYV39Lkw66nlFV5ZSEJLdfNtlcxx-HvCSZSsu4ku51zfPLBTwIyd-hIvXQ3j0csan1tsF-PJ7m_K0eFsNJJG3xA_gIiHwcXwaj9IOwfWfVZwWxB1bZKT6BDIhGLEnFdxWPpO7FGCsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77114" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱۷:۳۸
[جزیره] هنگام، الان صدای ۲ تا انفجار بزرگ اومد سمت وسط جزیره
جزیره هنگام رو همین چند دقیقه پیش دوبار زدن
📡
@VahidOnline
🔄
ساعت ۱۸:۳۹ خبرگزاری مهر
:</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77113" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0AEOyvTIfZBpr9wTfoM4ci7GAMOqsiDbptduEaOTL_0d0H93unLKQnQlRhttOb7JfiofdTK8GmAZ1FajpvhuMuzBUahtVJMVlLTAJZgwZ6_t2dBtvqdaEAHrKQSW4fcjB0jyu4qtWXdve8mA6b6fNcKMtcn-YTBjYTC58RgiS1WOYN59xQO-jy6utX5afLAqWI9CqZ6TecFrTbX68-MrH0ILuCAm0GF5IYojMvmjwAeIGW04eud4F-jQYCTPbUmla_XHdSKVcknFA1Nc-aC3UBY6xHbN85-v-2e2Js8XVbYrK6lQL3zLUJRtTGkCdhFkNdgTgPKbVyWyNbRmQfxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/op24aoc77GhOIdNNmBrq5h7UlFDa3YkTZzdLI13XNMxWb_M5bOP0G83Dn0qlmTiuPPXnm2ETPakJKslaY9sUeKd9o7o2yFb-RXDOvzmw4WKos-6kJW3y1UaA0oo3-h4rANLYysYoakXenV-5ud9Je5iKiYxxVvmlJ93pUF1qf3r37EOxoxEANQdOxmAw8_gTZju3zIUONo5oBtR8niHhbSRL5zRQVXcSPqttS_YXMXWI1bNTmG0r89eQaSJAHBvRf76TCQQjDpCnjSzu1mhGtK5_-xO2DdcrIMtRKajE2ufVs0pGBLMWoIMirwhfn0JQ7gNmq7d2eaLmpZRiKbWtrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بیانیه فرماندهی مرکزی ایالات متحده (سنتکام) آمده است: از زمان ازسرگیری محاصره دریایی بنادر ایران، ۱۷ ساعت پیش، نیروهای ایالات متحده مسیر حرکت دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند.
@
VahidHeadline
صدا و سیما چهارشنبه ۲۴ تیرماه گزارش داد که در ۲۴ ساعت گذشته دست‌کم دو کشتی که به گفته این رسانه قصد داشتند بدون هماهنگی با ایران و به‌صورت غیرقانونی از تنگه هرمز عبور کنند، پس از بی‌توجهی به هشدارهای اولیه، با شلیک اخطار نیروی دریایی سپاه پاسداران متوقف شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77111" target="_blank">📅 17:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ECT7pD7AcWyBVABi4ARfZk9TYjonuDjFW9lv8xglfowqgAMEyndDSvhElWTMFYifUvJ6MfWiagoqGJDpMlhQaFR0lullylKpN4e9HcNSra17BhvpDUFYZA_r44ImZOipEEBpIWIVkV7XGV4frYvFWJfUs5oWJJXlwbngtVSmKpl9ki5n7mgvNQqXnQlcc_Am12fZnxBR0TqsW_qJ9CDaVOnCOKhZvP3f7c1Lz0qdccx6kYJsHu52mJzYSgePaOIqIxHnUMKX-PIY66rgPwSEZNR3EnsfdKmtHiVLwU5ROo_-_zHQkVM7tRi1-3lRjdbeJNcr24PvqfdgIR6DVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده کریگ فورمن، شهروند بریتانیایی زندانی در ایران، روز چهارشنبه ۲۴ تیر اعلام کردند که او در زندان اوین به دلیل انجام مصاحبه با رسانه‌های خارجی، به دو سال حبس اضافی محکوم شده است.
کریگ فورمن و همسرش، لیندزی فورمن، در جریان سفر زمینی با موتورسیکلت از اروپا به استرالیا، در ایران بازداشت شدند. این زوج اسفندماه سال گذشته از سوی دادگاه انقلاب به اتهام جاسوسی هر کدام به ۱۰ سال زندان محکوم شدند؛ اتهامی که همواره آن را رد کرده‌اند. مقام‌های جمهوری اسلامی نیز تاکنون هیچ مدرکی برای اثبات این اتهام به‌صورت عمومی منتشر نکرده‌اند.
پیش‌تر وب‌سایت حقوق بشری هرانا گزارش داده بود که  این زوج ۵۳ ساله در اعتراض به رد درخواست تبرئه و جلوگیری از آزادی و بازگشت به بریتانیا، اعتصاب غذا کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77110" target="_blank">📅 16:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mfjGOSFXoIsnFn8BkloqwehwSU0u-N36Ih9ohWefvo82FlqvtXcscQDp25g6lBfjp1Ai6Lp2clk2RfPJ1bKodxBXt8lBE-AqEzb1hNEyWuZIMHwpTpSPoDffsnWExvQqOK_dRoU040fJRAo1hYWhgoX0QTgfILFBEysaNotF8E6PPo7NBqnHzqynOKDWEzOQEMDBOWzGju4CU5lYtNLO6yqAhX68MULt4V3FZ7ovSv59XFq5rFO8quwSbLqSXpzbHN6Iv8Rv4j46W7ox00AmJW-IK-ofmfWBJ4hvGmOrDW-ltw9-koJyiPGaOVMEEbiT9GcuFGTKnHRrPcRpUNABvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77109" target="_blank">📅 15:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=hy6AisJeZIEfPBMXIlIDTpEiDP3__-bvdt5RrjzHRQNXDQox11h4DLg6GpEx2GMySyZNWMX6ghGykXssZ5eVZOommWIE72s-tcOSY-G01P1_W2TeWnAYlfPmpiZkx2qsLhURyZoQmlDtR1GG7eVixmWBgRa5W8ot-iI3s_vERIRtoGAxX-Mv9Ahac0966nMJWqEcQ7qIMQDABA3CnfJ2201SxfP-iMG3ItTJadxT6V-dvHMrT0Wo4t7D97c1g6fVGLS7omR5LWd9XQef9XcTVQxc-x1O84XocTqWUBpd0U6oBr2XQu8Cg5NIaoNGdeXZ3-phpzFRfE3uJQz7WJfPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=hy6AisJeZIEfPBMXIlIDTpEiDP3__-bvdt5RrjzHRQNXDQox11h4DLg6GpEx2GMySyZNWMX6ghGykXssZ5eVZOommWIE72s-tcOSY-G01P1_W2TeWnAYlfPmpiZkx2qsLhURyZoQmlDtR1GG7eVixmWBgRa5W8ot-iI3s_vERIRtoGAxX-Mv9Ahac0966nMJWqEcQ7qIMQDABA3CnfJ2201SxfP-iMG3ItTJadxT6V-dvHMrT0Wo4t7D97c1g6fVGLS7omR5LWd9XQef9XcTVQxc-x1O84XocTqWUBpd0U6oBr2XQu8Cg5NIaoNGdeXZ3-phpzFRfE3uJQz7WJfPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از دکل مخابراتی بندرعباس پس از حملات نیمه‌شب سه‌شنبه و بامداد چهارشنبه آمریکا در صبح چهارشنبه ۲۴ تیرماه در شبکه‌های اجتماعی و رسانه‌های داخلی ایران منتشر شده است.
بر اساس این تصاویر، بخشی از تاسیسات مخابراتی در این منطقه آسیب دیده، اما هنوز جزئیات رسمی درباره میزان خسارات، اختلالات احتمالی ارتباطی یا هدف دقیق این حمله اعلام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77108" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77107">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=CNmTkw9Kf0vK58eECeDCWk9aoFqhQLerdu9cp3jdVI_Lfd8O3c6aVzmYiUp2xlq_c_f-UA5oeBjT60pd7WKVE0ZJrDD6sZ4x2x-ws1jsdwHDNUHYDGWQfGLPqiq6rOjQzntid5hOwPp-iYAF0DfrSnbr0Bg79pKAe5RsvNVjY8uV5JGur2DakQBCHNFtYE8E0KL3u1yWokhe_6jXyne1l1tY2IDVtmeD3AzBe20q5zZX3_Gu-VGXvasGvMxDyD2_ci-kngrV7JDtwjIU_uTobxHbkpnBBHVJfKxk95KtGvJVY4Pe3IMA8rBnaPoMM_PRMDxxx9beuXURqAYBwhTwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=CNmTkw9Kf0vK58eECeDCWk9aoFqhQLerdu9cp3jdVI_Lfd8O3c6aVzmYiUp2xlq_c_f-UA5oeBjT60pd7WKVE0ZJrDD6sZ4x2x-ws1jsdwHDNUHYDGWQfGLPqiq6rOjQzntid5hOwPp-iYAF0DfrSnbr0Bg79pKAe5RsvNVjY8uV5JGur2DakQBCHNFtYE8E0KL3u1yWokhe_6jXyne1l1tY2IDVtmeD3AzBe20q5zZX3_Gu-VGXvasGvMxDyD2_ci-kngrV7JDtwjIU_uTobxHbkpnBBHVJfKxk95KtGvJVY4Pe3IMA8rBnaPoMM_PRMDxxx9beuXURqAYBwhTwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام دور تازه‌ای از حملات صبحگاهی علیه ایران انجام داد
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دوری از حملات صبحگاهی علیه ایران را ساعت ۷:۳۰ صبح به وقت شرق آمریکا در ۱۵ ژوئیه به پایان رساند.
سنتکام در جریان این موج ۹۰ دقیقه‌ای، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد. این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77107" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G38pX8WbRQXOc6BmNpW979b5Dq0vXD4aGztfMEcxkkI4Wy0CN7AkhKnL_94Xr6d5Kyt-eo9YifazE-LfUk9HJUEwZS45NpBy9sSuS6X2RXADbo7n2Xq_qlWHZxS5pd-ULQ1cs2wOiFZU6IivDknmpL3Bjy6hUdmNf_OVmhCacmZmVnMoy5sLSS5YbpQ659L-xyQFvUUBMdiEC7gCvSke9PdYpucT1PLZdTBjYPzcMIs81Q8pUN5AszYOJkYog-6VDFPwaYZqb2nX-36EdHSVlZ0xhb8BznXPHuciCMyENJI1fhDzPUmaenDEhxyLvQzADZUVezU2J-NhfmrxJTR0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپیده ابطحی، مستندساز، تدوین‌گر سینما و از اعضای خانه سینما، صبح امروز، چهارشنبه ۲۴ تیرماه ۱۴۰۵، با یورش ماموران امنیتی به منزلش بازداشت شد.
خواهر او با انتشار مطلبی در صفحه اینستاگرام خود از بازداشت این مستندساز خبر داد و نوشت که مأموران امنیتی علاوه بر بازداشت سپیده ابطحی، تعدادی از وسایل الکترونیکی شخصی او را نیز با خود برده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77106" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77105">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwhvyUjbhp0ObGIU8Xt7rRl_0PBmq9VjrazmXkWLQTezMj0xlTdttww-sCP107axm56alzsnc386FTjpB03Cepvwm3apd77AuAkYk1HUXPoOfmLgvOhBUDFPV7NsZ6MaF2wYtVdx5nu4wYbsYkQL_6wM1wlkpb77XxEAPemeSUIho5XSsXwbO2MzFgj_l_uocKFRKy5bN3Gri7lnR_VLsqBEOfAjyxHG1DjncjUrKd4f7cUfPCr8CQDf2QqCveqhQlrp_2zKxT6R7Gjjz0GCXKPdYqUaA-sSO_Pfl4Ku3EVT_rCZ2uDvb_27U2BvTGN0MHsSXxzItNkJRy-jWfixAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای هر دلار آمریکا در بازار آزاد ایران با افزایش سه هزار تومانی نسبت به روز گذشته، از ۱۸۷ هزار تومان فراتر رفت.
براساس اعلام سایت‌ها و کانال‌های اطلاع‌رسانی طلا و ارز، قیمت هر پوند بریتانیا به بیش از ۲۵۰ هزار تومان و هر درهم امارات به بالای ۵۰ هزار تومان رسیده است.
برهمین اساس بهای هر سکه بهار آزادی طرح جدید با افزایش چهار میلیون تومانی، بیش از ۱۸۴ میلیون تومان قیمت‌گذاری شده است.
این رشد هم‌زمان با تشدید تازه جنگ و بازگشت محاصره دریایی آمریکا بر بنادر جمهوری اسلامی رخ داده که نگرانی از افت بیشتر صادرات نفت و درآمد ارزی کشور را تشدید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77105" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmlPISZV0ZOQyzYRQG1tY94nkGW5dUE6Rw-mVBqVmFCzaglAU680Pq9N2s--U9aMXrNMhf2z1UzzWmTTl3ETd_GNDGMMTrqgtQjUwTDPQsqEIJymZNjDPusw2gvxvyeoijtFGQJCscKtzxUYlDjcLFbTtdR-eX_hf8vNI0ANvgsll6EBZqpwMP7DNj8YtGnWt2zjWqCW9wSOaWUBg0yTnTum0-ng4JHlbR9zv_A6GAdCLEMr-4qIsyWxAjNgGemCLk4JbqzHYvK-yTipEHRD8Ua1PgOtLIFuWSXn20D4I-68QxCs-2AXYT5yVLnmM5FS6D2PHOJF6NFYePCgwhsWxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک زن ۳۱ ساله به نام پروین الله‌دینی بامداد ۱۶ تیرماه در محله هشت‌بنگله شهرستان مسجدسلیمان به ضرب گلوله کشته شد.
متهم که از آشنایان او بوده، پس از ورود اجباری به منزل، مقابل چشمان دختر ۱۲ ساله مقتول به او شلیک کرده است.
عامل این قتل مردی به نام جهانگیر معرفی شده که پیش‌تر بارها از پروین الله‌دینی درخواست ازدواج کرده بود. گزارش‌ها حاکی است که او پس از شکستن درِ خانه، با یک قبضه هفت‌تیر وارد منزل شد و زن جوان را هدف گلوله قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77104" target="_blank">📅 15:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpSt4Wh66Bo6h3ukFmn_BARhf9sz1xTXxEW-izSc9Osz7JJrTWkZPh9JRkGKPm-SR5lsfY7oGhgbDwo-AzUl4QUWYCspdrJhlORmA8M8a_BuEGBNJS7H_LBgSKQAgBERkoEB5U_bn79CAt1CbNgFatFPvA1rPbMlkmxGQuaeKhuHifHNLqcjlBzfruNf9jHg6LGdGUti0VTymAAF5Ew6D8QvASsPqybqQH_3-XsGN6Tp-DOoS4wx44NppFYi_KIlsQgh1OpKdEOc-JbVqdxSOURht1ZBGM13Pnko-TbGJNksLuv7ufQm-wteSigGMhyxXVtyozgeA7wPnsB3LkySaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های هند به نقل از خانوادۀ خدمۀ هندی گمشده در جریان حمله به یک کشتی قبرسی در تنگه هرمز، گزارش دادند که جسد او پیدا شده است.
این تبعۀ هند با نام هرامب کارمارکار، مهندس دریایی شاغل در کشتی کانتینری «جی‌اف‌اس گلکسی» بود که سه روز پیش هدف حملۀ سپاه پاسداران قرار گرفت. در جریان این حمله ۱۱ نفر هندی دچار حادثه شدند که ۱۰ نفر آنها نجات پیدا کردند.
سپاه پاسداران انقلاب اسلامی در بیانیه‌ای با تأیید حمله به این کشتی گفته بود به دلیل «حرکت در مسیر غیرمجاز و نادیده گرفتن هشدارهای مکرر»، با موشک به آن حمله کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/77103" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idYJF9tUjNRl6PyknEpKTENKNGvfCW4qCrLBCDzNFpe0exu5LusA8_yxSxV48upno0xqTI2lMH673xrk8oywRWean7KmlR1QQAmTEWm4IihT-fHAl4ROyLtWwC0iL9UaYS66-nolSFwhtClKLnXXhc4F3qkOXFGDjgKtgfkrxgC5YiT2s3ngeuXTr1gd01trXI8XrDfa9U_CeZTyNKyhNRlTqIJzj7gyG7YjymaAIQvtpUo_kXUgLnHMsqkn9rgXAM_7yNdyKXVFafwtM5ioH_88wzQGK1AOi7AGD9Gk9hfP50h0xkpVsIlFIYEZwMHYomCumEezVP2ZGxHYEXSzcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی صبح چهارشنبه ۲۴ تیرماه اعلام کرد هفت نیروی پایور و سرباز وظیفه ارتش در پی حملات آمریکا به پادگان نیروی زمینی بمپور ایرانشهر در استان سیستان و بلوچستان کشته شده‌اند.
در اطلاعیه ارتش آمده است که ارتش آمریکا «با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش جمهوری اسلامی ایران در بمپور را هدف قرار داد.»
نیروی زمینی ارتش جمهوری اسلامی تهدید کرده است که پاسخ این حملات را در زمان لازم خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/77102" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=dZTJ_iVqd0xSQyvr19x2ZhkvVHn5VatnaDsu7A9K0TuLmZ-nxSIVEpQsNFIwdAg65_NTzeyujKUpaIa0HRFb5_5QrhuiD6lC590eLpeo0zj3g0vWrZzgGMcBKFdYX8d6PryYsmBihxtquOv2Dg_3fmYed1r7PHdP1ouXtRdxmC54Y62lvq6RK-TWsjS46hm6IjQbPZVfKB8CJqN7AR2sGKJ-SM6ynZ-kBtBTmbaN0sHg1iQQKL4vSmqvy1nwzP7YYUuCdHu2YdCuCHa33bPkHq1GUufzlYx5ZZHWVi9nsKJDQBSH0v0LJZlZXodIRl2lGxUHVHmCEsjNb-oK8nJP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=dZTJ_iVqd0xSQyvr19x2ZhkvVHn5VatnaDsu7A9K0TuLmZ-nxSIVEpQsNFIwdAg65_NTzeyujKUpaIa0HRFb5_5QrhuiD6lC590eLpeo0zj3g0vWrZzgGMcBKFdYX8d6PryYsmBihxtquOv2Dg_3fmYed1r7PHdP1ouXtRdxmC54Y62lvq6RK-TWsjS46hm6IjQbPZVfKB8CJqN7AR2sGKJ-SM6ynZ-kBtBTmbaN0sHg1iQQKL4vSmqvy1nwzP7YYUuCdHu2YdCuCHa33bPkHq1GUufzlYx5ZZHWVi9nsKJDQBSH0v0LJZlZXodIRl2lGxUHVHmCEsjNb-oK8nJP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
🔹
صدای انفجارهایی امروز در برخی نقاط شهر شیراز شنیده شد.
🔹
براساس اخبار رسیده به خبرنگار مهر، این صداها ناشی از عملیات انفجار کنترل‌شده معدنی در محدوده معدن کارخانه سیمان شیراز بوده است.
🔹
بر اساس پیگیری ها این انفجارها در راستای فعالیت‌های معدنی و برداشت سنگ در محدوده معدن کارخانه سیمان شیراز انجام شده و با هماهنگی‌های لازم و رعایت الزامات ایمنی صورت گرفته است.
🔹
شنیده شدن صدای انفجار موجب نگرانی برخی شهروندان شیرازی شده بود که بررسی‌های انجام‌شده خبرنگار مهر نشان می‌دهد این صدا ارتباطی با حادثه یا رخداد امنیتی نداشته و مربوط به عملیات برنامه‌ریزی شده معدنی است.
پیام‌هایی که من دریافت کرده بودم:
انفجار وحشتناک شیراز ساعت ۱۳:۱۷ دقیقه
وحید یک صدای عظیمی اومد الان شیراز
شیراز
همین الان ساعت ۱۳:۱۸ صدای سهمگینی اومد
من سمت زرگری هستم
درود وحیدجان
۱۳:۱۸ شیراز سمت ما یک صدای شدید امد، فکر کنم زدن، چون چندتا از دوستامم از جاهای دیگه شنیدن صدا رو
انفجار اطراف دلیران تنگستان شیراز ساعت ۱۳:۱۷
سلام شیراز  ساعت یک و نوزده دقیقه صدای توافق اومد، جاش رو نمیدونم ولی صدای مهیبی داشت
وحید جان کارخونه سیمان شیراز رو ساعت ۱۳:۱۹ دقیقه زدن
ساعت ١٣:١٠ صدای انفجار سمت محله فرهنگیان شیراز اومد. برق هم که نداشتیم از قبلش
سلام وحید جان شیراز یه صدای  دور امد که شبیه برخورد موشک بود ۱۳:۲۰
سلام شیراز یه صدای انفجاری اومد
طرفای صنایع صدای انفجار مهیب
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
من که این قسمت شهر زندگی میکنم هر از چند وقت، محدوده معدنی کارخونه سیمان انفجارهایی دارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/77101" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px1M2v89naq4B5c47htlrdAI6UbK3nMshm4fRgCPBBCyHYMdTwkfcp7SLXLaNauG99yEtYxlJA9_ZxfYLcFkmZEkh7HdjrTHg1PAt_29ftLmmyOkN-TS4n1o8Zfcf00JIFV8oCVoK1b7JHSEWOxCJP-CDgVeTUbew3zU6nrRLO6DtIf_TFHNpQIiTJladlLWTbsrm6xycWw7WA5HA2Jc77d0FbGjOhjf9AZQ3OXJXTB5MtS83XNA6LLOI1RjhteCSIJNsIStzKzDqJJvQO4als1EVmBGc_62CjY5b5wcJ3fDDd0Da4_dTPv2jzhDfdhwOS7xbn5UxhHXYn7Ka8rZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش ایالات متحده، سنتکام، بعدازظهر چهارشنبه اعلام کرد که نیروهایش از ساعت شش صبح به وقت شرق آمریکا (۱:۳۰ بعدازظهر به وقت ایران)، موج دیگری از حملات علیه ایران را آغاز کرده‌اند.
در بیانیهٔ سنتکام آمده که این حملات با هدف تضعیف بیشتر قابلیت‌های نظامی ایران در حمله به کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه،‌ ۲۴ تیرماه، به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت دور جاری حملات به ایران «تا زمانی که من بگویم، ادامه خواهد داشت».
او تاکید کرد: اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد.
او گفت: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/77100" target="_blank">📅 15:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77099">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGaSLAi4SfgfI3CpVcS5Hl1Gx1y5frn3oNn6mCT1uhIAcPD7Kc7FVOWIE9NfE7w0xhyVFIzJiNTGGdnHJIDwoAAJ7aIACpv-9lavuEQtFSJrx6TAMJxXTncAiWLW4MkYdGlQAym7j06Q1Sv-nsujCD9xTVjQ334i8lsK-sqBVUsCyW3-RZU3IGhF0aXijUXVm6Ih7jgQFHB9jWzEsQiilQNzX3tRTX5Ij6eT9vJbg3zpZ1Krudd_0OQmxExjbYlfsLgv8Ceg7rGMrL-iaJhAgg3xekLnREYBNN9MeWFh9G-25-vdZEUy2P7USFsBV7I8Nq5-xQYlR3aud_lpYPQ3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77099" target="_blank">📅 15:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M7vcfkGAl3o3GfkUR0IjG97DNqJF-kaAi35L0gBT64jO8m3X62i-aYe0L19g0XNVQR1xw89xkXReGEBNCZXrqNirUGy-_TbINjCiLFN8AXSs_3scyxlisUi4tWPdhs8ioxxJeFOEznJPz0gr8BtZxTaZLtujgXAZUNaGv0LEGOGL34UG8MBmwYsY5FpfBIoS7iHth8Tag915Jf2sKYytGQr3gtDQDcR7DGqrOCe5ToDH7Tdo5lPz_fWbh_yPLtMATNYTBqDR_8LG62ptq9X_8eu-7WN0a9HRhVgCCODcspNhWZKa_UIFjoKr36jkj8vGB4gTFox-qT4uBVcEjyFURQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M7vcfkGAl3o3GfkUR0IjG97DNqJF-kaAi35L0gBT64jO8m3X62i-aYe0L19g0XNVQR1xw89xkXReGEBNCZXrqNirUGy-_TbINjCiLFN8AXSs_3scyxlisUi4tWPdhs8ioxxJeFOEznJPz0gr8BtZxTaZLtujgXAZUNaGv0LEGOGL34UG8MBmwYsY5FpfBIoS7iHth8Tag915Jf2sKYytGQr3gtDQDcR7DGqrOCe5ToDH7Tdo5lPz_fWbh_yPLtMATNYTBqDR_8LG62ptq9X_8eu-7WN0a9HRhVgCCODcspNhWZKa_UIFjoKr36jkj8vGB4gTFox-qT4uBVcEjyFURQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#چابهار
، چهارشنبه ۲۴ تیر، ساعت ۵:۳۰'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77098" target="_blank">📅 08:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67211d7671.mp4?token=ILGnpyHAxIFQA9hlGvQmR5yGzwkEfqormqJzZGz0K-REjrTDBW_V9ssfCyWCcSPhK52gGHKCiWi83wkAWildL3gVkFgCFT0AJ14J2MYQVoJa4Je1jUaZIVEF5CCkaMxQoTaJgr3xOCyk8vB9GA98Felflwn8R7NvjWyUnceMACbsBhUz7SCh_GgN7-a_c5VGAhS7X2H9opawUuLCzfYIRTW9L6qbUbhw4puCpjJKaJGaSm7cQiucFS7dZJrUQ406RfN6CXvCELLksaoRhbXw37w-soLd7aFnPj_FHfjB3s-3s9MdTyUhLRmVchwH-y0kQQ8hNbEAN6h4xA6zbjaFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67211d7671.mp4?token=ILGnpyHAxIFQA9hlGvQmR5yGzwkEfqormqJzZGz0K-REjrTDBW_V9ssfCyWCcSPhK52gGHKCiWi83wkAWildL3gVkFgCFT0AJ14J2MYQVoJa4Je1jUaZIVEF5CCkaMxQoTaJgr3xOCyk8vB9GA98Felflwn8R7NvjWyUnceMACbsBhUz7SCh_GgN7-a_c5VGAhS7X2H9opawUuLCzfYIRTW9L6qbUbhw4puCpjJKaJGaSm7cQiucFS7dZJrUQ406RfN6CXvCELLksaoRhbXw37w-soLd7aFnPj_FHfjB3s-3s9MdTyUhLRmVchwH-y0kQQ8hNbEAN6h4xA6zbjaFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا در ۱۴ ژوئیه، دور دیگری از حملات علیه ایران را به پایان رساند و ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار داد.
جنگنده‌ها، پهپادها و شناورهای نیروی دریایی آمریکا در جریان این موج حملات هفت‌ساعته، مهمات هدایت‌شونده دقیق را علیه سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی به‌کار گرفتند تا توانایی ایران برای تهدید کشتی‌رانی تجاری و خدمه غیرنظامی را بیش از پیش تضعیف کنند.
این حملات در همان روزی انجام شد که نیروهای آمریکایی محاصره دریایی علیه شناورهای در حال تردد به مقصد یا از مبدأ بنادر و مناطق ساحلی ایران را از سر گرفتند. این محاصره امروز از ساعت ۴ بعدازظهر به وقت شرق آمریکا به اجرا درآمد.
نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که فرمانده کل قوا دستور دهد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77097" target="_blank">📅 06:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JKTqmP8p1QVNMSfgcq0qxY283PcqUfMfclHK2Lk2KpyBaJJRzCi0tRVzyGQdU7YkPjAjoAUHVgtJr5IxGWBlUcDNuDxoQoh2Au3XR6eu2rcn6e_wxNy3j6-dZCo8d4ATX7pxPiI4ZVrAUCPAtEi-K179Ub61EXR_D2kDuXgHata9wWtQSHGtcazpIEwp23QHQVfhJ6DXoLj8dRaVLaqRLDqgCnozqJjufar8pJXL_gTCtwqm4-Bnv69s93PHNKtOyYhV4l5r-rSDl_d5z1T8FmmYq9sasilplXBmmcjSC7XDGP8RVjQ8OmXjqaS_cxVk-U3HgbF380SsSro62QMjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFibI6R9ZuD39JmfXdyoLN68cz5duDy7-jZXNsqpIoEL3mO3gLa5U0WtETrkCS79OAgqU9Lx_6DBybTL_jT10-p5rbPxrp7R9qHWOfEJ3asfeKi70WvHBWI-fzCiJaFmu5h-8vAUHFIPSIIfyCDJqmRGIdxCrYIXypaOyTjR7YuX6u6Q5WIfBR0oOvZYkyGqVfvzWXSVatriwgpAY-jGc9EfmeIVjqd06HEfTvjfs4NR_CBXidksdLbze29RRyWD3iLFoc_SgemWGsSg6pRU47uLQV5kk4leA70rPDzr5AacClAUtv1n53aFfLQ2skZD8GUmZWTyZgiZ2uUzZlcRWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=uBYU5h56JMLAfWZ00gO_hxVtm6S6Wko5N-5AxL0OvHbnd0u7W34vltZ6iVMRPja5z1lYHNfJ0cZ46c4zPSMeM2An1Rr9S-CVk5NiftfXwL6RQGc9z1W8XS3EdyiwD-3V-29Bwh6ackjQLLfRx2gW90V1UF1klPXRNprsjjAiz395jnn2dF1IMOIgxoqFHQO9fw_kGCu34lGfj1-0JRZUNPlwqgMdbD2qByTzb_UdfHBARG-KHUWRenreE5PHeFhCuaTxLAPm8l8jFP6XwzC1IQgOo4HP0Sxrb4PnT_n8bDfl9WJ3yn0Gq34_xTg9Zg-_7BAK21cZwsKJwxJkaD75Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=uBYU5h56JMLAfWZ00gO_hxVtm6S6Wko5N-5AxL0OvHbnd0u7W34vltZ6iVMRPja5z1lYHNfJ0cZ46c4zPSMeM2An1Rr9S-CVk5NiftfXwL6RQGc9z1W8XS3EdyiwD-3V-29Bwh6ackjQLLfRx2gW90V1UF1klPXRNprsjjAiz395jnn2dF1IMOIgxoqFHQO9fw_kGCu34lGfj1-0JRZUNPlwqgMdbD2qByTzb_UdfHBARG-KHUWRenreE5PHeFhCuaTxLAPm8l8jFP6XwzC1IQgOo4HP0Sxrb4PnT_n8bDfl9WJ3yn0Gq34_xTg9Zg-_7BAK21cZwsKJwxJkaD75Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح:  انفجار حمله به چابهار حدود ساعت ۵:۳۰
چهارشنبه ۲۴ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77092" target="_blank">📅 06:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G17H0vdf5TRtRAgfLakCOmVvkDqM8oMzw_EqZjTcUm569h-wEk44K6Rr7ST5k3UGPvVSgARBudTnPnQrCiRJsRvVGsgs1Ufgp3slTiUAi5b0ueGo2RjgIix0FnpolpkxwwFELMdPH4Fu8JKZ4ByjLprVUYTPy4QcuglDM2pKAEfNAbW-9IoxD4oMV-ZxTRQ05JuNp5koO525H9cloUXSaSthEsfzlYAMS417yyPn4uiBy4qo-x4kHpD0hAo9Oax3XjzH1NWcYl1OOkdScseSPqToKp6Orve_h4t20DahwdG1QvcvpKHaS1eMxDrOnsK_mvSW64UvcZC2fxTEuxWQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از سیستان و بلوچستان:
چابهار پایگاه مستقل امام علی همین الان دوتا زد
سلام کنارک الان دو تا زد
سلام همین الان صدای چهار انفجار در کنارک
۵:۳۰ دقیقه چابهار سمت دریا کوچیک فکر کنم زدن. صدای جنگنده ها میومد.
ساعت ۵:۲۰ صبح جنگنده وارد حریم چابهار شد پایگاه امام علی و کنارک زد
کنارک دوباره یکی زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77091" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیام‌های دریافتی دوباره هم‌زمان از سربندر و ماهشهر:
همین الان بندر امام خمینی‌ رو زدن سه بار
یا خدا سه تا انفجار وحشتناک سربندر
بعدی
وحید جان سلام ماهشهر صدای چندین انفجار متوالی
سلام ماهشهر الان زد نسبت به قبلیا موجش بیشتر بود
همین الان صدای شدید ماهشهر، نمیدونم کجا رو زدن
سلام اقا وحید سربندرو همین‌الان‌چهار بار زدن
ماهشهر الان ۴تا زدن
۵تا شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77090" target="_blank">📅 05:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7caCK4aB7f9fb8gRkqFG2L-2-3Xefb0KzJB57BcjmD4H2ARXb5tVxWrJQA2UXceJO389voJvxOl3xcyV40ZV_J5rX1l_hsEqTTLWx3axeLSAGpdMD91eQHOwSi-ndv4G0so-9AEzbJ0qfnXXmEDhQCq13a3HzSubTzolH6mG-oOklNI5oyH9nfbFIGm19hdo8O2w2oJNuGZ7HNmlNQb-cBNLltD8fwrId0ASvQoeH-DxejVrz6hcSg-UkKruz0auatYhVrH3POgu4P1B0-GAqgCCkuJchNrq6FRj7mJb6aKdBQLLP91tG4jMPGRZy19JgZ7xLuQEYkQpcTIe2JvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از پیام‌های مربوط به شهر بوشهر، پیام‌هایی از شهر جم در استان بوشهر داشتم درباره شنیده شدن صدای انفجار:
۴/۲۵ همین الان ۳موشک به فرودگاه جم برخورد کرد قبلن از اونجا موشک میفرستادن
جم بوشهر
فرودگاه جم
الان صدای چند انفجار در شهرستان جم استان بوشهر شنیده شد.
دیشب هم همین موقع صدای چند انفجار شنیده شد.
همین الان فرودگاه جم رو زدن
درود وحید همین الان جم سمت پایگاه چمران نه سمت فرودگاه توحید دوتا صدای خیلی آروم اومد بعد دود سفیدی بلند شد و نورانی، معلومه موشک خواستن بفرستن نرفته
جای همیشگی نبود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77089" target="_blank">📅 04:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر صدای انفجار همین الان
انفجار ساعت ۴:۳۸ خورموج بوشهر
سایت موشکی را زدن
بوشهر ششم شکاری هوایی [رو] زدن
ساعت ۴:۴۰
سلام وحید جان شبتون بخیر ساعت 4:41 بهمنی رو دو بار تا الان زدن و همینجوری دارن میزنن پشت سر هم پایگاه هوایی
انفجار خیلی وحشتناک بوشهر ساعت ۰۴:۴۱
وحید بوشهر ۴:۴۱ پایگاه هوایی یا دو طفلان مسلم
😂
بوشهر الان زدن ۴:۴۱
درود وقت بخیر
بوشهر همین الان یک صدای انفجار بشدت بلند اومد
سلام ساعت 4:40 صدا بزرگ انفجار از بوشهر اومد
۴:۴۰ بوشهر یه انفجار بزرگ
وحید ۲.۳ انفجار سنگین در بوشهر ۴:۴۰
وحید بوشهر ناحیه‌ی بهمنی صدای شدید انفجار
😭
😭
😭
😭
😭
😭
بوشهر زدن الان ۴:۴۰
شهر بوشهر ۰۴۴۰ زدن
سلام وحید الان بوشهر رو خیلی بد زدن مراقب خودتون باشید خیلی میزنن مراقب باشید ساعت ۴.۴۰ بوشهر بیسیم
وحید ما سنگی بوشهر هستیم صدا خیلی شدید بود درحدی که انگار صدمتر کلا فاصله داشت
بوشهر دو تا صدای بلند اطراف تنگک اومد
آقا وحید پایگاه هوایی بوشهر و زدن 4:40 صدای انفجار خیلی بلند بود
داداش بوشهر شش دقیقه پیش یچیز سنگین زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77088" target="_blank">📅 04:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=VwCyp9t_5rQKG-NoF9y-9Ro4LJ2jt0FNo8kH2lziaOf0w331G-GHsY2_GqsZb981lWbT5YaLmmZN_WLgpZAtv1bZOdzqv8yqHGTbFyABZA1_bicbI0fiVw2DL9rhFhviMK8vZAdmBlplj0bJX8GQErfL-vJwt4DgAi85MlY0HIO4JhEXuejGfD_6FBtTWS2rBV_16ewyUbPzNvXUnUjd1iSGTuzDLY6PI2YP0Bx1BeP2TkQyvTntCWoIFBDkWil2VVvscDcSLNMe7xBUomtHgFUdCCOs2130I_rYFtAG0fzXH2gPif2awrt8z1YTAgGbqkcxkvOmh4rIen-ImSsODA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=VwCyp9t_5rQKG-NoF9y-9Ro4LJ2jt0FNo8kH2lziaOf0w331G-GHsY2_GqsZb981lWbT5YaLmmZN_WLgpZAtv1bZOdzqv8yqHGTbFyABZA1_bicbI0fiVw2DL9rhFhviMK8vZAdmBlplj0bJX8GQErfL-vJwt4DgAi85MlY0HIO4JhEXuejGfD_6FBtTWS2rBV_16ewyUbPzNvXUnUjd1iSGTuzDLY6PI2YP0Bx1BeP2TkQyvTntCWoIFBDkWil2VVvscDcSLNMe7xBUomtHgFUdCCOs2130I_rYFtAG0fzXH2gPif2awrt8z1YTAgGbqkcxkvOmh4rIen-ImSsODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
تصاویری که بنا بر گزارش‌ها پیش‌تر در جریان حملات پهپادی و موشکی ایران به کویت ضبط شده‌اند، لحظه اصابت یک پهپاد شاهد-۱۳۶ را نشان می‌دهند. آمریکا همچنان با ایران به تبادل حملات ادامه می‌دهد و اکنون اهدافی در بحرین و کویت زیر سنگین‌ترین آتش ایران قرار گرفته‌اند.
sentdefender
,
MenchOsint
ستاد کل ارتش کویت، بامداد چهارشنبه، با انتشار بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» است.
این ستاد با تاکید بر اینکه صدای انفجارهای احتمالی ناشی از رهگیری این پرتابه‌ها توسط سامانه‌های دفاع جوی است، از مردم خواست تا دستورالعمل‌های امنیتی صادره از سوی مراجع مربوطه را رعایت کنند.
@
VahidOOnLine
وزارت کشور بحرین، با انتشار هشداری فوری در حساب رسمی خود در اکس، اعلام کرد آژیر خطر به صدا درآمده است و از شهروندان و ساکنان خواست آرامش خود را حفظ کنند و به نزدیک‌ترین مکان امن بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77087" target="_blank">📅 04:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری جمهوی اسلامی ساعت ۲:۵۶
حمله به یک واحد تولید آب معدنی در موسیان
🔹
دقایقی قبل، یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان (استان ایلام) هدف سه پرتابه دشمن قرار گرفت.
🔹
مراد یگانه فرماندار دهلران بامداد چهارشنبه به خبرنگار ایرنا گفت که این حمله هیچ تلفاتی نداشته است.
🔹
وی اظهار کرد که در این تجاوز به تجهیزات کارخانه خساراتی وارد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77086" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=V7Y3bBx22gvIEQmDaphJtBik4O6lxD144F-LbgthUUYsv7D8AlUbBSLrQkV0Uxrd0--tqVa52-Zv7M5MuDGMTXKVoFI9c5QiuFTAq3oiuEdH1lZkJFbAHZ99gzOVh9uV8n359l_DaxOFs0LS0O9CzxMy8uXXf3s4xzVbIb-iMKTbMHZlLDa7qv77eSgxa9VkrlKcsWMccgwvznZkQTytE9a--Xw7ojeAtZDa2MHcZrbcEiz_d8vmw0kJhhoRcCNFTAuils_MQZhZ3vALqUEILfOnkuClAyy20IYPGHoTWeJ1B9UaoHyeJg1sGQgrzdH_g0MtzlIIV12JJ-Z0UqJN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=V7Y3bBx22gvIEQmDaphJtBik4O6lxD144F-LbgthUUYsv7D8AlUbBSLrQkV0Uxrd0--tqVa52-Zv7M5MuDGMTXKVoFI9c5QiuFTAq3oiuEdH1lZkJFbAHZ99gzOVh9uV8n359l_DaxOFs0LS0O9CzxMy8uXXf3s4xzVbIb-iMKTbMHZlLDa7qv77eSgxa9VkrlKcsWMccgwvznZkQTytE9a--Xw7ojeAtZDa2MHcZrbcEiz_d8vmw0kJhhoRcCNFTAuils_MQZhZ3vALqUEILfOnkuClAyy20IYPGHoTWeJ1B9UaoHyeJg1sGQgrzdH_g0MtzlIIV12JJ-Z0UqJN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
منابع محلی از افزایش آمار مجروحان حمله به تیپ ۳۸۸ ارتش در
#بمپور
خبر دادند؛ دست‌کم ۵۰ مجروح، دست‌کم دو فوتی در بیمارستان و گزارش‌هایی از تلفات گسترده در داخل پادگان
بر اساس تازه‌ترین اطلاعات دریافتی،
تاکنون دست‌کم ۵۰ مجروح به مراکز درمانی، به‌ویژه بیمارستان خاتم‌الانبیا ایرانشهر، منتقل شده‌اند و حال هفت نفر از آنان وخیم گزارش شده است.
به گفته منابع حال‌ وش: «از میان مجروحان منتقل‌شده به بیمارستان، تاکنون دست‌کم دو نفر بر اثر شدت جراحات جان خود را از دست داده‌اند و وضعیت هفت نفر دیگر نیز بحرانی است. روند انتقال مجروحان همچنان ادامه دارد.»
منابع افزوده‌اند: «همزمان گزارش‌های متعددی از داخل تیپ ۳۸۸ حاکی از آن است که
شمار کشته‌شدگان در محل حمله بسیار بیشتر از آمار منتقل‌شدگان به بیمارستان است و ده‌ها نفر در داخل پادگان جان خود را از دست داده‌اند.
با این حال، به دلیل محدودیت‌های امنیتی و جلوگیری از دسترسی به محل، امکان راستی‌آزمایی مستقل این آمار تاکنون فراهم نشده است.»
به گفته منابع محلی، بخش‌هایی از آسایشگاه سربازان و سایر تأسیسات داخل پادگان در زمان وقوع حملات هدف قرار گرفته و همین موضوع موجب افزایش شمار تلفات و مجروحان شده است. همچنین تدابیر امنیتی در اطراف تیپ همچنان ادامه دارد و از نزدیک شدن شهروندان و خانواده‌های نظامیان به محل جلوگیری می‌شود.
حال‌ وش
پیش‌تر
از وقوع چندین موج حمله، شنیده شدن دست‌کم ۱۱ انفجار، ورود آمبولانس‌ها به داخل تیپ، خاموش شدن کامل چراغ‌های پادگان و انتقال مجروحان به بیمارستان خاتم‌الانبیا ایرانشهر خبر داده بود.
تا لحظه تنظیم این گزارش، هیچ‌یک از مقام‌های جمهوری اسلامی درباره آمار کشته‌ها، مجروحان، میزان خسارات و جزئیات این حمله اطلاع‌رسانی رسمی نکرده‌اند. اطلاعات منتشرشده در این گزارش بر پایه اظهارات منابع محلی و شاهدان عینی است و حال‌ وش همچنان در حال پیگیری و راستی‌آزمایی ابعاد این رویداد است.
haalvsh
همزمان با انتقال شمار زیادی از مجروحان حمله به تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش در شهرستان بمپور به بیمارستان خاتم‌الانبیا ایرانشهر،
مرکز انتقال خون ایرانشهر با انتشار اطلاعیه‌ای از شهروندان واجد شرایط خواست برای اهدای خون به این مرکز مراجعه کنند.
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77085" target="_blank">📅 03:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQ3PL5BJjSs-iqo65vS6p-327XxUvPo1bwZ-4mjWaNI3wuuC2YlaDnzNsla7Fqm_hIaQg4naPbRniuHOkCCjE28EymnBEBNpxyQZIEXkiBB0DIkHaXWtPlLMSmMMr47OeYUihT0NYaFlirsHQZMp2-L7kGQzUXclbWyOSYnDRU8RR0HFvAeSu6SReBWZShxKZ-Y6MmDzDh6cnjEP5C7Ypp3s2CsOiWgktN7RJHnbWxldElcawEWUBRSxMS1v7tVPwMGr_BwkMiWAm9D2TVh2Unfiy3tQs2HMyzr5qULxbVB-QPFBFahIT7gR2I8YrtNsaWtEB9LzhGtrldYyayOTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، با انتشار بیانیه‌ای اعلام کرد جمهوری اسلامی طی هفت روز گذشته با حمله‌های عمدی به غیرنظامیان در سراسر منطقه، هفت کشتی تجاری را هدف قرار داده است. به گفته او، در نتیجه این حمله‌ها نزدیک به ۱۲ نفر از خدمه غیرنظامی کشته، مفقود یا زخمی شده‌اند.
@
VahidOOnLine
تصویر انگلیسی رو سنتکام منتشر کرده متن فارسی رو بالاش اضافه کردم. ترجمه ماشین:
بیانیه فرمانده ستاد فرماندهی مرکزی ایالات متحده
«ایران طی هفت روز گذشته با حمله به هفت کشتی تجاری، عمداً غیرنظامیان را در سراسر منطقه هدف قرار داده است؛ حملاتی که در نتیجه آن نزدیک به دوازده تن از اعضای غیرنظامی خدمه کشته، مفقود یا زخمی شده‌اند.
نیروهای ایرانی همچنین ده‌ها موشک و پهپاد به‌سوی کشورهای همسایه در حاشیه خلیج فارس پرتاب کرده‌اند. نیروهای ایالات متحده، ایران را به‌دلیل این تجاوز بی‌دلیل که همچنان جان افراد بی‌گناه را به خطر می‌اندازد، پاسخگو می‌کنند.»
دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77084" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=T9_mWU4jNN3fMVNyOCvGjw6Lk9cA7D1_rKKuqmJO3suOFtc0nomxqPhklF3inP4EQvu2JakVGWjOnP1YZRAXjIU0MYgkXfMIhHMc-8DxmMuuWsEVx1GU7TAL6DMR81CasFGk2CGeGgeeJCuLVwpY_odQK5vOky_S4CrNBrsiLkxD69f8ASPIbVGk3_ZFyLLh-9JijkPcMhXu17ZqdFZMD83aHmMMpDlrvRh9ord2PbigbBVVGEEgV69V7Ga2p2KCvCA0StavW-JfAx_0kUFsV0tK9-UtTVbbaVpbXeSMO_gUdaadynyDpRlSoSAwUaN5B41wgUDkMJZP_711yu3Wpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=T9_mWU4jNN3fMVNyOCvGjw6Lk9cA7D1_rKKuqmJO3suOFtc0nomxqPhklF3inP4EQvu2JakVGWjOnP1YZRAXjIU0MYgkXfMIhHMc-8DxmMuuWsEVx1GU7TAL6DMR81CasFGk2CGeGgeeJCuLVwpY_odQK5vOky_S4CrNBrsiLkxD69f8ASPIbVGk3_ZFyLLh-9JijkPcMhXu17ZqdFZMD83aHmMMpDlrvRh9ord2PbigbBVVGEEgV69V7Ga2p2KCvCA0StavW-JfAx_0kUFsV0tK9-UtTVbbaVpbXeSMO_gUdaadynyDpRlSoSAwUaN5B41wgUDkMJZP_711yu3Wpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Vahid
پیام‌‌های دریافتی:
وحید جان همین الان تبریز موشک زدن باز
سلام وحید از تبریز موشک فرستادن ۲:۱۰
سلام آقا وحید ساعت ۲:۱۲ دیقه از تبریز تا الان که ساعت ۲:۱۴ هستش دوتا صدای موشک اومد
سلام وحید جان همین الان ساعت ۲:۱۴ صدای های انفجار میاد از ارومیه
مشخص نیست پرتابه موشکه یا چی
پرتاب موشک از حوالی تبریز به جای نامشخص، صدای غرش خیلی شدید و بی سابقه
سلام وحید دو سه دقیقه پیش از سایت موشکی [...] دو موشک  پرتاب کردن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77083" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=TaioeJAoyr4Y3R4f5Yf8KPK0TvvSLmkXcBtgalTgZbjfxu8OuaqFgK1S6Kxb3gr9ricD-AlsINYC1wk9ZOF6-HulCH-7hgEpqr_XY85IDCt2JGc4nucVen2YfU8sHO9w6-clAw6dGKqZapmz20mIr_y6YQ1J0JHWU8imOwiEk9B6rscehc6-fYh6bv2aTWcxEkIAywoGBGXvKDtBY9RJ79cWoS3vusIRksAShT3angX_3cV9C3GyA6vy9jTJlqvII1e4kRT6ay3tvs5eVmfc65aakkWfPJYw5NR7_FuJvoOvoQfmArINo_cuY-60xSF9tVHYhi8pI5LiPi38EYyaog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=TaioeJAoyr4Y3R4f5Yf8KPK0TvvSLmkXcBtgalTgZbjfxu8OuaqFgK1S6Kxb3gr9ricD-AlsINYC1wk9ZOF6-HulCH-7hgEpqr_XY85IDCt2JGc4nucVen2YfU8sHO9w6-clAw6dGKqZapmz20mIr_y6YQ1J0JHWU8imOwiEk9B6rscehc6-fYh6bv2aTWcxEkIAywoGBGXvKDtBY9RJ79cWoS3vusIRksAShT3angX_3cV9C3GyA6vy9jTJlqvII1e4kRT6ay3tvs5eVmfc65aakkWfPJYw5NR7_FuJvoOvoQfmArINo_cuY-60xSF9tVHYhi8pI5LiPi38EYyaog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه، در گفتگو با «فاکس‌نیوز» در پاسخ به مجری که از او پرسید حمله‌ها تا چه زمانی ادامه خواهد داشت، گفت: «تا زمانی که من بگویم کافی است.»
او گفت آنها (حکومت ایران) هنوز تا حدودی توانایی جنگیدن دارد اما چیز زیادی برای آنها باقی نمانده است.
ترامپ در پاسخ به مجری که از او پرسید، اکنون وضعیت را چگونه توصیف می‌کند، آیا جنگ از سرگرفته شده، گفت: می‌توانید هر نامی روی آن بگذارید اما ما ضربه بسیار سختی به آنها زده‌ایم. ترامپ بار دیگر بر اهمیت باز ماندن تنگه هرمز تاکید کرد.
ترامپ در پاسخ به مجری که از او پرسید آیا جنگ از این فراتر می‌رود و اهداف مرتبط با انرژی ایران نیز در فهرست قرار دارند گفت: انرژی را برای بعد نگه‌داشته‌ام.
ترامپ افزود: امشب و فرداشب و پس‌فردا‌شب، ضربات سنگینی به آنها می‌زنیم و هفته آینده برای آنها خیلی بد خواهد شد. هفته آینده نوبت نیروگاه‌ها و پل‌ها است.
رئیس‌جمهوری آمریکا گفت: هفته آینده همه پل‌ها و نیروگاه‌های آنها را از بین می‌بریم مگر اینکه پای میز مذاکره بیایند.
رئیس‌جمهوری آمریکا پیش‌تر نیز این تهدید را مطرح کرده بود اما پس از آن اعلام شد که مذاکرات از سرگرفته می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77082" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=EioGNZ-MDTMMVsFeZI9Kzg5WhYeM0E9Fqstw9HOUj3uk9g-0LYtD4HTc01PXCljG797rSug_Df_ratL1eWC3IaTRtXLAC_LVQ8qxHyK_36IHBaDxkhNyoaIpo3ui79ZL6f27UpAu-_xETB8UvGFJEwsVBeQVtTTgb00CkWPPANsZOoIcLyUJrkMck5hG53o_irhERcACsoAZCJNs6KFWucpB48CXrT90AetV4s9sbE8B7VVe6HH3u3Zv0fGaK9mkDYNK3d6-GubooyA9HUw8GhrnbIOLtPRLepbIz-KJP-aW66drF3atEC6Iv9sKXD29311aQRigiukQDL1QBRCEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=EioGNZ-MDTMMVsFeZI9Kzg5WhYeM0E9Fqstw9HOUj3uk9g-0LYtD4HTc01PXCljG797rSug_Df_ratL1eWC3IaTRtXLAC_LVQ8qxHyK_36IHBaDxkhNyoaIpo3ui79ZL6f27UpAu-_xETB8UvGFJEwsVBeQVtTTgb00CkWPPANsZOoIcLyUJrkMck5hG53o_irhERcACsoAZCJNs6KFWucpB48CXrT90AetV4s9sbE8B7VVe6HH3u3Zv0fGaK9mkDYNK3d6-GubooyA9HUw8GhrnbIOLtPRLepbIz-KJP-aW66drF3atEC6Iv9sKXD29311aQRigiukQDL1QBRCEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
ویدئوهای جدید از حملات و انفجارهای شدید در محدوده تیپ ۳۸۸ ارتش در شهرستان بمپور
بامداد امروز چهارشنبه ۲۴ تیرماه ۱۴۰۵، ویدئوهای جدیدی از حملات و وقوع چندین انفجار شدید در محدوده تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش، واقع در نزدیکی روستاهای ریکپوت و کلاهدوز از توابع شهرستان بمپور ، به دست حال‌ وش رسیده است.
به گفته منابع حال‌ وش: «در این ویدئوها، صدای انفجارهای پی‌درپی و نور ناشی از اصابت‌ها در محدوده این مرکز نظامی مشاهده و شنیده می‌شود. شدت انفجارها به اندازه‌ای بوده که صدای آنها در روستاها و مناطق اطراف نیز شنیده شده است.»
منابع افزوده‌اند: «حملات در چند نوبت انجام شده و ویدئوهای تازه، بخش‌هایی از لحظات اصابت و انفجار در محدوده تیپ ۳۸۸ ارتش را نشان می‌دهد.»
حال‌ وش پیش‌تر گزارش داده بود که حوالی ساعت ۰۰:۰۵ بامداد، دست‌کم هشت انفجار شدید در محدوده روستاهای ریکپوت و کلاهدوز شنیده شده و منابع محلی از هدف قرار گرفتن تیپ ۳۸۸ پیاده مکانیزه شهید حیدر شهرکی خبر داده بودند.
تا لحظه تنظیم این گزارش، اطلاعات دقیقی درباره میزان خسارات و تلفات احتمالی منتشر نشده و مقام‌های جمهوری اسلامی نیز درباره جزئیات این حملات اطلاع‌رسانی رسمی نکرده‌اند.
haalvsh
لوکیشن دریافتی تایید نشده:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77080" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در میان رگبار پیام‌های اهواز سه پیام متفاوت درباره جاده تهران-قم حوالی فرودگاه داشتم که نمی‌دونم چقدر درست هستند. هرچه صبر کردم پیام دیگری نیومد ولی اون اطرف کلی نقطه نظامی در بیابون هست که لابد کسی بهشون نزدیک نیست:
پیام ساعت ۲۳:۲۰
هم اکنون انفجار فرودگاه امام خمینی
صدای انفجار دور بود ولی لرزشش احساس شد
در پی مکالمه اضافه کرد: من اطراف فرودگاه هستم. چون اینجا بیابونه و نزدیک ترین لوکیشن بهمون همون فرودگاه هست اون  رو گفتم
پیام ساعت ۲۳:۲۳
سلام وحید جان جاده قدیم قم نزدیک اتوبان غدیر هستم صدای انفجار و لرزش اومد
زدیم ماشین رو بغل
پیام ساعت ۲۳:۲۶
سلام حسن اباد فشافویه نزدیک فرودگاه امام میشه صدای انفجار شنیدیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77079" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmFjaEn-4GpzAHgfCFFmGS56paLMw5AtR4QYkfIfjdyftXuGajtxZ0k91G-1TGVmgNCNcxiDkte7CqBhI1YWMk-59ztNQQqsp8MpcazbhdHDK0moABXKTIFT-dUJM6BaonRk8nTTQ58wUdHbXPqpwC2kDtOyMbfGdIJbpOxR70T9YlpIdQa_ZL9YHwVTtbibVH6Y6Fi1Ru8GqChX1LKBWRILrF1r-_V0tosti7vGf667FEuzeui-hfIKZgrQ1jZwDO83_vOdBbqgPwoTo_TTCcCZnoiqei8ZAftXH7UfJkz4CfVoNjExyYfXRTUDVjPa6pJfAezkqLd8L-Z73ld6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، [
در پستی تازه
] اعلام کرد نیروهای آمریکایی از ساعت ۴ بعدازظهر به وقت شرق آمریکا [یعنی دقایقی پیش]، محاصره دریایی کشتی‌های در حال تردد به بنادر و مناطق ساحلی ایران را از سر گرفته‌اند.
سنتکام در پیامی در شبکه اجتماعی ایکس، این اقدام را پاسخی به آنچه «حملات اخیر و غیرموجه ایران به کشتی‌های تجاری و خدمه غیرنظامی» خواند، توصیف کرد و افزود آمریکا جمهوری اسلامی را مسئول این حملات می‌داند.
بر اساس این بیانیه، در حال حاضر بیش از ۲۰ ناو جنگی نیروی دریایی آمریکا و صدها هواپیمای نظامی در سراسر خاورمیانه مستقر هستند و نیروهای آمریکایی «هوشیار، آماده و دارای توان رزمی» باقی خواهند ماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77078" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۳:۱۸ یه انفجار دیگه
ساعت 11.19 اهوازو زدن
۲۳:۱۹ ، اهواز صدای انفجار اومد
وحید جان سلام
دوباره اهواز روزدندساعت ۲۳:۱۸
ساعت ۲۳:۱۹ اهواز صدای انفجار
سلام وحید جان 11:19 اهواز، زدن
اهواز الان زد سه راه باهنر موجش اومد ۲۳:۱۹
همین الان ۲۳:۱۹ اهواز دوتا پشت سرهم
ما کمپلوییم! خیلی نزدیک بود فکر کنم لشگر ۹۲ زرهی بود!
سلام اهواز صدای انفجار نمیدونم کجا ساعت 11:19
اهواز  الان  ۲۳:۱۹
سلام ما باهنر اهواز هستیم با اینکه کولر روشنه و فوتبال میبینیم ولی صدای دو انفجار حدود ساعت ۱۱.۲۰ شنیده شد
و کلی پیام مشابه دیگر که بعضی‌هاشون فقط نوشتند: همین الان یا دوباره
که چون ساعت و دقیقه نمی‌نویسند نمی‌دونم کدوم باره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77077" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در بهبهان
بهبهان رو چند دقیقه پیش زدن خوابگاهمون کامل لرزید
سلام
چند دقیقه پیش شیشه های خونه وحشتناک لرزید
نمیدونم انگار تو شهر رو زدن
بهبهان زندگی میکنم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77076" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKs65qAAb0FA3KST4gOBOW8pglIAOHiERouWLRAIdpbcNR7xe0YnQ48Nmg3JqdgipgbbfOlq1pqrRPpXJEBb4kmiqZTBeGVcipttSpRH3h3HQWQnUYh2h0xrTJIMq7oB9s6vWhm3J0JmLV2tJmDqxuQ5Us-d1ykLrWHw8Aclqtho-ft2zLngSGMj13EUJa9I3XPqlFBGpEMAqGTE0JI6dgA3A_Y7-RY6bIzKdHtphh_Y1Yk2LkeLNW0gM-dY5QpetHyh-L1-OUhzWkijWTj_BK8CAzUzOJs5ufCmeyeBL6vSD1A_zqSpXMgQQp_NRgKTyvt30uJR-kuqqldOhrONfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ تهران]، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شود، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌کنند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا [۰۰:۳۰ بامداد چهارشنبه] به اجرا درمی‌آید.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77075" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
بندرعباس ۲۲:۴۴ صدای چند انفجار
بندرعباس ساعت 10:45 چهارتا صدای انفجار اومد
چند انفجار ممتد ساعت ۲۲:۴۵ بندرعباس موجش زیاد بود
ساعت ۱۰.۴۶ صدای انفجار خیلی بددد تو بندرعباس
درود وحید جان بندرعباس سمت باهنر چهارتا انفجار شدید بود
🔄
سلام بندرعباس انفجارهای پشت سر هم سمت منطقه۴  ۲۳:۰۸
بندرعباس ساعت 11:08 دوتا صدای انفجار دیگه اومد
ساعت ۲۳:۰۸ بندرعباس ۳ انفجار
باز بندر رو زدن 23:08
دو سه تا انفجار مهیب ، لرزوند ساختمان رو
۲۳:۰۸ صدای دو انفجار شرق بندرعباس
سلام آقا وحید بندرعباس دوتا صدا پشت سر هم اومد ساعت 23:08 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77074" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۲:۳۰ صدای ۲ انفجار
سلام اهواز رو الان زدددد
سلام وحید جان اهواز ساعت ۱۰:۳۰ صدای ۳ انفجار مهیب
همین الان اهواز صدای دوتا انفجار اومد
اهوازو زدن
درود وحید جان همین الان  صدای دوتا انفجار اهواز شنیدم. ساعت 22:31
اهواز ساعت ۲۲:۳۰
۳ تا انفجار
سلام وحید الان اهواز [رو] زد ۳ تاشو من شنیدم۲۲:۳۲
سلام اهواز [رو] همین دو دقیقه پیش دوبار زدن
سلام وحید جان اهواز همین الان دوتا صدا انفجار اومد. زمین لرزید.
ساعت ۲۲:۳۱ دوتا انفجار اهواز
سلام اهواز [رو] زدن خونه لرزید
سلام وحید اهوازو زدن ساعت ۱۰ نیم دو تا
سلام اهواز دو انفجار شنیده شد
وحید جون 2 انفجار اهواز 22:31
انفجار مهیب همین الان در اهواز صداا از سمت غرب اهواز بود. اونقدر شدید بود که زمین لرزید
سلام الان اهواز سه تا انفجار شنیدیم
سلام آقا وحید اهواز الان زدن صدای 2 انفجار نزدیک خونمون صدا مهیب بود
سلام وقت بخیر اهواز سمت کیانشهر صدا اومد ۲تا صدای زیاد
ب[ذ]ار فوتبال نگاه کنیم جون مادرت ۱ ساعت
🔄
۱۰:۳۵ دوتا انفجار دیگه اهواز
سلام اهواز [رو] زدن خونه لرزید
یکی دیگه زدن
۱۰:۳۵ دوتا انفجار دیگه اهواز
اهواز رو الان دوباره زد
هنوز اهوازو دارن میزنن ۲۲:۳۵
همين الان ١٠:٣٥ مجددا دو بار صداى مهيب توى اهواز
ساعت ۲۲:۳۴
۲ تا دیگه انفجار شدید اهواز
اهواز  . از ساعت ۱۰:۳۰ تا الان ۴ تا صدای انفجار
ما کوی نیرو هستیم اهواز
صدای دو انفجار اومد
حدود دو دقه پیش
وحید اهواز رو دوباره زد ساعت ۲۲:۳۵
سلام ساعت ۲۲:۳۴ سه انفجار در اهواز
همین الان اهواز برای بار چهارم انفجار مهیییب
با اینکه کولر روشنه ولی صداش خیلی بلند میاد
اهواز ساعت 20:37 چند انفجار پشت هم
۳ یا ۴ انفجار ، صدا از سمت ارتش 92 زرهی بود
صدا سمت  زرگان  کوروش کوی عابدی کم تر و بیشتر سمت کمپولو هست احتمالا لشکر باشه
سلام وحید جان.
تا ۲۲:۴۵ صدای ۵ انفجار شنیده شد که یکی از باقی بسیار صدای بلندتری داشت برای مایی که در نزدیکی پایگاه گلف و الحدید هستیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77073" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuZIkiz-br0czFeXQWqjIsZWwdteL7FIKvC0VIl74Q3WYKMplnXmVmFKU8rEgpZyYAXFaakaDrOkwMDl-0dkUCfiwP392eLotRG3qj5F12vHv0-Y5jm9LXtp5yhzvz3bx6iJmf_r8t3ISLwsQA7vl-MGoasLvveZpPcsPVl1nep0j3xVt5_U2sRYMNycTq1FoplBjVN7H6o76xnAT_zGwCLtLJ_sHCfaEN2sEkUJzBJW_74kuKPsR5lEAgS7N95En5HyDvrSrLeCpS4E-YJyIvBjInPGL3IXesQ3cQ7p5o-lgbMqF0zpekZZxKFM-kPbzeGjqDaOtOgpc_CSrxQgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس به نقل از مقام‌های آمریکایی و اسرائیلی گزارش داد که رئیس‌جمهور آمریکا روز پنج‌شنبه در یک تماس تلفنی، به نخست‌وزیر اسرائیل گفت که این کشور باید خروج تدریجی نیروهایش از سوریه را آغاز کند و او را ترغیب کرد که اقدام مشابهی را در لبنان نیز انجام دهد.
بر اساس گزارش روز سه‌شنبه ۲۳ تیرماه این وبسایت، یک مقام آمریکایی گفت دونالد ترامپ به بنیامین نتانیاهو تأکید کرده که حضور نظامی اسرائیل در خاک سوریه تنش‌زا است و می‌تواند به تشدید درگیری‌ها منجر شود.
به گفته این مقام، ترامپ به نتانیاهو گفت: «آن‌ها شما را آن‌جا نمی‌خواهند. باید نیروهایتان را خارج کنید» و افزود که همین موضوع درباره لبنان نیز صادق است.
در مقابل، دفتر نخست‌وزیر اسرائیل اعلام کرد: «نخست‌وزیر بر ضرورت ایجاد مناطق حائل امنیتی در امتداد مرزهای اسرائیل تأکید کرده است».
این تماس، یک روز پس از دیدار رئیس‌جمهور آمریکا با همتای سوری خود، احمد الشرع، در حاشیه نشست ناتو در ترکیه انجام شد.
به نوشته اکسیوس، سه ماه مانده به انتخابات پارلمانی اسرائیل که برای بقای سیاسی نتانیاهو حیاتی است، بعید به نظر می‌رسد او گام‌های مهمی برای عقب‌نشینی نیروهای اسرائیلی از مناطق تحت کنترل در سوریه بردارد یا فراتر از آنچه پیش‌تر در لبنان پذیرفته، با خروج بیشتر موافقت کند.
ارتش اسرائیل در حال حاضر بخش‌های وسیعی از جنوب لبنان و جنوب سوریه را در اختیار دارد.
اعضای ارشد دولت اسرائیل خواهان کنترل نامحدود بر این مناطق هستند و برخی حتی از ایجاد شهرک‌های یهودی در آن‌جا حمایت می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77072" target="_blank">📅 21:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRREsk1xNRNvsO8-iZVUfimELM-4nqxfE2T5jFFzMvi_kq3R4d_fAYFYFIJfxOeAbysXg9FeTRneODB8b4GnJ4Deh7HgxhSNKt5JZsQfcwXrx8TZelY2ZsRYuWBjtPGC4vsFQz6EUBkw8CBiJn5YIghZ6K_J0PWjNyL2oLZomkESRsNfPn1vuU10-rWMPpgokZRsTt39PhQm4OzX0YcCcNGNYoPd6dNm5TOVbEX-kwV6ugKz7va3tlhYbZWNSfUkB7hd2F8kC3CykO6dnc59A_oPf84kFk1g7O1zJGPNj1dGeavqXwkGZdjRRGPQ15TlKf3cKAiad6BcvSm00vSunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه عربستان سعودی روز سه‌شنبه ۲۳ تیرماه با «محکومیت و انزجار شدید» از حملات ایران به چند کشور عربی، تهران را «مسئول عواقب ادامه این حملات ظالمانه» خواند.
در بیانیه این وزارتخانه، از هدف قرار گرفتن تعدادی از پاسگاه‌های مرزی کویت، یک سکوی حفاری دریایی متعلق به شرکت نفت کویت و حملات به سرکنسولگری کویت در شهر بصره عراق خبر داده و با اشاره به حمله ایران به اردن، بحرین، قطر و دو نفتکش اماراتی هنگام عبور از تنگهٔ هرمز، از «تداوم تهدید امنیت و ثبات منطقه توسط ایران» انتقاد شده است.
وزارت خارجه عربستان در این بیانیه «مخالفت کامل» خود را با آنچه «نقض حاکمیت کشورهای برادر توسط ایران، ادامه رفتار بی‌ثبات‌کننده آن در امنیت منطقه، و نقض اصول قوانین بین‌المللی، منشور ملل متحد، منشور سازمان همکاری اسلامی و اصول حسن همجواری» خوانده، اعلام کرده است.
عربستان ضمن درخواست برای توقف حملات ایران، بر همبستگی کامل ریاض با کشورهای هدف قرار گرفته، تاکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77071" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GED4Rr6M1Pt4HQ3KuJZf37JSVy_MVrSOdbj-WxNID6v_gwPVDqjA44uaPIOJAQAQMvtfKjmSeyhu8DT8e8JVofaICxDirzxpRjZ5NxiF1w-kRWMRugvKbkQV5bg9Auc-t0bFP1wgVwtgx0XnGY3Ux8rafFtmlWgAWxYilCxBA0yor3JRPDTCaCZ9qneQfWVFISWPEaOo3VxKMOeLkpECeR25EO19fSnHM8WnSrYzhpQIpqHNddAHD6H96ZCHCXO0BHj1GXDV8IEOpkOcefYjFH-wrgQ_Pkocj3kkgDkGJiW5Tm6tjA68T3tCrL9F4zxqh_mjgYM4PBCyNBy7b64zvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا عصر سه‌شنبه ۲۳ تیرماه و ساعاتی قبل از آغاز رسمی بازگشت محاصرهٔ دریایی بر بنادر و کشتیرانی ایران گفت هیچ‌کس نباید برای عبور از تنگهٔ هرمز عوارض یا هزینه‌ای دریافت کند.
دونالد ترامپ در یک نشست خبری همراه علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت که پس از اعلام قبلی‌اش مبنی بر دریافت ۲۰ درصد عوارض بر کشتی‌های عبوری از تنگهٔ هرمز، کشورهای مختلفی با او تماس گرفتند و گفتند به‌جای دریافت عوارض برای عبور از تنگه، مایل‌اند در آمریکا سرمایه‌گذاری کنند.
او با اشاره به کشورهای حاشیه خلیج فارس گفت این کشورها قرار است در آمریکا سرمایه‌گذاری کنند و فکر می‌کند این موضوع راه‌حل بهتری در مقایسه با دریافت عوارض است.
رئیس‌جمهور آمریکا با تمجید از علی الزیدی گفت اگر عراق به حفاظت نیاز داشته باشد، ما در کنار آن خواهیم بود.
او گفت ما در بخش نفت با عراق همکاری قوی خواهیم داشت و به زودی آن را اعلام خواهیم کرد. نیروهای آمریکایی عراق را ترک می‌کنند و شرکت‌های آمریکایی وارد می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77070" target="_blank">📅 20:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=mTJ0h_aM1b-tJUsdDC4SkqnkW6d0TpYFOVLZkKsJq6qSmE9kzXtMya8wfBSXDhyW9_BlPEKrbHUwB7_oXSMBz7rqh0oMj__MFHpqHdt97E_qVyj3ml0whzEh2UimfveEXysP4dt4Ffuv8MCUmxDNSQmeGLUCYKvNRw_3uHexPi0ZL3_YQGmH54PBCGHK3FhQwH7k0PJNmlf5IiQHwMPOsUvLL_YRUkHb5byo1nOQpFP9Qf6ReVHObdZo4HVLS5FfOkzZz0uPCjQYDASxF4rT3Bf_SoRAq-oLpPI8pFmCRumZBmeQqkR3ssUA2EIuFKlQmpaZ1OnK0L5Y7UbGVrl7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=mTJ0h_aM1b-tJUsdDC4SkqnkW6d0TpYFOVLZkKsJq6qSmE9kzXtMya8wfBSXDhyW9_BlPEKrbHUwB7_oXSMBz7rqh0oMj__MFHpqHdt97E_qVyj3ml0whzEh2UimfveEXysP4dt4Ffuv8MCUmxDNSQmeGLUCYKvNRw_3uHexPi0ZL3_YQGmH54PBCGHK3FhQwH7k0PJNmlf5IiQHwMPOsUvLL_YRUkHb5byo1nOQpFP9Qf6ReVHObdZo4HVLS5FfOkzZz0uPCjQYDASxF4rT3Bf_SoRAq-oLpPI8pFmCRumZBmeQqkR3ssUA2EIuFKlQmpaZ1OnK0L5Y7UbGVrl7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه ۲۳ تیر، در نشست خبری مشترک با نخست‌وزیر عراق در کاخ سفید، اعلام کرد که خاورمیانه در حال تجربه وحدتی بی‌سابقه است و دیگر خبری از ترس و وحشت ناشی از «قلدری» ایران در منطقه نیست.
ترامپ با بیان اینکه ایران پیش‌تر با رویکردی سلطه‌جویانه، کشورهای منطقه از جمله عراق را تحت فشار قرار می‌داد، تاکید کرد که اکنون توان نظامی این کشور درهم‌کوبیده شده و آن فضای رعب و وحشت از میان رفته است. او در بخشی از سخنان خود به سرکوب معترضان در ایران اشاره کرد و یادآوری کرد که آن‌ها ۵۲ هزار نفر از معترضان را به قتل رسانده‌اند.
رئیس‌جمهوری آمریکا در پایان ضمن اشاره به نزدیکی کشورهای منطقه به یکدیگر، نخست‌وزیر عراق را به عنوان یکی از رهبران بزرگ آینده در خاورمیانه توصیف کرد و افزود که این اتحاد منطقه‌ای، در سایه پایان یافتن دوران سلطه‌گری ایران، اکنون به واقعیتی دست‌یافتنی تبدیل شده است.
@
VahidOOnLine
دونالد ترامپ در نشست خبری با علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت: «نخست‌وزیر عراق در انتخاباتی پیروز شد که بسیاری تصور می‌کردند فرد دیگری برنده آن خواهد شد. من هم در این موضوع نقش داشتم و برایم مهم بود کسی روی کار بیاید که بتواند این مسئولیت را به‌خوبی انجام دهد. اکنون یک قهرمان جدید و فوق‌العاده داریم و حضور او در کنار ما مایه افتخار است.»
ترامپ افزود: «شرکت‌های نفتی آمریکا با حجمی بی‌سابقه وارد عراق می‌شوند، با این کشور شراکت می‌کنند و همکاری گسترده‌ای خواهند داشت. روابط ما اکنون به سطحی رسیده که دیگر نیازی به حضور نظامی آمریکا در عراق نیست. ما برای کمک به عراق حضور داریم و اگر لازم باشد از آن حمایت خواهیم کرد، اما فکر نمی‌کنیم چنین نیازی پیش بیاید.»
او درباره جمهوری اسلامی گفت: «ایران رقیب اصلی عراق بود و بار سنگینی بر دوش این کشور گذاشته بود، زیرا قلدر خاورمیانه محسوب می‌شد. اما اکنون ایران تا حد زیادی تضعیف شده و توان نظامی آن تنها بخش کوچکی از چیزی است که چهار ماه پیش بود. این وضعیت به عراق آزادی عمل بیشتری داده و یکی از دلایل ورود گسترده شرکت‌های نفتی آمریکا به عراق نیز همین موضوع است.»
@
VahidOOnLine
ترامپ با یادآوری دوران فعالیت خود به عنوان یک چهره غیرنظامی، گفت: «من همیشه می‌گفتم به عراق نروید و به آن حمله نکنید».
او با انتقاد از این مداخله نظامی و با اشاره غیر مستقیم به ایران، افزود: «صادقانه بگویم، آن‌ها به کشور اشتباهی حمله کردند و آسیب بسیاری به بار آوردند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77069" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BM0PmHC7Xv6rk52uWhlw26V6qGCUGWOIVeo43N1B_OFnLZmvRIyexu3vi-SxEPkwiDOPYdLVsnNVMZcR1Hwf4xPuULPXKHeizCBZrN00cWtpRtfWfKvqyzYdbz9Rez2RBW0TAk3ZgHLJB4BCN_kSCWgtzY_TCcBDvb4itt7WAftKwK2Zn4-KGK4zxGKnq3wWUVahX2HBEVF7v20iSMD_L5YJe099vOcHKNhJEhKf8KjQWqFNvIAXbdt5AY8SUZ3EHjPJXm5X3YhpgQj5e7ni_T2AjXyxwgTryBzP1hgJsYvUlzT5Inu5KiL_moXm7dOl-uLcCE366WYqEZ15OrTjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار خطر در کویت، همین الان
رسانه‌های ایران عصر سه‌شنبه بدون بیان جزئیات بیشتر از شنیده شدن صدای انفجار در اندیمشک و جزیره قشم خبر دادند.
صداوسیمای جمهوری اسلامی به نقل از استانداری هرمزگان گفته که ساعت ۱۹ به وقت محلی، «نقطه‌ای» در جزیره قشم هدف حمله آمریکا قرار گرفت. صدا و سیما همچنین از شنیده شدن صدای انفجار در اندیمشک خبر داد.
هم‌زمان، ستاد کل ارتش کویت با صدور پیام هشداری از رهگیری «اهداف هوایی متخاصم» در این کشور خبر داد.
در بیانیهٔ ارتش کویت با درخواست از شهروندان برای رعایت دستورالعمل‌های امنیتی گفته شده که صداهای انفجار احتمالی ناشی از فعالیت پدافند هوایی در رهگیری حملات متخاصم است.
خبرگزاری فرانسه هم از شنیده شدن صدای انفجارهایی در کویت خبر داده است.
@
VahidHeadline
سپاه پاسداران در بیانیه‌ای حملات شامگاه سه‌شنبه به «مواضع دشمن» در خاک بحرین و کویت را تایید کرد و گفت عملیات «نصر۲»، پاسخ به حملات عصر سه‌شنبه آمریکا به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی بوده است.
در این بیانیه آمده است، در صورت تکرار حملات، مقابله به مثل جمهوری اسلامی ادامه خواهد داشت و این «تجاوزها» نتیجه‌ای جز تاخیر در بازگشایی تنگه هرمز ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77068" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIr7N0g1xM7iBTt0sfpW7mdywG6RF3y92k5vWYVlVyiXAhvBKlKKV2XJ6iG688ekoSFaYFc1eI-Xs2KBUfvBryN9Gpc-50-LTUEcrzCPMDy5-jyowTcvheFcEcWIMth4bP12H-LAsBA4WomXd8AAxh7rj0DBFlVU3cyBysJYkNLVh0N05JilJlwQYG9DdKJtJJRROmUMOcquRvHmglyJoTEfXOpFU71A1_ynRcVFPOUCFcJ7-kdKVtgKshYbfhIzrBc7LK201n62z33PQZ4lNQdes8xET_GLWGQBqRAcpy7T1qD6hXBsLjHHrADbxcifRX0eU7TkJyL3fCxKLSq72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌ها و محموله‌های مرتبط با ایران، باز است
ترجمه ماشین:
نفت به لطف قدرت شگفت‌انگیز ارتش ایالات متحده، بیش از هر زمان دیگری در جریان است. درود ویژه به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دن کین، و فرمانده ستاد فرماندهی مرکزی ایالات متحده، دریاسالار برد کوپر. به لطف آن‌ها و همه اعضای قدرتمندترین ارتش جهان ــ با اختلاف بسیار زیاد ــ تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌های ایران، باز است؛ و این به‌دلیل رهبری دروغگو، خشونت‌طلب و بدخواه ایران است که این کشور را به مسیر نابودی کامل می‌کشاند.
بنابراین، ما یک محاصره کامل خواهیم داشت، اما فقط علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هر چیزی مرتبط با محموله‌های ایرانی حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده با رهبران خاورمیانه،
تصمیم گرفته‌ام «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌های تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حاشیه خلیج فارس در ایالات متحده انجام خواهند داد.
این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.
همان‌طور که همه می‌دانند، ما بیشترین میزان سرمایه‌گذاری دلاری در ایالات متحده از سوی هر کشوری در تاریخ را داریم، اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهند کرد و شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطوحی تاریخی خواهیم بود؛ امری که میلیون‌ها شغل پردرآمد دیگر برای آمریکایی‌ها ایجاد خواهد کرد!
آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای بی‌سابقه. دوران کشته شدن صدها هزار نفر، از جمله ۵۲ هزار معترض، به دست ایران به پایان رسیده است و مهم‌تر از همه، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77067" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4730c53847.mp4?token=LqvlpICuiReDNT-y4X8Ab5ium0p4nkK5L1iUbLuVgUqkZhV4fuThEMPUOgyM3F4zDzlIeq-ph9XSkmL6mq8f29SWm9iOQB13O7lI6Ss9kA-r7LKjWhC6ssOnpyfMa1Gldy7hgNnN8A0eXILd6tKsAte16K0Ua5xXcg-FhKYLxLVNm6o-nvRcS5b_6tAuGPq3VwtT08kB9SgmppDlWks65zPGA4oi0gzpY6RZYRR6QQUYtVm7rDgJBhviB3xsGYhc95KXmVTsrNUxAyNgpA8Y1lT0V6mZ1lz8sCsYj-qZonlL_cbT_RWYlHgFseuJPbTB0twVUv5v5VoWMAQbVDyC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4730c53847.mp4?token=LqvlpICuiReDNT-y4X8Ab5ium0p4nkK5L1iUbLuVgUqkZhV4fuThEMPUOgyM3F4zDzlIeq-ph9XSkmL6mq8f29SWm9iOQB13O7lI6Ss9kA-r7LKjWhC6ssOnpyfMa1Gldy7hgNnN8A0eXILd6tKsAte16K0Ua5xXcg-FhKYLxLVNm6o-nvRcS5b_6tAuGPq3VwtT08kB9SgmppDlWks65zPGA4oi0gzpY6RZYRR6QQUYtVm7rDgJBhviB3xsGYhc95KXmVTsrNUxAyNgpA8Y1lT0V6mZ1lz8sCsYj-qZonlL_cbT_RWYlHgFseuJPbTB0twVUv5v5VoWMAQbVDyC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۲۳ تیرماه هشدار داد که اگر تهران حملهٔ جدیدی به کشورش انجام دهد، اسرائیل با تمام قدرت به ایران ضربه خواهد زد.
@
VahidOOnLine
ویدیویی که دفتر نتانیاهو منتشر کرده، ترجمه ماشین:
ما برای هر سناریویی آماده‌ایم. فقط یک چیز می‌توانم به شما بگویم... نه، این را به رهبران ایران می‌گویم:
اگر به ما حمله کنید، روی آرامش حساب نکنید. تصور نکنید آنچه در گذشته رخ داد، دوباره به همان شکل تکرار خواهد شد؛ زیرا این بار، تکرار گذشته نخواهد بود.
حمله قبلی به‌اندازه کافی قدرتمند بود؛ حمله بعدی بسیار قدرتمندتر خواهد بود.
دورانی که کسی به ما ضربه بزند و ما با ضربه‌ای چند برابر پاسخ ندهیم، به پایان رسیده است. این کار را در برابر محور شرارتِ ایران انجام دادیم و در برابر هر کسی که به ما ضربه بزند نیز به همین مسیر ادامه خواهیم داد.
روش ما همین است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77066" target="_blank">📅 17:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYGIzrWSGZoEataKUjf24sQclXdO85DUrMD5fAq7tOvsLqQcnQ0mXx567lxayGMWNXWfJHlN6GrOEs4v3ij-inHJohQuXy11YFXXl5n--YSjtrWXkqj5O1QY-KGkONKYW4c5VXL_MmTVr9hLlJe6-quRnRMYjSy70RBGQiOIUdd6yASCbrzIKSQkvyxZm_7GdX7WwRkCE0D9vK1Ci0Wxnx1_TO8SJ6G1v2tzrWmBgWOm83NHZ5bYddWE6XdFk2mmDSQujQGJrjQIZE2S6yU2Wc89ahkBXJ2n-eP7xtP_MOgxWbsvHWQVqSbImN56o8rYX4-l3ViMwchU2LgQnh0Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع ارشد در تهران گزارش داد که اگر دونالد ترامپ تهدید خود برای حمله به تأسیسات زیرزمینی موسوم به «کوه کلنگ» را عملی کند، جمهوری اسلامی «پاسخی ویرانگر» خواهد داد. این تهدید در حالی مطرح شده که کوه کلنگ طی سال‌های اخیر به یکی از مهم‌ترین و امن‌ترین مراکز هسته‌ای ایران تبدیل شده است.
دونالد ترامپ، رییس‌ جمهوری آمریکا، روز گذشته در گفت‌وگویی رسانه‌ای اعلام کرد که واشینگتن یک مجموعه زیرزمینی عمیق در ایران را به‌دقت زیر نظر دارد. او مدعی شد هرچند در حال حاضر نشانه‌ای از فعالیت آشکار در این مجموعه دیده نمی‌شود، اما آمریکا ممکن است به‌زودی «ضربه‌ای سخت» به دهانه ورودی این مجتمع وارد کند.
کوه کلنگ گزلا که در رسانه‌های غربی با نام Pickaxe Mountain شناخته می‌شود، در استان اصفهان و در فاصله حدود یک‌ونیم کیلومتری از تاسیسات غنی‌سازی نطنز قرار دارد. به گفته کارشناسان، این مجموعه به دلیل عمق زیاد و استقرار در دل سنگ‌های سخت گرانیتی، یکی از مقاوم‌ترین تاسیسات زیرزمینی ایران به شمار می‌رود.
برآوردهای فنی نشان می‌دهد سالن‌های زیرزمینی این مجتمع در عمقی بین ۸۰ تا ۱۰۰ متر و در برخی نقاط تا حدود ۶۰۰ متر حفر شده‌اند؛ ویژگی‌ای که آن را حتی از سایت غنی‌سازی فردو نیز عمیق‌تر می‌کند. به همین دلیل، برخی تحلیلگران غربی از این مجموعه به‌عنوان «دژ هسته‌ای» ایران یاد می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77065" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J9_apNyVUrQIcXymTGq5gDh6XX7wH1OMdt1hpn75vtaQi6f8XBK5Y-kTVhl1aoXSrVlrQZNV0KdCf2_ar_H9oB7KE2YSNM9mA21NzKnEGb5ujGupP0BLQmpeJUft74ZbaeQEnLWbLFs6ri0SiCYIgubPE9Gsxxx2uR7fBGWM4RQUZe0WsvdxFGjJPXw20l6VI2k9AR3Gws5SfWHx595FHOK9YEOF53gmTC1SL9M_jPv10UYFat4xUwxNTwoTXRG0MtqtwWegKUp02GS3HoC6Td57AhMrKkylMvK8tQBAK6e9EJQI7jrs0Dge92CDVlo4ntt5Tcu-Y7SkolTgMI3s1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NolYo7kYqdMwGvtKD_nBaYwzBhQYWIbn4LDefVdJtlUnzkJ-XiK4f_WC51DMOirB5rYB8GX47vTU35mNL9f2vv_rrXBJpvVJHME9oDVNRP9_xT4eKmpLmuF1VeFYZoOEf0rwaDzdu9ZzT1z_ndYUOnfyRKT9v-9mYO69zysR89LWLUMVJ6NMHiSpTnKGzBrJEuLh0CJO5Me-7Ft3NWlvq0y5r8Rz3oYG25CB_PbmGH7FW-SzdqZh3DlOuWv6TLL1mJnHTHbc5PNXIjPx-n0D9A1WQ6v9fBZOhSxDwXsmFTWnzV1SQZQ97AT0rBVtphgNTeI0bkZOTU1YvUEw9mlG5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت نفت در بازارهای جهانی روز سه‌شنبه ۲۳ تیرماه و همزمان با تشدید درگیری‌ها میان جمهوری اسلامی ایران و ایالات متحده آمریکا در تنگه هرمز از ۸۵ دلار گذشت.
@
VahidOOnLine
قیمت ارزهای خارجی در ایران در روز سه‌شنبه ۲۳ تیرماه افزایش قابل توجهی پیدا کرد و نرخ برابری دلار آمریکا به ۱۸۴ هزار تومان رسید.
قیمت سایر ارزهای خارجی هم افزایش یافتند و قیمت یورو به حدود ۲۱۰ هزار تومان رسید.
در کنار ارزهای خارجی، قیمت سکه طلا هم به ۱۸۰ میلیون تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77063" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pe0cBxsPUMTBTzUua0eAJFSnE-yuHc7z70JcU-NNhI50LthZhLBQMON4fFH4fS1P2r2qVpTEc8uCmGv9gTS21r77cLHsfbOQwtToi3gBjc10omSH7Yo6x5wM67EplpgNLRhqVGSGZR6ghWCoDDxRL_lSeulEnse2R_mcZgL5ypWMhd9n7uGYUsRKhqV7B0g1opKsPsABi42HXDE-G0ELRSd8O-fwFXSZzgx-NgAhcP8TmDW96ceQHs-tcwQOrGHGEnn9n95oR7DjgU7eSEsOurrAKEiT5EFG1T3TRQ6sB1N4TfpRepEN7plHnsL4I5hxgnyhJ_l-f5faY5Hu2QoURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-Ny5OpbjReo7Rj2aLpsjAY3tZLTagp0dT3Os_vel0iIZls7pF941Mx-qp7D5jHAOCWrdtauHgepyJngOgBUN2_EndhlDdSH7GEgjOiK833A_z1YbI9nU_PtCbpmP3YtggGQ6881vhB7x4mkdqOrdBBoJR3qheyeqNCLEuswwb5LTE7CI0B05VWyOVUnP4mswDtfnHye-IANzgyPm9cEu9MYd588Bu6F0i8m3xW9EgXm-hOymD19V5yHmg21PLQXxFL0Lwk_c0RMj0-IH2mr4ljdGPKwsOxUP65U3CXQrIoo8PtDPgk3BSndhKcGpItHSVJpqyLFPwxOerYanN3Oow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در…</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77061" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXwiD8Osspi3qQ00sZ53qm5dYBcOEkDa_VvbpTByHDeschFESIYhTTSl-znXBCRjXFn-CZAex1ifkncWbfkUkP1RkZeS64_SODKtLVep0Tfi_-SFYBP7RrIf4XSJyF3FuG8yr9rLVwUwfVoVTO3_FYi39q6OLgj13WRsfjtc8ioM5lPt0QS3wauQSJe7EMu390qdct-VW-iKLM3dxS8LQYykIB07at9_VTivPSue-g8xmxJAtNYaLILqbpqTNGrouuGg-EftsFFUUs0ld2fnCgajRBa6MZXSgDRltLuDJvwFSKuQuY00Tq37aBCRbtA2IV3PH45SwwfboGs5AK6iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی صبح سه‌شنبه ۲۳ تیر از اعدام دو نفر به اتهام «بغی و قیام مسلحانه علیه نظام جمهوری اسلامی»، خبر داد و و آن‌ها را که آن‌ها را از اعضای گروه داعش معرفی کرد.
قوه قضاییه نام این دو را محی‌الدین عبداللهی و حسین پالانی اعلام کرده و می‌گوید آن‌ها اعضای یک «هستهٔ وابسته به داعش» بوده‌اند که در ارتفاعات بمو در نوار مرزی ایران و عراق و پس از یک درگیری که به کشته شدن سه عضو سپاه نیز انجامید، بازداشت و محاکمه شدند.
جزئیاتی از روند این محاکمه منتشر نشده و شرایط برگزاری دادگاه و دسترسی آن‌ها به وکیل و دادرسی عادلانه نیز مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77060" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=XEPOeMhwkxLW-Net0E27b-f_C4HQemwunZBiw6ih2kpDGn25xawFbtRPcNunTq8XHSalIJbnFN4riboeADQtOMN0_3bwV8B2G6yi2pE0AvcwpvPTcmI3x4VWXrQOg2r1b37VBdr7JrHjf6pXHGshp3dXu1dLjkcOzzUfg7e8boiYnwhGUBUFw3tb7H_nwa8fvAvzljdxwYAI663ZxXil5JiVTSxtB45SENP2aVKDynGAY_wZI_pVvswk17sSjNbP6ubztVfPBm2pJLa0qX9I2CTvDtOykIazF4UI4KINkFOpsQHXx8kybrb03VQAwNjMHjJpY9iBra9qznR05sfl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=XEPOeMhwkxLW-Net0E27b-f_C4HQemwunZBiw6ih2kpDGn25xawFbtRPcNunTq8XHSalIJbnFN4riboeADQtOMN0_3bwV8B2G6yi2pE0AvcwpvPTcmI3x4VWXrQOg2r1b37VBdr7JrHjf6pXHGshp3dXu1dLjkcOzzUfg7e8boiYnwhGUBUFw3tb7H_nwa8fvAvzljdxwYAI663ZxXil5JiVTSxtB45SENP2aVKDynGAY_wZI_pVvswk17sSjNbP6ubztVfPBm2pJLa0qX9I2CTvDtOykIazF4UI4KINkFOpsQHXx8kybrb03VQAwNjMHjJpY9iBra9qznR05sfl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در منابع حکومتی:
'حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77059" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fuWblmLq7PBOLjyTXdfbMZ0q-v4VkxmmxEPKfxufvV_akWauWkjNSiZY9TA6iqEXIjoISribfsvTQRoThEJu17DXb8TtofdmqDqrTI__B_tPG5hP6Z3D6CTKc_YLXsogewpElDHOdoCo2jeW3ZgXuaaQBQX_kcqOwAdX4jnYXnagofZuZbv0IhQLe_7eYshI3SYvfzKtWyU-gUEpDVz3dXT952BEEY1Dp5pWpBue8qmet7gULvnaZW-wtbqtip3RfK4Jdmd9Lj2eQlMHvdJId4or49-gPBPujH3H4TWglOKwge_u5W4z64L0RXwbPDRU0dugDOumdCbSAGVfeTY8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'مرکز آماد و پشتیبانی دریابانی نیروی انتظامی بوشهر محله بهمنی، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77058" target="_blank">📅 15:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J__6rJfbSK3tsebTDhGr8zwQ1nCMtQxMlB66C2euxZ1NN4QIFxDNaUK4MdhTdQRccwdnMKS3E0iLw7I2TvPXYE3F65Q_lWdbrx3rrw7A6g4H150IRe5CbrTdkRMv-w-MhTqnkAewESbXr94zqkkuYkjGQUM2rEKebQxlFAboqNXD7kpVxwpUTuPl8N_mbOUS7ZRTy8GYlNBfX5QAeu2mo8IGfKrs_0JvKiVzmA7u7s2WG8x463xTx-7F3PJ3orfP6R1VvreY-w__OjEd4-JjaFn8TnEgU4DIW8KuGJKl014mWIQNZll2hhatuRxP09-UJxl_ssuHA_8QaF3kW-_7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=HKaNFf5i1bzTkSWheLKm_hBQDUorLCoKSax7banS7rNtY05RdQsbSpfFVdRr5D4COOYUPS07unz04N0cQqWfRvET1dABkPPrEtJPODNfuyom_72JgOoHrA7dg88xzldDtF4Tmel0WmJALQMsrSrxaX_ubQD98EjVGWY8cvgo5VdzGhI0lUqO4D8jI9V0Ili_PTeiQ-0iwSjnLW6pEkU3cilMiVljZ97WQKN6nQVVYRI7RlfHJan16BL5Ylj8zmMt2NduAiNerLqQIdUFdRpIgD_wJxWlbUSMeyVcjpZHruUm4VCd1o0FCf2SY-OlgrLVM8IVtO1DiyJvYWcEjc48gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=HKaNFf5i1bzTkSWheLKm_hBQDUorLCoKSax7banS7rNtY05RdQsbSpfFVdRr5D4COOYUPS07unz04N0cQqWfRvET1dABkPPrEtJPODNfuyom_72JgOoHrA7dg88xzldDtF4Tmel0WmJALQMsrSrxaX_ubQD98EjVGWY8cvgo5VdzGhI0lUqO4D8jI9V0Ili_PTeiQ-0iwSjnLW6pEkU3cilMiVljZ97WQKN6nQVVYRI7RlfHJan16BL5Ylj8zmMt2NduAiNerLqQIdUFdRpIgD_wJxWlbUSMeyVcjpZHruUm4VCd1o0FCf2SY-OlgrLVM8IVtO1DiyJvYWcEjc48gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا برگزارش شهروندان از حدود ساعت ۱۲:۴۵ بار دیگر به نقاطی در
#بوشهر
حمله شده و بیش از ۱۰ انفجار رخ داده.
تصاویر دریافتی، سه‌شنبه ۲۳ تیر
#Iran
Vahid
از بوشهر پیام میدم
ساعت ۱۲ و ۴۴ دقیقه صدای انفجار امد اما کم بود
سلام وحید جان
ساعت 12:45 دوباره بوشهر رو زدن
بوشهر ساعت ۱۲:۴۵ ظهر منطقه بهمنی صدای انفجار خیلی نزدیک بود. خونه لرزید
همین الان ساعت ۱۲.۴۲ بوشهر منطقه بهمنی رو زدند(احتمالا پایگاه هوایی ارتش یا پایگاه دریایی سپاه ریشهر) زدند. صدای دو بمب شنیده شد.
سلام بوشهر ۱۲:۴۷ شدیددد صدای انفجار میاد.
درود وحید جان ،بوشهر الان دوتا محکم زدن
الان بوشهر و زد ۱۲:۴۴
به نسبت اخیر صداش نزدیک بود پس میشه حدس زد فرودگاه بوده دوباره زد ۱۲:۴۷
الان زد باز ۶/۷ تا انفجار بزرگگگ کارخانه جاته چون خیلی نزدیکه ۱۲:۵۴
۱۲:۴۷ بوشهر حدود ۴، ۵ صدای انفجار اومد. نسبتا شدید بود.
۱۲:۵۳ دوباره دارن میزنن.  حدود ۷، ۸ تایی زدن الان.
سلام   بازم بوشهر داره صدا میاد از ۱۲و ۵۲ دقیقه چندین صدای انفجار اومده
ساعت ۱۲:۵۳ دقیقه حداقل ۱۰ تا موشک به بوشهر زدن
از ۱۲:۴۰ دقیقه نزدیک به هفت هشت بار دارن میزنن بوشهر رو. خونه می‌لرزه!
وحید جان بوشهر رو ده دقیقه یک ربعه دارن همینجوری رگباری میزنن…
خیلی میزدن انفجارا همش دنباله دار بود مشخص نیست چنتا بود
حدود ۱۰-۲۰ ثانیه یه کوب صدا انفجار قطع نمیشد
وحید جان  رگباری باز بوشهر منطقه ریشهر رو زدن وحشتناک بود
ساعت ۱۲۵۸ دقیقه اسکله والفجر بوشهر را با ۸،بمب زدن، انفجار شدید
سلام ساعت ۱ ظهر صدای انفجار مداوم بوشهر
از ساعت 12:30 تا 13:15
بیش از 15 بار صدای انفجار مهیب توی بوشهر شنیده شده و موج خیلی زیادی داشته
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77054" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌های دریافتی:
باز بوشهر رو زد
سلام دوباره بوشهر رو زدن
دوبار بوشهر زدن ۶و ۷دقیقه
حدود ۶:۰۷ باز بوشهر رو زدن.
بازم زدن ولی صداش به مراتب ضعیف تر بود.
🔄
سلام وحید الان ساعت ۶.۱۳ دقیقه باز کنارک زد خیلی بد زد
چابهار ۶:۱۴ زدن
بازم چابهار همین الان ۴ تا شدید زد گفتن تموم شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77053" target="_blank">📅 06:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=HewXI5AJFJIHNfOsDGyzCyi09nVqBODJAuPwn-ZTbSft1tNKazdwueLP2Oh_XmUCk1YYgFLpHhAAYn7z328IjXT9MOpwVc0HuCS879jSYTzBgFuFVK8bjcGmWstR0lpKzoOHP7IA3AbCupd5_z19EA5sOLrjmsbstc5pBFrhtSanayIPFGyXUU0ExV6Ng5iIG9Yw3yoS_iAAS27Vh5JLWgB9MbahpmU_bauYtl4UtfXC-chM2BLV-81GgsRFZu4UMMxX0pBP122dXl4olWH9dD5PWy9kREiKj8X1HNM1VFem3YL8ozeni9Zpqpy4Mwn-AZahwKxAVqCDyCaIij3m3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=HewXI5AJFJIHNfOsDGyzCyi09nVqBODJAuPwn-ZTbSft1tNKazdwueLP2Oh_XmUCk1YYgFLpHhAAYn7z328IjXT9MOpwVc0HuCS879jSYTzBgFuFVK8bjcGmWstR0lpKzoOHP7IA3AbCupd5_z19EA5sOLrjmsbstc5pBFrhtSanayIPFGyXUU0ExV6Ng5iIG9Yw3yoS_iAAS27Vh5JLWgB9MbahpmU_bauYtl4UtfXC-chM2BLV-81GgsRFZu4UMMxX0pBP122dXl4olWH9dD5PWy9kREiKj8X1HNM1VFem3YL8ozeni9Zpqpy4Mwn-AZahwKxAVqCDyCaIij3m3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا نوشت: نیروهای ایالات متحده حملات جدید علیه اهداف نظامی ایران را به پایان رساندند
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) تازه‌ترین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب به وقت شرق آمریکا در ۱۳ ژوئیه به پایان رساند.
در جریان این مأموریت پنج‌ساعته، نیروهای ایالات متحده با موفقیت اهداف نظامی در نقاط مختلف ایران،
از جمله بوشهر، چابهار، جاسک، کنارک،  ابوموسی و بندرعباس
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری را بیش از پیش تضعیف کنند. نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران را هدف قرار دادند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77052" target="_blank">📅 06:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=bSRFMneXf3kXepdMLYnNtw-xNZAzfwArz1PxMxVJ1EDL1fAhsyKI34A6JcGXgSeUGFyXtE8Rp9psxCnzXuCOTgxVhBuhK7Dw4MFrqzvrTWXUa1cUcCD1cGRbFVcaDR8gcNru1hs_xlUEp_Qw2nj2vg5XpGiAB9JFQoSb8z_VHMEuKwl-h4avtaRsB3RCOnmCtTrWbxWrkAyL6kmuTSFsPniI0p0FyTUkWhzcfmJ9JrSrCfz2_YZxTnNF9fli062KE-42aUZKA57P4iD4odXDCrQw6CyBqwtsQGpg1QCyYbUsWvk2kLdsCEJqa9_lRicGL769Qa3omW1iv9qbJxkd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=bSRFMneXf3kXepdMLYnNtw-xNZAzfwArz1PxMxVJ1EDL1fAhsyKI34A6JcGXgSeUGFyXtE8Rp9psxCnzXuCOTgxVhBuhK7Dw4MFrqzvrTWXUa1cUcCD1cGRbFVcaDR8gcNru1hs_xlUEp_Qw2nj2vg5XpGiAB9JFQoSb8z_VHMEuKwl-h4avtaRsB3RCOnmCtTrWbxWrkAyL6kmuTSFsPniI0p0FyTUkWhzcfmJ9JrSrCfz2_YZxTnNF9fli062KE-42aUZKA57P4iD4odXDCrQw6CyBqwtsQGpg1QCyYbUsWvk2kLdsCEJqa9_lRicGL769Qa3omW1iv9qbJxkd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش: حملات به مقر سپاه پاسداران در سراوان
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77051" target="_blank">📅 05:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
همین الان ساعت ۵:۳۹ صدای انفجار اومد چابهار و خونه لرزید
الان چابهار رو رو زد خیلی سنگین بود هنوز نمی دونم کجا بوده
سلام ساعت ۵.۳۹ دقیقه دو انفجار شدید چابهار
همین الان دوتا دیگه هم زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77050" target="_blank">📅 05:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
الان بوشهر [رو] زدن
دو بار
باز بوشهر رو زد
پایگاه هوایی بوشهر [رو] زدن سنگین الان ۵.۱۲
باز بوشهر رو زد
وحید سلام  بوشهر [رو] باز زدن 5,11
سلام بوشهررر رو زدننن
ولی الان باید بریم امتحان بدیم توی این شرایط
😐
😐
🔄
ساعت ۵:۳۷ موج دیگری از پیام‌ها رو دریافت کردم که از شنیده شدن صدای حدود ۱۰ انفجار پیاپی در بوشهر خبر دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77049" target="_blank">📅 05:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve2sd_AmXsclYDfpcDZwo8yivC-iPZTqlic0RU0CwFtIiSSgd_F-JUc_jVYg2uHbHAOqq7nffSSF1DtoBLpRluMwTonBnDI6eBGlgm4chqiqMaBbxWsurfJZVqH61rzKrp6pqEE3I_kf1RQ1ddXGIRbn0xACIDKxHtwJ0yOU4J9IxOpg6boUY3QTcN5pp2eqnxyx8-PCo-_-6Tq_KyuMNK4yi___1s1GnBDviezHBEpmsy-8PStRR9pK0z8qd-Bj3whuAZ6vW0qNuivPersnGEKuCOiVuAZw-mcfeO9-aECO4lAlmJaqXCY2mle_bxca5ViyDLG-vbjyhJMfXhGcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWVvtTW9KX_eyQhbkVu5gbkrmLebqesUcYwa8cxw4OSI8-6mrHeeIP6UleQ0vxuirUjhbjXUNPuPDQZcRC8Ea_DhXGYV8HpYl-IqHPegDL4CD-4huctUMkVFZ3XVi-vuMpv8_bqbZHifVzSL_Xa7wLQhQDGevYpLd4YnPXIp0zWCsB_YKjEIKsEHY0q16t9S6VtbdglLD7cIC70H-YAAPzHiH5KNLAlUddbWxTnl6w3QtTl2vY64uC_-5GzlbouXIDBt821DO39j57vTymnetJVGGmNY033ilZZRsvFeemTY7XhAjHUmmecHVVCa8Nj3na_ylTY8c6yL93HoTaemzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ow5JzBzX7YT3Td07SXza9AlCi9zraR1DGY_KKu6huTOs_V2Ex_Gl2Vl_nlV48g0v_iMjC9aYmsD7NMtDvuofmWk_m0fPvkwZMwToWdJF_-ub7Qiv540m6iCQZJRz2JXfl1u2mEj9u7YBQjnjP21ceBkVYVbsU1i2IJ72qZPN6Vz4iipHMllNFiBXe5MsiRtJTF6b1R9-JKrfNwgtVmevl76Rt4EYCJ8BnrIkZoowkGHEEZZepe3Scz0opNunhXp0k5YICRStx4hSPUrR9FakRNuA_Wk8W5_l7RxEwZpVYQPFkS4QNB0umG6H5S5W0mxcDtnfr0bviln8W2QeTyOjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKyuofHcVtAtHAQ_VVp9DRR2Fh9cqbnr-D4GDzIeh-3wxxaV-tgZ0FZcsrisNfEqhRjPsRkipmSm54UKfAh_5iLORC1ImejjXWciJrZIJy1Uouc8zTycNUzR7yX8rRuAJcp050olsBXbxBA2kB44tTaTa0tY3jSpIafDs0Y6bfddX-BLMdapXhdoh_IhWc4Rx6ukyihyYbWhJQYudK-9M40avk5VpYofEXGkImvulYCwjvGScI61V_1VrRPgCrFpaIgOa0QLzlKWw2UoibEJ4cBaNxA7-Q5SB1_u89aon7oi-Lb6kmrIKK7uWiOd6BpZ_Ez9PLRJi-OnKKP2i-SgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tdem8ii26z_kPgVDbrLfQ7V6Z2kbE-HTwCmcym-eQ0L3sygP_c7DUdhqM6JAP_U0pMlhcFXi6AQvE3NcmvwMGSbw52LCpKw06Bgu_O3X0SLlW-r2wWGPcdo8ihbRyhIWrWOR8m2wxZezZ6Il0wmNh_SAXRdWU3oS_7e0UaNh2M5Z2YQKk75OYUmZnmiwz2i4DlSiGLFV3NY4TcUmZO9ZI8TjAvzL_PBK2AZcHlStrS9Zjwy-cbzAvo4llYKM513SMTwNqn1HiVCSBo8H0RRTFqG30iAY3HJpOxJz1iiTSMtp14vz3185ySgEbPbUI1I_Im6EfiCOiPDUqHFh3DUQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeT4ou0E2bFECxt9MSILGsPBhTcfZSWjfrjmZbSoOOHLFnAedxeAYK-5U5MkyACRn7BWB11h0cFKGyu0EdVlZScpUXW65mhK00qwr4L9BnNqBwklcBZE3dhhk8Yipl7s7Gu5gC6asSq3FimnegRTHJXMabi7-5WQAQ5Lmr-ncrzdrlZoIMACnV5Lcqk6EiQmMyHJR9b10IUWKcRHcqzrCNnxzb19d0v2jf39E5MsKKzpVkpaHLInIA91NM8YQKxFxRulR_RicQxs7z7Lmf78hCDR3houNHstNevorIxLPsu4wEv9DT-RW6DfpEPs_-3az_l-6891YOk8IYM_or5c8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجلس [شورای اسلامی] پس از ماه‌ها تعطیلی، شب ۲۲ تیر اولین جلسه علنی خود را برگزار کرد.
به گزارش خبرگزاری خانه ملت (خبرگزاری مجلس [شورای اسلامی])، بیش از ۲۵۰ نماینده مجلس با حضور در ساختمان بهارستان جلسه خود را به ریاست حمیدرضا حاجی بابایی، نایب‌ رئیس مجلس، آغاز کردند.
نمایندگان مجلس با شعار دادن خواستار «انتقام از قاتلان» علی خامنه‌ای، رهبر پیشین جمهوری اسلامی ایران، و فرماندهان و شخصیت‌های سیاسی کشته‌شده در جنگ شدند.
در این جلسه مقرر شد که در مواقع اضطرار و شرایط خاص ایران، جلسات مجلس می‌تواند «در فضای مجازی یا خارج از بهارستان» تشکیل شود.
از نکات جالب توجه در جلسه امروز مجلس، نصب عکس مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی و همچنین غیبت محمدباقر قالیباف، رئیس مجلس در صحن علنی مجلس بود.
تشکیل جلسه علنی مجلس پس از ماه‌ها تعطیلی، آن هم در ساعات غیراداری واکنش‌های زیادی را در پی داشت و توجه رسانه‌ها را به خود جلب کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77043" target="_blank">📅 04:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRjfien44yS7xI3p8_ofvBHEff2ewpCxpyMdx0OZWibySaLiF6VJzaSM_O-imaelB1aBiFMtQXf9MoKI2pu474LEnPbanuXV9VpNpozS2VojnUbRSfqJtMy97dYnDnnX1rW6t9cVjNEruo7lzWS8bVzlBqL1PWEnYRYehkMqFa0AqMgN3emgH2ra0Vcx09YvEGUAJl7sqlNaja0TLgTMZWPoNAnodHya4kidlCa0K7ujVry1LHOT384OERqT2Co5BdP03sc3ifFIxNbFTOyVQ14FzKBFvJ1e0pbcHOWT07EcYyziWMpfKmMEQnCXdzK5TT_5CRttOYpQyrv1rxu5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان گفت: در ساعت ۲:۱۰ بامداد سه‌شنبه، نقاطی از شهرستان امیدیه مورد اصابت پرتابه‌ها قرار گرفت.
به گزارش مهر، ولی‌الله حیاتی گفت: بر اساس ارزیابی‌های اولیه از وضعیت مناطق هدف قرار گرفته، تاکنون چهار نفر در این حادثه دچار مجروحیت شده‌اند که اقدامات امدادی در حال انجام است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77042" target="_blank">📅 04:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tskj7IqJHJp27uLt9vz6UbJ9ficzvHuePc9hFVjewOLLkzJvBIZL62yLWVZ1cSjGSfjC2yCnpvJQHB1iT9tbJh78p7kGizRy_D0Ab7EWV8O1WFA1BK6TBssvcAtLn9iWkgQt6UHlMrxT_ueq8FuLgeUKI9X3CpbXpkHW-YNh6ABznIcKsL_2CTTemJ6R-8nwdzHs2Dia05ri5uPac-8Mz1rAa-VLO8pwQFGoSnXF2BUIW2VPcQoqkRT9S-Mvv1pohCbDbEj-XyVY_-IB7Wf-VuAUessHg7AO9PSAldo0B0aJ-OFYz-XcTLqRGPqzGiphjtA9JA-k5_07XV89QaYKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی اعلام کرد که جمهوری اسلامی ایران به دو نفتکش در نزدیکی سواحل عمان حمله کرده است. به گزارش آسوشیتدپرس، در این حمله یک نفر کشته و هشت نفر دیگر زخمی شده‌اند.
@
VahidHeadline
" اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی"، ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت قهرمان و مومن ایران عزیز؛فرزندان شما در نیروی دریایی سپاه بر عهد خود در حفظ حقوق ملت ایران در تنگه هرمز تمام قد ایستاده‌اند.
ساعاتی پیش ارتش کودککش آمریکا که از شکست های مکرر عبرت نگرفته است، با تحریک شناورها تلاش کرد تعدادی از آنها را از مسیر غیر قانونی عبور دهد. دو فروند سوپر نفت کش متخلف که فریب آمریکا را خوردند و با خاموش کردن سامانه های ناوبری و بی توجهی به اخطارهای مکرر مرکز کنترل امنیت تنگه هرمز کشتی رانی در این مسیر را به مخاطره افکنده و عبور از مسیر مین‌گذاری شده را ترجیح دادند، مورد اصابت واقع شده و از کار افتادند.
نیروی دریایی سپاه به همگان اعلام می کند همکاری با دشمن متجاوز که از هزاران کیلومتر دورتر آمده تا حقوق مردم منطقه را تضییع کند و عبور از مسیر مین‌گذاری شده جز پشیمانی، خسارت و تاخیر در بازگشایی تنگه هرمز و ایجاد بحران انرژی در جهان نتیجه ای ندارد.
و ما النصر اِلا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77041" target="_blank">📅 04:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nEexBXhAemrN7FWiByHY-BX6mehg3nNZBJfZhUd-vogHMd_LFTnArF28CmTU1JTHIUUQ6sW3mlBS_qe5ekX71FRYCqZXo1Fmb4RMqLUWg9IwnLTEjbej2ZIxw5izIQpRlsMubQG-y3pKITC2MxRZoZ1IaveUraVwSa2sA-LDjcLu8sm-T6u3HxCIRhqpRzNiGRmKy_DkjsYhXROG9tZcw-kV2hBjzfG1nIRVbJaH2ITjnP1gukfzNftHjzFVnd0jl77DBYGjnk2qSiY5TgbG0MpxvWCM0mPeCkRv-V4WU1Bwb27jmoC7xsk7b_EqBeptbx3kFnCCJZWaluIUjQ-eKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSqCkDrLt9ICMxhHZtguyc-GDKQA_pNrLYiNTP00SVEPW7SThvhRmuahaO1jHAD6aNNZJZo4afniz4x7w2j9oF6nzUyx6IsHR4PxjzPGy_M15_yWSSMsbZdBYYP88_o0a8fIo0a9X6W0mx57BtDJ8fDmFIdwmOIrYhn89x1C10j-fgVdcm2JYqP6BZ7m8KP-MXb-oNfg3AIssq0xwUkwsI6w0ZKFoIhCRS2MLWN2hGWI_-bRLAd9T4ovq1J6CGJ9fvhwkbMcquh0XL30SUqkp_oPUZ2zXQahsFqjsRL18G1gi7QT6T0TZiL5vNJ_kBh43G-pMaj8vKvZaGEU0zyCpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: کرمانشاه ۲ تا موشک شلیک کردن ساعت ۴
آپدیت: ممکنه تصاویر مربوط به پرتاب از تبریز باشند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77039" target="_blank">📅 04:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تبریز
از سمت شمال شهر  دوتا پرتابه با نور شدید قرمز به سمت جنوب غربی دیده شد
سلام وحید جان، تبریز صدای جنگتده میاد [احتمالا صدای شلیک موشکه]
سلام اقا وخید همین الان صدای دوتا انفجار کرمانشاه
سلام
صدای دو انفجار در کرمانشاه
ساعت ۴ و دو دقیقه
ساعت ۴:۲ نردیکی هرسین تو استان کرمانشاه صدای ۲ انفجار سنگین اومد
سلام ساعت ۴:۰۳ کرمانشاه دوبار صدا اومد احتمالا شلیک موشک.
سلام وحید کرمانشاه شهرستان هرسین دوتا صدای وحشتناک مهیب
سلام کرمانشاه ساعت ۴:۰۲ دقیقه صدای انفجار از سمت تنگه کنشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77038" target="_blank">📅 04:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=ZsjzbI88e3MYawaDpzgMh3YFUEIcEpoyVpOO6axu8GHRnfSA-SGsapjPZHrraL4HUMDSc5hqBOhhj87DRH13tgCRxJC4Kt3GZ6pXmnHJqnh9poebzh4uosVU5WuQGnihYsihkWSD4S0Fk_jeMIdav-BQRZpaYvoT3cBKVTL3DpLfDmxyfZXGtSbWqBGmUoZHY6XlHF2BW7DTLkN-CsddTKOjF0wFJ5YHz69-BXS1jcM2RijuptqOX3gH_QdYgsPwmmLFGPJsVyfLFbiU-gRkPshLOXQBUY3jUrNYuo4LAgwc03yAwU4yVhESpII4gC3IAmyLDXYlJf7LL2x0RsaDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=ZsjzbI88e3MYawaDpzgMh3YFUEIcEpoyVpOO6axu8GHRnfSA-SGsapjPZHrraL4HUMDSc5hqBOhhj87DRH13tgCRxJC4Kt3GZ6pXmnHJqnh9poebzh4uosVU5WuQGnihYsihkWSD4S0Fk_jeMIdav-BQRZpaYvoT3cBKVTL3DpLfDmxyfZXGtSbWqBGmUoZHY6XlHF2BW7DTLkN-CsddTKOjF0wFJ5YHz69-BXS1jcM2RijuptqOX3gH_QdYgsPwmmLFGPJsVyfLFbiU-gRkPshLOXQBUY3jUrNYuo4LAgwc03yAwU4yVhESpII4gC3IAmyLDXYlJf7LL2x0RsaDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده با شرح: سراوان سه‌شنبه ۲۳ تیر
پیام دریافتی: اینجاست
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77037" target="_blank">📅 03:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYXL1JsHBXkeMKPJjrzipMCDVvCuFTOvONMrhXF4utj20B2FycK2Nu-eFIZGgTZI7XPn2rgjhz1hn-g7SeiTYzGPz3pBlHXvTgGxvATIMOb1P4h4BASxCVi_t5gkE-BMaoJ_qAcbhv_UtZEDLs6JeBFcdMNz_WhJYMcrAHPKz3U2e28611HOuarjucJ_N6hB1ZBzDe0K4r-HeNNzTNyKinfoxyGy9Wo-4v56RI5Di0UgV8vMFRqajpl0qjSQjJKX8hetQjbz-sJ4oZCvZwp4GTY3UjdlkSysKdZWqvy-hODsWvY7MaYHq_D4SsE4znf93bcHu_CaPBsbgCAW_DYo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۳:۳۰ بوشهر دوتا انفجار خیلی شدید صدا توی بهمنی اومد
بوشهر 3:28 مجدد صدای انفجار
بهمنی زدن 2 بار سنگین بود ساعت 3 نیم دوباره زدن
وحید جان دوباره صدای انفجار اومد بوشهر ۳:۲۹
سلام همین الان بوشهر رو دو تا پشت سر هم زدن فکرکنم انبار مهمات یا همچین چیزی بود
دوتا انفجار مهیب پشت سر هم شهر بوشهر ساعت ۰۳:۲۹
سلام دوباره زدن با صدای انفجار بدتر
بوشهر تا الان ۴بار زدن
چهار تا صدای ترکیدن دیگه ۳:۲۹
پایگاه هوایی بوشهر ۳.۲۸ سه انفجار
سلام وحید بوشهر همین الان سه تا انفجار خیلی شدید پشت سر هم
بوشهر رو زدن ۳:۲۸ نزدیک به اسکله جلالی گمونم، پایگاه هوایی
سه تا تا حالا
الان بوشهر صدای بلند انفجار ۳:۳۰
3 تا انفجار سنگین
بوشهر ساعت ۰۳:۲۹ صدای انفجارهای خیلی شدید و نزدیک میاد
بوشهر ۳:۲۸ ۳:۳۰ هردو انفجار بلند خونه ها داره میلرزه سمت بهمنی
بوشهر صدای ۳ انفجار همین الان بهمنی
بوشهر همین الان ۳:۲۸ تا ۳:۳۰ ۵تا انفجار شدید ! خونه میلرزه
سه تا دیگه زدن
تو پایگاه هوایی
سلام دوباره زدن با صدای انفجار بدتر
بوشهر همین الان باز زدن
دو سه دقیقه پیش هم زده بودن
بازم زدن سه تای دیگه
بوشهر رو دارن میزنن
انبار مهمات اینا نیست فرودگاه دارن میزنن
و پایگاه هوایی ششم شکاری
و موشک های تام هاواک هستش ک صداش بلنده
یعنی جنگنده نیست مثل سری های قبل
بوشهر خیلی بد دارن میزنن تو این چند وقته اینجوری نبوده باز خونه هامون لرزید چهارتا پشت سرهم زدن
بوشهر - اولین انفجار پایگاه هوایی بود ۳:۱۳
انفجار های بعدی شامل دو انفجار در همون حوالی
دو انفجار مهیب دیگر در اطراف شهر بوشهر بود. احتمالا چغادک. حوالی ۳:۳۰ تا ۳:۳۲.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77036" target="_blank">📅 03:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
سربندر همین الان دوتا پشت سر هم
یکی دیگه
همین الان بندر امام خمینی‌ رو زدن سه بار
ماهشهر ساعت ۳:۲۳ صدای ۲ تا انفجار پشت هم
[احتمالا همون انفجارهای پیام‌های بالایی]
سلام ماهشهر تا الان سه بار صدا اومد
وحید جان ماهشهر ۳ تا پتروشیمی سر کارم لرزیدیم
سه انفجار پیاپی در ماهشهر داشتیم
😔
بچه ها صبح امتحان نهایی دارن
😭
سلام ماهشهر زدن 3:24 دقیقه
شیشه اتاقم لرزید
همین الان ساعت ۳:۳۰دقیقه
بندر امام خمینی سایت موشکی رو زدن چهار بار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77035" target="_blank">📅 03:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر 3:06 صدای انفجار
سلام ساعت ۳:۰۵ بوشهر صدای انفجار
ناحیه بهمنی
سلام وحید جان ساعت ۳:۰۶ بوشهر صدای انفجار اومد
الان بوشهر و زدن ما پایگاه هوایی هستیم خیلی بد بود
ساعت ۰۳:۰۶ دقیقا انفجار مهیب شهر بوشهر
سلام . همین الان بوشهر رو زدن . صدا خیلی مهیب بود
سلام وحید جان ساعت 3:05 دقیقه بوشهر رو زدن پایگاه هوایی بود فکر کنم
بوشهر زد ساعت ۳:۰۵دیق شب
همین الان وحید جان زدن بوشهر رو ، لرزش و صدا خیلی خیلی بیشتر از روزای قبل
ترس و لرز وجودم فرا گرفت برعکس شبای قبل
واقعا ترسناک بود این یکی
سلام
پایگاه هوایی رو زدن الان
صداش وحشتناک بود
تمام بدنم داره میلدزهه
همین الان بوشهر نزدیک فرودگاه صدای انفجار بسیار مهیب
سلام بوشهر بهمنی زدن ساعت 3:06
سید جان ۳:۰۶ بوشهر صدای انفجار (فکر کنم پایگاه نیرو دریایی بود)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77034" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=aWt-eR8pNOgJ0Qs95MAwoZ5njrBVFpbmC0olFIJrTusowDH35xU-4CtZn2hlItxz6PT9wB2WJqwkx-DzLS56VeGwPfrbEdTnyEW075q7rOBrfcmwGyRtdZ3mkc95lIWMIIGTcX021B9Mocx1rLIiAUJz47KKgfxH1q3wbdy3gQI2kxuKjlXn006TfiJCAURcjrbS3oV3GyGkuK0_t-V6ECif2COREV1x_ycou4xUZDcm6nwsmC6CM6GpWEKLVudqFfsNyk9cTPr2oHNIKTCOGN2vyrC9vfTmDqDG4_zXNdlbW1LYDQHsHiwh4ARD9LxvlMfTD-sSGU_yFDhn45kuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=aWt-eR8pNOgJ0Qs95MAwoZ5njrBVFpbmC0olFIJrTusowDH35xU-4CtZn2hlItxz6PT9wB2WJqwkx-DzLS56VeGwPfrbEdTnyEW075q7rOBrfcmwGyRtdZ3mkc95lIWMIIGTcX021B9Mocx1rLIiAUJz47KKgfxH1q3wbdy3gQI2kxuKjlXn006TfiJCAURcjrbS3oV3GyGkuK0_t-V6ECif2COREV1x_ycou4xUZDcm6nwsmC6CM6GpWEKLVudqFfsNyk9cTPr2oHNIKTCOGN2vyrC9vfTmDqDG4_zXNdlbW1LYDQHsHiwh4ARD9LxvlMfTD-sSGU_yFDhn45kuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح:
#سراوان
ساعت ۲:۳۰ دقیقه [سمت] فرودگاه رو زدند.
سه‌شنبه ۲۳ تیر
Vahid
پیام‌های دریافتی دیگر:
پیام ساعت ۲:۳۵: سراوان رو ۴ بار زدند
سلام سراوان سیستان بلوچستان ۵ تا انفجار پشت سرهم
پیام ساعت ۲:۴۱: سلام، سراوان بلوچستان رو زدن، ۳ تا صدای انفجار اومد خونه‌ها بد لرزید، حدود ۲۰ دقیقه پیش.
همین الان سراوان سیستان و بلوچستان رو زدن
سلام ساعت 2:20 سپاه شهرستان سراوان سیستان و بلوچستان رو زدن
4 تا انفجار بود با صدای خیلی وحشتناک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77033" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=Xy1RfdIrMMBvUxYy-7mHgnv9jXX4XHGdx1Emd-d0mdg2gkE2R80FOsQS0Py9VPNG9b1UdOv1EKEf9N01fMiyZWNM0_-o38Yvx_Csc7EdJOARVgDy_KcaTq3zRGB8gsYjOw2k4YP69YgtkzHBPBo4VOyRhFn2oJYgMqlrUVgpRZ20bUvum_WUmHcZKQCUz7Jp8D49SlC2EDEBMB_oo4-8ketKK_3piHAuosClWKj1whivqRLWngJqh5xIpTT1sx5FGPyTNg7x4EF7tGi09cc5m3VaXLY8mtm7BQDSB785YlsPn6sGjeilbnG6QW9uvUXl6WZi0sGXc0xZKs2zjRtM6yPywTiho5Ok-zFc-V9djo2wxjy3imNY9fS145dZldrgQtxcZfMajictv2n9aim1L-jg34OmnwkgdL-256ZE6s5y0ES4_7dn9d0RP6CH4FmU2Vhd_MsGMnMZATclFBUlRKhfdean7BiCWqZG5BBXVxRF0aMvHGKkfGVwYL31JtEEMsHEYz1lApSf5JVMCNKFR5wz6CMeFAuWZ3vQQ8JNgAIbrP_z4O9cd-jY7F4R1j_tOPhS3TXzOHiHMdgq_sXQQUWVLQqz-qGJcWQ-BtnHWXNsnCvlbsKd20sqJUj8zkgHAjz7Ml8oDtJTz3GfkJDr-COkEdi2HPIBOFHNP6XCscI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=Xy1RfdIrMMBvUxYy-7mHgnv9jXX4XHGdx1Emd-d0mdg2gkE2R80FOsQS0Py9VPNG9b1UdOv1EKEf9N01fMiyZWNM0_-o38Yvx_Csc7EdJOARVgDy_KcaTq3zRGB8gsYjOw2k4YP69YgtkzHBPBo4VOyRhFn2oJYgMqlrUVgpRZ20bUvum_WUmHcZKQCUz7Jp8D49SlC2EDEBMB_oo4-8ketKK_3piHAuosClWKj1whivqRLWngJqh5xIpTT1sx5FGPyTNg7x4EF7tGi09cc5m3VaXLY8mtm7BQDSB785YlsPn6sGjeilbnG6QW9uvUXl6WZi0sGXc0xZKs2zjRtM6yPywTiho5Ok-zFc-V9djo2wxjy3imNY9fS145dZldrgQtxcZfMajictv2n9aim1L-jg34OmnwkgdL-256ZE6s5y0ES4_7dn9d0RP6CH4FmU2Vhd_MsGMnMZATclFBUlRKhfdean7BiCWqZG5BBXVxRF0aMvHGKkfGVwYL31JtEEMsHEYz1lApSf5JVMCNKFR5wz6CMeFAuWZ3vQQ8JNgAIbrP_z4O9cd-jY7F4R1j_tOPhS3TXzOHiHMdgq_sXQQUWVLQqz-qGJcWQ-BtnHWXNsnCvlbsKd20sqJUj8zkgHAjz7Ml8oDtJTz3GfkJDr-COkEdi2HPIBOFHNP6XCscI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان تامی بروس، معاون سفیر ایالات متحده در سازمان ملل در جلسه اضطراری شورای امنیت، ترجمه ماشین:
بار دیگر، این شورا برای برگزاری نشستی اضطراری فراخوانده شده است تا درباره تلاش‌های حکومت ایران برای تهدید همسایگانش در خلیج [فارس] و تضعیف تلاش‌ها برای برقراری صلح در منطقه گفت‌وگو کند.
در ۳ ژوئیه، یک پرواز ایرانی از تهران وارد صنعا، در قلمرو تحت کنترل حوثی‌ها، شد. هدف این پرواز، انتقال نیروهای سپاه پاسداران، از جمله کارشناسان پهپادی و موشکی، برای حمایت از تروریسم حوثی‌ها بود؛ آن هم با پوشش انتقال مقام‌های حوثی به مراسم خاک‌سپاری رهبر جمهوری اسلامی.
این نوع حمایت، حوثی‌ها را قادر می‌سازد مردم یمن را به وحشت بیندازند و آزادی کشتیرانی را در دریای سرخ و آبراه‌های پیرامون آن تهدید کنند. از زمانی که پروازهای ماهان‌ایر به صنعا در سال ۲۰۱۵ متوقف شد، شاهد تلاش ایران برای ارائه چنین حمایت آشکار و گستاخانه‌ای از حوثی‌ها نبوده‌ایم. در واقع، رهبران حوثی آشکارا از این پرواز اخیر به‌عنوان دورزدن موفقیت‌آمیز تلاش‌های بین‌المللی برای منزوی‌کردن این گروه تروریستی تجلیل کردند.
این اقدامات نقض قطعنامه ۲۲۱۶ شورای امنیت به‌شمار می‌رود. ...
افزون بر این، صبح امروز دومین پرواز ایرانی با وجود دستور صریح و علنی دولت جمهوری یمن مبنی بر خودداری از این اقدام، وارد یمن شد. بی‌اعتنایی عامدانه جمهوری اسلامی ایران به حاکمیت یمن و تصمیم‌های جمعی این شورا، به‌سادگی غیرقابل‌قبول است.
به همین ترتیب، بی‌اعتنایی آشکار ایران به قطعنامه ۲۸۱۷ شورای امنیت را نیز دیده‌ایم. ....
هفته گذشته، ایران پهپادها و موشک‌هایی را به سوی سه کشتی تجاری غیرنظامی که در حال عبور از آب‌های سرزمینی عمان بودند، شلیک کرد؛ اقدامی مغایر با حقوق بین‌الملل. این حملات می‌توانستند دریانوردان را زخمی یا کشته و خسارات زیست‌محیطی قابل‌توجهی ایجاد کنند. یکی از کشتی‌ها، یک نفتکش قطری حامل گاز طبیعی مایع، در حال سوختن رها شد و تردد دیگر کشتی‌ها در تنگه را نیز بیشتر به خطر انداخت.
سپس عصر شنبه، ایران یک کشتی کانتینری در مسیر امارات متحده عربی را هدف قرار داد. یک تبعه هند همچنان مفقود است. این حملات از هیچ اصل مشروعی سرچشمه نمی‌گیرند. بلکه همان‌گونه که یکی از مشاوران رهبر جمهوری اسلامی روز یکشنبه گفت، این اقدامات از تمایل ایران برای تصاحب غیرقانونی یک آبراه حیاتی و استفاده از آن به‌عنوان ابزار بازدارندگی راهبردی ناشی می‌شود.
فراتر از عرصه دریایی، ایران در هفته گذشته پهپادها و موشک‌هایی را به سوی بحرین، اردن، کویت، عمان، قطر و امارات متحده عربی پرتاب کرده است. وزارت کشور قطر گزارش داد که سه نفر، از جمله یک کودک، بر اثر سقوط بقایای عملیات رهگیری پس از حملات روز یکشنبه ایران زخمی شدند.
...
در چند هفته‌ای که از امضای این تفاهم‌نامه گذشته، ایران بارها این توافق را نقض کرده است. تا زمانی که ایران به تهدید عبور امنی که این تفاهم‌نامه از آن حفاظت می‌کند ادامه دهد، ایالات متحده آن را به‌طور یک‌جانبه اجرا نخواهد کرد.
به زبان ساده، اگر ایران به سوی کشتی‌ها شلیک کند، ما فوراً با نیروی نظامی پاسخ خواهیم داد. عملیات نظامی ایالات متحده پاسخی به این تهدیدها در چارچوب دفاع از خود و دفاع از دیگران است.
...
ایالات متحده در کنار شرکای خود در خلیج [فارس] ایستاده و همراه دولت جمهوری یمن، در برابر تهدید تروریستی حوثی‌های مورد حمایت ایران خواهد ایستاد. ما همچنان متعهدیم با اعضای شورا همکاری کنیم و از همه ابزارهای موجود، از جمله تحریم‌ها، برای حمایت از راه‌حلی مسالمت‌آمیز برای درگیری یمن و حفاظت از صلح و امنیت بین‌المللی استفاده کنیم.
و در پایان، بار دیگر از شورا می‌خواهیم با صراحت و بدون هیچ ابهامی به ایران اعلام کند که این اقدامات آشکار، مغایر با حقوق بین‌الملل و غیرقابل‌قبول‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77032" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=KtuRacNfvUNZ6AqVcif5DCk5c_DzIPhTPdikIlN00qI5A9WMrZ0NOdRr4MYkmftJx-JCdpeRradkwXzPz1JJiDV7FaVlBZRNQ7OeFXxNG5YDaWZ8UHLR0PoVPdYsOVL2QwDOc4S4almYseJrObhomOTi6tXtasTmzK-D6cXL5Dyb59J8Zjrrczc7dDIAdRkNiO2O3wk065V1E_FhmEkg8iXtu7eDxL_hh82H-D03sCbx5yUbRITiJxggvGMTjxeqQR1fcfdjv3fzjlH3lxrFK4dt7T1EOwRQf3OMLY3BJEl9opwePATDYa5GVfzovLuqYKLlOJ3dTfmRL64lis7Zmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=KtuRacNfvUNZ6AqVcif5DCk5c_DzIPhTPdikIlN00qI5A9WMrZ0NOdRr4MYkmftJx-JCdpeRradkwXzPz1JJiDV7FaVlBZRNQ7OeFXxNG5YDaWZ8UHLR0PoVPdYsOVL2QwDOc4S4almYseJrObhomOTi6tXtasTmzK-D6cXL5Dyb59J8Zjrrczc7dDIAdRkNiO2O3wk065V1E_FhmEkg8iXtu7eDxL_hh82H-D03sCbx5yUbRITiJxggvGMTjxeqQR1fcfdjv3fzjlH3lxrFK4dt7T1EOwRQf3OMLY3BJEl9opwePATDYa5GVfzovLuqYKLlOJ3dTfmRL64lis7Zmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#کیش
، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77031" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از حدود نیم‌ساعت پیش:
سلام وحید جان
امیدیه رو ساعت ۲:۹ دقیقه زدن
سلام همین الان امیدیه خوزستان زدن
شهرستان امیدیه خوزستان
صدای شلیک دوتا موشک شنیدیم
بعد هم دو تا انفجار قوی خیلی نزدیک بود فاصلش
تونل موشکی که در روستای نمره یک امیدیه ازش استفاده میکنن همین الان بمب بارون شد و تخریب شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77030" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌های دریافتی:
حدود ساعت ۱:۳۰ چابهار یه صدای انفجار اومد
سلام وحید جان همین الان ساعت یک و نیم صدای پنح انفجار در چابهار شنیده شد
سلام وحيد جان ، چابهار صدای انفجار اومد 1:34 بامداد
#چابهار
: فقط باید تهرانی باشیم کسی به فکر ما باشه؟
[آپدیت: در واکنش کلی پیام حمایتی از تهران دارند می‌فرستند. زحمت نکشید و ننویسید لطفا.]
صدای انفجار ضعیف کنارک
انگار فاصله زیاد بود
وحید الان چابهار رگباری زدن نزدیک 10.15تا
سلام ساعت ۱:۳۳ چابهارو دارن بد میزنن
کنارک همین الان نزدیک ۱۰ تا زد 1 : 34
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77029" target="_blank">📅 01:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VfWpMKg0aoQdZvv6nJQlX-FewICXMiv7BIfp7CN5pV209264DT48oyjm95PQon4pAE0Y31l-tX4JtC-J71TDj4H-iOc5gj_MZFWzPsXBX4VA5wcioG3h2bFRL8B3PQoF3Ny_4rgTIHui3VaPa2hmwqqBJ2h9myXWlCpuUm6jSVDK6WFacox432h24JFfnYsfko3prvtpe6nUfc4h2zsUGlXKIglmSjRimzL5HYCEkHEJ9CkFAtm9vnsgRYlY6lKdxgQQxkT6VseW2yVu_HFXHpLLzF07yCXd0j5e4ZrdBRRgTJBWy5bMjaA3Xqbph9XW2MjZuP3r7tjPZ0wV8a-scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oo9Ize3mJE7um1Sx9usfI8hc5wWD5jl3RWK2qvei_XW5Awxk-arGdiCfcrAOSVgwlWMwmN9aygh2g0ag7RrCGjgYNX_6truo1hEbbnfio4gpJYvpe_AsMqLG-ASsyJHNOxmfwimkXsYPXjaobzmj8YpMG2Esj_o7GW2FOzcQ1yzxYD63Xi2uyfUNAbkaz9qcNq12vw8iuu99sol_FPXiHws1UsPWe16c9DMknbXjKsNLOqazERQ8XtdRVCA2Fuc1oK_u3JySt0XE4SbkwsEdYesRPDk7f0laurLduKttQJ0juVRKKuAOGWeVCeKFL8pqCxikOrtWd7Ljrss1g4wHIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: '
#کیش
، سه‌شنبه ۲۳ تیر ساعت ۰۰:۳۸'
Vahid
بعدش هم حملات و انفجارهای دیگری بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77027" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
کیش ساعت ۱:۰۲
۲ انفجار دیگه
صدای انفجار داره میاد تو کیش
کیش دوتا صدای انفجار دیگه
دوباره کیش رو زدن وحید
الان دوباره دوبار کیش زد
کیش رو دوباره زدن
البته صدا دورتر بود ۰۱:۰۳
دوباره زد کیشو
وحید جان این دفه دوتا زد
بندرگاهو داره میزنه
مجددا کیش را زد صداش از قبلی ها خیلی بلندتر بود و شیشه ها لرزید.
🔄
سلام همین الان کیشو دوباره زد این بار هم دوتا بود ساعت ۱:۹
الان سه بار دیگه زد کیش رو
وحید جان دوباره یکی دیگه زد کیشو
و مجدد صدای انفجار در کیش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77026" target="_blank">📅 01:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f01979093.mp4?token=XSswE2SNkLeuFEpvHjfjxNBukS8N1l8rOxpZAxfmWrN3vyedqEv_q8IeOAZI1wRYRU-Uz202VVUlpx7rC-qfwj4UDB8siFQZZL_FK1F_8TE3m3R6tuakp9T63_fvxq1XAG3l61KsiCsPK6BTlnMe9GGDTBqLLVyKvTtd5eDsdXCsi2j_6F9oA_0y_-Jp7x2TfelHiMnJtEu6jwpJbTYNAsMvAgV9tkDB91Lzy9o0hK2LeWsfCMDhEer6fmlMatQlzAZddgsXHp0k6bNcWIBJKDg_TfgA5UxgJ_lG4dy60rcwqS0Pa4MiPQO8t5SY1og8MIWogTprzQQVdT_PBbbymw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f01979093.mp4?token=XSswE2SNkLeuFEpvHjfjxNBukS8N1l8rOxpZAxfmWrN3vyedqEv_q8IeOAZI1wRYRU-Uz202VVUlpx7rC-qfwj4UDB8siFQZZL_FK1F_8TE3m3R6tuakp9T63_fvxq1XAG3l61KsiCsPK6BTlnMe9GGDTBqLLVyKvTtd5eDsdXCsi2j_6F9oA_0y_-Jp7x2TfelHiMnJtEu6jwpJbTYNAsMvAgV9tkDB91Lzy9o0hK2LeWsfCMDhEer6fmlMatQlzAZddgsXHp0k6bNcWIBJKDg_TfgA5UxgJ_lG4dy60rcwqS0Pa4MiPQO8t5SY1og8MIWogTprzQQVdT_PBbbymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: انفجارهای
#کنارک
الان، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77025" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXYwodPjwt_0NV-BsBFllf04-O-I2DeC8rZRJY_bONNm1yzCx2Kg1u7HNesKV8A38e3SRckHkTYEJosfyU9FfyWHvg5I5U2pYyEzE07ByvIyzwE15-qovqPY0FqULj6yeQApr1zIeYlJ_U6etGxzKIG-jcWcGBBEP51nfKThh_f9R3QDsUx9Yp4x3WG0SIVukzfjvA75Yb4oNdkDAAKIvhI3klWPToobSun47aW0TZxCpoJm2tr58EwNoIdu0b0ryuxbmooCanFXMC8A261c2J2UZlnCCCVkxYM2pFCKF6BtRBQg2TV8sTxrhylo_fGLgZCjxufXN7AUH_QJOljRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرق آمریکا [۰۰:۱۵ بامداد سه‌شنبه ایران]، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل قوا، سومین شب پیاپی حملات علیه ایران را آغاز کرد.
این حملات همچنان هزینه سنگینی بر نیروهای ایرانی تحمیل خواهد کرد و توانایی آن‌ها برای حمله به غیرنظامیان بی‌گناه و کشتیرانی تجاری در تنگه هرمز را کاهش خواهد داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77024" target="_blank">📅 00:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان توی جم صدای ۴تا انفجار اومد
شهرستان جم استان بوشهر
چهارتا تا الان زدن
همین الان جم رو  زدن سه تا انفجار12:40
درود شهرستان جم استان بوشهرو همین الان دوبار زدن
درود وحید جان، جم بوشهر ۴ انفجار پشت سر هم، خیلی شدید بود.
حاجی جم همین الان ۴ تا انفجار شدید ۱۲:۴۰
وحید جان جم بوشهر ۳ ۴ تا صدا اومد
همین الان ۴ تا صدای انفجار مهیب سپاه چمران شهرستان جم
خیلی مهیب
سلام وحید جان همین الان ۴تا صدای انفجار در کنگان شنیده شد ۰۰:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77023" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان زدن کیشو پنج‌تا پشت هم
کیش رو زد
سلام وحید جان
همین الان کیش صدای دو انفجار اومد
دور بود صداها
سلام وحید جان کیش صدا انفجار پنج تا
همین الان ساعت ۰۰:۳۹ کیش رو زدن
نمی‌دونم بندرگاه بود یا فرودگاه، اما مطمئن که شدم، بهت میگم
سلام آقا وحید کیش رو زد ما نزدیک فرودگاهیم پنجره ها لرزید
جزیره کیش ۴ بار پشت هم زد و صدای جنگنده میاد.
کیش ساعت ۰۰:۳۸
۳ انفجار متوالی
درود
کیش، ۵ صدای انفجار، ۱۲:۴۰
۴.۵بار کیش صدا زیاااد پنجره ها لرزید همه تو بالکن خونه هان .. نمدونیم کجا بود
شاااااید رو آب بود ولی خیلی نزدیک ... هنوز کسی خبر نداده کجا بود..
انفجار در بندرگاه کیش بوده شناور سپاه یا نیروی انتظامی بوده…
بچه‌ها میگن حوضچه بندرگاه کیش رو زدن
شمال جزیره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77022" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان مشهد زلزله اومد
مشهد لرزید
یا زلزله بود ، یا زدن یه جایی را
سلام
مشهد نمیدونم زمین لرزه بود یا چی؛
زمین لرزید!
همین الان ساعت ۰۰:۳۵
زلزله بود گویا مشهد.
وحید جان مشهد لرزید
مشهد زلرله اومد
مشهد لرزید ۰۰:۳۵
دو بار با فاصله ۴۰ ۵۰ ثانیه ای
سلام مشهد ساعت00.35 زلزله یا یه موج لرزه‌ای شدید اومد با فاصله سه ثانیه رفت برگشتی بود
مشهد یک لرزش خفیف حس شد ولی صدایی همراه نداشت.
مشهد چند دقیقه پیش دوبار لرزید
سلام وحید آقا
مشهد یه چند لحظه ای لرزید
فکر کنم زلزله بود
سلام فریمان هم از زلزله مشهد لرزید
من تربت جامم اینجام همون تایم در حد دو سه ثانیه یکم لرزید
فریمانم لرزید(شهرستان60کیلومتری مشهد)
حتی یکی از اعضای خونه از خواب بیدار شد
چند ثانیه طول کشید
سلام وحید جان. ما طرقبه نزدیک مشهد هستیم اینجا هم لرزش رو حس کردیم.
🔄
سلام آقا وحید زمین‌لرزه‌ای با بزرگی ۳.۶ حوالی سفید سنگ در مشهد را لرزاند.
بزرگی زمین‌لرزه ۳ و ۶ دهم بود. مرکز زلزله سفیدسنگ خراسان رضوی بود. بیشتر نزدیک فریمانه تا مشهد
[دو تا پیام هم درباره احساس زمین‌لرزه در یاسوج داشتم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77021" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان انفجار بندرعباس ۰۰:۳۴ ۳ انفجار
١٢:٣٣ سه انفجار پشت سرهم بندرعباس با صداي بلند
همین الان
بندرعباس انفجار شدید وحشتناک
چند انفجار وحشتناک پشت سر هم
بندرعباس ۳۳: بامداد صدای چند انفجار
بندرعباس ۱۲ و ۳۴ چهار صدای انفجار
وحید بندرعباس ۳ـ۴ تا صدای انفجار شدید
بندرعباس ۴ تا انفجار فوق العاده شدید سمت نیرو دریایی ارتش و سپاه
همین الان ۰۰:۳۴ دقیقه ۵ بار صدای انفجار اومد
سلام بندر عباس همین الان صدای چند انفجار شدید پشت سر هم فاصله ای نزدیک بودد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77020" target="_blank">📅 00:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33fa32f341.mp4?token=ljSGG4bt5Jsvv8isdQgJHlL4w-y0MH8h_g57lHKBhgvUY3_lTFR0nIsl8_9TP7H6hH0hibkfGEkObkG_zDSJafFVpq2A-aVmvj2JfMX-pB-sqgszQvKeCe1ivnrOWT85fMpz1-mZSIKCh3jw3IxfdCLXxIdp4nvCsHu2V5N9tDxoCosPpzkf7vSagRejcvX9xrAKzCXxCx4lzVMAukJbnA_8GCv7N2U_c_H9hIO4GWPPLxcOWj3ZPFqLW_Kd4CBZF4iMCGtpPPbQtFj_HWFRzyeQkIRRf0BMttHPIswpkONEyEVEabrB8ErqKILlnSUr7j6k-hphiUI_-Pq89NVUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33fa32f341.mp4?token=ljSGG4bt5Jsvv8isdQgJHlL4w-y0MH8h_g57lHKBhgvUY3_lTFR0nIsl8_9TP7H6hH0hibkfGEkObkG_zDSJafFVpq2A-aVmvj2JfMX-pB-sqgszQvKeCe1ivnrOWT85fMpz1-mZSIKCh3jw3IxfdCLXxIdp4nvCsHu2V5N9tDxoCosPpzkf7vSagRejcvX9xrAKzCXxCx4lzVMAukJbnA_8GCv7N2U_c_H9hIO4GWPPLxcOWj3ZPFqLW_Kd4CBZF4iMCGtpPPbQtFj_HWFRzyeQkIRRf0BMttHPIswpkONEyEVEabrB8ErqKILlnSUr7j6k-hphiUI_-Pq89NVUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از مصاحبه ترامپ، ترجمه ماشین:
🔴
ترامپ:
این را می‌گویم: به نظرم مردم اشتباه می‌کردند. هرگز فکر نمی‌کردم [نامفهوم] بتوانند کاملاً مسلح شوند. هرگز تصور نمی‌کردم چنین قیامی رخ بدهد، چون این‌ها آدم‌های خشنی هستند.
رهبران به‌اصطلاح‌شان بسیار خشن‌اند. آن‌ها قاتل‌اند. ۵۲ هزار نفر را کشته‌اند. آن کشتی‌گیر را یادتان هست؟ آن کشتی‌گیر یکی از بهترین کشتی‌گیران جهان بود. او و دو دوستش را کشتند، فقط چون حرفی زد که حتی آن‌قدرها هم علیه حکومت نبود.
آن‌ها دیوانه‌اند. به کشتنشان ادامه می‌دهند، چون تا وقتی شما کاری نکنید، مردم خودشان را خواهند کشت.
🌳
Hugh Hewitt:
آیا شما، ارتش آمریکا یا ارتش اسرائیل می‌توانید به آنچه از رده سوم، رده چهارم و رده پنجمشان باقی مانده دست پیدا کنید؟ می‌دانید کجا هستند؟ می‌توانید آن‌ها را بکشید؟
🔴
ترامپ:
بله، می‌دانم؛ اما نمی‌خواهیم درباره‌اش حرف بزنیم. ولی قطعاً زیر نظرشان داریم.
بله، من درباره این موضوع خیلی چیزها می‌دانم. خیلی چیزها می‌دانم، اما فکر نمی‌کنم الان مناسب باشد درباره‌اش صحبت کنم. ولی خواهیم دید.
برای نمونه، امشب آن‌ها را بسیار سخت هدف قرار خواهیم داد و فردا هم سخت به آن‌ها ضربه خواهیم زد. هیچ کاری هم از دستشان برنمی‌آید. هیچ چیزی ندارند. هیچ کاری نمی‌کنند، جز اینکه فقط لاف می‌زنند.
خب، فکر می‌کنم کمی خل‌وچل‌اند؛ همه‌شان همین‌طورند. رده اولشان را از بین بردیم. بعد رده دومشان را از بین بردیم. سپس حدود ۲۵ درصد از این حکومت را از میان برداشتیم.
ذهنشان کمی متفاوت کار می‌کند. دیروز توافقی داشتیم و قرار بود صددرصد نهایی شود؛ اما ناگهان تماسی دریافت کردند و همه‌شان از اتاق فرار کردند.
این آدم‌ها... این آدم‌ها دیوانه‌اند. توافقی داشتیم که در آن به همه خواسته‌هایمان می‌رسیدیم. اما آن‌ها اساساً توافق‌ها را زیر پا می‌گذارند، می‌دانید؟ توافق می‌کنند و از نظر آن‌ها، توافق‌ها برای شکسته‌شدن بسته می‌شوند.
این‌ها آدم‌هایی به‌شدت غیرقابل‌اعتمادند. صادقانه بگویم، اگر روزی سلاح هسته‌ای داشتند، ظرف یک روز از آن استفاده می‌کردند.
🌳
Hugh Hewitt:
آیا شما، ارتش آمریکا یا ارتش اسرائیل می‌توانید به آنچه از رده سوم، رده چهارم و رده پنجمشان باقی مانده دست پیدا کنید؟ می‌دانید کجا هستند؟ می‌توانید آن‌ها را بکشید؟
🔴
ترامپ:
بله، می‌دانم؛ اما نمی‌خواهیم درباره‌اش حرف بزنیم. ولی قطعاً زیر نظرشان داریم.
بله. من درباره این موضوع خیلی چیزها می‌دانم. خیلی چیزها می‌دانم، اما فکر نمی‌کنم الان مناسب باشد درباره‌اش صحبت کنم. خواهیم دید.
برای نمونه، امشب آن‌ها را بسیار سخت هدف قرار خواهیم داد و فردا هم سخت به آن‌ها ضربه خواهیم زد. هیچ کاری هم از دستشان برنمی‌آید. هیچ چیزی ندارند. هیچ کاری نمی‌کنند، جز اینکه فقط لاف می‌زنند.
🌳
Hugh Hewitt:
ادامه بدهید، آقای رئیس‌جمهور.
🔴
ترامپ:
متأسفانه این کار را کردم، چون آن‌ها را شناختم. [نامفهوم درباره تفاهم‌نامه] خیلی بهتر است. می‌دانید، مردم می‌گویند دست‌کم آدم معقولی بودم، اما آن‌ها را شناختم و فهمیدم کاملاً سنگدل‌اند...
🌳
Hugh Hewitt:
تفاهم‌نامه‌ای که مذاکره‌کنندگان شما آوردند چه بود؟ آیا آن یک تفاهم‌نامه [نامفهوم] بود؟ آیا طوری تنظیم شده بود که از هم بپاشد؟
🔴
ترامپ:
برای آزمودنشان تنظیم شده بود. یک آزمون بود. نمی‌دانستیم.
ببینید، وقتی با آدم‌های پست سروکار دارید، تفاهم‌نامه معنای چندانی ندارد. حتی وقتی با آدم‌های شرافتمند سروکار دارید هم معنای زیادی ندارد، چون فقط یک تفاهم‌نامه است. معنای زیادی ندارد.
من گفتم: اصلاً چرا این کار را می‌کنیم؟ این یک روش استاندارد در آمریکاست که ابتدا به یک تفاهم‌نامه می‌رسید و بعد سراغ توافق نهایی می‌روید. من گفتم مستقیم سراغ توافق نهایی بروید.
ولی می‌دانید چیست؟ آن به‌نوعی یک آزمون بود و آن‌ها پای آن نایستادند؛ به آزمون پایبند نماندند.
🔄
بعدش جملات دیگری هم گفت که در ویدیوی بالا نیست:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با هیو هیویت، مجری و تحلیل‌گر سیاسی، اعلام کرد که ارتش ایالات متحده «کوه کلنگ» را در ایران هدف قرار داده و آن را نابود خواهد کرد. پیش از این، خبرگزاری «وای‌نت» با انتشار تصاویر ماهواره‌ای جدید فاش کرده بود که این سایت زیرزمینی محرمانه در رشته‌کوه‌های زاگرس که آژانس بین‌المللی انرژی اتمی اجازه بازرسی از آن را ندارد، همچنان فعال است. موضوعی که پایبندی تهران به یادداشت تفاهم اخیر مبنی بر عدم توسعه سلاح‌های هسته‌ای را زیر سوال می‌برد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77019" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XezjQavqSWz7wQMWBKb_WKAOkDbKV3wMRB9-zOIPifslQY4KJX2Otozqde5q-7fpX1D-_3zIo8T-jzhmpgMUYCBfjWewwFoR6DsG7eploK0r624KAR2BbLLVAkSPzrkpPSuZ1sUtDYiyWiOqBVQmgDHLX5DX52bhmRv-gKQzfPMLXaCbkWx924OQizVr4C-AImRlOjYEA2Plqxgfxgsj-wKI5i2dUi9uTerrExMQqKkDJk8Mi5jtNHmOOVkikMv1F3RUFQ58JmDxQGmQmwc-6r0aMRwglyyNVoDp5p-XeCvsyhVTFEe0uNMYKXJ4mP3vZYQqkAZoKDdjUtFUPr950g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا در امارات متحده عربی با انتشار پستی در شبکه ایکس اعلام کرد تمامی وقت‌های کنسولی سفارت آمریکا در ابوظبی و کنسولگری این کشور در دبی از ۲۳ تا ۲۵ تیر به دلیل وضعیت امنیتی منطقه لغو شده است.
در این اعلامیه آمده است سفارت و سرکنسولگری آمریکا همچنان در وضعیت «تخلیه اجباری» قرار دارند؛ به این معنا که کارکنان غیراضطراری دولت آمریکا از امارات منتقل شده‌اند. در نتیجه، فقط خدمات کنسولی محدود به شهروندان آمریکایی ارائه می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77016" target="_blank">📅 23:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جنگنده‌ای که صدای پروازش در مناطق مختلف تهران شنیده میشه خارجی نیست.
هر شب هم‌زمان با وقایع جنوب کشور صدای پرواز جنگنده در بعضی از شهرهای دیگر شنیده میشه. گشت می‌زنند احتمالا.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77015" target="_blank">📅 23:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VF4T_LYFLvwipxCF2Ds3HnY_uvls_KuqadlzfKJMyu0a9IvW13hhipdAEeq9bwGiN9Buqp4IGjfLfYeb2pDKlzyB1-NThga_10d0UOaqZq8atI8eewFJnbdagGROFXXax6vuAfjpnOu8pt3o_ofIwamAt31jFwwOVLkdLe_wW0OgHMKzEUVlxGcYufoVGBIZQtGsOiRVWxiirUM6PX_nLfTl8YZsJ0QzbwcSJqYxh1mA2qc4LhfKRJyNhJqkiL_H12rc7AuB7VUAven6JGdPwSlt9gRJ0qROj_-S3hPVfc6CyR-lhaTppyo5mJQCsmEdtwmwVCLogXBRYwdoBlw24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
رئیس‌جمهور ترامپ پنج‌شنبه شب، ساعت ۹ به وقت شرق آمریکا، برای ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع سپاسگزارم!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77014" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایرنا:
خبرنگار ایرنا در چابهار:
هم اکنون اصابت چهارموشک دراطراف کنارک و هواپیما امریکا در فضای اسمان شهرکنارک
صدای وحشتناک و کمافی السابق درب و پنجره ها شدیدا لرزیده و با غرش و لرزش همراه بود
صدای خیلی وحشتناکی داشته و تا چابهار و دشتیاری صدای انفجار شنیده شده است.
همان انفجارها
فارس:
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس به گوش رسید؛ هنوز محل دقیق این انفجارها مشخص نیست.
دقایقی پیش مردم در چابهار و کنارک صدای چند انفجار شنیدند‌
برخی منابع محلی محل وقوع انفجار را مرتبط با کنارک می‌دانند و معتقدند مردم در چابهار صدای انفجار کنارک را شنیده‌اند.
🔄
آپدیت: صدا و سیما
برخلاف خبرهای منتشر شده در فضای مجازی و فضاسازی برخی رسانه‌ها؛ در بندرعباس، جزایر هنگام، لارک، قشم، جاسک و سیریک تا این لحظه انفجاری رخ نداده است
من هم فقط از کنارک در سیستان و بلوچستان پیام داشتم و از هرمزگان الان پیام‌هایی درباره شنیده شدن صدای پدافند در بندرعباس دارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77013" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d63f96615c.mp4?token=gg0xtcqpJ2Kecfqc1pFjFBvcJ-d7NlwvTwQ2vA5IvZIaa3_N9PFvM9_v3ceZZG9du8SMAJYGmvQHXwIZdwUiRyzVyx1NpJt7hZXw6B3Adx2PrqOaybg1sx1JBSt4K3EeGPZCylevCj-ILBG95J_R4iPpZCa7pEVFkfym5nleBlS3ocHQJ4HG4hTmLzkkzuMz1nE-xX9c3XTjenvKSvsg07zqqpiNt6nMxhbAUMMRBVFNYWByFIq92_PCafEV4jDvrE7oQQi4KJvDXFNglvpn1G_5tW_tiUUbleX_ujmfbPt3oHYK8y7q5y1Nu8VvVkilM9-kiLZEua31CozKGGGnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d63f96615c.mp4?token=gg0xtcqpJ2Kecfqc1pFjFBvcJ-d7NlwvTwQ2vA5IvZIaa3_N9PFvM9_v3ceZZG9du8SMAJYGmvQHXwIZdwUiRyzVyx1NpJt7hZXw6B3Adx2PrqOaybg1sx1JBSt4K3EeGPZCylevCj-ILBG95J_R4iPpZCa7pEVFkfym5nleBlS3ocHQJ4HG4hTmLzkkzuMz1nE-xX9c3XTjenvKSvsg07zqqpiNt6nMxhbAUMMRBVFNYWByFIq92_PCafEV4jDvrE7oQQi4KJvDXFNglvpn1G_5tW_tiUUbleX_ujmfbPt3oHYK8y7q5y1Nu8VvVkilM9-kiLZEua31CozKGGGnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۲۳ تیرماه در گفتگو با شبکه خبری فاکس با اشاره به ایران از لغو توافق اسلام‌آباد خبر داد و اعلام کرد واشنگتن از این پس رویکردی به‌شدت سخت‌گیرانه اتخاذ خواهد کرد.
ترامپ با بیان اینکه «توافق نهایی شده بود، اما بعد آن‌ها آن را زیر پا گذاشتند»، تاکید کرد: «آن‌ها همیشه توافق‌ها را زیر پا می‌گذارند. ما با این افراد ۱۰ توافق داشته‌ایم، بنابراین، ما به‌شدت آن‌ها را هدف قرار خواهیم داد.»
او اعلام کرد آمریکا کنترل مستقیم تنگه هرمز را بر عهده خواهد گرفت، چرا که دیگر حاضر نیست به صورت رایگان از امنیت این آبراهه کلیدی محافظت کند و کشورهای ثروتمند هم‌پیمان باید تمام هزینه‌ها را بازپرداخت کنند.
رئیس‌جمهوری آمریکا همچنین با اشاره به سرکوب شدید معترضان در ایران گفت آن‌ها تاکنون ۵۲ هزار نفر را کشته‌اند و با ایجاد فضای ارعاب، جرات اعتراض را از مردم گرفته‌اند.
او در پایان با تاکید بر اینکه «آن‌ها گروه بدی هستند و مدت‌هاست که همین‌طور بوده‌اند»، خاطرنشان کرد که این گروه اکنون در حال متحمل شدن سنگین‌ترین ضربات ممکن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77012" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1dhqRbe11ieau2nG_m48OF6cBrj6fqefPxBhNWvmMDtCy_UiM9HCofH84gyhcV2jpRtzSLpM5G7nueb6_X8OIpGXK-YwG5m040s340WxSCKa9eF6whQrFdu7OZLyffBhe8_vpakYtLRtpfCTx9Z-iGAvO53qwWFyM88-ORKtsqZL6P4sHYE3q7C6zl-5YK1w9DbrwzUs0C17JW8Q2R7jds5dOpDBHP5SPVChWsxXMsha1jlOaUvpvudn1Qv4glPgiEpgpX3l97r7LaUF0ZyzOg1t9Qk-fg7ricQsPK9sM8jExO3mWZL1edpEIMvvx9YnaUlM7-3HG2YZm_KRP_nRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، به‌طور رسمی کنگره را در جریان ازسرگیری درگیری‌ها با ایران قرار داده است.
بر اساس نامه‌ای که جمعه برای رهبران کنگره ارسال شده و نیویورک‌تایمز به آن دست یافته، ترامپ نوشته است نیروهای آمریکایی ۱۶ تیر «حملات دفاعی علیه اهدافی در داخل ایران» انجام داده‌اند.
به نوشته نیویورک‌تایمز، این نامه بار دیگر اختلاف میان کاخ سفید و کنگره بر سر اختیار رییس‌جمهوری برای ادامه جنگ با جمهوری اسلامی بدون مجوز کنگره را تشدید کرده است.
هر دو مجلس پیش‌تر به طرحی رای داده بودند که ترامپ را ملزم می‌کرد جنگ را پایان دهد یا برای ادامه آن از کنگره مجوز بگیرد، اما کاخ سفید همچنان تاکید دارد که ترامپ در چارچوب اختیارات قانون اساسی خود به‌عنوان فرمانده کل قوا عمل می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77011" target="_blank">📅 22:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 10:09 دقیقه حدودا سه انفجار در کنارک
سلام کنارک دارن میزنن
سه تا پشت سر هم زدن
۴ تا زد همین الان کنارک 12: 10
کنارک بد میزنه حاجی
چهار انفجار همزمان
خونه ها لرزیدن
6 تا انفجار وحشتناک اطراف کنارک شنیده شد
ایرنا:
🔹
خبرنگار ایرنا در استان هرمزگان از شنیده شدن صدای چهار انفجار در شرق بندرعباس خبر داد.
تسنیم:
منابع محلی از شنیده شدن صدای چند انفجار از بندرعباس خبر می‌دهند. این در حالی است که به گفته منابع محلی حملات موشکی و هوایی به مناطقی از لارک و کنارک هدف حمله دشمن بوده است به طوری که گزارش از ۴ انفجار سنگین در کنارک حکایت دارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77010" target="_blank">📅 22:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=ERuUgGOg8TVAfsnRe8mlXlpHvPtp5FRtA51IfE7N8OajpJQM8TtPlFCxiS7ScmM7BI3UyhWlDRnsiZdyB_-cEDsWVYlcv2DO8EK1O0V4L46wd0V3iNPpBZJR5rz0eHFgYc8PABI-XytjjS6FY3zN4wzKgEjAszIIEWGb5xgJ-4xyBlU34BQBdkRqelGRYcI1hWRDv2aQvZoYzDXUAgYteeOY3yPhLJIWzdqowBfN5nPujDlWzS1ouoD1mfpAiW6_lxdshBdf_p1LP8rQSx3nPn_sIT9-im12MMDlzVkUCxTolwl7SDQVfLwcmNZcpAKlnv5x6oanXtiQHUGvFJuNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=ERuUgGOg8TVAfsnRe8mlXlpHvPtp5FRtA51IfE7N8OajpJQM8TtPlFCxiS7ScmM7BI3UyhWlDRnsiZdyB_-cEDsWVYlcv2DO8EK1O0V4L46wd0V3iNPpBZJR5rz0eHFgYc8PABI-XytjjS6FY3zN4wzKgEjAszIIEWGb5xgJ-4xyBlU34BQBdkRqelGRYcI1hWRDv2aQvZoYzDXUAgYteeOY3yPhLJIWzdqowBfN5nPujDlWzS1ouoD1mfpAiW6_lxdshBdf_p1LP8rQSx3nPn_sIT9-im12MMDlzVkUCxTolwl7SDQVfLwcmNZcpAKlnv5x6oanXtiQHUGvFJuNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکایی محاصره دریایی ایران را از سر می‌گیرند
ترجمه ماشین:
تامپا، فلوریدا — بنا به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) از ساعت ۴ بعدازظهر روز ۱۴ ژوئیه به وقت شرق آمریکا [ساعت ۲۳:۳۰ فردا سه‌شنبه به وقت تهران]، محاصره تردد دریایی ورودی به بنادر ایران و خروجی از آن‌ها را از سر خواهند گرفت.
نیروهای سنتکام این محاصره را علیه شناورهایی که به مقصد بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها در حرکت‌اند، اعمال خواهند کرد. ارتش ایالات متحده همچنان از جریان تردد در آب‌های منطقه برای تمام شناورهایی که محاصره را نقض نمی‌کنند، پشتیبانی خواهد کرد.
ازسرگیری محاصره ایران از سوی آمریکا پس از اجرای اولیه آن از ۱۳ آوریل تا ۱۸ ژوئن صورت می‌گیرد. نیروهای سنتکام در این دوره دوماهه، مسیر بیش از ۱۴۰ شناورِ تابع مقررات را تغییر دادند، ۹ کشتیِ متخلف را از کار انداختند و به بیش از ۵۰ کشتی تجاری حامل کمک‌های بشردوستانه اجازه دادند از محدوده محاصره عبور کنند.
به همه دریانوردان توصیه می‌شود هنگام فعالیت در دریای عمان و مسیرهای ورودی تنگه هرمز، پیام‌های «اطلاعیه به دریانوردان» را دنبال کنند و از طریق کانال ۱۶ ارتباط پل‌به‌پل با نیروهای دریایی ایالات متحده تماس بگیرند.
اطلاعات تکمیلی از طریق یک اطلاعیه رسمی در اختیار دریانوردان تجاری قرار خواهد گرفت.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77009" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ98VDhkSMeEyGS6Mo8boUhv9Ly70YLlmVSqcPAzfmR4Ld7Uit5yRezQ6-ogLtg2wDHn21vQ0NoQYX-CcqZgSsn2bqD-VsqpcyDnB68fmdCE6zR3UsmqGtCv34CmLQl8WVflYd7x3SmjtefmmM0xLc9BfDrx9M8LKQKdd0T7ZMpdW0L2MI91qytbmeJn2MjY1FDI1yXcLQ_c2xSmm0unwAh6zCsz0cGI4Pczf9pUgVZ6qW4mv6uykn1w2Cmg_AyvOqPPtL-QJOlomc8YjEBq3fyAPh3KJgdQ-YQHi3bKO8dX80fOijGnFCIqjSKjohXSZIPjdBuxii0RtdvzHvWyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه ۲۲ تیرماه و دقایقی پس از اعلام تعطیلی سراسری دو روزه در هرمزگان، استاندارای‌های خوزستان و بوشهر نیز از تعطیلی و محدودیت ساعات کاری این دو استان جنوبی در روزهای سه‌شنبه و چهارشنبه ۲۳ و ۲۴ تیرماه خبر دادند.
خبرگزاری‌های دولتی ایران، دلیل این تعطیلی را «افزایش بی‌سابقه دمای هوا و به منظور حفظ پایداری شبکه برق کشور» اعلام کرده‌اند.
بر اساس اطلاعیه استانداری بوشهر، تمامی ادارات و دستگاه‌های اجرایی این استان در روز چهارشنبه به طور کامل تعطیل خواهند بود و ساعت کاری آن‌ها در روز سه‌شنبه نیز تا ساعت ۱۱ کاهش یافته است.
هم‌زمان، استانداری خوزستان نیز اعلام کرد با توجه به شدت گرما، ادارات این استان در روز چهارشنبه به صورت دورکار فعالیت خواهند کرد و روز سه‌شنبه نیز همانند استان همسایه، تا ساعت ۱۱ دایر خواهند بود.
تعطیلی در استان‌های جنوبی در حالی اعلام می‌شود که در پی افزایش تنش‌ها در تنگه هرمز، ارتش آمریکا در پنج روز گذشته حملات گسترده‌ای را به شهرهای مختلف به این استان‌ها انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77008" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAMeyARV91HqwG3HadF0St4M4ss0ran0UCXZlEiE3pdgVls-9GEM5l6Zf2dYnUuPRgL-Eh-SIYNdtvBgyasMWkg2wKEpATn9jDb9JWf92zWrQNIEKnF2AfAekihCQpLoVUKE_kVHG2s2-4hlec3HlbRJ8GG0QVzpeGffW13PFqjFK0xUVy2aKzkEk8a9O-GGQCDgcHAzKH3mIhmb52tBSBh0_3R9Y5INwDQUuh6mO59--WOXz0VZpfQTZS72BB4aBVpQQc45ozZowHCobwRyv3t34W83xwABQhFeOjjMAunTbHrJepe_lOiLOlvW9IBHKvOsQkLTCF34UWy119LqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، ترجمه ماشین:
رئیس‌جمهور آمریکا کاملاً درست می‌گوید. هر کسی که عبور امن و بی‌خطر کشتی‌های تجاری از تنگه هرمز را تأمین می‌کند، باید بابت این خدمت غرامت دریافت کند.
ایران همیشه «نگهبان» تنگه بوده و تا ابد نیز خواهد ماند.
البته ۲۰ درصد بیش از حد زیاد است. ما منصف خواهیم بود.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77006" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd6a7b0gYoV5zia1edh56Ll-2HA4At-lShA67y3KjsOLA3Ul2SBuuw0f1JoKCLWylO2eZrFX75yTMyJ3aW0wwfbwtKU_cLYfqaqVcVDcSXg-OpYN7FGTb3LBu9B87O206xyxaRttVv-CJkIl6OkeDDxF7Z9yY4p0mzVWVZbY_6uRxhWQEjRbF4tQgovBdjItQ72w9vsu6eFs9VTgkIUsc3-mMnervbBSkcceMxcroRM5wax4QFM5nFIJ6xlV9789F9XHABIAiJKoTbJlqwvBTfZq7Z5PpmDpkZyVj6eJP4NMWlX_em4Bh0fYJaqGnlxa1xRob3DAS6yKAu3SGEIB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا پاکروان، معاون استاندار هرمزگان، روز دوشنبه ۲۲ تیرماه، از تعطیلی تمامی دستگاه‌های اجرایی، ادارات، بانک‌ها، مراکز آموزشی و دانشگاه‌های این استان در روزهای سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
این مقام استانداری هرمزگان در گفتگو با خبرگزاری مهر اعلام کرد: «این تصمیم با توجه به بررسی‌های کارشناسی، موافقت استاندار و مصوبه کارگروه انرژی استان به دلیل افزایش شدید دمای هوا اتخاذ شده است.»
به گزارش مهر، مراکز خدمات‌رسان، درمانی، امدادی، امنیتی و انتظامی برای ارائه خدمات دایر خواهند بود و
امتحانات نهایی دانش‌آموزان و دانشجویان طبق برنامه قبلی برگزار می‌شود.
این خبر در حالی منتشر می‌شود که در پی اقزایش تنش‌ها در تنگه هرمز، ارتش آمریکا از بامداد ۱۷ تیرماه حملات گسترده‌ای را به شهرهای مختلف این استان ساحلی انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77005" target="_blank">📅 21:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8gBrQCRx6H3elFXSYU_J5RWPAAxcaPa7Qv0aoLidiUBHjKo-2SQgPNBAPRlcre0MiRbYUO23Za14AG2ejknDEUKfHRYRlyKW7N2ISWGBliSsLv7sZuz6j3pA3gICK7apYtDABmisoGpGh1UAMA6n1sT8LRTOrxnOom_GalPeSRsucXE_DzxHSLXhj3Gmg4lPqZny4SCLwzoFWnAFDMNgUejEvJHPYuZ_AMVC1lbJaW-5R3UiZxsacH2M_yTSHbsGkGeSRWSM-gfcI8HFTBg_IO46jOK4M8-tyH8DxDlcN-Y57vbv7yEkkD2-moM_FDO7HMfO9ctTyWH37dniTUySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تام کاتن، سناتور، ترجمه ماشین:
رئیس‌جمهور ترامپ حق دارد که به‌دلیل زیر پا گذاشتن قول از سوی رژیم ایران، هزینه‌های سنگینی بر آن تحمیل کند.
در برابر حملات تروریستی ایران علیه همسایگانش و در تنگه هرمز نباید هیچ‌گونه مماشاتی صورت گیرد.
برقراری دوباره محاصره، رژیم را بیش از پیش فلج خواهد کرد و اجازه خواهد داد نفت برای متحدان و دوستان ما از طریق تنگه جریان یابد.
SenTomCotton
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77004" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao2F9rrhXhruUk52PcOvdDNOHDzJkQPB0TVUy0itJMUyS0kaPEmNyIdqLFn3ZFn3dGxynauu-Nc9fyCqLbgrNne0x1iZl9tAbmSX0Ootk_qqgBszhDsmGOE717kkHDJCMhBV3jn_bhnxLDAHyJ4PzDUiKbI1W_Ty-l4Yh7S9-LNpQkydlNaUkz13gmuNJ1dhcrkzWQgkj-qVa3yobx8R0-oPuaJKv7zuvC6rr05Zm-F3q83oZPwDgXbiIvQNBop9Oiqv6QkfpER7Jex5XaQRBcnzSdQX7l87ySb1T_JPRKuBAnAziw-jRyLqeC_gXSNXCe8NFC7P_dzEc-5EdDO2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس روز دوشنبه گزارش داد که اعمال دوباره محاصرهٔ دریایی ایران هنوز اجرایی نشده است، زیرا طبق الزامات قانونی باید ۲۴ ساعت پیش از آن به مالکان کشتی‌ها اطلاع داده شود.
یک مقام آمریکایی به این وبسایت گفته که فرماندهی مرکزی آمریکا، سنتکام، زمان دقیق اجرا را اواخر روز دوشنبه اعلام خواهد کرد.
یک منبع ارشد در خلیج فارس به آکسیوس گفت ایالات متحده موضوع دریافت عوارض احتمالی برای تأمین امنیت تنگه هرمز را با متحدان خود در منطقه مطرح نکرده است.
دونالد ترامپ رئیس‌جمهوری ایالات متحده روز دوشنبه اعلام کرد که محاصره دریایی ایران بار دیگر برقرار می‌شود.
او همچنین تصریح کرد که آمریکا به‌عنوان «نگهبان تنگهٔ هرمز» شناخته خواهد شد، اما ۲۰ درصد از ارزش همهٔ محموله‌های عبوری را به‌عنوان هزینه دریافت می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77003" target="_blank">📅 20:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5TDjjHKwSXg6UQRnntHfrVVz8oZETl8ousnENPitHlO35R_rs9YvPM2C1f2CeBA5EiDxOtyuU01KF9YUTvRG8BP1c7Dje2msrFgGg2SH0UXJlGkIqKN6xW7Ayte484ocsjjRtdx7uo9AUN49Bwzms3SG6DAzGJ_7kYdX9u6TJQyDL9YEBcko9ZTZi2bLH70pahXHrNo2H6EEq5NASbRaXYB8OQo2eEZOhfxpU_ZCR9RHAprK8jfAjpCqVBxwBhV9Bjnm-n7Vl1lJZAYdv9u8TViktckN00CKw8Cw--1WI62arAvDvaFCwsi6Dg8uurPWmUoM5TRUW25w0X6D7zAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در راس نظام سیاسی ایران پس از سرنگونی حکومت فعلی بود.
بر اساس این گزارش که به نقل از منابع آگاه آمریکایی و ایرانی تهیه شده، ماموران موساد طی چند سال گذشته در سفرهای خارجی احمدی‌نژاد با او دیدار کرده و حتی هزینه‌های مسکن و رفت‌وآمد او را تامین کرده‌اند. «دیوید بارنیا»، رییس پیشین موساد که پنج سال این نهاد را اداره می‌کرد، شخصا برای دیدار با احمدی‌نژاد به بوداپست سفر کرده و به گفته مقام‌های سابق آمریکایی، موساد، موضوع تماس با احمدی‌نژاد را به‌طور رسمی به سازمان سیا اطلاع داده بود.
...
بر اساس این گزارش، در ۹ اسفند یک حمله هوایی اسراییل به محل اقامت احمدی‌نژاد صورت گرفت که ساختمان محافظان و خودروی زرهی او را هدف قرار داد.
به گفته چهار مقام ارشد ایرانی، پس از این حمله یک خودروی پژو مشکی‌رنگ در صحنه حاضر شده و احمدی‌نژاد را با سرعت از محل خارج کرده بود.
منابع آمریکایی و ایرانی آگاه از این عملیات گفته‌اند راننده این خودرو از ماموران موساد بوده و احمدی‌نژاد را به یک خانه امن در داخل ایران منتقل کرده است.
اما طبق این گزارش، این طرح در نهایت ناکام ماند. احمدی‌نژاد از شیوه اجرای این عملیات نجات ناراضی بوده و به گفته افراد آگاه از جریان ماجرا، نسبت به برنامه اسراییل برای بازگرداندن او به قدرت دچار دلسردی شده بود. او سرانجام خانه امن را ترک کرد، هرچند شرایط دقیق این خروج همچنان نامعلوم است.
احمدی‌نژاد از آن زمان تا دوشنبه هفته گذشته، که برای لحظاتی کوتاه در مراسم تشییع پیکر آیت‌الله علی خامنه‌ای، رهبر فقید ایران، ظاهر شد، در هیچ رویداد عمومی دیده نشده بود. در تصاویر منتشرشده از این مراسم، او با وجود گرمای هوا ژاکتی ضخیم بر تن داشت و ماسک جراحی را تا زیر چانه پایین کشیده بود؛ در حالی که سرش به زیر افتاده و از هر سو افرادی که به‌نظر محافظ می‌رسیدند او را احاطه کرده بودند. حسن روحانی و محمد خاتمی، دو رییس‌جمهور پیشین دیگر ایران، به این مراسم دعوت نشده و در هیچ‌یک از تشریفات مربوط به تشییع حضور نداشتند.
به گفته چهار مقام ارشد ایرانی، احمدی‌نژاد اکنون در بازداشت واحد اطلاعات سپاه پاسداران به‌سر می‌برد، پس از آنکه نهادهای اطلاعاتی ایران بخش عمده‌ای از ارتباطات او با اسراییل را کشف کردند.
...
متن کامل:
telegra.ph/ahmadinejad-07-13-2
هم‌زمان گزارش مشابه دیگری از هاآرتص: @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77002" target="_blank">📅 18:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=s0-rl6p_0lA0yPKZWxt4-4wly8Nzz0WpPVszXOkno32VZsBjYdMm-kUMPsIesHhWDNGcqZX2dJVmztmIz8wPVrdbQZ-jMPKiovma2lFM_Meln-3TWiNLV7XqVqlY6iM6RY83Nx4xkzKhy9-pN1FP4e8naTSrEMDjAU8IqWX6ZOKL1r91J-TDBo7Vss4YRfKrrOjR8BXuKlgb-fHHiHrIbuwEDKiv0g8RU5-O_nmT-HibALGVwACy6k-QMkOCLKcVWiQXCEP1PAh1cup6EqkvZoDygz28CRpPHYDSdu5gejzAW8k4XCorX5R4bnHPSgiW1rHwSfxcdr46RDosFEDdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=s0-rl6p_0lA0yPKZWxt4-4wly8Nzz0WpPVszXOkno32VZsBjYdMm-kUMPsIesHhWDNGcqZX2dJVmztmIz8wPVrdbQZ-jMPKiovma2lFM_Meln-3TWiNLV7XqVqlY6iM6RY83Nx4xkzKhy9-pN1FP4e8naTSrEMDjAU8IqWX6ZOKL1r91J-TDBo7Vss4YRfKrrOjR8BXuKlgb-fHHiHrIbuwEDKiv0g8RU5-O_nmT-HibALGVwACy6k-QMkOCLKcVWiQXCEP1PAh1cup6EqkvZoDygz28CRpPHYDSdu5gejzAW8k4XCorX5R4bnHPSgiW1rHwSfxcdr46RDosFEDdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام): یک تأسیسات نگهداری زیردریایی و کشتی در ایران برای نخستین‌بار با استفاده از شهپاد هدف قرار گرفتند
ترجمه ماشین:
دیروز، نیروهای سنتکام با استفاده از چندین شناور سطحی تهاجمی یک‌طرفه، با موفقیت یک زیردریایی و یک تأسیسات تعمیر و نگهداری کشتی در ایران را هدف قرار دادند. سه شناور سطحی بدون سرنشین «کورسِر» به بندر پایگاه دریایی بندرعباس اصابت کردند؛ رویدادی که نخستین استفاده نیروهای آمریکایی از پهپادهای دریایی در عملیات رزمی را رقم زد. حملات شب گذشته توانایی ایران برای ادامه حمله به کشتیرانی تجاری را کاهش داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77001" target="_blank">📅 18:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKX7wdsIz_K9XVMsFj5qV4jnEqvq2YWa0EyVsLHI9HAEqrER4VMYN_mqYnXXb2oK3ncbWtbTUu-Yc6vjCPsyLznXkHVq37Bmi5V9oAg5vkKXemXYZJ5XD43kmG2iL5oqRXR_jd8IbZ6NDuJsgt5MPve49r2N68AmL5eOZdKvk1O3X5KP4O_1HK4hau1--fsaAsYW463Mp5Iw-dZh3mgIMA_QLgFtllzE0lHadEJQqm_nnNlfLzdfBtAnfT29MjdmjNaqJaQhv99fxyFSMlh5Y_RAscigEMMnG6zvmsjEbce556kw9z0mtlb_m9x_2m7Q1KDrEY-tWAU1wJ74MOD3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره دریایی ایران را دوباره برقرار  می‌کنیم
ترجمه ماشین:
تنگه هرمز باز است و با ایران یا بدون ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره برقرار می‌کنیم؛ این نام به این دلیل انتخاب شده که این محاصره فقط مانع ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود. همه کشورهای دیگر امکان استفاده آزادانه و منصفانه از تنگه را خواهند داشت.
از این پس، ایالات متحده آمریکا با عنوان «نگهبان تنگه هرمز» شناخته خواهد شد؛ اما در مقام چنین نقشی و از سر انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان، معادل ۲۰ درصد ارزش تمام محموله‌های حمل‌شده را دریافت خواهد کرد.
روند اجرا و تشکیل این سازوکار بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77000" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1f13be57b.mp4?token=EAZh4WpppVZHhaXGGRNF9qQSMxUowGgXwlNPyhz_66jMNOO01f9c6fnjeqJ2MLbpGsm-HqNIw89JTk6n3l8pE0QWWKGCaJURvg72tc5btpA1CYGgIL7wpQdG0fExFTnDy8eCr1bQ74oBTIvtN8fbvFguQ86lYaY-R4Dl1HZK0sg9TdXUaXlXxufYJ4EuG_qgxaw5d2mFbNxG6PVUFDYvlK5hgYt8t8sEh-ExHY5lmLErCQugvDmnU0kyvfqCBLkEOBUZO7L_-rEjUB5LWAqSnjEL0Zwa5KWPFXMuQy9M8YL1zynXQwVN_ZF8Fv86FPM66XTKbmtQs0uZGHbt2mlzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1f13be57b.mp4?token=EAZh4WpppVZHhaXGGRNF9qQSMxUowGgXwlNPyhz_66jMNOO01f9c6fnjeqJ2MLbpGsm-HqNIw89JTk6n3l8pE0QWWKGCaJURvg72tc5btpA1CYGgIL7wpQdG0fExFTnDy8eCr1bQ74oBTIvtN8fbvFguQ86lYaY-R4Dl1HZK0sg9TdXUaXlXxufYJ4EuG_qgxaw5d2mFbNxG6PVUFDYvlK5hgYt8t8sEh-ExHY5lmLErCQugvDmnU0kyvfqCBLkEOBUZO7L_-rEjUB5LWAqSnjEL0Zwa5KWPFXMuQy9M8YL1zynXQwVN_ZF8Fv86FPM66XTKbmtQs0uZGHbt2mlzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شبکه فاکس‌نیوز گفت: خامنه‌ای مرده، پسرش ۹۰ درصد مرده است.
از زمان جنگ از مجتبی خامنه‌ای عکس، صدا یا تصویری منتشر نشده است و در انظار دیده نشده است.
دو روز پیش عکسی جدید در وبسایت رهبر جمهوری اسلامی منتشر شد اما نشانه‌ای از اخیر بودن در آن دیده نمی‌شد.
رئیس‌جمهور آمریکا بار دیگر تاکید کرد که نیروی دریایی، نیروی هوایی و پدافند ایران از بین رفته و رهبرانشان هم کشته شده‌اند.
او در این مصاحبه همچنین گفت دیروز پس از یک «جلسه ۱۱ ساعته» بر سر «همه چیز توافق شد» که اشاره‌اش به ایران بود.
او به جزئیات این جلسه اشاره نکرد.
او افزود: «کار اینها همیشه ۱۱ ساعت طول می‌کشد درحالی‌که باید یک دقیقه باشد... اما از اتاق که بیرون رفتند، دوباره تماس گرفتند و گفتند باید چند تغییر اعمال شود.»
دونالد ترامپ سپس افزود: «همیشه تغییراتی در کار است. می‌دانید، آنها مذاکره‌کنندگان حرفه‌ای هستند، کارشان همین است. البته من حتی نمی‌گویم در این کار مهارت دارند... آنها هیچ چیزی از من به دست نیاوردند.»
آقای ترامپ چند روز پیش هم گفته بود با ایران بر سر همه چیز توافق شده بود اما ساعاتی بعد آنها به یک کشتی تجاری در تنگه هرکز حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76999" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3BhVavjAqdg8kDgrs4GkGGLA37HoW3AXhVumd_R_3Kx9RuZIZ_6wkUKzxRr6kMn4KVmGSJ76PG14Qo28af1Lj-M1NrsvsUZvyu8mLf3suHK4n_p4XgMqJJoN_j4aYp8l_twZv9gMLhjpUVI15pc-EbFLj6kyJcWeeuwCVyLkMKvoAeSSeZbU3LlvwQehgS-eOXmSKf7BcSPQwqCJiUuIDbwOUFFGT-qFl6Ka1YRobwbWSbDA0KoE4dFYeEWaHBT7UsNaIaF-BmCDoycmYsdAMyVgcia4FrMakdJKth1OrzhwVeq_Xa_RmnpnhfB0PRPeLYxOrlywCs4ESZgPHkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه فاکس‌نیوز با اشاره به تحولات مربوط به ایران و تنگه هرمز گفت: «کنترل تنگه هرمز را به دست خواهیم گرفت.»
او افزود: «ما به یک توافق رسیده بودیم، اما آن‌ها آن را نقض کردند.»
ترامپ گفت ایالات متحده مسئولیت حفاظت از تنگه هرمز را بر عهده خواهد گرفت و افزود: «باید هزینه این کار به ما پرداخت شود. ما بابت حفاظت از این تنگه، پول دریافت خواهیم کرد.»
رییس‌جمهوری آمریکا همچنین درباره مقام‌های جمهوری اسلامی گفت: «آن‌ها گروهی بد هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76998" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeOJDfIy2MyeV1mHS11TbwHRBMugJPVPv-fgDZdY5JCwQWc877jlIfR83XEKpUwQgltO9d8K8iXYD7l60WQxPKHd3skXwYCY_csQpNIHtwMoliJSxu6xhEmOVIXuXgQWuzVYfE39EtFuhgtQlVsWgkwoqYgZerSpai6O3In6AhMam3vnrjfi8yCAUdk0wVnrM6TeTxRYKR-9UAIo_Hknn97HXdFH_xN6jNh0Wr78qq56xnmKAY8R1Ru_Ab1TkuIUuAEBgJPJPjsoSH1k5GvdA56vBIZxiP3EdAjD692Czs7akTdeYSyB6UF6VzxvQ4ZyD05epD31_1Ry70N51e9nvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.
سپاه پاسداران پیش‌تر به‌طور کامل مشمول تحریم‌های بریتانیا بود، اما دولت‌های مختلف در بریتانیا از اعلام آن به‌عنوان سازمان تروریستی خودداری کرده بودند.
لندن سال‌ها زیر فشار پارلمان و نهادهای امنیتی برای این اقدام بود. سازمان اطلاعات داخلی بریتانیا، ام‌آی‌فایو، اعلام کرده بود بیش از ۲۰ توطئه بالقوه مرگبار مرتبط با جمهوری اسلامی را خنثی کرده است.
دولت در ژانویه گفته بود سازوکار موجود برای ممنوع‌کردن نهاد وابسته به یک دولت خارجی مناسب نیست و در حال تدوین اختیارات قانونی تازه‌ای برای این کار بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76997" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=DTzTxkET64VoCkk3BL9RBqRXahEfzjfztn-NUYvhKonrxmdM7OOsoYIiXp_eFmtNMZ-QaPiZublniv4EggiE38gMAJTln5r_i6xw8mY2uOdZINSeslSiU3aykfGYWOqVwT0iMtk2A80yJkPVvwOMJJdwzBIidFOAt2TlNYDvUDfOwd500NmibCE5CPcCm3FwyuDQvqbvWM0E0e8KzwQ86NneeYKqqNQaki5akbRYeOKXynqhre_oG_ayhZ_rfP2vYx0r1TYN40-MFWeWCRJsMUakviDg15Mqb7MFOBdgKoqROwFPq3FRH45r8M6RQPi8UpCZFpnokewPt9VOLtebjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=DTzTxkET64VoCkk3BL9RBqRXahEfzjfztn-NUYvhKonrxmdM7OOsoYIiXp_eFmtNMZ-QaPiZublniv4EggiE38gMAJTln5r_i6xw8mY2uOdZINSeslSiU3aykfGYWOqVwT0iMtk2A80yJkPVvwOMJJdwzBIidFOAt2TlNYDvUDfOwd500NmibCE5CPcCm3FwyuDQvqbvWM0E0e8KzwQ86NneeYKqqNQaki5akbRYeOKXynqhre_oG_ayhZ_rfP2vYx0r1TYN40-MFWeWCRJsMUakviDg15Mqb7MFOBdgKoqROwFPq3FRH45r8M6RQPi8UpCZFpnokewPt9VOLtebjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات متعدد به باند فرودگاه صنعا امروز ۲۲ تیر منتشر شده است.
وزارت دفاع دولت یمن، که از حمایت عربستان برخوردار است، اعلام کرد که باند فرودگاه بین‌المللی صنعا را هدف قرار داده‌اند تا از فرود یک هواپیمای ایرانی جلوگیری کنند.
حوثی‌ها، که متحد [حکومت] ایران هستند و کنترل فرودگاه بین‌المللی صنعا را در دست دارند، عربستان را متهم کردند و گفتند به ان پاسخ خواهند داد.
بعد از حمله به فرودگاه صنعا گزارش شد که یک هواپیمای ماهان ایر در فرودگاه حدیده به زمین نشسته است. ویدیوهای منتشر شده نشان می‌دهد مسافران این هواپیما پیاده شده‌اند. خبرگزاری فارس اعلام کرد هیئت رسمی یمن به سلامت در حدیده از هواپیما پیاده شدند.
پبش از این هم یک پرواز شرکت هوایی ماهان ۱۳ تیر به صنعا رفته و ساعاتی بعد به تهران بازگشت. این پرواز ساعاتی پس از آن انجام شد که گفته شد «توافقنامه حمل و نقل هوایی میان اداره کل حمل و نقل هوایی یمن و شرکت هواپیمایی ماهان ایر» ایران امضا شده است که بر اساس آن «۱۴ سفر هوایی در هفته از سوی ایران و یمن می‌تواند انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76996" target="_blank">📅 15:09 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
