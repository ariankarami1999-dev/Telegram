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
<img src="https://cdn4.telesco.pe/file/sR-SzQqCtzYcj71W3SzNITm0nLbuOq-mShKevBrRCzdvWqqd9lBeMjGp2gSZTpmD8oEdFduwm4XOH7rWZScC-5bagJFBQcJmda7QtlDuIgPBSrU6BKMQS94IqJiy1duOfR4gk-2E6ps4X7RYJ8B6awimcAY3l1w5HpK2sEZFXf6hImzuxmv2-y2ElbAvHSBu5I1J4gOfdcxGlu8QCE_NVP5iAG6O9drlUA0aytDLFh-Ys6HwYhLciK-KKraWqBVx_JxucONUFIjGwwWhr6tkZ23bdvzzWLqM4fh7rgz_IHCpDv93WYAiVWNb8aOdhCqNYf66h2t5jcXuOBOfobf87A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-82769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حاجی چرا خودش ۵۰ دوستاش ۱۵</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/funhiphop/82769" target="_blank">📅 17:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAri</strong></div>
<div class="tg-text">منو ب چشم بیزینسی های کنار خیابون میبینی؟
۵۰ بزن بیام</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/funhiphop/82768" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/funhiphop/82767" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=Eia3GMsQziFcuYD2WjDFWJkG5-TJr7RZERIvMUfuJ7xWA_8EIX645a6KSfcJ5cT6g5u7VLI1_xIaceFAhz9FHWd2WlWMhfW8MvBmdK_C2rHhjMI1DoZhhxb568qDUlYAQzX0C4hegSntXRKxmzBi_FwMffXk2SH74F62_2XFttyWCzilDSHQL_lVc1-HhpBOltOYHTN7T55ARiUni7FsaCjD7V8ZxmSBx_1Ez8jyam2LTf28fuRO4jCqUEY6zRQXm9foutY-qJcYcZNsvyn-7W3uuJ-XnjK3zPxgwrInKfbtcxP8oAWA1bQiX0ZSKzS-WJOca44QHLlxq4x4c5yGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=Eia3GMsQziFcuYD2WjDFWJkG5-TJr7RZERIvMUfuJ7xWA_8EIX645a6KSfcJ5cT6g5u7VLI1_xIaceFAhz9FHWd2WlWMhfW8MvBmdK_C2rHhjMI1DoZhhxb568qDUlYAQzX0C4hegSntXRKxmzBi_FwMffXk2SH74F62_2XFttyWCzilDSHQL_lVc1-HhpBOltOYHTN7T55ARiUni7FsaCjD7V8ZxmSBx_1Ez8jyam2LTf28fuRO4jCqUEY6zRQXm9foutY-qJcYcZNsvyn-7W3uuJ-XnjK3zPxgwrInKfbtcxP8oAWA1bQiX0ZSKzS-WJOca44QHLlxq4x4c5yGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/funhiphop/82766" target="_blank">📅 17:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e06015a.mp4?token=i5IO9zatR7KayWf5-mHSPnZB8AslIQLVVo5O1WApyQf1jXBgglo0dhVwMO2ZrhQSRu5ZroZZ_G5FyAht5VuHD9B75RfNt_Sy30PDgMybQWeMug52OIlUIJvl6wvIiRvuDVR1yo7fvnxnCg8WV0rJ1iCjAK-pKeledN7xKy0rrkwrKPTCYASicUt-xr49lat7Bc7-oCVqRG6n7tB6FbyzzBhC4NDhip9PENISj9R9s08x3RfgKcd3THd5--NbNA2S7XPrxXQGVzU-GOguZ4G0Evg5g9UGAmj4RMQwWfIcvoxeq2Dg4Zy_YMOeU5L8RGYh4UHjOxpKBK5ZKJiJfnCk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e06015a.mp4?token=i5IO9zatR7KayWf5-mHSPnZB8AslIQLVVo5O1WApyQf1jXBgglo0dhVwMO2ZrhQSRu5ZroZZ_G5FyAht5VuHD9B75RfNt_Sy30PDgMybQWeMug52OIlUIJvl6wvIiRvuDVR1yo7fvnxnCg8WV0rJ1iCjAK-pKeledN7xKy0rrkwrKPTCYASicUt-xr49lat7Bc7-oCVqRG6n7tB6FbyzzBhC4NDhip9PENISj9R9s08x3RfgKcd3THd5--NbNA2S7XPrxXQGVzU-GOguZ4G0Evg5g9UGAmj4RMQwWfIcvoxeq2Dg4Zy_YMOeU5L8RGYh4UHjOxpKBK5ZKJiJfnCk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا محمود زد به ناموست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/82764" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ژسوس زیر دست فیلیک شاهکار میشه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/82763" target="_blank">📅 16:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بارسا نگو بگو سطل اشغالی سیتی</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/82762" target="_blank">📅 16:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الوارز میخواستی بارسایی؟  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/82761" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYNwo1vfg-sQSLVeCkx8mi-O69NtQ99ysJTTZ282ruK5C8HAsOEJOqfUk62A1792F0RV0oBLFoTTSi1KChCE0h-hGZfmTqk_cTwDpfrsMdmkzwhRxALGx9031LRlqhg3YBz4s6oHWMr6G9RhO_Q1Nm9KjGIIf2CcgPBhdQhnMyKSHNg6D_EL_M0HhiwaIcfbLUeyzjRGJ8RCEqPtgmarlcBOGfgfRYWxJirJbd8rUKnqbLcfQsCZ-1mBAHRuVfWw559cQ7LTKCIlpIUimmin_n9yBjmDfzd5o8CcpHlbNEYbzJVzSjSC-HXukDnjR4DyDO3IOlaZJ7KUjrFhiD_Q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز میخواستی بارسایی؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/82760" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2CaFOaf3PoLm_LesKgaSGqjrAIgPK9RJZ7ekNX5Ei_5TlVZVzTvNpzyjCMRsgnbhoFsqAueUfZoQZaXz90I0yVbbdXDIWcCbFIAbMhYTTqUFuLpUJSe9lzCruuaS4CnQyQ0YmJjV3qCCuARJ2OCjLCdj00Toj5t7H4On-AXxhBKalgR21gVy6dPEcBo_PnOk4O9fnwvu4rkuONt8xVc3z_YzE4-a6XkVfoAYD_0bOptst9NwzSQHrvcSbp3CVhHCGQuYFk7Nw-KaXX_l8-9wAUKXnSkyV0_Ev6wZZKVJJi_GkuYYgh49yvNFixwvLYgn3zVcwHglBZvydFSIb8Ltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خنده ای مادرکسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/82759" target="_blank">📅 16:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=Ghg4QJLSXwnywFnfz_eVfcOKOnwzsi6Y8z6kdXhvPt39AnKIwrHjvv-33zDk3q5pjgLXsxb02EKTbAeoaklRol2vfr_53lID_zWyfzYq-qhQjAYkNVrwotKsZRTbEXjcMEzGEJSQjQZHETl7M4ilne2s7LbFhTa7R8MJpKJqV8NyLmlsBrPFY7ZMG31_6ZBna9OxLrr1uSO8r-oRFOyrF-SgPrgt1nW029dhogj-LRyb-oJnnLQR1IfxkFIGusCSohRa8H6A8x7ZS5OFo5GOSTgPXsqOGW2wzSxg9Gw91alPGucb6nGQ2KfLpnNwWBUl-BAPxz-v_D7U_UClxkDwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=Ghg4QJLSXwnywFnfz_eVfcOKOnwzsi6Y8z6kdXhvPt39AnKIwrHjvv-33zDk3q5pjgLXsxb02EKTbAeoaklRol2vfr_53lID_zWyfzYq-qhQjAYkNVrwotKsZRTbEXjcMEzGEJSQjQZHETl7M4ilne2s7LbFhTa7R8MJpKJqV8NyLmlsBrPFY7ZMG31_6ZBna9OxLrr1uSO8r-oRFOyrF-SgPrgt1nW029dhogj-LRyb-oJnnLQR1IfxkFIGusCSohRa8H6A8x7ZS5OFo5GOSTgPXsqOGW2wzSxg9Gw91alPGucb6nGQ2KfLpnNwWBUl-BAPxz-v_D7U_UClxkDwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به خلسه گفتن چرا تیک تاک پیج نمیزنی مثل بقیه رپرا، گفته دیگه من سنم رفته بالا به من نمیخوره تو یوتوب دنس اینا برم.
حالا عادی ترین محتوایی که خلسه تو یوتوب میزاره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/82758" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82757" target="_blank">📅 14:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-BCYbJv4wrDWmbE4h6Gnh3Q6s-pxaxq39d3q6Xs7LRcL-hnBJLfA7Oh8fAQnCOjgsGzyccvDWcNA_TArH-PkEDG4V3Pb4ReY-WH-C0mXZNqBR31jX6aCk3dljS2muBXLs0luuYbXEf-XwQy1byacfdlJP1pz3hwARglG0fEL2dbaH5OCPpvo1vCMFqIZO7MK1fqDecixg6SERPLgWAZpGlAL3EEZk1JyRSJqp_iz9ZdyDVQPgNoBjLYPaWPmCCbD-1yUbqAALIU0jlFhHaoJI1FpLizI27_9qimsvZH2qZ1UhcQkovU-BRtsUs9Qq8xqWvtf6zK3z47CtA3lxlzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوریا ادرویت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82756" target="_blank">📅 14:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82755">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدیونید فکر کنید این که مهران مدیری میاد مرد سه هزار چهره رو برا صدا سیما میسازه و توش عراقچی و دولت مردانی که رفتن مذاکره رو مسخره میکنه اتفاقی نیست
کاملا خودجوش مهران مدیری و نویسنده هاش تصمیم گرفتن اینو بنویسن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82755" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حکم اعدام برای ۱۰ معترض در اصفهان
شعبه اول دادگاه انقلاب اصفهان، ۱۰ نفر از ۱۶ معترض بازداشت‌شده در پرونده «میدان شهدای اصفهان» رو در مرحله بدوی به اعدام محکوم کرد.
بر اساس این گزارش، ترانه رحیمی، نوید الیاسی، ابوالفضل دادگستر، مهدی منصوری، احمدرضا سعیدی، مهرداد بوئری، محمدمهدی اسدی، آرمین غلامی، پارسا جعفری و مهدی جعفری معروف به مهدی خسروی، به اعدام محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82754" target="_blank">📅 13:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=myWOv0w_ASMs_NvJSTq7Hi9zcSXlzagYckVDq8ue0LUSZqseBV-kFVUevUOTpvxs_4m9YeGSQR8W0arZ9GJYlaeFJqIWd5CK5fwn3cvLrLQoeF4tiEy7RxWWXLE-2Xjg-7DCUZ1Y7N5OHZoHVtFkwc2vqWghC69fO16JNyQ62ejKxsNttuNp3ik7m1g7wt-OG-JOEWHxbLdaZFRX3xeDFfKINwcyu6PcSIOxVC068OgFrnEmn-4O8TocwrZ6mykIWLTrvPNeiaUPMmunXwoBlqhqrp1UbG3Cs09-CA7048Dn3g92EFG3PTJDnAbe7bXDxQlsI3DLx1rTUDf7Nj0UUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=myWOv0w_ASMs_NvJSTq7Hi9zcSXlzagYckVDq8ue0LUSZqseBV-kFVUevUOTpvxs_4m9YeGSQR8W0arZ9GJYlaeFJqIWd5CK5fwn3cvLrLQoeF4tiEy7RxWWXLE-2Xjg-7DCUZ1Y7N5OHZoHVtFkwc2vqWghC69fO16JNyQ62ejKxsNttuNp3ik7m1g7wt-OG-JOEWHxbLdaZFRX3xeDFfKINwcyu6PcSIOxVC068OgFrnEmn-4O8TocwrZ6mykIWLTrvPNeiaUPMmunXwoBlqhqrp1UbG3Cs09-CA7048Dn3g92EFG3PTJDnAbe7bXDxQlsI3DLx1rTUDf7Nj0UUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سجاد شاهی تو پشت صحنه موزیک ویدیو ترک "تا ناموس"
حتی اینجا هم داره کتک میخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82751" target="_blank">📅 12:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSPEmxlHQ2WK0XM6d-XDwseMTJyc1E_atigkMUTKpAk-Qk5TL2WP0GhWbwPotIXkvFHL5x3wPx4Z-sGJeV2aub_8OUtrdAQWlawFBsxV70nPXC-fzc2_L4kP8zUnMpsHjJkK8spaTCnPK4wvqYOrw4EXgnEufT3yPePMm7LRA0o-z4Jij1UEnUHQQHSRjKYQLyWk57ApxTz3pPuDtmc0-xRqreg9oZ3SV48Fx0tG2K8C8B8wfqs2EhrIyE_pKh5tlkRZQtMSM7BwBXq0kTzmxpcFaVTZgs_rBrGp62Wiif3lASJKwujgsIY0XjBgkTTU7EyYq4sVTPqJqbDqu9Sjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس پوری و مامانش
حالا سوال اصلی که دارم اینه چرا شلوار پوری جیبای عقبش جلوشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82750" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه
مشتی حداقل الکی میگفتی میخوام برم مسافرت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82749" target="_blank">📅 11:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=Cu29eHzWS8nS2OYcEXyxrzCiyKAnZDenyXjo9NQi4DYzI0dZ83RpfpO9jb2Y6BLfIBmmfk5XdHf19o2ZSzle-nAo4hPPw-CTDByRScSr_vUgutT5v9TPRGARCEUNaAVBY4YigFVx93g9qjcdmj89VvBHL-UdB90uKWSXm23Wg4TfEmBCD1TpqPKErqcE6v7wRnMIO6HW40jryJIPUK_XjnmgvU0cwFNuRDCym8xAbiXpu0t3ufIdC__DMO7NZvSJL234rY4JkQYOEHVoBDX6uPqw2nFCGjjt-3Rf0NI7HWpWs1HiJu-kuR1lCWf4Wt8pfzyuqN-jsPVtv4wErYqfTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=Cu29eHzWS8nS2OYcEXyxrzCiyKAnZDenyXjo9NQi4DYzI0dZ83RpfpO9jb2Y6BLfIBmmfk5XdHf19o2ZSzle-nAo4hPPw-CTDByRScSr_vUgutT5v9TPRGARCEUNaAVBY4YigFVx93g9qjcdmj89VvBHL-UdB90uKWSXm23Wg4TfEmBCD1TpqPKErqcE6v7wRnMIO6HW40jryJIPUK_XjnmgvU0cwFNuRDCym8xAbiXpu0t3ufIdC__DMO7NZvSJL234rY4JkQYOEHVoBDX6uPqw2nFCGjjt-3Rf0NI7HWpWs1HiJu-kuR1lCWf4Wt8pfzyuqN-jsPVtv4wErYqfTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا این آدم نباید رئیس جمهور آمریکا باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82748" target="_blank">📅 11:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU_HjQIG9-Ydh4-Tm2kHTKxCTiiSAjhVM6TLcx7gJnF6d_9Sn2-V3y9od5mBTbXPHXOS6Y5lgelqY_Eo1skTDF2j52pBC-B5mA-YwH7i8TVXSVn6y8oc4KXKz80Yllo2UdS0dHZqYginK0qSVV1apcRvqdW8pb2R-7NA1nrBhWCK9acuJCEKrgYlv7JcL0StTgLeQKUL1iqu-Q5vEzAcT8fm2Q_xMYeQVXXQQHwc1lox68LFjozRfqUWK5GUONAu6mwJQyMyPUYenShAMtzBzlxbD5efwweqdui4ntU84F4tMCL3C1TFaQchMn1eXKJJDbzAdk71R82ZFNgksKVaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش این عکس حداقل واسه ۱۵ سال پیشه
از اون موقع هنوز ریشات در نیومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82747" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEnlzl-Jnl00w2nms88YGYx71xanz3xUbMriNY1kTjaJJZKOfSCIcyRUhOgwVepUNsu3yf9oonnanc2n9Eh4odxTJ62mLaVRTDCWpaw9Y3BrvDF0c_Y8XOmLyF9qCl3Tqx6MfNG1Gqwcc4rhlFbCuRnmfrSOj67H13NUH8-dyCtF6WjDy2vpcyqB_g7zh-vkQ5rc7n4C3PZpvIDxVV5vHxAOZFCGV0u5JWhwXLVui6nCZ7YkyaPk87c90wW5Bv57f3ndUDK2H_bZhz7zMJd9yn2n8YiKgYwV8NlHo2J-KtiXr7YaxW-IDCdigNdl-RI6e0J3806r61fHODv-IXZuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز نقدی رولت زنده
🔘
🔥
با ثبت پیش‌بینی در بازی‌های رولت زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۱۰ میلیارد ریالی بت‌فوروارد دریافت کنید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/ROU
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82746" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSHMeHJOpk4M01QA6y03nxX_fLhpoS1r4wpr1C6Tzck9L8YM61uspYreq1q0VnOZ0KXvxgnUxN5ZMewvfWyskL4MYFfJc6ffA9F6zhtzPHMjXtF8YmSUcLq5aVLnq06QTvRxpDwbioX_Y7DFD8RnjvD0o4VgVBtBptkda8OTp0yMC0l4T5_GUVlefw3izf5hcrEDgSZv_amYx07MiXF1vw9tWEbxuy5Pd-UAEVKni3ayzUW6crcrYkBwiTCPE7Lc6D19BvgEQ7MX60BQcQ5j-lwMhpIxTi-GdDGY7m1QzlCTr9fg1aH2sOYimMoDBC_SYPEZ6cyA41kQyuye9d2-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82745" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جدیدا شات های کصلیسی بیگ شگی هم بیرون نمیاد دیگه، فک کنم دیگه دخترایی که میره دایرکتشون عشق میکنن باهاش پخش نمیکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82744" target="_blank">📅 01:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDOOr9MHFF_idU5CBPFcGS7lN0KtdmWib9nnZY4oeylL7fvzRqHQ4KW8LFV60XmbH8LS5MshBXGhnjN-5sYLyRYrJbUcO86frMxibLFDRRSWXK6jyjFecSKJrsrrBr2UU5cRHa5vyivzFiWx2sXw67fx6rz8xoNTXTPDQGq6rCks_7LEoTClNmXOmxymq-uc0QkGpm0oQDTTiISuuLWDwRwrMc8MPg64UgPfhdmeGgYnnine9lYXfPskZRMK0z5i5YXgDDbB0JHZT9PC6ryfSDLzXclCi0lmpK7A3j0PYb6ousZ5V3nd8GcElaCq0_Dd92pHYlle49X1Kf4u9LshPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی‌ رو دخترای خوشگل میکنن ما میدیم
یه یوتیوبر(aj king) میاد پیج دختر فیک میزنه با هوش مصنوعی و به نصف یوتیوبرا پیام میده همشون هم روش کراش میزنن و برای اینکه ابروشون نره کل چتا رو نشون نمیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82743" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=OHcXsJYB5iufWbPUJO3zulIbFcb1wjg2Pg5iw99t27hIjbfV9NSe-zR7eAuF0v2f-njdhI8h4B53xoQy_nBualPkzK83c1LpBokylBElJMPH6wQIwuMKSxejasHZlOA-2dETN3uYOGFix1OoalF5DNnnR1pb_Te1YOcZsVXetXl2oqp2kTJv0TmxEM8hpzBhSnxHV_c2onxrL_ImZ__rwN2ocXywKmzWs5f7qPtfbHaDPsQ2Ye05FQeCPROxCWOwvLNrpaj1zmM_0BbIVm_3pRrhoMd-Mo09GZkuLu-RCRW3OvAE_9tHd5ju7AMhocwom4V_bhGp7tclHx2N5aS9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=OHcXsJYB5iufWbPUJO3zulIbFcb1wjg2Pg5iw99t27hIjbfV9NSe-zR7eAuF0v2f-njdhI8h4B53xoQy_nBualPkzK83c1LpBokylBElJMPH6wQIwuMKSxejasHZlOA-2dETN3uYOGFix1OoalF5DNnnR1pb_Te1YOcZsVXetXl2oqp2kTJv0TmxEM8hpzBhSnxHV_c2onxrL_ImZ__rwN2ocXywKmzWs5f7qPtfbHaDPsQ2Ye05FQeCPROxCWOwvLNrpaj1zmM_0BbIVm_3pRrhoMd-Mo09GZkuLu-RCRW3OvAE_9tHd5ju7AMhocwom4V_bhGp7tclHx2N5aS9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتاح سجادی رپر با استعداد نسل جدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82742" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=f6wYOFpeVhh7tn-5_qv3ZmzVR3DKrJFFijOB0ZtqOcYDHpoggph4oqVMoQcr6dWa7X70JK57Iw29FTByJrG5RoLUdbdbLIj-rSXgKG_K-7lPQBXfgZg2kDUwHKPA9rzN_4TLzYlDtD_YqlkBsDtKCrzBSSM6aup28L4LbSRvLvnKwatEWSVNRerpBfXwg_q03MgHoHrF7qCmrEo9yU3uNCvn6HLP_iaFVScd2sJvo7gxDxHuSgegqrMPvZ4tX7ewbFzwv6Kw48LHuUDpgABwOTql47KeTA4TT879C9VlB5_E_LbrmU4FQbodR46ped1RZqWAZlDTFQZs6F6NZZurTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=f6wYOFpeVhh7tn-5_qv3ZmzVR3DKrJFFijOB0ZtqOcYDHpoggph4oqVMoQcr6dWa7X70JK57Iw29FTByJrG5RoLUdbdbLIj-rSXgKG_K-7lPQBXfgZg2kDUwHKPA9rzN_4TLzYlDtD_YqlkBsDtKCrzBSSM6aup28L4LbSRvLvnKwatEWSVNRerpBfXwg_q03MgHoHrF7qCmrEo9yU3uNCvn6HLP_iaFVScd2sJvo7gxDxHuSgegqrMPvZ4tX7ewbFzwv6Kw48LHuUDpgABwOTql47KeTA4TT879C9VlB5_E_LbrmU4FQbodR46ped1RZqWAZlDTFQZs6F6NZZurTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارتون عالی بود پیشنهاد میکنم پیج تیک تاک بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82741" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz1Letk-rcosctLkq541LMti_r2kLjOaF1Dxn9lufqKjo236i1lobjqx9xmyGFIs3as1XNHCpbAf-ng0CsETJu2pe05Gvvq8KD0S8rf9Q5JnszhMrm0zYWflMpCQZGSFtZC02wW-8EX4ornVyZf_ghwNZs1XdqyRjR_Xl6QHcfzA0gExBf10-7IkcQI4nWtayNtqG_RUKsiSTTYEmnSqTasmVfBSb6d0U37snP89wO7sIF0Mi6g_yrSfydGBwBjKZ3_O_XzCLPHtWuH_hTC8csH-mbk2UZzPDcDe2r8Htx83aIxkz8HtgxWfTVeqtwCgT2IITeCRe5x-0qk0woB3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82740" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732d114172.mp4?token=DnQAFmuFmtVsBac7dkeQ8fpnRvsxp-WcAgoUccw8GSKnaJBhDyDJYoFAS-OvkGd7GFQZPVHChYpHh6wY5EZvD4dESdTNwUQrNLjQTLKhJfla_CAKVfCXoyqoNn0aXAlTXcrx-7w_EpOSmalVCxb00LJqzudMcC0uL33ZNzt-MAZk7kTGkTM8e_K_RUgLGDUnrasu8joDjtweMUIjkZbMyLysutqo4tuhG8sKFPlXHezctl6Gw43OfoWiviYRehbP9Ej9mWtEbc_m4L4EuTIsHZLG6A1FQuYqojFL2X8LQdI8MFeCKzb-UEOVyI5w1EcckbWR66Q3v-Si2Bc3pnm0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732d114172.mp4?token=DnQAFmuFmtVsBac7dkeQ8fpnRvsxp-WcAgoUccw8GSKnaJBhDyDJYoFAS-OvkGd7GFQZPVHChYpHh6wY5EZvD4dESdTNwUQrNLjQTLKhJfla_CAKVfCXoyqoNn0aXAlTXcrx-7w_EpOSmalVCxb00LJqzudMcC0uL33ZNzt-MAZk7kTGkTM8e_K_RUgLGDUnrasu8joDjtweMUIjkZbMyLysutqo4tuhG8sKFPlXHezctl6Gw43OfoWiviYRehbP9Ej9mWtEbc_m4L4EuTIsHZLG6A1FQuYqojFL2X8LQdI8MFeCKzb-UEOVyI5w1EcckbWR66Q3v-Si2Bc3pnm0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار خلق کردی علی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82738" target="_blank">📅 21:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82737">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vf3qIcqbZyugjaUdPsIn-HwPYLpeifDBeWKDuYwypZ-mFO_YznaacEhf6r3MBPbnBi_2tUhtom6oC6PDFErule-ts-9uyPJATYSsqejZ9XdvVLYmY-r6pFf7OOMgZRnDuWfEcUPiNXjK4KFbG2ejDdZr80Ez8FDtDegouNbPWYIUzgbgtbKJwbfaq4Zn1AS3XaxXr8A1owTdbUsaavGTsqLsoG-7I9FovF4mQ9Ty1rTZy9vrwSY-6IFdCefLjrRoCEkRnb_0ELhEuKsROIvGPsm6LvHMdxFPCNDqtV9K5LOiAevuUnQitfea-tR0vpJFR4E9hyy0HG35wMQ4xM-6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نپال قبل و بعد از سیل
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82737" target="_blank">📅 20:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82736">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgF8JSaRt80KsO56BnNYh6g9JBh6QcKbp-LFSBZ9r_PlWf4m7c_dmIyO7XNjPs_VGJ3BWoUtCIahkNL4ojpPgMKKroiuAC6JHX1NNFx9UejT5BxXIGMty2-zgts0p8oy4AXpde663PjPoJXQLAcPOTDz_9JjGTRkUpX7la50JmUctx_EIuoHRboP79Zxkm6GEbO2sIA0CfWSoH4_D6QkDD27XbrXr0Y_h-gRF1SDIcHbEelSGlieTu1L1BzCDEcoJcMZx0qGYFoMMOFlBbgulSAo2xNOhEgaKiD5uuqCBfDDhvrlgHi4FxV4Plo1zAeFImI3fzztvvoLUB4l2evrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلور قراره قوروق بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82736" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82735">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_hAJ5s1i8RV4lh_TewGPcC_R0WzBe4jqQGZ9lklYivT3-PhinCidoUCKwKJJoJWeBPEM8OUI44JQRdE5E1shW8oeOotkcHrFOeFA5ympnZY_27GCrbV9l2lCxanKlgzYtKKI_VliXbl05KpQ73EO11RvPEfhIxgAeKpfaAmRHov7p7PBWDJgEKhcR_T3sK7Iey5JDJSfmYKMcWWGDJAidsF4wUr6-9ovc-SxuhFS1ArBgoXQQTA0fX60KByrnpZQnDwPiLcxWGbT1VqeazmsGyCJkQdBEAlWPFqqx9p_qWiExkZwM5DlpbErb3WQvUStMPUSrpoN7CWR9ezj2qhVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری ببین کاراتو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82735" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82734">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojR6llyB2KPRWNVtgCaNHMgFseyqfAw-DaoqJEIklCEo02FZWUQ3fOLSzp20fxtnqacrLfjn7v8I6ESvarIAaHLQH7bQOc2gH3qotIAUcsuOAemCAv-R_i3-nBTPfHFQS_zZVvvJqgnpf32Rv0hahYMm9R6b_yytK-jt1dQJOaNM4YuTDBaxczb_TzIkEflW19p0lct4DRhPuofLgz0lhsn1NqKYWH_hpiRDjHlmRsX6s3dRsCT3jkwvAJvZAWnB_f42iwDVkXBU5MjFzehh5XbYLQk-FmnO76uvtxkm7WhmWsJZ6OhHD2KRmdkpp3eMKak_6_8uQNoEQDOEoX9peQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا وضعیت سلامت عقل شاه مملکتو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82734" target="_blank">📅 20:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr_S0mlXanzmwoLvZrC_r8wDLgxZAarAzkVa_LjHmB_jPhQygQPc7cc4tZSwuJ5r21rT9jfd6KszJ3qf2VhSEOC_J5rb3HMGfsUDE2DcHMQ8njOI2FFQBOfGQsPa0W8na88GJF6oPmbc43bIsP3ffJQzBGk-mUpNq0SYZLz4NsF9BLOCIgK5YhA27d6guf5jk7YCoUI_KIeYakC7NqpaD1AHlA5xfapi07bmAmACpWaWZO1jXoaL-3RA3yQNXylH7LhQK4n4mpx5HU6qDuU83SKDYIzjen6ONhBhNwlZrm96goGnrnCqrYWk0px9XymJxOPrkqTxKKY3CD7zXcGjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53fb725890.mp4?token=eCnBcFKvKJwyr-AfwPL8yetjblgzsHqhomJ2xTPTToggDwU0h7yMIEv7U-cE8g_SbfJXErSF_ZWIWQmnfuA15wKyHOCFZ2Ib_NVbAZAYFlvgoHuXadK7DVFr6qaTqtb9ZzDKtBoY01VFrbHLbsTClWrZeHgU_JT3Tcxl6mjJzw5mMwU01xSrnow4zArXydUqa4rqv1nwMRuKGSI7GE46SZOZR-IBIji4yP4ILebKd_1uacpbjrS9ovY4S3P8DCT36q_uivFNdgqdbjusxn6_oXdDnFh3iygRUDx8NonzlpDGykVtD4_HYkppcf6gFc7Lci-pEqE8HAFkQOZWVkQl2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53fb725890.mp4?token=eCnBcFKvKJwyr-AfwPL8yetjblgzsHqhomJ2xTPTToggDwU0h7yMIEv7U-cE8g_SbfJXErSF_ZWIWQmnfuA15wKyHOCFZ2Ib_NVbAZAYFlvgoHuXadK7DVFr6qaTqtb9ZzDKtBoY01VFrbHLbsTClWrZeHgU_JT3Tcxl6mjJzw5mMwU01xSrnow4zArXydUqa4rqv1nwMRuKGSI7GE46SZOZR-IBIji4yP4ILebKd_1uacpbjrS9ovY4S3P8DCT36q_uivFNdgqdbjusxn6_oXdDnFh3iygRUDx8NonzlpDGykVtD4_HYkppcf6gFc7Lci-pEqE8HAFkQOZWVkQl2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه تو خودت تو ساندکلاد ۱۳۰ تا فالور داری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82732" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=SKK7CIAWPgdTiLKAsds_j3z5BAx3LR7ywgfheIxznOX-Gc48lPdfWC7HJF_0Ix8NQD0q5wO1JFA0Z5UlLMJQxKuxwB1fxSFPJj_ze76V1W1NR7Wz91VCwwJViCRMH0Akb3x8ftf7Zo_B4cf5UdetIfs6HgzedJfZQW9smpLsF1JLKCi04zi3AzlTsFkYHxVxzFMsH5lqV-RI-xjy3c-qUcQmQbY7cCOjzDl3QvBtsf33ioGUN6VGxaRrESLxrqy0We3drShC7-lGnoodri6wRYy0IQVn8TLlkGTCgaqSrfB6ZE9NiqmDpIcvvV4xr7ICSFmvE50nLC4daAl6Zpmc5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=SKK7CIAWPgdTiLKAsds_j3z5BAx3LR7ywgfheIxznOX-Gc48lPdfWC7HJF_0Ix8NQD0q5wO1JFA0Z5UlLMJQxKuxwB1fxSFPJj_ze76V1W1NR7Wz91VCwwJViCRMH0Akb3x8ftf7Zo_B4cf5UdetIfs6HgzedJfZQW9smpLsF1JLKCi04zi3AzlTsFkYHxVxzFMsH5lqV-RI-xjy3c-qUcQmQbY7cCOjzDl3QvBtsf33ioGUN6VGxaRrESLxrqy0We3drShC7-lGnoodri6wRYy0IQVn8TLlkGTCgaqSrfB6ZE9NiqmDpIcvvV4xr7ICSFmvE50nLC4daAl6Zpmc5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر چنتا قانونو با هم گاییدی دلقک.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82731" target="_blank">📅 19:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OITO3E9J5OlPrQ_5E5LAYkBoxL0TaSAtSwoHkKNnUR4TbQBP6ipCBFxMEJSJy64ZnkWs9jnP8QvDZlw92pVqEDtRaBd9SX6PR7cyytLMaFi9o6HBA9veJBaEl0xT0LsKMcC0qYeOFwFTBhmtGXfejdpiizL2bADqZnsRrFR5Ltxk0vU1CTcdRWYkI8brf5VaJWDpZ10Ey-lCRgdRHF25cpbiT7F9iIw8f6j2-LU_JT6j2RPD1TAr0ilI2VPinsVFwozCtSnoEpf2dGi2hsE0ktEyzo2W7pNxhL__3W29PvCUGEYgyVLTpsb8jJlMTBFTVBlbMKJCdtJ9EDwOaDxxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۵ درصدی انفجار (ویژه شنبه‌ها)
💣
⏩
هر هفته در روز شنبه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در بازی انفجار، در صورتی که در همان روز حداقل ۱۰ میلیون ریال پیش‌بینی ناموفق داشته باشید، ۲۵ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BWC25
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g7
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82730" target="_blank">📅 19:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTI2DDwnXJz0Q15k8ugsyzH9Fbjyz_svFXAY7zCU9geWDToTlWhI7z-jUC06MxvdJ0jhSBfPO8h8Z8sqH5NhYRh-5ShJ6FQ0yRjEBaSt2KIJlecOkp5wjoCZjg6m5LU1doN_RuSvehuT1omBBxckeRsvb8y1EFJhoLnCfzd-ux3WjNIa4K9MJKfPJDBjGAY9h3hLrvrhidijDBRXyTxDCNGHv3-3pUvtOz1bAZvROosAT95Yp0R8AzBddQaNgcT7k5ZbMq5V3ICHMrzwsT9rnPYfaxsqMV6T4RIz3M3Yo5GUPQWvArO1zvPgiK42IdY8tlVmjy9rSQAVc1l8ooAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت پولدار شدنه پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82729" target="_blank">📅 18:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اون قیصر خواننده که اومده بود ایرانو یادتونه، حالا میخواسته برگرده بره نزاشتن، و الان ممنوع الخروجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82728" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تنها طلای این تو کشتی بود که اونم بعدن معلوم شد دوپینگ کرده طلاشو گرفتن ازش</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82727" target="_blank">📅 17:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82726" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBb3eWGyPbWnsm_dRAY8oL1Oqy4UuW1yossuldVbbgXQOBU2Ffwk63VbMxjXwZSmwMcCZHxXyvQVmlNpMQ2CnfgGMl9i_7zjNjTo7l07ZRPFBL1-Oej3dxv9irq1L5aEdgxf7ktXXGFjm7hxMl47RY6dfNibxbjwqAwb8M3Df4Gr3MxW4gVCtsrIzwzk2cdYriOEfbPfCnf-ofy1j39S0s74UotpmvBZICHtkJFjcdNSEga7EVYPreoAIhY_nz8F-52xAIkPREWcYhgxcbDk-8EXqIrS5SaRNJEHJ1MFV5FGW7-XraWKhkG1ItCUuTtfoCsHGvFsVBIJ-RjP-7y25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82725" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irpMI8JgBTsIktuMTG6hkCqaPAkznGObE9BjevUyWZL4AkaYi9E019vsyQ5VAJPr6EYRCu0RU2s_F_0eMIqsr5JxO8X95jIBT0sU6rCaMegTL1YqiJNJM8gMLOdyUeM3yn8oTh65x9q8xQi9h6pvL7J3wmITHhne_SCmfItdE3vlO_dsaMFGmfTma6Gn9Mp_oW0-u703aGdXE6ERHGTSGANVPbipX0Djn-EYvHJFxOkQ-znu-4TN_xzoUnjCBgJLnUIcoakwsui2WiF7TOPsV4owTCQwRwbdFGUYCJ0TTN1BSc6CN-uBsyxhJWE_B0xIzsTgLb3Rhul8rwAYDbIGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت امروز گوشی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82724" target="_blank">📅 16:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خاکپو لیورپول چقد استیل خوشگلی داره</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82723" target="_blank">📅 16:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIjksVOtXd2Lu01GHK1Z-Qnarp6n4QgVD6FCM23z7DYNxpLaIGnHlcbE5hHKq3IQ1xZeAPMWkxuza4nQuRjWwf_E3aPEVbSzJJk8bGlIX4qbD1STxGOrxX4Ams-HLtFSbbRmQ-v6yzFccoe_eWQgFY0BHN3Tk_K-9jHGNsjmwdVX2MJlkVseaHQawG5Qx1kNv1oXGiQLSc_FuOLojZmlzAoSmy5XqFd6fDOcuY0S6JWwL_awJNGp852-nuJLndFeEhySi8qE5s7ySIxLmVUdfBEon3hxM3wWF54b4Om_7Rl-J99xMBkVpf8AKjm_ioFbMf1HIjFKzPisK9tGSeoQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور سید عباس عراقچی:
یه سری اطلاعات کیری خفن و محرمانه بهمون رسیده که نشون می‌ده قیمت نفت و بنزین خیلی بالاتر از ایناست و آمریکا فقط با خبر و اینجور چیزا داره قیمتشون رو کنترل می‌کنه و اسرائیلی‌های بی‌وجدان هم می‌خوان رئیس جمهور ترامپ رو با این خبرا تو جنگ نگه دارن ولی مردم مظلوم آمریکا دارن این فشار اقتصادی و پیامدهاش رو کامل حس می‌کنن.
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82722" target="_blank">📅 15:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHsFaRkAFE-NgJFuVMfzE9uS34JWKK1mO0WBPWKra6OQqzr9ia0K0B851zYZo8BA8N3VMRwSet7WpQv4O382m4nnqqdkg8nE1oTMFYUNMGtxPqRnl4SIjIU3yUr4LOZcbHPCUxGnfPBo9iNuQX-Gn5TiKwC_U2GnMgsVKWcEoF5rguUl7_UeiLgGw6CqfCLdbgsP7NbuskRopw7-x-oLbPVhVWXZfUyAEH-lKLbIKJ4Kcnt8HvX0pWTm0T5G97-JZaWid4m9V-NBwCSxTPYNtjPAMdEWtC01naonax63hconpByp3MFZTJXnVgfX8pJt1UhgKDOeZ84shGelUdtRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نوید یک اصلاح طلبا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82721" target="_blank">📅 14:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته: یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه. یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82718" target="_blank">📅 13:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82717" target="_blank">📅 13:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUoBuft6yRpAdapsAzFXqfuvMURfwPHY4CbQaUueVEV4cS8M5HujWH6Nw1cdT9tO0PYS7sbjxGF787PKkFqa1vM9dAHCiQ3j7p6CLwQbDCV8UBkULxD8JrLspre9dO3TCYQtuXKYCc9jcRN2-K6WBS2MgHvJHqzq0WT6KVV9IivcoKZBjtxcDD7sfABNzADenXTwZk4-JSVaHHrSeSMD96BzrtY0ZRvGzWRUjltv-x8Mr2CHAob0GiS2JhQDCIOYqddonO8viAt8sgyvQgH_kR7WeddS8XqQzMyQuNMoC5_9fSS1tRTKH1Kynqh5Io4024b8RkGK3ye47I7QolIUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82716" target="_blank">📅 12:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr-F6sSJFqPrx4JcFtqLkSVb0UjErFDby3fQ8pGW_cjkfWoOY1kPXkZ65IWKJQrisS5rEGEkacGQFcWsxsglnHo2rKHXpbD91EeLiBBdUaRmOxwHErj_oOJPw5LplPJr1UGER3ZWqIKYZQCcrN58uA4H0LnEEcra6UycLMEbr_l3-x_zkP4obyHY8TkSvg5UWtfb6_hS4WvFInHawPNRycuGQgQ8rTuaSwcNBTxrvd7HlW4zENFGDGJnIGGlrDmgitYSFl6NJJ9kf-YT0MC-XvSSHFzR4KFVzwomPwXwEFG3JcrXWFch9iTyhelfl1kOgsTAinyvW4fQwC5M7t-n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن سابق و پسر حصین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82715" target="_blank">📅 12:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Va7rBY3yjF1pXfW4tbpjhEP0wOhfUFAZ280Ku_-Iud2nHOL6VtDaYAEUKFAP8gpTzH35lvagaFc6UxmiG2lf4XJLZp3E-MFdY6_l5X0-e9L4BfyOGKys0h2B6jeCqnz4q2jR6lPB-OfnHoBp6bBxFSbyNS55BlLcanTHBA5pyIBruXC95B4QVo_cxvfRdXoZKQBBt7anpzoyzmRiir8PG-0m8AKtuxkjUs3R94nujSgeF6CWAdD8WrN4C15Q6fRLh4tjXHwozwbjZa65B5qQZ-mX1pUGrJ_3_2fv4cG1bSQrWSoFfvy7jv-1n1Gc84K9-okaIAU8MN7tVcbHVs9CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jamXlkQg7ceFxW0u5z-Tk9vYh3i2ejGyB2ksWh-wfl5VWqzhK2uXvW3rtXVeoYb8rv7M-wW7gSBXRMvr8RHOZzOK9ObNeZLspozPZyW5SxMTF9m_WAOEdWgefQKsmGjZ8NrcMpydRNq4o6Uh9gVvCZv1I1_DT5y5LT2JJvRRh4zoeLtNP0dPi6-ROndoKLktBFu430_Q7_umEJNPBRj-hgcNLos0oSAUa02l4VOdg01VqdDjVZdKx1XAUTArxs5ds259u1Z4hb_IFkuAM3rbfwPOc1AmSV4KRswi8t7Vxewv8PqS960buZbJ5DmU1SEt9vDQV70-QSKtPYuFbscjSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82713" target="_blank">📅 12:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82711">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLV8aBu7YosPnnmwBF0rNZ5U8RgSNw11W0MRifAweqlgr6c12n5cpSjSivnO4_4w7rw6hxT_nO4EzCeGDbqV49DvcP1E5vlCU_yXoh8_0PyFkQvu0zuKpUap6xJPIqVl1EGuboRQt70Djo25HQQ3BT04uBCSJtXvy60EW877VTvTOOiC2GELFP-3ECXqvfUX4Hn2QmV30K9osHuuHbhUK-WfWa6ultQ9_TveQh3bCdHSjzQkHmBznXi955mmEScFO_o2AQZwO_vuVQ9IQju98hsC_hVg9Sfq-G_6fyxO1BsjGt7Zg-PHDXMugYJEnmTnNlJIbJdoTyuZrVBVV2oH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه فن اکانت انگلیسی چلسی اومده یه ویدیو از ریدمان های گلرشون سانچز درست کرده و گذاشته تو توییتر
چه آهنگی روش گذاشته باشه خوبه؟ پلی کنید بزارید رو ثانیه ۳۰ میفهمید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82711" target="_blank">📅 11:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82710">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4AkptoH4LUNmwd0R4WQssA7NXC989Eyy7IyVaQpDE2PZa2c8U_wruYoF2POfV_WU5np-Ltol1OcbsKR9c_aZaorM1HnXg8ObFzl1FE4jzLaPGTa1nVO_ACBo288lsKGXEt2B2A8job2sTfUx-pDrzUjm1CCCXlWuXjqBM3lBELSZyfqjlxjTBK7W6eLjbj2QgU8Nm1LQIYh9aoTHQugn4mItsTKpNhKSnXXHsvsgEGTCoS-jcOYAlAui8MqEQXXnqaum8uUu5hGH_bPOrZdtus5ICoUyGCO93z24v_4gv5prfp4zOBSgeiJdMfWfKX2ocj4iurtYzJV8O_Lxdya7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۵ درصدی انفجار (ویژه شنبه‌ها)
💣
⏩
هر هفته در روز شنبه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در بازی انفجار، در صورتی که در همان روز حداقل ۱۰ میلیون ریال پیش‌بینی ناموفق داشته باشید، ۲۵ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BWC25
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82710" target="_blank">📅 11:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه آمریکا قراره بدنساز بشن
پیت هگست وزیر جنگ آمریکا داره به نامزدی تو ریاست جمهوری فکر میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82709" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82708">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449380bcee.mp4?token=RPLqRdWpMCUrxFiVcH8Igxdu1nAMJM66CnM5xnzd1kAYSfzHaX3tm9957CLUtwm0H_aGtqLJsZqskxv0JC6tvgC4AKeF0LCLSPmpnk7lhv3ZlUnHIwmZwFuCX2V0hD1PEphrxeBMT5MoL0El9qxCRCKq90yeX6kR5Uq6QOxUypg6nLYcs2xroO_411et8U_bKshqXrlgzAceyQt9IPRVW_iuI2rqfYpGfQocKmNxZwc6b_i1l7epdqsh9sAxPSxSEqpOmyUo6O9LAnB-ag7t_vWkgOrjMdMwjG8RDCbc1Deix_7A765DpTouDbRcKICPzC6VzVdJjj4qz08ZjGCm84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449380bcee.mp4?token=RPLqRdWpMCUrxFiVcH8Igxdu1nAMJM66CnM5xnzd1kAYSfzHaX3tm9957CLUtwm0H_aGtqLJsZqskxv0JC6tvgC4AKeF0LCLSPmpnk7lhv3ZlUnHIwmZwFuCX2V0hD1PEphrxeBMT5MoL0El9qxCRCKq90yeX6kR5Uq6QOxUypg6nLYcs2xroO_411et8U_bKshqXrlgzAceyQt9IPRVW_iuI2rqfYpGfQocKmNxZwc6b_i1l7epdqsh9sAxPSxSEqpOmyUo6O9LAnB-ag7t_vWkgOrjMdMwjG8RDCbc1Deix_7A765DpTouDbRcKICPzC6VzVdJjj4qz08ZjGCm84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82708" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82707">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=qYx6vpWm6ynUWKed85_Qmv-hP8jAcSvsyIVApJh2Jz3JvNisaCiQ9mzMJGpSzX1E34vrzP_aFa02SzcMUcSsQEFM2vXLn3d5s2bJm7S0dIQWWNZ1T5XXuMS3CtkL8y8Gmt4c4PcTivYRno4B6MtZWa06kLl-_DZPfXoNuHvDwFIBEYdyRTOx3B4_qIehqSFP8W7Pdh0pTMvWqk_RayKbMMfuAoJL5nTIKtRYAR84NMOL2buqZ8zzs_DN_Xd2HkG2ZIhDNeq4V7LFjgOHQtowNpfj4FgMMq-hvFeXNK1DPA9eHEYjPZrBgposi-RaIKpFNoHyeK9mG5TnUrK7odkB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=qYx6vpWm6ynUWKed85_Qmv-hP8jAcSvsyIVApJh2Jz3JvNisaCiQ9mzMJGpSzX1E34vrzP_aFa02SzcMUcSsQEFM2vXLn3d5s2bJm7S0dIQWWNZ1T5XXuMS3CtkL8y8Gmt4c4PcTivYRno4B6MtZWa06kLl-_DZPfXoNuHvDwFIBEYdyRTOx3B4_qIehqSFP8W7Pdh0pTMvWqk_RayKbMMfuAoJL5nTIKtRYAR84NMOL2buqZ8zzs_DN_Xd2HkG2ZIhDNeq4V7LFjgOHQtowNpfj4FgMMq-hvFeXNK1DPA9eHEYjPZrBgposi-RaIKpFNoHyeK9mG5TnUrK7odkB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82707" target="_blank">📅 10:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82706">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نمیدونم چجوری بهتون ثابت کنم ولی شنبه حتی از جمعه هم تخمی تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82706" target="_blank">📅 03:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGsygfLSv8dSCI2d14kxsfXBp4ncAYAylYFHRuiaGcDCls81weCoR8MaFfboC2JRpIlFhLt7Sa1E2hU8nZ01qMG9S_T0gB1L1SsCjV2kL2fo8Fsqblo0Yb1Spl3CsXj7Lg6g28iQl0GAuUcyFSauTvDECeJbIntmlu4R2zl5uIbq-vlBEz2CvLM9FnRivpTg2U0ABBtJ6JWmjyQlhb3dMKQ_Y0QUHyW28O_bc6dqyYTwpZcHOWOyt5IQepp234hShGFVD6t-_f2mCYHeOy3mlKsIK9afjzB6myPFdvDo1-nPmFvfPKI1ZAbt18ZeDQmEFKWxWRcrFN69KUucO01NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلی بازرگان: شاهین نجفی برای پدرم با صوت قران میخوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82705" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5zLHDB0l6JyjO6P3Dpz69zqRZWIhGCVQugs-9hOsy82daPkSzlJ8S_HM_XcYmBhIqK3ggkF36ggvBbw850Qfl1Pe4pXKDrLYz_GLPOTUiXqkveS76EZcqlf6dyNHz2ixPp4U0E9iJt_-D0XHrdpIONLngULj7ZPeahKvqBLtdp63ROvYSdPxb-BlMEilZ4pJFPJseDLcHOXuJq8GG9-HNn6XxTkDn23QgireEtVQEvjDioZXDSPrdxIk2g3sspJpVQGyIg3Eptahav0PGa-9N3gvu2ZHC7mOWxXqppRUt0YYiDL2SjFKn7as7q7QMHkGxvNjIUwghI9ErU4aPgrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=nLwch6sJpLbn_lCOi4MMWlkSRO7KxI6ySoZMfoeXKPIqKBj7FwM-o2_USa7Umn2PET0yGvxdSMWT2eKxYJPlw-b6z-6U46db0UsgbMxt2V7pyYe7aKApNdEIUCw8hC7xFaNN1InjhHF1tywfHoY6K2bQ0QrnQbOSUOKEMtIdKMIp8SQTIA_ykR7OY_mrUNDRqiPzdSuCDC16XM2dKn-T5L8q2tvG8CsfvhXtXfXapIrmdqTnJ6OA2a-dzMgPygSDBNVIZW1Do1I-xJWda1sCm00u0FxHL26b0ebttr2PZjIBA-qTAFjMxRg4NBc-uGH2Ulw11-92U4Qldog5FcZr_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=nLwch6sJpLbn_lCOi4MMWlkSRO7KxI6ySoZMfoeXKPIqKBj7FwM-o2_USa7Umn2PET0yGvxdSMWT2eKxYJPlw-b6z-6U46db0UsgbMxt2V7pyYe7aKApNdEIUCw8hC7xFaNN1InjhHF1tywfHoY6K2bQ0QrnQbOSUOKEMtIdKMIp8SQTIA_ykR7OY_mrUNDRqiPzdSuCDC16XM2dKn-T5L8q2tvG8CsfvhXtXfXapIrmdqTnJ6OA2a-dzMgPygSDBNVIZW1Do1I-xJWda1sCm00u0FxHL26b0ebttr2PZjIBA-qTAFjMxRg4NBc-uGH2Ulw11-92U4Qldog5FcZr_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هر حال کمی روغن میریزیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82703" target="_blank">📅 23:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a822db941f.mp4?token=eKGGVpRe_6FF96i4Q7Ad5L_fPRUJogw9XKsZkGPaDOzHTEKSwM8mgF3rXhEBzpeBkFKi4X_KtO1NI9wuWnyctYsOeRcY_eziGfz1OxImwF08fdhO_EpQ6Di6m1c7wAizW0aXfvK-SmJUvsMk1cs7yZ8RV9eKwaYX3xPt-new5LI539thFwo2Hul5Jc0IIm_M-B3aia15ZtrDsGQp1ryKXmg2ZRcnSBLBc-eJXw9JBww7xVZgNUgkSOVbIC0FmyA2A5p4I_3WVEuf8p8MqPmWtyp-PWo-zwK3ooCdp_rQboDsMYZSDISD1kU3-sLrz40xCi1rIKIOcD6BDtnFedHaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a822db941f.mp4?token=eKGGVpRe_6FF96i4Q7Ad5L_fPRUJogw9XKsZkGPaDOzHTEKSwM8mgF3rXhEBzpeBkFKi4X_KtO1NI9wuWnyctYsOeRcY_eziGfz1OxImwF08fdhO_EpQ6Di6m1c7wAizW0aXfvK-SmJUvsMk1cs7yZ8RV9eKwaYX3xPt-new5LI539thFwo2Hul5Jc0IIm_M-B3aia15ZtrDsGQp1ryKXmg2ZRcnSBLBc-eJXw9JBww7xVZgNUgkSOVbIC0FmyA2A5p4I_3WVEuf8p8MqPmWtyp-PWo-zwK3ooCdp_rQboDsMYZSDISD1kU3-sLrz40xCi1rIKIOcD6BDtnFedHaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکوندی شیر
مسعود پزشکیان:
نرخ سوم بنزین از ۵ هزار تومان قراره بشه ۱۰ هزار تومان ولی زمانشو هنوز خودمونم نمی‌دونیم سورپرایز باشه بهتره.
(احتمالا بلافاصله بعد از پایان شهریور)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82700" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjK9-UIfIdLChW6GWFWXRFiX75Qs-2sRQmC3rnpD_D2X3EJWDS08jXUPi4FoNI4ak7oFuC3zoUvlnoU5zRfmLLRvQqPhsfQkPzN-aMWRNhXnAj8bBXmqdzPx2NXETK9dGhpQ03pV6YRGAruNTr64zKc0yvrYhuX91isdYVapmbRNBR6Wryl4EmYiKOmM2A5TKzXeC7i6H2Xi3o_gfkvjdihO9bt-rnc7PcU4CPf5sr4FRam_wNZX3uxvHFEdLQ8TjNUZLvLvaMponVFTRBVrptBnRnDpgVZXToKDFOT0srzryaHR7_VZM2-WId_rdXV13kJf8jZSapDZdEVC3Zl9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای تکمیل بازی Gta 6 بیش از ۸۰ ساعت زمان نیاز دارید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82699" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnSLAKU4hrmeTkQgDXRhyOd8SBxCcZT8ykahBl1IQXV6UPIpWY5qJLj9vXJiRziB98UURb3cqMw0ubskpoZJKdnZlIcO0F56wVzoBRE6nRHd9pNx67M3-blrCBgypQp6YAkQPZ7PwAuZ-VP8b0qX1yg-pA1mqASbj-DMiaAFar0AFADgE5bgnrE3FFolsKosFqmj5IRkfAsr24jqKCJqfc84ADMWK0_GMgymrI0nfGITC0uWwUjRq_EJjJBodeD_gas945JO_kHPR_j1MQ_R8Wd2c7FUAf6IU0UebQhlp-cs0-FqmjkL7F6D3Zg5YFvuAPnS3SV2JPnwKjQRaZYgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکی گرون نخررر
حجم نامحدود واقعی یک ماهه فقط ۵۹
هزارتومن
تست رایگانم داره؛تست کن راضی بودی بعد خرید کن،خلاص
❤️
@VpnRgbot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82698" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فیت خلسه و هودادکا رندوم ترین چیزی بود که میتونستید امروز بشنوید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82697" target="_blank">📅 21:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GA1u_3tMYKb7AffavsA9wMSzx7hwjJ8Ay1tOzr3glvM1CtMKpzulCISzN-3GfLIlcrAuqQXCtkrrBytyT87p4rG_CstJNNsbrx4mK-GR35t06Gvs7P17ftKVC1jIm5g6mh36WRq_Lu6HuzABsxxYSpnABuRCnU_wGKBoVFn7KDQofkPt-NKRlyLwaGDIUiWyVjR0FHXr33byvcrx_QVh4iNMt4dBrkJlfg9VgA3V2Ag5QgZrGt800M7Iq8kR2UaYbC0uEgeONKnEeG7EoLCN17uI2R8UDoFM-nbecQWF1uSj8df9SF_TvcO2sNW781hl4qmKFkZDDGx4ZL2iA0Uvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aldpT4yq9_Ah6miStnDb8ndiTxDyR8-9KAShEtAxZVjRIL00MyZe0eEDnu7HlP3z95uwhJy9DUAG5vU0k0yLuFqwfgQjPgW77Zj3QltKCvlZuDo6NgcNxI9Xm6u9-yZvt_NQTydE2B8wPlVOcAyCIA0xgW71OjNSforzlaxTKBUK8e2RzLe8GkFRY-wfGMG9gZbQHt4JC43ujMhx1-c1pi_ch5wxZ2q3YJKB2AQ_xgR-jHcf9LsK88PIAcL5wRoYsCvv0Z-i1SLBn4CPb2zXy_p_cUeRmCY0JQPmTC0hKN8N6r87oxQmPcivVvtQM3vopfK2zPADOA28RWyVLgXY6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای کسکش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82695" target="_blank">📅 21:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFt1JtTRyK-hvwFBa2wRiXk7w1I2ZG_WwYrVPxdw6Nv2i14CyyoRehPktHXRHeESeklH_huzbfe8OF1nfhS0lEmhqaxNRtla9BKpLO2DzKKP-i6tCemnvEQ7BB-a5qD1464GlGKNfH1DKsNJbGqJujlYD4pINoPhUzfAUEE_eFuSrzfBXleqlcJ7HR_UE00MeDQc11f8KY-PP17Q0dr4KlSdcm5WB4AaAojs0LWS1pAXJzs6PM1mg4nj-xHq0hkCUmcFQM1g5hnES6h4eEdhc4Xakuy40NLsWxps34-hlBpiV_Ua7P4Bb8tAdOxrEn-GBa_vC6twM1TKPItHRZpMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82694" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مجتبی_خامنه‌ای.pdf</div>
  <div class="tg-doc-extra">250.2 KB</div>
</div>
<a href="https://t.me/funhiphop/82693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای: به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه. دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82693" target="_blank">📅 21:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مجتبی خامنه‌ای:
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛
مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه خودمون بیایم ضعف‌هامون رو علنی و پررنگ کنیم، عملاً داریم به دشمن کمک می‌کنیم.
مشکلات و ضعف‌ها هم باید با تصمیم و عمل درست برطرف بشن، نه اینکه مدام درباره‌شون حرف بزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82692" target="_blank">📅 20:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=nkY9mXAQOnF3Z8EP3Gg80pUX1EBG_jqh7kjnjYhfMLIPlDjyshiA5Mul66dxS3K5lo2HpOONM_KMkI1kXWfdD8HrBk45-jmQUoqPbVDwu4ndj_AV2Ws90ujJEY-cBiEONFaxA7sTQgH15f4Wox5TFmGsaRzBqfovXf5kh9g0o3iJujSyV_03gIvEmgjDkqLidJkNbSSz7K9EFd_6SFfNy67xHq02Pprs2AQFToO910nC-GF3xrBWqeJmgZhlryTD88tVTDpDeaVWnzLSFwBSRhfLhIZJs5Jq41ZC-Aj9_GXDBntWLJdrjI4WNw-agbs6_wHdyjr_toGxQhi9jkzsnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=nkY9mXAQOnF3Z8EP3Gg80pUX1EBG_jqh7kjnjYhfMLIPlDjyshiA5Mul66dxS3K5lo2HpOONM_KMkI1kXWfdD8HrBk45-jmQUoqPbVDwu4ndj_AV2Ws90ujJEY-cBiEONFaxA7sTQgH15f4Wox5TFmGsaRzBqfovXf5kh9g0o3iJujSyV_03gIvEmgjDkqLidJkNbSSz7K9EFd_6SFfNy67xHq02Pprs2AQFToO910nC-GF3xrBWqeJmgZhlryTD88tVTDpDeaVWnzLSFwBSRhfLhIZJs5Jq41ZC-Aj9_GXDBntWLJdrjI4WNw-agbs6_wHdyjr_toGxQhi9jkzsnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر کلمه‌ای که اینجا تایپ کنم فقط از شاهکار بودن این محتوا کم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82691" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-E-7J5p3ERiSsF9q4BRrQAfeXqCh06_SnR-YLzwxFTOuRwwvpqZPLiSrJXJCIuua-BR7vT8jR_0960McLRHPwnhwTN5PZhDp8s63ieYzGZonaU3X1UkAXE6NTjA0pp0WXSPBXZBTTT5uVPL-lRdHmZem8NzCVxzhIFoaZdToj9hUn-GkBpcY92K4gtuUyTGqICOU98YGSlhMH14IgE_7O0QizHAmAuhD_kHfMS8S7W5Zs2DMwW3rfPXA0osRInT-7rrInXdJ3dFCvDxUm209qH9IdV5P9lqqox4Ss4JXb5L17np43aZnQeNBjqmn_p-iIubGIzOq3qwprv0HhBjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های خارج از کشور هم میشه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82688" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn_isuIUUTHzIOWIki8RnV96lSU8Fnd7TytR7kc3JEafiri68u98kI_yHYaWugDXhMvYfwLH0KUg4iy9VeeK-F7UaGW7GyCuB6CIt6yfBYmUceXcXs6jDOFfXBAX9TdPDt4BqSm94h6rCqoDAtMU2hx4K3XId1kTm35QPxM_JPq5-ofqRRhZj7dUFagXIX_J8e29glMtrC9eRWf6UGeeuQ5Gwp4RbmxTfVzR9Jeoesy0Y8bBH7Ym05PehCEZXO9Iy3VN7BaqicaUK5V9JQNBhRrBZZQFmioW3kfsmiOlKV6ZIyoR4bMGyAEiuayk6K8ocvnMGuM-byc0WJgDVBfy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا راهی میابم یا راهی میسازم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82687" target="_blank">📅 18:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐍𝐢𝐦𝐚</strong></div>
<div class="tg-text">حیف بازیو نمیتونم بخرم وگرنه  تمام کاراکتر ها رو میگاییدم زن و مرد فرقی نداشت کل شهر رو می‌کردم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82686" target="_blank">📅 17:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-qucPVG0-py66nhzQJuJVF1nfa2NvqViR_4AoDipRUJwd4L34enLKlTpO_ebHecbfeYAbuxEE6f1_iLhYpownK4P3Nt0q-QGLvSfhlKbrsmi5EbG2du9EUY5WthtALWkdA-auQD-Je_0HuHMenjc94PgTFqU1eEX3JK_zIVIiAqEq3k0uQYwff-LK66DJQs3FDtD9ffeRPRMvH62xysm5TwPYSUHYFnSydzzfwLAlWhDtTwkvxQpj339D6Eptjw1Hh0C9Y1OMTguWD8G6cNC_rDRuzS9AKOKdDFMILnWXK5S2L9qoSpE41KLjWpXM7YXB4nTl4LYNEK2YQR_sk1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82685" target="_blank">📅 16:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پوتک آلبوم داد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82684" target="_blank">📅 16:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پوتک آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82683" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتیجه نهایی اومد برید و کارنامه طلاییتون رو این زیر بفرستید ببینیم چه کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82682" target="_blank">📅 14:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=LvTwGNKvXfizoZLje3J_r5m7-zKhP0qMdYfv7FVXUpvWGDG1NI4zjHe06k2uWDKQzCMl15VsVLmo9mahBWcySwIh0qfLysRegcHZu1-0wDlpC0SBLKjb38nIniQp1CQS_4z87lgWaO-qxZEH1o9pTEnlkT8-S3dP2TjN4CGPdXGEgAac594sLqnJZ58sEPvRjWPHzixfZZF-6_6Ul_QRt22A5uAGVJ4QBIzYyeJhfj-FpJCKq99hTrLEN-25FtPUaut9Xewx6UzzNgnKT-X1iYnhlFDksSMEyv628zkUJakpGpHf3n5gK0luz3vcBy_SkiU-LsWBE2qmYXADEs46vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=LvTwGNKvXfizoZLje3J_r5m7-zKhP0qMdYfv7FVXUpvWGDG1NI4zjHe06k2uWDKQzCMl15VsVLmo9mahBWcySwIh0qfLysRegcHZu1-0wDlpC0SBLKjb38nIniQp1CQS_4z87lgWaO-qxZEH1o9pTEnlkT8-S3dP2TjN4CGPdXGEgAac594sLqnJZ58sEPvRjWPHzixfZZF-6_6Ul_QRt22A5uAGVJ4QBIzYyeJhfj-FpJCKq99hTrLEN-25FtPUaut9Xewx6UzzNgnKT-X1iYnhlFDksSMEyv628zkUJakpGpHf3n5gK0luz3vcBy_SkiU-LsWBE2qmYXADEs46vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرش عمید، معلم هندسه و گسسته‌ موسسه ی مدرسه آلفا وقتی یکی از دانش آموزاش گفت ما برای کلاست هزینه کردیم به جای صحبتای بی ربط، بیشتر روی آموزشت تمرکز کن هر گونه توهین و بی احترامی که دوست داشت به دانش آموزاش کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82681" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUTlYyYhGdumEvVsMiEVzL3BVMOOD0HiJGbiOT1VXuRSz1Yx-tEPRA8KpCOJ8Ni8DAiKLlX-Jqe3_eT0ZgIJEHd9OVnKLYOMIsuaxI-_aEDHB4Y7pA-9IP75ggKeSzG2LFWWm5EKroljs_NbtQBYuoxDB1UJwE4TMI54I0qkqf7uOoemITkbL0GyKX_vacZPj5AvzIxMPsX-R6m_mb2diN1tUcEeOeAcTaAutP8Uqn327VVeVH6h-nmYcs17Wr8_5rSIAvdV0u9csW9Ff9HLKQbLoUp17dM54t1E5TgbO1KEbOyIomsWJx09fO9unNmAzCQISOoH60EaRRaTZRDTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی جوکاش قابل‌تحمل‌تر به نظر می‌رسن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82679" target="_blank">📅 13:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GODhltWntjISYRGOgRG4yFQ6wUec3PrtGleVMGb71Ty9xVnhtEPHBzYst4pek_6-n_z4AyfsIpomnI6wHI-O2zE41RUnEWYWcAV7x7zM8dmOp87_tTACIyV0p1HG2nwkTidVnKd2aB786S-8kq4hfHm1KISfGQ0qMnImKjx_vUjL1-KUKowHmhLJGhk0oCcQ-w2iHSJbqyCbyXBTZO4u2qQBXC-SxyqTgXlhKvIMlSDT_sOdPPSJAzjk-nWgnS_biTe4g7XiXqLfQuwrCBO3toXxLlPity79Tk0s_0WP4j0eAkC3lPXa7n1MOUbU-BkJj8KPYvr3xhTR1R_rzKcB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم از همین الان پس‌انداز و لحظه شماری می‌کنم برا کنسرت استاد نامجو تو برج میلاد. واقعا حیف این همه نبوغ و استعداد که این همه سال از وطن دور مونده بود. ممنون آقای پزشکیان
💘
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82678" target="_blank">📅 12:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=mAOlopVEBDNUwZV1cM32r-d1tyDzkacaSuHAw2vO2ds4lrRLeUxpFJ6ZOv8PJ_TUB0O5loRFaO1G79SoYkmfK-TLDpanUndVphXZwTFfSrhVeyKm6Hj2NLKYWm_TFcTz8vI23N4wVGkzAviOOf4deWG-milYkEE8apq65lwLIOFwzgQftFn2ojEunxYoujJ1Av2VGB5WIj2ngki60SVVPSqboRLqmvHC5aNCE0AXwQU2gas6U7StnJlq5lDPvwQ_tim9a24saZQFBqrbU5J5J-wBLy2JDI7UQMy0tLE7CHps00-4byqbDCD4eCJc_9ZC_5y8ZJikW62evao-8wFXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=mAOlopVEBDNUwZV1cM32r-d1tyDzkacaSuHAw2vO2ds4lrRLeUxpFJ6ZOv8PJ_TUB0O5loRFaO1G79SoYkmfK-TLDpanUndVphXZwTFfSrhVeyKm6Hj2NLKYWm_TFcTz8vI23N4wVGkzAviOOf4deWG-milYkEE8apq65lwLIOFwzgQftFn2ojEunxYoujJ1Av2VGB5WIj2ngki60SVVPSqboRLqmvHC5aNCE0AXwQU2gas6U7StnJlq5lDPvwQ_tim9a24saZQFBqrbU5J5J-wBLy2JDI7UQMy0tLE7CHps00-4byqbDCD4eCJc_9ZC_5y8ZJikW62evao-8wFXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82677" target="_blank">📅 12:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbN0EyMZQRuEt9DjXBiP7SMVTV8cPQC_PpEC1v2GuOEWXzjAFGIwAl6acS9AfhiY2ZX81CK9r9B0qODKA5LyGoLAB5QXh3YJiP2Z8n9LkpLOOOCsX_2S4muSf8UOAiVGZMXarYeyPFIn_FPNH0UeyIOD5gc3OWZp06qg_NmVAsy_ZwElx6jbEhYu31BSC11ceB-ZGaazIAti_Ng0vKXCqewRfcjOat5xExUcYABJgzXUkJ-Wj_SrtzOSRBevDPAf_QJl_3vHSYgRGAN0t4lK8LGdnNP2D83MV5tnWO9HeB3bk6izEWFcjQQ-5-1s7TsqJ7fHMnxnLWBNV8cgQHSVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlkekLmrPv8ykjmEeMzNELH8CGru0D6ZkWzCE21_Jf4C9D2BTdte319m7hR66d5fLccjGchpUoKCwMCutNiCPFl7tKCiPZMVVOZqtqxgHxHoRcNNhpZCl--w0ll9Y7lVuIKMh2AES910gzMbEIginrPrNaI-oUp6Zsk6895OHXd_GZkAUsU9xErF30vP0l0ttTrWh8Bu8iTSPhaUHjc9pshqoz5LXCaJzBmhHWGKjvToWx9iq6utNbkASaVLvbqyu-wlGd3WeyTiEwRDWy4DA9XWZSR3J0D5QYkiWYH8kb64L3E9zaTnNheJjSA50y9EjOVEc8w6jPvVEtoi6U1Zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسلان دیگرد (یه رپر زیرزمینی که احتمالا نمیشناسیدش)، چند وقت پیش تو یزد یه اجرای خصوصی و محدود می‌ذاره و تو اون اجرا یه ترکی رو اجرا می‌کنه که یه لاین سیاسی خیلی تند داشته؛ برای همینم براش پرونده تشکیل میشه و به جرم تولید و انتشار و اجرای موسیقی غیرمجاز، ۳۷ ضربه شلاق می‌خوره و ۸۰ میلیون تومان هم جریمه‌ی نقدی میشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82675" target="_blank">📅 01:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8brUcUzpAUmgdPBPCb44WcSDA51rC42Ub0Ipc_0jqIOXnZzZ8fCF1uJoH5SetzA_t4iQa3pY1YUC_DQckmVVDHJePWn2H1tk04PfnFswkLKgDSOxpRtylflsfZAYJMJCOmrJLsVOoOMtm4xYqEoeFvNBymq7THS9jagHQ4r2bCpkTgjdeGNvhJihxP5GAjA7wNVUjCrPQEOr_7UcZEQE2-U5yLTzCDPASKdavN28d9I3W1hHMlbSpQvolBA0yRI3qzktYZWFZLlC4BiHBHFrI80gW8t7D_1uFF2eGp-xYKlGxKjTp78sDYZg5lplPruEI9bt-O6nb816aYZ_VnWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نا امیدی ممنوع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82674" target="_blank">📅 00:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پدری شاهکار ترین هافبک تاریخه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82672" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82671" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82670" target="_blank">📅 23:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82669" target="_blank">📅 22:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82668" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده.
اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82667" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینکه هنوز ترامپ نیومده بگه برای آه کودکان مظلوم ایران و گریه‌های سحرگاه عاصم منیر همه‌ی تحریما رو لغو می‌کنم و بهشون ۵۸۴۳۲۳۹ روز فرصت مذاکره می‌دم کم‌کم داره نگرانم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82666" target="_blank">📅 22:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا: ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82665" target="_blank">📅 21:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=Q03vNRMN3yLeBsGmbsobPVVDCp6pE23Nrf-EdicyguY4WJRVZ6NLT4NeCilVjzvhlKMGta8jiHkl5EnKuxgq_rJQ4s9_q1TpIkACSr6hB5czHiK75eYby_9okzXLbq0hrTDlQvKGoS1mkv9-d1x4uvW5uT23xM50GTpoEz-2S-fKi4_rJf8S2gMIb7ZwzjaqevlS_Z1vwA5kBmu0bdq-bTmS8AWnDVgbtTpJUlZLq68iPEckf_OaylFKtoiB1DvGXcv7HY3uDfd4ERDQ-JLxm9oudyzpeZcPuSXI_X_svdRrFuKBsSNTmMLRVZV8A9r7k3X68M_WKuUWEhDW0rU3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=Q03vNRMN3yLeBsGmbsobPVVDCp6pE23Nrf-EdicyguY4WJRVZ6NLT4NeCilVjzvhlKMGta8jiHkl5EnKuxgq_rJQ4s9_q1TpIkACSr6hB5czHiK75eYby_9okzXLbq0hrTDlQvKGoS1mkv9-d1x4uvW5uT23xM50GTpoEz-2S-fKi4_rJf8S2gMIb7ZwzjaqevlS_Z1vwA5kBmu0bdq-bTmS8AWnDVgbtTpJUlZLq68iPEckf_OaylFKtoiB1DvGXcv7HY3uDfd4ERDQ-JLxm9oudyzpeZcPuSXI_X_svdRrFuKBsSNTmMLRVZV8A9r7k3X68M_WKuUWEhDW0rU3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا:
ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82664" target="_blank">📅 21:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-MUbYNSiSRSeXlW2P1wxTFq98v2ZAq5ltU0psNprh-lWXNmTYo18OlmL3LGyTcOfIIGEckKjkg_93DCMJVwmQ-YvAEN-JU0l-YTNzXqDCwe-hra9xiXaZU_qjEhGHjKpoiRldruNFbrCYekRgOkyZhhP0k2qfm3u3RlWiK0TocAc8RtoRMbVai5kQBRatOS31ZQeFoXdg_Ev_azAeEKJssfBLO6CoOWiuhyA2kI6KooB3anteSMj4IjBFNKLNQ2N60VMQwCxN-TJvjF5XAmtwnUIbdbTTD4AiyEHutRZfjK052k7idfsiiWgnBYygOlAJ-AlGudRgORWUjwRLdD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافه‌ی اسطوره‌ی نون حلال و ایلان ماسک نابغه‌ی ایرانی به خاطر حجاب پلمپ شد.
💔
این بچه تازه با کلی زحمت و امید و آرزو بالاخره تونسته بود یه ذره پول جمع کنه تا به آرزوش نزدیک بشه.
اینه جای تشکر و حمایتتون از یه کارآفرین مستقل؟
لعنت به قوانین سختگیرانه‌تون.
😔
آقای پزشکیان و مسئولین با غیرت لطفا هرچه سریعتر رسیدگی کنید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82663" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFm-AXSqZrvi8USfVRWjtfmXxSNd6_yA6Ern9CkCEm0bDJzKMts7CY-I94wpkRy0SjJrUHeYm2flMlx0goMoysJ4PyjHwxQUIFpzJVdtjqeapFdMyMvK3kCLiQrrC2043Q-if0yhUtvQ2JHVSHsZeWwtC71F94u73iwaBmnLt_Wap0HD0gJ3DeuY9u5whHU8VGMj0Lss0IeyxzBFH6r4pifPrg5oO3P-4Ar5FL4ckOT9ZfK5EwOy2BIiJwdyn_LFMt_Gvk0A_tGrJEtQisyUVg0XrgOF0r9p19yyAxbHsZd-ZG9qDHiKOP3AyzSnkcnrnUokZ5WRq3crbjvJ0b9Oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوستمون اون اسرائیل رو اون وسط نمی‌نوشت، خیلی جالب می‌شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82662" target="_blank">📅 21:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShirazVPN | شیراز وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rib1IJ078QQoOAOtjlFampZyazlA4zjXagXo1rgU4AmhI7ekaoIg80b1-QQWbhzPe-a4_YzwvbgHDjwM6wPw0jgG-l9k2hLO_ZSybgYNi9C7ugsGOCwXVw33zQOPFIjm2emR4EAzRp_AtmWsRkjFhZkjONOnJxbqq_oZ2fY9N5OYLF3kMr2zCXzPM2OmWvjQ2bGJOgrkFID-DWLUVjqG7a9UyD1VlZs3bW9YvolpSxwkT_jQiISku-RrSJsn1ubbtNfOmXchHT-AJpt8O2dNShD0t_fysv8DBRcCRyhAAfuWvWJJwZ5i8eX25lxKIJiAh0ECubvAf9lev7ZpJB3UpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پلن نامحدود فقط 180 هزار تومان | خرید از
🤖
@ShirazVPNN_bot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82661" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DggLwgH79wNSzcwSmRHZg53s7yeU9OCQRvONMlWTRaMmGWjwBEQ7OUE2WJP_PzNRXSJ-q9ll6LrdUsEYtyewq3fWiSYGm5xptDsZIFrWf6J0ug22ICaLzf7YT6nt13dAS-xmcV9ROy7NY6dDB_FjWvt-cd6JUA4MhHojNTFIOD7a3yA3a2DWNe5MKLli--UuPsbl4qNoBo8ZM1x1GKs1ihzzdXghAKYV24TAPqFq-7C9yQiEnySXBu-xY_WL71bELGZsHQa4W_90sGPJtf9kU5K_xIOYCLqnn2dnLyk_TBwMsx8g6MEP8nKAQMyCN1z-gFoMHA2wwyDHZWG5AaU0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82660" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82659" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-2VH_zhFdWUbfDp-CqI2Fy5584qclOK8GcxGD1KH2ftYn1E_RIEHMBp3Urj9Ka1EGSnHxsUp4EkJvdjZWnOJd6C6w2TPeBMUptPLdxrBWy8lS8z4sk69K4vJ0Vwgpv1srp18wyoK3qKJQHFvQizXIPBmnUFp41ipiLHe3NjNT_X6X5NV3CCcrbvM2FG7mK_FKv_bJJpwmrE4Q1kCOhdTs0y064-U4TiJRA8JJXXufeSfTNqM_fHq0gKovoYIO3ExZBi5GXPS_q1NFZ-v17VCl6mjIDf5yzI-E9pAmE4nfhPhZeI3xWOkcm7cS1O6Zuq8EB4mH7hfaUC7eIZD8ayCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه رئال تو سی ال چقد سخته</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82658" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بارسا بخوره بایرن بریم برا انتقام</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82657" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4KzNBko7ol4utAyvJpRMW-o9EoTOJyc2A1_ywj_ryag5r7Nv6Nb8cWgjiWcd6lNBWDn47m0ZRVzgiSN4wgJ-0X1QLHZvM568qYekWbU_UPFBKSMfr8yZLJLc_Cm8nP9Ib7IIIQYJWons_aDFW5u9PDbGN_q8l-Eyp3HEgqeGxlnSXg4jOhj-PYlxOr2_xDRtkYvHFilOq0f-sUP0_iEgEZuRFSNtG_6OIa-PDU6j07XOsihYJaPJC2ao7VQHNTpqbRQHegZV-Ps903wN2ibr5SE3STSEwsr_8I5SUmINL2QHHXFeCYAjPZz89fHVJnKAPAlpc-vj0TKqb8iokNXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82656" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17918269ee.mp4?token=au2vvUjccJG2QLaw7wlYIs7nyA5P9AtZtHNVmBtA_uix8ddetwyeTvEBvKTUXQtw9MVeK8s-z3TuNxl5FHstDz5nzIe95RPR-wTDlfE5OpGc9Bsz3WrAuBpBtF9M2_plsGbdZGftC_h3-8LkeWXHtjLgVAHMwfWy-osR9zbte5LupP_nZu9V9gWp5ZSude2elL3Lu-eyAs7UjbDs_X3q-PCXEIlCwBr4FTT61xUqpODIZVhVeO0pSzSShlk9SIvDjHIM8f3wXHSKdUSfB6g8fSQSFWAb8Jr-2Xh3mdJDIYU59WS4f9rDkKxhp-VzLt0SjLmsZOshsZvHZhONSUNkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17918269ee.mp4?token=au2vvUjccJG2QLaw7wlYIs7nyA5P9AtZtHNVmBtA_uix8ddetwyeTvEBvKTUXQtw9MVeK8s-z3TuNxl5FHstDz5nzIe95RPR-wTDlfE5OpGc9Bsz3WrAuBpBtF9M2_plsGbdZGftC_h3-8LkeWXHtjLgVAHMwfWy-osR9zbte5LupP_nZu9V9gWp5ZSude2elL3Lu-eyAs7UjbDs_X3q-PCXEIlCwBr4FTT61xUqpODIZVhVeO0pSzSShlk9SIvDjHIM8f3wXHSKdUSfB6g8fSQSFWAb8Jr-2Xh3mdJDIYU59WS4f9rDkKxhp-VzLt0SjLmsZOshsZvHZhONSUNkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داش علی تو لیگ عراقم داره شاهکار خلق میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82655" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWHxFW6rKs0eYhk9Di_SmKnHrLI4ju28XfS4SYMtKiFYgBBOJgePuKvgpZWAyXtcy0H-EevxXs15EXy3AHrfLnC-kPsn9e-uAurJ8LnEbD1yhTuQnmV4nB2Mrl7T5nOJaAVq3oJQRcHwvgPzjRbJpN38Tcdl4UM16FR6BCiKS0AZcQyCpmtpxaJ9_abArzQBZeqn0ngPLgvW7meB7FLEvj4hk-_y2JCKuIF-I67r0D6KVWBGH7S5XgQbO8T8THrMF0Hjdvu8KQt1IeNE-7fG3mdM_UCAYtKmkXmGJv4GC1C-QfCdBqqN0HtNemJcWKq3jlWwZ5f5PCB1N5-srIhNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این خیلی جوکه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82651" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">listen to demo</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82650" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jpxx-1A4K2fAF_Ta_GD5P2ufzmQ1Je7Y0VgqXryAdXxO5npt2SAufKWianK6X2mi2obOs8x_3lJiwtbIsRWoHSRT6cl03FbV6QdMDu9OlegU0BcCQi9QXXL9ni0QY1u62ftJL9XV_9I-N_02wMx1Yjyh0zMB3282PqxxxBG7IDbasyE_kEIWRXOV5Yc2lYcgV-O2-RZEb-RnA-9su0qO8LTfvRQgQQyuL15yfidKkKnjQycMXGDOaqaxOsUVaFd4ibspZb2mq9inpwtM5dcQ1gOXuYrOorlcL-CzZghKkUiINFGF9dYA6ED3dCDNIwwmBqqJebcMMzWvsP5OHMX1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید زبر به نام ثاگ لایف با همکاری سعید دهقان و سیامند منتشر شد.
SoundCloud
🔸
Download
حمایت
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82649" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
