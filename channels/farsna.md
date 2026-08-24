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
<img src="https://cdn4.telesco.pe/file/n_f7BTl6uWhr2O8BBWoCIqkt-IHiqMJfOlZzQw0hA_SnLhzZQTQ5O6SdmZwghuLe0a3bpf6ejfgZm7Mo_bztLTqKLTAGagGEwtnfTW2GJba57meAilGt3bu_gmTeiFpIRu5W8mXxHUeGf6Zwd0dWYTOWMLWJ5KlCnSif-xiWuGKUVJ3f0cfXiePBA_IqsHjmdmgRpYBtvHHevK_UdpCnaigbfW2oJunKA0D7C_9d52IWqM3AOf84c5Dh_MtWZn2QJhYeRUYwHkUqcqlH2IR18fbdO5R5Ah1xBUWC9STKlJ1l_Hm3KPGPG3xq_I9V28QYQfjc3QazJzrF6QooF956lQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 19:34:25</div>
<hr>

<div class="tg-post" id="msg-457993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21f2ed615.mp4?token=h6KB4HimAbnLVrNp80OFeuyMHILNgVjme45GBAIvM4NI9Dh_f8tdM8t5ZhFJlDu3WME4jhnoYFzt5H5fkwMNF9p1B9TVnct3Z_QkE2Zl_4oSFM0hlahl5sJ5B16peOu_LaDlo233j6bwa7GsWUchJ60RBFShLE03VwYeI7DdCsHkeeUG58bAOsxpWqwTGxuMfvzpi1GX2mjp_gHFyTbCIWsT3MvUP0rMkQl3cH-zZvujaCn15I0nazoKlAgBECSyRt4smNK4R4DUOfbfEhLI-JUmE-yVOpVyp7TkWbbSwcMQ_U-HFuJ2xnAYQdJPa6fHXCJhYctS7JHBRGk87GLFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21f2ed615.mp4?token=h6KB4HimAbnLVrNp80OFeuyMHILNgVjme45GBAIvM4NI9Dh_f8tdM8t5ZhFJlDu3WME4jhnoYFzt5H5fkwMNF9p1B9TVnct3Z_QkE2Zl_4oSFM0hlahl5sJ5B16peOu_LaDlo233j6bwa7GsWUchJ60RBFShLE03VwYeI7DdCsHkeeUG58bAOsxpWqwTGxuMfvzpi1GX2mjp_gHFyTbCIWsT3MvUP0rMkQl3cH-zZvujaCn15I0nazoKlAgBECSyRt4smNK4R4DUOfbfEhLI-JUmE-yVOpVyp7TkWbbSwcMQ_U-HFuJ2xnAYQdJPa6fHXCJhYctS7JHBRGk87GLFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتند قبل از رفتن به اینجا اشهدتان را بخوانید  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/457993" target="_blank">📅 19:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRRXq88W6VfI2YBQgOQ_zhDt05SWaErZGfv4yLinR0v-W54ou89TLkg7W-6EVW2Dlgbvah_6MbNClBu9_TWVQzUy1GCxmZ3ua8DoJbHyW2IlsgJn7UAKG7lftUgboOtezObZe-cD3l6NvHWTIScfRROwlRt-upBZevA62ggCy0pL611-g5qlyYGnQZb5qMzNz8dZZSKgIhnQZX3ot8yqd8yCxfT3ZRbNCoyLypG8J40R5bGxeCTqHSxVGXnEzlaDjicTmTmbn1bVq70euO1H2lgsjSMDAsAUqMHO3Wyje1UYk40dWFb3tiiH7acbiKkg-F4zFUcD0MQ4IEy8bNNgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/457992" target="_blank">📅 19:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با قالیباف
@Farsna</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/457990" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjCCkBauihlKtcPONBRXlastedTtgeu8sP6y23lCXQ_g1V456QCU0w4oSIuX-U37oZkq7NDdRp_4lF8uSbI5_8HLMHRbZ_a6PyNbMytASqj2_8NApXoKUK_nuWLfLWPC7KiiHyLq2ZkCKQojtEHlnOH6vM9Bgz4H9Xv6EMWS7AwrOa-DKseP01F9dDp56f_6-l0w6lFYXHKyNQlZQTCG0aB4HM9DRWmBes009yuE0P2s6nopon1PgzWjolTx1TOvBQ6tJvw7C0i067waa2fFTWGB_e6FrVwswhlSzlXTzv-g0vHTs-6TuEhcOjhBi1c2xzBjrdB_JMDGyZ_0LdTPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقلای ترامپ برای ازسرگیری مذاکرات با ایران
🔹
شبکه خبری الجزیره به نقل از یک منبع آگاه خبر داد رئیس‌جمهور آمریکا دونالد ترامپ هفته گذشته با فرمانده ارتش پاکستان، عاصم منیر، به صورت تلفنی گفتگو کرده است.
🔸
به گفته این منبع، ترامپ در این تماس، درباره پرونده ایران گفتگو کرد و از او خواست تا از نفوذ پاکستان برای از سرگیری مذاکرات استفاده کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/457988" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8987415951.mp4?token=n8vGb-njPUK8NMq6kfV-FtJkda97qZRfA2x-4c-3JZhsL0kshIkcRFXHmW5CjlPqe0KqMZ-F6jhAIRjPnAv5FTsAc-GcfEW7c7s-RxJOlTxH9qrIgkHAsp_P_hrLa2WXP3FzPlHHLiwgTCXEsgXq-9MOt2VSAgFpy6oEWYgtsb5ohg7JW8VzQG4B5XgS-w3sLZn8g2wpdb6tZ7vk0QMzsRCmeEtfpMGnOme6u68aFmwT1UQ2hb1lxszyFHSjKJtmp74PPSnWd8qZCoWllHrg7puZr2zcgh38LaNSrtn8X7HCdILtHjMNJyNbovQkiVZu4Rcpig7a2tMdjgpx5nA81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8987415951.mp4?token=n8vGb-njPUK8NMq6kfV-FtJkda97qZRfA2x-4c-3JZhsL0kshIkcRFXHmW5CjlPqe0KqMZ-F6jhAIRjPnAv5FTsAc-GcfEW7c7s-RxJOlTxH9qrIgkHAsp_P_hrLa2WXP3FzPlHHLiwgTCXEsgXq-9MOt2VSAgFpy6oEWYgtsb5ohg7JW8VzQG4B5XgS-w3sLZn8g2wpdb6tZ7vk0QMzsRCmeEtfpMGnOme6u68aFmwT1UQ2hb1lxszyFHSjKJtmp74PPSnWd8qZCoWllHrg7puZr2zcgh38LaNSrtn8X7HCdILtHjMNJyNbovQkiVZu4Rcpig7a2tMdjgpx5nA81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کار مرا به گردش چشمی تمام کن...
🔸
نماهایی خاص و متفاوت از حرم مطهر رضوی و حضور عاشقان «آقای شهید ایران» در جوار مزار نورانی ایشان
@Farsna</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/457987" target="_blank">📅 19:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457986">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd_jubxKwkPbmd81sgk2D74s0yJj7m4V587TS6uUupFEFFaZKvR3uFQYCAXrcJxQtBjKlFvQ0gEp_dVPYaYzx4cwR5N3UQ66RQeG9bDWxm28NwQbttR5Uv5b_7t1W5LE5U-55ABj8_poXjHB4we43gkoFoHlqIMm37n0aICFQa9g4XtlfdnwDC-Oq8vVSsHYfTYT55tEYm6x4Qov10coTg0A5hS_FQAlkpJ9QWYDTIXpDxhoLN8MgZa-DaG-8s3KE3gE5OU66Uuikhfh-4x4ZiomLYP2aDNg-ObxUzhotFV_dpdykpLzIBbXYFl9LJuZ_L0IwxbRdIWeDp6wJaCPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: پاسخ ایران قاطع‌تر از گذشته خواهد بود
🔹
۴۷ سال راهبرد خصمانه شامل تحریم، جنگ و توطئه برای تجزیه ایران، نه‌تنها به نتیجه نرسید، بلکه امروز با انسجام ملی و بازدارندگی جمهوری اسلامی در تنگه هرمز مواجه شده‌اید.
🔹
این شکست راهبردی، هشداری قطعی برای تداوم محاسبات غلط شماست. پاسخ ایران قاطع‌تر از گذشته خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/457986" target="_blank">📅 19:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457985">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVLdnL6UUGfEA6lqAnNJ_9GIC7LT2ciewzMqA_3U3MfNFUIiBOzKGgk2dUE7uT3r3ffFDsymaLnEoiHVB3QXOJT_p1-slRZkCXXZF1pVoL8ndV7kb8y0YxlzUqZ7aY0gfwAXZ6rEzSJuPSfkF7vzqEmKluWxE_DOysubG1DyPto24kgtV3LHwIYINxF7KYlTstG-JLFcvpzB_HgeL6-5pn6f_HGE2qVviTEnojz8DOYWmWampkbJFdDrHSswVxw7uKpaJOf1SeWhpLM-RbQJmeEPZnTwX9RW0viurT1fZiZ6vzIb01HBBc5_2EKdTX--kTuXskMs_5ojhToYElKHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا آمریکا را به قطع صادرات برق تهدید کرد
🔹
کانادا تهدید کرده است که در صورت تشدید جنگ تجاری بین کانادا و ایالات متحده صادرات تمامی برق و مواد معدنی حیاتی خود از جمله نیکل با عیار بالا و اورانیوم به آمریکا را قطع خواهد کرد.
🔹
داگ فورد، نخست‌وزیر استان انتاریو، گفت: « شما حتی یک دانه شن از انتاریو نخواهید گرفت» و افزود: «آن‌ها بدون نیکل با عیار بالا چه خواهند کرد؟»
🔹
داگ فورد همچنین اعلام کرد که «همه چیز روی میز است»، از جمله تأمین برق ۱.۵ میلیون خانه آمریکایی و همچنین مواد معدنی حیاتی مانند نیکل و اورانیوم با عیار بالا.
🔸
این اظهارات پس از آن مطرح شد که ترامپ از اعمال تعرفه‌های جدید ۵۰ درصدی بر خودروها، قطعات خودرو و فولاد کانادا از سال آینده، و همچنین تعرفه‌های ۵۰ درصدی بر ارزش ۲۰ میلیارد دلار از کالاهای کانادایی از روز شنبه خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/457985" target="_blank">📅 19:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457984">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIc9loS3JhVO5sqffaCjs_aMQo9zwhlGX3TwYuaFbrhSXLChN85HtpgekXs0x2X2-6yoqluArA3sBG3lAxq6gldSLcRt8N4IH4MOxKxFcaf2Ml0ew6td11wQ7rA0AjYAmHcOE8QY_6xqnzl2J1Lv4GxvRo7XR5JS_cDTrPUMFM1nzBOnxVtk7x7jyihuIxqR_oXurVEkSof1i13_nhRehDO41th0ZEXwY5c6NA9KHHltQSPStY3YlDwo_Gi4SrqqtUibcSW6LZwFh4KuYNjcyGhv_3K_borwLMIQItXxkZgR4dVMEsZPjrmQXNx8P4oFXpIJVi3Xmf4j1o-v9etltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: طرح مقابله با نفوذ بیگانگان به فعالیت علمی ضربه می‌زند
🔹
معاون اول رئیس‌جمهور: تصویب این طرح برای فعالیت علمی کشور زیان‌بار است و می‌تواند استادان را نسبت به تعامل با دانشگاه‌های معتبر جهان نگران کند.
🔹
فکر و ذهن استاد و دانشمند باید بر پژوهش متمرکز…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/457984" target="_blank">📅 18:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457983">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5baa8d43fa.mp4?token=sDGSxsSRzV8F2QtEApToUpycJA0qyy7u53KbCexLrxmiQKux01VSPM1QNS_QzCHNeW7F7PgfM9qPVnZt87aPY0HFOCYR8KhCEHNriV61ZMqzBVDwdJOWKaFKE9wGOBmi3wR-Ej5P_YzQd9hm-FasiT8wNUlLQ94SVQvZVtKkjbSQMP3XtMsuLLBUuzljV1lN0TbYDNwaq6Mnjgll7SvCvwy94WxoKU0nTLZYoKex9I2PnspTwegdsx8d4lsJhtJo0gggUH8Dn5HF0SEpxj1QW2calxYn8YRnXDdGu11Z0yeb-97jHO9Rnagk4kq2fXMahuyQsGroDUKj4-VX3XP-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5baa8d43fa.mp4?token=sDGSxsSRzV8F2QtEApToUpycJA0qyy7u53KbCexLrxmiQKux01VSPM1QNS_QzCHNeW7F7PgfM9qPVnZt87aPY0HFOCYR8KhCEHNriV61ZMqzBVDwdJOWKaFKE9wGOBmi3wR-Ej5P_YzQd9hm-FasiT8wNUlLQ94SVQvZVtKkjbSQMP3XtMsuLLBUuzljV1lN0TbYDNwaq6Mnjgll7SvCvwy94WxoKU0nTLZYoKex9I2PnspTwegdsx8d4lsJhtJo0gggUH8Dn5HF0SEpxj1QW2calxYn8YRnXDdGu11Z0yeb-97jHO9Rnagk4kq2fXMahuyQsGroDUKj4-VX3XP-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویلاهای ریاست‌جمهوری در قشم فروخته می‌شود
🔹
دبیر شورای‌عالی مناطق آزاد: ۲۸۰ میلیون یورو برای تکمیل پل خلیج‌فارس قشم نیاز است. این پل از طریق تهاتر نفتی توسط پیمانکار ایرانی ساخته می‌شود. پل خلیج‌فارس، قشم را به بندرعباس وصل می‌کند.
🔹
ویلاهای منتسب به نهاد…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/457983" target="_blank">📅 18:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457982">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGiYrKZ9uVyBHYkiq1KxmrP1oqv5-_zZAWCdq5ZkgzI8O46FeeE_kmkVZKG993voerHfk0zQ3vdUhIq51pr0QPFKeIeJ9UDoBIYtBPNcCwglXUUP_XU4TVhaU9B6ZPnLuP3MZmvlxmueuQH7iV_ko2-d0iP48KB_R37BWDN6iUdhLeAZGe0PLttVta0DhJA01zZTu_vUwCZKhr-svV-S_eBy7wHePj7ZAO3DHQVaZ_wlCcMWS77VL7P0bVp-eiI2nP1yYQKfmQ0zbbjuI7SuW_OkuW3k3t7vTxHsEJsBu1hIsiIqhXlexEw2OX_LyTdaGGJiJVji7AV4pMFgGUSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ دولت با «طرح مقابله با نفوذ» مخالفت کرد
🔹
هیئت وزیران با گزارش کمیسیون امنیت ملی مجلس دربارۀ طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه» مخالفت کرد.
🔹
دولت دلیل این مخالفت را ایرادات جدی طرح، از جمله ایجاد محدودیت‌های علمی، تشدید…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/457982" target="_blank">📅 18:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457981">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYG_V6RBGxR4bSs8ZAIrRhOPft1PiR3wLM_6Kr6IWd7MheUtLtsTITbK4AX-kzzgbb0uCm8-YzVbv2vnmlniU8F_IJqLttx_xtmTXilby-tJYLBjID8imoN88WQwP4KF3VB5R4N1c5MPaKu4ZXGuqkKlTvcjkAnY_-lnRz3KW_Y_v1EjBsUB4iBkDO9MdPXrbD3g9uO8_hTAAXR6AyEr7DlMqohQUk6a8MMEnkV2NEesDEkO3ssDrtrydWnoSvlq74J_WPpzgehFR_QVogNgSPW9EtEUPwJLUoNN2j0YpP7wVyaHct5C-7_dv5ys6H_YnRoulDE2J1ePyUeIxyK4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوچ تجار ایرانی از امارات به چین
🔹
شریعتی، عضو اتاق بازرگانی تهران: ۸۰ درصد تجار در امارات تجار واقعی و ۲۰ درصد تجار با شرکت‌های کاغذی صوری بودند که از اختلاف نرخ ارز سود می‌کردند.
🔹
همهٔ تجار غیرواقعی که از امارات رفته‌اند. تجار واقعی مثل ما هم به چین که «شریک اول تجاری ایران» است، رفتیم.
🔹
تا پیش از جنگ فقط ۱۰ درصد تجارت ایران با امارات، مربوط به این کشور بوده و ۹۰ درصد مابقی تولیدات، مرتبط با کشورهای دیگر است که امارات مبادلات مالی آن را پوشش می‌داد.
🔸
حالا بعد از جنگ ایران بخش اعظمی از واردات به مسیر شمال، مرزهای زمینی و ریلی شرق کشور منتقل شده و ایران به صورت مداوم زیرساخت‌های این مسیرها را افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/457981" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457980">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOoD5-plpPkBtulSr-7jI5Xj67QAm9tKDlCIh9QyavwYH7G9achHUsFpWLWJj3L0EZWXYbCrB-heeJM06hg282h7pw6cROtzOhRidqQjWc3633EP4MqJVCQo-uY7xuBc82SzLyYgJco_4Ypr-c3ywAyGW-105cD62_RB4cSiKptNm1JhPBoqeywyizmTyqIywZLU2PS4meY3zPoIsfWue4n-XMDwT5NC3qYk-6FP7CCslrhDpWcbPEwe1QA5urhr8AWtSOTzg0NrSScc5VNJHr6vX7GOkQJR3ncvfbEssFBiuFcOXkwlEOvaeKJum257XsyTvXrzgZem-QToI1pWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: برخلاف تصور دشمن تولید موشک‌های هوشمند و هدایت‌پذیر ما استمرار دارد
🔹
سردار محبی: دشمن در این جنگ به دنبال ایجاد اثر ادراکی در جامعه بود، آمریکایی‌ها با هدف قراردادن نقاط کم‌اهمیت و برخی چهره‌های ارشد نظام، به دنبال القای ناکارآمدی ساختار سیاسی و نظامی ایران بودند. اما واقعیت میدانی نشان داد که با حذف یا تهدید افراد، خللی در ارکان اداره کشور ایجاد نمی‌شود؛ چرا که نظام اسلامی بر پایه پیوندهای عمیق میان مردم و حاکمیت استوار است، نه بر فرد.
🔹
دشمن با هدف قراردادن پایگاه‌های بسیج و پست‌های بازرسی، گمان می‌کرد امنیت خیابان‌ها فرو می‌پاشد، اما حضور مقتدرانه نیروهای فراجا و بسیجیان در عرصه‌های عمومی، این سناریو را بلافاصله خنثی کرد.
🔹
با این حال، دشمن در محاسبات خود یک متغیر حیاتی را نادیده گرفت؛ همبستگی ملی و ایمان مردم، مولفه‌ای است که هیچ هوش مصنوعی و ابررایانه‌ای قادر به محاسبه آن نیست.
🔹
ما نیز در مقابل، فناورانه جنگیدیم و با هدف قرار دادن اجزای شبکه عملیاتی و اطلاعاتی دشمن، چشم و مغز عملیاتی آن‌ها را از کار انداختیم.
🔹
برخلاف تصور دشمن که ذخایر تسلیحاتی ایران را محدود می‌پنداشت، تولید موشک‌های هوشمند و هدایت‌پذیر ما استمرار دارد. مهم‌ترین دستاورد این جنگ، انتقال آسیب‌پذیری به زیرساخت‌های حیاتی و مراکز وابسته به دشمن بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/457980" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457979">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj5zPOapjQHZSgWPQ7F2vfibCNCSu5GKUMmukZ1U9L-7ghcPTlWHk85hAF6o9DU8OYun0fxwzvdsATLJGOyd_bgX64Q06K5laMEwsVTt8Zy7c4tiymQ-so8CwgksiIJzLZdfFGp9PNOWAQMaO1azzPh6e1Pi6HzspJ-yts3ldpt7QN8ccAUxd8196j7D9O1TQghdsUGkCGaYhLduf5cwCa6b-f7b_PJ-cGGNwT4mNXUQPSZps1IDeva506i24mpcDreep1lXzpLwgMNK0qTijxbVi3SQdU1t14vDW6NqqTNplZA-ALo_J0bG7D7P6hDX031wm2sjXuA4xdW6ueIbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰۰ هزار میلیارد تومان پول مالیات در جیب دولت
🔹
آمارهای رسیده به خبرنگار فارس از سازمان امور مالیاتی نشان می‌دهد در ۵ ماهه ابتدای امسال ۸۰۰ هزار میلیارد تومان درآمد مالیاتی وصول شده است.
🔹
این در حالی است که سازمان امور مالیاتی در ۵ ماه اول سال گذشته ۵۱۲ هزار میلیارد تومان درآمد وصول کرده بود. این یعنی درآمدهای مالیاتی ۵۶ درصد رشد داشته است.
🔸
در ۴ ماهه ابتدای امسال درآمد نفتی پیش‌بینی شده در بودجه هم تحقق ۹۹ درصدی داشته است. نفت و مالیات دو منبع اصلی درآمد دولت هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/457979" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457978">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b2c1deee.mp4?token=hQhAlslL6FUHyBG3WuyaRbS_IjBlshTm_7W8tg28B8eULb1OWYtUqHu9QLCdedFZy6coreWSBl8_xwfSs6CbA8flw8Wo3H0h5L3Yor1UBRqzXS3rz4k-5DkiZZSNVylP5dQqKBKITzpNK6uZPsL8CtkHqIDEsdhegOND1-Z1MHxUj6pm5UfvVCt2yYwiJtgPr7Qr9mzNPykgdG7hp_YVUpDg8-H_-8un34MHcVDGgAKdl-OQ1VX1M41dNNH3ELlAyoVp1v4F9XQrDrWbTjS1dSK8SJO6ByzfpWohCWE94yNw0E3H4ivGKG8Fcbc-YGz3v1VTa2V0FwobyBJYkILhqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b2c1deee.mp4?token=hQhAlslL6FUHyBG3WuyaRbS_IjBlshTm_7W8tg28B8eULb1OWYtUqHu9QLCdedFZy6coreWSBl8_xwfSs6CbA8flw8Wo3H0h5L3Yor1UBRqzXS3rz4k-5DkiZZSNVylP5dQqKBKITzpNK6uZPsL8CtkHqIDEsdhegOND1-Z1MHxUj6pm5UfvVCt2yYwiJtgPr7Qr9mzNPykgdG7hp_YVUpDg8-H_-8un34MHcVDGgAKdl-OQ1VX1M41dNNH3ELlAyoVp1v4F9XQrDrWbTjS1dSK8SJO6ByzfpWohCWE94yNw0E3H4ivGKG8Fcbc-YGz3v1VTa2V0FwobyBJYkILhqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ هوایی اسرائیل به جنوب لبنان
🔹
خبرنگار الجزیره: جنگنده‌های اسرائیلی ۲ حملهٔ هوایی به شهرک المنصوری و مناطق اطراف آن در شهرستان صور، واقع در جنوب لبنان، انجام دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/457978" target="_blank">📅 18:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee6df3ac2.mp4?token=THG5ZP1Ogk2Gd-ov6l2iNsMz95z4DqucovSHeXBDkk4tonptUl09oNhBudwmM0KwTDi6K6KWg3r577b6_wLLhv5ZcipA_R7JQ_JFNzPKGeX2nKURZW7lh3skJT8Fk6WIWQndOwKaawN6X906wPdKQiYrfGYcG6mCtYFZ2alFdtVO5-OEXXJ1pmHOBYIbrTX4k_ytLHT6-E3Yu6h5rltbkeaoTIrC2L-d0rBNTGqGEQWiptVWDJVsqCETE_x5EG0whxw0QSqgB7omxDTzkKEDrlrovXrC-_Y7Y6CVGYJW_YcVdiR01zpTxVm7Wr7UMRt18eO5U0dbQROa6XNNJdj1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee6df3ac2.mp4?token=THG5ZP1Ogk2Gd-ov6l2iNsMz95z4DqucovSHeXBDkk4tonptUl09oNhBudwmM0KwTDi6K6KWg3r577b6_wLLhv5ZcipA_R7JQ_JFNzPKGeX2nKURZW7lh3skJT8Fk6WIWQndOwKaawN6X906wPdKQiYrfGYcG6mCtYFZ2alFdtVO5-OEXXJ1pmHOBYIbrTX4k_ytLHT6-E3Yu6h5rltbkeaoTIrC2L-d0rBNTGqGEQWiptVWDJVsqCETE_x5EG0whxw0QSqgB7omxDTzkKEDrlrovXrC-_Y7Y6CVGYJW_YcVdiR01zpTxVm7Wr7UMRt18eO5U0dbQROa6XNNJdj1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروسازان چطور بنزین‌ را می‌بلعند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/457976" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ حملۀ موشکی یمن به تجمع نیروهای سعودی
🔹
نیروهای مسلح یمن: در حمله به تجمع نیروهای سعودی و یک کاروان حامل تجهیزات نظامی، بیش از ۱۰ کامیون حامل سلاح که از خاک عربستان وارد یمن شده بود، هدف قرار گرفته و منهدم شده است.
🔹
همچنین چند تجمع نیروهای سعودی در منطقه…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/457975" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌  یمن: یک کشتی سعودی را با موشک بالستیک هدف قرار دادیم
🔹
نیروهای مسلح یمن: نفتکش امزان متعلق به دشمن سعودی در نزدیکی بندر ینبع با موشک بالستیک هدف قرار گرفت که منجر به آتش‌سوزی در کشتی و فرار تعدادی از کشتی‌های دیگر حاضر در منطقه شد.
🔹
این عملیات در چارچوب…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/457974" target="_blank">📅 17:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یمن: مانع عبور ۴۸ کشتی شدیم و ۸ نفتکش را هدف قرار دادیم
🔹
سخنگوی دولت یمن: نیروهای مسلح یمن از ۲۰ ژوئیه گذشته تاکنون، موفق شده‌اند چندین معادله جدید را در برابر عربستان تحمیل کنند.
🔹
نیروهای مسلح یمن توانسته‌اند معادلهٔ «محاصره در برابر محاصره»، معادلهٔ «حفاظت…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/457973" target="_blank">📅 17:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70cfdea7b6.mp4?token=HJlRZqFuyUIk8Y0BXu9QmQFccFymCdCy9vdB9XvwVg3powyf9HPvsI7QGw-CrO6Zv9VDfPV74EPIO5dsLnU1jiVXJ6HwpySeqrzuYJqNVcWiiP2lExZoFQiX4DlzvmHf-R99o6xRY7fR5POh5YNF44lLhaXrdY98Q2Z1XC2hyS0k71-awMTVZfKbu9j4Pk_Sr45EdZuzGDvRnehtlcx-qfdqWOkHBrU27b66Z0QxSWZQLABu9pEptFeIRBlY34PkU_hZVVcdk0QT1qyqc9hZJLMFM8vQ85DV4-nZTVAJz6zVZ_FMzChD3I_VNyM5x6ns18bhX7iIlGDqNXij5LkFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70cfdea7b6.mp4?token=HJlRZqFuyUIk8Y0BXu9QmQFccFymCdCy9vdB9XvwVg3powyf9HPvsI7QGw-CrO6Zv9VDfPV74EPIO5dsLnU1jiVXJ6HwpySeqrzuYJqNVcWiiP2lExZoFQiX4DlzvmHf-R99o6xRY7fR5POh5YNF44lLhaXrdY98Q2Z1XC2hyS0k71-awMTVZfKbu9j4Pk_Sr45EdZuzGDvRnehtlcx-qfdqWOkHBrU27b66Z0QxSWZQLABu9pEptFeIRBlY34PkU_hZVVcdk0QT1qyqc9hZJLMFM8vQ85DV4-nZTVAJz6zVZ_FMzChD3I_VNyM5x6ns18bhX7iIlGDqNXij5LkFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درپی حملات انصارالله یمن انبارهای تسلیحاتی سعودی در گذرگاه «الودیعه» به آتش کشیده شد
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/457972" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520e8ee19a.mp4?token=RxO89XJzD14hKVIyynUZDAEbygMLHFfVE1kVW3Hb1r8hIkD0z6-QgynGHbJR-2lZUOaC_1YeAo0dyZneZ5POT61UwJ_ga2k1U1loyNqqC-Z75XI3NvDLW8RX2OM22vgyIvzES4tVNf2MA7yo4_lb5MmpHT-hrvYLzpPVSuxgBv_eOV3q8ViQ88PJURhzFOxaHfGPcnOwgVIiWCPN5TwiUmeioWUzMX3JWv9GXwLXFqRs9_kwnuL50zdwFmRanIT-t9Aw6ycIUCHRByVzGKCK8Q85F-MrsAMmH7o_7OVeN2ZTuSe9k9qhq1aDmDA5SCUNN5DPJYW325586ibrMCBv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520e8ee19a.mp4?token=RxO89XJzD14hKVIyynUZDAEbygMLHFfVE1kVW3Hb1r8hIkD0z6-QgynGHbJR-2lZUOaC_1YeAo0dyZneZ5POT61UwJ_ga2k1U1loyNqqC-Z75XI3NvDLW8RX2OM22vgyIvzES4tVNf2MA7yo4_lb5MmpHT-hrvYLzpPVSuxgBv_eOV3q8ViQ88PJURhzFOxaHfGPcnOwgVIiWCPN5TwiUmeioWUzMX3JWv9GXwLXFqRs9_kwnuL50zdwFmRanIT-t9Aw6ycIUCHRByVzGKCK8Q85F-MrsAMmH7o_7OVeN2ZTuSe9k9qhq1aDmDA5SCUNN5DPJYW325586ibrMCBv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: مسئولان نظام برای احقاق منافع کشور هیچ اختلافی ندارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/457971" target="_blank">📅 17:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457970">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r02ANR8hfSNJAIvTUCWxhi_JyboSC9Rae9Jok6DTtD2oi_MTddAZII7IpovWt5gwMhzU8_XmjhzWv59ppDkhg7pI-NHQu_I9vXHGa5BIMgYXR7vcC2c1XGoicBQ7DdMDDwknszULc0iyV89qAQK-tZm1zmyNIiCODUOe0TG65402-39ymilgAt1-QvzBNoOSTL5JYb5i6ITMVS2ga1F9awLpJU7cOkyfoXN98j_kG7Y5LLk-BstvcqgVjE9_CY9SJCBnF37m8WnpPEq5q3XiGNpP3xDv6EyqI1Ko7jVkFWY2QmgIb0b9ZKlSI-sDco6J2O6tD9SFgOl_D4pYG_vimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی وارد بازی ساخت «مغز» گوشی شد
🔹
رویترز: شیائومی با توسعهٔ تراشه‌های اختصاصی Xring O1 قدم جدی‌تری برای کاهش وابستگی به تراشه‌سازانی مانند کوالکام و مدیاتک برداشته است.
🔹
این شرکت حالا تلاش می‌کند بخش مهمی از فناوری محصولاتش را خودش طراحی کند و تولید تراشه‌های پیشرفته را به تی‌اس‌ام‌سی بسپارد.
🔹
شیائومی برای تولید تراشه‌های جدید خانواده Xring با تی‌اس‌ام‌سی همکاری کرده است.
🔹
این همکاری نشان می‌دهد هدف شیائومی صرفاً ساخت یک تراشهٔ اختصاصی نیست؛ بلکه این شرکت می‌خواهد کنترل بیشتری بر قلب سخت‌افزاری گوشی‌ها و دیگر محصولاتش داشته باشد.
🔹
تراشهٔ Xring O1 اولین گام مهم شیائومی در این مسیر بود و این شرکت اکنون توسعهٔ نسل‌های بعدی تراشه‌های اختصاصی خود را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/457970" target="_blank">📅 17:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457969">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtJ_H3N6rpe3RYyd8nC_LCftF9Dk4voh9Md65Ufpec5t9EB2xOm-Enh8Lx8HovhGbZfM9Bfjg4MYxidRKoREpweNMBStanKsW2-E5JUtZdOpuXOtmmUtpfdzKQvVvmvlOdEKqtS07nfuIY4DI-SZwKEVJHPJ16ik3ojgfZJcAHYvQNAx2noSFVkseBN-Ugm8V5-rx4PLEreW9ecXabcwJq_9VH3GujP_nylpg7uu3pbnFi2g3vZKgANII8BOfkahuT9qKERS1R5P7fPjh9uwSqZt-HhiF88H4_Jbr1A9AArMI4RpSYVYdUQeFZvgrG6a9QHwiTY4p1VaP1ag4fN1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور چین خواستار تشکیل کشور مستقل فلسطین شد
🔹
رئیس‌جمهور چین، در دیدار امروز با پادشاه اردن ملک عبدالله در پکن تاکید کرد که مسئله فلسطین یک مسئله محوری برای خاورمیانه است.
🔹
شی جین‌پینگ،در این دیدار خواستار «راه‌حل سیاسی، ازسرگیری مذاکرات صلح بین فلسطینی‌ها و اسرائیل و تحقق هرچه سریع‌تر تشکیل کشور مستقل فلسطین» شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/457969" target="_blank">📅 17:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1816d0d414.mp4?token=IpulSI9UnQOeNJF3Y8AneTw7H7Ehd_S8fHuxbkINrFJQTZ8iz9SyHLQ8UJ9TWjP201r19WyJZ6q-ER10eSbqsvhZQwyy8Jz7Ee98V43NR5LJ97F4wKosORqrurzDu46E73IB0dTQFJJ33G095d0_iJsaBPP0LapxUsfBchwxuSZF8MZQSyJPxP7c1X5uXq0Pv2IFN_HdouQqJR1mn-lnBmBiC50PNdsT4wyOOe7IKBtu2gF7IV77q0S3rPeHhAbWa-dELziu6YeINELsQtOfk2bTrv82iFu9lwPz-fuU_zWlO9bqeiLybF6EAFY5fxqy6qe5_xX5Up8_vOSuWZrDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1816d0d414.mp4?token=IpulSI9UnQOeNJF3Y8AneTw7H7Ehd_S8fHuxbkINrFJQTZ8iz9SyHLQ8UJ9TWjP201r19WyJZ6q-ER10eSbqsvhZQwyy8Jz7Ee98V43NR5LJ97F4wKosORqrurzDu46E73IB0dTQFJJ33G095d0_iJsaBPP0LapxUsfBchwxuSZF8MZQSyJPxP7c1X5uXq0Pv2IFN_HdouQqJR1mn-lnBmBiC50PNdsT4wyOOe7IKBtu2gF7IV77q0S3rPeHhAbWa-dELziu6YeINELsQtOfk2bTrv82iFu9lwPz-fuU_zWlO9bqeiLybF6EAFY5fxqy6qe5_xX5Up8_vOSuWZrDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام‌رضا(ع) برای میلاد پیامبر(ص) چراغانی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/457968" target="_blank">📅 16:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAQqa9hgVm3me4uCWDyv1Uku5PGYyTNDHUHu0Q1V3tWCmPWz_qFiz8SwfkQDe_NAozOt25BF7LQolOeNuetmwEr4qQU8g5C5bq_i1STILyEOCvh6VJ6oZkUTp9S1KUcjgwCbhbObR-uN5CslCC76z37pAGEAdeTBf5_p3gA4IncYHm_-Z1RsEqPJ8QMp-xpGH76RGSCEnF9PHMZCSQfVvS3TwEsr7TMpMwSzfhDlgwhNQi4l7YyQpN_oabVUEXcUpmNVDrUOJfz7LiocHDmN4rWcH-J7cD1zXjSx3ZfgvaHOhod287s2LpFrsStZOmGNfYlnvyXInbuFY51WmIvLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4L8MlhtboUyDo8zf8k1FIiCIUL3cVXuogTRJA4MDS93bYTb3jLltBjXw1or89joIKrdiUYwXi60mqduOQ_cnylr8n_gujM9zmOLCrof9qB6HAq4uyVOX06m5-bPoD6RPij36-hWvWaBhHn_FQL3QPIj_b1BTIUykBYuPh1Z0JzgJjq7qb_lIREv0sWRbt2KookzpeRXaNrh3WOweExhIGWrbVjb0Tl1IkY2qjywDDy554J4sd1XmGqTK-AtcxTS9fF7o4lr8Es__QKrW2lvqD_DdKspJDqiImhJGc1R6kId-RpfbVQ4lkFvs6YUjk84UIBPbzW3-Av4DvlIWaaLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRL5Y_r1IwS_bge-zfau3ZRBqluKhsZBFxD_IvLYw3GHx6mtDnlNXsvQ1ZC6ahxVzCNyl7hCe-V3XDdFayVzbxzpUX4vv9mePXN63cYdOufpRVNxFjSrMVhwQd2u1Yw2_lhlJQzHVSj4N9JXClWbj1Mxuly1j-7KEV8cQ_IpcdsxPNDHvnt2rFqptBeKXYKJJRPVOmhuGT4tRw4KghlCjBk2Ul5irQuDbC9XCCVZNzrEpro6eybKFMYEHVs_I5sDSPpdNZi_u4x_85JOvCa-TaHa2PZhZBxNfj2dCZfn0dJWes9zqTCUWT1CnaUFGhDA1Gplr9etu9EysZwGH8IYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDbTJriCScx4Nlkx40-zswxCUUQzCJXMimWcESloPN3NLSt4yxqHVV8NICEoxBNQgMljY-Xt0lAzsKtF5Dm99gfLhO3i409ogINKk1fUEEBbAMQ1B96-1FHGHw6_Ycrrl_kVdsdnTCok6HgT7-kMCYyq7oO5eCQSeh-q8Ifhru2aCPF_kjvNb226lVINzn3WTzaY0d53eLbS-aF2FV_pCDBZOZA6G1rPbX5dLG0Gt4_oCEPZGAxYhJZ2BY3_yhzFzkKbpYTW8vhkIYUfJ_i_Ud5hx5Nq4vJGxCpL2GscD7MBjsL-JoRjnNOLv5fPf9A8bXHQ9EN49hqFeyBxGPtVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0N7c4qWL6l3EnCGpxnV5RXBvJ83xhR2Z4TVkkUrk1GYqSrduK94ADE2QbihEbejF4jistp0P7CgryV9cPk7fUB7DWIaFqFr4Xwr7ZMxOAlF5KKEnRMaInITc8yQVreIDSk4S8e-TM2ddLPHgw9uPNnGxK-Wd9xcnt-U8xPtlckmc2FoMOMOblwkA_0l6oECETp_nd1f4_SMQCWMCSQOyFXblqN9JQqHZ-cxQFODcd7qzl69rWjgOXWzsWfGmsIcYqg35aMJxpP8ZLomplM_8XC5R4aNBspI8x_5v9qnHB0N1_CKGdRMNs4GcXk8tpvt7m0B5Q96BMWstp3BIU1SpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMC5TESIieftm5hIR9sGCb6bcvWBzZCOXsX8ovqfS89nCqMhL9ff2OEnH-8yWf3Fa-FyAqRxRY3uAUhjomXaLpS-qCcrwLzWuk2-1eAzVhqiFzny03lCoV4pciNlhFv5Hf2BjGYIGvwKi6Ll1awesFZ02_VJGr0ht86pCGavn2p404SB3NlBmm8PziDWSaqxqh0DBJfNkKQAkfweZCwyGpeOn9GtW-7T6x_87AxyRpXCCJGbee2_nPToBCyVij6KxjnihINwrHvLiYSVGPWeQAmbdmJr0D09znKajFDQDatE8OPDdEpt05dVykcQVEjPjugdkP8Z6GqzfnhIIRgAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trXvNaE1tjYyAo4IyoIMVNXGJTVrPvGg7-7Ra6x4HpxjfrvdAV6A10Hfrr8rbEuCiieoKosliEzozzuGshI7CFHNkWsVwTGR_ShGt52JMfMI9TPzqTM7HJZE2JtlEXD4GXrACkowvVtydtxW-7d1CbEqvAwe_doPYYwH2-loisS7ZIfpBahM9XoQecQFwgYE9sDtDiPl6CwV7xPJ4sMfXkT_xmf2vkrk3RxgemEAOJZtzXT47IPsGgcojpb858oCdxJ27qq5JWvBcEWOnm6edFbA1wo5RZhTJ1V0tPksq_Cewu_mJaudexObXtbDtdgu1YxYLkHBaPJGbbvWhT-jig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز پزشک در ارتش
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/457960" target="_blank">📅 16:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش: آمادۀ کمک به دولت هستیم
🔹
بیانیۀ ارتش به‌مناسبت هفتۀ دولت: امسال در شرایطی هفتۀ دولت فرارسیده که ملت ایران در معرض آزمونی بزرگ و شرایطی متفاوت از گذشته قرار دارد.
🔹
شرایطی که اداره امور کشور، حفظ اتحاد و انسجام جامعه، تأمین نیازهای اساسی مردم و استمرار…</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/457959" target="_blank">📅 16:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBysBC5G9OLWx14o1RwEFcPENzvkaqMuolydbC18g1igL7gW0igS0gazIuuaqFCmtwOmli4VY3DjZHI3caGSekfjcey_ARPJGgFjfr-q_XDf2E8jOWkllHuMSb_dX0D0-YJkl3pGIbhK3ZlXsDaAxcpxbxNi8YqeRuiNOE1MxNJrzZPWyObXlsLx9lkFbD2QXAWLEjUCcKRtPTTIHrhZupaozWkaD1PuSCOQ3qI-xoDL0RRNZR1QENWumHFukfHMmFfr-X7fdDFb7H593CSC7PrQbMooKKj6mlr2OkiB9zsqYTs4C96XFhN6ZVnD9pzDCLt442thgV9cGoRYBETNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۴ هزار لیتر سوخت قاچاق در بندرعباس
🔹
دریابانی بندرعباس: درپی توقیف یک شناور در سواحل شهرستان، بیش‌از ۱۲ هزار لیتر گازوئیل قاچاق به‌ارزش ۲.۴ میلیارد تومان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/457958" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGg3pgkHuy8DvdyNoGw7SrwAKECj41Cx90Megawv3_yB1PRVglkUxYWx3UDNQVAL4AeJ-BuuJLQA-FbOnw0ky8-lIiwDQ7LUGAGMJv8f9FHLXSFdb3bRyQqa08aVGNQOvpBGNYuI0NXxEm04eNtIrUz87M8H2efZVDoFTNWozlLP8FR0stl-koOuuAlIZE_NdoFF19BDvBKvti6pE8p-5SQ-atJcq1yyb3Vf-67qyp67-5euP6t7GcLSrO9GHQ535t2UetslKvhE5sDi0YIT7mwx5YdmlYi7_gfDr1J5LBV8f6OIUJwFYrqm_TTz0tCSDkQZffcvV8LnfA_eT6ASjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدین: روش ما مشخص است؛ فوتبال شرافتمندانه
امیر سیدین، نماینده تام‌الاختیار مدیرعامل شرکت معدنی و صنعتی چادرملو در باشگاه، در آستانه دیدار چادرملو مقابل گل‌گهر، با تمجید از عملکرد بازیکنان و کادر فنی در فصل گذشته، بر تداوم مسیر موفقیت این تیم تأکید کرد.
سیدین با بیان اینکه چادرملو فصل گذشته شایستگی حضور در رقابت‌های آسیایی را در زمین فوتبال به دست آورده بود، گفت: «برای ما بازیکنان و کادر فنی چادرملو برنده‌اند» و مجموعه مدیریتی باشگاه با تمام توان از تیم و حقوق باشگاه و هواداران حمایت خواهد کرد.
وی همچنین تأکید کرد: «روش ما مشخص است؛ بازی شرافتمندانه و تلاش برای نتیجه گرفتن در زمین فوتبال.»
نماینده تام‌الاختیار مدیرعامل چادرملو ابراز امیدواری کرد این تیم با حفظ انگیزه و تمرکز فصل گذشته، بار دیگر شایستگی‌های خود را اثبات کرده و در پایان فصل مردم اردکان و استان یزد را خوشحال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/457957" target="_blank">📅 16:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cATB54xK-q3yEny7LJGwUFRU-ADEtFLjEBXxCdWHWSlruvFwG1qcItmLup_qgLZO6Pz-NSeZ0JGK-zgKv1DAjHHL8Nsy37zWvBEPmrbdVlNJujZ7zppPRU_SSPeWaMGTJiIgw6csBoZ1aavNKR4icUPK3d8yslPkkLb3r4hVx34Go7mATsMe_WdXK45f66jENRKGqjYjGea2D-LkolBXhhjUhZTQf7IPZb6Zcxv97TRnOdnxmAlu8K5YNK-q9UR5T6ZdRudFemfiFnfK_Spy8S_QYVCqLFYhbiLGY4K0NTKaqlsNwawz8SWMbgHwz6iPhG1aZdZXCeaP0e2q_2ja1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آخرین فرصت ثبت‌نام در دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه»
📝
فقط تا ۳ شهریور با تخفیف ویژه ثبت‌نام کنید:
📝
دوره حضوری با ۲۵٪ تخفیف
دوره آنلاین با ۱۵٪ تخفیف
۲۴ ساعت آموزش تخصصی، کاربردی و پروژه‌محور؛ ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات.
🔹
ظرفیت محدود است؛ فرصت را از دست ندهید.
🖼
مرکز آموزش‌های آزاد خبرگزاری فارس
ثبت‌نام دوره حضوری
ثبت‌نام دوره آنلاین</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/457956" target="_blank">📅 16:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/457955" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68ad7a978.mp4?token=NULk_hQOMRtC9JGQ2Fx37mS163gtgQd2jK1yJT9G70wmt8zjt09Wd3nJaPdr4IbsVDP_RMvotoSA1Mo2ppxR3l6hjL-2pq6SB2MGeH_y67cA4b_Fgigt_kk_1-iuZczAKAlyNCPli_5N64yQX-ZGzblZ1aoni36QJr2bkibsNkg51yJa8JDojzQQFZkZ5f4ocFWkGlXtf6u8trnLNaq2H3OZY3IMVaGIxFymLjzTXQPcEJqGx3lGzXpqsjedymUROSD2TzZK-SmKZUHmtjZHYqK2Re0fFU4FPzunjuKnVDOjy1TWHuPPF5VmDxhvpP-J68vysoGy8171daSKLHqdODLNmecbBxuQMoP1Y9Dbha7pDMu7igaM0L6rbaZRo39S-3VCf3LhX5tuey58KNcwksh68xax85HGQ8z2UeH3yQwcXUqhMWri1F9vAjGTyZu8TpDFakzmhR3rXzMueA4vgBh0FJeSAT4HeA7LpoJpXjp0i3vgK37ODPgE4mxgdukp9_OeG4_0lDDTZbHkWDNKSmowL6ZWAbSSypBhefyCc9PpYf8bVVTvrEfZiLrlYUZ-sY-8SMzKanlBV7r6hwV39UfXCL7Mxs84W28XY2krAZ17HrgLTJv1zC5RALlBimAUQ1H8JgUJwoLvPyK-i1xuexlM5sx6qDDKqJP-1uLUUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68ad7a978.mp4?token=NULk_hQOMRtC9JGQ2Fx37mS163gtgQd2jK1yJT9G70wmt8zjt09Wd3nJaPdr4IbsVDP_RMvotoSA1Mo2ppxR3l6hjL-2pq6SB2MGeH_y67cA4b_Fgigt_kk_1-iuZczAKAlyNCPli_5N64yQX-ZGzblZ1aoni36QJr2bkibsNkg51yJa8JDojzQQFZkZ5f4ocFWkGlXtf6u8trnLNaq2H3OZY3IMVaGIxFymLjzTXQPcEJqGx3lGzXpqsjedymUROSD2TzZK-SmKZUHmtjZHYqK2Re0fFU4FPzunjuKnVDOjy1TWHuPPF5VmDxhvpP-J68vysoGy8171daSKLHqdODLNmecbBxuQMoP1Y9Dbha7pDMu7igaM0L6rbaZRo39S-3VCf3LhX5tuey58KNcwksh68xax85HGQ8z2UeH3yQwcXUqhMWri1F9vAjGTyZu8TpDFakzmhR3rXzMueA4vgBh0FJeSAT4HeA7LpoJpXjp0i3vgK37ODPgE4mxgdukp9_OeG4_0lDDTZbHkWDNKSmowL6ZWAbSSypBhefyCc9PpYf8bVVTvrEfZiLrlYUZ-sY-8SMzKanlBV7r6hwV39UfXCL7Mxs84W28XY2krAZ17HrgLTJv1zC5RALlBimAUQ1H8JgUJwoLvPyK-i1xuexlM5sx6qDDKqJP-1uLUUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت، جواب گزافه‌گویی وزیر ترامپ را داد
🔹
صبح امروز وزیر خزانه‌داری آمریکا ایران را به تحریم سنگین تهدید کرد، حالا مدیرعامل شرکت ملی نفت ایران می‌گوید، هر اقدامی که انجام شود، برای آن راهکار پیدا خواهیم کرد و نگرانی نداریم.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/457954" target="_blank">📅 15:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457952">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc07824292.mp4?token=TX-NkMySSSsEyxJC2NtVbShvAWwd-RVOX3BBoOljEK3N7mQbpQC8m68ozFd_13x9krqFwYd_lKuOKH9ntbbhYs_M_LnqWCcyE-ilNeDQhw52_GlZcTjijQmPyQ90v7LhzT1-RH4xjF6VqKDKVQJV3kL8iU5epRd5dIZqpWC2fYrOvVZM5dW7wB6ZemLv7_3gJz-aGhzxCvISZunlEFxpoWMEvfjzwnstc_DyrxyIvxIrKl9p5RyYlC-1lxkcNfa9eXfLCrAqyshFN0TMppare2Vv9eUfXrO8jg3DLYQwX0bce77vKYg-YmQTGaYIgNnegP060oSdeepWFTiVQ8Yr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc07824292.mp4?token=TX-NkMySSSsEyxJC2NtVbShvAWwd-RVOX3BBoOljEK3N7mQbpQC8m68ozFd_13x9krqFwYd_lKuOKH9ntbbhYs_M_LnqWCcyE-ilNeDQhw52_GlZcTjijQmPyQ90v7LhzT1-RH4xjF6VqKDKVQJV3kL8iU5epRd5dIZqpWC2fYrOvVZM5dW7wB6ZemLv7_3gJz-aGhzxCvISZunlEFxpoWMEvfjzwnstc_DyrxyIvxIrKl9p5RyYlC-1lxkcNfa9eXfLCrAqyshFN0TMppare2Vv9eUfXrO8jg3DLYQwX0bce77vKYg-YmQTGaYIgNnegP060oSdeepWFTiVQ8Yr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردی که ۴۴ سال بی‌هیاهو به رهبر شهید خدمت کرد
🔹
حاج حسین ملکی، پدر شهید و چهره‌ای که اهالی روستای «وادقان» کاشان او را به «خادم رهبری» می‌شناسند.
🔹
او نه به‌دنبال میز بود و نه در پی دیده شدن؛ سربازِ بی‌ادعایِ ولایت که ۴ دهه عمرش را وقفِ خدمت به مردم کرد.
🔹
خادم رهبر شهید: ارزشمندترین هدیه‌ای که در تمام عمرم گرفتم، پیراهنِ رهبر شهید انقلاب بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/457952" target="_blank">📅 15:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457951">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILhIuy9w7Vh-IRjmLhJDTG7o-HBsj6kCjgeir8jHQ-UA9Nb1BW6fY2sMjZiMo2rc-bhdBVGZ2E5fD_dYcpWcJ1N2RdETUHq4CBzBI5KlCvye29aQfgS0-EI8u9jXB9ta46WKjK3IFww_u1z53USF6MJHusSArX8XYbClfdrBh3TBNmYMlqHA0tk57sLb0Gtu_7zBSxjEcr4iOMknrgqGvXLdwzBEP7lkqYudYsE0P-uSxNgyjSD8fjeLx0ZgDeX2JKa44qtuAa2xHa3T2WOEpQVI2hylH26hUPpIijl9shSzhfbjXF02sC9m5c5Q9h18T7i1luafFg193WTNhsozzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیکوپتر آپاچی آمریکایی مایه تمسخر ترامپ شد
🔹
در پی گزارش سرنگونی یک هلیکوپتر آپاچی آمریکایی در نزدیکی تنگه هرمز، کاربران خارجی یک سوال اساسی پرسیدند و آن این که هلیکوپتر آمریکایی هزاران کیلومتر دورتر از مرزهای آمریکا چه کار می کند؟
🔹
بسیاری از کاربران با…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/457951" target="_blank">📅 15:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457950">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5db2622c2.mp4?token=UX8KTXzSAfleroDLbQd2qifWri287-3yZLKUeuE1hg7Fklnq8qKasS_Z1vS5ZWipk1K8E64k96jD5RsXm13NJJVK1FDuPIEHmkouzc3PtorKE6k-7nEtYJefCD--Scw-7xryo9bJxMqzcBUngZPeqEkN1s-Vq0aQsxjWHL0DRsPTHldE2yhuBjESasYGMDtODDJECj1N-Yauiq6N1TqrKlcCepUB0r9uZXmVrWbnIdDKYA6FcT6mndsHLjcU0333V3g59-Ii_rwgjmntKHS7D8xUhDXIRTHZ8YxkxDwWa1_5CzWkmUPxRbUCSaS86vVXV62DaLrsISj_N5VnzJs7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5db2622c2.mp4?token=UX8KTXzSAfleroDLbQd2qifWri287-3yZLKUeuE1hg7Fklnq8qKasS_Z1vS5ZWipk1K8E64k96jD5RsXm13NJJVK1FDuPIEHmkouzc3PtorKE6k-7nEtYJefCD--Scw-7xryo9bJxMqzcBUngZPeqEkN1s-Vq0aQsxjWHL0DRsPTHldE2yhuBjESasYGMDtODDJECj1N-Yauiq6N1TqrKlcCepUB0r9uZXmVrWbnIdDKYA6FcT6mndsHLjcU0333V3g59-Ii_rwgjmntKHS7D8xUhDXIRTHZ8YxkxDwWa1_5CzWkmUPxRbUCSaS86vVXV62DaLrsISj_N5VnzJs7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژهٔ فولادسازی شادگان خوزستان رسما افتتاح شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/457950" target="_blank">📅 15:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457949">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBA2VN6q9EUvNuPhRRrcYauIcIbXp8fJ7T4miaQTpMF5Sxi0DH2jRfq1DV_mSYwoehCxwFfNpsVze7zk8vrZxPlbiMZDBJ3G3WjUJha_NXQ-w6js57bqMOsB670of2G1jk8iChheihADgrEdWWDtsFGWSGCSpeyOvzg4V4dz5ubOEHk2txXghopRVolOyoqdwv702H7-HJr2-4JsISBB1iWV3K86hdkt9inGcecC0O-6tC1NOQg2q_zvN8yVtrvbqqHdjo2orIWSxF4uR0JE0vGD5eqpBQc-cRqKWq_KHvcP6M93IpIE-YE_s4kj4wEAIbSk9qSjMzcbbymBGwgYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ آمریکایی: ترامپ در حباب میلیاردرهاست و مردم آمریکا زیر فشار گرانی
🔹
ام‌اس‌نَو گزارش کرد: ترامپ در حالی در کاخ سفید مشغول حمایت از رمزارزها، شرکت‌های هوش مصنوعی و مراکز داده است که آمریکایی‌های عادی با تورم، افزایش قیمت بنزین و هزینه‌های زندگی دست‌وپنجه نرم می‌کنند.
🔹
این رسانه همچنین به ترکیب ثروتمند دولت ترامپ اشاره کرد و نوشت: دولت او شمار بی‌سابقه‌ای از میلیونرها و میلیاردرها را در خود جای داده است.
🔹
ام‌اس نَو با اشاره به وضعیت اقتصادی آمریکا نوشت: خارج از «حباب کاخ سفید»، نشانه‌های هشداردهنده متعددی دیده می‌شود؛ قیمت بنزین همچنان در حال افزایش است، بدهی ملی آمریکا از مرز ۴۰ تریلیون دلار عبور کرده و نرخ بهرهٔ بلندمدت اوراق قرضهٔ آمریکا به بالاترین سطح خود در نزدیک به ۲ دههٔ گذشته رسیده؛ وضعیتی که نگرانی‌ها دربارهٔ تورم، استقراض و آینده اقتصاد را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/457949" target="_blank">📅 15:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRm0WzhuKAhl60iiYPKopPHPMGww0fhOmG988F4QkoTDZ7ESbQolNbJCY1L3-Tfu40MZ-BzLFvx73sOqxFQegVmJwe1GvclnufolHkpuM8JRTJEzXJMmyUzDfB8wm-sJV_airZA5gO-ZdMB5bizMFp6FJ_DanACcoVu2_Vupt1nJvJ3DYIxQf3iM4UnSOrcbnW7hHG84bptrXOd5SdVogEpTJ52ndUwETizcWY3ohsAPYvxmxV-CFrjlg-kPJiGv_HVVytBK_tEwHNPIB9v-m9oF0y9VDCQ0FW-WEIX-fsxvxQEzj0tCV0zBrAJQbtI6WKAyOsowGwGQAR8RsZIYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف شعار انتخاباتی ترامپ را به تمسخر گرفت
📌
ترامپ امروز نسخه‌ای تقطیع‌شده و جعلی از سخنان قالیباف را در پلتفرم خود بازنشر کرد.
🔹
در پاسخ به این عملیات روانی، رئیس‌مجلس با تمسخر شعار انتخاباتی ترامپ نوشت: آمریکا را دوباره گرسنه می‌کنیم! (Make America Hungry Again)و با انتشار تصویری، آمارهایی را براساس گزارش‌های رسمی نهادهای بین‌المللی و معتبر آمریکایی از گرسنگی مردم آمریکا منتشر کرد و بحران واقعی جامعه آمریکا را به نمایش گذاشت:
🔹
۴۷ میلیون نفر درگیر گرسنگی و ناامنی غذایی در سراسر آمریکا.
🔹
از هر ۸ شهروند آمریکایی، ۱ نفر شب‌ها با سفره خالی سر بر بالین می‌گذارد.
🔹
۱۶ میلیون کودک آمریکایی قربانی فقر سازمان‌یافته و بحران معیشت شده‌اند و در تمام شهرهای آمریکا گرسنگی یک مسئله است.
🔹
قالیباف در بخشی از این تصویر خطاب به ترامپ نوشت این عددها مثل بلوف‌ها و فیک‌نیوزهای تو جعلی نیستند و تو نمی‌توانی شکست‌های خودت در مقابل ایران را با دروغ، جبران کنی!
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/457948" target="_blank">📅 15:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URk8aPmKlQdCAtsnc2jpV70rXTD6BmwONyT7x_79lRcZ6GWiJ8GWLn5qivUg7HmbgK79kh5JlPZ77F5s3t0jGQ1JmsnfTw4EWjldDZA45D9zS-Sh350SGk6BHLIkYSGw6HXuKZ4P8Qt7YCEVRpSu_VM34YT-RCTpDSLK1ekq9AjmeEqX1j3HL957QUQapdjb4AErFK5x-cw7KmoKR5aUTQf4GttRe76I-G094vjOE_-Jw8hgjtsZapHDwgXW60DoJA_Kp8TJKs0KpbQHBUH2Wc10AzvLrDDtiKm5tK4DjHtIFblatILvH1vaDFPXgKZAdpw_PTBMzU91AP_wZwR9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار رادان: دشمن به‌دنبال ایجاد آشوب در کشور است
🔹
فرمانده‌کل انتظامی کشور: جنگ سوم هنوز تمام نشده و باید با حفظ آمادگی کامل، از دشمن غافل نشویم؛ دشمن از ما دست برنداشته و جايی از ما دست برمی‌دارد که ما دست برتر داشته باشيم.
🔹
دشمن به‌دنبال ايجاد آشوب در جايی از کشور يا تمام کشور است و بهانه‌ها از جمله در حوزهٔ معيشتی، بنزين، اقتصاد و بيکاری زياد است.
عکس: ‌فاطمه عموزاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/457947" target="_blank">📅 15:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPKo3DWYkpRjO0RBNxZVsFvMeXRnU4iUJn95cjQDLzktaD0ndWnXSVG6SnDtYJEOTyo6_YtcFuo9n3Ll6aJT-YKT1q9piuqyZdtQ9NJ4UnMrMfDxpLG3ah2G-kFWraNm1fL55q552EDE2p9QBChdN4Yu_t_zOYJ0-f4WHjU6VLkGjceXRBngcN2tRfvfxAI604USOZwuU0MZDaucE271Sq-W2i0KGdv1QVvQFmFP5qlr3X7BpzDIGy-7wWggNnP8B9MV5_Zoba0QKpTTMvBDpE_HL0aY4dupNt-lnQmTtrHuD7JM1NohSDnVmbZqbbvRT0Dk0-KAyZPC6eck0HugVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فدراسیون فوتبال ازبکستان: تیم‌های ایران و ازبکستان ۲ مهر دیدار تدارکاتی برگزار می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/457946" target="_blank">📅 15:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNRtdgckOiY0DTi0GTnA53L2B6-w8lR3q9RqKcMCfvXrSqkwgcfwSxWcOaiWM3NSBws11c95wuh7TTWJ-J4e0aRGek6D0ilUEekN0I1lCX4nJSoBOVKFpPy99kKJRxwjfD89I4AydETOypFuOfiqTt9WlOsUm2T_zXQfek79aPXJV3nVLNhvvuggQxiZx6VrjgD8PmUC-RAVymRjmXquZfyQn7VJWibNrtnT2Tey0BDpfLpCGbM6wCeChGOnWsPwMRklsooxHS_rTBo0jFDWg2ha83LHV6zh4LdMdGZahiUVgR7Oy1guWIVcgptnWelig4O3Lghy9xe1kFekxZ5CIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرسامان پیشوایی رئیس بسیج اساتید شد
🔹
با حکم حجت‌الاسلام طائب، میرسامان پیشوایی به‌عنوان رئیس سازمان بسیج اساتید کشور منصوب شد.
🔹
پیشوایی دکتری تخصصی مهندسی صنایع را از دانشگاه تهران دریافت کرده و پیش از آن در مقاطع کارشناسی و کارشناسی ارشد در دانشگاه صنعتی امیرکبیر تحصیل کرده است.
🔹
او در دورۀ دکتری دانشگاه تهران به‌عنوان دانشجوی نمونه انتخاب شد و از سال ۲۰۱۷ تاکنون در فهرست پژوهشگران ۱ درصد برتر جهان در حوزۀ مهندسی قرار داشته است.
🔹
پیشوایی همچنین به‌عنوان پژوهشگر برتر جوان توسط فرهنگستان علوم در سال ۱۳۹۸ و پژوهشگر برتر کشور در سال ۱۴۰۳ توسط وزارت علوم انتخاب شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/457945" target="_blank">📅 15:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9519db8048.mp4?token=BnkZaDJY_OjIXU4jmrGYqfVFIIfRXKV2BgVFhXN5ZCyq_cBDi90qgmBsm0-6SWsm0_StFDrcC6ahZfQBgcni_5F4J15Y0y5cZk6ckdq9gbGbfNQHQ7yvmMucxNqfF3VGhgtGW64hZppcjaZPTjSzECDML3bnoEqVM4X9dSfV2DrotUrnCp2l1Dl-HOxKQ5gIpUNxTYD2fwwTXFQ_PxNOFj5L1Di7rEuXIDh6LnDCEYMW2GhBgyCtrI13aQTDvzAUuqjHZfW_eIrIspGKrWxvJ4yp89EqUVoam-G9a7sInR1Cifo8_5FNAVC8MLGu6WZ86uFc8RExuOxFbHy1kmLcRz2lW6fzi8560nQka1Yedh77qVoLveLq6fTsnUSoFtKKUXse7cENDHEF_wMe-WhAnrkJE2PQ4oJr8dUMUHh0obTolyy9ubtHsQ6XpZUNegBPM2U_j-R43bdcAQCLwPCUr_1WIi0t9EHpnkOoBKoov3N1R1xI-sOCHX_aC2Rk24xnQbgDX184YPBrFX3Ex8zWJb4njh7P7mviyj10F8IB3b3O7GeZAg3q_a2W5tl7IZz1KwtQWIrJBogtCWiZkiXuez76LilzM-N2xpxeZUd4R-LaT1hZcVLZov8PQ49JF1RMYfoKvNbNJDcGYJhzfONgE9a-cVZjYBXaTubQ5GD9V3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9519db8048.mp4?token=BnkZaDJY_OjIXU4jmrGYqfVFIIfRXKV2BgVFhXN5ZCyq_cBDi90qgmBsm0-6SWsm0_StFDrcC6ahZfQBgcni_5F4J15Y0y5cZk6ckdq9gbGbfNQHQ7yvmMucxNqfF3VGhgtGW64hZppcjaZPTjSzECDML3bnoEqVM4X9dSfV2DrotUrnCp2l1Dl-HOxKQ5gIpUNxTYD2fwwTXFQ_PxNOFj5L1Di7rEuXIDh6LnDCEYMW2GhBgyCtrI13aQTDvzAUuqjHZfW_eIrIspGKrWxvJ4yp89EqUVoam-G9a7sInR1Cifo8_5FNAVC8MLGu6WZ86uFc8RExuOxFbHy1kmLcRz2lW6fzi8560nQka1Yedh77qVoLveLq6fTsnUSoFtKKUXse7cENDHEF_wMe-WhAnrkJE2PQ4oJr8dUMUHh0obTolyy9ubtHsQ6XpZUNegBPM2U_j-R43bdcAQCLwPCUr_1WIi0t9EHpnkOoBKoov3N1R1xI-sOCHX_aC2Rk24xnQbgDX184YPBrFX3Ex8zWJb4njh7P7mviyj10F8IB3b3O7GeZAg3q_a2W5tl7IZz1KwtQWIrJBogtCWiZkiXuez76LilzM-N2xpxeZUd4R-LaT1hZcVLZov8PQ49JF1RMYfoKvNbNJDcGYJhzfONgE9a-cVZjYBXaTubQ5GD9V3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم ۳۲۰۰ ساعت است که پایین نیامده
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/457944" target="_blank">📅 15:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgj94I7hb0sOUgohMaBPfk1S_7YPqnTqRsZQkZnIMvnEJiEl1xhdwCvpnRrVXGHQyhS0ijZsDNfmv2KxWkz7my8sN3Q5lJtD512EotW9T7V0Ob-XCDoP_p0XYZaJ1xwDlA8Nc8hwv74IW6P_gDVHw8HEVrpCNhSTs45wxAgWHAF5YPxzAa1EujwFDSMcHovo0FehX2PG7MByFpzC2EyaRXN9Uc1cSpIT_LjzG5JEhEPbRPpPlzMYW-QX5YYZ5l1JKB4jd2jVQYjew4O9lTuu0qiJnxz403WWkV9CdTSSyJwJwtndXxPbUDL_LGzWsAJ_JWFa0fLZrFnfXKEFoFpYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرلشکر رضایی: همۀ جهان فهمیده‌اند ترامپ خالی‌بند است  @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/457943" target="_blank">📅 14:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKFTsLq0bvcryN4l4Uowtl0cwFLGtrwqrm0-KD8d2gt33K02WaAlgrQAlnzK_qg0QvXHzWaZImT8JN1atk-C_h7FPEnbIYYee4bw2G1aVXVuq7jvBgbvf108KkNcCq0Pk7fLJFk54QS8VdlSsFD0VoE9pkFvsuqCNs9hZWk3gYhcFBD4S9yQU4q20xa_T_2pTFc1T1FQSWD7VWGQ3NJkxtS-GJK54g7itoTdEsOTejshG3919_9qxjAaETClrXmQD3VDZOogsErKAO_JBwharnP-nZrU_wbsZwQB8lBmbk2RDHtFZi8yvWl5cNvlsVLQOgJEjHYzcQ3D8_CyuyMp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش برای ذبح قانون و شکستن اقتدار کمیته‌های انضباطی
🔹
نامه ۲۵ استاد دانشگاه شریف در اعتراض به حکم انضباطی یک دانشجو، با واکنش منتقدانی مواجه شده که معتقدند حمایت از دانشجو نباید به معنای نادیده گرفتن آیین‌نامه‌ها و مقررات دانشگاه باشد.
🔹
منتقدان تأکید می‌کنند میان «اعتراض مدنی» و رفتارهایی مانند اخلال در نظم دانشگاه، تخریب یا هتک حرمت نمادهای ملی تفاوت وجود دارد و هر تخلفی باید در چارچوب قانون و از مسیر کمیته‌های انضباطی بررسی شود.
🔹
حجت‌الاسلام رستمی رئیس نهاد رهبری در دانشگاه‌ها تاکید می‌کند که رسیدگی به‌موقع به تخلفات هم به نفع دانشجو و هم به نفع دانشگاه و جامعه است و نباید تخلف بدون پاسخ باقی بماند.
🔹
سعید عبدالملکی عضو هیات علمی دانشگاه معتقد است که دانشگاه هم مانند سایر نهادها باید بر اساس قانون و آیین‌نامه اداره شود و اگر قرار باشد تخلفات و رفتارهای ساختارشکنانه بدون پاسخ بماند، اساساً فلسفه وجود کمیته‌های انضباطی زیر سؤال می‌رود.
🔹
مهدی تقوی جامعه شناس می‌گوید که باید بین اعتراض و اخلال در نظم و رفتار خشونت‌آمیز تفاوت گذاشت.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/457942" target="_blank">📅 14:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457941">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN1IdMzVnkym5LSR9eQc-3-iXJ_y9n8YYqZrI5ydnSyOXFoIghdcS2gs7cF5QMkuAbJ1-bRE_xrSB7ICTULB7FMS_E09-33qLGZV8t6CFJMmN8H5xzzI_H1sJNSEvX4bBIKgIh65EiQ2QzBAK04tjTL3-ojCcQ7EKczVKCigD4ywcwnlKaAz4TODT1OouUYovr39R97FUjkMF_US3B2VU_-q6cKgUq2NJVE7gABYPkpmzcoq5upp1KMEGOeKWfu8o69DN1uqkljCDj4KNNKVVnX9E5Ty-VB4k7Wnras_PHzlrmtwYqChBoWu-LSIPxvNQEvBedc9ZBehyicvS6YDAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستان شهریار: یک نفر از اعضای شورای‌شهر فردوسیه به‌اتهام دریافت رشوه دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/457941" target="_blank">📅 14:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457940">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84e839840.mp4?token=anZgpIPqWo2joDN-RWxni4kSqg_lkWrjANpC0ywADg83S3MNnf4_bSC3QvsE85MqpgTXtitDUxe8lywcWdy1whQUqLUeRgl3ZesUrmrDJ1otYYADtJi3lW3L511QEE6zoAd9G_gr90S3iH-esmbrLi0XjabA7MdTPscawDG8nXAgnxj9gEBwjP0d1ZyoMbezJ4zXoPf5gOZ_S4IMH-8cQBz_pPCGl8uj0XzaQr87NXIr-20AbK2Twg9R0PHTPRHedd43qrt2TFNJOpx_fD571HJQAGSz2H9-jfFCyHPbo-EgFbWMJVKQAuy2kg-ld6jTEl_YAX88iIqKrtM8xoP0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84e839840.mp4?token=anZgpIPqWo2joDN-RWxni4kSqg_lkWrjANpC0ywADg83S3MNnf4_bSC3QvsE85MqpgTXtitDUxe8lywcWdy1whQUqLUeRgl3ZesUrmrDJ1otYYADtJi3lW3L511QEE6zoAd9G_gr90S3iH-esmbrLi0XjabA7MdTPscawDG8nXAgnxj9gEBwjP0d1ZyoMbezJ4zXoPf5gOZ_S4IMH-8cQBz_pPCGl8uj0XzaQr87NXIr-20AbK2Twg9R0PHTPRHedd43qrt2TFNJOpx_fD571HJQAGSz2H9-jfFCyHPbo-EgFbWMJVKQAuy2kg-ld6jTEl_YAX88iIqKrtM8xoP0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: پیروزی را تبدیل به شکست نکنیم
🔹
آمریکا که تا دیروز به فکر سرنگونی ایران بود اکنون تمام بحثش تبدیل به باز شدن تنگه هرمز شده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/457940" target="_blank">📅 14:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457939">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
وزیر نفت: ۷.۵ تریلیون گاز در جنوب فارس کشف شد
🔹
بیش‌از هفت‌ونیم TCF یا به عبارت بهتر ۷۵۰۰ میلیارد فوت مکعب گاز کشف شده که با احتساب ضریب بازیافت حدود بیش از ۷۲ درصد امکان حدوداً ۵۷۰۰ میلیارد فوت مکعب استحصال گاز وجود دارد.
🔹
این میزان گاز معادل این هست که…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/457939" target="_blank">📅 14:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457938">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات فردا در جم
🔹
سپاه جم: احتمال شنیدن صدای انفجار ناشی‌از خنثی‌سازی مهمات از ساعت ۶ تا ۱۸ فردا وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/457938" target="_blank">📅 14:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457937">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a612469ccf.mp4?token=C9kDtMzjL9wwhjpolvqiG_QAel1GfBYzhrLUFVVv0E28oSecH4X5mnCAehDvJ7t5_BND3o4OjaGYFYDOWVu6pEnfXMLCL3MpcJNcKZg9fasMI1YsZ-QeafMDf9nodujcDnNCky9_BXjOXRRGpvBfoMvJWiyz4PJHDRs63bz-zmGN6z3oqUCwBJgJ-K2DlMczmfzuPd4kLYMRZrO88x_3w1jGJa5rFMBPe-Szd2a84-ilWJqqnNQqr28foEmWkDWAJXKgD6tylpqlDrfnCB4dx2u-ugCT32yMmbITaESqQyhKPExZkf4YevZf1qASwKL6Cg073X9Mvj0slHqPMD98aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a612469ccf.mp4?token=C9kDtMzjL9wwhjpolvqiG_QAel1GfBYzhrLUFVVv0E28oSecH4X5mnCAehDvJ7t5_BND3o4OjaGYFYDOWVu6pEnfXMLCL3MpcJNcKZg9fasMI1YsZ-QeafMDf9nodujcDnNCky9_BXjOXRRGpvBfoMvJWiyz4PJHDRs63bz-zmGN6z3oqUCwBJgJ-K2DlMczmfzuPd4kLYMRZrO88x_3w1jGJa5rFMBPe-Szd2a84-ilWJqqnNQqr28foEmWkDWAJXKgD6tylpqlDrfnCB4dx2u-ugCT32yMmbITaESqQyhKPExZkf4YevZf1qASwKL6Cg073X9Mvj0slHqPMD98aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خورشید هفتۀ دولت امروز بر ۴ استان کشور
تابید
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/457937" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457936">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGJQ5FJrR7ozKyTBBePyGiD0DcCLwWiCmi9o1mfsTpW4EHv2Bk6Nqo_vM36GI5xIn73Z2TzPdykYTXKDIeYZJ0qWnCP1-x9zs08b4LCDDL8oaZeyR2V_5UBOV3ycyuWRZN5gx4yZTIattezbsd3CQOzBHZcX36P8Fx9DCNw5T7cQd7URBI17bPCeCacPIM1rDMNv7fSVFcsRZBk4nGJl6yYBDWU41L4lqAQRsszYJe1CrbeiZpSFVyH_GhKBPsfA3v5Ryl7ZII1-epXM2AP7R5L-y533IMVI9FHAIN-CaXKscceIrXzidHaoMRjagjvxlTBJbkV4PaQMYQd2Vb6scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رقیب جنگی‌اش را عوض کرد
🔹
رئیس‌جمهور آمریکا پس‌از جنگ ۴۰ روزه بار دیگر سیاست فشار حداکثری علیه ایران را با کلیدواژهٔ «Economic D-Day» دنبال کرده و از تحریم نفت، انتقال پول، صرافی‌ها، شرکت‌های پوششی و شبکهٔ کشتی‌رانی و مالی خبر داده است.
🔹
با این حال، بخش مهمی از این تهدیدها هنوز در حد ادبیات سیاسی است و برای اجرای واقعی به سازوکار حقوقی و اجرایی نیاز دارد.
🔹
بسیاری‌از این ابزارها پیش از این نیز علیه ایران استفاده شده‌اند و اقتصاد کشور طی سال‌ها با تحریم‌ها سازگار شده است.
🔹
آزمون اصلی ترامپ، توانایی آمریکا برای وادارکردن شرکای ایران به‌اجرای تحریم‌هاست که در این میان چین به‌دلیل نقش مهمش در خرید نفت ایران اهمیت ویژه‌ای دارد.
🔹
از سوی دیگر، ترامپ با ایجاد نگرانی در بازار و فعالان اقتصادی تلاش می‌کند بخشی‌از اثر تحریم را پیش‌از اجرای آن ایجاد کند.
🔹
بنابراین پاسخ ایران باید علاوه‌بر حفظ موضع قدرتمند در برابر فشار خارجی، بر اصلاحات داخلی، افزایش بهره‌وری، کاهش رانت و مدیریت ناترازی‌های اقتصادی متمرکز باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457936" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457935">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYI2iyfYDnjfY7lw0KlXDYujvQKEjM46OkSj74ZvovrYY_lALIFg68St5z3fa2XM3d3zL1WSP0N0CbpR6n0HcJBKLRRL4b1jklwEGexFi0VXVBUr7j2CihC23BqX9LcnkXFTrMK3Sh13l_SGuHros5Y75D23XY363ElEmh6Rsno2NEnT4nRegklpHbE1lYOxvxXXIc18WcPzROOelQia6nAe6awxYC8CAiZvW0_OfGUOV-TuA3Tvs1MBhr5RPl-xzBzHTxvlFL3IenN9W2bfqBHU5MGfFtvxyhvBlfxbrLHfGtlQef_IesAScTVHn6nt-E6R0ppMbZ6TrlEmlV_DdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/457935" target="_blank">📅 14:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457934">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=MMsCAGTnO8Ib2IdfvpfI8bsSyBMtjtlifErr1HtPMp3hJb018HBjvWUpb9yMCJUHmMmXcf1Yzf0FcfRQox_ysLkl4gLb5Qy5fpqOs4k6uCiNRXeJc0RDFjWoBFV6fpjwnh2NmbAnV8Ko_NSzEWESCPR6lcr8RsaB7w43Oa1VD9LltT_cdAHX5w0oZ7g5u894aT_zugScQp9z49KiW5__TrJrMztR0C8JBtZWLv91VgnTsupvHypO_xjKo4u7uR_KpSL1wHfOw8383pkaDD4acDQqKa4p6xpERBSonzRkJyoFxYXap0dyhsp_o2Gc-hWSbMJ3lnoy7fVBM2t5Um-9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=MMsCAGTnO8Ib2IdfvpfI8bsSyBMtjtlifErr1HtPMp3hJb018HBjvWUpb9yMCJUHmMmXcf1Yzf0FcfRQox_ysLkl4gLb5Qy5fpqOs4k6uCiNRXeJc0RDFjWoBFV6fpjwnh2NmbAnV8Ko_NSzEWESCPR6lcr8RsaB7w43Oa1VD9LltT_cdAHX5w0oZ7g5u894aT_zugScQp9z49KiW5__TrJrMztR0C8JBtZWLv91VgnTsupvHypO_xjKo4u7uR_KpSL1wHfOw8383pkaDD4acDQqKa4p6xpERBSonzRkJyoFxYXap0dyhsp_o2Gc-hWSbMJ3lnoy7fVBM2t5Um-9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: وظیفۀ ما خدمت به مردم با هر گرایشی است
🔹
خودمان را بالاتر از مردم نمی‌دانیم. باید مشکلات معیشتی مردم را حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/457934" target="_blank">📅 14:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457933">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88da696fea.mp4?token=O2hTbv5vYAD2Lfci3flURj4GSXtiEA-cJzFppTvhV2qt9IlExJ5ILndNRBY3LeH5sUHf5Me1EkGwQYhtOjmzm-zmHCEBI8gGpXsfehdm1d7IDu_dzLKUXrtqzDRKSTpmi34TBhfI9V2U4GFzQ5NYPQvU-QcXABFCdsXZGYP219r5fsLApJshNfJDkq4Z1lo_qFwiUkbZilJyVDB8iOBF-egssuLbpDWGSS8xJ7_E3n5SVUDp90709TwAxRhIs2xJKo_9fZAYPOTQuAqBj7xBpNySCFIjzESMxU7G3uhVNBK0ihelBCqnmOnvq2d6wMZt-0I-HJBlVaKVSBKW99BX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88da696fea.mp4?token=O2hTbv5vYAD2Lfci3flURj4GSXtiEA-cJzFppTvhV2qt9IlExJ5ILndNRBY3LeH5sUHf5Me1EkGwQYhtOjmzm-zmHCEBI8gGpXsfehdm1d7IDu_dzLKUXrtqzDRKSTpmi34TBhfI9V2U4GFzQ5NYPQvU-QcXABFCdsXZGYP219r5fsLApJshNfJDkq4Z1lo_qFwiUkbZilJyVDB8iOBF-egssuLbpDWGSS8xJ7_E3n5SVUDp90709TwAxRhIs2xJKo_9fZAYPOTQuAqBj7xBpNySCFIjzESMxU7G3uhVNBK0ihelBCqnmOnvq2d6wMZt-0I-HJBlVaKVSBKW99BX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده کل ارتش: باید آن‌قدر تلخی در کام دشمن بریزیم که از آن سوی دنیا نگوید نقشۀ ایران را عوض می‌کنم
🔹
ما باید دشمن را ناکام بگذاریم و آن‌قدر تلخی ناکامی را در کام دشمن بریزیم که بداند ایران جای این نیست که از آن سوی دنیا بیاید و بگوید نقشۀ کشور را عوض می‌کنم.
🔹
ما ۱۰ نسل ۲۰ نسل می‌جنگیم و حتماً اجازه نمی‌دهیم این اتفاق بیفتد؛ تنها راه این است که با زبان زوربه دشمن بفهمانیم که نمی‌تواند کاری را که می‌خواهد انجام دهد.
🔹
همواره اهداف کوتاه‌مدت، میان‌مدت و بلندمدت دشمن را رصد کرده و آماده مقابله با هرگونه سناریوی دشمن هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/457933" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457932">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbR-uAcpv20rBjHNqbRf7PTjRGxlNjMneEAm4cxuF72vrhVMZZU5guHOL2PyShkcfbGpFUl9W9m2e8NXjq5_eGxoadjoF-RQBCejx0aSX_dPbJrtBm1Eh0sJPgPsDP6osYbrYUhLMlC0kJatFM46foCc-Vm9zoDxmlrQZ3au2WjLnJbcTD8Wvvfi3B79B9hgJLwc8KYIZ9OCmNiZvAqZqYqs-cd7QZaJcfL8Eo3sZQVJFT2GWpdcLT8_PDWzqrPAsVnWxCPhL51Htr1PkOPGr8kAhgIzSph_ovJ66gRuYU-zN5K1VMP4a98ra3YD7Zqp9_6Etc_xR_pDWEd9ljoraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تزریق دلاری پسته به اقتصاد ایران
🔹
آمار یورواستات نشان می‌دهد، ۳۴ میلیون یورو پستۀ ایرانی فقط نیمۀ نخست سال میلادی امسال، در اتحادیۀ اروپا فروخته شده، با این رقم می‌توان ارز کل نیاز گوشت وارداتی را تامین کرد.
🔹
صادرات پسته نسبت به‌مدت مشابه سال گذشته ۶ درصد افزایش دارد. این افزایش در بحبوحۀ جنگ ایران و آمریکا اتفاق افتاده که از اسفند ۱۴۰۴ آغاز شد و آمریکا با محاصره دریایی تلاش کرده اقتصاد ایران را تحت فشار قرار دهد.
🔹
یک تاجر ایرانی به خبرنگار فارس گفت: هیچ مانعی سر راه تجارت وجود ندارد؛ دولت پول بدهد کالا تحویل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/457932" target="_blank">📅 13:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457931">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9fe0cf116.mp4?token=Q_2XJWxoVmy5SVyZBuMkr3A6B9pmb3z5TggM4b07yKxLJlewGTLapW6qSKLwot7wMWn8ep0AUr5FoNlHndQe4TxHhstryyfBvz-lHrWcfUt9D6XQPFQLXwHsecrIlWU83P-P27QDZl1yDvrUd9XLD0qfjf73dIzWcihkmVo41nZH6qoKqybxm6JPh7-3rdZImDC2LAw6mzANThGKc7l6nblNYPuURM90GHbMktxSVMfyiVHZvUhKWPo0RKo7b1fH-3e4wZSknSpRZXau2huChsuyuuvxi1UXdx3zzvYuWBP3OsCoRBYYo9SDWLoKVbW6uG6lT-tcCJuk80hHsYezvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9fe0cf116.mp4?token=Q_2XJWxoVmy5SVyZBuMkr3A6B9pmb3z5TggM4b07yKxLJlewGTLapW6qSKLwot7wMWn8ep0AUr5FoNlHndQe4TxHhstryyfBvz-lHrWcfUt9D6XQPFQLXwHsecrIlWU83P-P27QDZl1yDvrUd9XLD0qfjf73dIzWcihkmVo41nZH6qoKqybxm6JPh7-3rdZImDC2LAw6mzANThGKc7l6nblNYPuURM90GHbMktxSVMfyiVHZvUhKWPo0RKo7b1fH-3e4wZSknSpRZXau2huChsuyuuvxi1UXdx3zzvYuWBP3OsCoRBYYo9SDWLoKVbW6uG6lT-tcCJuk80hHsYezvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/457931" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457930">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766881483a.mp4?token=Y5t6Ke5SuynbiC82GMHjYQgxYheNXhmQLmVmPsmvKyf82e1FxRA3LipHrvOB38frHoJwoO6ihHNQIXmt-vzBafoHN8AzmM_1b8UJE0ZCktJKpLEBAtlBmUcACIebxG4fgcylf9yJo4H4oydHMBQ07OOL128mVM7lVyLy3sX1hkQEiVmWmzj7XNo8gNBSFfzuy5Zpj6XubypS9-luGMLnj75XZQkpZkfEOEnVNsaTrtEJ1ry5w6OpCbb6y2hLuZDAhwANR3ROFfuRJ48gK7G_QLihpkUgDfhHz-z8K1heD34ltLce5X5WtSWPyWmbQn8SsLo29324SZZNK9NubQR4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766881483a.mp4?token=Y5t6Ke5SuynbiC82GMHjYQgxYheNXhmQLmVmPsmvKyf82e1FxRA3LipHrvOB38frHoJwoO6ihHNQIXmt-vzBafoHN8AzmM_1b8UJE0ZCktJKpLEBAtlBmUcACIebxG4fgcylf9yJo4H4oydHMBQ07OOL128mVM7lVyLy3sX1hkQEiVmWmzj7XNo8gNBSFfzuy5Zpj6XubypS9-luGMLnj75XZQkpZkfEOEnVNsaTrtEJ1ry5w6OpCbb6y2hLuZDAhwANR3ROFfuRJ48gK7G_QLihpkUgDfhHz-z8K1heD34ltLce5X5WtSWPyWmbQn8SsLo29324SZZNK9NubQR4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: مشکلی برای تامین ارز نداریم
🔹
همتی در نشست با اعضای اعضای مجمع کارآفرینان: ۲۰ میلیارد دلار برای صنعت تا پایان سال تأمین ارز انجام خواهیم داد.
🔹
از ابتدای سال روزانه به‌طور میانگین ۱۷۵ میلیون دلار ارز برای اقتصاد کشور تامین می‌شود.
🔹
برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/457930" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457929">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYPdckV4eibDm905ajaMtsw9b216sWBKbGs-27aZjxWlR-iJ_dLEa7QkjfbI7ADHmQIzl9aTn90sxG0SlpAPytGMgAPW40ISwWtiC6T92jkHbwmWMpAYm_BxoZWeEhQUMtjtD6G1tsugbDqvhRkJ-oheVpfCxa9p9Kyupz7WwI_qNjKyXZ46EABKe8HYfoC2mrD6Jk1eGj1meoT_3Z-7qryNmch9gnyoeVxIUwGlP7M_7jT18EQO6Bqq1Zl4GkudxaMMdm5Hsq_1STQKRSRDTJp_YZv3_pUobGSWHCk7ZX6Jl36682SxJunliBduB1AmH9TZZJ2EEMkGXbYvlLGq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مرقومۀ رهبر شهید دربارۀ شهید پاکپور
🔹
سرتیم حفاظت سردار پاکپور: رهبر شهید دربارۀ شهید پاکپور مرقومه‌ای داشتند که شهید پاکپور به‌خاطر فروتنی اجازه ندادند منتشر شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/457929" target="_blank">📅 13:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457928">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7c83d867.mp4?token=uh-_bk9EKzkQcDtQEOQboHir4_gnMLJFg08NakRxPwhYJbbIy6VLkrEkC6nFLzbI7EJfZ2BEeQOVcj2WTpDKNLn3xEN6JHoha_7vqnxrRIOoEc8R65WFIwxoOf6SvnSgHdb4XNEYJsUsWYitPIVyJxudCsDnVy-JgHMTj2LLBIFyCNZ16qcXCjMAw08exmaBg4pQQgq3rxCUBTkuIb4a_7CtplTARjZUhHxe-dOfuDvb5XAs4jZuBlEBa9IDds23KpNKIoW8KDRFJP7uE5UHzkbKDeu27Mam3jaaTiWGdH7Tq9Q9pGu3Q-AiKS49POnwbKY_57iemUWdeBYuFnOWCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7c83d867.mp4?token=uh-_bk9EKzkQcDtQEOQboHir4_gnMLJFg08NakRxPwhYJbbIy6VLkrEkC6nFLzbI7EJfZ2BEeQOVcj2WTpDKNLn3xEN6JHoha_7vqnxrRIOoEc8R65WFIwxoOf6SvnSgHdb4XNEYJsUsWYitPIVyJxudCsDnVy-JgHMTj2LLBIFyCNZ16qcXCjMAw08exmaBg4pQQgq3rxCUBTkuIb4a_7CtplTARjZUhHxe-dOfuDvb5XAs4jZuBlEBa9IDds23KpNKIoW8KDRFJP7uE5UHzkbKDeu27Mam3jaaTiWGdH7Tq9Q9pGu3Q-AiKS49POnwbKY_57iemUWdeBYuFnOWCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبداللهی دادستان انتظامی قضات شد
🔹
با حکم رئیس قوه‌قضائیه، علی عبداللهی به‌عنوان دادستان انتظامی قضات منصوب شد.
🔸
پیش‌از این مسئولیت دادستانی انتظامی قضات را جعفر قدیانی برعهده داشت و عبداللهی عهده‌دار مسئولیت حفاظت و اطلاعات قوه‌قضائیه بود. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/457928" target="_blank">📅 13:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457927">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA7BJmfVKzswUXkX6JFkH87KyNF7jgiRdnmU0p9AWWEFfYfSInHdzMLb64uRcqCbs3Z6a0StcoaH0AcByKyzq7y-fbcjG37T5ipPxMS2OY70fThK-Fnp9aWpudnIHtv-93djc7AGttYVXIjznwq_oamtmV58FEVqp4cyKfo95Xa9KC43G7PsdYbRRDSyP82ZhOnYOO-57DCZsvGCYW7a1OQn4jK6zlXpT8Rs_xcu4OjJLChcZgZuy26zZeiwsLK4dMwLiiyXpv_a6cz9LS1s6imyCdMq6f0TFEViBgj2v5P7TGbk4o1l7kLdNwc-ji3AYt7E7gndtn6lezcGuUlOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک بسیجی اهل سنت در زاهدان
🔹
نیروی زمینی سپاه: نادر سارانی سخی، بسیجی اهل سنت، دیروز در منطقهٔ شیرآباد زاهدان درپی حملهٔ افراد شرور و کوردل به‌شهادت رسید.
🔹
پیکر مطهر شهید فردا ساعت ۱۲ ظهر از میدان امام حسین(ع) زاهدان تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/457927" target="_blank">📅 13:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457926">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469cda217a.mp4?token=I_QhRHEhQYA73Z4FGuF-4WAI63FcmIPFiOUzJfMKgAj7WsFh59iuHlKwLLzCARm5F0De9xDXCOf3hhGtljroyaMd3T6mchvDH7mbPu4aUd0ouWo0ZcSKpI6FC4KYur7q5p13-PrQDVZtwDvXpTShDlY5c_N7TbE--TW0fS5LWAkFywIACfceXhRn0mnQeTzh2iDGpKOo9onddwkWsWTegxx_rlSCkaM-4edBXy6Ncj_Ojua8LjBGGDBK5kPaOtfG5ISia2qm7jwv4cXRSvOMni2qm48rpWT0f2OdQASSNkYbdWY296f1N-aOfpG_N-16KVyK9NygxqvE0duDL6hATQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469cda217a.mp4?token=I_QhRHEhQYA73Z4FGuF-4WAI63FcmIPFiOUzJfMKgAj7WsFh59iuHlKwLLzCARm5F0De9xDXCOf3hhGtljroyaMd3T6mchvDH7mbPu4aUd0ouWo0ZcSKpI6FC4KYur7q5p13-PrQDVZtwDvXpTShDlY5c_N7TbE--TW0fS5LWAkFywIACfceXhRn0mnQeTzh2iDGpKOo9onddwkWsWTegxx_rlSCkaM-4edBXy6Ncj_Ojua8LjBGGDBK5kPaOtfG5ISia2qm7jwv4cXRSvOMni2qm48rpWT0f2OdQASSNkYbdWY296f1N-aOfpG_N-16KVyK9NygxqvE0duDL6hATQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ما با دروغ‌پراکنی‌ها و شایعه‌سازی‌ها میدان را خالی نمی‌کنیم
🔹
وقتی ۶ میلیارد دلار دست افراد معدودی قرار می‌گیرد و ما می‌خواهیم آن‌ها را ملزم به ایفای تعهدات قانونی‌شان کنیم، آن‌ها واکنش نشان می‌دهند و بخشی از واکنش آن‌ها، خلاصه در حاشیه‌سازی و دروغ‌پراکنی در قبال مسئولان‌امر می‌شود. ما تا استیفای کامل حقوق مردم و بیت‌المال، پیگیری‌های خود را ادامه می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/457926" target="_blank">📅 13:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457925">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f6915bf1.mp4?token=tmKIT1Z__ZLZ4gQLV0HPZvUOSk6MzdgWH_IAE19JK_JTt3grw77zSUga4tNpKTh2isUFFwEYAtPoNPxUmbg986jaCnqXS0jXhBAsWDactHjIRrdyrks_t_IqVZxA3ub5EMQ5B7HT5nKLQqvsG73heWWVD6Q0quATr0rIF320EViauGKtqL39TITc26dLyP3UsojxjDI-Z-aYPW5vRCaWAB0r9WNOLzJrOhBp-XURs5gyltbZzwXT8Zk04Oa_7ahG4Fbpr55yLIWfzG26sKnxjc8lf_8afVHYx2mZ-kYklYslugDxBWZkk4P_TJNZrJ3QF5iNQ4Obgwax6wAjB8r_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f6915bf1.mp4?token=tmKIT1Z__ZLZ4gQLV0HPZvUOSk6MzdgWH_IAE19JK_JTt3grw77zSUga4tNpKTh2isUFFwEYAtPoNPxUmbg986jaCnqXS0jXhBAsWDactHjIRrdyrks_t_IqVZxA3ub5EMQ5B7HT5nKLQqvsG73heWWVD6Q0quATr0rIF320EViauGKtqL39TITc26dLyP3UsojxjDI-Z-aYPW5vRCaWAB0r9WNOLzJrOhBp-XURs5gyltbZzwXT8Zk04Oa_7ahG4Fbpr55yLIWfzG26sKnxjc8lf_8afVHYx2mZ-kYklYslugDxBWZkk4P_TJNZrJ3QF5iNQ4Obgwax6wAjB8r_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در موضوع رفع تعهدات بیش از ۷ میلیارد یورویی، من به دادستان تهران تکلیف کردم که فهرست و مشخصات دقیق و کامل بخش‌هایی که رفع تعهد کرده‌اند را ارائه دهد
🔹
در همین موضوع رفع تعهدات ارزی، حدود ۲۰ میلیارد یورو هم تعیین‌تکلیف شده؛ یعنی درج نام برخی بخش‌ها…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/457925" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457924">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ad069d7f.mp4?token=o78qaL0ojMHzpPW1vbbCaPG6JBB8cjHHag73_Lmf_afCh927erBBuO1nXf_wEA14pHgwXnjOQnr4PqC7U2SAiiyEbudZTxXbQPs9SXg3pKriEy3MVxIcpd7-kHoUVr61yuMHzgnqCON4AZdjG0M_zw10SWOck_37mJtPBzhrQdU7tcamzEtTSnkdR299ZpitaXEseYzh0VH9DVLXMC1XXTcL1LHLZSfFRg2LwAtEHfvqrX4yLZ4pDwmXFdFLL5-PV6AE2SWfe-NJIO71d0h7j4nfxBi0dCK9Ih5aTMfNi3I_LqH0w3axFkpmrpdic2oc_xJoxS2c3L27gcytqvM32w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ad069d7f.mp4?token=o78qaL0ojMHzpPW1vbbCaPG6JBB8cjHHag73_Lmf_afCh927erBBuO1nXf_wEA14pHgwXnjOQnr4PqC7U2SAiiyEbudZTxXbQPs9SXg3pKriEy3MVxIcpd7-kHoUVr61yuMHzgnqCON4AZdjG0M_zw10SWOck_37mJtPBzhrQdU7tcamzEtTSnkdR299ZpitaXEseYzh0VH9DVLXMC1XXTcL1LHLZSfFRg2LwAtEHfvqrX4yLZ4pDwmXFdFLL5-PV6AE2SWfe-NJIO71d0h7j4nfxBi0dCK9Ih5aTMfNi3I_LqH0w3axFkpmrpdic2oc_xJoxS2c3L27gcytqvM32w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تا اواخر مرداد ۳۵۸ پرونده برای تراستی‌ها تشکیل شده و در یک فقره بیش از ۷ میلیارد یورو رفع تعهد ارزی اتفاق افتاده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/457924" target="_blank">📅 12:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457923">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a66bdffa3.mp4?token=kESFZwAxfwTn8C35712uD9xFCF8aKdlDNpVNJwF9y3v3iCCQn0rCFiGRN5vKBP3lvDOCsyW6MQKeQ5wrQVQ1eN0KFLexLn2uboJC14K_yBNmFQ7qMvRgNYGt9Nf_f_fr-JGMx1HLuSGk6KmbVnBU1pcd056Vwtv2n-EYN8-iHwNfmR_n9TrIniPnFShWiwIe7GH8c342J5mTVahorah47p94E-H00ep1p4fUJdZeKF4uDeInGK4WHvzPWdRsBUsLONClBWJF8SRGJSQnQDVjWagij4q1Afg7wtLfWfr1lFv2vs0ikol6ZFZ9gmfxN7rDbBPKzDm3zbk2njSVkWnaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a66bdffa3.mp4?token=kESFZwAxfwTn8C35712uD9xFCF8aKdlDNpVNJwF9y3v3iCCQn0rCFiGRN5vKBP3lvDOCsyW6MQKeQ5wrQVQ1eN0KFLexLn2uboJC14K_yBNmFQ7qMvRgNYGt9Nf_f_fr-JGMx1HLuSGk6KmbVnBU1pcd056Vwtv2n-EYN8-iHwNfmR_n9TrIniPnFShWiwIe7GH8c342J5mTVahorah47p94E-H00ep1p4fUJdZeKF4uDeInGK4WHvzPWdRsBUsLONClBWJF8SRGJSQnQDVjWagij4q1Afg7wtLfWfr1lFv2vs0ikol6ZFZ9gmfxN7rDbBPKzDm3zbk2njSVkWnaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ تراستی‌هایی که تضمین لازم از آن‌ها دریافت نشده، نباید رها شود.  @Farsan</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/457923" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457922">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58124046a6.mp4?token=S76QaxBH_go3lW3nFfGYgqHPxx6EMLJNY68ays-HzrAyvoDTY0moG7DPMOfBWai1H6D2AKZ-20NBIaY2U2LJjQq8d0lO8QqgAXTaMrYyDWsH2iBNI-vHWaDfJrx5Bw2AY5ZJxvPRnodhL-k2OFtvRYmLDVRqURfxrksYvMqTrnvj3iThY58pKh_Sbp3KwaB7i-hrO0eHFA5AHz0DUFYmd06zKlY7WYrq_6EUIIZEXwfxZjup3CdAD2wh_f1yU3M8mG48cIMANgwcqTetTr7vtpFLS2TLHMxFLBCaYl5XsH0nvNfbLcWW-Gec_LGDddLBJS-0QC_SPC-Zx8DAoHQ-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58124046a6.mp4?token=S76QaxBH_go3lW3nFfGYgqHPxx6EMLJNY68ays-HzrAyvoDTY0moG7DPMOfBWai1H6D2AKZ-20NBIaY2U2LJjQq8d0lO8QqgAXTaMrYyDWsH2iBNI-vHWaDfJrx5Bw2AY5ZJxvPRnodhL-k2OFtvRYmLDVRqURfxrksYvMqTrnvj3iThY58pKh_Sbp3KwaB7i-hrO0eHFA5AHz0DUFYmd06zKlY7WYrq_6EUIIZEXwfxZjup3CdAD2wh_f1yU3M8mG48cIMANgwcqTetTr7vtpFLS2TLHMxFLBCaYl5XsH0nvNfbLcWW-Gec_LGDddLBJS-0QC_SPC-Zx8DAoHQ-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراستی‌ها چه نقشی در اقتصاد ایران دارند؟  @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/457922" target="_blank">📅 12:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457921">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af8c2e951.mp4?token=gDlW0_HlfqVY6D4WO1Q0XcMl7rmCr2fLSQBA3qjTnkPPKMo8RbOygMC5SB4mseMYXPdQZ-NDvmgdDexjaGtBhZtSfAF126ulxvLAua9qHqt_cnezLUuqW4Zwq9kYHYLKQVrJ4QE66GPWbDLuQzEngLcZWVRZOdWawhBOG6HjggeGAMNV2njiPzUrJofkWh-L56X6v9ZcXb_fK97kRpnPEoiUZL2MLBswSJ4LkCg-y7F1od-A9h2q91EB-ctiwcqWc5qma0olRNEd-iyGVPzQNxNm9YJfnk_Un4U9NP7YnUDj2AWdtB6f6m4EgXUB_w9SnMoxEJTLIZtr08IWGeflBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af8c2e951.mp4?token=gDlW0_HlfqVY6D4WO1Q0XcMl7rmCr2fLSQBA3qjTnkPPKMo8RbOygMC5SB4mseMYXPdQZ-NDvmgdDexjaGtBhZtSfAF126ulxvLAua9qHqt_cnezLUuqW4Zwq9kYHYLKQVrJ4QE66GPWbDLuQzEngLcZWVRZOdWawhBOG6HjggeGAMNV2njiPzUrJofkWh-L56X6v9ZcXb_fK97kRpnPEoiUZL2MLBswSJ4LkCg-y7F1od-A9h2q91EB-ctiwcqWc5qma0olRNEd-iyGVPzQNxNm9YJfnk_Un4U9NP7YnUDj2AWdtB6f6m4EgXUB_w9SnMoxEJTLIZtr08IWGeflBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: مشکلی برای تامین ارز نداریم
🔹
همتی در نشست با اعضای اعضای مجمع کارآفرینان: ۲۰ میلیارد دلار برای صنعت تا پایان سال تأمین ارز انجام خواهیم داد.
🔹
از ابتدای سال روزانه به‌طور میانگین ۱۷۵ میلیون دلار ارز برای اقتصاد کشور تامین می‌شود.
🔹
برنامه‌ریزی کرده‌ایم تا ۷۰۰ همت از طریق ابزار‌های تأمین مالی و بدون اتکا به چاپ پول برای تولید تأمین شود.
🔹
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم.
🔹
قول می‌دهیم که ارز مورد نیاز کالا‌های اساسی و دارو را تأمین می‌کنیم؛ همچنین تا پایان سال ارز مورد نیاز صنعت را هم تأمین خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/457921" target="_blank">📅 12:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457920">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3LUC19h0b0Tt0EymbH_anLhC1ymB2lNxplNwWQUI8JNq73HWpBxmr78qTeey9sJ6kJ664ZMiMCfcA4xpYjkM64LEWajS0j0BQmtcVrdobOJlMCncK1On5nZzEw5_pIXoVwvAbWCEUNsTzQdKcPg2vu7NrtgMmFUJPrAA8gdpJ0HU3BX7Ee863gP8Jl1Gs-qmu-zFW7wCLFuXLVaInAmMKUUckrYLOjUzVzKFvklfIdemaHrib22SFBWHFi42k7OpWozFVkvIBLyWzZ377uQhhdDIcpkNWGuiCWoypv4ptngBLoc0g3Pl0t33tLgWsbFsXKtCMoJ9OVgtzNw3IzpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جدید بورس در ۶ میلیون و ۱۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی رکورد تاریخی ۶ میلیون و ۱۰۰ هزار واحد را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457920" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457919">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b227f579e.mp4?token=bzflJFU0lEsamdiWCYwHP5djnZLrUDfU0cDZO4atf0f_suXp8rQZC6H66BIk9yxUUYaW0VUlMuMwMtdP9-VLJXZ2HeanEUg-xjc3kJ4rNGKH-P88Emr5j9K2T1HNYS1NrKYQpeYYxZMeLv-3sQupu8sWOZwu5IIqRubGjepmhXEe9f7x693fc44QWoskAkS_fYDDrpeL7Jt9zMEkcCd9SQfeWXOUBFq5yiZ-hWS2EaR_tNdSiI_x9LoXNcbWqSRz9vO0-85LXmcdjLNzzt3-03-q6IPnUTFnSR4gBudS5XeOsuiKMIA16QoAjWiGh_qKbRw-PboTOaYBWOR6B8-Ncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b227f579e.mp4?token=bzflJFU0lEsamdiWCYwHP5djnZLrUDfU0cDZO4atf0f_suXp8rQZC6H66BIk9yxUUYaW0VUlMuMwMtdP9-VLJXZ2HeanEUg-xjc3kJ4rNGKH-P88Emr5j9K2T1HNYS1NrKYQpeYYxZMeLv-3sQupu8sWOZwu5IIqRubGjepmhXEe9f7x693fc44QWoskAkS_fYDDrpeL7Jt9zMEkcCd9SQfeWXOUBFq5yiZ-hWS2EaR_tNdSiI_x9LoXNcbWqSRz9vO0-85LXmcdjLNzzt3-03-q6IPnUTFnSR4gBudS5XeOsuiKMIA16QoAjWiGh_qKbRw-PboTOaYBWOR6B8-Ncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
مگر غیر از این است که در ۲ سال گذشته بارها حسن‌نیت ما را با بدسگالی پاسخ داده‌اند و به عهد و پیمانشان پشت‌پا زده‌اند؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/457919" target="_blank">📅 12:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457918">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عاصم منیر وارد تهران شد
🔹
فرمانده ارتش پاکستان برای دیدار و گفت‌وگو با مقامات ارشد ایرانی وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/457918" target="_blank">📅 12:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457917">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjwW7CT-9zbB3kBb2QbOLKoCWY_c64_K-dZ4cwRdXadL4CsIJzLdqkjI5AIUbXcIso1uQgJnlFRSwcGqwmLLUKfNUGlsqd4u5FwNJgX28WXXHh56rYCMRs-dhzmqfPOelbOOOEcguOSTS8Wg8ANDCYWDHRyd-gXaCNPAlzLzCRSznsVsEWta83EpCSba9AFdvReIe8ZhY43eF8-sU5iwn5vzjphPWuMikRqHffkvpuYivjS22nuGhANcO33RQuXf9R1xdZEyclyIbVW4oq4UkNPkmVgTnlyUyh2CtfVu-tY0RAutP07W7I3kVhGfxY3oKtZGoyQd99gGS_zW051rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: عاصم منیر فردا به تهران سفر می‌کند
🔹
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/457917" target="_blank">📅 12:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457916">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9BFt5a2NksKkrKXcPOf7HFCpSxQLXUrLdmqqElXgBZeQJo83FZLhA2O5pHNayD0rFyzl69lAqlErg80CzZitXJv6TTwV70_xbg0Pe7ak8zs8es-rA-b_c0w65epi54lIbLBC2LJ_t2ORIt8oGSwgGKt-j-Thqd1v4UeDBFCuSkK8c2Zf3uhYU_QRMTS7WmNlpf1U-9xrwbp5H2NMCtaFcNhbTdjqh2hVfT2RVXU4Xm9YKEMYRdiMxcTaIpaA3Dozxpyb00nRI8Bp9sqkD3rBKKZRsSAQUgBQrYm0beixzqMmEa9kJa-ZcAVvI1XJC_1YOHL4zW0jmu1LQsMFv6XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلید اولیهٔ سؤالات کنکور منتشر شد
🔹
کلید اولیهٔ سؤالات آزمون‌های سراسری و پذیرش دانشجو-معلم سال ۱۴۰۵ برای هر ۵ گروه آزمایشی منتشر شد و داوطلبان می‌توانند آن را از
وبگاه سازمان سنجش
دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457916" target="_blank">📅 12:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVUGbyHDrxpxQi4H6XAJxm2JmUC-nGeFyFJxAKTug53ENvDXiR-QZs86P2HLhpW5rV8_3NZp0D_G7milecTLnqwGuZmppAv4BVvRNpJ1sxPH3kU3xRSnHMD0UbKhsfk-03kR3rfqHRGbc1iU1GejaaTCdGkFxNI3fzByx-ZnE9ZA5DpD5lr1exqZJCzok7Y_9_xAq0olqReCOC_1OQTay8tIVpqSJqJTb3pxqUASG7dOiG_dbaxnp0G5vokmwGL8PBuCLMFxbN7fR7VeDITJsAgiC6dNosVTkzwMgv3Gq2DJptIHgIPYieN8Cr3gGklxBJPLklvz0-OCPRFIRbRrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش سخنگوی سپاه به ادعای آمریکا درباره امکان عبور نفتکش‌ها از تنگه هرمز
🔹
رصدها از طریق ماهواره‌هایی که آمریکایی‌ها تصور می‌کنند، انجام نمی‌شود؛ روش‌های دیگری وجود دارد که شاید طرف مقابل هنوز قادر به تشخیص آن‌ها نباشد.
🔹
اگر ایران چشم بینا برای رصد تحرکات دریایی نداشت، چگونه می‌توانست نقاط حساس شناور‌ها را مورد اصابت قرار دهد؟
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457914" target="_blank">📅 12:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmgpHx74W9BsNlZTzlEXVYyagD3rBYVnUs2QTg3PUXOi9H9DB-Qbh-nC0iYUp4eKpzdavd-6g0dsYgXhkEnveBGbVcthTPNhp6wqb4-_AJSApD6RXKAJg4zHfsesR6ZSpWJLkhGEvuyJnvUSFNjDLTWVZKfQ1II9dcp70dSGxNM3T_kIaMo54vv2ime42Hi9NBKGo4TigdEArjwxBcPhPwX-oOygCJVbc6Ry1gAcww3EOAX6erfR3KK8gPscWBBfYoEB717kgiG6AcQtskFXiQKVutfrlsPTtlKW0ixq3oLgXPgEkQ1NG9qi-aRW7EgFaNgVtGLiX6FVf1E4cqaQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtGgqXuYF10tLsfkojdYy6f7A2cqUMZT6i0bIkthpaasitv2ceOkBqdFb_PMCDvJNlVkK-bK81jC8cE2FKlQ9HVoJvoJ4TnQ0FwOPA72beUZg1CN33VY7tfhifx3aBGugjItcf0xkb0Yw6JHqixKoZvl3uOWZwzyRMBoRYRr4Av_8T4Lf2qk0unBrf_gAOFu8o--2XYfQvCnTPDNTclfDeFjBiLNF-iYUIKotuZqpHDyGpAlFif3JbOWfeeyP6xnt7BUlBQCgTwMFcbaylJoLzBVbhxDwQ6vF0l0XWmAimF6BJXMK0eN10kz44O_Tsp8TGKI7hhaNBWHa2e6kjInaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی پاسخ تهدیدات وزیر خزانه‌داری آمریکا را دادند
🔹
اظهارات اسکات بِسِنت، وزیر خزانه‌داری آمریکا، درباره آغاز «بزرگ‌ترین حمله مالی» علیه ایران و ادعای نابودی توان نظامی و هسته‌ای آن، با واکنش کاربران خارجی مواجه شد.
🔹
در واکنش به این مواضع، برخی کاربران خارجی ادعاهای بِسِنت و دولت ترامپ را متناقض دانستند. آنها پرسیدند اگر همان‌طور که بسنت ادعا می‌کند و می گوید توان نظامی و برنامه هسته‌ای ایران تقریباً به‌طور کامل نابود شده و تهران در آستانه شکست قرار دارد، پس چرا واشنگتن همچنان به دنبال اعمال فشار اقتصادی بیشتر و قطع شریان‌های مالی ایران است؟
🔹
برخی کاربران همچنین ادامه تلاش‌های دیپلماتیک برای دستیابی به توافق با ایران را در تضاد با ادعای «نابودی کامل» این کشور دانستند و تأکید کردند که ادامه جنگ اقتصادی و تلاش برای مذاکره، خود می‌تواند نشان‌دهنده آن باشد که برخلاف ادعاهای مقام‌های آمریکایی، واشنگتن هنوز نتوانسته اهداف خود را در قبال تهران محقق کند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/457912" target="_blank">📅 11:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99eb90451b.mp4?token=HaInwr6z7AyiLrVywlIXFjsC80BNvUccVdOy989HsD0PftWR4XgE9l4AnbFcsFV3lfEV6w-bOtjjcQwF_TofmhCrnFuza3Lycf3Lt6MUMPN8N0TB4aRlv73ss_tAtaoGcvRd5ppaYgNmJWQQeB4l3q4EPDlxIGSslQflZsgOYlD2LyUjyyOANsnAZ2an0KG-D8B4q14dQsIkLZ3oeM9JOqOXWFc0sOFTRCuKbxvE8sTIV_CgoDTOR0Lerp2hQ_v5kZRg_71a4E-2hXwC9N04w2xH6fwNQWt9nVfFeV4T36mGVhyPUREq4QPBAjbAgspeSi6sCWjbU2g3VlEZg2kf7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99eb90451b.mp4?token=HaInwr6z7AyiLrVywlIXFjsC80BNvUccVdOy989HsD0PftWR4XgE9l4AnbFcsFV3lfEV6w-bOtjjcQwF_TofmhCrnFuza3Lycf3Lt6MUMPN8N0TB4aRlv73ss_tAtaoGcvRd5ppaYgNmJWQQeB4l3q4EPDlxIGSslQflZsgOYlD2LyUjyyOANsnAZ2an0KG-D8B4q14dQsIkLZ3oeM9JOqOXWFc0sOFTRCuKbxvE8sTIV_CgoDTOR0Lerp2hQ_v5kZRg_71a4E-2hXwC9N04w2xH6fwNQWt9nVfFeV4T36mGVhyPUREq4QPBAjbAgspeSi6sCWjbU2g3VlEZg2kf7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: چه کسی گفته دولت باید بنزین را ۱۳۰ هزار تومان بخرد و ۱۵۰۰ تومان بفروشد؟
🔹
برخی تحلیل‌ها و موضع‌گیری‌ها از تریبون‌های مختلف دربارۀ مسئلۀ بنزین غیرمنصفانه است.
🔹
جدا از بحث محدودیت‌های مالی، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومان بخرد و بعد آن…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/457910" target="_blank">📅 11:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c647992.mp4?token=f7h8YxASHx6ps_kza-48xl7VSpQhvi4SGqV55YkiSG-MQ8-p-QxWwBNWhOGFnBMzWHC3Jh5mJyv2tQMj3Y5TDZLg6m-56jMe1TFiJ5FBC8z8Cwps7tlls9889e1neOULyowhdZHTsrDEVXSS2PuHM95l2mdpHdOcpEvr215XMe1AbqAKprX56n74E7WJcOxQTndPd9cK54k3yd0h9EWcdrPMCD3xXvCutQTZanv9YtxbIgvH37EjVff3cMGqqluby-zgbcaOZcHxe95UBvsaUOHw2MRsLCvcZpUkiVb45oXmXKJkpfewD7FQp6ZLCG0GuDSchQLCzFonXpI_zzZ9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c647992.mp4?token=f7h8YxASHx6ps_kza-48xl7VSpQhvi4SGqV55YkiSG-MQ8-p-QxWwBNWhOGFnBMzWHC3Jh5mJyv2tQMj3Y5TDZLg6m-56jMe1TFiJ5FBC8z8Cwps7tlls9889e1neOULyowhdZHTsrDEVXSS2PuHM95l2mdpHdOcpEvr215XMe1AbqAKprX56n74E7WJcOxQTndPd9cK54k3yd0h9EWcdrPMCD3xXvCutQTZanv9YtxbIgvH37EjVff3cMGqqluby-zgbcaOZcHxe95UBvsaUOHw2MRsLCvcZpUkiVb45oXmXKJkpfewD7FQp6ZLCG0GuDSchQLCzFonXpI_zzZ9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از «تحریم‌های فلج‌کننده» تا «فشار حداکثری» و جنگ اقتصادی، آمریکا به‌دنبال تسلیم‌کردن ملتی است که تصمیم گرفته از حقوقش کوتاه نیاید.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/457909" target="_blank">📅 11:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3ffcbf39.mp4?token=QYHUaeGIY3aoRADLllIm6uyN0f8-M56WWSHNFr--kINNK9qhAfzgG57c4nzDLwRWGnmT_jCrIUtQ_tIOPrd3poSxFcqEfLZOlkbHuVothDpIHlGfxVZ4VPtcuOdrKkbtfrKRlo5XLAcYh8Yu2EIokrs_Z2WPB7tSOuq-NwmLscdlUD556-9utOxeAr_ZsW9bGPBFNjs18jtQgweRFIhfziBIYNiS7TarKvBSnLRMu3zMtHaf5Xe6dUwW2Nry1t_GB7Y3g3Zwcu7hgnU6JuTlWJm1CEQGr-NQUOXQpcC3lA_Ua6OUZUZSyHj-L4nQqxXTE0bJQBQ4tU9oZCJ89D_R1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3ffcbf39.mp4?token=QYHUaeGIY3aoRADLllIm6uyN0f8-M56WWSHNFr--kINNK9qhAfzgG57c4nzDLwRWGnmT_jCrIUtQ_tIOPrd3poSxFcqEfLZOlkbHuVothDpIHlGfxVZ4VPtcuOdrKkbtfrKRlo5XLAcYh8Yu2EIokrs_Z2WPB7tSOuq-NwmLscdlUD556-9utOxeAr_ZsW9bGPBFNjs18jtQgweRFIhfziBIYNiS7TarKvBSnLRMu3zMtHaf5Xe6dUwW2Nry1t_GB7Y3g3Zwcu7hgnU6JuTlWJm1CEQGr-NQUOXQpcC3lA_Ua6OUZUZSyHj-L4nQqxXTE0bJQBQ4tU9oZCJ89D_R1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای‌عالی استان‌ها: بیش‌از ۶۰ طرح در شورای‌شهر مشهد به‌دلیل غیبت اعضا بلاتکلیف مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/457908" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در جاسک
🔹
فرمانداری جاسک: احتمال شنیدن صدای انفجار کنترل‌شدهٔ ناشی‌از خنثی‌سازی مهمات تا ساعت ۱۹ امشب در محدودهٔ شهر وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/457907" target="_blank">📅 11:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkvNplUquhRB5KfcGd06eqwJXhwhzEbz3Ofwp9ReGEYgdu3sg9jFV7gbFpS1A7YMfS3xaLSD8VE_wkgQ5lmaBqaIC5JWzhYnsTkzpxwvpkJrzbhGs2XecqLsOkiEaXhJmUyYFXcZQYUU0Eg04RqPe0Wsb-BT3_5hOMvTZHDwxpMJOIgs0pgiure5WmcDhL6iT5pasGkro3OKngAGmhxbwLBldY6UhqiA-KdKUd4VxZ5ff_OyqFfwbuuWCCmjpG0RBFdWSkT0KhIRu_4AZv-xCABd3pIfJfgXAo_22HErryHJtGBNb-NfvVv0Y7XLAymNlvBOmOJ1CdCoXPREPHs_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در ۶۳ مایلی غرب ینبع عربستان سعودی هدف حمله قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/457906" target="_blank">📅 11:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496effd822.mp4?token=UWcNG6gnmlvfBp937QBBecLGyTXLLBtxb1rkeWuZQblWNjNWGKgJJQLea8uqyBtEzctGs0BK0TdwWgAfkSnfn-GtPO1AgAJ3uNrtwAwlRXmStZ_0dFzCUF9DT1TWBxNW8HI5U72oZiFQ6iA0ZSTef-a4NGScKX3-XDaBloZExOqrOqM1RyKEU71krEKfKpEwjmuv4rXCM7kLvZUqdj0zSShaOCGECGQQssIYcRHIl4fqa9XZp02WSLTGD3QdFRnXjusrqlCxqkQSaJfL25WQBBHATVElRMCdamufrwDVMdlwjZXCHPYiQcJ8AWv-q6TMq1mtdtRP2ewNK1vKj5QorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496effd822.mp4?token=UWcNG6gnmlvfBp937QBBecLGyTXLLBtxb1rkeWuZQblWNjNWGKgJJQLea8uqyBtEzctGs0BK0TdwWgAfkSnfn-GtPO1AgAJ3uNrtwAwlRXmStZ_0dFzCUF9DT1TWBxNW8HI5U72oZiFQ6iA0ZSTef-a4NGScKX3-XDaBloZExOqrOqM1RyKEU71krEKfKpEwjmuv4rXCM7kLvZUqdj0zSShaOCGECGQQssIYcRHIl4fqa9XZp02WSLTGD3QdFRnXjusrqlCxqkQSaJfL25WQBBHATVElRMCdamufrwDVMdlwjZXCHPYiQcJ8AWv-q6TMq1mtdtRP2ewNK1vKj5QorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
مگر غیر از این است که در ۲ سال گذشته بارها حسن‌نیت ما را با بدسگالی پاسخ داده‌اند و به عهد و پیمانشان پشت‌پا زده‌اند؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا هم دربارهٔ آن‌ها گفتند «امضایشان را با مداد می‌نویسند».
🔹
ایران هرچه می‌توانست در مسیر دیپلماسی برای جلوگیری از جنگ تلاش کرد؛ آمریکایی‌ها برای نقض تفاهم‌نامهٔ اسلام‌آباد حتی یک‌ماه هم صبر نکردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/457905" target="_blank">📅 11:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOosTvz_dY_RXkf_0GQkQ0C0KqM-TO7G-4WCow8rOZiDy_GGSlhJwlIoR3flpnXnK-POj7-CoP6jSpDdyB5hu-je53FJOs4oNbzVwxL9nL3wFw8s100FqzlsfLb1lpXI-Q0Gk0bp4EtftBtStIXwPK3kayNdeLyfUSdaSz1PMWe3q6bP0OEY7V9TYooAJPydfAV7H9VlHwaaXviG8ym3OQChXxhjuR_H0qW1iRloU7xddfq9JVYEUQGXBRR2dDg4zEh9J5tSMJISDXbokkT3bIip5NMbzvlpbt3PqtM1_UQ5xiH5U93UYubf_NEMI1vZri5vfi8Nsid6nV0zUQMvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بهانهٔ ناترازی را به مدیریت ناترازی تبدیل کند
🔹
رئیس‌جمهور بار دیگر با اشاره به ناترازی در حوزه‌های آب، برق، گاز، سوخت، محیط‌زیست و بانک‌ها، شرایط ابتدای آغاز به کار دولت چهاردهم را تشریح کرده است؛ اما مسئلهٔ اصلی نه تکرار ناترازی‌ها، بلکه نحوهٔ مدیریت آنهاست.
🔹
ناترازی به‌خودی خود به‌معنای خاموشی یا توقف تولید نیست و دولت می‌تواند با توسعهٔ ظرفیت، مدیریت مصرف، بهبود بهره‌وری، مدیریت بار و استفاده از مشوق‌های اقتصادی، آثار آن را کاهش دهد.
🔹
این مسئله مختص ایران نیز نیست و اقتصادهایی مانند چین، آمریکا، انگلیس و ژاپن نیز با شکاف عرضه و تقاضا مواجه‌اند.
🔹
تجربهٔ سال‌های ۱۴۰۰ تا ۱۴۰۳ در حوزهٔ برق نشان داد که در کنار توسعهٔ نیروگاه‌ها، مدیریت بهره‌برداری و مصرف نیز اهمیت دارد.
🔹
در این میان، پرداخت پاداش به مشترکان برای کاهش مصرف نمونه‌ای از تبدیل مصرف‌کننده به بخشی از راه‌حل است.
🔹
بر همین اساس، مسئلهٔ اصلی دولت میزان ناترازی تحویل گرفته شده نیست، بلکه چگونگی اداره و کاهش این شکاف‌هاست؛ چرا که مردم در نهایت با نتیجهٔ ناترازی مواجه می‌شوند، نه با عدد و آمار آن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457904" target="_blank">📅 11:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4c126731.mp4?token=tInvHTkpPYSgvd9r0F7gTaEdfJJE3NNLW1XTGcCsKoYxR_PEjNMtVBqM0rLsWgeKjXvHJTRwbWSEU-XQFzDZa9Z-HI_h8BHnfuEluKHPGBUhg7_xo9mU2lHCXraGUJZFps2_zdGDYtUhJB46kOVuni41UI81S_vImjOAHPFqgXB8OyAuDZ5hHf_kH1h-NhPzQySUcFFVTNtkfjU7jgiUQL7eHngaQJzZJCiL7O0KpeHc9xt0nVV5CWwQGhwg78ZpJu_1dGHSvkSvVzs8grY-hCiQGT6cMhTc1JJC05X5PiSPvAmEwXbmbMUZWktkdq7zZHg3ZxiAgvaSV4HhMBuDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4c126731.mp4?token=tInvHTkpPYSgvd9r0F7gTaEdfJJE3NNLW1XTGcCsKoYxR_PEjNMtVBqM0rLsWgeKjXvHJTRwbWSEU-XQFzDZa9Z-HI_h8BHnfuEluKHPGBUhg7_xo9mU2lHCXraGUJZFps2_zdGDYtUhJB46kOVuni41UI81S_vImjOAHPFqgXB8OyAuDZ5hHf_kH1h-NhPzQySUcFFVTNtkfjU7jgiUQL7eHngaQJzZJCiL7O0KpeHc9xt0nVV5CWwQGhwg78ZpJu_1dGHSvkSvVzs8grY-hCiQGT6cMhTc1JJC05X5PiSPvAmEwXbmbMUZWktkdq7zZHg3ZxiAgvaSV4HhMBuDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به خبر عبور روزانه چند میلیون بشکه نفت از تنگهٔ هرمز: این بخشی از جنگ روانی دشمن است و چنین چیزی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/457903" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda71af95f.mp4?token=ae4xv_H8tTT3Ei7JKbuwyJ47awL-8akdLLF3F7nrCvvYn9Q9H67DFNnyEOW_JOcpuaN5sDAAaiTPfrpq__nYOR_vFrafb7V_EMlfPFQsSyNsw9nwox1S1Mvbs-aJlkpO4fXLoNI0AEL_Ryj83uxC4w2PBzTg790lP-u0x89YKrkqCm-QIxEe1dFBhgZu6lsp-SuZqssM7MUWd3AwSDQIksPmdR1lyqwF1AuDIr5oqem9P9w-KRci9giXggrdSUdqqvrebh54B_2blEZXJDPJAnt9oru1rVbK6pITGEW75OgRCIYNxYPIDiNV6Z_hSxuprHlCHEaa8aEKo0_TWrc7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda71af95f.mp4?token=ae4xv_H8tTT3Ei7JKbuwyJ47awL-8akdLLF3F7nrCvvYn9Q9H67DFNnyEOW_JOcpuaN5sDAAaiTPfrpq__nYOR_vFrafb7V_EMlfPFQsSyNsw9nwox1S1Mvbs-aJlkpO4fXLoNI0AEL_Ryj83uxC4w2PBzTg790lP-u0x89YKrkqCm-QIxEe1dFBhgZu6lsp-SuZqssM7MUWd3AwSDQIksPmdR1lyqwF1AuDIr5oqem9P9w-KRci9giXggrdSUdqqvrebh54B_2blEZXJDPJAnt9oru1rVbK6pITGEW75OgRCIYNxYPIDiNV6Z_hSxuprHlCHEaa8aEKo0_TWrc7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با ترکیه، پاکستان و حتی عربستان پیوندهای عمیقی داریم و دلیلی ندارد بابت پیمان مکه نگران باشیم
🔹
پیوندهای درهم‌تنیدهٔ فرهنگی بین ملت ایران با ملت‌های پاکستان و ترکیه کاملاً روشن است و این تحول نشان می‌دهد که کشورهای منطقه نمی‌توانند…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/457902" target="_blank">📅 11:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df75e8de6.mp4?token=h5soH2PlhLVnGS98BmEm6gTwx_t6G8OrqqTdS8_Gw7V0Z0LwgCYr5ofsFRlKvLeSELv5JW1rW-wB8TDizqbYMWo82Q992hN50CtzDVLWXWzxjccQ0yj6TxfcvCOMbbFinDbnM04IL9m7pa95jsWhHgT_INMrT7xW3XaqaJ7DbW5UVULYZVTzKSE-_AhX4xiYL0HYTItEUNuaZY2KvsVnu8vLzBkD7lpgViA3rk7N2OvBT_DhHUPiYBlRC-RDPQffHnwCeeCdRpUQSvptctUgiPLGIxQ37kauJaIpe820ELEPUJsrzxYRJBepm1YrrkBQRL0eFpLkwJwE1wcLmc1BAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df75e8de6.mp4?token=h5soH2PlhLVnGS98BmEm6gTwx_t6G8OrqqTdS8_Gw7V0Z0LwgCYr5ofsFRlKvLeSELv5JW1rW-wB8TDizqbYMWo82Q992hN50CtzDVLWXWzxjccQ0yj6TxfcvCOMbbFinDbnM04IL9m7pa95jsWhHgT_INMrT7xW3XaqaJ7DbW5UVULYZVTzKSE-_AhX4xiYL0HYTItEUNuaZY2KvsVnu8vLzBkD7lpgViA3rk7N2OvBT_DhHUPiYBlRC-RDPQffHnwCeeCdRpUQSvptctUgiPLGIxQ37kauJaIpe820ELEPUJsrzxYRJBepm1YrrkBQRL0eFpLkwJwE1wcLmc1BAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همکاری بلغارستان با آمریکا برای حمله به ایران، عمل تجاوزکارانه است و هدف‌قراردادن مبدأ هر تجاوزی، حق ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/457901" target="_blank">📅 11:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
جلسه‌ای که رهبر انقلاب استاد راهنما بودند
🔸
این فیلم مربوط به دوران پیش از زعامت رهبری است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/457900" target="_blank">📅 10:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz9N2-2KEM70i8MOCwCj_VuCvp2OMWPIuJ22c28jCUvsdl-w-u7kXJzO-NgMOJD0Iec42iJG5OsZ27hqgcEPIQLcHOVNf11v6_k_DaxpQgY3R4sYYI-NmgqfCCTmrBA0pS4qAD2dgKQYHv6NOjVUz34qHVZuyzRhkstM660Q4rcXLqztE6V5IrShyb7hi0PQ2q5WI82O5IVJa518kUVEdSbm21TRAk85FlgZ3bVbl28U0gt6ezdwA6_DXB7Mu05DTBe4d5fBaeEdvKLRlzh9OJws6Tq6REEWm3007c6tXFIbWAq8oYYyqGqmZg7aOfTT47y9bGBnRgxvj648yQxvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: آمادۀ کمک به دولت هستیم
🔹
بیانیۀ ارتش به‌مناسبت هفتۀ دولت: امسال در شرایطی هفتۀ دولت فرارسیده که ملت ایران در معرض آزمونی بزرگ و شرایطی متفاوت از گذشته قرار دارد.
🔹
شرایطی که اداره امور کشور، حفظ اتحاد و انسجام جامعه، تأمین نیازهای اساسی مردم و استمرار فعالیت‌های اقتصادی و خدماتی، در کنار صیانت از امنیت و تمامیت سرزمینی، نیازمند همدلی، تلاش خستگی‌ناپذیز، تدبیر و هماهنگی همه ارکان نظام اسلامی است.
🔹
هم‌افزایی و وحدت ملی یکی از مهم‌ترین مؤلفه‌های قدرت جمهوری اسلامی ایران در عبور از شرایط سخت و خنثی‌سازی فشارهای دشمنان است.
🔹
ارتش بر آمادگی همه‌جانبه برای همکاری و همراهی با دولت در مسیر اعتلای ایران اسلامی، تقویت اقتدار ملی، رفع مشکلات مردم و عبور سرافرازانه از شرایط کنونی تأکید می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457899" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN_A1sNduVw-p9edcUuXC_ku0WWaGll0KBjuZj5VNEYEU0-J2g-rzP7TRdtpCEc4HDNBB0dMbVmbtK3PmzNvYKecEQsC-8Q9Bvs2HPz1zXYRRh73hm6P1Gsk9upapJSfmTHeggvuAJvl3lWS12Q9gnqzVXS3nFt4s73aUP3vnH2sSdkDDwkKxPmBY2NmgWXwN8jjyv4Ls54FpiwHjQxd0bIBeiK_PeOrXMY5lkA4EX5fF8zwPOnPCpoLJQ8PBnjg2sRj3cif6SgHblMKBus98PDV0zbynb3h4ARQzYpM0SHQvtb2rCyYJ6YaQImiUcx8bi0pbZR_4QbKqiAF_IgfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: تنگهٔ هرمز نماد وزن ایران در معادلات منطقه است
‌
🔹
خیابان هم‌صدای جامعه‌ای است که دنبال پیروزی است. دوباره دوگانهٔ معیوب جنگ و صلح را شروع نکنید.
‌
🔹
اگر دنبال پایان جنگ و پیروزی ایرانیم، باید حاکم تنگهٔ هرمز بمانیم و یادمان باشد که موفقیت از مسیر مقاومت می‌گذرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/457898" target="_blank">📅 10:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60671806ec.mp4?token=Ke2szQQVBeiMZCM3CuCaDu5Ia71J_qgV1Vye64pQBrTBUrCNJGw_eJ2ddT_t6eUgkyNqBw1NU6Rr1ayxpBmbLvzWaU5bs1CCYfbgwr3HbpnnvyKMNocV0xKaXvdWN5TBQIX-linZOZvs7U84WsL0W0H-YPasYNRertBhwlVNbERL01IZCXkW_qf7IQN1WkCKSIjxkxkVXZvqawmBlhm4jGZQzxnxxbxCi983ve-s2NLKPCZBAKdMeQu6mKeb9fG3w-4Jm41wulpQgS-wLKfHNJENbAwRb6S-AW8l-aFe_7vjq9LNUaiibXVjk_-AevpkjOyL843a84n32I4_LnlKZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60671806ec.mp4?token=Ke2szQQVBeiMZCM3CuCaDu5Ia71J_qgV1Vye64pQBrTBUrCNJGw_eJ2ddT_t6eUgkyNqBw1NU6Rr1ayxpBmbLvzWaU5bs1CCYfbgwr3HbpnnvyKMNocV0xKaXvdWN5TBQIX-linZOZvs7U84WsL0W0H-YPasYNRertBhwlVNbERL01IZCXkW_qf7IQN1WkCKSIjxkxkVXZvqawmBlhm4jGZQzxnxxbxCi983ve-s2NLKPCZBAKdMeQu6mKeb9fG3w-4Jm41wulpQgS-wLKfHNJENbAwRb6S-AW8l-aFe_7vjq9LNUaiibXVjk_-AevpkjOyL843a84n32I4_LnlKZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرقومۀ رهبر شهید دربارۀ شهید پاکپور
🔹
سرتیم حفاظت سردار پاکپور: رهبر شهید دربارۀ شهید پاکپور مرقومه‌ای داشتند که شهید پاکپور به‌خاطر فروتنی اجازه ندادند منتشر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/457897" target="_blank">📅 10:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH62q46HArKCoIebOn59vJUG0BH78ALo6D3NwhClwKHYLjn4UIxaJ9pFpi4dASYfRVI6wZGAh6aUma19A9ANDNZQPo86A1lwHYrKlI4UCEYI6NchPmR1HjS-h14pK99Seyadk4ox-rTXdDVW4OdsANvv9p4etJoCw-8lPI41r2YOJ5I5Rlx70k3nDtKK0ShgysoXL0aJMNJnNXpnNDd9ceaE6TQG1s6YaQe66nwHq3iCWvjJBMHW-8wSlJ-Zq32faoETjF7QAS8o4CN_tybVr_pX_ZB6wbfQ_raps-P6WGO3XmgjoQjHbn2XygJBg7NJAKud48pFw9_zuRa1_xNu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصره‌شکنی کشتی ایرانی در «روز دی»
🔹
طبق گزارش پایگاه سوپربرو، یک کشتی کانتینری منتسب به ایران توانست با عبور از خط محاصرهٔ آمریکا در تنگهٔ هرمز وارد آب‌های ایران شود.
🔸
این درحالی‌ست که ساعاتی پیش وزیر خزانه‌داری آمریکا در یادداشتی از آغاز فشار اقتصادی جدید علیه ایران موسوم به روز دی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/457896" target="_blank">📅 09:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محکومیت دولت آمریکا به دلیل تحریم کودکان پروانه‌ای
🔹
دادگاه حقوقی روابط بین‌الملل تهران رای به محکومیت ۶ میلیارد و ۷۸۵ میلیون دلاری دولت و مقامات آمریکایی به پرداخت خسارت مادی، معنوی و تنبیهی در حق خواهان‌ پروندهٔ کودکان پروانه‌ای صادر کرد.
🔸
در پی خروج دولت…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457895" target="_blank">📅 09:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNuXj8dh0dtNJlFj7AUo3WhsatNvdCOI4X8XYY7DHzLcri7Z15CJLSq4dpi9eBYj1pyK_oma72h5-1OkZVjkyvN285pKXI1U9MxReyJz3FW7s_wljpKbu25jl95GI_J4_bo5NNfUN_d4m-MHGW7WeMuYgtnrk6ma35EQkPjMItfTrXVY-S_M2XkukCus5-NCEROKpRZSr4TuiWHFZ8nwB6z65Xsc2_u4RfRBh6kjaN1svCumFLwwN-LedLK_E4K52xrBuI4WpnZd1mMFoCjIgXDgTQgGf2jCg02yLd_FKnSlfNNGDHHVUqyLEJoG8r9rze2jOqoox5ZAlJAQGYpvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ عمان فردا به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه: این سفر در راستای تقویت همکاری‌های دوجانبه ایران و عمان و ادامۀ مشورت‌های مستمر سیاسی بین دو طرف، به‌عنوان دو کشور ساحلی تنگۀ هرمز، برای کمک به تقویت صلح و امنیت در منطقه انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457894" target="_blank">📅 08:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457893">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856e524d9.mp4?token=HRFDqzwJsiqAPjuV6kaqErrzkCG8qe6Q8Ak6xO6-XOpO0S7ynzGIpxOPHaA-2gXj1scRiqIN_b6qrM9jQFkZcQVSTUL0Cyy7Mngn48crTN-cEbcz58Vw15Ri88cI33lyWEyYa_72Lqh9uW3aMeVfjf63pt2jsZ32LUM50dFNSvaoTxigHogsUIfG86L7kuuEsQs5X3lQHxOYbTM5yH3VhvKStZlpxtzYUMykVcaWpOTF8RHqXOCQE2W1yPQU-b7t48FeypMf6Dnt82fFxdBO1Tav1DDiRbgzi2IrjgJbdsWE3rNNwwu7UgokQ-nqc1Qu695fTkEyEyX8DlD7nS1M2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856e524d9.mp4?token=HRFDqzwJsiqAPjuV6kaqErrzkCG8qe6Q8Ak6xO6-XOpO0S7ynzGIpxOPHaA-2gXj1scRiqIN_b6qrM9jQFkZcQVSTUL0Cyy7Mngn48crTN-cEbcz58Vw15Ri88cI33lyWEyYa_72Lqh9uW3aMeVfjf63pt2jsZ32LUM50dFNSvaoTxigHogsUIfG86L7kuuEsQs5X3lQHxOYbTM5yH3VhvKStZlpxtzYUMykVcaWpOTF8RHqXOCQE2W1yPQU-b7t48FeypMf6Dnt82fFxdBO1Tav1DDiRbgzi2IrjgJbdsWE3rNNwwu7UgokQ-nqc1Qu695fTkEyEyX8DlD7nS1M2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در بیشتر مناطق کشور امروز هوا گرم خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457893" target="_blank">📅 08:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457892">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۰۵ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/457892" target="_blank">📅 07:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e697756d.mp4?token=DB6TzOzSr5XnxT-WwBlkGEIAEYyga8dJrl1Cq9Y-rg1DECuNW2miw0a6eWhamELb86i0uefjLH_GQsu7lJyeKcX1isnDI7-eNifG-_4NxaIxNmHTRSSQ5sjXqt6D1lZuQAnKVFe_OACS0w_zYq92DugTu515-sQqpdUB-TCTg-OmFbOUx2Z9QroaJ5bhLwAteSeejwO5tMRix4JBY0RdS4EbFeZQGYcbpNuc-zN42uQyEw5dZJY9_ivAkE-OAAXkPC3AC8_uNKmryqP3Uuhtdfxu7jQJ0eGQUcfnri9BafNODNSdMO-cTHF9aOfcbQRVY1coO8aPGzGrmCi8GMYqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e697756d.mp4?token=DB6TzOzSr5XnxT-WwBlkGEIAEYyga8dJrl1Cq9Y-rg1DECuNW2miw0a6eWhamELb86i0uefjLH_GQsu7lJyeKcX1isnDI7-eNifG-_4NxaIxNmHTRSSQ5sjXqt6D1lZuQAnKVFe_OACS0w_zYq92DugTu515-sQqpdUB-TCTg-OmFbOUx2Z9QroaJ5bhLwAteSeejwO5tMRix4JBY0RdS4EbFeZQGYcbpNuc-zN42uQyEw5dZJY9_ivAkE-OAAXkPC3AC8_uNKmryqP3Uuhtdfxu7jQJ0eGQUcfnri9BafNODNSdMO-cTHF9aOfcbQRVY1coO8aPGzGrmCi8GMYqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعهٔ امیرالمومنین(ع) خودت را ارزان نفروش
🎙
حجت‌الاسلام کاشانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/457891" target="_blank">📅 05:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457890">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملۀ اسرائیل به چادر آوارگان در غزه ۲ شهید برجا گذاشت
🔹
در نتیجۀ حمله به چادر آوارگان فلسطینی در نزدیکی بیمارستان شهدای الاقصی در دیر البلح در مرکز نوار غزه، دو نفر شهید و چندین نفر زخمی شدند.
🔹
این چادر محل اسکان آوارگانی بوده که از مناطق دیگر نوار غزه به این منطقه پناه آورده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/457890" target="_blank">📅 03:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457889">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-O1_tHf8CDuLiXFB5lOX8VyhhyAZzsVNlXVAC1myKlGXE7qPKRgBZwVJxm3dky3bsjdswqUL_F0b1PQJ2doGcLuwN4WUytXam5OZCi7cUHMApUUyR6_4txRdsKRc4pWrKN9v5x6dA9dY5ZjuKWnt-UdGJteBPPOAYO-B6JJRFC9griQBYrjof-IRonGt0JYwwt6Ebq08_BngZDKGwqgI8I2JnDPENZHPEy5rR5A_G289UyC4mMqQCnDGJsI_rsSfYYmCGpRNaMZhXX45_9BzX_np2H8Yt3QVveMbxrj3UtX15J5OHHDQCLaXH8JYaq0nJOJf6dNHG1Yobv5kG35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاوشی برای مردم جنوب ایران آستین همت بالا زد
🔹
محسن چاوشی، خوانندۀ نامدار و دست به‌خیر کشورمان از راه‌اندازی پویشی تازه‌ برای آب‌رسانی به مناطق جنوبی ایران خبر داد.
🔸
چاوشی چندی قبل نیز در اقدامی خیرخواهانه از راه‌اندازی دندانپزشکی سیار برای ارائۀ خدمات رایگان به نیازمندان مناطق مختلف استان تهران خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/457889" target="_blank">📅 02:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stCiW-ptDAynKhqapRKL_LOWPidaK6ZVNTV2XCrsJZoy4KG8DUPqqDD9ZJ2qWF5w4wWCp6oq99ZNZ7a7iJ-COUEgfEUXB9vAzcvMGiqNgEqx5BzhDQf1jr_-NFMCUTxM-D-8YI8a688NNaOPAcWIwv-fiMLlX-Mt1S4j-xppV3jwLFmyhz6RoTutsxAoB_GZfCDM1Y9_dH54wE2pnbHHkRpeDOte6mFhpY7aLwfi_opPVxZ0AJhZgYRhvL1laqJhgue-FIovOEeZ8BfpLaWOBe6PciTtVaFWOesYZEFktwdWDOruwfVf9_Z6GFMzbKtO80SmGd2tHU3DGJHUMUnxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj6TXhb0pbOvexgHDGzUL2nAMeQGF300Yfmz9m_htYiUNhfrA6kYU5fvdLwbnTZ2zRI1lpZGh8ALAdUGIEJ7jFqZ8TiNMu3wmhIwH40rw2_JQSYxe3lVB0TlJM2gzdsxn2uik9p24cJDNmse7weAV88i0ay7WSJ7xSSYeYOeyAvn4qCJ2q5X-0PEWUfucCbLnItOrViUT4crRCHC092CImXhZCR0Fbg3DhjQhnHcf9KPwv-s9zE4sUxEx-RyNyfYIFo98tqD9bb7582xbCWZzyf-VfemoFf-k5FjLNB-L7UnmelLwYpacbYpuUmt3JqwAv_pHDTuLJIoW7Y33NcoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6XhOqEC8gMnhS78rdfTsx1b8UrfdYEcl9UQp58JSnU0icIv0kQ61ayETetf3K_IFJQKhEfluh6QViPdEpU7UZLzFznO3haGLbCwJ_4-k1pFWlF_g3RCjxXOTW4Zwd2MoPm2bwN4QRBa_AqqfMhnP_AacJMLP-VHc5LA6w04d3tDSead2RfQWNvrXE2Hhxj0gSUuIwO6D06IJ1UgrHArPAMailzbQ_tHGZi91e9XLEoT7e33QXPgWkreneA_tANlhjlWZdVxzxaZilbWeT0oTG1Dt-GD_v3W5zXZyL7gGli_SL1FfsYB-OeRUVqbTCxAq0CJDOfFKcCOM-G_jfHzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dp48WfD_HSXVbAqbWFct3UYyAXLsx4mvQj9jVxidSHKj6S5LCK_Etqn0bG3xoQkt-b-SozQCaS3QUvqg32DeEpBNNwzRfuauHzZLLO7_G6RkQNfQ2yG61GoA5JCXLf1c72aOeLC4HiOwAe6LfMU903uGkByWP0LpDE-w5wNva78HeUK4-kUAEJJ6Yo0SHWfabrsyAgGhcS1cXn6UGaMg-n7Mrt7k5zgeedcXe6BHIl3N1Nw8NI9MLPVC6KcZmNcxU0cDvj0KXyhkO2jFJzeqEkWzVVvqjI4MamTLd4GsYdeUjQjUsUn9qk5gcf1YdnlznUm-aEVmorrmQf9IX99KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y97RSGPZWozEQdxBuxkBmeBMZ5iCBLaPyAEMT3UnC4v0tXpq-huGhjVFZ8PHjfmgQqvVdZwjdeG57G6mV0RNfpAKcXydR2LX8Tmp25OncFdr0Gb7CadApzXoRuTSgxxyqkAUc0OaIk0KymG2uic05P3y0WxeGxmFoh88J_zplggS9DHiVCqMdcNojjT74L8Xo90C-4fGOcKp5TmeHST3mlchurZTs8yo7eQdAelaw_AYFIXNbpcgKTytjMIZrwURMNICFFouhMTR4kkHbnaom-dYIuC0JVJ1rx8-95swwkFo86BJLqgyakhdo96_1awwmdSKkzQHrzD8LOzvPP5HAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/457884" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqVdC-unc_AGGOWj6lR2ciM-cfQDkT5rilUOAqD7tUBwMxpSP0bzJGkcaoLecR-4ExU9742Oz-RuplunqmyVRb9pXM61kzzaH2HidBw7T4w3h_WWCgh7Tr72wa-pu6grUYb5dG_kDHrLP9JJjF6Vrnuq_56DOXn6Mk7n2yhgPP5MMVpZuBfulA3-5yA6SHGPBO3wX4MbSbVGxJmOqFoAaeUhzwB1QJBfVy_VW7TlN49PucsSkZLHjEWuNSOsXZtmZadTWmMQRKGSs-lKLhSw82LaxiDFdCyC3ap7xNUNQXlHBCATNx9t_qT0C6hLX3kjmoqAozbe_3RcV-pN4uzTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3n4gRi10Lel_NU1KNP9cSb88KLdGyCF0cOY_c4YVyhgsP5_8X5yJQ3adqgkAAFPHkjlfjkSHTYljQzxTnyHjTI5tFIcbBMsVIQ7sQfFfq6d_xuZbdEaiWNOtbwLMEw8v3QG84grlu5IY1YJSMlKKBdwYUR5K26lk_Q1XdbKdJ6IhFLNzNNXSbN3ciWq4-q_WMCCdfUHnDWFkJzjSA_S58X3Jd6GDJefGEywXV7tJcJE6qxtw2GDYIZeWvKKEYKkg8g4hVUzCMDXD4PbY91XwnwDe4MLJLhJEfCR8L085DJiIuoT0NppEK55sSN6Den_g5oPhWCQYich0XiAkSpXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLfD7s0RS93AVsHOCXYYzO91KTHdXGIoBfaFhZTwvu1caOi8tN73kwTp7FTHeAYo_qZqRaTIfOoHV3oVieu_tVnX_elVnbJ1Do_9uKsCcQKCinGC5P6datQuQpVLC9v_R2qf3Le9NeOCygUq0z3Yyx1T9fSbI2JmsiXo3bbJaUvWT3Ir009uSHqGYw9mQaJXun8NcRafjKF-LxMvcSJQ_FZHsXvHXv-s7enBodhTD3q55ZO8YRfAyPJp3IJCb8FAMRB1s6sYN2Nt8iwtbo4pTNElJjHofnXPFUcwT4CRK4tvbPMRf4uxB3iD2IahMnDFKxl8f5As75tajHRok6EO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHIy4pSt6K7ftOq_nSbd__-ucPW4Z8GDXjEIdLYuyGDh5mjxJG7bCwC3vwAIVueB9wb61RzwT2e4RGvYKckHhgm7DwocVWcEg1gLanNBVwvzUfCTFJ33L7Tv5w4OoYtrcg9iyhsbsUWUKSDdzADcELY7aJnwuq16iH7LeVwh1soUU8-hbhWV9Sx9YUDGu4DhrSia1at6gG7gZ6putB_KGP-X5J0NwE3mDUpdGjlkCKRPOwIPIJcQpd7_dNYbE8issiLF0aQClQZED2LSfmzc6wbZRHtx5EVJhUOYeXg_orOFqpZfp0deLoNnjFcTVOX0GeK1PFJT15iYUMbljxx9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AX1K2OG57qqObH_NL5X7mNoM6m_ufY5w7owxUbEe-n2LKotW7GV54jbLRVThi_cwjY9EX4UWTWU3G7uENkKepS_ILmOGyRu5xzp3LZXgnqmwusOM-6Sze5WsvGxUzvuP9ICORfnzgUeS4K8UlKx-gv6rpms0uWpAXGxtRAbhwavJ4wmoQPLlzEWAxFgZUrhEmsbeXLz6QVWFaTg3u6kHIN8rAlG2dUjCDBEV764ziH5a61mP_vhtepQbfuMU7PWkPvMtlHkByXXLam9V2bm85ufqL6VmVyDaxDJalu1Skn07XhsTAfp4JiM-QegVlnrVxN3QT5hl8rDY2QVi0cRKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSL_K3ow5aYQCrIuA7PRTvzZZJ2amMQLF9MhOjs5nl-b0pCegOT9dw2uaM3-VP5d9sw8hnvipFoUiYZ5ODdZN3OzQ9FUVaWOG87Tm5Hiyeu7CaSf9R9QTcdZJjCXKl_4F7WbaWbY6Fps1v78DqX_sbaVP-RZ8ujbke8nbgC_RFt-PMVnOqUDRYupOe09uOSJSGWHETWPtsf_bhgnFtS1LvFEganvwZzOngDWmb11D4rfGsYPYYO8zwd9dZv0Ig2Wb_HqwR-OmAgWfo3F11PXiDTiFAG5d38GXaLuEVIO-ncimjv5sCOxX2zZN-aY0OrMV26dvBUv8FRO8FOFgEVclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIV8zwXikcNZ3ZKZ-p9ry7XuJdcbGhvYFRikmJbTaBVyzUn8w4Gjv1EoWM8IJcXviYM-aIQGNbllXjrwZRtzXcck6mwnliU_bnwiT6moYozHh77RokAeti1K7Lok3bbjGkAlLG93fU2jV1w9R_-CaPHKFe7RBBIYYi9R8grrWY6WWBMJsGeVOZL5wTTORyC24UdEzyqQYt_uhppssti7Xv80WNC0L8z6SF6MAT8wuAoye2-xgJp2d71JHp9bV4zAjxoanhPAdulKku-MvTSxrBvjpDQykQWDAgqzOYaCAzoZFzXJUqvdyRv2J2WuUHg5WyHh6Y-Ho3KC5z6i510r6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTUDNzB-RaTEr0ZrUUNS6x-uONDkfBzxo8H2qDkfe5AxNNVvwX7v4JOKSXMhKKRsl-fHzGzAXnXL4vFttXF7Xy13NxYVbWlqOFMlkQc-DKX8988QMuRlqSjNOesV7TvFkXwiNKVpHfMaB6lAXMpYxnID54bRUCRM9xm4QtUqD08Cq1-fFj3V8HGt3LNUfo9Q7Wa0-sW0JdCxiyF3uXL1owZJbOYbIf7hhVRtGg330ze6N8ECdcyKEyfGIfEnHV672RgyJ5UsyVP0zc88WI_GshFZukLhoSBOfFcsTwe_FES31z6qwUBN1y6DCGgjxGJeNhzk_qtB3hnBj2_O0ez5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzBhpYPmyd7j6kq-i5me5hSO-Ma-RvFBehxIdM4UNGNOOebjAOcMnTlKiwdvNEf1lsNVogueuv3SaS1xecFUyRrxR7e6jrE30TnmbF_RUe47acqWbwGujDU_KP49sMsffk6VMRLbMLykGY3lF5oPP9gz2PZwfs_Fkb08-nw5bJL3ZTzOd8Ukri8uC8pkx-BDUNXkKAEyPgIsZiss66P3lSn3Rofbsn4hNFnApLppyLIS4Ng5A0TwEK45PVX4QrxWeCAd9uWfRxhcTIDNqDZ866cpb9OXNgDWQ9FkifC6quGhWBhG0dyLEv5mswAiZP0-MQaQiPGMN8LXoVAq--otZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTnrWiZWkWQGk091tHAokALNTXaxuDUuAIeUxF3bxEzi7zj2wzpGYH2Rhjb68aS0IrrL8PMSyutcode2S8O7BTOxl8E_EIRuMJwWaCPSSyiQHJAEhwVgRE52NdYOnEWRyM25s-4NRgpvWpIAK8LiDAdfec0WQTqrIhZbAMMZthHvwMPF0hN87-7Rm-otKjblwELnrai-vIsbmCgGxxJ2yQScXdlhXRnuysV9vIY0xD7_1PwxBGxqLAE0dc99eiAm_rPiRSZxDHIxguuHwEbcgCQHqCknwpgU4_O-Yqx4l-gNJ2u7pTrc2n3MCcX5AVJ28yQWr4v8pgsNOrMvBMjQtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457874" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملۀ توپخانه‌ای اسرائیل به جنوب لبنان
🔹
خبرنگار المیادین در لبنان از حملۀ توپخانه‌ای رژیم صهیونیستی به اطراف تپه‌های علی الطاهر و شهرک المنصوری در جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457873" target="_blank">📅 01:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f837c1cec4.mp4?token=UuI-GNlwUJMl2fbbULoxwUJXpORnlDXYjfOiWeQgvuhK8Ji2erQMnixym2JngA2Y_3khyRGD0S71Z9iFP7kV4dcpUp4RHLB-GY4tGNSjWZIUv-MPtmoAcsprmgGkOtedceAurkkqiaploJFzySsIQdGLUvLDRVB3fMv01V8j6QECsndm719njcmS0kotvEgYvCPYTfafcJo6PmUihTVjVai1jZspXVJ7c9OBwFmzCHCEW0H3OR3TtvgiXgnX3Qit_ktDAvvPYVVNYZMXVnJlVAwHldpWF3uJLyS3Qngr6QDH0KSqS__xj-yLTst2K2BhmsUvpN4OnrLTCJjkjgchNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f837c1cec4.mp4?token=UuI-GNlwUJMl2fbbULoxwUJXpORnlDXYjfOiWeQgvuhK8Ji2erQMnixym2JngA2Y_3khyRGD0S71Z9iFP7kV4dcpUp4RHLB-GY4tGNSjWZIUv-MPtmoAcsprmgGkOtedceAurkkqiaploJFzySsIQdGLUvLDRVB3fMv01V8j6QECsndm719njcmS0kotvEgYvCPYTfafcJo6PmUihTVjVai1jZspXVJ7c9OBwFmzCHCEW0H3OR3TtvgiXgnX3Qit_ktDAvvPYVVNYZMXVnJlVAwHldpWF3uJLyS3Qngr6QDH0KSqS__xj-yLTst2K2BhmsUvpN4OnrLTCJjkjgchNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: فعلاً تغییری در کابینه نخواهیم داشت.
@Fsrsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/457872" target="_blank">📅 00:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd26757de.mp4?token=Da8Oo-PF6YCoJZEdGf028qhqBze7So2Baw7TGCNvFAUMjiikgUwmsg9lpCheBsMj5s7k1kZZnxl2Elw8-vP60Cxcc6ayWpA_woE6Vk5_i_hQnMb1EpswZXTErFRxY-5avI--oNemzbEMEc0TVBQDTy3wd-kMXwnm04qAZTzeEJswGzbVJGGVpcehEdYvkdH1SRAMfPGjen2Nzi_Okm-q9AH3MIg4IGKDnqxK1V2VK9PKyAanCxZSKySbBrJAhu2KdbobL-IZrMMuzj-QtqwTP1sKCFRxbFQ96pAUXpM2jIj6dDin1Fn6Okjbvf-SiyX8UMjXs8cu90ingyJaXIbTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd26757de.mp4?token=Da8Oo-PF6YCoJZEdGf028qhqBze7So2Baw7TGCNvFAUMjiikgUwmsg9lpCheBsMj5s7k1kZZnxl2Elw8-vP60Cxcc6ayWpA_woE6Vk5_i_hQnMb1EpswZXTErFRxY-5avI--oNemzbEMEc0TVBQDTy3wd-kMXwnm04qAZTzeEJswGzbVJGGVpcehEdYvkdH1SRAMfPGjen2Nzi_Okm-q9AH3MIg4IGKDnqxK1V2VK9PKyAanCxZSKySbBrJAhu2KdbobL-IZrMMuzj-QtqwTP1sKCFRxbFQ96pAUXpM2jIj6dDin1Fn6Okjbvf-SiyX8UMjXs8cu90ingyJaXIbTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقه‌ای که یار میدان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/457871" target="_blank">📅 00:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIi37ltUyyO9ynZorCLn_Fy_rggE1E3vn07IoGCC-m6hvzGmV7e_risgPVq3eVPPjhskqPaapJBBF2UZ_3bPqoFxfkaaJS0jFCYCnEAo07rM1wYm0_WN1gGIjtiYRS3jDTlbPHsRNUVu665F9_5fD6FgiMlWD8BUxwdN-MoW0XPcQqk14jRhlMSzA0udfP1E3TckePHkAefvbf7dQgxBPIqezczYnUNXfdtAou0rDCeejTPOj3d1NfP3MCAY0fBV-2mWefaX2IxJWDVIfhz64kQxxbKRLW37WUR0ucrDnS_ABN1LocCC02ZDNkD0AwyEKm3Q8AjttdOJSBNXkI984Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور چهره جنجالی در کنار استقلالی‌ها
🔹
‼️
در حاشیه دیدار استقلال و سپاهان یکی از مدیران سابق استقلال در ورزشگاه شهرقدس رویت شد.
⏺
فرشید سمیعی، مدیرعامل اسبق استقلال که قرارداد منتظر محمد در دوره مدیریت او به صورت یک‌طرفه فسخ شد و یکی از متهمان ردیف اول بسته شدن پنجره نقل‌وانتقالاتی آبی‌ها به شمار می‌رود، برای بازی با سپاهان در ورزشگاه شهرقدس حضور داشت و در پایان همراه علی تاجرنیا استادیوم را ترک کرد.
⏺
علی تاجرنیا پیش‌تر نام سمیعی را به عنوان یکی از گزینه های مدیرعاملی معرفی کرده بود که این مورد با مخالفت مواجه شد.
⏺
باید دید دلیل حضور فرشید سمیعی در کنار علی تاجرنیا که قطعا نمی‌تواند تصادفی باشد چه بوده و آیا سرپرست مدیرعاملی استقلال بعد از تلاش نافرجام برای مدیرعاملی سمیعی باز هم قصد دارد شانس خود را در این مورد آزمایش کند یا خیر.
@Sportfars</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/457870" target="_blank">📅 00:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0qVjuzzZGNEwwUZPM197CyLbdB0cqsOu7NlBJX2POjwjphSdaYFqn-2yfnPip6nblJMhKrlL9mkTNgohC9PlXtXMk58rNQ_xN4MzxDKKLXkzyVthOaArPo-Ri8FsuNGoJXf27eWZlgA_TKaP3aPjovagrsnNajdtkuJ2cvrJ1BfMontIlDaO8IYZpswXTbCr5CU5SRhvTP50px-CzIs34SWr42WxmxgCvTUcw7zN3uPx4SwK_6TTQa09OTj_MTuYRtfmBGnnTBEFEnTH-amYCOe_veVpUdcq83hDVeM132Bcoia4ljKxU-OvJhPkL-vs0GtuDPwFilrRYx-lEjxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHu3JtCdoCgQuJ3sL9fS0HTO6AoayPp3Ae6mle5gzv6HWkMNimT_VnVJ2XgWhvYxeywCtCu-imLrnH_NDzGPKbnNzt1S4GTktX-19vDqHLtY2606SZTRIgwELWG7dOS__GAZCCmFLPF0ivzoz2Wt8lj09bBJb9W2nOyvOvYnde6WbiHwaIpqSbtzPrLonWi0aMR3tc_yC_TKxbXYq5l8dvNUSjCegu-4cEG5AKZB9wMOvxgLLOGRWNA5CltKdu4sahJnm40cuvUiohNjh7yiltGoA5UU6i_3-SwjxagGZTwFSI67vRYwTziBy0y4y41FR9ZTAqHGmV44RNmpwQbf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pV20lYdgIkvfwQHZyWKVE3RTZJW90_Jq0iex0lxkZ8f9FBuqHNdCE7mFY_5J6LdMK_Z98eDTltJ5xMJC9xjvN3yUkz4q7tCK824T01NEE4YOd_wuInnT9vNqnJaldZKAjGfWuwybHAXq1YU2bCs65ChpiXFfZ21AZmvgCpWAKknEgsAJ0s-57WY1tFpOK61nIVwkEe3yxY4IWYRhwhVH6_Q7K0kRawFEVd3hWSBRGhsDeiZQym_YmsluLObNmtdot-MsPSx4-by0kOMQ0fROfr7Cic5E0Ua5XOW4rnHCIRZHMLvMcvnv7Z7qLQeaO4FkL-HLdZt5S9nFPlaMhH22RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlZuHQDDut-FJP0PvhGpn4-sRNphPfS5Uwl4UmmdMFjW0dLtVl8xslrSvQHZAbEJD4uRG3Azz8U8hChcByy90PCVJSxtILJfM3yuBY_pjz0eDJ20bTl8IE7dIqhVwM_Acy9OfYDRz99E8x-pVgUpAu5JoenefxJDKGh_cBz8kmfwCSXkPMNpn9-2JoiIP8W45Kixp2jDh4CESmhBUiR4b9Zl9vQXiCdkuwnd5Kfb3BKfjksKl2DW9YkpfbEywKMWYgP8Wl6cKO4Eem36t_zQwpNbrWxmReWXAvgl2bV_b5v6G-9CWEWbHPt-fx5BDAMUAnpJDoxIF5z1Nqsj0DjhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8thUrpzPWKJem-IMgGPPAjIlySivzi9tcG3R8yy0LiSBlrbr1vBfIY6l9BKVPvq1PxUvOD93_nCF8R22QIUKF344xy83VcP2i5foH77RRWb2EqLWZELFYv9T_ti2sOpR8IJEUa-Bwf765uapuWBwFfY-dMX_8szjnuEigxPrpVyAj7QVdAvfokVYIhz3_BAH2HZH_puL0sLkYyvvEniU2svUmaXhZDAaCtscsdor5ULpuem2-UnnLgKIpcvmdhKP7lOcugHoKqSvG6Otu3SuQ-uojSqp49vBoWRc3wQSlAiDjZKI8wIJzMjLz8zVrQrUnwwrevphmrklCv5zdJvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN4M98S7MZYLCaUr54rfvLX1tZEEE9cxdpxKHtt64tVx1R4vW6GfaJFFYSsOrKy8m70s_wkZkGAjgP5KsghcgT2Ndxhmz7VWtD9kgful9ifoyHSiSFpju1Qln2oQFNrbiCl9ViaDPvgR9mG3Y0S8SN6NaCyLNIt-Qwt_f7B9RWzEaVkqw0m7ufU0aaNGVIoIg2HGlK98eBsYbEGpmz_Sx1nBAt8_y-ae8XDIWfQ0axHxfh3olSJ9JBSnFeSZ3cHE8j1v__j07KyE8b-evHS5qOOFdsaZs9hhGEgmM85ulv3o2F1cSG6NKMzJFlpUzkSG0dI1SE4Otn7hKSL5ED_MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9fGyGPKaMI5Wj9ZwqITaYldwZVnUoA0ZBAkmZfq4Q52O3aDuG2H8jC92hQ7CmBRU6-xzhFr3nphw5fibOjYPfRODOtj3kXb4VJfCXN-mEZ2nZnwO195bihPZDV8_WGOvKVEbK3R9xCxnVmivYqlArkQEpfAo4HiRqCO9NyIzqL9thbSv1RutS9FvnaRBr1591OKBakfPi5uvHQ1_rcl6TYIY08OOxmF5Wz3ey-2ytT_A_ZMU8WANk6-p9o7rBwoFX5gdVbYApYPe8WjKqmKQNWXaD0tjPbXSBdZEYKiqFU3N9H94DfUtgLL1WvNPHDZpLxo8-8G1iQ5PnFkCgOwsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازی شمس‌آذر و آلومینیوم اراک در قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/457863" target="_blank">📅 00:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af406c72a.mp4?token=fhiFjUH-4BCSvVUAOycQBSVfzHOg00C6I1SoSQSLDpk9eN6vvQtOqUoGnPPqVI5QHvE3x90JMTak-t-ge1h9y7BPn_nfdrLM0dHkgtLB4exqfM8P-O5_ZBDYzMV8-dxneRYChbndezrmGvjY3iZyDXAz1GawrMtmguJLO9eAt5j52MApc0ICfVXyJiQFmsQRHcBiXON--63yJu91WA0wr-mdA57Q5t8eOw5LSKOtAVz1ditqKI0nPR0TOPv92wzKRqdNCaMiZXn3bxa0Pbx5x2CTVJg09Zerrpx9-6w7LRJeGTE4Gb-FZU5q3GrpjVoKQEzdez7ghi9wrUdzatYmmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af406c72a.mp4?token=fhiFjUH-4BCSvVUAOycQBSVfzHOg00C6I1SoSQSLDpk9eN6vvQtOqUoGnPPqVI5QHvE3x90JMTak-t-ge1h9y7BPn_nfdrLM0dHkgtLB4exqfM8P-O5_ZBDYzMV8-dxneRYChbndezrmGvjY3iZyDXAz1GawrMtmguJLO9eAt5j52MApc0ICfVXyJiQFmsQRHcBiXON--63yJu91WA0wr-mdA57Q5t8eOw5LSKOtAVz1ditqKI0nPR0TOPv92wzKRqdNCaMiZXn3bxa0Pbx5x2CTVJg09Zerrpx9-6w7LRJeGTE4Gb-FZU5q3GrpjVoKQEzdez7ghi9wrUdzatYmmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بوشهر: با عشق رهبر زنده‌ایم، تا زنده‌ایم رزمنده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457862" target="_blank">📅 00:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74bf93ac1b.mp4?token=oaJr5zOnh__Uybwm7gpYWyn0ZSJix6214eVsDRcZ5MkD8oUX9mOXtVvc8xJhIJY_m6FxLJDfTvOzLEC15yNR4gMb2vTI2W-1ltig_0S85wysiDeegeuDC92Scw-BGNQXBp04PzMpUGN6_LkxLhvQTVVGMrJA2RlgbHFBgKvVU7lCKerVZzo_S45NaefI-MKFSbWHlK91iGWfi0Lr0Euf8sFSBr4p9Vv48eMKlIJJamEMqM8vTqtlQYQgrAoTA6YZ_7qkoo3JIee3u84PL9VouHS1llJTUAf5gbCveRufAkXfklx8E6Dew5Y1oxjX8l_Ny9ZAvX4UGIq98hPNFX95PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74bf93ac1b.mp4?token=oaJr5zOnh__Uybwm7gpYWyn0ZSJix6214eVsDRcZ5MkD8oUX9mOXtVvc8xJhIJY_m6FxLJDfTvOzLEC15yNR4gMb2vTI2W-1ltig_0S85wysiDeegeuDC92Scw-BGNQXBp04PzMpUGN6_LkxLhvQTVVGMrJA2RlgbHFBgKvVU7lCKerVZzo_S45NaefI-MKFSbWHlK91iGWfi0Lr0Euf8sFSBr4p9Vv48eMKlIJJamEMqM8vTqtlQYQgrAoTA6YZ_7qkoo3JIee3u84PL9VouHS1llJTUAf5gbCveRufAkXfklx8E6Dew5Y1oxjX8l_Ny9ZAvX4UGIq98hPNFX95PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، ‌تحلیلگر مسائل استراتژیک: حتی در محاصره می‌توانیم نفت بفروشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/457861" target="_blank">📅 00:05 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
