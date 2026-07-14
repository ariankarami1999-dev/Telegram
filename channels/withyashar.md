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
<img src="https://cdn4.telesco.pe/file/LsrkeohT1HZyMY4KIbpPif9vZ5sidyn60SJXIoNDzWa4cW1e6poaFwPnImsW8g-_E2IvwhDnPRUSKrry1hp-9gZg5__Rtg118-gylyBOfcTaNcTJsO2RyRXHWdn8ercm0A1Vn9Mm0e8T5Ayh9AeL48ZcoTOe1H2yhBgQq_ihvKBtSQREUSDBb6hl_JAUmHSajktA-7mwptc5e_6l-iK8XYvD96I1Vs6x2fQY_kacCSyCcU_U2fr3L6WTcILuEk5nH-MEsqfwKLsu_aPKssh_0HtBRcA9ilENIJ7TydJTHR881Dr_Hk4o5j0DjJNurnXU9NeBV4tbB2RCN6ElNYMtJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 386K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو: به رهبران ایران می‌گویم که به فکر حمله به ما نباشید، زیرا پاسخ ما بسیار قوی‌تر از قبل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://telegram.me/withyashar/18003" target="_blank">📅 16:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSrJzGzK2QUrxdBGBbMsALNwUJgHznWdP_OlsJUJCqAHqKwfG5s85FAzq7Sp9buE5LBfWSDda78ccJgpaDF3eJ5M9zW2yvJfrky0pn3jxXKqEG8z0VpZxFXN-w5CuKswwZ0V2ubZOKKVEHoaA21bTSngQPEa2tuh9un-GGcH-sW82QflX5G8RyDuxdvTx3XKkQqpAC8UJ5XGt3Sy0rYmHRnUOyxLqlibN_VDko-I0mQaFWTMUmxM1VKU9JUsiFtHWYOrM-dsIouR7Xke5_MK_W6LRlo22L0jqBr2SJlhiHFfS563AQMaJy50izMIyIv1FCX93LWZCByNVkicNNvr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار امروز رادار سمت اسکله باهنر به سمت شهید رجایی بندرعباس زدن کله هاش‌ پریده @WarRoom</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://telegram.me/withyashar/18002" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2558677705.mp4?token=t3ZtAwa3UzIPXJcTXcahG9RgTbiUVRRA5fxHywKPmbiQvG0TucUEQ-SEmcEmtuxrb0hhOz1tClhCGmTZ6qDBUCYRuaxiY_Eq4K7NtUIWdnpBqqamF_lJKe0_opOtIOPUEX38xnbN-QoFnLQWUNuKK8ePeweqqxTvWoQYUosd8DKTHLU8jiEIti7To62pVFwHHg6bQWdQj9DzoUhElFcFM_TkqV_mkrPKSqXssylsp-rd4zOMO7RozEFwLyM5kb_GVDOphISzNBFKbubzw3kGp1SbUzW3pCo_xPKmOWKqv4ax3gsN5kU7cm3zuzKUcTM4V8ctU1h1IUZAfgNVhYv53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2558677705.mp4?token=t3ZtAwa3UzIPXJcTXcahG9RgTbiUVRRA5fxHywKPmbiQvG0TucUEQ-SEmcEmtuxrb0hhOz1tClhCGmTZ6qDBUCYRuaxiY_Eq4K7NtUIWdnpBqqamF_lJKe0_opOtIOPUEX38xnbN-QoFnLQWUNuKK8ePeweqqxTvWoQYUosd8DKTHLU8jiEIti7To62pVFwHHg6bQWdQj9DzoUhElFcFM_TkqV_mkrPKSqXssylsp-rd4zOMO7RozEFwLyM5kb_GVDOphISzNBFKbubzw3kGp1SbUzW3pCo_xPKmOWKqv4ax3gsN5kU7cm3zuzKUcTM4V8ctU1h1IUZAfgNVhYv53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عقل عرزشی : آمریکا ، بی ۲
@WarRoom</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://telegram.me/withyashar/18001" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCNey-D7puIc8_97vx7ONuv1ldehjI3OatOBWoEZIjKP1lKlfy3R8yzrO4wWh_zv4s0Cx37qg7OsksX1AOoLPwj57LSSZY4hDgUobEtJMj-aSidvcmg-IKnDLU8-7DDzqIjOqk2SUeZoHP6AmnqiXGKR-pTD_rii58VNmc8dtwR2sKUyI-1C8FBMtNmZG83RIsgbnGqltc_OSyvq6KAs5YioBBw2GD-ekJvhp86cddUmU-eymV6GA0Veu6ruYsD5CkK7Y_1kbBUtUrLdimDGHBBp9e42rF7IlKf_XzuAByMIyZDWswByhkib2RZQpa2ZeBX1cZttrWcH_jx-8W42aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار امروز رادار سمت اسکله باهنر به سمت شهید رجایی بندرعباس زدن کله هاش‌ پریده
@WarRoom</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://telegram.me/withyashar/18000" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گشت زنی پهپادهای شناسایی سپاه بر فراز مناطق مرزی شهرستان بانه از جمله مرز سیرانبند و مرز برویشکانی
@WarRoom</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://telegram.me/withyashar/17999" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17998">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فایننشال تایمز به نقل از یک فرد آگاه نوشت که مقام‌های کشورهای حاشیه خلیج فارس مظنون هستند ایران یا گروه‌های هم‌پیمان آن از توافق‌های رومینگ میان اپراتورهای تلفن همراه منطقه برای ردیابی نیروهای آمریکایی سوءاستفاده کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 71K · <a href="https://telegram.me/withyashar/17998" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7Gnm3j6XPZez27tb_JHY6x2udE-1R18l4fyS_Za7MX34h7CI7oPuGxwdO8rmfAV71L0kr7GkTRwn3Td40X0fJgkQcr5XHz_nynVxMQRCV8x62lu2BCN_gfX_JVPxEWf6kghC21Ki_k6wHUmPlijYpcuDaX7HSOZt8c22Xj81mdEOrn8fl5d290UHCa5Wb0BNyeyZlzhw3dPb4_hu_G6SAhPoWQ_YxKk-Y0m0tPIxIqgzoqT64c5ClHBDaTW6qDfNNcZLzS_t4IX36fwkhw9BotoLWP83OtQPnKJ83Xx2PlQ14f8QxYk1uAyPA2jOGTCPuBHeCxKXoW45Mip6QKiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی بندرعباس  @WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://telegram.me/withyashar/17997" target="_blank">📅 14:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96d03cec9.mp4?token=Vkfu_m9O6n_Ju9iulITY_9KkH3wwpPP2mJa5lhDUe4AclPBZ6_ihrzb4etNdKGBvt82GWF7Ow1yWKXFEZeyCgA_aOSipPi-8zghdWKlvsSJFlG6c0Dqv4XTXzpXvKU50U7qq_br7GMa_ly9HxH1OK3ZvvSGei141Ipapf1cgqb4JXvUhxg45qy0m1AEFikKzChXDUe5fC37ymvTp7s6w07fovtBk1xNYdjPvAJNEyrBkLiS1LQ7HdILDBQrePLUxJevpT8GKGFUz3k-FAl2R_diDIuFedmaNka3xv8TAIfDBPJ3Xkzl1lRHxm6ja4QcfrsXz4sGJHQki_5xCHtb7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96d03cec9.mp4?token=Vkfu_m9O6n_Ju9iulITY_9KkH3wwpPP2mJa5lhDUe4AclPBZ6_ihrzb4etNdKGBvt82GWF7Ow1yWKXFEZeyCgA_aOSipPi-8zghdWKlvsSJFlG6c0Dqv4XTXzpXvKU50U7qq_br7GMa_ly9HxH1OK3ZvvSGei141Ipapf1cgqb4JXvUhxg45qy0m1AEFikKzChXDUe5fC37ymvTp7s6w07fovtBk1xNYdjPvAJNEyrBkLiS1LQ7HdILDBQrePLUxJevpT8GKGFUz3k-FAl2R_diDIuFedmaNka3xv8TAIfDBPJ3Xkzl1lRHxm6ja4QcfrsXz4sGJHQki_5xCHtb7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای خسارت‌های وارد شده به پایگاه هوایی شاهزاده حسن، اردن
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://telegram.me/withyashar/17996" target="_blank">📅 14:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هیچ مصدوم غیرنظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://telegram.me/withyashar/17995" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بندرعباس زدننننننننننننن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://telegram.me/withyashar/17994" target="_blank">📅 14:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اصابت موشک‌های آمریکایی به آبادان و حوالی ماهشهر
معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد ساعت ۱۳:۲۵ امروز، نقطه‌ای در شهرستان آبادان هدف اصابت پرتابه‌های آمریکا قرار گرفت.
به گفته وی، حدود ۵ دقیقه بعد نیز منطقه‌ای در حوالی ماهشهر هدف حمله قرار گرفت که در پی آن دو انفجار به وقوع پیوست.
تاکنون جزئیاتی درباره میزان خسارات یا تلفات احتمالی این حملات منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://telegram.me/withyashar/17993" target="_blank">📅 14:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لحظاتی پیش توپخانه اسرائیل حومه شهر قنطره در جنوب لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://telegram.me/withyashar/17992" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1235858ce0.mp4?token=oLFw0Ouom0BfAffnRqZGVoLa-sIW2u-kBjrF2Q5f7TClC_pbYiYvcRjItoz_cRslIdxOQ17VFLggYgrgcUHTHYsm9sGIu7vRb7afEbzNfusI9RAm4h2IlzZ4f9Nh5eYGOnuywElJYXAsxz5iZskhm3ItKuc0M73tkgQep0FZO44HTgSt3SiLHCw06R1uSxa_DSrG0qPrcSK3cwigID8lSwE6IIU_JfCVoo1WvxIG5Sx3z1MxTS1fN4K0-TNEM5px_V0tCwtsR4amqH9b6EqlcVqx-m6WmTieZ2IoVkMCSFpEF_LsmGg-FxpH3kR-0RKMQx243EswG5mR9fc3Y75lew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1235858ce0.mp4?token=oLFw0Ouom0BfAffnRqZGVoLa-sIW2u-kBjrF2Q5f7TClC_pbYiYvcRjItoz_cRslIdxOQ17VFLggYgrgcUHTHYsm9sGIu7vRb7afEbzNfusI9RAm4h2IlzZ4f9Nh5eYGOnuywElJYXAsxz5iZskhm3ItKuc0M73tkgQep0FZO44HTgSt3SiLHCw06R1uSxa_DSrG0qPrcSK3cwigID8lSwE6IIU_JfCVoo1WvxIG5Sx3z1MxTS1fN4K0-TNEM5px_V0tCwtsR4amqH9b6EqlcVqx-m6WmTieZ2IoVkMCSFpEF_LsmGg-FxpH3kR-0RKMQx243EswG5mR9fc3Y75lew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
ساعاتی پیش فردیس برای یه تعمیرگاه بوده
یاشار : چه تمیرکاه پرو پیمونی هم بوده حتما همون تعمیرگاه بی بی بوده که ماشینارو دستکاری میکره
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://telegram.me/withyashar/17991" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان در رم آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://telegram.me/withyashar/17990" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در طویله رو باز کردند با دلار ۱۸۴-۱۸۵ هزار تومان  @WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://telegram.me/withyashar/17989" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx819Xy9frFeag7gpueDV2iMH5n1XoAelmGfuN5YIVIh0dk_aYhHgZczwFZUSrM0AWR8dYBWrxTq8RW1PRvLZFvwdQvRVE5n8LZ75Qot2LxHZEbBuSAm3Ym7dfDtz4BR6MAxSUQ5ipRv_ABWf123QcTeYRGuUHAweV-SdA6HAX67iAaeH7bPy_Tc0lhiNRQQK5yiZGp_B48WSYKTpI-EnoXXNJWspCFjT38d6z3wNeTMCl107PPa4f5vTbd-OE6VJtTWUEj4qxAb8lmzvwDXj1boaso1PF8poi1ilKVJ731HmdV5i_cKEwcarvsU6ckegqFhwJZH9-HYxfHzdZ8YNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا آتش سوزی شدیدی در فردیس، جاده ملارد اتفاق افتاده.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://telegram.me/withyashar/17988" target="_blank">📅 14:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtCx_soyGRnZOAytsUAkIgCzfhL0WQuleCeBMJ_yQ3OReohxAABsNLZ_Y4LV5VVuXUD_Y23r5HBBvD1iACCN0M4BpXJwK1A7x9X4egJlhQCAsg6RJVBb2GzpWzbou2z5z84j7kBe1Jf4haseVpK8dCCu1VlFcmQFL-iIXyWkPu_ZC30vfUHuVVPy4UL-XCjge-vXqJB5W11pK8i4_gxwvs2Em7NXs5QUS-_3J7X33z5woIGYZr2ynvGPEzhgwF1aBGrKO3FsZpCJZLAYOPn4lmUDtgKWjZJZ_RSttIO4XLWo0mC96Abt7oUqAkbfATxPKqoOSCyzgo_KLoDSJkKqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقر سپاه ، خورموج ، بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://telegram.me/withyashar/17987" target="_blank">📅 14:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJVGX7lI7CRwd-z3yhGnPnywPkb1-EFDRzc5rraQ_l11fKfMn9QloKCLBeVnPDfLDdjWM95aYTsY6VlTUtSuzvac58t6NYV7pILkEo6N65OFaf5YVoo6E40uztOzg0o_4X97HEhn-bzePc62VtwzIBUTyGZBAKyeEYeMCcoSZtH_MJ6MK5ba7DSpgHmIYHFVcCiUuIDDEhw8xU3IrZsBc5_r7wvk3u5Sgz-DxITgI1-FXcTwFNEe4cnNukf9sZPMX8ZxkQmP-uNmk2LU_gA0j1zDaTpk_k6M-fm1grPufPUK2uCAQYU0CJA63lxa80w6kiRpFPybJzUH3U17ywSayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر @WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://telegram.me/withyashar/17986" target="_blank">📅 13:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری صدا و سیما: یک حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://telegram.me/withyashar/17985" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyYsmy2pJcbwTHhfYJfKGAukHDz2PylV017T7cOLU1JhNtFjPotbJulnF3DNEQqAMaZKSCUVfzzR0-oLt5dhx_2_JBXmjPvw50poj6w1E0WeI6sE0dZQxI3wSxDK1ldfAqRyNT0sGpqTkigDYXT58I_ZNaHihiQSDC61TgD9OHXzOOv2fZZdsSnvBqIO1wroapyJP4f0aiQVApffA8T6zk09a5ONPiGQztih6RETMOr0eD1YPLjkbyWCZs26yulBH_ZtzeSTJLIS2wK_UR7SHQ5DW408QrlKORTBBGgNit62VtY2TcnDushydfr-oeJGqSxW7HZ-R-HjNMvknVfU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/withyashar/17984" target="_blank">📅 13:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3796203d13.mp4?token=QfIQtb01Bav7nbtCLmNyLsAs0t_D9o_v1bvr64zhd9AvwrpbhVN3l1qDf9ZWtzttKQzjw3_nQtAWsY70uSX0-X7J2xjlDvin0Uvnd5eDGHQJ_ieNVujeK9pCxn1D5Wt9onFEJJ-oPPBZiIiacge3k3riNTTFRkedtJXuPD2kPVgkRVwz6PKUNQI76dq6jyWgJuXW8i_58DZ3gVJWXSDULARj7_GZUeCSsgkdslz-YMr4tlJlY-hSJW_qlxseQX3F3cFm9T-y3auVmd2Mzn7KpmgHdwvrQvOp_h6qAUOwaHDLChf92iBKrhf8d6SPGZlvS1JCgbtEyqZo3psU3rGYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3796203d13.mp4?token=QfIQtb01Bav7nbtCLmNyLsAs0t_D9o_v1bvr64zhd9AvwrpbhVN3l1qDf9ZWtzttKQzjw3_nQtAWsY70uSX0-X7J2xjlDvin0Uvnd5eDGHQJ_ieNVujeK9pCxn1D5Wt9onFEJJ-oPPBZiIiacge3k3riNTTFRkedtJXuPD2kPVgkRVwz6PKUNQI76dq6jyWgJuXW8i_58DZ3gVJWXSDULARj7_GZUeCSsgkdslz-YMr4tlJlY-hSJW_qlxseQX3F3cFm9T-y3auVmd2Mzn7KpmgHdwvrQvOp_h6qAUOwaHDLChf92iBKrhf8d6SPGZlvS1JCgbtEyqZo3psU3rGYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صنایع دریایی بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://telegram.me/withyashar/17983" target="_blank">📅 13:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری ایرنا گزارش داد: به گفته معاون استاندار بوشهر، ۴ نقطه در شهر بوشهر مورد اصابت بمباران دشمن قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://telegram.me/withyashar/17982" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO-DQMFVKhoanaitKOMeSRVV-ffzloexcjkIATz20666_RO0Aqv1q35iL-1u52sxz8z9FD7k8HerDwBkJ4BtD4TRFnX9OFhblUESS9JzIP53yUr8NIX94CiB-tHvEhAqrFNAUoapARTKeSsUKYUalbcc5aaSDyLkyriSjgQO2mD-dZ7J-CCyknSEVFmX6EhkKj8ZViG9RNHu10WCk9oq6B2tdBhs-iRbBrigy5VnORtQfS_q97-U8OteXdbxr4TIqVDpE0_1EsG2Au0G6mQYkg6tHQoIURoBqW_d9lcJhYyIEP7EivnBUj_weOMhSuTXe2gWXSSm9EJpfQrwo6EtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://telegram.me/withyashar/17981" target="_blank">📅 13:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtD-03I6o6L2XFMEiWG7mDayxxUC9_UC_A6w4sHLDjzBoqq0FeFpIEuCvbsfMbpmZWlyapuVjsIGkHm5eeTKYQwhkK-cMZ43kAlp-htfD9o1_-cPwLse-X4FmQcXlF1udSiATk41hS0-XY3dM7i_dewwatJxZ89FlZuqxPL-vqVMQZ2lnM0O_U1cftAwk5hbv9o6MzvZeThwoKuGn1hoI32UksN6k0n-1JKMVIkdgUlZl4s0U7qELIJpDEttZn6ox8fgeAR49GnG5kgVaAX93loZ5dS4sRZ2XFNzIuogEtijsWS88sccLlk_aApfxr_eEvjThb79RJtslXY-ebjrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طویله رو باز کردند با دلار ۱۸۴-۱۸۵ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://telegram.me/withyashar/17980" target="_blank">📅 13:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پلیزززززززز</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/withyashar/17979" target="_blank">📅 13:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcqeX4ocaLAAd4bneWK_h82_9rxwoAN183KSfG4pI_xkk7Wwg5BPtKsQG6QBlEWoBwslhuIGIdMuKnXenl9oh09Gbp1KIB-mfEdNzXWxTd58prlhBBiwdH0SwLdADVsD0U-ax4qP4WYEDtLkC-1fuVpx4Q6E_ln2oHiFfwJcTXKBAnQWCUROO_NtPwwuyFgbWYMox-gIPcf9qoy0ua_zhV7_4sZG1gQxcIMYTdJBMqM54lmZp0mRWvOUfsDkoQJtDX9gj09NhSX0YGJrhrhuAmcvUa76eRbKObKeWX5rwFVdE1ALbGnOe00zIDz0YLZ-05QsrLVJ_vQiYGOCe1NkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارخانه جات نیرو دریایی بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://telegram.me/withyashar/17978" target="_blank">📅 13:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf78206044.mp4?token=pwfGOhwIngTqMkavTy83rMXFKvVj2UYfgnX0Rf3GxV6DMXR5ukYeiNnBWrgKWzsIUFSDsvLQUhK6PEzfx6L2NhPeRHjeylkjl6cmr4EUqf7IgTnHn6TAd3G5T64iQrGyeK2JlGDZZk8l1FH4AdGmQFIBHrIjWXkmcPHBsZ7JZgxUzMXF-Sr5oQ2c6qP6qqsVLrclHmJVqsmV86GEcnir8XObo5b2JLyctpmyazdOl-msDeRWkscPwosIDGAuo_zDqbuKl0MXW16n2ROEdbUOIEmrgH-sYCQtXNKptLwgbpl6OtTP6BVSvbtM_3sWuPk6ZloO0nsuicy5n4IYsJQGGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf78206044.mp4?token=pwfGOhwIngTqMkavTy83rMXFKvVj2UYfgnX0Rf3GxV6DMXR5ukYeiNnBWrgKWzsIUFSDsvLQUhK6PEzfx6L2NhPeRHjeylkjl6cmr4EUqf7IgTnHn6TAd3G5T64iQrGyeK2JlGDZZk8l1FH4AdGmQFIBHrIjWXkmcPHBsZ7JZgxUzMXF-Sr5oQ2c6qP6qqsVLrclHmJVqsmV86GEcnir8XObo5b2JLyctpmyazdOl-msDeRWkscPwosIDGAuo_zDqbuKl0MXW16n2ROEdbUOIEmrgH-sYCQtXNKptLwgbpl6OtTP6BVSvbtM_3sWuPk6ZloO0nsuicy5n4IYsJQGGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرجاسک یه لانچر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/withyashar/17977" target="_blank">📅 13:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqq5-kZcz5KCJyuzdTBoAuhWJu25IV6351Liw8kWY2Vz3HBrwCTZYtBKePWh84MkdObd3Hcwzf6eVWlhrSTm2EBpu02rZPomyzjodC12Wf0z4blSPdvgqZcqaw43qUhkJmwfLkQk1XHs0HSwND5R62qQDjYzSaj1ghnpqnEAoAHd0CITvfTVa5tNaBV_t7m4gn0zs005UZ9fco8RtrJGiY1nscQPBgAcNvWTZbV156xrDRH6rqS7wnpVp0rRKarRVIc8oWiMcNLTvBaKYGyqKzM4D_NsQb6AL3kzq5Efy9TVUE1geIg4Lq2zw2x5aMQl-Su0-dbt7X9-tnORkjcEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر نیرو دریایی
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/withyashar/17976" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c41ba639.mp4?token=EF-fLyOCrObtMSjo7N2vU0xdyVFo5UTzLBeh1b82ocVysTW5RK-s34pBYckO7-n1zHwtrGbCZgnf-9GPOP8ueslvDOS-K5VZw1U4HahDs5wfdRdCK6KJHdg7h01WaCy7VjO7AbLN48bgASf_AaFjVvxMlLY7KK4Fq1gCTqfJWRssvVKlsPT3fZqPwVxqp1kdMU2xfSxtrP2htFc6knAp0l0rnSIuOSsx55PiBm56wl1pnFik9Hf0MsfDdKqgbWErQxJbKLLHnK0AiBqor0Z3QVw1oBDWIfdpo0oJGPMxPnTrwbJ-HL3Riskei24bn2CI0O7Vmr9aA8v5Cn6lLiZbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c41ba639.mp4?token=EF-fLyOCrObtMSjo7N2vU0xdyVFo5UTzLBeh1b82ocVysTW5RK-s34pBYckO7-n1zHwtrGbCZgnf-9GPOP8ueslvDOS-K5VZw1U4HahDs5wfdRdCK6KJHdg7h01WaCy7VjO7AbLN48bgASf_AaFjVvxMlLY7KK4Fq1gCTqfJWRssvVKlsPT3fZqPwVxqp1kdMU2xfSxtrP2htFc6knAp0l0rnSIuOSsx55PiBm56wl1pnFik9Hf0MsfDdKqgbWErQxJbKLLHnK0AiBqor0Z3QVw1oBDWIfdpo0oJGPMxPnTrwbJ-HL3Riskei24bn2CI0O7Vmr9aA8v5Cn6lLiZbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر صلح آباد
@warRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://telegram.me/withyashar/17975" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsGuhR_SQbcVEovR1AEYpK6rdCM4PcywEtf_9en4o_CY4A-oPVHnT7kj22cxYKBbbuIu1FTl_vAoLVJLkOMmhdehV0F97Lj5jYtw8fZRkW1owKR4oKIk0GkGnU3VLSeorinMWqxl9AnFAob9QmaeT6lrGsVRYiJkeyAD2RmFt1V3jYMGzeEShW7Gncu2dxS_5CjtKjMzFPu_-K6rg53OFRia0wRjVPZ0SD1o55lYcRu0qb9yO5kRftsz2L6GYxKeQrJn9df3SWwfxadjXtELQNWM4XrDUkrfewQopBu8sO62r6WzpNelHXi8OGRmwyQzOT0OCLC2XZ1nGDN1kYuu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://telegram.me/withyashar/17974" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcszrrfVwwQdW6oEtoUArecN1HV01Bsc2QHLE7kEihvYeY5imkDZQql336zfjpu943SD8qYbZe4dXdi4z11U2oY9NpnhAsS3VzeY1DakGqA1mSI1BfB-1Dfd1wJLsWSujsgY4lKQCL41mgkyg6oWCG4mYlEMkHoh1Vn0zd_jH9UNVIXpdJd-6bbOXFWxPm26FFs784W7xA0DYerz-YTXSJ4hhl6ZYAhjcancOY_Z6G2IPHcuyBf1rRS3LZTfotA0lfgQ3uoV5o6MKAWTGfZhbo88R4rvPe6gPBKJ7K79vIYnntl0zoB2IrSIVXzGt9PSj-fq1gL1s0M5OnZ6wOVKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTcngc10YI9s6lULhuxABU4va_UQqFV6RnemMA1R8f6RRvaCI1CQqyFW6edUtVYx3g5hXBXn037uebeSKflQBAjFfdJRukYBBQjEGtPuBjTgw9vHq3FdKIu0ALcqcOaV7IFdW1y34rvtF3INZO-QToHfcCeK_Y0qZQu8hmyxKgc7hIEmCKEDG3_OKh0VafF6hANKt0BwaFfB-8nZIfmyIFH4WseGQ5-Pjgsw3IaXpjUQnrj8QNE6T5x2acpGF9GoMoN1Gt6Z8S0bRVQuYxfv9yTg3KYsQ-iah3Z1amcJH9nHshorFdi3f9hk7SlUwJaoUMMJl2cVunzU8PO5akKS7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بوشهرررر نیرو دریایی
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://telegram.me/withyashar/17972" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t941yXwqZwgKEK74Fb9Dg-VKb6eroWxNQXJytk-rRI2Y6GJKt4ND82QAI_UN2qhmFORLhs5KvHimxPbmeo6gc7aqojVQVHy6SLeagXPiIxLXcnDvVKQetNEjb2pDY6DGvETIQRn934DJ6i6gpSZ7sa4dUbuyZG6DXjq3rKMlQ87Vk_VKW-Tp0gSBj4BKy-Uy7ce_AcuX8CPdCSkM2zPPNUgOpLf11aVx_463gnT_901cDA0GnEjVfB61Cuj1wOzZFaM6mzVkzzX3riiXMqPl_Kk-mS_4oHEIK9pn3LNXOv5wN8OILtE2KDJ415pzoZuYmvk3RbjUTmapOHK5ZYE7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و دوباره صلح آباد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://telegram.me/withyashar/17971" target="_blank">📅 13:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوباره زدن صلح آباد بوشهر سوله های‌ پهپاد سازی
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://telegram.me/withyashar/17970" target="_blank">📅 13:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np1fMUDfuSHXtL9IChovGY6xKVQ5CI73wEx8cKNzexS9EakvvIvGDdK_JN_St3orCqofeb5eSXwo6kmYRQjmmypqieLBOhqhLHKG_SKWj5y60U75U-2uL0Bj8Msb6xeTK9_hl_aJjetJd2P-Hfr7MggfaNuMyqgmROUbi3mYGn2PAtFwgmfE_OMAR-PlNo1IuKB70vHjyg00hyDsz58fYw18A6fD_P3HA76e0S-GwQsJYJqDK2x8u_yKOO2RN80-c0Av6rdADV_rj6Qsk6_wy-DfYHSExgfXrg03juyOtBUGwmpTkewP6zuAaVbSRx4Rt1i_1A31g9mxOh7-asoHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر سمت صلح آباد بود انفجارا</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/withyashar/17969" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">3 انفجار خورموج
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://telegram.me/withyashar/17968" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای ۱۰ انفجار بوشهر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://telegram.me/withyashar/17966" target="_blank">📅 12:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری صداوسیما:  دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://telegram.me/withyashar/17965" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وایچرت: بن‌سلمان خود را برای جنگ زمینی آمریکا با ایران آماده می‌کند
برندون وایچرت، نویسنده و تحلیلگر آمریکایی:  دلیل حمله سعودی‌ها به حوثی‌ها این است که
محمد بن سلمان به وضوح می‌داند که ترامپ به زودی قصد دارد حمله زمینی آمریکا به ایران را آغاز کند
.
در آن زمان، حوثی‌ها به هر حال به سمت سعودی‌ها حمله خواهند کرد.
بنابراین، محمد بن سلمان در تلاش است تا پیش از آنکه آمریکایی‌ها نقشه دیوانه‌وار خود را آغاز کنند، به طور پیشگیرانه شرایط را به نفع خود تغییر دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://telegram.me/withyashar/17964" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کمی‌پیش شلیک از ایران و هم اکنون صدای انفجار مهیبی در بحرین شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://telegram.me/withyashar/17963" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کان نیوز: ارتش آمریکا هواپیما های سوخت رسان خود را مجدداً در فرودگاه بین المللی تل‌آویو مستقر کرده و برنامه ریزی برای بازگشت سوخت رسان ها به اروپا را نیز لغو کرده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://telegram.me/withyashar/17962" target="_blank">📅 12:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ درباره مرگ لیندسی گراهام:
پزشکان گفته‌اند که یک بخش خاص از بدن او به معنای واقعی کلمه منفجر شد؛ این وضعیتی است که پدرش هم داشت
در پاسخ به نظریه توطئه، دوست دارم بگویم بله، اما فکر می‌کنم او مشکلاتی داشت
@WarROOM</div>
<div class="tg-footer">👁️ 110K · <a href="https://telegram.me/withyashar/17961" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ما به عملیات خود در جنوب لبنان ادامه می‌دهند تا در برابر تهدیداتی که علیه اسرائیل مطرح می‌شود، مقابله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://telegram.me/withyashar/17960" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور خارجه عمان: در حال حاضر، مذاکرات پیچیده‌ای در جریان است تا یک توافق بلندمدت حاصل شود که از آزادی تردد در تنگه هرمز اطمینان حاصل کند.
ما مسئولیت داریم که با ايران و جامعه بین‌المللی همکاری کنیم تا به توافقی دست یابیم که آزادی تردد در تنگه هرمز را تضمین کند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://telegram.me/withyashar/17959" target="_blank">📅 12:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش‌ها از حمله به سفارت اسرائیل در بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://telegram.me/withyashar/17958" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر دفاع فرانسه: ما برای خنثی‌سازی مین‌ها در تنگه هرمز آماده هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://telegram.me/withyashar/17957" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۳ اسرائیل موساد اسم روز محمود احمدی نژاد رو «گربه چکمه پوش» گزاشته بود  لحظه آخر توسط ترامپ متوقف شد و نقل‌قول‌های تکان‌دهنده رئیس سازمان اطلاعات اسرائیل (موساد) ویدیو ۱۰ دقیقه ای تا دقایقی‌دیگر فقط از اتاق جنگ با زیرنویس فارسی….. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://telegram.me/withyashar/17956" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPeSR0F4WgtarXAUnnwP85zHYeLfFBuRvxSq6ede_r9rEjNa1YPoDXTtlm-ofoKPfsyiKbxn1hZNdmXauDiSLWfJ2Am5ZBIBHbMgcw2tiYC1IfTX0CIM6HxZ7fQTippvjw9LjQgkVCiNIZFsNvylR-nLQ5-u76i_S2czb48XI5GTludkmSfjFcTRpd7G_4FnPmLahaJ-zolNsofi58jRW5xHmGMY2g-l7Z9N3czAY6hpxte1gtTCxQbP-P_71VsDKJSSzeNITCIdn80apoPtpjrIQYGOTJPd_Wj35ArjNQmT3nIXly7wiao6Slwj1PDqj_F29iDF-MlmfVrICo8cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بیژن مرتضوی، یکی از بهترین نوازندگان ویولن ایران، قراره در فینال جام جهانی فوتبال ۲۰۲۶ آمریکا، همراه با گروه ارکستر به مدت ۱۱ دقیقه اجرا داشته باشه! اون هم در کنار هنرمندان بزرگی مثل شکیرا و جاستین بیبر. تبریک میگم استاد؛ باعث افتخار ایران و همه ایرانی‌ها هستید
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://telegram.me/withyashar/17955" target="_blank">📅 10:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU4qTDRqfGjbSlq58N0dGgUgAiOGehzzNLtspOEbLZN9z6hGrvN1MtQV0FegMUesLXOV0TsAwSjNgwNexlNygenIkug1UgKfyXP3ffp7o_ZgrVoJTM0vk8bkxcYIxNr3ZG4H2Y3cay0FfkjLk_GMhrJpdcjfhJQa6l43hiOkjPC1jph_0VUO_vtrV21UovDGFHWEW2F6ZoTzMrDuzz5cHMXPwPvER-3JxsZSVG5_zz1XEF5GzV-MTjiOcoZFhr7Vrg6YyLhja-LZaOqwkoVP4o1W4F98pz3mDUKpU0fEstzYe3vuUWAVAptSa0NLjY1tADHzDFysy-v5BRvx549mEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ
(یا کوه کلنگ گزلا) به انگلیسی PickAxe منطقه‌ای کوهستانی و مهم در رشته‌کوه زاگرس مرکزی و در نزدیکی سایت هسته‌ای نطنز در استان اصفهان است ولی کاملا مجزا . این کوه به دلیل ساخت تاسیسات زیرزمینی هسته‌ای در عمق ۱۴۰ متری زمین، در ماه‌های اخیر مورد توجه رسانه‌ها و اظهارات مقامات سیاسی (دیشب ترامپ)قرار گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://telegram.me/withyashar/17954" target="_blank">📅 10:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر نفت ایران، پاک نژاد: صادرات نفت ایران ادامه دارد، علی‌رغم لغو معافیت‌ها از تحریم‌های ایالات متحده.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://telegram.me/withyashar/17953" target="_blank">📅 10:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای انفجار شنیده‌شده دقایقی پیش در اصفهان، ناشی از انهدام کنترل‌شده مهمات جنگی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://telegram.me/withyashar/17952" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری فرانسه:
صدای چندین انفجار در بحرین شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://telegram.me/withyashar/17951" target="_blank">📅 09:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بلومبرگ، بر اساس داده‌های ردیابی کشتی‌ها: تردد دریایی در تنگه هرمز، از اوایل صبح روز سه‌شنبه، تقریباً به طور کامل متوقف شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://telegram.me/withyashar/17950" target="_blank">📅 08:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه: در موج سوم عملیات تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در خاک اردن را که از آن برای حمله به ما استفاده شده بود، هدف موشک های بالستیک قرار دادیم
.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://telegram.me/withyashar/17949" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سنتکام : پایان عملیات امروز در طول این ماموریت پنج ساعته، نیروهای آمریکایی با موفقیت به اهداف نظامی در سراسر ایران از جمله بوشهر، چاه بهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند تا توانایی ایران در حمله به کشتی‌های تجاری را بیش از پیش کاهش دهند. نیروهای…</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17948" target="_blank">📅 08:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fdbd7112.mp4?token=MS7UT34xLG_bmkvBl6KKWGdGeWR1Lec2Dzx1Wzmr6nAFSXAZbAHRSAEvwgCGeG__Zrg-We63Nqj5fJN0LNA3SD7cr3DLbfgsI11dv08Y0NoynUQG6l3_WB8EXIQ470YIdk1wihh0e_xKfdh0MH7DpJQV8xVmIDWDDzoF-C6pnlMLIAAhI-hmuusxerUafiOqx01KvWw9-iIU7MUPT6gM2CV1H9F5eJnGnp--lQLx3mdVE67FW0dTCxmd5Df7qTLpG0a7dt3Xqg4g5VGOZReUD10NjMLuSELXzDn3UxOjL_d0uqnG7FJHk2ZMWCyHjlhUkBHMY57tUUkmpmgI0gPpvWHuUH_Ycwf5iwns2FMw8p0FFzBwRFbpZIs8dEk3cibX7JripNaPGH5gYt-8frSYv9LnNF_rDYjX6wBY0Mh6mXzMitQpwsjqeefH42RKSJJrBORQqUkeJRj0tbu-PIojXEAinQYh8yB5J2fXJ_PavlnkkEUetKvAOlnpS5cBgySELrA8GVOEwG9ZVBkARDKj9Pvd0r_eirRV8_uAfXMFBsLBPjfBjqTWCdVCbWPuP4T0HWeAesw1Ktn12wAfo1MF9werub0p0JHBt1vt7N-3NYrKdwq8agoxrWyRnQ_2LQIltHIxeg6csOzsmW9B4_5nlJ0QzlrixU2aPfm6zQNQNDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fdbd7112.mp4?token=MS7UT34xLG_bmkvBl6KKWGdGeWR1Lec2Dzx1Wzmr6nAFSXAZbAHRSAEvwgCGeG__Zrg-We63Nqj5fJN0LNA3SD7cr3DLbfgsI11dv08Y0NoynUQG6l3_WB8EXIQ470YIdk1wihh0e_xKfdh0MH7DpJQV8xVmIDWDDzoF-C6pnlMLIAAhI-hmuusxerUafiOqx01KvWw9-iIU7MUPT6gM2CV1H9F5eJnGnp--lQLx3mdVE67FW0dTCxmd5Df7qTLpG0a7dt3Xqg4g5VGOZReUD10NjMLuSELXzDn3UxOjL_d0uqnG7FJHk2ZMWCyHjlhUkBHMY57tUUkmpmgI0gPpvWHuUH_Ycwf5iwns2FMw8p0FFzBwRFbpZIs8dEk3cibX7JripNaPGH5gYt-8frSYv9LnNF_rDYjX6wBY0Mh6mXzMitQpwsjqeefH42RKSJJrBORQqUkeJRj0tbu-PIojXEAinQYh8yB5J2fXJ_PavlnkkEUetKvAOlnpS5cBgySELrA8GVOEwG9ZVBkARDKj9Pvd0r_eirRV8_uAfXMFBsLBPjfBjqTWCdVCbWPuP4T0HWeAesw1Ktn12wAfo1MF9werub0p0JHBt1vt7N-3NYrKdwq8agoxrWyRnQ_2LQIltHIxeg6csOzsmW9B4_5nlJ0QzlrixU2aPfm6zQNQNDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب  @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17947" target="_blank">📅 08:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
امکان ترجمه اتوماتیک و ایموجی‌جاوید شاه رو از دست دادیم یه حل بدید ، اگه پرمیوم دارید!
اگه ندارید به دوستانون بگید</div>
<div class="tg-footer">👁️ 35K · <a href="https://telegram.me/withyashar/17946" target="_blank">📅 03:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">منابع خبری از یک حملۀ سایبری به سیستم‌های بانکی بحرین و ایجاد اختلال در آن گزارش می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://telegram.me/withyashar/17945" target="_blank">📅 03:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حملات جدید به کیش
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://telegram.me/withyashar/17944" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deE4zGFiZjd-WJ1J6Bb5kC9U7z7X8y_HybZBdKna4Jka7glkgFpwB6HzT9aue6BQlO6P-sgjqBokKmd6cmvmJCkCrx_s9W4RQp1ycNgQpiKBrWEYRAbhUM7qVlvPPuHBVYeXuoNImt02gW3ZwOVRENjxtL91PYrCtxFttc9Dn20sN3JNRol88acYDI-tr1w7VHSWd_xXObLn7MvDk4doWtoHs8Zzd8c99MFuxhbMFq_oe4rSwG30_KT3silKSQnzpkz6m3iajvZalIAlGralQc_XcxAoaTMtf6dzNqCJje9h1tajsXysD3kuheHpX7DQpX9qHMPAgfrOciBvJmMatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای سوخت‌رسان KC-135R Stratotanker نیروی هوایی ایالات متحده در حال بازگشت به تل آویو کد اضطراری ۷۷۰۰ صادر کرد.
۹ سوخترسان دیگر به همراه هواپیمای آواکس و پی ۸ همچنان مشغول انجام مأموریت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://telegram.me/withyashar/17943" target="_blank">📅 03:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پایگاه هوایی بوشهر رو صاف کردن
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17942" target="_blank">📅 03:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسرائیل هیوم گزارش داده که کشورهای عربی برای از سرگیری دوباره جنگ با ایران چراغ سبز دادند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17941" target="_blank">📅 03:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سه انفجار ماهشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://telegram.me/withyashar/17940" target="_blank">📅 03:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دو تا انفجار بندر عمام
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://telegram.me/withyashar/17939" target="_blank">📅 03:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منابع عربی گزارش داده‌اند که مقر ناوگان پنجم نیروی دریایی آمریکا در منطقه الجفیر بحرین هدف حمله موشکی ایران قرار گرفت، همزمان با فعال شدن آژیرهای هشدار.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17938" target="_blank">📅 03:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار‌ سنگین الان بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://telegram.me/withyashar/17937" target="_blank">📅 03:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۳ پا به بحرین جمله کرد ، گزارش صدای انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://telegram.me/withyashar/17936" target="_blank">📅 03:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813cc8e47.mp4?token=fTywFg2t7LgyUAtDMsbfwHePitUrKU4vSbV5yAt81b6by5VhFidNx_rchgwQo4VnywnLlE1H2pIE1K2jQO7D6dCy0bXWaZwJvqo-Bw9QlYvn6MASC204i6spw9IxgG8q3tDaKsOL1aIkIX0Zlk9i-0olhcoYIe7vhkk_z440DeWz2UOXRKSlQUxKPLmOxERGKxbWZTWthJ-_R7uq2upbamzdCZkaVAwGHOnDuhkempS-mebsp8jBxwC0X29IiV1Em0Wst6P_nqiDg52EXZHi99lBshxIJ1G8fA6o6Wbkgc6kdCqaSye8Q48UixEzxVnhZ4VxtajrBXf02-t3PCgzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813cc8e47.mp4?token=fTywFg2t7LgyUAtDMsbfwHePitUrKU4vSbV5yAt81b6by5VhFidNx_rchgwQo4VnywnLlE1H2pIE1K2jQO7D6dCy0bXWaZwJvqo-Bw9QlYvn6MASC204i6spw9IxgG8q3tDaKsOL1aIkIX0Zlk9i-0olhcoYIe7vhkk_z440DeWz2UOXRKSlQUxKPLmOxERGKxbWZTWthJ-_R7uq2upbamzdCZkaVAwGHOnDuhkempS-mebsp8jBxwC0X29IiV1Em0Wst6P_nqiDg52EXZHi99lBshxIJ1G8fA6o6Wbkgc6kdCqaSye8Q48UixEzxVnhZ4VxtajrBXf02-t3PCgzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سراوان سیستان و بلوچستان
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://telegram.me/withyashar/17935" target="_blank">📅 03:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca7de4eca.mp4?token=h12RxLKgZ8C_1ajHIaJ1KIWVaD0k1q7f-2X-vs4AMuI7XJV2LrRkhoQgd3-rcQN6xzARh374_UGfEYA9V-eS8Y9DAwLspXm17HuhDZzs6LMfrZL8MZ1HpBopTik5EPuCyaw_2Ll9m01ysIOK7-jVPZOZoIucn0A_hldJM0GGn0zGwkIFHWcBTcUoVnxPuPP3O1-BIZTVNHvDc7nIGuz49iQkqMcmD2eBGNsVm7uQkAeYVtmDG41ezQQShBMxTeB2oeDT3qhhDPLGjycH-COxosrSUWDr5p0Usd2e6A65RhFVwCCQYL5h_5OEFp44bcskyXOmB2yD7kWk5EyHrimZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca7de4eca.mp4?token=h12RxLKgZ8C_1ajHIaJ1KIWVaD0k1q7f-2X-vs4AMuI7XJV2LrRkhoQgd3-rcQN6xzARh374_UGfEYA9V-eS8Y9DAwLspXm17HuhDZzs6LMfrZL8MZ1HpBopTik5EPuCyaw_2Ll9m01ysIOK7-jVPZOZoIucn0A_hldJM0GGn0zGwkIFHWcBTcUoVnxPuPP3O1-BIZTVNHvDc7nIGuz49iQkqMcmD2eBGNsVm7uQkAeYVtmDG41ezQQShBMxTeB2oeDT3qhhDPLGjycH-COxosrSUWDr5p0Usd2e6A65RhFVwCCQYL5h_5OEFp44bcskyXOmB2yD7kWk5EyHrimZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سراوان سیستان و بلوچستان
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://telegram.me/withyashar/17934" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لینک های ورود به چنل از استوری‌کار نمیکنه چون تلگرامو فک کنم یغه کردن
😩
دامنه اصلی t[.]me تلگرام در رجیستری .me در serverHold قرار گرفته است، وضعیتی در سطح رجیستری که آن را از DNS جهانی حذف می‌کند و هر لینک t[.]me را مسدود می‌کند.
سوابق دامنه نشان می‌دهد که این تغییر امروز رخ داده است، اما هنوز هیچ توضیح عمومی از سوی تلگرام، رجیستری .me یا اپراتور پشتیبان Identity Digital ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://telegram.me/withyashar/17933" target="_blank">📅 02:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1e42bf62.mp4?token=N0lGmu2wvSDFdwnpatuwk8XMyyhFuqalMpZgQErpJObEXEEy3T2qNkUg4mpXLdnwj0xgCRGu1blTaw6ECN9pLlnqDDxsK7CnIYnAqnllZiJiZt9ybNI3_qVDlEUn1Beoad8qbYu-SgeMb913369ZTT9t10anLS1MSIaw2UDVrRy0AotKeDizOTmNfDIDS6_E8NDkHTkFI5K1gaYmiHGHsBikvyvsKLROWOoGth9fGnY5O3WwxjVqkCUcFL81LeNMkHMxhPaEPEKLFwT5YXmLVmUDj6fhmkJg1zFMCK-17BhQ4_Dwp6XQCrjGL1_SMKjUbWH_hm7fHU4l8iNnCFhe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1e42bf62.mp4?token=N0lGmu2wvSDFdwnpatuwk8XMyyhFuqalMpZgQErpJObEXEEy3T2qNkUg4mpXLdnwj0xgCRGu1blTaw6ECN9pLlnqDDxsK7CnIYnAqnllZiJiZt9ybNI3_qVDlEUn1Beoad8qbYu-SgeMb913369ZTT9t10anLS1MSIaw2UDVrRy0AotKeDizOTmNfDIDS6_E8NDkHTkFI5K1gaYmiHGHsBikvyvsKLROWOoGth9fGnY5O3WwxjVqkCUcFL81LeNMkHMxhPaEPEKLFwT5YXmLVmUDj6fhmkJg1zFMCK-17BhQ4_Dwp6XQCrjGL1_SMKjUbWH_hm7fHU4l8iNnCFhe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکل مخابراتی بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://telegram.me/withyashar/17932" target="_blank">📅 02:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ded610f5.mp4?token=ofzbNPGet7nZ7BsVjre71qVI65O8W_cW2V-eJPqhqMBimrhWSRV_uiV9OrTFxKG6pkixKrL5w4PFZN0Hvell5YnftFQdotl2RoPWkjMoCRVqBEuknr6-VSKRoNODCPsUkjlkC1sULXc3l2CWkY1Uv39E0ae-OBKeCK_1zuWBBHW1dwdVcJfktMgeEBUSFeYVesvgGkZsSWQUU7TWTAH33NPHIrg63MrTQ0EX8asdY8YvykySfQQ-tuWWkjQ6N0dM0YfT9FELsXE2ncGYZEQkI0P7TFyzKdMhSmzek2hhceQp3RlSQwQfRDCGKbjE7SCB7xMl5YgqeMV8NTbiymOJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ded610f5.mp4?token=ofzbNPGet7nZ7BsVjre71qVI65O8W_cW2V-eJPqhqMBimrhWSRV_uiV9OrTFxKG6pkixKrL5w4PFZN0Hvell5YnftFQdotl2RoPWkjMoCRVqBEuknr6-VSKRoNODCPsUkjlkC1sULXc3l2CWkY1Uv39E0ae-OBKeCK_1zuWBBHW1dwdVcJfktMgeEBUSFeYVesvgGkZsSWQUU7TWTAH33NPHIrg63MrTQ0EX8asdY8YvykySfQQ-tuWWkjQ6N0dM0YfT9FELsXE2ncGYZEQkI0P7TFyzKdMhSmzek2hhceQp3RlSQwQfRDCGKbjE7SCB7xMl5YgqeMV8NTbiymOJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شناورهای تندروی کلاس «گلف»سپاه بعد از حمله سنگین آمریکا در بندرگاه و دریابانی کیش، در آتش می‌سوزند. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://telegram.me/withyashar/17931" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارهایی در شهر امیدیه، استان خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://telegram.me/withyashar/17930" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296ed3620f.mp4?token=eg_iQpHF2PTE7_ZoWlUf66_fl-dZZ2tKfdBr9pTpkgt0ez8N3xFGyT7_ATgUgRi7-W0qwXXUGQkmQDCinTdUuuOyENgTr8kcIqwnXF6H_Ot2fgvKxX9yGvU8msQ5TpviFsB6NFx2tpPGwpJv595nB68xTZcbW3VUgpFGGL5F1J7_Iouw7vbGDOsce3S9rWQlB-rZJG1uD-MqqjxhG5OWjpgNfSTRS2Y0qEG9g5-0jIaWObbaJTSjCNnkVoINYgoxjno0lRMRVseOyVwwffwFi8KuHtXit5pAI4e-A7s8SS3u1ZKHpDdeTPkp2gLQYmOScnshD_f5JOS6uB7cIeuKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296ed3620f.mp4?token=eg_iQpHF2PTE7_ZoWlUf66_fl-dZZ2tKfdBr9pTpkgt0ez8N3xFGyT7_ATgUgRi7-W0qwXXUGQkmQDCinTdUuuOyENgTr8kcIqwnXF6H_Ot2fgvKxX9yGvU8msQ5TpviFsB6NFx2tpPGwpJv595nB68xTZcbW3VUgpFGGL5F1J7_Iouw7vbGDOsce3S9rWQlB-rZJG1uD-MqqjxhG5OWjpgNfSTRS2Y0qEG9g5-0jIaWObbaJTSjCNnkVoINYgoxjno0lRMRVseOyVwwffwFi8KuHtXit5pAI4e-A7s8SS3u1ZKHpDdeTPkp2gLQYmOScnshD_f5JOS6uB7cIeuKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شناورهای تندروی کلاس «گلف»سپاه بعد از حمله سنگین آمریکا در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17929" target="_blank">📅 02:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مناطقی که امشب تا این لحظه در انجا مواضع سپاه توسط آمریکا مورد هدف قرار گرفته‌اند:
💥
بندرعباس
💥
جزیره کیش
💥
سیریک
💥
کنارک
💥
بندر کنگان
💥
جم
💥
سراوان
💥
جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17928" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ : همون‌طور که می‌دونید، امشب داریم خیلی سنگین ایران رو میزنیم، حجم عظیمی مهمات داریم؛ تعدادی که سال‌ها بود در اختیار نداشتیم!
حملات شدیدمون ادامه پیدا می‌کنه تا وقتی که ببینیم آخرش چی می‌شه.
داریم تمام توان تهاجمی‌شون رو از بین می‌بریم، کنترل تنگه‌ها رو هم دست گرفتیم و محاصره رو دوباره برقرار می‌کنیم.
احتمالاً محاصره حتی از حمله‌کردن هم مؤثرتره، ولی به‌نظرم ترکیب هر دو همون چیزیه که واقعاً کار رو تموم می‌کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://telegram.me/withyashar/17927" target="_blank">📅 02:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صدای زیاد جنگنده در آسمان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://telegram.me/withyashar/17926" target="_blank">📅 02:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرزیدنت ترامپ در مورد جمهوری اسلامی ایران:
آن‌ها موشک به پنج کشور مختلف فرستادند که حتی نمی‌دانستند درگیر هستند.
آن‌ها دیوانه‌ی تمام عیار هستند. آن‌ها دیوانه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://telegram.me/withyashar/17925" target="_blank">📅 02:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: هدف ما از این حملات از بین بردن تاسیسات و توانایی آن ها برای کنترل تنگه هرمز است. کاری که آنها دارند انجام می دهند، به شدت احمقانه است!
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://telegram.me/withyashar/17924" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: همه چیز خیلی سریع پیش خواهد رفت
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://telegram.me/withyashar/17923" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://telegram.me/withyashar/17922" target="_blank">📅 01:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5b514d41.mp4?token=T4gwXMLKwZWt-RgqYsbHN0kHRm2ntPw_9OJ5Zl4dpuwWw3KxYWUq7D7q3BFmyRV9f7fO1lmV4pVOGToWIiPecVtpmiruyI-uW0VdxjRPIQFYZ5Of7nIUcjd5SA1j5QZ_xfxVqC6lMvletsn1Yd___W0Og5RQ8B95EWcf6-gD90LPAzssxN3lSpP77gGqlLiq8VEJx9OKuvumc9tc7jCRnj-oVkictV0Z6MTAGJv-6e5qrFsgyS_81tKSmjN327m1OJil_kUI6JDVyIBUlgUrUfdV3xk-B1zb8NirpzLTtGIeNQGF-t9LkQb_te12krNtUHI-1txpnWXMWkhj3_4VuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5b514d41.mp4?token=T4gwXMLKwZWt-RgqYsbHN0kHRm2ntPw_9OJ5Zl4dpuwWw3KxYWUq7D7q3BFmyRV9f7fO1lmV4pVOGToWIiPecVtpmiruyI-uW0VdxjRPIQFYZ5Of7nIUcjd5SA1j5QZ_xfxVqC6lMvletsn1Yd___W0Og5RQ8B95EWcf6-gD90LPAzssxN3lSpP77gGqlLiq8VEJx9OKuvumc9tc7jCRnj-oVkictV0Z6MTAGJv-6e5qrFsgyS_81tKSmjN327m1OJil_kUI6JDVyIBUlgUrUfdV3xk-B1zb8NirpzLTtGIeNQGF-t9LkQb_te12krNtUHI-1txpnWXMWkhj3_4VuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «دیگه تموم شدن. رادارهای قدرتمندی داشتن؛ همشون از بین رفتن. سامانه‌های پدافند هوایی قدرتمندی داشتن؛ اون‌ها هم کاملاً نابود شدن.
متأسفانه، تمام رهبرانشون هم از بین رفتن. فرمانده‌های رده اولشون همگی کشته شدن، فرمانده‌های رده دومشون هم کشته شدن و حالا با فرمانده‌های رده سومشون طرف هستیم.
اونا ۴۷ ساله که دارن مذاکره می‌کنن، اما هیچ‌وقت کسی از نظر نظامی بهشون ضربه نزده بود. ما داریم خیلی محکم بهشون ضربه می‌زنیم.»
@warroom</div>
<div class="tg-footer">👁️ 143K · <a href="https://telegram.me/withyashar/17921" target="_blank">📅 01:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 134K · <a href="https://telegram.me/withyashar/17920" target="_blank">📅 01:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دو انفجار جدید الان بندر عباس
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://telegram.me/withyashar/17919" target="_blank">📅 01:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چابهار رو رگباری‌دارن میزنند الان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://telegram.me/withyashar/17918" target="_blank">📅 01:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: توانایی‌های تهاجمی ایران خنثی شده، بر تنگه هرمز تسلط به دست آمده و محاصره مجدداً اعمال شده است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://telegram.me/withyashar/17917" target="_blank">📅 01:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل به تمام خلبانان ارتش تا ۴۸ ساعت آینده آماده‌باش صددرصدی داده است
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://telegram.me/withyashar/17916" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ویو اصلا ربطی به ری اکشن نداره انرژی بدید خداییییی ، کجان اونایی که پیرهن جرررر میدادن
👑
👑
👑
👑</div>
<div class="tg-footer">👁️ 140K · <a href="https://telegram.me/withyashar/17915" target="_blank">📅 01:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOHBupit-bb0jJDv7CV7AJCgXLLmxuDR68vgZQIOf_gUSoQyKo_-at_XYxgCP01-0qRt5ry16hd1NT57CM2W1ceHFquUxAVJL7C7EWCwm6WKFV0jF7SL0ZNrUTSW5_eMaqDxOCc57ap3kihKOIZ-qdS8yx-u6z62lQ-GX8wNq6Y1U7WbktpGLBTz-2A1n3lXqXaNcizRFxwE2yQX5bEZYkKyvl9WNP-URTV8GeJb6ONMfKatAaO-Hvle1kibVsJ_-dOnggk4SxC87d4s5tWqR4dZSTFfm5D4x0ZsNm0S70XPerM5enwqJuvG9MGuNktlVuyuZ33K0AKlefe__TfBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاوه , کرمانشاه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://telegram.me/withyashar/17914" target="_blank">📅 01:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سی ان ان: آمریکا چندین هدف نظامی ایران از جمله سامانه‌های دیده‌بانی ساحلی، پهپادی و موشکی رو هدف قرار داد
@warroom</div>
<div class="tg-footer">👁️ 130K · <a href="https://telegram.me/withyashar/17913" target="_blank">📅 01:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه های رژیم : چیزی نیست چند تا پرتابه برخورد کرده
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 130K · <a href="https://telegram.me/withyashar/17912" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd534a1de.mp4?token=kYxLnstMaTDDxyXk9tpC61-Z6o4-cJrI1KOZ0AWwvUpaNpbErJ9sczqNnoJTmHVZO_cDYFV0YNW2sv9Bo8JrG4jTUtkc24m3cN3ygBv3FLGJhaulpFRdm1-m8t2Q_YB8KWWDq0GJaoeaGSp3pZv1I7mh_ZDX9_xA3lIUxQzjb4_nbIoE7tcJQm8X8u8Y3uXunt0kDWplrC6t4LwM6tGq27g6QaufBEdLbX5lmi9iLe5DikDSROwxhd9KljVPzuMXrDkTeORvQHbSsfUTU4m_EiclnfUO0O32NckCfCF0Ox-eyizjAePhg12RRNu2l2EzhleanFX1ibPGvQJemWd_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd534a1de.mp4?token=kYxLnstMaTDDxyXk9tpC61-Z6o4-cJrI1KOZ0AWwvUpaNpbErJ9sczqNnoJTmHVZO_cDYFV0YNW2sv9Bo8JrG4jTUtkc24m3cN3ygBv3FLGJhaulpFRdm1-m8t2Q_YB8KWWDq0GJaoeaGSp3pZv1I7mh_ZDX9_xA3lIUxQzjb4_nbIoE7tcJQm8X8u8Y3uXunt0kDWplrC6t4LwM6tGq27g6QaufBEdLbX5lmi9iLe5DikDSROwxhd9KljVPzuMXrDkTeORvQHbSsfUTU4m_EiclnfUO0O32NckCfCF0Ox-eyizjAePhg12RRNu2l2EzhleanFX1ibPGvQJemWd_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی ها پای اخبار جنگ از اتاق جنگ
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17911" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYO3sauIdAwBGE-apOY5iU8PecV8gELuhY41PpiqnQOCpnJQzP_oUUMeBzO7m0PJm3fzVVHktAYv65sSgCbAXqPkb_LIjxe_gLlo7kbm-zlFuwDTxb0aWKlrcQnrZTTsOwMf5aQDBBX8jOWpmhDENyJST3VDL0J7Yb4GfbPMV-o1m7qT4RWmcK7pKhXmYoOtCsQrijmyBy0bODnwnqrpfrkH9FpEEnEtSD2Gyio6q-4ggQoKzIcxaByk-SyfNyQcZiGTgKc1ci2-bmdXR6kQShoTon4FMxPbchB2MTaa6O_3YTs6YKJ3sR0jqEXqPu_CEUqfLZ5juDAh_5rcEDDeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک‌ از جم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://telegram.me/withyashar/17910" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eop-7U0Aphk0HsoE-xs89Zrw42TnGAL8w40WlO_mJHFOFGXwL4H9bd9Q3tLrkExz5vmkuFXF2DUIlqPC_W6AGWgW0_wV6XWTLB5lR0ZSYJfA0EVadsVWVqsMlBappL8uNWBb2oJGRkOdaRS-lAGWmF07Q0BNs5szQ-ZuJjqFTqz1jc2ukn2ABXmG18dihbzrVMu-vKt-V9wIi2DDDeDL4sg30tuCj7N34hryWsIUk5tRB0IarsrYZ4fT21AThRTJ2yPk6l7lCWJs_wExx8bE_P7niXz0FKQCF_3eclsZ3ru8_9ZJW5Rn_phwKviEGp4ERviQuZCMvuWWDPX0FQ695w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qv_AmiAQ8AiaJng4Kp8rZETKnvUYZHi-W9jAzpFttoDq-1bADilKnkdsAvFVpmmhxV1CEc1A_sFg7jDml3yNluxKYDxjX6cr7KhXXUBIBPIKdtVUiCqzAbl0Swidfwu6tszSe-xz1tDh0HvxEHbhrBRfJIx3DkUyuggwR1w6dKa5g4lgY7m-WN5KXpIWmzjvVCBQMSWf8owSFFu6T1tpDT_HBfAcjeYq9URoyb8F0y9WoKB9gqX0FniW1XnwDHXdQYd8-If3X7A858S4eQrFNOw1llcx9ykOyWnsH1M6Bfa6SZkZgJApLoxrwzbgMKKDJHInNz1h8b2zFzXoPSoK2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیش الان
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://telegram.me/withyashar/17908" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همکنون درگیری نیروی دریایی ارتش و سپاه  با نیروهای آمریکایی در ۲۰ کیلومتری تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://telegram.me/withyashar/17907" target="_blank">📅 01:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دفتر محمود احمدی‌نژاد«گربه چکمه پوش
😹
» با صدور اطلاعیه‌ای به ادعاهای روزنامه نیویورک تایمز پاسخ داد و اعلام کرد که حصر خانگی رئیس‌جمهور اسبق ایران کذب است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://telegram.me/withyashar/17906" target="_blank">📅 01:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0Eto4_TFSMyLJjS6oGtqM2FxV-5NnV1qqTn8oHyDTQ8YoGFDfLUYHxr132qoOQtJ0NIVWeGQw_DOAUXVtKKEp2oYmZR182bAECGK1V_QoJYhE9xV2qyrsODd9-tFfpmgxc9Mxi7liPy0PV22IC7cDlRizdRhA3MGhRihmeE4hQWCDQUwqICkzO_1PTnBHa4_8aD3mB1P0J1gAPnV2nd9-9iz636rg5CDmKd2pXsfZErrSjJACVf5tN41_DkCmPwG2xDEFKWyq32sHDsjs6ioCSdFAFtbp6JOfnuFACBgvvZ-30sLHhhiKDbPyWsPUsknex0FHb3GzHGRm-QpW40Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، فقط فقط همین کامنت را لایک و اد استوری کنید. ترجمه در چنل تلگرام. https://www.instagram.com/p/DavJyXLhhos/?carousel_share_child_media_id=3940411242254309932_347696668&comment_id=18112905515304028 ترجمه : ،  بسیاری از ایرانیان باور…</div>
<div class="tg-footer">👁️ 133K · <a href="https://telegram.me/withyashar/17905" target="_blank">📅 01:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوباره شلیک موشک از شیراز / عبور از از آسمان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17904" target="_blank">📅 01:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">زلزله مشهد  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17903" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوباره کیش رو زدن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://telegram.me/withyashar/17902" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوباره کیش رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://telegram.me/withyashar/17901" target="_blank">📅 01:03 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
