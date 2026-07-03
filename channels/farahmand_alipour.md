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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 21:24:38</div>
<hr>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwvQxP7MWyGOP7Jy4AhvuaJFv9Hb61w4gpKTyBcBF6F7t1GtOXMxj-_GiBON2JVB_wwXTWfP6bDTk-g_9EMrxsq7f4sDpL2a4Ire73jXSh8akgW3hVulH-y5j7B9FXJNW4ZVZ7cqiROawcm3MNzNXVeyOxLhOmqjCm07SuFHzf82FBA2w1esHrBZkXggWWmJ9P0dZLCHUJ57ZK_1ha-X15pOKZ0lwfDLvSGeW2NbXdhMJTfg6gC3wj-OZwe4gOjgAFOTqQGiLWAjQqja_cc_2EzaMzNJ5E7jb9R2gIRvXHXojHyD1dPDBXB1vtrX8BWLbCyesP-hr5B6dBsgfy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=v8qSdGD14Onic1sJ1CB0hiprR5DEnlFQ3lS4EdO1ZkdnJegnuewGSLOeHWSRDDTClQQxkyD3mt4TsQB8S3a7vb0WbsnmN9YtBsHt9_lrIMWHXIRhImCYz-ZgDtgUDH9UvE6Ld2MtmDfdDzO2GLOGu1odHT2wu5d2gR7a8CII-Qr96eNXtZWCbJN-Ce7Ni3Qy5BchdVNimoQxdTG9ryxdqrZMajdsp599bgAgSkttTrMfs5axTTXQc3n6WCcDqdtJHTOUBJoV1fc9EjW15nv4lFx-ZTNg1wUzVbEUFPwypfh6FjomDvjmTNoNNwbTUCdwTVacQQa11PbesPAA72qi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=v8qSdGD14Onic1sJ1CB0hiprR5DEnlFQ3lS4EdO1ZkdnJegnuewGSLOeHWSRDDTClQQxkyD3mt4TsQB8S3a7vb0WbsnmN9YtBsHt9_lrIMWHXIRhImCYz-ZgDtgUDH9UvE6Ld2MtmDfdDzO2GLOGu1odHT2wu5d2gR7a8CII-Qr96eNXtZWCbJN-Ce7Ni3Qy5BchdVNimoQxdTG9ryxdqrZMajdsp599bgAgSkttTrMfs5axTTXQc3n6WCcDqdtJHTOUBJoV1fc9EjW15nv4lFx-ZTNg1wUzVbEUFPwypfh6FjomDvjmTNoNNwbTUCdwTVacQQa11PbesPAA72qi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #98</div>
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
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyF_JP3qdOXU2uEvAUl91kSTTiUKm6yREMfkkLHgh216Ig2JK1GZCuyDtgd1vLv8ylnRQutIA3kxbww9-iywomR0PTGxZjSpJDAfgH_ZCqpa4MKYdBFHsId3X5Yl-A0W1Qvts7KcFQZ6RxEeFD2PV2ghZm3Os67MaAKcTb_DLLH53rp1w5cdOe6meTA2eYDcFumTA16Egk4CcXrCobzh4AQR8K0SL2RL3-WevpUWFqChucfESKkD_I_8nDyd-N6MsRPwG5aQPGalH0B9n4TjQtbLe84D5nVrkeOmaEC8tSoGIQ4jc2_PmIygI9PsZXlbaBpjUN3FAlgerQf9qLfPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3hHkNgPFzNdSS8f9s9MUj0S-Y4JL8_ZbbnhM7K_2WsWprViTTJssKFTVygZ1WOg9Ga34OjeFOaZ_t6sljnFjHshev-OtrSHM40-G1uAaLMedmnmuS5k32w3Kmq2MkG-fPvLRYm3a4mNmR5bZx1sLKwu9vIeUySuQOzEdUfd5JWKyKFfripWufCrfN2UCqv2sFOPXA3h0jyGa0ZEmzsm9hyyQC_duC6fRk283uQ8DseSQYTJk7X6i-rjnsFOPMN4eY3uE9zoLGKF0UddlPyzT60cvOEOddVLCe-R-xKaLEJUtdl1kE4A_ewt43KC0HqWD9qhjUVSFwJjNyGlmHXipg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=J8LOXhRSytnGinKSUZNgfHyXSSn1LzwYWx5b5aB3AMM2vxLqUnfHvYXJwTB8qJnPeg5cUw1hHf4ot9AnScGVeQiXZh6_zQXpQRjlKIg4qWhHVc-fzM9Tzw62WaoQsRVXFqLyoTIz-GCmfes3QkXxiV5N51l4DC0DK7B55sLduqcH4_B1Q5V6hoLwRSvORsTiXR-Puf8ptBB2tvky76RG4U_LNsk3wrpPBYFVUTtszePf-9OZQFh3eDZlbYI8YR-V5nnyvPEj1qLYCwrHY5Ijjxd9NbgCtvkZWwWU-u79SFZOkq0eNYqU36M8z5a9zkv0D0U20O4KKBj3Wo8TfIqtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=J8LOXhRSytnGinKSUZNgfHyXSSn1LzwYWx5b5aB3AMM2vxLqUnfHvYXJwTB8qJnPeg5cUw1hHf4ot9AnScGVeQiXZh6_zQXpQRjlKIg4qWhHVc-fzM9Tzw62WaoQsRVXFqLyoTIz-GCmfes3QkXxiV5N51l4DC0DK7B55sLduqcH4_B1Q5V6hoLwRSvORsTiXR-Puf8ptBB2tvky76RG4U_LNsk3wrpPBYFVUTtszePf-9OZQFh3eDZlbYI8YR-V5nnyvPEj1qLYCwrHY5Ijjxd9NbgCtvkZWwWU-u79SFZOkq0eNYqU36M8z5a9zkv0D0U20O4KKBj3Wo8TfIqtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=HlsBckFh-rG3La0hBGFpcCkjTf9qH8Zdpc32Q01TPUHp4mjlDummOq7AH4D1lqpO-LLiIWq3lW1RIVuh8dt1RmzUVYApWiKdY2Yl0ZR3VrSaUjlDkWbN5EQlWAkKyjkb4WgSd1VG4jZKYL4aEPXYuVZIp0IcU25dJzwaU8UHg01nebz1_U-BmnBNR_XeJwwwnVMMZ52LJOMGcP9_8wc8dpN30W2oXA-6JyvfqbnM7FmRHjlIGNqmgnpq_5eS355gQQSGWYUZRsI6UN-KqwmgsFZlpH6gXdpvK_MB6VoHidM4me8L51oduBjB7uBqyp9VWsPI1vzn9zc8NXmAAzh8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=HlsBckFh-rG3La0hBGFpcCkjTf9qH8Zdpc32Q01TPUHp4mjlDummOq7AH4D1lqpO-LLiIWq3lW1RIVuh8dt1RmzUVYApWiKdY2Yl0ZR3VrSaUjlDkWbN5EQlWAkKyjkb4WgSd1VG4jZKYL4aEPXYuVZIp0IcU25dJzwaU8UHg01nebz1_U-BmnBNR_XeJwwwnVMMZ52LJOMGcP9_8wc8dpN30W2oXA-6JyvfqbnM7FmRHjlIGNqmgnpq_5eS355gQQSGWYUZRsI6UN-KqwmgsFZlpH6gXdpvK_MB6VoHidM4me8L51oduBjB7uBqyp9VWsPI1vzn9zc8NXmAAzh8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=PMZ4AIMwMfy2mGqaeYrDa_NC8iQRkrE3BqRYmiELDSfTm39rsAFVVpJ2O1MJzG_IYKf0ETEruaCRlRm9nlwX2yAWbXTPYCa8TTf2Jq-2azq1UehFHm6IuBFePuzB84w8PYMvmUJidHCh2Kz4Ihr5sVI9-4eCu1fkgk_MUqLwjCQ1EEWyawxvjEMGM6h5qn8iaBIP5fgNBI_vmta0xFm_wZaQ8q2VFtAUwXHow1uVYzfA6yUqCTMA1qgT310OOmESLdZuMwtV0iobQtmKcx9nvpVHScQppfl1Qp5o_kGOe5CafmiUfjmrmGhVr4udUlqC90dyhEkKO6tg7_X-ag-tiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=PMZ4AIMwMfy2mGqaeYrDa_NC8iQRkrE3BqRYmiELDSfTm39rsAFVVpJ2O1MJzG_IYKf0ETEruaCRlRm9nlwX2yAWbXTPYCa8TTf2Jq-2azq1UehFHm6IuBFePuzB84w8PYMvmUJidHCh2Kz4Ihr5sVI9-4eCu1fkgk_MUqLwjCQ1EEWyawxvjEMGM6h5qn8iaBIP5fgNBI_vmta0xFm_wZaQ8q2VFtAUwXHow1uVYzfA6yUqCTMA1qgT310OOmESLdZuMwtV0iobQtmKcx9nvpVHScQppfl1Qp5o_kGOe5CafmiUfjmrmGhVr4udUlqC90dyhEkKO6tg7_X-ag-tiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XTlNpAt2_3ZhIkO1dkDvWsaFqPvUNZnT7BG_Dc3Hmyo9sCHa6Fk7CtUeSyRof8UQZIidnF3vDBK0cfBQirQ37mbaCNGlXrU2QJtsZio4azEHgY9aAZiH_o6OgWRThU2m4Lj68CJKmO_iiqMIhjVUPpINmb3HKAIipxXZu-Pu5nzyd7vtv8G-5A3hA3FC_cEcGBgQjRbaLb4ZkwWCQ6Q2kTkaHNHq1mqEKVyVtGmK25vQoJEoN6-gIuPbTGwxbyw8Z5OlmK_dpAPy9AN1nRvVARdGh1f5hbITYMqVcbRU8vahP60URCnohmmSFHtnbepUN13o3Y782hXodCI-vbZvog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XTlNpAt2_3ZhIkO1dkDvWsaFqPvUNZnT7BG_Dc3Hmyo9sCHa6Fk7CtUeSyRof8UQZIidnF3vDBK0cfBQirQ37mbaCNGlXrU2QJtsZio4azEHgY9aAZiH_o6OgWRThU2m4Lj68CJKmO_iiqMIhjVUPpINmb3HKAIipxXZu-Pu5nzyd7vtv8G-5A3hA3FC_cEcGBgQjRbaLb4ZkwWCQ6Q2kTkaHNHq1mqEKVyVtGmK25vQoJEoN6-gIuPbTGwxbyw8Z5OlmK_dpAPy9AN1nRvVARdGh1f5hbITYMqVcbRU8vahP60URCnohmmSFHtnbepUN13o3Y782hXodCI-vbZvog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=UL1FcaE7eEZ6CTmdc2m96B2LCsDp-XeMYn3unF72NZmajJQg2c4vfuhPGcjUiGo8bBE_PGbgjiKnWMKj19q6el4Ba-d6rTFk6YXgd64aIonckOJ3a-ct8xLXOKVKdJeCHpa2dy8XaCB2OPsE_ZwkdKC3gV5xTfYNDIn6I1dpmubMP-YHyZjdrzkb6ZSmZYb_ET6G7kQlJlg2sWADBQXzKeBFXyGCZ9DqeSE50MfE113OY5Smi6WxhmCEWCfM6Ujw9FzGqQajP3IpyKxibUF4P8xl9Khk0BpNpHg-_-o7rvDEhS8avd265zV-_iR49bBH9KLYtneFM0qsD0i0_eVqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=UL1FcaE7eEZ6CTmdc2m96B2LCsDp-XeMYn3unF72NZmajJQg2c4vfuhPGcjUiGo8bBE_PGbgjiKnWMKj19q6el4Ba-d6rTFk6YXgd64aIonckOJ3a-ct8xLXOKVKdJeCHpa2dy8XaCB2OPsE_ZwkdKC3gV5xTfYNDIn6I1dpmubMP-YHyZjdrzkb6ZSmZYb_ET6G7kQlJlg2sWADBQXzKeBFXyGCZ9DqeSE50MfE113OY5Smi6WxhmCEWCfM6Ujw9FzGqQajP3IpyKxibUF4P8xl9Khk0BpNpHg-_-o7rvDEhS8avd265zV-_iR49bBH9KLYtneFM0qsD0i0_eVqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sYjAyA5tFZGsmaZIO8tiUW5vunEAufkP8P1rGTJV_tc7U0tWX78lHnvCLm3jCaG4MC72mHXjwQ8UMWWeJ4VK1UxoLPIxrcmC2aM1LydlgvradcgoatLuKxBk6-OjsKpks9eec8CbXW8m0qNhxsuQtBaD-jxlhjLGtyI3mS4fyIax0GZUUAFCNcmVqMOqwLAdIKHuXNrMQIv-oJA6AREQStGipFrHQYqGnjEzydhx-wo5fJqO-ydM49xcrrNavBMMUaNqzRUV_DNfDdmqXIPHPv_2u1NvFpr1_nGNR0jyahsAbrayKCH6Oc2PGGLdZD6cJhW40kNs6ojTx4oFNXcXJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sYjAyA5tFZGsmaZIO8tiUW5vunEAufkP8P1rGTJV_tc7U0tWX78lHnvCLm3jCaG4MC72mHXjwQ8UMWWeJ4VK1UxoLPIxrcmC2aM1LydlgvradcgoatLuKxBk6-OjsKpks9eec8CbXW8m0qNhxsuQtBaD-jxlhjLGtyI3mS4fyIax0GZUUAFCNcmVqMOqwLAdIKHuXNrMQIv-oJA6AREQStGipFrHQYqGnjEzydhx-wo5fJqO-ydM49xcrrNavBMMUaNqzRUV_DNfDdmqXIPHPv_2u1NvFpr1_nGNR0jyahsAbrayKCH6Oc2PGGLdZD6cJhW40kNs6ojTx4oFNXcXJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=O7G5ak5clmbXsLkSOGYHko-0nJ4llfgHKc5YYZQ2iGfbXMlXT6zMbnwtj0g4TP12o1Gl7UQwgx0vysEDBpo8ONxG031PdJ892JwwuCCNMvQ_E_U66b0K4QPnb_Cp1zFXwA5_o4_7qXX6cwngbhPT7EE6ri-uWd-dODmZJOBXQA5j037hM85dUeCNoLF2o_6Aqic3bGdi3HJCKI-madvPS1UqtlVyy7toxQAiMS-LJByPlt2OQ5v8xoUeMiT3AobQQ35qEi1ydKMZ7TBEZeHfPeGZ92G7Ua4S0NoOLgrIT9ewp_34J5Kc3gJ1vjmjGezmqTYPeirh_sUr5-xfMiIolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=O7G5ak5clmbXsLkSOGYHko-0nJ4llfgHKc5YYZQ2iGfbXMlXT6zMbnwtj0g4TP12o1Gl7UQwgx0vysEDBpo8ONxG031PdJ892JwwuCCNMvQ_E_U66b0K4QPnb_Cp1zFXwA5_o4_7qXX6cwngbhPT7EE6ri-uWd-dODmZJOBXQA5j037hM85dUeCNoLF2o_6Aqic3bGdi3HJCKI-madvPS1UqtlVyy7toxQAiMS-LJByPlt2OQ5v8xoUeMiT3AobQQ35qEi1ydKMZ7TBEZeHfPeGZ92G7Ua4S0NoOLgrIT9ewp_34J5Kc3gJ1vjmjGezmqTYPeirh_sUr5-xfMiIolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdU_YwtD6reIXUCj1bbe84iXObVKY9dyAciLvq0WjyDkT3M8t-G__Ef0Y-CF_c3dush8jeLBgQ0IOCwaUYnwKzwxZ2PfoBGcV_xLSXV4mCpJU1KyPhdCHk2bN-NTlNXnJle_Pyb33bGSKIBrUboE-zRmjgOgfSVL9bfPd3dpCCX7HE6SYUebbIeudMPQOLVYaSdqowyNFD5QPYqMDGd7FVR0fItYCJx8qerz-stTWe-EY5iIyzHZJXLlna-BkqidK8HWVTbq3oWpkhTpnrMvGMoV2FPIYvp67pFCcUycbHA9z9q3YImGneb67H6r7iCd4buwpE9ESbR61q3g8zHGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ovblJHBlw99ynkGsZbAJhPCTGnbP8ycWsQlIvwDAy6YTKtn1kbgCilfZrh7VHTsx1lU4z0f7BJuYF6zVPKt4aJ0opJKVYM47sOg3tQ-SNJ00T2K1PjlHPeSYtqqfYA0ggAzkr1qk_a9sqJwFEEqNtqx9ITfuSXwoF4r52OMnKPQbxVA_rDnwcVPak3qzarBgFecL4H5PoAifXKCGh2lEpwvYtpbz1EC_bnWpidmhLOQ-kypNWNY3QQO14GFCgzNiXSJKuAWZal3LloxMfyNlJr8rrM-hPX2YV4jovl7zdsakJkhwZKmw0kS21eba_jmDK6TNOzoeBuxuOqujn1oO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ovblJHBlw99ynkGsZbAJhPCTGnbP8ycWsQlIvwDAy6YTKtn1kbgCilfZrh7VHTsx1lU4z0f7BJuYF6zVPKt4aJ0opJKVYM47sOg3tQ-SNJ00T2K1PjlHPeSYtqqfYA0ggAzkr1qk_a9sqJwFEEqNtqx9ITfuSXwoF4r52OMnKPQbxVA_rDnwcVPak3qzarBgFecL4H5PoAifXKCGh2lEpwvYtpbz1EC_bnWpidmhLOQ-kypNWNY3QQO14GFCgzNiXSJKuAWZal3LloxMfyNlJr8rrM-hPX2YV4jovl7zdsakJkhwZKmw0kS21eba_jmDK6TNOzoeBuxuOqujn1oO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=cU3wmDS9HMr2QHAklDrzcBrOxOFBqxzfULQaxgekOBG9kTMhv8eSGAFWNucqJTofuQ3VZE8hf53WGLdy14Gb8W_UX1zMBrM9OwrDNFBxRPGakdO3MIBBHF0mmfbIU_8E3fiK5e1di-8PkKG0A-QxHHWs4TrE-WzNOA4BFWXXYjfPGc79R2p0VP8ZtXkuTtpsFtM-RdKgxh5NN9czmGuuj_M_2DHZaI2H6Llz4w6NgM681ru4u7hOrn4rWWIARRr1Q3oTDKNaYml_Wa_SGuvRJD741Lwc7dIzgqbPvrmtCBZY7NdAUWPuDTdN1Af9Kuca9XHYW3dj8gjyV14i_PcA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=cU3wmDS9HMr2QHAklDrzcBrOxOFBqxzfULQaxgekOBG9kTMhv8eSGAFWNucqJTofuQ3VZE8hf53WGLdy14Gb8W_UX1zMBrM9OwrDNFBxRPGakdO3MIBBHF0mmfbIU_8E3fiK5e1di-8PkKG0A-QxHHWs4TrE-WzNOA4BFWXXYjfPGc79R2p0VP8ZtXkuTtpsFtM-RdKgxh5NN9czmGuuj_M_2DHZaI2H6Llz4w6NgM681ru4u7hOrn4rWWIARRr1Q3oTDKNaYml_Wa_SGuvRJD741Lwc7dIzgqbPvrmtCBZY7NdAUWPuDTdN1Af9Kuca9XHYW3dj8gjyV14i_PcA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=tIKbT3kdSOcqBqqiBWwWlur6qoRIXvmzysUXL7WIcdAoxriiMwOMcpbDeWaMToXYgmYmPOdSUAnEhFwtorXuw2Yf4zFH3vhqKb6a3pM7e_JDKAITrEpPdyy8zIFqslhGWthOiqBU6t1w76BY_gDqMsOatelh-unfzWy1t3Di5CMmYcQnFZGFgQnrelTKY9uKDnvL52zx48EYDlXgsIqcpkCLY1JUoo3ITLuIO7qTOsds89x3sy9wngYJHXsLe21cCSjYBt85aXfn_MGt9-XyAEFttunPPvhaNX-EX405RObBcbzHmB11IG8HEXeUUNCat9U2CQAU5nl1Lit9IqwCyUD2LaoZ6ejizsdyb-3Z7f95H5zTdtpP-OZrv2ptPI8J4MTRYtwPdBDQGb5cuQ_1lDNW6FhJHvItXq4Lbjpv01Mp-4nI7yfItCCflNvcobKm-yvhLHYMRVQMIzISi53Vi241gJvaNSzHjblu1S8ja4znABixr2e-S7nWLvPIcX7_Xc4SWkNfcu93U4WawW6JB3tDLcBoE4eF5agAHgTe6gDBuaczCgu4qBPbqeSUdJV1vJZ88dEeJNqYK7UJ9mnD5fC_WHSTIehkZCMl-fH5N2yMotbxjvlNTqvsdNhAUbjdPrIG6Ea-lzvLVdkTzgaTU31UQyNLRA18YawT_jA2yqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=tIKbT3kdSOcqBqqiBWwWlur6qoRIXvmzysUXL7WIcdAoxriiMwOMcpbDeWaMToXYgmYmPOdSUAnEhFwtorXuw2Yf4zFH3vhqKb6a3pM7e_JDKAITrEpPdyy8zIFqslhGWthOiqBU6t1w76BY_gDqMsOatelh-unfzWy1t3Di5CMmYcQnFZGFgQnrelTKY9uKDnvL52zx48EYDlXgsIqcpkCLY1JUoo3ITLuIO7qTOsds89x3sy9wngYJHXsLe21cCSjYBt85aXfn_MGt9-XyAEFttunPPvhaNX-EX405RObBcbzHmB11IG8HEXeUUNCat9U2CQAU5nl1Lit9IqwCyUD2LaoZ6ejizsdyb-3Z7f95H5zTdtpP-OZrv2ptPI8J4MTRYtwPdBDQGb5cuQ_1lDNW6FhJHvItXq4Lbjpv01Mp-4nI7yfItCCflNvcobKm-yvhLHYMRVQMIzISi53Vi241gJvaNSzHjblu1S8ja4znABixr2e-S7nWLvPIcX7_Xc4SWkNfcu93U4WawW6JB3tDLcBoE4eF5agAHgTe6gDBuaczCgu4qBPbqeSUdJV1vJZ88dEeJNqYK7UJ9mnD5fC_WHSTIehkZCMl-fH5N2yMotbxjvlNTqvsdNhAUbjdPrIG6Ea-lzvLVdkTzgaTU31UQyNLRA18YawT_jA2yqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=NtMsHLGp7o_tPCxElAfN8O4NKqh4bPbtpbO721qjjOucAsXh6dSyhAftAaC2hps76-h1mzP2qZF3ejoTXJnNXV9fo0AxYGgGUXyGtXYUJoQl8lzRuWkEPwTaD9mKo1jABbzFnIlVsRgyMXMdZtX-tXUUKUpQAnUUWzJXMWybAjrsbzM5bxBJ49d3FshUhX1HPyG2vChHTKVftE7dKnAFec9FTQX5s0P--x-2inHDMYjY2_eq2tW829rXSlSIF6Yvd-jTfJ2EbnfyOPte-xBlTDenymTZ6Yn5tI-M1lT3A9Wsy30cJrRJGfJmXjQLo6fnzFbyW15XVHZeLHZLk5NZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=NtMsHLGp7o_tPCxElAfN8O4NKqh4bPbtpbO721qjjOucAsXh6dSyhAftAaC2hps76-h1mzP2qZF3ejoTXJnNXV9fo0AxYGgGUXyGtXYUJoQl8lzRuWkEPwTaD9mKo1jABbzFnIlVsRgyMXMdZtX-tXUUKUpQAnUUWzJXMWybAjrsbzM5bxBJ49d3FshUhX1HPyG2vChHTKVftE7dKnAFec9FTQX5s0P--x-2inHDMYjY2_eq2tW829rXSlSIF6Yvd-jTfJ2EbnfyOPte-xBlTDenymTZ6Yn5tI-M1lT3A9Wsy30cJrRJGfJmXjQLo6fnzFbyW15XVHZeLHZLk5NZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pfx5b9scFiZL2Pbaw8mCEFFvxbRQAK1brQGek7oqF47t3sIr4sBTX7Prrf8rRHnyxo7H0pPpeYW47ECtqaxYKkc-ebiisBHuNJZjMpsgqrRgC3hjUXAXq3QB2eN6N-AU_FD6k85K4PdEnmEuaYAfqji1AaEIKFUc33X1ZK_gmlYZVWyVi43Vks1kEyeWHzvR5oIwNh88sS-KyXffzGnVcOi_MjlrniwkyQhG_etvGaLRd-7eJC6DIZSvqYxkzhwg0sso4f9UPvi99TkGwOuAhOuBRMKO3bqpJaJAH8_MpBDEDTBN-NSs2-PDFS2lJeFM3X1wZT1yaIS3fXzS21CYfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pfx5b9scFiZL2Pbaw8mCEFFvxbRQAK1brQGek7oqF47t3sIr4sBTX7Prrf8rRHnyxo7H0pPpeYW47ECtqaxYKkc-ebiisBHuNJZjMpsgqrRgC3hjUXAXq3QB2eN6N-AU_FD6k85K4PdEnmEuaYAfqji1AaEIKFUc33X1ZK_gmlYZVWyVi43Vks1kEyeWHzvR5oIwNh88sS-KyXffzGnVcOi_MjlrniwkyQhG_etvGaLRd-7eJC6DIZSvqYxkzhwg0sso4f9UPvi99TkGwOuAhOuBRMKO3bqpJaJAH8_MpBDEDTBN-NSs2-PDFS2lJeFM3X1wZT1yaIS3fXzS21CYfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QK9Uhq9r1x8TrYWmYQBq82ZMeLDSYGgn2Hf5k_JBKN6fWLe5c9i40iVcZMh_efkIIMH2WmAkV_kYxVr0sfcwYSZ4qvU13JtK-r6zPfzg-Jb-UWnFxKvPGWx6g_BVDTbThzfDHFlLlpx3q_OXRCnP9wdxYnwCWAuwz3S-YKgVh4acGzC5Ac9z58IM9yN4t1WuB8KozLd6DM5T5myToDvULiOBQTIZeQFW37crR-uSl0ANVgRXQANysnvtN5VvZ9SYqZm8Vv1CwjO5iarHfD8I2Gg-SLNYfOonrd2-RCKAY_eGZ_fQWKYTS1NXHJptj4gC-9WaFtsqEVbAd7x4ZeiAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQa3vhjW-StAGhNzc6SzlRZjFndCGC2lGj-54h9g0c854suotLa1UitfcbP-fv_Wq4qFmqtI3eUT16-GeBzAHJ04sDpLUmiK614u4S5xpHyaE-TAl3smT96zKfKn7VCUgqki5iKxdSD8MA2UzKeU_s_Eyspab2YZ7dB0Rtb_NjxNnd_gN9SoR6-mqxVuxi_uMI4Dw9id15ZWSjhbT9XidciqvDegFEFavoPpvFfysuY7zk3p_RF-roJyYx_Xn6FWRhEgfu4ZXAH7HWV0Wuyn1pZaZ4SrB4hN-PMA33M6v1sOAA3ErtG4SwbRcGPNyJfNRP5nZwFda-Y5b8R0pZRN3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=m__ks9ftTwXoMzJujteH_2G8Pch3WwPQda0wVvKiAEdOg2Es_gWm7v_lCibmztcLwfyeh78F1sn8ddDpu-kadpTb00Y6B3ryfVA13yQxET317YbUuMqLkZe1I90Oomv5Pl3FiCAcOm3OB3InOuM6gcH7AM5mWM9KywMfoJjepKTF-Qu3PWrIICJGb7iBp_oOjjuxS5u9dY3hQy00tKqidb4acC7rHHyB3CcP0oW7Du_6mRFxwREUAQt8-eEo4T_Fags87y3qRIcGdx4dVcyobJW6HriH3iCb-viwcySrbIjfvEPFDzVZY6PT_D2Cung6HajDm76ya179BzfoEOW-k5xAmO5IoqlHrLPUMSAznU1RkZ3Lt3ORyCI-Yl4QyYePV8omUIaWZLErOFh-ZmaPHamPLYLjoniWy_HmTadRgONl4OWh2OpTK4wuMopHhAOTU4XXjs-0OBtcxYvGXPKvETGkOr8KuTBqS6Hn8dxGdVu3Moh47-TeB5JeGTHPF_VAeq9RJnYhhbe9d8EcFQHFp1W58-EfQF9oxbVpoNpGdVqp_b28sUheDQVRUTinoReR6YWUfLgmgV2DY7oVNvawlsqUQNa9JFoNLcwSyaHd6iLZ_bCnkL5oGeZ8A4Hi7L0iGzMhjXyiDZp3Ki0DCOVxSVKgAVkDzgd1hKFEWMsbNt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=m__ks9ftTwXoMzJujteH_2G8Pch3WwPQda0wVvKiAEdOg2Es_gWm7v_lCibmztcLwfyeh78F1sn8ddDpu-kadpTb00Y6B3ryfVA13yQxET317YbUuMqLkZe1I90Oomv5Pl3FiCAcOm3OB3InOuM6gcH7AM5mWM9KywMfoJjepKTF-Qu3PWrIICJGb7iBp_oOjjuxS5u9dY3hQy00tKqidb4acC7rHHyB3CcP0oW7Du_6mRFxwREUAQt8-eEo4T_Fags87y3qRIcGdx4dVcyobJW6HriH3iCb-viwcySrbIjfvEPFDzVZY6PT_D2Cung6HajDm76ya179BzfoEOW-k5xAmO5IoqlHrLPUMSAznU1RkZ3Lt3ORyCI-Yl4QyYePV8omUIaWZLErOFh-ZmaPHamPLYLjoniWy_HmTadRgONl4OWh2OpTK4wuMopHhAOTU4XXjs-0OBtcxYvGXPKvETGkOr8KuTBqS6Hn8dxGdVu3Moh47-TeB5JeGTHPF_VAeq9RJnYhhbe9d8EcFQHFp1W58-EfQF9oxbVpoNpGdVqp_b28sUheDQVRUTinoReR6YWUfLgmgV2DY7oVNvawlsqUQNa9JFoNLcwSyaHd6iLZ_bCnkL5oGeZ8A4Hi7L0iGzMhjXyiDZp3Ki0DCOVxSVKgAVkDzgd1hKFEWMsbNt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxtz_CgeWN37omGKMwDjojIbTqF0qvdCJiPZH3JixWM7gHj5J_1hhQ7ZpEbobaMlshKxSd_hHC0TG3zaMjxKcEHIFeF7Y2c-_zd-Ot4SNmV-0GqN6mLHBeRUm3P8Whx_7bdit1imnCOTJ0Kuk35ORuX0qisWZmPB2M9AXjXzgcRhqBNWMhcLE0VMxPNZI2qNLkBdx9ViZl4NkJdTQcW-Wa3I-8nu-MSi3wxB9lXu2pwKRbR_IGyPOOvx9BYnQMWFw3yo78e6di3F1R_6Pn3DR2Ds1A_2kKO3iOIBmRo700aV7DsuovRBXH1kgIRmZcu7F6gJzIg31dkOwC4A6rHE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adudlOdW0LQtHR6bvs5HINz5xC5JoaCxsmUtQufk_h4xp0RO0W6h9AzdLtGDK2X58VeVUXGAJwGsZI3ah6HKNfhvpL4DOui6JeRnrW_mt32n1DpPa_uG4WnLEetlD3Q6BmJAz8mplzN-UH9Y3MmKwod_ubsnumDCkkWRMz-Mv_toe_03g10fkQB559YD17aBOFtIBlSakjToB9A3K5y0sOAIOTxpmbVCRbIKI872K5NcVnG7VgTqKMKPmQoz4aiExRJ6hYWJQF22FbbsFzxMFgqnVjcGiWQz9mk0Q24R4AovEQFhKAwWLFDGt0crOY-nwIFiKsOz1KQl7sOpBKvHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_TMI1wOJmGfCTYarNWLa2xKgeGHsaCu7wtW-gAh1bQDNsc7A0D0nMNbnitaa3AnZ8J8Q0ERuaXq5IXPWq4NlunOWQlqvNR1EtIlsKhhh7kZzW310fLA1iWLn4z5r7zkcMww9xMm-FuYObDuioHyILP2IusdqfqE14CCk8gpyxaDCmEFtlgpxBJi0NWWX8BCd6CxMsS7KOt3vcYLjTGZeyfcQ_t81Hx5EgazkQh0Kq1hB2Ld748wEqGRLLHnIc2NVoCFr8OGjhBVcxwW7squZsTnhYUAj8KfHWdATJY7tvl8_FzJsghQ917JaR9GXGi4Be7kfrb7InKxD390e2mXxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUqt12FqaHS_3MW8LBgHLAt3o9dj7S0qyN8SbAj4c5UQia2XQ3z-_UtXEUE6M7B-zpkfHjQlYqFXsYeco2WEVbsLkL9HIj04qcPhLRG7lUlrePl7OrDUltmOO3Irggzc_PEiNycN0xdgdtJfGo3WPi85_YIEigftY9NBweRPPL3zJglfdTdoIyz-dS69sM1MkRi1IkVNqpg5ZifwuMGftX2EUkKHBkjQHVFV2Q8LqYqX_GiS4zIXnLS2aUvyN4KOjxvPoM6neN5rMUl6TJ3L9E8uCnzsOYqDuF8GqDso1ojxR6EPqxMZ9ic8nCb9Rak1GxLj1_zFegQGZgosDE10kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=bjZir-KRx-_l6vL1YQph0-VCck6_0FBinK1EuXTrgVQm6uPuMlgUOJwR3BkJU-ten4ZxDD-vk4gwd4BG5y7xUWs_DWqV099Qw3FbxUGxCahbNzhc6k0ry7xWqCvgx_dkcf4TR6u1zjPAiSpLg34Asf1UVQuVtieQDBFwJJlQMdjPKPANf1K7yyDnDRiM9qnjgkX1ihiuL7UXF5zpNiqVqtNOfBeTaEvuj8uyjQ0BImnk9QhHJ_xcESqB4l3kejKAYjcPZxXQssrnmS2QpF9L1uJvsekC1cCuigH-W-pP26gMX2aDobbLzDKTEo4REWMy-NZa9HXYzLAcdYGLP3Ypgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=bjZir-KRx-_l6vL1YQph0-VCck6_0FBinK1EuXTrgVQm6uPuMlgUOJwR3BkJU-ten4ZxDD-vk4gwd4BG5y7xUWs_DWqV099Qw3FbxUGxCahbNzhc6k0ry7xWqCvgx_dkcf4TR6u1zjPAiSpLg34Asf1UVQuVtieQDBFwJJlQMdjPKPANf1K7yyDnDRiM9qnjgkX1ihiuL7UXF5zpNiqVqtNOfBeTaEvuj8uyjQ0BImnk9QhHJ_xcESqB4l3kejKAYjcPZxXQssrnmS2QpF9L1uJvsekC1cCuigH-W-pP26gMX2aDobbLzDKTEo4REWMy-NZa9HXYzLAcdYGLP3Ypgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=E4Y6NZhxok4V1tpuXD05NiG9NLgNlo0SsRoYNgU0Of3VXb3fg8CycYVEPAhN1Zf-u7nXJdElRrfT9lC6_p7jEil4HsyzMZbe3A3GbLdErtnFaL380I5ePUKfjJmjO_tmiKKA1mlHChPE3v8uqqFByOmzC6SFIC9cymYJQv5zuKBUOc_kp4VKSJ3AQcctMMQgG9W46MonvdsDucjEFjODZrUCuXaH-28dUftzrJKHf3EBZyZeEA6zDXSPVTCVu0-TQkcpJsbw_02BDGpBMRHuT9zPL1tfU1eMeC3I_JWc4yp2Xr3gYqfwHMQVJpWIsv1-LFpK5eT7kdV74X23OTHfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=E4Y6NZhxok4V1tpuXD05NiG9NLgNlo0SsRoYNgU0Of3VXb3fg8CycYVEPAhN1Zf-u7nXJdElRrfT9lC6_p7jEil4HsyzMZbe3A3GbLdErtnFaL380I5ePUKfjJmjO_tmiKKA1mlHChPE3v8uqqFByOmzC6SFIC9cymYJQv5zuKBUOc_kp4VKSJ3AQcctMMQgG9W46MonvdsDucjEFjODZrUCuXaH-28dUftzrJKHf3EBZyZeEA6zDXSPVTCVu0-TQkcpJsbw_02BDGpBMRHuT9zPL1tfU1eMeC3I_JWc4yp2Xr3gYqfwHMQVJpWIsv1-LFpK5eT7kdV74X23OTHfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlFeiGHx52rR5-7y_9u25wzaOwl9BAbNKEUbvs1dKIS3jT1uTa9iJP7lmoBGiwbaKwKD19OhVZs4Gq3li8yNcvQ2XZVl44tk6RCiVV8MCAfK18ozTvJPkqvKO4VIauhzygyv95bXLAf3TV7JuLCpWCRiFTmYzbR6xIz6bWn4wNUEFeTB3Lr8z7zPgqAf7NbGgkV9YoPjviUw0LRgIwgNafhEazcqq4PuIamYgZqilrMv1jzLsrH7GtRDR4XDdRU212czKe9LRZTtwF-kfCkGujyEO7ILuhpmC4Saoh0CxVJ0QolGAEOY2PD3aDZoxakWpmkCLH2dzWECHi9lua6Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=FkZ6w3bBgM2b_cf6x3slvM6G_VLQZBBlHSu3eXwnEvuDcVa8E1DH3JoYIwhpDmTRrnGMIFV5WSJ-gmgpFKpxtcqA0uTJqLUhg4-kI_Av--Wb19T8GjtL5d-e8CLj9R5i80Yf8-J1BYQ9Bys49VF1xf2P6apPEZGvc44jiI9lagjMiNZ1TAEZj42YL5tnrK7RWmCqIdItZDLituxIghfpO8kh6LhZIvzqYzpqJpEfOhcoWPsw-USR2IxRS0fql-EkLQsOGzGdN_PvByMlwa5IWf4ssFWMP32koBa1b5mlXE9bR4NC9kzyCopk7Erwy06HpkImBr7J201ENpre0kQX-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=FkZ6w3bBgM2b_cf6x3slvM6G_VLQZBBlHSu3eXwnEvuDcVa8E1DH3JoYIwhpDmTRrnGMIFV5WSJ-gmgpFKpxtcqA0uTJqLUhg4-kI_Av--Wb19T8GjtL5d-e8CLj9R5i80Yf8-J1BYQ9Bys49VF1xf2P6apPEZGvc44jiI9lagjMiNZ1TAEZj42YL5tnrK7RWmCqIdItZDLituxIghfpO8kh6LhZIvzqYzpqJpEfOhcoWPsw-USR2IxRS0fql-EkLQsOGzGdN_PvByMlwa5IWf4ssFWMP32koBa1b5mlXE9bR4NC9kzyCopk7Erwy06HpkImBr7J201ENpre0kQX-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=jTfUNQzLve0OU7yMSGemukCfWa-SpdUGVaLZq5UPDMSt-2jMSLKD-_cpsH_b_6AtNq3i8AEaGjCDI625sGxRHVV27HQ6shuJQh6rK9dZMZxRpOulAt8BITVKkQiky3NXzT3jrV6-OxvZDyHfXvSkArFu1hHhED2Pai48GWPXMbdshdJNClOPfxLa0XHnDyMYfCJKqYjRX9bLdu5MqWjcDbxX1zZBQ4I0wQx-LbF-xKiMfeNQeq1kaDqXkzkBgP3943VAY0drGsM5Zs6tbufUdNWgV81qsXugdJlyGgXBcMwXmFKknRksPR5zHmpV22wp7c414My4HDRHwCw4JrLgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=jTfUNQzLve0OU7yMSGemukCfWa-SpdUGVaLZq5UPDMSt-2jMSLKD-_cpsH_b_6AtNq3i8AEaGjCDI625sGxRHVV27HQ6shuJQh6rK9dZMZxRpOulAt8BITVKkQiky3NXzT3jrV6-OxvZDyHfXvSkArFu1hHhED2Pai48GWPXMbdshdJNClOPfxLa0XHnDyMYfCJKqYjRX9bLdu5MqWjcDbxX1zZBQ4I0wQx-LbF-xKiMfeNQeq1kaDqXkzkBgP3943VAY0drGsM5Zs6tbufUdNWgV81qsXugdJlyGgXBcMwXmFKknRksPR5zHmpV22wp7c414My4HDRHwCw4JrLgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=UdD2YTA57wJA_p0-69_PCJoipUKp9cG4IWT-yiNQvZTHwwClFwSea0lhaX0YuTguRCD-Emib72tzmlKK5bVKW-AMF0F4rapKSLFONqQee06tBUZP9K6_nb3S4fdh9camxPKop-VfL2ZWcV7e29SNopaTM4PFbiFHy_YxqgjpTIR3Txx5df1oyl-3vjclrr9H3QfVGfXg5Y5uuveIOaQrLQ6ZA1EnFWCR4wxiIqo7bWZ4xl-gy9qRfzAAFrurUUYxo-J0DwqsIK5zAvfTTxokJ05SnDDNJ_VTfcQEBbplCUW9nrC25uxO0X5zFfoIb_mCN2qhrOV4HexgD8YKl15z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=UdD2YTA57wJA_p0-69_PCJoipUKp9cG4IWT-yiNQvZTHwwClFwSea0lhaX0YuTguRCD-Emib72tzmlKK5bVKW-AMF0F4rapKSLFONqQee06tBUZP9K6_nb3S4fdh9camxPKop-VfL2ZWcV7e29SNopaTM4PFbiFHy_YxqgjpTIR3Txx5df1oyl-3vjclrr9H3QfVGfXg5Y5uuveIOaQrLQ6ZA1EnFWCR4wxiIqo7bWZ4xl-gy9qRfzAAFrurUUYxo-J0DwqsIK5zAvfTTxokJ05SnDDNJ_VTfcQEBbplCUW9nrC25uxO0X5zFfoIb_mCN2qhrOV4HexgD8YKl15z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgfNzIlMgP-nMp245ffhbfv5YHVZwpLda7rdciw3WCm_T-SKYo2yTJjkqlaCzOhxsFt5bJIaQ6GLREf7CCvpwDm-tzf7to8GdQQ_DUcC0pR_FdEWd0nVMHT7p_ubjm4egTKch96mWrGB-s74IdPnt7bcaHev_L93rh5PbO_6cuqAntBJeprxRzCHKUMqb29F24lSNR60omirP5ECNxjtDX5yaYzFE0co4WA590GHdeLcN_F-qKLpQQfEJTJdmnoPJhNanjxFiCzeepeZL8WoQj75W1LOTLG1MppsUzlTrxxWLecUfdkr4cwo4CpR7HQh9mN5I_vqvENBYVflJyjOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=dwg8nTeRDa3LsQEu816ca1xBTZvAzl_emSz7kR4roNxRXKQ-VfyMCoJ73lmDBQXLlA_pKWCqIAgKLH1AyCtKtk0UwSH5sUkMj4CPQo8s2alAHdO2OxYwrKxNo1gKTY3jnw2FFYSDk53xS72b8vv5loTnQP9dW9ufazeJf1a1J8Okiw_P5qKX-Jy_BbKn5RjE2OETpmiR_KAPXzFQTQH9ickuEGND4_sw7EJolPWLONTdEkBISmdTCEHU_o005MtOx3_9xKw2dh6mcMxB8iAVnvxmrQwsZvWUuwq6nDCGmwPttVPaFJ1ryoS8XnOR-xjHsegTJEuqJwvwnqQfQ1352w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=dwg8nTeRDa3LsQEu816ca1xBTZvAzl_emSz7kR4roNxRXKQ-VfyMCoJ73lmDBQXLlA_pKWCqIAgKLH1AyCtKtk0UwSH5sUkMj4CPQo8s2alAHdO2OxYwrKxNo1gKTY3jnw2FFYSDk53xS72b8vv5loTnQP9dW9ufazeJf1a1J8Okiw_P5qKX-Jy_BbKn5RjE2OETpmiR_KAPXzFQTQH9ickuEGND4_sw7EJolPWLONTdEkBISmdTCEHU_o005MtOx3_9xKw2dh6mcMxB8iAVnvxmrQwsZvWUuwq6nDCGmwPttVPaFJ1ryoS8XnOR-xjHsegTJEuqJwvwnqQfQ1352w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag_VhGi50QKUkfHEt6qZjbJVgF1pahelH2PJPpXIHNPXxUnl63MM0mMpPoBy3ofZ9uxI5qGHtzvy5v3n-PE_Ed_eMNcevAdKkdZlUwVoBglrgHimLjiIfw83GqTfVGML8nUMJYOceKtcs57q5yidgyJn7wQjZmq8snC-qDKiMWKL0CD_4MApPlidCFqGptnuK2tVYA0vaQF8GXdHfxKEvbfpacAglJQIqDOkwz3k-PolbeJbQLKAzvgdnEAycA0kl9TTS2jHd9MCJpsmZKtr5pLIG-oPy5sus1HSeW4gDE2hX7iyTnPNvZgSb2S5_MVM34ZR-47aR2f3FM53zFHvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPiW0w12dfMpNfFRVw2tCGSOeikh5Xawu-jC8piFhIDIXDXkNpsH7xkl8bAFDhr9A_oYDvrPnJyP508kwJPLybu4DWOFEz4BDL2_JAK0WXlt6pAnJvz8NaYSzaGFqVzjzisDBJWRgUhMxaohc2q8hvHd7MhY32CoKs0QdQvcAjMZLbbxVq7DRdoZ8JBxpr6U5jLyiVfR3C_obyR7gcUXIaUtIdAukLy8A00FLMB3O51yLUBzdjxgXcxQdb55V3yvTHXlwZHJ5vju5bZvS-_RbN2haFwv9QoumvaYO6LLesILtTpzMqhmpoQLYaoEvmHy_RyCBiJo7oZiLXfYjuiKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=RbUELTHfg-Mb_3NRqPuWjbZDJTRH-9rpemBU22uqZEzxrlOr4_nMSMgW_iVOukNNQfqVeEdpljB7OVRImlAkffVLlGX0EUAK5MdsHlBJHJU0uFtG23wbwifZvSMWhFHWOx41-IzzvlhOWnYj1dop1WLz4HES2kAPmP58EvPMf57klqCPBQ9d1p1AGw1oMIFhyBvp0BE8ijjLvSGIaJIjlnBZzGkcxZ40LJwdnGTTZJldo-DDGtc5S9h3kk5hcOh45czOVmZwbrPkxONdCGWlrWbl7SLqVQoe9n3X6Jy5pfpEGdYpcUb9ou5iVVwxfPaTwhQu8qJPa3RQ-KldUqyblQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=RbUELTHfg-Mb_3NRqPuWjbZDJTRH-9rpemBU22uqZEzxrlOr4_nMSMgW_iVOukNNQfqVeEdpljB7OVRImlAkffVLlGX0EUAK5MdsHlBJHJU0uFtG23wbwifZvSMWhFHWOx41-IzzvlhOWnYj1dop1WLz4HES2kAPmP58EvPMf57klqCPBQ9d1p1AGw1oMIFhyBvp0BE8ijjLvSGIaJIjlnBZzGkcxZ40LJwdnGTTZJldo-DDGtc5S9h3kk5hcOh45czOVmZwbrPkxONdCGWlrWbl7SLqVQoe9n3X6Jy5pfpEGdYpcUb9ou5iVVwxfPaTwhQu8qJPa3RQ-KldUqyblQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=tyH5_wUMDNz4QuVlLaN3H8h2Z8XlGKcwd1XKXgKrViq_1Z90NPgPCK0eL6URw0eyIGnqQcxCkI8Mulsii1EBSbewxr-paFxmO2acWSgoHPX-u4MTGJcNRWnkiHsBpy_1s9Y8HoHRo-UXxJHx84RDNGrkHUszOK8KWNKHzLnEVPrH6V9bEceugjkrrP6hn7dcLd0mTijQvJfuT5-4hcs-35ILgIovreFdG9My07-Ei6Wn_lsbFc1ihRz22ZunvH7OhnGM1VYbnw2r620EX0ksBFqC4EJcKSmic3-nEV4Yekgf3nZfwm1NWGNj-4FHHac00QLa16auQDlqkjd5RylCqZT_PR33thh5bJ78UtveRZ1oQFigSBtqHFsV7HKf4GvhyNFV2350ugpZDoMWbwT41lOrQss_9ant8gHuFip7FyNKZyFnS9HdJzyLDsTISCGlFUoNHbuXH-h7bXvrD4ENmS8jlRcrPYdc7PfsFcJ33D7Gk43bigDc3GlL-fwyHj8P37SrMwkXuT4vQhHxqW8XS7tncWK1tWIv1FClLMOtZzdkDcv5wjEurqTVMWFeymmHQmMYJQsaLEGXjCkuWSee1l-jDlrEKezoqwVqHuYnSJgh8sd0LWlHyT6H0m2zSnzurRS_7DlhwEoIHpfPNlnv08FRWA-vPb44DEfSGlTeIWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=tyH5_wUMDNz4QuVlLaN3H8h2Z8XlGKcwd1XKXgKrViq_1Z90NPgPCK0eL6URw0eyIGnqQcxCkI8Mulsii1EBSbewxr-paFxmO2acWSgoHPX-u4MTGJcNRWnkiHsBpy_1s9Y8HoHRo-UXxJHx84RDNGrkHUszOK8KWNKHzLnEVPrH6V9bEceugjkrrP6hn7dcLd0mTijQvJfuT5-4hcs-35ILgIovreFdG9My07-Ei6Wn_lsbFc1ihRz22ZunvH7OhnGM1VYbnw2r620EX0ksBFqC4EJcKSmic3-nEV4Yekgf3nZfwm1NWGNj-4FHHac00QLa16auQDlqkjd5RylCqZT_PR33thh5bJ78UtveRZ1oQFigSBtqHFsV7HKf4GvhyNFV2350ugpZDoMWbwT41lOrQss_9ant8gHuFip7FyNKZyFnS9HdJzyLDsTISCGlFUoNHbuXH-h7bXvrD4ENmS8jlRcrPYdc7PfsFcJ33D7Gk43bigDc3GlL-fwyHj8P37SrMwkXuT4vQhHxqW8XS7tncWK1tWIv1FClLMOtZzdkDcv5wjEurqTVMWFeymmHQmMYJQsaLEGXjCkuWSee1l-jDlrEKezoqwVqHuYnSJgh8sd0LWlHyT6H0m2zSnzurRS_7DlhwEoIHpfPNlnv08FRWA-vPb44DEfSGlTeIWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=FKUJvVIC3Z6lROPER1CW3ZDSr8VHwI8a0p-msRBbKhipP553XDD5--Mr1CaUg84YHuGKNo82de8LN8SvmNVZmOTY2tXu1tmy67Xnd3kZTTbl0kjb5GxapP0zGo7jsshN-qT_uENRFsY8ophg4LuOFi2M4vpZDFnK-HT3fRklOQCLkc2cbyRpXfJCw8A5hSU30xDRi3p9zbxycvH0FzRYAqqsb4E6vg8FBv4lbCXLiRcG0QlpSgMNxU5sEiVoov3L7zxGY7Y9QGOoO4LVnRJs89FK6MKxO1I-eNXoUGxIARQqBoy1i6IiEs-1JVsDMW23Sl8UA0ZIWoGOFT4SwhZLlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=FKUJvVIC3Z6lROPER1CW3ZDSr8VHwI8a0p-msRBbKhipP553XDD5--Mr1CaUg84YHuGKNo82de8LN8SvmNVZmOTY2tXu1tmy67Xnd3kZTTbl0kjb5GxapP0zGo7jsshN-qT_uENRFsY8ophg4LuOFi2M4vpZDFnK-HT3fRklOQCLkc2cbyRpXfJCw8A5hSU30xDRi3p9zbxycvH0FzRYAqqsb4E6vg8FBv4lbCXLiRcG0QlpSgMNxU5sEiVoov3L7zxGY7Y9QGOoO4LVnRJs89FK6MKxO1I-eNXoUGxIARQqBoy1i6IiEs-1JVsDMW23Sl8UA0ZIWoGOFT4SwhZLlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOCz5RxECgDuHhJkH9TX1Vx0rY6NZkLUQu5ZFFp-Q4tudwfqe6h129tU720JDXdngcWCMWN3Z9GHEXOFyWWCmkTg9Lob5pLBfeACBTKV4wOYm9eddS4RE53uTSIc7N3yrFxffs8VM6gYCDVLsEyiQ5wmE_XYyJfYUz1UeGip5AOjRP-mtown53G6VRExbwC8noZnQRVbspKeLy7V7nHF0MVI5RcCwOpqFy8ma6f_KYjC36ClswB7mTIh5A_HWIv-EZ_upaDt8co4igyNKkxZR4EnTT10U8AeGgqYFx5WPEwyAuyE3C2ioF3NThwcwcrHr24FdItoZy5_mJPidbhwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=WXlxaV_CBPRLHuODxd0tPESUiiUDs_aHwRLBZOp7m0xUp2h_K0_JuO3P1kteHABFzW3_k9F2OUBK61LuDD01ScHwCV8ADp2BaCXhm4IaRVCWZldro3ZhNTVhHwTBu4i4PMWGKv6KOx9i2DQDHUIvmk9MYhVOaEcQgdbWPr5vJyQ5oGgZxLda-BQQzDxEfoCJxJKZY4S2ZKmCXuJm3RdALlfi_DAQshAlPLnDIoUX-L2SAYGcuJibFFYEpwO39crH-f8lLsTgWA4p8t9lnsL2Zv54ZsJXSNoShnjuvED29UpJCAP2gKxSx8yjkE7IIZNNSONrOyDafVjYica_bXxRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=WXlxaV_CBPRLHuODxd0tPESUiiUDs_aHwRLBZOp7m0xUp2h_K0_JuO3P1kteHABFzW3_k9F2OUBK61LuDD01ScHwCV8ADp2BaCXhm4IaRVCWZldro3ZhNTVhHwTBu4i4PMWGKv6KOx9i2DQDHUIvmk9MYhVOaEcQgdbWPr5vJyQ5oGgZxLda-BQQzDxEfoCJxJKZY4S2ZKmCXuJm3RdALlfi_DAQshAlPLnDIoUX-L2SAYGcuJibFFYEpwO39crH-f8lLsTgWA4p8t9lnsL2Zv54ZsJXSNoShnjuvED29UpJCAP2gKxSx8yjkE7IIZNNSONrOyDafVjYica_bXxRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=q3gWipZrHPtfdvmA_Styisxli7NKodyBqwkSKIs7TYXi-kszJAD9tDJdjcVmL_4JaMJHXISiJ-u4mHRt5m9Mx3eWRLEtQj9ZYShQxvLzwULK-9xMkyL26iE85ujgDfyjrogiJF_EL2INFI6F-WEFl-UBK9uvCwKfMnER4fiHZTStnbLWn3jGDqleRRX1hZzhYTKMj9pgS_9w4Wr3WijPMbqQYQDyqlDX8CaZwZzjQ5OAz1zhXnvnjuL7jf2N_s0ahXhWhBhEFcKJCeR-FAwzr25ef9617A2fKy1jzgCEumAC4WJ7dIuwoLXT7srppvfU7y2sA7xLDv_T7O8tyNixZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=q3gWipZrHPtfdvmA_Styisxli7NKodyBqwkSKIs7TYXi-kszJAD9tDJdjcVmL_4JaMJHXISiJ-u4mHRt5m9Mx3eWRLEtQj9ZYShQxvLzwULK-9xMkyL26iE85ujgDfyjrogiJF_EL2INFI6F-WEFl-UBK9uvCwKfMnER4fiHZTStnbLWn3jGDqleRRX1hZzhYTKMj9pgS_9w4Wr3WijPMbqQYQDyqlDX8CaZwZzjQ5OAz1zhXnvnjuL7jf2N_s0ahXhWhBhEFcKJCeR-FAwzr25ef9617A2fKy1jzgCEumAC4WJ7dIuwoLXT7srppvfU7y2sA7xLDv_T7O8tyNixZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=qd7Xgm-6idX8wEzY9iTnUuYFJtECRB2MCjrS5k6DjY6zwS5B8Sh3rDmjl_yK7a7vRDINPzF0hRhweAh4la2ciwplcS2tYRlFgyhU6ZZV6cAaQt7yPz84SzJj_NULw4NUpEKmu-WpmDYB4Yd93VGm5C5-c36OI4pti88ykryYxpeiX0QgZzu6YAsA_U5_Gl3DXZbIMqbVgkIo2dPe5Ur2J_8E6cD_vFaiCs7ueYcSPT4LGKDWbiN7qUev1DlWnIvbVxxwHt9YXEPwmtwswXtFR0b2fgrNWgrdhl-U4efJN7BKTT1PWRauSt9GWSXlmsJEQmusjT_WxduhdkAOv7IyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=qd7Xgm-6idX8wEzY9iTnUuYFJtECRB2MCjrS5k6DjY6zwS5B8Sh3rDmjl_yK7a7vRDINPzF0hRhweAh4la2ciwplcS2tYRlFgyhU6ZZV6cAaQt7yPz84SzJj_NULw4NUpEKmu-WpmDYB4Yd93VGm5C5-c36OI4pti88ykryYxpeiX0QgZzu6YAsA_U5_Gl3DXZbIMqbVgkIo2dPe5Ur2J_8E6cD_vFaiCs7ueYcSPT4LGKDWbiN7qUev1DlWnIvbVxxwHt9YXEPwmtwswXtFR0b2fgrNWgrdhl-U4efJN7BKTT1PWRauSt9GWSXlmsJEQmusjT_WxduhdkAOv7IyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=I6vORv1vsIotXpnbNvj7e2H7Ec9P-pocr7a77cKNgFoYQrfNp4luQwHSNMSVUuTBTNh536gBAxJSsrfjd41o7oypPMkviLLLo8D3wJhIDNPuRJTVpU3yrSw-kjAQiv-FHSTbGu2TqNEFwHByzuf4M694IYfyhRoRYrwaj7Y4J7CpBKr_aqJuGudSz8VaPpd9FX0mn2685mS4leaUKoOPybpM2cuYJGQQxUq-ROGYBQ0w5_2XncCeIodpcdM31ZP6vZPuor9LDqMzP1sI_lw-Jb6f58eIHO4agVm6ioUKVXMLbZkvWEA_VT2K4LiSYN70gqEyx29PD5iDw51dIhwRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=I6vORv1vsIotXpnbNvj7e2H7Ec9P-pocr7a77cKNgFoYQrfNp4luQwHSNMSVUuTBTNh536gBAxJSsrfjd41o7oypPMkviLLLo8D3wJhIDNPuRJTVpU3yrSw-kjAQiv-FHSTbGu2TqNEFwHByzuf4M694IYfyhRoRYrwaj7Y4J7CpBKr_aqJuGudSz8VaPpd9FX0mn2685mS4leaUKoOPybpM2cuYJGQQxUq-ROGYBQ0w5_2XncCeIodpcdM31ZP6vZPuor9LDqMzP1sI_lw-Jb6f58eIHO4agVm6ioUKVXMLbZkvWEA_VT2K4LiSYN70gqEyx29PD5iDw51dIhwRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwRqy1sk_aHnqlzSF55qOHyND1TciKA1nK_J-ZlYO2tYEUrtBdrvsOeOPLe5rYeJSvu-TG3LPjmVpv-z82jQg_mkmv6FqpRaf66TQJNuJry8yITBCwJqmgzqrmv9dY5eAKPqtwZN8zxGQoRqNwSaKWr2B8eZvtNeIx9Wd2sUfGWkaysoQPk0JHXOmRByK9HRzJwKEWFayK2vtDJBoyZYCxHgL63rDbxX-zYJsBW0RUSppBDrBPjyUPGvVjHhiI-KkROENROQmt2llj7Djad3WLoG9RbUgres9U0tOoEr07yJ1_wPIqa3q1htdrm64QO6c2hsW6J7TbfTuOjgh58tMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=vRteDbw5RyxSR1IHSYFhiYNuHqJryLPZSsMee0CmoQS6ZhWTvJB_VBqe9XbtJ--WjOeV3bLM14ZuweHvzSdNZ-4tLv0gzM9PEKps4i5Yl058rnf4oiGQSkwd0nGdlfBlRMV0s276sGicNoZoHQQ4XoCqTSAwLQv0VRyRyYvoJp2BzTPl_wMkHv1pFyaamnQHCD2XyDudQuM8NLX14sZtzYOoK5PMooCLO8J031mLjyDVaUonzWsQxCaGUBhQO5Uy_M2uYuwkNUlNPRmqg2vYwJ7xFKETnQhEhpEKds5GE4lakd8T9aZWaUQhXuI3n_22zNlcC61IOR_T-iIYmYrjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=vRteDbw5RyxSR1IHSYFhiYNuHqJryLPZSsMee0CmoQS6ZhWTvJB_VBqe9XbtJ--WjOeV3bLM14ZuweHvzSdNZ-4tLv0gzM9PEKps4i5Yl058rnf4oiGQSkwd0nGdlfBlRMV0s276sGicNoZoHQQ4XoCqTSAwLQv0VRyRyYvoJp2BzTPl_wMkHv1pFyaamnQHCD2XyDudQuM8NLX14sZtzYOoK5PMooCLO8J031mLjyDVaUonzWsQxCaGUBhQO5Uy_M2uYuwkNUlNPRmqg2vYwJ7xFKETnQhEhpEKds5GE4lakd8T9aZWaUQhXuI3n_22zNlcC61IOR_T-iIYmYrjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=VeTJX5sPBiD6ZcZeKtGE15Gb5EBZDgjYuzE6Pahi3T-To6crGUTAWt1W5hLLLlwROTrLNE82IipecZ_g2Lf-qQ7PN9af0irpZDMw7a3Vh7AF9PQZq7WAKu6jZS-b6bya9bQ5TlhA3m5ylRs_cHUvDaRnbiRpx7ILuQ0blmtf_z3ch-aMDW0s75xhYSo-Qs9XwJ8Di2PfYx0NfqwK6Llh6mmkCbATen-lUSsmAfoDP9kOYA9ypzcoaJ03Rm2VYN-Rr0kcK5bLepTqCzqaT4KWZLR1zmD_-Kgnh8qqMIFSSzFxX6DlWSoj5V2pYvfxLcYt-mW1dKue44wWsmYXwDxjWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=VeTJX5sPBiD6ZcZeKtGE15Gb5EBZDgjYuzE6Pahi3T-To6crGUTAWt1W5hLLLlwROTrLNE82IipecZ_g2Lf-qQ7PN9af0irpZDMw7a3Vh7AF9PQZq7WAKu6jZS-b6bya9bQ5TlhA3m5ylRs_cHUvDaRnbiRpx7ILuQ0blmtf_z3ch-aMDW0s75xhYSo-Qs9XwJ8Di2PfYx0NfqwK6Llh6mmkCbATen-lUSsmAfoDP9kOYA9ypzcoaJ03Rm2VYN-Rr0kcK5bLepTqCzqaT4KWZLR1zmD_-Kgnh8qqMIFSSzFxX6DlWSoj5V2pYvfxLcYt-mW1dKue44wWsmYXwDxjWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYQO14JkrmX2yfZbB_cfvuIaP33mOMSlDbp7kDzmpyD3VfwNt-sbjcn-SkQvffdRP0VZYm7g0KjJdcGTZYLqfG6-dxuqE1OCfxmajZ_1nifops75PlKd_PFyYtn6V-mHq79b1a3bmkxEdpCfVN2ni45FwmlIbcNRabLhErTCarhjnyEyTeWyKA7tIttiMGpxAMVq4TJBH50Ipx2xYiuxCDnWymnQyxzU-lPL9EdPijVB8EvezQ2U94LSdi1irYnBIQKZGM3yvEmfY8cRsTHCvi1NakPqXVwXeaysWyUDFHWso2sjnFQwihzn3YzsuKgc48dI4Y3RDjT-45zd9DfF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FomQ519jg9qHaDyChaX232E2Mk_K906GcuYU8lv5bnzxI28UGqcTBJORMoELXqZQQghtnMY_A-SXvYiI8k5w6VsV3MsZzzY2RByul1PS2f3SNR6OOsbJxFLADBkc7td578kyldF-utkZ9827Xf8WH9nrbntRnpKd1_XAaP6gCGIj3kl5dw5k893NQfDKDdmFkBijlIfC6oqCj1m66fFr5dvmCrvV_3zblBu3bysBa5ccuZN81fjPS-zdlvPW-gdaBdwilnewYosWoVp0Op9akmjb3c2pKfMPxmjU0-3SMtooX_vL-11uKrdAvbTboKgfklms75lXhFiVFonKnM1oaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FomQ519jg9qHaDyChaX232E2Mk_K906GcuYU8lv5bnzxI28UGqcTBJORMoELXqZQQghtnMY_A-SXvYiI8k5w6VsV3MsZzzY2RByul1PS2f3SNR6OOsbJxFLADBkc7td578kyldF-utkZ9827Xf8WH9nrbntRnpKd1_XAaP6gCGIj3kl5dw5k893NQfDKDdmFkBijlIfC6oqCj1m66fFr5dvmCrvV_3zblBu3bysBa5ccuZN81fjPS-zdlvPW-gdaBdwilnewYosWoVp0Op9akmjb3c2pKfMPxmjU0-3SMtooX_vL-11uKrdAvbTboKgfklms75lXhFiVFonKnM1oaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ESBsegCDNXGYInbL1exHKdn7OSfRUi6QwDicqBOu8sWs16d3EUGAgBr014S0epeiruoeCe_CChsAfT93RGA1onYAkDNKOpXTWaWBlYfMkxo_GemzTq_rVvETrMK5Q0jmR2lZUlDtMzZHZBv4-8PbywCn2YTMIfF1MtVJvCYQsLzlPfCrvd0y6SgP2E45vxlQzg5DvA1GGkNsKwQV-tH6NIwSEHTGO3mzBnrjkhLvuNiVs1ORPXn93WRow9dsb0zqd_w3Z5VyicSdg5dcUICKTLOWhiIciSc-M9BFh_sf1csOUq9xCFIG_TJQ35Y8-jRqc4aGFKck9hxKkmZX3QDX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ESBsegCDNXGYInbL1exHKdn7OSfRUi6QwDicqBOu8sWs16d3EUGAgBr014S0epeiruoeCe_CChsAfT93RGA1onYAkDNKOpXTWaWBlYfMkxo_GemzTq_rVvETrMK5Q0jmR2lZUlDtMzZHZBv4-8PbywCn2YTMIfF1MtVJvCYQsLzlPfCrvd0y6SgP2E45vxlQzg5DvA1GGkNsKwQV-tH6NIwSEHTGO3mzBnrjkhLvuNiVs1ORPXn93WRow9dsb0zqd_w3Z5VyicSdg5dcUICKTLOWhiIciSc-M9BFh_sf1csOUq9xCFIG_TJQ35Y8-jRqc4aGFKck9hxKkmZX3QDX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=NXTLOfLAQIGxswc9r4uEPBBuf-j_sR_vwh8RqBXhlzI6g6bEzs6aUUJ8L-8x-Rm8qXrAVltu-5ZLcRGn6B10D2dgrGxhhdKenTtvtcJ3CkCQg0UGj0YOXp1Ea3E6FCI8Gvx34XC8m88bL9tpz-JzMw_ohV01qJMzE82QScWFGtYKZI9kCfGbdBprgyNFhQy0E5looT7OF0lmFZNyOirA9ovXvx9ErrOFgJqovQszuND6DT4xNRcsX2WKS2UYCvsHSZWteU9ahqbyK4D3EIMNzKEFnsVi9hyjzzbbpV_RwA3GF5XKf3cc5dCZQpElo5Bm9rrnedlURhpQ0k5MqTozjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=NXTLOfLAQIGxswc9r4uEPBBuf-j_sR_vwh8RqBXhlzI6g6bEzs6aUUJ8L-8x-Rm8qXrAVltu-5ZLcRGn6B10D2dgrGxhhdKenTtvtcJ3CkCQg0UGj0YOXp1Ea3E6FCI8Gvx34XC8m88bL9tpz-JzMw_ohV01qJMzE82QScWFGtYKZI9kCfGbdBprgyNFhQy0E5looT7OF0lmFZNyOirA9ovXvx9ErrOFgJqovQszuND6DT4xNRcsX2WKS2UYCvsHSZWteU9ahqbyK4D3EIMNzKEFnsVi9hyjzzbbpV_RwA3GF5XKf3cc5dCZQpElo5Bm9rrnedlURhpQ0k5MqTozjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3Ignr7giJvmYSlC43ZY_u_HeVX4Oofk0GgRhau6ae1g9FzfQcRKDLwUkfGkguT75uvgGCmy-hSdeHhRvYpTP-zDn-wgN9P1cNH7GynO0LnJ-XinJ225KQJljpsZ6flO3R2NgsI2pIp3qSXM2KvpCya51FA0Rcjaswx-EznR-_1SS1U6ZiF8FqSefro8uEHsZTSBfg2uTbzlXDB9WeY2t1kn6RM4otq7aLMwNUY2yMGoAsKmz9jYhKSeNgEMzxKYEK1Ic7eyy7HKa6v18nxMEUQoWxNLTWuzgQ19ELINMp4jMe_iMZN8QkLJF57p0IYC_0V-ccavQUzVjLw_27cFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMtf8qsg-F7BhTUqHSGIqccEfmCYNFz-UOP-LjcQUCM7tUA_f4JrdL9ksL1Kk19drYgopfnWnYX93s-T16VkNQ6GmBJz1DHUnya35cTT6QwTC83glUiNkBAFYDzDwGBJI7jlomX95jU9VCOLFrYXURwS0pb3rf1XATEj0VCOhs3Vd3z8sq29ctjUZsRYTLBFF9YBvIULTyjEC6Bd-OCJA1hCJEoBwZdA_GJJZjji9OjY5DH1NPA0yt5D9e2070URapbsSqeQeipR8VG7SkdByW-IgJlvEwK37TkXwgd0t4hg7q5h-aq9GJ_NBMUHn0IHXp51XNbrMek87dHYcexJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-tsBv0yqAJALiifO2xIzH2WnmybtvGU5qgNo-gfXN4yCjSnNJrTQU3A5Z6K_SsFev4BMZjqWYd8xZzOL8McxZ-XvfD8QLnds6f7f8K_DjBjDZUJEQJnCR_vWXKMgiMFphXPiya3prmqnmiYLfzUmOfq1RrVWJPvqpKauFF2iTLr_KVKp9Zr_HmeOQ_wserPcBNr6vAJ7WzDqa0qVT2q9kW9MA_dZJ-EFsYgqE_9BRi6KjVQan01MZX_XT7ATuOkNaM9YVtuECnnws7az7H7aYmYcw12wJFa5W8rf6Z6JT_YUHqv-dIIHqu_n2aXDbTzhUdjnTgMycyYMZqPwJZhpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=N02kkpMuLDCu_9BmeONiI6U-jfjt9AMf1MXs70TcnWHj2_ic55ISHNBMYWu2n8Y_HSaULMg3Tz7sv0jcWzDKI9EtQJJbp-b13wCbkXKE51iz7SSWwzKidRezwqFyxgoanhZIrvGbTaKodfrFjvL2wP6DuzAflIW9a7UIg3oSWSIVHaAfWGGSZoSwNzQVbqmIoE7bHk9PTWA-eUrqYUl8uETq3n5FVrFqN29XDadeKCbeCJZxIV_A6hVwT-wvgV-UFpn0Ap5DPY9azna7j1oZLXIOtbMgnxSRRQsfaJy5GFebFXrkPz73-6nqipKFVH_3O_dK1gRQSGWJkJzCyuZRnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=N02kkpMuLDCu_9BmeONiI6U-jfjt9AMf1MXs70TcnWHj2_ic55ISHNBMYWu2n8Y_HSaULMg3Tz7sv0jcWzDKI9EtQJJbp-b13wCbkXKE51iz7SSWwzKidRezwqFyxgoanhZIrvGbTaKodfrFjvL2wP6DuzAflIW9a7UIg3oSWSIVHaAfWGGSZoSwNzQVbqmIoE7bHk9PTWA-eUrqYUl8uETq3n5FVrFqN29XDadeKCbeCJZxIV_A6hVwT-wvgV-UFpn0Ap5DPY9azna7j1oZLXIOtbMgnxSRRQsfaJy5GFebFXrkPz73-6nqipKFVH_3O_dK1gRQSGWJkJzCyuZRnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYInDnQ8OdLEkFqsmhOz-AJQx3l6gWIoCTWWzoTEAaVnx_gvIEEcMXtn-PaGXIlv19Iylw3NXymToz-VcAYpENkMIMCibOme2rJWN38_NSNKxjCI-XUf-2h112CtPWnGsLVcuCejq3da2mTpPr-Tk92p7EeTA2KF2rD-nPGr329C3y0B3T50aFbrrnm_wmJiuoR2blLTwqqfOLoeOhJvkD1rG9ZqIHudMWOe6qt3xFBt7uLYwHTlc3OANoRIYl5qIspdnr1584gwoYFGbg4B_622TkAMOJxobElLhiNX7AF1Z56bUwwvmdN_cXG48Pe_k-XF1e5aqEfcyeAMpRrVWf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYInDnQ8OdLEkFqsmhOz-AJQx3l6gWIoCTWWzoTEAaVnx_gvIEEcMXtn-PaGXIlv19Iylw3NXymToz-VcAYpENkMIMCibOme2rJWN38_NSNKxjCI-XUf-2h112CtPWnGsLVcuCejq3da2mTpPr-Tk92p7EeTA2KF2rD-nPGr329C3y0B3T50aFbrrnm_wmJiuoR2blLTwqqfOLoeOhJvkD1rG9ZqIHudMWOe6qt3xFBt7uLYwHTlc3OANoRIYl5qIspdnr1584gwoYFGbg4B_622TkAMOJxobElLhiNX7AF1Z56bUwwvmdN_cXG48Pe_k-XF1e5aqEfcyeAMpRrVWf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=gkjSfnPLOAoKs5sbKkaxvgMaIJkuPp5DE5n3u0auvSwNGI3vWwf57Fcqk7qtRTSkeR_GEFyPsxOvpeQicZmHk1BSs7eeEULDtm3mJArCHOxqeibNT4N7T3S4rnyXW27YXO3COGWvhC_hPQta0RWjCxVfLrscBj_TBKpi9zhdudQ_g79_hAfwT9luYuhJwGplbVStM3BoeZBXSJh2xDm-AxEIP80YAodKXz1Ky9-Qkkrpd9uWDh6yR-qdL2caYwYNqbWgq7GiJ4tjB11dVl1tbxsXgehQmxK8VA5b1vXVLvFhcimSmep_cAViMKTH0v0EFvvAEu376gn-FG2fGgZWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=gkjSfnPLOAoKs5sbKkaxvgMaIJkuPp5DE5n3u0auvSwNGI3vWwf57Fcqk7qtRTSkeR_GEFyPsxOvpeQicZmHk1BSs7eeEULDtm3mJArCHOxqeibNT4N7T3S4rnyXW27YXO3COGWvhC_hPQta0RWjCxVfLrscBj_TBKpi9zhdudQ_g79_hAfwT9luYuhJwGplbVStM3BoeZBXSJh2xDm-AxEIP80YAodKXz1Ky9-Qkkrpd9uWDh6yR-qdL2caYwYNqbWgq7GiJ4tjB11dVl1tbxsXgehQmxK8VA5b1vXVLvFhcimSmep_cAViMKTH0v0EFvvAEu376gn-FG2fGgZWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEdW02WX-MQBEA7htnqBOL94BrnCY0iT9tPLME3jWPtE6-AcfOE5kukp3KzL44xm5QcQf3CZXpbUnI2bfIGv10nMNveK2Jew_scFJWZg4IVhGpqSjFN77G_ulAFYgBD02_othhXmT_9RIOQHxLvdN7LoDpfhwWaJfXMBxcV20gB94ze77s3J81wOG1FdNZlKZq1EFzVKzv-ECY_EkJa_TOulZfLuQok4Qdn8KWDPJTwQ-7FFU7DRI0KvcUZW_zHdpPb2sDyyksVsVIAPWkbUfK3ulIKnuo4llwzjionBccHk_qcRKBWjJDliVTkVNoKeRA5fpGn2AOr6DnVJBO2ghg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHDZWkn5p6ifHt6x3rvT6Yu2ohpe8IQMP-NrzJUReVtsRcICGnoS_d0_9r-PO1O4Jo1xYGx0y9IkkZNQf_8H8QbhPqumfOt-N3385W0iwmXiayWeiZ3Grjvh73IUhqVXfZ9iAmPK6uWLA1XkAzQE-pf1WNZifvDBh2Fu3XGBsafNnBo2tO53DeUejJlVvo7E6nirUzM491aDmLlP-kQpeMSo0iGN1FKilCqXmGOBJlE6wdHuYzp7uHyTLKBRc9kxnxXYp2yfsGHVpjTNQCRzxUzE18rRHDAmCLw4x4ZdBz2eVvTBqLCKZWndO5fyWCzC9e6m1T9qVyMLwt7BwSl_1IrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHDZWkn5p6ifHt6x3rvT6Yu2ohpe8IQMP-NrzJUReVtsRcICGnoS_d0_9r-PO1O4Jo1xYGx0y9IkkZNQf_8H8QbhPqumfOt-N3385W0iwmXiayWeiZ3Grjvh73IUhqVXfZ9iAmPK6uWLA1XkAzQE-pf1WNZifvDBh2Fu3XGBsafNnBo2tO53DeUejJlVvo7E6nirUzM491aDmLlP-kQpeMSo0iGN1FKilCqXmGOBJlE6wdHuYzp7uHyTLKBRc9kxnxXYp2yfsGHVpjTNQCRzxUzE18rRHDAmCLw4x4ZdBz2eVvTBqLCKZWndO5fyWCzC9e6m1T9qVyMLwt7BwSl_1IrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDzeqhCgJT6c4bJtBgfPnxKEeEZD1QjQQ3vLRz4ZkMxtH20QhcQZrFoOKipsd94H37G34-a-CCHc7Vhv5Ia3Eic4wVaudc_BXdnevz-LMhCiKmb-WLV-2796Wi4aLJiMaGqaYDBYQ_5tGx-696lYIx0AYBsjy85FdwHz2dCrkNuQ4EYSsVPg7RUptuaEdTbJE8oYlMvl9P8X20_7R40aQJ7QA80CCDCjL1BNmAvjfdCXVNdIDx4pzXX_HiC_Ne114h65p453z_LgorIun2nBJQo2ySa_tpAHKdj78MPJJXNyc0xuiEDZuM9sFWuVfKG-sUBgctyMopsHjqRQB-Mrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=mrX_y_wT8qNeH6DVAw2U3QX4Xp7eiUNUENVQfyYpF2ZTvc6VGeLK06DmHNiv9LnYQH7iE6jeGjva-dIpscmCgk0neI_Q5iDbLYYxgKUecTyM1AVGuahiSZJatSO3yfpWgFb5fyA-4hjjzHBhRMj0OmxO1fcOjtOm_CCGPM41yiS9bx9ER7QIC380vaft66w8BbOyflK3rYcYiwUH-au7NEjAomPjhEQa9ow6dCVowS4nTsDYZwy7bsexqffl5kXn7TBSzsoK58LYcHiKc99UT87SmPAced3H-CPRK5HbJDoL4_V8zzwYYHLaSim1za5dh51FrdeHM-HGFGzebpki-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=mrX_y_wT8qNeH6DVAw2U3QX4Xp7eiUNUENVQfyYpF2ZTvc6VGeLK06DmHNiv9LnYQH7iE6jeGjva-dIpscmCgk0neI_Q5iDbLYYxgKUecTyM1AVGuahiSZJatSO3yfpWgFb5fyA-4hjjzHBhRMj0OmxO1fcOjtOm_CCGPM41yiS9bx9ER7QIC380vaft66w8BbOyflK3rYcYiwUH-au7NEjAomPjhEQa9ow6dCVowS4nTsDYZwy7bsexqffl5kXn7TBSzsoK58LYcHiKc99UT87SmPAced3H-CPRK5HbJDoL4_V8zzwYYHLaSim1za5dh51FrdeHM-HGFGzebpki-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=rhcjYLIwZ-MhmYyKd_2BsQa5S_EaphP72TFhG9WyGyKTbV70Bgc1Jdf9cBmh54QKO_-pWjM9o-JGf3wsOqbbsRxPzHq_5RjGVeu9fsLD8hncETKFd63ljgOygP3iLD3TYRYp4CkH33W_-FIt533XNImlh4gmw2XPv9R1FBhe0OyKPA7uMsT-iQENtyrU3rp6Xpw3q9FXyBpHIvGi-hOLiuDjgzmNDx3p6x-zkr5gUFJEfLFnzvfDofUY8loP8cNaHLC94PsEgokl3QXmiM_ocjHjuBq9jeBbFECS75qm5Z1EoXqvoaLzu59Z2isJWWnzEaZH0ZEeUxGbxjPCqKufGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=rhcjYLIwZ-MhmYyKd_2BsQa5S_EaphP72TFhG9WyGyKTbV70Bgc1Jdf9cBmh54QKO_-pWjM9o-JGf3wsOqbbsRxPzHq_5RjGVeu9fsLD8hncETKFd63ljgOygP3iLD3TYRYp4CkH33W_-FIt533XNImlh4gmw2XPv9R1FBhe0OyKPA7uMsT-iQENtyrU3rp6Xpw3q9FXyBpHIvGi-hOLiuDjgzmNDx3p6x-zkr5gUFJEfLFnzvfDofUY8loP8cNaHLC94PsEgokl3QXmiM_ocjHjuBq9jeBbFECS75qm5Z1EoXqvoaLzu59Z2isJWWnzEaZH0ZEeUxGbxjPCqKufGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=uGJtELBhSJuaoI0DeRFafE1o8ibULmW_9eLdVtJ3pgsRb2jRudbmqDVQUNI4Wi5Uj9TxEaPCzPuehKb0Ofbw2ZG2848XLd27FPuMex2AJDII7LdH3Z37TtSZPufaRFpBfo1yYXdMaw_74SGAHPGzjiA0VWsnqp68wb3xiIJFndonHx69Hnv5TZMVYWRhCWkq9tcGKUhLKuRSMnfTDuwCB3ouujL8i5nsEw3LUwRkaC9CB1Ewmi9IwrbWae0nXUfwbaHuuV-eRPubibqGgas--qdrmSwhr9B9Q98IFtA9Dyb2fZlGYZMIDabfkHGwQAanZqH2HHiRdOqcAx-9oYOC8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=uGJtELBhSJuaoI0DeRFafE1o8ibULmW_9eLdVtJ3pgsRb2jRudbmqDVQUNI4Wi5Uj9TxEaPCzPuehKb0Ofbw2ZG2848XLd27FPuMex2AJDII7LdH3Z37TtSZPufaRFpBfo1yYXdMaw_74SGAHPGzjiA0VWsnqp68wb3xiIJFndonHx69Hnv5TZMVYWRhCWkq9tcGKUhLKuRSMnfTDuwCB3ouujL8i5nsEw3LUwRkaC9CB1Ewmi9IwrbWae0nXUfwbaHuuV-eRPubibqGgas--qdrmSwhr9B9Q98IFtA9Dyb2fZlGYZMIDabfkHGwQAanZqH2HHiRdOqcAx-9oYOC8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXIUbe-Ua60r1tPdx-ehapD2RcNxOOKHEWEN9toEL7nNn4Jbhwyu5sgzNazAfI5WhuNCGnUE8J0IAHdAuKQqFvaJUQ2e2y4NblzrI1zONBp3pdPpS-qUWkfQMEPH27_DaKuy3gjylHgr3j6Iz4bds8CYYrgUUBqnBTa5hjtT3A0pjtalEMyt3Rr6tQ-osLupf8kGmBDzYUCF-49Kt-Me-2DBjbdseiE4-SVevjyn4_A1Qm7UGT-0oc_bUJEUD7vryOskEvW0dDPAHujMG-qtbpIO98WQu5obxeRjejYOUTLaJHWexG8Dq135dl3vdm331aVK7GTaIEpr0fPfOgI7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ8hsTRJMvNSwExFXJyw67KY1AE5YoGOoKjNp6WATy2lTtRXSUT_60VGz103qRCL9M0sT4p-4hCPFha9kbfbI2wy-pgCKbMyb0TFX36vEVRyhJdBrNChFo4eZUSV8UAoePOh_84qiYgO2or8QDluro_y9SkT4ci0tfvl1JK1rvuYAm0ULWFaI68PzYd_XlnFqfGPpuE5ZOKqyX9ft6H9uFEw0lf9kW-GIRxJ6dBLkmKcK0_HLWr0XgBYVxNXd_kBa2_UaoA_yRS4l8mrN_QMZ5g1ye57Y2QyKq6s7ESLb3BuzPRDwo41GEmTK0Yu7pTQhXrPkaqi68a7w6AoekRSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=E2K-ukd7ExLjyI831Wz22yo9YHweRbbLf8omQkj1LIxosJ_6dLaoho7nznH3rJ9gkrZpMzcZjw4aR9K0xeL_8_G-hp6GdyS8JLT6jD9pdkb2wWTFruEDchDFRMxXlyVBnabHZHhLyAigKMKzGELey7RdbJurEXlrXm6FnhwnySnwD9eXSmrYo1UvTN5syqsvTTjzI2a2-UOhiE1HrlcGo-mhbw1tapIkqwsaQFHGe4uBOEPpl5HMS5hIlkTtyrMVz05VqegCEURn7vVsa8mUf9YizfAQkB_A1slrTlCmn-C7_UDvzl4D9vDO3miORtr-Ddl5MdWBdNTKsCxfPhivbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=E2K-ukd7ExLjyI831Wz22yo9YHweRbbLf8omQkj1LIxosJ_6dLaoho7nznH3rJ9gkrZpMzcZjw4aR9K0xeL_8_G-hp6GdyS8JLT6jD9pdkb2wWTFruEDchDFRMxXlyVBnabHZHhLyAigKMKzGELey7RdbJurEXlrXm6FnhwnySnwD9eXSmrYo1UvTN5syqsvTTjzI2a2-UOhiE1HrlcGo-mhbw1tapIkqwsaQFHGe4uBOEPpl5HMS5hIlkTtyrMVz05VqegCEURn7vVsa8mUf9YizfAQkB_A1slrTlCmn-C7_UDvzl4D9vDO3miORtr-Ddl5MdWBdNTKsCxfPhivbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqAyaYPmYC3QyORs2zycSfl8G7CwVP6vhYzfmNVzajGj2v7MaO-uqi8oTRlL-9LYw4wPxMFpOs9eomCgpCt5oPCcGEROcW41ubAk2G9xQ4InqQ5tW5ULLgSY1pc0-y16UVmcMLRadiLW-SLyCB2Bm94Odww9hCKwKTt8CkPC3vtYtKhIpRmjOgUQZeLkKEY5F2HCTk_sk9Fyw0ke56ggJZEqQIBXEnizsRbX4vhQin1xmZoAphtiDuw4YsfbLs0Bztrl79oTSWzg3NiA5_s3aRlAfuYSA73k_VUn5NDuD82Zk8NWb45jzFttMo5ykKtIVDcFBRpzP2OePbF6F72B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se0lyps6Drpg71wbaxdWoCO2IabWpFPG_N8P05EXzdND4gotTnCaj-tRXFZ_FG7w-e-ndgt0_WnmentH1Hep3_7U4-4n2VYnLv779OGSQS-bC34KryI3kKs9h40AbRpdUIdPuwXKJpPHpINwIfM4TpvlPbXRANLH0E_XBhjrZUu7rqYb53ogf4y4ppT1MJvyONJhGDmJn3XkKG5OjEX7LfbW6pmD6My3u4BhaxJYmZA1D6k6eY8Y3a3E0ixFV91s6uw0LVu4uhe_0zsRDANMwMyFmo-aglOXZvcVRKqHc7Ju4-c2cAc3zAabpdITOlmSRE2ywE3sFIV_zORIVrpdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Xqnozr2D0oEtM2trPRDw8Z6v2S1VGfvQKcHApbxMcRCY8gkwcrPgpJv7fR-xTX-cBncABcxBImmZhIQxMCBqrr2bdXI3Lia9eTxbbQ-BFQHFbReTwCUiylQyTUEqEGktZ5Y0fR4tHFp4wiVpZLGsmj6sKeRfGu-CYApUBlDlTFQ7_G3X8XlimGexnqEBAyPvpaW8npCnQ8M09Bd_1SZ52Wi6VV2aSx197belMMNDrsqtB8stk3G6CGCVG5eBNFOWGbGXxogVZn5jx6jeEwP0q6B1FnM_CSFJwOVjE5vxvtUxOvHx3zY1I0k_yJmxznxx4Xd4Sod63rNAAu2YzwU9pwUg8aE-qzRFY0BEJjUe-38LiYnWYVk1yxLvrc2c5xB5Rgpa-BU-_eNWUD7nSQYjQrZf-LVxi94asltOjWPr_PmUuCsVu0p2DywK9SBWZJQJi-GMslapZ_wzpW3784NhidaTh3dW_rcCdTgp7iblx4mypWYftW5UtLx1hCLV8qoVgBHn5U-SLpKIhN7BsjGjygqdrREgP4PpkyZPFs2I0R7wo31dOPBjcT5kdY1BC26MrQm_QhbzDQIcsiektMHL-wipM52R54WVlWJciRMruk2q8eOmmfvp7NOTqyvpTMPOrz-cgOZTHFJSWJbwuRzSf54wsJ5UbrMpbHvhEtfMq6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Xqnozr2D0oEtM2trPRDw8Z6v2S1VGfvQKcHApbxMcRCY8gkwcrPgpJv7fR-xTX-cBncABcxBImmZhIQxMCBqrr2bdXI3Lia9eTxbbQ-BFQHFbReTwCUiylQyTUEqEGktZ5Y0fR4tHFp4wiVpZLGsmj6sKeRfGu-CYApUBlDlTFQ7_G3X8XlimGexnqEBAyPvpaW8npCnQ8M09Bd_1SZ52Wi6VV2aSx197belMMNDrsqtB8stk3G6CGCVG5eBNFOWGbGXxogVZn5jx6jeEwP0q6B1FnM_CSFJwOVjE5vxvtUxOvHx3zY1I0k_yJmxznxx4Xd4Sod63rNAAu2YzwU9pwUg8aE-qzRFY0BEJjUe-38LiYnWYVk1yxLvrc2c5xB5Rgpa-BU-_eNWUD7nSQYjQrZf-LVxi94asltOjWPr_PmUuCsVu0p2DywK9SBWZJQJi-GMslapZ_wzpW3784NhidaTh3dW_rcCdTgp7iblx4mypWYftW5UtLx1hCLV8qoVgBHn5U-SLpKIhN7BsjGjygqdrREgP4PpkyZPFs2I0R7wo31dOPBjcT5kdY1BC26MrQm_QhbzDQIcsiektMHL-wipM52R54WVlWJciRMruk2q8eOmmfvp7NOTqyvpTMPOrz-cgOZTHFJSWJbwuRzSf54wsJ5UbrMpbHvhEtfMq6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETi5iRZfS3Mqxyti6ZEr_S_0rzmdNi0wnp3C9O0FofgmVke-8T8ehR5aM1s7T0RlgcuL_D9yWVdl48vxEHhc2rj96UD3lGfwNi3lDkzpX3WTpt242wW2mKbmfuTeCwijRSj6RuycRWACNYR_uSSyu0RdHWTf652WPZDoY1Bc4RswdklDVcr8psihuKttpptgc4znasojQvW4rDm0H7i1DnGJF3Bq18jYMgf-o715IUq2JgcFDeVZcTcjxZ0niKpNpgjWtLkMZo3JVKgFUvMY6Wo9wG7HbcgaGBeUYgzSDxw5RrG1yH-mwBtjd9IASlYUTMIrUoWHE8VU5s6bF7zo08Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETi5iRZfS3Mqxyti6ZEr_S_0rzmdNi0wnp3C9O0FofgmVke-8T8ehR5aM1s7T0RlgcuL_D9yWVdl48vxEHhc2rj96UD3lGfwNi3lDkzpX3WTpt242wW2mKbmfuTeCwijRSj6RuycRWACNYR_uSSyu0RdHWTf652WPZDoY1Bc4RswdklDVcr8psihuKttpptgc4znasojQvW4rDm0H7i1DnGJF3Bq18jYMgf-o715IUq2JgcFDeVZcTcjxZ0niKpNpgjWtLkMZo3JVKgFUvMY6Wo9wG7HbcgaGBeUYgzSDxw5RrG1yH-mwBtjd9IASlYUTMIrUoWHE8VU5s6bF7zo08Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=L6mHxud98rvF8O0TanpuXOxfhIQqKyd3snExMAAcYywx78Sn8ZiFqhcCR8JbIwWBBpMlvm2JAOEnWAXj-3VxIpi3yW7raR73Bt68vBj3lOGDRPKsstdYoRcE76sSYKuXILkRe3D3GEBfex0fxNv1nXTdV9rpslKsRyUGY2eiC2rQ3lcsvttTX8PvMghm1iBm6phaI0i70lpF2bvN0p2kErOKcYB_0FPZIh7shNAbaXRXIgKvcCztqcSuR-58Qg7ukgI6hOcfTjslKjKmGtZjvoHmnJj8EpQechgvYL2SY5i-9Yq3I8OxFnT_v-7Mwx3S343n6xEYMK_vaIKEZskB0Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=L6mHxud98rvF8O0TanpuXOxfhIQqKyd3snExMAAcYywx78Sn8ZiFqhcCR8JbIwWBBpMlvm2JAOEnWAXj-3VxIpi3yW7raR73Bt68vBj3lOGDRPKsstdYoRcE76sSYKuXILkRe3D3GEBfex0fxNv1nXTdV9rpslKsRyUGY2eiC2rQ3lcsvttTX8PvMghm1iBm6phaI0i70lpF2bvN0p2kErOKcYB_0FPZIh7shNAbaXRXIgKvcCztqcSuR-58Qg7ukgI6hOcfTjslKjKmGtZjvoHmnJj8EpQechgvYL2SY5i-9Yq3I8OxFnT_v-7Mwx3S343n6xEYMK_vaIKEZskB0Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=mfFMOubgRhZnZnXRQcn5kC9TCe1MAyyD-OzbNZmNxozS5pNafHw_zIz6y8J99A_RWk7Ho68hichWm5Eh7xfLiuKyumopM1Wgk5rGz3TysmsJrxCV8RhJRxDR7-Oj1e994cZCKxsCTPaaoczp239w_YcgIkPWOmHBu2icD4sWqwhFi1_gkhPFK1V7bGgtG2XVeOeD3c5EmsPZtkZvh3MoXrTTrzslhTyMyMxG1zppt3gwONYYAK_7WfNViPMU0QXF6ytpkGfD0Ca4-qrHBmO5lq4B53aQ4EQPPjPekTJZYIShLSSSDX2ZZuGTNmO5GwvQgWHc8z9GllMaZQbxfqggmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=mfFMOubgRhZnZnXRQcn5kC9TCe1MAyyD-OzbNZmNxozS5pNafHw_zIz6y8J99A_RWk7Ho68hichWm5Eh7xfLiuKyumopM1Wgk5rGz3TysmsJrxCV8RhJRxDR7-Oj1e994cZCKxsCTPaaoczp239w_YcgIkPWOmHBu2icD4sWqwhFi1_gkhPFK1V7bGgtG2XVeOeD3c5EmsPZtkZvh3MoXrTTrzslhTyMyMxG1zppt3gwONYYAK_7WfNViPMU0QXF6ytpkGfD0Ca4-qrHBmO5lq4B53aQ4EQPPjPekTJZYIShLSSSDX2ZZuGTNmO5GwvQgWHc8z9GllMaZQbxfqggmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz_HyukULF49XqAUzHB4mUxBReTPcnyZUWj9Z54mLAJFePzm5DOVBwsJ6aSI370Xm67oq1yKvALA6dhHpiP2vFvwm1bFitPoQ8Z8dsA-_uwDTHCSl-wZfOxdB6Z9zTgdiEZy96WucR2YumYjR_4QdO2Upl8EgLlrrtYJookrV7zQcVS9rB2EeC_pIKvZeVkJ3G3ELtWavxhwLAqepBX97EHk1SgbL9L02vsV9aIRixuJVY0na4LJ6BK9ZXiD9-sSyr6IQbd9psZk2CzP_dYmw4-FXvq__Eowuc-4Km4kIFIFxqlLgeV9qjdgX58ycOhOsWGvwVnczPBOKIwpKuitEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWGgYwifzjFRV6A2VgDfIJmIl4cpRu6pC81gj8fkVFXOKvI7bEPRdmJgAeHp1KCd2za3DgCGxBvcGzBcpWzvUEEkNogycCYRQDcIIzoUGLF2sqksdy-BxY8NXptVRFfdKY_RfZkrkhIhS_BbxbvBNA87Qc1ju1JSgAjXAWfUoFUvPAfXuzYuKAzmONYsPVrFLTl2SD5ZZJcIgYeZnQlNTNbQrGCIaNsJbDxbN7L8rvzlkL32LxgezGwB9ouRVmVrRLz-axcOcwXebfTAwShFO8o7QzxmloWVunpptY47O9SbHQTjyZTNSVY6xUGsV5vyOdDmbQaurl22Y9g-XR_HnQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
