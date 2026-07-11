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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 20:57:56</div>
<hr>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZExvXYrKb95P0UkX6Lo-i-Slobbm4dLHiRxV36wzp6jw-MN22FGKo_6MkUdxtPA6JkjSB51FCRe4P664vq61_PglWacWSd6ux_JaAxeEUeEOovrVCbHaE9xN09LGjk520zMw1uZ-n8jYboPp06GGhMnoS57CmWKNpM6oaY0kxu-ybSzeBgTGwQVy1jhg3_nJVmt-VIxXzMkiGObSBR1eSrM-KwoOVsnKJP07Mh4gWInljJuEWeSv61gQ6Uvw1GuAt-_pIvNLZTPfHrGSzvPs1tOb5Ddrm6SCGrsqXxEoJi1FYn1xKVfrnZffQIcfwRpuFIh9h4aYvfOXqBa0pPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxKglsdb6Mbd_UNUzznSEFJba-hUcAlksaFDxgogYHRW_1hWPOy1r3HYgMaum3LCflVMbe4vfjg39cp94ZwqluWYR91_Ar6kfmcIyolrmF5yZ3dUZ2wGvF0mC4d3mWvi3hpnDmEWy8jeEfcQsOnODnZ2qbSuI4tZR7vExqgOKU2nPkWFFpNy3vGt-JAlvRpEsuxoErpbToDAnlQFk5JMp1aEtlnBn02czNBv464KW8-6nCua34BvFViKJK1DVEUx-agNm7v5DqJL08XHZ2VMdvqqwZJPJiiBHo8Dcav7JTrzBnLX8f1Ea2jfHjVd9fIXAsqbDxStn6cmTbsfhWXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U96hKYMfFSWOJnz_zWk2pW9JQM7vex1V5H4S_X3gGEB-KSggWff7HGNdszgoD1aI74xNsZOOwsbbYSyzAIawoxFtXlkzx3k_BBuFeYDwkNqZ6FLq2N68E81tWE6QWDzPUQ3m414UItrjHj8Nd1BMpx4Lb81DUQc7kGtDqmGtfgun4VoXbDlAE_sd1ATTdrsynrCtQZX2GsqHeeQnNubI6W8iZDrxCIx_KOwFfleY_Dj-k3JjFMVFsCuFoQGNd2yLt1hGfJTg1jcDhzjdAlGZO9VymQC3r1t8t3kuBk3DwjibnaMat2lg_zlOEb5nXr8DLQs33SNESIkhjK11ZEZnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTxGXxJ3hoILIB72CYQz0qHjgi_FtmHAEq97suaoFoMfCpwZWUQL6BexJVUmynmNes0tKtb2cSrrtTwmQQcAU_VaP3OetCS76XLRqKSLYIjNPWz2V6ah3vbNNqH7kBARXHB7wu9OTouk5Jj5-5j35DM4wTMF4ubGttGjIV83JKfjFlWEeFj7tqXwDbjMHRLqnMxWL5nlfW8JtuawU2DoXRRxyOGho1VIGV7wUWNWC631U99dgfMTJhSo1pIAJ0xR8yYI-JvsDAcIfbAbrceb6hIb_-guIwpBWVniTUlV8z8cmzAAdYGoLqhBNT-2tryXVie_4-Vw4JTTngkIko6MBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obV_3tY_7TVC9N4T_o5OXBP26OreUk4iCQOrDss-b-TNpMIrypE5QNJu-uwHOnR_UW56nuCktO2Qiet0FMfENvCHQgCfn7EGGxt2qeb02tXTSeJgIriEzBnUW04gXc4CS3GN6BfNy_oRlO5YtTMlzGEDOZth8MAY-cBCZ0deVWZCiRjvNB2ZfB8A2l20OKfb97RJhlEbapiqd7Y8aSz86Z8Ai_1ULkN2t0oPIeEmfeJB4x4CrbkYLhrL61JN96Qk7SRkXy9dtHW6QszQRHxo7Z3UuIMXwZKaCJFzlEhj3xzGX6OezfsVq4uFjHt93OfTQFkj9jI9irCaJ_-7clR-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRGj0O1ns7PG0MrADifk8JMG6f-uvpSELaPwBIa2P4cSXVL0J4pIj08MohQPparVhrp3CEWAG435JchC2UIiK_EKEjXY1zmpFq3ZMsxJDyRPEc16v7GUxn6G5KzmQ9b1Z__02-o5zeKiWZDGqnN1U4nmVr2gRc7fdb702jCyBHiB3vrpp855chzn6YLBpIYIhOkWfFluJKBUFPEZpIHzX7CBo8wdJ-IC4lhdNS8wrLBJ9Dk8zVgJc2oNP-kNQ244xcqL8LU-OVnTyOqLYc57qtq6LQ9UgpdsTjFXKaSLIj-AdAvudiG0tZv0hd96QO0DPVTihrQ5p5jtWSXogylyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA92UrkPVvO5oncbNgEdmpwN_E0t_0Ec_xy7NH4x5C2SuV225LWRuXS_5xiUL25GD-zjHYJQ1FXgCvcJE3TB2X90ZT2rieXVkiknl-KHDW0rOcbeJiCAOhGxARf70RcbCh9VcnpTqoRjndtUZNKqhVtoQJURFCbxbGMNbZ1kBdRHIp4k5pJVgrsB1gMJMWkO6dIT03_pNnVYAuAx6UHs5vYzy4VzRKA-0kmCRht2Dde67-45G9l_xXLmgS_rZSvMYMuQYRSMl9I0q-LV_6zmDR__sNOy21JQD_EgW88NQu5Xeg8H1P3hYZBowcQzWgScRUbe65rXyf4R9flzsoXWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiQ40lKidiwAgpCBV9qfkTIsc_t8uCWSV3RJMvg9jEN0U8uoiJ_1smTajhTJDt3G6kTvMA2mP-U0b5HEoqjuH6TvA7NFHxXPd6BHWabiaDx49k-5cbKemO0LYZ5NFikl6QydUblR601rAqJz0c1BPsgB-QJyrs1sGdSH74aQEBRq_JyG8fxAvrndn84ZD7Ey1hoG7ZXJbAzcFUC_So-afu-0c29j0CBkMkJlHSjN-WWYIOKmBP7qYy9IA1QAD-pYTSdAqJF227wpiSbFQNB9GUlJOY9GxB529_uS6B6GrPgA5p1JbwafypWKxCvUnLAfSClwe8ftHDzAsv3DXwLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7bSr3WeT0WfIBT7Yd-GxAQmo3yFhANXMbvcwybw5gBvjoHT7aB3Y3sD0-8II7pPn5VvtMWpl3zvoEFOg0zBaE7ot8GnNoQQtngcGJ4wlMmhs4i-RIVMd1c6THVlcH6ksbshhtM64wkGIR6jkRHysrWMKzLgzu-LKG4JqOu0AqlaK0ZKG6Uylq4FQ2tb4UxZOXDUoMZDhOs24PnglDat0YRPKAZBUD4KUu2F3KvpyPiE-yRTf-z05afYBlBoT1-2fHsMQo6yUHLXFZ3CxQCNZ8U4ajH-RaFQ1bDK5vjuTuLhUsvUaRP35ZsuSs9ZVaTPtj-15slZ60KT9qMNllekBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyk0LMIwkAxLtPakownpgSQAzoy-5t4zoL9fFf68ew_BJwfuhTQpOo0R89qKEJQcTp0nhhJuJ6UKxEfNPfEkuRsF8L-LW1CXcNa0YBHup0JLLBa0GxT0TlCJmmV2J1DtU3Pe2WziUU63KnCYnRPtHnq0Twno_QbciuO_7zajDykrhvjnFFq3PhhYkWNBW7iCQ1TemhEXCPBdmEp1y6Pj0_hvGFWT1vTSnPSQD4zbLgsLq2ppPkeD0NOq53rKjnpNx0IB1LJvC-9-4mm85RqqqGJ9dcZ-Z0Q7PZSXCXQ0PZ4Kn3gCGJsdTJiL6YfcJSzUx-7R5VeBwAS8L0nnvKs4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwChkSfxQzqiBvhaniubPFE4M5IjbvUmW87Uy_0ra7cgkxqDGjRek4mH4elgHRz5JZ_0MfOOgpAtAeF1icb0u2Vp6N9tS7xvo147ZowlK54YfCTdOMXk_XCyfuvaS_TH8Yl9jRrY3M-Gi2l24LN-eIIBlG8DdgWtkmiQ06zqE82AePGW16MR95a_Gd7nS3j36iSzJC839PnYNRLYGFCSIcUELBdGbQRKjAotKHz7O23QNO50NQx4HC1RE3KxadiGGJFojPNHS6J7jJ4K9l89FNawupg3FfTtJkgYrfOhRzrQzqKBGIolzKZyVEC5jt3vMujNY7TJXvBls632kXVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk3GnIEwrxW5c4Ctgg_MM6nvcagjPCBEUHH2TUNjeGpYUNpppBarelBSOISREOorfaqs08krUccyVKze1IzDr7fUWJrA7hVS76EP53fW-KuiOIo1SFz6xkqxafBQHpGGE856a3ofOGPBn9njXDJZxLfsle1_ikZECEkOuz9T_IARRe6nO2l7gwlyPCfZH89rYviBZJR9jH6HQqOgCeVtaJSpjlz0J2U5p1tmdxWXt5K7Udy65wESNmDQrGUpzNqJS5NP5TiDgDi9YKxHmpuTXbWknX4HWWFTDGcD-arSEOQo8ttf7AhpZMbCigW1RSQ_qP7IGiEC_MhUdZefLtiH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz4XYmiLMeJhXpeYvf2Q18l1doF1AczmabpR77AS5wDymGORoXhBorljv08TU_jQoV7XGGPP-RcEuquGwvVIGYNVXo1mhKbhhoiVHD3-JuanhZ6V4TiYo2jHVqkC1SHwAxT7xypksrSdL6Gq0DT98ykjcJ9YFkXI3E-_XqThp9e13H-VZM04_rURv4ZuviLXIccix1UTrSu_EoFjKYCVqHCuJ90HEQYh09LGaxzaaqfQ1TN7b7I5vrgXIWz1g2j7ZLUARepSK8CzO6zlJBvUz4Hxmsan7qJPfXKSxs3Y7057bt0uQDJr2qRd_mPMLLaSBi1yAZgFHCR31_V6LEn1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY5LvNclVQ35gJgzu-cvnHQWz6Cp2amGWmg7o73HS8PHdhGp-vvQe_5lR5LM-5IYOQNXpwNM4VNqvq6ZW3KEJ8gMUx23WtTCg6tOmZJavMUgoaDE3S9Qx-vpiw5gRH37X2jd3kG983IxUlgmvHcaYuaTkKJmd2wEsnZH4DO7YJK3We_okuSajbyOqsmbHkUJoPhN8zYSuJEogkr-Fp8FuoMNe6aL81mAyJJyFpt6vwtsc786T0u48CCvsYeYPgiRFpBnHSRoxp6KICdlyX9uFgZqMSvB7-hLv1M_8XROpZNF3j9mgZXCQns6fgAj6-Mf4PBa7Poj8L813vIeAYXVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f29VcSfIkNzXjSsbl8FKlqsxBeWDUvoUErXKoD_pmvpN0gPNAaTNxzSOftrVR8DkQIRpWtq9uI3k3kcOuhclprIYy4WnPl_4Q6xBXb8eeCH1WtEAAyBENFMlukO2An0Elh1etoBQLsnKvbRduUuMZFgso12_Z8aLHHzuj6QndrsO3jK0T4gwXFKwpnVK75he5hCnepLTnnHwZGf6ig8McQb3gDkNIopmp6wjttl4PjBWA7MugYrUDplh5LFMqYs6Xs5V-v2b_pMwzKaEtx654dbLyEI8qYoc2eQbyJJQCgPx60Agk3Licul418Z3Huya9vNQwXpqSwGIfsl-outSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9PkffCtbuCZC4-lffGKH9C14u25mzi_Z4tph4tDe0pOFPKDN4LmQMfpe2RdAJSg2FBt2FrAfhHqQJeI6lmkgfZO0XM48mPNEm5JJXxnYm-DmrSLj9p3t-b6oe2ULR_9EDS2wto8ratuPv3EpMXVtg3J1NiSUbhVP8xm0S53LfT0aAFIvh2SvmDo-TwTsLcanaG5zlACeSQW-Fzia-d7OzoSIyouZVtp1edWb-jlOkWuPrw-pQbmC2x0MGKAQhuXTO6V8to_CoT9EaNlPbP8cf67B_43zm4_lZsp_w_U4TGrEyE5LfZ-uFjQJUxqyUqd8VuCjB-fSchbJL2Km52DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-UiCZQ7V-fCeBkpPHdxAAvxeFEefk4E6fOh3n_TadMpsJI3eAGmfbfl7PmkgzhVPyc46oavDIQHXiV1SsxPwEV1J-FLB3Uy-KW7K8Gsx1MjOAe42XQ32moBdDAYHibuZSYCuZ-mup4lAwhe4QhGZQ9U0aQ0CEYnEOPn90K7aUC1Jr3w5PQs5BzxZ88_jYU6RKNNkaJYMeZOmk-gJ8D9A2l3Xpzi_Gu4Rg3eUUwbxqiGwwvp9OzC5yMbyorp-OnmQUt-O1u3X2CESNjQ-IeGZOBkCiSsz32453mgASTydZkwlHjlg3ykUX0wGU69By4Gp-Wloh9r25lJZsmtYlWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjKw6s-uTvVe2E-rPu6k6m0_-ztja5rzWFYlFGmHfq3gnfsMnjixgsng9ihqCqmPDiyOHGDJYCjGtYp1WDTPd2OGox8n6flepyYGyz9tKy5iASTY_KwCPHzyBiNBurcrL2iXyd_qWcoUi1rGlFVbMGmoDrG_lDxTvUxGqvVeQ6QvSFGERqdeN8cac0PoKwFWKdkEZ8pWqgu6i4MJxfeL5KHL6iNw_BHJQt4i0Fn_s6cpg6Lwd3esPMKmfHutRR7bUbKDVMiEHTDxIEoi1JWkM40CSmiDTUBsJjV5i11AfJqOlkXNrOG7SjYGtPkOluFNN8wxKakhsw4X4mXAyangjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r36ArEaf3Zpc146X1fLUU4B3KHNusHJMhKQ1XRbA1nKtuotBrZ_fdSrThuvypQt3ooY8HRPaB_5ZK921FgCmgImRnl1dUKJ2luKGdDOVSLJzzDLTOIn1WejFIS4k1zS4l9mZyHHMPb30r1KHLEeU_4cSzfPUL17eEBsRSNxgbAtX8zrwz5eSrYrSLy9nMxZTzbiQ33jER1Oh3V8gQttJr1UAXbWQ3Nt2d1u8fnkYHn_T7GFMcL0V3MMKxgWZZQcugz_8hfXd59HBw8wKzIT4tjHgy9YZk0uhVGpCF7tnAGRFCYM1Kv5YyHwvm3Cz2M_1li7DbBtOWfOuInDVO2BGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7Dxxhyz05k8N4zA4SkQdQneKJChbUHumD1G6BOmFXRK2JNVhOEq3IkmKqaMNHCPtrZQ5agdfMFdpJN0MBghOu-mnzsJJ2nOcjSW9vqNnZUtgrlFWklG-FAPR1j7XAWirIP6xNoVhUN3vkirngv0cb7w5pN_5CEpeKZ4ftxXbJ5VHmPoZp6JelQXmM0BDYLQ43rdsKx8TwISZ__gsnJWgMtlKkhA-5tguAOS2bpW4lTNwAqqKy56GRhO_kEm-hn45V9_7nb5r5a_U4FIP7mtG3W1VoOP0rQlV0PTs4CGsLJSu1DQQVJRn-WJuDxpJLLveb1sQ33x-8dTwlnZvOfqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGgLmFVYaKR8l9xSjnkyFNarXnXsTmZTzQY8Vz6276LMEVWChtRqjKoGjwIAafEoFnfmvVkmKx_l6KOL_rPpeoNsIzL1wvNM68hOzNAkk1Cck6wlyOp-KPlEazkW-AD5fGU9QvfnKEv2ow_egEw9MaQmiuw-rSNOhboSDiorFzLVERuWygMM9QAz7pG-buKbt8wX4EdjCSaFo1JdpPlKLk45gywEnZEQze1kmy4j8sTzzn8liY49U-FP8qrg9cx50Gy1PSQgygJqAOZ4JlhckPHQzkrHK0iUEPYR9G8cQFWdc_GsiTSx_hHLw5fNwfP8xps_kvU3bQFPesIiI-J0og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEGG2VQs7mKAiluUnoFhNa5-NLscgLHLoL6AuOKsz7kBVVycV26Vub2aN85Td0RYM9GqPNFjcP2QeDBb0Cgzn9BkYGMgAMGojWpqJOj6JBRRKTWty5Fizhmq6QgTXTGynf7LmtfAPjygVjpY5EyTBpe5PFceXXCSZzbtz4SvFBs19j9beqcxiKm1K2Gmzga7rLlIcsMSuf3PstpUPBlfgowAMg5C7PzuPadelhEZBBz_vKzKpPTCeJVKQzp0WqWcsaWcPnK4H-URnmHpzSg1Ivd5nMR0tembkT4_HBKKnXQec7HaY5xyy2iCSIqJJL6Na3Lc02U5SeJ5e14k6muNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJe5WjnWK2BClSb6LCaZFtXzgr0x6fRaaB-2LZkU_xhwqExkkZbU6E5oEtqph4U0kbb7NkOXV5-HtDAP8Op7TKPDz7jqWMbmhnvcAxYC1vggvC7sdNBvDmCQCw3GCXNSfMDvul4HW96jkFFeaSCnNJ3xpYbcCcAGhjFj4jyAv3ktvpJW48z8oAtbWihVdzdOHkKf40AOI-26NkzqfZx0Dj6-8gdSTGQHJJTukQgfV-xyupCKybAm6Dm9a8njfzcj3IM6kZ6mpI2xpBKzH6eJVu50SP7Ct8yQigU70kSHV9YZu11VVAUEyob7nobWeVYFCciBzNmfgRYQvRunirM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf__u0qFYpuD_1-6Ohm_m9fujtjTc02TtbHq3RglO1sqyULvDgv0XIwzgZWviBKcsaQ5oa5ze6bKxJ_8J4JaMzCWHNanXblPTvkv60y2anLUkjXizwGLl_dcawKGWcZUcuAgSPAfdcMWRBra3UvgPDxKETWfa4J5wY5vQHjQAq7rkYrgvHAR9mkAnraaghKXoD_0IwG33OdEPHR-H_IX_xXGlMhQw-qkxje0JyfdelhgxTNjWY7X0zBZgqg4BbxMcXSxn5wdYKJrbREv2Be5c1QiS9HOPN9YCy47tPuyBlLUQv9r9XBj9zxuzpDU1Gf_U9e_X-GdzeK-znRxNDvp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1qFi5NPtQNL8jN0ao0sqmK7yugCS0ZaBZZAGTgAZKbW6hppXJtvLfEkEEERPdku2GYdO3-k1mVx1PXHR63VzUco1hAwVksuIW_PyNbt5sGVXUUOg_NnlLMhkrxK6QOBC4KdZImznHvpCovOahdNBxwbcd-P8-9ISItDPsOZitcsVQzweDMeByu6GZRlQ1GyFl3Xav2uhpmSfuOoE519ZfVg87ALKUWQyyFQE7hni98UhKLTJmYrMS_n97bJZe4Ltce0uEXx_J6me5ZErNdw09NH0u_46AOWVkqCGUcXDXNzNYzj6gqpKY5iBoPJBseXmxjATAiOiR9y3EUbfEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m83TIinvhdBIIYLJT7-BCiqG3J-s-yVJtiY8-ODzaWnXUVYeAGlyRfv7Nc13FzN-KIdcB0KeJr4s7plDa74bozmuxtCiUJamcFmvJV4N1L8IlZXs-wEqL3DmFcqjhMj5zbkQa9r01FW_tClDYzurb3D_fYINcAOJwqp6BZWEYnyAt_-KbBFwI9kEohnYSbgh5XLKIcIcfjXSH3bTV3iFgCAB-dRMs0MlLu1jTSi_DQW0qcQz-sf2lC8eBS4wvTMHf8o9WeOS5Xsq46N7aCrLIGdgOy8llGZLIR2BS1KqwzCarq0D610-YRHo8FPBbdm0oddhlW2C12fxdO_t4sWlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0_fkMAgU3UrH-XNC1WeGAUyA4jvDGE3SgvLTjfmJywN4qLWrYEynhjUG6MrSCyMO5yS13_o8XyAcPfkLU2nx5ohyQOx_ZWKsl3_NhQ-vNQ04qy09f1FNr1CGHEBiB8HH_N-TploOnrNYjn2mJIIu9NlYWWY2P3xm4MmnANVmfjnoOkiuC0r2taoNljwS93HzEWN3RcLsFBEHHhMNRNEmmV9sBFTCjvPoOhwXxtn_TXXFiFcG2eYs5RdwVmbi06b7ZDb5bhUIylsdojbVviqNhVcRpV_7l2CtWpWCJaXFeCd44S2sT69adDaXcjoZ2LMffZdTPiV8fFo1C3-grX2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDSW3-7qmipyMzIG_lx0YpeQpKg7OfJ0iZ7uAy0UfaD-GcjBFZarEbiIymFFrdXF4glene0nDuVpr2mVk60qyiGY_eNKwv9aSnoR7yr68E-ZmyA3pJZ5PZgVcSo6SANSJdPAtDaZt54IbZDrdjBLo-WDekrRioNPqe9KBoG2Ndo3cHzcDPCquGPa0xgC8obm5n9ePdgmiSKj4BV-DIHtl5AzykrEq0MCtRv7WgTarrhVQ6oGmvyh1pGCFRL8gCsILQwXctvRNTKr31UwS8P6j45yCz3LI0PMUQ2xdxhqX7ft8SG5zlyXyMBsFfb7i7vwURU83kvEDNJqrdWcnZdfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu7Wz2898xkIBpegUNhuocBpFt2YH_cEVU7GMKLTHW28ztiHMW0lFL0lnSZL0FBdsCj2_mNGNWcbzR0vjRm0ymYjWKeDv1YtJx40ga9Nrn8r_UDW0jesfuwDTfhBXmfZaY-4u3Sn6c11BqzQjHA78tG_txaF2CHlW9J-knnhb2lL_-j-42KWAC7Ol1oGELRE7rKdoIS_AZcfoQ_zXcf4KRtZrUG1CZy8_0xnicVOixm_lYVQUOCEONhwRkiAUNxofbuzTCfdGPxQqwV5QptdYPurhD7FMbVyVh_c5mo7m94mgSyJNPU0K9xyJAAaQ01Xit053M4zRsMVVF5gH0jo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu6XFIQ1oKkXASsjAPbIi5hCAWfABZ34L9JISH-hnYGWWFoQrZ3x4jz2XgPc7yNLfjZ7akraVVvwcxXtdq4_m3naHKEE0rsogln_PIADmHsXlJ0mAksyYHqpZmmats1InFFRkSE2z1E-O_5OJUIcpXC-ydk1t8snEySvSci0RciBiK6zc5zM0DU7IUEJJ0vCO7lx1akwSh8VZdgh_GqR95M1vJTBluS1arYB5vkQB7HlKqpfcebdITyHlLDeU-uZUe_B-Dfd4VMZPaaMDwHbJgkZTkKHBKT6a6BfeBuNxq7VkDrtcRNln1bmtNFlfjRkkYUFakSqag3FBKWyE3D_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdL2097y-Q1lOEhQya_kygl3FwmVrwbnNoHs4yZa07-OHesMqx48uNu_bWwEMANpWdVNNry--UUZ-mP4Pal3nAjDqscM8yDMxX3OFOgxs0LIpmMkg1JqrN4JJA1A0PTHQ4dPviW3pyCIQS4k4AsHPwRpwafTnG6Mwl58y8y6XNwHFeC2t2Un-OyXWo94r-OxR-vwYANeO121VwGElWfnfIYqm6QVcTGskWBhz5t36YyFzIvBqXOzsMD3eXlSN4UVLtxYrsnLoxdvmvvkNm4GSo9yy773PUHp87yCNr6rnQ0Rw08ppo2hNFwDq5CO8XCi-Y8NloKc8rOL7yOW2Hkczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8oZwv9Tkts9WkNEHzqQ6CpAE8gvnsflN2pKCYtpLjW-63pyfzU5EmBW6b5GbTKnqCtUAO9XM29Us0pshfsBlsm2fSen_JKDJg5MRepJpgozIXA1VgudNlKsSBOy2jPazC4HkzPsj6PPhUohd6IRjc1DWYpG3t7hpggLOXxsDzBJTjtc1j7sAhdQlzqEEDAVuQ9-K7LjAYd90crKL_D4xQrFF2969GnYMHo5nCvxwaGCBjL73hwPEZlENdIxbWbmrHwU2mBIStTJUkKov68sNevwG8ZjncOm9kAc6JPP8hjPG6N9p5KFLWn3u4Ytls2xP1Es87zXgRkvm9nhzHp8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHGcg19nVXZi9-PdGwWnfVE74E_u_slWoLrJN-Y0TWJIC2f46xjAn_zKaqmZBDBLB1EhkvOyEThuYr3kWZuBeK_XArKoskA3SexZr3sGb9Bnp801Cs0fclSInCNDkP5jIiAinK2lHl7SoB_Mc1_Vq5HMw-M2eDcbuBzRODVJa1K2usXWmg9x1ZRu7eLh17IpQSA7PnT9Rnj26OAvzXDK4qUvIJafRF920dRE_vpKWL06a82yn6AvcDfBrj7xvu98bCsn3Qn7q8eLEbdPbsl1sLB2RrGYN73sI4TiXp_u3A751l1noR2MGKgJWk6lTu_R-ud8OJJL3Ftf4O717jurfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJFsXlzqt_8u-YxUUAIQ1tf4YqRyCNbAbYckNLAn9YNL61MWu2I7Pp2xZKLSVpTCjhqmnc-jY7TFniCXJ4cOY24Bg5K3muHtdaxoDUPPHY8U12_G3zCwK2Noy9gNYan1QzyG_LUmF3HQZTKqU8QOTIK39CkUrEOcl-ZdeHJxRpE-PaP2cKSrZonkhQtVsWv20X5TqQy_X3A31GN8Ktj7MlQ3wKWCjsDlC0bTdqXMXb0D1YlhIpFFnucAGVsUkzyUPvZvmmKBMLOlkGySbpcP79EHHeOxjhHee8wJ2rRIUIVEVenRX6YvG7W1MWf6RFEyu_EIwtmYsrEJE618ZsNRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQWarg_O8X5JmVD0XbbTPZ-8ZLfhvxQQJQiqspc6QH5R8MqvkdZZ9D2AsBNpzI-64pFrgag14qP9k1yecFzJ954vxvXdPuUzS3vn3xu63jSBSBDUrs2eu0j3aF7ndKA4564FT4nNilZZIURrH7TPb9ir4mm6UXemcV_21T-XTwiSa-vDBR0LPN30B4_B7aQR9U0fiZpRTt9KIOgFCd6Lb9rnw55j4bOLl73Kdt1LgVC6qjjZe_71fvNElSTb5PlxRE7-h3oTeDZGJb_4wI44Hv-XGyQTCkeKivJPB9WaeAli_cs3crWepbL57A88Z5wOcLsIwYxnQQK8yfcac32LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WluyItEvSk3K_isSejg-IEgPZ4kHEmYktlcm3z0nWYkEph1Kt6_ewaARO33S8cjr_EhZyGBLqPGd5z6KyAF2C4pZ_fZubxyW1QjsQm63jk7LsboxvQrtGZLV8Z3hj1LGwFBqvdIZvhSx2gIXTQ7C--kYpA2t-uqi-K6Vk37BiK1gPHUlh0I5YMo99cNXYf6y6rwJiuuEfYDt_QgMAbFfq5lsV2dSvbSGdEcxLwG3LjxJvP9SjXcgf8rq-cNIfDG8orxLXmKVkXCTagc2KwsvCcZTDyAmJSgYIRlgzzyUd84Y3jXFA186CrIZMbrJI1gGn2sIelFPwfGd2c_HRwjasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=Hl8TkE6f3rFtwLpGyziv9C2VYCkqReaRd8b4u0nqH-7Q7IhYCsUJMwX2jFVlMU-VWQ-gDxEzKUd-sGzxqvyOUkBgz5tXFV0ch6bLenw8KjkC_0pkydbr6QdWWnTAPuDrnB0OT7vXkvki03QQ_wxQu-btDzFOFU0nWhKPVyUpi0KvDidDXF21v7whigkqKMz1RmMJ0aFMi2a40q_hCqF2-w7ZpEzqODfEi0C2qVNDg7GQUPxbP8Km6YfDuTxyOaGIfrBfpHBvWFTwaAuE2epWddbSVh5puKXczEIErtXGAbzPLPvc0T4yiv-OxAJRdxiq8Ujj5BR0eWRdMX1NvuJtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=Hl8TkE6f3rFtwLpGyziv9C2VYCkqReaRd8b4u0nqH-7Q7IhYCsUJMwX2jFVlMU-VWQ-gDxEzKUd-sGzxqvyOUkBgz5tXFV0ch6bLenw8KjkC_0pkydbr6QdWWnTAPuDrnB0OT7vXkvki03QQ_wxQu-btDzFOFU0nWhKPVyUpi0KvDidDXF21v7whigkqKMz1RmMJ0aFMi2a40q_hCqF2-w7ZpEzqODfEi0C2qVNDg7GQUPxbP8Km6YfDuTxyOaGIfrBfpHBvWFTwaAuE2epWddbSVh5puKXczEIErtXGAbzPLPvc0T4yiv-OxAJRdxiq8Ujj5BR0eWRdMX1NvuJtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJLnxZGOkS4OUM5a5WWYfcAHc6TEYpC1cVcmk-i6o5L7l0gEYPmsawZ9c6xbkbDw8-woJv5jV36dfBXSlpDUyjIPFmIXItYyv3Np-OfWn5hFkAWUZKPOIXBg5_p5Wa_d2diH2sDRbSxkto_uKM94ZFSWJ4I_ZrglLs_f_jaaLfy2Reu-rQgUAlWzKT3a1cOugz5eCRCuroNxY6Hz_HNgXF9X8OZsuy8Sq-DwjbdFjUPJddWv8fT7da3k9Nh5b9U4sSwGmUjJirm_djM33XyYgU4-yiw3h-dBu-5RN4M5E6ekXiOhcx2dxgTcrv5hg0G1v2inOeYG-HXN1hE5HwUU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqk4lKIG-g2dmHFaqSNV6OMC7udbRRxlZHp4nkvboxppeXdz6WiC_8VdPNYilB08OsAaqnFpJI-8FoBBGJ834tGkLTlIKI6KCeU-D0ZRhdUmJ_fXrP9jzxq9FD4k9v2m1IWtoBnMEeFnFO3DI4UdOMmWwqGGBjjnH3s8F05KQZNEd_8bVRh2YW1ae5J3FN_40Snh1aivKjXxiBnLThwJVbExAfD_jMSuMdpXHJhbp5QA96pIyK4u_UT8yKYAJS-Sae3UvOtc6h4nr4AxXaVA2Dlf6Dm9E7FjrwDFtiO6EE-vfHUTsE3zjLhWqSNbxcpOeNEOKOn7v3kD9izC79CobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTl7sswmE-CCfbwJC60Z4aX8nUT6gzrf09gsFsV7pjTfBA6h3zQl2VSBdy1BfYJ5ESmNYlYsbOii30xcuSi3RMKPjC7Q4q-4W34aebQ5WvVIQGqsT8_4JOa3yH8A2tPm1CodT8-vh5OBwqgds3pAXZdMoVFyDS089y-2LccO1Y3B_G09XGKKREHPI4hyJdHNsKiXRLWEhPvZCavkhk24Qw6ZColLs0pqm-oirHteXktbvEPv-7YUH5gsfXVwBomR81K3hAq0789JETyyH37IKRt1DM4SoHYlERcNd3loz-ZZ54kKJgoA0ERtNcPBEYmpSty8maja5HCGBKE7wcPb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_6je_6t1X8QiUU2C8xIgetgpwbEFiECdNhd4yW4mGiUIxfUgD6Gt7Z3ASbHyBemxUIRCr0CNTvt_KnEo8QBpbDTjuiJC-9WvIfy3y9iL_XbpPwWQpjYsH_JHAHME5MrgbJZinejgF1xgvMAwz74BRVEWs5-ZVnQKx34mfQr11xIYqc-XAvxVRWCZ2Vq5sRJy38dwPJ9hqfsR1w_yaAi5IPo2StbAoFnyv3h6W5_InWr-z4AtjmWtPFSPA7eMk1CtpBih9lJqYO3c_u95wdQY0SZHx6BOFjGdwOXv-1_ht2W3awRLKiontC3a1tyo5436U6j2oukPcoUU5IxokndtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRL9lbdaSI1cEFbNjCsPxp642PfutWPUc-R8el1cOtkVMQkFo52_QvW1YOrW788XrUaV-KLGy9iBkcqq8KSW-2XsoBrdzLXXzunWLpzto4p7qJ7AXwuRiOJp9D3WhbFL1MY1G0U6mnZoU7CLC9LUhNxaw7_mQeeQlVUWmtGJ496IIeCooC8nheOSe1ymfgKVP7ZGznfnfvGs8Xk-yvfUKej7frt0qRZIcpXY2Rkyw-iN1AdWyUhc_7_W4xF2h6gg94FePByPhOsHiLq6ny0jBZh65SJEzo86wAkxccdusNveonQSBbkbH9-xCd6FGyI_zUw8CU-ih0QAsE6ELJdYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AApilATnLRxxB4UdomS7RZa4pgMOi0bqceBg8vVkVHtabsx-wfp1lz573PTCfdJUPoODkUANLlAFCf0ApU9FhmY7Bo298jbwchdwHyvYEjVoVAPNqRCy_fxXNl7nDOJSFzzDuEF8mMmbjKUGfrVIwLkhtDCI-zIrpYIjhmRQzwOjzvdpCu5He6CC0dO4IJLUStyoVMWCrndgxirGiCoO2AP-EEfxV2UswecY8EDqOGNhtgDFibcafDNz84tqXtiIgotthes3Agtdkagn9d8eC89eHNiT9VyAA3SmgNyX-Ec9tdkMi8O6p8uGZVDl--pUO7i8euvLUrjdrbt2tOrpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL4S0_FejAlcnBX4lG3FLwlZyYyCDvVNemBju8I1hFUwALYrc148zOpmlzSHAMQ1cIHt6HvO25YSDQClXvG3_LxWZNuunY3E5Qmh79aPEuimzVGSuQMfPJlblWOS6kF9QPwt0xb6ZfrAiVqYXeyMDfIAYctiL8KUZgyqMBK_1UyKtDb6fat2INqCQjBEyrM2uYi2ksY5gk5iiYelRtbVNtFd1PiUivvZlcCqDq5w5gMG_KjBEoE4QK5bumJXnGMbtuBRbM79XREu_oQDoZ0O039RhDYR48xEL-rBU6uGICJCOmOrtNFhROHmX6tKMnvW0Zf3kzZbss5XDlUGuEMvGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtg3Kil6sQhDDbMsepauqQaQCzNtO2cczSsC6iyS-wYvpyFe3Fm63wEgH5j8mg-icjVcey0N_EKinUxdHlnHyKNITfF06Cd4MZB0RxzfK86e87TWfTfokbINu6MFQhD-uOgMJsGj-mTFRE7cCWJO348jsTkrEzSyTzc52hPYZdsifLOKx27nRIkVBJv1RkDSGVP0mDHQDiO6__hMHbmJpovhGaXhfZW2katHUmf4_o_4gOSQ-B47eA2cpgOsyJlob6LR2qlrCLgimD6T6yOfogvoT3PLgZtUFYen9_N5EqkutejX6S0XR6QpF_H4twF72xV2l24Md3ZzJNa9FBFVog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKx7cqEOQtczTeqn43dSlrgWUuNyGXBzjFKEZFdzHUyA2UMzHz9T-1Q8oVj5PUtDu8lLvBmF--2t7SHXRroDei1lUZiofajMH-_CCZ8qcvlY-NLeoaEKz1_jKhMNq0SPAUB9wigPgTKdy2DghXJjkgWzKj9BSzCxfq59TqHmGlWtbrKl3z-oH_guP_vAYRJwaL5WrNK5yVeo-mwwqONrr5u7hBGpSIGlillCJxx5R0ApTglJMhuw2R2Se1qDNr59WL0shoxVZP7PVN7HhCFR8B9aM_s4PndkdDJzwV8N69eHAcS68cZDb4vM4SdOjaPX8yrWLt4dBfwpcq65T-h7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTk4D_0Z81XMHpmGa7FgFiNAn1CA1mhNwuQUcPOB1trHJV3F4jHoRsWAMBf8oU-Hu9i5rWJy18WOsDYi60CWdjnHNzEvyXUMWDWSn9fQsb44eV6FDmbIlO3e5v5yRqxZjxHyPmCM_WvDyd4H3h-ljZ6_KbfXCmqDf-9Ix1V3DOof4MSJWiE30MjV8IUTIahiP7932w3qU_HRIlqGFFs5_oBrDLdfKzbhdWklqMDJbNGWoce3L20e1zq3LkK12aXong4aTBGtfKP5wG_UL05bJDW9CvTW0_U28I7xjzSGWi_YL-AGrZrmjZgzyzjZNRPD4B2kD_tk2QP_O4_D8ijesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjYxpk1ml4XlgjHy-7eU4vneTBL9XHWpsq633avsIoPC-VR7SEH4v_L1WIkCXJL5zXaQTrheHAbgASUid4_DIz6bf6uKK0MSW5XPaJm5hqbx7ePMoS4TicH0oWddWAoOUen32zrkYuowlP-c_YTaCO6S0wv7Eknjhv6P2SAFLg3--BiYrlyitJKPpEPgsauy3JNnoQXhrsHP4Ai8S0xs5AH7veI5BcsKxFP2YScmDEtGJsivbfFxMaSjs9yrPR3yHxunvZUVTqZz0CcMYsXRPtTtYvBNFyTnh21qkRT65y8qjN5CGFbaxHsvJxUS4eBLBpKWmokXGs-Y7Aiw-KvUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDUOh9sPsC5UtWUX4hWXaZw7MndQw5CKA0sETSxDvR9rjqacq6TP7KM6-5Bd1sMvf8tvwvvbXRphCjbrsNMg90wc-_WG5neZjJKq0vi1WC7stAToPWZDcwwiyFhHsnJZZ7UTSkk0pUVP4enymm9cseQD7rM7fPONYfjUzWarzbKvZH2iJpNUtJfgDHQR-UsYLI9nUGppl6hGfiHUNEdc0wfUU6fv32aDMlcByKdL3wryMPrU4YKWshWBE_idelp55pqcVkDVQSrW9odvcoKpVr2WUfH5FHthQhLo0LeI3v8QwcRO_4ns6kXESFg_7iVO7c0b0G5gioOIYSM420AGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1jsZ9R2NHrtXv19pZL65t3gTzKmx9wMQO130RPhmGbOSvcZp4flmTataKnwby-yuTzR1MzjTiLsjsR2ovdx3fKNbwvMMRkUlX7k0baw34dxPaBH_MxaEQbmPxGD5JOGwFxxbQ9MLR1vSMyedbBV5zYLis9-Fn-ISwKBJ9LuIgqX9wudEge9n7OXtru_z3T_HvDm9wsi0toGvinfDD2aa4zfgOZSn6xlhBljf2saoXLzzWqpqOe6svdJCPRRkHYqO1Xal0xfNFP9aQP1df-t6fTfTaMGQ-JMDFhfCZoUL5sea_9lq98FjIuwWsKoTz1vBXbCb-3o2B9fOLYM7CtF0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5QHftSVHmSV8889d1luk82QN4YFGKDCh0f2ORqfNTsdmTD9JyRnuHx1V0TpZxbJ0akrSEDDUnOQOVR3TFtXsBXt-v7tvc5vXRkDYe-rTVCUwzjpD17xWeK_AgUbTJqFEQU5YshS0tAcOTIMLDA7Xuvkx9dBTSAD3jsic65Muh3PgJ__tFAjk_FIJxcHh0P-oOW6w-o1-IsRdxIRZJQCoWCKSrjwPEylufeMccYPatipAbeZpMWrkZlqkX53u-p4syt5YBa7VRZ8ntN4clLNvstc7K3CQKFo1PCFyRnDCAYBnADniwIFl4_vq7Jp3IO4aeMc7oXhZ0FgUL8cgQUcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIcbfTSZL1APCRCaRKzLU4q8Y5kw96jpA-FqBEQjLSgDttHbG4i3Wnmp-_LWZW5CQ0vbv6qZ1R3NYl2Say5_isptHKAen_qvbY6mpCiTHppU0aZlFohbr8sofrFPafiKJvyijZhf7buxTM7vifuMcX1WXQYMSgWVEhp50iBaQTnFgqRphAemBW14gVYsTdUEohbZ1v4AU13SU8KLZUWSEK7peHklPUHYMIa5CeG2UpRn7vzgDkuhXwO9Tmp4kmuKMZOGn7EMfYdm_TAzTBOKFNX91DBlwPltG12vLLTJ_-PE5_tBF3LY6b-TUl5rhZmdvQLEdBeiYBXXn6Wst_6NeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaWLruqvEEIrxsSWhbHR7vYHgOZkDYT-uqjOcbLrCkLRf07tFmshAcpmFXIfMrXS5QTxyFqo1FNWbC-tY_JWmnDhm30OH02806GZOy82SeHQrIWHZuq6HS7RGWNayy_3_4atAsQwmEYY8hDQc6PpHKIlp-B6PsRW33pZrqGVnyq-sN2SGNeeJhmOz3DOQVxtd6QNm5GSNQMRxU1yYfjBxltlzhg7jbgusyvfcS4a8WA9m9lzOFVhDuVyJCbMlvb_itAvMXtRUYLU-qZi5BB4-L4MGy4ZJ23XKKJ_t-vrw5WetTH-0CwHfwmVK4v5PTyqrKI65nJ5pBOWa6Pa6WYmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhKG_GE_AgyOwCdFILYZ1sd0mZuei7qnIM8ymz29WUblXuzL4_J3kEqbx6OdOcRu3bsFh1Ybb0oZE-CLcLFCDPMNuKDPnvxM_yBw_vpXWoBxvLq3QqNTabFnLg2PErb5WsGechX_OUP-AH_fHpUpvafgh5zDV8Wpu9aYusxfnPC4sV-rWOtS3LbimAmOMo1odEiDQWWs6ocZMsb2eSjSFZ3vfk3uNBF0KJ5vXecp5LbiJvleYSZqFo4Rj2jqURKqB1tbQV2TC0FmWm-EfeZn1-460OqazQ919WkUjewgZHD09EvzxRAlYVStEZ3bYZw2xr9l3qGZcKB3OOwxbqq1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QueSrIUPRoOwHWfiQV9OYz7vTxVdTY7xDXSknhqInn8TZQhvqb2Fc1pVTT0XJYtTmEW44BWU3B8Xn-oOnD9LXAfVBIXBS_rw1bQykULCmjsHqlkKZB1JR8WEmDBIrfiWlaoYIOvUTLznPF6ibmTTyhB_ODLZJ-zIYtXRKSvXlKLnwpdm3tX5nIyiPqcg4lfN04k8aceXuamdFyFfvMexMCp2NaLhTf7AYDlnUUJP7sTjkDVlJjbiPJgyNZB1OnP2R9HXzSmehFqCZ7CT8a3akxDCeWJoKpaCNhpW-iquG-lVfxsBPx-JAM2GFV3EAM5uwoDTRgM3xIZJ4I4ijIgXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7SR5uWFWD0DNi9_5rqLYCOpvsnj30ut32OKtpy1CcOMjjxXtBnGEYFTch7ikyYJtBrH26SQwgR1GHch7aUh4um2HJaaPbWHiMiwyzHY2G1COvZN8knpjPnyZnPbUmg36_q6pPP2pCoiuSy3wbu4-UM0z5FIux3-dbdIFoXkWc0lGadrGlBZWpdQbXXfi0ddMkz1-X-2gvZnzzgz57cJq45YHXnV0DCVb80f4h6kNs6y1x1nTWPaPrcamOh7hmuFEyf61I6RX5Jdl5kOUTKiolanQI9vDSlh4b9Bd9qB0D_8xtP4xd2-hwY_flAI7D6eJL-uNbbzgxmWOIjOcz7X-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUxiHBqF5G459OZRx4CyJM5lxvQ1SJMFPpsfQtHgtZQ68ytF67nO3VK_uHwtOKqz8_NWeVtMcj7DHi_NhOLVpXwQnPp72T0HauL6GeLDxCJ8N2fVH8JSwWflkmasj0dJ9ud_kdi0gI4cRt3As292YoD0rXZTwrnjVjB25rUU7Tt2Gr3w7rPkax2fB5YJB_i1LDrGFOB7U9woxwAdRnjXWiOPEdcuGVpn8ewc1xBSwHm319B_ekoNkuAE-_7KIKdE3xGMDvfVcXUgEP2kmd6mCpfmZFbn7Ruzn7l1GnIBcWM5Z57L_uLy4maLKk9-N9CVjkZKPAl-QabfWGYsDIUsFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcoklqcXUwYFPPA1e6ilIIXKhRxTUMiNfg0TgkfdykJy0-xayq2f5jdgwepCn1H6JTfy_W3s3KEctqm8z6t7An7jyuDYyOzse38B63kobtwN9agHWrXJvPCRkMAXHAIa45cGfo4iap2nm5ZpC8kb6EHX26Nm1Eh0d2Hd7mvmosqKUyNPhmlUma5bZKNY1lkmaRnzhwuJSSfzkA_7V7YSyrVYSrMDPuoK8dudUGyiN8_s8ytLfixJBKw8s7jpLa9OgITgAE5fR7D2o7F90cXLBew2Wq0CFkAvJphqcIp0k4C5MRdw3KX802D5bWhqSK1v7YZtGKjk0Z4ZuanMiufTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltHg3oqyWhUzbt4AZvL-w7F9Ehebdaaut5faOZQ7tcELd0Ofn3c1M5ejc1NATL1p3RahcyptsJo_7OIY6eyoJo-RcseNHk1y1NsEyRiEflmyHprp-kyLcfh23gROGfWGZzz5A_XLi6NogS0U300upepcI35zi9BzHOzha-9pS38H_QDTanFz_Zv1QYtmrLVAGEThxFCHPOQJAJJF0PaLK6NYG9_8kAXIzdy1yQndMqq4IPEP65ZuYbDErqP6OJd4KCvdPiBFKkFZ6G0lIAQKBWHJUzB_PEojFPjjzruKH7gUS6MhBgG1DkhSwEBKcHzF4Tik2FzoV1GkrJyf6RrnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdCu-18wHsyT43NQLsJSySoUZZLZZ70voYK4ESkB_UnIaS_Sb0URiaZL9rikuOwUzuFbEyUlTk7eR5Sat6ls--9BKAYb1wYcceEQvbPtDMrc4XRPoqkYgniduA_zi8PfHey5mJvVGWXxelR3usvfUXPBOOTcfVpZph_JGGJWwhqj8XY4H-r45AGLqAPZNljBbf-cHJJ0t8rgbguR_pFvAgtzukoFoEGsB7KF1N4gpsdzJfQdKok5YXKMKZYgECW-L8tPF33GKkSz_nUK5bsk8bKUyr24V-QQztjf_D-xO3U_BgZN4DWRMXL05eGv8Dx4SvudNSLp-byxTSPnXPvk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lld8UkLxbJyz0_xxiDdiXJWKiYKxcBlZsXY_-LtuEDG49XhGpnReQUh2Db7xIXMYoTLHkEP9hLh9Pwe4e1yZCl-Rc0dNxQwrdrMsE0fbFpzhwhmW6TyTGyn5OD8A3NFb-4Skifp2aywu-q__N84DLUDEg53HEk45cOfNcKOL3EOk7C5UvQvgl-pDOSXZIhYHqHPLWDazy2z5V-2mFrRg90_sgA45PLl7bVPIdg0JnQc6Gcq7ghSIRHobevGl-cql3idoRsBsE1cB1CEC10VuZdIfEM_EHQ6wDGHIe1DNdjM19yPnakF7Nv0_K6KxYvE5t1cjsMBQDlPt5h6gOPfYrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InnxUMcAOZMi8ttfhDNBbhivAxD0WqrW0G_eIIZliVtnIXbRvBvnnLStIHZvtvKMqbowN_o_dPPtrjbuo7Vha7zIvDoOqT-3CXrVHSlxQJIi_K8-8omKuAqzBo8eQPHOFqd_tuwoaybBXpZyT5VKHQB3PaTTCgGts8bIGz4b447VUfTKDpWeGdLsO7dwW00xTGUPX8NO0nXhfbgPyvv6YAC4z0e40YrB7Uzr20Osivz57BU6kzEFlUbhsF7ubrLEZRd6KoM_zLf4rUVDpRzgOl3HppTpWsqgCp8dnxAkJ2NjXfoim-ZUIdZ1s1v1bXSaIDXa3fLnH3KvQqZqLnE_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUN6NFZBw4ZwJWUb7gAvY8OWYWAn-RvHiLvtG3NGctKiPX6ZhJxQtrF14aCo7QbYYMVI9hRZofRT_A5NjgkWs4py6b6UQCL5ezgO9XtNzS6UJnPDJRXOgQG_BuOrdHP1HZhyJzOOXirphzUckI1Fbs2B5gjnMZREp8xO5u4iv0xbGAyVApxB0rFLJtbQg8tnZr_niqocVqoaGAlfZaN9Nlt8JFhGV3rVNrJkHlxEVNp6lfrUq0aL8jFeJSdCuURyIeG74xm3zFVH16eVlDXKTuW8RModDFMGfUOzk95-paejSj18ic_tBbr6pMzuv4GthO6b0Zb8lkb8A0ucgNQhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT9eqCp25dWbh5VkTpV85gdSX9ttBSB_sQL7Kok9AITVzWue6d7OsINrRaaVadaYV1J0BIjlnGN-SQRR-mQmEQ6LWPKOFKH8nNnQ6JEy3-QtkYJgkW8jYtxwxQs5CRAoP8LpWV9A_j0utoj2fEqYOmJSjnCMzss-CsrXp5pZvF9Xz2VinJRM4WJ_F5_QsPANCdfIv2PCVyoY6WW-bXwDCPcjqfiX7w61l8lCNHbUviE5bq4rgHg3OMZeH223Y1LUwbSUH0Rbm1yh5dBxQiRnowEfBbs43j8tzGIZ2ok_uQvs3FeCAcPQENWLDJfPRwJCtYFcigUJu_GdeSQLyyf2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJBi8I5X9cEJdhqQBVzmeNriNenACQ9dQBB4kvPdKoSl35M3bTu97BrfO5r7qDh8FADUsZE3NDW8h1F1X2CWOCEDl-8D2Gi33o0f7ol1iE5uKXs9YqinExSfwYi-r3KoGnwVeMqqRKlNWfO_gWlmVZliLTaWG0YfRiHhFBoU83xICok5duny9e8Fxlrmu2xW6ZIlqpLa71Vu9ikhDJvQD0aas2LtgEFjvOS9AW8x0AGtifDX6R-l1PoPIrDer0L6MCRxrcPC9PFx8rUjXDyLwL_wHsF5Pg4vWv1lvPWzV1MvRh2g6zJFaF---U62baxMtcJCWeaD2p3gXCv04tZBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gifLgPaFoL5O0mTAkrnoLwB4-wTPoh_Pn7Ewc5vjSlFmOJBnzjxXoknqiSfv34glT6q_Y76klHrmcDSLE1v24DZjYDy8jbW-GbO4-CFQj_1-elmdzsXk9SvrXjPGOyxqPOEFxoValMVrTZdrJKjTQ6vvSBe5Gcle0oIwmtic5qZEo2Fv5z-Wa8vg3wSP6uozJcIoPuU8qTnHwysaFF-iZDP3yXaHPY_kZI2ChMRfqsjzoMpFkcNYN9VWss-ZTjEteSCszMJ4uDizcaCIrPCYT2zMnxcn4gke2POT-NL3HxyMKad6n_6oS6siRAuQGXMu-EtwmM9uaVSsmmcQT7S7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=pz7MydrjGscr8iReQDR2DcDTMXnhDxnZq2MlSIkUtev3VMHJkbsAWVr2FCanCvsv7OgUI7YK6mj3kdT4K4j2AH7qmIRz6V1gLs5-VF30iZb0urXst1siyWf6x1wRXE7Uj-8jxi36RId0Dy8NQwhYrhiJNmmnySD7EL7490h5pq3yzTBKsDnkoJSuXJkV0lew_QzmB5T1Wfe4wQHt60DDReMcgmXqDTOB1g6VT6eRtFoAq3Fr55q80yeKF44VYxOS_CqP5kWoAQHZ4HllJhx6eVSqx7lJf0YHAtrRwgHhRXpCdn6nbtJv6BnZ2aCtzSQEx95y2qshjOERACUMAAQRxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=pz7MydrjGscr8iReQDR2DcDTMXnhDxnZq2MlSIkUtev3VMHJkbsAWVr2FCanCvsv7OgUI7YK6mj3kdT4K4j2AH7qmIRz6V1gLs5-VF30iZb0urXst1siyWf6x1wRXE7Uj-8jxi36RId0Dy8NQwhYrhiJNmmnySD7EL7490h5pq3yzTBKsDnkoJSuXJkV0lew_QzmB5T1Wfe4wQHt60DDReMcgmXqDTOB1g6VT6eRtFoAq3Fr55q80yeKF44VYxOS_CqP5kWoAQHZ4HllJhx6eVSqx7lJf0YHAtrRwgHhRXpCdn6nbtJv6BnZ2aCtzSQEx95y2qshjOERACUMAAQRxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv6z4_tV9ud5qy7V4icY34GLoqgD0kRfTJ9MnGVH0PGebw6OFMv2gl5lt021pi3wafDD0AuATN1Ljq3qIkI1831NzhZVe2Dz77w-AxvjXpZ3VKEyQz95wivcReZD7i7q31M5EFJTItn-0kmGWxX3tHdDfcbZ9FPtzI93tEXau_isS495AGX34BJBt4_hEkVtWQUAnS1jMrgCIBh8b6eRRQZBlk1lui1vBIAMEiiJ4XR7DDAFaHOOaY1ubjTkYIq7zvqVZgGBzuXTt30yfIcm3oYbQUG43EQSoyQRpYAQisyd_BBz22KVc1sZAI7M4aK7vlIDTWzKJbYOpARN7S56Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKbeSNe2I4r-UZPe6zOs30384DE9JimHEFx2t5buUO9Jai2pIu6q-ZFv7kxoqW81sqJcKY6n5qAhmlrdJPEz4Rtp2jpfvHRjTPMds48nT0NE0ULZc-_RtSqSjWlfLvur3kK5YKLMRw6nR0N2z29iCyMPvlg2Pis3LKGKHqbuLPBcQNvHgQKxnyl8cI7AMn3Ect30cuuzSAuD6In1oDo_44HaCSuN32aAtXOQGIEu5cxUshG-zYQ5fv38vJ7vkVTULR9BzFb1w3DH5zIZwR4xfcoLnOCvkNC1793cxUrxWpFSSAWUVwOZPTb395EU3fiJeGsS5znJtwqry9HloKgITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjkKHPmz7NxiTeXshQ6C1QdQS0TNSK0umZ64vAg0VwKnT2icQl0FHdz9j6F6u1j1JcrKjg0-RzAk7p57iLq84yVx4M2XxrfK63RqYkilTLu9o9zT_N_qAkBWzrPY-65sZVM54RzGHx5MZ4EpX-dxR_UeqjCocJLs5B4TfdbjWlmx6J9LGEwQ9hzlrMk-RhFuIY9FQSkJGvKSgjlEI8Y2rWP1QHLU5U37Zj6Lax6PQXTuJ9t6xCaBsYpy5h_Ob3gX-PnIHr3xC2whE1Qz9DrkpSgHXCSj0bY2qhogO04o62rCRvcOsjMBsJ-pK3vxPJ0o2ZpReXRen-vVqOyg8aQ2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDGxOYJHpqAYnOasmH3bQfwnVHz6TxM8H06npqNiXw0C3ZN0ZBeCvaUHX9Pv845pF5rrXBzZISFAKMS46zaxSXUZP2b6wejWsdlP7esvRWF1L1bO9gflSGj_66o5ZMiRdqe_StE5QxxUa_lsJkUs6wzY4vNk7RTN-u5LVfCtJumFmR1bIW-ueOje_MDkPptCWWfMABas9XJpt8t9vST4QjflN111j4y5rNLmI03cMCXY0dbwk-Zc7SabCtkmgmuD9ES6kStNOsLifqA6iKarZnE7giG7Ck6DeRXFKwZmNcq3JBf6SoHl2RtKcgHdZQTKXd-hjFXyTL6nak86BclrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcdOsQiZJ6qza8RgEmOU1fyq7Mz3URbiCRDwAMUfRQ7pQEJGUNGKJOxuVBlgW-_9d-rSC0JVqvEq7k98xOS_d_UhyV8_dv5tU2QNXD5duUJP3_3tOHJlGlhJQ4BefF8_A0BZdO1yKyZgVoWCZ4sC7AI6ts2jPY3IDUIldrOmWnhaMf5hmrFE9NnR8-5dGvJuNoSVAfUkakyoZxv4zg1KWIVGZEwRVEE1CT75aNM35k6QDfQPBvM61kMI1AZTJX8ZyanKReNSWDeRkCRuWYBEW2WgdO7k0sTcr-Uhb9CSbN0T3bS2JhPLONHERHrkyr71Pq5MIcW8d5M2GydEgw_wnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai5BdpF7Yyxt_AxjWpOSHZ3mI415610gheBvLzNQlmYIa0Q47HAl6zutG-ATAD9fHAVcdhavj2qcGFNCjn9oquzeHBhhWXYpl1RvzzX3vEHVzAzYhqsZDsaX6WuwWvLDkI3XMkZ2RtAf1CphBgYWgkdA9ZLnYeTQE1jI6Sv6hIa4KRRFnvnkBZV_-4WfWMnJkjx2JDQtQfPupQEtFr1qnSYsWsMs7hRdTxJiuFMcgL8naH4D_GijEPEP837dqlTyN22L_o7Ahz8Db1gu3z-wDPVN0Z6u71b5mHgfM7iiP9MQ-WipFJvbT-yuAzY430f48MlB1sHe4-u8jdsXvOEXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlmRaDoXEKRfMynZMPDBXPtC4OScDXaNEbwwqhiUUGZOltZyzDgDutETXE_Jj7Nc8QvhXUJe25z3rZcUTzp_3xd-dZZXZ6zk3HNT7BSOlUL7omx2DsQafGxiP62OFohH9nzmY01CKbaYi7fe6mMwZO1lo2SR3EhwIabX1CiQkDDqlulVBFYNxETCgS65Pucg_s1BFTZuAb3BqWLq4oWCqBSTOqufimQtcU9ZwaTmN8_C-pivB6KZP5mOUzNwIHIMst0D6KLJcoUdURZVgt5PneG8acs0EHs99ePcwsHWTZzHgjyxvqO_Mvv1NFyLaw-fcvX4vFLNk2oow94SLKOsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWto_ex6IRkmDy6xifZhHzooDJOCkUkjF_PILrxerMoaZMiVEEob4hmqEtFiEY-zem7wpD8mHlOggwd3IJnyxo8TV5S4ID5WCNNJ43CNZTGBVpG35qvWtN2WQGYdQWUiGqZGyiEIapDFk3xS_XS5NmOVJAzo-e1XDhGWhFDa309CCVbirNBmZIRTCb9MeqnnfDZXYeMao7sScqawGe7dl62gg3FjHMcW_3gjN26hCqJhGm6PuEOyjGUv4BFvt-dgTE-PoqD8t9WJE4jeaqLvDouR7WQpAQpGUcLdOwy3Te073vf0p-7C4wOxKxeu43sf9nEgOrk8w0MkGGPx_adQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep7TiVBVqEAyFLqaA0vNcA71wm4V3xwZrKEwnpt7GGA1bie_rnNqga-NdTgS1osFn_QLtwzrmi_wfV75PxSHs2mmQQs7TTyxFDS9tM9LpJ_iMN2nUULR8u-5cK1A1pILv52w4esfJnYFQyDuDqhkrMME34xFRMekcIHtNPltqLKpZpyj6ssWIU1qJuqhgvgmYQwuuir1LBeQNUsATl474W6OnWcxhN0HIlYhiTtb2iMJrrRZLKmhEZ3_B6_cwcvHEtP8hjo_cgjk9a9qT-gBtNgzllCj4ecXi7bu08vk8OA_gjLywu3togkAT3U3ZlsvSwXisvSS7ts-6xw0AeuLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGR1jXmdZk2XlSg_iKX3dah0CPLmUGmL9gT2nzEehmVvUK7iA9PvPlmZZQha41VlCbBmNkgy-wh6NTvtwnaPrDtElbvKxPUd_cIw6YfmE5LlocWECZiZWnC7bn4lQ5ncyIoAWBIK1SFxOHd7B4cPmMCoiLd4C_uQea_g93usHwfH39CrdrhLSjxGeipmZB73PLGYi-39OyAvgteZBMOcbxE0Mzed8twtCv7Qg3KpPrpTXI78L3OTuY34re84C2pK3CUlDt4hVBD0BmD8wLA4NJkBbrvYMMHqdZg9mhA8QKIav0HbSlHLkscWAHuIaauoYoWADLwo9IpTV2feS89BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GksQNsqCh6aseMUhOQlb2nsNumxKIThVUbBuzcxvJbzGHxFU-ZkRf7Zc5V-TwFdrje2yzOTtl_pVf3fFMhx-owMr4FiJrNy-d4diRDzU7rnIk9fgU3uppzDcGCQotFCK19ev5BVrTeMdqAhGFjbMBGtpwtm4B2_Xy6J7kM4YdfbNILqbebA9lcr_rM7lT3wwcUIwA-A6gjiNqKHdK-QWnb9lsD0S6FU1u6fXX0WpYr6Cg2ZBBKY-ZA92LuN1bRrIzWEaUAIgHG8SeUd7E4sNhljFj42DKzzf-gH75MTCLlWh3Ej3POPxzM7hLg8vszl_6PPFdAhG6qJEAYs1lhyRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZlIZ3SS0HHsi0fxUL9xfEyGFkgNZwQgsj8W4OU3lZd5gVvIQbl2Xr2cEgAksdPj4WrPqmqKG-bKVwAH5BMT8dYP18foZu-8deH_0vpeAW1mOgLxxS4ZWiAwxlgLFp6_nnr8Xftp7aW1-K9ByCfBqVNU5vFI437rbwwQvBcctY2bTrMfWcZL8PiLpnYnEyRzO3qAXe5OViXifzETIbD_I8tt2ZqjCBUwKrGZkdHSI2xp4QdOqC4ZLaSUWIG4pNg0TJWlu6NxNfewP_kYF4muxF-_XNuC7B7wgg7KcTrE__tG1pCjwgDUtcPUeQpKPwH8rxsKQa0v6Bz9vmdgIEGaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfrmIx0u6SVrwhLScSiSgyjAEkvcQ5uT80evXzWvGqIfQ5fu_LX3MfUlhJIBwBakH8q8D7x4lU0nliEfh9qBazj0Ms2GBmriWMYhD21UEjZYa52vriXne_zb0fM0TmKBC5RcgdM7y1dtAg-l8xoNd8x2nUGB8xuqiO4GEjvore3Y-f7vrv_54bhqlBAXv7cfeIDv3FNSZsq1QDfkWYMtD13vtcF0gZ9YFD329KXjvNlLK-j9g_w58TDQB8pJt_aiPeaW7MT0waNsGweFYZK7R-4Tm_39dbFvq9y89KtvRtGsyWB3n6QBIgRybvKjAihEbDgoxBl2YWo-MRS6Ya5JtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=GcccoLk0bc3rrzXYam3yLlFjQ-cP8L8gS-cE_vjSytMOk2dzwXgN-Fhy1HtbiqhkKOV3aJCU1lHhQPor2jqu79pcLvHuZyA2jXwfPCVvayZu8T4v9zefDsDcXpkge37DRsG966MmzOULvhpdi6lCU-wnoYRZWNMF9XNwJU6GlYlUK3lQriGbuMVnuk5CtNcrzFBrLi9E2ys-udZl44Ukt1Wp4IwCtsMgcsz4W04G4y5LLmb5HKZ-R_15w2GNRenD8DErwTHRUv1bBR0L6daH5e5JttGtyNCKopSPONt9FdbogBu_DDNQrpU7HPueUimr2cVG_vP8dnA1zExxVAumlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=GcccoLk0bc3rrzXYam3yLlFjQ-cP8L8gS-cE_vjSytMOk2dzwXgN-Fhy1HtbiqhkKOV3aJCU1lHhQPor2jqu79pcLvHuZyA2jXwfPCVvayZu8T4v9zefDsDcXpkge37DRsG966MmzOULvhpdi6lCU-wnoYRZWNMF9XNwJU6GlYlUK3lQriGbuMVnuk5CtNcrzFBrLi9E2ys-udZl44Ukt1Wp4IwCtsMgcsz4W04G4y5LLmb5HKZ-R_15w2GNRenD8DErwTHRUv1bBR0L6daH5e5JttGtyNCKopSPONt9FdbogBu_DDNQrpU7HPueUimr2cVG_vP8dnA1zExxVAumlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=sQ6_E-cbyMz6omZR9Ouhw2MlcA9JMiKWgaAUEVhuCZwWn18h4l-j3wy9JECcd1MdPLfCy1PL2heWvaF41pqHE6gNl5f5Sncc7DRGdAbfttFOthJPJtJbWwSOla5nScoMKKvBKfaVVMhpjWNZIoucWKoU4JVu7H-93NmkNlvJ5OHutz4YkRT-V47PRHVzIxb-C_2nF83XIbDizXZE7N8veLXissbBU67OlPdB5GPd7Dt2HusLLlQkvDeGet4xoF9QlOBRPD-cntxfTODlmTmmt3Am_25MRH8O6zastnSJewzthDLKA_NeNn3P4bgaHgobpU6W61GvEJwgHQmfjMUl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=sQ6_E-cbyMz6omZR9Ouhw2MlcA9JMiKWgaAUEVhuCZwWn18h4l-j3wy9JECcd1MdPLfCy1PL2heWvaF41pqHE6gNl5f5Sncc7DRGdAbfttFOthJPJtJbWwSOla5nScoMKKvBKfaVVMhpjWNZIoucWKoU4JVu7H-93NmkNlvJ5OHutz4YkRT-V47PRHVzIxb-C_2nF83XIbDizXZE7N8veLXissbBU67OlPdB5GPd7Dt2HusLLlQkvDeGet4xoF9QlOBRPD-cntxfTODlmTmmt3Am_25MRH8O6zastnSJewzthDLKA_NeNn3P4bgaHgobpU6W61GvEJwgHQmfjMUl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY16VY7f40k8tjcTHWzEZ0FRS5ttIZRFav27njYDC9t1bviDUZgm2CnJDrM74E_z1pOekhYrq0EEHX0zcgavcSiPAWkiIX8J14iotm2UzXK4H7NO9cfmxQLce_xZuB_-b1gBHddb0iINE6qpn0Y4OXjSEpTK1NpQDw9pargWWK0IWdUSfQ6Zq70d5H3x1aG4olhqlO_zElCsVqOx96kO7Y4bjEXM0bVuGYEwaOTaXLfJeH6pUMqlelaE7UhvXtvFxr-wlrc4f09b1SReksFFejubWYXUMIPsXlZFyEaGDXZdACU8YNz28IKlO7M02WsjKSalrvAXloFU1agMItNxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
