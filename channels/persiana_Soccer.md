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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 425K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 21:55:24</div>
<hr>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIhco7KVl0Dmj-kO-xFH5pPZWHbVZFcLvUXAr5098R3XSsuJBHy5nGkhi-kaw_cE9YSDZte1-yptG-LOa367uw0S9Y8-XsEF2VlX3xloSwg_0Xt1INveKh4bVeh6A5vfDhtz-N767597CxEvFmfcIhUj0uAUisgblhtk8gTKnLTpy80pJv-sCplncvhlRtOTrIqqocvvcBJPWUgwpx8FVch4_2R5xaZrAgcEMeuyFBlLT6GdF-iHbdHC87srylIJPmUGBVgmJ_IXWwIshwig8qdOe_u0wi5BjNGLmk6TWk9mCep-_LRVwGCGNufJHlyEgmeP0eunqQJq5oOcIJSuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZExvXYrKb95P0UkX6Lo-i-Slobbm4dLHiRxV36wzp6jw-MN22FGKo_6MkUdxtPA6JkjSB51FCRe4P664vq61_PglWacWSd6ux_JaAxeEUeEOovrVCbHaE9xN09LGjk520zMw1uZ-n8jYboPp06GGhMnoS57CmWKNpM6oaY0kxu-ybSzeBgTGwQVy1jhg3_nJVmt-VIxXzMkiGObSBR1eSrM-KwoOVsnKJP07Mh4gWInljJuEWeSv61gQ6Uvw1GuAt-_pIvNLZTPfHrGSzvPs1tOb5Ddrm6SCGrsqXxEoJi1FYn1xKVfrnZffQIcfwRpuFIh9h4aYvfOXqBa0pPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxKglsdb6Mbd_UNUzznSEFJba-hUcAlksaFDxgogYHRW_1hWPOy1r3HYgMaum3LCflVMbe4vfjg39cp94ZwqluWYR91_Ar6kfmcIyolrmF5yZ3dUZ2wGvF0mC4d3mWvi3hpnDmEWy8jeEfcQsOnODnZ2qbSuI4tZR7vExqgOKU2nPkWFFpNy3vGt-JAlvRpEsuxoErpbToDAnlQFk5JMp1aEtlnBn02czNBv464KW8-6nCua34BvFViKJK1DVEUx-agNm7v5DqJL08XHZ2VMdvqqwZJPJiiBHo8Dcav7JTrzBnLX8f1Ea2jfHjVd9fIXAsqbDxStn6cmTbsfhWXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U96hKYMfFSWOJnz_zWk2pW9JQM7vex1V5H4S_X3gGEB-KSggWff7HGNdszgoD1aI74xNsZOOwsbbYSyzAIawoxFtXlkzx3k_BBuFeYDwkNqZ6FLq2N68E81tWE6QWDzPUQ3m414UItrjHj8Nd1BMpx4Lb81DUQc7kGtDqmGtfgun4VoXbDlAE_sd1ATTdrsynrCtQZX2GsqHeeQnNubI6W8iZDrxCIx_KOwFfleY_Dj-k3JjFMVFsCuFoQGNd2yLt1hGfJTg1jcDhzjdAlGZO9VymQC3r1t8t3kuBk3DwjibnaMat2lg_zlOEb5nXr8DLQs33SNESIkhjK11ZEZnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTxGXxJ3hoILIB72CYQz0qHjgi_FtmHAEq97suaoFoMfCpwZWUQL6BexJVUmynmNes0tKtb2cSrrtTwmQQcAU_VaP3OetCS76XLRqKSLYIjNPWz2V6ah3vbNNqH7kBARXHB7wu9OTouk5Jj5-5j35DM4wTMF4ubGttGjIV83JKfjFlWEeFj7tqXwDbjMHRLqnMxWL5nlfW8JtuawU2DoXRRxyOGho1VIGV7wUWNWC631U99dgfMTJhSo1pIAJ0xR8yYI-JvsDAcIfbAbrceb6hIb_-guIwpBWVniTUlV8z8cmzAAdYGoLqhBNT-2tryXVie_4-Vw4JTTngkIko6MBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obV_3tY_7TVC9N4T_o5OXBP26OreUk4iCQOrDss-b-TNpMIrypE5QNJu-uwHOnR_UW56nuCktO2Qiet0FMfENvCHQgCfn7EGGxt2qeb02tXTSeJgIriEzBnUW04gXc4CS3GN6BfNy_oRlO5YtTMlzGEDOZth8MAY-cBCZ0deVWZCiRjvNB2ZfB8A2l20OKfb97RJhlEbapiqd7Y8aSz86Z8Ai_1ULkN2t0oPIeEmfeJB4x4CrbkYLhrL61JN96Qk7SRkXy9dtHW6QszQRHxo7Z3UuIMXwZKaCJFzlEhj3xzGX6OezfsVq4uFjHt93OfTQFkj9jI9irCaJ_-7clR-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RUTwyZRqGPi2vZ3QLitp4ELcloGQ_S2tr4M_UukXExyTa8xP5mm8GCyT-Kdsvua7AZIUb0qcb1FmM_yhBJKhIuxF14OiwvAMncpFt_ulePmJ1FTAB6buJC6jX59ezNbsUK2PwYp1bVfQsqgDJddz8Dz5MUTFfapUhos3S7Yz6xb871eVwNKHwjeSpO0LgYWIrT4wBYRdJntO0IAnWXxBZNpoIc-m2X70gnBlo4UCsE6dbbGCrB1cvy2ih19IJJE5cwroCiCIflnMkLPwNKafECtqJz-o6Ouz3cBlOcQVQpo0-ggjKEOSUhS-x78h2Hs4gw9NYQ58ILdiGytiolkL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RUTwyZRqGPi2vZ3QLitp4ELcloGQ_S2tr4M_UukXExyTa8xP5mm8GCyT-Kdsvua7AZIUb0qcb1FmM_yhBJKhIuxF14OiwvAMncpFt_ulePmJ1FTAB6buJC6jX59ezNbsUK2PwYp1bVfQsqgDJddz8Dz5MUTFfapUhos3S7Yz6xb871eVwNKHwjeSpO0LgYWIrT4wBYRdJntO0IAnWXxBZNpoIc-m2X70gnBlo4UCsE6dbbGCrB1cvy2ih19IJJE5cwroCiCIflnMkLPwNKafECtqJz-o6Ouz3cBlOcQVQpo0-ggjKEOSUhS-x78h2Hs4gw9NYQ58ILdiGytiolkL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRGj0O1ns7PG0MrADifk8JMG6f-uvpSELaPwBIa2P4cSXVL0J4pIj08MohQPparVhrp3CEWAG435JchC2UIiK_EKEjXY1zmpFq3ZMsxJDyRPEc16v7GUxn6G5KzmQ9b1Z__02-o5zeKiWZDGqnN1U4nmVr2gRc7fdb702jCyBHiB3vrpp855chzn6YLBpIYIhOkWfFluJKBUFPEZpIHzX7CBo8wdJ-IC4lhdNS8wrLBJ9Dk8zVgJc2oNP-kNQ244xcqL8LU-OVnTyOqLYc57qtq6LQ9UgpdsTjFXKaSLIj-AdAvudiG0tZv0hd96QO0DPVTihrQ5p5jtWSXogylyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA92UrkPVvO5oncbNgEdmpwN_E0t_0Ec_xy7NH4x5C2SuV225LWRuXS_5xiUL25GD-zjHYJQ1FXgCvcJE3TB2X90ZT2rieXVkiknl-KHDW0rOcbeJiCAOhGxARf70RcbCh9VcnpTqoRjndtUZNKqhVtoQJURFCbxbGMNbZ1kBdRHIp4k5pJVgrsB1gMJMWkO6dIT03_pNnVYAuAx6UHs5vYzy4VzRKA-0kmCRht2Dde67-45G9l_xXLmgS_rZSvMYMuQYRSMl9I0q-LV_6zmDR__sNOy21JQD_EgW88NQu5Xeg8H1P3hYZBowcQzWgScRUbe65rXyf4R9flzsoXWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiQ40lKidiwAgpCBV9qfkTIsc_t8uCWSV3RJMvg9jEN0U8uoiJ_1smTajhTJDt3G6kTvMA2mP-U0b5HEoqjuH6TvA7NFHxXPd6BHWabiaDx49k-5cbKemO0LYZ5NFikl6QydUblR601rAqJz0c1BPsgB-QJyrs1sGdSH74aQEBRq_JyG8fxAvrndn84ZD7Ey1hoG7ZXJbAzcFUC_So-afu-0c29j0CBkMkJlHSjN-WWYIOKmBP7qYy9IA1QAD-pYTSdAqJF227wpiSbFQNB9GUlJOY9GxB529_uS6B6GrPgA5p1JbwafypWKxCvUnLAfSClwe8ftHDzAsv3DXwLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7bSr3WeT0WfIBT7Yd-GxAQmo3yFhANXMbvcwybw5gBvjoHT7aB3Y3sD0-8II7pPn5VvtMWpl3zvoEFOg0zBaE7ot8GnNoQQtngcGJ4wlMmhs4i-RIVMd1c6THVlcH6ksbshhtM64wkGIR6jkRHysrWMKzLgzu-LKG4JqOu0AqlaK0ZKG6Uylq4FQ2tb4UxZOXDUoMZDhOs24PnglDat0YRPKAZBUD4KUu2F3KvpyPiE-yRTf-z05afYBlBoT1-2fHsMQo6yUHLXFZ3CxQCNZ8U4ajH-RaFQ1bDK5vjuTuLhUsvUaRP35ZsuSs9ZVaTPtj-15slZ60KT9qMNllekBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyk0LMIwkAxLtPakownpgSQAzoy-5t4zoL9fFf68ew_BJwfuhTQpOo0R89qKEJQcTp0nhhJuJ6UKxEfNPfEkuRsF8L-LW1CXcNa0YBHup0JLLBa0GxT0TlCJmmV2J1DtU3Pe2WziUU63KnCYnRPtHnq0Twno_QbciuO_7zajDykrhvjnFFq3PhhYkWNBW7iCQ1TemhEXCPBdmEp1y6Pj0_hvGFWT1vTSnPSQD4zbLgsLq2ppPkeD0NOq53rKjnpNx0IB1LJvC-9-4mm85RqqqGJ9dcZ-Z0Q7PZSXCXQ0PZ4Kn3gCGJsdTJiL6YfcJSzUx-7R5VeBwAS8L0nnvKs4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwChkSfxQzqiBvhaniubPFE4M5IjbvUmW87Uy_0ra7cgkxqDGjRek4mH4elgHRz5JZ_0MfOOgpAtAeF1icb0u2Vp6N9tS7xvo147ZowlK54YfCTdOMXk_XCyfuvaS_TH8Yl9jRrY3M-Gi2l24LN-eIIBlG8DdgWtkmiQ06zqE82AePGW16MR95a_Gd7nS3j36iSzJC839PnYNRLYGFCSIcUELBdGbQRKjAotKHz7O23QNO50NQx4HC1RE3KxadiGGJFojPNHS6J7jJ4K9l89FNawupg3FfTtJkgYrfOhRzrQzqKBGIolzKZyVEC5jt3vMujNY7TJXvBls632kXVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk3GnIEwrxW5c4Ctgg_MM6nvcagjPCBEUHH2TUNjeGpYUNpppBarelBSOISREOorfaqs08krUccyVKze1IzDr7fUWJrA7hVS76EP53fW-KuiOIo1SFz6xkqxafBQHpGGE856a3ofOGPBn9njXDJZxLfsle1_ikZECEkOuz9T_IARRe6nO2l7gwlyPCfZH89rYviBZJR9jH6HQqOgCeVtaJSpjlz0J2U5p1tmdxWXt5K7Udy65wESNmDQrGUpzNqJS5NP5TiDgDi9YKxHmpuTXbWknX4HWWFTDGcD-arSEOQo8ttf7AhpZMbCigW1RSQ_qP7IGiEC_MhUdZefLtiH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz4XYmiLMeJhXpeYvf2Q18l1doF1AczmabpR77AS5wDymGORoXhBorljv08TU_jQoV7XGGPP-RcEuquGwvVIGYNVXo1mhKbhhoiVHD3-JuanhZ6V4TiYo2jHVqkC1SHwAxT7xypksrSdL6Gq0DT98ykjcJ9YFkXI3E-_XqThp9e13H-VZM04_rURv4ZuviLXIccix1UTrSu_EoFjKYCVqHCuJ90HEQYh09LGaxzaaqfQ1TN7b7I5vrgXIWz1g2j7ZLUARepSK8CzO6zlJBvUz4Hxmsan7qJPfXKSxs3Y7057bt0uQDJr2qRd_mPMLLaSBi1yAZgFHCR31_V6LEn1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY5LvNclVQ35gJgzu-cvnHQWz6Cp2amGWmg7o73HS8PHdhGp-vvQe_5lR5LM-5IYOQNXpwNM4VNqvq6ZW3KEJ8gMUx23WtTCg6tOmZJavMUgoaDE3S9Qx-vpiw5gRH37X2jd3kG983IxUlgmvHcaYuaTkKJmd2wEsnZH4DO7YJK3We_okuSajbyOqsmbHkUJoPhN8zYSuJEogkr-Fp8FuoMNe6aL81mAyJJyFpt6vwtsc786T0u48CCvsYeYPgiRFpBnHSRoxp6KICdlyX9uFgZqMSvB7-hLv1M_8XROpZNF3j9mgZXCQns6fgAj6-Mf4PBa7Poj8L813vIeAYXVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f29VcSfIkNzXjSsbl8FKlqsxBeWDUvoUErXKoD_pmvpN0gPNAaTNxzSOftrVR8DkQIRpWtq9uI3k3kcOuhclprIYy4WnPl_4Q6xBXb8eeCH1WtEAAyBENFMlukO2An0Elh1etoBQLsnKvbRduUuMZFgso12_Z8aLHHzuj6QndrsO3jK0T4gwXFKwpnVK75he5hCnepLTnnHwZGf6ig8McQb3gDkNIopmp6wjttl4PjBWA7MugYrUDplh5LFMqYs6Xs5V-v2b_pMwzKaEtx654dbLyEI8qYoc2eQbyJJQCgPx60Agk3Licul418Z3Huya9vNQwXpqSwGIfsl-outSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9PkffCtbuCZC4-lffGKH9C14u25mzi_Z4tph4tDe0pOFPKDN4LmQMfpe2RdAJSg2FBt2FrAfhHqQJeI6lmkgfZO0XM48mPNEm5JJXxnYm-DmrSLj9p3t-b6oe2ULR_9EDS2wto8ratuPv3EpMXVtg3J1NiSUbhVP8xm0S53LfT0aAFIvh2SvmDo-TwTsLcanaG5zlACeSQW-Fzia-d7OzoSIyouZVtp1edWb-jlOkWuPrw-pQbmC2x0MGKAQhuXTO6V8to_CoT9EaNlPbP8cf67B_43zm4_lZsp_w_U4TGrEyE5LfZ-uFjQJUxqyUqd8VuCjB-fSchbJL2Km52DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug4Hw7ZivYcmdIVFA129aEXD9grmBQwrwd_3NO6gyKgWHGvMxLN_bdQK7mU-WRVxKXQ7ZZ7EjPIoYTd32b2bQpD4t1p1EUPb_8Tmo07jetxXBq0e3f0-jiR96l-60sB6g03FCbXxcASRu6RxaavHHStiHkf79rhWZj5bQzPffsvgFkAPLcVhgSINkjHSbSaFVoyiMk7kM0qi8Vo2WDNTdVR37gMUTQ8x7yn1esRfE3ifXw2uv4wZjOmjYWq0Pbd27coe9-yohX2CKfIW5PG6-T78gmGKSQzoh8Q-nbi6HrJCUFMtxYkgBvPyaUp0wbr82OQ3aATBx6lTOQ2rDofKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-UiCZQ7V-fCeBkpPHdxAAvxeFEefk4E6fOh3n_TadMpsJI3eAGmfbfl7PmkgzhVPyc46oavDIQHXiV1SsxPwEV1J-FLB3Uy-KW7K8Gsx1MjOAe42XQ32moBdDAYHibuZSYCuZ-mup4lAwhe4QhGZQ9U0aQ0CEYnEOPn90K7aUC1Jr3w5PQs5BzxZ88_jYU6RKNNkaJYMeZOmk-gJ8D9A2l3Xpzi_Gu4Rg3eUUwbxqiGwwvp9OzC5yMbyorp-OnmQUt-O1u3X2CESNjQ-IeGZOBkCiSsz32453mgASTydZkwlHjlg3ykUX0wGU69By4Gp-Wloh9r25lJZsmtYlWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGIzRQtYDgCybJemVPFMSBbirfqzGxRvm_cTZCc4Gi1Mn-QcwEqn_qDMdkBmoSe0-LjG3s7no-7heRcSAn_YpX9eesNaMKTeygoWu_WHiW_y0zmqc2zWpVl6DZo9SV6pvrh8uhgg0LXKFbE74Mawsg67ydcMRplkC5vptLtXSEuvPCM7JknbrPSrYNt7bWPBTE7oPmVFnQaSgJE-JcKAbmK-rLnOaoT0ru9Q9PqlGpY3SLAPhm6iJJbi7HeKJKO1KX9erJF_oAUb7g7YWVjr_5At8ks3c2SVONYzD5WuRDMoFZelUn1KXuytYx7aRl9NbbeWqymY7DBD_DXcBQxh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r36ArEaf3Zpc146X1fLUU4B3KHNusHJMhKQ1XRbA1nKtuotBrZ_fdSrThuvypQt3ooY8HRPaB_5ZK921FgCmgImRnl1dUKJ2luKGdDOVSLJzzDLTOIn1WejFIS4k1zS4l9mZyHHMPb30r1KHLEeU_4cSzfPUL17eEBsRSNxgbAtX8zrwz5eSrYrSLy9nMxZTzbiQ33jER1Oh3V8gQttJr1UAXbWQ3Nt2d1u8fnkYHn_T7GFMcL0V3MMKxgWZZQcugz_8hfXd59HBw8wKzIT4tjHgy9YZk0uhVGpCF7tnAGRFCYM1Kv5YyHwvm3Cz2M_1li7DbBtOWfOuInDVO2BGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7Dxxhyz05k8N4zA4SkQdQneKJChbUHumD1G6BOmFXRK2JNVhOEq3IkmKqaMNHCPtrZQ5agdfMFdpJN0MBghOu-mnzsJJ2nOcjSW9vqNnZUtgrlFWklG-FAPR1j7XAWirIP6xNoVhUN3vkirngv0cb7w5pN_5CEpeKZ4ftxXbJ5VHmPoZp6JelQXmM0BDYLQ43rdsKx8TwISZ__gsnJWgMtlKkhA-5tguAOS2bpW4lTNwAqqKy56GRhO_kEm-hn45V9_7nb5r5a_U4FIP7mtG3W1VoOP0rQlV0PTs4CGsLJSu1DQQVJRn-WJuDxpJLLveb1sQ33x-8dTwlnZvOfqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGgLmFVYaKR8l9xSjnkyFNarXnXsTmZTzQY8Vz6276LMEVWChtRqjKoGjwIAafEoFnfmvVkmKx_l6KOL_rPpeoNsIzL1wvNM68hOzNAkk1Cck6wlyOp-KPlEazkW-AD5fGU9QvfnKEv2ow_egEw9MaQmiuw-rSNOhboSDiorFzLVERuWygMM9QAz7pG-buKbt8wX4EdjCSaFo1JdpPlKLk45gywEnZEQze1kmy4j8sTzzn8liY49U-FP8qrg9cx50Gy1PSQgygJqAOZ4JlhckPHQzkrHK0iUEPYR9G8cQFWdc_GsiTSx_hHLw5fNwfP8xps_kvU3bQFPesIiI-J0og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEGG2VQs7mKAiluUnoFhNa5-NLscgLHLoL6AuOKsz7kBVVycV26Vub2aN85Td0RYM9GqPNFjcP2QeDBb0Cgzn9BkYGMgAMGojWpqJOj6JBRRKTWty5Fizhmq6QgTXTGynf7LmtfAPjygVjpY5EyTBpe5PFceXXCSZzbtz4SvFBs19j9beqcxiKm1K2Gmzga7rLlIcsMSuf3PstpUPBlfgowAMg5C7PzuPadelhEZBBz_vKzKpPTCeJVKQzp0WqWcsaWcPnK4H-URnmHpzSg1Ivd5nMR0tembkT4_HBKKnXQec7HaY5xyy2iCSIqJJL6Na3Lc02U5SeJ5e14k6muNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJe5WjnWK2BClSb6LCaZFtXzgr0x6fRaaB-2LZkU_xhwqExkkZbU6E5oEtqph4U0kbb7NkOXV5-HtDAP8Op7TKPDz7jqWMbmhnvcAxYC1vggvC7sdNBvDmCQCw3GCXNSfMDvul4HW96jkFFeaSCnNJ3xpYbcCcAGhjFj4jyAv3ktvpJW48z8oAtbWihVdzdOHkKf40AOI-26NkzqfZx0Dj6-8gdSTGQHJJTukQgfV-xyupCKybAm6Dm9a8njfzcj3IM6kZ6mpI2xpBKzH6eJVu50SP7Ct8yQigU70kSHV9YZu11VVAUEyob7nobWeVYFCciBzNmfgRYQvRunirM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf__u0qFYpuD_1-6Ohm_m9fujtjTc02TtbHq3RglO1sqyULvDgv0XIwzgZWviBKcsaQ5oa5ze6bKxJ_8J4JaMzCWHNanXblPTvkv60y2anLUkjXizwGLl_dcawKGWcZUcuAgSPAfdcMWRBra3UvgPDxKETWfa4J5wY5vQHjQAq7rkYrgvHAR9mkAnraaghKXoD_0IwG33OdEPHR-H_IX_xXGlMhQw-qkxje0JyfdelhgxTNjWY7X0zBZgqg4BbxMcXSxn5wdYKJrbREv2Be5c1QiS9HOPN9YCy47tPuyBlLUQv9r9XBj9zxuzpDU1Gf_U9e_X-GdzeK-znRxNDvp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1qFi5NPtQNL8jN0ao0sqmK7yugCS0ZaBZZAGTgAZKbW6hppXJtvLfEkEEERPdku2GYdO3-k1mVx1PXHR63VzUco1hAwVksuIW_PyNbt5sGVXUUOg_NnlLMhkrxK6QOBC4KdZImznHvpCovOahdNBxwbcd-P8-9ISItDPsOZitcsVQzweDMeByu6GZRlQ1GyFl3Xav2uhpmSfuOoE519ZfVg87ALKUWQyyFQE7hni98UhKLTJmYrMS_n97bJZe4Ltce0uEXx_J6me5ZErNdw09NH0u_46AOWVkqCGUcXDXNzNYzj6gqpKY5iBoPJBseXmxjATAiOiR9y3EUbfEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m83TIinvhdBIIYLJT7-BCiqG3J-s-yVJtiY8-ODzaWnXUVYeAGlyRfv7Nc13FzN-KIdcB0KeJr4s7plDa74bozmuxtCiUJamcFmvJV4N1L8IlZXs-wEqL3DmFcqjhMj5zbkQa9r01FW_tClDYzurb3D_fYINcAOJwqp6BZWEYnyAt_-KbBFwI9kEohnYSbgh5XLKIcIcfjXSH3bTV3iFgCAB-dRMs0MlLu1jTSi_DQW0qcQz-sf2lC8eBS4wvTMHf8o9WeOS5Xsq46N7aCrLIGdgOy8llGZLIR2BS1KqwzCarq0D610-YRHo8FPBbdm0oddhlW2C12fxdO_t4sWlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEEWWnbV4hTnRMjPbh8OPTPrLoTRXXRbDVSBie4HGeq5yRhuRlkdeubPemVzfOz0Je5Vcf3DpptaB1idwcovOoHHFWv7yjxfS344VocFERG6g_J5vPJho7xQHXL58NDw-4jsnxiH0Ng3qZjJJHaSTXdo6CI2PwK5wO1zmMRvwKxNX0o_l1UiCZO_xQFbToI5n8BOGiiGAc5dRYir_yEUk0tshooHB7zsxzuBs9P0eS7kVLepsOTGLh__IC2Sef-5RNenOSQWjR3VfMlMHZmOzh6hj2vwMt4J-kqu_AoBhlGflwjmsiTGhKHI8hAOd8-Rn4d2vlMgCC72Rg1K-pnP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfa97lGFEDUmhkFGsDXDBQU85ta5icewxOT1aK8jFTd9Z2IVZAnFGS0iQfw9mxdYjo42HAPNyel0-vFXJHluR0ukc1FM29Hm8K8jrdP7EnSaRMg8gxklPoPuBTEyTYj2uq2ef6eU17bZbYiJr6Kylv3S0I5Ug1p5aNNliliwSRGR76uh8FfXclIDGtSFdajGLvUOQanPe__3AT29Bzk4FMsQVwQ4Uan_NbYmqRhITXIQbDzlaGgLxt3_J4abkTcbJBeyA68c6SvQUKl-PbvbfAfUq1loJ2UN5oULZvCYHSg_jAhece11ojXe9wc0ec8JNIw_ZgKe2vbO8SQd6G0xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gTrlnCYnlBVz2PZYIbM7vK3SOSUFwI07EbwVmLxHPJi8cSoZwH42k8O8V1IPEyi69sZthk22jWjKTBC_bC3-OzuV3XjZ5dmFlSzaZII96u3uT-1Mt4BMWT-8a37KezYvhSB9bM1_LFlFoLNnR5ORRqJkx4pM7NUdNUI4zKCiNsOujWiGs7Sq9kjBaPUrbm5R2EA6jXOdcrI9p87t-mYcnTHkEJyIBbm48Qx2svcYBjLZgO3xsi2cVXsjSMAegXG8_5lnci99XVQvj4gyTQT7SftTQ3yUI4Q82x8gGTGPTsgTj28PoEp359wPENkL25E1BWQ-ywNNup0JemTow-GFqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gTrlnCYnlBVz2PZYIbM7vK3SOSUFwI07EbwVmLxHPJi8cSoZwH42k8O8V1IPEyi69sZthk22jWjKTBC_bC3-OzuV3XjZ5dmFlSzaZII96u3uT-1Mt4BMWT-8a37KezYvhSB9bM1_LFlFoLNnR5ORRqJkx4pM7NUdNUI4zKCiNsOujWiGs7Sq9kjBaPUrbm5R2EA6jXOdcrI9p87t-mYcnTHkEJyIBbm48Qx2svcYBjLZgO3xsi2cVXsjSMAegXG8_5lnci99XVQvj4gyTQT7SftTQ3yUI4Q82x8gGTGPTsgTj28PoEp359wPENkL25E1BWQ-ywNNup0JemTow-GFqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyAvJwgY3o53afDdFc3C6-YfeLtbqbp6YOkLyjNEmXaROtkjm27q_Jym34OUZ4-RsqxqBSzg8EFbUPs4ZrK2IPZECwvyE-95i7sUWaT05W4cYpZewUIljzxQuqIHMqCPiF4HBbCYvbP-wS8vC_oUqLgqNHcM8G8ThxsP59ZgUiTWUy7ChSDLJhovbB4dVZjMJeaqRoWxzVnywCjzg6_DUdf-QxLTsKLTvttBrKiCYS6_zyBNOMFlBkckQOS1vjfqTftoOZAsgwRouVPzP4U02pNj6IO-C9MFeI1MImWvBEfZznfhEVQFZqruYYOhXm1Jnsr0WxDMByQJPug6U6s-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu7Wz2898xkIBpegUNhuocBpFt2YH_cEVU7GMKLTHW28ztiHMW0lFL0lnSZL0FBdsCj2_mNGNWcbzR0vjRm0ymYjWKeDv1YtJx40ga9Nrn8r_UDW0jesfuwDTfhBXmfZaY-4u3Sn6c11BqzQjHA78tG_txaF2CHlW9J-knnhb2lL_-j-42KWAC7Ol1oGELRE7rKdoIS_AZcfoQ_zXcf4KRtZrUG1CZy8_0xnicVOixm_lYVQUOCEONhwRkiAUNxofbuzTCfdGPxQqwV5QptdYPurhD7FMbVyVh_c5mo7m94mgSyJNPU0K9xyJAAaQ01Xit053M4zRsMVVF5gH0jo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=G9eOBEQNxH4X-P6vEFaQ9sRUa6NFYiNcU3jr3IIPFO6CGg7etUQ4WaRsztC4khorpUSplPup160WuqwGLdRnmoviLOYzZrwFinOpsAtwxdrzHK0js7Gt2IgC6Hh-fuiseiDMsHh_NMcYOqsjnIa0Z_8z2CioQ6Iq9u9T2gSVQi9bFTJtyzIiggtz-zJXWurRiczNkC90-ahmh8ltx6tDoG3zP7S6mpYYzjX7W1b-NOOyeGAr0si6Ur7alHS60xqzwIj2DoSz06qoHfgQVybN5_kCw4ltczqvMkq8O3rxoZCkHPIHa39NPS4LabK3n-hguc7St65W-kBDsrnju4L82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=G9eOBEQNxH4X-P6vEFaQ9sRUa6NFYiNcU3jr3IIPFO6CGg7etUQ4WaRsztC4khorpUSplPup160WuqwGLdRnmoviLOYzZrwFinOpsAtwxdrzHK0js7Gt2IgC6Hh-fuiseiDMsHh_NMcYOqsjnIa0Z_8z2CioQ6Iq9u9T2gSVQi9bFTJtyzIiggtz-zJXWurRiczNkC90-ahmh8ltx6tDoG3zP7S6mpYYzjX7W1b-NOOyeGAr0si6Ur7alHS60xqzwIj2DoSz06qoHfgQVybN5_kCw4ltczqvMkq8O3rxoZCkHPIHa39NPS4LabK3n-hguc7St65W-kBDsrnju4L82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu6XFIQ1oKkXASsjAPbIi5hCAWfABZ34L9JISH-hnYGWWFoQrZ3x4jz2XgPc7yNLfjZ7akraVVvwcxXtdq4_m3naHKEE0rsogln_PIADmHsXlJ0mAksyYHqpZmmats1InFFRkSE2z1E-O_5OJUIcpXC-ydk1t8snEySvSci0RciBiK6zc5zM0DU7IUEJJ0vCO7lx1akwSh8VZdgh_GqR95M1vJTBluS1arYB5vkQB7HlKqpfcebdITyHlLDeU-uZUe_B-Dfd4VMZPaaMDwHbJgkZTkKHBKT6a6BfeBuNxq7VkDrtcRNln1bmtNFlfjRkkYUFakSqag3FBKWyE3D_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2xOG8-_mJTnn8KkHX-Qk9xopz848viiv0gqfO96CsU17_1GaPFyD7K1v87ozhF7aEnpg1pJgqMfIRcJHeKIbTeil4s5cNQ6z0opIt6e3fql196jgEHhu3Qh0oBDiPb_Qao6jKBcT_M3up5F-M0sdN71M4X7Pv4BXL5wkToKHqh5r7Trd3PNrkm6p7LSctHHilGx6zrp5xU1MBmKRS6dVTit6lqRdRJXVbf9wG1EtaiZoXlnK0gCp6_uu6ybRjdz1MbXI_Wk9YAxJM43nKglJEH-v7rUDr4el1vthfjjIW1lEkP3_iAbvi_iXCNrAYmcIguO6GEREbKH0xL57tqgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8oZwv9Tkts9WkNEHzqQ6CpAE8gvnsflN2pKCYtpLjW-63pyfzU5EmBW6b5GbTKnqCtUAO9XM29Us0pshfsBlsm2fSen_JKDJg5MRepJpgozIXA1VgudNlKsSBOy2jPazC4HkzPsj6PPhUohd6IRjc1DWYpG3t7hpggLOXxsDzBJTjtc1j7sAhdQlzqEEDAVuQ9-K7LjAYd90crKL_D4xQrFF2969GnYMHo5nCvxwaGCBjL73hwPEZlENdIxbWbmrHwU2mBIStTJUkKov68sNevwG8ZjncOm9kAc6JPP8hjPG6N9p5KFLWn3u4Ytls2xP1Es87zXgRkvm9nhzHp8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etare0BPT70netFNR-T8j62uLlnb892DZwUF4ECD9tB8zIOvgWm9FQlAM3HbgWzukJvGJ4PFbhmwAuEO8ixW0X3s5kRWc9vxJcAWFB7cSulFwsp1RL2E2s-S--cqzVQ-qRgFmOEgWipsLUxz2qWiHUJIxxFfxiJFi9vw7o0DWvviocyPD3jnmMWGzR62g5jPHMNcm2pPcNHncGrvHxkW6qR1nyhYv0JeveaeXDcSMZw4s_jHqDI0a7WF62qCk5q8t4n-4ykeRVEp81d4xoV9zN1H3emDlGFDcvrc_htacuhp2mMzHJ-pieLMhDAjud5IZ0Wv_A_916YPYZk9jomOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT-_935UgqKj0Y4j6xwVMLoen_wwv-ob7jr-IcCLBwOlwMnUQw4vFVgzZo6n-z9TBsxYFE3z0v3BCKTx2qydSL-N3IVtMi5yK2l_RAF-H31YRb0UDmTJb__ZDBEnPasmol1YurJVwwPFCRdlPVu20D0f7C8Z1Npa-6vbNsdsEj_S4suWzYY6Sn57J68DF2PB6aS_HyDCZc11IhNrsvHKZi0Zm6bEiYLKGLWj2uWx4oSHetWApWbHHPf8memKeXJVi-BS2DBQBfp7QBSSyKzyhDWjPBWZeMbFfxgz-nkdCw2manJCqA185zvQEeEEIu0rQbbUfjjDIEWI8M40GINxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJFsXlzqt_8u-YxUUAIQ1tf4YqRyCNbAbYckNLAn9YNL61MWu2I7Pp2xZKLSVpTCjhqmnc-jY7TFniCXJ4cOY24Bg5K3muHtdaxoDUPPHY8U12_G3zCwK2Noy9gNYan1QzyG_LUmF3HQZTKqU8QOTIK39CkUrEOcl-ZdeHJxRpE-PaP2cKSrZonkhQtVsWv20X5TqQy_X3A31GN8Ktj7MlQ3wKWCjsDlC0bTdqXMXb0D1YlhIpFFnucAGVsUkzyUPvZvmmKBMLOlkGySbpcP79EHHeOxjhHee8wJ2rRIUIVEVenRX6YvG7W1MWf6RFEyu_EIwtmYsrEJE618ZsNRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=q5OIJr7mBhmi17SFWpoBAwqzdjceFXTx47Od5ljXH5KPitqSw0uz0gD4b8Ljwrn8qrPtTS76nzl3ZPepZjDJAYAojo1s5RV9XMqMFclc4qmRdIosBU0IEwklvVzt0pDj_Rig3W9yzuGWEoCcuO-Q1suqy1gahfeZ7zi4XCC_Al5zeKQzkKFDRob_Mx2i7f-v3s8UFvgDb8-6FRbHneK_KdjVEIQKVJKdOZGx8lZDgNLVCyg-ux0HIu72hFwvtDoGaPbI6FtbbM4s1WQDBFfxMVaWMG8oPmcO3rxhT493tbgyRWI4Lwh531_AVb7PDoyGRP81sVnPmiO5bWRdXanGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=q5OIJr7mBhmi17SFWpoBAwqzdjceFXTx47Od5ljXH5KPitqSw0uz0gD4b8Ljwrn8qrPtTS76nzl3ZPepZjDJAYAojo1s5RV9XMqMFclc4qmRdIosBU0IEwklvVzt0pDj_Rig3W9yzuGWEoCcuO-Q1suqy1gahfeZ7zi4XCC_Al5zeKQzkKFDRob_Mx2i7f-v3s8UFvgDb8-6FRbHneK_KdjVEIQKVJKdOZGx8lZDgNLVCyg-ux0HIu72hFwvtDoGaPbI6FtbbM4s1WQDBFfxMVaWMG8oPmcO3rxhT493tbgyRWI4Lwh531_AVb7PDoyGRP81sVnPmiO5bWRdXanGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=q9gxOG4m5DWb5NofCDb8AqOOUCI7Atb9hOEMzfhJiyl1PWCtVT2V21Q2ql6DNPAoDYe1GkoDOx0PGEks4HdLA5BqtgDSMTkWu45AWz3QCA2-VcxY3N6je19NzcQrjUSX7txo1xdKZJnYt65n-4TZm2XDG4LzfMEdboyh9d-Sr-CbWUl0L5OZL6DcaV3F5pvg6NdusqPqEaU9sP1oaaUAJaDTrCKEHDlGEhdp1SBdCFAZYuF6L8gTFiZFgd2ot9nnHII2uMUUuBvnnIyLvVT9sfU5X5s_XXuCKCLKB92rI4n3oCYQpOV97y8FWeiZxB2CqzX4oMnTGfdNg_gr1y_oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=q9gxOG4m5DWb5NofCDb8AqOOUCI7Atb9hOEMzfhJiyl1PWCtVT2V21Q2ql6DNPAoDYe1GkoDOx0PGEks4HdLA5BqtgDSMTkWu45AWz3QCA2-VcxY3N6je19NzcQrjUSX7txo1xdKZJnYt65n-4TZm2XDG4LzfMEdboyh9d-Sr-CbWUl0L5OZL6DcaV3F5pvg6NdusqPqEaU9sP1oaaUAJaDTrCKEHDlGEhdp1SBdCFAZYuF6L8gTFiZFgd2ot9nnHII2uMUUuBvnnIyLvVT9sfU5X5s_XXuCKCLKB92rI4n3oCYQpOV97y8FWeiZxB2CqzX4oMnTGfdNg_gr1y_oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQWarg_O8X5JmVD0XbbTPZ-8ZLfhvxQQJQiqspc6QH5R8MqvkdZZ9D2AsBNpzI-64pFrgag14qP9k1yecFzJ954vxvXdPuUzS3vn3xu63jSBSBDUrs2eu0j3aF7ndKA4564FT4nNilZZIURrH7TPb9ir4mm6UXemcV_21T-XTwiSa-vDBR0LPN30B4_B7aQR9U0fiZpRTt9KIOgFCd6Lb9rnw55j4bOLl73Kdt1LgVC6qjjZe_71fvNElSTb5PlxRE7-h3oTeDZGJb_4wI44Hv-XGyQTCkeKivJPB9WaeAli_cs3crWepbL57A88Z5wOcLsIwYxnQQK8yfcac32LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WluyItEvSk3K_isSejg-IEgPZ4kHEmYktlcm3z0nWYkEph1Kt6_ewaARO33S8cjr_EhZyGBLqPGd5z6KyAF2C4pZ_fZubxyW1QjsQm63jk7LsboxvQrtGZLV8Z3hj1LGwFBqvdIZvhSx2gIXTQ7C--kYpA2t-uqi-K6Vk37BiK1gPHUlh0I5YMo99cNXYf6y6rwJiuuEfYDt_QgMAbFfq5lsV2dSvbSGdEcxLwG3LjxJvP9SjXcgf8rq-cNIfDG8orxLXmKVkXCTagc2KwsvCcZTDyAmJSgYIRlgzzyUd84Y3jXFA186CrIZMbrJI1gGn2sIelFPwfGd2c_HRwjasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=sapB5jtFZbLhgDHvBfYxdx2M4IfQu2wa2wANWGbTwcrIZX8DAGGp5DhF2eVtJ6fzSPrUE91HbpGGyw6vx1c0g3Z2qg2dLpmeE4rw9uo98HLYruI7axHK62i9W3UvUvTu4xrvqLjyOaQX2C4oSZViIWdtQ4b-icgpiiISTWGk9VNi0FeVK3IDwCFceZ14qcRUElkoTlKYed3w0YC7MU0dwTlJRwyjJ7CtxP4P6ZaLEuIfAS0OQ5GfHzg8ZzWYsVJhDCqeRNJu5rLyoUTfxyCoxnfMl6M1LFVuCg8sniSKhUlct68qKjlX0gBnno1tgDdykunZkwcpDwdwuU6JYjWU0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=sapB5jtFZbLhgDHvBfYxdx2M4IfQu2wa2wANWGbTwcrIZX8DAGGp5DhF2eVtJ6fzSPrUE91HbpGGyw6vx1c0g3Z2qg2dLpmeE4rw9uo98HLYruI7axHK62i9W3UvUvTu4xrvqLjyOaQX2C4oSZViIWdtQ4b-icgpiiISTWGk9VNi0FeVK3IDwCFceZ14qcRUElkoTlKYed3w0YC7MU0dwTlJRwyjJ7CtxP4P6ZaLEuIfAS0OQ5GfHzg8ZzWYsVJhDCqeRNJu5rLyoUTfxyCoxnfMl6M1LFVuCg8sniSKhUlct68qKjlX0gBnno1tgDdykunZkwcpDwdwuU6JYjWU0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJLnxZGOkS4OUM5a5WWYfcAHc6TEYpC1cVcmk-i6o5L7l0gEYPmsawZ9c6xbkbDw8-woJv5jV36dfBXSlpDUyjIPFmIXItYyv3Np-OfWn5hFkAWUZKPOIXBg5_p5Wa_d2diH2sDRbSxkto_uKM94ZFSWJ4I_ZrglLs_f_jaaLfy2Reu-rQgUAlWzKT3a1cOugz5eCRCuroNxY6Hz_HNgXF9X8OZsuy8Sq-DwjbdFjUPJddWv8fT7da3k9Nh5b9U4sSwGmUjJirm_djM33XyYgU4-yiw3h-dBu-5RN4M5E6ekXiOhcx2dxgTcrv5hg0G1v2inOeYG-HXN1hE5HwUU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqk4lKIG-g2dmHFaqSNV6OMC7udbRRxlZHp4nkvboxppeXdz6WiC_8VdPNYilB08OsAaqnFpJI-8FoBBGJ834tGkLTlIKI6KCeU-D0ZRhdUmJ_fXrP9jzxq9FD4k9v2m1IWtoBnMEeFnFO3DI4UdOMmWwqGGBjjnH3s8F05KQZNEd_8bVRh2YW1ae5J3FN_40Snh1aivKjXxiBnLThwJVbExAfD_jMSuMdpXHJhbp5QA96pIyK4u_UT8yKYAJS-Sae3UvOtc6h4nr4AxXaVA2Dlf6Dm9E7FjrwDFtiO6EE-vfHUTsE3zjLhWqSNbxcpOeNEOKOn7v3kD9izC79CobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Z9q91GHA0515RH2pVVYewgChrww0Rixtu9sbIV-3t6TyY71kDl5kmhkPhZ7-DiWrTwFrnTY28LSmIDU1jCeQCBfZ4vDxw-1HYtdfaaFKUpPDOC9hll5onehI6Dy-Wo-3PEOhgTGwjLaLLfgAkfzX8T_wIN32123aJoSIN3LsLR5Q4H5FoMqtXCee-Ujwc0t8PVSaaXINsnV7gXIy_HdakEYWUdNewfqCAXUCAWCAjBCTFfSGzvs0xbM5zK1TA467RriiHWZLC3X9vaXK7gYftVAxesH0iI9AmIN5hcYlRm1tr__hDvexDovFMs4JoyY5Vkxft_v-GPvSC7B68k1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8E6-wZuWJSOPv-BzNvio5TXYlchNXLCfXtD3q25-GeSZ7ol6d_Lj9VbdMh4UTj-zwznutcYM_MoOY70zlRF7Aot5siu0QFkdKOG_gvGynFRSxuImVw37MDQz9r4WBQO2B9evgUpADInskvrNEdoKl2f5b1af57wUJ4USRqmNx1lgXJDbLYClzuePGQ4zK0Dg0adBXi_IVfUE-RZEZjtD4ecu8FEdTI2EzD0cSXlZlgMs5jMxueKAuN5_mifpSV4dTJwtG0oz7SwurNQhogNbX7St3pxUiHDtDOEYNjVprQ195pE7yGDF6H_ulorNr_fmR-hGM39l_TGW4xy7zU9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQUtfk3n9gFmlZBL-zBFgfL9uN3WOljEKN2uKm3glH9T1hquh-WKBUeMHtY1eIhb6yrl7fn8GK6Lfb8DQxUhjI1fo8xo93GWnDub_p3tEC2AwQzeIJ_YxunSOefLLfdObiPDdSBkF9XCldblvNXkXDkBtUtbSwS3YGzIPbMpQi28KGjYXaLr5MhgJrdZ9tIKiM2ROxoMCzSV0Tfxf_JW5YEC1Q_gKPW9Tb1e67whGmL45RPfWP3ZSi26Vj4NPgziYi9_-lqBxujK870tZzzZDc-13QyN5MpWDegDHN532Ek3Qc3pBNGv4-KHVrZsmXKObve6Ie7EXU2ZiDq7EbPhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePvpQVvMaoBd8btWjVRyQ794LPkU7ECngnllOERGVo6_nlL8lkOJow999kOOZ-E6flmzQlosJs0cSujrmzdh0K7rTViSZGbQG5tfjcZMZsTP223VFrtDionztE6Im7KyAo9kdl8-iMB2QjOcaAUxugObPtluJkpMWskrTlsbZy-U9p8VYwDLJtuCVkwgoTsNStuVzouHaKEHP66YkyrYXMLVUz1ZRth3hJMft0CXhFVQnAVNT2fHKvtmwXHlRunDfEzZ183xCAP8acqX-e1xJhBqKzXz4EmGlqKreMU2ykHH70N4H48fwZ0aGpOkLgvJVfmWJuWwkbiJhEJga0JpDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-cuG28m7i8uI4uC7m7_DAvKFFApWn0KrGfhxXC7Wt6fVbvnkFwi_KsToGQCxQiweTSj5RFEPa9SzTdWkCaUca1Z8qzvnX6y0Bp-Ki_gJkvbfTLinj6uZgmPhGcwIX-HM37dHr1KM8daTgC7mZs1EECWqOl75UgbAbfZTB7DLd6XFWvGcoSXIFNnb4WnGqRmnrFVrZDA9nhJONcgxpeZYLBZOYzqsosEB2-MzVyICji6454ZN44rmbGBSYN1L9oT8b5SYfthfXu00TS9IoRecLzRXdHS69r7TAZQQiuq-Id15r14-Ul0msm6lOp3idIhQlm2Ai-jtJ8YImhaXT8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktRr2zhfxFd9keY-qUQcqvX6IAquI2HgCGAhmIiGqpi1raBx4tSJdnQSq1nogGlm3BcCTbHNz-GgXjDXOGuVdT7XllSL7QnnGKXgl0eKLaAvQeXpQXUavsh2BophY5_ABFsSrozKXcea4_D8cdO9dwDHkjWU0IoYV_13xWA492lmClxWQwdXP0sIOILhybnF18tiwbQi0se92aK7f-sGnt9xZLoWIsNy1-o69Yu2tddKem_WxIXPhiZ0hpYvoHk_E4mZ2GpEisedZjRcYOm1a93AdYv-3nM7Gma04bUDGqR4KEN2hQWCH0iOVpEQYQzbsbhIWgBPm4QxoF2iSEVkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-nwrGI-ik1Kt-h9uvmnP1YvaQxu_ZGOoaaelcgPmxk7mmCK6RQ3ykIjjwLVjvy_0olGcNkLGHl6uHI-65Rpn7PeJYURetEJqnvdOVOM5iWA3EguI28phsGjR0sWabF0x_J_6r_UZvgZTtHEps2UN1GEn5rc4z_NDURiNHPKHfaHFW2VNnVYokDDz6ZikyB5hQXm7VgTvxt5YkU3f_OIXb60d20R9iltv670S416MybAaO2ctS9gHjOSMEvaJfcpKdKbVgvTtBXDKahzhAnBVcmnvyiCyCVMIAAiAmiYMvLNHWY904qo4vxsWYri0EmBFIHad-xqf-ZYPlli9hMr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDeOgk34oLu8LFjB1PPGHxtNVGrj-X9UXVuzoJc8erhekA2hocm9Vb7Q0Mm0AJ2ll_WSCMcy7Mx0QOn00BggFvF1gA7YubgQNyihhLQT4t7FpC6DZM8SBZcsHEo8nMXNVX-qIR7fvY-b6_dpdFHl20Z6C5eKA5Th-nt2Q-Qv-14OlVAkFSohw0y5BdQnr3dWWuCb6XiwpueZWCw983Kz2er8kpF9jyG_MNnBf0ztY7mkJHfMdGhMPKFDmtoMCb1sepEU7IzXGE0sHgzf3ItnRs3tJgj5_89ly2gKm9_3Yt64rtwgb_X5p5i7My5AzClFn0YxPMgUWbwIYP6xfJYckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzkiFKQHVwT3Ry_sW5S8WJfdQ2D542xcIOFOlvE9CutVL1H2o2nuyYhHY92Ib37ifv_bDzfxnfAmhLrx1dtGQVCKST2LCoZoVxVCL7S0Rl4TnWF9h4QTC0LVa4nWgZKxGy0olXGo2CbPa9cSNNA_Z-YPrKK3tDfMoBx_Uy9YYVbJgC-CjTuUdFIHkAq7E-LJDRX_Vs6dgZk8JqIx6rFnnxTFeMW8vT_0VWW7kwn-hGlb3WUjlK69Z8FHW_hLm-UhdnmA-UklvRA5Wd8ciZwqvRMmj2qTqjZnmq31-CDTImLLVa99wY9cxX29-dUt6aLGhsZmv1cZyDo1jlN_NrxH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDy6adQUdDMc-KINZcs3MM8eftKx4XNOXpBWqFr9y-afhhJlqH7bKYUYIBQDGWxpHxmJFYt1NTT8hylVCuR3XkuHAXxC67h-j59JalkJkX75fN4xoUMP5xf7H40mUUlViDa7yxCLtqUhoBWtwJ3XxbY62Lo4zxXwOn5XvAsAOMSOi_7-kjO_uRu96y6NHG02aUWghjZiEIQ0GLkXaQDiJ-eWxM5V9Slei9evB_R375uUA7xeCPdNXjSoPAHk_wsPwng33z097SkGx7pb98eZcbzEvIqmXt-EQpdJSYsF1Lt7386zIUVjLc5fCFapGuSMVzRAWEP0LWKFYLlr_GG3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiLOvkEL612g8AFt9fV8__xvbRT1_ZPamt1mGolUFjlfqQIPi4luSUXG9_sz7Z5RFNmXAzIKBzCxn5kjm240QVsKaN5MP6mlOUmMmbWrfKwzpGTFD0tgdm8eZ2C80VFbcQ0NhwunhZ0vHCwvTO1FVmZkqWjSPfHfnEceB2kMuHL3l3gj2U7ZC-rrrAdlqgKcSXdkkOv1W8G3e88cWsZriGdM4lDEkpLvS7LuAiRI0Sh4DYeJh2LWscdhWK-44YBa3V2_PAVqc9YbyyV-GYx2r6qiSfgfauMtuuAvLLzgxGQGfJCXngxIstyXrYVSaPevbDj0TN7CeB5PNDkg4xCQ0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCMQZa_2jBaOm6g6yzd114u0qe2LHO1cRU_lJBb7ctVYmby5gkLuwnoHnWirmPm_Q0TnFsdfAIXgATRN8e9CTMXGeIm4_dNdcNgpd-BwTNt5Th6oAaXq5fdLQzebgUIv9U87R1b5LgDNxn4FiQ-6tM8uhqIgIok035FCunILb7IW9G53ucSUqKC_5b_uslu6nUa3N-xauN7L3rps9QWv8XLAyXonxNjXcjomwgmiHYTXFqxdU_a29tKDThMX57eGsCAnk9Vj_gDWrD7SUQYsrAPNr2hjslkhIpTh0jDVmICINf4RJTL-x0Lmek-pNrzI6CIYXPC2acE64MVY_hPTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw3HyjVSYEjV4poqeXvEY8C1ntXsu3vDsZE5T15_CSEiYSBqe9iF-H-iKNpRbE7TbXmbqOeiItOex_kt0eNYyVSdDkmQycYzkEpuUFS0jXSkbGZcM-7S_HHbrAHW-V9hBiqrWka31nTWHL35z9IvPlwXL5L-3AaYA1WaYf6zfGFG5TD6PBq8qN6Czlul8b9NPP_dYFPR-TUH3dN7UOt_74ipMse69D67-ix03fAPv6ioGNUk3s7bF36YXGqNo5BWvsErcOwXr-hDTZm2HSCCQknRc2e6Qtc-pqA113fIY2Bxz9TWjTuHp3gJxoeFrYN2aB10wKieG21xE4CWbRmgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcREXvavBs_5sjImfi55W28NP47dvMk0Mvz9ScywMscFNk1lJbvftpbugp_uw_a-xn7nJdD2gpMWHKm5AJ4TJHOPrh0fERrdP4r4iC_qvVYbFWJB_m9r7F-5H-Si2hnEtvoKMZbEIdwXDew7yqlG4HaWkksilI9uwNULuHzAAhl7trrO8NJzFvz6yolQS7XGdB553KRAMziiNL-RlKjjxtdJNp9TWms8JxoIzDtxTi3WgINexNfvhCQXVDEouEyQmJNw8l1WQTl5WqdC4Rdw6DEYTNnfz2jm-h1wPlkpLnPPmcwRy_UiWGSlX65b5Esl1Gz1fleO1N-z5JrtoJbwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2CDLiORQjjqGmVUXHohdrDylFdX3BcmY6YXdzzhrnwpDhovurYVJ1BUZMjUhk0bbltrObd9yovU_kxGDs7iZTe88zBD0TKsYvWWAO9z0aMFti6ae_sw3Y-5LayV_drKdaOZawRPGbk-ICZJVHqlYP0m3GCG3cpnvEJQjxr1IONIe1SMTtkWlPOW-oJPwN22jPlL04mZDq7sNW82VXg_njX1wBHLY52NrxLwINlgrIRjYXBdGuN0kFQYR_hjCmXR_aZz11OPXivDPaJPXe5LpD00yQWBbREW484qYLnHGvoPGVO2XXZgv5WtQ7E2tGobAITd2mTtwM3DkPnFQlnwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYpEyr0qYTeqJxCzV_H7NL0dkzJhRuz94Ux9I6ordrLPKWUfJJbrGFpRmYb9WbvWWQcGG7-cYv1R9wB-k7tJ-80mzcb9Mza7enUWedufuFMImFvERjLrdwXvdvJRImkoF_cXv2LBFPuLkhl1gdgDgh54jCE2euDOGCMCz0hQ2RO6jASW5XGWlJ3hNIl1-Ab46UG7sNlJ-9OLvZyl68KQu5fExxgyV0qmzh51DmkfrQ56HO6DdnAPLSEGqfKpueaF9leFd4dma1vm9QOTgodvC6aWCnuHo41Y1dLh4O7ycegEOGG6XRmLOyMsf4CH7SuExMDoz9q22gg2qCaKpbtvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h38SFWi5KxZI43G1D0GiUODsoCWT8Q7AfIh_dhofcdSGuLb_9IPW1SpHU_FUVrOcw0AxDUAsWjCtseLm6H62IYwC7VtE1cefA2dJkcdge2MCeIv2pChHAjJxYcooi_tj00R0gGhDkoxR7SD6j2qQAxNDVIHS_Fl2ux0BJaQMeeagtv2_imKEQF5MNL9pP7PrbGb4sKWhy6wqJyBK18UnR_2-QgND4kmM8wVEaPMehwzDOhO76TDr4EIaWP6_JngF76WP8ZieJHmOWX2M1OLsQWVwqD4vCJg1zD3HjTZzpS-FQT7VytG-LdVUfTlPIP0Ge9t1bUMEjj1ErrmOJ8wdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPY_UbJ3kkUA3eZ6PH21CwfQuorG5K3F_bRMLBx_8BEwk5njgdL7DvizDlzPrp3xt5bd5Sc7W1hYi-igLAXWTh550iurz4YvndsB0k00EyY8m0CYp_cjI34FqWJo3mKfLjep4GRS9GRL-FP9kBEtm_Og8DhX1k0a_yBkkeO6ebAjDs6f1628WbGl2XjJDIo3E9gcot_fOU7vuwne59n-i2ffHsA1jrknQIvJlorVsWx13uJ_wxZrWfjPQZD7BSLDa1NjQf0RriWYbcufdpHgYQjh-od5satU6DTD1wXhkQPjgOaxhe4ZgdMm5mUqDHP1nHrnG_XIUboVI2nEdqqvoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOB4QpevJ8UkJqYHNT67gTYhAR73frCF7NgHy1J4iEsoHxIB25i409UES3SDgz8GkTpCddfS7FrYwHOOqbe4VNqkzuM8mELO1u1sWLtdVK_nNbKCkwtMnfdGwucgm5jMaVmKCLHYTkJtT3xaeE5pRfM0OIdfOa5pUgpyQehmkoNe0h61Z60zTNOMjg_r42XO0rPw7Rn4L9FATAY6ocp5uPgq55k3zTcNynjVAqLvERw0_5oEb0zF6k_zXxrxU6fKrTwJ787Xvl3qR3cQVNuCL1EzZjwVJFUIZLanpm3zlHygHHCuDNYnJQ6mjAkFTA7-58S8Fixh2HiSd676HjNGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD7mwVCxv0Vk_7zNHxzF-DiznPIMx5LbTGP7PoDN7ukw5DR9Ue2XY5ZDbIBk4rMgOXG-aG3Av4V9Rh-uLj9ybyiNh--WMyzQ-k9U-pS2e3qDVxEDpYckewf0-gyXvw3Bvw6lpQIV1mOi5x3WpCVulPkuW_9-2PNdzXHgZf7eRwjJF5wZpYfbIx-oAVau7Tg81jDkyiB9NNuUf_tQkdZN06hd6apY2ocQgjKLjcjP2Gc6EpUZAbaWnco7W9mMJeVkZHn40WdLRkeJb_3SiCPapXP0gRhMkOZC-6AXZ4mMOZOe1lCEH1PpcHNzI-FW4uXcLmZ16NCCe1wI1Ce9j334hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5l29DYY0qMnBlWiK4Bg2lwTVxa0S5e7jnRNxWflSi_clkMxjhiH1ipmLr-ayl1O7paCn3vZi29w8-vmF574jeaq-5kB3cuLemFYf2XRcKyRLVGPcq1ik1nkiZjKUlhH6GDR7XAp6XlTHS-ums6wO-bKcUPNVCVEfK5BXY65Ur-RiiIeXrJo6UnBkEguEnyoIXfOOctF1cJ195hQAzt3zlIHlJZqlmL7h8CMCKS4c-HWbH7GbS2LiOWRZtRm9AXBvIp3dm_YsDXwrp9lgCrnxL4ZwvLJpG8UoNFDOxnhKFKL2edgOdnLzdZ6I4KW-FvNeJnEf0Zh2qZdsquTXClQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU2-y_0bFqOrf5gLHm1dPnEjfnL07uyMUJkmbIEJMJN-i1U1iz8gTHI1Qj7VB3YnNft999QvqJkI0-BzLNefqDe9EUOr3ZTCkCnU3RSBk3WgxmkGKqV70TLbDE59hQIAvo7vQFaAxGfuct0xdqfav7NdB_JsVR0kyV5c3fO8gz-nXZemjHjjbYgWuhoq6JJNcbNmBLMtZoUrhQw6OPlV-Kyh4b0QdtA3s9hu4g3Huo0zKlHDDxwMuuE7wgT6upzGP15U3rH6KIqo_IDuZgu-5CgB4v-Qd67pVjwyfB8Rc_GpBLwN7aMUplN21KEA6A4FEPpA6fbDa9btZK8bPuzhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuWLXjtuLWiaYcr1l2SKRyBZBk-tuWTh90RXsFJJWvXf3Nhg4lCo_99gfP4Ih6B1_LLp5deO1PSYKFe5uGufyVeo8gzJluN52o3_UBluMTtzGf6YVk31OThuFo0CsfVn1wXNMunPPLOOk91fHJPYjkKbFRCgu2C70VNGl0CRcVANQAHSzGWgfYCheodx6MhBr0qubpDLP1kNVCggok_kfqoo4qFhHq855LZXqapNjOEdYyCiz129LLkGyRFPb3lIzx2Q_KplvYqXFrqLZOv2SL1l-3H1Gi-9tBffiz72kpukfXsGtjLoEwK-FqjfeVbYQHzx26BKASJfhl9rK47sRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIxn76D2SiII6kkJd7MmT6mbdjOLWkIYRX-XAANFJ_lrY2ugNQYxaagHCKxBAc7kmQfDpE6b3pOD7mz8plfnIsWLLFLdlMizwbjgBZ1Lp_CVvWc39xl7JlP37OnTXYRFLyMwSlFrPR3ldCWA7eYElOZtlWBshWVJHqbd4SpVc9UgdCCP_toLOqpBAhaW0tZiFsTPunXJd9aB_z7JANx5e7FEgI15pV7qDEezFB7LKfuloPLOj1LGdfqVGv6yXKi6Wf7G_JRwdMHARK63Sr3Ot7_EO6RuDFiTTsTrvZS4SB6xIw-jYlvms7d7citE1lh_JMDFuupQid0sJ_QnZ00nGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM6EdA1RDxDzGZsS5SBMxcWXAL6Kk03iZE3TBxljpULpBC5cXjEEi_cL1nQPwi8UO7aD_ucypE6UnH--2kT7YMzMDHXGaKWDJTq2FYgNJ4ALARj9ZNGp84yaR6Fx7rDI8C8ycdjT7GnEeiKNPAUSrDw1IbZq6akNR00Uutd1neoYOwsmAEXyifDKEWvXnc6yYHu9rl38ITjhGMBCj3HSYbPPhCo1WtznKHHZtjzY-d2Gh4kUZR8JLvbftC-cGeoiuA9PubboMZ4zb9X69DXOlPZHPojcUF6-qnQZkIu5dG74XdVEblWxWWlKPQ78isYz1KoFO2EV1n6C45q3lSXx4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvrN0JhjXyhsTA_UZD7tAY1JPOWcCJSkyvFZvb1LHsnoxrYTT205T_yw2R_Olb01p3LfwRal-B1WD5PwlVTY9N6oC9I8kshnkZMsn4Uotz2aOSWwTSmLpJbPw5defkb9vAHGXmgPw7SeIPnEYQo7dfu2KD5hD26FqCqitPsReNz25RnRRvom2sMR8kBBr5jDBm6iWRL4XyG6CP1Rjdvdi9cKFl4LX8W3vP9bn0yXijM_exjVryIEUhCIwDl6DrnlI1HGpfF22xrzoFvlU9xfTghdBaS-GUmNE6xQJDnp21Ezdue3hUYNRDuL5LWf0x7tnOHEyaGEO6C91r5TgdZk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaUeg1XhLK3fCeTBohEHmo0hJqFFYEDfoIYjifG-pLuWxzAIIa0LQKUblwSc79LeprPNhiXS1mGnJ8OiHSOEDhzW7oXXLCKFnE04CTyL-LlymFmXOWSJV3n-wempSyavIbePgnOmsA5dXs-VXXtbphjTk9M1VuNJKIIi112e_fydhmsDLKfOA-WHYvdQEqOqexiHy_Sc537yH7xXpPOlYbz6LMzDoKOCyMh14aNR-ayIwEoAhx_6zRd_fczIqHBbey7Ygdm0kBkzv7LOtj1xjZ6gvgRQGjGMFfoN8Ksiy1gxj-O5Nt6_Z1POVCKWMg7tUi-KGqPEombf2RoOfaS5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=LhdvlDXu_fDjbh7KGOO9YkDi0zPpaLOqEMk522km0J391I0aeHNNU-K9AS0iCAZu4HFf9IhJjnUiCAui1bJyGcr-XgI2KI9eLVl9X4WlQTSUrtuEtmKHHm6NJxverMI2pD8d0lH6f3_qc5xbRlxY1nIruRo8oU7ri8btLaWhSijZ_YijB7BK3PdxrmAC59NTQWnBVaMWFAQqh72fGTmzMYZQnYmuEtMuW3wULzvWk2xZo56HaTn_XAIpnWL_N2AtQ-zu--7aW1HPW4SG6FlIJlEuvg3OcGuCSSfDbbebqF4tXj3GWywpSJ3h9xOgqBqqLBnX4o7IyPyn8ZoO6NXMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=LhdvlDXu_fDjbh7KGOO9YkDi0zPpaLOqEMk522km0J391I0aeHNNU-K9AS0iCAZu4HFf9IhJjnUiCAui1bJyGcr-XgI2KI9eLVl9X4WlQTSUrtuEtmKHHm6NJxverMI2pD8d0lH6f3_qc5xbRlxY1nIruRo8oU7ri8btLaWhSijZ_YijB7BK3PdxrmAC59NTQWnBVaMWFAQqh72fGTmzMYZQnYmuEtMuW3wULzvWk2xZo56HaTn_XAIpnWL_N2AtQ-zu--7aW1HPW4SG6FlIJlEuvg3OcGuCSSfDbbebqF4tXj3GWywpSJ3h9xOgqBqqLBnX4o7IyPyn8ZoO6NXMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv6z4_tV9ud5qy7V4icY34GLoqgD0kRfTJ9MnGVH0PGebw6OFMv2gl5lt021pi3wafDD0AuATN1Ljq3qIkI1831NzhZVe2Dz77w-AxvjXpZ3VKEyQz95wivcReZD7i7q31M5EFJTItn-0kmGWxX3tHdDfcbZ9FPtzI93tEXau_isS495AGX34BJBt4_hEkVtWQUAnS1jMrgCIBh8b6eRRQZBlk1lui1vBIAMEiiJ4XR7DDAFaHOOaY1ubjTkYIq7zvqVZgGBzuXTt30yfIcm3oYbQUG43EQSoyQRpYAQisyd_BBz22KVc1sZAI7M4aK7vlIDTWzKJbYOpARN7S56Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsmTO-CxvW_V49GjrAQgQotEdwmUgxBDqnVMOlOpi0YR5u5BDGFao58kPxky3VFxchO1AuJ2cLfCeQB8I21Da6DELh0zi2BpY9n3IbQw0tY6O1XCh0PMXJEKCUW-8vOyHAWLjlvwwbwg1XdoD3TxMo9MzTCUL6qen4cif3CUeBTSVO1jOdQvuiv3sk-1k5YCkwa7L0j0b7kkhjs8fwCbnNjCuHErs-azTRevyWciwkxUp646gnwZTGIE41BKr-JLPPIkqBYXCjWL5Up24ZPJn-zm3wYlNfN4akiHuXLhenG36YQYkh1IYW8THeHJKOii-FtB-Kkt5dzXG7x1bZ0UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euA0oUUD-8vUWcc_Tbgrx52wDP1IDrReQ4RNLxluaz11nA-t3n1uu_Sb88WEPVhvMiMUdm5oZkYoi9GJhpzTRYCdixBulSkBkP7fv5abwslgdwwg5mYGYSGjaJoWeT2E5VzHTjhzX-WKk_fwjq7fEs-Wb7xWTDtwh-xEMwEeUyyJeh3P451O8PY8TkygDNTu9lrsvgjAUF83DvDarI_56NVJ5WG-22GjgHPj0hgOYv7TC--xSiPwA6mVwmlqqwXsMXVdtnveWCGvontd3ucxBAgzeffDtY8k1p1-NDq7caRolteOLXVL8xJdwg-Kqdj3axFWqs672ecNLA9ZCxcQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLiGhKMq9A9FAil-zK9JErGW7duN3A8nVsla08080BdmaAU9ZTrjThgtgYH_tVcDE1QO1b8svH4veSQHFUAP_Z0YqvAMujTueZ57wedBAxCq2SMKLSWSeYRznq5k_36mGRaEfFDGv5WqzorCxOnHuCi5f55w2W8K4xAUVu-P_EoeacjBN0aGgpsN-2_5mbZTIFKNP91jHy6AI9k6ceIuIVcfmohD2v9JD_Tgh6Ya4z_pbqh47dODQ4IjbTqmPvz0su2hehz7vIeoxewLIw6v8jxxrNiz7PUiNeKLcQ61PfWOU9wnIp8ir3eGxYsGBYwIGpDR_3Hl5na-TZ_kNr2f1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSeiJe3-rcDVzHjgzuBNMcCRujDyCBl1LxJFOSobKOPknSabkERlQmQmhnhQm2jytvjSQs6w7lueQCATOL55gubebOAdF392Ilqi-5XFfjTqU_hHXjJORA892Haq3svlnN6AGvl_quH7Ed4gR8wS_gG46Y_C07ZEbyHD8bBI0Ql0SiW37R8a5J7QhG6CmQGGleJxDOadn9SPe4oMNdiF1ogRy8vMlx598HWqU9_vtoC0HpijK5h0vzdOAvaq2nHQJCt0Cjet-sETBpjf8XY7_fvLr-2awkm1i9_smQd8Wa69Rs70Cu5J69TexPJR2BaE8VVqp-uKiqDtQlxDBqfC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6ujh046zOUMzgiAPkvox8d5yqweR6kS0NOFgHkqcc4qChoGjjs8cVMJx2Bl1srDVa5sOyCVmaQYjKA1bNfJtyxgogUgC7t_WjKHHuNSaWQXRp3kTXVctN1yDjTwmzxXJzMKyLrEl4VJDkLbR4ixjwyIW861D9ykKA9FTlITva58Gm-4YfNU5gruWYQy0wGbHSl3tikJ8dqjA6AzfsasUtj0EDgZ84i7c6-OaddEqgaAxEPKDKVBKXc5xR_bblY1fvlwLLq-yfeU0L3IoGm_Io9GRrFieXvlIsyYHTVs05ZnrfP6Q8coTumX6HnT2kBuZ1ZhOobF6Tu01mO7WQTIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi1ty03O6Q8LHWzzsPl2zaoA2-phjUW23goGmY8uqSfTayuUq7jeUp7Zmo4qum8HUVNuI1Yj_bVoVCaRO4paJHBwUzFEi02qyhttnGkWCufi0fyd2VUBf-XP4Ag-AtKnzPVN81qiBmhQ8SA6xFnbAIUszjWq8KIXI0OggzFZZzXa-B9xODEu1x0I-ZJMtoVyIdE8FSyE1C9z7c9NPQRhhOGHZdXn40gCX0B5XzKhBg5ESgwNvWs51fp9O7FBIiSqqMf2pG80UoLtLMuOy5NLW-nSTGlFb0yfVClScjjWLEE2Wc-tfXf9sUOA-gWP7xIoKzEg5RKaPmko26awg18JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m56YZ2DI3Rxu88uAEZTXU_dTo9DTzsvTfiX2rp-iHKaRbYS-4_8YvL1xtxCQZqYlrOpAyUXPWE_XX7PdNp4ULOsyIzE6dEHeII260M78xUmd1jGm4eKy0gP3-Urv5jHaLv8CZuEt7GdrCTmcHMlj1Su4i45kQ7JG8APX09F7R60DDUGm-mZXvlOuZhp6ch6B1aWRfwuVkNuxI7uoPFbXLhrgJM-_9kfMGaNMh10EK4nqg3qhEFti1Xg-yiHC4x_fB_OGHwePLVAeENks8jhMc5Nn-W2BM3qma33qa4JEeVwBo7ig6NZ4Xru3moVZtEhN4bYnUwFME86QCaJRM9d0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGELdykSysehIzZ0GBBTsh1P4B_TYZ8TFoYglXlItee2TtlwbXJwAlqcPt6_X2ef8svkaI1B4OCiAGyy5gutwLeZglg_S2C55qm0upSOweLkfEiYZpz-2j3sIUfcP1bnxZ6ivtFqc4Ry7HZcm_M7R5YMKFoPKJaS0TkW_lFcpEIJnlsdPl6qZ2ZQI-5jMfn7DNgRd0Rs3nx-TF0CruL0d0rIFmdTCpyp0XkOJv8iT7e_yPmrn0jP47G4im8U0svTiLXfsuKK_b42dTG0c-rfeWoigZfjklEO2SzZI0fmqe3VNkp2xp6dy_b1rBKh7k7oCo71tuwmDOYg8lMKB3BWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1Kmu3CfAdGL2CBFy1scoapg1AKUsptV32ScQXwHLwOqAueUMy0agc3MHVgBfC0g9tX5wigfAPmTEpYtxNZp-bqe5gmd-oexu_rvhO0rvfTEcjfmRIGmFF3FSG_kPMCVvGZp42IWRmTXOqJVPEUBHoOd8sEKaralJClHNwkk9mpmI5mwxWnwjo-2Q77pJLbTRLyhO_ZVG98zBcEYp-JdRfAldhw0J4wsyWFtR3u1HIT2nkgHYihkNsZ4lvntjjzVxBwsX183f2k9raiO9eWg4OGrsWiC41KI1fUA-ypkCdYEBkDLmITtcnKMiEfBWG_TaQZUnpPljhLz_77t3osMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZVuCX4hmgTP0M6NV6iuCiDkgceLD1K_iiqfGLhMTA_DnHqU2N8H5_DChLq3JQRIahogW09ZVp-UVGPBi1_WMAL6i3opD2HGVNjWr_-vF8nCDAS3hN4QAAY4dOlh9OlPO3ZAZB4-CQ3FWn6mRS7l0IYvS9g2xYqy8AGwtUaOlyOqqakIy-nC_8Yt47DyPUy0Mn2btsnwp7YIob5b7lZzlkVvqp2R46Tuvoc71HyNIXlvHXV8AoeTxdHfZ6AAzIBLU-Hp8xaSzNMwf9oFvk86V1tjxXZYXVb1IN3F4JlGvVez5k9TZ6D7YM4U9NwJa4vWd2_0LmcjUmamGMT8UsZkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI0cay7RbZPKO0vDr2UsYf3O6yKRPv54-zB6JVfZ6rxlQ_M-ZMc9VdrqrQXMAslMCiX8jM71vSW1WmAPlfEXcDNGqP0XPCCtEqid95nY5qz05YZoZuVJBpw4bBT-1pobdRnV9NAMSTqhP6fvnMBn8eGSsy9VqHAgvfX3oMbSa1pZiH8k1P0DcjOCEo2qFomGj_-kpcW_DLd9f0cff78Zv3qmZM3C6__fI0LULy23Z-sQQvx7QOdI7Rbpi8xqQr-ig00ELr3CrS_x6HxBiXC3BCRDof18e2u30pkgcA-JVkO90EyK9vLHLnNvXXbYqseMDRFEhtIq5FB_-msA3-9WAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndRSRNhfR9V_s9HCmb34MxBfemcQybSyq5EVT5X62UDbyM6nNw7QZfKLHP7nYYaXFyh-c11NtG57BtFCHNtPSOSz9Xk3EG1FQWFH6Fw_EIzfDzdgq43-zQWe9UpRAdvUVgIJbIn2WuVCb6uuW2QGBOnGHbVGlVwaH944ocHqnkFBD-NGnxid9edLzUb4SFaaEuzIW6fwWlfkXuB4BvIByxlatMTnFc1qRPdW5hA8RZpwEI22y1dPC_OVHprj3jub2eES5q0G6xsWI2iux_3irkxsoldOl1WVu7kr_wo12wRzVYTVbU6JYIpKRpwNavybK2hXjUDh0dx8laUHqqv7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
