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
<img src="https://cdn4.telesco.pe/file/Wnddt4d1UHGbXjSYSQL33owErkEaAUxMdSx03aFpSPMjgVIN0J-8sPQTfo_y7Yxw9BmqaaUaVnTIhEyGtaj5qtaKUjQFMu9bnj6Vqtu-bqYhqjeNrNO1aE_OFf5Uo21W4KfavVRiDrgoZsS5vLV3TtXQO7mbjCrvKvlLgqXaHa9aRW3pXLrZnGVsGMrQClxITzoXAc1_kfm1a1cVoOy2-a7Ilj6M6OWoPPD8HlaYnQm3Np4mq_vCqMn6DLv1Gcvx6d0qCUvFT7gxndjr0k4f-1y0gBfLmYeN55wSkF2gzjPRyjNTcJvdSuCUdvLedpp1riLKOigX4dee9dPySGELrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هیچگونه انفجار یا حمله‌ی جدیدی در بحرین یا هرمزگان یا لبنان گزارش نشده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/funhiphop/77391" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">CNN:
یک مقام آمریکایی گفت که حملات اخیر به عنوان یک هشدار به ایران در نظر گرفته شده‌اند و انتظار نمی‌رود که تلاش‌ها برای مذاکره به منظور پایان دادن به درگیری را مختل کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/funhiphop/77390" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجار هرمزگان
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/funhiphop/77389" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صدای انفجار در بحرین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/funhiphop/77388" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مقام آمریکایی به فاکس:
حملات هوایی علیه ایران «در حال انجام است» و اهداف شامل سامانه‌های پدافند هوایی و تأسیسات راداریه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/77387" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/funhiphop/77386" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این تو بمیری دقیقا از همون تو بمیریاس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/funhiphop/77385" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/77384" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاکستان هم افغانستانو زد
🤣
🤣
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/77383" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جنگنده ها از فرودگاه مهراباد برخواستند
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/77382" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سد مجید :
و ما النصر الا من عند الله العزیز الحکیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/funhiphop/77381" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5sGEKqDkaahMzAhoVeztCb02hOVGEJfTdrvYtiaz4fDiywuabqdxkSLq-YWRH-rzZXAZ-UBO0Vrvrg7EOsmHbTkLW0xf5XjUEjGpQ57IW4Jojndwvr8lztPyjnwToa4eU8QjxJxKfe8F9Z_lo_2yExysDgcTi_xPQNkbaSwU6Xe1UoTKZFH2kzdcwqoaQh_RAmQOAyJUFBJsRGs8INxzOX2X4LQmDdbX0lHXHVjHk_HV2iZX8C7ukM572j5FXmBiGQaTXIuCMRyzixRoAw_g-1wHtBFu2dcJg_wkuTScME2MwPtanyk5dloJ-3cgzbwSe9I9YxxCiI-hVc-nsCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران سوریه و لبنان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/77380" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو این هیروویری اسرائیل بیروت رو زد که ایران به جفتشون پاسخ بده تا شاید آتش بس نقض شه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/77379" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قطر و کویت حریم هوایی خودشون رو بستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/funhiphop/77378" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لبنان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/77377" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هگست الان زیر بغلش تموم شده داره بارفیکس خلبانی میزنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/77376" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حوثی ها: مالک گپ مگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/77374" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تسنیم:
ایران همچنان که ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
@FuunHipHop
| Nima﻿</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/77373" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدا و سیما:
پاسخ های ما تا دقایقی دیگر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/77372" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
سریعا به تجاوز آمریکا پاسخ خواهیم داد!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/77371" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به آ‌ب‌ث نیوز:
فکر می‌کنم پاسخ دادن بسیار مهم است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم.
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، و من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد، و این همان چیزی است که این پاسخ نمایانگر آن است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/77370" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجار تو میناب گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/77369" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هم اکنون جلسه اضطراری شورای دفاع به ریاست علی شمخانی در حال برگزاری است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/77368" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارتش امریکا از شلیک چندین موشک کروز به سمت ایران گزارش داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/77367" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77366">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الان ترامپ زنگ میزنه به خودش میگه حمله رو متوقف کن چون توافق نزدیکه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/77366" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/77365" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">درود بر فرید جان عزیز بندر عباس یه صداهایی میاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/77364" target="_blank">📅 00:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77363">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاری دولتی مهر:
شنیده شدن صدای انفجار در منطقه سیریک، استان هرمزگان. ساکنان محلی از وقوع چندین انفجار خبر می‌دهند. مقامات رژیم اسلامی هنوز درباره علت آن اظهار نظری نکرده‌اند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/77363" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77362">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/77362" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/funhiphop/77361" target="_blank">📅 00:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiy1FaM6bxA-1FgJzVI4N93R8yaaSGRxPm4jK3rW0xL78SNPIpY7ZAG12PV636_0mjS_-f7WZwuxbtq2sYOirTEvRiwKKGCIFK-I_sEYxL_3xAC9LsIbLqYcm0i1pzPatf15mf0oT3KxYMx8QRhtZJeSdEAsmoHFIJrwM-b8iNyiy0luAcIl5Ur9yk--kzKFYGVBv9jx1npGy4DGQOvuYAFO5BUnZAeTltTc6KfPVfmD_GS6RKnqb-wbl7OcWqsJ5MhRC66oCFibimAEj3YdjDaQaLq-g8pmtiUcEOUrR6e70TNqRKe4u9sK1d4t9zGVpVQjWxPKltA_joQdiAIBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس جدید شایع به اسم
عصبانی 2
ریلیز شد
Youtube
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/77360" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntkYhm3oX3apqL3xfJK4M56MvjIXnLvkIsU4nNePnpXhqu50OmONBD7Sw4u3_hXT8Lh3dsLfizVOKFg6U6y-qGG5AueoOu865f7CsvPFY3w8Jtk2xJdp-lLen5OZeJCI5z06vNsIrGeUN3XUwS8cu6iW2Rx-qR3EMOP8DntqinxOOGpacHVXO7cQEoKPPFyt8Sf-SNBpNo7n4v4bkZ9kqGuMoY0k7U1NTizEeHnH2pxmDYEtr8D8sdvBuaVMpzK6HEznTwYA9kgevwAAoh9hRSEOuMprIMOkZtrF3dgp1jfoPFwLO3jnw9y0nOVsTHrxMoNf-IScsfeYVZmpmJAl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:  ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.  این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.  هیچ هدفگیری عمدی از سوی ایران علیه…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/funhiphop/77359" target="_blank">📅 00:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNhgNiu6rc5xjIdn2_vAjPqx6tJtLdN12-KNnNXnpadZJs-U5RQRk40c9i0aUnysaz--eLMEoJce-o0OvLNA9ifW9VcbdvTt8V5qiqkLltx_luPTxzmSZ7CG7PizKIFMEn4CtLRCFzTrAR0cEZcJwMwhuBbeuQpeF_7zNBf39H1QhhIzFhyLrFYnhBXcWmDSK19TgfF8KJ4-0kL6oZQ13gYhvaqT7v_RNnI8gqPNDWYioIniZup64vSttIdyQxlvgqXGzot2uUEFlBCf_UOhQtdclmHLxcCfhSHj7zjYnvloUJTqCDiHxKOv_vpcSURLPxz_raheM-y-4BvDq8Q_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ورزش:
به قلعه نویی دستور دادیم اگه وسط بازیای جام جهانی کسی پرچم های غیر رسمی (مثل شیر و خورشید) رو بیاره یا شعاری داده بشه سریع بازی رو متوقف کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/77357" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به وال استریت ژورنال:
حادثه هلیکوپتر آپاچی موضوع بزرگی نیست و خلبان حالش خوب است و مادر بنده هم جند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/77356" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/77355" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLRDkD2OqbTZ2v6tCHBVLlVxa_XNvkYsTKHrO5xu_o-zIqLivllCY0QDPV1cygmXiuELYtFd5pm1Roa0ld3b4LHjlzuB1GjEiXgeqHmxP-H0f-DmD7LtXHdBboSrzXIrDeW1qfrTjBefUW6uA3CLUAEyuWqN7_tXq5HgEJlEtVxxJ-d6_M6yXtGqJb_gYnO34NKB0KRuztor0f0U-Y647QGaHYlRWKaGaruY69UoILrncjZA4KscYbF-Gj3qqU8LlcXqZXF6QsaI_IeEQsEBR72LMxwV9c0EaZEJdA0WYAwQ1-nseaQHHY4YoBqGlC7E-9edWbMU7e6fN5PlQsGDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77354" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF1-91u8vwDRGJrvUlEbqtXkq5eGsk7CIlNaBgSueRcnnLnvqBTm3W_5pCrB8skDeeUqHQnuDx6VB79qxjBc1_9jSy-yb3d97SzweIA-E6XlSx4L2mIoavpQFyXLCAuZudJkLg75xvcNOfMkcrum4bjjbio_zz44dfGvHsG7GZXySh2wjoarc7LvkeIvx6uLQbPXbqYfAm2j8M04V9ZysaYbnyjIGYJ0WbXPoPidIysPrSsiG5Kjs_QWyL5uRyAPpGxwvaAmoTecJfG4Rp1jmsfbiBErRZDnHD9nM0alMOe5Iw9exFv5ECMPwjBhGF_8Ly3eqarY5-CzmquMGlvU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/77353" target="_blank">📅 23:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxd6rrP4zKmVCHjNe0LZg0YxULbIyMXqg4GgEgiTXoAQUxoHoWetgwAhRmqi4JO9uOBviIYrdvj2VaMbyWdrA4WdXXeX_lU0k4p0z-CG4S8gsDNlqpXrOQYW8QO15tKe0OZvxysMP369UUOwutmDKFcbeR4LZyEyPLAM_GAI4MSYMRMidS_ZBLykEL8rxSN3fvn7k8W2Wfsv0tNK8qfLvtlL_14dpr4gu89nZFwuM-C74r5-y3iUeRAhpbaeJ32DUAWI7jbbgODZ2JBKP4gsMedS9VLa0kF4zUPj_I-sCKnAnIe-vXljtnj0p5ja6HqQFjAjV92v3bkEQII9OaWUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77352" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">داش بمولا این سری، این سری دیگه میزنن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77351" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب امریکا میخواد بزنه ولی ازونجایی که ترامپ دالگخیزه تبادل اتشی بیش نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77349" target="_blank">📅 22:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNCPU1IdRxZgdD6DpUTDCYAa8R4OxYCxGQ8Bn-wBGg7zxs9VZOlibbJs1gnlYr-OZx5i0KPlwIERb2chiVLSYNFmEuzKFbe39fPYEaxFfILnTHckZ3-OfbHA19iG3-Rm2E1J2niaaHExDeM6RPvzvVwOY66-dIyogfxu4VDflWxOQ9n74nGPXhQMfYrpummNHQ_Sa3IKHeLhu2pN_RnHqTaZNe4EyAgmUxMt0UsTgSe8xcoxBMJus2BgJBVitMqtEve08d0HHo9Qwps_288XoKdLA0tyMYs7aIs6Vv5fEA-RFsE-gL6Hh-YHERf53yKK7639k0A7tbPa6UGpURUe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77348" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارس شو</strong></div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77347" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRCjKE4ttkBZu1lBUUggswgBB5Q3r5KoepfZsWUDV7rQOLWfV_mBzZ10QKmUN_wkcm_MfhH4K5XsEx3ncocEkz7joubgq836phUdM1Plf-3S1lE47kZRKrieiwffyKMwfaxo3Az7gVvcOmEAsdNEBhGVLKm7kGoy_GT7hVjqnlhkWsa35S5jnBxi-bYAIq646Tagb-WM1P_RQ8dxlcv7d0jvhAE2qEaVS4DA2ViQTbmsF5c6L2LWDOa-eA7MvOxyW1RR3vP-dXHjXK7Htl6-C1pDY-qZ83OVzhXUIAkpkQjSEog2n0kI9uzYQ-BSZSXvAJ3GuLSDP2yjkI9JGF85TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت مذاکره:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77346" target="_blank">📅 22:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77345" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوسی خبرنگار فاکس نیوز: «او در دفتر بیضی شکل بود و از او پرسیده شد که آیا خط قرمزی برای از سرگیری یک جنگ داغ علیه ایران، کشته شدن نیروهای آمریکایی خواهد بود یا خیر. و او گفت که این دلیل خوبی برای از سرگیری عملیات نظامی خواهد بود.»
«در اینجا هیچ نیروی آمریکایی کشته نشد، اما به نظر می‌رسد ایران واقعاً، واقعاً تلاش می‌کرد نیروهای آمریکایی را بکشد چون یک هلیکوپتر آپاچی را سرنگون کردند.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77344" target="_blank">📅 21:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آکسیوس کاملا روانی شده:
نتانیاهو پس از سقوط هلیکوپتر با ترامپ تماس گرفت و از او خواست به این اقدام ایران پاسخ ندهد و حمله نکند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77343" target="_blank">📅 21:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار فاکس نیوز گفته رئیس‌جمهور آمریکا در آستانه دستور دادن به یک انفجار بزرگ در ایران است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77342" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77340" target="_blank">📅 20:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77339" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دالگخیز ۳۷ بار توافق با ایران رو «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77338" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC6g0YvhfFNAvCzv6ccFCU2hU8cNcOpSkuiyig9V26oFy0TUb9MOeZHVTKldalu60NX5ffeKsHo8-ycc3QW3E1S_ofnu9pYJ9xhv4KeETo51S448n4DBjmbFX65sddwn9zUd25qcHRo3hlcqUNxjXnPqZ6RqfFZNLo_npLtJUsLIxj2fEs3wak1C6EvIYzwP0oBQSX0cHdgFeI-L692sRZ4MbZYjeAWjhj5sHSUBXk9cII8CjnhX9eSlCas__EOI76YZSeipWgn2HSJl1NiFU-GpgOkpZD_KSvpPlEgokrYQpYcVgp_rLNTi6cCpmG6Ot8xZrYRU_0dFZKahz6iTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز:
ارتش بزرگ ما به من اطلاع داده است که دیشب ایرانی‌ها یکی از هلیکوپترهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه دخیل بودند که هر دو سالم و بدون آسیب هستند. با این وجود، ایالات متحده، لزوماً، باید به این حمله پاسخ دهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77337" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzit9HgOsUGaNqB8e5ZNH7bwUTvioR5G8L5yXsD0lnggsWBofGBR4GfhBXLWbjEYY_2U4ohSYaOB6SPteUa4VhTwU58JVmTC0CakJJmtAkSAq0QrCYU9q_xU6fNPJNyWZGh-XvOwCRL3VuJNuN_5aoAyHElhBBAvEm0R3D09LeYVA2_Ix7-uZ7hqx-FvH-0J0P-eNNV7nQZeMmlDlvHSpNcUbYzigWumkvx7JmMODoCrPfzuXVvtRaCHamg10sHXLpDh-lymc5TtWO-IU1SmnVZLOps8HM4vZZAswDCMSSPV-s2uMhssy3Raw6kfjFgJVj0BxT6BoyBufNYocoi2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر تخفیف گیگی ۸/۵ رو از دست ندید
❤️
🚨
0️⃣
1️⃣
گیگ 100 تومان
0️⃣
2️⃣
گیگ 200 تومان
0️⃣
3️⃣
گیگ 300 تومان
0️⃣
4️⃣
گیگ 400 تومان
0️⃣
5️⃣
گیگ 500 تومان
تخفیف ویژه
0️⃣
0️⃣
1️⃣
گیگ ۸۵۰ تومان
مدت محدود
🦋
سرعت عالی
🫶
بدون قطعی
🫶
با لینک ساب
❤️
📩
همین الان پیام بده
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77335" target="_blank">📅 20:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کان نیوز:
تو درگیری اخیر آمریکا به ایران ۳ میلیارد دلار از طریق یه پرواز از مبدا قطر که تو تهران فرو اومد پول داد تا دیگه به اسرائیل موشک شلیک نکنه و آتش‌بس کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77333" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77332" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه
این پیام بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77331" target="_blank">📅 18:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMnkKRzTyiQA2_VkEcJtDZUER5CT-11Q9oNvHIsAKAqdWQ1wEyATHq9-Lbc3q5Mtudd-DZv3s-8Wj1KC495_XsKocSuo-RHxoKUcK4Y1Ve--fG1DC8keBii3qXy07_ZOwSyN-XYWonCNe7Gyygq2Vv-XmiWJOUkc-w3JDDk_GOehve9RIH2rypdv-QrUfaN_9a7GdbRFDM64QbVfF2zERaZUoIgEUGwi2RMTA0nK-Ig5btzja-8vFcuy9JWQK_4s4NS2ar0nh5opAft4BItT_NsKRlYKX_o3nGUfhNGzAXA-6mPcKMDRYmeIQbVVx22-zMFqjSOT1dwklq08Asn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد مهدی طارمی و رونالدو توی جام‌جهانی 2022 :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77330" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/77329" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9l9CIvZ1TTvnoD5RAUjgds23GuvHnFQ3crjpz6MW35c13urgEBDZaA2GL7pbMdFaJTMEJYvugok2ebTb0HmSX1-Hj1jpjEgO8c91SUwkJDmi6QFc6qpU4lH4SW0nxa-OCEz0lsFOOTHksx8vvpAEknDcpQZoEru6txt7rI8Q0-fWzk9mNgpkC-VAWOc4vlD9UYPEWpZtdUyx5-039wtjBK7YvVrMxzUDaLnYv9GV-5V3ZDB4GyKB_FukvZ0hNmsxwXPkoOBftE0YDZHdTXXJeQ5bM-AWic5I9abs1m0B4lv3zQ_6kkt6SaHMgWdqIiFoP3YtvILW4oXl7hBBT6AKQ.jpg" alt="photo" loading="lazy"/></div>
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
کانال تلگرام سایت: g19
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77328" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنگوی حکومت طالبان:
صبح امروز عده‌ای اغتشاشگر علیه امنیت ملی در شهر هرات اقدام کردند که نقشه آنها شکست خورد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77327" target="_blank">📅 17:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77326" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77325" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یوتیوب قراره رفع فیلتر بشه.
@FuunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77324" target="_blank">📅 15:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77323" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77322" target="_blank">📅 13:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تو افغانستان اعتراضات شروع شده نیرو های طالبان هم هر که رو میبینه مستقیم بهش تیر جنگی میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77321" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4VKKxxjQ9Zzf5A5-ZEhxP6iqpxHiU9hryVTdpP8cvHZTviZ8afFO_YNQCmSsTWtliq5BJh_jRxrL3NRXHdvU9unLx9c0QfwsoqvlFMIndekPai8y06Zlp-NRJVH-Q5xkQzyr8YKX8-n-cVeav8Wxeo8kzMpetLQHA183McBWs6mIynRC17ZSbl79nDHYJoqK1r4lM1APKeoI3GED7sOrzx5KXxLSGxJA5c79xPMN9w_QI423RosYeOX33s6ayL1em221E7TYRy4EtJ2oy3rvjsRUOkHpBCAPKxTz4fnQ13PvV5BS8Ajqe8o2UevMYN3SVT0rentyqUoe36ZNdB8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین حق‌پرست، از معترضین دی ماه به اعدام محکوم شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77320" target="_blank">📅 13:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آتش بس vs آتش کم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77318" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
ترامپ در واکنش به سقوط یک بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز اعلام کرد هر دو خدمه آن سالم هستند و کسی در این حادثه آسیب ندیده است.
به گفته او، جزئیات بیشتر این حادثه در گزارشی رسمی منتشر خواهد شد. هنوز علت سقوط این بالگرد مشخص نیست و احتمال نقص فنی یا عوامل دیگر در حال بررسی است.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77317" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=sCq6DrbYyGH_0Ng2rrLU9gxGqKZ-_psRsyFOPmVlVpC41NlZvuDbLzAjOuJN67_Ai21RN8X_U2TEAxxVQJ1MmYmB9M7QwwmmZqzCTsYjYHVOXGuyKdtfxOkSL_S_SDDfIy1GNwMv4IBbE8EOQWVoNJ9ISwl3JIEwLm3YVfAn1OfuvqpZFr1UH_XfhJl6EYmYKpbrVJMCtMhcH-Rx6O5SOXvECM0jo_e0p2dBbSu7tIjd0qNEBEHjvG56AO6gamN7CFcTsSqDhySJevO4APd1C93s5KzMjMNje_iN-MP9uK2ZNsmGKj2ieSA7dKxnV-uIeLxIUd35fp0Llv5AHZe43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=sCq6DrbYyGH_0Ng2rrLU9gxGqKZ-_psRsyFOPmVlVpC41NlZvuDbLzAjOuJN67_Ai21RN8X_U2TEAxxVQJ1MmYmB9M7QwwmmZqzCTsYjYHVOXGuyKdtfxOkSL_S_SDDfIy1GNwMv4IBbE8EOQWVoNJ9ISwl3JIEwLm3YVfAn1OfuvqpZFr1UH_XfhJl6EYmYKpbrVJMCtMhcH-Rx6O5SOXvECM0jo_e0p2dBbSu7tIjd0qNEBEHjvG56AO6gamN7CFcTsSqDhySJevO4APd1C93s5KzMjMNje_iN-MP9uK2ZNsmGKj2ieSA7dKxnV-uIeLxIUd35fp0Llv5AHZe43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از پیام حسین رحمتی به برنامه طبیب :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmO7Wwni1ZqIGw8TL9tmJt7KKqZ7DiRcWrpTgEo3kLsDQ2_YTLWd7hh8LDhnYDow-sraG_mCmDgBawhdoCm48jxgfOjmcbXkMVrpdqYpYDqQ0ENm9wx6QpAS1bGHIkFn5w61OZ2CcfA3UOuHR869z7JK7X76DOw80fHwA77C2bFrR7pCRjM-oI5v1unU29Fqxai0G9bX2UfTKlEi840ZX3ZWKD7V7orj94RrfOjO7JBzd8TS_ozTghB7uxyZce8A5JzEsUEhGihRtRrXZBxOOCGd8NPApEUxoCecZX0tullORJU7TdIXJPSmq87NDFOUu2vpQd72-Ck-KDY51KH0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
👍
ورود به سایت با فیلترشکن
R19
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🤖
ورود به ربات تلگرام ‌بت‌فوروارد
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-jqy_AvzKm-oqe9Z9RYt6wYT81mInYWq8VTGyQI1nZs59K-d6zWK0ddOw6Ycj4oqI0GU65jRMgl6SNAWyaIQHJxsUj270yBQfC0ZEnlCtNIo4bK4sDht2hz3KJAagCz6lu-tCgryD957LEMNUQvMbtyItwotz_PKvpoqT7TlQI-O6lcMxKMGJEjzXgRnUVLxCc0z9Jhkfo5UFYqh1v8IqDv_r54_a8dWJ4BmlCakH2qDp9-5omr3eifEVYd_5_3dyQTy_kspRwQFy8Q-2DndBNLgVb9ZNynzJQ5sni2Lx9sZD4YFxO9eNWE6jPWARcJ3AbO4Qv16gmreMn_vacPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArwnO61HUio5WnV3-tRFxebeENEYAuoPnfGJ5noxITuA1vUZfvmFAfZWRYKeBDw0BDYLxrIWFMRaw0YlJJl5EVuiAJYdA7Yva5i2a8-R0bttl6IMXjUEaTGqEPKbA-nhOWMh4Kevdh-BUyZVs7hGjxp1tZJ197TtsWjOZK4Pm3nNKAUU6HxociKkhfu4elOxTXEN4RS8bwGXcD4hgT9e2-qHE62hdIL-huJWaQzOd7w6R5sCAbPnhatWUxSmrqD-yEtYAnU2i0EqO3ikRXd8gL2gZIBrGkp7DXnTMG8S7Bag_kddBHgqzb2P9LAVxTdMUvv_74MkBcNRXD4gY5z_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekrGManKpiEar7B9YyNHHK79dNG-hSUriNlAbwvuubnEklvuDK3FK5paez18nIuHSgZ4w7ZVTEj_hg-TBN_PCF2ZjYMoRgGvndG4WbJt-bWH-_dTtb1frgPf-OKAAEZdDhzCMge5lvpspP6Mn3qbfTbcXubZ_0zZKiyGSnh0Jl4IVJJPAVbQZ39Q5EHx7HpXhkw4tCIF0656lQX_FRb9ONRXzUwAiGsMhEk5isWSQCzYQuUHYIk2kdLJzUId2QZgys3HVYpqGS8gdUblKbYQUBsSxstVGMCZ-6SJy_YIpQN0axiy4GcQBWtluVI61oQHEwccBRTPjMveh-Naqn7NSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0pDo8m01_r7I8yFIwfxwbM_4_su_haSJ_N1B_van9Vl5qyMqrsMV4TBhnzxXKINZ_PqmEhCmnRQFbbeqo-hNaGCCQ2pLtdWCFmz1fnZVmVM_slfVrVoSKm8iLwFb3FTcOh5e-ZU0UZjceC9WlbsZdb_kJySphSCVSuT3q7wehC8M0bPZRkRYnJaeYz34623BS7Wl_uQkrVqfGt_o_rDXFCD5j4rAJf7HWw-Jhri9j2t56RkyOk1ecoicL80Y2RLkyXFDWLhDEq_Udt-R4KGPn4YqORSAVmWF4_lbQTzC33mnGRzCglS-tVR7mJ_t8YaXaJS-kpKYT3lzsRlYgp39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7DlYd3qTKBXrFEzQRis6LI-dCO50gbHZAm9NeJ-002mTL0cGvSCeE1l3Bw7ckxZ7xiz6f-o9PNB5IAE4Kc3I0D5F_9I8TCS4pdxjhW8MzHD910ex6pYYorqnoHPg3X4O1KeI_biehVAz9aAZqtOiIRs80sw5-k5jTCh69MjtKntyT4DIVzQ-74Vx2huytEcHMTkwYsXUvcUHH1Q39zYpBesaOY0XyGez2sZW7QWiy3D7-xyBePBlASn4ggnOhkB_fKvDtS0ENyAeZZU-q3TsRG0duH-snJCCbNCpufX5B4n_KnZ_92D1j7krm9MWnYXBkQcCkW9L6BUvuhzVaGliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJLOS-NQUZtT43niiJbq6-cpmQ5bHv_V2v8Q7bfnlbeIM9U0_3qyvwNs0bR357vVmp6rOpg2PjORs90jCVEug9pCnZgyxubusIETdR9eBF0ATydOwtZjl7e4-5W-8kWoOBU1tB6TVRqyN-L96rZuBEOUX-hzdqpO5JlNVa8xRD4FRLwFdPDUsNIus0XLSBFxwU0DNMylWWh_p2X5xDmSxVsW0S3-bpAdDgCcN9T1NFZrD24VYXEPtj8u4I1r4-5UsD36x5e2ebDlTNAnPKC56FEKHJAepKzxiP7jlsoOFZjuj7h5gttbMBeb4CVYqYAGGkTc1pAGG8aFEoQlR0a9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6QsDWnmLI266Ky2gYuFp82DJ9YSAtlz0A95lkXf3GZtfjKqoBGG-RKzzjh5e8olvmz3dta0syI66uZEI8Px9Fw1-tb1K4bD36qGjQMEoQhmzBbK72OFHNOI7-vnGM96uKsnExNPYa-P8sgFlfWSXC2rmdnes5Qk9yyTOZJiTmJKZ1_20VXDalPgMoYg7PQDpGhDaWyI5tAAWN13YGzHh8M9KA5-KILac_LZSqBoltkIIpea4TIuEV-uJ0nDlGtWvybIXD90BoEEjqzn7NsFlJT6-GEO3ufF8k_e0OFzGBtUUWVLye4-1Jsw2Mj4qC9d3PMH5AKry1OReBGdtbyRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0qvkEORfXzwNyE5bygNEU_8Xktn0hf7leD3VzB9UrStuxozCdTDk8ls5WaxWTI0IKVzfvqLHYfjIgTAlHQgnCCvLb5y9a4Bor5P95jhBPrINezQBVv4uxJ_8KF0jLSdNLiqYAHb48XlJXNmbcT6LsLXUXEJJA4lfOpvIECD4MajudFt5Afc-VBKJIZT9kR5pFkwxZpKVYclJutaB1lhEt5R9nkuAGAuEYc4-ZTtb7sc73-Z3CbHljKp5dhFvtRsu95YfP879aP4B_2Ck8gQZ0zHYqA-TLv0wGD7E3ke7a1RyPYUed7tRtHrGf36pDTKneJRyZGf7RtWkLa7R0ZPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzG_SbJO3F_3S4RtrdYRSI1mxzzyuSrsZNs_I8wcv5cw_fOy3HncjkGfp6DLIOPr6mmRpyd8CQGSMLJAAX5MQT8HCuX5ddYgj6lejh2AveauiV55KAGQL5G3obUbJI38k5d4ZgxVW4Ylbz3Ms0yvQOO0gPmVJ2htdk191mTeR85PmHEUUd8-WOEikN8c4bsuC8J4i4QhT2VWX86VrXUVgH3Mjyq3rWSAU1PA-kRLvZqbmgrHfd_rdcMMn1BJ9StAGDtkLJJbRU-f8s1DNZoSi6gvBc_iSPdU-68lk6ohYDRUA-7qXxYiyslNbuRDx4PBJq7cW-DZhbVsWfslMug3QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🔹
ثبت نام آسان و سریع
✔️
🔹
نصب و راه اندازی تنها با چند کلیک
🖥
🔹
اپیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Las1O7Une1Q_Kcbkp4nsUm5h1mhCl-izP46OA2CaiXXFy5ok84rOgyg3eur0aAEqa02OW-rgwBCuydXY478Z4UX10BeoETptCGOcrJohbPievbAHic0T8x1xWVf7PlgnLzDA4t_64bXZxBXUT3Zhc44mVsNkF_GvsQNoTugqk7pzczZqP2U-_JuJnUpmMMq4eRsEJ-kGeURyol2VH4tH63xeLNUNildsriydbyjjeOT131NOOxnUG9PN0BPj_oO85NB-1KHA1nspzs2T3MPon6UGoXVj6FXmLRthfVvMOwzWo3_igGMmDC_cGHT0gjvu85R6fOpMco9EI85krMAVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎊
با لنزبت، دنیای واقعی پیش‌بینی رو تجربه کن!
💳
شارژ فوری با کارت بانکی و درگاه امن VIP
💰
برداشت لحظه‌ای تا سقف 10,000 دلار
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🎁
جوایز هفتگی مخصوص کاربران فعال
💵
پشتیبانی از تمام رمز‌ارزها برای شارژ و برداشت
🪩
امنیت جهانی و بیمه شرط برای حرفه‌ای‌ها
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G18
🅰
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9RLLr9-HvZpMQnU05DeDYsQQTtCetOdLLci7OecW6YzFzp0xXuvHrg11N-h-piMGqkiNV0AUSg9tr2V76WXT0bGWLPZeuLdB_X2W6qtjboyY0eEELo39fO7YL54a-kOLI8ayTjUHmfwHOGgY7nLoVYKfz00sehFbJ3OtQc4iow04qHezOueKgOP7W3Y_WyCOzATjVVeRHGKm_UfhkoiDJ4wf8q8xUW-XFOZ-Jv5irFgBv2xLLxL-e2YccDMTVatABO6SZRIRfJ1TCWdjsv7WOfSqVqqamyE2asSJhbzMuAnEkeIj7qgYLUiRZIpMwR30xlMq8wILucWu5oFy2zuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpJgA1oGGjOLAYv5zCbwm_og1hvyyjgtOiTJ4GR7kU6LNoFyZlZrsihK31dOL5Ih7K3KNFsYDgXgtiCDGwHAGVaYk6bJT9KDIUIFXii6lajIltbiwNyUyTFQ6-s5pdfNcttTHAK_dC-X21kja3NSFnrt5XCDZo_4o6bY-njZ40LWWuLScPRwSPiVtABXFsQUG8cK8cAyIXpmF0AI6FTivXxLNcqpjmzubf4jXOwYfx6-KAg28ajun0JmHrXydF8xd6qWOeWgEoL0Xo5fS189bUr_FB4RUqybmI3Fld81WNqR65ogT3bL_GT6retAi5X0y-EAqPv0F-eAOPbgCjWGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX4J4sSANO7Mg32zXV7eK8Pso-ozi0G1kJFzllU0YUojjy-5aQbLM1D1hoGlyVReTuJoiIe0SdJg-2oQUjcraQlKSp0-dOFmhXcMHjtZWqd5KOsiwywrN95resXtLrU-IlipK-xNWBxOR3H6xu-qUKTmCZjG_L5EfM21gut8_WE3bTyueSsnVFDhP1TXeefKPIYNnOJZazq-uZaR04cyre4oFq6tVJYuw__DKA9ojxH9pRehBaDhiSYbTDM2-jlp5_TCuBV5s5EtD8Mh2j6fNCUyMP1S9078tclDWlyJELzxfDZuvca1BELdXOgnRcnfSrmc7Dp2M1xNf9klnqp-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
