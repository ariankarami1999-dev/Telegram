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
<img src="https://cdn4.telesco.pe/file/QmPwEQcZpIpNjiA4Jg0SjR6nSDK5YtWhw42C3PCaPhKURtkzmQQ16r5pT8m0xU92vGDFyHMxcFhBypBtkr_TIxPpjU9FJpgKGdZX8ldtAVXMAay1bmTyf0Qea0SemQu997j-1q5rz1-L6rNXQmTTmjS9lLHlhQv15sLn_FzFXkqok1b5rYX8ZEYKNn7z4GLLvO4L561KfP5KOtAzNxsxKPYNNo04W97c9QGJA9iko59nWryIu5fmpTrEo_O173ZnrOqvsKyjKT9yJb8QKOCt0uTg_lpGL3icwPtRrlZXO9xDLdijRMVOrOaMvSkAGTcTX_esvYUyyVVtHH1dLgneRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-440546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/farsna/440546" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حزب‌الله: تجمع سربازان دشمن اسرائیلی در مجاورت قلعۀ تاریخی بوفورت با موشک و توپخانه هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/440545" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNwZefe4BiSgvBhrdcCe3LVmDdMXtIhDjbCdCEAETdxp-IlEXJ7nQVO9qr_voIu89MmB6kV_4VsxAn26huR6JVZwhwn7DxrvSHADQgjBp6uU0xjqIo8-TrlsZZ6jWTp3Y_nFHEede-oixXVmGnkhMIwJmRKl8aP196P82RPBBI1dDYGm5Dwx5STDuer7xSjJQUeLuTNxPMSvxBi865SZnC0_P9mP1uG6-y-oJMtIPLmpOotkAkL0mrUT7PEVHFLH2RZWju8GreuObuZw98f9adbeC7KXiPUEJzzCnYLH_pzRjtorsNUOza1zPoNtfeyCLOmNUQGsZWJJfAlo8LWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌های تلفنی عراقچی با وزرای خارجه انگلیس و ترکیه و عاصم منیر
🔹
سید عباس عراقچی وزیر امور خارجه در تماس‌های تلفنی جداگانه با ایوِت کوپر، هاکان فیدان، وزرای امور خارجه انگلیس و ترکیه و فیلد مارشال عاصم منیر فرمانده ارتش پاکستان در خصوص آخرین تحولات منطقه‌ای در پی پاسخ ایران به نقض مکرر آتش‌بس در لبنان توسط رژیم صهیونیستی گفتگو کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/440544" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زنده خبرنگار بی
‌
بی
‌
سی از بیروت؛ موشک‌های ایرانی موجب خوشحالی و هیجان لبنانی‌ها شد
🔹
پاسخ ایران خیلی زودتر از انتظارها انجام شد! همزمان، حزب‌الله هم رادارهای اسرائیل را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/440543" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r01O-UGFyJgddnos49BL7_5PPNM0lc_8fE7kMFw20YnJ4h6eO4JBZwgDYMdgpt8YnmJPRo7yDhhttegEfGZrOkrAShgOCcrQiJDRpA0mtYy8ztX-4qJCRcU0RX-VtLvyHjua-VYRj4xHnHIp0tdnBDYUXbqSFZq8E621fUrW9CsXZqlYOdEPxOUs-pA3frTSRl03KMa3ZFH7pQ_j5dsjPA1lS9_1a0xlUx2mUiqTtsBcEsPszDqqoRZmZpKv-RbAnvstYLZJ8ILdeW7Iw0yQteP0yNAjhKBD59u9IHNbgxSdHeBrpde3ckSrlz8ey-azMUgnawYBOkaAMwvw0UvHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/440542" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEhyWtMkPcBZHYHe1wFoNIENa3llM2KkzyJDY5YWuCPuTrhUFWXdPDgTymeNdS1a_DoITJ6onHofK4TEikh_NHyeIB4NLUz_EOUhdNiIsAyXtu5zi2CTumihCleQWTpudnGhbdKy_3wUSGgoUpFHgE5dN3PKjgOHGuBlVMvZDz74jVmIzBZNDAo27hW1xoiP05PzT9Xn_wKIdpArUDxb1sfeYfcBzxmGbl04fBuPMYshQZJ3QtvWdkNTCcF0ii-ugfh20Jy2aKyeQPZxKY4RBD5XYUqFlVKrRew76F08c4Mv4pzP6CwF8aTm1X5PDwKRgdKvTcKwQbIWO8K88_UYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: صهیونیست‌ها در صورت پاسخ به اقدام ایران با ضربات کوبنده روبه‌رو می‌شوند و حملات ویرانگر علیه رژیم و حامیانش آغاز خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440541" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم انقلابی البرز خواستار مجازات صهیونیست ها شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440540" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440539" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG5V-Gc0zUteRs1oai6N2mqUmm32OYkIBK-oFmrEBRpce0spih4Y3ntCQkGWKoKjkIaqHYU6AXMRJW-QZBT2K-n-YzcpolOpiZY3HybvFL84gqKdnRYEx6AlSGAtF5OhohAJSpQqzX_Y5fhw9Z-juEkEtWKYnUQ8Zj2Oh9UlX7C7ixYmFiaTkMF36qiJEMZbE55KB7k7cda0k6gXUerZjZdLkiW1a8EOUrQ9Iudpagz65mi_XOMwxm1T5fa2MYIPGFHChxDM1hrXBnqH8qpnWnaxaX-gunU1ruYWTFvEChXpDnKoA0rJbmhXhZCC0KP6N3U7cSBRmniWsN3DuZA0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440538" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام جدید فرمانده هوافضای سپاه برای تشکر از ۱۰۰ روز ایستادگی مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440537" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440536" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم ارومیه به هدف قرارگرفتن رژیم صهیونیستی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440535" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: سید مجید نقطه‌زن، تل‌آویو رو  شخم بزن  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440534" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در میدان انقلاب: سید مجید دیو رو بزن، تا صبح تل‌آویو رو بزن  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440533" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFfcpr4pDgFHr9zuo4ySa4srJR_zpS1TeqohPEdA8xVTs-CORqF1Hskr3L0ykh06ST0MfyLZHbmf8aVP-S9MdErRCvf8ibTQwPaXaVIuARBmrmTW9XrSJYxbWaZt0ThHAeM0Cpqnv41_nebNvNKcdxtpD-VSuaGX_WyLRmZYW6f8AggVvcifSqsNrHUGpXAHP2jNcINaWOgm88goetong0CD8wfdZi7jYjr40OPBOFVSdu-S8dnd5rVwm0XCI8Tjg8h7aI6IZibJxlKNv5UIAZAl-sbwON61ylS4uEq3vmhNtnV-mrcVx5kPDxcxTBZLM3eJWwCA2AaXQULxcblZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود
🔹
ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440532" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم در میدان انقلاب تهران به شلیک موشک به سمت اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440530" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440528">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPuqJ9yM_ZlApAnuyYJ-Qs9h9YiMfbimboCweT3SA063grYRt0bA6_i8sEShSKWbE_xNssncfden7B09xxdc2S7GfDTMjFo58m7-q1cSt-Fr1VdJBYbrAqiSWSl7Qh2hfE39BmcU963jVF0Z6PRQAOyC6z53EMQG3I1-OOkaMChOakp5MxBIjQQOdA1YsV7Dhu_ta8DfzdqJWVdrzzbuJLl-viEsP-YwS4-7L9YlZQ7UgTPgubz0ioPchsujy4BPCGbl06m6NVGsYu-NzCbeFwmwvN-kxyxs-xr9AzP_W7_--afw7UUyVsJCloUXYDzLjD2XvXyOTLw2ZvdepeKQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نفَس رژیم متزلزل صهیونیستی به شماره افتاده است
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440528" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izY56D3UZVj9-pATj82qwc243kZfYNvfxfsszJphXDWqbj1qCxSvoEMoV2FpiAV3Nnr8rc2padzXswmf3TSFgDme03T3JVjTTceBFDpowQMeUn5TYx2S45NiD_bAz8NsUUa6p0Yf_eNV_Y3Qtyg-TIf3EzhX6GIsjj5nGbp29ao6OGj0s0unQOxE5ocVGqXNLmFXajORQzPYYqt3RqWBR0-yahc_6GZcG3MwgpRd0HTNu4p-U9ZUyE8x5K253LwKRsbngf4ILQ_hoPpBelk0yZnu6eXNCacMLanMVbnUzVWj28u0UOqouuIyrp4Kf7ZrwamtIVvUj_VieXlPIjG13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توصیه‌ام به ایران این است، موشک‌هایتان را شلیک کردید و این کافی است. به میز مذاکره برگردید و توافق کنید.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440524" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پذیرش آتش‌بس توسط ایران در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود؛ لکن مثل همیشه امریکا و رژیم صهیونی به تعهد خود پایبند نبودند، هم تجاوزات و جنایات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگهٔ…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440523" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/440522" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: در پاسخ به جنایت گستردهٔ رژیم غاصب صهیونی در جنوب لبنان و کشتار و آواره کردن گستردهٔ مردم مظلوم مناطق صور و نبطیه و سایر نقاط از جمله ضاحیهٔ بیروت پایگاه هوایی رامات دیوید، مبدأ این تجاوزها هدف موشک‌های بالستیک نیروی هوافضای سپاه قرار گرفت.…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/440521" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/440520" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد  @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440519" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPuQHbOCr0MEq8PIYHbxqin2D_-FU8HQAdf0ABLaNFSNHDcDN2Wt0cgI7zgY1iVoNVqz2uqgcQfyUZOXqFNbU8U02IATClB5oCfDPdTvga36NB_8rQKGUDj4R0-7HHlY8ZVaJubjTeYJb9Y3TAQ9xbo7bWPyuqDpiXgc_VL1Nh4YqaYSx9sk7cmqOcU388IHnc2oI_32CY5nKbg6s9jjgtH1A8OA1ktPRNKCSf7XT1YTqKVdIAu0dDf5HTFjSMYxeuV_stTeqxBK1OQj2LW553M7wTkzReZK7RsJYbrM8i4EwIcoT559OywE4RyAeUy6_PpQpBLX9HnURevjPk5Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ایران بارها اعلام کرده بود که نقض آتش‌بس و تجاوز به لبنان را برنمی‌تابد
🔹
امشب متجاوزان پاسخ خود را دریافت کردند؛ این پاسخ هشداری است تا دست از شرارت بردارند؛ هر اقدام جدید پاسخ کوبنده تر و هزینه‌هایی سنگین‌تر دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440517" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5kdBbAM0ODt1vlRzmE5Ksyto-3fGDkpYqbfRE-yG39cyQz17d1gArcsW89ZHSJLI0D-K1yM4BwjYMuJ6mPs4F-ubLLo33exZzDSDlEhkEPt7xTC0zwBG3-WjH5NQXehFvGKFi_zUBNaAH3H7WYrgXvZBVEXAWrjejxJYz7DIDswjacKd6s9Zk54DuEdqpAwGXO3BH7aIshTcZep34DcOSoG6ubweHhg8tLTtY7-yrONlCcSefloQdUME2ZNTGIUk8q9KUoFuNXmPN2r9i9IwjKMKvm7uYKRp4U-pVf5tNgIsBWiDflctHtTzdHv7_xR-qFAuAPHGGvmTpeB8MJtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440516" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTbSFcXXyoiC3ags4zEsRYuLgQl7pj6EYOrop0EMQLNNzI4Te-uWnhmbi3-SEJzIoJpq8T3o3Zp14LxqD95lnpalaSnmQyoH28sBRw-TT_qCB08tWpQAsQFzYTcugwpLuHy988EhWHxD98H4HuDVqc-qanJwNQ6Ne4jhJqYyVYx39o1B-zV3tQvdc3JIgfQESrn-KqKOubFgw_8bgTYmMUwX2Vm1LOfA7SRC-ydP6r7EtVA2im8CbGWeM1J7BQ2bai_MKyKHZ1fzIHOLs5suyHWVeoQvtEkZ4Iew75D3d8oBNllMAMNwGEQ21vpIOAwpvCvTaxzoldymf12ABijscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام فرماندۀ هوافضای سپاه: الوعده وفا!
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440515" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
حملات موشکی حزب‌الله هم آغاز شد
🔹
پس از حملات موشکی ایران به فلسطین اشغالی، حزب الله هم دست به کار شد و شمال اراضی اشغالی را موشک‌باران کرد. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440514" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم یک‌صدا؛ بزن که خوب میزنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440513" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدارس اسرائیل فردا تعطیل شد
🔹
شبکه ۱۲ اسرائیل: وزیر آموزش اسرائیل اعلام کرد تمامی مدارس فردا در اسرائیل تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/440512" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی دوباره نواخته شدند  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440511" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از
موشک‌های ایرانی بر فراز فلسطین اشغالی
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440510" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIx9hMPMsAA5olU0esWXKftE1y2fcqPc62VlXAo7S7dqY8Z1GcO4plVl7tysxNzN9EyTmiPGkQt_lZnBB_rAGuw4JnHFU1WNMHfminYaJ9_9T9VhG7EgsrWwWWtyE9Oil_4wYl2yOZGTSAYbQ8mII7F9UQjhmv4CEkgxg0UteLjUvlmPq_qlgBxlsPAJPO2SlpcnFQco-7DhUIHOqMKfivbldoQg0QsoGwf0M4UvGAx8UMCWaTikt0pBD4JN6DjTa0FJhFTQPa57sUhcyAvlVFpUV-qfx4Oz1foKyratHe6BTC77ozbK8cgjTd-E8mMIWSUcZPr3ihkryZbvGKocrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
گروه هکری حنظله با انتشار پیامی، از اجرای یک عملیات سایبری علیه رژیم صهیونیستی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440509" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه حضرت خاتم‌الانبیا (ص): ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و درصورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران، با ضربات کوبنده‌تر و پشیمان‌کننده‌تری روبرو و حملات ویرانگری علیه رژیم و حامیان آن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440508" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2rpAuyprZjs51l5JbSjoAPcrM1GhStwCFOv-L3AmSzysuuBbdEvPAu35oD-ic7Zk2vz6439X26tCCrhI45f-SmppkCJw830GQcIRP7uua-C1Oh2NK58W8RC9nZS8MFmeLqPKw7V4VGKDm_ktuu7Ckehi_2y_hRAvgDae1PznlMNvviMfRu3lNKoAsM3CJxZj1v4nIvpqn6wRxrzJmRsjkKVqroRMfvFo705vp9qKxNeH1oOV9mOBjRqxPUnTBBgTXDkYUA4-w-CSlfNpIAzrhsrdPirwNvun2hA5DrfMhJs-9fg-m7j_oWQo6HMnxvln1A6fd4CkTdVAocsrEyPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440506" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
ارتش رژیم صهیونیستی: موج جدیدی از موشک‌ها به سمت اسرائیل شلیک شده است. @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440505" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
منابع عبری از شنیده‌شدن صدای انفجار در «نهاریا» و «طبریا» خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440504" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
جبهه داخلی رژیم صهیونیستی از شهرک‌نشینان صهیونیست خواست فوراً وارد پناهگاه‌ها شوند. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440502" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
منابع محلی از شلیک چندین فروند موشک ایرانی به سمت مواضع دشمن متخاصم خبر می‌دهند
🔹
همزمان آژیر خطر در سرزمین‌های اشغالی به صدا درآمده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440501" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf3d2c79e.mp4?token=pAWLPrF7UNpjXtWrbyMAcHBOBexrqXcz0iP97h5_AgW-D1HKKBKJ6G2fEWVj7zFApD5AQ5pGAuiWa-jPeT1pDgVuHD0rsOfqXVUL1n1K-0ehaIt3JSnKpyCNMleTbY1dFkPwnjkZc2KL89OnjYtYnqoXne2Iy6JGI3qJgd8Zhm1xyiZGnY7ty7RqBn8Ow6_SQrldXheHWD3Aiog7fjS2Ik3QKAEpINUCXjL4OITxewFNEJ5JW62a8xV5_IVqwTDc0jwg91lKZ9bZdVyea9flMA39IT94DrAHsvt1vUdq-7gnOKxWNFDxRhhllXZw6GwI1K4SOsJ_Ab3c6L41CGHwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf3d2c79e.mp4?token=pAWLPrF7UNpjXtWrbyMAcHBOBexrqXcz0iP97h5_AgW-D1HKKBKJ6G2fEWVj7zFApD5AQ5pGAuiWa-jPeT1pDgVuHD0rsOfqXVUL1n1K-0ehaIt3JSnKpyCNMleTbY1dFkPwnjkZc2KL89OnjYtYnqoXne2Iy6JGI3qJgd8Zhm1xyiZGnY7ty7RqBn8Ow6_SQrldXheHWD3Aiog7fjS2Ik3QKAEpINUCXjL4OITxewFNEJ5JW62a8xV5_IVqwTDc0jwg91lKZ9bZdVyea9flMA39IT94DrAHsvt1vUdq-7gnOKxWNFDxRhhllXZw6GwI1K4SOsJ_Ab3c6L41CGHwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/440500" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2fuR4stj16rbJtF_IHkGOkPh1YLrbaoFy1CvmBFhrVEuFFXRRDGfOk53RP8FMfq1vP1YefeV1wgoOMPtGbA2qivpWR9ZM8e78Lf97NpLip2KI2TsfnAColVsZDNsFmv0MlaBEyvbvguX3kylrquD0plurj_XdedYK8pI6FQCOybCp1nlJsOZ_cbMNdmb1COw0M0jriJ8iR3SpgV-quxzRqj4hTM0r5df5VA7Px-Yf3jAuG_uTPJkDt_-7k_2g1cwJmi-TQm6OgdmDux0SOXE9EFuAFVmOS35L9H806LN6Ej-Cml4xdkMc9WY8n1t4I6ZRLOG-F78IO9C2xQQEGOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملهٔ موشکی به شمال اراضی اشغالی
🔹
جبهه داخلی اسرائیل اعلام کرد که شلیک موشک‌هایی از ایران به سمت شمال اراضی اشغالی را رصد کرده است. @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440499" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حملهٔ موشکی به شمال اراضی اشغالی
🔹
جبهه داخلی اسرائیل اعلام کرد که شلیک موشک‌هایی از ایران به سمت شمال اراضی اشغالی را رصد کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/440498" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آماده‌باش آمریکایی‌ها از بیم حملات ایران
🔹
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از مقام نظامی آمریکا نوشت که نظامیان آمریکایی در خاورمیانه آماده دفاع در برابر حملات احتمالی از سوی ایران هستند.
🔸
پیش از این رژیم صهیونیستی بار دیگر آتش‌بس را نقض نموده و ضاحیه بیروت را بمباران کرد، حملاتی که ۱۳ شهید و زخمی برجای گذاشت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440496" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701c82e151.mp4?token=QQTXYXsaUX3fKkmoO0f3bi9BInDKvfrWOaiS_pFegdsJIMTUZMTJgWa3tjpG2oCJkJLA_fEBfWtWntyZNdOQcu0hbqrLnP-1Kz5ezFq3Y5iQavqP0yTw8RhD8Xl1lsnnpesCOmEvRpxRVZHU9Nx8jjsabIa7mAnHECykMY11J9QCERH9o8ZsTY_XFJD6B0bor45KkwL9QJK-oRe9z0AVGpGcXgg7BtVXsKw2R5HInzVr5_ApgsiXBkoTy2PtdrPNfm2Xw5SJzd4vzAm0hsmWHWcY3vC_FyYn8lFcRcOOmWfBwzwq0Os0AqQX0g_b_rNO2Sp95hyN_lI7ij-ildwQMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701c82e151.mp4?token=QQTXYXsaUX3fKkmoO0f3bi9BInDKvfrWOaiS_pFegdsJIMTUZMTJgWa3tjpG2oCJkJLA_fEBfWtWntyZNdOQcu0hbqrLnP-1Kz5ezFq3Y5iQavqP0yTw8RhD8Xl1lsnnpesCOmEvRpxRVZHU9Nx8jjsabIa7mAnHECykMY11J9QCERH9o8ZsTY_XFJD6B0bor45KkwL9QJK-oRe9z0AVGpGcXgg7BtVXsKw2R5HInzVr5_ApgsiXBkoTy2PtdrPNfm2Xw5SJzd4vzAm0hsmWHWcY3vC_FyYn8lFcRcOOmWfBwzwq0Os0AqQX0g_b_rNO2Sp95hyN_lI7ij-ildwQMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شهادت شهید علیخانی از زبان مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/440495" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e9c6e26a.mp4?token=WhDzpyAzHAlSahS_IF6nZZxGbFq2ojFWAVWuUTRjOS0vFzlPC9NiYbjrpLO1umVY5pSLx9WM6L2Ckwz8Op4LqTT5uxAwuTfl4dkSSrURNITsWzayOb3NJV5KUuO_mdPeUOBRirwjB4dI8wUEJqhpB-NiakUYXwYZvOUugVg_iEdC7glguwj5K8xlAeVI0-SYC-XbBApGeEfj38lPQ_eARF0EUxWLeWL4FamxN6jblRNgJdIV7DoS6DWshvCtpY6UQ8_w5I-_VTyHjmRnM7CnQPxjzC81OpK2YxeCI4d7eO9a1LKeks1xRhdFk5mnN1V5hLgJT2I0Dwz7FRUv1JdWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e9c6e26a.mp4?token=WhDzpyAzHAlSahS_IF6nZZxGbFq2ojFWAVWuUTRjOS0vFzlPC9NiYbjrpLO1umVY5pSLx9WM6L2Ckwz8Op4LqTT5uxAwuTfl4dkSSrURNITsWzayOb3NJV5KUuO_mdPeUOBRirwjB4dI8wUEJqhpB-NiakUYXwYZvOUugVg_iEdC7glguwj5K8xlAeVI0-SYC-XbBApGeEfj38lPQ_eARF0EUxWLeWL4FamxN6jblRNgJdIV7DoS6DWshvCtpY6UQ8_w5I-_VTyHjmRnM7CnQPxjzC81OpK2YxeCI4d7eO9a1LKeks1xRhdFk5mnN1V5hLgJT2I0Dwz7FRUv1JdWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباسی‌ها امشب فریاد خلیج فارس خانه ماست سر دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440494" target="_blank">📅 22:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۹ زخمی در تیراندازی در نزدیکی کمپ انگلیس در آمریکا
🔹
نشریه سان: وقوع تیراندازی در فاصلۀ ۴ مایلی کمپ تیم ملی فوتبال انگلیس در آمریکا، ۹ زخمی به جا گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440493" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b67285381.mp4?token=AqS35aCsLK_uF_vntDszn5vQK83ZHaT5RLyq0CFi0-hXq18J8rx7PRkAOIFqNGtfrTx2IxwYgAR9QIN3FGpXmhS_zYTBDFH0JTXw2IPT5m3Q4gpX5F74Gt5Ro6yfYDXg1POZh1dtYNmz2brIIxQkjTe9VPdxmlPOC8HL8TbibFwmOetFkr1WRXyQkvfvN9dQP9dxAlFk6hnJc45ODPxGoPyq_t8lyOx09KJorut8_rVAZzx8qrAyOgB9s2yWhT2Ig__14LPrCBtVoHcsdmujIuDMX9mUiZFandk46sBsUdRVPg5GYEHxDR5h-ehif62-u1rkPjppaMUwwDBdonFK5zxcn-9znEkDMhdGSJ3AYgfWbkLyHzhaRqKSidUsaX82DoYUz6ByM8bP7o9ljytDNAfmAzi3RHgCzDO0UTl6cFIgYWhcTnwgvY_S44P3c4-kYjExj7_l6ziF67Oq-avgQeaAuVMHUswWDxGWM6LaBgVx8f-eYuVV20XaCg4v01NRFwtvwsIZbUALISZtUko1jUlq_okXz_Z2kwbTkNK3SAE5i0G8ppjVLHoLTshGGyo8pLVRsJLMAYCQxZKbdkv-dlATtF4kiywnAzPlp0MP2ARMls0i0D9ltfzUI4_4DL75jmoaYTGa09BocDfkT5GF1L0ywX5g3qxjf7LukqpwnAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b67285381.mp4?token=AqS35aCsLK_uF_vntDszn5vQK83ZHaT5RLyq0CFi0-hXq18J8rx7PRkAOIFqNGtfrTx2IxwYgAR9QIN3FGpXmhS_zYTBDFH0JTXw2IPT5m3Q4gpX5F74Gt5Ro6yfYDXg1POZh1dtYNmz2brIIxQkjTe9VPdxmlPOC8HL8TbibFwmOetFkr1WRXyQkvfvN9dQP9dxAlFk6hnJc45ODPxGoPyq_t8lyOx09KJorut8_rVAZzx8qrAyOgB9s2yWhT2Ig__14LPrCBtVoHcsdmujIuDMX9mUiZFandk46sBsUdRVPg5GYEHxDR5h-ehif62-u1rkPjppaMUwwDBdonFK5zxcn-9znEkDMhdGSJ3AYgfWbkLyHzhaRqKSidUsaX82DoYUz6ByM8bP7o9ljytDNAfmAzi3RHgCzDO0UTl6cFIgYWhcTnwgvY_S44P3c4-kYjExj7_l6ziF67Oq-avgQeaAuVMHUswWDxGWM6LaBgVx8f-eYuVV20XaCg4v01NRFwtvwsIZbUALISZtUko1jUlq_okXz_Z2kwbTkNK3SAE5i0G8ppjVLHoLTshGGyo8pLVRsJLMAYCQxZKbdkv-dlATtF4kiywnAzPlp0MP2ARMls0i0D9ltfzUI4_4DL75jmoaYTGa09BocDfkT5GF1L0ywX5g3qxjf7LukqpwnAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از نودونهمین حضور مردم شیراز در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440492" target="_blank">📅 22:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuC0SzFypAvbwYInQikTvcsUH96POHQgo4HC2yXEL3ZkpImENGUHbbDjNeXzUZ7vym2T3rson5BANAO-_2br0eUsqlUFHLw4fNTZPLY_dKhoAw__NqQ8ccxt3s9bHS1UXjvlgQQc1xQPkemXP3P-Tjt3_Zp-nkBndnoaFSQaKcvWm7pbjJtBcRfZ_C4PPLCYQCWpiEY3LTy5JkQa6M2z77c1zjFuxNWeNir-SlZzyhYz7YKf2zskJ07eLhLobxBENKVfTYGeqv3_Z_3P8WQCgARMBzKUZleoRvdYkZEmOexBKLeFGhsy7aIJGDE1SWr822n1RPHKsHFjspGF131KsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXta6vXcbIp-A7t3-G01W5QA2tJ-EslRO2L6BSw_zGINzigQaTKy84aVH48urZPlDougOAAQ5blMqTmKHd7O3SZ5JsRaLAVRyYLJpFnXLpqOblxfhmDT0o-TN-gkv8DMbgizgsgOdwFnjPLjNa_ltIaJaN5LBTA3_2fQ3UMJzHK-Mg0U-CgUjEcA-OI9a_JWkQkSfTh-qC4-_fgLJNjl-rbm-C-rpwLMKr4rhGDDYC8CMFewa2juVyIjMSji1goBtd9jUuNlxPvz-x8oDrg8eWvd_fueeBBGmlqOpJWdV7ywjTmBZOKcYff1Vnhq_F38NIb6V3keZoJpFSPAEXu5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYykXEr8TTAjBQ4WyiwCXLMi6KEd3AZU0dfZb_FlQEfTD2TfF8he6YmZViqn7CEvhnTM5Ty97V3KLt8WOCbbMLv8HoWkrhh87aUjF0zhMR6LHqVhFIirSGAtP5JNVMWUYMrqrM18CozOSGgjf6_RM-Ro_ZAmqnqBVeBfWm4VYjiTSvU8E39WkLYRTxMRqNHiUYrMVrZjX6rtPbcgxIxaJvpXLDEJ0h5NyTqZ4Uy5SVTVeFW-VctGjLTi-BZ-jIcQp5KvLY8KCBUtK9bQVUmmxiDFnVt68gG5Bnok_VPjDAeOi2xC60yWFa6VEl5txKm72qstCVT6e1wYviAmVj62Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-duWEy7glz6wCcImHdPawRF-KEQYbXhFCFwucHg-zFs4q9jUFFjCIu19sYW5sYRIaxtsPaD6xSrfiNOoasWgM94qX20tL5D30z0_oz9tFfQWqvPxW9gzpwPMNH83GFF7Dbpp33hZsJ5F4TBwRpkFUhWDCNHSLri9i36IeIH-QnhAxw83Sw9UoSTSbvsEGb8kWXDlXruucSzVwJvMttNUIzQLmIPecCcFpWB8jxJEsC149KoXM0V2xe9ZdcMbhywZDnK6uqW-_QXXOzXDgXce-ASnFitsPnkg5G-rReU7Q63HWONEVymZT1yGRQOdmJ12Vg2WPdOVDsvYjKSBlzokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rU7P2WDpBFka6DOGFiueCqllzRbn5nxuuDTzvYAQ8EijHSxAOD2cQfhRcXkAHPH14Szd9sBVdgrtjHeu3gdaunHJzhPFazOwmJYyrjssyZT-JeAzVXfAEc5yTNAmtTfXmG3OZ3bd4HqSii5n3mzUquzVQ152T5n7QSL1gl5t_hbq_1VwGjoO8IzTAx68BZazwgsH5MaqtrQdkULZc40XS3GeqiB5Upw546D3OGq13to7CXiAOx8KWYXWL4DUVSYPWRp6DITQI2ewZE_-CAUIXZIU3H2qx_H4QR5zDSOumxpTnJDSBn0OLNckQIon3zG6CaBJfPoLQuzJZ21SnPbdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfdR0et1Lcu9En7PjhmNS7nhNffiZcR1nmm1AgbZuhhhGEFcXykeepXPz4uJcizMdFkI40vEEF06drKocvYoP9EA_fWRC_cfOZ2n6FzgIh9DX_28EUikM7_ulXAGQOqh4xs8Br3RvxI3YppSUwZCwGlb2f3XyQt070hNuAguv9q5hZVd3wtVovDkd7P8e9MpFeLkLBxXnKKXF_5URwyUOx_RkyjgFY7euBehW1bO4myvp-ZDFjYt2xyuAkOSm2jMz_tv5u6tdwfAafOzUvpgfXO26CK1dUU_jaCPGS8fV7wwGumkiiV6rh1qUyYO-lSDQikNLRRMDhZ12LX5tKUkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICUK50fj90tT-JFW6McVfwgK9VCisg4vn1J2uLLDovT4kxAZ5_ATmOpAGZehN7LlIGuhluUkmB1BC8ijHMXx8DqVYIaXTPhPipIABhM9OsNQEVR2YRXcCmV17uhdICTRHpoJSp7G6ugxMLwpi5ORcs8V0hzd-ImRexDy-V5jXiCrWzJYoAHhX_w5NpHVTEKgVNeR8RnNmxTEYl-a5B7MsStjUvhK7dhQHMauTdYj_A8q2ahOHLIXpBMBFzCDyVCEZHyro7-E6EfNlQxcEO3kNoNJ8nBW3FK0YdKHHyDtKkO-wRxEI7_JhLV1YFJSbZxN9hZCpBWoFB8NU5mhv0IJ0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست‌سازه‌های فلزی هنرمند همدانی
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440485" target="_blank">📅 21:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0Uze2VdHTYl4Qs8kWjjKJH1Xbx8XqA_D6kIzwUJhG7UP7zg2thWkl-ycLLLAlwqVs40CxXtPx1vPtmmx3yr5mY-S5YQkXzKhpCl2bC4ChdfsC3R2NvY0GCEJ-jQrgBJFR-td8ZtzR-AS72-Al5wXV5ARrF9jn9g2hTADvmiccxYw9ZOJ-ER7bNyIDkXE9rZ6XO4IawunwTBQIlCZfKUb2RTI2Zm3_5cy1MeDNaRD2ZR2StVSCdv9pVMLoZp-_wxpjVBj-QoDVZnc0rCshczd7HptLnDLmMkUSOz7lO8YahRibhHgJB63UOMVbxdLlA7N4oEE5RMx7Eye_SzcG2z3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be159b4b4c.mp4?token=Fm6NN9CcQ3PJBoRXIqResJ5k9Rxay4uyI_Q5u1zp5lzg5ccZObyAbT48FCsrXUxWfTLnAshvG1Emz2mvioPbkKyf_rXbStBd7eENPs6Nlrm3xeXR9ExBaq40e6jhaV6r_f8Oqtw7yIwJZvIv0EqHn22kDEIajqGt70U6eU07XJYQvgME1hYZAwTsP2aqAZxR6tiEUTQsMbbBw3EBH5I4CxKyCs-WHUv60gMEgYkLvMYilKgDkJoSy5FymJefJo-McG1k9D5atbsL95rQJ1J7OcqpCUSgsiCpEW6UlwrypSTiDGmqxEwRSrVnvhQzCZtayuVd3HDrwFXMWtrxWj8VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be159b4b4c.mp4?token=Fm6NN9CcQ3PJBoRXIqResJ5k9Rxay4uyI_Q5u1zp5lzg5ccZObyAbT48FCsrXUxWfTLnAshvG1Emz2mvioPbkKyf_rXbStBd7eENPs6Nlrm3xeXR9ExBaq40e6jhaV6r_f8Oqtw7yIwJZvIv0EqHn22kDEIajqGt70U6eU07XJYQvgME1hYZAwTsP2aqAZxR6tiEUTQsMbbBw3EBH5I4CxKyCs-WHUv60gMEgYkLvMYilKgDkJoSy5FymJefJo-McG1k9D5atbsL95rQJ1J7OcqpCUSgsiCpEW6UlwrypSTiDGmqxEwRSrVnvhQzCZtayuVd3HDrwFXMWtrxWj8VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک به دنیای فوتبال
اریکسن باز هم دچار حمله قلبی شد
💔
در دیدار تدارکاتی، دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شد.
✔️
گفتنی است که فدراسیون فوتبال دانمارک اعلام کرد کریستین اریکسن هوشیار است و حال وی نیز خوب است.
📌
اریکسن پیش از این در یورو ۲۰۲۰ هم دچار حمله قلبی شده بود.
@Sportfars</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/440483" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5d171bf5.mp4?token=D3imaNgqXvMG-EIojXy6i2QN7Cx9u9l_AbXiPiNjrYxZVApCzOuWpLwzgHPg3tEU0uucnqc3zfw5tw92LTg3yrSygrkn8gqIjQT1QJA00EGbP0MYiPuzsj_XLFh9Q9-4wyaxx2dos9uZBJO9Rh4Sqx639Ui9FQOhwa1IQNq1C8usE1QrZHY3hd40-YmVfWbBxdATklF7yQ4dZxyMblJ4nD--RPhRLR1-8BquOdOIDbxWdXgod65IUQ36bZdlF4hWZLADeZzCaDSysdQnohcSLs2X-FMk8_MNLCy4hWPwlPjNWP2sTsiKSH653dN2FKvJBb28hSgXguXxdLor5YPX2YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5d171bf5.mp4?token=D3imaNgqXvMG-EIojXy6i2QN7Cx9u9l_AbXiPiNjrYxZVApCzOuWpLwzgHPg3tEU0uucnqc3zfw5tw92LTg3yrSygrkn8gqIjQT1QJA00EGbP0MYiPuzsj_XLFh9Q9-4wyaxx2dos9uZBJO9Rh4Sqx639Ui9FQOhwa1IQNq1C8usE1QrZHY3hd40-YmVfWbBxdATklF7yQ4dZxyMblJ4nD--RPhRLR1-8BquOdOIDbxWdXgod65IUQ36bZdlF4hWZLADeZzCaDSysdQnohcSLs2X-FMk8_MNLCy4hWPwlPjNWP2sTsiKSH653dN2FKvJBb28hSgXguXxdLor5YPX2YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۹۹ شب‌های اقتدار در شهرستان بسطام سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/440482" target="_blank">📅 21:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48e558a2a.mp4?token=VQip9jhhL6MQVhMRCHmtQIL6TZayTIb7RQ-Kl-h5harJ_3irmL7gKwVZVKj0dQlZd9HF7slJf9kEX0DigBI4zeyximK5i3VKHL6oStSIEVuB7G07H0o7pIxN8MXoy6M3jjlENA319mwKhzJDEefNJf8_m09AcMcwjbIwQYIIaHMJipc1HiqC7SFmO6qizlJKCDO_HsHVSKxewRGeXWVEOEg_J-bVQ0fHTsTop7AqXaAgY6G-sr4zwr6WgV9Hiw3R5cjKdpm38WQp684cWfRWvLgEu3iYzIUdgkWnJWhftS8LeCCI8qfWtCug2M6SGjpxqfeS1xcFD9wdn5BwREH33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48e558a2a.mp4?token=VQip9jhhL6MQVhMRCHmtQIL6TZayTIb7RQ-Kl-h5harJ_3irmL7gKwVZVKj0dQlZd9HF7slJf9kEX0DigBI4zeyximK5i3VKHL6oStSIEVuB7G07H0o7pIxN8MXoy6M3jjlENA319mwKhzJDEefNJf8_m09AcMcwjbIwQYIIaHMJipc1HiqC7SFmO6qizlJKCDO_HsHVSKxewRGeXWVEOEg_J-bVQ0fHTsTop7AqXaAgY6G-sr4zwr6WgV9Hiw3R5cjKdpm38WQp684cWfRWvLgEu3iYzIUdgkWnJWhftS8LeCCI8qfWtCug2M6SGjpxqfeS1xcFD9wdn5BwREH33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور گرگانی‌ها در موج ۹۹ همدلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440481" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حزب‌الله: دستگاه اخلالگر ضدپهپاد ارتش اسرائیل با پهپاد انتحاری در اطراف قلعۀ تاریخی الشقیف هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440480" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f993d294.mp4?token=ko3u8Vf1oGzoukK7Kj6lotpXYRt8gSNwIocdqMalEaPeXyE3G4yAkSdgfqZLSxi1R_l8TMel7sH5hMrBQW8FxzN6lfDyS4QZBd_aSYL4mTB8d8RiqzqtGkOUMblm314A3BqVgZvB8lPj4y6IbGLTlTB8Dk7lyjSkYBLIYJlbtRdeegmCNHrMHBZomzsGaYqO-LxJv8m03ieoVx3F6P91_1xJI_JU7Qzb4W4SugkMcMgz1MdFE8OxXZQO5iW_6CBX2aHuJ3BdGZNb86eAst25fKJpBO6C25iJgqyRQteQW2MKed8v_dJjRLaJwfE1nMgudgfqglevKtPpdKUygOSVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f993d294.mp4?token=ko3u8Vf1oGzoukK7Kj6lotpXYRt8gSNwIocdqMalEaPeXyE3G4yAkSdgfqZLSxi1R_l8TMel7sH5hMrBQW8FxzN6lfDyS4QZBd_aSYL4mTB8d8RiqzqtGkOUMblm314A3BqVgZvB8lPj4y6IbGLTlTB8Dk7lyjSkYBLIYJlbtRdeegmCNHrMHBZomzsGaYqO-LxJv8m03ieoVx3F6P91_1xJI_JU7Qzb4W4SugkMcMgz1MdFE8OxXZQO5iW_6CBX2aHuJ3BdGZNb86eAst25fKJpBO6C25iJgqyRQteQW2MKed8v_dJjRLaJwfE1nMgudgfqglevKtPpdKUygOSVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش سنگین تگرگ در شهرستان اهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440479" target="_blank">📅 21:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
معاون وزیر خارجه: دولت‌های منطقه که قلمرو و امکانات خود را در خدمت تجاوز علیه ایران قرار داده‌اند، باید خسارات وارده به ایران را به‌طور کامل جبران کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440478" target="_blank">📅 21:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
معاون بین‌الملل وزیر خارجه: ایران متجاوزان را رها نخواهد کرد و خسارات جنگ را مطالبه و دریافت خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440477" target="_blank">📅 21:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
معاون بین‌الملل وزیر خارجه: ایران متجاوزان را رها نخواهد کرد و خسارات جنگ را مطالبه و دریافت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440476" target="_blank">📅 21:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZB8lGX9mPPe4wtZi20RfqUM3H2d1bLZp-FtXBmBUsLhZrRXh4ACEzX1DUU7gssCn1_E5rki9qgE1hcNG8WvS01MutD6GKr80vIxy5S6IsUqgmbn8d0EswmuPNYk8R_inMyr-BcrDoYrbsfXlSbAJ7r8XuRSY7f8Op_EKbFgTDuVgBtHHeolqlXN0pU-KtpQbwXC0UiQuvbHHNiP19w7bIpNSNU1tiSTWtedZdlrF_3o4w1zob5_2-GdOvsOFFoLPzIhyb4sjGH9iuwKhgEUsy4lx8WXhchUQIHv8qcxIMTP-48Ajk8pPWwVebeStpShjq7xL2LWNOSjHbinfRNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440475" target="_blank">📅 21:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHpU2ulWDpHk2_adpcy940eCPri2mBmsyXPCCrpPpDyBwUwQYkM3pgPWtK8kunR6VBrP0-nqF76F1K4LbRsUWmlr-M5FqEpwKHrh3yhXRAvT3N_MHrEfnbuXanzjmGTJxoclHGNQkeaLH8HOHjynbweYEKMzhYk1s6ank5uV-eOW342tsB21rx1bArgHiKqeF51QXn-oS3HoCecy8473ZSM8phsb9fFK92hN_z-B0NQzq4TSZWbh9g_20mHqU77ideHCxGX4k0azlZTA5j-enhjL5aCp5sKzpOVM9Ms690WUUxOCbUKQeLbi3I0p6uBNRhllYA9W0Om6QUM9eJbM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر لالیگایی سومین خروجی استقلال
🔹
آنتونیو آدان که در ابتدای فصل در انتقالی پرسروصدا با قراردادی یک ساله به استقلال پیوست، به احتمال زیاد در فصل آینده پیراهن آبی‌‌ها را به تن نخواهد کرد.
🔹
مدیران استقلال باتوجه به عملکرد و شرایط سنی دروازه‌بان اسپانیایی، تمایلی به تمدید قرارداد او ندارند؛ البته باشگاه استقلال هنوز بخشی از مطالبات گلر اسبق رئال مادرید را پرداخت نکرده است.
🔹
آدان در مجموع ۱۹ بازی با پيراهن استقلال انجام داد و آمار ۶ کلین‌شیت و ۲۲ گل خورده را به ثبت رساند.
عکس: علی شمشیرگر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/440474" target="_blank">📅 21:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440466">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454ea6fc43.mp4?token=hoqaLwfW4xhwR8lpAV_5ncn0R2D_Po3I7rcJkPM2ydvyoH8Yj9pxMbaQy9ugRRakP3x4PFaApqgGOAgt18HzJMBQCECLzLfLvNr2_RxyPcc6M7qiKKVQ1sRVbx2AfZXPNC0LNtvI6WjlVWXiZGwunT8j5ugSnE6S7_o88uVXGASeBXXlZXhbJvqIL_9EyoFAF4IiTTHHDSsFnWzezYvTQdF0kdQZPdaXZah4w611fXq_G5Ifh3IUyHk0lAyKRIS5YWaBKMNlj-vjQMPUcfWfkNrve9jZohObaDDwdxvk5gXF10DN70ZghumJ3gPXc9CoQ4u3qzzIkKEeiUj5Ysa65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454ea6fc43.mp4?token=hoqaLwfW4xhwR8lpAV_5ncn0R2D_Po3I7rcJkPM2ydvyoH8Yj9pxMbaQy9ugRRakP3x4PFaApqgGOAgt18HzJMBQCECLzLfLvNr2_RxyPcc6M7qiKKVQ1sRVbx2AfZXPNC0LNtvI6WjlVWXiZGwunT8j5ugSnE6S7_o88uVXGASeBXXlZXhbJvqIL_9EyoFAF4IiTTHHDSsFnWzezYvTQdF0kdQZPdaXZah4w611fXq_G5Ifh3IUyHk0lAyKRIS5YWaBKMNlj-vjQMPUcfWfkNrve9jZohObaDDwdxvk5gXF10DN70ZghumJ3gPXc9CoQ4u3qzzIkKEeiUj5Ysa65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دولت با تمام وجود تلاش می‌کند و مدیران شبانه‌روزی سرکا
ر
ند
🔹
وقتی تا اینجا رسیدیم معنی‌اش این است که دولت توانسته مدیریت کند و مردم به آن شکل جنگ را احساس نکردند.
🔹
کشورهای منطقه، اروپا و آمریکا و آسیا همه به‌خاطر جنگ تورم و گرانی و مشکل پیداکردند، مگر می‌شود ما تورم و مشکل نداشته باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/440466" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440465">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153f1c205f.mp4?token=kQxeOd9-fjFMiKKtC-Z-59n0tyw_wUjbE-F1umA1iMoAN6ydQoHpsGcONPfe1_f39p50s9tdex7stIUBlK4jSKZMUsz3FAxJWzuxfajCtSlHvSFUlziQ1mgGFt6ZP2oEVU-YqnAvq8iUrunOO3NHA8XynC_-zwl50mcq-pRRE9jNqh5-JLLgdXpAgHvM5Rh0N0GTiRS7eUChx4DBBBFYcmk0xBF4myb30AFEXLZZzEwGdE-WMVcZfL6haAtKykbnNsi8dCC2sKvmo_jDp3mtcle7w7yg1xC-diCJIsxfJggD0VFEauhG9-f7-I4bch0sE7O0aQZgRvl6lxJ39xMZg6IVi4GIJPHw4-RJggvN2p3zQjn1npQcZFbElVK2SNilea1HhSxYUb2cJTfOJG8K0Vs4M16gPVhZp-RPfSz5PfMkaQcwndqCiWFB4st9KYC5MV-nWat4HZpN9akJ_lXk0MphBR4fwojCnsfIiiIjvTYWDfHeW5DBzTAtM4_8v4nwb5C2odpO9X3QHNfEvV-EZ1jvi_rZgCbKqUqgPpqQxkWi90nNY8VMwGST6N8SVx7gZNQ2oxW7i9cp08_jSYhAFJ7n9r-vbCHjEF462xl4KVAyWfKPuQmzNfCsEgivrAzLw_AsK7JGjadxYmynRh19b7IEtLaoidTpAqr8WmAbu6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153f1c205f.mp4?token=kQxeOd9-fjFMiKKtC-Z-59n0tyw_wUjbE-F1umA1iMoAN6ydQoHpsGcONPfe1_f39p50s9tdex7stIUBlK4jSKZMUsz3FAxJWzuxfajCtSlHvSFUlziQ1mgGFt6ZP2oEVU-YqnAvq8iUrunOO3NHA8XynC_-zwl50mcq-pRRE9jNqh5-JLLgdXpAgHvM5Rh0N0GTiRS7eUChx4DBBBFYcmk0xBF4myb30AFEXLZZzEwGdE-WMVcZfL6haAtKykbnNsi8dCC2sKvmo_jDp3mtcle7w7yg1xC-diCJIsxfJggD0VFEauhG9-f7-I4bch0sE7O0aQZgRvl6lxJ39xMZg6IVi4GIJPHw4-RJggvN2p3zQjn1npQcZFbElVK2SNilea1HhSxYUb2cJTfOJG8K0Vs4M16gPVhZp-RPfSz5PfMkaQcwndqCiWFB4st9KYC5MV-nWat4HZpN9akJ_lXk0MphBR4fwojCnsfIiiIjvTYWDfHeW5DBzTAtM4_8v4nwb5C2odpO9X3QHNfEvV-EZ1jvi_rZgCbKqUqgPpqQxkWi90nNY8VMwGST6N8SVx7gZNQ2oxW7i9cp08_jSYhAFJ7n9r-vbCHjEF462xl4KVAyWfKPuQmzNfCsEgivrAzLw_AsK7JGjadxYmynRh19b7IEtLaoidTpAqr8WmAbu6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ تهدیدی این مردم را متوقف نکرد
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/440465" target="_blank">📅 21:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bb62d0a8.mp4?token=bOmpDe6sS2_2c2CU-ULv7m6ttPYL32UeFLEqsloBfxM910IHKjO5xFfYUg18acr8rkkgVE7FlksEL_Hr5TowoPsPbBhB687xojl7dLjnfGu2QmRd3tVsMXJDhyqurx_FJ5xTPQAtgxC8xJX-7RW9OwhnX_Yt_M9bPgzHGQ62CHetzubH8f0j4XX-xSKim5JeWbVZLj6VGSqOP0qKYJVyinwYKH7iP4PN1srdMphdZ1JBY6oQuPxB9JHAAEUDAoytUqpeltMROnrZtOP3MgrFWTq0eMnBS6oE5DLraw2luOLu7fbUSEL4Cf8Oa-oh5XCilWXPl7jMxuL8gKKQkaYBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bb62d0a8.mp4?token=bOmpDe6sS2_2c2CU-ULv7m6ttPYL32UeFLEqsloBfxM910IHKjO5xFfYUg18acr8rkkgVE7FlksEL_Hr5TowoPsPbBhB687xojl7dLjnfGu2QmRd3tVsMXJDhyqurx_FJ5xTPQAtgxC8xJX-7RW9OwhnX_Yt_M9bPgzHGQ62CHetzubH8f0j4XX-xSKim5JeWbVZLj6VGSqOP0qKYJVyinwYKH7iP4PN1srdMphdZ1JBY6oQuPxB9JHAAEUDAoytUqpeltMROnrZtOP3MgrFWTq0eMnBS6oE5DLraw2luOLu7fbUSEL4Cf8Oa-oh5XCilWXPl7jMxuL8gKKQkaYBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشت و مرغ کیلویی چند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440464" target="_blank">📅 21:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440463">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb13583a9c.mp4?token=RAKn3QwKgIgW6rpBMAu48jQq-KB88gR9oJilWUsbjvL2UhFYxKeuACSOkRuwCK1MrGY7oWTI4FqopwmxcZvLflZ53TTGsxt0j3EDIFMpWf8ZcanACCAVZfgVYq6D0tkj9-XqVPC7d29KmTorEOc0ChUNNZz2rTQ-2b7jF5nTGYE15yjpPQsfHxN5PkgoQG_VBdqNMTVi8iEWp66wFemrlT2ghKV6fm8uj1z478nWFLtzLsgy-__imVYjv2dedKuOXHD5zsBmf5-dKhTj4ft-Tszh1FuoSPysyupZZTGoQEj9y6QxIlLa84QGwtwHxsAvbJK8TxfC8rK9CI27eDW7SU2p7l9np6WRJEfkxGJAs3UZRgSs3GnRNzGWqIlARkKlmPxz0aG_Mi9bCwKj5Slse3FTZd-EO9R7HhuRM114VcaH0Gg8cSjrrfuIoelzlYdemPhoXUFrSwSkVIVh90-nAUK-qg8so4Rr78i5_C5tz00lUYr5xXauW1hvFRbiqIaEuDXpOBEGrMjt7cHt2CF39ag2T8bAb5AdW6WOILrON6Z8y5ItFElKwPGlHjBGWIyb66h2fShFTWiM9IM5M_HjMfXUSn6RjScp93HjmVuOzxk9TDJCEu0SKVmxEm1zhexswWSCTRX9tgJOiYWwh_RaY0WAQhodxPqa-NC-VPVCEqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb13583a9c.mp4?token=RAKn3QwKgIgW6rpBMAu48jQq-KB88gR9oJilWUsbjvL2UhFYxKeuACSOkRuwCK1MrGY7oWTI4FqopwmxcZvLflZ53TTGsxt0j3EDIFMpWf8ZcanACCAVZfgVYq6D0tkj9-XqVPC7d29KmTorEOc0ChUNNZz2rTQ-2b7jF5nTGYE15yjpPQsfHxN5PkgoQG_VBdqNMTVi8iEWp66wFemrlT2ghKV6fm8uj1z478nWFLtzLsgy-__imVYjv2dedKuOXHD5zsBmf5-dKhTj4ft-Tszh1FuoSPysyupZZTGoQEj9y6QxIlLa84QGwtwHxsAvbJK8TxfC8rK9CI27eDW7SU2p7l9np6WRJEfkxGJAs3UZRgSs3GnRNzGWqIlARkKlmPxz0aG_Mi9bCwKj5Slse3FTZd-EO9R7HhuRM114VcaH0Gg8cSjrrfuIoelzlYdemPhoXUFrSwSkVIVh90-nAUK-qg8so4Rr78i5_C5tz00lUYr5xXauW1hvFRbiqIaEuDXpOBEGrMjt7cHt2CF39ag2T8bAb5AdW6WOILrON6Z8y5ItFElKwPGlHjBGWIyb66h2fShFTWiM9IM5M_HjMfXUSn6RjScp93HjmVuOzxk9TDJCEu0SKVmxEm1zhexswWSCTRX9tgJOiYWwh_RaY0WAQhodxPqa-NC-VPVCEqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان کاشان و آران‎وبیدگل را درنوردید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440463" target="_blank">📅 21:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440462">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CczRFu3sBSDeBYKb745op2h4AsmhwwQfv4mdSpX9L6PjwPaFJkxE2fXcP-dpvXzUyIMifJ7x306Snm5tjKg3pmZOEiOtvOtDAnoRzpi-_HRWYb3hVzXo8kJcTtHtI0MVPsVXbe8GBd5b9daYJ9PWxkD6PLzHMGv1IMOcUXcaQSfa-MyQfHxVMuC-u946ZCtJmNMDJOME4UzyccD89k3Lh-qiFMDgRIB-vCPoOoc3NZ_p58yIxMWrrT23P07KYMdr7NtwiZF98STgBuUS5wABzBUtFgEXvMBWZQddLJlEtiza_-9bEhN28PtP2oGqtNE-XRSS5hIAGUlYZ-4WTiRi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله وزیر جنگ اسرائیل به ترکیه: اسرائیل درحال فروپاشی نیست
🔹
کاتز، وزیر جنگ رژیم صهیونیستی در پیامی خطاب به وزیر کشور ترکیه نوشت: به وزیر کشور ترکیه که آرزوی اداره کردن اورشلیم را دارد می‌گویم اینجا قسطنطنیه(استانبول) نیست.
🔹
اسرائیل هم یک امپراتوری در حال فروپاشی مانند امپراتوری صلیبیون نیست.
🔹
شما و آن «امپراتوری عثمانی» که اردوغان آرزویش را دارد، مدت‌هاست که ازبین رفته‌اید و هرگز باز نخواهید گشت.
🔹
شما دارید تلاش می‌کنید ترکیه را به یک دوران تاریک و عقب‌مانده برگردانید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440462" target="_blank">📅 21:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ctbhFC1fTChf5G9XrRTMUFTsD3nd9dI9taUbGEXOoxUKzrE-DzBgaSpnsM0wjQ90md76_e-5EN5tkNz7ZqLWoG5DK3BIn9vmWynHX7QLm2ye3kCGPcJG099GomOPiVNWwg1xP4U6iFA9QahOC36JZEG83k4SShzrQAyo4v-JeP7w1vW4jMuLtDHg2nFYVFE4sQSlPQrGXZ6yGW6s_Xl7iYYDhgoNI0a2aRtUpkY9ABQs9FpkVqaRzCbXMxWB23TIZ9ckleshy1jpZ4jD3oCHJKT6BDw9oYPggS4iqLHB4Ids5uKxQXgAv2Cg5PChZLL2gsYa5Og52IyH7lSyjGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیباکلام ۳ ماه از انجام فعالیت رسانه‌ای منع شد
🔹
قوه‌قضائیه: هفتهٔ گذشته درپی مصاحبه صادق زیباکلام با یک خبرگزاری، دادستانی تهران علیه نامبرده و رسانهٔ منتشرکننده اظهارات او اعلام جرم کرد.
🔹
پس از تشکیل پروندهٔ قضایی برای نامبردگان، متهمان به مرجع قضایی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440460" target="_blank">📅 20:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx8YX2vPB-Q3ws0KZDXJuhE4drMfBwVAH8ijRKP5o49Y5xUByjk-z5hpdHCp5mPAUKUmi6fYU8ezXqsYL2SHU658_sDgpn9wTcMXlEf901VibfFgjaF7lwOfxo1c1NuVAo5ci3wsBWX3Zz7js2ecMbXJY2N7w6uqoad53hhWC1QBRNc_1d4RF1Xx4c8K1F4WCPm7CSgqqJGxZ0MIEnQu052Xfr68tntA7E_mteTLkcRn8vLRVRn6k8Q1Z9rBsJRpRCIMGOQ1gZvR2iewrzOBpZ4cnQJx1YyId9OvZuAEld2_RPBfY9O9-szvpLERN_HHvKAwl5eZrS54VNNux9P2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماینرها ۲۰۰۰ مگاوات برق کشور را می‌بلعند
🔹
معاون برق و انرژی وزیر نیرو: هر ماینر معادل برق ۱۲ مشترک خانگی مصرف می‌کند و حدود ۲۰۰۰ مگاوات برق توسط دستگاه‌های غیرمجاز استخراج رمز ارز مصرف می‌شود.
🔹
کسانی که دستگاههای غیر مجاز رمز ارز را اعلام کنند، به ازای هر دستگاه ۳ میلیون تومان و برای ده ماینر ۳۰ میلیون تومان جایزه می‌گیرند.
عکس: وحید بیات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440459" target="_blank">📅 20:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_TudCqq3VcjaPPgeV_9RqQFvwW5ugRLSBLQpgPbRGTa8PxhC1I6T3TMfXXU4K5WyDJmRf5ROJM47R7v-MP3UOmmlWEQWeNiTidNPgs0Xy26SxY0JOw_phfLWApl0VoXfzWjKrh4gQs6L9ICvSnbIxdnzRsojmiyaYY7M_zYvFQ20lay0PeGsy_RbDOiWhSkieqQUkD8RPDZviVLJZEudxfoeXATg9y7OqfnJo04NDMJ13dMqS00vApwyY2VT-6shorNXfjiR-NKqp3w7JPEl9A7ql1KkhIv1oRuHgJsOXIxz6KeWPQNTTzzuE-d5E5Nt6ASzT9q-j9rygw16HnZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسروپناه: تغییر در مصوبهٔ کنکور خلاف عدالت است
🔹
دبیر شورایعالی انقلاب فرهنگی: آنچه باعث نگرانی دانش‌آموزان شده، احتمال تغییر قوانین است؛ در حالی که تصمیم فعلی بر پایهٔ پیشنهاد وزارت آموزش و پرورش و با هدف مدیریت شرایط اتخاذ شده است.
🔹
اگر قرار باشد تصمیمات…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440458" target="_blank">📅 20:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f750c48735.mp4?token=JWErlZn6Zyv7ToiKxMWDilIukF2KiDZ7gV9CHMyIHq0sI3N2Jj6XCI8y9Nd_qOIlfkLmAkrMVts8mjB1CfKan_j_CFWAa0YzbzOOnFjTStZDdXRL9SmgvwshhhP5P2nF-KHfABO_Gm54aVdFcL___Nggo73yn0OoGkvXFKI7GQPei8Ptn3tIaGGGmDaUJjazB5FebaN5hGuUIpt1TA5KAlOkQe_ZXLRCys9DrbttEK7RbGVJxpbkkaucMwH0WWpl5_XiKU7IR6vcMYFfjhXD9hCjFzIPWY4zXa_5OLenZyvCVJGqT2T_NKsnFN_iCx98v2Wdwv9oGYnzoaS5KuLQ44bE-Ufb7z8Q2pMhECj3LHeyRhdEXyDVX2YYXbsx-4z5WwE4dPy3eTcnOqGPCKSSzBZOVpuHPQfHmIl7yHuF06FiwSNCX6u63ylVVw0y3BD-biAldlVrGRhKi7UDqBvdRK7pLkh1_2zeXIsRMz_urybKnZaBcuunbWU_E1jHclhARGT5rfWrZN5zheaxZ-kw--m5RZh0gVVIb9g3QhmhKmGp3Wpst7YByLQPsycrqjvWVjkXknFZtOiyu4RwPxNJWWq1p15DlfXVwsbAysNn7nG-5_JWi0Y_Y-D8P5qsr4aijqHRBP28RJJ9K0AAZ0kEtf0fAEWW3_joqWTRh3kXWH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f750c48735.mp4?token=JWErlZn6Zyv7ToiKxMWDilIukF2KiDZ7gV9CHMyIHq0sI3N2Jj6XCI8y9Nd_qOIlfkLmAkrMVts8mjB1CfKan_j_CFWAa0YzbzOOnFjTStZDdXRL9SmgvwshhhP5P2nF-KHfABO_Gm54aVdFcL___Nggo73yn0OoGkvXFKI7GQPei8Ptn3tIaGGGmDaUJjazB5FebaN5hGuUIpt1TA5KAlOkQe_ZXLRCys9DrbttEK7RbGVJxpbkkaucMwH0WWpl5_XiKU7IR6vcMYFfjhXD9hCjFzIPWY4zXa_5OLenZyvCVJGqT2T_NKsnFN_iCx98v2Wdwv9oGYnzoaS5KuLQ44bE-Ufb7z8Q2pMhECj3LHeyRhdEXyDVX2YYXbsx-4z5WwE4dPy3eTcnOqGPCKSSzBZOVpuHPQfHmIl7yHuF06FiwSNCX6u63ylVVw0y3BD-biAldlVrGRhKi7UDqBvdRK7pLkh1_2zeXIsRMz_urybKnZaBcuunbWU_E1jHclhARGT5rfWrZN5zheaxZ-kw--m5RZh0gVVIb9g3QhmhKmGp3Wpst7YByLQPsycrqjvWVjkXknFZtOiyu4RwPxNJWWq1p15DlfXVwsbAysNn7nG-5_JWi0Y_Y-D8P5qsr4aijqHRBP28RJJ9K0AAZ0kEtf0fAEWW3_joqWTRh3kXWH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: طبق متن موجود در تفاهم، فقط تحریم‌های کنونی برداشته می‌شود اما آمریکا تعهدی نداده که دوباره تحریم‌ها را برنگرداند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440457" target="_blank">📅 20:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub0JMH5zTIwFPYztqL0kCmi3dhLGakUBWQYPrYkqV--Dg3HjadqT7W4wg2OZoj46uH6wK1QC7o1Dxen8Zvzk3CkLUnD6S6F0ATlZudYL1-spy32_GVTJnrT0jM4Whm5CNEOygKzQBOXyMLg6vxJ2g7ppxv33-ne8q_x8Sy3x15AEs3II7Q3lbCa6raM-fVe-eqATeSzv4Q7kM7JqqhU-LVL84f8UrAU98Vaohb7FkLmZHHWvTTWCpyUvlJwqQ3Z0JwFwb2p9gGr7Q8_FiCfOv9tJyVUuI_fianV4vql8Hb_9B7eN5mTjnFwXV6uwO11VIqwdUmdd5VrsIQZUkUVkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت مسئول امنیت یک شهرک صهیونیست‌نشین
🔹
در عملیات تیراندازی ظهر امروز در شمال کرانه باختری، مسئول امنیتی شهرک صهیونیست‌نشین «تسور ناتان» به هلاکت رسید و چند صهیونیست دیگر زخمی شدند.
🔹
براساس گزارش‌ها، دست‌کم ۷ نفر دیگر از جمله رئیس پلیس شهرک «تسور ناتان» زخمی شده‌اند که حال برخی از آن‌ها وخیم گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440456" target="_blank">📅 20:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb3c4a972.mp4?token=Fe7OjmSnGu4EMrtWiiwUhklCzo0AD6TJUCynLy5YKfbBRBvxOrQJoW7M-M-rHNy4oukzWLOAYIHSjy6sDo2DKCBDvuvJ3Zh--Wb4lHuS_ZdmNUaqPfw0IaG7csy2zpE7hg7_gsfno-h2aHnJsu1EJVyD3i6H7IZqN9FMMZwxyBXWH6IwSSVmHM6xXiU4_tAYgReOa1lIP4drVv4V1ilcE-opTauRwWaFThLsIu0mVVTMiu2saz01f6294x3cghYol2DsOBv6bcoRTvy0cj7JS5-oxm6G_PsHIIMQ-hf4k5TFFf5T2FDkTtCQAXDfV0qZ9sh3a0GDbnkt3LwcEFz_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb3c4a972.mp4?token=Fe7OjmSnGu4EMrtWiiwUhklCzo0AD6TJUCynLy5YKfbBRBvxOrQJoW7M-M-rHNy4oukzWLOAYIHSjy6sDo2DKCBDvuvJ3Zh--Wb4lHuS_ZdmNUaqPfw0IaG7csy2zpE7hg7_gsfno-h2aHnJsu1EJVyD3i6H7IZqN9FMMZwxyBXWH6IwSSVmHM6xXiU4_tAYgReOa1lIP4drVv4V1ilcE-opTauRwWaFThLsIu0mVVTMiu2saz01f6294x3cghYol2DsOBv6bcoRTvy0cj7JS5-oxm6G_PsHIIMQ-hf4k5TFFf5T2FDkTtCQAXDfV0qZ9sh3a0GDbnkt3LwcEFz_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: جای تعجب است که ایران پیشنهاد واگذاری تنگۀ هرمز را داده است  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440455" target="_blank">📅 20:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
حزب‌الله: دستگاه اخلالگر ضدپهپاد ارتش اسرائیل با پهپاد انتحاری در اطراف قلعۀ تاریخی الشقیف هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440454" target="_blank">📅 20:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExCjEbak7vhlgvsDsGyFSOGFO5PME8Zcm6ZTxcXdXlhOsFjrh-GkPjzMijAv6RRBOeu0_URVITa0L3hPSd8AoiBmprwWLv3Lx8XBXGS1f_qMPkNuJL9EKLrAdWGj616IwRKo8XSBpqalwHhcO1ELd07vCryIyN7ntMj3wegfH1zX3GukRJL55bTG0P2IZBN7UaclsGTtZdCaJfA2Am2QxESqGARfe4TwxZZR94ShI9y81gjEb1WyQBXtgCIxXUETdkLykmXB6JELAEdgAaydECkOC4mMDJ30vyl-Ht8eN2-V7ZarEqWKeljXlsM1u1cVSrkd23MpID3Kb_cnKWJILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازسازی ۲۵ مدرسه آسیب‌دیده از جنگ رمضان در هرمزگان
🔹
مدیرکل نوسازی مدارس هرمزگان: مرمت ۲۵ فضای آموزشی که در جنگ رمضان آسیب دیده بود به پایان رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440453" target="_blank">📅 20:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قوه‌قضائیه: پروندهٔ عباس عبدی و مدیران روزنامه اعتماد به دادگاه رفت
🔹
قوه‌قضائیه اعلام کرد پس از انتشار یادداشتی از عباس عبدی در روزنامهٔ اعتماد، دادستانی تهران علیه نویسنده و روزنامه اعلام جرم کرد.
🔹
در جریان تحقیقات، علاوه بر شکایت دادستانی، حدود ۸۰۰ نفر نیز از عباس عبدی و مدیران روزنامه اعتماد شکایت کردند.
🔹
اتهامات مطرح‌شده شامل «ایجاد اختلاف بین اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» است.
🔹
همچنین برای عباس عبدی قرار منع فعالیت رسانه‌ای به مدت ۳ ماه صادر شده که شامل مصاحبه با رسانه‌ها، انتشار یادداشت و مقاله و فعالیت در شبکه‌های اجتماعی می‌شود.
🔹
با صدور کیفرخواست، پرونده برای رسیدگی به دادگاه کیفری یک استان تهران ارسال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440451" target="_blank">📅 19:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440448" target="_blank">📅 19:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
قالیباف: آمریکا فقط زبان قدرت را می‌فهمد
🔹
نه به آتش‌بس پایبندند نه به گفت‌وگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440447" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440446" target="_blank">📅 19:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440445" target="_blank">📅 19:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله راکتی سنگین چند روز پیش حزب‌الله به مواضع نظامیان صهیونیست در شهرک العدیسه لبنان
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440444" target="_blank">📅 19:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuNS32CuT_5RQe52GZw-RW43JmHcOQX8WSMoVO8G4ToGjhYx05oWqxADMWIuDWOVOJW3sBURSZQAY1C4GrjixWpQMCCgMpTECj2K6nGHc2DcxLSVOG3jPUxo8GvU7nEgDoQVqrIHYAxdbRRTCQGkesoqLW7P7eFVLN2W3r5Y-3Sl3pClqGo37W6q4rw4q_HCJTYNIdPH8XltzOT5_vTw4EOk41YXx0O-WT8xUvMuTwdoyVZDyUchMJOl7xUqsI7D8ujBCC4df8mdsXbXXQP3O-i2_sgf0UdBW_gvR-GGNXeQZA0W_Fz6B3GPhFvWRprH_ZgStn_9DVcWfSW1dnSz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
امضای تفاهم‌نامه تامین مالی نوین دانش‌بنیان بین بانک صادرات ایران و صندوق نوآوری و شکوفایی/سازندگی نوین با تاکید بر اقتصاد دیجیتال دانش‌بنیان؛ نقش محوری نظام بانکی در تثبیت اقتصاد پساجنگ
🔹
در راستای تقویت حمایت بانکی از اقتصاد دانش‌بنیان و فناوری و تسریع در تحقق سازندگی نوین مبتنی بر اقتصاد دیجیتال دانش‌بنیان، تفاهم‌نامه همکاری جامع میان بانک صادرات ایران و صندوق نوآوری و شکوفایی به امضا رسید. این توافق با هدف جایگزینی ابزارهای تامین مالی سنتی با روش‌های نوین و حمایت راهبردی از شرکت‌های دانش‌بنیان، گامی مهم در جهت حمایت از بخش خصوصی به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440443" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWoARGjZ4hrH84GjpBCrAyOwY-iFbJJ0adGQg_KkYSqE9GfHJu9U_tiMzTTgfoq_Rcxl4wGnZ-lsUMJIm9xeALJ4Sk0GhNGt12k5r6OQk2qWv6KYtx6QpMQhQb7F6APRfl0lZ8z0Gz25HNDuuq-znMn_CJLHAVpebkc7-L-teG2HXua2O0nRDy8XHXz6MizS_kKo_GGbLbYd1KQV7nzfZojmJBJDq60xPWbzA8whQ7-Psowh10I_qaStxGZsQ8ejC9qjaMHoF1T3ZcWzHZr_E4JoSA8BIspDde66IjE87QH6Nx-pzKMpVvXqw_ls74sc9TbvFBlVVbLro7MHKyCpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مشتریان بانک رفاه کارگران معاملات و فعالیت‌های مشکوک به پولشویی را گزارش کنند
🔹
مشتریان بانک رفاه کارگران می‌توانند به‌منظور پیشگیری از اقدامات مجرمانه و انتقال پول‌های کثیف به شبکه اقتصادی کشور، گزارش‌‌های خود از معاملات و فعالیت‌های مشکوک به پولشویی را ثبت کنند.
🔹
مشتریان بانک رفاه کارگران می‌توانند از طریق مراجعه به سامانه گزارش‌های مردمی معرفی شده در پایگاه اینترنتی مرکز اطلاعات مالی به نشانی اینترنتی
fiu.gov.ir
نسبت به ثبت گزارش‌‌های خود اقدام کنند.
🔹
دسترسی به این سامانه از طریق سایت بانک رفاه کارگران به نشانی
www.refah-bank.ir
نیز امکان‌پذیر است.
@Refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440442" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/440441" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxZJHTCd6-HJTihQ3a6pt_zfY9YShdm9Zp7gog2BJVNJeO2JmWmZTHzCVf3H8XI-AiLosJPtb6ALMOldVG4NLdY5MZJCy4UFIk7tLhSk9JIvBHyf18OHX1W_C6A8_JdxIMxDVArSgEC2zGIE2V7Tmva03XpwSECwM-LSnJW2ufVa7qdMkW3HU0mbZRfNKjLjxy8jdVslrhhbScbf1-PChAHSPgZVHJRUc78EBy1QcueVzQ6FrVHSTbbf2OkMkTUQYAskTP7RhKlFUPDbU9y08GGlSimwrujl4bMxkQ811Wgn0jY51RrgXQ794QnYQtR4mIiq_26QY67J7_nSFvntsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مرندی: صهیونیست‌ها مجازات خواهند شد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440433" target="_blank">📅 19:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-58.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/440431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۷.pdf</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440431" target="_blank">📅 19:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8f8a22db.mp4?token=vCfntdSw8d8_GqErWoI8d9skVZO0U9nY9XMS8ve66TkRKPQmbdo3G8Dhn7QaCQw64FxMzjv5YCbvvB5GGTBPXV35Mhx04wKY_ax1GI4wxBmJN6Ori29vf6gmcFqZHrAU13_iY5RQQIQYw-RGtMWHw6Qjd93KuuO3Q9bM14pn6Eyez3HLsqr1Uh-M3xDErP1ul2i4NNum5TZ5z970iiGPYJuwoauWs4JAgq8Wr3-od9-tSU-4ZkcxBOeeyl04bPyxDhOciRr6ESmHXIRPzzvqIkotnDMTYmi7gd4EOaFAYFEE5SIICkzJDt5h3vaLx5P8wwP_crqQ-SLRUok3II5jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8f8a22db.mp4?token=vCfntdSw8d8_GqErWoI8d9skVZO0U9nY9XMS8ve66TkRKPQmbdo3G8Dhn7QaCQw64FxMzjv5YCbvvB5GGTBPXV35Mhx04wKY_ax1GI4wxBmJN6Ori29vf6gmcFqZHrAU13_iY5RQQIQYw-RGtMWHw6Qjd93KuuO3Q9bM14pn6Eyez3HLsqr1Uh-M3xDErP1ul2i4NNum5TZ5z970iiGPYJuwoauWs4JAgq8Wr3-od9-tSU-4ZkcxBOeeyl04bPyxDhOciRr6ESmHXIRPzzvqIkotnDMTYmi7gd4EOaFAYFEE5SIICkzJDt5h3vaLx5P8wwP_crqQ-SLRUok3II5jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ با عصبانیت مصاحبه با خبرنگار آمریکایی را ترک کرد
🔹
ترامپ در اواسط مذاکره با خبرنگار رسانه آمریکایی ان‌بی‌سی، پس از سوالات این خبرنگار، با عصبانیت جلسه را ترک کرد‌.
🔹
ترامپ در حین ترک مصاحبه خطاب به خبرنگار گفت: تو یا فاسد هستی یا احمق، رسانه شما هم فاسد است؛ همچنین رسانه‌های سی‌ان‌ان و سی‌بی‌اس و ای‌بی‌سی‌نیوز هم فاسد هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440430" target="_blank">📅 18:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkClwBI3idoDUj-kV3NZvmo_-QRXMoqylMZ_QTtqNYk9KtQJCtfzBHlMF214KdY8h1vEXagQvZUXDcDIcu96GmN_hbzjI1-KyhCXXAgvF3GT4Uhkvo4kf6HkVQKxjF5Vl5RNq7dJ2f6vjFOyMaiUjXaaC8RSDSxMfFAuY4yiIMjUjkU-2W638gPkwWiVELBTZIrYgg6TClfOZBMwWufeY8ccd8AU7vbMfX0GHdUfdbY65Mi5EE-P8KstkMOcct7HNP_EaKncr9LrzJPzwYcrXeOxVg-qCHeD9xYQBTmPK_dNcaoLiych5AsNXQNfOCv5_VLJum6WTdvppT5r9xj2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: به حملات رژیم صهیونیستی پاسخ قاطع و دردآور خواهیم داد
🔸
امشب آسمان سرزمین‌های اشغالی را ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440429" target="_blank">📅 18:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-gUQXGa5TH1eTCKn5PBodOqLDgqpgIJhkofETh9_kIk581gxq2m2QeWuIpTvfIXUHAKaJPOUAgA7XWUZYom0Pptz_gSqwgS97r5PtZR4Szck2AZE2FJ5D03JC2TZThbwqrrUpIFqVx0vTqsxHyJGD-yxO5b_F3MApZWTW01EuhPYCp2xdswdjrLmCDVOiVWi_MuEuS9MmiFgUqViE8x4p6xVIQuBVCO-_3ZMbnhHKevWK6SbL-woPPAVFVPVnhHgyOuLdgyku4JvLrJoJfpkK8WjBcgzLBIX9l9Y1-SqgBHkq6K8DDYeCkLAxGcuKdx-cSOOCogm_HMQAMU6P-rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440428" target="_blank">📅 18:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvfSikICAkfwUk_1BRCpKNuFgCj1A8FN4UAAHmFSlxVvlehvyBTFjUeVkgT9ZnfJtIdvRLyQkKZcv5Q1xPJsbn3eFvhl6ymd9neiGWwk_wcZAk7kf8V4lEiYNcK8pVxyz1EsdggArKW-bZ617nWDCJaUGcDAVpZCXTHOtd64qXubLzH22BhX5P9XUKFtWXsYUUY7Kk5FZ4cvlPoXAy3SlTIKTPpWYp_jKUR0WbwFyHu7Bch_HMfF2BrQLhIuZbDbFwsT9FbRKYCDmGrYaBYuGTppjZU6Cofsi-fgBPzbFoBgrIi3sWE0A3rRHqp_8QQt2IeyJEY-5YBmUpqaZVEBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrOP_3-iTpaUtkzJ0USp1giDSWxW9cj5hmnNh1dLPC8SW3aUIREe7NMcj9UZVRWmYX8Nd2Vlrba8P_8bjrYTa8I6UF4oud14IJfOnCsRVz7hTBGXZFOrgK1eX9psLKVmmglCKxzQS3lmTA7AdAB1JCq98s8enisESnBiLfdJX0uAd8K1ulGjiTerbj_0zmH-7qKxwmGmsoxtypJGW_FYxo2llXSrS7EwhmIdjQfHbtKsI4a_ftphTIup7ZGj5sEWiRV8bZkWJERTF6QhfdW6h_QmVeldWxxIGYYJfCgFtzBXbMHMoMjwhwEpo-HLxUe_jOQHZoaE089VR_I4_Rd6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cu6gpeil7c4KLTd7CVaF0oC2AXac07cgB5avQNNb6adtT727TvdRG15L8w00nHYmRmHM3BehzEqUetKDQVweIIApATglAk4MfqqMLc0p499mJE5RPLV0g0ZzjcOzzg-HPBEGe346Dnbcn3V0yU5Gk6HadRUjo5_gI1NPTRzfCj416U4HTS0-o2KyFMDyieGvBXZRTnblZZ5ww5Lpm9R7HPCBmb4HLR5NzD-AonybhFOKqjXTLMNPANmU9XilaxkjWgsRVbl6b8mlQVNxo5J2QNlIPgJ79PRs8Jkz5z28UaI5wyoYkxsQ_OEqNzXSMwiruMp4N4QRGx9T-ksD7r4otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVr92kIb029aB9DQXinAkm8EUMD5kdLVIH2aUylbb-LpUOpKEWIWDQ5CrvWU_WEeQlLciavOnWSdE8ACEiUYs4QVDXy87JUlYqH7eU2ycqzCg3sNGWUJPJeZPXlXSMmmCB4jAktJsJzU_nNPhO8UV3cl33aug97jC2kDM9eWaIt2os9dt04wYhhOcnt9FNly0e6Ma9r44rjBl8Fbmdh65Sn14nCXVv9wgCXuugJprJWm_jDaTCQDhSdLrOiIk1_jmJwKiHmMr5yBZIh_Ae3m7RMamEnAiN0mESXvi557kga1CF-vGQcN_Lx-bXCKAO8-0SEXyHwlqQqo_I84_eDDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wte6MoNVxvyvFND3ycoaBhxlsdi6ImnRm-fILF4tjjLVeiB5oItty7k7XlEis92kLUbuy9gN9PnjOYg4GW4hOCC-XVllBxiLH9LXDSYpBEpkmJz-PnwteUJ3hA_PPKskfSd8EQsERRD1V2XzUREzmrNEAFWed-Kb3N-VMjGVYFiLiSxl_OyfqHlBjWt0P4c-zJuR7h1Pg2cCwIZAOjiA_hWZd_Mw8lz40GO-hHyMH3_aAzh5DcJO-WsFzNcUCdoTR0zZ--mmuxIeewtVGTLG___SmG1fz6m1R4_AsM3RHiJGqJKHDw20Y-XXdgD0xtUFZ6TsVrXRuYJ9TJs8NllTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdlZfJBVuXzoYWgfAKS8jsX9riHghG11g5nreE2zSEDF28K8tUi2xR9rbHtfappsSrhAMWZGZLRKLa7HQo8S_avPi_NRF4Wd14YBcVWh-1iqzDcXIhGyEZPmx-_UxXA0L1pe3ap6L4bWxZeyZM5TpzDbYTtCU3kgILwUjH_EbYhon8jxo-9dZnrGTXkm2KqwqPqq7kyFXq9CLeVTb7hEcIaUJWK8msFDXpqGPx8I7heHk7q_xF1O8GGjgyu8l4CTpS9AUqSkX4X8Gxng0zfXzS4sOfWNTKNkaJKx_EXK-G4SmWiRyqanykr8BSaX-TGdLFIuBK4PrZYczVMYBBXVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iloeN-s-8WfWf7mtEh6e8QoD_4rNx8h5UgU3eG3Ip1ksZRcEIDB3bpv26Xa9RJWibwJMIO4xfGT3375mip73kbGGIO1QNicqc95fAa-gscdtj7hmzU8gnlSgRvvILZTotOK-zaRKqs46EpPIGrkuvSgd1ktObPZu6VGaKAOKYie57X7tD87cxZTHkFo1y9gBoyjX4mJfOJ6-ZVU1Bu_dH4G6wsFULCIk0uLBnolZsnT5zhRHmFmc8GGvBenxbp_Ot8oDEfgtaO6UyfVj4NNwutRCd4CXvpVHfpZDe9vBByr0H7DX06vtxup1Ajyh3q3bv49n20ozLF6m02KjY4qZSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهید پاکپور در حرم رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440421" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
حمله به «ضاحیه» بیروت با چراغ سبز آمریکا صورت گرفت
🔹
شبکه ۱۵ اسرائیل خبر داد مسئولان رژیم صهیونیستی پیش از حمله به جنوب بیروت، آمریکا را در جریان آن قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440420" target="_blank">📅 18:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG3VD6UVoLgPD2eh3VkeFrRl_4r7Wdcd1S2rQrIyGZhVrsyIcA_qr5wL5wHaq6X0fvplYTYDsciNa9dr9DRByIhYHTPH4sp8C2LxaQkJaAAtgw7pcKbCAyR9O8nsOBqUM7uT1BqzKqLt4WGoxBg4_cxJKCvB7ZYk6wkEWAUC6ihaeHm9rqGOh25PTifnvoEA6Zby5qAyqjznWgq6xVbKZAtI7BtwICXm8fMyYiuUT4_9GSF0oALYWPp50truHHuJyDJoLjz7H1dicEtc9c4BQ82_UWZv43U7eF-1ZLLmgCmRePjLjhyaN8gBwbtQdso9HMRqsbS2SYzYXln5yP5ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdea240b7.mp4?token=aTEJ1eKFh4ashlTkppiLk4_XAv2_r1aEUHqx1M7U8xTU4MuL4HCJSTqyrL1tuqVEHjcK0q1fc9hvoQNB4u13ttOD38R8twvTWM8DvAP4sV-qTrSOKruXJ36DB9dgeBy38VE95bj9hpy0VWXbUzGYYu4g4uTvtPiqNqTVLI4oTQ6YZRrtP2iv2Mvfb65XIorD8F_S0mKhUKAHFlaCVhSAC-caX2aNvK0QQdIvG6vZr6sMgHvOET89BMxuofKRUuTreuDfDgsi9GgS89CdIwEBIikrPuUe8BTllSwhhyR7ONMwh-KfFEppy8maNnmmqqmIi1yGh0meS__EcewyPj1V9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdea240b7.mp4?token=aTEJ1eKFh4ashlTkppiLk4_XAv2_r1aEUHqx1M7U8xTU4MuL4HCJSTqyrL1tuqVEHjcK0q1fc9hvoQNB4u13ttOD38R8twvTWM8DvAP4sV-qTrSOKruXJ36DB9dgeBy38VE95bj9hpy0VWXbUzGYYu4g4uTvtPiqNqTVLI4oTQ6YZRrtP2iv2Mvfb65XIorD8F_S0mKhUKAHFlaCVhSAC-caX2aNvK0QQdIvG6vZr6sMgHvOET89BMxuofKRUuTreuDfDgsi9GgS89CdIwEBIikrPuUe8BTllSwhhyR7ONMwh-KfFEppy8maNnmmqqmIi1yGh0meS__EcewyPj1V9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم صهیونیستی شهر «صور» در جنوب لبنان را بمباران کرد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440418" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440416">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0036f2550.mp4?token=c802JoyXdRaTKbzIpzYpAlGYdOr2q69hlI5sDfJcjKxUC213Q4-bQJTQaABXtLZ6r6rW8OhdZl7wCfTWBYc7kbQfgaz16BM53-5WFmU__x8UXD6XraD-mnYqUQRR1zTiNiRxt52sV6jUu4N0RJT2OOuahsqRLrfm5rUYATq8y-yF23IJmSmGk-dE7gsUfDsk6gJU5a51WYQV-e_DEAEb7od3dsIEnaK78-2djXXRvid7Mo7fDWLnGNXi8ZDE_nGop9X8S9Vt2E-vcGzRpEZF1V0j95Z-_GkR9ty0RehnnEu0gxmldl3Udwoyz3IpVBghwPKHKqTp8y3A4_xzfLHXgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0036f2550.mp4?token=c802JoyXdRaTKbzIpzYpAlGYdOr2q69hlI5sDfJcjKxUC213Q4-bQJTQaABXtLZ6r6rW8OhdZl7wCfTWBYc7kbQfgaz16BM53-5WFmU__x8UXD6XraD-mnYqUQRR1zTiNiRxt52sV6jUu4N0RJT2OOuahsqRLrfm5rUYATq8y-yF23IJmSmGk-dE7gsUfDsk6gJU5a51WYQV-e_DEAEb7od3dsIEnaK78-2djXXRvid7Mo7fDWLnGNXi8ZDE_nGop9X8S9Vt2E-vcGzRpEZF1V0j95Z-_GkR9ty0RehnnEu0gxmldl3Udwoyz3IpVBghwPKHKqTp8y3A4_xzfLHXgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها با پرچم ایران به استقبال تیم ملی رفتند
🔹
جمعی از ایرانی‌های حاضر در مکزیک و بومیان تیخوانا با در دست داشتن پرچم ایران به استقبال تیم ملی رفتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440416" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsNeXSrle-Uur0-n82Kcimx1VwqceygdT9dVVg4DKYjjdGW_yEFHrBy8zHE6BlEsXvJKAt_ZlzygQlAj6ldXOJrNtJy854Ces6uCjgpF-UhhR8q83yVQb9CGzSfIWvNB89LwWwLDsN_Ej7j_gAYxZcgtfDdHPkbEuHQdRqOsi-YqnQZhXa11VwYuURat8afKY9k9_F_9Y0jzwyDM_hiOXgbdyVzc2XjOFV3tIbFfOv_WNHvWnmtihJri8tZI5ZU9-lv5bkezdH2wuzdDk8-1xJgr0IWpNxjT4gOqKNP3whnt7KkBx1er_aVDndczjl5jYE6ib11e8fxv2DtqxZdbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قدیمی‌ترین مناطق حفاظت‌شدۀ ایران جهانی شد
🔹
منطقۀ «قمیشلو-دالانکوه» در استان اصفهان به‌عنوان ذخیره‌گاه زیست‌کره در یونسکو به ثبت رسید و شمار ذخیره‌گاه‌های زیست‌کرۀ ایران به ۱۴ مورد افزایش یافت.
🔹
قمیشلو از قدیمی‌ترین مناطق تحت حفاظت ایران است و زیستگاه گونه‌هایی همچون قوچ و میش، کل و بز، گرگ، کفتار و پرندگان متنوع به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440415" target="_blank">📅 17:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440414">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQhzXMu_k9mPyWxsUHDeaes4z0dDKuI6apF_iTjrHtoIRmY42x8uHXHtblIYMKLckfcLpvYCig6oUxlN9XK_vm3dFQXcPtl_LB4GbUzgMIcCKs1OrMtgT_T1sFuE3DxcH8z350IpabkPVNHy4pOiM4H6Ue-UPA-DFrgqHQChUH3tNzARxR8E6mFILY6HOlZKkgBzD1-rUg60p2qu56-RIn3K5MH20LJaJxXmiIcWE9ryRs4K1o9KYJPVoCArjuulUPlugcolnbrtsuDrolvw8hzepgOQ9Hy5hqb89b6dL1Xo9ChVWMIOwu0PeKcGklBSs1-vwSyGWWyHYnPVjSAqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت عوارض محیط‌زیستی در تنگۀ هرمز به کجا رسید؟
🔹
سازمان حفاظت محیط‌زیست از نهایی‌شدن پیش‌نویس نظام‌نامۀ دریافت عوارض زیست‌محیطی از کشتی‌ها خبر داد؛ طرحی که قرار است پس از طی مراحل قانونی، برای کشتی‌های عبوری در منطقه اجرا شود.
عوارض برچه اساسی محاسبه خواهد شد؟
🔸
نوع و ظرفیت کشتی
🔸
نوع محموله
🔸
میزان خطر آلودگی
🔸
نوع سوخت مصرفی
🔸
سن کشتی
🔸
سوابق تخلفات زیست‌محیطی
🔹
سازمان حفاظت محیط‌زیست می‌گوید خسارت‌های ناشی از جنگ نفتکش‌ها، جنگ خلیج فارس و سایر درگیری‌های منطقه‌ای، آسیب‌های گسترده‌ای به محیط‌زیست خلیج فارس و تنگۀ هرمز وارد کرده و کشتی‌ها باید در تأمین هزینه‌های حفاظت و احیای این منطقه سهیم باشند.
🔹
معاون دریایی سازمان محیط‌‌زیست اعلام کرد پیش‌نویس این نظام‌نامه نهایی شده و پس از تصویب در سازمان، برای بررسی‌های قانونی به مراجع ذی‌ربط و وزارت امور خارجه ارسال خواهد شد.
🔸
جزئیات رقم پیشنهادی عوارض هنوز اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440414" target="_blank">📅 17:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqoSj3XNLsdaDPQCIclet_DNOcFZjQrbWPV73FqMoqCK7KbIqiQtYTRhfWJEZlC_k-W6SMzRG-CDAUiLrLZPwoAMXmJvl06qMdLaDttZXQI3LzEH5jcg54xaNHCcTx6mjGiEKi8hpOy2C2godsPYVmevUKcA9fqIp0Xd2x86iQI6sGxzWH4qPfnpsCMa20JNZDn8AH0IVmnvvuUYiNPQ58my3SQ_LT3gTbbX1vWHuPmAvLrpeNgI3iT3JRIAxwxOwyuwh6MMLUtbbSeoG5__F92uU0PPN9OMrt05V3TUMS5BHHZjMtEjaWdja0JOYcuk-hi9d1nohZxTsYKuSX_1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkxIsxucXfknsmaZ4N5qGERZBhkw7EutmNrdP8Zr8n-4GzCqQoL2dQL2xN1KljLQ_4f8rAaQ2bn7pBQKPwbVGaIoYXmvfES_siXMxObxJykFx3INiA8CaXNqI1ecwUnjYEKaxdQibgXLLtg-KODt9i6Bx4u679PzeobEJy4u71PWHJFHCLaqnxBSbqNFtF8xxB9Z6XRh3MPsLQ9M-9KtZtD4rW8UtfPB_c15DQ2GBSlvB8Q04ASNU4mCQXPX8SGhVGBwqLx0KZDoOZbXcKy1M7UBVSs83BzrG4tTwV6k1lmRhQ3a52DBOiR7j9W07kW34kcOOKULfG7YRwi9Tam2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bplvZaOyKNE8L6YppUTj52RgWMeqGP1JbGL_V2eCv2g0awawLFZT2vDDOCqaDy2QYoW3002WVHypmLhhCgWRyZ4fPw_sbovwQXUvggYofPN6hCpveSgZN2WfrJimsZSved8ae25jikaaqJLKWyL-tEKCVWQu4qfNiUYow2tICeUzAKqHb5PAx4i-R8DsA7NUsI0ydJ7KKmxYuIXhnAi3FAuXthiXyygLHwYoZ55nlpjUTW39x3slzluJlQoJl4abTNgTArEzb5wZm5dcdPRslHTY1tzoKdwoYhKtBK1KfW_Y5TOylqUO37DxHaocbBet5eVFTLCxvMZ3CQSng0qAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jR1YqpuD2oTPj_pcIIxfnb67iFwzylQ6HKgQt72-_-fIBNku91gAHylrwQa0GRWN3vl3scP9ObWQAmh8HGTVwSOal2rWUGskFcYCejx9ZWz8e6PNGOwzKQJD9XooLWcqyJch8s9EDR38szcnDkL6Id7nL8FhNutF63ecSs2yMR8muCbPGA-j1Iol-moSzRCNcBVVBL8KchVKpWOfPIzaq6vGTHGWzrLC-43MQIxBiHRpVKBfGpgV1iifs_21LNwdAvUQDu5K65sZiORO6020h1ajsvkHIhrVOX8lZs-ST-9q4XLMD86G_QTpB9UaRzlKuyqvBvdf8vhgGF3fMR3-pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440410" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1759b086c7.mp4?token=vZoIOosMjlFE-aytu72PNN4v1nvKXPMu5hpbEpGNt0S2a6oZhHktN5sofdIPU9KsHyPmrEbGY29gWh5y5q_2UdAUNs158fdvZ-RAPG7B3_gLHBqDReI5qHUhztElv7e9mg8zt-AmALFBl5BuYr3xPeeR8wxW8nJy21D82wZjGNOqeXVg_4A0Am1TOIyQPGAgupoUzyVwYlMMv554iKedArecmvJHvy5nENp-URrx-tv3yNzvJqlVQaRGIes4dtCFEBoEa6GlEwxKLoEzivcnOtPIRCWvUkJVDD_MkcQuvmFE58HMquuJiNlvBvdjjpDYdbk_QyPSuTlThQ-ouLUkWC1QvQ0YzfWGKWGJEukEyBdYzSONPHY0fxukVYFku2wAN_hCFmenF5kt6ory_4iPnKAqOzmTYShGmr0uv7flGzoHTREfuugPiQPYzC92JxEd_KmDO6rhVpkusHWXlK0BwB9NqD8WEcX5xtKHecV9dXyBf75eV2JljsQP9vgc-6CTpg3DLWNbFR1Y5ol23fn9J2W5evzR4HacuXrXA_vtoCliJbzovK3XlSLTaNtJeBQc6WJDinzgwepSLqdMHrCR0yzJtiGURGFmtgXIChavAB6sEEX1WZGGN3NYHXAR9ZHoj296n8gO7PXKtzcwPFkmFoAwJPMCcO0TLX0MsdiS7_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1759b086c7.mp4?token=vZoIOosMjlFE-aytu72PNN4v1nvKXPMu5hpbEpGNt0S2a6oZhHktN5sofdIPU9KsHyPmrEbGY29gWh5y5q_2UdAUNs158fdvZ-RAPG7B3_gLHBqDReI5qHUhztElv7e9mg8zt-AmALFBl5BuYr3xPeeR8wxW8nJy21D82wZjGNOqeXVg_4A0Am1TOIyQPGAgupoUzyVwYlMMv554iKedArecmvJHvy5nENp-URrx-tv3yNzvJqlVQaRGIes4dtCFEBoEa6GlEwxKLoEzivcnOtPIRCWvUkJVDD_MkcQuvmFE58HMquuJiNlvBvdjjpDYdbk_QyPSuTlThQ-ouLUkWC1QvQ0YzfWGKWGJEukEyBdYzSONPHY0fxukVYFku2wAN_hCFmenF5kt6ory_4iPnKAqOzmTYShGmr0uv7flGzoHTREfuugPiQPYzC92JxEd_KmDO6rhVpkusHWXlK0BwB9NqD8WEcX5xtKHecV9dXyBf75eV2JljsQP9vgc-6CTpg3DLWNbFR1Y5ol23fn9J2W5evzR4HacuXrXA_vtoCliJbzovK3XlSLTaNtJeBQc6WJDinzgwepSLqdMHrCR0yzJtiGURGFmtgXIChavAB6sEEX1WZGGN3NYHXAR9ZHoj296n8gO7PXKtzcwPFkmFoAwJPMCcO0TLX0MsdiS7_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی بازیگر: کسی از خارج ایران حق انتقاد ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440409" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
آخرین خبرهای حملۀ رژیم صهیونیستی به ضاحیۀ بیروت از زبان خبرنگار صداوسیما در لبنان  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440408" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e688388c.mp4?token=Qm80MivgIo_Ji4WQ-O-RsJXJZXipnSaqGtX1hdHpJYtkoAPg0MoAWq-HBf9t0zTzN_Ig2z75_M4rRNFnNWbjiGPsJRCPVELReB5M_bPAqj4l9Qb7whUPmz2OtBQySx8G1xbrsTdG77wErqY62RObuAVj3CPWQ74yPCrkogQa2WaOImzh7SY6mfzG0SD0vqRFHR21dKP2V7j02dIpNxSTt9njD2DW-_6bo5V2Jwg7h63E_eU9uVKUuRCsh-3upLzRui-jAvPI_Ip1z40hu1bzfqowaLIuGq58FMwaQdTcHVFoQT5-Jeto3Vm1USK8ELy-wkIxWY0395mlc5sCqvzCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e688388c.mp4?token=Qm80MivgIo_Ji4WQ-O-RsJXJZXipnSaqGtX1hdHpJYtkoAPg0MoAWq-HBf9t0zTzN_Ig2z75_M4rRNFnNWbjiGPsJRCPVELReB5M_bPAqj4l9Qb7whUPmz2OtBQySx8G1xbrsTdG77wErqY62RObuAVj3CPWQ74yPCrkogQa2WaOImzh7SY6mfzG0SD0vqRFHR21dKP2V7j02dIpNxSTt9njD2DW-_6bo5V2Jwg7h63E_eU9uVKUuRCsh-3upLzRui-jAvPI_Ip1z40hu1bzfqowaLIuGq58FMwaQdTcHVFoQT5-Jeto3Vm1USK8ELy-wkIxWY0395mlc5sCqvzCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرنگار الجزیره: حزب‌الله با یک موشک زمین به هوا، یک جنگنده اسرائیلی را در النبطیه، جنوب لبنان، هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440407" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4ba37fd4.mp4?token=jlxmXkOQWa9ipJqQodewm3mgjNHxb1HoV4uaJ_E4C-20z3jCcVlfbWgwEloDZLykdja1dLeVSfT0qs_4I8O8A8SSdlL42WTEtmmt1Edu-MYUbsK3v3dF0orig4lrbH_F3boYfErdFhYgFn4r13qaHtCZkOuZg4Uj_51UoejzYD_VYlDd_QVUJPpCzAgmVZgAhvBKl5oZYC-ax5P2S5H-nWlQfFIoLZ_FI3o4DAv0FuzO4zOZ2fsRvxbeG8iXrk2SE9JmwS7ILWUZHqpKlAJYz9u_aY0OEryML5bVvQLkCov6ZVyY3PcFuZJvKBm3lPgZG8Om7tUd2GYtg1M6TQWerQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4ba37fd4.mp4?token=jlxmXkOQWa9ipJqQodewm3mgjNHxb1HoV4uaJ_E4C-20z3jCcVlfbWgwEloDZLykdja1dLeVSfT0qs_4I8O8A8SSdlL42WTEtmmt1Edu-MYUbsK3v3dF0orig4lrbH_F3boYfErdFhYgFn4r13qaHtCZkOuZg4Uj_51UoejzYD_VYlDd_QVUJPpCzAgmVZgAhvBKl5oZYC-ax5P2S5H-nWlQfFIoLZ_FI3o4DAv0FuzO4zOZ2fsRvxbeG8iXrk2SE9JmwS7ILWUZHqpKlAJYz9u_aY0OEryML5bVvQLkCov6ZVyY3PcFuZJvKBm3lPgZG8Om7tUd2GYtg1M6TQWerQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440406" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌ سخنگوی شورای شهر تهران: طرح رایگان‌شدن مترو و بی‌آرتی ۱۰ رأی موافق کسب کرد و تصویب نشد
🔹
براساس بندهای یک و ۲ این طرح، شهروندان خوش حساب در پرداخت عوارض و دیون شهری با تأیید شهرداری و همچنین تمام شهروندان ساکن یا شاغل در تهران در صورت احراز رتبه در باشگاه…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440405" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqGBIu7n1xXlvcMxicTYuTf7dviuCYKuqLM2wBi7EWsRYuqkC7zmrWW2tN_x-8heTW6mJwh0BiHprqI9KNygP0p2JpsIuKJHkZMLNgzYxn7j1CWNdHcMdxcHENo93ANYdZlroqEbCuP503j2Emnb-lkIUom8JMrVZ8uVF7VZc_FcRLU-Cc1-I_YqJsZStEF5eMY4XrSO5Vv3_8EocxQYJMTE6d_IBZ0fzLOIcokx8ACnv1aecoPGyDUflibjurFAw6koKezobhfHM2lrVxeSS8nsXRTG_2ujrpWE-HdFMF9p0QjyB8bM88ALXQ6obwXNQr3Mly1aIl0JmxD_MwL1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440404" target="_blank">📅 16:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440403">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f57S0iw-weZ57lEvJauLfeppRTBMRi4922mlQEnLTPZxefZFZtWPGM5l7QHBCsKgGQ_UAHkP6BqReKHP8y_6aRp5jFA_rQPadKr4CQNpNvZ8lmppbbs5aAMuJT3AkxOIaCwNrX6KMiWL-_D8puPv1CtUEKOdi826VL8RE2IcEVUK9YyLcpYQKuGxoAPip5cAhqoO7o-dKzJduJdhsB9tstSuQgTClbjU9DC3BK61jK3PINwtZhHJRs98U7OK5b6gZSDL7-6PHhyzRlP0p7Ogs2OiHuu5dwMgBdzx0fyOouXly6YPJPN8kmtXFtJJbl2fnx2anrzG_vBMYQ76JmgCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440403" target="_blank">📅 16:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440402">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ ‌
🔴
رادیو ارتش رژیم صهیونیستی به‌نقل از یک منبع نظامی گزارش داد که ارتش رژیم از ساکنان شمال اراضی اشغالی خواسته برای پاسخ حزب‌الله در ساعات آینده آماده باشند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440402" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440401">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
حمله به «ضاحیه» بیروت با چراغ سبز آمریکا صورت گرفت
🔹
شبکه ۱۵ اسرائیل خبر داد مسئولان رژیم صهیونیستی پیش از حمله به جنوب بیروت، آمریکا را در جریان آن قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440401" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
