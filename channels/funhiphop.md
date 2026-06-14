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
<img src="https://cdn4.telesco.pe/file/fiUtkfufKVOKcdNwJMsdSaiB0cUDSvUdrM8aoWmrB03xOR3HJXFTHCOQfR570KL518j_ZiB6T7GtfHZuv_3aAwgkhIFvYqgyvsFHtYBFv3fvTwUWzfaUZUrxFwXWWeSsB4AQX0lUSTzrlX-e3D8_itnokSjTa4rRvzBSMoaySVbNS7A3bwMw_VsR7PrEuKT9rCoi1A-4p3pbf40I3ws_0kKlkA4As4vZLJckj_uHus7ws09HKu1yzS8SSSwlSxg8scS6CH_sE-g7yJ4g8oynmHZzDDaQadj6_H1sfXGdRNPxEHc_5MArJP1Byojiuw-K_P6b_GF0eYzPXS1ixz61zw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گل سوم آلمان
هاورتز
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 742 · <a href="https://t.me/funhiphop/77887" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گللل دوم آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/funhiphop/77886" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ویویویویوی
کانال ۱۲ اسرائیل:
اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد.
جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/funhiphop/77885" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آلمان خورد
🤣
🤣
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/77884" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
ایده مقدس فتح قدس و اسرائیل و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزش از دشمن متجاوز هستیم تا درس نهایی و فراموش‌نشدنی را به آن‌ها بدهیم.
ما با قاطعیت اعلام می‌کنیم که توانمندی‌های رزمی، دفاعی، موشکی، دریایی، پهپادی و پدافند هوایی ما قوی‌تر از قبل شده و تحت فرمان فرمانده کل قوا، آیت‌الله سید مجتبی حسینی خامنه‌ای؛ خدا سایه‌اش را مستدام بدارد، ارتقا یافته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/77883" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آلمان چه تیم خوبی داره احتمال زیاد از گروهی صعود کنن بعد ۱۲ سال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/77882" target="_blank">📅 20:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پشمااام چه گلی زد آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/77881" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/77880" target="_blank">📅 20:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXG3vEy04gYIrhDn6-aGrSmy0Bby3PbLuNCxbVFPQoM47K2Tiss85r3TsbD-_EOJZtIosobOYX02fUUXEsH8vg1Xviw2rvPhK9TGQe895Bc5uEasRZbAZkNZuEpv76uI7qz0sbyFo3z73cV_kxHRX0MPGTl2mdLk7s2CZIWu1YFCERwVXQ4Ekol0MEDmsmC01oSdoBn8Xf_ZgUrkmBbQsams2K3AhELDHO6WhhZpooS-hETtCGH_jg-O0rZo3HSYS2jSxpw0SV1Q0mrk5tzkaBj0DKdO22TqDX7EuNXSXo3FtfTrLRc7TtrE5xljATtVpL6-RzZM9vokoNoe20MwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس درمورد میانجیگری ترامپ:
جنایت امروز رژیم صهیونیستی در ضاحیه بیروت بار دیگر ثابت کرد که آمریکا بدون اعتبار ضعیف است، زیرا حتی قادر به کنترل این رژیم غیرقانونی نیست.
پاسخ قوی در راه است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/77879" target="_blank">📅 20:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ت‍       :  امضای توافق امروز به صورت الکترونیکی خواهد بود و پس از یک هفته تفاهم نامه به صورت حضوری در اروپا امضا خواهد شد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/77878" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خ در ادامه: قرار بود امروز صبح توافقنامه را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت. به نتانیاهو گفتم که هیچ حمله‌ی بیشتری در لبنان انجام ندهد و هشدار دادم که این حملات ممکن است معامله را به خطر بیندازد. اصلا چرا بیبی باید چنین حمله لعنتی‌ای…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/funhiphop/77877" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تران در ادامه: با وجود حمله اسرائیل به بیروت و تهدید ایران به تلافی توافق امروز نهایی می‌شود. از ایران خواهم خواست پس از حمله اسرائیل به بیروت، با حملات موشکی پاسخ ندهد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/funhiphop/77876" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: توافق ظرف دو تا سه ساعت نهایی می‌شود. حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد. به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟  @FuunHipHop |…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/77874" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
توافق ظرف دو تا سه ساعت نهایی می‌شود.
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/77873" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسمی:
توافق نامه بین ایران و آمریکا توسط ترامپ و علی لاریجانی امضا شد!
پایان جنگ ۲۵ ساله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/77872" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqwbBf4jPsOEoWupK7Ir-AuCqi3XF0ioFHeL-ZczxcCdHUa3e1yQd9DagBAMFmrmTdB7NkaRS96uTFURBo1mJL7AkEFTHzQvPMuGdHAPeDjgd7pXQPp77fA3TDvhmcD94BwZ0ehUPvSb5IyciDVocbYXUnUnjjxy_dkTDTqd14mO82wLfqwISohCbAnNOLO_u7Ur919SoFNPzQL3H8kNgKUX3u0t1GnZ_X2TGAT45c85gWsMmKKxN88wZmmPFdwMHWRfL_V7pB3uTekCi4pnY1eABY6uutHbsaPT5wVTdVRTzN8k7dSZmZNprYvosU3cPSu9RwZnIPokf2yS-ZKwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهش گفتم 90 درصد زیبایی دنیا مال توئه
خندید شد 100 درصد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/funhiphop/77871" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/By3rxijtjqppdyRbH6scEC4Xi0xPntR85zNR-3OEIDPuAK66G33WeVODxTkg3hf7QU9I019vZBq3twfqrsX2t1-cSNxA5g7bDYUSuCsg2RWqPt4o5fzJpiFSW2D3ENeReIxugix_hsXHqps7aJiGUq6sNNfxK3WDQR8kF73ZvWrTYCXQRn7IiW1-3X3tubQso2VtGtzeC_yaa6EX4dZ6uX72uDSyN4qv7q1YKRgQGVU_OZ0y6kWLEIk05zA3xN665zc-OlYdcf5YK0d5YMp56HPKsmnsI3PU5QIF4vPZCGkPhWpy7uwRZw2BzNT0P5uvJ79aYboCAd-dB52cZ9ju2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S99x49IIAvOLYakXu4Jr7_ql6HPovl3XbyOVPkgDxoNj5EaXzZlgMyGjgaRh47sfkJDQO8oiN4hBJo7Qxgp0E0KHMO_70SWhDpeYNkePb0T0z1veS7WZ72eiSuJPgVkK50Ohl-adqz7aAhL-tZLWenU3oLL0NiDVHvSiHQfqH0FpI0T0iAjJBPK-jTCngleAfyOB_UMfXDv-T4V2Ch6qWJWPH4fZGv5T5S4QE4JZkOBkJN9BROIE5zpFMGUJCCpnbqHn_CYZboKt8Ax4vBy5k7Qs_8Ee3JJrpdDRgHt74Q2vD8E3pX5v52vP1tP9-7IGDZtRPyQ6RYb4oOap7SoZGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادار ترکیه تو بازی صبح امروز با استرالیا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/77869" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/77868" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioanSFgGNKnSVwPE4fbeWQz-1asZHE5s2oXCTEceb2i3D_JQ0R2XsmV3urUnRF_BFUQpcLvYxygZend0_gZiXCzVH2lIcUpyW3Z9e5GCWFs8tLwlEtsn3mswH4756UVQrvbbOrfz3rhhLlF4mgUBoWRVzfOrGNUMU041UCV_Q6QQFkZ_fNFPvOm1dBaI5vW7KtMcyIdz_9b0e25MfeAcZOIq3GI2IVJaQEZpV-M50q_vd26X9NwLiOGPOvQmV7Zl5463fSjagvRjW36JKh0qWqoDAICFNWZAtuuDgPY55_toT08Q7J_QXre0LM1KtdExcx1nvTyR9WuR4FMjFZu5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g24
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/77867" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ZHnLjLYYfGn64GqzSYuEFS8NpXADC0l_jtYa98ZacyZZZq97pyUDAtfemMh0faNU0s1k8az8xO_Zx2hQFzj6-t3zAm-dNoaZ6yqAD2iUdm7gKxxzGn7B3chGiHcTEusy7ih5cHD8RL5rcpP5efESCs4_JBLRl7FX3Z967_hb0CCfb5Xkb85U_qey-1LmysQYspiZ690BS31Vr1Xvf5IyxK1IuXTo-bDDQS0gHeHWM_O3RuI-JkNC7sziRwZ99UQ6VKIRmLF4MKHXwoEG1aAmvDiHurW_TIi87vaOEQvWsElW-5JDNLVIWlYiySuSCl8Kr-aT360_v-Sspkpf8uWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید آن را خراب نکنیم!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/77866" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V25bvotkGQ5V9fxFs24sagaOQMxZjtxG4CAwueWHsz7V_-ScaAHk7DxzaI1YDZ3tCTxueibBBSA1cdPrYtVkYqQKBRmZbA1D01VDntkb7dr_FcpNK7LHdQRsIenTzRYmdEHsRVrYR4LM32KcjaGG7PvgePs6KPRAV--anQ4zVjJzzjbqOHLmLb2RLtijYNUHmMiWVaulbWz3A3136aXmt6TUFO6inqfsqIZ4fl826EC24suEVXQ_PndpAWx7P3YQbg6MThY2UqpXmjEpukCP_T5Sd7PFslb1AA7agISczlaQQiACgpVmxzOoBa2loDUv7ZTdyJthreI3LFVBkxHiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید رضا پیشرو
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/funhiphop/77865" target="_blank">📅 18:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXwyrn-AUJk17LQq6YBCQq2ruKu3uZ9rnoBt8Dh9Hl5ycNkiF_F15dTh1l1m2Q1TKV5lcuiYG56NfT1Oh88PiV29o43hYLmlN26hKAPErUVt-nwxmFv4WQCu0K4OdNWmWhPiMMLU-vY8kG4Kr0L1uxG3vqCytiIYnDW_yuCHP0x2I-IeI2cR6XA3ZaXki6e-btT-mdFbTex4IwG6xTKL4_neLFioL8pG4C0RacAQi947CEhwnSASJsKQsBM1Xy-F_iFfe-TPjA5s_DUWDqym9gToGDM3vR1f6ociFjQlJJhzPZTY1QIKe2S-zyqxujWtM30b-TVat9Db74M2NH1MFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSu3vycLg3c0o8X2OVBFT34x7a7125nRgBXEcKfRB9Jtxkg_WtFshnUIuzseZ_D_TOjthO4ldOiaN_FmzQa7Rjrw3H7Qppkz9uxcXc-zw5nt3VkVNZui-R-5rNrZUCkWCYeYRNjjz1n09VOES0AeuiGN-RPkNDSn-fTd1S6oRQyGHsNRVh62hFArkbxufG9QMug4H_p9rAWv5Zd40NEtOcc5wioQPTevYBpnxpVW_Aav1AA3a4o8ao6LgJwBtNqDTNvsW7mlNyZzeqezdfrKUsFCSPPQAKkFUWE6BhFmn85_IMDe1mfgd47FmXtjXesiClqpvK0DQxw9ys7ZKJsW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muEb5WNQMEUCLdOW7Pq6uPnA2JV50wsmGQ7USqGHr8Nemr0qDxkOHFR_UR17YmYEv92UmgumbeOIkjTnxZsvZ4WNjqIbyMYRc_57ZFws_Msp3zKoE0WmTvLp1up2IWhAEZtODchzLBbxIsh7bq3AilVeDcgWUHfsh_cAaPnDQjfI9d7Tkkl_kr5ApgcSds8749mbfeUTO6D9I5zOdYpnOogjtWNsPRKUwEdZOUFAT7-n3mArim9hisbuSJXG2Mp_gPUNnzlkCS-IAcJ_dkSN6GCJnKPrOg_yojYOMBQ4wCfRtCN9U5NSQ75_-NRk5JkfIVOpWWrmoUxdCYBHbujpbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGjFNWO2a6jFJp0Z3pxRdg3wzFCMR1U5dqXPMhM2k5DjAojo5CNC63Jb-VNlKi_W68cvizyyUI87mehy9UW27VlvgdRzJH7IVJTgPG9hm6U1-VwKiwecf7audasdOaOt8FgKlAmO4_ID2gdLnBBPaST_JKveO3qiHE-kb6LTNtbIgd04rZEh8rF3gcmbr3W9qlDiScPQOJDZxAhhnyc4J_cXKPmHd3_aIMs1LSnx8aMmQC8nRnLgQAKpWdnhtk6EiwXNP2C56UdpOYGW5_Yeq2727nGVo-MnhGTeKjkwxRGr2GtlCLcuKKnvDP_HIk9Cdr6t28EdfnyN3ft72mNeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnMT3MhfV3ZtOoE9eWJsn7qIgx4yf4XQT4XEG1FKu1lU9QV9qbkt1YJMkt5Hs-Ibce6vt1b5JiW0ssatxFmpt-l0-M1-TFcLlEybL7KrWHsEDBgsGbKN3EV6cpS6BhStTFnJerKmvxslI6L7CZwdIuKikDIdoJIXnz92aA99Of9jeDbzk3MMCd5JyUx9lq0VX6XrsQ8dq_hYlA_iEjTCiAxSQvthsi5jUNguEVl2SFq9yZZTsY56O3Ibgg_whaoZz-n6-vp4DG1KBlMncxIwH22ItEWr4NQOWYpph-ddfj_L0ifWePwqzCEy5oMrxGvpyUP0gM7q1hVdAjCARvCl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAH-N4aK7CyBYnKs3afPIMMJ5Ca2B93x-qaC-LPO5Y2JTzc__xDx6ag8cECcKVJ3iz8-jNIhcfOpcCxwSA7PXuo1BwdzEsZFoxu6ITEZwVxFDLhzfDoEXlCHzdHmPS1kuLTtkPq_phLA6lGLWlxD1UAgx_Y868b1pnGEqkLCUrO46pSsCdqXX70g_u7En_zcLa342uXqhZj5Y9fXJyrqg8vLs-_9Tp26-knH5Hl7gdJI59nb99NgBV1_2X44-9Vr8dY3JtWtEVeqDrpkKS3Qp7k64CM4alOw8csjq2NN0HbbcUz3EUIFUprf-s4SQU5SQRvozNLVw4tYj1eblsRPIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgnXO6OsGCFs5Drff9C7j1HiT4zfXWfHLs1tI68-X5oQP1fbH8Yvfe3jpM1aU9vUg8ItDAlaNsNATuUL0pCOWQMtrVPYf7j0eD3QOZWjJZ5mlmLYH6DcImcPgjkStudWBJz9JXvzT8prEDDXlGW6ZBJ6_XOIe01nZxpGnXfYeoWlZF77s8qYaZNdemhEitw17r0MNi0MRI_db7sHLsUv28GMqHn4zyBUVsFoamsAp7JAHEWWXaUWwMsoLIwmxWYWz9RiaWPvc6ZcVcOAu9w4CaQpQBScQKk03C7y2tm69QcxJFLOiSiUvNBt3OWDhadBdV4DGewD4tiRgRsAQNLkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu9OAbs5HE4xgCpizXdcUplhqx1KSbsUWaNTYHUAE9r8L73MAGTNLWOQmC7FIXhqW4PbYvpCe7KUNr_Ao8U9AflTRzAo1HUB53x9BR71KXdcySr_V_tJUpQzvUH9g_l1N-QZX_yzPZ7tayaPPmbLdZHdtCUhxx4Kn1RWtyOeddGIiPOPpnqBGy7S95yfy6WI0q3EZ0anpWCEo_w_RsaJBUABPIFukmRKPOTFNlRYM-7rxEyT-aH5KzF-zH--W0YCID_-Y-tA15e07TeQW91nBGG6KOQNULfAiFwXOkEg9Ps9OPdxib1ix1-LWMDWjd8wCb6ysIju3mvejJ-pgVkGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZBt06tMeEvB_gQiVxC74STz3YLq4olgZg7N4w2DC-xAo9-JZM_VScYzZjANocrfsbPutraUyd0XuFCculjI_hvkavqeuEUMePX0Eqt-We6QFcgUp8pz6EbF14Nj_G03KZK7HXLmp4Wb1_JK0wElQz4Q8cGhrHNenjdXdT_g-ffP8W9rkg5AM_ITNS7cAnfOQt4DWtGIFsH0D2-wJ6kqWNI1VAejxICoIHNR_QDbwNK4pHVPIwLhN_TDGQBI9M9D5igAXI7YLOXweLcNJp03kL6JL1a2SuA1lF4Xs1xCH1nFB27QeSAbwRao_oNBeJnYCzzBX2S4kxXZjn8-sMQT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJeSGPoOpGpiiyvamsfMXtoPwKm9_idHFdo9l2hreMTl6rjZZZvoJFQcRv9901ckc5TVvDtz40J8khA96fjk5DbfHnu5FxDwpOSB5Ahvr12rdTNSj4kGD07mcZ3ghJTnQHdNErnqHfnTcDuDhVBjqal4ZNQdywnvLn0A41rMjlv-MtD4b_gj6xGpQX58v-yxHXfO6dfsaffPMe_htsjsChc2y1CMp4uopdmAlEnThXBx77_D-3Ndj7ZgtUgPBnuZzSs2F5OKrw1PetDpcSltX1q6iKC62Qu6UXKLMzR9ujijKain5v7i5xtWvf4bim7jwsOkrr1dmHJxcw1lPI3oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTjSdSejUphkYSJLToJElqg6tz0w83yD_u2nHpAng2R0d3BgcpbMSz6sabfpn0_GW43oEd5sJQL4lO02zGNYVOdvli2qNEQxlsdNXtNyGeTCLKEyOyKKeiCql_jHrfvm-VZvrHwvQWChYqdST_B5HyoGRu8tOR3zyNukiU8ZuLrnpGAP5LmxUycqRRcjTyorIj1Z-MP91YptoUpl1aorMEIj0St2HpKxYZCP-uo1XNMVrizfBzGFAYpI4pgFASEwG6RhIjSzgS50XCsaTFCNvSDsLgjy9CgATkq2f2m9ktlqSd5kSvtKjSVL4gc7oj0qgITz6le7ddaDASa2A-GwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q19k5q4DjaIeitLG7MAR8Y5Ugg-_I0PDkOCi0ECOd6tbKqHU-JVuvVaVHIPq6gmofjtXdCrdHcL7HcFpkeBZODgduWVkbEbPdcWfr6-9SPejXmQEbme94OUonTVhNDO1T7SBey2AWhluPw9LmK4q2toEphLOYGZDT6nEi7CCgvxquFuLn6M7wvMTLHp2K0Y1H8_OkF2OE-iMavnblCXDX9sE18WKacLDlbkyPjppT6w9fJstuGURm-ZZqSdsiQMdWYBITrQmPPH4Qem5766y7amiXAWz1z9a07bejTwYN2NUnA1ibiOIDsrbz8oRuXKCgSasrLRW-bCYwH0OSOTpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvEB22-5HVGKyc8UPYaGdIX9OAR6Ltf8cr5pRXy2RP1Nc8JidhFxOWkYF7KJZxCxOdD_M3fZrwkDHw_i3WfdaZIOkg7hf_XwuPT3QDZM-UohLY9cl4EEo3un3i9SRkSV71aVC-Kk3l7hiTebpkUW8tuhAaa4s9MhR3x0SE0489dRQTNt2XpaOaUXV6rQuEqB5WfaEkmmgbB_ZtLS__BPFP8dLwsKyr7Gl_ijRUYXdMaRm1mMWxegx--9c2objgTqAUDPs0jGc_oHz5THK1npINbODwybq6yu0cV63Y_Nt6NxAKNeWUj1dy6bBNtT0VbNyuWbr4HzL99-4eC7Oh22rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbfrzIviKqThzjjsaJ73Z8t97E3QaCgD___5R_vXcmf-jCEEmh5elsw5zoV3gBhylal4qhFc9-Ah9M9m_r54O94Zy2hejtwAJoHuJFrzmv0kU_Bl3xPxaaWSmqDhkJ_DzPzablYM-_pCYAmTRRSFhsJLiox2lYThvhMiqUNLyQSkNRJo5A7Jh05yeDwLzypehjlzO8U4SYunptS8OLrI69yHsdhCpC0AK3rMnBWsW7WBm1Ga0MeX7RetLZjnMx04qNAM8IhE02pfGswvRUE-T6c-W7o7Bddc6NMNXORooDUPlJGLeKNMPMRHNn5MxT1YUjaXTE9VoOjmqYewfDAdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=D3tkUKrASkUUKZrW2FE5P-F8oM7hrupVW5lU1PvZY9gZw0CWZzFZl9HRIp9yKSo-15UPkVX2ZN7DBP2-EgBiQezXc88cDESytxYVo8C1Q2h5jGh0RywhmulRFmB4k2xxBr2DC0es79mX3LeGMWDzpSENY5obIQoeFkjN_tokZi_HBL2naTa_tw9NDhoboQFZYI7gb2QU78NpvWXnM4diPcdAOIIFNY6UIac3nIduJ4kjbFj6ys9wqw7yHSOz0jPLi-zDgY2PO48uBN8r3IJ4m4HpLF2hBMYhI0hPkUMYlKqPdcemAGQbZgIKiyQNZNUiPIGx8d27a5GKUv6kLW55cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=D3tkUKrASkUUKZrW2FE5P-F8oM7hrupVW5lU1PvZY9gZw0CWZzFZl9HRIp9yKSo-15UPkVX2ZN7DBP2-EgBiQezXc88cDESytxYVo8C1Q2h5jGh0RywhmulRFmB4k2xxBr2DC0es79mX3LeGMWDzpSENY5obIQoeFkjN_tokZi_HBL2naTa_tw9NDhoboQFZYI7gb2QU78NpvWXnM4diPcdAOIIFNY6UIac3nIduJ4kjbFj6ys9wqw7yHSOz0jPLi-zDgY2PO48uBN8r3IJ4m4HpLF2hBMYhI0hPkUMYlKqPdcemAGQbZgIKiyQNZNUiPIGx8d27a5GKUv6kLW55cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Y4KMuVIeb0kZT0SBvCSd7tOjSbQr5ZaPRInBMwTAng5L1v6HFdEsoIcqGZTVRqUyCTfPI8v3QBHApb3pGa-7lN-ENE4i7PGmC36htGgd3RnLOGXJoEAyrW20TNUJwozqMMYnkeO8kt2O6rWs6ZLLWuVbdk0gDO4Hom6F1bvlk7_BcdwYPUGXfZlCyyWSE9iRaJLSGrRpYwEvgW537FAGfSHIfGVJmM99QtICiGgkgMDvVDQnDWOu35pjip3KUexbqKaTjjiD7g9h0c7cjUwqrgnu8NLBazgBQPZMn6kDPpa5TQigJ1WaT3cpijL3aW3LIteIpdhf57kC0ERBVbeTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Y4KMuVIeb0kZT0SBvCSd7tOjSbQr5ZaPRInBMwTAng5L1v6HFdEsoIcqGZTVRqUyCTfPI8v3QBHApb3pGa-7lN-ENE4i7PGmC36htGgd3RnLOGXJoEAyrW20TNUJwozqMMYnkeO8kt2O6rWs6ZLLWuVbdk0gDO4Hom6F1bvlk7_BcdwYPUGXfZlCyyWSE9iRaJLSGrRpYwEvgW537FAGfSHIfGVJmM99QtICiGgkgMDvVDQnDWOu35pjip3KUexbqKaTjjiD7g9h0c7cjUwqrgnu8NLBazgBQPZMn6kDPpa5TQigJ1WaT3cpijL3aW3LIteIpdhf57kC0ERBVbeTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=NsWPItK8QavZtoXptUqh-EgDPmIRqrYbqsfjEHswGTBRKtBeuG_oI_EskBdYcjGUbdNdoH2jqiJgqOiOMjEx1uiVs7aGfkZfzPp3mihE_r3sw3-u9XQaXyNPAAdfKkmc72BLNXq08KOKUqU01CDWj74vUkduFk2gVrF9ozsJ6NPtXM7lyYcuzV0fPkP-4E_iVARf5NOi6M4yxyYwz6b7IfW8APQaxg0Y-fuTynsuTyir2JDA7_pKFp2qLVHFUvSg187_rz1XvCBwdhHrYVMNTz6Hv3nTIstQLyKhjbJn9MIQBxgdKzjxZM3ApT48Kj33DtOWDs5iGA517CucUKaEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=NsWPItK8QavZtoXptUqh-EgDPmIRqrYbqsfjEHswGTBRKtBeuG_oI_EskBdYcjGUbdNdoH2jqiJgqOiOMjEx1uiVs7aGfkZfzPp3mihE_r3sw3-u9XQaXyNPAAdfKkmc72BLNXq08KOKUqU01CDWj74vUkduFk2gVrF9ozsJ6NPtXM7lyYcuzV0fPkP-4E_iVARf5NOi6M4yxyYwz6b7IfW8APQaxg0Y-fuTynsuTyir2JDA7_pKFp2qLVHFUvSg187_rz1XvCBwdhHrYVMNTz6Hv3nTIstQLyKhjbJn9MIQBxgdKzjxZM3ApT48Kj33DtOWDs5iGA517CucUKaEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLLC8Xl5uGV8mklvs4zyOZ4HZttFqp4SDcuFgDn1BoywFiJJZq51rX6QYyvvN0dO3XYzH0sDh3I4IdwVegbgWD4NEXygAlph5i5zUcPCuE520rsTBDkkZtowZROd_6jDl5zuoPPbpkyb6Q6FFjKjpCKYkQHuLQ842sU8m8jRT7TGmrJfNUsWGRR4B5VOX6l8hTEF0qQRsuZ78nzjsW0XJfy5j_pp8wbDl1H-3Qn9wFLRYaa0pf-VIbJo1bcYoU4z2QiFCeBMgteiAxBBnYseIkV93qcpgwPb0y16K2BBKss2ZGpUYjpWzz_0Ri26qLZ_4l5Cir0cWNp-i0wtdDYDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcKdy79ay_lt5iCgh8fwsbr-OUoMHaixyKWTZ7X_UG1GOX-otr5G_Iqt1CdJwtG6Eb788ekYON4r5pwfCNuGMfEkP0jkCICXqnDls3JqbuMt3PJ-vzhNOCRmzKfWuFtvDe3kY0kA2Eqr7iBbshpPocHvfPdnKWd8-QqNC9kyuz7p_FT-rlFy0GBt-uDaTS3FMR804xdlaLGAcoVwkond_mE3Ab-qbRCP2CJ6O7jpGzXY8Zv15DS8PU0m8VDehhdzK6sQLabD5qPkQjuluMqHJQ9KPeqTBscV7FDwJk1YrgRz401v-adqIqdZQSiXi23Cd3Qehmzd8E9tmcww808n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBU4Uxy9DIC25mKL18msADz9n0dkwjeoKExqM4ODs9BbjIGcQZ2oa7QUlYhW0zR6X-EQz-2LVc7E3tfY70uGKPilwATHO9NYJf0xBfMh7QcFxpzOvNxJOFvdCQWqgq4t7DMQOq65lKE58M2ndSx-1d5ulUFdD1W-V6dwZ9ejc3R3yjv9QxT5shmjiI7IdazYVvu5TyqTWBreUUypxexWd900O61RDhIBM8Y7R3rfHPUtmOtzZOqHKciz9dct-afS4ndq2b5jqHXbdEg4iWrlBZ_N5LVtJztMfRbsxw0u7x-1FQsOalJ0h80S_sko9FlOCwgdR7cBp6pNjmchj7pC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWbbAAm8wfdVNkYkMOQuzvfbfO_KHif1BF0NhtXXQ4OMoHXZ3a2oalFwOHSSOAqHzKIthScxv-cB81fQUh9LtZdPS6KJpP5wRyaEGlVH8bgr4BS7lk8I4J5HsCPOX197jaXRQWt7P89AVR3SK-wOqkpKFTvb48WhSh4WoOT2quxOI65ytvR_CB0xbR85UpLLp1vg77GMEEdH02J0RbJvMb77FD3fePhMVZJHEVVP3rQbrSJRfbCFEWJ0y0kfyGal1amyGb_jC1ikGoXGti1fFMtf1EJARPd0Cv5b3TWUXS7WyKlg-WKtYp4N3sdsHUCyCThfG7V-a0ouNN3p1jHnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT7YmNEVa8Q8ErRLNRShCHmtL2PsMq8QC6UNAqDLXns9ECHkUHcAkH9PZ7HWbPAPxOJpCg92VbXd6DlYfExJXuNnJV7Hff9P0LhzyKBSuq8gYKsE18s-foywEOBDd7OcZNBj-JyUyR3e2l-HW1oRKEGpDYMfBO_ejnPV1mY1KSpjt7KMOnHlJ1e_q7JEsz_d-eilXFH1bGP2g7vbiNg4iCJWKDQLj8E_0IeNrf9De-ZAUfKD80KMjrBj_i0PttEeRpmBI8kbSMafdr_6o0Yi9n6tRAlBq_aAqwi3THvke9a-DMuKsLGND4vB1AciVcrcMCm0GlPpoucgi4BYZGuvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzkgp7FPRnAgJk-beuBZtfDqlBVbdbV_784DsFhMcn_RUS9ctn12uyGh_0nW313l5DLRSDwAYEZ5ZQt5RpQZ7EenGPjo_zFY3iDsi18xE8P8yYhJbuzS7mMzlmnY9NZmBAmMXDXmIhX5ZKmbtmkjW4B8nuDkY4scp3HUumA3-RIfvyfVvw1C9O1Bt8IGiW3VBjVdPV41cFD-XN9dJodSxc8sQk6wLdo0XMmX7bzKQqZ1LwZk8GA0NY3fKkdkNTUusiwviUlQpetTzbWD_WS715wULGmcR0_vcoj_H_Ffzi5E6LRbg0tgmCY5IS4f7Od3r30IwqZemdbGxh8hd6R5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOrbcE2Oq2aWw02JuIV1_1jWm0lP8s3HdEFaNqsD_BvW31nLaVD3c33xCkQCKubkBfvLddfyXOKXT3wG5IiIPK7GI9E_UTwh6ExJGW669mtk7af4EnRDp4mGa81KTluHAKooOzy6qdNgwUcYJ57X6JWmM8Lo76kfaW2YU0V4PrNyu37qwjj7ZkPvW3VEXpxjm5XfZvNeK7tNYWjEyFtrnp5fxLI1hC-D3zvfRXBdqWKLDaMO1EaQ9I3eUAvcEYAM9s1EVEWFiKc19Z0ZY3gxiEz4UQnbJM8-X1kAI5aacEkWAErEw5ZtmucHlfQLvQQZHXmxccl5ah2Z2wYkfMF6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNGvx2n1VmlkLs6_pz92NQuvWnR6XfLLOg4nCU_l4ERPgAc9AH4HlqgqlUn49-SvoGRKouSA_tF75D2qyKbKj_6QGf5fE2E5NqdSzaq56gJWSwm4BcEsP9vsv6vXjk1iP_7mWBTCVy7pZz-_tcKA1nMBrgr-KIQIPgocNdG8MUP0N5iqPWX7NbTYFpgmrqHXWmjV628Yg2SBcCRkJqG-ihf1OLIV1S0rNsrd5G2Sl_4CRtjafy1xsxIbrhwrxIlqizCzuqy9CwU7LWB08NDOdIMtdxnkwC3XeS9Ke5AyWHwlMyIia9FeOhdVrN9TrkMrXKv_SZ8tVvQZXsYZ4dqC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epeGjocjpzxL8sLdmCn2Rmb5CarXjE2hec32P5VBX9bfogVtywGH0M8aD0-N8d-2LmcNt8DMEy0SFl3p9zGrOcKaDEgmlITlA7tp1xm3ZvKNIdA6KDaeaZP-y2wMBLnBOEeqm096ZlnRO3BSqiq7BJXFuNhVutoSVECKyHLcI6xDD8m0PukNGx95XKP6kPb5gCgtnss7v_GqVAJhguQaan1UGtn609kSBTnLdkj2D1YvQ321RUjoswpdmmZWiBerTDdFbqEzFdvmEORXVjfxVNzcWXQtShXdFFOHgmiIZb6mY-u1Gp6Wu8GSGyF92EB97-GHiB9_cGAu6UrzvIM0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smjOVdB4Lm2LAKR3rtp8D71r3TjepugzeFTF3_YGar8OOQZzqikIVbvRfZKIpx8nvfLRAXUR5g-btRvEuxtdm4ungXYCQ5Csf0kv8n0DDLryuSOvXlBkBricVgsD8eh4rnl5OkDet9SlJ7es6_-g2VQY3pb7UI6fDjCQcHh_6d44SkHgjc0P5cEp5JPZD0vfRH_hxSeCka3p4fXQgAJ_kpdjaLR6tz-oZj6Kc4VIwe-oIgTdGBoJJZf5EhCMwoDj2HSM-iPc4y5ftX0E3SZTmXZMh0vR0QDNCkFibJSAn2woSXvkv2vjHEJFcc05Zy_4tW-G_xKMFMdXtFaspBWucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Drake
📌
Ice Man
📌
Habibti
📌
Made Of Honour
📌
$
ome $exy $ongs 4 U
📌
For All The Dogs Scary Hours Edition
📌
For All The Dogs
📌
Her Loss
📌
Honestly Nevermind
📌
Certified Lover Boy
📌
Dark Lane Demo Tapes
📌
Care Package
📌
Scorpion
📌
More Life
📌
Views
📌
What A Time To Be Alive
📌
If You’re Reading This It’s Too Late
📌
Nothing Was The Same
📌
Nothing Was The Same (Deluxe)
📌
Take Care (Deluxe)
📌
Thank Me Later
📌
So Far Gone
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZrpZ2t9yuzAiEbRQ85xMRDmJJUPh4jYzn8YDzgHBq0VTgumo79OWZy6lpj4wtFn69GOxmcmxBVMC_TmQQTxVOiHfQhug7N5_vUH0NJIlrOr_OQQlOe1qj-dNTKnkqtpFT9PeK0LLQVEP3o9W1LQBWjtVlRX6jCT08XZCIx91lTD4u-G4wsK36Q4LWXnIWFL4iPXJzfrK7zS4rEw3VXUdYUkPLV8iFzFjzlPYz-8lnjNVUE_25rAYkENRIJIyNRaQ_PNNlMbKHccd6L2HYWsEwqhgUMuQiELs-c_HNCFcdpmK0xGcI3XfKrGNw5crxCFIFIhM9JV9UEn0Rx8gMck-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG1ED-LABrlt3kKqq8tnSmXjhvTEgxXIA62uoWQ8KKgYDBY2cD_7PCDIRKhkP3qAswKHIJwrsl0oMD3QDWh_w1IZszT1i8k6YSqhUwsUb4ya25p3q5AMtJM1wWMv-FimclGfTmavxbtLjKTfLmQwbnZB5F5i28yD5xkg_ZXJwGgMEHBPs7RGQaGwF7yxDtSypDYqEO3njbae6lkEwNgx9KyUHgeXl05KGh-sk-o9nmsRjZKDy4pcV-6gpy6d23JEZxd5Kod4CtVA1HXmwuC8YwANgHhjeTOdM17UxrAwNx9tdIWgu_WPjZ3-iN82z5jTrYC16C27QQzVZK-RXRNsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYUZkewcCa7yDAB4MtgBYWwcYwNEiOlowLQVmWBjxP7uZIkwTpyl-AgFcNpgfYPdPqVWC4fmO4tRT2dUTRbhm7bHDBn3R_COA_w5wAR2oSKjfngYV_eyzuMnyWxS1oE7ysw5CApoLmOTuDSdQ2Pnyyo7BUSn4pm922iPApfCSbg_aO-U2pM6GOVjbO0WNIH5RMuwY4Xqlcpp5RcXloZGtqLIPOy5tc7S0oTwPxIqUbV9wkR1KKPKjYwEcWFuFSWOnKFNk_XRRuArj1b59DGXEHb_4j8k7EUqXH-EHQKoWZ93r5_l7W4kQqUct5RpFlu_5dqS6oPdsX-GaUSReOiCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqnnpDymq0DY5QbqMmap5zSKbB1AIrMpsqy7piOlQ2uMgG8xl4AdTxyjqRzyUH80wxEXzzNL7J5SiywqV8EnkiLmJzTVv6YExCwO_KX3MlyyoZ1ZRO3uUD10437dBHxK7qHcHt7nORvfS3hqZGzIQCOeAb_XcrKXf0WEWgTS_pUcix6cBdIpd5hQgnngfi2Qi4_Vg2c2QWN79-xw3QIpxzOOvWDz1SDQAevaKKkWgkZOnTlneDx7Nx0ftcXThJ2QGBrMaoJgP5VkMiRHwR2xQqEZoLORgd5MLTDA6na0Gdx-3e8QrO2d2vDir0hBbc6jICWCbvjPLfqwnG2e0iV-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=VSihHaY7FkDAZ8knRVG5meKxu5JX7bD89tAqOSk9pCWKxCnS2By-oE7nToHTo5Ne4H_gnbtMNpfk1uZbjk6zqKpSJFLwFemXH_SUvFMuq-WBeujnSf3jHcZf53ugbpvOZdRkbFs7ns2wQf3J67pcGWQRKj91imRdR8LNUZ-ZERz0ZY55uaTAQFmvFzaRzfj5fwxJAY7y3o7cTg5xrcP90j-PPbOdJYyixavUIcFJn8BCZlK1GNFDI5Y86aDXa6zoJxYucteRYOp1-E5fSxkx3pu7T6ZKeb5nRD1PqrZw5AEbMfbyawNpbNeyC2tCl8-7OgG9vJrj4QuFFeMDJ4Vhhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=VSihHaY7FkDAZ8knRVG5meKxu5JX7bD89tAqOSk9pCWKxCnS2By-oE7nToHTo5Ne4H_gnbtMNpfk1uZbjk6zqKpSJFLwFemXH_SUvFMuq-WBeujnSf3jHcZf53ugbpvOZdRkbFs7ns2wQf3J67pcGWQRKj91imRdR8LNUZ-ZERz0ZY55uaTAQFmvFzaRzfj5fwxJAY7y3o7cTg5xrcP90j-PPbOdJYyixavUIcFJn8BCZlK1GNFDI5Y86aDXa6zoJxYucteRYOp1-E5fSxkx3pu7T6ZKeb5nRD1PqrZw5AEbMfbyawNpbNeyC2tCl8-7OgG9vJrj4QuFFeMDJ4Vhhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
