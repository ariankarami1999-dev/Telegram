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
<img src="https://cdn4.telesco.pe/file/ZSAIG-h_J2S3tTNbgwosEErXXw59NflU7ocrUYpJ2_WPRoYSwwjhq7ek6vz2BqsIgkXCRtfj9SzMWqT17R3oiZGfazSq5yAHah9EVjFfcHqzqBvI7nCcZUlDw0W96-drU1_dioWZwzBZ88-q0dhhU-ZbweCwMkjkpcTbl6Sj8Tz0CEl8Y_WeU__uC0lFo9_zyqiPFcNnwLlbXct6UmZfetLCXvvGvfTXG8EaQEXY7iMwBZapukrQWZyoE8q2XS2Qf3AVkdchU_kuzVzELnixtluAX7GEJDV_7NIZbDzSOmnN4UJScGUZt_BvSTwCORvNq557UViWDLw4Zr9UZLn2Tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=jecmGUBr1sPp12rp8-ArKzZ0Hd3rTWAw1mHkWs_qKdyp5HNrlaqmJ5P0qvvpr67PUtgPErNy4YNefH9rM-EHjD3Zsv3k_NexVMG22IalcmhQN0bCrXb341TtdBkMeaslJqcdm0hYlsK94DNGZTm6iha48KTtN9Gtdjfcv5IPBhogsxcWKLCaa3tIbbOMOh76GxOKyAY1EwwaOgqKJGMuwFeMUffaNglQyTm2GwTINo9in6pk9CqPlCLUBq3VjYVwYzwhJsOwA49mlqbSdyhKwHvOAUKAZRig42FpMtMDDdegxEFTTf17BzLMAkAWlFlBfiVF56zJxR-VDfI_TKN7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=jecmGUBr1sPp12rp8-ArKzZ0Hd3rTWAw1mHkWs_qKdyp5HNrlaqmJ5P0qvvpr67PUtgPErNy4YNefH9rM-EHjD3Zsv3k_NexVMG22IalcmhQN0bCrXb341TtdBkMeaslJqcdm0hYlsK94DNGZTm6iha48KTtN9Gtdjfcv5IPBhogsxcWKLCaa3tIbbOMOh76GxOKyAY1EwwaOgqKJGMuwFeMUffaNglQyTm2GwTINo9in6pk9CqPlCLUBq3VjYVwYzwhJsOwA49mlqbSdyhKwHvOAUKAZRig42FpMtMDDdegxEFTTf17BzLMAkAWlFlBfiVF56zJxR-VDfI_TKN7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت دارد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=qXzRLiALUPXNTTwYRPNRm6zec4HQ4hf6D9JRqrYhSxYxBintpbqEDSiF0DkTFuWF61l5ZOGIZ7zn0aWEnOGjkmsrGtxwkrSc_sfPRl6wbEQ5OAD0B4QxjDQ7Tw7rCJfvO6kPvwmd9-STtA-DfaiVPnT74ugn5ud5Wg10NYf4UIpsCfExu7EfKyNC8u7Bd5TJd0QmjulRl2U2Qtt0xuAcx0vtALYaF42yapf2ZiQx12ZKo72VyhWjyoCndkfvw639uwiF4Mbfxou4CFZsDfkSBv4tu04qizPWf3fLW6Vqv-X1S77HFqLQqaVN4V-TNo3BBdA7TRPFsgAZWiY0BPboJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=qXzRLiALUPXNTTwYRPNRm6zec4HQ4hf6D9JRqrYhSxYxBintpbqEDSiF0DkTFuWF61l5ZOGIZ7zn0aWEnOGjkmsrGtxwkrSc_sfPRl6wbEQ5OAD0B4QxjDQ7Tw7rCJfvO6kPvwmd9-STtA-DfaiVPnT74ugn5ud5Wg10NYf4UIpsCfExu7EfKyNC8u7Bd5TJd0QmjulRl2U2Qtt0xuAcx0vtALYaF42yapf2ZiQx12ZKo72VyhWjyoCndkfvw639uwiF4Mbfxou4CFZsDfkSBv4tu04qizPWf3fLW6Vqv-X1S77HFqLQqaVN4V-TNo3BBdA7TRPFsgAZWiY0BPboJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=fk-smHdSeeP3y4wpcZ0Q245pWVI0EuwgdMFB-SJGSGtGFGUe0yU4-bpEJ15fQCX90ff0Wc-cCCi8PKaFPau0Ng43zvs3OdT4CyjKrmiKPuCzsNoIGDewdjwkxnM08eK68V5J4FjZPze8s3ywZKUD0m2vNuc7yt5U4P24iOr7Q1c-Syk19nOQM26AxFvsKMmz6nDhiD42OzJr9cczfTAtWQ3EKZQNENifcu5HBLLJOw1JUqn_PZRootVRezQBn0aDBvuzRNIE7IsLCwGrk21ZWFAeKoG0eTo8s89BMfhM_KWRkSnAmIJ38LHzxIm7muQDZy_-dammSTrbAvOniGuZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=fk-smHdSeeP3y4wpcZ0Q245pWVI0EuwgdMFB-SJGSGtGFGUe0yU4-bpEJ15fQCX90ff0Wc-cCCi8PKaFPau0Ng43zvs3OdT4CyjKrmiKPuCzsNoIGDewdjwkxnM08eK68V5J4FjZPze8s3ywZKUD0m2vNuc7yt5U4P24iOr7Q1c-Syk19nOQM26AxFvsKMmz6nDhiD42OzJr9cczfTAtWQ3EKZQNENifcu5HBLLJOw1JUqn_PZRootVRezQBn0aDBvuzRNIE7IsLCwGrk21ZWFAeKoG0eTo8s89BMfhM_KWRkSnAmIJ38LHzxIm7muQDZy_-dammSTrbAvOniGuZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=E56I7jbPGe5mE2Qhau2_CTWi_ri8DDf9Fpc2PApmr4ofS7cu83J-Z9g842v04tKRnWIVHevqXbNhZievqEwtP-4sr0Efc9UaITtoyL4nw4rudEuUFAc4Lmt6hWIijHsqmfvcwq0t48h1KydbhsR8R3KgcbZMqaLR_Zmjq9MzikvVxx-sd_DiuRRgM-KcaW26SSvpKU6aPOEm6EUImlXcjKTvM4uFljhkQpHdWHa_RLQUOSxiizcqiUEXtJZ3FpZO7J5U0sB1YXHGgzGKiTFALsCpknDWRLQs-c7EK0aIr-_CuSn5n3lMWyxvkJ1EXyBmgNyvnaA-2f9jLnse13gxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=E56I7jbPGe5mE2Qhau2_CTWi_ri8DDf9Fpc2PApmr4ofS7cu83J-Z9g842v04tKRnWIVHevqXbNhZievqEwtP-4sr0Efc9UaITtoyL4nw4rudEuUFAc4Lmt6hWIijHsqmfvcwq0t48h1KydbhsR8R3KgcbZMqaLR_Zmjq9MzikvVxx-sd_DiuRRgM-KcaW26SSvpKU6aPOEm6EUImlXcjKTvM4uFljhkQpHdWHa_RLQUOSxiizcqiUEXtJZ3FpZO7J5U0sB1YXHGgzGKiTFALsCpknDWRLQs-c7EK0aIr-_CuSn5n3lMWyxvkJ1EXyBmgNyvnaA-2f9jLnse13gxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=tIypavevWZjZrDiwVRYk0Dn2hlW-IZD3Rk06hPhDwhowJzzzLS_LvSbpCLgPRcxRKEmrzDL6CeDMm0M0g1v8qSs5EkINB-WLjczwBAgfN4sbt67YiNguwr1lvyT7eOulCoEaI2DxWOxK9vgYRBWFRJ7csZBaorKpHp-3RjEksVM2pJi5KxkNJuUGmSxJ9ZZYHJj-QM4MEI-t3lmtFYw2bzAllnAZsLOeU55aw2HaWoNobew3BS3OYUfP_mSE73ZytuRKqkLWm12C_JNp1d29vX8kJ0fHWTIQiczlQtI-Ts54tJday-zRh1j0FtK_XnjWJjSfL-by8xgtnKM_vUpzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=tIypavevWZjZrDiwVRYk0Dn2hlW-IZD3Rk06hPhDwhowJzzzLS_LvSbpCLgPRcxRKEmrzDL6CeDMm0M0g1v8qSs5EkINB-WLjczwBAgfN4sbt67YiNguwr1lvyT7eOulCoEaI2DxWOxK9vgYRBWFRJ7csZBaorKpHp-3RjEksVM2pJi5KxkNJuUGmSxJ9ZZYHJj-QM4MEI-t3lmtFYw2bzAllnAZsLOeU55aw2HaWoNobew3BS3OYUfP_mSE73ZytuRKqkLWm12C_JNp1d29vX8kJ0fHWTIQiczlQtI-Ts54tJday-zRh1j0FtK_XnjWJjSfL-by8xgtnKM_vUpzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK7oDUDR0Lg57fvSypTz4XtISIJZ7giIkFSvZCNXulBSgefQUmLBiq462Mvo4gyy5apAeRk1BAbAQHOlTs85y5sYwnV1YjtWFS8XDvpMy0WyulwZZ3KGUHYSUWD9ii7tFyjyfYBJ79xtUlO758sA99zX2xms1L_922SCaxIQxB5xb16oliO0sj2EdMVJILnCEpmgxmmnuG3OaWkjNIuF4W7s99NE82RooNum-pnJUpB6YSrgAdeftwQXG78Z3T9yVpvekm74ihYsq2jVTM_uJprvFb3-ca8P22bnkmotbTFR9R0lc_j6WAuHAn1jCBxheDFxnx5ACcreWxWyDuCong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhOhRsIONcHbhyDqQg_lJtnYluf6dlG2a0SPTZnrTnBNuphUJq6FxEYDmTuPsk5ODjyD70mD3orZtdw8zjKwLCGetg-X_sv2Gnzgk0_GchpK84Zf4itRWZMBi597cfJ_ggXj_JcopWXgHNtjqT8aLofylcnCsX9AObKlUSCpvYgslL7D7Ad3h2UCj_aZB5n7Y-7zdDgA2lWEKCuKDjBrNDmxbB7By3sNl7w5H4DWTXkf4CO4MpyUpgkSdBP5n-I4ZmJBsTjMeptNZE2BijPb4gyNlczlX9rSv6sCP2VMQAWAcGhHTZzGzwqYtCJQoFpRTwXG-tcE-qKXsTLsn3y9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=cWFlJBoUTbl8CoVLQZMTzN9jDlgeXBRHdDY8a2TeVKSrQCuH5emqFnG8oks_kHVXBIBDery4tXni-Y-oYEkcmBdqikAGe72ujHOdFhimuJaDRCSnnQZsrZ0vH2wnD32ouSn361UR_VdxaCWLH-z3tGCWLWULyPj07auG33Suom1HCZN8MvCJjqAuY8Vg6t9WmPD643VeeyxPb-EH2wLfJVEZKwY7LZgBvEJI6ah1nijE1CMUJlB2v3hVx5vMAz1Uo_hGnIdjhzW56tFLLKIPn8LOWH34ednDxwSRB8unj2f8XDo6B_piNuUNWFZQrxEibvQMqI9xiAIgi7K6g48S6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=cWFlJBoUTbl8CoVLQZMTzN9jDlgeXBRHdDY8a2TeVKSrQCuH5emqFnG8oks_kHVXBIBDery4tXni-Y-oYEkcmBdqikAGe72ujHOdFhimuJaDRCSnnQZsrZ0vH2wnD32ouSn361UR_VdxaCWLH-z3tGCWLWULyPj07auG33Suom1HCZN8MvCJjqAuY8Vg6t9WmPD643VeeyxPb-EH2wLfJVEZKwY7LZgBvEJI6ah1nijE1CMUJlB2v3hVx5vMAz1Uo_hGnIdjhzW56tFLLKIPn8LOWH34ednDxwSRB8unj2f8XDo6B_piNuUNWFZQrxEibvQMqI9xiAIgi7K6g48S6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=LgGcfeQiLHvdz5OFP0I1BXIbHetkxWsFL2LNKAozFKBiM1M56kfhLBR_OQD6-nBWaJhe7S7v3_r0QqGXjh7cavqOwHzBo9EALUDJtMre8Hs2Z3FPt_Ux6u4u-HtzgqxO5FEgKePYNcUcpKds3Ejbq5WP2fR3Kj7ldttPBeM3ELhUZxcqdAq569EoNOfw78LyFQlNFSEutCzhxLJzL333WP91yEqRgLl2y7AR_ILQVFHfpIlv0K884XTHR8e6zy7iUalWgssUeAIczje6LRM72GKcjwDgJ6j8_A5F-RBRXw3qWSyo4DYT92qo9XF3NBQffayAEzlgqa-oZYzlnBds8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=LgGcfeQiLHvdz5OFP0I1BXIbHetkxWsFL2LNKAozFKBiM1M56kfhLBR_OQD6-nBWaJhe7S7v3_r0QqGXjh7cavqOwHzBo9EALUDJtMre8Hs2Z3FPt_Ux6u4u-HtzgqxO5FEgKePYNcUcpKds3Ejbq5WP2fR3Kj7ldttPBeM3ELhUZxcqdAq569EoNOfw78LyFQlNFSEutCzhxLJzL333WP91yEqRgLl2y7AR_ILQVFHfpIlv0K884XTHR8e6zy7iUalWgssUeAIczje6LRM72GKcjwDgJ6j8_A5F-RBRXw3qWSyo4DYT92qo9XF3NBQffayAEzlgqa-oZYzlnBds8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=cfRIO6_1JNvS1BT-nCcfykWqfQAhS--uhvzqpK1aQ_Wx2n4pMLEOE5vvWHXwkIKaM9VULuGYrYsijyVbtsIKVKWeTiRQKf1NOOAQbxxRDoYgeRHEZ_WllooUq9ixIt9oaeE82UfYdyMt9NO1tGYfRrhbs-lwbNJ4zcddwZULFwQb8rVgK1KffV3It_r730pg3-N5ZVB3R0EPGXS2eHjtFy2osmjB5MUUGg9hDT90qjnwzf_lR-El2Vj1GeSNBesnBMk7iyAu4pFqNYi-MAIoAMaR42wMrwkeQ8Q0JYH1ndXH-icapi1KbLjR7POHGAKzYgrRtIr0uvU7X8Asx0WisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=cfRIO6_1JNvS1BT-nCcfykWqfQAhS--uhvzqpK1aQ_Wx2n4pMLEOE5vvWHXwkIKaM9VULuGYrYsijyVbtsIKVKWeTiRQKf1NOOAQbxxRDoYgeRHEZ_WllooUq9ixIt9oaeE82UfYdyMt9NO1tGYfRrhbs-lwbNJ4zcddwZULFwQb8rVgK1KffV3It_r730pg3-N5ZVB3R0EPGXS2eHjtFy2osmjB5MUUGg9hDT90qjnwzf_lR-El2Vj1GeSNBesnBMk7iyAu4pFqNYi-MAIoAMaR42wMrwkeQ8Q0JYH1ndXH-icapi1KbLjR7POHGAKzYgrRtIr0uvU7X8Asx0WisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iar1tRk7tD_a84D3gi84L7EHija-OWAtjxLuCwtPpHwdTpw8BqyxUNFtSlHTnrX-5E40SDU1HZ9spjcLbOKvfkaGsfmfo5TdNNwAWBQeImZ0w_vi3RYypztEj3xpSjjMoFkVk96g8Twm8aOQ45xFqPBXyY3cS51Qy42X7nOB6vJhVjUdrLC6A7dnRg7oIlXLpncxy_4UR-rt84wUKD1OnczwFTHFiUFYjgi1GppStIiagc4zd3NI2c2VrOk4qP3PFMz5gWXz2FpA_CIoEN3CPuyUOurJWX2l_QILhGRUdb3TMZfLyfpFJv4c676cFiPMEGsGT0slk0fM89djUBobjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iar1tRk7tD_a84D3gi84L7EHija-OWAtjxLuCwtPpHwdTpw8BqyxUNFtSlHTnrX-5E40SDU1HZ9spjcLbOKvfkaGsfmfo5TdNNwAWBQeImZ0w_vi3RYypztEj3xpSjjMoFkVk96g8Twm8aOQ45xFqPBXyY3cS51Qy42X7nOB6vJhVjUdrLC6A7dnRg7oIlXLpncxy_4UR-rt84wUKD1OnczwFTHFiUFYjgi1GppStIiagc4zd3NI2c2VrOk4qP3PFMz5gWXz2FpA_CIoEN3CPuyUOurJWX2l_QILhGRUdb3TMZfLyfpFJv4c676cFiPMEGsGT0slk0fM89djUBobjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=CZ9FGBg4kRpd_yISlAPm0v0QR77teugvLag1b0KAjincA3sKi9idxe_BFchA4FzJ9b9Gi49FR1pToTZ6WWKsA_OQJS0sAnTqdcOvbtUiqdbWKSoFsuQZkg2guskDgQrZ1sM2xuqvosGe_Pt426S071QpOhsX9cZ2GdUu6EmqGmcKUJVy2S1hYF7u5aZ-FeebemMK6Ujp_Kqk2ldB5UHf2A-bljdpxwdVJLZ6vmOBdJ3FfahSoeeKOWwY8RiItpMu9Bi6SHPRp_73PpN_LulC7NmuEt5i3kMoKpUjRn9aWja0f95XHkpmscyUd8cA4pvrufajMe0kWb-T1vL5yqJzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=CZ9FGBg4kRpd_yISlAPm0v0QR77teugvLag1b0KAjincA3sKi9idxe_BFchA4FzJ9b9Gi49FR1pToTZ6WWKsA_OQJS0sAnTqdcOvbtUiqdbWKSoFsuQZkg2guskDgQrZ1sM2xuqvosGe_Pt426S071QpOhsX9cZ2GdUu6EmqGmcKUJVy2S1hYF7u5aZ-FeebemMK6Ujp_Kqk2ldB5UHf2A-bljdpxwdVJLZ6vmOBdJ3FfahSoeeKOWwY8RiItpMu9Bi6SHPRp_73PpN_LulC7NmuEt5i3kMoKpUjRn9aWja0f95XHkpmscyUd8cA4pvrufajMe0kWb-T1vL5yqJzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE0OHhW8_itQJ5WSxR4V7olvBOWq7sku851seNbe-hWQoJMp-cUHJgstiS9YGqlN1lVlpYggOv7gqHSQJvK8fvlajXajM6H3DrDxPopASJmiiJMlVQ0KlSMvyLb1lziMAzMgCvXvLC_nxhwcPnYAf1HYGpRzrlKadDGIOrPtxKjCwPloms5UJ7gA5C5CVeMhQuiuqzh82DxZQM2YXe_H9uq_OfgiQEYOrFT53N69uUTk6VwmB6qAO1DiBiGLq49foExJvbW1G0NbiYf37Tx576xlIUGkIYMF6VocBM3M6VlFuqETx4y8xrN4epWKBdCUeMbcyxOIXuTD7u4oC3vcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A4Is3Hd7kQ4tev5IM0ME0Eq-45kh2UNmWXHopOkSJadKlcnFOeGDtJiuIBWWI12e13Zp4y7DHBuSoX8bL_1u2Y77VPJvuUio7Zbm8ROuWa4wtOPo440FUHusWTEVh3fQuxhp5clHF6652bjGJzifPnTadExe1oSVLVIOhvU8E0zTL7bxTdAFCaDs9_kRbi6hMh24ward6fn-VcNOI7dv6A7NXrX0CpiLalHPc0Vo8NUpj4vhmKvUpQyhL3-VJ0_DpCT-VxYE2KQpq5U4uJl_UXxnLOoE0TrhCqZi78ISijYrymZtvUDwL52i4yDARRaCJdLbRtDw-sunDwVQ26W3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A4Is3Hd7kQ4tev5IM0ME0Eq-45kh2UNmWXHopOkSJadKlcnFOeGDtJiuIBWWI12e13Zp4y7DHBuSoX8bL_1u2Y77VPJvuUio7Zbm8ROuWa4wtOPo440FUHusWTEVh3fQuxhp5clHF6652bjGJzifPnTadExe1oSVLVIOhvU8E0zTL7bxTdAFCaDs9_kRbi6hMh24ward6fn-VcNOI7dv6A7NXrX0CpiLalHPc0Vo8NUpj4vhmKvUpQyhL3-VJ0_DpCT-VxYE2KQpq5U4uJl_UXxnLOoE0TrhCqZi78ISijYrymZtvUDwL52i4yDARRaCJdLbRtDw-sunDwVQ26W3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ZqFWbwv5_z-MOZEJxqbXK_F8HOcxQkW0h8VMpthTJkrAStVK1Yip6KqAbK_h37W8PB-VVABNaf4PPRSbZUN0Ob6Jz66TWXnh-FvPrCMA9qnznZ3jHxn-KIER6fQrXHBeJv8zilq1fnqxKcd2w_vD6jm8-deVeMPVBYV2FvM-sR0lbIKMmjBSwjzgJuD0XncBNGbo7FBQ9vrcoyp1X5FRjW5At08e_wQU1JvQuKFwcUapHK3kxRuLZFrcGXddcPVl0Us95Mrb_8xah-mqma1UqSSo8fTD8qaKFQKpUMnmSvEEh46_00-xQ7F0GagM9uN0Mu6Gzb0OhLvvgag-KVUJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ZqFWbwv5_z-MOZEJxqbXK_F8HOcxQkW0h8VMpthTJkrAStVK1Yip6KqAbK_h37W8PB-VVABNaf4PPRSbZUN0Ob6Jz66TWXnh-FvPrCMA9qnznZ3jHxn-KIER6fQrXHBeJv8zilq1fnqxKcd2w_vD6jm8-deVeMPVBYV2FvM-sR0lbIKMmjBSwjzgJuD0XncBNGbo7FBQ9vrcoyp1X5FRjW5At08e_wQU1JvQuKFwcUapHK3kxRuLZFrcGXddcPVl0Us95Mrb_8xah-mqma1UqSSo8fTD8qaKFQKpUMnmSvEEh46_00-xQ7F0GagM9uN0Mu6Gzb0OhLvvgag-KVUJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ede_saILdwlM-L64jRh6-GHzBDaW97_fZtNvCIc3efmBj2GvdizTebkECygLlPd5Ly17NWaMFnvwMXW9sSAVbGkzMJqrz-OjOlhdGj3UC36DY4F4i_eGcR7HJ8sFCevLGgZuTpN4Ee632Mk9o3O0c9mvNh72783fVB9Xr2B2ONXLKw0qcaQ6udfcfFuHvcmct3bdOwUj2DmwOv7CMceAriy1zxMU1_iMlPpi8W2DWPlQovE54gxnxAzOc2Ejg_OmBa-WcZ0vroh5fkhHCixQsG3U270c-5KePCVUC3_PDwIMd0QwGw8b8IebJjGAoNUYBOyUk85felLDC0QPl8rIhxaEKmZBWS4XYwLrDd9w-oJ0VteYq_yA0JG0b1K3kXmb122aHaFl59lHsfczfSJlNYSukWfvZTryDG7NnJYbsnXly2-oqQZTxcQrLOYDFRgcmUgtSqT9d7Pd2S-2MbrvoeNSwuok3854BFYSRpnsbQwHZlypwP-ADBHLd83yyFTsU-NK_y-6APGsgRn1YkYOi_wSBb3iSh0fjesyXZ9LnMIUFRZQJiWqE3D_o-oXmozFQS3a3YQwaqT2iclGLsG1r4KHK8avew9F2YyzMYGNtgaPfV00ybrhzvEKF8jW_3LopuoVtsiCZay7CLaawrY0kDxhiVho4YLRvUK2bjsimoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ede_saILdwlM-L64jRh6-GHzBDaW97_fZtNvCIc3efmBj2GvdizTebkECygLlPd5Ly17NWaMFnvwMXW9sSAVbGkzMJqrz-OjOlhdGj3UC36DY4F4i_eGcR7HJ8sFCevLGgZuTpN4Ee632Mk9o3O0c9mvNh72783fVB9Xr2B2ONXLKw0qcaQ6udfcfFuHvcmct3bdOwUj2DmwOv7CMceAriy1zxMU1_iMlPpi8W2DWPlQovE54gxnxAzOc2Ejg_OmBa-WcZ0vroh5fkhHCixQsG3U270c-5KePCVUC3_PDwIMd0QwGw8b8IebJjGAoNUYBOyUk85felLDC0QPl8rIhxaEKmZBWS4XYwLrDd9w-oJ0VteYq_yA0JG0b1K3kXmb122aHaFl59lHsfczfSJlNYSukWfvZTryDG7NnJYbsnXly2-oqQZTxcQrLOYDFRgcmUgtSqT9d7Pd2S-2MbrvoeNSwuok3854BFYSRpnsbQwHZlypwP-ADBHLd83yyFTsU-NK_y-6APGsgRn1YkYOi_wSBb3iSh0fjesyXZ9LnMIUFRZQJiWqE3D_o-oXmozFQS3a3YQwaqT2iclGLsG1r4KHK8avew9F2YyzMYGNtgaPfV00ybrhzvEKF8jW_3LopuoVtsiCZay7CLaawrY0kDxhiVho4YLRvUK2bjsimoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Sav3tXAEbmqFWcmxAJ3pJRxIl-lhChO4LVYb1ILSErdwSjG1XD-bOuytFB6uaQFgFu_2BuNU2gnUeXYl5XU_cs1MtrLrSdP-XpaN3nnrrmY9EKrJm9d_X29cj69nUOKT2vTWPfhaSYaqYsJQzqu4ax05_O9Zos6wFQPpCvPdL85iXe6lmhdE2hQ-oF6_4tMB7dKnRzIGFKny4ciRle1OK9JPvOoOgwjJVhyduq9l5u0DNRwtaRFzEs70W4IJd-82jbM580Er33nFzpXIjGaVmzsbR5wOrPXjXJB6ox14qEQ9qCakTylOIJK7d6rDbi9onyNwFg0GPrZEce-arq1tAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Sav3tXAEbmqFWcmxAJ3pJRxIl-lhChO4LVYb1ILSErdwSjG1XD-bOuytFB6uaQFgFu_2BuNU2gnUeXYl5XU_cs1MtrLrSdP-XpaN3nnrrmY9EKrJm9d_X29cj69nUOKT2vTWPfhaSYaqYsJQzqu4ax05_O9Zos6wFQPpCvPdL85iXe6lmhdE2hQ-oF6_4tMB7dKnRzIGFKny4ciRle1OK9JPvOoOgwjJVhyduq9l5u0DNRwtaRFzEs70W4IJd-82jbM580Er33nFzpXIjGaVmzsbR5wOrPXjXJB6ox14qEQ9qCakTylOIJK7d6rDbi9onyNwFg0GPrZEce-arq1tAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=O9-tYqa6wuGnjLg52-MRGjWPFXMryame_--HBKgjHyWufs9XTgGWgklEHmjhmXSxdQTfInHh5F_TPHEoELBXsWgh5eXcKuxKkTEb7BqQCpGVvhTzPEAvUypnqBaG7_hryhYgSS3LmzdvIFt-mXKH2cGm_N9pnXjz095zf8MZ_Lx2xk99wAPR7DOAJWXxVgyPaEDEVZmF8zabkZZJypEQKbiKTzgzyiImr-R-VRsePsovZ1FL2fiJVi2B6b3fWR4a-O2v0yDdhvmlkF9WU9ofamgjg_bV0Sh_t8DIv7hI3TFjAu0QCb30oAoBK2iom0S45fYuLSaN3b73L6u0sY9L1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=O9-tYqa6wuGnjLg52-MRGjWPFXMryame_--HBKgjHyWufs9XTgGWgklEHmjhmXSxdQTfInHh5F_TPHEoELBXsWgh5eXcKuxKkTEb7BqQCpGVvhTzPEAvUypnqBaG7_hryhYgSS3LmzdvIFt-mXKH2cGm_N9pnXjz095zf8MZ_Lx2xk99wAPR7DOAJWXxVgyPaEDEVZmF8zabkZZJypEQKbiKTzgzyiImr-R-VRsePsovZ1FL2fiJVi2B6b3fWR4a-O2v0yDdhvmlkF9WU9ofamgjg_bV0Sh_t8DIv7hI3TFjAu0QCb30oAoBK2iom0S45fYuLSaN3b73L6u0sY9L1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diP48_VgHtC9yXN3lDrULXs9-O88Co1nAa77uFqYu5nqAk-xI5RN21PssITOZ0LYMIYjxLNAeizoKR_Z1OJJu3Zo-uvmoLRS4_L4qYCiRUg8Bn-TlYY0-4skBjUgUnTsYL8Jsldno9_UVeHfLLVFMWfXusgNUr2ZXhvWzrNpHvc8kO7Pcks_QRQIt46D6gTOM3EFt11qhYAHA2PpoIno2sCAD60I3z8mTayBfPwwj6S4EXyJoDbZa2T1jGJlsaHwLUbUXHD7wJFbJdm0D3qGh9FyvuqoyvjFO56Cn_tLzCXadbACGZfiS0lJ2rJP5fY3xWtmV3qjs9jFTM2AVdrK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMWBrCuTGLUFMeUYrA94fxb4RCZKC-i6w_uPDcclBBX7MUQqd7nmFCCk6cHgo72P5jHaxr4kWkvBc6k6LfnyulQ2KEkJoR2EJIM6Vy6fdamx65hNzh0G13odl-J6MSCa7ZivYkdFjCCQxbVLuzjVaTv_rG6SNycb_b6RyX9RUCZ1zXAcC1PQPxKNFH6sjmCPmQyJv1lRT77R92L0zLsv_nck5a559b8NF7oD7JNC4Ufs96eMV1dRz-EzNav-iPmK54riCFRFcQJeyByjvokrOLDcvIP0XwNndxpkCXoZh0wsmaJDdmOV6R9RfeQR0T0-5l-gFOoCbxycV6HFL83AdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=u6CgwmWs4Sflpqw43kXIgzXWArfjMmBGwo-Pxy965DsTsptj-FgCVWfYvgLMqx5Dw8RUid7iAhzeqTH9piqyPEPHpQqAfmjgt8FO7ir14l396d3fJA6R67cD1nfNLt8MgIA8GkyK9gPT4p9jkT60En6NjULJe7RPBbhE8D8z0KMv5CPBarcbtJCdESxNjLZVTWwy_emw3qB25VYEtANVPZyZaTt_U86_YDdXduUkAN-bV-GTKtZnNKCJZ-N_TkH6zRkWd0PN1oMpQwPpqZD5dNlqYZqw4zoTQ9O2fYEHIRM5Ukv2snh7wkk0qn5ES5xqaEKqs1E7c0OhXKYMvRIaNRi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=u6CgwmWs4Sflpqw43kXIgzXWArfjMmBGwo-Pxy965DsTsptj-FgCVWfYvgLMqx5Dw8RUid7iAhzeqTH9piqyPEPHpQqAfmjgt8FO7ir14l396d3fJA6R67cD1nfNLt8MgIA8GkyK9gPT4p9jkT60En6NjULJe7RPBbhE8D8z0KMv5CPBarcbtJCdESxNjLZVTWwy_emw3qB25VYEtANVPZyZaTt_U86_YDdXduUkAN-bV-GTKtZnNKCJZ-N_TkH6zRkWd0PN1oMpQwPpqZD5dNlqYZqw4zoTQ9O2fYEHIRM5Ukv2snh7wkk0qn5ES5xqaEKqs1E7c0OhXKYMvRIaNRi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oszrrPQ7whdGIxbeK_CyMqOv36argMYa1P51Sg4wT42C9TS6NEuevj9w9LAlTL_GgwoDe5Bc4VezwUD_QSjc7GbsdgXp4mfTrdXa4AiP-iMj2mV13MZY0Q48LFjT7nS9HUJt4v8OHsM6n9HPHbsgcZmS5OQgvZW9N5yE3VHeKtpnHb8lismJfiDAUd12PW0tbZKhN2eUkbRHSpn-QsWHWmGNK0QG9D5RTt-CZTO0DTHV1MpQSjiRraCTd7dbbP7jIlC8_N81ds-VXOjp0skwnkbSqejDdpgX1OFHjrUP_ZRfy3k13qDWfeIZxdqMMwZnHxkmwyIEVIr_MoYw3_WZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EefBjpdaedwQLS3PDjn7u723jA3pN9oUOq7YQw89M8p8DKhTc0bKo5uZiGfl2qkP8mpfUyU6p3WlSoq1qrwwJ7puJ_yr_47NqAfx_nKEhe9DpJ9hYSzhl4hzLcW6DWtr__vPphSBpRdvoeRCXRENtlt-dcbONCq1L9KErCFKAb2E-72iCaAOahUvF5xLYXzKU5J1F6-wAJkcEIfltrh6tpJjStuqOeZoKdArFBRGpKUHMC-O-DyLAanOIeSjxa5rLAXzeR2-YE9CoqyU77a1alok0Y8uMqVkDI5Rp4-GGRZ6486S_qyWvR-DB_n-g-e46tIxKPYmm3ENyrGV1NIESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fuTxR7xAtt4vocyPmMHdB1BaKxpDFyE-UPdefXaAecJOOFP-3UNJOfw6_uETEJqsjMp67drcDrL4NEzNNzjRKi0LzJNP3LOPn2CKuVCYmJolhzB3tMVTxGBMRdrCMzLEKXc2uVRmP59j7kGRq3uaa2mnu0SRjk7_BO8KgK34sZIBm_fqi-Zzq4G2tLSA01alqvZUNvtHEOSUjVl5c7vYIF-xw-hhTD1f49w2agV9vlctsQ1ueh8LQkD3CnsKWKriHGjg-LKXmSVsnbtmCQttdn6hpeAOoyOJDS4ncfHr26t-Rg28ARQw8bW0WsAX7z6fHstAfotHxu2hSkDIIGsUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6_jDN-6KBAEyyjpiC3_ZNXo3LLzVp8HpLrmLl6T0jKUillVuOHyalRyqnSsYx-rxV3nx-8lOEgsC_Clr8nWlBWn_RkOiXBx-M7K_tigERglKPwmTt0AGR9Ya9Z8ewzunHp76BTeCzX2XCkG-_iZ1kRdukVQIcdXHKXH6TjQuZB_-rguf8ws6jyWXpAkY1I2vB8za10rnkMijNiEIOdg9XOmKJ-IZvBzvQDW8uIrb_PQAsgoKGZG19AHBkq02I4DRa9BaXuh83Iv1VqiOtIgiDujSb-ECsG8NO94QhGtt8e6Zej2Yb35HH4vicyYT3yewtbkQYdqHYGnNBc0g5hOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=WDaB-TTDsz6b79w-gcKdUo7ilDPU2oE0q6zh3W5mKUDEYprsvl3O9b7MQfCO44AJcv6-1c_tfY9j6hemXLFgV97nuHuLQfX4lQZNr0_84j3OzOn02jkZsuI_ZsQHmCe9CY_drCn5xYgy2uKWv9mnrlnWq7SIWuL2gucy8i8yUOaqaaXyc4eKAoZukVUKgadvy43PXd6WYZcJQT3YGEUONptRyxAeTO3QQKNGlUacAmT7RLav7Q4gy0WfhNwQkVAiJtQgmrRa15rKQqzkuE9XFo6CVEQtEbC86RrZmQmu7TnlmJMChASdKGmmz2LFdZkughvEj9sHSwanOS9GGwGPMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=WDaB-TTDsz6b79w-gcKdUo7ilDPU2oE0q6zh3W5mKUDEYprsvl3O9b7MQfCO44AJcv6-1c_tfY9j6hemXLFgV97nuHuLQfX4lQZNr0_84j3OzOn02jkZsuI_ZsQHmCe9CY_drCn5xYgy2uKWv9mnrlnWq7SIWuL2gucy8i8yUOaqaaXyc4eKAoZukVUKgadvy43PXd6WYZcJQT3YGEUONptRyxAeTO3QQKNGlUacAmT7RLav7Q4gy0WfhNwQkVAiJtQgmrRa15rKQqzkuE9XFo6CVEQtEbC86RrZmQmu7TnlmJMChASdKGmmz2LFdZkughvEj9sHSwanOS9GGwGPMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=Hr1FPqgvm5ukKLSRpFLbYYoDime5EocWuyA10pNCJ-mA-wFAPaOFwox9bzZJ5YE4YYBXpM4vJALYcj_wLapUhH7Fz2UW_3XdlmVJKHJ7wlUbISc0RumaGnq3fXu5rQvbB6vA52rLjsG-R_0BdomZK1mshWNJJg0BW7Mc7bkHkM2_O1lqe1dlBH6sjYXBEGNOoB216utuAZeOEJvRqVxX5VANXn8tsKSaCGOuYMSTV_tmsuWH2AzGyjEpIXCfeno17Gg0IqFwmD8LpCMbPKJAn6D-qJ8_WE5chkkbJdcS5jKKFhkSNx9TIXQbl9cRdhDeO0ruVPWwkmZh05STlAeZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=Hr1FPqgvm5ukKLSRpFLbYYoDime5EocWuyA10pNCJ-mA-wFAPaOFwox9bzZJ5YE4YYBXpM4vJALYcj_wLapUhH7Fz2UW_3XdlmVJKHJ7wlUbISc0RumaGnq3fXu5rQvbB6vA52rLjsG-R_0BdomZK1mshWNJJg0BW7Mc7bkHkM2_O1lqe1dlBH6sjYXBEGNOoB216utuAZeOEJvRqVxX5VANXn8tsKSaCGOuYMSTV_tmsuWH2AzGyjEpIXCfeno17Gg0IqFwmD8LpCMbPKJAn6D-qJ8_WE5chkkbJdcS5jKKFhkSNx9TIXQbl9cRdhDeO0ruVPWwkmZh05STlAeZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1YP0oB6UA3Q73gEpe0_hkFJnOb2vFml7GIDHPTLQ1dHaOp5_Jnaxn__ZYs6HFlgN3adoch-Bjr0WU74vwiUJ6obxErT5czRjnAWNWLUDOy4Jtz-fCPXV2V6WL-JSwjXOQyxjIzyp0pPU5sXG4obAzdF3Sw6VjmmMVVQo2Qjg2B70CbWPKSS4oqxN1kt7-u1RZCF9LkePq8l7hbZdbZJuMzhTO2GPg9tLn-b9TIp1L2vDBDfOo2qqA-hjQDzr5uwuUDoA5NYrDXbO3I_y9CyFGoKNcZznMfo7AV-9EM9G0PcJlOkiLXDMXcqp7cHQgWZ2Nr7o-ArjriQiLegfFr88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Faq5CLwWs3wuT3Q7cXsxpmhA2Ejmn8J1NMBpwcHo5fReTcXEX6bHB2wdJblkT43QgtC6GZh32NLLTZGvvYKZPLzGi00S5HM5OO8aiI67uL1GBIjdpmgdyCdtxwJN-x9spIsuA3HsHn4TA6Iqj8QQEBSpinIvVJ2eOO_erGcNmS-Jg08-ctDleFkR5B2V31Drqf0BTkM8NicBbWY_l_hwor4_xpiZSBqe7bf_g9dkQCN7MbP3LEnunaqSEYFOLMMR2Fw33X4p6VdnSNITB0zeMXUC-L8OJK-p2ehhWVQ1T5VJI3YJ9tKs_5GvGrI8henOpdE1AZU_Y77q32uul8mo8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Faq5CLwWs3wuT3Q7cXsxpmhA2Ejmn8J1NMBpwcHo5fReTcXEX6bHB2wdJblkT43QgtC6GZh32NLLTZGvvYKZPLzGi00S5HM5OO8aiI67uL1GBIjdpmgdyCdtxwJN-x9spIsuA3HsHn4TA6Iqj8QQEBSpinIvVJ2eOO_erGcNmS-Jg08-ctDleFkR5B2V31Drqf0BTkM8NicBbWY_l_hwor4_xpiZSBqe7bf_g9dkQCN7MbP3LEnunaqSEYFOLMMR2Fw33X4p6VdnSNITB0zeMXUC-L8OJK-p2ehhWVQ1T5VJI3YJ9tKs_5GvGrI8henOpdE1AZU_Y77q32uul8mo8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=B-HEbf3LEttgzt0P4zsYA1aVXB6P2Ucoqqt3mk9FRvAn1XCiLShEZ5SXpEhzmEdEFDMY9N_voVu7AMI1RyT8uSHyEfY2KZMC-CXHBBjAturBLQQcm3D_Q69nzSAhL5oO0V2ptv28bmdlTrykVmQ0_8OdOu9YXMK1Wc28Eplsk4q1j-q4jTP6kGgKIMJ4_EDL5hjCXqYjIHYsFmR6bdAEUqPEHo4f6JsrUe_O6cJhN3l-5Zt4QaN8uInJLCzV8gxSlm8yal8d9DwT4Y_e1o1vGRFZM-uWRjOZ5lC30W0RcQwBwMg6soSzOy0hB2CcWFEamrPx7AREhi7JsL--1ZKWVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=B-HEbf3LEttgzt0P4zsYA1aVXB6P2Ucoqqt3mk9FRvAn1XCiLShEZ5SXpEhzmEdEFDMY9N_voVu7AMI1RyT8uSHyEfY2KZMC-CXHBBjAturBLQQcm3D_Q69nzSAhL5oO0V2ptv28bmdlTrykVmQ0_8OdOu9YXMK1Wc28Eplsk4q1j-q4jTP6kGgKIMJ4_EDL5hjCXqYjIHYsFmR6bdAEUqPEHo4f6JsrUe_O6cJhN3l-5Zt4QaN8uInJLCzV8gxSlm8yal8d9DwT4Y_e1o1vGRFZM-uWRjOZ5lC30W0RcQwBwMg6soSzOy0hB2CcWFEamrPx7AREhi7JsL--1ZKWVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=ry7KY-DhhtU62IvQPK8EHhZsNO-3iZqwGbRI5_JuHzpxoKBStDT3t25h1LgQiNXWTpIZ4cOWbWhJ9nL7Sfw2Iw3WGZMy0hIdEbEmrNE0k5UpMneGqaHyGryUzZNAdKFiFQlYw9myI6ZIMjc7uF1pP7lVmX2R_JA1_VVBShOVAjBBKelg30d33kPHQnaDd07xyzHn03CVHsA3GR-YkcsacDPcp2ik4TKPnqn_2v3qRO0g2LTnhDRW3vWQi8Htc_A3a4_SYgDDXf-MDpMafj0MoDrQZ_Khq7LBh3j0fkOJQygvud5Deu3B3QsWDWoH_V2r0r6J2FsqCNpNtMWdYpxh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=ry7KY-DhhtU62IvQPK8EHhZsNO-3iZqwGbRI5_JuHzpxoKBStDT3t25h1LgQiNXWTpIZ4cOWbWhJ9nL7Sfw2Iw3WGZMy0hIdEbEmrNE0k5UpMneGqaHyGryUzZNAdKFiFQlYw9myI6ZIMjc7uF1pP7lVmX2R_JA1_VVBShOVAjBBKelg30d33kPHQnaDd07xyzHn03CVHsA3GR-YkcsacDPcp2ik4TKPnqn_2v3qRO0g2LTnhDRW3vWQi8Htc_A3a4_SYgDDXf-MDpMafj0MoDrQZ_Khq7LBh3j0fkOJQygvud5Deu3B3QsWDWoH_V2r0r6J2FsqCNpNtMWdYpxh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgfNzIlMgP-nMp245ffhbfv5YHVZwpLda7rdciw3WCm_T-SKYo2yTJjkqlaCzOhxsFt5bJIaQ6GLREf7CCvpwDm-tzf7to8GdQQ_DUcC0pR_FdEWd0nVMHT7p_ubjm4egTKch96mWrGB-s74IdPnt7bcaHev_L93rh5PbO_6cuqAntBJeprxRzCHKUMqb29F24lSNR60omirP5ECNxjtDX5yaYzFE0co4WA590GHdeLcN_F-qKLpQQfEJTJdmnoPJhNanjxFiCzeepeZL8WoQj75W1LOTLG1MppsUzlTrxxWLecUfdkr4cwo4CpR7HQh9mN5I_vqvENBYVflJyjOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bmG6DJV5ulcaiaduZ7DJVP3XhvmK3UvS2dDiucZKPygi3P1iMfojYH8Avo_RvCg4RkmSAKdVUIsLV2whZUrNVltcd-GD-bhNOO-qTFYQryDMOy_i48wykHzDVqYMjyrTDT9gYabcRuumhptO2aXe0t4YGSIsWRMTa29ZqBgATb0HiXCXKFP7ucrjV-uaXkODwijOSRxfdMNYNOCnmxNnglNUnw0_RfBcBMCHCIMAxxHYxR6hSAr_S1Sd-qsGFbBapImZ1EH-hILCAagqQCOx_PahZVVp4C3TNBsDKbHhfGvsYH8294N7srwUNgvIM6Ym975RxaXm23Ric_203fvJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bmG6DJV5ulcaiaduZ7DJVP3XhvmK3UvS2dDiucZKPygi3P1iMfojYH8Avo_RvCg4RkmSAKdVUIsLV2whZUrNVltcd-GD-bhNOO-qTFYQryDMOy_i48wykHzDVqYMjyrTDT9gYabcRuumhptO2aXe0t4YGSIsWRMTa29ZqBgATb0HiXCXKFP7ucrjV-uaXkODwijOSRxfdMNYNOCnmxNnglNUnw0_RfBcBMCHCIMAxxHYxR6hSAr_S1Sd-qsGFbBapImZ1EH-hILCAagqQCOx_PahZVVp4C3TNBsDKbHhfGvsYH8294N7srwUNgvIM6Ym975RxaXm23Ric_203fvJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CexjbKnUUhfiaE5x0x-2bA0xpWST3axVterhF0ChW-5DLihq3p0qBQDaiYkzuJ9z9ruG7571ia31Vygmbz7509PlKvtngqnNnH9iIFfePNh-HQ8J5TfobGzVTFdKdvCP-UAcjrAZ9ZKIq0W6r2a2pYMfxuPbQnIAWYLV4o3KxVbfb6Cq26BCvCAZpp7FuQPbGVG4tcI2LW0WX4q-JmMIdsiKfxGpHXrcKHbfdBdnA5NIoxs4kaHrdpK-zGBZFRaF4iDbQ0MVyyEL4LcSpLXd_NzQHkBoy5z5FFIZUjW9Ql8sYxVjR1AgGQpUWKsk4pHl4WzjpJC6O6ivXZtE9-CcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDpSh7X0FsGxzq6WbzOM6q0I-CS5s6fx26fpi83Gc6ZhxxykAGJOmbgX2AUWTHaYzxaY23CszEBVTgKRDtLT5x2YKlfKeZhi8J5dISVPvZ5M9zxNHUE5FZE0wG2COGTIhKXm0UHG-TSkTxAYSGl3EzQx-H14gg0yrXjDncXY-vA2KYtht3AGlwdWThrnZ76yd0XrK4jeG4cAm5JrmEcIEecBAYV0RxZNAY0DSv4kBRC2H42nzQ-QmPhJVCFP1KPnbZWMW_l-5F06kSKoXR_zUjnmQwRZXCmtIK4jM_xeVOnugDyI-6LmhwKc5XMyBtJUvkK4tZgGCTaaVA0g6EXWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=b9sIsS8tEYf0w-fqdXIvuhO2jIHQ4c0OpW5X9bwjYKH6fRLyu87psVf99tvwr_eetCeWnOVAAL57UDIr7yAXMe-SKKhR7Fysd1IsbShTjzYVoC72tqQM8vKffZXtpPbilF4Vuds9x6WcJJrRT1Tt6WQzMi0qnn2FGN7EQjkIWmarn3hYxtQEdkyGEqwZLY8UmlTsg999MOJJA_50n3kCbjA8c7hxX17kj6qGiKrW1-hjihS8IpuPemi_Cyz4ODIV945nNQKrkQvI4RstKTW6nIBqQJEFerztLo42SpnLymkTiTGceoR5joklM7QkigGJymip-WrlJX_iulmuOdf04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=b9sIsS8tEYf0w-fqdXIvuhO2jIHQ4c0OpW5X9bwjYKH6fRLyu87psVf99tvwr_eetCeWnOVAAL57UDIr7yAXMe-SKKhR7Fysd1IsbShTjzYVoC72tqQM8vKffZXtpPbilF4Vuds9x6WcJJrRT1Tt6WQzMi0qnn2FGN7EQjkIWmarn3hYxtQEdkyGEqwZLY8UmlTsg999MOJJA_50n3kCbjA8c7hxX17kj6qGiKrW1-hjihS8IpuPemi_Cyz4ODIV945nNQKrkQvI4RstKTW6nIBqQJEFerztLo42SpnLymkTiTGceoR5joklM7QkigGJymip-WrlJX_iulmuOdf04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9WskLxww3fOAr0HAqf_Sjbfxa-RTiiopeCxvZGFg1fTmN47DnLxWrHN4MHow8ZX8hSI4iM7rdDEB7ygV7pviEEWCP5QKoDLOMUfp1MV3cRtNHZExyvPXma2cXG7C7_36h7nJP9rpL4JJP9ErMUF1kDb1QXD8UEp2qxaAE3SbbC-M_qQgvGzm7JyXhZ3RfK2VOlOv-nmrDFT32zdKnKKcut8g4sJFRdmSGyMRBrSrSIjGl3-gpBlco-Ct0BgHFhkEa-4nXMqQxblBzgS3z7nc54A4WtQAwgz8E4fR3BlciYAUvBbWKgrYvAVLmaNrvvaGnG6sb1BZrkzM51lJbfbDi-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9WskLxww3fOAr0HAqf_Sjbfxa-RTiiopeCxvZGFg1fTmN47DnLxWrHN4MHow8ZX8hSI4iM7rdDEB7ygV7pviEEWCP5QKoDLOMUfp1MV3cRtNHZExyvPXma2cXG7C7_36h7nJP9rpL4JJP9ErMUF1kDb1QXD8UEp2qxaAE3SbbC-M_qQgvGzm7JyXhZ3RfK2VOlOv-nmrDFT32zdKnKKcut8g4sJFRdmSGyMRBrSrSIjGl3-gpBlco-Ct0BgHFhkEa-4nXMqQxblBzgS3z7nc54A4WtQAwgz8E4fR3BlciYAUvBbWKgrYvAVLmaNrvvaGnG6sb1BZrkzM51lJbfbDi-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=BgaoKd3DcQGSR3J2wvAcG1XmF0aeXnqp30OOinEeCJc3wgJflzCAfVjSIw2cjvzL7hCi2dO6iuHGaCPIBf-gop25dHGN8NcPKp8kZn4JWqOEr-hr56LUYOm9XHOBLSJ81y2x7SCJWyDV_emICkcBOMowtF1rYS3MOoGUwZ6lTBU4CwVxZdqS0ILqpxqBcpWN6aApGInKFXs14oegILDussBSqsbFg67NV9yQd7WkPmqaq0PmuUlCLHIuzL4Q7VY94IsBC2Pa1I2yBp01oXfAczE6DgZ--Yeb64Zf0YucfsSYgx4CuxM8yvcBZ3H10htH6JGyS3WY3tsneRYOfICdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=BgaoKd3DcQGSR3J2wvAcG1XmF0aeXnqp30OOinEeCJc3wgJflzCAfVjSIw2cjvzL7hCi2dO6iuHGaCPIBf-gop25dHGN8NcPKp8kZn4JWqOEr-hr56LUYOm9XHOBLSJ81y2x7SCJWyDV_emICkcBOMowtF1rYS3MOoGUwZ6lTBU4CwVxZdqS0ILqpxqBcpWN6aApGInKFXs14oegILDussBSqsbFg67NV9yQd7WkPmqaq0PmuUlCLHIuzL4Q7VY94IsBC2Pa1I2yBp01oXfAczE6DgZ--Yeb64Zf0YucfsSYgx4CuxM8yvcBZ3H10htH6JGyS3WY3tsneRYOfICdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoG9_ONN0-Du_FRXLjFEBhXEiSSUDkxUCI4PCPB9zIHhv0QtH0KwlPk_8QU8pv8_K28vIWjwM8VJsnQjy_HeP_BvFhkruHwyHKmP2TmOJUEgc7pX_LbqGuh4DfIj_pj4MQqEolbL3uBYscdzDdt1wayA75ub3cmKGASrXH7K7Me5QIYaRess-AkqlXkzZ_fCHcWEe3IJm-N5ugAU9fbrxm1yx7IumraSEkNJBAxAM1i8j1e2lliz928ATpL-BY6BrZTCzwsM83hroDvKmpSqGr0QGAn7iqf9BcIwcEI0tbCj_E0BZkAXt2lEmtj9ixPONExGqcHjI4QpsWnTwEPqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=f1BVjCFIGcAIuJlK-x6PFNpotFhgQlSl6K4LUYzfyoGKMUVtkXu7QMctzLgIw5K8d7_PnzT58dktArPwql7FU5IfDIC1-cmE27k_Y8s1GN9hjdv3u_np8gEDq11GOLl0cUpL2ftmpH7LhC7xh5ErriyYmyUJHZCQ84Wdbbs0iPZ1u-R-EJWQO68KRH4P_p-5kBl866jBKulx_RXLUZHW9E5Ke20xbunQYni8VpynlxOwv6MbKfGH_fcPvyxiBvC8bzlJrZ5DdlP6jBtVUZ-M9m88s6TKYw2OUFkFiZeHs9wOtL0RZWbX-TyG8B2FQjSB_C8QFOiYxJ0LJfuyIOT0AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=f1BVjCFIGcAIuJlK-x6PFNpotFhgQlSl6K4LUYzfyoGKMUVtkXu7QMctzLgIw5K8d7_PnzT58dktArPwql7FU5IfDIC1-cmE27k_Y8s1GN9hjdv3u_np8gEDq11GOLl0cUpL2ftmpH7LhC7xh5ErriyYmyUJHZCQ84Wdbbs0iPZ1u-R-EJWQO68KRH4P_p-5kBl866jBKulx_RXLUZHW9E5Ke20xbunQYni8VpynlxOwv6MbKfGH_fcPvyxiBvC8bzlJrZ5DdlP6jBtVUZ-M9m88s6TKYw2OUFkFiZeHs9wOtL0RZWbX-TyG8B2FQjSB_C8QFOiYxJ0LJfuyIOT0AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=HXs6byaWtPyRoXQENMwHsE3BzmHdJ-KTNBefXCxn0Iqjl8Y9WyNfgpxNAg75t46tsupPY0I5hcUmWlWs2aBA2kjBKexnOS1G9CIF8aWM0nP3z3LR_wCgnFa90OwXe_vdLzki4MLeAi8yfUraKd7g7IRFdgcnGLsedtQNzutNVSP1uwA8OerjigRrA8i_02xtoiufLTqILlNeJueN-1TEa4zi2eqhnFKSmPnBFH5KOx-EQT-MeuayIQC1DpphSyyMhKoGXa8Y-CNUO8eTPb8969xFuyYRxD8cx5YGM-kb-KzyoZRAF_ujmwULEdUndcej9SaxtHzMMoy84O6C_nfMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=HXs6byaWtPyRoXQENMwHsE3BzmHdJ-KTNBefXCxn0Iqjl8Y9WyNfgpxNAg75t46tsupPY0I5hcUmWlWs2aBA2kjBKexnOS1G9CIF8aWM0nP3z3LR_wCgnFa90OwXe_vdLzki4MLeAi8yfUraKd7g7IRFdgcnGLsedtQNzutNVSP1uwA8OerjigRrA8i_02xtoiufLTqILlNeJueN-1TEa4zi2eqhnFKSmPnBFH5KOx-EQT-MeuayIQC1DpphSyyMhKoGXa8Y-CNUO8eTPb8969xFuyYRxD8cx5YGM-kb-KzyoZRAF_ujmwULEdUndcej9SaxtHzMMoy84O6C_nfMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=VYQEQF8MRmfU2qo1E8hcf7mnFapz_Niw-Q3mEBjrWDyFQOEo8rV11EpR_90tzn_UiU2-Mv5l6ivVkKuwZoZLmHRDbP38vsLJWLeeiLL94a9sQmwjXryOCb2CF7o_nG37HOL5HB9maVbUsAHchfcNwJeSPkUhqPrqQgPJeaNGBG0TSbxLtWZBIylkUQutpT7OolaOthevUyUXlr9wZfGKYdoTjC4QCB3RAgrQ9E7xhVZ2h_AV1mGQC4EcaZgEqppj8SB5w2GN7N6-fk4dW8gY-4IaNLW2emraBA4saH5OiRE2yw4cOw9HELtOpZgf1TOHAGDqQRa4ZxtlQ6-wHr8OIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=VYQEQF8MRmfU2qo1E8hcf7mnFapz_Niw-Q3mEBjrWDyFQOEo8rV11EpR_90tzn_UiU2-Mv5l6ivVkKuwZoZLmHRDbP38vsLJWLeeiLL94a9sQmwjXryOCb2CF7o_nG37HOL5HB9maVbUsAHchfcNwJeSPkUhqPrqQgPJeaNGBG0TSbxLtWZBIylkUQutpT7OolaOthevUyUXlr9wZfGKYdoTjC4QCB3RAgrQ9E7xhVZ2h_AV1mGQC4EcaZgEqppj8SB5w2GN7N6-fk4dW8gY-4IaNLW2emraBA4saH5OiRE2yw4cOw9HELtOpZgf1TOHAGDqQRa4ZxtlQ6-wHr8OIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=pelDlFPc3hKQkv6kXm2AUkfMOJKtrbaKiIPT_hFI5xYp3HClnhhCxkWMn7M2aG2tkrRYs9T23N5Ily7OUBiQh3Yjg9vF6Su0n46Abnh9oeP-BLENiMVu-Ry1hBy4tbghfJOdjcnyZibuNjKhLlVOjWnWIjTxrfRo5_zAX5Rlwxocq8g06NdQNKtRZ5fsfAQ6i2zBS7RtKPwUnNbER3hdtlaPBFLsnyaHnV4iiKE04ahWcSPHNaen9AvnwGA6SWy7EgLc46u6OSGjLAC6jaj582dB48DO8NLy9V_PoynctOMqgIhZj9U66BdfPJvQiwvaR7CfqrE1RpJLLVbCO8r4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=pelDlFPc3hKQkv6kXm2AUkfMOJKtrbaKiIPT_hFI5xYp3HClnhhCxkWMn7M2aG2tkrRYs9T23N5Ily7OUBiQh3Yjg9vF6Su0n46Abnh9oeP-BLENiMVu-Ry1hBy4tbghfJOdjcnyZibuNjKhLlVOjWnWIjTxrfRo5_zAX5Rlwxocq8g06NdQNKtRZ5fsfAQ6i2zBS7RtKPwUnNbER3hdtlaPBFLsnyaHnV4iiKE04ahWcSPHNaen9AvnwGA6SWy7EgLc46u6OSGjLAC6jaj582dB48DO8NLy9V_PoynctOMqgIhZj9U66BdfPJvQiwvaR7CfqrE1RpJLLVbCO8r4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEPWnoURN41stQGDGz8Px8WC4ptT4d6eeTSfezGt-HtTInYC-CTsMchgyw8bglmTL3w2Z4Xa3iOa_GkkhehcOiDGTjVZyaZm6u9MAarLwd8Y0i37yyYT5pvvcjN3Q0FROCvc2TwP_fBK9QNtKcD3pcolfRgoXJXDGGjvktlayyURwnvCWAvbF-5il76ak73iyqOG0pZVEVMn9VWY_MrRsrh7pm5tRHSmlPvsOf-S5H2qJDlF_62Faejbl_vFGYnDsA0bWouguDuA4G6B58_dg9_YnFJVMCVi2qqYbCgGQublLAWBJrxzZsPcYxjzq9_lWk3F2W5l3mp8ytM0LNTmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=KbZJCPPDnCNBoYWRIMJxQM6Aj9VbEUkBamf8Kumi_zG7Zjbnzymke_M_DRGYK9Xw6yRL6MoSlLRIgR3xPORo34EzYpZm2koK17G_kzyYDcWCr3SXBj2lVTkQh_9MfyMnLWXlBSvop81uDlvfkPjy4_n1FNRcM6ncR4PbxDYBOK8MblGwuOnCp0EjBEvArbJf4swAckBCrZU1ScWNMD0E9HtbbpGkPG1MUY27tf_gQQFaz8LmEXSSP_5CiCSdbKC8pZK8Feq572SS0JR3cU2REveqEIUMjirx8cYawujPs-6oj1TSBgShf9XFLTOXQMM8KuxnqGudtnWuJ5TDflLlTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=KbZJCPPDnCNBoYWRIMJxQM6Aj9VbEUkBamf8Kumi_zG7Zjbnzymke_M_DRGYK9Xw6yRL6MoSlLRIgR3xPORo34EzYpZm2koK17G_kzyYDcWCr3SXBj2lVTkQh_9MfyMnLWXlBSvop81uDlvfkPjy4_n1FNRcM6ncR4PbxDYBOK8MblGwuOnCp0EjBEvArbJf4swAckBCrZU1ScWNMD0E9HtbbpGkPG1MUY27tf_gQQFaz8LmEXSSP_5CiCSdbKC8pZK8Feq572SS0JR3cU2REveqEIUMjirx8cYawujPs-6oj1TSBgShf9XFLTOXQMM8KuxnqGudtnWuJ5TDflLlTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=eqVv-OjJvb6czbkC1J5NsKrZ9Xuko8yL2bzEldWWY-BXUBW49g33dF4qTrFunxUib7EZB98gzU_FiIAnwNVB2cZRpFnyQcKtIsDZ9XzhBH26Gr59CoUkB6XwQJznN_y5dJZwfaja8wGkW5bG9huRykiL8cnGKUxii0FmkAiroePCG49mjTeatYaqDjm0GjQr3PJ4-VgYOcsgNeeSu8q0PrLdRUKaYMyFofNEE36L0NqW14ldGM3rXUmFyHyFNR4jfIOfJQ0SA7URwb3QQA2Fk7QpTcKv11DzScbxsQ0Pks8UzTPsZnWgo3cAHaLmKdOqm7YanEcgAVZs1PyAh2wNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=eqVv-OjJvb6czbkC1J5NsKrZ9Xuko8yL2bzEldWWY-BXUBW49g33dF4qTrFunxUib7EZB98gzU_FiIAnwNVB2cZRpFnyQcKtIsDZ9XzhBH26Gr59CoUkB6XwQJznN_y5dJZwfaja8wGkW5bG9huRykiL8cnGKUxii0FmkAiroePCG49mjTeatYaqDjm0GjQr3PJ4-VgYOcsgNeeSu8q0PrLdRUKaYMyFofNEE36L0NqW14ldGM3rXUmFyHyFNR4jfIOfJQ0SA7URwb3QQA2Fk7QpTcKv11DzScbxsQ0Pks8UzTPsZnWgo3cAHaLmKdOqm7YanEcgAVZs1PyAh2wNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdnBKSg65_hmVrUDJkxSM-mWHJZKZrQ3V1uRrdnnQ3hjK2GL9rDFz7Yyjxid_-uCDA-jNZpaO6x1_2Ak5MOSOc7qbgH15BLKFRJ4Q56z0MKfEv5kTTHtPcBvuhiCgDe5Nc7NBtxWXhJbteHYDIcinR6tpTD2BUGwFVlZzg5UvPoja6mjAidRlDYbvRE4WM4O4xKZ5drMMH5-_CGMJ3W7U6Yr4019LgtFa4GA1-h1tplOdxAXDdB_rTvLxtX3XM_PepYTld2NWb-Cao5abnivJHgyzjpULOGIvSm0Hgl7okpIlv0rOyb2GX1gM0Dfp3KfRNpnAAm9EFXZBZtqukkrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MXNsHFfmC_aPhEKFzFBm6wCUBoz_q7EmfN3ZjrxSN7dPpRYqGemeF24wRuMMh-Cb1a8YESHSNZDPO9Is_T9tJdKzx-smCp19BJHxcxh34t70LQPs5CAvp7yydW3sGo-GhqBVzRRu9eMdiaAmqtD6K2HLgAK4EUTSDvTSrNMPvphC78z1AevrMG2vRF4se-tki7H4ocCdvWxkqLugN-oWV1DnJB21s0kfwOE_ClnbLCO1zkwLkFRCpjgTWrwtwZ7tFusAJ9HzK3Zxulwu__vvgegALZaN_eFjxvZhsraimDS8N7E3sXDNpHa29iiuhZs5c3e2DQJn15JG05_yxfNuXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MXNsHFfmC_aPhEKFzFBm6wCUBoz_q7EmfN3ZjrxSN7dPpRYqGemeF24wRuMMh-Cb1a8YESHSNZDPO9Is_T9tJdKzx-smCp19BJHxcxh34t70LQPs5CAvp7yydW3sGo-GhqBVzRRu9eMdiaAmqtD6K2HLgAK4EUTSDvTSrNMPvphC78z1AevrMG2vRF4se-tki7H4ocCdvWxkqLugN-oWV1DnJB21s0kfwOE_ClnbLCO1zkwLkFRCpjgTWrwtwZ7tFusAJ9HzK3Zxulwu__vvgegALZaN_eFjxvZhsraimDS8N7E3sXDNpHa29iiuhZs5c3e2DQJn15JG05_yxfNuXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=qVeZ_u6Gtn_TG9ZbVfRETWs1N61qWS4BVYXtv12xrdXA0ZeBoC781Bfp820M4Zb8ZhaA2KE4L_G-IUJMadExTkvNWFlLo4mCgtLvSBzdGvVa6Q_HdFcEmfnoK3MjoeTqx7pSKekGkJggzybYAKCoeiod6QDu9LxxcLS47EOQtn4DSlYftyMLhrSjlaAFQcb26BmhsDOwQFA32ewDicQJcBPfi73zTfPquAflE6AsHET8SffI6ntnaCfjgC-7fJyldBsNPYPg8VkmNvjYtC8GPXX3nMbmsaAFieroeDVFbBpK3lG--8paVrAA34XiDJeOsJIPA5Tm3GaFucMg_38yWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=qVeZ_u6Gtn_TG9ZbVfRETWs1N61qWS4BVYXtv12xrdXA0ZeBoC781Bfp820M4Zb8ZhaA2KE4L_G-IUJMadExTkvNWFlLo4mCgtLvSBzdGvVa6Q_HdFcEmfnoK3MjoeTqx7pSKekGkJggzybYAKCoeiod6QDu9LxxcLS47EOQtn4DSlYftyMLhrSjlaAFQcb26BmhsDOwQFA32ewDicQJcBPfi73zTfPquAflE6AsHET8SffI6ntnaCfjgC-7fJyldBsNPYPg8VkmNvjYtC8GPXX3nMbmsaAFieroeDVFbBpK3lG--8paVrAA34XiDJeOsJIPA5Tm3GaFucMg_38yWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IRwOp47xtsOUgjqqEHij5jgCKSejf7qV-tg-9u--IRD7tCL-eo2esQajWARvdbdl8yxUgOFt3KaNdrCsS9z8_qAdnBdlijD2jVaKZFngMwYqCJdBdSkvhQcwFws_gg0ZHL2mngPiaEYUHouiK0gmFA6OC5Xc5tEEodot9s_K5gd5GCCqf2dTubBCgieqeMcjUZChsFz9x8TRRr-yEr67z0asLvihOhm-SqpOEsD6jOZPspqnQ4C8hwzDOEIUUcLmzHjPHk7o_JoneAxXPshxaqUlFlIdHhjIy8DpNpL1r_sz7GltMIpVORKKvhUluYOpqiNoIs-kbus653gxi85XIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IRwOp47xtsOUgjqqEHij5jgCKSejf7qV-tg-9u--IRD7tCL-eo2esQajWARvdbdl8yxUgOFt3KaNdrCsS9z8_qAdnBdlijD2jVaKZFngMwYqCJdBdSkvhQcwFws_gg0ZHL2mngPiaEYUHouiK0gmFA6OC5Xc5tEEodot9s_K5gd5GCCqf2dTubBCgieqeMcjUZChsFz9x8TRRr-yEr67z0asLvihOhm-SqpOEsD6jOZPspqnQ4C8hwzDOEIUUcLmzHjPHk7o_JoneAxXPshxaqUlFlIdHhjIy8DpNpL1r_sz7GltMIpVORKKvhUluYOpqiNoIs-kbus653gxi85XIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXeLo2u9cGlMRTya4TA_zPNnPO3PPj05WlFByeaOSQhUQCn52nUYGuvjvBzvDTEqnHNYyF0D6tAJeR1wojQsG29g1samFY7TFFSOYDNo-upNRR4F6cz-lKTQzC5KGB_sPyUnRkWZ3S1vZP9FQO7EPTM3lFuoQQ4wk0w-K3l9TDQ6Cgt4k25Xm21AulXLRTGtdE9Ui7NF3nCMVLzBxOqMH4SorcRTVpdGeNokztEs7owxQ256BMc5qGP9FlsTFiCXba_t9ep29iSQGMRhlg1ftk6-5XSIsFVL-YCBshVJXygRbta1iucGQVS9IZTE8jTPcgbc4WFjXYbYdrWEtb4jFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHTkfuC3RNQLD_dwLvXY-hTEbgvY-tGcw9kO-twiKly0hFtXL_ix0oVrJvc5TeZLAmKERobKY2R0y0sl7-kGZ9tX65YZZW_V1gZ32klXwMZ_uf2LyJqckcyOYFFjUNI849cHWKFoiHGgn8gG6AGT3-3KkBGtCakECTF0PeEdfyBkH7VH1oyJMbMHq5v9w0JMnj4feFLjx9xx2e_cfyzIpPlWKH29oyac1ol00a02Oimhz600gbiTWkQBnkFbrgtfiEmK3jJLXy1_SyI38G-56BiuwnEd6wvd9cDnGJVG4Qyns1o3FuUf-Wr4bqmK9LU8hzK7A2E1aE_5fyqepBgXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFIqPr7wjUYTnxigZecuCVIPvQU59xDfIVNP-CxzxLfH1Z9n14Li141PUMhqbenvl6a11WTVGGLxaTssadKgkAGEm5WbhYmgsT7ZcsUOZyidVqXiqFk2BVSZCi1XVSR5rCYhjO2AUYM3MalzBTC0ilkUDjLc8CPMEEvO9bPr6KIME_GlhQzW7B-aXdzuYxQUOWg46Kq7ZtLm3ukxcHKPGxpVSPhD7dw1kRu0cR13LdAbY6nZnWB7CXKwAmNHb9o7T-fwafTm36vZe5cZvAiT7ELEYJuHLjPSSFfr_wtgIActbTkcnzPhQMpdoztEXk9y0qz3lv6ltp-n4_TWwtmvvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=IcLkRyLpfMQ78vyOw3lrX39FLijbxTWiSlrboIPm-iXgfj0ydnLWcaN2gqWrrOLWvFNL1PNHWqrhnbAb6HbcFrYsTVrHo8pw0Qgxs9xydw2wCq94xRShTY13C0yqguwrcqKI9_w5__UV04fip6nSiunaDX3Al7S1s8sTlEV905RkYADeSeudjL5WjrSpsX7lOnWfNYKLtpWom49dIyRqWOaOr0FPvCpMXr31wU_Uowk3h2knBqSeBrqMw8SMV_ja7s-VjaI1MhFD8MhiIcvmhwlU9tHMa3_-Vl1Lwod_yA1pDPCcVfvw9zbh2DzUPSd27bSzSUbTdy_70w4_OrzX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=IcLkRyLpfMQ78vyOw3lrX39FLijbxTWiSlrboIPm-iXgfj0ydnLWcaN2gqWrrOLWvFNL1PNHWqrhnbAb6HbcFrYsTVrHo8pw0Qgxs9xydw2wCq94xRShTY13C0yqguwrcqKI9_w5__UV04fip6nSiunaDX3Al7S1s8sTlEV905RkYADeSeudjL5WjrSpsX7lOnWfNYKLtpWom49dIyRqWOaOr0FPvCpMXr31wU_Uowk3h2knBqSeBrqMw8SMV_ja7s-VjaI1MhFD8MhiIcvmhwlU9tHMa3_-Vl1Lwod_yA1pDPCcVfvw9zbh2DzUPSd27bSzSUbTdy_70w4_OrzX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaSW3ugXEVhzSJUSkETcmiiLKdGm19woA77CPGAsB4oa7Zy5Qjap_gQ45qvl_T94wWCb4VDjbIGzim73TDo7HBOjLNpyn4rGo0kXDsbtknQGVTq3l6lrQpUQyIJGY5RCnfyLQ4hpAfLU2t-Cfs__mFSuz4j_B77cMxV8TtbOuVgUnuS-BfHbQG2vpdW0cScKTFl6Un4_qDpIjIdFWiXpNEnG6BDx5aL5VdmaOY87u7NgCp3oCTgO0PNzNhXzocwgZ65YlNAqRtJZl_lqqxACYo9dA5SQkBCc4n9NhTvrWTi0BDSGYa-hcK5Ul6nrny0bhPYNhMGcS5yEhXXlx34RfF-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaSW3ugXEVhzSJUSkETcmiiLKdGm19woA77CPGAsB4oa7Zy5Qjap_gQ45qvl_T94wWCb4VDjbIGzim73TDo7HBOjLNpyn4rGo0kXDsbtknQGVTq3l6lrQpUQyIJGY5RCnfyLQ4hpAfLU2t-Cfs__mFSuz4j_B77cMxV8TtbOuVgUnuS-BfHbQG2vpdW0cScKTFl6Un4_qDpIjIdFWiXpNEnG6BDx5aL5VdmaOY87u7NgCp3oCTgO0PNzNhXzocwgZ65YlNAqRtJZl_lqqxACYo9dA5SQkBCc4n9NhTvrWTi0BDSGYa-hcK5Ul6nrny0bhPYNhMGcS5yEhXXlx34RfF-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=F9x-YX0pA9wRtvA0ZtFpwmAp-TshkaKmLctOYwbEG25e0thAHQm_VSsE-NMSDcujOcoDWYGrgCuBh2LZz9bolb0xqID9iJ7VdE8Cb8refF60YmDRBvmQemPTk-GSFs7mPZOOIdyo3Ru-ETaCDIaXS5LVr48b00AuVWDDjO3GFOOv8ZtU97nDzvQsbFnv3Y8TtBFy-hz5SIRS1LLwNKpAZhSec8RNvAiOC4xO2vn-y8pjZslDIFfqVlHodv4pl96Ey0Jams0gUIifWFXXvdn284DmpOmUV_N-qW_R4kq7noz4mt6V_1Oi585HwoFA3D0ge1YbFGvTgp7FgHtkrCyTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=F9x-YX0pA9wRtvA0ZtFpwmAp-TshkaKmLctOYwbEG25e0thAHQm_VSsE-NMSDcujOcoDWYGrgCuBh2LZz9bolb0xqID9iJ7VdE8Cb8refF60YmDRBvmQemPTk-GSFs7mPZOOIdyo3Ru-ETaCDIaXS5LVr48b00AuVWDDjO3GFOOv8ZtU97nDzvQsbFnv3Y8TtBFy-hz5SIRS1LLwNKpAZhSec8RNvAiOC4xO2vn-y8pjZslDIFfqVlHodv4pl96Ey0Jams0gUIifWFXXvdn284DmpOmUV_N-qW_R4kq7noz4mt6V_1Oi585HwoFA3D0ge1YbFGvTgp7FgHtkrCyTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO1WJk_LNe1eGkSLTVZtcQUiik4kO8Fh1C3CXc8s8mfSkUql00PObkfELAAJI_M4OgAmxZfNGoOCFwmP5e5bHfBI6TNmqAsHuprlM8uFqsFquElmvHO365CboL-3wLWyrFkH96nTBU55njFBMXaPDtevAR-zWuHr22WmeGE9MaWnlVuvxkxhPoy_8V6GpNFHzihI-y7Mwydx8AVu0kH3129R6O51Knsvjpey_oZDBAveiy2rRvvxCLy3IMb8RVKzOQrCk4osZZdvYQPfDXiP7Cagt9naSmu0bNgT61wL2Y9AyzF6W9-lhn2b4_epHMlidbU43XPNwxBfTA8zIDg6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=gg8eNIRMAYNLmaipkaPrT-DSaKMmOXK0dvMBI07IF8b5H_KjxOONpcaGwYzbyAAMndbTu6NVqz8TDWPxKzSNiE5LjNYjbVh1MGHVfitGddSaswZdSE9PQn-jwNlGD1TxGGdGqHXNNdY1YsPI9dzi-A84MoxZx55MVqeyr8ZH_8m1W6ZTG57GYAe61MkslOz_AJQBJj1OmWIJppOqjpmTrVogwtMXpnQq5aABrS9J2xdCiOiBhKtQO6WNLAO6l4tJeNBLGnMYuuRdliKhhGpli-FdEErazupAH_qr8i2eR8Noh46QHb7luIOVWyEdhl6Limue1g9kMUcixdp0NvHdaQ478lPpWsXz8qxVW0vX7F-NtVj7Tv8jOz0gxpiDuYgufNucksh9HbtJQMXhlc61i_ZEZSy-rV6jUfbt9EXl3sLjBqtAuzxfnXrpcRxcxKQ2Rq-VchhqbJosm9serEQtZbwFEhOXarkvNV92GnuMWmkQGBues7RahzFGLm5_toNlZw8dlxHVb884dtzUTBlFa8iKyDZKFQ-NvIFnOmBCR77uyCsi8JXzbBbhSmGp0SVCUq9LT0zsExpc45Q2KXKDglfPzwKydB-f1IL6mKgP_E2O0WHzacnxQ8i4jemrAqV7hcNWfDurCk5mt7kZF2EWpmFqdwfL9Ji2tAkn1gbEF_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=gg8eNIRMAYNLmaipkaPrT-DSaKMmOXK0dvMBI07IF8b5H_KjxOONpcaGwYzbyAAMndbTu6NVqz8TDWPxKzSNiE5LjNYjbVh1MGHVfitGddSaswZdSE9PQn-jwNlGD1TxGGdGqHXNNdY1YsPI9dzi-A84MoxZx55MVqeyr8ZH_8m1W6ZTG57GYAe61MkslOz_AJQBJj1OmWIJppOqjpmTrVogwtMXpnQq5aABrS9J2xdCiOiBhKtQO6WNLAO6l4tJeNBLGnMYuuRdliKhhGpli-FdEErazupAH_qr8i2eR8Noh46QHb7luIOVWyEdhl6Limue1g9kMUcixdp0NvHdaQ478lPpWsXz8qxVW0vX7F-NtVj7Tv8jOz0gxpiDuYgufNucksh9HbtJQMXhlc61i_ZEZSy-rV6jUfbt9EXl3sLjBqtAuzxfnXrpcRxcxKQ2Rq-VchhqbJosm9serEQtZbwFEhOXarkvNV92GnuMWmkQGBues7RahzFGLm5_toNlZw8dlxHVb884dtzUTBlFa8iKyDZKFQ-NvIFnOmBCR77uyCsi8JXzbBbhSmGp0SVCUq9LT0zsExpc45Q2KXKDglfPzwKydB-f1IL6mKgP_E2O0WHzacnxQ8i4jemrAqV7hcNWfDurCk5mt7kZF2EWpmFqdwfL9Ji2tAkn1gbEF_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBH_5jPtFeIdeOwVWAnzbofBvf27INR4LDZjr8BzWaZtJu6ypMWkhYygWnRYVLVVdp4q3KkjBB3An_HIX_-Sm9pf8P9SAc-HudV-hbuWPHsr6S8Lx9-Fi2icSY2c7XHOTPSdHu5DWuyqMEAm-3ko3Op-xr8hLOBjI5Uu_yDwHGyXSWBEpdQ6hNYIZQmrkAMzuiGcwlBJAQoxO15dAlvTzT5CDGS4ZI397oTh7Za7oJIBfCfLJaSyxdxipipUs_1pJZHsZaflC4gXAVxVytm6q3Te6r5P6XqrNUQ3L9Mnoz-kq9sk1_EpCAVkug-7o0SqzUg5PD4hxPGKAMN5koZpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=tUy7ZbWoNEnCIweL1CAyYECAbErVw6ak-xZ-pxGfJC2-133oujUWGPd--y4uvDD3FKPgLppzgj9EItU9FpqqLrgpRo0l7wzPRozHw_9CF2VYuT58lUyahImARhG4HCUs4xnseBgZlgxMHP7YJwGpW4m_KGjIe0ogLNgJnxi9t9749p3sqNElCNQ3FveKcf_f4yvpOiNzdf1JTfG9DQfvAr3VP9Dce0m94Dspv1qI9YVH1FD8ZX7RHpxB0VK7URtn9jt6zC7pum8m1x2eqndLFtl4sBeoL5ZEInuMkajhPeLkZngQM5u9AT0l1Uakc0pznDBa3nLun3EuPoum7zN2iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=tUy7ZbWoNEnCIweL1CAyYECAbErVw6ak-xZ-pxGfJC2-133oujUWGPd--y4uvDD3FKPgLppzgj9EItU9FpqqLrgpRo0l7wzPRozHw_9CF2VYuT58lUyahImARhG4HCUs4xnseBgZlgxMHP7YJwGpW4m_KGjIe0ogLNgJnxi9t9749p3sqNElCNQ3FveKcf_f4yvpOiNzdf1JTfG9DQfvAr3VP9Dce0m94Dspv1qI9YVH1FD8ZX7RHpxB0VK7URtn9jt6zC7pum8m1x2eqndLFtl4sBeoL5ZEInuMkajhPeLkZngQM5u9AT0l1Uakc0pznDBa3nLun3EuPoum7zN2iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=qpHs-99b-K0jDxp2lzodE2jY2nwB4byA4vGK6n_n6fCGHYvi2ufKzQxYNaiM2rTwbUatv66lJEDY7SpQBTj4NGKZLQTXMHN-TdK6jxuoPZSavzFt4mfPaf1oUjKdpHHD4PpvmZX20gDtiTBJtKHCtj8vzUpnyEtUD2oMmJJfVBKuSG3WV_cS0I5ZxQabD6JRRNhBvHElEFMST_DJS-_Ef_29l35T1RCa_vO0zyiR7CMhowUDcO22fAeXT77jRGb4keXxj_FR8QZzM17UF-YkYyCP3hsvoZ1Yg1QuMghsHdhvw5HSEY2w66dQ7oBJdjJtimkoXVWaNQTyul7hyqGjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=qpHs-99b-K0jDxp2lzodE2jY2nwB4byA4vGK6n_n6fCGHYvi2ufKzQxYNaiM2rTwbUatv66lJEDY7SpQBTj4NGKZLQTXMHN-TdK6jxuoPZSavzFt4mfPaf1oUjKdpHHD4PpvmZX20gDtiTBJtKHCtj8vzUpnyEtUD2oMmJJfVBKuSG3WV_cS0I5ZxQabD6JRRNhBvHElEFMST_DJS-_Ef_29l35T1RCa_vO0zyiR7CMhowUDcO22fAeXT77jRGb4keXxj_FR8QZzM17UF-YkYyCP3hsvoZ1Yg1QuMghsHdhvw5HSEY2w66dQ7oBJdjJtimkoXVWaNQTyul7hyqGjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ro2q3ZoOw2jTxEP3Hsbf6-Kd7gMlVa0Ec2hKzFsc4cj6WghOIVODbQlCC7XW94PhgLl2M0L_tiRXEhwm5nD7fe7BznC1QvGnluivf-LXiHJV6Lhr6E0tXdqquKt5JtHB7ZJvmEs6Qn9pZ1xmOTqW5Fb7GL2yOJxDD28c6_bh1X3ndIkLkNg1Y24Lhrvagy4VfEJztdrhmgkLgroqCGZN0MAJN1UqIbvWwLv2dELg_CzmU1JrbayUQItMng8OKBGueKzOtpi4RoHuqU0H_hpElAwqYTTP3edP8kAEhns0w3rOp0RgzePSmEgESivQrzS_hWjOAUY8uwEpxa8CeOY1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ro2q3ZoOw2jTxEP3Hsbf6-Kd7gMlVa0Ec2hKzFsc4cj6WghOIVODbQlCC7XW94PhgLl2M0L_tiRXEhwm5nD7fe7BznC1QvGnluivf-LXiHJV6Lhr6E0tXdqquKt5JtHB7ZJvmEs6Qn9pZ1xmOTqW5Fb7GL2yOJxDD28c6_bh1X3ndIkLkNg1Y24Lhrvagy4VfEJztdrhmgkLgroqCGZN0MAJN1UqIbvWwLv2dELg_CzmU1JrbayUQItMng8OKBGueKzOtpi4RoHuqU0H_hpElAwqYTTP3edP8kAEhns0w3rOp0RgzePSmEgESivQrzS_hWjOAUY8uwEpxa8CeOY1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf3c6XVuBtkGxsGKDQsd7Be1SB8sea-w9u5oBeo27olDB-rUUYr7Im5-Q79xq5hWjT8UBWqngJwVnExA5YBPMPHuoJXrqOhWLk7Rxfi7nrXtjFvTrpSwl8OxuqIpT9-202W41mvQVqjhpTPa3mbSAtwZtUYSXhBnJuCGLreBL6j3PQmMNE-1ZmjAtMa_WwGZr3YSUJJ--b6u1IW5NnaHEfEKoLotLqnHwZLf5pFCdqxEtyds9yETMRmthQ3Y26U1arWZgTvp2RUn_oTcvuXobfht-56eq0cM6Py8sixX6fRTiqk0ha14hR6ZntksIJsJXaGG30aJxeFIC-tPskNXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKqh8WCxqZ0SSrTVVoRyZrESI-ETxSJdcKJD-eh4DrFdIuO-9K7rxNlCT7F3PEpMCBp5f16cKivG7MKttwrllsoH0uPrQ_zLnGKBcTQgfYkMBztbLf2AsO5J6zRLE3RpwETPoMYxmhKSI9ZaH6ICGgF-h-lioraX-khTg3v56U8ufp2csYBDhj-dV2KQXTxCEmUBDYmyQ4IkU4wS32vZ8fZc0p86rMY2DKmwQHIX310dQ2oxpllCnyXvXEfwht8q_lT-hSvgB8k1QpNZ7MYcC8vmMvgO0X_X-LDE6xV6QVycV1QbafXjlL2bJxpkz4KaLUciSq70jFP31LFXV5aviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=VHhJe3y3djtwFo0OWs8zMNKfZvPcahEZEbhuPyLGMB4nErdfCr8ikyo5oxuW4zZR_G7vpfWkc8BiQ85-wq5QSsGx7bp4SplAwmbAItkAtdCeRyDHR5n-qtjJmwtj_cGqb3NXoEqliPyvhcxRWoblPvObK5mBHgysp8HVdLjFZwbnnRU7bSlnOdDi2R1IuhROtxO1SviFE3T4tRKQTNCTHpv2mqkFwEd3HedRGTJ7YT2td-n4OjoO7_f6wPzKvnH_b_Yzg2wRW1QE_nBT5mI-9Cr5GyDY-TBvBqmSMiL3pTxrjGdMLFWiuac2YrtPOM4KDoQTfq22tX8ghvFNkn1w9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=VHhJe3y3djtwFo0OWs8zMNKfZvPcahEZEbhuPyLGMB4nErdfCr8ikyo5oxuW4zZR_G7vpfWkc8BiQ85-wq5QSsGx7bp4SplAwmbAItkAtdCeRyDHR5n-qtjJmwtj_cGqb3NXoEqliPyvhcxRWoblPvObK5mBHgysp8HVdLjFZwbnnRU7bSlnOdDi2R1IuhROtxO1SviFE3T4tRKQTNCTHpv2mqkFwEd3HedRGTJ7YT2td-n4OjoO7_f6wPzKvnH_b_Yzg2wRW1QE_nBT5mI-9Cr5GyDY-TBvBqmSMiL3pTxrjGdMLFWiuac2YrtPOM4KDoQTfq22tX8ghvFNkn1w9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJzI9LKSmCJM9Jzl32sDPYp4I2BCsm8VTKZB1JHdkuRyCHW2s4_lHEmW5BW_u9um9IMHFD-w-_jW-LrH9mE5ubDMlNJnXLoGlLI9AjEljdc1dvJ5l_lt-WY7xei2BOk10c2IM1JnvaworxZcriUfzmFLHXMuLFNkYHkLAQ5dpORYVEd6xyNsdqqcBclRCHMYcdcGsZHCESigO2Sm6eOE2KnsT2sMXvHtNINqbD1WxNjuXYuwz130J_SD_UDcZCfLuylPfojUPxalq8zjrNlF2wekia9tMgopoqhep7V-t0t1xwwbMUoJJ8LQqNN8hvZSyAj_ug5NCqUENP3QnSN4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7QYrK5rrKvfIHuTVZ7JTZ2pSAhm1zlyhPDIHse1c1YoCf_1LvvaKrmM2mVzpBbE5YzVKMxQViUPJlXbNrCTSucD9Uy3fCRjIDujCRnt6AELyW2uf77eRxhGKeT8yj0Zdy7p-d2MfO5K8rhgQtO3SEqFn_L8SjnEsJgTuBeTVqAbadN3QkRkuH8UUWnBLMODIEyU9Z0vUqCLlrNu-Y734RlbYVnCqZURZOfjfxV02XNfz_hxq0fMJerjhjq129yW2Bf1pbZ6lF308MlyE-4oF7V6XLYrGiqrgAW7SHTHVhLuAH4u6AFRoRH7QiLlaMogcI8enfWZJQwdx3Is3tdWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cmOqHeNESjSjlfQQWfityaMrrkh9dzdmYbFi9wfkiD51B6fj9Loj1wY8GpjQ7GN3Uii59ShGw5jwfHKvO7ZLP8WkIog_5Bu0C7TxZuhqiznWD0CVWaSOUw3TQpg2Apo2c0oQI09FO__oQ4UsdfCESkBGO3EIx82F07o1zl3vXxcUrBfc7iT2cx9MBM8oeyCh2X7Ip8MlVM7z974J3F5Vb4D7mzzya0M0BcNAi6WRCIDLKc1p78ZIbuxH_7V3F9bbHibg7FK5a_Me5tQX6WMYex878fiaLvgeMqOsIqLUhgq9_zdIR12504a6mWgRZfX-oZdbZ-ewkCktgTtIFjPJxiea7D-IpPxTbRtUUhaCUUyQ_h4ATW9z3XPoO62Fh6OMKNpqKNmIlUA4tZ043CLjUwDgPCG_0AlhrR-0Z_y6Q0pUvTXf0ADAk9Nr_yaf_-omJpDv-h-4IYHexn_Iqpg27ETSnhPNn6wCpU90Vr7RAER_Y1BCzx5Jzz4K4Kn-vRJGTo33PRlW1AYyIaV-BJ9y3QAU3ctAOSjT9KpMAzfswoBsMQA8537b4hp4E4Nzf99BPolK5OCU2B-pyXMjEE7IMASDFa2gFBm4f1JwfSKqMNE_Qs5QU657Fyx6S9o45ayDGuCp7YL2wtVeloosb774mL1IpICP9wtr78E28EEe_rE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cmOqHeNESjSjlfQQWfityaMrrkh9dzdmYbFi9wfkiD51B6fj9Loj1wY8GpjQ7GN3Uii59ShGw5jwfHKvO7ZLP8WkIog_5Bu0C7TxZuhqiznWD0CVWaSOUw3TQpg2Apo2c0oQI09FO__oQ4UsdfCESkBGO3EIx82F07o1zl3vXxcUrBfc7iT2cx9MBM8oeyCh2X7Ip8MlVM7z974J3F5Vb4D7mzzya0M0BcNAi6WRCIDLKc1p78ZIbuxH_7V3F9bbHibg7FK5a_Me5tQX6WMYex878fiaLvgeMqOsIqLUhgq9_zdIR12504a6mWgRZfX-oZdbZ-ewkCktgTtIFjPJxiea7D-IpPxTbRtUUhaCUUyQ_h4ATW9z3XPoO62Fh6OMKNpqKNmIlUA4tZ043CLjUwDgPCG_0AlhrR-0Z_y6Q0pUvTXf0ADAk9Nr_yaf_-omJpDv-h-4IYHexn_Iqpg27ETSnhPNn6wCpU90Vr7RAER_Y1BCzx5Jzz4K4Kn-vRJGTo33PRlW1AYyIaV-BJ9y3QAU3ctAOSjT9KpMAzfswoBsMQA8537b4hp4E4Nzf99BPolK5OCU2B-pyXMjEE7IMASDFa2gFBm4f1JwfSKqMNE_Qs5QU657Fyx6S9o45ayDGuCp7YL2wtVeloosb774mL1IpICP9wtr78E28EEe_rE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E62ZpXbmXaX6oI3aiJ5Y8zc6sDMGnz6CxAa1cdmOAV4ZpKIFw3e-laf6PRhZjC4F7x9clMtztmajCzd-v0dtQiAappk5wNAq1fL7a9HSu6MAiS3cqnU81qrOeeJJk61SDtTz1XnStgNLwrBZCtN_rF-8pYz6yQk0ex3ijhn-GEFr5CAX1eg5y1ppav3F5QjtYxQ3wUednIvykud_yHHhGeZ_9YtCQd7K48okzVdX8ipDGKfV5L1ZrftNeOT51vRMFTxyOE1CVbCW7WaldqoFtSjZlWbQRVT7bNQjWCaqWLBB6n-K_Gd0kpbnMowsiUVaTvJ5NY95hD1b6TyAnV9hM4Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E62ZpXbmXaX6oI3aiJ5Y8zc6sDMGnz6CxAa1cdmOAV4ZpKIFw3e-laf6PRhZjC4F7x9clMtztmajCzd-v0dtQiAappk5wNAq1fL7a9HSu6MAiS3cqnU81qrOeeJJk61SDtTz1XnStgNLwrBZCtN_rF-8pYz6yQk0ex3ijhn-GEFr5CAX1eg5y1ppav3F5QjtYxQ3wUednIvykud_yHHhGeZ_9YtCQd7K48okzVdX8ipDGKfV5L1ZrftNeOT51vRMFTxyOE1CVbCW7WaldqoFtSjZlWbQRVT7bNQjWCaqWLBB6n-K_Gd0kpbnMowsiUVaTvJ5NY95hD1b6TyAnV9hM4Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=cLXgIs_JTyGF9S7-R1fV9nRGGbpPo2Wpsc7smIzhrjHE-1EAERElOFLXSSQ-3M3gJlEuT7job5GxFCVMu2F9hGU9uxkx7o20El42hM1frZamz0AX1fHLhxezRrtI6jMw_vwLh62_lUofQBd0mQABjWyJksxmRkBIGzNkZjiI6_92HFPJTweoesWcFJDkrjdYIWoi1pBpQkU2lNhjj30ajX4t7LzLlEPQIeh4w5xVbohh6_WrvVA4tTa8Q8Z8jWRB5EF3PACm60USQ0xNWfQcMQC0zAnVg5vDWBveqVypxKOhZ_ZrPZLLKoTwPI6sEmfk556iyQ-JrnAgNgtNfRnjL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=cLXgIs_JTyGF9S7-R1fV9nRGGbpPo2Wpsc7smIzhrjHE-1EAERElOFLXSSQ-3M3gJlEuT7job5GxFCVMu2F9hGU9uxkx7o20El42hM1frZamz0AX1fHLhxezRrtI6jMw_vwLh62_lUofQBd0mQABjWyJksxmRkBIGzNkZjiI6_92HFPJTweoesWcFJDkrjdYIWoi1pBpQkU2lNhjj30ajX4t7LzLlEPQIeh4w5xVbohh6_WrvVA4tTa8Q8Z8jWRB5EF3PACm60USQ0xNWfQcMQC0zAnVg5vDWBveqVypxKOhZ_ZrPZLLKoTwPI6sEmfk556iyQ-JrnAgNgtNfRnjL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=hTDFVYqO0o2V6ewTsG1hJ3345V90NSgQJCJRRsyRXgdAI5wNCH7ftYT7ietZmsfVXcf_xmwF0Y1W1o1XrN1GKbjWwhmUObQXbBDIkg1swqRnOo_2sQZE6XbDT8Tk6KEmUH0mDXgaB0OVHMaoI5qVgWNoiNRnwtf7cmTn_ktCuInrlKe_WPECUgcyiNx_fn1FML-qTnRE9vO-CZr2DC3NsyXlV0gosdwTevA_6K6Vfb9KSvFRI1ZP8eRVTUP8f47JnbS_-v_BzwrwKzTvhs_ejjMwFs-buHzmMKkQVgOGT5Qknk_Y8Kq_BLYR4bL8LwC4cGL2NNlnKmCyHFOo2wUFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=hTDFVYqO0o2V6ewTsG1hJ3345V90NSgQJCJRRsyRXgdAI5wNCH7ftYT7ietZmsfVXcf_xmwF0Y1W1o1XrN1GKbjWwhmUObQXbBDIkg1swqRnOo_2sQZE6XbDT8Tk6KEmUH0mDXgaB0OVHMaoI5qVgWNoiNRnwtf7cmTn_ktCuInrlKe_WPECUgcyiNx_fn1FML-qTnRE9vO-CZr2DC3NsyXlV0gosdwTevA_6K6Vfb9KSvFRI1ZP8eRVTUP8f47JnbS_-v_BzwrwKzTvhs_ejjMwFs-buHzmMKkQVgOGT5Qknk_Y8Kq_BLYR4bL8LwC4cGL2NNlnKmCyHFOo2wUFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOs6QiXQm3_u8CgntmZOcRZANiihx4vNodygjtaxH91H0mzr5xX8oxO5vmqv_ZOz6zS-He2CLbLb94EI8DkkadBy2cKxjSp2FPI_7xUfhTS4lK4PFJ2Q_FHjGHIU6w5k1OBfXkc0peOjk-3GvpqQ6jCWiodeJ8In-Au3vxcWaK8xVYJ5sARuqEUuUIcRZ8Yu4F69oYPFBdbKzoetqOlXyn0JLw2oXbWsbz85K4PPFmkOv7RET-Tvj4bsG69Nli700vxUiNbXve40zbX2Fc-zWen08tLsLrufG-DWFW_5PrlDXlxtEoppNmSCxLp7MAOFcPxX4RracYp7IbD68sjnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqRXrJslm2K--sCUYjjLIQJByXL9abS2YXKwCLcT8Fmi1b-k9tBFS1XuLamN9CGQxhKUa_8DGhbxZO-vHzoPtAWEaC8YLbRq9oBQHccjBBWE6LkMYbLkCQ1dP_FTiTwohy0USHwPZUm0L5vN7XM4cYddiPoYDigQ5YlGq_JIl0SLkhn16ujU0mL7x-N_9wSMKR3G2JYj7jAO9iEilSDWl3rn9xEcwuB7UlI7XmRtkrQOP6EqPqPwNQ078bvILmIP0Bb-_R7LYlskl3r4IEZrztBJbraWkrxwD_uErncYvFDFyGE2ECaP2RJyOHvlmXwBi4Dzpk7Fe4dxYBdgH-e-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thcjGCe93omRLz8igi5HmcChbgptFPxTZO8YnSUiy2NEi2yozcBoxGGQkCeWWh8FqLRZria6rq0XwTj6HTtFWBVM-DJt8vZB5L1syDMINFI6UN_SxT-V73_87p_f2UhV7BfZrXBAhFb_oyCXaU-FuYvL5X6VsdT2I-_QLTeasGjhI9og-nHJHLn76bp72o7HtmVvJgGNmHMBhNjFma4LiXZn18R2yuCKAJ58piPyauwLXasNueCHw3ZxNrk5rrCytT7Zc-Wcft2qhP6Nvw5YwdhZMKCqiEtyqDvSQ-d9rWBZZ8ra4d0_lyhcaudWmiGh01W_o3DdTvZ_Dli7xi_0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9nOhOSTRSC_DA-gn91HkI8hraJGnqJJhLfd-ua1eOyzH_Dpn6QjuXffTjL1WeGf_gUrHumkqQ95862SsX7f2WL0Vz1aJZHlXgBNh1KXI5x2HM8cj0FwX40MFE_Mp2HOXhQZxMjfQYHHnzaTW912tMEw1bm7MLcY6KgHuoSQXDeb-0WFX_PON6pLft_hE3ncVLxFjscQq4rKzafIJpsmxJfx1ZENVFFglHLdqfoAvo-p2PiaEQkE36PhgkQIYd-2eveW9LMvHgp8y5mf05RpLX3yfYGYuHhLn1le1JykIvQ7bHDp3iMty_1_F9WjfsyAjjl4kgPyyu1z-xhMLZj-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
