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
<img src="https://cdn4.telesco.pe/file/bdiIB1ufgds_E3tQk2lgIldjwrghyjnbu8VHMsHfO90aRfeGHMD78K1QwVAQdHyE15gIgA06awTCG08tFtHFacIggDVfS_ywEF7P_2gnhLHn2wEauSHUSxG-xGOsiXSQFJaRFliJOQLv4eyETUiPIPP-MbE3KHDsGBo6s8MpRroxOHMPO5RYSr1ZLj_aonFHwdRY6SNR02MGD8tmiSbdvgKrZsNU45rwFXAlL8-P0jEJWibaATh5U1FffdIvzVGbWHHmdYHKfvpQUOQCgiAGBjRxSHjWkEMRyokzky0bBf1sYlGj4pSHw4e-PyZ65qt4eO7QO4J-4dmzspcv5s379A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 16:33:50</div>
<hr>

<div class="tg-post" id="msg-122337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: اطلاعات حاکی از آن است که یادداشت تفاهم شامل توقف جنگ در لبنان می‌شود، اما اسرائیل از این توافق رضایت ندارد و واشنگتن را تحت فشار قرار داده تا بندی به متن یادداشت تفاهم اضافه شود که به اسرائیل اجازه دهد تحت عنوان «اقدام نظامی در صورت وجود هرگونه تهدید» در لبنان عملیات انجام دهد.
🔴
ایران با این موضوع مخالفت کرده و خواهان توقفی پایدار و دائمی برای جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/alonews/122337" target="_blank">📅 16:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAw5QYrSvg9iuz7n4ythMKZDs-DbKgxoKgJWxk_sDjcOLSJ19cr80ALHqwHVFPPm-Bjul-9sU2aBEk9x8rC65eLdXOGNmZfEf4h1KIFUQfcs_cKQOJw6kuNGzS_FXGvqKwPz1i1_ccVrA_XSFpztmBUja_NWc0IAG6CnHuONtTDr3j8f65UqxeG7rK2Mk3Nq9RQt82SAi-A-0kqj2RrmiXXRR9X5T0sM_msmqFzThncYqsxMg-ztD3p0LoaQHMngButfnpPjjLHqYkA0KgWu-IMxeYFmoMMHs5Pb54lxTTepr8uaL6mWmHdVqa1iAjLjtUz5QfaYF_qVxREm7gL5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f7ec9925.mp4?token=k7Sf8Ml7QzSDE8iQNpqNexi-_b7ZRWnxTuGiC_sy4u-WryS0w2PZQMJhyVJstTPN3Y05fzZj7DMxA8Btgn9YtRssX6CrX85Hv1HkKNbEwr5KdD-eifMWeCO233MCeUENwNXifR1HW7HJDhgAY2xVonB_lPVovRzYVDqHrqqrZ_oxGGALztvSivhcivjIZDW2lqFlul2p3Vtpfx6IkdcAbeHOfy2v3ePYUX4D7SZfYQcykRhfqnc54nDzVVsKNGHq8M4GvqZP_auOpexp33pyF6wjlpr3lZkKFkybLiEER7BTAIik3ch9cVVW988QL6q45UKS9u7B8qYn7nSxWnkUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f7ec9925.mp4?token=k7Sf8Ml7QzSDE8iQNpqNexi-_b7ZRWnxTuGiC_sy4u-WryS0w2PZQMJhyVJstTPN3Y05fzZj7DMxA8Btgn9YtRssX6CrX85Hv1HkKNbEwr5KdD-eifMWeCO233MCeUENwNXifR1HW7HJDhgAY2xVonB_lPVovRzYVDqHrqqrZ_oxGGALztvSivhcivjIZDW2lqFlul2p3Vtpfx6IkdcAbeHOfy2v3ePYUX4D7SZfYQcykRhfqnc54nDzVVsKNGHq8M4GvqZP_auOpexp33pyF6wjlpr3lZkKFkybLiEER7BTAIik3ch9cVVW988QL6q45UKS9u7B8qYn7nSxWnkUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های ارتش اسرائیل(IDF) طی یک ساعت گذشته چندین حمله هوایی به نبطیه در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/alonews/122335" target="_blank">📅 16:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30316b65ed.mp4?token=Z-cHUsEpjmI3srcy0b8s-GG8FEl86i3RWT5HoTZ4pwieNySqtUXGB5Ok1nnySvS2YWRbRS6f5umm90O90KiFc_7u3DQ0jOlQwfUUmWYckGwivdXi_tPIT6N-wUT1hBnhNS4s9kvomF1k1vlH5OuGhiHZDZK71u3FqGioM-bKQYr_0CWtaGI3llQzuRuTCtpS0lWY2ICZmxGtbXMF0UZaBwZbJ7XPvY522s3aczh8c6v0ucW560gNSHviXh8FbWX-w4vZ-sGA0VpMU9I6dfHHXdrA_cWhngdNJCoIw6LJbLJbisrlDYSNwu0HDwsjDggYassTZE0RkroVeN2khuAI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30316b65ed.mp4?token=Z-cHUsEpjmI3srcy0b8s-GG8FEl86i3RWT5HoTZ4pwieNySqtUXGB5Ok1nnySvS2YWRbRS6f5umm90O90KiFc_7u3DQ0jOlQwfUUmWYckGwivdXi_tPIT6N-wUT1hBnhNS4s9kvomF1k1vlH5OuGhiHZDZK71u3FqGioM-bKQYr_0CWtaGI3llQzuRuTCtpS0lWY2ICZmxGtbXMF0UZaBwZbJ7XPvY522s3aczh8c6v0ucW560gNSHviXh8FbWX-w4vZ-sGA0VpMU9I6dfHHXdrA_cWhngdNJCoIw6LJbLJbisrlDYSNwu0HDwsjDggYassTZE0RkroVeN2khuAI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی کامل در عرب‌صالح، جنوب لبنان، به دلیل حملات ارتش اسرائیل (IDF) که کمی پیش انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/alonews/122334" target="_blank">📅 16:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea7eb6513.mp4?token=nXF4GAoaCOAVwSh55BVtTpzQmTWez54pyUymNlvCB1P0PpRafajxuCEqzG-HZHMrXBJSkmlk_WhKnUMYywDCAaWmaAIZPwMT3LDsz_6Ou8T-cnNtC66QY3aHjRIBgwKByAgyJbyhvZIedT3ENPK-UkiBbc1cijK5S9BwJC1nHoZBt0Fwyy_5bMjcbgxBAUVWCGeG_F-iP6tdbQYBwoTuxRENasNwpfhM1b5s_Qy2dNTDMbfRcArBYuJIQKbhePvdjm1cEKWPNshwdSkyWZ9igeqJXaYQx2bDmnzpEqd-L0ru1340rEw_hvU1kdLGOoNLBjOQS-xp8itOPEpmgFDvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea7eb6513.mp4?token=nXF4GAoaCOAVwSh55BVtTpzQmTWez54pyUymNlvCB1P0PpRafajxuCEqzG-HZHMrXBJSkmlk_WhKnUMYywDCAaWmaAIZPwMT3LDsz_6Ou8T-cnNtC66QY3aHjRIBgwKByAgyJbyhvZIedT3ENPK-UkiBbc1cijK5S9BwJC1nHoZBt0Fwyy_5bMjcbgxBAUVWCGeG_F-iP6tdbQYBwoTuxRENasNwpfhM1b5s_Qy2dNTDMbfRcArBYuJIQKbhePvdjm1cEKWPNshwdSkyWZ9igeqJXaYQx2bDmnzpEqd-L0ru1340rEw_hvU1kdLGOoNLBjOQS-xp8itOPEpmgFDvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سهمگین ارتش اسرائیل (IDF) را در تپه‌های علی طاهر در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/alonews/122333" target="_blank">📅 16:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پاکستان تفاهم ایران و آمریکا را بدون نیاز به حضور طرفین اعلام رسمی می‌کند
🔴
به گفته این منابع، توافق اولیه و احتمالی میان واشینگتن و تهران تحت عنوان رسمی «اعلامیه اسلام‌آباد» نام‌گذاری خواهد شد.
🔴
این منابع تصریح کردند که توافق اولیه در واقع یک «یادداشت تفاهم» است و پس از امضای آن، روند گفت‌وگوها و مذاکرات بر سر پرونده‌ها و مسائل نهایی آغاز خواهد شد.
🔴
همچنین مقرر شده است کشور پاکستان وظیفه اعلام رسمی این یادداشت تفاهم را بر عهده بگیرد و برای این اقدام، نیازی به حضور فیزیکی طرف‌های مذاکره‌کننده در مراسم اعلام نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/alonews/122332" target="_blank">📅 16:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رشیدی کوچی: اینترنت این هفته به حالت قبل بر می‌گردد، یا ۴۸ ساعت آینده یا تا پایان هفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/alonews/122331" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اوریت استروک، عضو کابینه امنیتی و سیاسی اسرائیل، به رادیو ارتش اسرائیل: توافق احتمالی با ایران به معنای عقب‌نشینی ترامپ از اهدافی است که خودش تعیین کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/alonews/122330" target="_blank">📅 16:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evzjqr5DiLKVeMCGjrrK_J9-g18F5hYp5s3ZaXh_fjWT5D_cDtT9zqTVuuRqDwlGy02sI5y0dU6DnEaxkWcC8lZVGiLMJ6THTv_2W_AllZgqtLN6WsAzNagD-eSlE2Odnw7a6q6onhiPC714qni2EY252Yxie3vH1EagOG3ZHHq9vAnlteMiVd3qRUh4To2zuJrKjHKCRR6htSVRWUYhxoE27o09GxZ6EXaLqFYfWmbYMR8OLguWlJ024jQQIROBVGezH5WX3GUuMNMkouO0DnvOhBY5xbZObyih1qQlkXTas3G_Gwhq0bmCCrMjmnlSP-lNmyzSaYANuO7-OmrOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: این گروه بد (بیمار!) است. بسیار مخرب برای ملت بزرگ ما.
🔴
از طریق تسلیحاتی کردن باعث خسارات عظیمی شده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/alonews/122329" target="_blank">📅 16:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIYC1uqrwW-78g6jJzth0wb_xUj5pMuHLTQ-8hG2NmmBuz_vjzsCS1ysYnuSx9_FPPjouo9gr56Y4V75zwjxUBWTID8QI5SMDorbar-MB5EUnyPH6nXh84H6Y_2lUuylkGKwTQov3wFR123BmqVT_N5ACXGT9K-km7vtvF8QiyAy91IzKhAI7vRmuKmPbQxXlGMVr72EtU0ZWp71RJ7_gvkj-Wj56LOAsStltk1z4tPfucGjHO_W8g8u-zngwDVm8Iva5HRX5vE7PyKW_H7KT6Gtmj0wiWAhJI3b7OlTxGtH2CW8L-AoIcXc_SfbeP0gCj1nl6FgpsdLv_-H6iV7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی از مجتبی کیان اعتراف اجباری گرفت و در کمتر از ۵۰ روز اعدامش کرد.
🤔
خیلی ها حتی اسم این مرد رو نشنیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/alonews/122328" target="_blank">📅 16:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
زنگ خطر شیوع تب کریمه کنگو در عراق/ 4 فوتی و 43 مبتلا از ابتدای سال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/alonews/122327" target="_blank">📅 16:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmFeDJ9onn56oUCRwwUsHSZOHjI_x6iLwZsQSochdkvUa01okLxoC51vXojG0ij6c5bOuCZODWEZ1h8l_Bkq-Q_514tndhXxAp3W-t-5U1jJhzxPx2YfDzsti9g02Yeo9Mn72p1dR72dX3c4NAxzAkfEJ8TwFWN1D1zO7opYeP7f5ATREZzX7-xTklrPOczuXvOszu0cUiAzAIJdA_QlSZv6HBe3HYOQOOjaj26gXHQPSyuDB0RFbXJsSKV-GkVeED3_DUTIdmZAWeXfVQJ7-wjLwPg7Y8WhZNzV4QPiPvqOE19zPxGX0Ty3KNhKuOV6Wap7tozHWvSpzY_yXueYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از لاشه پهپاد جاسوسی اسرائیل در هرمزگان‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/alonews/122326" target="_blank">📅 16:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCKcSP36p7skClPITqh3TlRnteDjZNQKMDcTY3YFqlLekZ3adoZ6T9VtpAMx-IyUK2yDFHzY8XTY6__gW9bfjRW1ACBBmsaREqkagH0GZVYRTNmVpeA210EZwF8vGvjcg_P_S6SnHgOH7ACJ2AlmeHPGeu1IVJwwLHieVkkmuLZ49fbRUmqysTEhOtsg1bHz2C026TIdAg-X97LBiRQhXRcLr3xYeS8EdHDwN5LB3IKQvIMA5BtpKi4_eY1-_YftN1i9C5EpmnK_wuxDkKO2NInfp_-9dNoLfRMsAFoZtpA38lqlIRoxmzI_O0lmlyCDzEuWGnWhkYxdB7O0x8Zr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VB6okloaCb2WbX0QhOlH7NtgwWzZnU451A0kzcA66o0GrwgveXfnlANQDy1nknykxT2mLRRiEClU4js0Y6WAbZnKU0LZ4OA1llglh4ShB8x4tse357d77rQPw0Iv7MCMru16DmKIEdKfTOLLpIGb5ILJTmm2K1zYoFCmeBLbQCZlafN5dUfXOsTM75Hv2Xx0ckeF6u3zgtF2x3taBQtU-59uBeec8i8jeLmVisTeRl7O6qsfvhg9Q2em5aubHznK81QQO95NXxamFuJnKRl8VNCw_AJbCiUyIHVF5_XbmwauPp52ZUR-_8CeMoSaapNYkNk_M1Ri5H0ik5W-UVCcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVoKZs8600xEXtovsylLIG61yNRLVsrd2WwqkSXlzDAqE8LocXSlDuZ5-ZO1RbSJK5gKbr1Ijx3-_lfETMYkm1eCdJsJRzADFj-zZWJYOz5ZALMW3YOUpy6uetpA4gtZyqcWqHpeg_0rzq_Z2r7VqlOPbmT-sY4X5zDCc6WNzi9ejyqEfFbi3a9nWq9UVs2xo3HAdSKYAv9TEN-f8uYstLTVe1aGKy_vRNubSUoCsi_YT7Qvv62Iru_Z_Yv8SbDl0tuQQSEjGq5oerTaZn3MAnS4LktCrsI7s591gpbZmsTRM8oX1Wmw8YHX_i7q0_CmSq4n5AujqBbsF-V6RU4Kdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ درباره چین در Truth Social پست می‌گذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/alonews/122323" target="_blank">📅 16:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCP11teqmpCFlUZk3yJOM58c64VP3Q0ax-vfrzKPtpxFsO5_sW3cxEQtCkU272caKjwKwzKYjK7ALQsTms0saormmoXKAA1ljWwKKyg5jNsw3PjLZb60X1Ty3SCe8qEt1nIGdgIbuKoqqFYXUW5m73SccKEvOZLcrm0xqLitzf2RA1wdRUVGkzEIo_Qqe2nzJRYbKFLmAc0O3PME0LG-TPWEcLJzUEYHSRhljUgC5iWoW2HNOY89viNkHmgLDBycWLYg5O_a0PpbHdQthSgB1l4n0DEpoYGvR716JCV7ae6liohm1HzZN_i6ygBgaYjR43oCZ7pchhXiOxCFk95nMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی؛ با اعلام afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان امسال مشخص شدند.
🔴
تورنومنت 6 جانبه برگزار نمیشه
🟡
سپاهان به لیگ دو آسیا رفت
🔴
پرسپولیس سهمیه نگرفت
@AloSport</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/alonews/122322" target="_blank">📅 16:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رویترز: ایران با تحویل اورانیوم غنی‌شده با غنای بالا موافقت نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/alonews/122321" target="_blank">📅 16:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYlv4m5lP2KibqkLz6YMi88y0JFgIPZffRpTlwVzha4HzJTwHuFAnWA5VhExPibCNMbFv2Mjj1UcOihnKra2x3ith5G_dDc4ZlwZDdFZHj8XpXCsKrPL37xhLtdRckJ7ULZ62LHx8_JwQVRjTxJPo6MGC_GT2E8exe-Uexrr8Vw-zP5hre6O6Uv06D_x-5drI7le8FKYtXm7XdoLFw_Tnpqo8GmtZA8JfXGXKa61m7hWKsnOkTQ9pR8kcFZ_SAWEvk85W1kqHDZLe1XSbjktGgaJl3_tPwTPGkqpT1ataVIrGNEdxruG9_kGeF6tfawDfldYg0Wm0aE0NtzVi0lhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/alonews/122320" target="_blank">📅 15:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csFvfbW5zYIrbDKD66srvZ069Xpuna9Y2KeQ4Igcwt84hqTbqDYat7mOWR8oALe93Dx5V8kXLdFRjWDw9WV980od_Y_pRpK45zOWa2A-nY6XtiHzOYC3Ozg8X83RzTqRM8LboLAZjY9OR_rsuxopann3Sdp9EHSbrjS_iSTW7pd6IkFOicZ-Ibgmlhe0p6Qb1am1jtcK7995XuzVN1Y1yhNmQ732diL_jv8F46FSsAfKg9cfBR3543Wh-bE1iHDHGtTLuZtED43jc0OPGF3NXTUtXqpdu6lWOw3srU0xQ5JUVTiVn-vNqvqyo0Vva0JjLPbEVNY14VXO3i5se4-7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ درباره نیروی دریایی ایران : خداحافظ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/alonews/122319" target="_blank">📅 15:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رند پاول از سناتور های برجسته جمهوری خواه: جنگ همیشه با مذاکره به پایان می‌رسد
🔴
منتقدان مذاکرات صلح ترامپ باید به ترامپ فضایی برای پیدا کردن راه حل (اول آمریکا) بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/122318" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF): کمی پیش، پهپادی انفجاری که توسط حزب‌الله به سمت سربازان IDF پرتاب شده بود، در خاک اسرائیل و در مجاورت مرز اسرائیل-لبنان منفجر شد. هیچ آسیبی گزارش نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/122317" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/122316" target="_blank">📅 15:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP1Cvh1xBumsErwcO3oQcsulxPywALzeIufQoOb_gtuEmcaAuXDqWrpjxxnVSru5iGPAqSB9FkAPTlLkEvsYVwJWslBDgQ40E7wTUJxB0ErNBBdR_bAlPfsTmy4F-q75ZCGiGxhUeuxN30JnOXXdAoq8NJh_QIdLS-Fy48IEYjQ2QbUBI7WlnY-mbsSsrXbG2IysCGN56V3rs20FOQscNTaU_smz7O1mpgBti5uGe_eneNT1g6lN4ZBHjXunCNODPyetraI1plLw4UpRbQqC31m-Jh-sSvk3HkqhYeY4Uh1-mDkRHxB8_MVE15Qv1hsiX_NoiCo9NfD7A76Pe6R3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت به نقل از سی‌ان‌ان: شروط توافق احتمالی ایران و آمریکا
🔴
یک توافق احتمالی بین ایران و آمریکا مستلزم آن است که ایران از سلاح‌های هسته‌ای دست بکشد، غنی‌سازی جدید را متوقف کند و مذاکراتی را برای کنار گذاشتن ذخایر اورانیوم با غنای بالای خود آغاز کند. جزئیات مربوط به حذف این ذخایر و مدت زمان توقف غنی‌سازی، بعداً مورد مذاکره قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122315" target="_blank">📅 15:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش اسرائیل خواستار تخلیه 10 شهرک در جنوب لبنان شد و گفت بزودی هدف قرار میگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/122314" target="_blank">📅 15:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سیتنا، پایگاه تخصصی اخبار اینترنت: احتمالا تا هفته آینده اینترنت بین الملل متصل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/122313" target="_blank">📅 15:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122311">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh3ENMHv6T_6Q_8l48x7JZnVtzCTuoiVkQaRKRYMCRHJyIjfCu6yfs8bx1ESf3VVFFpIgS2HycbVQD_lGxObl4as1pVZqdDMORLa_vW2KmzSUHILlItiRxnXwf-Lrbk-kOxmQo0Q5HrDP7f-0VGfAzUWg9Hlp2oVlT1EeicGcrhJN5e3Bm9yhNEwcFwqsX6mXZLpKiy-eSnW-SHRq3nu5ihGe455NuYltVb-hUE-SJvIStIIqNHKtllQKVWMh4-liL_s266xDOqc_qTTiOtgx98Jp02YQmMMTqcL_dCHAhMPx7Cb-KPMdjfGW0DqTLpNOnpy_dwNbH_-BDfp5e0HfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4j_xIcIm_kwXic-kLtJvlGwLO9eoEd1LoFP8KzOrRLRBr2h_iyJJU-wwTS0vXjyfl1Sm2UQsJ3O1ja73zoA9FOZrJpgTkYIbapZ4p-QjJpq1DWnSrb5e1CThi0KKwlNFr9Y07EwGbyZ3A489TRqgZU2lT2pNP5-80OplE33RzqHcjF-NvyudiSirXCMVqyWvnWuzhJFKZQB3QKx2yZI3L8SETrchlISJRMfKyeRfA0jqXtAM0gg44pMqf0GoS0K_Iu9SOauZlwtcoOmPuuF6ixcOHoyG1vShKx7GQdXlH1EnNcGqLZ54yAJ6nFQGwB1Vn3tNE1cvwVQTJY6bYIIFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری جدید از حمله سنگین ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/122311" target="_blank">📅 15:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb38d0d4.mp4?token=fwLl9OKitKh3jv6c9hmVzNlUHYEhbzMvQK2h4nEylkYkhhTH09M5veiojwFR87-bdLZKn2ZEHH2kzTwIc7tlPCLCFGABzxlWZxjMUoyBy4j_RK7bal9AivY9n-5ui33AxZSlmB3TcrGmqVooy7H59VchsOQPvGMjzK9qNiQyY10u2ri8MYa24D_Atyj1g8dp_BxuGk6jWnwtEabCa_8btMEPfPgpNts73pNOl7xbenEzpbjzD_OVcuaDaHkVcUkhBg7ULQEuy9LNmOfAkD2kW97miEc7AvVZmMqpsxNMLezpUHA-Ljg9kbB8cD_BIznlMaR80pck5nU-3JHVEWTSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb38d0d4.mp4?token=fwLl9OKitKh3jv6c9hmVzNlUHYEhbzMvQK2h4nEylkYkhhTH09M5veiojwFR87-bdLZKn2ZEHH2kzTwIc7tlPCLCFGABzxlWZxjMUoyBy4j_RK7bal9AivY9n-5ui33AxZSlmB3TcrGmqVooy7H59VchsOQPvGMjzK9qNiQyY10u2ri8MYa24D_Atyj1g8dp_BxuGk6jWnwtEabCa_8btMEPfPgpNts73pNOl7xbenEzpbjzD_OVcuaDaHkVcUkhBg7ULQEuy9LNmOfAkD2kW97miEc7AvVZmMqpsxNMLezpUHA-Ljg9kbB8cD_BIznlMaR80pck5nU-3JHVEWTSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم خارج از پارلمان لبنان در بیروت چکمه‌های نظامی سربازان ارتش لبنان را نشان می‌دهد که در نبردهای سال 2015 علیه شبه‌نظامیان اسلام‌گرا کشته شده‌اند که در اعتراض به طرح پیشنهادی قانون عفو ​​عمومی به نمایش درآمده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/122310" target="_blank">📅 15:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122309">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر بر اهمیت حمایت از تلاش‌های میانجیگری مداوم برای دستیابی به توافق صلح پایدار تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122309" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روزنامه بریتانیایی فایننشال تایمز ادعا کرد که سپاه ایران از یک شرکت ثبت شده در امارات برای خرید تجهیزات ماهواره‌ای نظامی از چین استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/122308" target="_blank">📅 15:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTWFHrDXPkQLe_o_nEmnJ0KaHEqU5KyEs8nZ9VtO7dZOl89qyvN2NzdWRxgiZp5h3JbL899RD29t-nMWPRrEkLo52sSGPuD8MYcid5sBYcosohCMpidRCZgAE8u1stdQB2a67ySwPzRCtaviCKU_BE_UW758_AKnRNkpCN1sAQg72DJSyy4nKEqpwSJldZrY8FNd_fWvSKKkmWO8eORvm0n3kIvL-bQ3nOzjpj3aDVt2Yv3dstN3x9nJbQt9mn7ZI9g0veI2IcV4_v1biQfJM86aYbcP-Db2RoemGZSfCmTlChV26c7aQHr5F4wIV6r9eqwupplCsKqaJoatDWCzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافق احتمالی بین ایالات متحده و ایران شامل تعهدات ایران برای دنبال نکردن سلاح هسته‌ای و ورود به مذاکرات درباره تحویل ذخیره اورانیوم غنی‌شده بسیار خود و تعلیق هرگونه فعالیت جدید غنی‌سازی اورانیوم است، گزارش می‌دهد CNN.
🔴
جزئیات مربوط به حذف ذخیره اورانیوم و مدت زمان تعلیق غنی‌سازی در مذاکرات بعدی مورد بحث قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122307" target="_blank">📅 14:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqsXy0jfMh5frkfl9rdQY5z90GZWDSvZtpF7znmNAu9AFiUbETjWostTukastWux0fKE_SMXfAVGItCCOEBskpaiFcYvKU-yOuiJ9tV4phPRRRMKklPcTKmM0d1nbF-lFuWasjEIRR0wKeTW1yOMp5j7DCRUnvBtcyj_jUiP5Mwdu98UFHsImV-gqBx9RbuboUoLV3FRaA4lPjG-vrlqwThPeQdaGhkvnHOOwtFxEBE4M1VuUuaTKhz9mGpFPWuuRAdXosFOjMMAN2N_ro90BI--NJyNarB9bu5uqhUbGOToHbCdoS360YQQbqiRf2fwYj9yI2CUzOHhJvioKMs6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش صدا و سیمای ایران، تقریباً ۲۴۰ کشتی در انتظار دریافت مجوز از ایران برای عبور از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/122306" target="_blank">📅 14:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80dbf33e59.mp4?token=rpdWnI4oWfKqragCZVCApYYCv9v9WtTCwKcwh-_PlWhbFK4zOsP2FkEbxgfQwpXfABLe93Ffh57x3sZt3AfDHV6mB3fF3EjLBXanfv5UosnNAN0sb3m8JgjV64bi5Z7BDcuMUnumJfwApmTVo4wRbYq2OeSrV3ejKOrBnOVvlLDkCEW44fgTQz64aXUDj5cGSjxPJOuxkT6sZ2oZjDZJmY4JcJ6E_ebQzGW__GgNup4WJsJwsW8KJ-LJLxsrbu39ivAynZVnankgyWvGB8lAEAwbSPa0u0yUfl_GkvOMp4c-64tbeH-YUPG7UgBrDx8_pdleerx2RPcOSFKYgBTBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80dbf33e59.mp4?token=rpdWnI4oWfKqragCZVCApYYCv9v9WtTCwKcwh-_PlWhbFK4zOsP2FkEbxgfQwpXfABLe93Ffh57x3sZt3AfDHV6mB3fF3EjLBXanfv5UosnNAN0sb3m8JgjV64bi5Z7BDcuMUnumJfwApmTVo4wRbYq2OeSrV3ejKOrBnOVvlLDkCEW44fgTQz64aXUDj5cGSjxPJOuxkT6sZ2oZjDZJmY4JcJ6E_ebQzGW__GgNup4WJsJwsW8KJ-LJLxsrbu39ivAynZVnankgyWvGB8lAEAwbSPa0u0yUfl_GkvOMp4c-64tbeH-YUPG7UgBrDx8_pdleerx2RPcOSFKYgBTBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قطعاً ما و تیم مذاکره‌کننده هرگز کرامت و غرور کشور را به خطر نخواهیم انداخت.
🔴
ما آماده‌ایم به جهان اطمینان دهیم که به دنبال سلاح هسته‌ای نیستیم
🔴
ما به دنبال بی‌ثباتی در منطقه نیستیم؛ آشفته‌کننده در منطقه اسرائیل است که طرح اسرائیل بزرگ را دنبال می‌کند و به طرق مختلف توطئه می‌کند تا جنگ، بی‌ثباتی و اختلاف را در منطقه زنده نگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/122305" target="_blank">📅 14:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122304">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcRi_GVjv4TcnQQ1UuZKjzhaNC-agRYtbNZRUwrQKFtg9sorKTvzULWCMUXMBtSEv3UwnluZea7IEd4NyGK0XzOenUKMuslnTVX06RCO76p5hZBPaesVwDF98SvdEmEk8TzlxhhrWklOzLP66fGHVBi4YFUIERiamc2_FvlZlUD3PI2v6VufPU0NxJlxLWCS2tSvUtfOc6HWGSDUfafwdhyJyZgkjY0vLU9RoYKLxyxZ8Sx_9oRegpGoOFBaOssOxAMA0nOiQ0Pv8lzC5PNArfrLu_NExfDGnkWFcJJaJAaPyrQbpyjTnVUdWvHo1ZN6H4ykOVmCUkcM4CL__Bc6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داده که شرکت موشک‌سازی اسپیس‌ایکس بعد از فتح فضا، حالا پروژه بزرگ‌تری رو شروع کرده. طبق این آمار، اسپیس‌ایکس بزرگ‌ترین عرضه اولیه (IPO) تاریخ رو کلید زده تا ایلان ماسک، ثروتمندترین مرد جهان، بتونه روی یک بازار حتی بزرگ‌تر از فضا مسلط بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/122304" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فاکس نیوز: توافق مورد انتظار تصریح می‌کند که نیروهای آمریکایی به مدت ۳۰ روز در نزدیکی ایران باقی خواهند ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/122303" target="_blank">📅 14:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122302">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6-j8WtDIXzv8ur_dSi0_OVShuim-wIHiXaCH_yV-b67wjlu-zB66TepYGGn1BWWbBniklXob9XgZqnF-cuFEB3fM-V7VKAn5TfTzyrEkQceHeH01i3JPH3p-cFlj8Zoao_y6I-Tbhg5W9h9l4Hz45vNpLGqsdXgc6cVj0MXo1iaLbyEVjWrLR1CBbHsTXWO716px5CTYIvIOGsdgfSeuxOOEFoZP_Xda6Jx_KUM8Kkoyjk1Kgq071Zg_dX-su8gKXQsARw3hVNt1uzfTkhmi2JWA9o23vm2HaGybfc6fFcSta5meVOA2mfbGiGjBY7laadlrlBx1d7tQWfPrXFTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین: نه نفر به جرم جاسوسی برای سپاه پاسداران ایران به حبس ابد محکوم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122302" target="_blank">📅 14:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز: توافق اولیه بین آمریکا و ایران، برنامه هسته‌ای را شامل نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/122301" target="_blank">📅 14:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbAFQK9gtOACGtQ_2FxhDIFi5bA8vchPJSpGoZkEHooqxC8E6tpjuOVYJlAwmoRq9sXJPF9Zipo_AIu0p3ZM-qLJcj6_YO5ugwuEK78slc7_-j7OuvIWVg9VLVMoikbzj-jJPZtFvLQmUGHJDDrUyOjl0d_iolSkZ5aJwUXXk04OpRkwbNn749EGQjt4V8y5oj3w4ZnWQ5E6ynD5N6mybftUr75SNCkpnx7ogQuVbjniK4GmeT975-_QlvTS1CD6LQvVqwppO-Htvv3LC32G2LN0dOrbVTZs43M0RanFZlwEWCCneQA30JbPZovsZvFHHj5_WFPxdLdn27GK_jnKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داده که جنگ، بازار بیمه رو شدیداً تکون داده؛ طوری که هزینه بیمه کردن دارایی‌ها در برابر خشونت‌های سیاسی، الان ۴۰ برابرِ زمان قبل از جنگ شده و این موضوع خریداران بیمه رو با چالش بزرگی روبرو کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/122300" target="_blank">📅 14:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فرماندهی جبهه داخلی اسرائیل یک سیستم هشدار زودهنگام جدید برای پرتاب راکت و موشک از لبنان توسعه داده است که طبق گزارش کانال ۱۲ اسرائیل، به ساکنان نزدیک مرز چند ثانیه هشدار قبلی و در سایر نقاط کشور تا دو دقیقه زمان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/122299" target="_blank">📅 14:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مهر: سرنگون شدن پهپاد اسرائیلی بر فراز هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122298" target="_blank">📅 14:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفيلترشكن |𝐯𝟐𝐛𝐨𝐱𝐢𝐧𝐨 |CH</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzG3NZSIO9QE31frNGBdu7knZ7F3SD_eyvrmsbzo1BPO3OssXUFikPjTmL9EWPa8Geb4iRScyluhKM9vEdTLMp2q7qdeVLmUcRgzfeY4jftHfQKxnSUhwG-C3bQFyhb8HI6orkFNJsoUaXTguw1q1EhO2DXBfO1KGAwNrOAlX6s7myuIwoSxFfRXn6c0vewssrDILmX6tQigO2uveoskoxlROVIK0WXZx3n72dm24zFMnT5449IXumXetVF3oZo42GOo8jz5MD6tUb37tEQTiP5O7uxRMufoju2leyEW-AtKOMAJF8BxrmCgc5YpePmguSbmYIqjUdA4-mHvop9zjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😱
🔺
پلن JeT
🏎
گيگى 126هزار تومان
فروش محدود باز شد
⏰
فقط
700
تا شارژ شد
😱
🔥
🤖
:
@v2boxinoBot
❤️
قیمت فقط گیگی 126 هزارتومان
🏃‍♂️
🤔
این آخرین ظرفیت ويتوباكسينو برای امروز
⚡️
🔤
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122297" target="_blank">📅 14:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تسنیم: در هیچ‌یک از بندهای تفاهمنامه، عبارتی مبنی بر بازرسی یا کنترل کشتی‌های ایرانی توسط آمریکا پس از رفع محاصره دریایی وجود ندارد/ اساساً ایران هیچ اجازه‌ای به آمریکایی‌ها برای چنین اقدامی نداده و نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/122296" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به ترامپ هشدار داد که اسرائیل «آزادی عمل در برابر تهدیدها در همه عرصه‌ها، از جمله لبنان، را حفظ می‌کند»، به گزارش AP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122295" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کاهش قیمت دلار: ۱۶۸ هزار تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122294" target="_blank">📅 14:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
بر اساس جزئیات منتشر شده، ایران تنگه هرمز را بدون دریافت هزینه باز خواهد کرد در حالی که آمریکا پولی به تهران منتقل نخواهد کرد و به هر دو طرف مهلت ۶۰ روزه داده می‌شود تا مذاکرات هسته‌ای را ادامه دهند.
🔴
تحریم‌ها علیه ایران باقی خواهد ماند به جز تسهیلات محدودی در محدودیت‌های مرتبط با نفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122293" target="_blank">📅 14:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کانال ۱۲ عبری به نقل از یک مقام ارشد اسرائیلی:  توافق احتمالی ایران و امریکا بد است، زیرا این پیام را به ایرانیان می‌دهد که آنها سلاحی دارند که به اندازه سلاح هسته‌ای مؤثر است، و آن تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122292" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت دفاع روسیه : مراکز فرماندهی نیروهای زمینی و ریاست اطلاعات اوکراین رو هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122291" target="_blank">📅 13:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
قبرس به طور رسمی علاقه‌مندی خود را برای خرید پهپادهای هندی و مهمات پرنده آزمایش‌شده در عملیات سیندور اعلام کرد.
🔴
مقامات قبرسی به طور خاص نام سیستم‌های مهمات پرنده ناگاسترا-۱ و اسکای استرایکر را به عنوان سیستم‌هایی که می‌خواهند به دست آورند، ذکر کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/122290" target="_blank">📅 13:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122289">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
تسنیم به نقل از منبع آگاه: آمریکایی ها درحال کارشکنی هستند و مسئله پول های بلوکه شده باعث شده فعلا توافقی نهایی نشود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122289" target="_blank">📅 13:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122288">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4eaf938e.mp4?token=F3C_E_Oals77DVU_2QjUiTZKVSNq97o5Pn5t7UdA6Gi8T587D8xtyNN3uBcPMvKDtXzADciKzb3nQ-3xO1-TXHhogrxd4Do9xz7ww-aCbp6z2zUB6aFmQbqUTdhgAWKgP2dbAkFu4pvDxjtguNLrGEgNlvtqF5Oh_1FYwuJwn3TvBpj8Ga5h8dEYmsJGDlf0b4SrWLdmIKVynIIUYExmj50AsqHptIaUMEEOHrvWR4mIaDSZn70bIAD4lU7ZfGXza_SyBE50rMgTzTkst3KU3K1GEe5Hf78R7Amj5Np5z38pu27rWXqKrDe4_XAz3vodu2ZkIIJEIOlU3zNCTs0dUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4eaf938e.mp4?token=F3C_E_Oals77DVU_2QjUiTZKVSNq97o5Pn5t7UdA6Gi8T587D8xtyNN3uBcPMvKDtXzADciKzb3nQ-3xO1-TXHhogrxd4Do9xz7ww-aCbp6z2zUB6aFmQbqUTdhgAWKgP2dbAkFu4pvDxjtguNLrGEgNlvtqF5Oh_1FYwuJwn3TvBpj8Ga5h8dEYmsJGDlf0b4SrWLdmIKVynIIUYExmj50AsqHptIaUMEEOHrvWR4mIaDSZn70bIAD4lU7ZfGXza_SyBE50rMgTzTkst3KU3K1GEe5Hf78R7Amj5Np5z38pu27rWXqKrDe4_XAz3vodu2ZkIIJEIOlU3zNCTs0dUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم نزدیک از حمله موشکی بالستیک میان‌برد اورشنیک در طول شب به بیلا تسروکا، منطقه کیف.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122288" target="_blank">📅 13:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122287">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کان نیوز: ایالات متحده به طور مداوم اسرائیل را در جریان مذاکرات یادداشت تفاهم با ایران قرار می‌دهد که هدف آن بازگشایی تنگه هرمز و آغاز گفتگوها درباره مسائل حل‌نشده برای رسیدن به توافق نهایی است
🔴
در تماس تلفنی با رئیس‌جمهور ترامپ دیشب، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در برابر تهدیدات در تمام جبهه‌ها، از جمله لبنان، حفظ خواهد کرد و ترامپ از این موضع حمایت کرد.
🔴
ترامپ همچنین مجدداً تأکید کرد که خواستار حفظ درخواست خود برای برچیدن برنامه هسته‌ای ایران و حذف تمام اورانیوم غنی‌شده از خاک ایران است و گفت بدون این شرایط هیچ توافق نهایی امضا نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122287" target="_blank">📅 13:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122286">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3FI0xhVAKmNpqQxqf71eDK3cYScfX_gw5y2U9iMRKnrxFgaEFIur2_f-tBRaOqvLAEfx62o0VftmTJmL-HR27ZjdF9sDZGWiMZJDINPJGMDkszxO3MPE9dDVNmviyy7uYhBZnVb0uUlQIU1INppW9nlNXLqvC1izKP5vOfNVmRNwEY9UM4UJGeIhs4J4c0w_uzFEz5HEl5Yxq77wfUFBG5sX757VnUpUZ7XxRDuGMw4QzfFydZwoQ808dhCXS27AJ8mFvsZZPNmN4AIigMFCqTtwEwsx-Fagz3eYd74q8Tsg49O8WV_9hROh_m8tkLYaUivaSTKHN92hNYQszJk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: جنگ، ایران را فرو نپاشید. کنترل آن بر هرمز را تثبیت کرد، اتحادهایش را از نو ساخت و همان نهادهایی را که ایالات متحده هدف قرار داده بود، تقویت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122286" target="_blank">📅 13:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122285">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نشریه عبری معاریو به نقل از منابع آگاه:
نتانیاهو در هفته‌های گذشته چندین بار درخواست گفت‌وگو با ترامپ را داده، اما پاسخ از سوی مشاوران ترامپ داده می‌شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122285" target="_blank">📅 13:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122284">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مقام اسرائیلی: رئیس جمهور ترامپ به نخست وزیر نتانیاهو روشن کرد که در مذاکرات بر سر خواسته دیرینه خود مبنی بر برچیدن برنامه هسته ای ایران و خروج تمام اورانیوم غنی شده از خاک ایران، قاطع خواهد ماند. او اظهار داشت که تا زمانی که این شرایط برآورده نشود، توافق نهایی را امضا نخواهد کرد.
🔴
اما توافق چارچوبی برای پایان جنگ - قطعاً ممکن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122284" target="_blank">📅 13:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122283">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خنثی‌سازی مهمات عمل نکرده در اطراف نیروگاه اتمی بوشهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122283" target="_blank">📅 13:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onkWTuG12nvxZv_Hs5MxTMz42zDpI3o7-KQuopTNfG8kkJ7fvQaEqCQZFPpdWqXzSoTOlhKvZve6Bbjt2t6wRZSeRy6k6Wh3GA2b0TK7E2D_LXo-S78Wbd6T70BkfgR4PhlmEZjIn8lBaHRv-4OClvZgTK1q3v8JtL8E1irNtt2-Uw9skIdMN75WB-YdnLJtggenlkgv0H79BzUgZqOZPqxCuGM8fX8c81ebE_Lx-7faoBpMSmn-dUTHLE4MiytcPqqri_nRn36ZOmWC4OAqkzbZWLBCYNO1rSrZ8UJdPHLQRgMMMzn69YAbgJsjOVxFEyRJv9sP2BJ_v7YrXDJxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
از سرویس مخفی بزرگ و نیروهای انتظامی ما برای اقدام سریع و حرفه‌ای امشب در برابر یک تیرانداز نزدیک کاخ سفید که سابقه خشونت‌آمیز و احتمالاً وسواس نسبت به محترم‌ترین سازه کشور ما داشت، تشکر می‌کنم.
🔴
تیرانداز پس از تبادل آتش با مأموران سرویس مخفی در نزدیکی دروازه‌های کاخ سفید کشته شد. این رویداد یک ماه پس از تیراندازی در شام خبرنگاران کاخ سفید رخ داده است و نشان می‌دهد چقدر مهم است که برای همه رؤسای جمهور آینده، امن‌ترین و مطمئن‌ترین فضایی از نوع خود که تاکنون در واشنگتن دی.سی ساخته شده، فراهم شود. امنیت ملی کشور ما این را می‌طلبد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122282" target="_blank">📅 13:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: به همکاری با شرکای بین المللی برای دستیابی به راه حل دیپلماتیک پایدار در مورد ایران ادامه خواهیم داد
🔴
بر اهمیت باز کردن تنگه هرمز و لزوم جلوگیری از ساخت سلاح هسته‌ای توسط ایران تاکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122281" target="_blank">📅 13:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K_yQoRma9GlpQeyoK8DmqFJ8DPFTLj8YRYq4JQGqcKOQL12piTr4PZaZyPSTBom92MjFqsPApPToXp0y3clQmfBFBzItX_kYteIpjjC4MdLWT6j4gUaKjMisZKXDtDKr1fW6r9KDoAQJ34s_HNgsXyrmv5erFtvy37j5-oXMkZnae4k2RLkJNK4nb8iPjUprwS29oRTY1I_9nFB3pAfL6OxZkePY-6-pfKAm1fnDgm8BxI5_99Q2Fb8ruEzyPZbxQ-ROOCX3koUdAfMyt-w1uiY_i4xr68jgf4n47HPcWyOg61ybvpWMB_Es3348PuF0bbFc_I39nZKFvCWqqX7lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lV7mBgrPBKoayOZ-43iQZc6xnxlOcQPH0pBo9H0SgQsYeZaqN8FP-xZQa16Jy6SNT-A3Lz2jQ8xYnPSyHTtXainbUK8dPaXAjC10l3G39uXNgBjDOULBfTqgwQY1BwAp7Dh8OqE8RyZpvvyIS124PBHZtVerDVq2qQNPN51Mptj3AAu6OLSxpY8lNGQjay-lKWnCQCAGBhe6f5PpTYtzgJjz-AQpLDc43nmYGR_4_XUEEg88c8gdqEydQurtV8jU4hVPq_jWRodNweUPlSUV-c2ZA__sVe5A1z7UX6lkJ44SBvnumNH913_wgyMLV43pwRtvptC4vblfFq28C2wucw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
این حرکت علی کریمی خیلی حاشیه درست کرده؛ عکس اصلی که یه نفر تصویر رضا پهلوی رو برده بالا استوری کرده، اما رضا پهلوی رو سانسور کرده و جای عکس پهلوی نوشته «ایران»!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122279" target="_blank">📅 13:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122278">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سفیر آذربایجان در تهران تایید کرد که رامیل عمران اف، کنسول سرکنسولگری جمهوری آذربایجان در تبریز، روز شنبه در یک تصادف درگذشته است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122278" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سفیر آذربایجان در تهران تایید کرد که رامیل عمران اف، کنسول سرکنسولگری جمهوری آذربایجان در تبریز، روز شنبه در یک تصادف درگذشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122277" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
قالیباف، نقدعلی و سالاری کاندیدای ریاست مجلس در سال سوم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122276" target="_blank">📅 13:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122275">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO1b69ZQH19W5pQ2DAXawd3K2bAdu7pnZ_NOIiKWOZzLVhGoZiGZ68sZxlhP6go1RIbhtrlmtquvuJm0eNUHeBJiPn2ejodsxBGrBsVxhMhfUQA274lvd9tyFtE7dJEjQAQgDeht8EnCDlOksqmuK0PfBeh-9osyc24Kf-fWLMwakaF_oVm70fv44lvgehYzWEgwlo03zuzZdO3jABTteEZ3OW8bTil8652ky-zL8niURs2XYsi_pXwjNy-bM1TKpojpQq08VBEn2sxMh271zXliL0beHbIZ8TVci3WCWLjq9orwwIF56N4SlRL7hVYnVwCYkwR675zzlWgz9krHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتنياهو شلیک‌های دیروز شب در واشنگتن را محکوم کرد و از ترامپ به عنوان «بهترین دوستی که اسرائیل تاکنون در کاخ سفید داشته» یاد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122275" target="_blank">📅 12:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر امور خارجه هند: ما طرفدار دیپلماسی برای حل منازعات و تجارت دریایی امن هستیم
🔴
سوبرامانیام جایشانکار: ما طرفدار گفت‌وگو و دیپلماسی برای حل منازعات هستیم.
🔴
از تجارت دریایی امن و بدون مانع حمایت می‌کنیم.
🔴
ما خواستار رعایت دقیق قوانین بین‌الملل هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122274" target="_blank">📅 12:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122273">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5837862222.mp4?token=MCn9ErPI7T8K0xQRG0KupnqTL4uGnbkOyKQ08QHIOQRRk5uLiRV12_6vV9TBinitBEZ5mrbCyYKyAf0ZFeDHqE1HSIWr8QRdux18zzA3OqNdEasMaY8sj7aXkApEZf56MBZRw32asyj2st20NTtYiZdnyohvHAw2OI7dEC7YBR1SImbF3232KZZcXDOdlwT_vMv3Ga91pSdnn0YsGMaIcr4hby9QH0ejomqPIDU9T9G4ERjV2t2-uNREX5ZJPbQDBJ9yCrjqPuCLZza5Z0s417zhcIUDSh-9SMOMkn0uUnD4oFqfJYeXMPhzYGPyWh2edyStnfq3nBSo9Nv07lOXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5837862222.mp4?token=MCn9ErPI7T8K0xQRG0KupnqTL4uGnbkOyKQ08QHIOQRRk5uLiRV12_6vV9TBinitBEZ5mrbCyYKyAf0ZFeDHqE1HSIWr8QRdux18zzA3OqNdEasMaY8sj7aXkApEZf56MBZRw32asyj2st20NTtYiZdnyohvHAw2OI7dEC7YBR1SImbF3232KZZcXDOdlwT_vMv3Ga91pSdnn0YsGMaIcr4hby9QH0ejomqPIDU9T9G4ERjV2t2-uNREX5ZJPbQDBJ9yCrjqPuCLZza5Z0s417zhcIUDSh-9SMOMkn0uUnD4oFqfJYeXMPhzYGPyWh2edyStnfq3nBSo9Nv07lOXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه هند: ما با ایران و آمریکا و اسرائیل روابط خوبی داریم و چندجانبه گرایی هدف ماست
🔴
سوبرامانیام جایشانکار: هند، به‌خاطر رشد منافعش، با تمام طرف‌های درگیر ارتباط دارد.
🔴
ما به دنبال صلح و ثبات در منطقه هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122273" target="_blank">📅 12:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122272">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
2040 ساعت از قطعی اینترنت توی ایران گذشت‌‌...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122272" target="_blank">📅 12:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122271">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9defe238.mp4?token=sTRG4vWqZzhHjglcA1ffeEE5Gu67fMVlRx7k54UCw7GbUQsUMvRYXta2FjoLt1yLBtV4y0lfBX7VeAdL2F_XDEzwl4DO0En5JNRnpMvEo9lGOyU9xyTmKygVMOLa-4YloyDn-Qj15J9IiMZy1OVgBMaSRTY8G7UpRA6J9WKOxXx-7WqJaWb7UFL8_4uOmmnLjDPHUI6L_8rLBNDJWlhpbzLdj6WFymTZPF4xVu45mrU38ecJqSrV2Mm1rEOAHUl0nBgxw2YelrqCI4tzmLTf-g_EsUHeCunO0E2LqossJ8a2-yGAgeIpRD_k_26WuHhQkkaRypBPk-O52lxHBfki8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9defe238.mp4?token=sTRG4vWqZzhHjglcA1ffeEE5Gu67fMVlRx7k54UCw7GbUQsUMvRYXta2FjoLt1yLBtV4y0lfBX7VeAdL2F_XDEzwl4DO0En5JNRnpMvEo9lGOyU9xyTmKygVMOLa-4YloyDn-Qj15J9IiMZy1OVgBMaSRTY8G7UpRA6J9WKOxXx-7WqJaWb7UFL8_4uOmmnLjDPHUI6L_8rLBNDJWlhpbzLdj6WFymTZPF4xVu45mrU38ecJqSrV2Mm1rEOAHUl0nBgxw2YelrqCI4tzmLTf-g_EsUHeCunO0E2LqossJ8a2-yGAgeIpRD_k_26WuHhQkkaRypBPk-O52lxHBfki8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال خبرنگار هندی باعث سکوت و تعجب وزیرخارجه امریکا شد
🔴
خبرنگار
:
«ما شاهد اظهارات نژادپرستانه زیادی از سوی آمریکا در مورد هندی‌ها بوده‌ایم. این خلاف همکاری هند و آمریکا است.»
🔴
روبیو
:
ببخشید، چه کسی این اظهارات را مطرح کرده است؟»
🔴
خبرنگار
:
«قربان، همه ما این اظهارات را دیده‌ایم. آنها کاملاً شناخته شده هستند.»
🔴
روبیو
:
«سکوت و نگاه متعجبانه!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122271" target="_blank">📅 12:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122270">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122270" target="_blank">📅 12:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122269">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ادعای رویترز به نقل از یک منبع ارشد ایرانی: مسئله هسته‌ای در مذاکرات مربوط به توافق نهایی مورد بحث قرار خواهد گرفت و بنابراین بخشی از توافق فعلی نیست
🔴
هیچ توافقی درمورد ذخایر اورانیوم با غنای بالا از کشور صورت نگرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122269" target="_blank">📅 12:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122268">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نتانیاهو به وزرا دستور داده است از بحث در مورد توافق قریب الوقوع بین تهران و واشنگتن خودداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122268" target="_blank">📅 12:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122267">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579c36b53.mp4?token=m5c_JnciONURfJKkTECrrIYhMXqwpfIVumjAt1JHV5ehTdicE9swF4QDXGA4zDSr8qXlrA6CFkYlL2oeYLZHnMQ8-eDOj8flGBgLAttb5DVuO0-Adsyb0bMHuX9epwpPOjKnceh4eGK9hqptPlB-1YO26nXsyP2m7MaURWvRBhtZPsBQ394VaBo-wEqOSkQGdQ0R6bwvmC6lhk21LWgL1IgknXtn75huM4he2jHpvdlUeCBnouxcxU9MWLpKOTfPWCi25IQL2XYQDRDC1H0GJpCB_vi1Tvoyw-Jtoz38XHp9AvzeI6tkvL2XYjTcii2jSJRthqGJ7g8qUVp42L-S6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579c36b53.mp4?token=m5c_JnciONURfJKkTECrrIYhMXqwpfIVumjAt1JHV5ehTdicE9swF4QDXGA4zDSr8qXlrA6CFkYlL2oeYLZHnMQ8-eDOj8flGBgLAttb5DVuO0-Adsyb0bMHuX9epwpPOjKnceh4eGK9hqptPlB-1YO26nXsyP2m7MaURWvRBhtZPsBQ394VaBo-wEqOSkQGdQ0R6bwvmC6lhk21LWgL1IgknXtn75huM4he2jHpvdlUeCBnouxcxU9MWLpKOTfPWCi25IQL2XYQDRDC1H0GJpCB_vi1Tvoyw-Jtoz38XHp9AvzeI6tkvL2XYjTcii2jSJRthqGJ7g8qUVp42L-S6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت فعلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/122267" target="_blank">📅 12:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122266">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرگزاری آماتور فارس: آمریکا شاید دبه کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122266" target="_blank">📅 12:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122265">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجار در راه‌آهن کویته پاکستان بیش از ۳۰ کشته و ۸۰ زخمی بر جای گذاشت
🔴
در پی انفجاری شدید در نزدیکی خط راه‌آهن کویته پاکستان دستکم ۳۰ نفر کشته و بیش از ۸۰ تن زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122265" target="_blank">📅 12:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122264">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ادعای العربیه: دور بعدی مذاکرات بین آمریکا و ایران ممکن است در ۵ ژوئن برگزار شود.
🔴
واشنگتن و تهران هنگام آغاز مذاکره برای توافق نهایی، روسای هیئت‌های خود را اعزام خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122264" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122263">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
امیرحسین ثابتی: جنگ و ترورهای دشمن در پیش است؛ چه توافق بشود و چه نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122263" target="_blank">📅 12:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nB403ylkBbcCsCH6r4v_449eLYxyv-6gNQQc6ROAF1XCPJg7zNMIx7rgdfCdwdovT35rNc4SfzNU6RBTnStKuaVkHvxU_io-5gxMXSvoGu_TDY9jxR6xQ4fvw9qeXR-w_RXQeueYfQEncPQiuOCvF8RTR5QHkKIqPZGfxaC_NpVK-nAMQiXOdgw6-vRJVpzcry3jloexfn5gMJ3CUmOwB-CXPY0vdbVqPqWBl1Vi6GW1ziwskXXoqjyDJaPIAogbeiYtptqTRxcwQqLuaH4QaR0RPgrtUCtjA0HZc91lKX_LSlR_kpr1Iu5TPzER9EoGDG7e0mJrTowP69v2dJj79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: آمریکا شاید برا بازگشایی محاصره تنگه «پروتکل» بگذارد!/ تکلیف «غرامت» و «تحریم‌ها» در تفاهم جدید هنوز مشخص نیست/ قطر متعهد شده بخشی از دارایی‌‌های بلوکه شده ایران را بپردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122262" target="_blank">📅 12:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122261">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الحدث به نقل از منابع: توافق اولیه احتمالی بین ایران و ایالات متحده «اعلامیه اسلام‌آباد» نام خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122261" target="_blank">📅 12:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122260">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122260" target="_blank">📅 11:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122259">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=srrjptDlnLjH-tIRqDgTH3nePrLxSvkgG646F_19smVxdtgxTO4Q-juvAEel6JGukZu5qRT3QQ-UySQz3HjQRR0FYErQI8biHsxlgdAVL792ROxKsYDYYzWygLnjg1nGYII3LgPdM_JkZ7J-GPfRqjz_7jQ3e2Dhie25o0codtcrbmwQn9PdSOroELmvihniQmH9rrXlwL3KdfJ8kQqzNvehfLoRoCfid-o1jFKX4mCGymf1MhLC7W2pV4-Byn7lzSzcr52Z12Iy6Z2nlF9TqXZcGuqmRnOtXjLvWxyQZcd75bwy0Engh_C1f3nMRVhY6dScsS9YZVNKDxCVwXNKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=srrjptDlnLjH-tIRqDgTH3nePrLxSvkgG646F_19smVxdtgxTO4Q-juvAEel6JGukZu5qRT3QQ-UySQz3HjQRR0FYErQI8biHsxlgdAVL792ROxKsYDYYzWygLnjg1nGYII3LgPdM_JkZ7J-GPfRqjz_7jQ3e2Dhie25o0codtcrbmwQn9PdSOroELmvihniQmH9rrXlwL3KdfJ8kQqzNvehfLoRoCfid-o1jFKX4mCGymf1MhLC7W2pV4-Byn7lzSzcr52Z12Iy6Z2nlF9TqXZcGuqmRnOtXjLvWxyQZcd75bwy0Engh_C1f3nMRVhY6dScsS9YZVNKDxCVwXNKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122259" target="_blank">📅 11:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122258">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع مطلع: اختلاف بر سر یکی دو بند از تفاهم‌نامه همچنان ادامه دارد
🔴
یک منبع مطلع گفت که اختلاف میان ایران و آمریکا بر سر یکی دو بند از تفاهم نامه احتمالی همچنان ادامه دارد و به دلیل مانع‌تراشی‌های آمریکا هنوز موضوع نهایی نشده است.
🔴
وی تاکید کرد: ایران بر احقاق خود مردم خود تاکید دارد و این موضوع به میانجی پاکستانی اعلام شده است که در صورت ادامه مانع‌تراشی‌های آمریکا، امکان نهایی شدن تفاهم نامه وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122258" target="_blank">📅 11:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122257">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فارس: بررسی متن نهایی‌شده توافق احتمالی، نشان می‌دهد آمریکا و متحدانش متعهد می‌شوند که به هیچ وجه به ایران یا متحدانش حمله نکنند.
🔴
در مقابل، ایران نیز متعهد شده که خود و متحدانش به آمریکا و متحدان آن حملۀ نظامی پیش دستانه نداشته باشند.
🔴
طبق پیش‌نویس توافق، طرفین بر سر آزادسازی تمام یا بخشی از پول‌های مسدودشدهٔ ایران به منظور ورود به مذاکره توافق کرده‌اند
🔴
همچنین طبق این پیش‌نویس، امکان تردد در تنگهٔ هرمز به تعداد قبل از جنگ و با مدیریت ایران، همزمان با برداشتن محاصرهٔ دریایی فراهم می‌شود.
🔴
علاوه بر این، تحریم‌های نفت، گاز، پتروشیمی و مشتقات آن در دورهٔ مذاکره به‌طور موقت لغو می‌شود تا ایران بتواند آزادانه به فروش محصولات خود بپردازد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122257" target="_blank">📅 11:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122256">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: از پیشرفت به سمت توافق بین آمریکا و ایران استقبال می‌کنم
🔴
ما به توافقی نیاز داریم که به جنگ پایان دهد
🔴
ما با شرکای بین‌المللی خود برای غنیمت شمردن این فرصت و دستیابی به یک راه‌حل دیپلماتیک بلندمدت همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/122256" target="_blank">📅 11:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122255">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4a57f0a5.mp4?token=KyKXG48aW5Ll9bzIdX6KZOa-UKZftQ6DbgtzViu3VI2OetNXaMwcJWstjne3Tz_rXNn4rdlID1QCswz3BbAw9R1MQpZ763U1YN6ecR-mxidlS0oArlaTG2ZKoxlSqqVy7xSJ_uWvsBumA329LThHKzChtjAeXobGMVfh99lxdouIFNASKWP4A5_39W7YQ_z2C9xiCFXv3JbP_W0O8tKZ11q2DugzOXifhIMvLFBfqqgXhmiNSicZKKEyxyU3WMzh91JW4fJXVnDELI_0uLB5eT7FGwA_8E3iOTgnDvlPOOIYlU0VozDndpb_BdZdYkYSg_9nSCA5Lorxy83ip_vFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4a57f0a5.mp4?token=KyKXG48aW5Ll9bzIdX6KZOa-UKZftQ6DbgtzViu3VI2OetNXaMwcJWstjne3Tz_rXNn4rdlID1QCswz3BbAw9R1MQpZ763U1YN6ecR-mxidlS0oArlaTG2ZKoxlSqqVy7xSJ_uWvsBumA329LThHKzChtjAeXobGMVfh99lxdouIFNASKWP4A5_39W7YQ_z2C9xiCFXv3JbP_W0O8tKZ11q2DugzOXifhIMvLFBfqqgXhmiNSicZKKEyxyU3WMzh91JW4fJXVnDELI_0uLB5eT7FGwA_8E3iOTgnDvlPOOIYlU0VozDndpb_BdZdYkYSg_9nSCA5Lorxy83ip_vFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: هیچ مسیر آبی بین‌المللی و هیچ فضای هوایی بین‌المللی نباید هرگز توسط هیچ کشوری در جهان ملی‌سازی شود. این نباید هرگز به عنوان یک هنجار جدید پذیرفته شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/122255" target="_blank">📅 11:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122254">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منبع ارشد ایرانی به رویترز: تهران با تحویل ذخیره اورانیوم بسیار غنی شده خود موافقت نکرده است.مسئله هسته‌ای ایران بخشی از توافق اولیه نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/122254" target="_blank">📅 11:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122253">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روبیو: پیشرفت بزرگی در مورد بحران با ایران حاصل شده است
🔴
این احتمال وجود دارد که جهان در ساعات آینده اخبار خوبی بشنود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/122253" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122252">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: پس از همکاری با کشورهای خلیج فارس، در مورد ایران پیشرفت کرده‌ایم
🔴
احتمالاً اخبار بیشتری درباره ایران امروز منتشر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122252" target="_blank">📅 11:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122251">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FboTZXU3bjHjB6C77bloxnFPgqMhJx1gOIhY583Qr37EgbRxz9Z2pPU7vtY3fasGk_xm0r-KvU0kIiL-pU5vTC0d6GsNIdin6-cphDIV9iPC-g4fSLRQiWKq1gZoFZrFJ0n5K16XwN9wtmUD9vmYS0i1Shfb73DttmKr-tPfpeLAV5_JsDciTHAO1T6YMUaBcL2Epj_JQL3hQtxU1s8eXK1nY5C3NFoIAN5rRGQ8UxJfR7GpIyXeIL6vfafZcuQUs_NbRtSJ3eTPPiNlQCm00U8azIEIU-pFGEYSlEYn2_Jx5oRCHF6u7hQ5rAkvPiCMn-aI9YaOjx-uskGJw11hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، سال ۲۰۲۰ میلادی: ایران هرگز جنگی را نبرده، اما هرگز مذاکره‌ای را هم نباخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122251" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122250">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122250" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122249">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mwfChq1eUrBKoaGbKglHOR-nSdCtry9THCQCnv5g2I9_ZGJxtxN9C_n9s-zy16V7iYxj__7LHyRhbHibolnLVPYXEqQhRoy9mf7ApIq9cr2v1Uiz044rMCFYJNwJXP4WiX6ihLYAWqMIwrayVn_p1-xpxhTBmCwyYAA7YfjU15LyXxGbEW4iur8dfy0LXbTJd-IHxVvekAAeyKH8pbot13MlmDN1nX-IMkYjKCfNpmhLqr_bmsb7LBtBdNiwFqaS8D6W-AwqOttaLwqQmSt-DojWMxjkeQdKjoxIjdcYmH4N4SEx9FKSz04gfLo0uoPMm8x15LKcR-R42OzA9Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
______________________
لینک سابسکریشن
✅
تست رایگان
✅
بدون محدودیت کاربر و زمان
✅
تضمین عودت وجه
✅
@darkoob_config1
@darkoob_config1
@darkoob_config1</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122249" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122248">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: بنده نسبت به مشکلات اقتصادی و معیشتی مردم، به‌ویژه آسیب‌هایی که در پی شرایط جنگی تشدید شده، احساس مسئولیت جدی دارم و با تمام توان در حال تلاش برای کاهش فشارها بر مردم هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/122248" target="_blank">📅 11:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122247">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: آنچه در مقاطع حساس، ضامن حفظ و ثبات کشور بوده، همبستگی و همدلی مردم و ارکان نظام است.
🔴
با وجود مسائل و مشکلات متعدد، از بیان بسیاری از مطالب صرف‌نظر می‌کنم تا مبادا زمینه تفرقه و اختلاف فراهم شود. امروز حفظ وحدت و انسجام ملی به‌مراتب مهم‌تر از مسائل نظامی و امنیتی است
🔴
همواره تلاش کرده‌ام سخنی بر خلاف نظر مقام معظم رهبری بیان نشود و یا موضعی اتخاذ نگردد که به اختلاف میان ارکان حاکمیت دامن بزند و دشمن از آن سوءاستفاده کند.
🔴
هر سخن، تحلیل یا موضعی که از هر تریبونی، به‌ویژه صدا و سیما، منجر به ایجاد شکاف و تفرقه در جامعه شود، در عمل آب ریختن به آسیاب دشمن است
🔴
گاهی برخی کارشناسان در رسانه ملی سخنانی مطرح می‌کنند که با واقعیت‌های جاری کشور و روندهای موجود فاصله جدی دارد، اما دولت به‌منظور جلوگیری از اختلاف و حفظ آرامش جامعه، از واکنش و موضع‌گیری پرهیز می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122247" target="_blank">📅 10:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122246">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
‌فارس: بررسی متن نهایی‌شده توافق احتمالی، نشان می‌دهد
آمریکا و متحدانش متعهد می‌شوند که به هیچ وجه به ایران یا متحدانش حمله نکنند.
🔴
در مقابل، ایران نیز متعهد شده که خود و متحدانش به آمریکا و متحدان آن حملۀ نظامی پیش دستانه نداشته باشند.
🔴
طبق پیش‌نویس توافق، طرفین بر سر آزادسازی تمام یا بخشی از پول‌های مسدودشدهٔ ایران به منظور ورود به مذاکره توافق کرده‌اند
🔴
همچنین طبق این پیش‌نویس، امکان تردد در تنگهٔ هرمز به تعداد قبل از جنگ و با مدیریت ایران، همزمان با برداشتن محاصرهٔ دریایی فراهم می‌شود.
🔴
علاوه بر این، تحریم‌های نفت، گاز، پتروشیمی و مشتقات آن در دورهٔ مذاکره به‌طور موقت لغو می‌شود تا ایران بتواند آزادانه به فروش محصولات خود بپردازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122246" target="_blank">📅 10:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122245">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: پیش نویس توافق با واشنگتن مقرر می‌کند که وضعیت حاکمیتی تنگه هرمز به شرایط پیش از جنگ باز نگردد و تنها تعداد کشتی‌های عبوری ظرف ۳۰ روز بازیابی شود، که همزمان با رفع کامل محاصره دریایی و اجرای تعهدات آمریکا است. تهران بر حفظ حق حاکمیتی خود بر این تنگه تأکید دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/122245" target="_blank">📅 10:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122244">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
العربی الجديد به نقل از منبع ایرانی:
پیش‌نویس توافق بین تهران و واشنگتن شامل پایان جنگ در تمام جبهه‌ها از جمله لبنان است
🔴
بخش بزرگی از دارایی‌های مسدود شده ایران در خارج آزاد خواهد شد و محاصره دریایی برداشته شده و تنگه هرمز بازگشایی می‌شود
🔴
وضعیت موجود در پرونده هسته‌ای و تحریم‌ها حفظ خواهد شد
🔴
تهران در دوره ۶۰ روزه از کاهش تحریم‌ها برای فروش نفت خود بهره‌مند خواهد شد
🔴
هنوز برخی اختلافات برای حل شدن قبل از اعلام توافق موقت باقی است و توپ در زمین آمریکاست
🔴
هیچ چیز را نمی‌توان تضمین شده یا نهایی دانست مگر اینکه همه جزئیات توافق شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122244" target="_blank">📅 10:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122243">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
راضیه عالیشوندی، معاون امور بین‌الملل و حقوق بشردوستانه جمعیت هلال‌احمر: محموله‌های کمک‌های بشردوستانه کشورهای عراق، ازبکستان و قزاقستان وارد ایران شد.
🔴
این کمک‌ها شامل اقلام غذایی، دارویی و تجهیزات پزشکی است.
🔴
این کمک‌ها در راستای حمایت از عملیات امدادی و تامین نیازهای اقشار آسیب‌پذیر در اختیار جمعیت هلال‌احمر قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/122243" target="_blank">📅 10:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN0KxK3VtSDuIc0JImIge2myR6d7Wmo3e73zkT7rsero9EG4iFiOWQyeLm_i3tv8EZ-RyjBfgaFo0qkgh86PXrmXz7LZdeAeI7eDGpheuHYvrYDYZzu9Rjz1dCASY9f7ZtLjUSTRmEpq7YiaL-fwb3iF_9Z7d87U43IXy5-oQ77qMS0hDNujoRk6rydO05Fsqfb3WYeoCcFsSSDKXawbGj0ly6p-w3PUuHiJ0766R60N8Wi2Czb0PG9M51ymuDw3RGsjre14CCKjvd8XqppuRKjzQjdmjJkFr_RILKIS-djb0PsEGUdCKho5e3IzMm03o6GKzQ_xvL8tBVDMyaZ9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شہباز شریف: من به رئیس‌جمهور دونالد ترامپ بابت تلاش‌های فوق‌العاده‌اش برای پیگیری صلح و برگزاری یک تماس تلفنی بسیار مفید و سازنده در اوایل امروز با رهبران عربستان سعودی، قطر، ترکیه، مصر، امارات، اردن و پاکستان تبریک می‌گویم.
🔴
فیلد مارشال سید عاصم منیر نماینده پاکستان در این تماس تلفنی بود و من از تلاش‌های بی‌وقفه او در طول کل این فرایند بسیار قدردانی می‌کنم.
🔴
این گفتگوها فرصتی مفید برای تبادل نظر درباره وضعیت کنونی منطقه و چگونگی پیشبرد تلاش‌های جاری برای صلح به منظور آوردن صلح پایدار در منطقه فراهم کرد.
🔴
پاکستان تلاش‌های صلح خود را با نهایت صداقت ادامه خواهد داد و امیدواریم به زودی میزبان دور بعدی مذاکرات باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122242" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7-p5nDX6EHVXJB1mKPf86B8DvbS93tN35eEZcbUe60tpBDzgis41Bk4zL62HDI0jHYhk5iZWigngcC4cQMUXCGnPv7Rp-JdFk93kw1L6be61ayQvW5y64guiYVLSp3mu1TNgNL8fmwCMC5GEMpOpc60z1nC3zkPS4AUp-1atLibcf3d-VhWm4Enl4UyAWMJggBseWUWZFJgGTtPQJXj2tN-86994nzOXJ2fE15iw1PzuAyhKM95DQoFjDLi1XPiElyPzp7YkrOFONGgsEk4jVtnkcKwsaWljNvI2wLJ_7pIzQ_tIsdAhTKK49ONCLe-baToqMjQ4SnPD7jja0pN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مونیکا ویت کیست؛ نظامی سابق آمریکایی که به جاسوسی برای ایران متهم شد و اف‌بی‌آی برای او جایزه تعیین کرد
🔴
اف‌بی‌آی به تازگی اعلام کرده است که برای دریافت اطلاعات منجر به بازداشت و محاکمه مونیکا ویت، عضو پیشین نیروهای مسلح و مامور سابق ضدجاسوسی آمریکا، ۲۰۰ هزار دلار جایزه تعیین کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122241" target="_blank">📅 10:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آزادسازی نیمی از دارایی‌های بلوکه‌شده ایران به ارزش ۱۲ میلیارد دلار نیز در این چارچوب این یادداشت تفاهم پیش‌بینی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122240" target="_blank">📅 10:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کابینه جنگ اسرائیل امشب تشکیل جلسه میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/122239" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تتر دوباره رفت بالا و الان 170,500
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122238" target="_blank">📅 10:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تشکر ترامپ از سرویس مخفی برای دستگیری تیرانداز دیشب: از سرویس مخفی و نیروی انتظامی عالی‌مون به خاطر اقدام سریع و حرفه‌ای که امشب علیه یک فرد مسلح در نزدیکی کاخ سفید، که سابقه خشونت‌آمیز و احتمالاً وسواس فکری نسبت به گرامی‌ترین بنای کشورمون داشت، انجام شد، سپاسگزاریم.
🔴
فرد مسلح بعد از درگیری با مأموران سرویس مخفی در نزدیکی دروازه‌های کاخ سفید کشته شد.
🔴
این اتفاق یک ماه بعد از تیراندازی در ضیافت شام خبرنگاران کاخ سفید رخ داد
برای همه روسای جمهور آینده مهمه که امن‌ترین و مطمئن‌ترین فضایی رو که تاالان در واشنگتن دی سی ساخته شده، داشته باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122237" target="_blank">📅 10:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری فرانسه: کشته شدن ده‌ها نفر در انفجاری که قطاری را در جنوب غرب پاکستان هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122236" target="_blank">📅 10:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
تسنیم: اسقاط تحریم‌های نفتی ایران در طول دوره مذاکره از بندهای تفاهم احتمالی است
🔴
شنیده‌ها از جزئیات تفاهم اولیه «احتمالی»، میان ایران و آمریکا حاکی است که واشنگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط (Waive) درآورد؛ اقدامی که به ایران امکان می‌دهد در این بازه زمانی، نفت خود را بدون محدودیت‌های ناشی از تحریم به فروش برساند.
🔴
بر اساس اطلاعات منتشرشده، در صورت تأیید مفاد تفاهم اولیه از سوی دو طرف، ابتدا یک تفاهم‌نامه (MOU) اعلام خواهد شد؛ تفاهمی که در آن پایان جنگ در تمامی جبهه‌ها، از جمله لبنان نیز مورد تأکید قرار می‌گیرد. اسرائیل نیز بر اساس این بند به عنوان متحد آمریکا باید جنگ در لبنان را پایان دهد.
🔴
پس از آن، یک بازه ۳۰ روزه برای اجرای اقدامات مرتبط با محاصره دریایی و تنگه هرمز در نظر گرفته شده و همزمان، دوره‌ای ۶۰ روزه برای مذاکرات درباره موضوع هسته‌ای تعریف خواهد شد.
🔴
ایران در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/122235" target="_blank">📅 10:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آخرین قیمت طلا و سکه
🔴
طلای ۱۸ عیار: ۱۷ میلیون و ۸۶۷ هزار تومان
🔴
سکه طرح جدید: ۱۸۶ میلیون و ۵۰۰ هزار تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122234" target="_blank">📅 10:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: دیپلماسی و مذاکره باید بر درگیری غلبه کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122233" target="_blank">📅 09:57 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
