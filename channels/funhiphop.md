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
<img src="https://cdn4.telesco.pe/file/nKaNqi6iKzOnoDu8z0qGSclrV0Q2_Naw51JvZEHTAtCZNDndLs_yPYvh5v6JA1TRE_3WRjj9DsZk7kTK1oLmjG5c1IzKm4F0ldIFn6hP--yUwG_MtVPysqgdWDODXgk_XEVbjEtoZIoKdotRAymdaEIy7iZHSixW3omNEuIwt-OQ6_10AfNX-rnSs4Ttn4Ki4UsQeRxYTtpvWJH6_NyFP-yshkrK4aKoMnoT5lmcU1dPnXTEzDvX3mOALSye-N3wmwn3aF9WsptL9KyxTnHNebzcwIcRzuJ4nQ4n3KvLL1ina76Cx7ec0RDfASs1i7gfGYA3c16vV_Ae4OYqbcF8qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCcAwtlZDXEb25ZYi8kTEn28aL21LFX6oIp-zDJS16EqT84CSFVDdXWkrdC3S6s1Zljar3osDnXbI300ArJgmKAVhYegQTFS5rgCoNfVww4klDLiF6ompHaEabNuTqoHzMBHy1TZ2J9VyFyccC7RtsyHyueNCKdCXdzR6R7JNkZQIo1X1p9cwyc-l4brGoIfQK6Wn42iTbdJr3sRN-cUvJJiP3Z0i8tF_tYQrwe8dllqdQCIsZlIhiVfYjeD5smAvx9AWKIiRGs9bVnJqc722TfXJCsXNHDhovCwr0aIvmIRcwp2RTUx93Fq6dK9J-_OTa5aOsxKD_8wZONo-wq4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b62fc504a.mp4?token=kYiDH0j1jaKyV6dS5BgdxQUcCq2O9Ct6w26T0YWB6Gnd8VW01AjJT55TFgkZJ51spwLuPfbW0BbGO1FrI3Koi4NziEm4dGl4ZXhHIkeucKTwCgF5WM01HHLp10R0hakdUBBqOlV44cOTC1MHQI-lnymcHD04M0GCgArrxYaSKhDV33ngaCWv3HQOlvPftaWrK08S0955Sn7A6dcf1BJBJDnJ8-G4KC8zoEX45gyujN7ACiE7QHRElKDv1XP8RzxevZs-ckdg1WPapUTKYbtGC0y0bocc2hjAhfNVJKuWC61os8SFpiQp8NKDJBHbTIwvnu7bBpKea8PE2J9hY6LMrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b62fc504a.mp4?token=kYiDH0j1jaKyV6dS5BgdxQUcCq2O9Ct6w26T0YWB6Gnd8VW01AjJT55TFgkZJ51spwLuPfbW0BbGO1FrI3Koi4NziEm4dGl4ZXhHIkeucKTwCgF5WM01HHLp10R0hakdUBBqOlV44cOTC1MHQI-lnymcHD04M0GCgArrxYaSKhDV33ngaCWv3HQOlvPftaWrK08S0955Sn7A6dcf1BJBJDnJ8-G4KC8zoEX45gyujN7ACiE7QHRElKDv1XP8RzxevZs-ckdg1WPapUTKYbtGC0y0bocc2hjAhfNVJKuWC61os8SFpiQp8NKDJBHbTIwvnu7bBpKea8PE2J9hY6LMrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مصاحبه با نیویورک پست : فک‌ میکنم مجبتی همجنسگرات و احترام براش قائلم
مجری؟ آیا مجتبی خامنه‌ای همجنسگراست؟
ترامپ: آره فکر کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/76781" target="_blank">📅 19:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4v8lYZa4KKGRE66YqhhYmvg9nDVIv1W6BN1OWIYrl7d-AZq6-kRMLC5qz2Xv_rnPNbS7zGW9ijyqftIjIC0l-Mw5w7ZtiXtqCnZF3crkpjcqxn6atDMSPIDuYd2fvZLQudOCmrLzfdwDgPXUTZO8AZeqfBLIKVzLre5AhcZGqftxJvQCCre8Xv151f7KRGoAK6g47oD3KewE75kO1xifda631N5aXlLsFKAsjCMkhEIe3S-QpBNcMw7APlYktk30XI11KTFVpMFsSpdSwBblLHMouhIxWHwOH6hNOYATtECyURY02pd_yxHD4907fYNhYgolh20V7MuJNreNFAgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG_jR0b_76F_dbR3eRiLwv7FBoBcO3FTUUofqfP3lbv6biBxV67fTeTIqeaGvxnxBTm1Hc2MOp24RIZj9ZDVeG7K-K0B5B0FwPWqyB7jzLdIaWYDpPgcy77WsuD-M18di-MIsNMGJC0UKVKrc8WsNzwbKGM5lBQhJ9mDstr5kOYPnltFGfFQ-g3GVkfBUDz6oyPfeeppdyuak7h10cJoevBxOOozh7X4qbPJNwBcACu6I8Y0qUcJ18FKdKhqG1BfWiz2HKWkIhnPPcWWUT7cdYb1YYHfSOeHljVaC23Q6s_OhOBKGHKr6WfxDAZE2AnZxoTfTI7SsAfY31XgpjvKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g13
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/76760" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=pXCh1Ngeo1AgC7WR7-J2yTsuuIf8ruUHdsglYxqpoKExuJwy5Ewl5WCjM0n26sWQ_QdqjywEDDc8KScQIYK-Q-2TtYBie9Xf2FvMyrjmCDI61ihqUvuPobiJ4OArB5AxVzZxCZr7eEjMNHV6_Q9r7UKUQCodt_yozjRJONGvhERBNyYgHWyHVuICT7tDeFdfv-YWTE1xvMg6D0ob7nsRmSDUhus7FXUrzBIwz7pew1YPaf19pWDQg2g7jK8HvF2okJ2R854ISRQRd13dS2ZA6we4X2ocOmZyPrldlIK4zAO1xpdptrssYY5twH8y5q_Ie3An0cDf10z5FMWGgOSlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=pXCh1Ngeo1AgC7WR7-J2yTsuuIf8ruUHdsglYxqpoKExuJwy5Ewl5WCjM0n26sWQ_QdqjywEDDc8KScQIYK-Q-2TtYBie9Xf2FvMyrjmCDI61ihqUvuPobiJ4OArB5AxVzZxCZr7eEjMNHV6_Q9r7UKUQCodt_yozjRJONGvhERBNyYgHWyHVuICT7tDeFdfv-YWTE1xvMg6D0ob7nsRmSDUhus7FXUrzBIwz7pew1YPaf19pWDQg2g7jK8HvF2okJ2R854ISRQRd13dS2ZA6we4X2ocOmZyPrldlIK4zAO1xpdptrssYY5twH8y5q_Ie3An0cDf10z5FMWGgOSlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKEf9aKJSrL_pCq1KMsVDUAjPAHczEU0QrrQfBKKUMAhE3JtC8W-6bidAvJnvlo1UBqP1sek7HIJY-WvJSoivXrnEakhizTlzlROgDE3QEpex7DaWx9J8A8zU-fnktbxG_rVROou3LACmF2G-tovhFAJ-RJokq71gDS2yKkoWFRMkjPFbVDPFdtImC_UwE87Z3-WD0TxR1bQXAvxEhlF6pg7_50a0yH3YNoR-5YUgxxiACED2MbPYLtJ4-eBS1d1AWEh4cLjG2MJRPUkFUrA3JBAkNBsik7DFMEYTmnl5WgA_21u4mqa-bG156hUNesAEL33zQnjkz36F2s4zeKriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sioh7jkurRxmT4YxByi0NxvZXT14QZ0dWK12yBOX4-sqiIEkMy4bU0TViA-yZSMU7l1xAXKhH9snvZBDBMIcb2Lk2TcNfGRi1--GelSjP3QgUxgWJXysQDEnR6qLZpVAi8hbftUWraZg80oQ4iz1hChltthOerCCR7o-TPTkOcx5HYw8FfZyeJOXYw5tYRXjJF-TfCy_qRXJHqzaTy-C1is0oIclv2SJwRNgbRxVX92NccyGDHBT2S7FwvMHBWlUvIPQqzBL-jNdhu63SRXFwgeTEwV7GyN8F3otAUgVHuvw4aem3WvhcLOslKrBeI6FLBXqRn3umM57z3hrwuxC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C16r9eSM0ytRmiwGpKpBa2oja71NwbWceJ9UpZsu6Q4gAj4MXpuhYTLKDtfJE0HFbrMBVCTT-dleFK47S0mWgTQDmrjnA-0XNECIJFHdLa4_nEBphEpuqTawCyh3ZS4aaWtfsS1av56ojtCJucz-6ZY0OxOqL9VtZB_baq1p1vgvL-PxGlDbYniVQPB4lF22KiF1j2E8LmgLsOp5UoKJ4PDM6VLmQe4Jcf552W0nAMVEqfhtX3VY24KE8RSVg297gaM1Y5z7AlbWG1M-VLJrYbYkKkcWwfsiYoeWEnLKCnEgnW6HsekH1Gz1e9zlDDUooQ29ka2nw9c8w_PV-zywLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZQd8iHkeE7fyF_SaQyw-5ixOxdXYfHEOPHnfnGD0faM8H6XDFuyxdIyGsC3wGEwyb5hsl16RkwkztO0CB5uNuKQXv7pPjjrSo-Ty6X8nT986r5YaGA__Ilw3XXeRGhUUAuqdXecGPe1JxSkUf1DRLpaR5zYQEQ8KAaMX8FcqBEH1aU4uktYo7msb6FSKUl8TLMJF2pMfLqTkwU2QQkau-3EuxVGVUf0W7gtNzkn2i1073h_-ye87zJ9cxN65n3ELC-yk1n8MhMT7DxOFoHvfS2vPtQqcvlSb6SK1nelFattirr2GiH2s75LNR6-eLqu1DF_dbpzXn6qhLH9Y8moeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVRercLgqh_3oh96m8hrdfzyIHC6KCIBT2_huj_mWf4oe-KdhEm6jSwyf5HJS8u0DqISuXieZrc9jWcGz9IeQOFQD5CuPCTFuJBiQOGlXQQlSDlcQIUwJ8sqUEMnfm4c7gWtRL3WBM2Ou61iiFo7yXtWjwOLp5lffxV2ctQuvAsN1jk3NwKY0ehW4mFEKRHIh8_8iWYXJnsVui8EXDu7BL37_qsZp0DFfZeJAhFrQSiiAfJkmqPyvM9y7j1OicIOankMRyUNvl2LSq4hM0vmLohK9Yh6MtUnqkaQ-KYguXxtRiRCBJA3NYhJOcrsVJn0EKR7LQohG4or79aTTI7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=K9zh6A8nuInUYwx9bB7EMarkbz4f-HKcyaVJ9cdNU6FtUC7ou8I_Y29NLeKY4mLGNe-C_PeTPj3RJrIZTQQivUywI9YVUz5uyiKLB0bfHT_huTB5_L10qO6cHMIPWQYu0ybLbMI6O8ihV0-UY28lV5ci-Ydbo-JuCFCw4v5X2qNiAW35LkR5_3onlxvh_Ey0hX9_5L2CJTpH291V41NIEtbaSunFLbg8FY4Zdy9yUvtifpoJFYIGkrt-a-N__n8qnJUP78eLJmlx2hjFi3UtsRxCx0LucZu9XyVURa2zOgFNLlVlKryc7QSiuEpNoDfToh7Zjq11t-ML3RjXhExFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=K9zh6A8nuInUYwx9bB7EMarkbz4f-HKcyaVJ9cdNU6FtUC7ou8I_Y29NLeKY4mLGNe-C_PeTPj3RJrIZTQQivUywI9YVUz5uyiKLB0bfHT_huTB5_L10qO6cHMIPWQYu0ybLbMI6O8ihV0-UY28lV5ci-Ydbo-JuCFCw4v5X2qNiAW35LkR5_3onlxvh_Ey0hX9_5L2CJTpH291V41NIEtbaSunFLbg8FY4Zdy9yUvtifpoJFYIGkrt-a-N__n8qnJUP78eLJmlx2hjFi3UtsRxCx0LucZu9XyVURa2zOgFNLlVlKryc7QSiuEpNoDfToh7Zjq11t-ML3RjXhExFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbQXPAtth0a2cMluLhyQrE5s7nI0gHj9-enF1yP5BwxhJNqldrWMeqk5akd8skQvT5yUjW3P0Yoj6iTKvAs6F-o3Fov02-hxPNPfZ5yXBHmfAIiTbapNyqBe9TCpBRNQ4O0OKcjsbM8O_8-OuvRlZyFKeiU10bc5u1MpqVqb56FkkvFnLq209DS4807_PwZk8A1q6KkAdCY3N3ufpdPVuImutj8dhATOOXQYesUJWqjsuyvqRla5osIbaein8Ja206y_wRinGmoaFWVb-Q1pbEhT48Ph9uHDYVHeffwCP4J386YqIeZPBdBwTc638-29I2EQYxH03RLjiZ2jdIsxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=D3qg-OdeQHvNwtIL8PNpFqzgxmXL54sNeg0vBRn_592dyuTNF44kbvDiDGydk3YZRfMY9Kqeg1rbl9wqliTPtwUydBdvgn3iOkzv-wQBOeZMxz2QhVGkh2aZyj8SeO8WO7PbFx4rz9Er34cGmGGpGd02x8pSwj_DT9rHIXz-OuJwVBZlrUdXgYzH3bXtIdxusQXyDtD9T3-SaHq4KpVN_ocv6DZeePXxHpdHua12c_MLxKqLln6BpEbukMlLAM8Eap2Yd2YTbBuH4pN26krOAtbktbiDyaWcXMQKE_QdQz1odSkUGUR6gUuOfenBMv99O-g5c1bELWkmYsoShKAVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=D3qg-OdeQHvNwtIL8PNpFqzgxmXL54sNeg0vBRn_592dyuTNF44kbvDiDGydk3YZRfMY9Kqeg1rbl9wqliTPtwUydBdvgn3iOkzv-wQBOeZMxz2QhVGkh2aZyj8SeO8WO7PbFx4rz9Er34cGmGGpGd02x8pSwj_DT9rHIXz-OuJwVBZlrUdXgYzH3bXtIdxusQXyDtD9T3-SaHq4KpVN_ocv6DZeePXxHpdHua12c_MLxKqLln6BpEbukMlLAM8Eap2Yd2YTbBuH4pN26krOAtbktbiDyaWcXMQKE_QdQz1odSkUGUR6gUuOfenBMv99O-g5c1bELWkmYsoShKAVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIxkxx8IpL3PjBtBFCZDQf_zLqosBYJ0VFxPpk30I8seR0Zlzy66wJZC7u89Emxp_7F3tLnA-pKMELQwAmFidwdDRBYKM-7JPMz54Jcen_jSj7G0vmSwbOP0GGX6aEXbVeR4Sim4jMkRl1nI_Kc3JyeqKlvPWF_Dl049DTCMOA5fY3QOKez3vyqZyb9TEFpm6P8NcsspBKiNktYYca3bIja-zjhNhX0jVugMVFNPNiSl1BXzqCaCA1uNoKNtGoY5OHl726Ukkr8bgHxLFStqffb-wQ4Apc0DzyvH77cMg0LhbrF9BDYHV41naCZRcUGdCHdkdGXAi3YJCZ_5BObNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYycaHPL6b3hHYtq4i5_2pNOPtgegBcp2vfRhuyDt7vOFE3egr_NIMNch9-iDgY0uR4wDMZ1Ht8-k7aaw2W26iCxQo3lu6wiavuhhwES-TMqSAEA4ZgKTlAk1EDzDdAVZfePvXD-QN354Y4SD4XsGG9ToGfekhKxtRHD_OhtvLUfeDmmCmxZ2x7bbgpBS8-1F3y30XtICFak6XfAlA2cPL9tEJ1oBhnIFt1yZInOYYdRbnrCxhNLXViewSkkA-8fEIfBmB3GTv018iv0OevfUaMM6gD44XZR7wPXP7QSEF_dXygGS7HwbofglRpZF_PR6etYI7tnzB8aJEsGt1I1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d668TStIanS87hRXOFmBZVLvtt7P4EJl__LMb9OyG9N-J0Hc4Xn_ZrmWYqmLPN4uHo91iHepwA7Ojoc1cP9vLqoS-LicyxBQylK1p4nR6kWCPvNMA6ZL18kbR2KOTLvEF5vNzohrA24FcNOBEKYllIHQA3TWHlK5TqN14pBZ2PKM7wKLAq8enbzDUn0oTTwurZyzC80ti3X5TjIZOGhScYbBqM00D6ZBz_P7Iv886e2centWX18zlNHQr2fQTsMUOAQEssJv8bF7_P0lDNFMBG7v0Q6gIHtYKLAzxd62psIGKG2vAekNhFFIfMm9sFgt17MB9gOTEWUH9Gi5USUesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5lX-ykrjwmfnk-yD2woYEYZNvXV-6D6NUxUpVW5Nv534salqMEZi6lJrZy3LrtEEqmg3pYfIrHhIE4XsGrR2pG2NdbG1rl-KZfpkK1gn8tQNsNIShXVFbERteLxNSncN6Pk1nqmoC3YJ7cH5CSU16NpE4FRZ3ojt3hxS1ZNzOowafnaJnHA0nTTP8kfGjhgB8mSxocY9CuzbQCyHdVwDM0f3S75mwyiZarq5ddS1GBkI_fV_ratY5AeRMK1yUZf0KwZfiOWTTPamPWHpNmiGoTMS7OdUnLDtL75EnP3fvPuGM61rWHGbUE1X2-tR0E2zQyyJOAKT-Ig9sykkz1tUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxGWzXKBANcGY6pLCR_0QrYSG5RWtIlGlJvvTZ7VpQjLNfOS9AvFINT-fPWM3nGoOA6OBSKmZfGnHlIMOULYQ5FyN0d_fW3J4_-z0EUMIssmRKtwyj4PEEYGlxXEEEvopE26_uWzvtFtwlRNFNiaGt2MLlegqseqSF6bXVbNX1YHAHVgDnYljwb2RnvFsUA6UIPkciwkAvE4SxNNyDQxo2FVUWi5qO0sEnK4ZiQC9GoPtiZEBNicQTjfrZ356E_tK7YrH7KlBrjYSPGCqsfSjl9rIstBrO96i48Dmp0KKi07yyi6eUWrw1w_20PP_d_8HlZOjDIA9QZLmA7uTN5qow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XEhbZx66FrJl8BvPrjwIIDBgEgv9GgSsHevoR9koyieTKrLarvkWL41MAaPyVhbivacbmC7zhLmoE1V7w77IH06RZow1CeIkmG9eNSaFg_xxV8JOE4d0MA_B5KaEXSi1e7GxdjbAysiCxuX2Oi8NGCXcZjh7r-pIOYa-dx0cCBjw3MRyuHUvE9Ec0TUFzjjo2Yiltg6nFR21km5ve65LEvcEb9CozFRubikK32Ghc3WmH-j-0XYL7GC3PzrkzK7MUL6Z9B2Za7bjzhIJI0Q242x_X-OriOWxwv-cQ6Q6Rl4cso4iS_rNBKzlAgt83SmPKs58-M81QV6LurOL37NeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEzGLu82eEcv_5sPB_ytoDTHilJpw_xqp0tptGkVLRNHvuGLBsyuMLCT-ilgkKcqflNUd5zX_uzm0i72FhjGK_U9SxtobWljNW2XyJVGHFfkrNly4YTkzrsndIBEkvfXdp4kwiMebe-nXM8dU81hvfGMm1ZU33FHVVMpcSTKXPITflRkzA5j6ubaj3UTum2rjlnwA4rjajV7um18Bkh1KUQN-yc25ysbDOaEhTSuZZBdjlEQj5Z0-ctmPiywxf3M0IkePKZ7HC8OcCoYCke7O4INkkYXjA9QEVQypJ7iWVNUtj4r7vV-Xe6B4IZllJ1-wwwCETVlvL5LD9NzR23h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76718" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76718" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWhcFYiFO_f2gfUoGJu1VS0slJx4J8SZAA6FUcA-qVGXsiGCxsCJ-JaRLZb-LohSAzq5IT0uBwwcWw4oh3H-QNntwMehM5KAIA6jKp8BobHE7xfaFyIPOfv5TQPenXa7NYA2j_-nShhysE4Th9OSpNIpgGpW6jdJc92udMx_7Q37suBdFaWaH7Fh8zH17jLF-35JSmFaRPpB2c5VMs6ghIoJalgEFFl8JF5lOYMQ7P1lSDRM-o-YnbUAZe77eiV3A4bioaZC8kRszK4UiLJeFEZPfCVXIZCJ36MEfmti-mYPg3zGISEllTIgx6kM_abE-I759fWdTTJs-IUtKEjUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r13
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76717" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوبی رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76710" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عربستان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76708" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCmN2H492qLoaUojpuyQFHvbxIMINEBcnAGvglOP9qCrF1bbfZxlmqgmVzURyIV3d7e8J2wPXToAoBMLDEmz6cw-G95BEULrz0LBiSlDkqooFMjErq8htHs-vhDd-Yps_daK1ik1W0a3Zm2slrb_hQLkBM94WCheCvd8Y40RMnex_nfQK0mPNPJW8kDDl_RY8u3foQTUwzzOFNJZ2l4zvbnIzZz2IYfDKD8Cyr_oe6-Jp2yWTERW-I39-8ZFTQPJ_XAOfNz_A36DoFrxQnguRSrTQN4KsmFEk5angJdfMyUGgH3h49wLTtqe5ty7v79xWueaRSyNEEIG3wRfgCfy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3wYnquG6o7ywszSsZ5vs7JBiQbLkJr0ljxWhdR4qkgpQ_SDT9BHWhP_3WgMzfkOfodVkHIzGJrHkSENaRU0gAP61yPTtZrkYKJESh5tFDzX-i92Wz9aZ0aWohygsva9X4T4XAPzuWZ2uEK_5yevNlaYo2hIW23n3HR2BwYVqoLKiH9f_mH5Q9WkLWulMzoLa3gACNkX3yTGzN_7edKL1FyB5bjWWDYGIOnDai2uYaV0ykF-M2_oI0F255l3wG1kuMoYNDkMEZ1aGDQICdMXehWLtyQATiA2f18q1dvD8wEQTf7qKPyuW6OoziXEV4lL93o9rd03ogAqRTn2YZ3pWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خیلی ساده‌اس ما الان میدونیم که ویناک و حصین میمالیدن و دیگه نمالیدن
ولی مثلا دکی چی
کلا نمیمالیده
یا هنوزم داره میماله که چیزی راجبش نمیگن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76693" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از نظر ویناک هرکی نگه جاویدشاه پشت مردم نیست و خایه مال سپاهه، عالیه وضعیت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76691" target="_blank">📅 23:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شوک قلبی به حصین:
وزارت خزانه‌داری آمریکا چهار صرافی ایرانیِ نوبيتكس، بيت پین، رمزینکس و والكس رو تحریم کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb13jhsvHqKiWaUVM7f67Hithd3ix9LV3unKgt1vNp740kiHYSfhr5POIEdppnGmGlxsGEAFJQr2wRvc5n6jmWD8IIK4ZQx202GiZy8-u6QTEpV_uwD-7yt94gVTyqKtW6yamykYpAY_s_sG6L5S3tGvfP9voq5fekxNtOiLN_OM3ySWvDdqc4NYdjGB_7YdGrLr_TGcOKB05H2Qh7NuyBV8NeiOL8UVplBmIDp3V_W_E8KVlE7qUro9N86EgpUK5JR7GTlPxM5VUNvyEWvyCN7UbhOzqBQyr0UsfysytMN7YeoDe1BNGxh8ZF5aMXrcZ80povzS0xYzaDa7ll5y5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1yYKuPZLIVSMRp5akE9ys8DYh8kfvZmJJMYPAetRAXWsnfb2qzwmJ2El1k7vEJIFqr6m3JtQZM_pMRLjNT3SseVzERP8FL_uCpvEgJ1E7p8ViWtFe_9oDtgVhmTLR7esYgLuQ7iFkueJTJiTwcNuBp8TXxdOUcnCY-XfJ4bBBqu7VocKRuAFoxXaYs_lGlLyPuHWfA45Snwpuj5eMfN_kXPcKqysGXGktJbnzHRMEpRtoECcE2WqzkypjClz--RY0Pa1KL2MNqgSETLPziIHoAaGyv8wwIk-EgTNgSab5KpFp0ogR1JqQKgDlH6a8ULtUOJHv2mxmRyZCmgtVgaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INKRpD4UNK0B7eYlsgaPfVNqdo3aHmEdv8r1GICRaPPizmw8osWGSKdwPKIG6ziSYqv9lA0z5DRIgOiF0fQaIxxlxgOhZFHWor3r1NAY4NDDJvBP9msbFfiu0TC3HWR7VCKvfwBhkec800FM47NFMb_QOnVob6oaF3qIrzJdidPKvWy8dbtizzcE28rpOI_OmHQ1M5fTggcjDh_v1TCbPp-dFA9tjkX5BrVvHEeOoF96PF13B77rFrbzargJJyJCsdhH-Sbu-q82lZYWpuNoYsv8kMMztwC2j4uWfiWvM9DTe1Q94jCxPvxNjARu94T69_YwrIfyL7--vHBvjBlDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76684" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76683" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">رپفارسی دو بخش است
یه بخش مادرجنده
یه بخش خارکسه
یه فدایی ای هم این وسط هست که خداست</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76681" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMBhA3PFftTkZzT5Y_ztXXBB7Ru5w6xyJ9WGrS-CfbeNsEXhDyQbGOkwgJkU0cYPjR3tXft5A-nm4hYyOEetdVyg9TSO-CRr_-rlEr4tmIgqIxNu4RICIP5IVciZnoyB9oz8P3-ajgunctq6MCPkrhsC17M2C9hngK3A0UV4mqZvf8J-WG1R3JoaegAXOEg83ekijR9W-3NjC09OG7SuNszOkZp5NnIWd25A_CPNO3dQG3ie2ThUcynAKgh20nd-PHavO3RaPIajGRrTk8iaAm3nZZfwHHILB_kpuHkgGmMxAoW2KNGyA_XAhzchr7sSBfFVYhXdKrqaxOAihlkwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ویناک گرفت رو دکی و حصین و سپاه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76679" target="_blank">📅 23:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">چرا بی احترامی میکنی بی تربیت</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76678" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">من رپفارس رو دنبال نمیکنم اما ایشون دکتر چی هستن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76677" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=XLJQtgwp4UMASb9au0ko-EusZuZVR48uHatVUgx5LVlpVwvI1sV_PvSyhw7JPl_-vharO6_4q8eOkgWUg8SaM6NOnDhVPTE1LeSxVTk9Xr5CFoIzYAa8cLtGa4Em-jBNfeKryGHWBylN81W2qpgbdW1wzSzJOMc94UfjrRcakM4qtTo1koxLh4VpaYmuibppuzrZEXSNDeZZEIFRNs5qxbVyyLFT6rO5r-7dunm8WDy8Y2OSdH0J2Ac9SmWIvksraKG-WFbErrLc_R7w42QXkZj9b2HmdA9u61DWZxwG-zScWkvFhrZG0xIQnIkfIdbGKgKMm6gSox4Nl7olMjnJHkSLsujRz4artlwPlWReIZNhhNJ3yItMquiQk6JegoioOuesaKS6qLlKgwdiT2-FxSM8EjK7P0Dbpa4peI-ZJkJ8wUtEToFrGDBXShFHyH0Ybog7MT1UszEHd16Netw89G8gQkekEgcK9Cy02xscaGYmnAaA4AkHwto7yeWOLAWce5gxsMtTj3DeAU_qG0u5qOLeMh30e7j-sKjX22ElzLq6wVJReFXyVVC-dSA34u9-HmqQhqe1wHpjJrMFzM8OtGDhVDtsboqqwfdCKMQspKqSB7gtHf1N-pKyHhDuByrq3LX1vZwVwNXqQuJa4JLw_r1zLb5m5yICNS2hYR6CTio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=XLJQtgwp4UMASb9au0ko-EusZuZVR48uHatVUgx5LVlpVwvI1sV_PvSyhw7JPl_-vharO6_4q8eOkgWUg8SaM6NOnDhVPTE1LeSxVTk9Xr5CFoIzYAa8cLtGa4Em-jBNfeKryGHWBylN81W2qpgbdW1wzSzJOMc94UfjrRcakM4qtTo1koxLh4VpaYmuibppuzrZEXSNDeZZEIFRNs5qxbVyyLFT6rO5r-7dunm8WDy8Y2OSdH0J2Ac9SmWIvksraKG-WFbErrLc_R7w42QXkZj9b2HmdA9u61DWZxwG-zScWkvFhrZG0xIQnIkfIdbGKgKMm6gSox4Nl7olMjnJHkSLsujRz4artlwPlWReIZNhhNJ3yItMquiQk6JegoioOuesaKS6qLlKgwdiT2-FxSM8EjK7P0Dbpa4peI-ZJkJ8wUtEToFrGDBXShFHyH0Ybog7MT1UszEHd16Netw89G8gQkekEgcK9Cy02xscaGYmnAaA4AkHwto7yeWOLAWce5gxsMtTj3DeAU_qG0u5qOLeMh30e7j-sKjX22ElzLq6wVJReFXyVVC-dSA34u9-HmqQhqe1wHpjJrMFzM8OtGDhVDtsboqqwfdCKMQspKqSB7gtHf1N-pKyHhDuByrq3LX1vZwVwNXqQuJa4JLw_r1zLb5m5yICNS2hYR6CTio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید این بنده خدای مو نارنجی چی میگه من بلد نیستم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76675" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWzQQdnNLnL351cvqFaoCz-uR02dmpbKZ3ju-fzjvRv0abcWj5KgfkO3HhO-QG0zmI6m8N3f8qIbnPYBraDQzOeaEw9jrMopcKR33SDZyGl-cdvdELtdSFXArIIoRTzwBERvI0v4e_-iUtmohd0WuSgznvbfe2tRdDWNye3tzRl-gNR6afoOoO-X_zIygLMKhmumnX0_aMDm_ksgknT34AcWPoXa9qixxcjic-FnwpwB86pjXXxoo9KJiBW_icxvMJxopL8REpHK4EUyhD-28kUD3vkUocZ24Qp2jbo3ARUHUha7j1cpmM8xtbWo084TYE3KcEVitmsTKglg3kjabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاقیت در ملت شریف موج میزند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76674" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درگیری مرزی هندوستان با میانجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76673" target="_blank">📅 22:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tkfs9f8Cyrolpfz-NZaMTOiiouXwMx63057ofqIgGL7W2nPQEi02b05gCYjKiBcekH6yn0bmYiiAe1ZwLXBlQL5X0gDCAAOTtrcuL-o1doAWZyqD0e2j4bKKuNTbaVSYIXKtUPQYa-xw9mnAaGyEu8z6lug1eYIYTPcHOrWKlGNPLuH2IidK8BUR-hygdhe10_Wi2AO74qAHaEPA3fj0naD2mrZ-1GLkmDzX_ZeLWWtyTtvwxh87HeOOmbMJ_2VzxPdfzRby2hurGGYRThg0X7Bw0SRF6i4EbuqtRe6tgnJ0NevDYd074TdezBiTay_fSWyv2Hamn_DT1O-toORCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغ جدید نایک با حضور لبرون جیمز و G.O.A.T
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76669" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml-oZf6K3K_AKPkyrv3dZJOSIL3PAr_5DrU1TkSKzAEV7mu-e59AaFLD_XGTm63BwQUbMAATOSBw0GQbenRwszi6CH4-N6gB5-AKwOCsUqs6n7VwI1yp0KpQVDxOUy6YjH68KfS6ZHyqV75g1v4olw0WvFENIPzLXohsdLI2Bs2vm1ktgrdYiboKxNpLs_IO4Zib8cddWyNiSzymXXOkRNmseeXYI3BK-myOHPD5zupw7pJ54GoFJIkhQGQLFpDPE59CwOCYwNRp88mk5zJ-cvKXH49IwL6QrqMUe9RK1ZXHG-3K26qDcSJllVlAOlwX3BStODRnxZJ3UEFpf-rETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین خارکسه اس، ولی به تو هم نمیرسه کصشر بگی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76668" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76667" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱,۸۰۰ تومان
🚀
@suii_vpn
@suii_vpn</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76666" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Ah0EPmXb6joD8KvLlSYXmakhUPx74FatBB7J2JpDdUEWcflCBSw6wvcvX8iDjfuPRWo_19xhg1ihyWYOf658E32V2JIcFtEcbpxDfmjPY-LdzeBV4JjuZTa7sQliVxa31-M9Ard1d9sdvBSk-9G0G9s4aadFsDacxn4b1ZTSNj5hvpIkBGOqhbh8P6CCtf1xiBnB4YJPeeuY9tAwI1AiQ2fh4KA23A1F_WX-BJNS2TPEK7amBKFwznAwutsjKinpTRPUgVN43Qibys8C3iwXRXg1h5nL3mShI9W635sqG8Ez7IKTnoX8bIEPo5SVslzzxAVjAmZoeCCtOOEGRm1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ح   ز   :
این چیزایی که فارس و تسنیم می‌گن مذاکرات متوقف شده دورغه بابا.
این حرفا نیست که اصلا.
ما الان یه مذاکرات خیلی خفن با ایران داریم که خب البته نمی‌دونیم آخرش چی میشه ببینیم چی پیش میاد ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76665" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روبیو: شاید ظرف چندروز آینده خبری از توافق با ایران بشنویم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76664" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهوی جنایتکار در مراسم انتصاب رئیس جدید موساد:
رژیم ایران در نهایت از صفحه‌ی هستی پاک خواهد شد و و ما کمک خواهیم کرد تا این روند سرعت بگیرد.
در آن نقطه، این رژیم هرگز باز نخواهد گشت تا وجود ما را تهدید کند.
این دستور من است – و این مأموریت شماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76661" target="_blank">📅 18:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز در گزارشی افشا کرد، ارتش تروریست آمریکا برای هدایت پهپادها و کشتار مردم ایران، از شبکه استارلینک استفاده کرده‌است/ رسانه‌های خارجی مدت‌ها استارلینک را ابزاری برای دسترسی به اینترنت آزاد معرفی میکردند/ چند هزار دستگاه استارلینک توسط عوامل اسرائیل به ایران قاچاق شده بود که عمده‌ی‌ آن توسط دستگاه‌های امنیتی توقیف شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76660" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt49TMaOB3EzeSdOER8Yu-P6U2qD1sKsRCNnUd_4f8xgr6crXC2yDo7qnHjiV8CmUinVEGT0PkrzIkhlrAZ9AVsV6omyr53BZQxx6R79iv10jbg2loxI3y_hh01SnOcHla801CIp-xWIxaogCXcdYUagtWzgoeUIqWp7NVVmuCpGUMzcDYSOFbyMDj8YwcH82B56l5jdpzq1nWwL6r6hY0E3xz0I3gvWtcePmkdDHdZJzGnp0Ny-OISCYPkA0qxzwT1YfJt27XoNsfG9K6HH5XdQE4fPFAts4tBCpfYT14JzuDpwaATZ-6g0L6L9gQTDkHIH-qWVSVNaZx71_MGWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیشد
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76659" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlRF3tTMXokQkX5DH6mXilFHLDKYIQU1V0VdBCJvJ9uY0LL8We-BUPRF8Pq2NzRb8buoBajJEVHjgnzeEf5hg6SqmaYFWPMRZhuyi2VpRg7UdirRQRNpYb3xKK42tkxbewUFqIufGqZT2ATFAmnJ5p3QQCsNm07o-2mbaXrdz_-OWnEI9aQteB6rw0-C_V2ATCscAFK3Mq8owWWJjNwxLg1IhuckPkRJ4CMGQniVHGqhkSgQ__5bYioLngSyATnOY8e8XOjuZ4WvR7m7ViCJDlxz5VO1ZSt2OhUxilCNO5pv-m4szpEawzN7sIOy2mJybpRgAC2npZFJimukdGXRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g12
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/76658" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رومانو:
کوناته به رئال مادرید
هیر وی گو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76657" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دور چهارم مذاکرات اسرائیل و لبنان توی واشنگتن در حال برگزاری هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76656" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون شهردار تهران:
برای تشییع جنازه سید علی خامنه ای ۳ روز مراسم بدرقه در قم، مشهد و تهران برگزار خواهد شد
آمادگی حضور ۱۵ تا ۲۰ میلیون نفر را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76655" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
