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
<img src="https://cdn4.telesco.pe/file/ZzDp9W0ZDLtejLlQiyPBG8RhXlGzCcQ_fletEC4kPUO2-L9y4xL4bBFV22D2AO5OkVAlWfvdEFzCZI7Y3bHmtK3IvxEeM3Ox0rm_nobh7D9u9fVkjI3p81JqE9rH-UhZgNlL-S2VrrJkiVHRCwg9bVWvdyF9F6XawkjLT4F5eCacKOv-tEDRljrqwKiUZhpC4zZd4Zzd3eQ3ec3OU9jySMZ8p2o2Q8ZamazJ0fCiBzeUoVPmBT-XAUTXAPvhXJwxLhJ4piXOxaZdeSsgeGqFcqN4X65NsrFZzg5oS31Z1ImtiLTSNO-szc2MCFJsLSuBGGDEZSbKqVO-jKhZesQmCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.51M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-660133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای ونس: توافق ایران و آمریکا مورد حمایت سران منطقه است  جی دی ونس، معاون رئیس جمهور آمریکا:
🔹
طرح ترامپ برای حل مناقشه با ایران از سوی سران خاورمیانه مورد حمایت قرار گرفته است.
🔹
ونس در ادامه اظهاراتش مدعی شد که اگر تهران به دنبال سلاح‌های اتمی باشد، آمریکا…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/660133" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TShSenGa23Y9Gr-oXHbVj0wjkCpyDEqaPfe-UT1KOWAw0jzAv-_UowxkenV1MwnWxJJW_PCOyPpFUf75p-PKsCSFxZ7kAQyRL9ZxG5qKWOiVnnFIxoqZ4fOlLZbzr3udw4cM4PvvqGFCeJ9s-lOc23LFkqCMv1C_9PsrP2ILm5gFOebX9dkpVLn-y5-rp7PC9WbgMYMrxJD3f9zjC-Gl_kpPRIksYurOksfMmznxf-XRSIwu8AXA2V8itRRWx1ErTdy82KnUbGHDGvCdQVWNBVE44_jKrdkjZ9ZRvH-5dUPO-1V5lV_g-0whoIBqmpXTLxb7MioxiWhLrXxjX6FaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev0XfawUb70kh16pFWWPmq85nbF3HcEvvL8W7JxR_CstST6B4HEion0pHLviQiJyhs7F1bG33adJ3UpgK8hyHujx-fmjn4x6rNyY_JcFSUsyPz9BBf3rWwOVbNGZwjNrHHaxLFe6tiRdht17SaAXHl2zEM7dKpkxunBkBmc2l0mJL31LUvMvcCe5vKBiX7Cg3RMXDJCTrA8dYOn8AdPEUbcEUp3XH-URlVD4hLmT_fTm36WSiEF_sdeCsnPTGHWhxx3f9eIcs5kMWI6KVplH0xlCVHoOzIGdRfZxjQnqFinTDiHntXQBZF_JV1FbXVmFWLekb5lH17rtfZJutzJCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eA9fi2Rp5CwoTdjPsd8pwzUFQRXb_zTDmrwkRh5vAOsalu6MASbW48E-3cCM4-adEzyqylu73iE-THAMypKjXDk5fXwhNL4ayjaECMtn4YyVi6wARrX_BZ4o2ZBulAX2s0Db4uCfrm_w7sNIg2-HbJiJf5mkpLD_RXcvsHdmIRZ6UZAffsenZZ880QHWuh3cWnX3-WN_eRC3tUEKJHi3Gm7a0fz6b7Hsv3238mYEfg9vJwn33OllxvBCH_iMxYCLj4lUgO9eThJ1mFkIUI9MZb7Kh8z1vu3jroYE9sAwRU9GCkWXP3nKTD8VVSPYHoS3l0V-UELyld2eFVJXJaRNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9IbwUSrfUUAsDbLaTBL6puvKgCNRuwb4lYWCjWc0HYoWEMHsfWHv5bKxJ3aDIaKcUY6S4p5XefMO5axysHUx1mBmMqbdboJrPTtrRJ4RjWybc8J31nmeorD52cq-xsrdjiKWLBv5O96sK71D_rbU5dy5QVqcEbsQ3-JCBIlzHprOx99_5-Kw0MUwmPBHzQwf_mK6fDuIoXtyauFkhAKEOuQSihzL2eadEY1vkHyWSUpJGDYvDFh-RlIcX7Tal39XC0n2OYRxRtW134MmY0WbUGwFOlwHX8eHFYoO92QrvBsAS4TAQClbzWbK18OfzCytGUY6XJyR6JYj-Fs8ftxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3JYON_-4jD2EOTX8QR5GDhLJZ7Jt3CQ7DYw_KepsKM2SWARziWlae7stxgM6Gfxr1l8GYVKlMh_nBKkAtIC1ATDPV6pwe_x0AyiKmfFtrWix5h1XfkwlcugcA_uHh0-NgUmO-qLzGC4H2F9ro3I9LTvXcFmltYtsY7QTzUVY-dlDpmu9M-MaQhRKILGbi8fcKxTbczeLR3OoqRTPRXBOL8EtRt_p51cGGXEYYrpJIPXWcYOzzhCgM6-3z0OGTFpaWs-rUdNLaBbbgdSNvy0FkzFR-3uJ7ztL10GduubS1kht46hJypLGIwsJGRavBMizixo4nr6iP9IS0dzgJQnmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ۷عادت ناخواسته سطح مالی شما تغییر می‌کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/660128" target="_blank">📅 16:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مخالفت آمریکا با دسترسی اسرائیل به جزئیات تفاهم با ایران
شبکه ۱۲ تلویزیون رژیم صهیونیستی:
🔹
علی‌رغم فشارهای مکرر مقامات تل‌آویو برای آگاهی از محتوای یادداشت تفاهم اخیر میان واشنگتن و تهران، ایالات متحده با این درخواست مخالفت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/660127" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادامه اختلال‌ در ۴ بانک؛ وعده حل مشکل در سریع‌ترین زمان ممکن
🔹
شورای هماهنگی بانک‌ها بار دیگر با انتشار بیانیه‌ای از مشتریان چهار بانک ملی، صادرات، تجارت و توسعه صادرات عذرخواهی کرد و به آن‌ها وعده داد که در سریع‌ترین زمان ممکن، اختلال‌های موجود در این چهار بانک حل می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/660126" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHI1CFWbXN5F8cCDplkhvgoPiPFbj-nkKGf0WcbivnSOvXBdd6EukVDi5R9cVNjg6hTZEeWchWYT5kKZGRCH_oMHcmyYU7hr-oghKIvkTGK43oxalZT2DBAz4J_IQdbxVNwpGFELv1TXNqDiJL1PwUrkamwroAQ2CtaiE8KyJsyHhvmAveMdY6gFazeCIAP10dEwq-DEbNSEAjIEl9KvEhtiyNhbW8CQxMdG9h2NAjGdKrv112nXAOL0iUJwNtW5NhOrZ_CKq6Ic1l_UN_EydHCubOCPKdfhVqVPn-MK_PRSqk8HPiPf0t1OPkM7ttdqw9nq-EIp2UZCA4eXkv44qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756924cbaf.mp4?token=E9DstI_NdvAsPinNynoEMsAtzVgozoOTIPE4FXDqve7OVxram9ToZixgSV1cxbWHRqRNPQjAoSHsxweoPTuHFjqZ2hmv5IBQt0ZYKfTFYDxZeIi9pgVDWU-kYZ3b-JX-F1HGUTaveDMi6JQSSn9buTXq_Pv_zD2XHGRrnPusxsK3GPnlogsaE0WnbWK9CGzHt-FEakhdJQ262h7lrlFennkMsRpuNfaXORLgQkN-GsVz9NfdQLKcIOArL3DeMGYlcCEctLR_7E8W_N6TjWhA-D_grCYqIK2pjFWaITLiPGBlFZSeOz_PHntOiqtre9yNx0s5XkZI_7BEwN_d7ZJFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756924cbaf.mp4?token=E9DstI_NdvAsPinNynoEMsAtzVgozoOTIPE4FXDqve7OVxram9ToZixgSV1cxbWHRqRNPQjAoSHsxweoPTuHFjqZ2hmv5IBQt0ZYKfTFYDxZeIi9pgVDWU-kYZ3b-JX-F1HGUTaveDMi6JQSSn9buTXq_Pv_zD2XHGRrnPusxsK3GPnlogsaE0WnbWK9CGzHt-FEakhdJQ262h7lrlFennkMsRpuNfaXORLgQkN-GsVz9NfdQLKcIOArL3DeMGYlcCEctLR_7E8W_N6TjWhA-D_grCYqIK2pjFWaITLiPGBlFZSeOz_PHntOiqtre9yNx0s5XkZI_7BEwN_d7ZJFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«جنین جنین»؛ مستندی که دوربینش از گلوله‌های اسرائیل جان سالم برد؛ اما تهیه‌کننده‌اش نه
🔹
«جنین جنین» (Jenin, Jenin) روایتی تکان‌دهنده از عملیات ارتش اسرائیل در اردوگاه جنین در سال ۲۰۰۲ است. فیلم‌بردار و تهیه‌کننده اثر اندکی پس از پایان فیلم‌برداری در جریان حملات اسرائیل شهید شد. این فیلم به یکی از جنجالی‌ترین اسناد تصویری درباره رنج مردم فلسطین، مقاومت آنان تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/660123" target="_blank">📅 16:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnF-s9CFOUaG3-94ZJOpXkcFvkw3ifHznvbFfRBqa1PoLDY10-Bun9rLptih14IAw0ycYaQOu4TLovbqXzAP2tjk9ol49wj5RyAiYgxL5pODhEOx87FEIVe3_UNMvPxQkiEeSvkVqAaPIOAz6wxX2ZJuojsKkZSdiAxK6Rx7aNc4ggRnVYUOXZ1eoaZ4ivbbSCAh59cuDewU5DUNzgH14e_yhqFHtSaOS0bfYD6baOE5vKY91dBQv_gslBpNXyMEaxKINXG3Alj_PB2oRecDeacQ81OkM7U531R_43YsL8_o5EkyGdTEaqqGqtva0tJ_TKcx-K9xTWbFgUtoI7MXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا ۲۰ درصد سوخت‌رسان‌های خود را از فرودگاه بن گوریون اسرائیل خارج می‌کند
میدل‌ایست‌مانیتور:
🔹
ارتش آمریکا پس از توافق بین واشنگتن و تهران برای پایان دادن به درگیری، در حال آماده شدن برای خروج ۲۰ درصد ( ۷۲ هواپیما )از هواپیماهای سوخت‌رسانی خود از فرودگاه بن گوریون اسرائیل است.
🔹
کانال ۱۲ اسرائیل: «این اقدام پس از آن صورت می‌گیرد که واشنگتن و تهران بر سر یادداشت تفاهمی توافق کردند که راه را برای پایان دائمی جنگ هموار می‌کند. / خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/660122" target="_blank">📅 16:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای
ونس: توافق ایران و آمریکا مورد حمایت سران منطقه است
جی دی ونس، معاون رئیس جمهور آمریکا:
🔹
طرح ترامپ برای حل مناقشه با ایران از سوی سران خاورمیانه مورد حمایت قرار گرفته است.
🔹
ونس در ادامه اظهاراتش مدعی شد که اگر تهران به دنبال سلاح‌های اتمی باشد، آمریکا به توافق صلح پایبند نخواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/660121" target="_blank">📅 16:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حملات هوایی رژیم صهیونیستی به چندین منطقه در شهر النبطیه در جنوب لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660120" target="_blank">📅 16:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a799d3ee3c.mp4?token=aV4OTRRc13bdXrjtaXd-SJcCqhulXxico1CgbIBwSmMNF815sCmaNGAqkQrx7UzNy8Cu2dcI61tW8CAEw7tBGjX8kyuQS39omvNDwBWxSPXSYXQI_iR4Gp83MQnro7lSyBD7G3qyau1RQOiR_qZka14sAm7ymFblQBdC6eI4X7zSPPq08lkyMSKBt6Uy30udYnGKtaS7Me1NrplXOqyLkYqSIp9tedzEl_-NAMKglutj4DFze5f6RGqCVMhQe9XHtwDDbX1v76NuLHwP-aqfrPG_zz8Grl4WgZ1d5H-zUNcxk2wpMv6flTiCmzYgNGgBH7WejtNJ0j0hKWifyuxUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a799d3ee3c.mp4?token=aV4OTRRc13bdXrjtaXd-SJcCqhulXxico1CgbIBwSmMNF815sCmaNGAqkQrx7UzNy8Cu2dcI61tW8CAEw7tBGjX8kyuQS39omvNDwBWxSPXSYXQI_iR4Gp83MQnro7lSyBD7G3qyau1RQOiR_qZka14sAm7ymFblQBdC6eI4X7zSPPq08lkyMSKBt6Uy30udYnGKtaS7Me1NrplXOqyLkYqSIp9tedzEl_-NAMKglutj4DFze5f6RGqCVMhQe9XHtwDDbX1v76NuLHwP-aqfrPG_zz8Grl4WgZ1d5H-zUNcxk2wpMv6flTiCmzYgNGgBH7WejtNJ0j0hKWifyuxUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: توافق با ایران را برای بررسی به کنگره خواهم فرستاد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660119" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تردد بیش از ۴۱ میلیون وسیله نقلیه در کشور
🔹
بر اساس آمار پلیس راهور فراجا، تعداد خودروها و وسایل نقلیه درحال تردد به ۴۱ میلیون و ۲۰۸ هزار دستگاه رسیده است.
🔹
در این میان، خودروهای سواری با بیش از ۲۲.۴ میلیون دستگاه بیشترین سهم را دارند و موتورسیکلت‌ها با حدود ۱۳.۷ میلیون دستگاه در رتبه بعدی قرار گرفته‌اند. کمترین وسیله نقلیه در ایران آموبلانس‌ها هستند که تعداد آنها ۱۵ هزار و ۴۳۹ دستگاه است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660118" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUN0ZBkmcF9oe-GLM0AodAwC-SzYu8HHR7hszO-jQjrbxq-_FMV7HQ22rOY__4JPAhGV9_nif9ZOdpbdBE8Ykko2t8Y886ZgShOHJLIqgdKrqY87d4D2r7piY2Qhmi1PeKF7_L7_W-44ZXwJdpwJfmY-3jIYDC7G1U_nn-VluwRFf8Xzz_70etOn47Ci_qU45Vn_rRbm5hbAi9T82kztv3J2cO_OsijypVjpCjPik3i9rXFEotfSckXoZb2ao_nrEncuYgGyeeYe9DJUeC0XkPil7P_d5lSHm656BG1EdzqbKaIc8SuY9jQMWktz-Ecs5ifEInuBdEbsY_iryw4row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام بیش از ۳ میلیون نفر در بازوی «عدل ایران»؛ ارائه خدمات قضایی قوه قضائیه در اپلیکیشن بله
بازوی رسمی قوه قضائیه در اپلیکیشن بله با عنوان «عدل ایران» با هدف تسهیل دسترسی مردم به خدمات قضایی و حقوقی و کاهش نیاز به مراجعه حضوری، تاکنون میزبان ثبت‌نام بیش از ۳ میلیون کاربر بوده است.
به گزارش روابط عمومی بله، «عدل ایران» به‌عنوان بازوی رسمی قوه قضائیه با آدرس
@adliran
در این اپلیکیشن، تاکنون چهار خدمت اصلی شامل استعلام اعتبار معاملاتی، پرداخت شناسه‌دار، دستیار حقوقی و دریافت گواهی سوءپیشینه را در اختیار کاربران قرار داده است.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660117" target="_blank">📅 16:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تشکر ویژهٔ شیخ نعیم قاسم از مردم ایران
🔹
شیخ نعیم قاسم، دبیرکل حزب‌الله، در نامه‌ای به محمدباقر قالیباف از حمایت‌های ایران و گنجاندن بند توقف عملیات نظامی اسرائیل در توافق تهران-واشنگتن قدردانی کرد.
🔹
وی همچنین در سخنانی تأکید کرد که ایران بدون هیچ چشم‌داشتی، تمامی امکانات لازم برای مقاومت و آزادسازی لبنان را فراهم کرده و اکنون با تحمل تبعات مقابله مستقیم با رژیم صهیونیستی، نماد عزت و شرف است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660116" target="_blank">📅 16:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: تنگه هرمز تا جمعه کاملاً باز خواهد شد
🔹
ایران می‌خواهد این کار را تمام کند و به سر کار برگردد و رابطه جدید عادی است و فکر می‌کنم همه چیز به سرعت پیش خواهد رفت. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660115" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چه کسی می‌تونه ترامپیسم رو شکست بده؟
🔹
برخی دموکرات‌ها از همین حالا برای ترامپ و تیمش در انتخابات بعدی ریاست جمهوری آمریکا شاخ و شانه می‌کشند.
🔹
به نظر شما کدام‌یک از چهره‌هایی که در این ویدئو می‌بینید می‌تواند از پس آنها بر بیاید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660114" target="_blank">📅 16:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای
اسرائیل هیوم: ترامپ در حال بررسی پاکسازی مخالفان توافق با ایران در دولت خود از جمله وزیر جنگ و رئیس سازمان سیا است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660113" target="_blank">📅 16:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای
اف‌بی‌آی: طرح حمله به کاخ سفید خنثی شد
اف‌بی‌آی:
🔹
یک طرح گسترده برای انجام حمله در کاخ سفید همزمان با مراسم تولد دونالد ترامپ را کشف و خنثی کرده است؛ این حمله قرار بود در حاشیه رویداد ورزشی UFC انجام شود و شامل استفاده از پهپادهای انتحاری، تک‌تیرانداز و یورش موج دوم افراد مسلح به دروازه‌های کاخ سفید بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660112" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: تنگه هرمز تا جمعه کاملاً باز خواهد شد
🔹
ایران می‌خواهد این کار را تمام کند و به سر کار برگردد و رابطه جدید عادی است و فکر می‌کنم همه چیز به سرعت پیش خواهد رفت.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660111" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoboaUTjwCUXtbdaTCngaeiP86-1lUpDrEFTHxSM8n1PGRW5e5vladNOvo5dE4E-DzhaRgVj8nkL5uFcaKfZdeO6WRR0LA7-_vjSOTWeU71VtDzA3hhzEdf3CFatQhtZB8noeMjqjOhHd08bnD2aYS0P8TYbJiruXo1FQvpzFwpGXSeOBH0uf1M8VdZdg4QsY7Rr0GawCKo1RFIZriOaWwkFrn3_nbW00V_CfIS13_PYjlkcjz4-PB6D6Jvj-s7QKC4O31E_Qs4kpF3RHECrASyJQDL5_iAlhiH1KmEqsJp96-N8u3BVqX5F27FGILNRNKvI2Y5uUEXKSc4eqnkKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک آدامز: ترامپ ناخواسته ایران را به قدرت جهانی تبدیل کرد
مایک آدامز، نویسنده و فعال رسانه‌ای آمریکایی:
🔹
ترامپ در تاریخ به‌عنوان رئیس‌جمهوری ثبت خواهد شد که به‌طور تصادفی ایران را به یک قدرت جهانی تبدیل کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660110" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hilBBT5N1TIVxbUzc0mnmUbDFRHthHy1Et151viMsKcD4eXLaKQKvKFusrbtHiBEe-qDjuPSiLYLUpkyi7t4_S1eKesjHd16w5cZhKJybVwq8s3l86M4MYrYfOzEWuFU4iKUXJppEniYo_7cD8sRvwF86_bCFTympwy5snDqNpEwBR8rF4Yk52sag8ta8Qe9PnV1CuMV1qieHypss34OMMwoIH-_DI5fkGmOLImEPVZTmzp8ptNT3CGqUpvhkKXOa10datKot8g2mmc14luTawPBs-5SHrhu99GZtKzQp98lpVwHAcR3-NTt68lP34YfA-rZWWUZ9lKgrq-33XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط یک ثبت‌نام تا PS5
بین 1000 نفر اولی که در سامانه کیان تریدر ثبت‌نام کنند، یک دستگاه PS5 قرعه‌کشی می‌شه!
با «کیان تریدر» دریافت اعتبار برخط، ابزارهای پیشرفته تحلیل و نمایش دقیق پرتفوی در دسترس شماست تا مسلط و بدون پیچیدگی تصمیم بگیرید.
ثبت نام:
🔗
kian.trade/kt
#کیان_تریدر
#کارگزاری_کیان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660109" target="_blank">📅 16:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnJPblc-9RA9KdaldcacdgV7qSzG6uspm3fgeJ6YCk87MVYlfeNf3xlgQVET1Ku1TOyMjXzDIHX1U-ikhOxO7e242GtzEsWZ1Tjdi1lhip5XJUM6OlYZm6CjI3puBZ3Y_abzrbsBxI_uzxlmnbKkgfllI6UHxw7i653AVxYoS397zncReChuRVs_kXAfzAHaLHb_NfDmhcloc8lK3euBukZwqZGw12C1oPHo0peKkZaksrHBFyVExqcocbMnSTWS_WeAgxLDNYunolxqiVEqmGix2NStShNCuIPPBrlmKSfW7Wa_-i1txjIoPxxFvdOilcpC-Yb0deIy1MQNgC_bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تراز تجاری» رو زیاد شنیدیم… ولی دقیقاً یعنی چی؟
#واژه_کاوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660108" target="_blank">📅 15:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMtDakpJ3SHyQDuXGPQFphKZK6FkF9HFS577OTysbTXgA7PTq1RhQIFi-G3xSbFjlKSwJASjmDLWhiATIhKC377r1PMPy00S46gOizj-ibflHO9-w8uz9Twq1feD8ExGkdMw_pjeS3yoEWvPRbkPMbzYJ8tsL2Zz7rF30VWJzii5HXcoJFegmo9mKhMWIJZML-iybKP_EtSzBDn5ydzMku965iRkBUZNfugR6Zdehnfe7FGaAYuKNco8cZNdjmU3CLnlfp_XSuldzROH2U7W9zzWh4KI9xvmevjIq8Zrgeqd6xr2yJYhxdP2AWfvNobl2b7gqSf3V2vjPStg4yNolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر در الگوی تماشای فوتبال
🔹
در این نظرسنجی بیش از ۳۷ هزار نفر شرکت کردند که سهم تلگرام حدود ۱۲٪، بله ۳۰٪ و روبیکا ۶۰٪ بوده است.
🔹
بیش از ۴۵ درصد شرکت‌کنندگان بازی‌های تیم ملی را از طریق تلویزیون و شبکه‌های داخلی می‌بینند و حدود ۳۰٪ هم پیگیر فوتبال نیستند.
@amarfact</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660107" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
احتمال وقوع سیلاب‌ در ۸ استان کشور
سازمان مدیریت بحران کشور:
🔹
از روز سه‌شنبه، به‌دلیل فعالیت سامانهٔ بارشی شدید، احتمال وقوع سیلاب ناگهانی، طغیان رودخانه‌ها، آب‌گرفتگی و رعدوبرق در استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، خراسان‌رضوی، اردبیل، گیلان، مازندران، خراسان‌شمالی و گلستان وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660106" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoTRk7k2CLq3z4l28FsxEO-s9q6vzM3hMtkme2vEzkVo1U1fK9r4-C3gky6qJqJRrgcNIuvnTbxCvzWfwoFpWl3BTNwS1ISfjD_3eiycv8n7Dq4ImiCdUhBYcCgpgkZMyzleHa3Css68K7qCPdiQNEQJkoWIzMLaKGF6WwNGeMI7L6XrVDnbafbxcWrqA9LXh2ydbm_XDKK26oK6lQ55a2gVog_DK3hOreRT10zbFMj0sZGQzUXUta2JiQJOV8ogwPRAWVcM5_k0IepO5knzl6aKzv7kKATEdr0rxyrzUnrqccZhQG4Mu8pNlIHxyveTkdTHOEB-cLJXRwHutnmIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ به ایران باخت، بد هم باخت!
نیویورک‌تایمز:
🔹
ترامپ با آغاز جنگ با ایران مرتکب اشتباهی بزرگ شد و این درگیری را در نقض قانون پیش برد.
🔹
آمریکا از نظر نظامی، دیپلماتیک و اقتصادی تضعیف شده و هزینه‌های راهبردی آن را برای سال‌ها خواهد پرداخت، در حالی‌که ایران از جنگ چهارماهه به‌عنوان پیروز راهبردی خارج شده است.
🔹
آمریکا با وجود استفاده گسترده از موشک‌های دوربرد و سامانه‌های رهگیری، نتوانست ایران را به‌طور کامل شکست دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660105" target="_blank">📅 15:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Yyo9VOPcvO2RF4vi6sLpRFH1JRgajzocTHeMgcLhOjkYxqsohC53RVqIspc0nqLkdgPPQtT4naL6lKx2eoKu78GMN_9JUbKDF5nIVpLIlURKKFOIzXdIqVuMIV4OcJX8m2zarNJqaPFygTcXZrhI_LImvgrHk5Bhhb-HDHJ2QXDlU3Wy9IhC4R-FLMyB_glekiuU6VjpviGeDN8vX3SNUoJMnoRBoVTs684-gVywdpQtKJpPDHG7ZGtPbeQSamPLo0jvN-PeTlSUfHpYokyU0fyjDa56I1nJyEHZBPMryG_847d-z2tCtbxOs4r3f30sw7PJs4lXQxoFOqp6mPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رامین رضاییان در تیم منتخب جام‌جهانی تا به اینجای جام
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660104" target="_blank">📅 15:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
احتمال شنیده شدن صدای انفجار کنترل‌شده در دماوند
🔹
طی ساعات آینده احتمال شنیده شدن صدای انفجار کنترل‌شده در برخی نقاط شهرستان دماوند وجود دارد.
🔹
این عملیات با هدف امحای مهمات باقی‌مانده از جنگ اخیر و در شرایط ایمن انجام می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660103" target="_blank">📅 15:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfmQ6cOKcmjFZEVvsJpWwJ4vWymWWB-Ga-PbCb5xfegh1xXNKeMHwRaysPhHoRoHLbGizAFb4JED-nO439zsKpsUKzoa-fRqCSKi8oM7ZG-UY73ZZFW4bEx6mVODMlS0c_2gu183A4-OQiZHg4mY4M8AVRTUi_qN2ATd9_jzVeID5lIuHRnbVlQxNbl3kzqFHgSvbY6MABmg_bOejkycquv0exbVrv8LzhzYgpcoC9YCMcByLkK7dW_JAiWJWCcA08TDJ70rGSkbdo4ica-5gKz9ixc5FmwZKPrBBMVqjGGuumj1WfG3TW_-CtYUrfgCb-5RIdn8k70OJrVLzb1Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه توییتری کاربر آمریکایی به ترامپ
جکسون هینکل:
🔹
ترامپ اولین رهبر در تاریخه که یک کشور رو ۶۰ بار «شکست میده»، و بعد مجبور میشه ۳۰۰ میلیارد دلار بهشون پول پرداخت کنه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660102" target="_blank">📅 15:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی قالیباف و نبیه بری
🔹
محمدباقر قالیباف و نبیه بری در تماسی تلفنی درباره تحولات منطقه گفت‌وگو کردند؛ دو طرف بر ضرورت اجرای تعهدات یادداشت تفاهم تهران و واشنگتن و نقش بازیگران بین‌المللی در توقف جنگ و حفظ حاکمیت لبنان تأکید کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660101" target="_blank">📅 15:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9d19be41.mp4?token=dQLF3Pz3_2vUes9BPZk8uhturaosTyqf4_vy_MHoD-u6-ebst6sq17K03H5h47STOJOh7NePj6m_MAmvnr9IxbT-lpvIuIXmeZl4-5jDhqEZVAgHJrQFCjmlgvK17RQchec0cDvhcyebbMLyqN4bzlJrvWkFEtR0ab24JPWO8SzMtsU7JuKDSIu2HFyJKjUmrcTXWAS14uPmTpVi1wMaLnAjgJPP7ckOebYx3MORIjFV2Ts2O4H3oucEy3kJy4TGda6WQheBceeezVNKuI-UL1MOupKmy6OEXL0HhM-yYSwqKrhtlHdZxBDpgBxhfjYLVjNgQmwspm99SNvbSVtp8ZHS5FJ76stS_9aWDeXR7-ZK4rxJCaZiRSJ9EPfPTfKgG40psR_7ECoxi8-jEVlGmctLceXU7bzz3UN6lGBs6udX1z8lxZpdBGl_dSiiQKnaO8bAjnwaTKxLUZAOd4BQAf3SwMseqNJCJFF7dbt74qKipxDA8WmS_a4t9nk_jCwrmkcRaNxN3a9-hlMtYSLmhETp59CGgMOD7SOg40mYin3ebKToMO8LB-NJP5Ni9hMFN3dOpcpnA1Fyj2RRqqx1mhDuyrCypwiUduBziPywWq7oGJ8o-pemPz873iNWvQ1MAqArbSMg_mJ7veqxPZlvNochJz6Zu097oOiTUYIj3b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9d19be41.mp4?token=dQLF3Pz3_2vUes9BPZk8uhturaosTyqf4_vy_MHoD-u6-ebst6sq17K03H5h47STOJOh7NePj6m_MAmvnr9IxbT-lpvIuIXmeZl4-5jDhqEZVAgHJrQFCjmlgvK17RQchec0cDvhcyebbMLyqN4bzlJrvWkFEtR0ab24JPWO8SzMtsU7JuKDSIu2HFyJKjUmrcTXWAS14uPmTpVi1wMaLnAjgJPP7ckOebYx3MORIjFV2Ts2O4H3oucEy3kJy4TGda6WQheBceeezVNKuI-UL1MOupKmy6OEXL0HhM-yYSwqKrhtlHdZxBDpgBxhfjYLVjNgQmwspm99SNvbSVtp8ZHS5FJ76stS_9aWDeXR7-ZK4rxJCaZiRSJ9EPfPTfKgG40psR_7ECoxi8-jEVlGmctLceXU7bzz3UN6lGBs6udX1z8lxZpdBGl_dSiiQKnaO8bAjnwaTKxLUZAOd4BQAf3SwMseqNJCJFF7dbt74qKipxDA8WmS_a4t9nk_jCwrmkcRaNxN3a9-hlMtYSLmhETp59CGgMOD7SOg40mYin3ebKToMO8LB-NJP5Ni9hMFN3dOpcpnA1Fyj2RRqqx1mhDuyrCypwiUduBziPywWq7oGJ8o-pemPz873iNWvQ1MAqArbSMg_mJ7veqxPZlvNochJz6Zu097oOiTUYIj3b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمارهایی قابل تامل در خصوص وضعیت اجتماعی ایران از زبان بطحایی رییس سازمان امور اجتماعی کشور
🔹
طبق پیمایش‌های انجام شده سه چهارم ایرانیان به ایرانی بودن خود افتخار می‌کنند
🔹
احساس تعلق اجتماعی، ۲۰ درصد نسبت به سال ۱۴۰۰ افزایش نشان می‌دهد
سرمایه اجتماعی در سطح خرد افزایشی است که این شاخص جبران‌کننده شاخص سطح کلان خواهد بود
علی‌رغم وجود برخی نارضایتی‌ها ۸۰ درصد جامعه خواهان نظم و ثبات اجتماعی هستند
🔹
جنگ تحمیلی سوم موجب افزایش اعتماد به نظام، افزایش محبوبیت دولت و همبستگی اجتماعی شد
داده‌ای متقن که نشان بدهد جامعه ایران افسرده است، وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660100" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a063c7aaee.mp4?token=veGDpgr1HOWSGOUWJLsmkVhc8D3qoDv1lZkdYNdJDhIdLjEhaEYbO-9CsOH_-WNfOxB9kJcAmRs9YLGwBjAt5l-uilnhGQSFSp-0k0999p5EThNT2QHbL2Sw2d_3mbfL4cVuwQ_wjLJdoB4Yqyp3BFMNd1vtA2nFm7fakFmgpx_87PlZzZQbmfKOeahE7YI_0lhlsoQP0Ld_rc-ULZjowKchg7H6iVcpeoVsgcc0k4FZqDRKoq8EU23dpFwA9EBJdrbtA3yz0CG_6cS_p9SLzncU43PL7qxQGvbh6RMWlfaumX6_hTVrxP3wkqaBxdV1qYqCoS_NA0foekSe3BFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a063c7aaee.mp4?token=veGDpgr1HOWSGOUWJLsmkVhc8D3qoDv1lZkdYNdJDhIdLjEhaEYbO-9CsOH_-WNfOxB9kJcAmRs9YLGwBjAt5l-uilnhGQSFSp-0k0999p5EThNT2QHbL2Sw2d_3mbfL4cVuwQ_wjLJdoB4Yqyp3BFMNd1vtA2nFm7fakFmgpx_87PlZzZQbmfKOeahE7YI_0lhlsoQP0Ld_rc-ULZjowKchg7H6iVcpeoVsgcc0k4FZqDRKoq8EU23dpFwA9EBJdrbtA3yz0CG_6cS_p9SLzncU43PL7qxQGvbh6RMWlfaumX6_hTVrxP3wkqaBxdV1qYqCoS_NA0foekSe3BFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارائه اسکلت خواهر به جای گواهی فوت به بانک در هند!
🔹
مردی در هند به دلیل نداشتن گواهی فوت، اسکلت خواهر متوفی خود را برای برداشت حدود ۱۹ هزار روپیه به بانک برد. پلیس او را متقاعد کرد اسکلت را دوباره دفن کرده و مدارک قانونی ارائه دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660099" target="_blank">📅 15:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای سخنگوی جبهه اصلاحات درباره احتمال رفع حصر موسوی
جواد امام، سخنگو جبهه اصلاحات در
#گفتگو
با خبرفوری:
🔹
رییس‌جمهور پیگیر رفع حصر میرحسین موسوی و زهرا رهنورد است و این موضوع ظاهرا با نظر مساعد مسئولین مربوطه مواجه شده است.
🔹
بعد از این که مجموعه بیت رهبری، ریاست جمهوری و مجلس خبرگان را زدند، منزل میرحسین موسوی هم در پاستور بود و با توجه به اینکه منزل، قدیمی است، آسیب دید و به جهت محدودیت‌هایی که داشتند، از آن‌جا خارج شدند و در مکان‌های مختلفی جا به‌ جا شدند.
🔹
میرحسین موسوی به لحاظ سن بالا، وضعیت روحی و جسمی، دوران سختی را پشت سر گذاشته که منجر به بستری او شد و بعد از دستور رییس جمهور، خوشبختانه رسیدگی‌های لازم صورت گرفته و امیدواریم این حصر هرچه زودتر رفع شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660098" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شورای هماهنگی بانک‌ها: سپرده‌ها و اطلاعات مالی مشتریان بانک‌های ملی، صادرات، تجارت و توسعه صادرات امن است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660097" target="_blank">📅 14:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoGKAAHsBv2em3iej9H9rINSLAGNj0VxXAr4NE_r01fjIRwD20XzHPmdgvXYDtrgSw9h2klMqckOTdAqHYnGfT7aIa9Q43hA-f82wUAp45AdUC5XYCHsMw__fv2YhxYwcWOi935bRuTBz4Db8wsIxdPvGakVgnT2aVbyi_qSq1zJh8jyGq-P-3Q1Z9c5r8IX59qzq8pN_hF-XtiNsDNBU1KAzMWFNafs0fPIFHSWyJFSTYZpxirOzqkZ7CDDRMlYEvI4opclxD-dkVyW-WNmJm9jqfJYX432_8gYufYlQ97bIqxD8N0h3j8FSaN9K3TMkpDw-BL0mfsiOJRnP8G3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی ایران و نیوزیلند در رتبۀ چهارم پرتماشاگرترین بازی‌های جام جهانی تا به امروز
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660095" target="_blank">📅 14:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879cce3a3f.mp4?token=rQze-uIgJ1SQQ9X_eZip9dHmVSSHGSuDLPjjJkJyUQpJpN8XQ7X59BuQ5sibimL2nGDQ0dCWMHhDJic9m8SBV6y005b_pSDP0cjHWTQtmgoUD2WM7-7oAg9agH0Y2-u_UUMI4k4QHDCqeHNZdxLjLreLgRHn84AZmOCch18bhAtOIbiiQQKpfdqm-aR6ZVxB4klzMU6IE8_IXA7uMRPXa0QcxsI-Nz602Jleho4bsHIv66vu9JEkBC0E9Cj1prUR85JLGYnT-NjHEx-tP8uEJsKSJbmAZ9aFMUL_RWlgsvsxo_bVbsGUFx_rf3SsA0N8SuZm6R7K_h68CASEaytZeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879cce3a3f.mp4?token=rQze-uIgJ1SQQ9X_eZip9dHmVSSHGSuDLPjjJkJyUQpJpN8XQ7X59BuQ5sibimL2nGDQ0dCWMHhDJic9m8SBV6y005b_pSDP0cjHWTQtmgoUD2WM7-7oAg9agH0Y2-u_UUMI4k4QHDCqeHNZdxLjLreLgRHn84AZmOCch18bhAtOIbiiQQKpfdqm-aR6ZVxB4klzMU6IE8_IXA7uMRPXa0QcxsI-Nz602Jleho4bsHIv66vu9JEkBC0E9Cj1prUR85JLGYnT-NjHEx-tP8uEJsKSJbmAZ9aFMUL_RWlgsvsxo_bVbsGUFx_rf3SsA0N8SuZm6R7K_h68CASEaytZeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
#استوری
کلیپ های شب اول محرم و آغاز ایام عزاداری سیدالشهداء (ع)
این خبر را برسانید به کنعانی ها
بوی پیراهن خونین کسی می‌آید
#محرم
#امام_حسین
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660089" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آخرین وضعیت تردد کشتی‌ها از تنگهٔ هرمز
🔹
عملیات رفع محاصرۀ دریایی آمریکا اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660088" target="_blank">📅 14:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ترامپ قمارباز: جنگ اوکراین هیچ تأثیری روی ما ندارد، جز اینکه ما سلاح می‌فروشیم؛ ما هزاران مایل آن‌طرف‌تر هستیم
🔹
اتحادیهٔ اروپا هزینه تسلیحات را تمام و کمال به ما پرداخت می‌کند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660087" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
جزئیاتی از تفاهم ۱۴ ماده‌ای ایران و آمریکا
عضو کمیسیون امنیت ملی مجلس:
🔹
تفاهم‌نامه ۱۴ ماده‌ای ایران و آمریکا بسیار مهم است و منافع ایران را به میزان قابل توجهی تامین می‌کند.
🔹
آمریکایی‌ها به دلیل برگزاری جام جهانی و انتخابات کنگره ناگزیرند که به تعهداتشان عمل کرده و توافق را اجرا کنند.
🔹
نخستین نشانه اجرای تفاهم، حرکت کشتی‌های ایرانی از حلقه محاصره بود.
🔹
شرایطی را ایجاد کردیم که آن‌ها جبهه مقاومت را به عنوان متحدان راهبردی ایران به رسمیت شناختند.
🔹
اینکه بند نخست توافق ۱۴ ماده‌ای بر عدم حمله به لبنان است به این معناست که آن‌ها لبنان را به عنوان یکی از مهم‌ترین حلقه‌های زنجیره جبهه مقاومت به رسمیت شناخته‌اند و ترامپ این موضوع را پذیرفته است؛ این نکته، بند اول سندی است که قرار است امضا شود./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660086" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7wMlrW2AgcTAyTtMytnzobiygwrNxbD3p2P-lnqIH8svdLUo6TPAiFKXnq5vc6NiwJVwBH93K-EtPpmb29Vtqh-wK7D6a2nxvTihMQMsu7cAt3P4LWLFEPzI6yQTRmH1ewZHbBUs1EE3zJFBvO7lIyKupzG9DpPCGQqo1MhMK70EgHVuXSNC2ITaYP-nVD-zYXsLaNoS5rrCYpp_mm6WlBYhqLpRa3rbzf3Pzcyk8GSj91D7Y2HkW8HbhrSxkeHoOx--2WSLc0q3bwkogmPv5_X-7yppP6YyQFFcORLON414IP1CM7TQz0uN_xzou831az49F7mAU_Cn5jp4XlX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات مرگ مشکوک بازیگر زن سریال شربت زغال اخته | آخرین لحظات زندگی او چگونه گذشت؟
🔹
اجه ایرتم بازیگر جوان و مشهور ترک، در ۳۵ سالگی بر اثر آنچه در گزارش‌های اولیه «حمله قلبی» عنوان شده، در خانه خود در استانبول درگذشت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3223371</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660085" target="_blank">📅 14:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw8CMClODvca7ROk57XzJWlTkQlFEESCVVta9f1eTYkFaQCG3-04Ar3auc_CZD0yrKICNN3FWO6w8-de1iwCQ_J_rz4Ef9oxDtVLAhgmnMxMqsLbO8m0uiHbo1emWIwKXKihAm77V4ZY3tcebjNcBYm9Gfks_Ia4gDsFIR7oSr0orJRGnEyLF6lwddM8ZkwMsBKLDEG5Sr7UI6E_Xr-GHj1sCgq57vCkiZwS-6ovUpt8O8xZL0jnA4cT5Q7-WsQmvhkickA7g2d1sn2hC6XwaEBfWlDHvjurwDkWHGsqf7rCPPVs7NVS0gaYRTZgbKHcmsOpcRNdkEhdfkUX1N79UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ کشته در سقوط بمب‌افکن آمریکایی
🔹
مقام‌های آمریکایی بامداد سه‌شنبه اعلام کردند که در حادثه سقوط یک فروند بمب‌افکن «بی-۵۲» در لس‌آنجلس، ۸ سرنشین آن جان خود را از دست دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660084" target="_blank">📅 14:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDpBFJSJaH3CKeR3HBcifDIlLAw4S60xDvRkKsXNqQLMob3HgtrKGZUnY-XI3fge9nY0BDZ-RaVKQGkvdH7MOy4SaINRX2y5wk5n_FRsC2Sff7qhkuF7Jy-NYvyf0_36V8XD9BjtX0uCsTCyyYe0oDoyJDzstks-ingiqXHvAeIf0phE7Y68ox4LVcRiVwyitAiBF0rPmpbQi5wfeiW124YrdCEnUurwL4CYyItXKsqvN7EvtDI_duMYgfF-jfw9TFqKqD-BCnihGQejBfWvaeOyUEc3Ktne6XUkoNMvAh3F--sZOKr9cwRmMBB09gXr_NM5LSHxeWJuJz_x0fnzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای دراپ سایت: دو روانشناس در تیم مذاکره‌کننده ایرانی حضور خواهند داشت
یک مقام ایرانی به Drop Site:
🔹
تیم مذاکره‌کننده ایران برای تحلیل رفتار دونالد ترامپ و تنظیم پیام‌ها در مذاکرات غیرمستقیم، از دو روان‌شناس ارشد در حلقه مشورتی خود استفاده کرده است؛ این کارشناسان از دور نخست گفت‌وگوهای دوجانبه در اسلام‌آباد در ماه آوریل به تیم اضافه شدند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660083" target="_blank">📅 14:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afed014df.mp4?token=LGRJPDm3YyhlaTVPhEN11PHkb-xZp19rHwGEd_RQ6u9bP-K_w2Pl4JE5xNOERt9e1k_afw7SRiWgRWHlEyPqgq5-pEQyifTF4XhwvOtq5N7B2pJR8EYFbTgiVdZKZV3k1nUd3o2tsp6oHgSYMVxs3TXXkhAQz-myO3_L8jzawkvWWl34l1kYQByVfBX9YPossekRaxahgjHKpBsWgTDqH5NPO-C1XSO3uLhINk_61shlbNjcM4Xw1FGN1-zMSX8juUNCBQGCTujcupkwGl-uQmfeaM-kbGNz0bg3PDjJUQnDmWY3IuNZlyA92EyCpz3swrJOIiz44EfM4UDtXY-Low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afed014df.mp4?token=LGRJPDm3YyhlaTVPhEN11PHkb-xZp19rHwGEd_RQ6u9bP-K_w2Pl4JE5xNOERt9e1k_afw7SRiWgRWHlEyPqgq5-pEQyifTF4XhwvOtq5N7B2pJR8EYFbTgiVdZKZV3k1nUd3o2tsp6oHgSYMVxs3TXXkhAQz-myO3_L8jzawkvWWl34l1kYQByVfBX9YPossekRaxahgjHKpBsWgTDqH5NPO-C1XSO3uLhINk_61shlbNjcM4Xw1FGN1-zMSX8juUNCBQGCTujcupkwGl-uQmfeaM-kbGNz0bg3PDjJUQnDmWY3IuNZlyA92EyCpz3swrJOIiz44EfM4UDtXY-Low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: جنگ اوکراین هیچ تأثیری روی ما ندارد، جز اینکه ما سلاح می‌فروشیم؛ ما هزاران مایل آن‌طرف‌تر هستیم
🔹
اتحادیهٔ اروپا هزینه تسلیحات را تمام و کمال به ما پرداخت می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660082" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رکورد ارزش معاملات صندوق‌های سهامی شکست!
🔹
بازار سرمایه امروز شاهد ثبت یک رکورد بی‌سابقه بود. ارزش معاملات صندوق‌های سهامی با جهشی خیره‌کننده به ۱۳.۴ هزار میلیارد تومان رسید تا صفحه‌ای تازه در تاریخ این ابزار مالی رقم بخورد.
🔹
رکورد قبلی که مربوط به ۱۸ خرداد ۱۴۰۵ و با عدد ۱۲ همت ثبت شده بود، حالا با اختلافی چشمگیر پشت سر گذاشته شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660081" target="_blank">📅 14:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52010c5802.mp4?token=pKx9I1i3BYGMOtxTqecxEz1lwBDxRx3i2TbAHldTsLB65fKAmVMsKeN-ASXFgDAbL_SQfVUWdt-GZOCWhPuBgH0dTKgaQfFZHD_0tjadxv0W1fO1tyLSjz_YbdodV9crvfNFHmoglPATsbo6I-VslRFwbs4bKA6zmDr-Nx1Dr0KC1nwNMDOom1--pWfQ1oo6iE2FplIMYdfo1Qwy5ihrAwoIwmY6m9Dl11zmVEs19bxA5ZQzYuUjw3znXbVzZvpBTz94f8SgKGraPIZENZVZcJth4cYBapWzBYTtW4pXKg5wd8JdlTnLf3ImTAu2q7PtArkRGCkK7_8ZU9kiPQzaYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52010c5802.mp4?token=pKx9I1i3BYGMOtxTqecxEz1lwBDxRx3i2TbAHldTsLB65fKAmVMsKeN-ASXFgDAbL_SQfVUWdt-GZOCWhPuBgH0dTKgaQfFZHD_0tjadxv0W1fO1tyLSjz_YbdodV9crvfNFHmoglPATsbo6I-VslRFwbs4bKA6zmDr-Nx1Dr0KC1nwNMDOom1--pWfQ1oo6iE2FplIMYdfo1Qwy5ihrAwoIwmY6m9Dl11zmVEs19bxA5ZQzYuUjw3znXbVzZvpBTz94f8SgKGraPIZENZVZcJth4cYBapWzBYTtW4pXKg5wd8JdlTnLf3ImTAu2q7PtArkRGCkK7_8ZU9kiPQzaYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت پانزدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای یاسر درخشان که به دلیل تصادف روح از جسم جدا شده و به خاطر اشتباه و خطاهایش در زندگی دنیایی از جمله دل شکستن مادرش متحمل عذاب و شرمندگی در بیابان برزخی می شود را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: یاسر درخشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660080" target="_blank">📅 14:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه قطر: قطر در دیدار آتی ژنو حضور خواهد داشت
🔹
توافق فعلی گامی نخست به سوی یک توافق منطقه‌ای گسترده‌تر است که ثبات منطقه را تضمین می‌کند.
🔹
ما در نزدیک کردن دیدگاه‌ها برای دستیابی به یک تسویه میان تهران و واشنگتن کمک کردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660079" target="_blank">📅 13:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای ونس: اگر ایران به تعهدات عمل نکند، گزینه‌های مختلفی مطرح است
معاون رئیس‌جمهور آمریکا:
🔹
اگر ایران به تعهدات خود عمل نکند، آمریکا تصمیمات لازم را اتخاذ خواهد کرد.
🔹
جی‌دی ونس در گفت‌وگو با فاکس‌نیوز در پاسخ به این پرسش که آیا این موضوع می‌تواند به معنای ازسرگیری بمباران باشد، گفت این موضوع می‌تواند معانی مختلفی داشته باشد.
🔹
او افزود ترامپ تمایلی به چنین اقداماتی ندارد و می‌خواهد ایران مانند یک کشور عادی رفتار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660078" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdDgNyN7t-hCaxisIks6WD6Q4C1rnRnisbJrTyzi6_Ky4LS6cXQwV0KisIlLvqoojq_8KaSP9psyR5E-FUU_4XllNY6LPq2gzUMPfI38ygqcULCptpVkRUbMwLIk0t9CwekPnpQnh_cgWq1IIZcjqCLEdHs_UnuUQU9LY9LTTAc_Anf9dcBOcP0cow7nRS5FKBQl_QVnfemm9DWdSyEwhG16dBU6Trwx8TBvUsLITI6vDgykrgwf0H3UQONnrN4hHqtPMD21cG7niZN6S4O1ZGuGCGNbegaDoGvwG24KWr0tzNYn7K8lg_CHppS-DtlLEbUi_C_WIzICVlB3CKIoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۴۵ درصدی سود سپرده‌های ملل/ افزایش سرمایه به زودی
🔹
مؤسسه اعتباری ملل در تازه‌ترین گزارش فعالیت ماهانه منتهی به اردیبهشت ۱۴۰۵، تصویری از تحولات مالی خود ارائه کرده که از تقویت منابع، اصلاح ساختار ترازنامه و برنامه‌ریزی برای افزایش سرمایه حکایت دارد
🔹
مجموع سود پرداختی به سپرده‌های سرمایه‌گذاری مؤسسه اعتباری ملل در دو ماهه نخست سال ۱۴۰۵ به ۵۲۷۱ میلیارد تومان رسیده که ۳۱۹۵ میلیارد تومان آن تنها در اردیبهشت‌ماه پرداخت شده است. بر این اساس، سود پرداختی به سپرده‌ها در دو ماهه نخست امسال ۴۵ درصد و در اردیبهشت‌ماه به‌تنهایی ۷۲ درصد رشد داشته است.
🔹
همچنین طبق اطلاعات منتشرشده در سایت شما نیوز، حدود ۲۹ هزار میلیارد تومان از مطالبات این مؤسسه وصول شده است؛ اقدامی که می‌تواند نقدشوندگی ترازنامه را افزایش دهد و منابع داخلی مؤسسه را تقویت کند.
🔹
طبق اعلام یک نماینده مجلس، به زودی در مرحله نخست با مجوز بانک مرکزی افزایش سرمایه ۴۸ هزار میلیارد تومانی موسسه اعتباری ملل انجام می‌شود و پس از آن مسیر تغییر مجوز مؤسسه ملل به بانک ملل دنبال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660077" target="_blank">📅 13:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e5486b92.mp4?token=Ohy0lDj7Sn9LFMruoZSjjCDLGcNNM1hdgJO8iyS2WlK3rftVJvYj2tp-OP5yUj5zWuD10XrSVCgnEVBgkp4J0dpKjivhGcvAWKFkK8QiKk_K-dBT5yhAnebodWJqp_PXHEcVrnAjvm9D0MIDT0CI0qPVxQW6aunH_319vhgKMNpM66InjX6lMKCtVCYJr_lY8ArjXBjo_bvBOVl51SnzGvoSRF4oE_3Uh0tjKVhMGAy1SH3dUvGFEhZsQ9BZ-iAVcJd1teaGoYl3cpuflr03m3PKtHkeDjQyJCzxdd3IflZtL8rXMgL777mrE0ZAYnsQKVQCUApZERVLVPqUqA5FKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e5486b92.mp4?token=Ohy0lDj7Sn9LFMruoZSjjCDLGcNNM1hdgJO8iyS2WlK3rftVJvYj2tp-OP5yUj5zWuD10XrSVCgnEVBgkp4J0dpKjivhGcvAWKFkK8QiKk_K-dBT5yhAnebodWJqp_PXHEcVrnAjvm9D0MIDT0CI0qPVxQW6aunH_319vhgKMNpM66InjX6lMKCtVCYJr_lY8ArjXBjo_bvBOVl51SnzGvoSRF4oE_3Uh0tjKVhMGAy1SH3dUvGFEhZsQ9BZ-iAVcJd1teaGoYl3cpuflr03m3PKtHkeDjQyJCzxdd3IflZtL8rXMgL777mrE0ZAYnsQKVQCUApZERVLVPqUqA5FKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: بدون من اسرائیلی وجود نخواهد داشت
🔹
جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
🔹
نتانیاهو اکنون باید نسبت به لبنان مسئولیت‌پذیرتر باشد؛ من از نحوه برخورد اسرائیل با لبنان راضی نیستم. #Devil
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660076" target="_blank">📅 13:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdR56ioXN_70aPL4Loho-ZIiTUEvK4lF14SFdkfkf8Rrk4HxTH5aM0r_w-YDTk3u22YofSmsuGNe6TGQn0POK0XjVQGxagpXn1WVOZuQfvQ9Mlp0EkTm9MljNWd-nDaqj_AFUnPcJGbuqYR8KJtyUgmmxCHaqMMBrCJsBaYVU07MYmElt_EODsMxndFEZCKPRfpLe2p9CzT7So4evgpKC8j4x2J0Oyu1yzuC1YICAiN_UM6BdAuWrLt1G8XqEFYxx8a7c2GzTTkTHFuJWQcS-7m9KfacqAHHq8CC-G6eyj8ZJ9OtjoC7SF6Fwlbqr-ujc2cYtpo089lJ0R5hIcQfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEgN9uoTilk5NneOnE8A-m6psCRF9qqMsG7Lab-8eehEfkbnO7APNM2oKDQ0FhnZtewY2poKj6Sj91WhhnjfR20298DuOQHN-FlOZ2lvzTi1d4VmeUQuszjAJOruA76cXKabuETjyDUePtXaFrS3VGLQpH8YmHYd2V0NuOklvJTiEqIybxteZOjgOOuZ-7vW0W_0XDSfpLGxdS0ejouz3hH4SUFybnBC2EpxAwlQ4EbPek5O2MHrnvTW_igSTP3Pr3ZFLiy_TbmdAuoeb4raYb0F3HqVuM7Odt_nYN7hXtRF6zcsQEZLwcy-d7ImRJH2g0i1c4tLHBhd28bAXNKu9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برنامهٔ جدید امتحانات نهایی اعلام شد
🔹
براساس بخشنامهٔ وزارت آموزش‌وپرورش برنامهٔ جدید امتحان نهایی دانش‌آموزان از ۲۰ تیر آغاز می‌شود و ۱۲ مرداد پایان می‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660074" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660073">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رئیس قوه قضاییه: دشمن در روند مذاکرات بدعهدی کند، ما به مقابله و جهاد خود در میدان ادامه خواهیم داد
محسنی‌اژه‌ای:
🔹
مسئولین مطلقاً نمی‌خواهند مذاکره کنند و در خلال مذاکرات از حقوق ملت ایران کوتاه بیایند؛ بلکه می‌خواهند مذاکره کنند تا استیفا و استنقاذ حق کنند.
🔹
نقد کردن و اظهارنظر کردن، قطعاً امری بلامانع و بدون ایراد است؛ لکن نقدی که ما می‌کنیم و حرفی که ما می‌زنیم باید متکی بر منطق عقلانی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660073" target="_blank">📅 13:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660072">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdIYYdkRMvtNsFi6QylBKK4_eMBxWCHf_Q6IGPm_X4L7jZX58V9y556j4nZ5bwNSjdNiFG9TvFZlbDrt1Cv_lF2HTpfIhMbuTG5qshLQf4OlzFr9gLDcI8M-0FMwfu8OJFf5Q51BTjBSdSmrAatZ_h4iXmwA6YJ1GM-0c3-QRx-sofUZDzORhkpYj1ha7t7x5q2wbV2bAzJWopAdQfusOluoolqxUua47XcUm-G3W39vjwqTDL2GFSFDAec3F1s4oaXO_1PGOEwuYx5EZyIJi_vdTcVKBZSbxsO8gIap1WyMUoFCdJccT13GFfWNxi0o-4mHXQzChkGnp2W4dkQbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم منتخب ششمین روز جام جهانی از نگاه Sofa Score
🔹
محبی و رضاییان در کنار رودری و پدری.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660072" target="_blank">📅 13:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شاگردان قلعه‌نویی به کمپ تیخوانا بازگشتند
🔹
اعضای تیم ملی فوتبال ایران پس از بازی با نیوزیلند در شرایطی که به دلیل تاخیر غیر موجه در فرآیند خروج  مهدی طارمی و سعید الهویی در فرودگاه لس آنجلس با تاخیر به سمت کمپ تیخوانا پرواز کردند و ساعت ۱:۳۰ به وقت محلی وارد فرودگاه این شهر شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660071" target="_blank">📅 13:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ترامپ قمارباز: ما توافق‌مان با ایران را نهایی کرده‌ایم. این توافق باید موفقیت‌آمیز باشد
🔹
این موضوع وارد مرحلهٔ دوم می‌شود؛ مرحله‌ای که فکر می‌کنم آسان‌تر خواهد بود.  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660070" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای سگ‌زرد: چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد  دونالد ترامپ:
🔹
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
🔹
اگر ایران به دنبال دستیابی به سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660069" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اعتراف ترامپ قمارباز: تلاش‌هایی برای تغییر نظام در ایران وجود داشت اما موفق نشد؛ فرصت خوبی برای تعامل با ایران وجود دارد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660068" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، حلقه اتصال دولت و بازار برای تاب‌آوری لجستیک
🔺
اتاق بازرگانی تهران به‌عنوان پل ارتباطی دولت و بخش خصوصی، با هماهنگی شبکه‌های لجستیکی، تاب‌آوری این بخش را تقویت کرده و با استفاده از داده و همکاری مشترک، به افزایش تاب‌آوری و مدیریت بهتر بحران‌ها کمک می‌کند.
⬅️
منبع: گزارش معاونت مطالعات اقتصادی و آینده‌پژوهی اتاق تهران
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
www.tccim.ir</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660067" target="_blank">📅 13:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhtmiEAOl7HeK7Lq20Hsj77RY4A2zSzDfohAvZfA5E61hzOhXELzBpX2TNojBAkyDFpt-ZVXWkbfF01T3IZAfHw_eOXatOUSgsOmp2PjaIIGD779Z9FIsIBYqnsmPpyi6VUzGNc-bp6E9VsaLUCmcXz1_PdJg5aHhmRdqKpG6JnpwUISAh2NMFfYgmyqvKPXa0X1tyKfxsmd-QTNoi2qpGybDdt6I8-Ub0yLyH87-ds8lJSyR12EWO7JT2AwMVGee5XK0YcKMMH72DGhCpFFsZ87Lt7DFjvZkvwBEbe-POSgLyowt3GuJBuybs10jeefzCrQg190O8Q-ijgbbc33wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از توپ فینال جام جهانی ۲۰۲۶ رونمایی شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660066" target="_blank">📅 13:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
اعتراف ترامپ قمارباز: تلاش‌هایی برای تغییر نظام در ایران وجود داشت اما موفق نشد؛
فرصت خوبی برای تعامل با ایران وجود دارد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660065" target="_blank">📅 13:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نتانیاهو برای چندمین بار روند محاکمه خود را مختل کرد
شبکه ۱۳ تلویزیون رژیم صهیونیستی:
🔹
دادگاه رسیدگی به پرونده‌های فساد بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی، پس از رد درخواست وی به دلیل «ناکافی بودن دلایل ارائه‌شده»، با بررسی مجدد و با استناد به ملاحظات سیاسی و امنیتی، موافقت کرد که زمان جلسه محاکمه کوتاه‌تر شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660064" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660062">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhXzY2c3OO5lBvHjTyaC4rgeXFNqsmVF5l_gJ3xcWvLePNIfN5eS_U1SzOaTNDFJK_iT1ppor4GEZb-OwAizwly-KTs5fxQKSG3tZvPw2nJ5y1QHdhJ14x1SAOu1IqhM7HTrJXQYeVKwYjAnCdcsUHqzAEBbohXMkZRsNKD3c4PjFFcf1wohCaz-lwUlxTxyyYppiNarXfdo1f4SBE7mxn2AgrrPljYU_WK8dZAqpLSvdWq9QlI0jopukK40yQ8weGbjlxHwQ-Z2S-DNp4uCurEsgsF87DxjsJX3gMWQiO9YadR8Zi_-FGZi0qbYVFfYRrtlYnGmpgo3AG3JDEJ_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کلیک یک مسئولیت؛ کاربران فضای مجازی چه وظایفی دارند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660062" target="_blank">📅 13:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee4549ab8.mp4?token=lGnlpg786xXIcRxqI1f4952GSfmZrEJbFwaqbX3B1q2zfofvJGymLdJ1q73NHU0bnJEyUG79s6W2GyIFtwiCf_x6_fAIZ6KPWbGVTTuQMKYz8-au9gNE2BXyYez2P1LYMifVOTHwuT_YaRTmzbjrf4rpcD8PCKQcPSTlufd85pPvL01xQSEIhI5X5yDse7VMJLQnn1rfZfRR2v75arq9L8G5QOwJcimRGlPpd_GWurz5AQccuZx4feRLLwJp6xxc9K_zAt_bpxsiylBbWyJhw8VmXAUJ7_YqC0yCa5xLbHe3oOVcdzfzyeHDSNEzSr5HZxbFRrPoYEgeFmRCQ1jR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee4549ab8.mp4?token=lGnlpg786xXIcRxqI1f4952GSfmZrEJbFwaqbX3B1q2zfofvJGymLdJ1q73NHU0bnJEyUG79s6W2GyIFtwiCf_x6_fAIZ6KPWbGVTTuQMKYz8-au9gNE2BXyYez2P1LYMifVOTHwuT_YaRTmzbjrf4rpcD8PCKQcPSTlufd85pPvL01xQSEIhI5X5yDse7VMJLQnn1rfZfRR2v75arq9L8G5QOwJcimRGlPpd_GWurz5AQccuZx4feRLLwJp6xxc9K_zAt_bpxsiylBbWyJhw8VmXAUJ7_YqC0yCa5xLbHe3oOVcdzfzyeHDSNEzSr5HZxbFRrPoYEgeFmRCQ1jR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قلعه‌نویی در نشست خبری پس از بازی با نیوزیلند: تیم ایران مظلوم‌ترین تیم در تاریخ ادوار مختلف جام جهانی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660061" target="_blank">📅 12:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660060">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c9f9a7e9.mp4?token=pKp2blmmQ6naPvlAFi0-rciSG92k02ON8ZlsgU6Pf6UzBr28rCj9PATTqM_G-FFwmG4sABX8Z_5OuBwli4R9iGBEKXk5oXfpxWWndINuXNkfIgC7AbnwiwGGTBnAdopTcT6nGkRwQGfynD-uUB4NLAavrhI1bYKImyj2FLHJ1sKIhykvaS1sqJN2WhBN-Eu9wwZuxUOuS4mrrHdiNmGv-p081FExioGWjYWCY8yQDpwKZ0Z0E-G8Yi2LHXkVBMdltXcOsNPGqmnBaF5m-eQuzye8habK61rjGW4ydpU_tMrjDyczmLuEQ5a0qa1TRtkSzeZDo2_ZtX-NWMXH9Bo1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c9f9a7e9.mp4?token=pKp2blmmQ6naPvlAFi0-rciSG92k02ON8ZlsgU6Pf6UzBr28rCj9PATTqM_G-FFwmG4sABX8Z_5OuBwli4R9iGBEKXk5oXfpxWWndINuXNkfIgC7AbnwiwGGTBnAdopTcT6nGkRwQGfynD-uUB4NLAavrhI1bYKImyj2FLHJ1sKIhykvaS1sqJN2WhBN-Eu9wwZuxUOuS4mrrHdiNmGv-p081FExioGWjYWCY8yQDpwKZ0Z0E-G8Yi2LHXkVBMdltXcOsNPGqmnBaF5m-eQuzye8habK61rjGW4ydpU_tMrjDyczmLuEQ5a0qa1TRtkSzeZDo2_ZtX-NWMXH9Bo1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: کسانی که می‌گویند مذاکرات بر رهبری تحمیل شده است، بر ایشان جفا می‌کنند
🔹
متن تفاهم‌نامه ۲۵ بار ویرایش شده است. رهبر انقلاب فرموده بودند که تصویب تفاهم به رای سه‌چهارم اعضای شورای عالی امنیت ملی نیاز دارد و متن در شورا تصویب شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660060" target="_blank">📅 12:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660059">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نایب رئیس مجلس: ما سازوکارهای لازم بر تنگه هرمز را تعیین می‌کنیم
🔹
دشمنان بدانند اگر بخواهند بدعهدی کنند، با ملت ایران و نیروهای مسلح جمهوری اسلامی طرف خواهند بود.
🔹
ما هیچ اعتماد و اطمینانی به  آمریکا و رژیم صهیونیستی نداریم و  نیروهای مسلح قهرمان ما دست به ماشه هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660059" target="_blank">📅 12:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660058">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حکم اعدام دو متهم پرونده کودتای دی ۱۴۰۴ اجرا شد
🔹
رئیس‌کل دادگستری استان سمنان از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی خبر داد؛ این دو نفر به اتهام محاربه و افساد فی‌الارض از طریق استفاده از سلاح گرم و سرد، تخریب عمدی اموال عمومی و خصوصی، اجتماع و تبانی علیه امنیت داخلی کشور و اخلال در نظم و امنیت جامعه محکوم شده بودند و حکم آنان بامداد امروز اجرا شد.
#اخبار_سمنان
در فضای مجازی
👇
@akhbar_semnan</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/660058" target="_blank">📅 12:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660057">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEUrpy4xclSySSxqAzOTbbUUnLXu69aeLdfZZX_a9xo2QRgk8z_NYL3ig8yFNCtmXjUw6WxLam8JeIKg6GzpWqOMmtBEkTuHZgEkWnacvr5goiZQZGqKPI6qRne_BtK6p4Ol6uAs5CSrH3G5EhXq4ZZOUpn3ccmOsAtfVigWQL0gxrLKBTFgkbQagmL-k3iuDKDdxlKWcvWyWqpHTl72WsmwwsnmkxyESZvHSfuEo7cFnmeNWEJQkhy_Z6TvVB4YDsXg0x4tTX3R9Q6PdMtvMuxtK-rVum7nQacUnMp8nfi0q_wo4LOX_szK5nXBC1YYLI0z0BF7pTPclmiuH6Wotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس از ۵.۱ میلیون هم عبور کرد
🔹
شاخص کل بورس که امروز ۵ میلیونی شده بود، در پایان معاملات امروز با جهش ۱۲۰ هزار واحدی به ۵ میلیون و ۱۰۰ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660057" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t492DaFpzKjcPzKQjSc-kr8UP0xueEandBsBNIvecTskmQkMaXtsfRb92Bgs5uWM_OttTHb_oXqm_bEw-6ayH0mhgDA9_jBKPackIhG64dHJx8WwGd1UUhi2VwQHhevp5UE5Qp75010SHlFSyMPrFc2ibOWciEaaqK7upZIfp2qQuHfe49oQXdp1qlyOZgO7ZC8oGziPQJDafLZV2L13EeJpVu1EIXXPYNI_7aT5Jh_v3oKhSPDnBo5V4m0BjqzRWzTtywYOPJqQAzd66Vbw-3to2ruTx2sM3RvGoLJ60K0s7C6MoyHynJ9HNegSf7yK1gydsI0ggIzcTqLK1o39qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نخستین نفتکش ایرانی حامل نفت از خارج محاصره آمریکا
🔹
نخستین نفتکش ایرانی حامل نفت خام با نام «DIONA» خارج از محدوده محاصره آمریکا عبور کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/660056" target="_blank">📅 12:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660055">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMxI1t5dUAe-2fs0BEbF5lbZDvrw17cF-gKI7sxjgUOUJTv7u5LY1o9F0tNwQv_UthW5iU26BTT9EtFGAt_EbD9IMuUs3mZJbcL7x38X1z_8eqsfy9QwupmFrLTVnLx0mSw2qRQ73hu5TwuUGP5lmvOJwJOKShKGivVxHUyTlgRYj_yKJn40rmlyA3bOoutwFCRLwWVm6VafA5SG8dBQ1PTeQgVpUsN_TVnGJuMSQbI5INxmgu8abmzbFsB6PsJfcCXvIFySDiRFBMFC-6ZTlcKFBR8BMc3EAcifcpi1evz8F5zr82f6opAcbc8_Z5ZAL_LhXHMfhQK8_CQJ5UnT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۵ خرداد؛ روز ملی گل و گیاه
🔹
۲۵ خرداد در ایران به عنوان «روز ملی گل و گیاه» شناخته می‌شود. این مناسبت در سال ۱۳۸۴ با هدف ترویج فرهنگ حفظ محیط زیست، گسترش فضای سبز، حمایت از صنعت گل و گیاه و افزایش توجه به نقش طبیعت در زندگی انسان نامگذاری شد.
🔹
هرچند این…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660055" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsaNXffHIkPWb7BZ6mFHxwa30GnYSRmx9UBc4lK5-6nS2Dl0M9dvWglJgZlkIKo1p0NBfQekD3fZxp70A6zz8ziiWSDjWM6rAKbvzehafAgbynNy5gkUsB0jh6eHahsDt483ETR_oU1roQTiLodrwbD4XPq9voBjcgrRSz20APQXqJZaN_GheEOvim_qp_B93YN64vFy6BdHK4KL7N46qC86456SuVe8hLKjqfE-GG7qiluPiRvI6UfZFdtqA6ZKzM7GKAf4dPLXZW0HRedf89K-KQ__IImJAeA-5r4TuHrtcTwYyT35M2TeF0qCSP_RVsd_yXQBSrfHOWfTg0hI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا از شگفتی‌های زحل
🔹
عکس روز ناسا قمرها، حلقه‌ها، سایه‌ها و ابرهای زحل را به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/660054" target="_blank">📅 12:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660052">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ثبت ۵۴۸ اصابت موشکی به جزیره خارگ
بخشدار ویژه خارگ:
🔹
در جریان جنگ تحمیلی سوم بیش از ۵۴۸ اصابت موشک در این جزیره ثبت شده است؛ در یکی از شدیدترین حملات در ۲۶ اسفند، ۵۰ موشک به خارگ اصابت کرد.
🔹
طی دو روز نیز شش شناور مسافربری هدف حمله قرار گرفتند، اما با کمک قایق‌های مردمی و شناورهای صیادی، رفت‌وآمد بومیان و کارکنان ادامه یافت و ارتباط جزیره با سرزمین اصلی قطع نشد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660052" target="_blank">📅 12:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660051">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمله پهپادی ارتش اسرائیل به یک خودرو در جنوب لبنان
🔹
منابع لبنانی از حمله پهپادی رژیم اسرائیل به یک خودروی ون در جاده حداثا به حاریص در منطقه بنت جبیل خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/660051" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660050">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5E_iLQtSiUCNb4K_L4_tZpoHXDw_wUyNn2UPq1KIkvC91gICqXgA6yKkfb0IA9FRlR3W4oxvduAQubwzy1Hgbnpa-mT51s2Qc3IQuHe__L2Pt311rnbsNUmUcd79tiDdhl8pDbPES06A7tDJJdmOb2pL_uvrWntgRb7sQCGJNng34fx3UqcJJm_0yIej3jYvAqLqFXxZl9NVnJ6AN2kjh5aBC89XGBQd-7GBcedd8ZcEIvDIO4eWlBqeG0VTho73vqUdDkWjOCmGD3y4McsdBMgiFSE_FfDRjJ23VB5YYCbL8tNqjNaXmVAm890sK_WSNXWfI_MNd6i3KyTN7r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماقت ترامپ
🔹
کاریکاتور: کمال شرف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/660050" target="_blank">📅 11:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660049">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تخت روانچی: قالیباف و ونس در روز امضا حضور دارند
معاون وزیر امور خارجه:
🔹
در نشست با سفرا، مفاد یادداشت تفاهم تشریح و تأکید شد جنگ در همه جبهه‌ها از جمله لبنان خاتمه یافته است؛ موضوع بازسازی خسارت‌ها، پول‌های مسدودشده ایران، تنگه هرمز و رفع محاصره در متن تفاهم وجود دارد و بخشی از رفع محاصره پیش از امضا انجام شده است.
🔹
محل امضا در سوئیس است اما جزئیات آن مشخص نیست و پس از امضا دور بعدی مذاکرات آغاز می‌شود؛ از طرف آمریکا جی‌دی ونس و از طرف ایران محمدباقر قالیباف حضور دارند و پس از امضا، گفت‌وگوها درباره موضوع هسته‌ای از جمله غنی‌سازی و ذخایر انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660049" target="_blank">📅 11:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c768b2c3.mp4?token=NvzxEj9aauLhMC0vSJx1ndrhWOYB_-4dpB6dAZpSL9RpWWGI-2teFGni_DpJeLKAZ91n0MPtrKPy7lvxxR2TtjWlBL0725xB_L7lXA4QuZ_jmyH_NSJzBw-b4_bJCSSSvalseUvekNzw5i0ANzWxicjUGched6w50xlsFGcVk7Ek8oXFZyerbuMT177ANRGaWw4NbOWo-R6uqstKUV6q4728lBln6HNUw2mE8q6EANpA9ZuVTuc9Fkznn5OQdY_n3A2oa_W78pZrSYd7PMif1MNE50pInAGFe4b9Jb7FYuu5tJkkFKJgapdNLZAOLzfyNbze99EQxrdUyKZJ_C28PJH_ORHdccIr_W6fIlJq23Nw4jnWgnjKLVvmx-RmS4FrPKRK11rXPqdbn5ZXvHruTvgsyKW-kJyAvt8gI2BwfiRjSNIoyp35yP3-v9d6g1pkqeVRnZj1-q-tW5TKfiw5sSCgiqSrns3zChcTTb5y84-WsjA3MnJskUd2Dp1bOCmXpCiBFFKE1qdu0jasOOgq3JeS0bFETTqAUECdsXI7zf4pavOAM4ItV9qVLdeg9VXl3bGxBqFnF76XB0xH3UcrihoOVwHDNE0xrSAGCVXQzqVZsRoSsSn53d6XVVnfXYhMuMz0EvJhzRXTGzYyo5UDy2qLtN4h4W8ZAGMLX2bBdS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c768b2c3.mp4?token=NvzxEj9aauLhMC0vSJx1ndrhWOYB_-4dpB6dAZpSL9RpWWGI-2teFGni_DpJeLKAZ91n0MPtrKPy7lvxxR2TtjWlBL0725xB_L7lXA4QuZ_jmyH_NSJzBw-b4_bJCSSSvalseUvekNzw5i0ANzWxicjUGched6w50xlsFGcVk7Ek8oXFZyerbuMT177ANRGaWw4NbOWo-R6uqstKUV6q4728lBln6HNUw2mE8q6EANpA9ZuVTuc9Fkznn5OQdY_n3A2oa_W78pZrSYd7PMif1MNE50pInAGFe4b9Jb7FYuu5tJkkFKJgapdNLZAOLzfyNbze99EQxrdUyKZJ_C28PJH_ORHdccIr_W6fIlJq23Nw4jnWgnjKLVvmx-RmS4FrPKRK11rXPqdbn5ZXvHruTvgsyKW-kJyAvt8gI2BwfiRjSNIoyp35yP3-v9d6g1pkqeVRnZj1-q-tW5TKfiw5sSCgiqSrns3zChcTTb5y84-WsjA3MnJskUd2Dp1bOCmXpCiBFFKE1qdu0jasOOgq3JeS0bFETTqAUECdsXI7zf4pavOAM4ItV9qVLdeg9VXl3bGxBqFnF76XB0xH3UcrihoOVwHDNE0xrSAGCVXQzqVZsRoSsSn53d6XVVnfXYhMuMz0EvJhzRXTGzYyo5UDy2qLtN4h4W8ZAGMLX2bBdS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
علت دوتا گل خوردن بیرانوند از نیوزیلند مشخص شد
▪️
قسمت سوم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/660048" target="_blank">📅 11:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خروج هواپیماهای سوخت‌رسان آمریکایی از فلسطین اشغالی پس از تفاهم با ایران
شبکه ۱۲ تلویزیون رژیم صهیونیستی:
🔹
روند تخلیه فرودگاه بن‌گوریون از هواپیماهای سوخت‌رسان آمریکایی آغاز شده است، طبق این گزارش شمار هواپیماهای در حال خروج حدود ۲۰ درصد از هواپیماهای مستقر در این فرودگاه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/660047" target="_blank">📅 11:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
خلاصه بازی ایران و نیوزیلند/تساوی یوزها در گام نخست
🔹
ایران ۲_۲ نیوزیلند
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/660046" target="_blank">📅 11:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e24cf28a.mp4?token=SgxZh7vWZeDC_xSkigNLVR6hv-BexAUiDZpG5BYLJwj5HGVWIw5_KDoLUNOJtphcqyKDc0Fa76UHpJkhLTVxAYkHqgAci7uXmSqO1pry0LzIZktBmGaF-9Tc4OFDvu9xUwk8pSCUe2O-J5R0NqEmJFzyMDpXMvLWcHNHoBXVMeM0mfEtKAJlzH7Go7rjiH-HsyE3foURQ9heE-c24Ect_jqgiY_9ZL_q-gpq89hyZQG5JeufvZ6INQjrWJVmJCvqzaVKsuCT14gNLz8duwBl4WIU15GA9_GKY7qTFQVrfBpuyJrw-ENO-MV07-tZATfIM1XsbMOc_e9X_k5P5GoB-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e24cf28a.mp4?token=SgxZh7vWZeDC_xSkigNLVR6hv-BexAUiDZpG5BYLJwj5HGVWIw5_KDoLUNOJtphcqyKDc0Fa76UHpJkhLTVxAYkHqgAci7uXmSqO1pry0LzIZktBmGaF-9Tc4OFDvu9xUwk8pSCUe2O-J5R0NqEmJFzyMDpXMvLWcHNHoBXVMeM0mfEtKAJlzH7Go7rjiH-HsyE3foURQ9heE-c24Ect_jqgiY_9ZL_q-gpq89hyZQG5JeufvZ6INQjrWJVmJCvqzaVKsuCT14gNLz8duwBl4WIU15GA9_GKY7qTFQVrfBpuyJrw-ENO-MV07-tZATfIM1XsbMOc_e9X_k5P5GoB-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی اسپانیا کیپ ورد/توقف اسپانیا در شب درخشش دروازه بان کیپ ورد
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660045" target="_blank">📅 11:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58a283850.mp4?token=Tl9dx3dPaDThSpD4-Jbo1GeZcxQnOny5W9RBnqCF0aaWL4R2ZppADx6CQh_P53h9tX6Z4x3NWoWx-7dqawDVhTa65UnUSM515EqTOkarp1R7bbvukijG_hEejcnY5W3TeFSDqswAQf23iLlYHaGFoQM1EyEVwTgWStTtVASwdTgnyS2RJs6bU6qWmoUgf7uEFOd6lboAN6GIGMa1kHTjduOZ7kdqvfyZLvBbjQPH5XVQFRpJ0aYynaagpd4hsan99GsbNLUynJ9mb3QKvwyEo1Xy9pJZEl0WDXRd0OUVWbYdKyfk7aWH1ICOfMUfGMOcEVbUUxBMB2pljrezizylcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58a283850.mp4?token=Tl9dx3dPaDThSpD4-Jbo1GeZcxQnOny5W9RBnqCF0aaWL4R2ZppADx6CQh_P53h9tX6Z4x3NWoWx-7dqawDVhTa65UnUSM515EqTOkarp1R7bbvukijG_hEejcnY5W3TeFSDqswAQf23iLlYHaGFoQM1EyEVwTgWStTtVASwdTgnyS2RJs6bU6qWmoUgf7uEFOd6lboAN6GIGMa1kHTjduOZ7kdqvfyZLvBbjQPH5XVQFRpJ0aYynaagpd4hsan99GsbNLUynJ9mb3QKvwyEo1Xy9pJZEl0WDXRd0OUVWbYdKyfk7aWH1ICOfMUfGMOcEVbUUxBMB2pljrezizylcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روستای سوباتان با نمایی از دریای خزر
،
گیلان زیبا
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/660044" target="_blank">📅 11:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای ونس: اسرائیل در نهایت با توافق آمریکا و ایران همراه می‌شود
معاون رئیس‌جمهور آمریکا:
🔹
با وجود مخالفت‌های علنی برخی مقام‌های اسرائیلی با توافق اولیه ایران و آمریکا، واشینگتن اطمینان دارد اسرائیل در ادامه این تفاهم را خواهد پذیرفت.
🔹
این توافق امنیت اسرائیل و منطقه را افزایش می‌دهد و درباره آن اطلاعات نادرست زیادی منتشر شده است. او همچنین گفت آمریکا حتی با نزدیک‌ترین متحدان خود نیز گاهی اختلاف‌نظر دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660043" target="_blank">📅 11:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بازداشت عامل اصلی سرقت مسلحانه از معلمان یک مدرسه در زابل
دادستان عمومی شهرستان زابل:
🔹
صبح امروز ۲۶ خرداد چند سارق مسلح با ورود به یکی از مدارس شهرستان زابل که کادر آموزشی آن را بانوان تشکیل می‌دادند، اقدام به سرقت طلا و اموال ارزشمند تعدادی از معلمان کردند.
🔹
با اقدامات اطلاعاتی، عامل اصلی این سرقت مسلحانه در کمتر از سه ساعت شناسایی و بازداشت شد.
🔹
تحقیقات برای شناسایی و بازداشت سایر مرتبطان احتمالی این پرونده ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660042" target="_blank">📅 11:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پرداخت مستمری بازنشستگان از چهارشنبه
سازمان تأمین اجتماعی:
🔹
پرداخت مستمری از عصر چهارشنبه آغاز و تا ۳۱ خرداد تکمیل می‌شود؛ افزایش امسال برای حداقل‌بگیران ۶۰ درصد و برای سایر سطوح ۴۵ درصد به‌علاوه یک‌میلیون و ۵۰۰ هزار تومان است و ۳۰ درصد متناسب‌سازی نیز اعمال شده است.
🔹
زمان پرداخت معوقات متعاقباً اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660041" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5dfbd87db.mp4?token=VPB1W_jlhFD1FiJFQc-AK5AySqAdpoX_5iAByw-cUTXQJUTGewP699znCl3T5jJWDdyxEWQ8sFeeoErxBDs7OsM52VIVIRhOKPPBRovDNc7fiOROYRTlk_GDlLB89aagVmwg__k7qiSNwsfit0iGcIE0GKJ6Sb06XGEwAj-TvIB0DYW1uOxwuHs-yV0GEU6GXp2puP3hb6IpNssQm1vaJIUsXjayRqo5GBuru5fXs2P4Sbk3mk9t93buKSRufoLLsexsRr7iNM7hBnw_KSnVr4wq7uj1BBGVFRY9bvSR-TuQ2C3NV2NGc5zacNHBuR4ddpUu7xKVe1g5_bI1VVmMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5dfbd87db.mp4?token=VPB1W_jlhFD1FiJFQc-AK5AySqAdpoX_5iAByw-cUTXQJUTGewP699znCl3T5jJWDdyxEWQ8sFeeoErxBDs7OsM52VIVIRhOKPPBRovDNc7fiOROYRTlk_GDlLB89aagVmwg__k7qiSNwsfit0iGcIE0GKJ6Sb06XGEwAj-TvIB0DYW1uOxwuHs-yV0GEU6GXp2puP3hb6IpNssQm1vaJIUsXjayRqo5GBuru5fXs2P4Sbk3mk9t93buKSRufoLLsexsRr7iNM7hBnw_KSnVr4wq7uj1BBGVFRY9bvSR-TuQ2C3NV2NGc5zacNHBuR4ddpUu7xKVe1g5_bI1VVmMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: اجرای رسمی یادداشت تفاهم از جمعه آغاز می‌شود  وزیر امور خارجه:
🔹
مهم‌ترین دستاورد مرحله اول، اعلام خاتمه فوری و دائمی جنگ در همه جبهه‌ها است که از صبح دوشنبه و هم‌زمان با نهایی شدن توافق به وقت تهران اجرا شد، هرچند اجرای رسمی مفاد تفاهم‌نامه از روز…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/660040" target="_blank">📅 11:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عراقچی: جمعه دور جدید مذاکرات ایران و آمریکا در سوئیس آغاز می شود
🔹
روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود. بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔹
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/660039" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تلگرام در هند مسدود شد
وزارت آموزش و پرورش هند:
🔹
هند برنامه پیام‌رسان تلگرام را تا ۲۲ ژوئن (اول تیر) مسدود کرده است، زیرا از این پلتفرم برای «کلاهبرداری از داوطلبان» شرکت‌کننده در آزمون ورودی پزشکی استفاده شده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/660038" target="_blank">📅 10:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عراقچی: جمعه دور جدید مذاکرات ایران و آمریکا در سوئیس آغاز می شود
🔹
روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود. بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔹
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام خاتمه جنگ است و بنا به تصمیمی که گرفتیم از صبح روز دوشنبه به وقت تهران که این توافق نهایی شد، خاتمه جنگ هم اعلام شد. ولی شروع رسمی تفاهمنامه از روز جمعه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/660037" target="_blank">📅 10:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DviaNNWiggnwGp33dYrhVgJ6B-Qvh76vnDLJpEINtaDkIkuS5Z0roTPtDDhIcD0-zg6pE6AGglt76zIY5-RNU__1gki7evaqYeodN44nMcfXcELJeVXJZ1q9_aNXmcY-3YpA551Ue6sHTzB2DIArUnRXBpyFpHAx8386B-r0T7Me-YTxakaty94qYhOtFIgxy6fl-JojU-FgB07nYKRe1B6EPH-FaKg3yIVVfkdx0iwh21bUDiWmQaBPia5x-YDdee89G0IFOlgecpf221FchIm5dnSsfJ7SEpqbslYELzZr5ROdZUN7uoiSCHjVZMsNdogetwrIRErn_SYRXA5fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۷ میلیارد دلار ارز صادراتی در سال ۱۴۰۴ بازنگشت
عضو کمیسیون اقتصادی مجلس:
🔹
بر اساس آمارهای منتشرشده، حجم ارزهای بازنگشته در سال ۱۴۰۴ حدود ۱۶.۹ میلیارد دلار بوده است.
🔹
در سه‌ماهه نخست سال ۱۴۰۵ نیز حدود ۳ میلیارد دلار ارز صادراتی به چرخه رسمی اقتصاد بازنگشته است؛ مجموع ارزهای بازنگشته از سال ۱۳۹۷ تاکنون بیش از ۱۳۰ میلیارد دلار برآورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660036" target="_blank">📅 10:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660035">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkhsf3p3Ny5u5rhgdpjRP_KNApHHKg-OyqEt3jbjQKe67kVSE_fI8QrC2fhGOmD3AO_mso7ilIuAcPUiTRrNkgCwaiw2gchgB7L9oiZhmaIJD1nCJkv-OkuvJBlRnKierw9CjGnk_COPiF047VG5UgwRzMJbVbWrN2_y_-wpO-NNFUv79t1W87dvskCk75TflPP1AU3p1NLejJxit4kHZb3FrqHpWADp69kM-Hp5E61fj0NVq32nHHiPhCwTIvo-3rO4lkn7FG-uDaLI7zzdYBLi7IiREHW1zmOLYz6aAKmWVFo3N1UfV0NYVI9ejjLRsJkUMjaM4bdxG_Q77uBjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاید امروز در سایه باشید، اما فردا زیر نور حقیقت
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660035" target="_blank">📅 10:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
فرمانده‌کل ارتش: هرگونه خطای دشمن با خشم انباشته مواجه می‌شود
🔹
دشمن در جنگ رمضان و جنگ ۱۲ روزه به‌دنبال تسلیم ایران، نابودی جمهوری اسلامی و حتی تغییر نقشۀ کشور بود، اما هیچ‌یک از این اهداف محقق نشد و در نهایت خود به‌دنبال آتش‌بس رفت.
🔹
برآورد دشمن از مردم ایران اشتباه بود؛ ملت ایران با حضور در صحنه نشان دادند در دفاع از کشور، اعتقادات و نظام اسلامی ایستاده‌اند و بخش مهمی از این نبرد را مدیریت کردند.
🔹
اگر دشمن اشتباهی بکند با یک خشم انباشته مواجه خواهد شد که کار دشمن را بسیار بسیار سخت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/660034" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f609ab13.mp4?token=m2vQQnNIUURA8zy_-HV5pZONT1QEXBijfxwJvA5Bkiu1YfKTdjnYVDL7l97Q-BMqEXE4eCfB5n0UgBGzqPUXw03AWIgzE9P9VtpVl9GPtII1H90Yh1THKvdbzeLTERWtu_WjpxowQ23bmqQXClHxP1Uh1HF7stQ02c7bOHBXjMLzsuHQviP_o8j3zECPHhmq7Itd2YBjs4mZH2h2AVlso2Ppl6-w9XtkdhgU7lNVdH0I2hXrWmwmAXG6A6VJU3TZIRsKFaNykEJBLzuLIX0m3ijlQG-zZ9i8vcLlkEfRQN1OiYCc_WOVD620Mzb13_dy9oTpPRxy9wNf6L06KgNF0knd-P1UuZZf7GhLiCXJdSN8R1LRx4FhG136zjpRXMVgmjpmmXL5CXC42LzNU2oHYwPI81z16IeEvNEMxG6woXvteyKX-SpksOPzEWVY4Urz_jkAYrEi2K0mN--RYMnUJdLY5qpkCYGKRIxTIRB3kRD6xdjglz1XcFlgTyUhNRrJ-d-Mek-t6VgDeHwR0hnizBYSX48g_wwM0S5zmxHUYqxaXKUMHuSEUKZWVB2h6-OxorlvFqsgamw6C0FKckveNCAI8DUHeWF0Yg9M6WQErXpHogSdANL-fdQwBPhmeIQ8pPWeNqEpfVKYauKKu0RS7gHzrg5lTOoV9Fg_bWk-imM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f609ab13.mp4?token=m2vQQnNIUURA8zy_-HV5pZONT1QEXBijfxwJvA5Bkiu1YfKTdjnYVDL7l97Q-BMqEXE4eCfB5n0UgBGzqPUXw03AWIgzE9P9VtpVl9GPtII1H90Yh1THKvdbzeLTERWtu_WjpxowQ23bmqQXClHxP1Uh1HF7stQ02c7bOHBXjMLzsuHQviP_o8j3zECPHhmq7Itd2YBjs4mZH2h2AVlso2Ppl6-w9XtkdhgU7lNVdH0I2hXrWmwmAXG6A6VJU3TZIRsKFaNykEJBLzuLIX0m3ijlQG-zZ9i8vcLlkEfRQN1OiYCc_WOVD620Mzb13_dy9oTpPRxy9wNf6L06KgNF0knd-P1UuZZf7GhLiCXJdSN8R1LRx4FhG136zjpRXMVgmjpmmXL5CXC42LzNU2oHYwPI81z16IeEvNEMxG6woXvteyKX-SpksOPzEWVY4Urz_jkAYrEi2K0mN--RYMnUJdLY5qpkCYGKRIxTIRB3kRD6xdjglz1XcFlgTyUhNRrJ-d-Mek-t6VgDeHwR0hnizBYSX48g_wwM0S5zmxHUYqxaXKUMHuSEUKZWVB2h6-OxorlvFqsgamw6C0FKckveNCAI8DUHeWF0Yg9M6WQErXpHogSdANL-fdQwBPhmeIQ8pPWeNqEpfVKYauKKu0RS7gHzrg5lTOoV9Fg_bWk-imM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۶.۷ ریشتری در اندونزی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660033" target="_blank">📅 10:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719ebe32ce.mp4?token=RMFTG81A70eT9fo7BbUIuXAcy528DKn0Qqps-1ZoiGzxqNzZaWcMraTaUDyAl1H0ahl3foCMeWRZAz8RBMSDU0a1o_FHxgRj19m6jJ9HBNHhBFUlE52pIltzxIp82zenAoutzp0ZZdGjAaeqbYb7KVlCrHXH5MQdX2FK511BYqDKqgGW_3DqUzToybb3LTCq_kT8TCiltr-vFnXVWObgTUdCuRiOMZuM4VXAHHE79190TTZpwSgcFaIcUtDYY2vJaG_W5HxrlatM82IKY0dwinGyO4KjeHaNw2GtaWtVmCd2MXOCxn8SdbwsBzZE3DSyqQbtSngHLM-_OIDLr9KVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719ebe32ce.mp4?token=RMFTG81A70eT9fo7BbUIuXAcy528DKn0Qqps-1ZoiGzxqNzZaWcMraTaUDyAl1H0ahl3foCMeWRZAz8RBMSDU0a1o_FHxgRj19m6jJ9HBNHhBFUlE52pIltzxIp82zenAoutzp0ZZdGjAaeqbYb7KVlCrHXH5MQdX2FK511BYqDKqgGW_3DqUzToybb3LTCq_kT8TCiltr-vFnXVWObgTUdCuRiOMZuM4VXAHHE79190TTZpwSgcFaIcUtDYY2vJaG_W5HxrlatM82IKY0dwinGyO4KjeHaNw2GtaWtVmCd2MXOCxn8SdbwsBzZE3DSyqQbtSngHLM-_OIDLr9KVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
بهترین فیلم کوتاه امسال
بهتره اصلا از دستش ندید
قطعا ‌دو بار خواهید دید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/660031" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z85xkVzCJ4Vmiia35UWHS5PIse07mMCbKU8P1Lw_OVE-bNjdmdwmDoqqqpcNAf0o6SVLtuwLGYTB0gLseqOp-BPj-Ho8wnGhi1yLdKJ5C7R5J-SImgD2Z28LrWflDAYdv5svDmsjm8ztOrwjImCjJiFjGh66VdaQ3YR9eS0FR3ikFpNJscwf9UmDDpUwH2j0JU84qG6IQoTPjO5zvmoV0SWnN2rh-fXN1isNoua5ROhIuhtlDKFX8Cyh7rtn7mpiZcoOiX0YDKp1eHnjAeJLa39qvNFvFhEjo-ng9KY5cMaBAKclKXy87qAH_kFBG9PMJ5mEfF5JROQSIIsedvQLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: همواره در جهت مقابله با هرگونه تهدید دشمن و حفظ دین اسلام و کیان ایران اسلامی‌از هیچ کوششی دریغ نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/660030" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660029">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEOIi0h0e6XDl1fOfwvEUQWSDuo6RkeFao3QIvrsHK5r6yqtOybO8IzDKo3Ns1FSzLwH-b3qjVF8mH-QwZSQxWMB71Lr35tzX4m1y77uY3A_2nsmWPAiqWLl-Ca_ggweI_dLyyb7dJPWzWi7mVehjwL4nRsqd_YMwaN27uPcvBDz-BIwIaU3g-V6TYCfZq9Br2Sn0tfi9uAHcMSIPyJRbpV-THM_uGvpwriZHic1EYWuTc_TXS-4212aYzXLxpUVxQ4O9alv7hAT1tMjb-_Rdkc56ISasBX-zVOyUZ0Vyqb0pncCj4HAw429Y348P4Iq1na0GA7nqQrNDZ_UuIQWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی و الهویی در فرودگاه گیر کردند
🔹
کاروان تیم ملی پس از دیدار مقابل نیوزیلند در حال بازگشت به تیخوانا است اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس با تأخیر و مشکلاتی همراه شده. به طوری که در حال حاضر تمامی اعضای تیم ملی در هواپیما حضور دارند، اما این دو همچنان در مراحل نهایی خروج از فرودگاه هستند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/660029" target="_blank">📅 10:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660028">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ونس
:
ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
معاون رئیس‌جمهور آمریکا:
🔹
رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/660028" target="_blank">📅 10:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660027">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZE9GaE7H31kMwDtxGItZ_BfTPMKLBoYuyGufqiWbAH51YMpffMUlnzNwioILwo7N-RYIhKIm3p1qZVWwLml0KjFVrhDYDWY3C1iazAhTo3aMRYMCn_bYvEDH4RZGPrQKy77eBEs7ofahfS_dB_SoZt9dW_73uWYeA0rcvezzHz7_HRL4uiY_LngdhF8yOO1SBnuBl_KpKNHt6XEd1EAkmJbkAGSeoCNirGdknlBTSsJ7EvhacP9LQA21qTvpo9VMDjjI-AaM-OgNPQty90QVK3FYN7XHmFOobqZ6FryykEcZPIx5WK3U__3G65LmVcNQpikMNkEZiQOW7sUcS0S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/660027" target="_blank">📅 10:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660026">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
صادرات مازاد پتروشیمی آغاز شد؛ بازگشت دو مجتمع بزرگ به تولید
🔹
معاون وزیر نفت: برای محصولات مازاد و انبارشده مجوز صادرات صادر شد.
🔹
مدیرعامل پتروشیمی: دو مجتمع بزرگ دیگر این هفته به مدار تولید برگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660026" target="_blank">📅 10:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660025">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRTwLGyllTRNt5PV_wMcOhFb0n9rIeX5SsKInUtdEBQaNkb_6WRHQ8A4FmoSWAVlrfwKzcLZxAuKnO-99T7_0kni6-hMGn8izCbzR5jaYj7J0jlPsSczkWI6xNT6x8gFGO30NQ5v5SvNd5uUNRpB_8q3IAPwf9bDalBtnC-SotP6CVjuTNM-K-yyjlvUcweHhRfhDBkden20EKZcuyh7lvxSktH3oxenWPS0aRfyAxlTEmhndllZDfNvjIP-zTmznlwJJ-0UkH9JNDzDcz64cu-lURsGLOD443pp_Sp2K5VnrQh0ErVud9yWmXw4ziDdrdrKvBrdCT4YIOAE0tYvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویزای مهدی ترابی منقضی شد!
🔹
مهدی ترابی به دلیل ویزای یک‌بار ورود، پس از سفر به آمریکا با مشکل انقضای روادید مواجه شد و فدراسیون برای تمدید آن اقدام کرده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/660025" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660024">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161a83f9dc.mp4?token=hRyoZ2EK4kyrWC8sV1cfQFbDq8JUYuNhFJ2eHvf4cZWBp90Ephqn_8G-7-ey9wkzx7_pxd9WJa10FfIzeRAqvr9poZrv1fSNM2Ft_kMvNoSfIH9fkXLdx_FxrMgR9Uc7Et7mZ7FPaXRjePjwvlLXQSg2S5EEkThfqWMqkikwsB1LIToooEHHZflnOLNMM6fbV5sVyXt9RRPL9vbH9JgMhnghzyvMvrxy2brw-lA0DHlduLJ9Sx-fn5V_Z0QNzyL_r2SZ_ctCRSqcNHEtWgJ0xl2xO1rLUy7NERoXPxM96CKQ0YJ5vyWDSIx_mN1vB3WVpNHQml-7XxfUltGEGN6jUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161a83f9dc.mp4?token=hRyoZ2EK4kyrWC8sV1cfQFbDq8JUYuNhFJ2eHvf4cZWBp90Ephqn_8G-7-ey9wkzx7_pxd9WJa10FfIzeRAqvr9poZrv1fSNM2Ft_kMvNoSfIH9fkXLdx_FxrMgR9Uc7Et7mZ7FPaXRjePjwvlLXQSg2S5EEkThfqWMqkikwsB1LIToooEHHZflnOLNMM6fbV5sVyXt9RRPL9vbH9JgMhnghzyvMvrxy2brw-lA0DHlduLJ9Sx-fn5V_Z0QNzyL_r2SZ_ctCRSqcNHEtWgJ0xl2xO1rLUy7NERoXPxM96CKQ0YJ5vyWDSIx_mN1vB3WVpNHQml-7XxfUltGEGN6jUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد فالوورهای شگفتی جام‌جهانی ۲۰۲۶ سر به فلک کشید!
🔹
وزینیا، دروازه‌بان کیپ‌ورد بعد از درخشش مقابل اسپانیا (۷ سیو و کلین‌شیت)، از ۵۰ هزار به ۱.۶ میلیون دنبال‌کننده در اینستاگرام رسید.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660024" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660023">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bcc6de0a.mp4?token=i2_sdtUu6fY44DLxw8OSoOb7BTs96VRzvFZAves8fYp-0uw7KsZdxGTJTIChBduIwOtCWH9oIodOzImIqvDSOpSwemT2Hhg06Uhs1Bdd5qluul3N3Ei9y6H5q6qQ-_e3tOUSqgXAyqDiJ3vVwmqpFuI_QwG6vKssPsHzUYjyLd14S9upAAFyANew2IUcgmNiXqgfQTs-_SZAXUaBWvBvlM3aM41q2wETDzo4JrdkBaUdTgqTrRVe1BRHs28Ljd5Hvu69lg8HrnFQi0m96UjZGEJwt-XPAuOwVe1xhgHpp_QG2LHZQO2Y6Gq9yzuAg4aaWLnEnIfgVVlkXGpy8XZ8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bcc6de0a.mp4?token=i2_sdtUu6fY44DLxw8OSoOb7BTs96VRzvFZAves8fYp-0uw7KsZdxGTJTIChBduIwOtCWH9oIodOzImIqvDSOpSwemT2Hhg06Uhs1Bdd5qluul3N3Ei9y6H5q6qQ-_e3tOUSqgXAyqDiJ3vVwmqpFuI_QwG6vKssPsHzUYjyLd14S9upAAFyANew2IUcgmNiXqgfQTs-_SZAXUaBWvBvlM3aM41q2wETDzo4JrdkBaUdTgqTrRVe1BRHs28Ljd5Hvu69lg8HrnFQi0m96UjZGEJwt-XPAuOwVe1xhgHpp_QG2LHZQO2Y6Gq9yzuAg4aaWLnEnIfgVVlkXGpy8XZ8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ عادت کوچک که سلامت روان شمارو نابود می‌کنه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/660023" target="_blank">📅 10:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660022">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rol9KTErSu-2UFStpXghbxQKkNt_EriB8KcDqmy7X4TBUIDFGM0_w9NNOPJxiRc7FT_Uztp05KCQHPaTrUO9m6pT5V-6W0KoVb04naBAyqoic46mfXYdM1hScmO-nXFCv_vf_sUj3ED0VbOoiyt30ib28AV0TzxLvfVNi2bqCb8Nj4sJIqpt9HXHQFBHQtSCOeuSSggt00Bdpp19Pfxq80wkyeoBVq_8odueCR3jVJ1u9fsIOrOzmJwRa6jDclKcjqKo-2c_K8wiKPcFIOvoRwDPaUYi3tcTKtisjoUqZTh1QvfIUTH9qkoq72--difi50sWUId3wMmlsEswOKF-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس‌های مختلف بانک ملی همچنان با اختلال همراه هستند
🔹
با وجود گذشت چند روز از شروع اختلال در خدمات بانک ملی، بخش‌های مختلفی از نرم افزار بام همچنان به روال سابق بازنگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/660022" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660021">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سند مالکیت پهنه‌های اقتصادی و شهرک‌های صنعتی ۳ استان زنجان، قزوین و یزد صادر شد.
🔹
درگیری بر سر جای پارک خودرو در شاهرود به چاقوکشی و مرگ یک نفر انجامید/متهم دستگیر شد.
🔹
بختیاری‌زاده فصل بعد هم سرمربی استقلال است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660021" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660020">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI4Sbs_mdKOI7RtBs0tjGikQFLY3YsEJw92nLvnWz25m3LoZHMtUeHw0Da4l5cOukRFgyU-TVvU-wtrzY6mfohGNWGI9BCh6m5rOUrUl39CssnvByCXYkIbL-F6Jb9sB--aI_I2qv2XTsJ9QOZORDFrAnXxeM-3QHjx07acEBqjxp3nyi6RW6Q5Ah72IStLvGwDQRBJQexoYQH9DOMtsG7Yfs_Cdkk0zNobGXqJnXvuKXWeLPnOe1Mr5D_T91pMrKPn3H8_VD6DDgPVjprgv6nzmhCltTZmflxTlWVjIPu9k-GNplzk4v5RlocJ7e9w-Dx6k6mes6KcAWvxGlV3T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از تیترها می‌شود فرار کرد،
از دوربین‌ها می‌شود پنهان شد،
اما از حساب‌کشی تاریخ نه
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660020" target="_blank">📅 09:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660019">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فعالیت رسانه‌ای مشکوک در خدمت باند فساد بانکی و بیمه‌ای
🔹
همزمان با تشدید روند اصلاحات مدیریتی در برخی بانک‌ها و شرکت‌های بیمه، تحرکات یک شبکه رسانه‌ای مشکوک با محوریت فردی به نام س.آ فعال رسانه‌ای خارج نشین در فضای مجازی افزایش یافته است
🔹
این جریانی متشکل از افرادی است که خارج از کشور فعالیت می‌کنند و بدون برخورداری از سابقه حرفه‌ای مشخص در حوزه رسانه، با انتشار اخبار جهت‌دار و  کذب، در پی ایجاد اختلال در مسیر مقابله با فساد هستند.
🔹
این شبکه با استفاده از صفحات و رسانه‌های مجازی دارای مخاطبان غیرواقعی، تلاش می‌کند افکار عمومی را نسبت به تحولات اخیر در نظام بانکی و بیمه‌ای منحرف کرده و از برخی مدیران مسئله‌دار حمایت رسانه‌ای به عمل آورد.
🔹
دریافت مبالغ سنگین از مدیران در معرض تغییر یا برکناری، با ادعای توان لابی‌گری و تاثیرگذاری بر  انتصابات بانک‌ها و موسسات بیمه، بستری برای اعمال فشار رسانه‌ای و تخریب سازمان‌یافته این جریان فراهم کرده است.
🔹
انتظار می‌رود دستگاه‌های نظارتی و قضایی با دقت و سرعت، ابعاد مختلف این پرونده و ارتباطات احتمالی آن در داخل کشور را مورد بررسی قرار دهند تا حلقه‌های فاسد بانکی نتوانند از این جریان در نقش منحرف کننده مسیر برخورد با فساد در شبکه بانکی و بیمه بهره ببرند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/660019" target="_blank">📅 09:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660018">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSC1CtMahBGO9AusrjHxxIQ0jwjLLrFvEYfKSNhb2oO5xeFFmeyR5rivpN1rNEldse0RcRYS_nz14fBhnX_MKqYEY9F04VKgNNSsO7tk2AASwjr_z_lYQB23khUR4clx9mlXZHPXMK5-M1G4xvsweAEs9QIFwNGoGmtTjs3LeD6psmlP0n03hp2ybGx_pUWWBz_qn3TZN49O9gKICvkwYujH7GfGXG7goBrAM-SqmQPfme1Id4pf6sZCvVbQaWyKymqzA8keEVTn2Nwv2tJx08tOrGRwyXrFsDNTJ82ZRvoFGEK1a3PVOTE675aLwqXEmIf4hMmN8iinCAjxO2ZB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا به وزیر افراطی صهیونیست ویزا نداد
🔹
دولت آمریکا روادید سفر ایتمار بن گویر وزیر افراطی رژیم صهیونیستی به آمریکا را صادر نکرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/660018" target="_blank">📅 09:42 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
