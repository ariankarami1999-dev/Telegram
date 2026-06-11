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
<img src="https://cdn1.telesco.pe/file/GTh1yUrPp6k1hrNNLuGeiMc_-1Urh8T9mucjgHP-paY1SOR34x5X5IAZz5t73hL8zcCV952Hq7J--xvlmgRUq6PjqTCycI1921EoJW5KMWW1QLyvnEEBw0ObvtQ3wzMeDJ5q3Nn2Awdr7jdiF0qYB1RtwNasoLzTPrhfHmlTMm3vKX-h_-dJiJ9XJ_YbL91D7xtQfq-iTzq3udamZhlCOo-TiKX3lEHf4c4yLrVSMMMROOK3IP-FQoVPI1LigO6pgfDrGfuTR-Zp30n9JdDR0dnNKd0Sx4bYW2089XtGznDTu5NfmiPOaC_22pyhZTJ9qDfKTHj3HTTVqZXTayPnBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/clBgUYYPFvTA9cOh1WAdPWXR5fKQvVjeHW_chgySiinVBSiU6FqcsQvt_QvDSFuHI1Ci00BhBHdAcygkjOmtRUQCo7AAiUTx2k_ykSPLgaAt4ijumHLqT2Ur1jLh1IAe0hsZVIZZ4Ib45jPHa-1DsFsXxcDxWCPsas8-YaHPtgrFe8omGX47dvzJkpMXBDZSywX0hHghGfcUIgm-zBP9UIbnKUYsZpWTKPHPUABtVm30KOevkag3muO6EYVg2wsig1pJWnWJmW7yJLDOgdl-OUyVIvTJ6pw-90v8ztRl5cz72-h8hBG3nS8AtZhcoe8ymFmlrrSzhincucmAVqDXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابعی در جمهوری اسلامی نوشته‌اند که: با میانجی‌گری قطر، آمریکا به شبکه beIN Sports معافیت داده تا مسابقات جام جهانی را در ایران پخش کند.
تاکید هم کردند که: این امتیاز توسط دولت ایران و کاملاً جدا از هرگونه یادداشت تفاهم (MoU) به دست آمده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/VahidOnline/76249" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48aba236c3.mp4?token=mtCAtY-DpMZPBGpQLAxHfHV_TKvNSl1qZKxpVIqNpOoFcoKc2m3Z9b5I84Rn2MKxYb9-vfXrwozyOIJD9YhhdPKiW6cnbNg5hI3PsEv9N9oqrJ2V6T7om_EXPvUxoWlMOlMOrj56RENJxIaBSZFjZ402Sc393mBJFhhtGqwkQG9kor8gV4V7qerxJuUOOJRAjIO-wmzpejbD-fpNFjdrDYsyjMrBoKZIpTfWbQU21NTmtRJBR7VWFrKxqxJGbywc-Vym5KAPHdpDN38ONSHih2flOe4XfmldnWXdedyeMConnJVBYAgVRy7pZg701k0HHuNbe9vSM3bMAQtLxtiGuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48aba236c3.mp4?token=mtCAtY-DpMZPBGpQLAxHfHV_TKvNSl1qZKxpVIqNpOoFcoKc2m3Z9b5I84Rn2MKxYb9-vfXrwozyOIJD9YhhdPKiW6cnbNg5hI3PsEv9N9oqrJ2V6T7om_EXPvUxoWlMOlMOrj56RENJxIaBSZFjZ402Sc393mBJFhhtGqwkQG9kor8gV4V7qerxJuUOOJRAjIO-wmzpejbD-fpNFjdrDYsyjMrBoKZIpTfWbQU21NTmtRJBR7VWFrKxqxJGbywc-Vym5KAPHdpDN38ONSHih2flOe4XfmldnWXdedyeMConnJVBYAgVRy7pZg701k0HHuNbe9vSM3bMAQtLxtiGuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات جمهوری اسلامی:
من این افراد را بسیار منطقی‌تر از افرادی می‌دانم که دیگر با ما نیستند. این یک گروه متفاوت است و من فکر می‌کنم گروهی باهوش‌تر است که منطق دارد. همه آنها توافق را تأیید کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/VahidOnline/76248" target="_blank">📅 00:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTAYfBodYEWTY23LqjleZjAphz_jLIgnqWpC0YwaOFiLFGeM8YNe-HaK5p9q_WnER0_SXX_46T9Hs_ennC-tOy1zo7X8pPt7lCSWEjGkVPelTuSxELZU5x97Qr1aGTgx7G9dkBitmsi0C2MuTlxOIzpZpVPW5EbWjvvDusnG9vCbQYqhDpB9rx3VXNOez_R9sfK56LS9KhXAjwuTc-CBBr2EMtbZWJBiVcyWcnNgr7KDwJHravNc8zcyWrNqUajKW16_5HGwtDlAfUg1aRBrOHarY9JCCU5VMaAagdRnM6rQWgMGACX3x5D2vtbiErWtCVReSs78UdQjtm-YMMucBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه جمهوری اسلامی در یک برنامه تلویزیونی گفت: «مواردی که درباره توافق مطرح می‌شود، گمانه‌زنی است و موضوع نهایی نشده است.»
او اضافه کرد: «وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود، اما آمریکایی‌ها مواضع خود را تغییر می‌دادند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/76247" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZKZ9FgazCMI-37vkapYKzBOAQuaFOAlGwQt7UGfgDPgN30fOtFh-IavLwOh1BeaZFHmIF2RmGb03GT6IQnlOEuqWU1i4YtuZwJpSbgImpagyOxC6jv4eDow2nAhPKW2josMPqAhBUhE4TO8PHf5uKqu5BGq1t-jxKi2Ux8Y84jXJiAozYeUy_lXUdrRekh1zOu6A5ZEBb4_gMOzh9igR-CI2sp28au1B8f-zcvw0_ANgDaSSqG_wge3aoe16GmyYhH8WMrwma7r_N8beO1ZPvzdkNce_xYhqz4ry8TDSDer3p5ikJlSBxc_Jn4qL7v9s2nH-xLnfr4sPg7X3q9WCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل طرف تفاهم‌نامه با جمهوری اسلامی نیست
دفتر نخست‌وزیری اسرائیل، اعلام کرد که دونالد ترامپ، رییس‌جمهوری آمریکا، درباره یک یادداشت تفاهم در حال شکل‌گیری با حکومت ایران برای ورود به مذاکرات، با بنیامین نتانیاهو گفت‌وگو کرده است.
این دفتر افزود نتانیاهو از تعهد ترامپ درباره شرایط هر توافق نهایی با ایران ابراز قدردانی کرده، هرچند اسرائیل طرف این تفاهم‌نامه نیست.
دفتر نتانیاهو نوشت تعهد ترامپ شامل این موارد است:
-حذف مواد غنی‌شده
-برچیدن زیرساخت‌های غنی‌سازی
-محدودیت‌های تولید موشک
- توقف حمایت جمهوری اسلامی از گروه‌های نیابتی خود در منطقه
@
VahidOOnLine
به نوشته تایمز اسرائیل دفتر آقای نتانیاهو در بیانیه‌ای که «سعی در کم‌اهمیت جلوه دادن توافق احتمالی» داشت، می‌گوید که آنها درباره «یادداشت تفاهم قریب‌الوقوع با ایران در مورد ورود به مذاکرات» صحبت کردند.
به گفته دفتر آقای نتانیاهو، در این مکالمه، نخست‌وزیر اسرائیل دیدگاه نسبتا خوش‌بینانه‌ای نسبت به توافق ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/76246" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=Dkivsi-k6dh4msmJrBqMZC3vEKaLNfBfruHtLEWpwB80ThBjzdaUJGZqdtzm-_llnrEmCPybFLBhsw88Oaipxzt2Pq6z3bxY5B5kwVe0X8O3RVjEgEQ8CwVXBYYPr3IEusGPm-Z2ObyJMf-lofw87wnso1UUCBZ__8quST6bEFeWEIEq3vXlqeOVKcZBtj_woISf_CSYFUgWvFlsleSKqEC47OC9t-grtwJ-RD2-DZLmwBPvcW9_bhYAe7VtvzXJJLLPJHIvX88ARpVd7qFDgvgzkLO_g7NwtTk_-3tgoOoi2e1x6NU4XJhw_RdvGhkcKCpMd5bzsbXTfpuz3sDvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=Dkivsi-k6dh4msmJrBqMZC3vEKaLNfBfruHtLEWpwB80ThBjzdaUJGZqdtzm-_llnrEmCPybFLBhsw88Oaipxzt2Pq6z3bxY5B5kwVe0X8O3RVjEgEQ8CwVXBYYPr3IEusGPm-Z2ObyJMf-lofw87wnso1UUCBZ__8quST6bEFeWEIEq3vXlqeOVKcZBtj_woISf_CSYFUgWvFlsleSKqEC47OC9t-grtwJ-RD2-DZLmwBPvcW9_bhYAe7VtvzXJJLLPJHIvX88ARpVd7qFDgvgzkLO_g7NwtTk_-3tgoOoi2e1x6NU4XJhw_RdvGhkcKCpMd5bzsbXTfpuz3sDvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ضرب‌الاجل شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
ترامپ: نمی‌خواهم ضرب‌الاجل بگویم چون بعدش می‌گویید من ضرب‌الاجل را رعایت نکردم.
خیلی مهم نخواهد بود چون قرار است امضا شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/76245" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=oYIFF-muwj_Lp-QR6HFDcXl_Ya2PWOqUj_vtuV-T1633BZkZhIFBgQV7ItxPHVAww4W1XHn70J-2UWDAC_j_74__7jbKXjAWbDCkzlujZvRdBKbJxeGbUO0h6aT0Bz65AaRhnautOOhjRusR0u8i5qFPF-kxU1aSkd22e1xii3sSqZrJAFCFLTrc60uuF9L7cYZSVRnmwfCT0-SN6bDiIEmZnBfohd1dv2HuIWpFF7tSlw00oFwUhGB2Qs8BkGkMEGOGTZfsg-LutK2dURi9nzokSwY9jER7-a0CZq0Y7lY5C5Ptr78Dq5aOmU4Du4kzvl3cMCAkH2xIs_yl_K8B1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=oYIFF-muwj_Lp-QR6HFDcXl_Ya2PWOqUj_vtuV-T1633BZkZhIFBgQV7ItxPHVAww4W1XHn70J-2UWDAC_j_74__7jbKXjAWbDCkzlujZvRdBKbJxeGbUO0h6aT0Bz65AaRhnautOOhjRusR0u8i5qFPF-kxU1aSkd22e1xii3sSqZrJAFCFLTrc60uuF9L7cYZSVRnmwfCT0-SN6bDiIEmZnBfohd1dv2HuIWpFF7tSlw00oFwUhGB2Qs8BkGkMEGOGTZfsg-LutK2dURi9nzokSwY9jER7-a0CZq0Y7lY5C5Ptr78Dq5aOmU4Du4kzvl3cMCAkH2xIs_yl_K8B1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه باز است. تنگه برای چندین ماه است که باز بوده، اما شما فقط از آن خبر نداشتید.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/76244" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=aj17k_hd6XVgqi2fjU_rUKXLnIheaJtwCJL2rMpm9b6vzZnyLyZiYv861qRMHikuO83R8UslLcQrP3I8vtA0CV3NsQxAHX4Qf-AvW0qRqrhMDxYpmsWnPVomx1w2C4Y67IWtGnO-O2fF3F2cgw3Q4PQmKo0INEO68TCKjxw5_gv7ZJ6TTpDncS7jp0cQ9RrDAiknGo57q3KNCiIDHQhOjPfDjWPy-5jnbQIo4RgXm8IVobB1iCPutFnl_mSlGigtwB4ZU0OFSAWxDIk3_DCoN5g_9CI6PAAC1G-8QJrdCIQ3OndYVmSHPrAUBzVsi4jhfxm93IRaryXrUQaxTfx8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=aj17k_hd6XVgqi2fjU_rUKXLnIheaJtwCJL2rMpm9b6vzZnyLyZiYv861qRMHikuO83R8UslLcQrP3I8vtA0CV3NsQxAHX4Qf-AvW0qRqrhMDxYpmsWnPVomx1w2C4Y67IWtGnO-O2fF3F2cgw3Q4PQmKo0INEO68TCKjxw5_gv7ZJ6TTpDncS7jp0cQ9RrDAiknGo57q3KNCiIDHQhOjPfDjWPy-5jnbQIo4RgXm8IVobB1iCPutFnl_mSlGigtwB4ZU0OFSAWxDIk3_DCoN5g_9CI6PAAC1G-8QJrdCIQ3OndYVmSHPrAUBzVsi4jhfxm93IRaryXrUQaxTfx8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما قبلاً گفته‌اید که ایران و آمریکا به توافق نزدیک بوده‌اند. هنوز این اتفاق نیفتاده است. چرا اینقدر مطمئن هستید که این بار متفاوت است؟
ترامپ: چون آنها ضربه سختی را تحمل کرده‌اند. ضربه‌ای که کمتر کسی می‌تواند تحمل کند. و آنها خیلی بیشتر از من می‌خواهند به توافق برسند.
===
خبرنگار نیوزنیشن در کاخ سفید:
از رئیس‌جمهور ترامپ پرسیده شد که آیا می‌تواند این توافق را به سرانجام برساند یا نه، چون پیش‌تر هم به آن نزدیک شده بود. او گفت: «من بسیار مطمئنم.»
او درباره اینکه آیا واقعاً این توافق تا پایان این هفته نهایی می‌شود یا نه، با احتیاط پاسخ داد: «به‌زودی خواهد بود، شاید همین آخر هفته.»
ترامپ در پاسخ به این پرسش که آیا رهبر عالی این توافق را تأیید کرده است، گفت: «برداشت من این است که پاسخ مثبت است.»
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/76243" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=JmPcDNFxMLn5O-dJyxU1nn6ACz-8EIS7whaP8glfUrbHEFBmaZ3kr42GM8dIONlKExfX6z1INrbYQOLkgeYjdNjwUPpk9fYuTARZIpEjfPS7galfltT-yScC4IH8RMbTTOY9XoJeVK0LKaIMeFl-p384ivFZDKiU7mwvE8w28aMUpicyzFM8vdYdvFX9N04lrt1ZNzxaEsl3T1HKEetH3_D-bAACgatWzO6lYgWDGJ5tgtEJ8BB_iWvYAUteb7Fw8iF22SFwnTKZtNfDBShtWgyulgco8Zb18v0JW8jwrG8p6etJzWwRVc1XFnrSQynCxaUU76k-Q8WXUKTsAycmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=JmPcDNFxMLn5O-dJyxU1nn6ACz-8EIS7whaP8glfUrbHEFBmaZ3kr42GM8dIONlKExfX6z1INrbYQOLkgeYjdNjwUPpk9fYuTARZIpEjfPS7galfltT-yScC4IH8RMbTTOY9XoJeVK0LKaIMeFl-p384ivFZDKiU7mwvE8w28aMUpicyzFM8vdYdvFX9N04lrt1ZNzxaEsl3T1HKEetH3_D-bAACgatWzO6lYgWDGJ5tgtEJ8BB_iWvYAUteb7Fw8iF22SFwnTKZtNfDBShtWgyulgco8Zb18v0JW8jwrG8p6etJzWwRVc1XFnrSQynCxaUU76k-Q8WXUKTsAycmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ممکن است آخر هفته در اروپا قراردادی امضا شود. من نمی‌توانم آنجا باشم، اما جی دی ونس آنجا خواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76242" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=lwywyVlJigKg96rJn-l2Ktj1BBODopS_P0TnvAHxbXxlDvk8cUWaRA6aCY-7s4WxSED7ENfxNP2-rRSg5MEDg64llykACGf2B5PZ1qZrQ3xO4-rix-I2PzaiYHUzhVaMTZmpZDVFdnIXTE0AAa1tNB4VhvR62I6nM9bVNB3ZY1_BzlJ0XN1jXpOpDjY8CY3wvPugBY3YdsK2PNXnPkh-5ckPiTQgpl77_WX3LDPYL3iFOeDquLY7FB7Iy-1jz5wmowErPFirCERUfMN7TGttzCIhRhPOJpklSBtiog6FUCKn2tbO7OKiWew2x9U8BFqpYRkF9ZuZ1YoiJmUiG28axw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=lwywyVlJigKg96rJn-l2Ktj1BBODopS_P0TnvAHxbXxlDvk8cUWaRA6aCY-7s4WxSED7ENfxNP2-rRSg5MEDg64llykACGf2B5PZ1qZrQ3xO4-rix-I2PzaiYHUzhVaMTZmpZDVFdnIXTE0AAa1tNB4VhvR62I6nM9bVNB3ZY1_BzlJ0XN1jXpOpDjY8CY3wvPugBY3YdsK2PNXnPkh-5ckPiTQgpl77_WX3LDPYL3iFOeDquLY7FB7Iy-1jz5wmowErPFirCERUfMN7TGttzCIhRhPOJpklSBtiog6FUCKn2tbO7OKiWew2x9U8BFqpYRkF9ZuZ1YoiJmUiG28axw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به زودی توافق را امضا خواهیم کرد و اسناد تقریباً در مراحل نهایی هستند.
دونالد ترامپ، رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر در خصوص توافق با ایران گفته است که ایالات متحده «به‌تازگی به یک توافق بزرگ در مورد جنگ با ایران رسیده است.»
او گفته است که «ما در حال نهایی کردن اسناد هستیم. این کار باید طی چند روز آینده انجام شود.»
آقای ترامپ می‌گوید که پس از نهایی شدن اسناد، «احتمالا امضا آن شاید در اروپا» انجام خواهد شد و این کار باید «خیلی سریع» انجام شود.
به گفته او «ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که هدف اصلی از آنچه که ما برای رسیدن به این هدف طی کردیم، همین بود. بنابراین، این یک چیز بسیار بزرگ است.»
رئیس جمهور ایالات متحده تأکید کرد که توافق «به زودی امضا» انجام خواهد شد و اسناد «تقریبا به شکل نهایی هستند، بنابراین خواهیم دید».
آقای ترامپ همچنین گفت تنگه هرمز نیز «به محض اینکه آن را امضا کنیم» باز خواهد شد.
او همچنین می‌گوید که با رهبران منطقه، از جمله متحدان خلیج فارس و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده است و افزود: «تمام خاورمیانه بسیار خوشحال است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/76241" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سی‌بی‌اس:
احتمالاً اوایل هفته آینده یادداشت تفاهمی بین ایالات متحده و ایران امضا خواهد شد که راه را برای مذاکرات بیشتر در مورد یک توافق بلندمدت هموار می‌کند.
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76240" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VziLtV-rpY5K7SHT7QZonW3DeDgz71Fj2JtXCe6a0Q6u8HxHz9Nlpi5Hkut5fecGqrxI3nVhjGtgf77Zvz6uygTTTN7dcUmioqsazzEUi3MXmWdRB9L29nQpjIYILJJUTg75Y1wTvuG3bKv3X6iRSlyOIcxSCGbQwGKtBqoACe_h9b7YQi2XrYnaww6v0iWPBLJ2uKA2WahZGtcQ4k-9AP5e0wDHumW7q_Bkz3S0WY_2eLVr15uSJc7Mp3OzZKCnml0Cmnq1H2jiLiBewfo6tYktNN4zgrPLGWLZ10urwgDNDpIMMfmLWZHGp1eRgWiOMk7jpuLFs5S-x8iOL531Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در پستی جدید نوشته:
"بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال تایید این متن در مراجع اصلی‌نظام بالا است‌."
🔄
آپدیت:
خبرگزاری فارس جملات بالا که در انتهای پست نوشته بود رو تغییر داد به:
"البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76239" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqf-lFwGdg_D6lJgHS6pg1ryP1YloIWXagPunoNoTBEY_cNflZqF39RNEPD7hK6UxpytOnlp5S09N2HR1VU_powUeTwrxr62oEgohAxF2lOHyIXz6uSh0JDU-nE9lXHwEUmNbm36ywXIwJk4an1FZPGNXEKcPhd9no_Dislj-34xDp_iGujvNY3PAsB3G9X9-WoUOWotaXQnww1XXewJVdb3jpougB6FKvkzaZtZQhHSK65ei_BHqZF-Tc4yFZ6PufYRLmBBEjnfflHP76K2Kuk7RBjFTRgc2vwejGHLkm5eE1WrEc3sXuneAlu90uZ5F-NEbVAa5EPYoUGxPoME2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث به نقل از یک مقام ارشد گزارش داد هیات قطری که از تهران بازگشت، موافقت جمهوری اسلامی با پیش‌نویس نهایی توافق را اعلام کرد.
همچنین دفتر امیر قطر اعلام کرد که تمیم بن حمد آل ثانی، امیر این کشور، و دونالد ترامپ، رییس‌جمهوری ایالات متحده، پنج‌شنبه در یک تماس تلفنی نتایج رایزنی‌های آمریکا و ایران را که به پیشرفت در تفاهم‌نامه پیشنهادی در چارچوب یک مسیر مذاکراتی منجر شده بود، بررسی کردند.
دفتر امیر قطر در بیانیه‌ای افزود که ترامپ به امیر قطر گفته است تلاش‌ها برای تکمیل مراحل نهایی پیش از اعلام ترتیبات مربوط به امضای یک توافق ادامه دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76238" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک‌تایمز: ‌قبل از لغو حملات برنامه‌ریزی‌شده به ایران در روز پنج‌شنبه، ترامپ با میانجی‌گران پاکستانی صحبت کرد که به او گفتند با ایران «توافقی» دارند.
clashreport
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76237" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSBFsh3qmPE3J-8zI1KJy430wOHjV2-whQi4EYxgg8Q_P05rm271MGPMtQ3PIEJJImlsbYUWRC2N0dDDPxagJHSO20VzEHk5-sOS0dBbKWGWHuYv_yZ67Z4kzZ9FtaXv6s2xXBkRmFA4KtddhO3hThyeJrCUxPrwE7VY5F_gHE7RPsRxJEBLu5sn2Y6pM_Ba0lgw2yG4A-Ouq9Yd-pq2pcjD2PNug1nguVTm5uMr-yh8IvIKBx1aIzh9GTk7t6tgAG5s-r4HWJwcdQbhv9AqGcbplZ1vw_X5lZQl_bAkZKqyzycaK5HXU319GyDDjqXbOgxcCpCHuhzCDJhhIEsxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد پست دونالد ترامپ در تروث سوشال درباره نزدیک بودن توافق با تهران، بنیامین نتانیاهو را غافلگیر کرد؛ در حالی که او در میانه یک نشست امنیتی درباره ایران حضور داشت.
سی‌ان‌ان افزود که این کشور از وجود هرگونه توافق قریب‌الوقوع با جمهوری اسلامی یا تایید آن بی‌اطلاع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76236" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n2uxYfbHOJ5HKoM3jm862QYC_j9vQshNogQNlkjdulkZATqIcHsGMS2gkEokgHNadxYzPXaYHEXEeWYahm7ThQ7v2i04RtPzBaxui5q33n_Qa8En4QLAXy1b6DwEjwONIdaMnyPef3olmJQbQNB_05SnirqQGoYMf5I3xMcTklzFGDkEOHsKJ-EDMzmF-Eodrr7Bv2YStr35iWJqb63rIm4zwrpG3TGffVmL7LP5fvZQvw-NkLFHx8XdSGI9McVsRAYo3H_NpmHAWz4Y33o5wO7uf3KM97kWdOTET-U4WfIermMtOgbjkqMJQcR8KURFHUVdmInr1neAm--6qCdSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، ساعتی پس از پیام دونالد ترامپ دربارهٔ مذاکرات با ایران، مدعی شد که «هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تأیید نشده است».
فارس ادعای خود را با استناد به اظهارات «یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران» بیان کرده است.
رئیس‌جمهور آمریکا گفت: «زمان و مکان امضای این توافق به‌زودی اعلام خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76235" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ri8F5LFj69ORlkgMM-Mv9C-dEmG69hBriC_P7ZramKaSghnJ-qSbruR56V7N21BvTtBxrbAToALHdI5HK6xbhgGXhX5IxCAC80BKq_sI6ETwMwPPzl4TLmad7KidHK6c-R-LXuC3YSGL5Mg4-pQUr3oCDp6aiP3LPjBJYGfGmlTLrdCAl1GhwJqigkgQfpIllMg_9vnnOaRBs9DWNYt2U1Qys5ReIuwrrDGMRT2xqdVZUQbcp047eFbFKhUn6zyqGUnr3LFNCRdeKpfmieTolmOJzcxKDbqvkohcxgPXE8TmXUj5zMC3OJ0EnIl9YNhSKZ9kZTH9JAJr7nl3JkHDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه منبع آگاه گزارش داد اختلافات اصلی تهران و واشینگتن برای رسیدن به یک تفاهم‌نامه، چهارشنبه در جریان گفت‌وگو میان مقام‌های جمهوری اسلامی و میانجی‌های قطری برطرف شده است.
بر اساس این گزارش، مقام‌های ایرانی پنج‌شنبه به چند کشور اعلام کرده‌اند مذاکرات تهران به توافقی اصولی منجر شده، اما مجتبی خامنه‌ای باید تایید نهایی را صادر کند.
این منابع خاطرنشان کردند که هم ایرانی‌ها و هم قطری‌ها تاکید کرده‌اند که حملات آمریکا در طول شامگاه چهارشنبه، تردیدهای ایران نسبت به نیت واقعی ترامپ را به شکل قابل توجهی افزایش داده است.
@
VahidOOnLine
ترامپ: توافق تقریبا نهایی شده
ترجمه ماشین:
... نیویورک‌پست نخستین‌بار گزارش داد ایران چهارشنبه‌شب پیش‌نویس نهایی یک توافق را به میانجی‌های قطری ارائه کرده است.
رئیس‌جمهور ترامپ روز پنجشنبه، پس از اعلام اینکه حملات برنامه‌ریزی‌شده علیه ایران را متوقف کرده، به نیویورک‌پست گفت توافقی که مدت‌ها انتظارش می‌رفت برای آغاز مذاکرات هسته‌ای با تهران «تقریباً نهایی شده است».
او در یک تماس تلفنی کوتاه با نیویورک‌پست گفت: «تقریباً همه‌چیز نهایی شده است.»
nypost
سی‌ان‌ان به نقل از یک منبع آگاه گزارش داد مقامات آمریکایی بر این باورند که نشست‌های این هفته میان مقامات ایران و قطر در تهران، به حل برخی از نقاط مبهم و کلیدی باقی‌مانده در توافق با ایالات متحده کمک کرده است. این اختلافات عمدتا شامل جزئیات نحوه پیشبرد مذاکرات آینده در قبال برنامه هسته‌ای ایران و ترتیب زمان‌بندی لغو تحریم‌ها و گشایش‌های مالی برای تهران بوده است.
بر اساس این گزارش، ایران اواسط این هفته جدیدترین پیش‌نویس توافق پیشنهادی خود با آمریکا را از طریق میانجی‌های قطری ارسال کرد. این در حالی است که حدود دو هفته پیش، دونالد ترامپ با اعمال تغییراتی در متن، خواستار سخت‌گیرانه‌تر شدن لحن توافق در بخش هسته‌ای شده بود و از طولانی شدن پاسخ ایران ابراز نارضایتی می‌کرد.
با این وجود، رایزنی‌های این هفته از طریق قطر باعث کاهش شکاف‌ها شد. مقامات آمریکایی در تمام این مدت در تماس مداوم با میانجی‌ها بودند؛ حتی در روزهایی که واشنگتن و تهران به طور پی‌درپی در حال تبادل آتش و حملات نظامی به یکدیگر بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76234" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CtWzlzHEcVB_QLBM9VqFaIBz1-w8uUMOySZNhepYzsvbKhu9tc_M5u3j7fwCjIVCMghR6jP2RIFGeR3c8u8whQ7VXlR3YjKslku1y1rKMgCSWDo9KlyFK_3d_8-18hGxboqKvOqM7zIG0YK8R9pfcO9_phjcU-vKc1nNhmi2i6cEDMYiu2A5ha0aGd7AyLDBE9K4RKD3Kv2R8oVfjHpybR2SaVKTLoltuOVQEUQeO-dHVr9MjzIDZEridWTg2SCh4gmDfNTQTNkRnPuO3iTOUsS4FgmSQ9HWiUqLQILDoJz9IoXcxrGQUq9e8kZpYupp3S6ELSuUt1O910yuRO-qRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله امشب را  لغو کردم چون بالاترین سطح رهبری در جمهوری اسلامی توافق را تایید کرد
پست ترامپ، ترجمه ماشین:
با توجه به این واقعیت که گفت‌وگوها با جمهوری اسلامی ایران به عالی‌ترین سطح رهبری ایران رسانده شده و مورد تأیید قرار گرفته است، من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران در شامگاه امروز را لغو کرده‌ام.
گفت‌وگوها و نکات نهایی، هم در کلیات و هم با جزئیات فراوان، به تأیید همه طرف‌های دخیل رسیده است؛ از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران.
محاصره دریایی تا زمانی که این توافق نهایی شود، با تمام قدرت و به‌طور کامل برقرار خواهد ماند — زمان و مکان امضا به‌زودی اعلام خواهد شد.
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76233" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdxWQakusBnd_SKmf4UHcYgVAMqsbOVPafMy9U0GeCkqrfgU8NE7lJsVf7ktWmvHUH_Vh9gC_DipmKyr3YbwJ-VF5SDS9FOu3NlirsiejSRX8kcp_oO7dwYLGF3c7JcdhB3bzOHBnGLN5xw_sHG0oGdXU7UNY5osjRj4sGwNcHNBAM68QaB421sDR6pI5m2NsJ-h5vFnD1dkxEn8zj_A65yFfAY80CR4e0rrMSK4gi8JdtFt7pnlxLwLq3vXU4uplK8XZ3_7nmJNArf8AqeIQ1bxn9As_qISWOqPnfZ9X4jYwKtbKRVtmK3B6MSEnTKX5U9daetSvGHzyVRGAv-aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در گزارشی اعلام کرد ایستگاه‌های زمینی استارلینک در اسرائیل، قطر، اردن، امارات و عمان به همراه سهامداران شرکت اسپیس‌ایکس و زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» به فهرست اهداف نظامی جمهوری اسلامی ایران اضافه شده‌اند.
فارس مدعی شد این تصمیم پس از به دست آمدن شواهدی مبنی بر استفاده ارتش‌های آمریکا و اسرائیل از زیرساخت‌های تحت مدیریت ایلان ماسک، از جمله شبکه اینترنت ماهواره‌ای استارلینک، اتخاذ شده است.
بر اساس این گزارش، «ایستگاه‌های زمینی استارلینک» در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران شرکت اسپیس‌ایکس و همچنین زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» در فهرست جدید اهداف ایران قرار گرفته‌اند.
فارس نوشت: «ایستگاه‌های زمینی استارلینک واقع در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران اسپیس‌ایکس و همچنین زیرساخت‌های دو شرکت الفیظابی و مبادله، از جمله مکان‌های جدید در فهرست اهداف ایران هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76232" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o70ellaA0Fk_faPXwrD__U9KBfBQYPGGfIabv4GGGRoVlfXvApWbBX5PSAezPU3nGLLWtfow4O-XrQAkzQQTO6HRtB0HbJHDV7YVjk52825srvSGsb-OXsNdV_dsMPIwCyKnPewT8T7iRVfK1NGygmxdBTE2a5VXoWTJrI-XNu5KicHKwZgQAaBtYVPj0yOrR_am3uKt9Ap4uxBLB2ZqhwyMU8ZwaDldwtt9gTHksdXD-PyFUObUuieH4LngWoRvLq2fGUncpP7L2WSE04Suyj0TnaPaTFarSl3VSkQcGjOoVVU4c-QdF2Yj2t0-rHhGMJ2WMNOj0H0PRD2YaNd7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع جمهوری اسلامی در بیانیه‌ای اعلام کرد «هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.»
در بخشی از این بیانیه آمده است: «بی‌تردید نیروهای مسلح جمهوری اسلامی امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76231" target="_blank">📅 20:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHn6a3JSm2aAJqAqVmSoZ_etpRxqBku-TRp-QqDr_sbyvTMQs51xh2LXHYZCprmfjgYGWu0bs-1eiRZNba6wTGNphVPH9IPRdu0H68HmeBRnTFmR5029gkwpOatI72Pi9hJvoTCaDYJkqmY9eRLP8PqeAIT-4rJnzTwydBhGAXoZe9a5obvZu7ePTKGTGLHNkICClK9ilynBcddEFr0LC7ZZHzn4hESeeNb0djL1OD02XXv3pE3ZpySf13AVBg4J30GWKj5R29nXrnoYicS2kB1MqV4EMAfO4-4Irbas4AQxmgaIlMYTDCiWxuVsY12pCrGVxUNPOd7E76BtTtYI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در خصوص تهدید زیرساخت‌های نفتی ایران از سوی دونالد ترامپ گفت: «یا صادرات نفت و گاز برای همه برقرار خواهد بود یا برای هیچ‌کس امکان‌پذیر نخواهد بود.»
او ادامه داد: «در صورت تکرار حملات آمریکا، پاسخی شدیدتر خواهیم داد و آتش جنگ می‌تواند گسترده‌تر شود.»
فرمانده قرارگاه مرکزی خاتم‌الانبیا اضافه کرد: «تناقض در گفتار و رفتار آمریکا عامل اصلی ناامنی در منطقه است و امنیت تجارت بین‌المللی، به‌ویژه در تنگه هرمز، را به خطر انداخته است.»
او گفت سران آمریکا با «عدم شناخت ملت ایران و نیروهای مسلح» در دور باطل قرار دارند و با جنگ رسانه‌ای نمی‌توانند «شکست‌های پی‌درپی» خود را پنهان کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76230" target="_blank">📅 20:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1ic1MXIVsje76ef43uHieqLXxW3Sj9FHhqvL3yDbOEj2uo7IcMK-UftEGWGlJZoIqvo0yl2JusbvmvLDJZWaGsmeFOEOirTULbu3W8N7jS9RWrEOPzU9r8765ruG4G9hkD64PDxZS1uMqhpfRaholRWw7uiPyHpvBLsym2L6pHDQzUAU6979RrRTyXuOHQajmiVaWz_CK18Xcyt44-XzL4wRCz1Mms9XGfncFtgVlKWA2FGBiJV43ke6uGOVsfxg-oQe_loK8ZcaxNruCrAqRlVyhUDnFzcSkycI8shmXp0IHisJ9a98C7oxZJ4ppJRqrEVRy2VyzClZoD3d8KFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
"تنگه هرمز برای عبور و مرور باز است
مسیرهای امنی برای کشتی‌های تجاری که از تنگه هرمز عبور می‌کنند ایجاد شده است.
این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.
صدها کشتی در دو ماه گذشته از این مسیر عبور کرده‌اند.
نیروهای آمریکا برای دفاع در برابر تجاوز ایران در موضع آمادگی قرار دارند.
ایران کنترل تنگه هرمز را در اختیار ندارد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76229" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=X8K7-ZVd6b53HG4GSbDcUBkR37iEMeqyYuSqRzFgtjtMEn6JMAvp4WvlZCsxPC7j0Weg2sC89PasqGx88iXOHS0w0sxGR9Rnvs21m6SOg2fvpc5ZkERPiFbdaOW006BAtqaZ-55C0_FqvJf9tLWNRbCb54l1_vnuqj4ZzPJ2Nn44Oa6_vP-p6GeUa5E6P8bvRH-3DbmrJI5YYYFZx7z0Aauoq0oeeda8SYhDEK-qzmp-pzJgHdqoW5FViqWfPU7xt0RXXf484FDboXAoJRxczFlx1M9Z56YdPpn99vkQNtez-po8KJ-ralS8vu-eB-5kLXJWFlv2Sc6KA4ZwcXCnVLsHpeJnD2kbTa94Wn3I8JhnOuim-5OGfo0Qp_WQ9AA6W1V6ftcpQlTurgZPNUb160Pfh28SRPoiRC_hZ1y5fYIT8nYlrfqsKlabF32iZbIvuujOuytpE4mAWnm9386OK1qafw69-cu8wu9MhzHRdFPTJ3SptgwoNRVn-seEfHJAwdU_8lnToaQQ3OdqCQCEDQNLx3mDlayUtCrUXPnNpkrpYzXVlyOhq6IsVC1yhMA_AMWcYu2go5ykXPRbFonzuYNl3hkB0AC8pARf5FXw0FCvEGFYvENxx4qaGarwcTzaZsk-Rt7wK1bQyd8ZXyFLPkq8oonPnZF6ZLsQE1vHY_M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=X8K7-ZVd6b53HG4GSbDcUBkR37iEMeqyYuSqRzFgtjtMEn6JMAvp4WvlZCsxPC7j0Weg2sC89PasqGx88iXOHS0w0sxGR9Rnvs21m6SOg2fvpc5ZkERPiFbdaOW006BAtqaZ-55C0_FqvJf9tLWNRbCb54l1_vnuqj4ZzPJ2Nn44Oa6_vP-p6GeUa5E6P8bvRH-3DbmrJI5YYYFZx7z0Aauoq0oeeda8SYhDEK-qzmp-pzJgHdqoW5FViqWfPU7xt0RXXf484FDboXAoJRxczFlx1M9Z56YdPpn99vkQNtez-po8KJ-ralS8vu-eB-5kLXJWFlv2Sc6KA4ZwcXCnVLsHpeJnD2kbTa94Wn3I8JhnOuim-5OGfo0Qp_WQ9AA6W1V6ftcpQlTurgZPNUb160Pfh28SRPoiRC_hZ1y5fYIT8nYlrfqsKlabF32iZbIvuujOuytpE4mAWnm9386OK1qafw69-cu8wu9MhzHRdFPTJ3SptgwoNRVn-seEfHJAwdU_8lnToaQQ3OdqCQCEDQNLx3mDlayUtCrUXPnNpkrpYzXVlyOhq6IsVC1yhMA_AMWcYu2go5ykXPRbFonzuYNl3hkB0AC8pARf5FXw0FCvEGFYvENxx4qaGarwcTzaZsk-Rt7wK1bQyd8ZXyFLPkq8oonPnZF6ZLsQE1vHY_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما هواپیماها را وسط تهران به پرواز درمی‌آوریم و آن‌ها حتی خبر ندارند. تمام رادارها و پدافندهایشان نابوده شده. آنها تمام شده‌اند... برایشان سخت است چون مغرور هستند. ۴۷ سال قلدر خاورمیانه بوده‌اند...
ویدیوهایی است از
این مصاحبه فاکس‌نیوز
با ترجمه و زیرنویس هوش مصنوعی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76228" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3ZZ7ce6dEHumYQe5PINbLNmclqD5i-8HHa_c0jjYqNKEOZ4ruhE-VcExiWS2PCjdPsgvf889-_JN4ij8POtugdjvUPeRnQkvr2UWEzbiLMJ1xEP2tGvK9VN4DaWj0u_mgRUnUteZic99tdVCHosEEWYSuAOxng0epCy4bssSXHrO6iLwQ1aqOIPCVIifeXCJ8G0JqUOopgT6v4mQQNlP2d2lDsY4YiQwbWDY4ji7yU4vRFVsvvfaK6TG9jnLWbEluOy75H63KIOWfgJvajx8YiYH7byFYXGW8WRklm1XTk6ziv8W1sYYnIWz0vP2LME_l-SwZpDA1J2Yvu-SvXohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از «منابع آگاه» گزارش داد که مقام‌های ارشد امنیت ملی امارات متحده عربی و ایران برای نخستین بار از زمان آغاز جنگ آمریکا و اسرائیل علیه تهران، حضوری با یکدیگر دیدار کردند.
این دیدار که در هفته جاری انجام شد، به نوشتهٔ بلومبرگ، نشان‌دهندهٔ چرخشی قابل توجه در رویکرد دو طرف است و در شرایطی صورت می‌گیرد که هر دو کشور بیش از پیش به اهمیت روابط دوجانبه آرام‌تر پی برده‌اند.
این خبرگزاری می‌گوید که منابع آن به‌دلیل حساسیت موضوع نخواستند نامشان فاش شود.
بر اساس این گزارش، رهبران امارات می‌خواهند برنامه‌های بلندپروازانهٔ اقتصادی خود، از جمله سرمایه‌گذاری میلیاردی در افزایش تولید نفت و ایجاد مراکز دادهٔ هوش مصنوعی، بدون اختلال ادامه یابد. این رابطه برای تهران نیز اهمیت دارد، زیرا امارات پیش از آغاز جنگ یکی از بزرگ‌ترین شرکای تجاری تهران و مسیر مهمی برای انتقال نفت تحریم‌شده ایران بود.
به گفتهٔ منابع بلومبرگ، تماس اخیر ابوظبی با ایران عمدتاً با هدف دستیابی به نوعی تنش‌زدایی با حکومتی انجام شده که آن را دشمن می‌داند.
از زمان آغاز جنگ خاورمیانه در ۹ اسفند پارسال، ایران بیش از هر کشور دیگری امارات را هدف حملات خود قرار داده است.
ابوظبی نیز در چندین نوبت پاسخ داده و در میان همسایگان عرب خود تهاجمی‌ترین موضع را در قبال ایران اتخاذ کرده است.
با این حال، به نظر می‌رسد امارات اکنون مسیری مشابه قطر و عربستان سعودی را در پیش گرفته که با وجود هدف قرار گرفتن توسط ایران و نیروهای وابسته آن، در پی کاهش تنش از طریق دیپلماسی هستند.
به نوشتهٔ بلومبرگ، عربستان که تأسیسات انرژی و پایگاه‌های نظامی‌اش هدف قرار گرفته، از اوایل ماه آوریل تماس‌ها با تهران را در سطح وزیران خارجه از سر گرفته است.
قطر که تأسیسات بزرگ گاز طبیعی راس لفان آن هدف حمله قرار گرفت، بیش از همه در پی آشتی بوده و اواخر ماه گذشته میزبان هیأتی از ایران شد و به‌طور فزاینده‌ای به‌عنوان میانجی میان واشینگتن و تهران نقش‌آفرینی می‌کند.
بلومبرگ تأکید کرده که هر سه کشور عربی به ضرورت همزیستی با همسایه‌ای در آن سوی خلیج فارس، با جمعیتی ۹۰ میلیونی و توان نظامی قابل توجه، واقف هستند؛ حتی با وجود خسارات گسترده‌ای که از بمباران آمریکا و اسرائیل متحمل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76227" target="_blank">📅 19:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slvAOI09-G7y6simFu6n-KB4L-wknouyJT_1HzKoBteWjx6XD0S5dmufWfYXfeZ1evuO9p_LZUC7EDaJ8f0aIWYIFAaKBmdmt1DOUJVOyop-LP912A8_gBRw64vw7kDXO295_V8XjkbdShIv0sa33rLfYxtivupqLyon1CBvgSwFze6WPzUbHWzqoUlW8zStdVWde5txe0ZHoyVfudJnqSa5ZyA53QfKEFd9m6sV9TMdjIGwk62_RzOscdbEbRvIN0ByDMVmqsu5fF4W9svPrkC2_00A6Qosx2aJtriuisyp08yLtWlYmGOvT0axBXGGDL41KdvSF0q8ZhGDkZMHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان روز پنجشنبه به نقل از یک مقام ارشد پنتاگون و دو مقام دولت آمریکا اعلام کرد که طرح‌های ارتش ایالات متحده برای تصرف جزیره خارگ در جنوب ایران از «ماه‌ها پیش» تهیه شده، اما به دلیل «بیش از حد پرخطر بودن» کنار گذاشته شده‌اند.
دونالد ترامپ، رئیس‌جمهور آمریکا، ساعتی پیش از تمایل خود برای در اختیار گرفتن این جزیره به عنوان یکی از مهم‌ترین زیرساخت‌های صادرات نفت ایران خبر داد.
سی‌ان‌ان به نقل از مقام‌های آمریکایی نوشت: «دیدگاه غالب در کاخ سفید و پنتاگون این است که تصرف جزیره خارگ یا نابود کردن زیرساخت‌های انرژی این جزیره، عملاً ایران را ورشکسته خواهد کرد و توانایی‌های آن را تا حدی کاهش می‌دهد که دیگر قادر به ادامه جنگ نباشد.»
در عین حال مقام‌های دولتی به رئیس‌جمهور آمریکا گفته‌اند که چنین عملیاتی نیاز به نیروهای زمینی پرشمار خواهد داشت و «ممکن است به تلفات سنگین نیروهای آمریکایی منجر شود».
سی‌ان‌ان ادعا کرده که پنتاگون و کاخ سفید هرگونه اقدام برای تصرف جزیره خارگ را به عنوان یک «گزینه نهایی» در نظر گرفته‌اند؛ اقدامی که به گفته مقام‌های آمریکایی «می‌تواند موازنه جنگ را تغییر دهد، اما هزینه بسیار بالایی خواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76226" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bagwnPaXkzwy_xvfMjBWVCSrUe9GqhSTgF7nkeS4yWaQiLK4ok74KODXeYKqg2tE7Df5AEKCGqRvQCrYYPhOtgLHzmQkTN790ch6_1vcYeNHUCv5sbpQ49Y6g375vD-pRhmszCYCINov22mCV29h5R0QfpP-iwKdt3r57HrOp7mLAKjadvNkR7DAwDEA8EmAwO745sGR4lU2OKZ4WUDVufNPAqXMHQzbkuSqrgKKRBQASHer8hgwDZMPAbM6Wofj2ewtL4CvQLJwtfnRLmxLe66lZo_JUxXDfya3xZFRMsK01JnC05HKZ86Q2NiH1_KlHExF63OEn8zp1seHDIkzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
راهبردهای نادرست و تصمیم‌های شتاب‌زده، کل صحنه را به شکلی بدتر از نو تنظیم خواهد کرد، زیرساخت‌ها و بازارهای انرژی را منفجر خواهد کرد و باتلاقی بی‌پایان خواهد ساخت که سال‌ها در آن گرفتار خواهید ماند.
شما با ایرانی متفاوت روبه‌رو خواهید شد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76225" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvD5ZylozrH5AYBIv1bI4Tsp2evfB_zG7d-aC6u-SJxw1-rEKOVEJSFtzDzttgsi27TwIUKNJd5ILXA2cFYulV_ZlfDS4GdQOhLl6jQV9Tj9nMFxDY01IUZ4HyR13xrt3rHKn48K4ALMPAN9hechVxE40-0XmiFbMkuwuz-EmaI-oRYplu1OUEkkkpc8fcPEbxL0DNYt2ITdB1r3Gg7ezZ38BHJNiTLfOAoqeqSLORzWHIJhxWBlIu9vjRbXGFrke1xZLGb73iEK9ODL8ZxicwsM-MPGMtj3l3pR7tpxqYMUYAIgPI_H3CTUWdZSC86sij0Q8BAkTFLS30e-2Mujzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آتش‌نشانی و امداد و نجات شهرستان آرلینگتون در شبکه اجتماعی ایکس اعلام کردند که ماموران آتش‌نشانی در حال بررسی حادثه‌ای مربوط به مواد خطرناک (Hazardous Materials) در ساختمان پنتاگون هستند.
شبکه خبری سی‌ان‌ان نیز به نقل از منابع ناشناس گزارش داد که این ساختمان تحت قرنطینه و تدابیر شدید امنیتی قرار گرفته و کارکنان چندین طبقه از آن تخلیه شده‌اند.
در همین حال، سخنگوی پنتاگون در این باره اعلام کرد: «پنتاگون متوجه مشکلی در کیفیت هوای ساختمان شده است که تا زمان تعیین میزان اهمیت و خطر آن، اتخاذ اقدامات پیشگیرانه را ضروری ساخته است.»
او در ادامه افزود: «وزارت دفاع در حال اجرای پروتکل‌های حفاظتی استاندارد است؛ این اقدامات شامل صدور دستور پناه‌گیری در محل (Shelter-in-place) برای بخش‌های آسیب‌دیده ساختمان می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76223" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک صداهایی شنیده شده. گویا بیشتر در غرب تهران
پیام‌های دریافتی:
سلام وحید پونک سردار جنگل همین الان انفجار وحشتناک
۱۸:۲۹ یه صدای وحشتناک سمت پونک اومد
داداش صدا اومد الان، هوا هم ابری نیست، شمال تهران
سلام غرب تهران (صادقیه) ۳تا صدا اومد
توی پونک اشرفی اصفهانی صدای انفجار اومد
صدا میاد شدید ولی هوا صافه
سلام وحید جان
تهران ساعت ۱۸:۲۹
صدای چندین انفجار پشت سر هم
من از محدوده تجریش شنیدم
سلام‌ وحید جان
خیابان جلفا ۲ تا صدای انفجار اومد از دورتر
ساعت ۱۸:۳۰، ۲۱ خرداد
اندرزگو یه صدا خیلی دور اومد
شبیه رعد وبرق ولی ابری نیست
سلام آقا وحید تهران انفجار شد یا توهم زدیم؟
میرداماد همین الان صدای انفجار اومد
سلام وحید جان ساعت ۱۸:۱۷ ما سمت مختاری هستیم اول خیابان ولیعصر صدای انفجار اومد ولی خیلی نزدیک نبود خیلی هم دور نبود
صدای موشک و‌انفجار بود انگار
نمیدونممااا من از صداش خواب بودم خوابش رو دیدم بعدش بیدارشدم صدای انفجار شندیدم
من غرب تهرانم بقیه رو چک کن
سلام وحید جان اگر گزارش صدا از  تهران شنیدی ۹۹٪ رعد و برق هست ابر خیلی کمه مردم فکر میکنند انفجار هستش
آپدیت:
گویا صدای رعد و برق بود.
بلافاصله بعد از انتشار پیام‌های بالا یهو ده‌ها پیام اومد که صدای رعد و برق بود.
آپدیت: حالا بعد از این آپدیت هم شهروندانی دارند عکس می‌فرستند که هوا به این صافی رعد و برق کجا بود.
ولی برداشت نهایی من از اون همه پیام‌هایی که نقل نکردم همون رعد و برقه. آسمون هم همه جا صاف نیست.
آپدیت: بعدش هم برای خیلی‌ها که شک داشتند واضح شد که رعد و برق بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76222" target="_blank">📅 18:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=F4Ln4dhkoEi5JYNgtRDFrn8jo1yMuehocqmrXyAE1w2yQAc_9287LYn8OjuYPnZqVzkDYeyP4jHg7o0-rsGmrBPzSVSH_69T6bOQz-vz7PSiFieOx8BK7oI-UeJOPOYsvaXT39YsIeouJKQkVw66S0WWZphE9lIoe-DbY0pTbOhRS6basTctVxefoogUIHarXsiGrfNkZxrAs9jLkFDLYFC4tUuW2zC6g7rjgDlkDsP_2T4V4HX3i_cD4H2t4LOkILMBLX5ys3CbCmgfIHbLLzWe9KCFawmrr_Faf5UWnpqs8wLK5MXSFGyZgC_VZ7KrDghKq9XbpXpqShG-qdmUNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=F4Ln4dhkoEi5JYNgtRDFrn8jo1yMuehocqmrXyAE1w2yQAc_9287LYn8OjuYPnZqVzkDYeyP4jHg7o0-rsGmrBPzSVSH_69T6bOQz-vz7PSiFieOx8BK7oI-UeJOPOYsvaXT39YsIeouJKQkVw66S0WWZphE9lIoe-DbY0pTbOhRS6basTctVxefoogUIHarXsiGrfNkZxrAs9jLkFDLYFC4tUuW2zC6g7rjgDlkDsP_2T4V4HX3i_cD4H2t4LOkILMBLX5ys3CbCmgfIHbLLzWe9KCFawmrr_Faf5UWnpqs8wLK5MXSFGyZgC_VZ7KrDghKq9XbpXpqShG-qdmUNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'لحظه انفجار حمله حدود ۴ صبح به پیشوا در استان تهران'
ویدیوی دریافتی، پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76221" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hwqUzrjZnc5eK1Il6NgWwJ6ejDmWRpRpAeRD9--RAIVIwS_C3IcVjA6x3F_96umReKKdkI15hIySLjJTqUsg0tey4OYyVP9BCBr8BCDwsHEd-MGek1nUAtzxVHzAP7s2YCbZL1qgWan-C3jQpNIxkS7EmltzWqTs5MtsWRyW7ewbAKL_NDgxokdOBldvBYL8sArKjTK3gCs5TFlV0Qhj31_6KnNBJpiDBif2MqORgo5hlu7GgJptk_MJjRmVtM71iXY9W01i3fGUp0R7O2BvaSbkVW_NSBUFMLxq_bQPMJ9XLuEaxmT1VQ-dD5LIwHmforwSgsQpHJX_B7-xow95RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YWADiIYDD1ZaUIdPRHWyEASQfwMoWxB61pcKa6o9ey0jr2b4CTtm8qUURyN14oRqgRSjJ10kZTaNXNpP4sUpiHdEPJAMcfeZCUmn1WW8PlmhBn1INoQ19eeib6JwzQmy5Z9Wxur797shPKY9fGnCAcCT9zgjjUCIfiAW2kC6vwO9IlPQdsAoIrCiWTWMcFVaNKUN09BZrsMFlgnqCX3D62QEZAo6tolI_oIDXtkgbxJwL1x4dil4fbYzTUu5ZskndY6fY0r6DdBmR5n7-bfIzQdKT_hoe4Q2lnBKXzM4oE3bSWoxrN9MKF-Hl2HpBb673gm8sDoOfHDQcHeSa0Wqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D_ShHQItmeRkEBCwIBUaZ27cslZShMvyaqpe-HDrAQ08jXzPq1DNFt436ZQU-BjkAtb3DDnJdkAayU_haeJZeNUcBddFQHreojhcyO5-a53AbqvMymA03d9Jrn77qPNmgCtvW75B3Q7zM7LK9BxtEs4Rn9B80yc-lV7DF3FZCu2_F9-p1lk4GRUMwFsBpDWNKCedzGnKut88ZGKnakTRsh1BDT-1T8vpAnRav9NO71LiTZSux8ult0fxx4pUVpnguecp6AL8_7VHaRiK2AecbQ6BcPmXpSBOT2XTkLR7-Zr8gkuuZ_HG1Wiqig27ZoJWKM1r4_T18J6QZ4gZLnVCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QWbcZWtdnzqmAqrE57wFdcfWAq2I31cPejKWVhwwwPEq1KAtLYJ_qnyLfucp28MgoXTGkZ0NqkV4nVZhOYbhfthuJYKgvM_5EgRhg5L6vH4sJTZGdyPq9A_gSK-_pIIbiunTSTG3j7XwWASoyiVJzBTQG7SZJgF1ig9OC4v0YXCdZHtV2-JiG_vFi2M1xxxBg5Oibbm9YJxEhW5b43z-qu53UroZ_ZyVdd_-cOVyZJwLF1DVWgaLBqPFS7DqKOcMg_803K4qNpgtCKV9PB4L-yOeD3wKLz3DNBOOdEXJWKlKPbofwDXgi5GHBkeCcplLbvwJxZs1wCNiHPADvDqdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XtKIT_9sUBAEc0eDYyCs-K0UpQMaCYftaFngYhLULiQysNtRvLhqw2urSVQAtd-07iJp-myuLIcYvgye6HXyLij5yA1h5jJwwqG-kEaSem2R49VZAg_mxn0BPDmIwwXOE0Mqn_gRA4asQUDh-IaHdcz0ElS3C8IwAd_0vFnGthZRERKmfZXIiuXK_5CjiF2ptdduNaFSHBTUgf6I5VqEINKwWeWTpGFmPiAv3FwDxwZPnnHDpTYothSmDLccPs1Dht3lw-JzxybQCDUYRBQ_UJGyDL4DBVrm4J_hZA4VKXXA9oxXUbKb3MCQ1hq6yaChZfACIEcTcsrjUchlxhzCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ICYKPllzHsTRzNShkePVkO3X2e8U8F-FCxN6XH0XMXtD86SmWK6NobwnhysMuhXrCbucGF6nThdDyBAEBE3fmHOPNqsjiT2HH4v_OU7ssZSCfyHO_VAPywi0mxhONWo242QI7_3yz2wkc5mRYUCKyOjCRXWFOmSefxQg7584Upy-l2kWp7izkOv6HaFG98EKnDHqN1ZqQoGo9Yxdsncuv6RNiR_hFLeX5QYWujrs_YehL_HcoloRjuamuS94Mlqf5GbFU95IODbNi_mV0XKPseH46owW75UnC9iUJ0cxyNOPEFb8YT67tQE-gtfZWcaJX00kIZkraLyZpmgsyx3i8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=WN3QGr9sjZb_sshyGdfPFTlrAWcmDtBv5UfuxURe76WEjFlr1Tn_e_zSnZnB5-5TNL_90HxTLTBB_Pg788upBTlV33DUTnHLCy14ijOJYjT8s0OeBEUAxwLO9sJonm7sG2Vz9huTs6EKib-wWa4hw4P3xWqAiFw1KsvPshX4-FQ0-P4V3er1qfpMCXDxiQjlaXhA-v7QkemeBfL4VAqDo0k8R_DGQnsNPpUrvyteIRulj6VOlQTsaJliUiv1yg6lukmmazmEmlIe4QA4Mo1SFgNWlyHkk2dfotV0MDWu1sFT3AGIbbvFCbk21VYAB4uVLbgzVWv7liUpOQyiWyICVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=WN3QGr9sjZb_sshyGdfPFTlrAWcmDtBv5UfuxURe76WEjFlr1Tn_e_zSnZnB5-5TNL_90HxTLTBB_Pg788upBTlV33DUTnHLCy14ijOJYjT8s0OeBEUAxwLO9sJonm7sG2Vz9huTs6EKib-wWa4hw4P3xWqAiFw1KsvPshX4-FQ0-P4V3er1qfpMCXDxiQjlaXhA-v7QkemeBfL4VAqDo0k8R_DGQnsNPpUrvyteIRulj6VOlQTsaJliUiv1yg6lukmmazmEmlIe4QA4Mo1SFgNWlyHkk2dfotV0MDWu1sFT3AGIbbvFCbk21VYAB4uVLbgzVWv7liUpOQyiWyICVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری آمریکا دقایقی بعد از انتشار
این پست
در برنامه صبحگاهی شبکه خبری فاکس حاضر شد و درباره این پست و تنش‌های جاری و فزاینده میان ایالات متحده و جمهوری اسلامی توضیح داد.
🔻
«ترجیح من تصرف خارک است»
او در این گفت‌وگو تاکید کرد که شامگاه پنج‌شنبه حملاتی شدیدتر از شامگاه چهارشنبه، ۲۰ خرداد در انتظار حکومت ایران خواهد بود.
او با اعلام اینکه در حملات چهارشنبه «۲۵۰ میلیون دلار» بمب بر ایران ریخته شد، افزود: «آنها [حکومت ایران] واقعا در حال تسلیم شدن‌اند، فقط هنوز خودشان این را نمی‌دانند.»
او هم‌زمان گفت واشینگتن همچنان با تهران در حال گفت‌وگو است.
ترامپ در پاسخ به پرسش مجری برنامه درباره تصرف بخش‌هایی از ایران گفت ترجیح او «تصرف جزیره خارک» است، اما تردید دارد که افکار عمومی آمریکا آمادگی پذیرش چنین اقدامی را داشته باشد.
او افزود: «با این کار ثروت هنگفتی به دست خواهیم آورد، اما فکر می‌کنم مردم آمریکا دوست دارند ببینند ما به خانه برمی‌گردیم.»
ترامپ در ادامه تصرف خارک و تاسیسات نفتی ایران را با تجربه ونزوئلا مقایسه کرد و گفت آمریکا «میلیون‌ها و میلیون‌ها بشکه نفت» از آن کشور خارج و به پالایشگاه‌هایی در هیوستون، لوئیزیانا و دیگر نقاط منتقل کرده است؛ پالایشگاه‌هایی که به گفته او «شبانه‌روزی کار می‌کنند و ثروت هنگفتی به دست می‌آورند».
ترامپ گفت از اجرای همین الگو در مورد ایران نیز استقبال می‌کند، اما مطمئن نیست «کشور آمادگی آن را داشته باشد».
🔻
«اکنون تمایل کمتری به توافق دارم»
ترامپ همچنین گفت اکنون نسبت به سه یا چهار هفته پیش، تمایل کمتری به دستیابی به توافق با جمهوری اسلامی دارد.
او افزود: «نمی‌دانم آمریکا آمادگی انجام کاری را که من واقعا ترجیح می‌دهم انجام دهم، داشته باشد.»
در بخش دیگری از گفت‌وگو، مجری فاکس‌نیوز از ترامپ پرسید آیا از جمهوری اسلامی عصبانی است؟ او پاسخ داد: «من عصبانی نیستم. من عصبانی نمی‌شوم.»
او درباره توافق هسته‌ای مورد نظر خود گفت: «توافق من راهی به سوی نداشتن سلاح هسته‌ای است.»
ترامپ افزود که ایران نباید اجازه داشته باشد سلاح هسته‌ای «توسعه دهد یا خریداری کند» و گفت در متن توافق پیشنهادی او، هر دو مورد گنجانده شده و حکومت ایران نیز با آن موافقت کرده است.
ترامپ همچنین مدعی شد «کار حکومت ایران تمام است» و افزود: «آنها دیگر نیروی دریایی، نیروی هوایی و پدافند هوایی ندارند.»
او همچنین اشاره کرد که هواپیماهای آمریکایی بر فراز مرکز تهران پرواز می‌کنند و مقام‌های جمهوری اسلامی «اصلا نمی‌دانند ما آنجا هستیم».
به‌گفته ترامپ، آمریکا همه رادارها و سامانه‌های پدافند هوایی جمهوری اسلامی، بخش زیادی از موشک‌ها و بیشتر پرتابگرهای موشکی حکومت را از کار انداخته و توان پهپادی آنها نیز «به‌شدت کاهش یافته است».
🔻
«نمی‌خواهم نیروگاه‌های برق آسیب ببینند»
در ادامه، وقتی مجری برنامه از احتمال هدف قرار دادن یک نیروگاه برق پرسید، ترامپ گفت: «بله احتمال دارد، اما ترجیح می‌دهم این کار را نکنم، چون وقتی چنین کاری می‌کنید، مردم رنج می‌برند.»
او همچنین درباره تاسیسات آب گفت قطع آب «ضربه‌ای ویرانگر» برای مردم ایران خواهد بود و افزود: «می‌توانم در یک دقیقه بگویم آن را از کار بیندازند، اما مشکل این است که مردم دیگر نمی‌توانند آب بنوشند.»
ترامپ در بخش پایانی این مصاحبه کوتاه گفت مردم ایران از اعتراض می‌ترسند، زیرا به گفته او «سلاح ندارند» و طرف مقابل مسلح است. او بار دیگر طی ماه‌های گذشته به کشتار گسترده مردم در اعتراض‌های دی‌ماه اشاره کرد و گفت نیروهای حکومت ایران به معترضان شلیک می‌کنند و وقتی مردم با مسلسل یا تک‌تیرانداز مواجه باشند، برگزاری تجمع دشوار است.
او اظهار کرد جمهوری اسلامی دست‌کم «۴۰ تا ۵۰ هزار نفر» را کشته است و افزود نمی‌توان مردم ایران را به دلیل ترس از اعتراض سرزنش کرد.
🔻
«از کردها ناامید شدم»
رییس‌جمهوری ایالات متحده در ادامه گفت آمریکا برای مردم ایران سلاح فرستاده بود، اما از کردها «بسیار ناامید» شده است.
او افزود با تحویل سلاح به کردها مخالف بوده و باور داشته است کردها این سلاح‌ها را تحویل نخواهند داد.
ترامپ گفت: «فکر می‌کنم آنها سلاح‌ها را برای خودشان نگه داشتند. این مایه ننگ است و من این را به یاد خواهم داشت.»
گروه‌های کرد مخالف جمهوری اسلامی، از جمله حزب دموکرات کردستان، حزب کومله کردستان ایران، حزب کومله زحمتکشان و حزب آزادی کردستان (پاک) در هفته‌های گذشته دریافت سلاح از آمریکا را تکذیب کرده‌اند
.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76214" target="_blank">📅 17:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNCSXQroOOD-FDoQ6ZvFgXQId7ll6u1v2ZZbxjFIQXPl7o9a1OFQ_IDPsBM4XNorfwqCcwTYnBI_-h3_HKBaYQmajXZuMb3_yrOXuMTtJOHiMWd-I0MSWis73kOGcWv-FF9NoNea2v3TT8uM7vFVpcQlzyHiY80QB6QtS8D63VNJHUyIIJleD6PYbsO9Ds0II_7OJ0yBaNTnooB9vF9zqhneB_DzqroF6NcoJf2QkH93NTuc_X2y1sdUvaU2Ur5Wte6wLeMtd91Udy1kyEgoz74cf5i36fTIQJMwzTg8iX8n0QRW-VkjGHlcnuSWmKhTd3PHOM6HBSuGtFu7eJyulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکات بسنت»، وزیر دارایی ایالات متحده، در شبکه ایکس نوشت که جمهوری اسلامی ایران در «بازی با حاصل جمع صفر» شکست خواهد خورد.
بسنت در این پست توضیح دادکه خساراتی که حملات موشکی و پهپادی جمهوری اسلامی به کشورهای عربی به‌عنوان «متحدان آمریکا در خلیج فارس» وارد می‌کند از محل دارایی‌های بلوکه شده در آمریکا برداشت خواهد شد.
وزیر دارایی آمریکا همچنین نوشت که هرگونه عوارضی که از کشتی‌ها برای عبور از تنگه هرمز دریافت شود، با برداشت از حساب‌های ایران جبران خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76213" target="_blank">📅 17:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4i21lvIuBzjFNTKxVphzJIIOGKc_gVXvX_on2ar_NC557C2yxBVAbVgV7hsbaALfWEF3uphdxMvu7clawRd4zIwbu1Efbf7tuN3HQDqaSPA8tgWBAZXUDopWOAY6QK8ZL1R5ejhmJC4lNlpxU5x51fDvtqCbm8R73iQoHy4-2HmU5D-DiSsF1aIyu2AXbN3SZ6pLMzkINzU7QKtuqumm5jwv500O403z31vIbbxgAP-cbEDXe4WEglIVTPifNpO0kItJcV1jcApqSV_6RbhsntaaOxkvYv2gqanS17KrZQcU1Sq2VbN67vKr3nRMkwnd-_IKpZNfuVGo5aF9XJqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز پنجشنبه اعلام کرد که ارتش این کشور امشب بار دیگر ایران را به سختی مورد حمله قرار خواهد داد و از برنامه ایالات متحده برای به دست آوردن کنترل جزیره خارگ ایران خبر داد.
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال نوشت: «ایالات متحده امشب ضربات بسیار سختی به ایران وارد خواهد کرد؛ کشوری که نیروی دریایی، نیروی هوایی، سامانه‌های راداری، پدافند ضدهوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش عمده توان تهاجمی‌اش، از بین رفته‌اند!»
آقای ترامپ در ادامه پیام خود نوشت: «در مقطعی در آینده‌ای نه‌چندان دور، ما جزیره خارگ و دیگر زیرساخت‌های نفتی را در اختیار خواهیم گرفت و کنترل کامل بازارهای نفت و گاز ایران را به دست خواهیم آورد؛ همان‌گونه که در مورد ونزوئلا انجام داده‌ایم، اقدامی که نتایج فوق‌العاده‌ای هم برای ونزوئلا و هم برای ایالات متحده آمریکا داشته است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76212" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHSNA8HeUMv2nuUs_07t6aL41PMZjbilFs978vzsXIxP0Ya2Xb4nJwLR1uRODA6odQTj44ZqAn0QNp8J7gDliQxupxCG-zFhBUdnG4czUFE5q0J-PQHJAxqu1sjdf2BsFbn2CQDZXSJv41DgJ10XF5TAE1HDb7ZXrvf_DdCARdvXeefuqTO6UZJNdaxGdbW1AHWoud_sqlQa-h7RNxcHjUbTjN1kRlPMmIZCBsG36GWmikr11QnvEHQ5tjbwcEggsUIMtE9t2kbAdEYctIAF0Mm11WV8d5jO_vLg1_QrKmfi_fQMQeQxPlpqTAYWNFLzU2Le1yg3Qlyyb22CXcZ5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل متحد، آنتونیو گوترش، در پیامی تازه درباره وضعیت خاورمیانه هشدار داد که این منطقه «هر روز بیشتر به سمت بحران عمیق‌تر کشیده می‌شود» و تأکید کرد پیامدهای آن فراتر از مرزهای منطقه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76211" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8-Mi2mOm5DRCrRluxKRb_8WubrU-yQGwDuT-TKxulXS_Xdfox_zLhVig0MT5Bx-QuYDmBIZkBaZOpQ2ZXs7rluwBcD602DdDgo8HZPkdA0nJPmvXNe7ewOV5zuBzxNa-M1_n00RwYsV4igBQZQQImTUE0opkaYF3cX1qiMAXw6XkVXn8Cu-5iXKS-hjFrKzyzRpQduD6lut-wvb9F8U5xKdWN4pYM_PIFWQo2ifnWvSMZWa0xNemyEBGczfRQUch392gTGSBg8fFu9b_VLS00WcDuaOgjdlDkk9qrsySSnmKD2OtxyPiBudGSQTqvwMCSFsB4BmKwc17tgMjT-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی با صدور بیانیه‌ای در واکنش به حملات ارتش آمریکا به اهدافی در ایران، این اقدام را نقض قوانین بین‌المللی خوانده و گفته است این حملات آتش‌بس ۱۹ فروردین را عملا بی‌معنی کرده است.
در بیانیه وزارت خارجه ایران بار دیگر به کشورهای حاشیه خلیج‌فارس درباره استفاده ارتش آمریکا از قلمرو، امکانات و منابع آنها هشدار داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76210" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d46260783d.mp4?token=s_xsgtEFOQmUs-HehENyskVk5tAX8GMvogHo1TOGj0s2ckpPztR2-vRDPJxFgXeNIagB8M0mk7mwGFjAuqAgGh6Fty_-18-DPgVtPqCZUkEZJ7S7zqOXfchQ34k_rdCYC3MEmk3a_NXZWBBiD_hK0TKtrWpC0FRaV4cXm2tMqeaxCMrmZyDOIzqvVtgr_5-zuHsXySIcKVaG7WRvdr68gjUMu_1VqRVlNc0gVA82efjjDpdANSynsHHy0KBAibF42KQUvLgBLpPoqKpuLACgvfWbPSfQYa14zyvKVCktlFlqgLO8h_2dTHJxT8Yg3DWdIFsw87rULeIf5apoMkp3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d46260783d.mp4?token=s_xsgtEFOQmUs-HehENyskVk5tAX8GMvogHo1TOGj0s2ckpPztR2-vRDPJxFgXeNIagB8M0mk7mwGFjAuqAgGh6Fty_-18-DPgVtPqCZUkEZJ7S7zqOXfchQ34k_rdCYC3MEmk3a_NXZWBBiD_hK0TKtrWpC0FRaV4cXm2tMqeaxCMrmZyDOIzqvVtgr_5-zuHsXySIcKVaG7WRvdr68gjUMu_1VqRVlNc0gVA82efjjDpdANSynsHHy0KBAibF42KQUvLgBLpPoqKpuLACgvfWbPSfQYa14zyvKVCktlFlqgLO8h_2dTHJxT8Yg3DWdIFsw87rULeIf5apoMkp3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا سومین نفتکش ناقض محاصره را در خلیج عمان از کار انداختند
تامپا، فلوریدا — نیروهای آمریکا ساعت ۱۱:۲۰ شب به وقت شرق آمریکا در ۱۰ ژوئن، پس از آنکه یک نفتکش با تلاش برای انتقال نفت ایران محاصره علیه ایران را نقض کرد، این شناور را در خلیج عمان از کار انداختند. این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی از کار انداخته می‌شود.
فرماندهی مرکزی آمریکا، سنتکام، علیه نفتکش
M/T Jalveer
با پرچم گینه بیسائو اقدام کرد؛ این کشتی در تلاش بود نفت را از ایران از مسیر خلیج عمان منتقل کند. یک هواپیمای آمریکایی پس از آنکه خدمه کشتی بارها از اجرای دستورهای نیروهای آمریکایی سر باز زدند، دو موشک هلفایر به اتاق موتور کشتی شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی به‌ترتیب در روزهای دوشنبه و سه‌شنبه دو کشتی با پرچم پالائو، یعنی
M/T Marivex
و
M/T Settebello
، را از کار انداختند. مارویکس با تلاش برای حرکت به‌سوی یک بندر ایرانی محاصره را نقض کرد و ستبِلو نیز تلاش داشت نفت ایران را منتقل کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام ۹ شناور نافرمان را از کار انداخته‌اند، ۱۳۵ کشتی را که از دستورها پیروی کردند تغییر مسیر داده‌اند و اجازه عبور به ۴۲ شناور حامل کمک‌های بشردوستانه داده‌اند.
این محاصره به‌طور بی‌طرفانه علیه شناورهای همه کشورها که وارد بنادر و مناطق ساحلی ایران می‌شوند یا از آن‌ها خارج می‌شوند، اجرا می‌شود؛ از جمله همه بنادر ایران در «خلیج [فارس]» و خلیج عمان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76209" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYimmdol4Z4lnNHRQnps0pfSzgNgd8iRG4fkN8uBQfne6_-f59fSSMC_i7APWcle9DKBxg4NNs6NnX9__eheaYIO2vy4XxS98k3M62PnN5TYuJAK3FzpnTy-mOCtyiJuRSc1Vrhk2frYzIPPOAzoRSH3XIcxO_9NRmnuHF_pG3xOkAbOQl8GpJeogulfybi9AVnp2a6VZ0aRwlSgmHIU3o1e3vP5XPW3DE_M_MiSrlS72BWV2SoGRd8OV1WQ_5VGquSZctvU4hLw7FnQVN-bIwz1A8aI4jqa6yG8uSOS5Gf7Uvdxc-OdGacAoLWpgLHd7M0T_yVUijzOvyagHZawyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرحیم سلیمانی اردستانی، عضو مجمع مدرسین و محققین حوزه علمیه قم، توسط دادگاه ویژه روحانیت به شش سال حبس، خلع لباس روحانیت و پرداخت جزای نقدی محکوم شد.
نزدیکان آقای سلیمانی اردستانی اعلام کردند که وی تنها به شرط برگزاری دادگاه علنی حاضر به اعتراض به این حکم است و در غیر اینصورت، حکم را بدون اعتراض می‌پذیرد.
او به اتهاماتی چون توهین به مقدسات، توهین به علی و مجتبی خامنه‌ای، توهین به مقدسات تشیع، توهین به مراجع دینی و هتک حیثیت روحانیت شیعه متهم شده است.
سلیمانی اردستانی در فروردین ماه توسط نیروهای امنیتی بازداشت و به زندان ساحلی قم منتقل شد.
او پیش از بازداشت و در تحلیل نخستین پیام مجتبی خامنه‌ای که به تجلیل از علی خامنه‌ای پرداخته بود، نوشت: «مهم‌ترین هنر والد شما این بود که مخالفان و منتقدان خود را بی‌بصیرت یا مزدور بیگانگان می‌خواند و هر برخوردی را با آنان روا می‌دانست! از صفات اخلاقی ایشان دو صفت لجبازی و کینه‌توزی را بسیار برجسته یافتم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76208" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNSK8b-zLxxdreJjoxNhQaG-maLzbdlYzEDf8UhYtjLJkB_qFE7cD1LcVV5rctDheXXm9Fjq12XX06z_hX7YRXE_35h8qkRrdHDbXbY8hk3qOOA_GCTrSXjiNVQTxHAvcDwRkPv90blpifyC7bimDvb4beJ0BxJDoet0KT4suX_6eNXTJ3amJH5d6k_tf26v_kbjUyJmd8Ae9DT8xWLd7ZPFWwTklaMA8TG4OtgHexrJrQbaHQgTNqqrI75s-YdlktPTcesgKJFT5CNfxi4XwZDVCsifFJZy8Z0YWjh2oFR8KW_5sDONI-383LkHKBeU4GckbrtZeFqWaWq8kwMzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی از پیشوا در جنوب شرق استان تهران
'دود انفجار حمله حدود ساعت ۴ صبح که در ورامین و پاکدشت هم احساس شد.'
پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/76207" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/769901b74f.mp4?token=NumsCc5gtvon5GOCzKqwjwGfyZX3gXdYgp9Rgw9TbA52MiRwPWlMWZthAR_yvoCfp2XFZxfboH_4JIV5wKcjuA1W3uX-d_RLIMMpavBIBtft0uSwEL0-NmMC7x-kn8pDTWtmQluNCqIZbnmULB-KLDakK0b05MKZCf-eWkaXUVe-ZjabA2tNI4yAwWyZ8HfsvVMI3n-_aNKn9eOmt5ejHJ5XHQ5F9fnKaex0ggDFgYngAHzZhX7GgQlEf3wSHXqSGJUVzaXc7m7dEcpYDj6GD5kpWlcEBmyzA1ie6kB9qPTP1ptrU-B7ZOOvQPSgyawGjctivqhNlHRNIqeEOnQIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/769901b74f.mp4?token=NumsCc5gtvon5GOCzKqwjwGfyZX3gXdYgp9Rgw9TbA52MiRwPWlMWZthAR_yvoCfp2XFZxfboH_4JIV5wKcjuA1W3uX-d_RLIMMpavBIBtft0uSwEL0-NmMC7x-kn8pDTWtmQluNCqIZbnmULB-KLDakK0b05MKZCf-eWkaXUVe-ZjabA2tNI4yAwWyZ8HfsvVMI3n-_aNKn9eOmt5ejHJ5XHQ5F9fnKaex0ggDFgYngAHzZhX7GgQlEf3wSHXqSGJUVzaXc7m7dEcpYDj6GD5kpWlcEBmyzA1ie6kB9qPTP1ptrU-B7ZOOvQPSgyawGjctivqhNlHRNIqeEOnQIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'نور یکی از انفجارهای حملات بامداد پنج‌شنبه به استان البرز'
ویدیوی دریافتی: 'فردیس کرج، ساعت حدود ۴' پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/76206" target="_blank">📅 06:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i6RtpCTdBlHU-kFJ1ETC9MGYurentulrK4luGzaiKp0GFOuhoUWkiHkr7LRTXnQNAc4fotl-Pbmq9wrPOyQ-2QUsQmOGOPF5KrAorUQKkGZZtpp63iX9MTQ51PX57epstHq0NPSwsvFuXbgrTCdsO0ksPqBnTxtHEGG05wtV9K2-9ZyvA01ZP-F3DdqX3fG2bgzTKxd2b-_M2neAN5uQ9cRDhlH8B7dXnneFUYM4o-tNJ_bMoUhqD7TMuHL_hq-DeseIHrXNSRPgTX2LK9RzxHem_FDUt-5VasFm0WDl_xVRRONCdXfqAzuryzh5x_w9KrwICLviq0e4OZkJZlFK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZOq3qMThcGzhWOiQBds1n9Jf2QhScH6ffEaf6IAd35iwmvEv5YuI4raXDCmw4oPPoHJL3AASxw82nVVcjcWXeZ5AE56cWHsr-ivKgKwJ252Bd8S_FmbYKATl-KWe_bjQFKRtOc5UTthvv0UuYI9AGSsSkuzr7SzWhVHxXe_XJtFQ_RMuNwnbp8DMuKmJWpF83vpJQa9AYSB4XpEOkNLViU43hap9TlRq3JBwsI-tJA68HLffKL-azSuHADC1L3d1c6u6_wY1y23kCnlU-IztXn1sHD9keJD6D-QIHaZTYXciVYCCbpcif6SGhHklrFBQh_dxJe23qHf5vK8WYI9a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JpT0Vyn9_9sG6MYvPFI7LI78AlvzNSiWHNS4sJRn33NJCKG8R4K0-4WFGWhYdiMxKEUjTZyQbkNcoFIRtLl9ejOKdmmR1TTt3AAxH1nhl1fZynETOWl4WTn1JKSZhHIiwOQanJoJ7p0rd2IFHu7YDKdE63QAqKQu3fwFtN1GpmDwWnaiw4F3aXGWcDEQUUbPFjM08zxPLhNnWo5GzGJxYeZcb9faHcpXLAdW9fUM4EHt-KpbKSp6fqG7DZ6rNNnPvZMJAhl_TcE198s6K0J_71L4w9WcQXuLItVARo4w8ATAB7Zlm3YyYWGi5U19KLIXESawHEuPYeaUfL_zV0bCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgSQU6HWxcxQ6U5RMuMMqe0YOcHDIwEcMYkrI1zBUFmyCZHUbcMqyTjPW9iNPD7aL0GhOw8JXkzdooIjcIMbAIy4KxsVovGIYVvKNAkI9QewZczomNtYBQon_Cshl9mGhVLW2yY2hdnJFEdpzoGcB5Lhdh1NtldF21wosUDe68grBopKnjU48dqb23L8ossoAQ8GXUftpmSGETueMmACCTTtlvN1UlFzLh8hFKVbxbszuVZFC6GfVqQ5mRRgIqHabeDiiQliOpfgIlr0XYE_bGIMrBnYPjueDYx6visnjNr6GNhO44DXMV7uB0qbkoxJv7FF7HY2_6EuDyvpkoT_YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e891de921.mp4?token=tkJ3tNbFzWEi_TUi9EHkFlPjjDchRhGh5w9NFC1Qtv8AlCPvAw7BzesWnzf4QLykTJWM571WeaYyrw1T05MPu0pYZsT6xQw_mKz7kYpUNGzitCddU5qc1I4rlz6MKiHmmZq1b1k8QPThMApALRAa5sscWBRBaaCIlDgT87aR4plX81LAxmOYyyLLZhyleRS-gRrUmD1k6kkEKkIjq6nLsERnp7anABQDaI8xj1TgPTgpH2_tJ4cZButkbC7bGLs39Y6bVRiBGuB8bjYaaSpNPejNQT76caJPnMHx3xxlmnGV-VefM1oMMeugYpQIYx5I2zQSTYW0_HKr-22NG0c85w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e891de921.mp4?token=tkJ3tNbFzWEi_TUi9EHkFlPjjDchRhGh5w9NFC1Qtv8AlCPvAw7BzesWnzf4QLykTJWM571WeaYyrw1T05MPu0pYZsT6xQw_mKz7kYpUNGzitCddU5qc1I4rlz6MKiHmmZq1b1k8QPThMApALRAa5sscWBRBaaCIlDgT87aR4plX81LAxmOYyyLLZhyleRS-gRrUmD1k6kkEKkIjq6nLsERnp7anABQDaI8xj1TgPTgpH2_tJ4cZButkbC7bGLs39Y6bVRiBGuB8bjYaaSpNPejNQT76caJPnMHx3xxlmnGV-VefM1oMMeugYpQIYx5I2zQSTYW0_HKr-22NG0c85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دود انفجارهای حملات آمریکا به غرب استان البرز و
#کرج
تصاویر دریافتی از  حوالی "حصارک"، "کمال‌شهر"، "مسیر کرج به قزوین" و...
بامداد پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/76198" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiHp_vtuHJlptUuh3VzOAHxTI6cnTqGyDt8r0wmDXmcZZiWnJhQQQE3iPD2pZDFTev_NIvURQ6W74L7coj8SX5VIhRD-Wr8Hp4OUTp3AjuRyYAI3e0AdayUC7MfyoKtT7G3A7rwOW9eMSQtE3F4dCE9ExIlg-FhZaitESdCsVU-rcSC0SJOQsQCkAvxRL_m8Yv9FxGuFAx7BnD-mpHwaUnhl-q7Eya3w5AYBGSpy8DStuvYxo-j9T7HYZLOwQSOjoBaq-swCkvlRjLjaKYKOLkYHVw3X63XGLmofWNw0SOW38AGz8mRsLIc421pufSZmQ1xug0SNfBTmFRlJnjyJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح : شلیک موشک از استان اصفهان ۶:۰۳ پنج‌شنبه ۲۱ خرداد
آژیر هشدار حمله هوایی در بحرین صبح پنج شنبه برای بار دوم به صدا در آمد. ویدیوهای منتشر شده در شبکه‌های اجتماعی شلیک موشک از چند استان در ایران را نشان می‌دهد.
@
VahidHeadline
ارتش کویت بامداد پنجشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور در حال رهگیری اهداف «متخاصم» هستند.
پیش‌تر روابط عمومی سپاه از حمله به اهداف مرتبط با آمریکا در کویت خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/76197" target="_blank">📅 06:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863187a248.mp4?token=cCLgJ2rtsEae42ReED84CbdcZIEmENwzP2VqggXMRA6T1i_bO3hckH-Geej3gGQGiR4j53zfVmzBCpqciziQ9jP6DVIpLnLYdxr5ovTaZ9ncTn8MhYEQe0OGEZeI4iUbFV1YcnFUneUewltpZ0SjP9DO_HsCkZWlJufnsrE1WLJUmHlUUYLxKVqJpABsqm--Gqs-qOwNxXKelFl1p_XNQlCLp9sl2oRL9nMtbxRzMNOpGY6S2l_IhRi_alMMUXSUuqcf-7NsPEFEKFWiChOEe2m01-8RApfZTL4ibnvUlKx04WKfP7OQdFLqP3seqQnfW9upIbS0ZC19rXbUVVCHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863187a248.mp4?token=cCLgJ2rtsEae42ReED84CbdcZIEmENwzP2VqggXMRA6T1i_bO3hckH-Geej3gGQGiR4j53zfVmzBCpqciziQ9jP6DVIpLnLYdxr5ovTaZ9ncTn8MhYEQe0OGEZeI4iUbFV1YcnFUneUewltpZ0SjP9DO_HsCkZWlJufnsrE1WLJUmHlUUYLxKVqJpABsqm--Gqs-qOwNxXKelFl1p_XNQlCLp9sl2oRL9nMtbxRzMNOpGY6S2l_IhRi_alMMUXSUuqcf-7NsPEFEKFWiChOEe2m01-8RApfZTL4ibnvUlKx04WKfP7OQdFLqP3seqQnfW9upIbS0ZC19rXbUVVCHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'موشک‌های شلیک شده از استان
#زنجان
'
ویدیوی دریافتی، پنجشنبه ۲۱ خراد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76196" target="_blank">📅 05:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=Fe288QPcJvv2WQaggmnurfdYk96ufE4pX-uNotP3EH2B8PLT4_wP2gGTMxFlUwcM9hG0Tikn_zSQpxmJ_w1vwpdNoPaRRk8Zx5HF9GIKCavpJh5L7goEZBHul5dpn6cxLn4ZzVNLwft4iOXiCHUYUG5yDQ3V4Trrv91gIDeWQ9FaegI_R5EaSTYXve0Om6ZPsCsfeA_MDsPI-ugHACTeS-YKAxMq9AUoErR_BUApRY0YoGHpi9gbEUfBrbbmV9SPt7VfXI1HLnlfo_GXrcowD15LYHrtQf7WhOMW0iTKGAPMZapCsLYr_vuUrDfxzSI8tqPbUC5_8WQ_E8AdCzJnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=Fe288QPcJvv2WQaggmnurfdYk96ufE4pX-uNotP3EH2B8PLT4_wP2gGTMxFlUwcM9hG0Tikn_zSQpxmJ_w1vwpdNoPaRRk8Zx5HF9GIKCavpJh5L7goEZBHul5dpn6cxLn4ZzVNLwft4iOXiCHUYUG5yDQ3V4Trrv91gIDeWQ9FaegI_R5EaSTYXve0Om6ZPsCsfeA_MDsPI-ugHACTeS-YKAxMq9AUoErR_BUApRY0YoGHpi9gbEUfBrbbmV9SPt7VfXI1HLnlfo_GXrcowD15LYHrtQf7WhOMW0iTKGAPMZapCsLYr_vuUrDfxzSI8tqPbUC5_8WQ_E8AdCzJnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان تبریز
ویدیوی دریافتی: عبور یک موشک از میان رد موشک‌های قبلی
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76195" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/056cecd324.mp4?token=O5fiFJUENC6hOlNAT_8-IaCc70RfeL1GUXneE_t63lj0nRu4fwrpnfK5sAbxWbCb4254Kn1RSPZtMatNM_E4euMF7Vxnd5r0u5j-P1TglI2e4bcjtcm2Gbj88rwwWTaBd6VjWKp2-Z3VY5mhKgvvrEqTMcLvZT4r0AQSybO2HfsQCdIVndfh9aBAYghYbzRAbcIN1u5IRfQUmEvielyBmI6_cTe0XwMi0oQjisXzD_pYETHJSfuC7kZK2zGe28UKyMVXZrdDcQYlvzbdKISBkHPWHgxQn9pA58NgJjGtQ1RiQrSapPrGd9TLvWYccRMZHuG1Elqw6srFDuTkkg36KA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/056cecd324.mp4?token=O5fiFJUENC6hOlNAT_8-IaCc70RfeL1GUXneE_t63lj0nRu4fwrpnfK5sAbxWbCb4254Kn1RSPZtMatNM_E4euMF7Vxnd5r0u5j-P1TglI2e4bcjtcm2Gbj88rwwWTaBd6VjWKp2-Z3VY5mhKgvvrEqTMcLvZT4r0AQSybO2HfsQCdIVndfh9aBAYghYbzRAbcIN1u5IRfQUmEvielyBmI6_cTe0XwMi0oQjisXzD_pYETHJSfuC7kZK2zGe28UKyMVXZrdDcQYlvzbdKISBkHPWHgxQn9pA58NgJjGtQ1RiQrSapPrGd9TLvWYccRMZHuG1Elqw6srFDuTkkg36KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: رد موشک شلیک‌شده در آسمان ارومیه
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76194" target="_blank">📅 05:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=uArBMqygw0UtpbmiFyQh9NN9oGT_hrM1lMLYjgugNaGYjI72mn0nm99EsTdGfAMaQ6UAJ60-h_VEGOp49QufS4BLZQ8VnCkoNMCTJU-qxSMfBVFovmXADWkAecBNRxpDG3p42Ms-Q53uTSR5k5COhpbDLl7ux8IqYQinh7ALf9Vm5JE18Y6BGZDRectR9t2sxJCN9H9zR0n3gVMvmPYBGOJz1aKNaC9iwGw7Wc1CghHsyW0h8w_jFrl4NU_zKLZsmb5xWkEwNJhqyTqWV9K4khkth3mPxSuc4bsKDxem-Dsy_VoLbl5d9SZMjfYxOooWfs7h35MleMw-zUb_SR5nMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=uArBMqygw0UtpbmiFyQh9NN9oGT_hrM1lMLYjgugNaGYjI72mn0nm99EsTdGfAMaQ6UAJ60-h_VEGOp49QufS4BLZQ8VnCkoNMCTJU-qxSMfBVFovmXADWkAecBNRxpDG3p42Ms-Q53uTSR5k5COhpbDLl7ux8IqYQinh7ALf9Vm5JE18Y6BGZDRectR9t2sxJCN9H9zR0n3gVMvmPYBGOJz1aKNaC9iwGw7Wc1CghHsyW0h8w_jFrl4NU_zKLZsmb5xWkEwNJhqyTqWV9K4khkth3mPxSuc4bsKDxem-Dsy_VoLbl5d9SZMjfYxOooWfs7h35MleMw-zUb_SR5nMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک از استان زنجان
ویدیوی دریافتی پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76193" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TnghvrkuMK00dzd7wkBNeJT3QaioIagxl00B1OPH9rdq-z8PLc6I0NgCifKpF28-T64X3ZOuACahQ4QUdX7jfolNiNlDK4pl8oayV3oKcS3aWdDJ9XtrJVsCpis9XHjlf5dlgOXQT_KP852WhgQ55M7vr-X423NCs3gKTs6wt35gQamSUQ-F86BTofBUxT-CKwI4m1sUXzwhnVcMpsBM5P_tZPpecp9Ih_XEsnVHZmDAQQoHbNPR4lLuZs9VZWcpNrchQUsQPdTXP8rgQOUoSHUYVXxmPoQpaN1dxMmYoqpSz74e6SJkcxTOJmHz9iTPZ8w6ejyXfzGvKTRmDEK4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q1QkH5NsGNC8XmznRs-pEtdQNIm9PicaEKrC2fVOg6mQrt6ah7Mk3IGtYW7L8SlV4LYBU7o5LCMGn-3GLDjeJkRBHoeuhVsAcnfkqcsM-XpuEtz4Mpjstl3wBzLa3Pso-M_3pGmuWvAEHNC8tFdEc--4FD-2F7O_HAfUfGaOxYWsOBieJHIXiYcBiCE5jDIDLMnrg0tfjZxDU1ckRPaQYzHSPqt-pFaXxmBfiVghZ0eNHtqsVRUYVzm8nY3vbmo8vC5Yr3e1NBHcciB48HH7VQ5J7SuvHSlaTDkTbASeJYYZQ3hjU8Kk8TEij871tHWaUB6i8lWrxnAVVi6d33uRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VdDjFRYnAEBp5JO_hYPt2tsOx9PoF9qENmcNusMi7VFYk7kFoLOysyRYzUbguCGHakUkxVrGZsfxsYIbL08KuT_FjcRrRDMUctcKrYq2DswVNHNfzgdfT5e9fWTjIF5TK7V0cVrf8bjSE_wNEql0yceu1WaDngbOa9MIEq7Akfs2CBUodowYgpC8Tm_xr-1PxsWscGi0F-8t42k4DaiQ-MURNB7A9wv0vr0g6K3BKk42yNjim4Z_WugA5A3oM6_8vUJvdBKlgHkuyLmZcfnmDFazmqlvx_FphncEL-tgQlydEGNrQvT51iW4Qh1IwJO1L1cRkNJU0g1GuWT7Nr7dcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک موشک از زنجان، تبریز و ارومیه
الان از شبستر تبریز سه تا موشک زدن نمیدونم به کجا
صداش خیلی زیاد بود
الان یدونه دیگه زد
سلام 5:16
همین الان تبریز صدای انفجار قوی اومد
از ارومیه موشک بلند کردن
5.18 ارومیه  صدای 4 - 5 انفجار
سلام وحید جان تو ارومیه ساعت ۵.۱۷ چهار بار صدای انفجار شدید اومد
هنوزم ادامه داره
3 تا دیگه زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76190" target="_blank">📅 05:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVl0K2Kiw_9DOpLumHDgaL5hBhhbjRwDeLLHTp2pOeuuu89mx0RRoeXrCKEJL2WPI-xKCMkHX5tWdnpnyWz4p0r4s-2Qpm65zwHKOzCNBtwVpfHSfrIB3cJPcR8lq0CRn8jyOURfqozZ-jRDKwNO95XqXclTKOZEKsl5xXkm5Ox56wrK1CEknKzATvcwvBb80H5xo4ioIOxNacgu0K37BVzcg7YJbTg2kpnJShWckPM7APmly-ljPTEmHSqqMkdYNB9xzpyXrwJeYsn-PbQb9uEvXw-vjA3P6vJuk1lBeQgWBUToILOuywpQ3vMgcvuIqb995hZioq6K_3zIKL9R_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
ساعتی بعد از حملات بامداد پنجشنبه آمریکا، خبرگزاری‌های رسمی به نقل از ارتش جمهوری اسلامی ایران نوشتند: «ناوگان پنجم آمریکا در بحرین، آماج حملات پهپادی ارتش، قرار گرفت. در این موج از حملات پهپادی ارتش، آنتن‌های ارتباطی و تاسیسات راداری سامانه پاتریوت ناوگان پنجم مورد هدف قرار گرفت.»یییی
همزمان وزارت کشور بحرین در پیامی در شبکه اجتماعی ایکس از ساکنان خواست تا با حفظ آرامش به نزدیک‌ترین مکان امن بروند.
سپاه پاسداران از حمله به« ۱۸ موضع نیروهای آمریکا» در منطقه خبر داده است.
کانال تلگرامی سپاه نیوز نوشت که طی «دو موج عملیاتی ۱۸ هدف مهم» متعلق به ارتش امریکا در پایگاه‌های هوایی «علی السالم» و «احمدالجابر» و همچنین پایگاه‌های هوایی «شیخ عیسی» را هدف قرار داده و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76189" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T5lILP6J3Y7jnlOUPQb57KnGT9Yha8F1Av7edohgGKcSNuzxeAtpx5jqigTqetdqqRSEhX-QQVzfjJobHdGQ6tjPyhTPHQpOM3emV5siZQqCWYnCtrnUMNCdGomsZQGs-2P-QhgluZNXleXRi9dTfTrmwKNQrquxRSQKGeavqi8WK4e65VqMLDZnHd2PcMJi8hPncfcU5oWaIGdSetn3habMBawh4a9IE-Y9J3I6uFRus9z0Me4LKfBxKOEh2DGqnZSD19PSmRAPHS8J69Nv6-IV05ZRuQdpPO9GUWFSZ2slLO0UskkIEf--yD4NsGDMVNK3r4XXCjzLoUDVY5WXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ گزارش داد که اسرائیل در حمله نخستین ساعات بامداد پنجشنبه به اهدافی در جنوب ایران مشارکت نداشت اما به‌طور حتم ارتش اسرائیل در سطح آمادگی بالا قرار دارد. او در عین حال گفت که آمریکا بیش از ۵۰ هزار نیرو در منطقه دارد که بسیاری از آنها در عملیات مشارکت داشتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76188" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=vuRIzuOJui5iJnsNgSb-UuWpS471tQdEKk1huZDkeXuJvf14t4R_UOBsWnVp1HM5UK_DSN1IsMVzc8HJO_9f13HrwNsD8ZpFvUwQfxB8N-IcOBv8Mv61kYXlMXXMiI4DpEorkLmmSIp5VBE8GIDIhd22_5bkReNnbZ5vNAyHxkVlSpsoE_LjQSvOSjaVbLqNTL5S-xcWIG7BCmXVKM_Bg1NN9ymGdvxuRmYjA767DHqwPdPPzKaq8Rd21gj33jsBrD80Zu-idXXr9zCsFdoXOlbAPbzI-5JK-tmTD4KRIsByFkvmUwQMp6qThXnX_qtpUKY1ciSLf5NuwBoscEMapg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=vuRIzuOJui5iJnsNgSb-UuWpS471tQdEKk1huZDkeXuJvf14t4R_UOBsWnVp1HM5UK_DSN1IsMVzc8HJO_9f13HrwNsD8ZpFvUwQfxB8N-IcOBv8Mv61kYXlMXXMiI4DpEorkLmmSIp5VBE8GIDIhd22_5bkReNnbZ5vNAyHxkVlSpsoE_LjQSvOSjaVbLqNTL5S-xcWIG7BCmXVKM_Bg1NN9ymGdvxuRmYjA767DHqwPdPPzKaq8Rd21gj33jsBrD80Zu-idXXr9zCsFdoXOlbAPbzI-5JK-tmTD4KRIsByFkvmUwQMp6qThXnX_qtpUKY1ciSLf5NuwBoscEMapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکا تازه‌ترین حملات در ایران را تکمیل کردند
ترجمه ماشین:
"تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا، سنتکام، روز ۱۰ ژوئن، به دستور فرمانده کل قوا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران تکمیل کردند.
نیروهای سنتکام حملاتی را علیه توانایی‌های نظارت نظامی ایران، سامانه‌های ارتباطی و سایت‌های پدافند هوایی در سراسر ایران انجام دادند. تجهیزات و نیروهای سپاه تفنگداران دریایی، نیروی هوایی و نیروی دریایی آمریکا مهمات هدایت‌شونده دقیق را به سوی اهداف ایرانی شلیک کردند؛ اهدافی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند.
این حملات در پاسخ به تجاوز بی‌دلیل و ادامه‌دار ایران انجام شده است. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده هستند."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76187" target="_blank">📅 04:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های دریافتی:
درود صدای انفجار در شهر کنگان ۴:۱۷
شهر کنگان صدای انفجار
کنگانو زدن ۴:۱۸
سلام شهر کنگان در جنوب کشور صدای انفجار
کنگان رو زدن
سلام.
کنگانوووو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76186" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک صدای دیگه از کرج همین الان ساعت ۴:۱۰
سلام وحید
یکی دیگه الان
همین الان دوباره کرج
ساعت ۴:۱۰، انفجار دوباره
۴ده دیقه کرج کمالشهر
وحید صدا های جدید ساعت ۴ و ۱۰
ساعت ۴:۱۰ یه تک انفجار دیگه گلشهر کرج
صدای انفجار خیلی بلند و طولانی بود
ساعت ٤:١٠ دقيقه باز صداي انفجار هشتگرد شنيده شد
مهرشهر کرج ساعت ۴:۱۰ صدای انفجار
همین الان ۴:۱۰ گلشهر مهرشهر
دوباره صدای انفجار خیلی شدید به همرذه لرزش زمین
سلام وحید جان کرج دوباره صدای انفجار همین الان ۴:۱۱ دقیقه
و کلی پیام مشابه دیگر که نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76185" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام از پیشوا صدای دوتا انفجار شدید
ساعت 4:۰۶ ورامین
۲ تا صدای انفجار
سلام آقا وحید، ساعت ۴:۰۶ صبح پیشوا ورامین صدای دو تا انفجار اومد و مثل اینکه سپاه پیشوا رو زدن
الان ساعت ۴:۰۵ دقیقه نزدیک پاکدشت دوتا صدای انفجار اومد
ساعت 4.5سپاه پیشوا
وحید جان ورامین همین الان صدای دو تا انفجار اومد
سلام وحید جان ورامین دوتا انفجار پشت هم ساعت ۰۴:۰۶ دقیقه
ورامین 2 تا انفجار خونه لرزید همین الان ساعت 4.8
همین الان دوتا صدای انفجار شدید داشتیم ولی مشخص نیست کجا رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76184" target="_blank">📅 04:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام وحید
بندرعباس رو الان زد
صدای انفجار شدید
صدای انفجار بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
سلام مجدد ٠٤:٠٥ دقيقه بندر دو صداي انفجار اومد
٠٤:٠٧ دو صداي ديگه مجددد بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام خوب هستین من بندرعباس زندگی میکنم ساعت 4:6 دقیقه صبح دوتا انفجار مهیب پشت سر همدیگه صداهاش به گوشمون میرسه
داداش وحید بندرعباس همین الان زدن
دوتا انفجار به فاصله یک دقیقه سمت دریا
۴:۰۶ یه انفجار دیگه قشم احساس شد
همین الان بندرعباس چند تا انفجار پشت سر هم شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76183" target="_blank">📅 04:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای انفجار در کرج
آپدیت: میگن شد ۶ تا انفجار
کرج صدای انفجار 3:53
ساعت ۳:۵۳ کرج انفجار
الان باز صدای موشک اومد
۳:۵۳ وحشتناک بود خیلی بد بود و هنوز صدا میاد
درود کرج ساعت ۳:۵۳ صدای انفجار شدید
کرج شاهین ویلا همین الان یه صدای مهیب انفجار اومد
سلام، همین الان ۳:۵۲ انفجار شدید، کرج، ما باغستانیم خیلی واضح بود
سلام وحید ساعت سه و ۵۳ یه انفجار خیلی شدید ( گلشهر کرج )
۱ موشک دیگه ترکید
وحشتناک لرزیدیم
بازم داره میزنه
وحید سمت ساوجبلاغ ۲تا صدا خفن دوباره اومد
خیلی شدید بود نمیدونم کجاست ولی  نظرآباد میلرزه دوتا انفجار شدید فکر کنم آبیک بوده
بازم داره میزنه سمت هشتگردو ساعت۳:۵۵
علاوه بر اون اون پنج تا انفجار قبلی الان صدای دو تا انفجار دیگه اومد ساعت 3:53 آیبلاق
انفجار در کرج سمت فرودگاه پیام
وحید جان من مهرشهر کرجم الان یه صدای انفجار مهیب اومد
سلام نظرابادم
دوتا صدا انفجار وحشتناک اومد از سمت کرج
بازم زدن همین الان۳:۵۵
کرج ۳.۵۴ انفجار شدید
کرج جهانشهر صدای انفجار ۰۳:۵۵
تک انفجار شدید اطراف شهر کرج همین الان ساعت ۳:۵۴ شنیده شد
فردیس کرج هم صدای خیلی بلند اومد و شیشه ها تکون خورد
همین الان فردیس کرج صدای دو انفجار شنیده شد
۳.۵۳ هشتگرد بازم ۴ انفجار دیگه اینبار نزدیک تر بود درای خونه لرزید
سومین انفجار ۳:۵۶
سومین انفجار تو کرج
سه انفجار وحشتناک توی کرج همین الان!
گوهردشت ۳ تا انفجار خیلی بلند شنیدیم
شلیک موشک اینا نبود
انفجار بود
ما مهرشهر هستیم صدا خیلی بلند بود در حدی که خونه لرزید
چهار انفجار به فاصله یک دقیقه از هم فوق‌العاده مهیب ساعت ۳:۵۵ اطراف جنوب کرج. همه پریدن از خواب. لرزش عجیب و غریب. امتداد صدای انفجار شاید ۱۰ ثانیه طول کشید. مثل پژواک صدای رعد. تا به حال چنین تجربه‌ای نداشتیم
وحید نظراباد صدا از دور پشت هم میاد ولی شدید خونه میلرزه
سلام آقا وحید سمت باغستان کرج سه تا صدای انفجار آمده و ساختمون لرزیده
۳ تا صدای انفجار خیلی نزدیک اومد
کرج باغستان
شیشه های ما لرزید
ساعت ۳:۵۶اطراف هشتگرد نظراباد بدجوری دارن میکوبن
سلام از فردیس پیام میدم اینجا الان یه صدای وحشتناک اومد
دوباره هم یه صدا اومد ولی اینبار دورتر بود ۳:۵۷
سلام آقا وحید. من شهرک بنفشه زندگی میکنم و ۵ دقیقه پیش صدای چندتا انفجار شدید اومد
صدای سه تا انفجار با فاصله یکی دو دقیقه در کرج، ساعت ۳:۵۲ بامداد
وحید جان چند صدای مهیب در مهرشهر کرج الان.
۴ صبح . مهرشهر کرج . صدای انفجار میاد
سلام وحید جان ساعت ۳:۵۴ و ۳:۵۶ صدای انفجار و لرزش محدوده ساوجبلاغ البرز، مشخص بود از طرف کرج عه
یه جوری فرودگاه پیام رو زدن سه متر از خواب پریدم هوا
وحید شهرک بعثت کرجم ۴ تا صدای انفجار خیلی زیاد اومد
ولی صدای جنگنده نیومد اصلا
خیلی موجش شدید بود
3/59دقیقه فرودگاه پیام و زدن
همین الان صدای انفجار شدید اومد
بعدش ده‌ها پیام مشابه دیگر اومد که دیگه نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76182" target="_blank">📅 03:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام دریافتی از شهروندی با سابقه اخبار درست:
"دو انفجار. نیروی دریایی سپاه سیریک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76181" target="_blank">📅 03:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پست خبرگزاری سپاهی تسنیم:
۱۸ هدف مهم متعلق به ارتش شرور امریکا طی دو موج عملیاتی مورد هدف قرار گرفتند
روابط عمومی سپاه:
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
رزمندگان شجاع نیروی هوافضا و قهرمانان نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه های ساحلی سپاه و فرماندهی انتظامی و محوط فرودگاه بندرعباس طی دو موج عملیاتی
هجده هدف مهم متعلق به ارتش شرور امریکا در پایگاه های هوایی علی السالم و احمدالجابر و همچنین پایگاه های هوایی شیخ عیسی
را مورد اصابت قرار داده و منهدم کردند
وَمَا النَّصرُ إِلّا مِن عِندِ اللَّهِ العَزيزِ الحَكيمِ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76180" target="_blank">📅 03:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی از حوالی غرب استان البرز و شرق استان قزوین
من سمت ساوجبلاغ کرجم
ده دقیقه صدای موشک اومد
الان صدای پنج انفجار اومد ۳:۳۲
سلام همین الان ساعت ۳:۳۳صبح اطراف هشتگرد صدای اتفجار و موج میاد
سلام ۶ بار سمت نظرآباد البرز رو زدن
ساعت ۳.۳۴
۲۱ خرداد
ساعت۳:۳۰
شهر جدید هشتگرد
۶/۷ تا انفجار پشت هم
اما خیلی دوره
نمیدونم کرجه یا تهران
ابیک قزوین ساعت ۳:۳۴
بامداد ۲۱ خرداد
صدای و موج انفجار اومد، به نظر میاد از سمت کرج یا هشتگرد باشه
۵-۶ تا بود حداقل
۳:۳۰ صدای ۵ تا انفجاد اومد از اطراف هشتگرد بود فکر کنم قشنگ شنیدم
سلام وحید نظراباد از دور صدا ۷.۸ تا موشک پشت هم اومد در های خونه لرزید
هشتگرد ۵ صدای انفجار از طرف اشتهارد
سلام وحید جان ساعت ۳.۳۳ صدای ۱۰ تا انفجار شدید اومد من نظرآبادم ولی صدا از دور بود
پشت هم موشک داره میاد با نور انفجار و صدای مهیب
محدوده نظر اباد هشتگرد
از پشت بوم کاملا مشخصه
سلاممم کرج هشتگرد 4تا صدای انفجار شدید اومد
دوتاش خیلی بزرگ بود بطوری ک کل خانواده از خواب پریدن
قشنگ کل خونه لرزید
۵ ۶ تا صدای انفجار هشتگرد جدید ساعت ۳:۲۰
سلام وحید جان
۶ بار صدای انفجار مهیب اطراف اشتهارد شنیدیم‌ از حدود ساعت ۳:۲۰ تا ۳:۳۵
نزدیک چهار یا پنج تا انفجار اومد از سمت آبیک اطراف ساعت ۳:۴۵ خیلی مهیب بودن
سلام وحید جان ما سهیلیه کرج هستیم بد جور لرزیدیم
۷ تا ۸ تا صدا انفجار بود سمت سهیلیه کرج‌کامل لرزید،
سلام ماهم اطراف آبیک قزوین هستیم ساعت ۳:۳۵ حدود پنج تا انفجار شنیدیم اما دور بود ازمون
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76179" target="_blank">📅 03:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNiH23ffne2f3T_NNcALXhYgGD9uMT5oT-0BvR6UpkKfAnESx0to6qENkUdwUevLd8_nm6qjFbblKnnwE3cBi9VfpJXUoumi_BEYTrHlFlQluxcv-AqxmO3Yx9zY-D_sbS5rM7Qr2tmlzwaV3Zl1Heazmg-2Sz_MG_6qa8nrbT-dwU6UUdi4ZQHidi5FxwDJHWspE5-9Xtjqt0cO0_e8qx7MvdwWDZ1iTUhkSPWvZQJA8VUBSjwseQy0ZM13UrPnUU_h_odFPovVvtkyKQTN9OeeoEyzjDtQtV9d1wJzFrZ70Nns7GYrlG1fGBGXUhvbc7G5wSC2KOQkd4I1XeXHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما به نقل از یک مقام ارشد جمهوری اسلامی اعلام کرد اظهارات ترامپ درباره تماس او با مقامات ایرانی دروغ است.
این مقام افزود: این اظهارات پوششی برای فرار از جنگ علیه جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76178" target="_blank">📅 03:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bEwYiI1idwWsdoS2kOK7b0Oxakq-8uon8IDza9RBneTCCoQOnAcf1XLHOipyeI0hYbq08G8z9P8801GuwatdxQw1bCOtbYCxMZrHXih9FdV-b9I7Xmdj7Zcvxqh89R3mrlq7XaCOHpvdh-N7DaNVOJRAslgeN0SEJMf68dL08bMjowKjONb0e1yEPNnglDGvwnoiwwPagUEVMEG8x7jbyFX_4VVBnqn92qZUIqszE6wjhWyMprVH_XghpkQ13Z_ZuB5NGSckXm0MbzjJvWy4fXRIhKDUZkTJZC-30xtZFSnjZR5oCbE3n-fVT5sMP5RfhS7mF-VYvccEuDGvn0eUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌‌‌های اکانت فرماندهی مرکزی ایالات متحده، سنتکام
ترجمه ماشین:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
✅
واقعیت:
کشتی‌های تجاری امشب همچنان در حال عبور و مرور به داخل و خارج از تنگه هرمز هستند.
CENTCOM
🚫
ادعا: منابع رسانه‌ای ایران مدعی‌اند که ایران به یک ناو جنگی آمریکا در تنگه هرمز حمله کرده است. نادرست است.
✅
واقعیت: هیچ ناو جنگی آمریکایی هدف قرار نگرفته است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76177" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYbH3ZdQIVouEf-N1QBNkFQC1LvzZT6mz0gT6XO6GFMqYPf2SACFguQXx31sj_pA-69gWi0bNYWrK9gkSCFV83jrDfV4O_ZxrbXGmyuSn3mMXal71VO-tmknX1z_dWbpgWJHHN_tp3aK84HkiIJvWz-Vx56VGXlZ21SRdcdV66YsT5XBbs6ddNUj8THZ5FkjgE1zou1borTWK3aZwZ-RC8P__2RNhqVNSk1SZ6M7LdxyhWONiphIZeMoZe9Xc3cQ2mwrSicigEAwa5f7b-sBjanS-9U4azmVj6I5xu8eTmkaZAfbqQ1jc6nAsKL395fI9RynY83tVZriG4Svj3AQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: مقامات ایرانی در تماس مستقیم خواستند بمباران متوقف شود
پست خبرنگار فاکس‌نیوز، ترجمه ماشین:
امشب با پرزیدنت ترامپ صحبت کردم؛ در حالی که او از اتاق وضعیت، حملات نظامی آمریکا علیه ایران را زیر نظر داشت.
رئیس‌جمهور به من گفت که امشب مستقیماً با مقام‌های ایرانی صحبت کرده است؛ مقام‌هایی که از او خواسته‌اند بمباران را متوقف کند.
در زمان گفت‌وگوی ما،
ایالات متحده ۴۹ موشک تاماهاوک شلیک کرده بود و جنگنده‌ها نیز در حال بمباران بودند.
نزدیک‌ترین هدف به تهران حدود ۴۰ مایل [۶۴ کیلومتر] بیرون از شهر بود.
ترامپ افزود که
بمباران به‌زودی متوقف خواهد شد، اما اگر آن‌ها توافق را امضا نکنند، «تا سر حد نابودی بمبارانشان می‌کنیم.»
پرزیدنت ترامپ این را
نقض‌شده‌ترین آتش‌بس در تاریخ جهان
خواند.
جی‌دی ونس، معاون رئیس‌جمهور، به من گفت که ایالات متحده در روند مذاکرات، هم با صداهای میانه‌رو و هم با صداهای تندروتر در ایران سروکار دارد.
به‌روزرسانی‌های بیشتر در فاکس‌نیوز منتشر خواهد شد.
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76176" target="_blank">📅 03:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3LJe-shX3K73wpxcIkx3J-UyUpaj7QLA0K6MMmAMNdRtGyqb5fFIaDC_NfphNUDUFGmLMIR62Wvtnz70SGQaIY_UUbctwOeVMunQCZF1ttH7j8R5gkNU6nHGrMLhb0AnoiFskWRSbHni2afdvtApwKH7BPWzD5bX9vFTMueeK5M017ZM7As9yu1ymkKVFk8i2XclrZVYZEEkeXMZsE5jdqO46u0dJzZ1gugLkV9mwgLDwpL2sWUfe28QHwyk95XcnFiIYlcdqAE5A1SQ_L1EqmPGHCoW-GjUD2NFKeuWp_G3H-_13rO5OcjZWkrNGRSqok4pMmKEzLTRAellhfuwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی پس از بیانیه قرارگاه خاتم که در آن تنگه هرمز کاملا بسته اعلام شده و هشدار داده شده بود که به هر شناوری که قصد عبور داشته باشد شلیک می‌شود، تسنیم از مورد اصابت قرار گرفتن دو کشتی در تنگه هرمز خبر داد. در گزارش این رسانه وابسته به سپاه آمده است که کشتی‌های «متخلف» قصد داشتند «به‌طور غیرقانونی» از تنگه هرمز عبور کنند. هنوز مقامات رسمی و سنتکام در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76174" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgGbpDkrBYcoUg_OnM_Q0dUWK1LpAQpUn8caNlYHxzn8ERyDeIdTb1kuxQrE_9nyrZ1ov-3KfpxmN8AAXq-rlYpjCqTbq1qqcg6SFLrS8LkLtZd7oAIIiDtsP5gaG2mzTNxfZ9EJrMFefZSe9ksC9B-Fx9OT1eAV6xYc2jxA6uq70RDLjNGYCZ621mzD1ttUT3WaWuLBkmDCEYDHYv3KGnY0wnWzJuMD89pb1LRLUMriSrhewCetpCY31be0qLrqRmxUNJeXxlYU2bTblxBa7nCHfA5o2yumJ_NHadQuBnOv6eRK4cWs4DmYboNHGhXxY-FLBDDiPa259tiIjQsMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
روزنامه وال‌استریت ژورنال پنج‌شنبه شب به وقت واشنگتن به نقل از یک مقام ارشد آمریکایی گزارش داد که هیچ سایت زیرساختی در ایران مورد اصابت قرار نگرفته است و نیروهای نظامی ایالات متحده در حال حمله به پدافند هوایی و سایت‌های راداری در نزدیکی تنگه هرمز بودند. انفجارهایی در امتداد تنگه هرمز، از جمله بندرعباس، جزیره قشم و سیریک گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76173" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی:
قشم ۲:۳۵ صدا و لرزشش حس شد
۲:۳۵ دقیقه بندرعباس دوباره صدای انفجار اومد
سلام  بندرعباس دوباره زدن ۲:۳۷
[احتمالا منظورشون اینه که صدا شنیدند!]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76172" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdPjsAG0dvZ21DOAop4D4f29gJZawU4QYFO1x0bdduGD36JEO3XgY4hP0T6WfebBrZgXiVcWAQqadYWQmKA8ngNpEvukbImtbhddtr0fCc_SQyQ3f47Bl1O88Y5S6OsYKaoD7hkYTUAMuL6f555WlZhzOlpKumyWi2j0b1YND4x0RPihzPL_zWwf8yG9NmgvZ61-InkCtYL9Yc361qJpBcD-ueApV-vtSdQu4_W0GN7UyawVnaddJkrJhCHdIVo1D6qhjjTiqHUOQnqVnMefJjgwAgC57x6DSaqfLZslSKWLKKw7bav7i7SenNP26vMWw4kTa2L3kpr9EN5c3kNpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: هرگونه تردد شناورها از تنگه هرمز مورد اصابت قرار خواهد گرفت
منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76171" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2wNg7k5cU22Qo6U3BEqhIVbfwG8lxpKwI6UAZHdMAumf_KpOLlzqHEjL9AwU0Hq6GC_QG8Px9EuG-_7BvCADU1PTQGj6I9ZqMLuVeqeB3MfYLJrYJQ7MI8-cn9y_IbBWYX6b1W0p5zUPj-DN25kkTAbHdfut8S5rxXVaCj0poqJh4BLqvaeDzYXpMDxWswzErm0sBD01jCrct-5A9UoqShQEn5pR0Ts6IKuKGsgMZeqF0Gu4mIcedBj6bkoPuMEonB9ltX2cQ2k-xIBIoXYXuqtZ1ZJgOttMj0-J1fwsg_7cutAfl-SBCUakLVr4lL0vC1zqYCx0sIr0czIwjGQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس بامداد پنجشنبه ۲۱ خردادماه به نقل از یک مقام آمریکایی گزارش داد تمامی اهدافی که در حملات اخیر مورد هدف قرار گرفته‌اند، در جنوب ایران واقع شده‌اند.
این مقام آمریکایی گفت سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها از جمله اهداف این حملات بوده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76170" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بعضی کانال‌های خبری به نقل از تسنیم نوشته بودند:
‌
منابع خبری از هدف قرار گرفتن یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه خبر دادند
خبرگزاری تسنیم وابسته به سپاه در پستی نوشت:
انتشار خبر جعلی در کانالهای فیک‌نیوز به نقل از تسنیم
برخی فیک‌نیوزها از دقایقی پیش به صورت هماهنگ خبری با عنوان "هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد" به نقل از تسنیم نقل می‌کنند.
این در حالی است که امشب چنین خبری تا این لحظه بر روی هیچکدام از خروجی‌های تسنیم قرار نگرفته است و چنین خبری تاکنون صحت ندارد.
به هرحال اون خبر رو خبرگزاری دانشجو وابسته به بسیج هم منتشر کرده و الان به نقل از اون داره پخش میشه.
🔄
آپدیت:
ایرنا، خبرگزاری رسمی دولت در جمهوری اسلامی:
فرمانداران عسلویه و کنگان که هر دو شهرستان میزبان تاسیسات پارس جنوبی هستند هرگونه حمله و انفجاری را تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76169" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
صدای سه انفجار در بندرعباس
بندر عباس سه صدای پشت سر هم ساعت 1:20
وااااایییی تو دو ثانیه سه تا انفجار شنیدم بندرعباس خیلی نزدیک بود
بندر عباس همین الان چند تا صداااا
بندرعباس سمت زندان شهرک صدای جنگنده یا انفجار طولانی اومد
همین الان یک انفجار خیلی خیلیییی سنگین بندرعباس
دوباره انفجار بندرعباس ۱:۲۲
وحید بندرعباس الان یجوری زد شهر لرزید
وحید ساعت ۱:۲۰ بندرعباس سه تا انفجار خیلی سنگین شد
دوبارهههه صدا اومد ولی خیلی دوررر بود فکر کنم سه/چهار تا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76168" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxdRP1XKl_6TT52SV0491mH-VATkhFalvveQGkUpV-33OSphuZLBgp4zGumUTHbVrbiQZidkxIz-TtzjoWD69JRTlSspKsW_0dRglXtvssT1QL4IbMvxB-bi8jQ6wTMwPpN-pzSfEQvKVjvbGOkjaNiPx6q7zr4eYGJA7JMkpDaAyp5lr_K0VkRFAlJw5iFTVWvoHXrDUz78EAFa8QsjxQw8vabAI4cGFSWypEJ6IHGbEoVgCcDTynk-U-_uBsrB_J_J9zdfDVg85Z0cceUxIPzVGXGUdrKWhsvQKdr9S9NIrBexzi_7M2Wk4ns0vUatpeZ1ALHUFsYBMCHrf9wD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی آمریکا امروز، به دستور فرمانده کل قوا، از ساعت ۵:۱۵ عصر به وقت شرق آمریکا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران آغاز کردند.
این حملات در پاسخ به تجاوزهای بی‌دلیل و ادامه‌دار ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76167" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱:۰۳ بندرعباس صدای انفجار شدید اومد
بندرکرگان شهرستان میناب، رو با موشک زد
همین الان
پاسگاه دریابانی رو زد
صدای دو انفجار در بندرعباس همین الان
سلام ساعت همین الان انفجار شدید در بندرعباس ساعت ۱:۴ دقیقه
وحید از ساعت ۱:۰۳ دقیقه بامداد
چهار تا انفجار بندرعباس
سلام وحید،صدای چند انفجار همین الان بندرعباس
سلام. همین الان صدای انفجار شدید، بندرعباس، ساعت یک و سه دقیقه شب
صدای انفجارهای ممتد میاد
صدای انفجار بندرعباس
بندر عباس فکر کنم سه تا انفجار با فاصله چند ثانیه
صدای انفجار بازم میاد میناب نوار ساحلی
انفجار دوباره
سلام،وحید جان بندرو زدننن من لرزیدمم
همین الان صدای انفجار بندرعباس دو الی سه تا صدا اومد
انفجارها داره زیاد و قوی‌تر میشه، بندرعباس ساعت یک و شش دقیقه شب
سلام‌وحید جان بندرعباس همین الان ۱:۰۵ دقیقه صدای انفجار اومد
سلام وحید جان
همین الان ۱:۰۶صدای انفجار داره میاد بندرعباس
پنجره خونمون لرزید
درود درگهان همی پنچره ها لرزید
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76166" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، بدون هیچ توضیح بیشتری نوشته:
شنیده شدن صدای انفجار در سیریک
🔻
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
بررسی‌ها نشان می‌دهد که
تا این لحظه
اخبار مربوط به صدای انفجار در جزایر کیش و قشم صحت نداشته و صداهای شنیده شده مرتبط با درگیری در خلیج‌فارس است.
براساس گزارش منابع محلی، دقایقی پیش صدای انفجار در اطراف میناب و سیریک شنیده شد.
🔻
پیام‌هایی در ابراز تعجب از پرواز هواپیمای مسافربری در تهران دریافت کردم.
🔻
تسنیم در پست دیگری نوشت:
تاکنون صدای ۴ انفجار در سیریک شنیده شده است
🔻
عکس‌هایی از فرود  هواپیماهای مسافربری در تهران دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76165" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=tXA9ed-3qT_kR-TjGUKng4d5eQgRT7yNikebyGqz3nNRuTmBEc_sgm_5Na-byKwBYqI8fxdBrAUDkJiNo3PPmwllAD1rLtGmB42Cy9aBrur4JYjVLkl5ldj-LwVIbxGQGKv4b3T47QqYZYeCB4I2BV4GclXtaKrbMBNkhcuJlkIkVWYyi62XEjT90KONugfEIQUI-52MBO94DEHVhNNmYB9pM-CAzCVD8AiVj36bGQKl59UNM0_fjqutCegJNhB2HQqiX2vleULZ4tv6JQkhgf4lIYcJE-U0YFMqGT01WzgInBNN2W4EhB2uS--q7weOxQkZT74t9Ev2ZXar1tPbH4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=tXA9ed-3qT_kR-TjGUKng4d5eQgRT7yNikebyGqz3nNRuTmBEc_sgm_5Na-byKwBYqI8fxdBrAUDkJiNo3PPmwllAD1rLtGmB42Cy9aBrur4JYjVLkl5ldj-LwVIbxGQGKv4b3T47QqYZYeCB4I2BV4GclXtaKrbMBNkhcuJlkIkVWYyi62XEjT90KONugfEIQUI-52MBO94DEHVhNNmYB9pM-CAzCVD8AiVj36bGQKl59UNM0_fjqutCegJNhB2HQqiX2vleULZ4tv6JQkhgf4lIYcJE-U0YFMqGT01WzgInBNN2W4EhB2uS--q7weOxQkZT74t9Ev2ZXar1tPbH4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در جمع خبرنگاران گفت حملاتی که امشب به ایران انجام خواهد شد، «قوی و روشن» خواهد بود و فرماندهی مرکزی آمریکا امشب درگیر عملیات خواهد بود.
او افزود آمریکا تاسیسات کلیدی در جمهوری اسلامی را بمباران می‌کند و امشب «ضربه سختی» وارد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76164" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riQ75j5C1AR4wrFVHd4lZVJEuYDINlzTQ9TTFmlI4Xt6um_DJKrv1YMSBwSrvjgMIrEntIrUFz7XR7642BWkK10KBqGPt_DnAJ8ulNgI9wsnpRBVOFiV_ztKuriDEAr7aXIobOw9N9j10ktgfeiGsL0xP2BJ2tlRM1vGuE7AVUygiCn886C-Vg8WUzWgmNeYZE_5Ip8F2Dye6kkj_aJNvjcyWwC3bACSXDY9W5OiucJzDuHYIO3u27lwOZR63_u4EfVxMUOxDWdgrSZ1E9Djk8Vhl-yXzryaM3jBh_594m_S6UhI3urvSnmilsKv_78X1fY1R8_h5r0IR_lkNKoSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ درباره گزینه‌های حمله به ایران در اتاق وضعیت جلسه برگزار کرد
ترجمه ماشین:
پرزیدنت ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت کاخ سفید برگزار کرد تا درباره حملات احتمالی تازه علیه ایران گفت‌وگو کند؛ این جلسه چند ساعت پس از آن برگزار شد که او به خبرنگاران گفته بود آمریکا «امروز دوباره ضربه سختی به آن‌ها خواهد زد». این را دو منبع آمریکایی اعلام کردند.
این منابع گفتند یکی از گزینه‌هایی که ترامپ در حال بررسی آن است، انجام عملیاتی است که از نظر مقیاس بزرگ اما از نظر مدت‌زمان کوتاه باشد؛ با هدف فشار آوردن به ایران برای تغییر موضعش در مذاکرات.
این منابع جزئیات بیشتری ارائه نکردند.
پیت هگست نیز در فلوریدا خطاب به سربازان گفت: «اگر قرار نیست توافق کنند، ما ضربه سختی به آن‌ها خواهیم زد»؛ سخنی که بازتاب‌دهنده اظهاراتی بود که ترامپ پیش‌تر در روز چهارشنبه بیان کرده بود.
axios
کلی میر،‌خبرنگار نیوزنیشن گزارش داد پس از آنکه پرزیدنت ترامپ گفت ایالات متحده به حمله به جمهوری اسلامی ادامه خواهد داد، پیت هگست، وزیر جنگ آمریکا اعلام کرد سنتکام امشب مشغول خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76163" target="_blank">📅 23:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU_eYQ7uG9Dk2gxyYQaBVVmpgVMgG0LLgyHqjODWH-p7lz0xxUV57VFxOYxgbwkECYrjUWsmpflUO-g4JVyhZOkFPCbexM55piH8tBKRGiqOHMyEhlsMoJCYqeivbX_AbdY2k_PC09Iko5KMswwkwRQMIoszRc-YcAGHI2tFEpvN4EE_YDkIguqihWCNT_lv33GmgJKIYuThi9O5rtsAIC4QlJ2MO8SegH9XQHkVLZhMdmnWWYgDdOL9TQJ1RCGi59ukticAa-6fOcUZftFRdnY5IfvugMUnfXcr5gdHbbuvySRA240oDvVSYB-e2VXS71aU-bXNctbXUJ2CnvB39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز ۲۰ خرداد ۱۴۰۵، گزارش داد جمهوری اسلامی با پیشنهاد میانجی‌های قطری برای برگزاری یک نشست سه‌جانبه با حضور نمایندگان ایران، آمریکا و قطر به منظور حل اختلافات باقی‌مانده در مذاکرات موافقت نکرده است.
بر اساس این گزارش، مقام‌های ایرانی و آمریکایی طی دو روز گذشته به صورت جداگانه با میانجی‌های قطری در دوحه در تماس بوده‌اند. با این حال، تلاش قطر برای برگزاری یک نشست مستقیم میان طرف‌ها با مخالفت تهران روبه‌رو شده است.
اکسیوس به نقل از منابع آمریکایی و منطقه‌ای نوشت که همزمان با ادامه تلاش‌های دیپلماتیک، هیئت قطری روز چهارشنبه برای گفت‌وگو با عباس عراقچی و دیگر مقام‌های جمهوری اسلامی به تهران سفر کرده تا روند مذاکرات را از بن‌بست خارج کند.
این گزارش می‌افزاید که دستور دونالد ترامپ برای حمله به اهداف نظامی ایران تنها به دلیل سرنگونی یک بالگرد آمریکایی صادر نشد، بلکه نتیجه افزایش نارضایتی او از تاخیر جمهوری اسلامی در پاسخ به آخرین پیشنهاد واشنگتن بود.
به گفته یک مقام ارشد آمریکایی، هدف از حملات محدود آمریکا در شامگاه سه‌شنبه «بازگرداندن اهرم فشار» در مذاکرات بود، بدون آنکه تلفات انسانی بر جای بگذارد یا مسیر دستیابی به توافق را مسدود کند.
دو مقام ارشد کاخ سفید نیز به اکسیوس گفته‌اند که حتی اگر سرنگونی بالگرد آمریکایی عمدی نبوده، واشنگتن برای جلوگیری از تضعیف موقعیت خود در مذاکرات ناچار به واکنش بود.
به گفته این منابع، حملات آمریکا به گونه‌ای طراحی شد که تنها سامانه‌های راداری و مراکز کنترل پهپاد ایران را هدف قرار دهد.
اکسیوس همچنین گزارش داد که کاخ سفید ساعاتی پیش از آغاز حملات، بار دیگر از تهران خواسته بود پاسخ نهایی خود را درباره پیشنهاد اخیر ترامپ ارائه کند، اما مقام‌های جمهوری اسلامی اعلام کردند هنوز تصمیم نهایی اتخاذ نشده است.
بر اساس این گزارش، ترامپ پس از نشست ۸ خرداد در اتاق وضعیت کاخ سفید، دو شرط جدید را به پیش‌نویس تفاهم میان دو کشور اضافه کرده بود.
نخست اینکه ایران ظرف ۶۰ روز ذخایر اورانیوم غنی‌شده خود را رقیق‌سازی کند و دوم اینکه از دریافت هرگونه عوارض یا هزینه از کشتی‌های عبوری در تنگه هرمز خودداری کند.
در مقابل، واشینگتن آمادگی خود را برای پذیرش انجام فرآیند رقیق‌سازی در داخل ایران و تحت نظارت آژانس بین‌المللی انرژی اتمی اعلام کرده بود.
اکسیوس به نقل از منابع آگاه نوشت عباس عراقچی به میانجی‌ها گفته بود برای ارائه پاسخ تهران به چند روز زمان نیاز دارد، اما این روند به نزدیک دو هفته انتظار تبدیل شد و موجب افزایش نارضایتی ترامپ شد.
این گزارش همچنین می‌گوید پیش از تشدید درگیری‌های اخیر میان ایران و اسراییل، دو طرف به دستیابی به توافق نزدیک شده بودند، اما تحولات نظامی روزهای گذشته روند مذاکرات را پیچیده‌تر کرده است.
با وجود حملات متقابل و افزایش تنش‌ها، مقام‌های آمریکایی به اکسیوس گفته‌اند که مذاکرات همچنان متوقف نشده و واشینگتن امیدوار است فشارهای اخیر، جمهوری اسلامی را به ارائه پاسخ نهایی درباره پیشنهاد آمریکا وادار کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76162" target="_blank">📅 23:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2AJnaZ1qNSX08mm156ndwQmYKZjJJK-WXoGnowSugjT5AfhvQXd3WORyMpFVTephZNywK_mqfxnwYZZm7Bj3FvZcH6KBYvq8HHYpuQbqmlnTFA-0LlQsJtxpRSYnXSqoSGwxn36c5aoaSJ_M7jpH-3zRR7B45k9ROjxyTVdEkrnWa_zgdcfUNW5x1QDciTk2rixrQSrARvd0i9f-a9Th3eCD56dGywEKmAMj7syM77axb79E5dmsoVlSkpNzOyGAq39KshB3cj796S_pO7hEcxd0kfc63OgKAxhBV2WpAqxsu_G7eRS1mnryzXJsJHApfRZCAwzs1HPzW1u0_VC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس، در شبکه ایکس نوشت: «در جنگ ۴۰ روزه وسعت آب‌های سرزمینی ایران افزایش یافت، در جنگ بعدی شاید وسعت خاک ایران افزایش یابد.»
او در مطلبی دیگر تاکید کرد جمهوری اسلامی آماده‌تر از قبل است.
او همچنین در یک برنامه تلویزیونی گفت: «دست از لبنان برنمی‌داریم و دشمن یا باید به خواسته‌های ما در میز مذاکره تن بدهد یا در میدان نبرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76161" target="_blank">📅 22:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/274405ecae.mp4?token=MoY_EJQmatCk6lnXwKZzgQ_iYgwUlRCfp5bT0XolfRexNSpgBoKJ00foVSyZwLO3oscPsQGEV0UwKk5B7p103dIihRK5Fnaj2maKegQ8caSPKY8AEVZ5Kc5CAVhBDVUDsH7bGSxfJCEm6JyTLXqB8gsF13Cf_XMdApKzXCW9xfFY1w7QvkKYrfEcrv0qGJ0EewNQQz1Dribyia8IpjM76m27XEWAg2aLXLs_CWImNB6hNI_V22kCGlqt-K3Jj9VIhY5rQd5a-QFInsaRUoIJTTH0NHt9Lzv_yJjaJyuxCAI-68fjdoDAVTExSUOMjrTfp2bQpMGb_f2SNeUgMbnqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/274405ecae.mp4?token=MoY_EJQmatCk6lnXwKZzgQ_iYgwUlRCfp5bT0XolfRexNSpgBoKJ00foVSyZwLO3oscPsQGEV0UwKk5B7p103dIihRK5Fnaj2maKegQ8caSPKY8AEVZ5Kc5CAVhBDVUDsH7bGSxfJCEm6JyTLXqB8gsF13Cf_XMdApKzXCW9xfFY1w7QvkKYrfEcrv0qGJ0EewNQQz1Dribyia8IpjM76m27XEWAg2aLXLs_CWImNB6hNI_V22kCGlqt-K3Jj9VIhY5rQd5a-QFInsaRUoIJTTH0NHt9Lzv_yJjaJyuxCAI-68fjdoDAVTExSUOMjrTfp2bQpMGb_f2SNeUgMbnqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
و گزارش صدا و سیما که میگه بیشتر انبار فرش هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76159" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_m6ErQi9UzQM5nGymFXsmVv21CMY-QaBSgpY9mRjtV4h-JExYUIum3GvZaZcw4EwnftPUq39Cu6XD9s8Y2OlaT__r-5rlu_JMlV16_JeoubpwfT7CLOJbhh_o-2nYtbcmtuW7cfrgqaoc_WTmfmGAZLjcCQpZubnM8C8N4A6uWMdmkUzukDPlP1m_1_6u26hIX3pVZaDQ42_5xOEaAYWYSkBA0FsXMW6w6fZyBinRmQNcKFTComAET6eJSrC8zIinCo1jPWv6sj2LOoeF_EynplX5w3-uRKsG2VlgWB5_DZfWSLd8DdARCXLbJeAy2xA3NFn-p_l1zdcyNGvDFi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیش از ۱۰۰ میلیون بشکه نفت در جریان ماموریتی محرمانه از تنگه هرمز عبور کرده است
ترجمه ماشین:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76158" target="_blank">📅 21:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbVIFEAjW83qPXt_U1z6qCMd0h2gyEKJJLGQaFvTPsBjy8xu_35M9SnEovTkIThqnIQOKd4OW6JLKehIiyKgzP-CQfcImzHs6P4awhnF0U5YCXx9seyf90mOXWuF1DCY1k3VN7mCHKpqXIv1If0SvhXQWEfxJ0l1AMOSxtQoXuSNEf73LURNOrZI6GJe-qYrUEJ14iLkMUq0Z3ljKLWJLuLhSgf9PALKHsZuoAUE41a6lVtIEKs4QIvPcI2WK7fcUFtcpvg6VZPBZMz9g5p7Ci5wvv4qmPJdvE0GYjiPnoLfnzPtiN89-Ooc2J8mtocFkVfFdHCfiJK2L1r-LhO5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=OxQ3qliPWamg7MX6lQEc3h8-XVoI5mI_q0wy6JuDmvQOyWLgxzra3JMhevdRRDVQHWXJ7ijJnjMalHt3bOuZUan2SB4Tr-P3ASb8zcniR8FyU8-dfwQo4HsAg1gXv-xw-TsxLUjE7_OzCB8t_DbG7am9WOLGFvvFrw5JK0U-qgaeOw1mJESDFwZrAEuP3ofSaM6-xEYScy7KDvCoH_CKefQZjHEqvl6S4L3VbgKIn904yeA-AiGqcJcELADOfBGGtzT_X8J80lYzRkiUsLZi1QOOoXgurGAd3l-7s30Vd21msZ2bZa8iLgcwW-flG-Bv6qRCvUuj9ue6EAPSPE87ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=OxQ3qliPWamg7MX6lQEc3h8-XVoI5mI_q0wy6JuDmvQOyWLgxzra3JMhevdRRDVQHWXJ7ijJnjMalHt3bOuZUan2SB4Tr-P3ASb8zcniR8FyU8-dfwQo4HsAg1gXv-xw-TsxLUjE7_OzCB8t_DbG7am9WOLGFvvFrw5JK0U-qgaeOw1mJESDFwZrAEuP3ofSaM6-xEYScy7KDvCoH_CKefQZjHEqvl6S4L3VbgKIn904yeA-AiGqcJcELADOfBGGtzT_X8J80lYzRkiUsLZi1QOOoXgurGAd3l-7s30Vd21msZ2bZa8iLgcwW-flG-Bv6qRCvUuj9ue6EAPSPE87ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از نزدیک‌تر: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76156" target="_blank">📅 20:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftBiCtArgp7PmEehvXwgU6_BNLWZVVDHMm-dHuIGCjhCK7xnnvdKgN8Ny5mjInPHmu--98y-OQ500ZLUYokBRLoramiXQJUdxVqoq83wSWfVK9qTmBRHjk7f8NU8Wurb0iEPu9quLz6rVexpClQ7-g1nv4yr99WTT-hLVVfw81xQfJKnHgAun4Hp0lSNi1pHDv4p49kbvzDiODf2BGlGqdFQEACE_VVBuJIeepCBleF30Qxnbt3KIaA8X0j-Ue3WO3QbUjZ_IQEKxe9H6IvmUKIQCrLpaps-HoqjAAqZ_ICPrLFc15VwXnrPg4JIx545UXPvF5zrxUPORyrCRHAxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nwy1oDayfXrT1qGcXt-9SkD1VKvpppbFA6yhakepZ_E_2DSsC0iwkaiyJZtELu7G91K9MKKvvMsZMD3IFkeaLOwry11g3Xy899-Bkjz-Bak-4WVv3rer5vzN1qjk_BLy8P96L0-xHpz91D6IJFpKC42jgy0uuKcWCW9l75wzQivAEW4okfeHn94DTvtGrBosdDHkBQkwyWDd-77-mjD-GaQghcHyQmGmBsnfZ9K-Y5Elyj3dZog3b48R1z-1l6LNuRHk1_AiV_KGw8Mi8VTuEPkMa3TFcwOZIFMfdPWaPYDh3feWFyKbrO4IlYYuGSQlyFbQqZ8JyR1npzTHtutMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s0FH2tQkOihl0v-v1qx1LIf7ZU-5cSR7P26OqKrFYy2d0zkiafs4cwLrTLmL3h_UkbJlD5uIAAQ3c6ScGd7rd4Nsyaz0KMg8MSFmeoFXvZAtjWi-MKkpnu6gomJZoryeVuGmcJenVYKgFagaowzupWlDTxKIuKAjr1KNVqvY1rWAIt4KhK7Wxvg6uc-YapOO1yI6onK2L344B6OadG0pluJgEOXLWaROUpVRv0hNg9q0r83oamBM0ZWykTMmS_CplGisaM0Xwzgb_2xIA_63Rat23ZoY1h1MMVhJscxMwhGRhRIe67fuCI-TWMowlsSli6sI4C1eD4jxfCRdpe1dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FlGsJoOe-ZZpgHE7MhvJwgx4KVqzEOMiiSnMI0Co1q2dKtaR46XoDsQBi0MB9XgRV7IQCV8C8cD9RqYkaXOYQhc6EmoZdxq0pqsqYwP_lxSG7__h8jzg2WGK7--gWsKi6PggvOB77C2g9YwTdpjfZrqUof7oWva0shTEITIbNSDdP0Gq81utS6h1ImsLLaBhRAucYUqZIUB78I5THHTkwFarQ2MuROXMiVTlJXMirKDn31LqV-t4haKnDhGhfyG2La5raC5nM8UdFSALX-BoKnWKGraASBkU520rPhkNC4p_ysfwm1bRzA5XtptVN60beosh0xOoXUnP_BGVHngu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ooy8iOHVUnjnCkE1PbB5aVqkx-3ve-Ro6TVnjNJE7SVQoMCr703Ck8dgrDmW_i6fyxBIKYhPsj9syr9peF1d1bU3dhh2TfLyovSjGAoumht_qi7GHAe0_lO_ixsGt4gdh88GZfoLtNMPt0kWfSs_O_ZSMPNwzrVYgYtUd41Ma1Eexjyv0LdiXDfaEGhRcUu7ywzszvJ1EJTnml6cON0pnZXqD6rXCevjdK-hfOXlEPxOZ40M2-hgIt5ZDToBE6EM7ixxurv_A5VHqkBfm4YAlHuqfPtyFz7pCIYnXlpSJasrOJF0eIko8yg3hrExNUX2D4rlOOjGdfr1AfKAijp9_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از ستون دود سیاه و غلیظ حوالی مرکز
#تهران
منابع حکومتی نوشته‌اند: "یک انبار کالا حوالی میدان قیام در منطقه ۱۲ تهران دچار
#آتش‌سوزی
شده است."
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76151" target="_blank">📅 20:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=EESqZ0JrzESGtv7obUzSQDelsb-4J0ZH1dy0zxfoeOKRXVmJ7G1nJSW_dVbLcOdK_GI7gbzAZ0-ABtQjJjL2SvZJZN5iD9prh25J1NLXzi3J9rSmdRqQxLzAkb8ZLazbUD76ZJdEunIIvKqqIDcNQTEVYi-JpdFaIFloRnx6DMEj-zh5Q7FqO5zhoO-6Hw4u1sDEzC1s6NL9bCVgnLS8UcAxJIZ53LHeIu8orMGzuMap3xWvs3g7usDd3x0ObkLiTNu-nlimTgo5Oxg638YiC45cdq_Odhe89SBohHRcziAVkOcMOPAYxnM8x2k10kGSFm2wI5XrroxXLjNsnepGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=EESqZ0JrzESGtv7obUzSQDelsb-4J0ZH1dy0zxfoeOKRXVmJ7G1nJSW_dVbLcOdK_GI7gbzAZ0-ABtQjJjL2SvZJZN5iD9prh25J1NLXzi3J9rSmdRqQxLzAkb8ZLazbUD76ZJdEunIIvKqqIDcNQTEVYi-JpdFaIFloRnx6DMEj-zh5Q7FqO5zhoO-6Hw4u1sDEzC1s6NL9bCVgnLS8UcAxJIZ53LHeIu8orMGzuMap3xWvs3g7usDd3x0ObkLiTNu-nlimTgo5Oxg638YiC45cdq_Odhe89SBohHRcziAVkOcMOPAYxnM8x2k10kGSFm2wI5XrroxXLjNsnepGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، طی سخنانی در کاخ سفید درباره جمهوری اسلامی، گفت: «ما آنها را بسیار سخت هدف قرار خواهیم داد. باید توافق را امضا کنند. ما توافقی می‌خواهیم که معنادار باشد و کار کند.»
او ادامه داد: «امروز دوباره ضربه محکمی به آنها خواهیم زد.»
ترامپ افزود: «نخواهم گفت آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد یا نه.»
ترامپ با اشاره به هدف قرار گرفتن یک بالگرد آمریکایی گفت جمهوری اسلامی ابتدا مسئولیت این اقدام را رد کرد، اما بعدا آن را پذیرفت. او افزود بمبی که به بالگرد اصابت کرد منفجر نشد و دو خلبان آن در جریان یک عملیات نجات زنده ماندند.
ترامپ بار دیگر گفت: «دیروز ضربه سختی به آن‌ها زدیم و امروز هم دوباره ضربه سختی خواهیم زد.»
او در پاسخ به سوالی درباره احتمال هدف قرار دادن پل‌ها و نیروگاه‌ها در ایران گفت جزییات عملیات احتمالی را اعلام نخواهد کرد، اما آمریکا توان انجام چنین اقداماتی را دارد و «قوی‌ترین ارتش جهان» را در اختیار دارد.
دونالد ترامپ، رییس‌جمهوری آمریکا، در در کاخ سفید، گفت جمهوری اسلامی «به هیچ‌وجه» نباید سلاح هسته‌ای داشته باشد و نخواهد داشت و افزود مقام‌های جمهوری اسلامی نیز با این موضوع موافقت کرده‌اند. او گفت تنها کاری که جمهوری اسلامی باید انجام دهد امضای توافق است.
رییس‌جمهوری آمریکا افزود توافق «کاملا مذاکره و نهایی شده» است، اما جمهوری اسلامی همچنان در حال وقت‌کشی است.
او گفت: «چند روز دیگر هم به آن‌ها فرصت می‌دهیم، چون این یک سند مهم و معنادار است و آن‌ها می‌دانند وقتی آن را امضا کنند، تعهدی جدی ایجاد می‌شود.»
ترامپ بار دیگر برجام را هدف انتقاد قرار داد و گفت: «توافق اوباما، برجام، یکی از بدترین و احمقانه‌ترین اسنادی بود که تا به حال دیده‌ام.»
ترامپ همچنین گفت جمهوری اسلامی از برخی اقدامات اخیر آمریکا اطلاعی نداشته و افزود آمریکا چند شب پیش ۲۲ کشتی را در تاریکی و بدون چراغ جابه‌جا کرده است. او گفت جمهوری اسلامی «دیگر رادار ندارد» زیرا آمریکا سامانه‌های آن را نابود کرده است.
او در ادامه گفت زمانی که تصمیم به حمله گرفت، به اطرافیانش گفته بود اقتصاد آمریکا در بهترین وضعیت قرار دارد، بازار سهام و حساب‌های بازنشستگی به رکوردهای تاریخی رسیده‌اند، اما جمهوری اسلامی به‌زودی به سلاح هسته‌ای دست خواهد یافت و به همین دلیل باید اقدام نظامی انجام شود.
ترامپ افزود آمریکا با بمب‌افکن‌های بی-۲ به جمهوری اسلامی حمله کرده است. او این عملیات را «بسیار شجاعانه» و «کاملا موفقیت‌آمیز» توصیف کرد و گفت پس از آن «مرحله دوم» نیز باید انجام می‌شد.
رییس‌جمهوری آمریکا گفت برخی پیش‌بینی می‌کردند بازار سهام پس از این حملات تا ۲۵ درصد سقوط کند، اما جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای «ارزشش را داشت». او همچنین گفت نگران بود قیمت نفت تا ۲۵۰ دلار در هر بشکه افزایش یابد، اما اکنون حدود ۸۵ دلار است.
ترامپ در ادامه گفت نیروی دریایی جمهوری اسلامی «از بین رفته» و ۱۵۹ شناور آن در کف دریا قرار دارند. او افزود جمهوری اسلامی دیگر نیروی هوایی ندارد، هواپیماهایش نابود شده‌اند، بخش عمده پهپادها، توان تولید پهپاد و موشک‌هایش از بین رفته‌اند و رهبری جمهوری اسلامی نیز جایگزین شده است.
او در پایان گفت فکر می‌کند جمهوری اسلامی خواهان توافق خواهد بود، اما افزود:
«خواهیم دید چه اتفاقی می‌افتد.»
ترامپ همچنین گفت با پایان جنگ، تورم کاهش پیدا خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76150" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXMvSJYbcVV475yeFjr2wBxkEN5_FBcp_dSvqymRdDjBY5u0Gpez-hAc8NlnECsexdSqJ-w6R_2STDWCugC2HB9d3mP216AakzHLAgroMhJYamEG6UnspLTDnhaxeXcBq4hk5mLLOil3W6PPVE8wuW9RcODVQ-OucqVy35lfz9hp4gCUNbXpsh2wddV3gIoA7Y9NW405ERQtL1Mwu4AYXklslQVIMEUL4ITmkfM_lTY_8yT4Q4ECRx9wBuraMJgmRJkVqybeXM1yeNcc8hq9mcWmAG6rXQT2WXUgaFfK8x7vXrEiCGy_TVbVuN1UnDeN-PirloZA8f8l3PLePSwxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز چهارشنبه ۲۰ خرداد، در پاسخ به درخواست خبرنگاران برای شفاف‌سازی درباره اظهارات قبلی‌اش مبنی بر اینکه جمهوری اسلامی ایران باید بهای طولانی کردن روند توافق را «بپردازد»، موضع تندی اتخاذ کرد.
دونالد ترامپ در دفتر بیضی کاخ سفید به خبرنگاران گفت: «خب، ما به آن‌ها حمله خواهیم کرد، و بسیار هم سخت حمله خواهیم کرد.»
در ادامه از او سوال شد که آیا این به معنای از سرگیری کارزار بمباران [مواضع ایران] توسط ایالات متحده است؟ ترامپ پاسخ داد: «بله، خب، با توجه به موضوع بالگرد، فکر می‌کنم این حق را داریم که چنین کاری انجام دهیم.»
ترامپ ایران را متهم کرده است که یک بالگرد آپاچی ارتش آمریکا را بر فراز تنگه هرمز سرنگون کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76149" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/460f7345bd.mp4?token=V8NX-x0qgWRPHLnDKN0hl18CFnEfzHMONU2zOFij5-UIkfduRQJBBaNqLmqaXjCYIMTbfbwXnCItGALNaB9GY-vG2bMyljEbEPySA-2TxvPLwLhX6VOFhOxvFwUkrcyO4MavJqyn9NQN_HzMlCv3Hfq1z0AhMeHhXFdYCiVjqZeip1bkad5Me51AVDhai3KLWjDi-4clmI4bSQBLw7vU46qSOxe3xgr44Dknz2iAmzAyoNH9Jh67v0tOBWV1wDQfK7MomGsqE0WAvn6lg0AduEzaJP5YIWd_blrVWAgZk8AhOdE-xx3FJyF3GcqTI4GUbnXs_67Zvbkqtl4cN-RDxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/460f7345bd.mp4?token=V8NX-x0qgWRPHLnDKN0hl18CFnEfzHMONU2zOFij5-UIkfduRQJBBaNqLmqaXjCYIMTbfbwXnCItGALNaB9GY-vG2bMyljEbEPySA-2TxvPLwLhX6VOFhOxvFwUkrcyO4MavJqyn9NQN_HzMlCv3Hfq1z0AhMeHhXFdYCiVjqZeip1bkad5Me51AVDhai3KLWjDi-4clmI4bSQBLw7vU46qSOxe3xgr44Dknz2iAmzAyoNH9Jh67v0tOBWV1wDQfK7MomGsqE0WAvn6lg0AduEzaJP5YIWd_blrVWAgZk8AhOdE-xx3FJyF3GcqTI4GUbnXs_67Zvbkqtl4cN-RDxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان هرمزگان گفته است در پی حملات بامداد امروز آمریکا «زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک» تخریب شده است.
عبدالحمید حمزه پور گفته در این حملات «دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته و به طور کامل تخریب شدند ... که نقش کلیدی در تأمین آب شرب بخش بمانی و شهر کوهستک ایفا می‌کردند.»
@
VahidHeadline
خبرگزاری فارس:
آبفای هرمزگان: شبکهٔ آبرسانی مناطق آسیب‌دیده در مدت کمتر از ۱۲ ساعت مجدداً وارد مدار بهره‌برداری شده و مشکل قطعی آب در شهر کوهستک و روستاهای بخش بمانی به‌طور کامل برطرف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76148" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoSHyaaqd5xCKwvI0-LrRS9P2cv9cWXvWTUAQDnJctzUwBnU8ZugSiBAVkST8sA_sorNpyGeN74cs4mis1TsJQ9L1I0ExonUMYoujwG1CZMJjjtGigUZk4aNRhnwdDw_nB7lYD1ajvBrjjwmFmpip3T4uD6dgbRlAnyE7sTUK2-DyYBG3FTd-EzMbwydZZmdFDaoQz6nPv1eQKMSlaQaj5-rhu8SHN8k2RzRIX4KQzlAdQUDv4IHxqFLuCVJ8NgWZb75uwg7woTV1X6MpviWYVyr8Ul-Q2jBoiGzCY-SMc12gbB5psZTfd0jsGONwcjcqkNJpgaObN7YQ2cvgbHVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، بریتانیا و ۲۰ کشور دیگر در بیانیه‌ای مشترک تاکید کردند که نهادهای امنیتی جمهوری اسلامی ایران باید به توطئه‌های خود برای ترور، ربودن و آزار و اذیت افراد در اروپا، آمریکای شمالی و استرالیا پایان دهند.
وزارت امور خارجه بریتانیا روز چهارشنبه ۲۰ خرداد اعلام کرد که سازمان اطلاعات سپاه پاسداران، نیروی قدس و وزارت اطلاعات ایران، مخالفان سیاسی، روزنامه‌نگاران و همچنین جوامع و منافع یهودی و اسرائیلی را هدف قرار داده‌اند. این کشورها همچنین حملات منتسب به گروهی موسوم به «حرکت اصحاب الیمین الاسلامیه» را محکوم کردند.
در این بیانیه آمده است: «ما در عزم خود برای محافظت از کشورها و شهروندانمان در برابر این تهدیدات متحد هستیم. جمهوری اسلامی ایران باید فورا این اقدامات را متوقف کند.»
این بیانیه به امضای کشورهای آلبانی، استرالیا، بلژیک، بلغارستان، کانادا، جمهوری چک، دانمارک، استونی، فرانسه، فنلاند، آلمان، ایرلند، لتونی، لیتوانی، هلند، نیوزیلند، مقدونیه شمالی، نروژ، پرتغال و سوئد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76147" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N18zmScyF3AIHI6RX-2swCWpErr5_yQRsNB9JptxVn-cSshSq7H4vwNKAQYG2AL6JNhifW8K-9M6pAuGIExzRIpnJBRwqe-SNT1efZsj5syvm6EquCr7FBfnSfEpCkPvPiHIzwuU6FFUwq9dru18FdWM4yiXg_rOBjJCUBkUELibwlgBtE1hPiL6sI0vtTrl1gussWX8bDmAjGOvU_GojGixZtEjgaKXAxdpzxorIuhLCMLx-Fr8v76pJljeO6atARpJAhZbdDvjELtB2JQk6RjP3BBYNBn6E1ioCd2zo_hWTJ3wELcgR9lgp8hbsYN1xV8YixiNcbxXosIZD7PLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای حکام آژانس بین‌المللی انرژی اتمی روز چهارشنبه قطعنامه‌ای با حمایت آمریکا را تصویب کرد که از ایران می‌خواهد ذخایر باقی‌مانده اورانیوم غنی‌شده خود را اعلام کند و به بازرسان اجازه دهد آنها را راستی‌آزمایی کنند.
به گزارش خبرگزاری رویترز، دیپلمات‌های حاضر در نشست غیرعلنی اعلام کردند که این قطعنامه که از سوی ایالات متحده، بریتانیا، فرانسه و آلمان ارائه شده بود، با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع به تصویب رسید.
به گفته این دیپلمات‌ها، روسیه، چین و نیجر به این قطعنامه رأی مخالف دادند. آنها همچنین افزودند که ونزوئلا اجازه شرکت در رأی‌گیری را نداشت.
هیئت نمایندگی ایران در سازمان ملل و سایر سازمان‌های بین‌المللی در وین در واکنش به تصویب این قطعنامه، آن را «سیاسی» و «عاری از حرفه‌ای‌گری مورد انتظار از یک نهاد فنی» خواند.
در بیانیه این هیئت نمایندگی آمده است که تهران «از حقوق مسلم خود، از جمله در پاسخ به این قطعنامه ناقص، کوتاهی نخواهد کرد.»
تصویب این قطعنامه می‌تواند مذاکرات جاری بین ایران و آمریکا برای رسیدن به توافق صلح را پیچیده‌تر کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76146" target="_blank">📅 18:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kreu5A_rcb3qMmENR4UIpAOTXakZ4bSLra9766jzfc70_dzobq919zXmv0eAUZclJk6rPuFMnOaBxj0HyrWGFfjIfF09CfT8RSMS11us8oTRwh0uX9oyUDBB01Ry9iDJVuzWJs-kaEYmLy4rfL6QtYWYtgrTfy_GECd-P33iHVaDn7Yur62CHuTY0laeWqNeA0hckzTcnZ7OhT_kepNrcWY8ugb68F4xQvSPS4IORpcvFKM7fZX9Gy0FXfmHyjXhVuPsy0QFMJii9bhVHdG4MCre5f6wdwCBf1PwoetlwOuRZgzxcsGol0Jvv8TB1WctXEJ2D9rhct0cquAJSD_XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا در گفتگو با شبکه فاکس‌نیوز اعلام کرد که دلیل سقوط روز دوشنبه بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز، یک پهپاد ایرانی بوده که در بدنه این پرنده نظامی و در فضای میان دو خدمه آن گیر کرده بود.
به گزارش فاکس‌نیوز و به نقل از گفتگوی تلفنی ترامپ با تری اینگست، خبرنگار این شبکه در روز چهارشنبه، این بالگرد آپاچی در ارتفاع پایین در حال پرواز بوده که پهپاد ایرانی بدون منفجر شدن، درون این بالگرد جنگنده گیر می‌کند. بر اساس این گزارش، خلبانان پس از این اتفاق بالگرد را به همراه پهپادی که درون آن بوده، به پایین هدایت کرده و در آب افتاده‌اند.
در پی این حادثه در شامگاه دوشنبه، فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد که «حملات دفاع مشروع» را علیه اهدافی در ایران انجام داده است؛ حملاتی که در ادامه منجر به پاسخ تلافی‌جویانه ایران و هدف قرار گرفتن تأسیسات نظامی آمریکا در سراسر خلیج فارس شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76145" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGMABc0rVJRWEqnkLUJghjjVFj-5AOFnvsTChgvDdUyV-nh1CVsOOPthQ1pnrI39yTPbo2_sjJ_Nzx3J5n4mp3WFNwe9xe3U-j8A5Et_cv8G3AB3gxJmLEJWuiFDw1apPwWbrnFrG_7gtAjyF1EpBPEYBMI1uM321TPk6VN_bcqDaxTWtqy6Tre445Ev_DFCUm5fzwYqC8_dCEX4Mp5TiTD5d6dfqWbqxCM6RZVgDku-AAd8W1aGyCiScOpy8NUTvuZNwYrptEv46BpudRKSNpY0wsM2Gb76AGErK01cpQz2Sj4-7kzDOGxDKnLc2Q_lZKFbEVMKvAL9gdeKdXjX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های مختلف به نقل از دیپلمات‌ها از سفر یک گروه مذاکره کننده قطری به تهران در روز چهارشنبه برای رسیدگی به اختلافات باقی‌مانده بین ایالات متحده و ایران خبر دادند.
خبرگزاری فرانسه به نقل از دیپلماتی آگاه به این سفر نوشت که این گروه مذاکره کننده قطری «پس از مشورت با ایالات متحده» به تهران سفر کرده تا در دیدار با مقام‌های ایران «شکاف‌های باقی‌مانده را پر کنند.»
از زمان آتش‌بس میان ایران و آمریکا و اسرائیل، پاکستان به عنوان میانجی اصلی مذاکرات صلح میان ایران و آمریکا را هدایت می‌کرد اما در هفته‌های اخیر قطر نیز به عنوان میانجی دیگر تلاش کرده تا امکان برقرای تفاهمی میان ایران و آمریکا را فراهم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76144" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwA_f42SKxEg8XZjvylwoMbcjKHxE5yWkIjuaj6ZwN5EODUXGxH4EYbYRIwBwIB2hoOqFpk-e-whNVwtIU9DeUFP8kwdt2J-rd3sjtH41F3MQVvlF-hkcQ-O6SAHJ_ycg_Ub-ySI5lzSumxbfrNuFwcOBvTncTcoDGX_MQSJzh_pa4gd2BgXIeXaJq09YmopeJQCP0oinEep9fe3gQyirWPVfMPn724PbM9FsSBxwU16somguMB1aNtJEbdzlMnml66LUiUgVFU_t6XgXbKyLHqXGEyHRCKyctZFnxbtzwcfszdyd7Qao6CGRqufJilHquQut74ORHPCtBqAVpo61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ممکن است به‌زودی دستور حمله به نیروگاه‌ها و پل‌ها در ایران را صادر کنم
دونالد ترامپ، رییس‌جمهوری آمریکا، در مصاحبه با فاکس‌نیوز گفت ممکن است به‌زودی دستور حملات جدید به نیروگاه‌ها و پل‌ها در ایران را صادر کند.
او دلیل این موضوع را طولانی شدن روند مذاکرات از سوی جمهوری اسلامی عنوان کرد و افزود تهران دستیابی به توافق را بیش از حد به تاخیر انداخته است.
ترامپ تاکید کرد صدور دستور حملات جدید نزدیک است و گفت اگر روند مذاکرات تغییر نکند، تصمیم‌های تازه‌ای اتخاذ خواهد شد. او افزود ۵۵ درصد از سامانه‌های راداری که جمهوری اسلامی در دوران آتش‌بس بازسازی کرده بود، در حملات جدید آمریکا نابود شد.
🔻
دونالد ترامپ: محاصره دریایی جمهوری اسلامی، یک دیوار فولادی است
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروت سوشال، محاصره دریایی بنادر جنوبی ایران را کارآمد خواند و آن را به یک «دیوار فولادی» تشبیه کرد.
در این پیام آمده است: «رسانه‌های جعلی از گزارش میزان اثربخشی محاصره دریایی آمریکا خودداری می‌کنند. این موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است.»
رییس‌جمهوری آمریکا ادامه داد: «ایران هیچ داد و ستدی انجام نمی‌دهد، به نیروهای نظامی خود حقوق نمی‌دهد، بدهی‌هایش را تسویه نمی‌کند و به‌سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است.»
🔻
ترامپ: حمله بامداد چهارشنبه جمهوری اسلامی به بالگرد آپاچی ناکام ماند
دونالد ترامپ، رییس‌جمهوری آمریکا، در مصاحبه با فاکس‌نیوز گفت در حمله بامداد چهارشنبه جمهوری اسلامی، یک پهپاد ایرانی به یک بالگرد آپاچی اصابت کرد اما منفجر نشد.
او افزود این پهپاد میان دو خلبان گیر کرد و با وجود برخورد، انفجاری رخ نداد.
ترامپ گفت خلبانان بالگرد را در دریا فرود آوردند و برای نخستین بار در تاریخ نظامی آمریکا، به وسیله یک شناور دریایی بدون سرنشین نجات پیدا کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76143" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqcBzy0zzfzbTclNlkLBK6RJxS8r7hGT7tpYUXHcuGKKzPIt0AuhuVNHDuaQXtWBkCAL2fH9cszjDJFS05gRATPPr1GAuhGdmLJni-2TFF0A8pOgLP-1_IqmCBFFwBAQWs2vxhTCcq6rkO69nyD5dwKp16sTO46pb-J1mNc6kK6fHKw2mgAuHezDyrg_f6om9hOlXd0dq2xqziYLAv6pg-2vy7MIsxVuWBg6HaMZbmr6LLvv8jwhOyYXDNPYMBSy7euC2lTz8Ny98EF_Fgl62-eXGSHG5BiJ31mdnOMdq2U1BJt4-BsGpV1apShbMcnwonHPY2imNns2CGBOJ0V9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a780747f7a.mp4?token=sa-aVqEG01u33A0G5tQI4gXTPqvz1tLz55p9AFmTE51pupGoWEDJCjQNt61GUmBS_YRDbkdNngz_mwMEUgxBtDFs6gBaJfRqMI6-_0mZAnHVxdqr3UJBep8YmUT4l8YG-62mGj44jQu5ENLTvNzvPVeDU0ezGQTEGiOCO0dc4gG70yUmCEKOBZ66kY0rSXj4ZzMK6FdNP34OPPRnWm3Uv09CnJTzCGIpNXPE098tDsN7NN1EuI0ZLYcpS17v_ADxMgaj5NxPsDSG8pwNXqFtNfXHhjrMKhgHfBpsM3sZDGVrfhIN0yr_aIlFfKZ0_cYQYK3kV7WCaoenJ7YM2D52ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a780747f7a.mp4?token=sa-aVqEG01u33A0G5tQI4gXTPqvz1tLz55p9AFmTE51pupGoWEDJCjQNt61GUmBS_YRDbkdNngz_mwMEUgxBtDFs6gBaJfRqMI6-_0mZAnHVxdqr3UJBep8YmUT4l8YG-62mGj44jQu5ENLTvNzvPVeDU0ezGQTEGiOCO0dc4gG70yUmCEKOBZ66kY0rSXj4ZzMK6FdNP34OPPRnWm3Uv09CnJTzCGIpNXPE098tDsN7NN1EuI0ZLYcpS17v_ADxMgaj5NxPsDSG8pwNXqFtNfXHhjrMKhgHfBpsM3sZDGVrfhIN0yr_aIlFfKZ0_cYQYK3kV7WCaoenJ7YM2D52ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل ظهر چهارشنبه ۲۰ خردادماه، ساعاتی پس از صدور هشدار تخلیه برای ساکنان شهر صور و مناطق اطراف آن، این شهر در جنوب لبنان را بمباران کرد.
@
VahidOOnLine
بنیامین نتانیاهو در واکنش به محکومیت حملات اسرائیل در منطقه از سوی رجب طیب اردوغان در بیانیه‌ای گفت: دولت اسرائیل و ارتش اسرائیل، که اخلاقی‌ترین ارتش جهان است، به اقدام قاطع علیه ایران و نیروهای نیابتی آن که خاورمیانه و سراسر جهان را تهدید می‌کنند، ادامه خواهند داد.
نخست‌وزیر اسرائیل در این بیانیه گفت: دیکتاتور یهودستیز اردوغان که در حال نسل‌کشی علیه کردهاست، از سازمان «تروریستی» حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی را زندانی می‌کند، آخرین کسی است که می‌تواند برای اسرائیل موعظه اخلاقی کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76141" target="_blank">📅 17:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۲۰ خرداد گفت که ایران برای رسیدن به توافقی که می‌توانست برایش بسیار خوب باشد بیش از حد تعلل کرد و حالا باید بهای آن را بپردازد.
دونالد ترامپ در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «ارتش ایران کاملاً در وضعیت آشفته‌ای قرار دارد. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی، عملاً دیگر وجود ندارد؛ آن‌ها کاملاً شکست خورده‌اند».
او افزود: «ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!!! آن‌ها برای رسیدن به توافقی که می‌توانست برایشان بسیار خوب باشد بیش از حد تعلل کردند و حالا باید بهای آن را بپردازند!!!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76139" target="_blank">📅 17:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9GeOZMgdX6rIDoMn3QjsG5nfZRXRQpR9n_iIBHRZdMIcla3NNXYoLG_It5_c_INlIEjN5HS8TKGd-H8vnhCELq4lJYNYufmnciRUVerj2UuRE-SpVE_gOdLMwSWHDZEbd_oscjzUQ0WOUL_cXWBNC-FQA_uA7bLWjWsWehNqaHz3SusYnraACyWuKcsyabGZKlTYxA66unfL4n8fCJKaFFlfkKAAcFxFDnMZAlUG0EdFAMdkeLJlaUYQKsC-0sDRZMfW6H7b4K_wwwZ46cjr3OOcODJe2W46AXdfHBR2-SXZvRDGZjJf_qf8DqIVZr2p0zRev8A-9BR9B7vu6j-7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه ایران درباره تأثیر درگیری‌های نظامی اخیر بر مذاکرات با آمریکا گفت ««باید بررسی شود، دیپلماسی و میدان دو امر جدا از هم نبوده و در امتداد و عرض یکدیگر» هستند.
اسماعیل بقائی روز چهارشنبه ۲۰ خرداد دربارهٔ آخرین وضعیت مذاکرات هم گفت: «با توجه به تحولات دیشب باید بررسی کنیم. روند دیپلماتیک در خلأ اتفاق نمی‌افتد و برای پیشبرد هر فرایند دیپلماتیکی نیازمند فضای حداقلی هستید تا بتوان روند جاری را پیش برد.»
شب گذشته ارتش ایالات متحده، در واکنش به سرنگونی یک بالگرد آمریکایی در سواحل عمان، حملاتی را به جنوب ایران انجام داد و ایران نیز در واکنش به شلیک موشک به برخی کشورهای منطقه اقدام کرد.
دونالد ترامپ که پیشتر بارها از نزدیک بودن توافق خبر داده بود، هنگام انجام عملیات آمریکا در جنوب ایران گفت: «ما توافقی بسیار خوب داشتیم و احتمالاً همچنان خواهیم داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76138" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th_dYeFm2GZe6Ar3NbtUcCzQyeXDtjOi0IFs4mlio9Dfoy9SLseIugkZTZxMDJhR7p50OshDVPpy6XK9geHfck9HsOuL_5NCCYjHcRxy-BuYgSrzjzU6-NqDZJhrjUMtudGC7dOW86ZOuqX8iqg9XlzJp9QMsNr7pAFRggIeplSFfLMt2qdZM11EhkQXB94UTYdaR3O9GnAW9FG8KgG_oSWrajUdXlBWOLazTJtTo8xjhdvEM7OuOzRTupk73SWBAkdm5rmI4SoVi-LgfdTHeO9BIEsxGL4TYMmMhI3GXp0Fa6CeEL8Auw7aR5YCdRIvEX8GNryMOpA2IFlPmCLlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه، حملات موشکی و پهپادی جمهوری اسلامی به بحرین، کویت و اردن را به‌شدت محکوم کرد.
وزارت خارجه امارات در بیانیه‌ای این حملات را «تروریستی» و «بی‌دلیل» خواند و اعلام کرد که هدف قرار دادن پادشاهی بحرین، دولت کویت و پادشاهی اردن هاشمی، نقض آشکار حاکمیت این سه کشور و تهدیدی علیه امنیت و ثبات آن‌هاست.
در این بیانیه همچنین آمده است که امارات همبستگی کامل خود را با بحرین، کویت و اردن اعلام می‌کند و از همه اقداماتی که این کشورها برای حفاظت از امنیت و ثبات خود انجام دهند، حمایت می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76137" target="_blank">📅 17:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/leFD0sTkHF5uqxIV13-T6ty78B8UCosJFRjrsCs3XEYUHy3MJKNIxsCLwvfN87dCZRz69PBhiJ9mYesbFVRQIS9Wndf8q9kmXDocv7G89paRZvnq3XeBbZ8Ac2Z80HDVGtiuYhp_pNf-lOP5lngYHDkX5MAIafr_HVQvOVema7q1TOlHnEH8poEpsnAJJguswnSnnnGOHL8RKiTScR2D_CM-6BYP9DvKWLMeCRmvajU0gkBcpUK_AR49bB_Bc-l9BmWqD3aKVovDfkdyYGtm5aquGeKr95p6jQvpFO79PxkP_2tsuBcYT8rY0KtlX92PwnWcnf60gQKoz2tT3kfHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bY6Kut-oFhHLhmBugT9gcgCN-ap5YJQ0iaJ0sI3urdiYcDagQUtFOAIRdJVdbgua2jpR9z5OdnuLMczOsdXCE1NM1dFaXiBQv5il-ccEa-5p_63wizu1SHIMRoQ8ovYp0FJDYH48UdZte_Gq9TKTnS2SGMpk47j286CQqGfEr9wUCrBdS0eCtq-MRegSh9DV4sBFiy0k3WY1RYUvXb0t7ptkTn5xDOLQGs8GWPJm6c4t7UjTIdIhGjPUQ72Emo2fM_eGQfU1PzTEOQHCsEOm3BY2jBZExcmNTNQciTM3JlNY1lJX4DchuNKCKbCBSMVpAWV5oji0l40rlVCIrKlV8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انجمن اسلامی دانشجویان دانشگاه صنعتی شریف با صدور اطلاعیه ‌ای از اعمال نخستین حکم اخراج یک دانشجو توسط شورای انضباطی این دانشگاه خبر داد.
به این ترتیب، رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر، به اخراج و محرومیت از تحصیل در تمام دانشگاه‌ها به مدت چهار سال محکوم شده است.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف اعلام کرد که آقای دالمن با وجود تبرئه از سوی دستگاه قضایی، از سوی شورای انضباطی دانشگاه با این حکم سنگین روبه‌رو شده است.
این انجمن یادآور شد که حکم اخراج دانشجوی فوق برای تأیید به وزارت علوم ارسال و در روزهای اخیر نیز حداقل برای یک دانشجوی دیگر نیز حکم «بدوی اخراج» صادر شده است.
رضا دالمن، در ۲۸ اسفند سال ۱۴۰۴ و در اوج جنگ ۴۰ روزه از سوی نهادهای امنیتی بازداشت و پس از یک ماه با قرار وثیقه آزاد شده بود.
@
VahidHeadline
پیش‌تر گزارش‌هایی منتشر شده بود که یکی از دلایل بازداشت او، آویختن یک عروسک موش از درختی در محوطه دانشگاه عنوان شده بود؛ اقدامی که در فضای اعتراضی آن زمان، با اشاره به لقبی که برخی معترضان برای علی خامنه‌ای به‌کار می‌بردند، انجام شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76135" target="_blank">📅 17:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GunFOvYVoJuOrQbEBCfaOorktEB1h65tQbVhio-3mCQp-bq5lQ_LKSEqpagDnbL0CIX-n7y7Pef6soxwFMIwEfFeTSNykBMtdNX9-jWYko51bL9PHeBUbkMw2br2COBwYpLEL81lXByu8yiq9SY9VnslV6I4mSiY5tsmehdJ_kQsyspWRKv-wzsAH8TjDJoeQEH7mDBuXBSosrveP20-2OdsasREkgldaNqc-s6iR4Om8YwBlJYXvpsmEeFy8zL7wPQ-ZpbbLYxJ6hLH9uIomk1kdYLrQtAVistPc47dIF_mq0dLEjCkrYbe_S4aiuG3aB1UMtsNd86RWLl6HxlCqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی روز چهارشنبه ۲۰ خرداد خبر داد که صادق زیباکلام، استاد سابق دانشگاه تهران و فعال سیاسی، بازداشت شده است.
خبرگزاری میزان، وابسته به دستگاه قضائی ایران، اعلام کرد که «قرار نظارت قضائی» بر آقای زیباکلام روز ۱۷ خرداد تشدید شده بود و به دلیل انجام مصاحبه‌ای جدید، علیه او اعلام جرم و سپس صبح امروز بازداشت شد.
اعلام جرم روز ۱۷ خرداد در پی انتشار مصاحبه صادق زیباکلام با شبکه بریتانیایی «کانال ۴» رخ داد.
این فعال و تحلیلگر سیاسی در این گفت‌وگو به زبان انگلیسی، علی خامنه‌ای، رهبر سابق جمهوری اسلامی، را «ستون فقرات تندروها» در ایران خواند و گفت او در طول مدت رهبری خود به مدت ۳۶ سال ایده‌هایی مانند «آمریکاستیزی، نابودی اسرائیل، حمایت از حماس و حزب‌الله» داشت.
زیباکلام درباره مجتبی خامنه‌ای، رهبر جدید، نیز گفت تردید دارد او ایده‌های پدرش را داشته باشد و همچنین اعلام کرد که او نمی‌تواند قدرت و جایگاه رهبر سابق جمهوری اسلامی را به دست بیاورد.
او در اردیبهشت ۱۴۰۳ در پی تشکیل سه پرونده قضائی بازداشت شده بود و تیر ماه همان سال به دلیل «ابتلا به بیماری سرطان» از زندان آزاد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76134" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSFPbFlyMMpHmPFh7PJjXzJHarsZSXrXsr6SIBMzau6eVkUYg4W4lsALKRfk7x6UqrRwBFbx7HhjzQGoabYmEQJq1WGFa7Ik8qBWRrHoey-56IvSPuKgx13PkPRwTFXq-wB0dwVB8seYQQHhJ1PiTlN9XIMve_gSoQukkIb5vsBoXsfe_qlies8t7NWoU7VSySUrladfzyqmkdT1vcw3L2vVYprbwWG-CP7_6KoSlxDHtURTD8ygGuRF8EYJTAttmJ8hdhMhzGaoY4kBevm2SLFE130wFmiQjB17vZBEcZVarBiypUFAkOTgfPIellGldzdrBs6Y51dalEhi8tOQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
«از آغاز سال ۲۰۲۶، بنیاد عبدالرحمن برومند دست‌کم ۷۱۱ مورد اعدام را در ایران ثبت کرده است. این آمار شامل دست‌کم ۶۶ مورد اعدام در ماه مه و ۱۸ مورد تنها در نه روز اول ماه جون است.
‏
@IranRights</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76133" target="_blank">📅 17:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=qP6vQRRPWMcH7i_qHtlBoT0owjIzNMbO7hBlmrrQHt9vfvKz74LVRJLRe8vKNQ9E5qZ0IVxBt3N3zfP0lc9pYsSaZuAUhojbb5WA7uFynbzliqOlDA2dZ41Xltk4QALybvBhWdnqEQYq_N7eHtPrDGf8cFnfg9IdqF26JMxYMEf_BdYalsDLcadYHpr9QnAGbW_nPbwHf8PWDGtLwa3i9iBlBG_-Hrc5jfE0Svlwj4m3M1PXeHbRuWKlC_VkiOWiNPJ1u51T9Brb7NUCVnLtSlZebisv7deJVQjz4TkGKjZKmuGOW_c3YiZZ4wfpqpRlCmoAvCSBTzrQVbhnWDWOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=qP6vQRRPWMcH7i_qHtlBoT0owjIzNMbO7hBlmrrQHt9vfvKz74LVRJLRe8vKNQ9E5qZ0IVxBt3N3zfP0lc9pYsSaZuAUhojbb5WA7uFynbzliqOlDA2dZ41Xltk4QALybvBhWdnqEQYq_N7eHtPrDGf8cFnfg9IdqF26JMxYMEf_BdYalsDLcadYHpr9QnAGbW_nPbwHf8PWDGtLwa3i9iBlBG_-Hrc5jfE0Svlwj4m3M1PXeHbRuWKlC_VkiOWiNPJ1u51T9Brb7NUCVnLtSlZebisv7deJVQjz4TkGKjZKmuGOW_c3YiZZ4wfpqpRlCmoAvCSBTzrQVbhnWDWOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
realDonaldTrump
چت‌جی‌پی‌تی:
ترامپ سکانسی از سریال معروف سیاسی The West Wing منتشر کرده است؛ سکانسی که برای مخاطب آمریکایی معنای کاملاً مشخصی دارد.
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
با این حال یک نکته مهم در خود سریال وجود دارد: بارتلت در نهایت توسط مشاورانش از واکنش نامتناسب بازداشته می‌شود و به پاسخ محدود تن می‌دهد. بنابراین ترامپ با انتشار این بخش، بیش از آنکه کل پیام سریال را بازگو کند، بخش خشم‌آلود و بازدارنده آن را برجسته کرده است؛ پیامی برای تهران، و همزمان برای مخاطب داخلی آمریکا: «فعلاً محدود زدیم، اما گزینه بزرگ‌تر هنوز روی میز است.»
گراک:
**این سکانس از سریال تلویزیونی «The West Wing» (نام فارسی: بال غربی یا اتاق بیضی) است.**
دقیقاً فصل اول، قسمت سوم با عنوان **«A Proportional Response»** (پاسخ متناسب).
### زمینه داستان چیست؟
این صحنه ادامه مستقیم قسمت قبلی (قسمت دوم فصل اول به نام «Post Hoc, Ergo Propter Hoc») است. در قسمت قبل، یک هواپیمای آمریکایی که دوست شخصی رئیس‌جمهور **جوزایا بارتلت** (با بازی مارتین شین) داخل آن بود، توسط نیروهای سوری سرنگون می‌شود و چند آمریکایی (از جمله دوست رئیس‌جمهور) کشته می‌شوند.
رئیس‌جمهور بارتلت که معمولاً آدم آرام، باهوش و اخلاق‌گرایی است، این بار بسیار عصبانی و دنبال انتقام شخصی است. او در اتاق وضعیت کاخ سفید (Situation Room) با دریاسالار **فیتزوالاس** و مشاوران نظامی‌اش جلسه دارد.
### معنی و مفهوم مکالمه چیست؟
نظامی‌ها گزینه‌ای به نام **«پاسخ متناسب» (Proportional Response)** پیشنهاد می‌کنند. یعنی:
- سوریه (یا نیروهای مورد حمایت آن) یک هواپیما را زده → ما هم چند هدف نظامی محدود مثل انبار مهمات، پل راه‌آهن و ساختمان اطلاعاتی‌شان را بزنیم.
- این کار «عادلانه» و «متناسب» با خسارت واردشده به نظر می‌رسد و جلوی escalation (تشدید درگیری) را می‌گیرد.
**رئیس‌جمهور بارتلت** اما این منطق را قبول ندارد و با عصبانیت می‌پرسد:
> «فضیلت پاسخ متناسب چیست؟ چرا خوب است؟
> آنها یک هواپیما را زدند، ما یک فرستنده را می‌زنیم؟ این پاسخ متناسب است؟»
او استدلال می‌کند که:
- دشمن دقیقاً می‌داند ما چه کار می‌کنیم (چون همیشه همین کار را کرده‌ایم).
- بنابراین اهداف را از قبل تخلیه می‌کنند (مثل همان انبارها و پل‌هایی که سه روز است خالی هستند).
- نتیجه؟ پاسخ ما بی‌اثر می‌شود و دشمن جری‌تر می‌شود.
بارتلت می‌خواهد **«پاسخ نامتناسب» (Disproportional Response)** بدهد:
> «اگر یک آمریکایی را بکشید، هر آمریکایی، ما با پاسخ متناسب برنمی‌گردیم.
> ما با فاجعه کامل برمی‌گردیم.»
یعنی ضربه‌ای آن‌قدر سنگین و غافلگیرکننده بزنیم که دشمن برای همیشه بترسد و دیگر جرأت حمله نکند.
### در نهایت چه اتفاقی می‌افتد؟
وقتی نظامی‌ها گزینه شدیدتر را پیشنهاد می‌کنند (بمباران فرودگاه که هزاران کشته غیرنظامی دارد)، بارتلت عقب‌نشینی می‌کند و همان پاسخ متناسب اولیه را انتخاب می‌کند. این نشان‌دهندهٔ تعارض درونی اوست:
- از یک طرف خشم و احساسات شخصی (چون دوستش کشته شده).
- از طرف دیگر مسئولیت ریاست‌جمهوری و ترس از کشتن بی‌گناهان و شروع جنگ بزرگ‌تر.
### چرا این صحنه این‌قدر معروف و مهم است؟
- نوشتهٔ **آرون سورکین** (نویسندهٔ نابغهٔ سریال) است و دیالوگ‌هایش بسیار قوی و فلسفی هستند.
- نشان‌دهندهٔ یکی از تم‌های اصلی سریال است: تعارض بین **ایده‌آلیسم** و **واقع‌گرایی** در قدرت.
- مارتین شین در این صحنه بازی فوق‌العاده‌ای دارد و عصبانیت، ناامیدی و در نهایت پختگی بارتلت را به زیبایی نشان می‌دهد.
- خیلی‌ها این صحنه را نمادی از سیاست خارجی آمریکا می‌دانند: آیا همیشه باید «متناسب» پاسخ داد یا گاهی باید قاطع و بازدارنده عمل کرد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76132" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URVcU2Nf8q7odjiUvwp5RQofCIoWG9msLx2tbP3IDI7o9xpbpxUFQdFWUuFj1l8vz2Md4GV2QLmH9hBjGdC26VRvq9lsZUCsALZKTFjVlKqpU6ZDqaT4csr5JjifXxe6mDXXrGhVzPk_vcsAlxg1dEH0wstMLgUzLAkHU_a-MuR9APbeYp67yP_PKS4OASbyAm5vt1g-rClvVN-nfRDWk4C4gJLmIviJWspKq19Y3ci7bWVfW2OBKN5DoWfF9qoib1xVrVR7T5qc1tOXuz-iYGaep_q7vOjIs9-ga_wX2IVlRzP_vvE6KNfdxbeNtD26iP6X5yGMikSp5P2_huqItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درحالی که سپاه پاسداران ادعا می‌کند ۲۱ پایگاه آمریکا را در منطقه هدف قرار داده است، نیویورک‌تایمز صبح چهارشنبه به نقل از یک مقام آمریکایی نوشت که برآورد‌های اولیه حاکی از آن است که تقریبا همه حمله‌های ایران رهگیری شده و هیچ گزارشی از خسارت به پایگاه‌های آمریکا یا تلفات نیروها مخابره نشده است.
یک مقام آمریکایی دیگر نیز به نیویورک‌تایمز گفته، ادعای سپاه درباره حمله به پایگاه‌های آمریکایی صحت ندارد. هنوز مقامات سنتکام به‌طور رسمی در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/76131" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-ZIHVIlS09Qw_Re5cs_QgWGwMCR5R5sFkn66GOp4O3Z6IyL_F6_1uUKi12VD2O59uVl0w_n4955VlDyCeHew5D0jOkj8ATY8t2c55UTncgn5eqqyWM47Sbib-mk6rfSGbpKWVM3wrjyeRZUj3dL9E4jfDpp4UoEh8DJBrfodKA50n2214fuvy8xqsRnGsDMZ2Wm1c6-HAfXr4MBmWgivPMxd9xS4_mNGw5V93MXwWIbs1vAdxkJ1o_7HjGpzQLPJnmsgDrIg7UzI3miLjD1XRpuzAqnl6mLvgD16P_wRxBQ4gbcUnXxHXQO0Eid1W_GryS6BHqQEPXebxvNK2aeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش ایران و سپاه پاسداران اعلام کردند که «با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین هدف قرار» دادند. همچنین گزارش‌هایی از حملات سپاه و ارتش به پایگاه‌های آمریکا در اردن و کویت منتشر شده است.
ارتش ایران می‌گوید این حملات را «اقدامی متقابل» در پی «مزاحمت‌های» آمریکا برای ساکنان جنوب ایران خوانده است.
خبرگزاری فارس گزارش کرده که سپاه پاسداران به پایگاه ارتش آمریکا در اردن حمله موشکی کرده است.
سپاه پاسداران گفته که با «موشک‌های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه‌های جنگنده‌های اف‌۳۵ در پایگاه هوایی و مرکز فرمانده کنترل ارتش» آمریکا در الازرق اردن را مورد هدف قرار داده است.»
باراک راوید، گزارشگر اکسیوس به نقل ازمقامات آمریکایی می‌گوید که دست‌کم ۴ موشک بالستیک و چندین پهپاد به سوی پایگاه‌های آمریکا در بحرین،‌ کویت و اردن شلیک شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76130" target="_blank">📅 05:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1XKSmHohoQMr_aBtoue5UKlk5yMD6XbvmIAqO09Us-LU_h7PKEtu8R-hDeLNCyUk44TWXsdIEUjLIaHQ40si-7reQLCIWmpIGOIy4sXTA0k5-UkgKL8IQlHlVaxycVSHJ8jeQWpwBrFUj-YfLBRvgNd4or4NSYOH5U_KInMmjp8cC58cksS31S27v7SRmJp9pY7r0rUxVjr3B4zqpjxFeO0ZMukKVptcpu45oyzy3C9qpcFV7aWwgJ945QfoVyshMpxaXjDgryd6LTQd1M0Llg5nlADl4zZt0zERSiFmH7TbWzObwGRWqSLD_S1FMXp6hijFRWnolFjKY7STOayfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه از حمله به ۲۱ هدف در پایگاه‌های آمریکا در منطقه خبر داد و گفت نیروی هوافضای سپاه با موشک‌های سوخت جامد دوربرد، چهار «هدف مهم»، از جمله آشیانه‌های جنگنده‌های اف-۳۵ در پایگاه هوایی و مرکز فرماندهی و کنترل ارتش آمریکا در الازرق اردن را هدف قرار داد و منهدم کرد.
@
VahidOOnLine
توییت اکانت وزارت کشور بحرین، ترجمه ماشین:
آژیر هشدار به صدا درآمده است. از شهروندان و افراد مقیم درخواست می‌شود آرامش خود را حفظ کنند، به نزدیک‌ترین مکان امن بروند و اخبار را از طریق کانال‌های رسمی دنبال کنند.
moi_bahrain
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76129" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/luGSRZlaU1hv53Y8eVuGNoUeSzR1ZygeyhVaF1HYW4KZwH_lCnhmkIy7QV6wKv-qJNTbz5Hl_ZzZiNcyv-hHwaIccoWF9ZRLses6WVVP-IiFjE1EGuYb6m-Tpa8mhAZJduQRvYqLYAzzoMVgndy-RUbWIU6BI0N5kl0KgKnHRLCUZgUQx3gR9f8dQGm9MxwiPduTNVeWGsZgM5FU4_6iTnkK9TpKF5Tb7DGTB3DhhRmmdf63cF2Y8ADJAzEPapkw8Rv_ZaVAEM-bHrSdvik8ZpXDAbzHHruXg4DG-WOrT3931kEx9JOlHbSfu3hdS42t5SIOz_AA4ff3ZfyWPQ9GNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس‌ نیوز، جنیفر گریفین می‌گوید که یک مقام ارشد آمریکایی به او گفت که سه‌شنبه شب به وقت واشنگتن ۲۰ هدف در داخل ایران هدف قرار گرفت. این مقام گفت اگرچه حملات آمریکا به گفته سنتکام پایان یافته است، ارتش آمریکا آماده است تا در صورت تصمیم جمهوری اسلامی برای تلافی، واکنش نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76128" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSkUow1LlDjZoyWnbp84IM474_PYMf74XQy6cqUTveeL58ojjxNDmlv-YVKXBxqCGeBA988uOtAH25T4fwLLksD1o0_wToY33awBTRubrwOYZssEw9wv53zykmUmWB62yeIa8lfk4gDauFPes24XEHZ6XjKo9CYfh6duan06fEDuxZunD7L64aCRu7FMfn-2rO-3NMEFoZt4XCP0lD8e7LgfByZx9WsxMI8Z7DBt4ODPsUGzVf7NIk2GP4KeKfEgcj3OylpvB-ix7pT_aSqOJeaLH6lJ_UeLVoWHJyksGb0qGySu1q0CKAWRJmtX0ek1V7sv3qzFplueSZLS5KSqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا اعلام کرد ارتش و سپاه در پاسخ به حمله‌های جدید آمریکا علیه جمهوری اسلامی، برخی از پایگاه‌های آمریکا در منطقه هدف حمله‌های قرار دادند.
این قرارگاه تاکید کرد در صورت تکرار حملات آمریکا، جمهوری اسلامی «حملات سهمگین و گسترده‌تری» علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76127" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=oZOmv-eKtG7APn2hNYp_0ktpzEZIN2Pvo5kjxfOQ6d_9LttoHlbykIetea7Pwh4u2E559mEqlFoJOl064Xj2O07D0er_QV-eFawfRhvGxEvLqYhSNYmGCFYtaeGKhJ3wQOT1UK8p7YmlCXtnDDLMkQ00WUEXE1FipXKRcupVIE7RuLFEG9Y5-gijib4JPxXOAJPY6dkM0-q_qwziKfjAd6TZYCoF1xN4X3afUfIKmchXqxYJXCEWT2sZYxJHihg3oJjblOfwkn-jPmHJ7y23M1N_nxArAAKvGwSODWBhHc76oQcHSZbzrD8-RLBKf7CH_3BsCa0dloQTttkM9zHLkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=oZOmv-eKtG7APn2hNYp_0ktpzEZIN2Pvo5kjxfOQ6d_9LttoHlbykIetea7Pwh4u2E559mEqlFoJOl064Xj2O07D0er_QV-eFawfRhvGxEvLqYhSNYmGCFYtaeGKhJ3wQOT1UK8p7YmlCXtnDDLMkQ00WUEXE1FipXKRcupVIE7RuLFEG9Y5-gijib4JPxXOAJPY6dkM0-q_qwziKfjAd6TZYCoF1xN4X3afUfIKmchXqxYJXCEWT2sZYxJHihg3oJjblOfwkn-jPmHJ7y23M1N_nxArAAKvGwSODWBhHc76oQcHSZbzrD8-RLBKf7CH_3BsCa0dloQTttkM9zHLkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید  ساعت ۴و۳۶ دقیقه
خمین ۳ تا موشک پرتاب شد
همین الان پنج تا موشک از خمین شلیک شد ساعت ۴:۳۵
سلام وحید جان  همین الان ازنا لرستان زدن
ساعت4:37
ساعت ۴:۳۵ از خمین چهارتا موشک زدن
از خمین حدود ۴ تا موشک فرستادنننن همین الان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76126" target="_blank">📅 04:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hEdhfaEHKpA6KbO7q21qAiFB2DFtGmCw-GQXs_SfiCzoV6D8EB63YxKhfeJqYpe_s5e7dd_HnDeA_4xa_TiIJjZTsgH7KDfvqVWwx-1J3vKdoXbhsHxU_PX53q_rnVZEkaii2dReca9-jY02kMssJgm_63DWxFgpWITXN2pe-OCGnWoabuCAPbUIvr4iR7HSW7QlfxPt7zhNlmgpB6-aPRfYjdvSkaCh4sRyZtNQotXyTxvzzzlMJfH0FiXCweQx3rRSva1eSTIjfsFe46tr0ecMmSach3GWF92qsQgVM4JOuULZ7fCm_QffZ3w-UIPO5tzr57JAm3nGF227tx9U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا حملات خود را در پاسخ به حمله ایران به آپاچی تکمیل کرد
"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده، سنتکام، روز ۹ ژوئن به دستور فرمانده کل قوا، حملات دفاعی خود علیه ایران را در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته تکمیل کردند.
نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق شلیک‌شده از جنگنده‌های نیروی هوایی و نیروی دریایی آمریکا، سامانه‌های پدافند هوایی ایران، ایستگاه‌های کنترل زمینی و سایت‌های راداری نظارتی در نزدیکی تنگه هرمز را هدف قرار دادند.
این عملیات پاسخی متناسب به حملات اخیر علیه نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه بود.
نیروهای آمریکایی همچنان هوشیار و در موضع آمادگی برای دفاع در برابر تجاوزات توجیه‌ناپذیر ایران باقی می‌مانند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76125" target="_blank">📅 04:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه:
"
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76124" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
