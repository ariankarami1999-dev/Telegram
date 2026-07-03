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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
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
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyF_JP3qdOXU2uEvAUl91kSTTiUKm6yREMfkkLHgh216Ig2JK1GZCuyDtgd1vLv8ylnRQutIA3kxbww9-iywomR0PTGxZjSpJDAfgH_ZCqpa4MKYdBFHsId3X5Yl-A0W1Qvts7KcFQZ6RxEeFD2PV2ghZm3Os67MaAKcTb_DLLH53rp1w5cdOe6meTA2eYDcFumTA16Egk4CcXrCobzh4AQR8K0SL2RL3-WevpUWFqChucfESKkD_I_8nDyd-N6MsRPwG5aQPGalH0B9n4TjQtbLe84D5nVrkeOmaEC8tSoGIQ4jc2_PmIygI9PsZXlbaBpjUN3FAlgerQf9qLfPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oszrrPQ7whdGIxbeK_CyMqOv36argMYa1P51Sg4wT42C9TS6NEuevj9w9LAlTL_GgwoDe5Bc4VezwUD_QSjc7GbsdgXp4mfTrdXa4AiP-iMj2mV13MZY0Q48LFjT7nS9HUJt4v8OHsM6n9HPHbsgcZmS5OQgvZW9N5yE3VHeKtpnHb8lismJfiDAUd12PW0tbZKhN2eUkbRHSpn-QsWHWmGNK0QG9D5RTt-CZTO0DTHV1MpQSjiRraCTd7dbbP7jIlC8_N81ds-VXOjp0skwnkbSqejDdpgX1OFHjrUP_ZRfy3k13qDWfeIZxdqMMwZnHxkmwyIEVIr_MoYw3_WZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chkXavzWtplJ_lY7nK1aMg7df4yGcRlVRhEJzHj9ovHVpTM4rR60AiVArdVjrLa9NgtfAjQFrE-LOCWQRh985flNPvnr4vSXQkEj90yBt3_aflg0gcB3bF46vssm4zBLFrZFszJsjSNWE5iLke5PxhXjfR1F9y4egdT5FJ-zKNI16jtovVv4FOJgFVbwl9vjTwLgNupCsXukVGdkP-QRsAyowyE8MrndyuzNTjVpNXlLFvQYaD-_CdB4jA0Bm8Ew575lcMNuE-hVBSQ3Fl6Jk1ouL_a5Wn76CsKGe-wqejAdgXuLEfh2XlDheBlEcRq2egTpDWBE_ft4AZ4hnDzw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI6UEoIptYth5i_fvshTcfoWo3yG_3KzxZWhrl-gJtgRIynck1Fe8L4yGxw--4WFQixVPUGET2ylmNgRkBeo31BcmAw9u0dp1kUCXcGjmsEh4-teqLU4OaiCfklSjAZn_8BD0T_uushorXoDWtT-BrANhuVsb4o4ZCfc3jQbHgdlYmOWIxK5bdzeHJTeuA5iwwh4t6uZobXkQbzGeWaYwv3HFLjOSQpqf8OLyWF6RA3oLSiI_b9gO-i2ZU8vlQhccIVXuC1Dv_8ocDKTfK0f9jICoCfxRseVOsXcwKaELYIMbu3eZBDMbJRVRs0nrBpSBK6tmXbK0MWlpisvIS_1VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6Eow52lCQwQgB_YoEbam_QcBMe0J2U0j7LEHbxNI2orkw-BNDRzRyNRdpjuP5eVR_d12xFknbtKi3xEK4xuNLpg1oAMn0LwrAg2Cn0wsvXqjw4drrLYC-ooFhYfiFigq5b96Zh_MpKCh9urP4-NuDZupiRAP46J8qG01Fo8uew94HzcPAxhLWcE0KxjuZqODO01j4V29UhCF8a9-IKWCdngXYY0sbG_tdmMiZ9B81lbu9ZBWUvr-ZYok-h3TNXAsPuxE76rpXuUXtoFmEfXgE4AcsuLMZ9f2T6lKODLmBZAQEWbM3GVYWKTqyoLzjxhTfoksX0OU_XdAaZZP8ACNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=fndLmVC-VJhQo6JySvxLrzXS7j0JvlKsBmsCHWYpRHXOKqufrXVDXpWNpeR66iMW7aybqIXVGl7816jJZ_wxeh0XTL0S3QDN9XOuLsck8zjBDBjuDqHrcRQOEgDjDIXrTdizh1ByHMy9ZCu_8HJpQ_NekgX3NeyKVPCE2DpJIHhoYtFWzSvATmnTmRlNCNRMl7YQ08oguKdU8cJLG5SjZBSMcmGizaSRzIi1s4UvCatG9UcN_CKzH5QLEioXOepGWwPxw3JikXZ2kOteQJbrp71o7v2W7YOkx6iRH_ppCOWEbTJ2Sn0lbrWxeCREzzlIxBjvU9y-gHV0dmFNLTIwEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=fndLmVC-VJhQo6JySvxLrzXS7j0JvlKsBmsCHWYpRHXOKqufrXVDXpWNpeR66iMW7aybqIXVGl7816jJZ_wxeh0XTL0S3QDN9XOuLsck8zjBDBjuDqHrcRQOEgDjDIXrTdizh1ByHMy9ZCu_8HJpQ_NekgX3NeyKVPCE2DpJIHhoYtFWzSvATmnTmRlNCNRMl7YQ08oguKdU8cJLG5SjZBSMcmGizaSRzIi1s4UvCatG9UcN_CKzH5QLEioXOepGWwPxw3JikXZ2kOteQJbrp71o7v2W7YOkx6iRH_ppCOWEbTJ2Sn0lbrWxeCREzzlIxBjvU9y-gHV0dmFNLTIwEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=uVdaJA1WWbYbO5uG0PR4HPGHyEyO4hxmjkdCW985NKcrN-GYRNz5379nz1j-Drm1Bh7e1jjTSFZqT6Jugp5VvcfyL_dhNT1iz1bVjTGkVT4e6TJXERgDQHYgx7GG9bGpIVg1VwkzHPjU2efdiw2qKJBz4jIFUscobE3_0DOBRajjFglscg-hgUqJ3ItjKd3qISYlDTPDYm_pDy3SaCBhHGe__qkZcx7nDjGWzS4JupYvDj9MrqAKhsJ2BwB0YhHQfnNmkifMXzcYGDby693rA3GcSlYHmzetWJN5UCe93tynO34iFcd15kZEq9CiSNw8KjTitqAXKYf2-doYlJjxXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=uVdaJA1WWbYbO5uG0PR4HPGHyEyO4hxmjkdCW985NKcrN-GYRNz5379nz1j-Drm1Bh7e1jjTSFZqT6Jugp5VvcfyL_dhNT1iz1bVjTGkVT4e6TJXERgDQHYgx7GG9bGpIVg1VwkzHPjU2efdiw2qKJBz4jIFUscobE3_0DOBRajjFglscg-hgUqJ3ItjKd3qISYlDTPDYm_pDy3SaCBhHGe__qkZcx7nDjGWzS4JupYvDj9MrqAKhsJ2BwB0YhHQfnNmkifMXzcYGDby693rA3GcSlYHmzetWJN5UCe93tynO34iFcd15kZEq9CiSNw8KjTitqAXKYf2-doYlJjxXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St20yGnAJxxwTTCiVzuHR1fa_J4J0pmSJ92NUFkmTY9YiZpPq1VKmwF7uwgcR1XHHh8mfGaDNVc2N7tCchuaR-_1O87Wjr11YE2iqPfwByxc597MVl_P3bjnBifnfAvQbDDYDeLO6t53HLfRoBXONqE2IBJ0GeJ6J6CKtUyEo_0fSqevXDf3mugLfajv73YH0xPIxAFF9SLa2JUWk67yAfSagVddlTDXyEPwUOdwScRizKY2_lMJjEMqF-aqBa1FHNZPdPv2998LFx8SOeITV-YDs-5BL6ipwWOV-OCvTiic5GxD6jmq4Dr9Z2BCJOu3IHYq_buOBwmWCCKnVEzoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=RvCxZaLB98DuUmcezPqbOPTVBq_xo0Fsa3VtfpWC9AAz2K3hqk814HltDrMwl1-JDVnu2W8sMzi5YCQdrhW-HTB5njCEscI22_tZrBCQaOeCVxbtdQ4xIXkOquOH7rdGZ6JN_TX9a-obZB_509dgR5oLUPftPIuzeoJ-FaMrK3OF95tpnsZxQuJ4CjTGdPsclDdEWEJdQC0jpbJ8jbxjDWEugJQyGGGUV_Q_NFc3SotL4NKh_k9OoFhn6sHi6sPsCO3ASdT6RB0zLoiCfI4TusOhpB1g-wdN2kGCk3eT04OuGR9Qd-LYjmK2Is0a0cvO8bjqd3USiHaB8W-SlphvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=RvCxZaLB98DuUmcezPqbOPTVBq_xo0Fsa3VtfpWC9AAz2K3hqk814HltDrMwl1-JDVnu2W8sMzi5YCQdrhW-HTB5njCEscI22_tZrBCQaOeCVxbtdQ4xIXkOquOH7rdGZ6JN_TX9a-obZB_509dgR5oLUPftPIuzeoJ-FaMrK3OF95tpnsZxQuJ4CjTGdPsclDdEWEJdQC0jpbJ8jbxjDWEugJQyGGGUV_Q_NFc3SotL4NKh_k9OoFhn6sHi6sPsCO3ASdT6RB0zLoiCfI4TusOhpB1g-wdN2kGCk3eT04OuGR9Qd-LYjmK2Is0a0cvO8bjqd3USiHaB8W-SlphvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=DM4NxXFBkwasP6JdEtWrWUfytHr5-EaoUskoSds5rlqPIceQa4E3H32MrUQbFobf1MJVMakjWKDpDYCrb-iNp0wq_eO_kRTbBCtsQ8K7htm3QStnff_iZCfgtBfNU386AS7R2LXHxR7sBnAn5ZCMtpADhWLKQ3AEz8x3GlzwCay12tojNVTNweecIQUin_z4Yp7-XGd6Yx5qPzI-_W-HR_G2diZn82fyHciA_vZOEK-y3HJHMwDsxvHF1tZURi0E-n5PprywaS8rRRFWoxELwm4yoHYA2WH-WXZy3S3PNGgtFj8IjNhTBwjBauEJtB2vSXSQ_pAEcItI2_Zgot5z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=DM4NxXFBkwasP6JdEtWrWUfytHr5-EaoUskoSds5rlqPIceQa4E3H32MrUQbFobf1MJVMakjWKDpDYCrb-iNp0wq_eO_kRTbBCtsQ8K7htm3QStnff_iZCfgtBfNU386AS7R2LXHxR7sBnAn5ZCMtpADhWLKQ3AEz8x3GlzwCay12tojNVTNweecIQUin_z4Yp7-XGd6Yx5qPzI-_W-HR_G2diZn82fyHciA_vZOEK-y3HJHMwDsxvHF1tZURi0E-n5PprywaS8rRRFWoxELwm4yoHYA2WH-WXZy3S3PNGgtFj8IjNhTBwjBauEJtB2vSXSQ_pAEcItI2_Zgot5z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=TVkMnvkf5A_gZuGODozcALnU8XS059ZprP9M659DJTSt5MTsucW0DI59mQliulR6Ut_RBUFwezpZq1-FOeHOGaSWdBQKGKp37vkKy5ovCLUb-whzmi58XdwU-qUx8gMkK_-6do310IJaOOxGtYDyeA2LX8CNa1m0JNHVWWF-nTuTtVTVxfRu6fGkzy3_T8zulcnokHYNJBA8IB7nY7Cpa2JYaih6lt_f0NLChUoy3uGamo5Pbxs1cQ3VkYcKhWMYHCGtvgRrIaCs6_A7iLhzD84j53t_zh-wagvErA0s6bfQjnYeEGQGC11e6HOPK6TfLh8niyI52TpdVy9vAkcVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=TVkMnvkf5A_gZuGODozcALnU8XS059ZprP9M659DJTSt5MTsucW0DI59mQliulR6Ut_RBUFwezpZq1-FOeHOGaSWdBQKGKp37vkKy5ovCLUb-whzmi58XdwU-qUx8gMkK_-6do310IJaOOxGtYDyeA2LX8CNa1m0JNHVWWF-nTuTtVTVxfRu6fGkzy3_T8zulcnokHYNJBA8IB7nY7Cpa2JYaih6lt_f0NLChUoy3uGamo5Pbxs1cQ3VkYcKhWMYHCGtvgRrIaCs6_A7iLhzD84j53t_zh-wagvErA0s6bfQjnYeEGQGC11e6HOPK6TfLh8niyI52TpdVy9vAkcVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=RIfCf0FpjOyqZweYJLiaAkF4-zgVpssfl2UF8XyaUyt_3zg7KTdbL0s9QP1hDye6FG39iOjavy52ggq7nl0kBhesg-MxbhxK2VfMYAv8VSJpXqoWOuUURmUgBN7DuuSWnxM7d0HlYdIDGuThmN2s_fYts4s_u-oiqIbNrEU-wU2IK07Jm_kYHj3PGn8rMHYKENV76zvK91jJmqFcopfpgqaQqsV_6jyoY_QtzMYsauXUZJFNzvfQGpu93C2mRXKqJtqLYcAZ3msfI6cuZ26ktjibMvsG9m1IfOR3uubKl86bUiJZ2SeWmdeqIpKEHmggx-VlMoUpuS7OnzEi4b70eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=RIfCf0FpjOyqZweYJLiaAkF4-zgVpssfl2UF8XyaUyt_3zg7KTdbL0s9QP1hDye6FG39iOjavy52ggq7nl0kBhesg-MxbhxK2VfMYAv8VSJpXqoWOuUURmUgBN7DuuSWnxM7d0HlYdIDGuThmN2s_fYts4s_u-oiqIbNrEU-wU2IK07Jm_kYHj3PGn8rMHYKENV76zvK91jJmqFcopfpgqaQqsV_6jyoY_QtzMYsauXUZJFNzvfQGpu93C2mRXKqJtqLYcAZ3msfI6cuZ26ktjibMvsG9m1IfOR3uubKl86bUiJZ2SeWmdeqIpKEHmggx-VlMoUpuS7OnzEi4b70eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIZSSbLFvNh6l5wS0__lbXm90ZlVfoWuKuvIn8n6Mfo3N6WP8HgRSzGNkdzldGTRyY9lqdWjZ1NRKozXcsTqA1294OKGF-N4fuUy4kU-QwWQxwUV3XLhCow6JKp_AxBM0gsJ-bP3x1XS71iQiDIbJHShUEpzxcjek26LBLZdTI14xlwZB0dq8RVAULEeTFs8ve-YtnZhOhs4hMvydsj27RisVDAhzQxuXBe-KZHvlAi7_ILf3I1WHZ42HEojvdCPQieCE8MukBib3U4e7_Uq0-__dlAoILFF5RDjPqb5JvgGSllukI46eeSWGm0OY6JfBohTrgRr9JDzCPRF-GkG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Kg2im98KzSWR99bHCpnFPki7SbkB1hNHB0CKmqT47--e18aWreeb9oYdxi7cYPBNGekcEWUjxNEqghnau158veRjS8zIK82pIvUUyiAUdOenvvsfe_rq8x91RDRuVJeM3f2-GykrshgmGPtyQxTpgPGUJ38ENF_VT5b4pfzcPXmh24unX5SlNJ8WZPp1cCLu4cIGGoe9GkGXR9BGiuZ7-K9ZiK1hEZzeIsD0HaV8squtj38yMFh2e4SoTwJDUXT2TZsuUS6jyFr93VEUOArhFdNsOdVvCTOpWNVrZygC3NRkdN0_m6prP11-SR4YxSNsYKLhAYNEt9J1tOvG6a3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=FN3973AgQVyU1A_lFouyW_6Pgm9uslj5wSTSZfU51qjY-BSfLqThvjyGfRtLJEHrwOHMBqFG-xvjLj5H04sdoWvIA4Q_aklnghCWzAMH6heIjbL_3Ct1cnY6przLK6tBNpiYLRggVKJ1943TRHwWdxQGc0g7TuglHHiLs9ymYNRJwnGHHAqm-wLXrTH3Z4yi0ZCfymvvW_Y7CuEGZsiF9a-kGhM9of7nx-Kso-tlOMh_0WQFDeYBjQyM_BZknDcYr8cFdzUZTqib8PxkM4OT4t6BJQjmSG_T35cIn1TLgzwFhJf4dnP4oFoxHs6mr-KdI16L_xNjZtekGxHHv-aGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=FN3973AgQVyU1A_lFouyW_6Pgm9uslj5wSTSZfU51qjY-BSfLqThvjyGfRtLJEHrwOHMBqFG-xvjLj5H04sdoWvIA4Q_aklnghCWzAMH6heIjbL_3Ct1cnY6przLK6tBNpiYLRggVKJ1943TRHwWdxQGc0g7TuglHHiLs9ymYNRJwnGHHAqm-wLXrTH3Z4yi0ZCfymvvW_Y7CuEGZsiF9a-kGhM9of7nx-Kso-tlOMh_0WQFDeYBjQyM_BZknDcYr8cFdzUZTqib8PxkM4OT4t6BJQjmSG_T35cIn1TLgzwFhJf4dnP4oFoxHs6mr-KdI16L_xNjZtekGxHHv-aGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Ya5qL_OM99PCNLlmP3q1SfCS4osZnDKNqc7IT11cGDd9DIjbjSudWQLeGMg2kd5VW7x-GOfsz30nb3uOuJpxNEBl18GsndSUUuLOskoteZSihwPa44p1CJ5SADJeZL1SUOMdYetgstvL0S2WD0P7CDkOfpa_hfJyJ50PUnsueQphLsq6mx__IX7iTFsM6dEHr3qzWrOuHpCa90xB23jmjYDeLbpgoZzAlMl_tx8ZIZ_ifdmHNOwJpha5Q8uBOx2CL7pknB2xPQ3jsJFkgSvWo2QgQ2-X5iFPw8WYeo4eE8potTm2JgSvqktcrNUMN_0NiVwMgclSsEfqRwn2Ln_Ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Ya5qL_OM99PCNLlmP3q1SfCS4osZnDKNqc7IT11cGDd9DIjbjSudWQLeGMg2kd5VW7x-GOfsz30nb3uOuJpxNEBl18GsndSUUuLOskoteZSihwPa44p1CJ5SADJeZL1SUOMdYetgstvL0S2WD0P7CDkOfpa_hfJyJ50PUnsueQphLsq6mx__IX7iTFsM6dEHr3qzWrOuHpCa90xB23jmjYDeLbpgoZzAlMl_tx8ZIZ_ifdmHNOwJpha5Q8uBOx2CL7pknB2xPQ3jsJFkgSvWo2QgQ2-X5iFPw8WYeo4eE8potTm2JgSvqktcrNUMN_0NiVwMgclSsEfqRwn2Ln_Ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=NeriDNJ-HO6e6kjhr9hn51A5ak9f4ey7UHi04KCe4eq7skvIwMpiID3Q126M45stD9LBr7289h33mwrsNJnuE4QkVS2ixQj2rPfcEzyqmHVrT2jfLlSBtWrT2SWlwgwpcwj44Y0GU_K-IZfF5KVcKREpQaL9xRwVRHUP9hGSI1144SXkKnkt0ePT1j4-KBLRdyzxk44ZUE6SeeZVkws69bxogq2yW4K-fx3QCiTUT518ghuk1V9VMs-qxMt9qDidNFxupKGvs66FiY-pkeUyRSOEO3O37h9Y1byZ-7PUM6TUjac25Gtl6DG1iNjj4EKZr24PJqaO4sGzdyEbzNa67A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=NeriDNJ-HO6e6kjhr9hn51A5ak9f4ey7UHi04KCe4eq7skvIwMpiID3Q126M45stD9LBr7289h33mwrsNJnuE4QkVS2ixQj2rPfcEzyqmHVrT2jfLlSBtWrT2SWlwgwpcwj44Y0GU_K-IZfF5KVcKREpQaL9xRwVRHUP9hGSI1144SXkKnkt0ePT1j4-KBLRdyzxk44ZUE6SeeZVkws69bxogq2yW4K-fx3QCiTUT518ghuk1V9VMs-qxMt9qDidNFxupKGvs66FiY-pkeUyRSOEO3O37h9Y1byZ-7PUM6TUjac25Gtl6DG1iNjj4EKZr24PJqaO4sGzdyEbzNa67A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feOnWnVBST4RFh66UTTPhZoeJjn-LkcPysvwaO3MG-v6v4R5NRgsl4hPMQGgQFjV2SZrjTDp5mAfPAS5Gcn0eU2HaDwrTAGTkIdDJqQPWmaHMGC3TmS83HGH-TN0QAjOlSJiNyonhojaY5UWyzQIcmIk64-9u9KLmRgOYEGwwrCl5nH9neI7Jgn_hVy9DiZNNYxG0YRizFI6ZtNllvW52qFNBMt8hr0YdXb4Jmul7CLsZyrPgAXP7eHiZbOUSJjOORDa-zspS7Q03UO4adnteMFooBSDeYR48VFbEqE4zMwlOim1oXkE9eqkEpuWQTDMaG-tn9J9hag1eu72Z2dcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=D_DaSh96DfAPUpzkHo7QFUgPqcoeyawI17Fd6MhfmfOPIvFQbH_kGLghos4eldcDz-9eCQIgTaWNNAeezeSkonjpWmOvWXnyaBVfvTUi54lOmOrTXy7pvC81a7Ni_y4h9Vpx383FAz4liQGUd3qq-jeDqjnA2xDLFkJFMq1gfG5falaJxzCUvW9MKbiHieFk-B81x5BKIxZIdIS3RX_22liohmPVpuOko14fSvxqQaVSIV6_OsoP_NPrOCQqqMp8Ubf1_VfgqSnz7oXZM0qD7G4-yK6CHL5J15Rs6aaFK6laWDLqpfdEBRhljf2MDw-RFAeGPAYVGQgaB8oX382gxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=D_DaSh96DfAPUpzkHo7QFUgPqcoeyawI17Fd6MhfmfOPIvFQbH_kGLghos4eldcDz-9eCQIgTaWNNAeezeSkonjpWmOvWXnyaBVfvTUi54lOmOrTXy7pvC81a7Ni_y4h9Vpx383FAz4liQGUd3qq-jeDqjnA2xDLFkJFMq1gfG5falaJxzCUvW9MKbiHieFk-B81x5BKIxZIdIS3RX_22liohmPVpuOko14fSvxqQaVSIV6_OsoP_NPrOCQqqMp8Ubf1_VfgqSnz7oXZM0qD7G4-yK6CHL5J15Rs6aaFK6laWDLqpfdEBRhljf2MDw-RFAeGPAYVGQgaB8oX382gxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=O0wkwrz_ncIINdQYeD3VaRqHrefaetz1jEEW3ywLCsOfvWE33n5cWeBwL7xG3eagf-YYgnJpzZzxoqYEsS8Oe2buFGfXWlhi4t0kApOjdRiEg9oNXUlXYJmn2oPLmKe9JCupRHzabyO_j_QzT3hiUpjh-qOsqF3ZPiDOACP0CIJ30a6qAONCi6Yykd4fq3PdZq3C6WcjHG5PCIhrEuM3Bor4kHcI-_mPFbk_x_KET_eEGbTmyQDI71_wZaWgfIXbE4FF0vDMCRz1KvycVr3vi2XEyq9_m9cCAxUwOIWoww5XwXMIWPQ1WAX-DDZ5g1sPMwy6TXsD7FYIPXRd0FO7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=O0wkwrz_ncIINdQYeD3VaRqHrefaetz1jEEW3ywLCsOfvWE33n5cWeBwL7xG3eagf-YYgnJpzZzxoqYEsS8Oe2buFGfXWlhi4t0kApOjdRiEg9oNXUlXYJmn2oPLmKe9JCupRHzabyO_j_QzT3hiUpjh-qOsqF3ZPiDOACP0CIJ30a6qAONCi6Yykd4fq3PdZq3C6WcjHG5PCIhrEuM3Bor4kHcI-_mPFbk_x_KET_eEGbTmyQDI71_wZaWgfIXbE4FF0vDMCRz1KvycVr3vi2XEyq9_m9cCAxUwOIWoww5XwXMIWPQ1WAX-DDZ5g1sPMwy6TXsD7FYIPXRd0FO7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=lbyA9K-RgMxj4wQp8nbGlWhVPh-gauGQr4d8aFEq0_y_QZ74rEoHGfGTa6Huas1TUK00sschqeLCPcs-JMWrfPTeF6k2Xrbw8-pBc4Hv4KR0UB0ACoAsBGLdMeLmDq38MBwVfK4PDgQXVtL8B7jM99ceVzzTJfa1vgAk1A-vaMBvk7NfZ62VQxYVszkPHLmjpj9kBTWO7ST4kWqAej81e72HeezCeK-VfYx2FVzG-IMSkadZ34FY-sxC8qPSVvaoWiIWEy7HTpfZOXrrQKbAH-n_v3aJMh4chjOsXrJh1MjKZ12KI6Tx0mJb1PEk64V3xhGmMLaYPPNlT6rJCCs0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=lbyA9K-RgMxj4wQp8nbGlWhVPh-gauGQr4d8aFEq0_y_QZ74rEoHGfGTa6Huas1TUK00sschqeLCPcs-JMWrfPTeF6k2Xrbw8-pBc4Hv4KR0UB0ACoAsBGLdMeLmDq38MBwVfK4PDgQXVtL8B7jM99ceVzzTJfa1vgAk1A-vaMBvk7NfZ62VQxYVszkPHLmjpj9kBTWO7ST4kWqAej81e72HeezCeK-VfYx2FVzG-IMSkadZ34FY-sxC8qPSVvaoWiIWEy7HTpfZOXrrQKbAH-n_v3aJMh4chjOsXrJh1MjKZ12KI6Tx0mJb1PEk64V3xhGmMLaYPPNlT6rJCCs0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=a5cPBQeOeQHyMKTwJ0_nIQ3s4tjBxC_6VUPo-t0e7-Um75T0Zuu-sisHXqlnuR1DX03g_8JnQC_jinRdusoMSodXN3t475a76syfjPIyJ_EFJNE78lmYGX8W_r-86FiWAzY0lxO6j_2Y-OpbXzY2-ryTYS443X1hkjlwVAMzC1PrpK5HwttG6Y280cvvhgOheOfyYpQzQHTbzpen4weZHEP49y3aB4twM00Krm3Gy85BL6U2hOdtPsIcJpZSuq7OY_gsCUB4rR1rwrBO4TUvWQRNwibe2wXYYXGsDtENLDH5Ah938UTJUJ9rh7VqQZ10z_FI0tvy2SSbrwIttBmIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=a5cPBQeOeQHyMKTwJ0_nIQ3s4tjBxC_6VUPo-t0e7-Um75T0Zuu-sisHXqlnuR1DX03g_8JnQC_jinRdusoMSodXN3t475a76syfjPIyJ_EFJNE78lmYGX8W_r-86FiWAzY0lxO6j_2Y-OpbXzY2-ryTYS443X1hkjlwVAMzC1PrpK5HwttG6Y280cvvhgOheOfyYpQzQHTbzpen4weZHEP49y3aB4twM00Krm3Gy85BL6U2hOdtPsIcJpZSuq7OY_gsCUB4rR1rwrBO4TUvWQRNwibe2wXYYXGsDtENLDH5Ah938UTJUJ9rh7VqQZ10z_FI0tvy2SSbrwIttBmIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_8I9d80F7lsiKJMVMJgYF8V43uUjj90b07fWrxCUMJHLF-quqJImhldFaaoy6aoxYyg_fw6lSxnedHwV5ImWjzOsEzNJc2uo1XouIptFnLKRwn1lLDcFSTA1LoU8e197gRfvSI2wQorp2tNP2Rdls36LO9PKiERG4WsBvNK-94EcIiU9lSfgHmiQk9d5zfFi8spUhx28E15gVp9wKZAr-ekYETHQKL1OsWGyQplMlWZiog2_-PvYkEKJ92UJr1faeYEo81UQhl1KNbXgOqu0nvzEsqzSXDLhDNi6STbc5xNxRm4uD_KDCxgLmWQte8f_oKRE6CuAcfSsfMihKnc5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=QyeGFX5DyxMSBxfCH8mgsjstgDKJ7DguprGRvFyimGRa5r7rbj0s9OLlf7YoqfrZbXlgUqwvCxhN49P4br8qLeqGoy8AQbn9GMfCqP-nqZ_V5wZq91IQqozJhEU3QSUgEi9hL3XclnT1uwe6R1kvBJCyXO4DMb1F_YYPYby7crBfgiHlKqwO6h-HO_g2NJpnSbTKH9Dn1TERcD6A2h2t1b5o7rcVChIxFEVub12XMTntpmTt8FvsLLunJDviABkNxSFiEN0c5AvqykZeQS7aLYfoomRPDuXOKF_Xb3ENkcqTBGuiSJtbG3uT-8b2C60Xs2SIc4_P83czXZAEMNKvJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=QyeGFX5DyxMSBxfCH8mgsjstgDKJ7DguprGRvFyimGRa5r7rbj0s9OLlf7YoqfrZbXlgUqwvCxhN49P4br8qLeqGoy8AQbn9GMfCqP-nqZ_V5wZq91IQqozJhEU3QSUgEi9hL3XclnT1uwe6R1kvBJCyXO4DMb1F_YYPYby7crBfgiHlKqwO6h-HO_g2NJpnSbTKH9Dn1TERcD6A2h2t1b5o7rcVChIxFEVub12XMTntpmTt8FvsLLunJDviABkNxSFiEN0c5AvqykZeQS7aLYfoomRPDuXOKF_Xb3ENkcqTBGuiSJtbG3uT-8b2C60Xs2SIc4_P83czXZAEMNKvJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OEutLeCBJeaHnBeiCW4CyPbC0MR1TdUMek_dLlZDyAQ6A90ejh07as8erN_ohyAB6CjD4Ioh_g302z1lJxalQ7tZvfTvjU1jljEthHNciTTHY59N14zGdN3D_rk7j6n6w-x9tdw9p4IYHo3wLcwqakIL-D6-fT0wI4aq1woOcJ7-fUecmF0K2laKKplvMHZ0l5EkePUruCawwBKvSUacQV5qI4hXTcJeYqbqo8mVDJhJkODlV8j4UgG8kCGaJvnGinzohxoKzKPIxpv9ajawQEfjqhnTeAiDpjhOwwG-pctrPYZtmEpY82IqFXzzp5H2vgypvwx-40jWR0aQnTE-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OEutLeCBJeaHnBeiCW4CyPbC0MR1TdUMek_dLlZDyAQ6A90ejh07as8erN_ohyAB6CjD4Ioh_g302z1lJxalQ7tZvfTvjU1jljEthHNciTTHY59N14zGdN3D_rk7j6n6w-x9tdw9p4IYHo3wLcwqakIL-D6-fT0wI4aq1woOcJ7-fUecmF0K2laKKplvMHZ0l5EkePUruCawwBKvSUacQV5qI4hXTcJeYqbqo8mVDJhJkODlV8j4UgG8kCGaJvnGinzohxoKzKPIxpv9ajawQEfjqhnTeAiDpjhOwwG-pctrPYZtmEpY82IqFXzzp5H2vgypvwx-40jWR0aQnTE-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_toIBE0a5YPe9nKc09kvOE8NWiwKtHosOUCTc1Gkaoc3dsHH8zk6EhqZzUE01P97KSy0-sfjV1smVAeqLTDpL33MSusBk61qNAoftHS6grD2U70JKdAH1d3HNSvaWeBf3XIUwasTHz8kJpswDwLTkhkHRne4S534zNxH7LTa1ddcqZ9DSB7a0xBt_5zttYztp_z5lUS6PeLkzox26EiYg2mZLpfcIH_LONeQjaASzTrnqSVdtKCtbxFBMLfcszzPG7Y2GhkZDl_F36GCQWbBxqS_jQQCvA0_3b0ijdbAMuAttvPJAdeCIsQACOSk5vPJg9VQhEJW9_xCkksjihMPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=IICy6mMERStR-Nxzo8-xHkjg5nkrpfSbd_zJYbrdAVUN7-lVLt_50LUhZHZBTVIHV1S-OHx4gKutotRuNg3hB8WLaH_9wxHuEs8bq4T0EQ6uwGXnxmObZQI8PPxRy3ESCnDPMMutaEhk7a71mwb3Dh44AUrVzGZxJNy_iKD3v2QTNqwSA_znE_pNLsSeiZjm0GFuKYHh3wW0LxusfY1xxNNaK6zali9NCp-MPV60we6yi5nzBXz5oWg875iOSP4ck1-iR8dycVcerxPTsxwMZNzDzw82LzEnH88a4XJU2dlHw8Rqq-jreZB1W5KJ9YRUFJdfz0n-E2molNMJK-Ujvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=IICy6mMERStR-Nxzo8-xHkjg5nkrpfSbd_zJYbrdAVUN7-lVLt_50LUhZHZBTVIHV1S-OHx4gKutotRuNg3hB8WLaH_9wxHuEs8bq4T0EQ6uwGXnxmObZQI8PPxRy3ESCnDPMMutaEhk7a71mwb3Dh44AUrVzGZxJNy_iKD3v2QTNqwSA_znE_pNLsSeiZjm0GFuKYHh3wW0LxusfY1xxNNaK6zali9NCp-MPV60we6yi5nzBXz5oWg875iOSP4ck1-iR8dycVcerxPTsxwMZNzDzw82LzEnH88a4XJU2dlHw8Rqq-jreZB1W5KJ9YRUFJdfz0n-E2molNMJK-Ujvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=sMU9TAvOZvjuLORr12h4EMFpBtwr_Dz4Z21LbJGtEDnxD-E0O0YTewYtuwiclRajuuzrLn0a7CJLO31byRkFLIuzHRgX1IeUPAmewrfjxsCDvKVc4mx-Qg-5Hw6e1e2GY5u4lmgQCY2nqQHIhrogFepMNNZZN4GFV2OPilwUiAre6Siu4ZvKEMlgd4YPm_SjP_K1-LiwFP9-mkYt40uR9qQpWqs5thuk5_beddzzHzS5KhB3DlwGrFDjcR760wiLuV24ZH6ptjtDB9TQaAfISixtkfseB8mnXVcEcCSR0Wv6Xx2gYSZ2lbrOC5ZEzaig48A9J_k-OaeajnzSS-UlFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=sMU9TAvOZvjuLORr12h4EMFpBtwr_Dz4Z21LbJGtEDnxD-E0O0YTewYtuwiclRajuuzrLn0a7CJLO31byRkFLIuzHRgX1IeUPAmewrfjxsCDvKVc4mx-Qg-5Hw6e1e2GY5u4lmgQCY2nqQHIhrogFepMNNZZN4GFV2OPilwUiAre6Siu4ZvKEMlgd4YPm_SjP_K1-LiwFP9-mkYt40uR9qQpWqs5thuk5_beddzzHzS5KhB3DlwGrFDjcR760wiLuV24ZH6ptjtDB9TQaAfISixtkfseB8mnXVcEcCSR0Wv6Xx2gYSZ2lbrOC5ZEzaig48A9J_k-OaeajnzSS-UlFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ4WS0PGbtoh96R34NfOPvanNC7xq8NwzfVAWJ463jNmqAhhc7OO9f93rp4btD8aeWwsFDJsvW3gjzNpELPu6eu0GYlZERghvg7B4dkSNV9y5rddvMyQpWIMNRQuDyN_tIqrMbof9HeKotGVD09Kuf41GTyezbJs2SN_J4PB4vn6CBMymJfvwQaIKQ6sK9WGOsiss2cU9xcoPfpijnH-OPNrWlRPYLJ9Hp-iTkClYi7Zz3U3srWjEWWseYCO9hyB5F4Wz2fDJgkXTnxsaREMcbJ31OJ0B9GXlTFueLwvtBD_lJOW4n3anwyi1bxvQsp58-7q7upX4osQyZyaG7BS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSiLYe9nzkcqm28QX1GttmkeRSWpnXycCI6JgLYE54gcSMvgPD8OIR2QQ06Az9B0ccgqyFfvHdbrYF5BU_HeysQ6INNUzkze_SoS0QzxkZVaOyZwyDMAAPhtla6KI_9hgWxLTOm3f057FqZZoFxlZ5Zi-REtTi_0UDX-44YXN7e8EVVD1hkCpjROrNQjeWxuWv1LF89mfH1CL5o6PqPUz4LEamHRtb-jLtS6l6qI9QaYZoy9kTYyk28BwN6dSrP35Jb65tl6-rwmD_-6Jj5BoQ87hrLKuU92QStO3CZKLHDQGunQa92xZB1aTbrAMhu0V8SunvV_I-uAJahePEk9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leOkAyLe93KywDdXJPnOpN72wUmtbvpwyxL6i03f3UssjFvwJGZznzWbQSA-KBx7dRpDvT6Aco1U4NP7uE1V81poUBEIo6GCMxLDWuY0OeR15e_m_4dS-rIYG2nK8FELphui_0yVvG3Wez5ySQVN9KaLQzB3PvfnfyUVKpRU4qWjdbB4GHQfJ82gbb4mgLEuMRi-Jrd-D61iXyTR4cFy9N2CkJGu-BS3wm-xk4i0UF7TvoFJ5NDYdjnsZKEnOEfdn5eZyiflbb9MiboiVEyX-Vufoa1FsMhD__ZzYEK7ui4CTFMiQgWTfrACR7r2chHCCaSsrDNSVUGBrNeKQ2yvIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=E2vmo_kTX0D8nQaZJQS56qn_Zr4YWzthv39nL337UbS2E5gQG9uvbocbHZjStge59dxiFqmormVXZkVEHECAPT9yEO925lKRCA7--4igKmPNsh3rDH5Kk_fCgL9TkUReJmQq-pzitRt4nMUZDOnU79kNuZTZEJPuTgD-UVavz3dAo0MtkY1Bwq3Zk9LoScpCHWPhAce1pt3YnIXDwDcBsS-4U9Z8Z8rE1Ls_Kk1bD1mU_2ncQvCQsaXb3aSgQu5eq6ws5UU4c_MJ0KM9oN8WvsGNVtTIUMYo422UZ9V7HNHZY5lRy8w3QRDQsKfedc3QNbXtDme_AS6nhDNjFhpXIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=E2vmo_kTX0D8nQaZJQS56qn_Zr4YWzthv39nL337UbS2E5gQG9uvbocbHZjStge59dxiFqmormVXZkVEHECAPT9yEO925lKRCA7--4igKmPNsh3rDH5Kk_fCgL9TkUReJmQq-pzitRt4nMUZDOnU79kNuZTZEJPuTgD-UVavz3dAo0MtkY1Bwq3Zk9LoScpCHWPhAce1pt3YnIXDwDcBsS-4U9Z8Z8rE1Ls_Kk1bD1mU_2ncQvCQsaXb3aSgQu5eq6ws5UU4c_MJ0KM9oN8WvsGNVtTIUMYo422UZ9V7HNHZY5lRy8w3QRDQsKfedc3QNbXtDme_AS6nhDNjFhpXIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_xpOpzpfLZ1yeeshyQUNZjC0txV9Ar29RJI9kLfHSB8rXxoirRAIgtdLZyK67pVmXuwlE8wS6Uyfx_HMPNCWJxsaWdcXykd4gW2bIXaW7N2EZFde_fgYoIlNAdU40fThwJNlrKZjK49dfL1E8jRDAtUSj-p7A2wi7dvzugVwjfU_hozkt0xUL0vBdxv68gi_uAuBRTbVQC1zDSV03VcCEcg6LkdKMHhtU-GaaOWorD9uy_Mf6pUIJFuGMfSJUBQrUJD02C20Jt1yH6A39ONwKbL6TUmaUgFPzWnLIYRpv9jH55ZzLHroufzaLq51Kk3ISddxs6dmq9o0Lg4m6YOA05c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_xpOpzpfLZ1yeeshyQUNZjC0txV9Ar29RJI9kLfHSB8rXxoirRAIgtdLZyK67pVmXuwlE8wS6Uyfx_HMPNCWJxsaWdcXykd4gW2bIXaW7N2EZFde_fgYoIlNAdU40fThwJNlrKZjK49dfL1E8jRDAtUSj-p7A2wi7dvzugVwjfU_hozkt0xUL0vBdxv68gi_uAuBRTbVQC1zDSV03VcCEcg6LkdKMHhtU-GaaOWorD9uy_Mf6pUIJFuGMfSJUBQrUJD02C20Jt1yH6A39ONwKbL6TUmaUgFPzWnLIYRpv9jH55ZzLHroufzaLq51Kk3ISddxs6dmq9o0Lg4m6YOA05c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=fScMWAsEnwq4fgA8NZyUvy60M-aU5I8T9uyAxLAiyklaQFTdOozeQkXhFnLitSYqeKMpbJGKjWp0EdDP0XX38Y6ElJiZtOt2QA8M2OYNY0DPXL9ZQuHyoCSyqqxqUWYcPDkh_-ZfO7MJlCrHdLG4pQebnaxONKt6mTtJVkFs7PekoXWXjqC-91MXSRE1lNsa6G92znHxX5LoXQ6uhJv36OXEplQcyN4LZyZpFQeoFZUDsrh-PbSmHGIi_5KmPlMPLy5uzgzA7u646JX746BXnPY5xm8o7u-XHu6sHf09_ANaL-y9wxIDqGWp-mjbd0pDjkCieDWbn2GXzrb4Tdo3jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=fScMWAsEnwq4fgA8NZyUvy60M-aU5I8T9uyAxLAiyklaQFTdOozeQkXhFnLitSYqeKMpbJGKjWp0EdDP0XX38Y6ElJiZtOt2QA8M2OYNY0DPXL9ZQuHyoCSyqqxqUWYcPDkh_-ZfO7MJlCrHdLG4pQebnaxONKt6mTtJVkFs7PekoXWXjqC-91MXSRE1lNsa6G92znHxX5LoXQ6uhJv36OXEplQcyN4LZyZpFQeoFZUDsrh-PbSmHGIi_5KmPlMPLy5uzgzA7u646JX746BXnPY5xm8o7u-XHu6sHf09_ANaL-y9wxIDqGWp-mjbd0pDjkCieDWbn2GXzrb4Tdo3jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKbbf3p6gPTuo_malik7WUAc292PQmn4WQX388VM7cRBNpjAxY_XIdz_AeEGfB2L5O8IzsG3gfOWPap6zqr9fqgYs7LKlJqdZ49-2f3n28xjQmVdcuq__7tL-WuhaIe7U8iNqfOzw2-03JRXzSK0dRyIIzgO2i7uTzGchIzYbXcGB4ldwYxHFIqZQRwteORPFKAsPrKgeKDSXgq0IH7TitdMSDHdfPLiFrpHLo84d62hX2G-1HAptYxiYt93U76o0_ExGtbjMfT2MOsU7hz985P7GLRBK9Pd9vNQph7gCLxcGH9CGFcetYPYsz_0DriuoVhqETkiizKFRFLCI_iZLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTifwo_rjLs5CnLYGnIEI5nKsqTwrSgLgz_h5rfYzNdS5BjdHZ2By6gkMNF0J98-LbF5LWvsmdY4c0L4hcVCWlbtq-pzKtQcAJeKBbNpyAaqgLPYsU_57mLhylOF4KAei6erh040DLe3S-7C5ac3AnqUcxl6U5QMzDh1VpzvO5IcQ7o-npHW_WKynQQD9FaHJsvevFoikeQtHyCuwDCeuhZQ5cncUtf_XDyQ_vyUluXJHM3KKQvghJUmRVoKbtNECZXEEokMAwRhnFjmTXC9gLCrvOgAYEp4Jm7GAZAJi3saBD8dOAn9N64CMgpTzaJDKTDr3DJz7Owdik4QJoNpyK-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTifwo_rjLs5CnLYGnIEI5nKsqTwrSgLgz_h5rfYzNdS5BjdHZ2By6gkMNF0J98-LbF5LWvsmdY4c0L4hcVCWlbtq-pzKtQcAJeKBbNpyAaqgLPYsU_57mLhylOF4KAei6erh040DLe3S-7C5ac3AnqUcxl6U5QMzDh1VpzvO5IcQ7o-npHW_WKynQQD9FaHJsvevFoikeQtHyCuwDCeuhZQ5cncUtf_XDyQ_vyUluXJHM3KKQvghJUmRVoKbtNECZXEEokMAwRhnFjmTXC9gLCrvOgAYEp4Jm7GAZAJi3saBD8dOAn9N64CMgpTzaJDKTDr3DJz7Owdik4QJoNpyK-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=jCGBL3JMyQggLaTqoNq5nJ6kmfdI6LlLIK-pkUWclo9wt61Zm0KxQj4yBxpJsLM5HOZbJGAw0JOBTYbTn2VbzUdiXtDevs-SZ5NNwxXrQ0u-aOnWe5_ba6uvr58IgmC82jIKsPklcQeBn4QJWfxRhGfcAtX6TZxVJ9Q9wzkchCxEvzCsHGqgX2AEfYWAem8M5fKF0mqtsJwiWiJ0q_eQ45HJ2YlPo6kMsoM5NjgTF0s0ws-fISVEFKI2NlPVmfxTnwxLDNvya5-PpxSuM0d5FFT-zmgv8OO2dN39g9ebFhKPbQUrSj1tpWYr6FiKL1BdnweF53JTGBW0uDesDm4Hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=jCGBL3JMyQggLaTqoNq5nJ6kmfdI6LlLIK-pkUWclo9wt61Zm0KxQj4yBxpJsLM5HOZbJGAw0JOBTYbTn2VbzUdiXtDevs-SZ5NNwxXrQ0u-aOnWe5_ba6uvr58IgmC82jIKsPklcQeBn4QJWfxRhGfcAtX6TZxVJ9Q9wzkchCxEvzCsHGqgX2AEfYWAem8M5fKF0mqtsJwiWiJ0q_eQ45HJ2YlPo6kMsoM5NjgTF0s0ws-fISVEFKI2NlPVmfxTnwxLDNvya5-PpxSuM0d5FFT-zmgv8OO2dN39g9ebFhKPbQUrSj1tpWYr6FiKL1BdnweF53JTGBW0uDesDm4Hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=NjIZ-9MeCzJ-H0afKzPPTn3AaKHoXTmT3q6iQVJUtlorSa9EUzvR01yfrrEXTyediVfkFeKW7GXUTMpgFLJz7I8-GozwTRAY3v-Iy0bYhySRhCSTAi0kXIyqmvuqR-EM9tsRi1Z-o09-U933F1h9umbzAiO59As7kvNMx8_UlxNdwu6YUz9G6gVg8aBNt9TyxbfGloY7mhq0rAPq87FeZutrLicHdSzawR61oKO-VTquEKxruXLghbcDKnTOeQFVWtqs4QFYRLYZUrTFeNksxb07z65RukEMfLm1H3OC3xBSr7C6RceV4mwC1c_P5lHW7mMwhzKSwr4Ked2xCHe6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=NjIZ-9MeCzJ-H0afKzPPTn3AaKHoXTmT3q6iQVJUtlorSa9EUzvR01yfrrEXTyediVfkFeKW7GXUTMpgFLJz7I8-GozwTRAY3v-Iy0bYhySRhCSTAi0kXIyqmvuqR-EM9tsRi1Z-o09-U933F1h9umbzAiO59As7kvNMx8_UlxNdwu6YUz9G6gVg8aBNt9TyxbfGloY7mhq0rAPq87FeZutrLicHdSzawR61oKO-VTquEKxruXLghbcDKnTOeQFVWtqs4QFYRLYZUrTFeNksxb07z65RukEMfLm1H3OC3xBSr7C6RceV4mwC1c_P5lHW7mMwhzKSwr4Ked2xCHe6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=WFdtBMQl7I4wNoOBRfsVGdwlEryVGdeyAkr6l0_11_cU5nEPTReNmAhRAR1blwN71YBS8qYlHJM-GWQK-q1bSQRZdBOS5AXYufIkncEbCFyP_x8i8XQTe7KgiZnuq8Ei5ecfdd775NUUEgxkN3r0wIDZVE9WMayy2PgAgBHlfhNAXCvYOPyaNYYHDDAJVRrV4jjzqRCI2ypIFff1dospibq8SK3Wf6SU8WE9z4gvmSwia22LH-NlqqNudRUzm8whx4aOljm9tIYdRLnbCdKv5bsbGlcw4HedBVSIsPCQ14AIKxrJiB2DTQ9kgqc5RiRiM3HskXYxNRf27qGHtQ355w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=WFdtBMQl7I4wNoOBRfsVGdwlEryVGdeyAkr6l0_11_cU5nEPTReNmAhRAR1blwN71YBS8qYlHJM-GWQK-q1bSQRZdBOS5AXYufIkncEbCFyP_x8i8XQTe7KgiZnuq8Ei5ecfdd775NUUEgxkN3r0wIDZVE9WMayy2PgAgBHlfhNAXCvYOPyaNYYHDDAJVRrV4jjzqRCI2ypIFff1dospibq8SK3Wf6SU8WE9z4gvmSwia22LH-NlqqNudRUzm8whx4aOljm9tIYdRLnbCdKv5bsbGlcw4HedBVSIsPCQ14AIKxrJiB2DTQ9kgqc5RiRiM3HskXYxNRf27qGHtQ355w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MytNKh8vo5rEFGsV-NAs7BRQ7tsXeR1mDsqKS0eOGp-49v0zxUiu6zXNgF_YHMELBzDsHCkLZdEFxyyvWbq5UUULgyuEtgCCwfTrOUyhlcvRpYYLT299I9ZKkNyOxWVA58SC3moBYHA5Ajz9vZaJAXSzBAes8UcgIQa8ojKcpJSJprPvhXggp323Q2EOQWhwdgbhTaE6FUijx0B1VYXyY0Ljd6yOuAkgMIkvmYhPDr6oGuKrVLOXuZR1e0M2JHcU0G4VECd5UHqDyTmqagpwHGUmQZ2FRa6twvLGXDE88gXLBoxfRHI1jZJXgSg-Xdy32mOFbrtP2xmM7mm2-N-mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STG8ysiBkk0Qe74fhb7oRYIO9NEJ26ysihKiyHO1is0yohfR44q7W_DgONc1XvEH36jvlNnolnccbZKUng9x1xW2yLe1ZbX3D1rG6bONi0fpHEETL1a0LHXWQpMHqbN7EYjC8KYdiYW7FFoi6LNhk4e3usmbfAnOfe-WaW6_N0Zsam-_0l38xpGzM7gSkNpih0ik_tDorMNahjY33j451LSRvARdggwAgJRH5IvrSit-tFjgaeDgPlaztbg0mfgetxySJ3x85V2Kpve-koeiR-RBqmeA1ca2VhsVMBD9O2AYpjpIJiKkyTl7e04KGPJrbh6MVgPbw8O61TKbPmgIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=qO4r8XiKcElujyle6YYLSq2CEo6cbS-px_pSzyzjB2VK9xCORn6xtOHp_ukzt0rzY2q76-P6QmQzzwRAo8qnI6B2JZUddWrnV2vhtx0LX-kimnYkna4oGLquOGe2gzVj2ERWVEXsoLa9SNAxxn3IykNc_a_LR6rAYUcuNhQtAsSjtTjpOws0zmZS9VlxgtN2AYYzCoWe_8l1CZFSzv5f8hsDytlj3BC7pVIl5lAgLBKqqIKb5gbQTrmj8PCfI8_QnZqFEZvVOZ6wdnsYnMJsHiJYbGXHizoLdcnL96IwdzsASAhSO249Euu5MthK1V69SdOifGFrm57bdBWBqZBDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=qO4r8XiKcElujyle6YYLSq2CEo6cbS-px_pSzyzjB2VK9xCORn6xtOHp_ukzt0rzY2q76-P6QmQzzwRAo8qnI6B2JZUddWrnV2vhtx0LX-kimnYkna4oGLquOGe2gzVj2ERWVEXsoLa9SNAxxn3IykNc_a_LR6rAYUcuNhQtAsSjtTjpOws0zmZS9VlxgtN2AYYzCoWe_8l1CZFSzv5f8hsDytlj3BC7pVIl5lAgLBKqqIKb5gbQTrmj8PCfI8_QnZqFEZvVOZ6wdnsYnMJsHiJYbGXHizoLdcnL96IwdzsASAhSO249Euu5MthK1V69SdOifGFrm57bdBWBqZBDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrP_uunw3xb6UiZorxBdUTok-ZH8EUpS-_ukPJTTgqU-FST_zy6V-glMxuGJGjcBv4FA4_SgB4vnwrCunggieBQeqwxUCgTringKgYbtpFpC1veqDVuCiEVXKDSpRquErFarvhGkFugKZHP_Dk3NmRo_Z_2QvS6L3-EBYw1e1WoAAttWZaWP6efkP5nzarMaINGJ1GO-8rHoSyog4UtbzPyCXxNUveat2gpnH3ftKmeYJ1J_5LCdUo02MGWDQWVRXXfLnzL8K61-NFtlHXOmQjoJKUixYclDj0nH7PoNpq67xZyU6ywMR1vN-137K8Tkw8ar8A7vgaP04J9YYFVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHzgyZAYG2tW5LRw6Q9XYD2qztZgBNW585tdNQm4Ielx1PSMsFYVqxd9g7Gt02DhkO-7ML2fk9ZOVgOpCrA7I_aqoBIlFvu6WHqNpLqRXWIdsVYMUsYgBerQcDL5aklDFXdSGmdt7zY9mm1D-glxGrFO-8-azVOlx10Bs5DhWiC6qr5Y3jgWulf4-vVUz_6WY1NjqrcVBRzgCo7lpUT5n-_LC7cyLp9FUdnZeJHTd3aa8g0RAd2n_svmgeH1unv6MCnNqFqWJt58WQHq7H5V7OvPdXe2JBSQJ6nnC1JehxqLKsOC3F-3gkg2fNpG8SQNZ_iWaLCi9avuadeEoQUA3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Q4HbDAm1YbZh0BNKgYs2PXBg1Fno4ECuF8iF7nkAyi00vRXQGMZ3aq0J7XPJteIGcPjWbvtnOfGfZqlm5x4G86u4fKvBQWyo_ll8BUR9EFrY_K3X61yuIR4F-Qns6rpElzAsggkN7gXBASr7ML6Pn-zJ3jktCbx4uoQetwNODO3l12CS1xsQGpeTMN6csfcswkbX1ox6-rMp_9iCxzKeF32UjlWNWp2Lo-CR9BK4JtI6Yb8cRIktWMVKE_8g1Gv5zUQS7bdQwNbYDw_DJsCLzHTiubxPm9xbEEQmliImFuhNolMYD2mZiKMs5p84FLPzvjXe_38RVMKSckBwfo5F5QtoEfygF63VHqTkqZJa7qK9G3Sw0HFOrIyQjXJwQwu2O8BhnxEHHGwB2ofSRboXUhQUNXSNHRQHmyeILZBEID8XhgGSIkHpZ8IO9SH03mWpeXMCNYjFpyjPOtOuDhDq5-B-Y65v2xdUN3Yb0pT6R0ectdLr2hPV8TW4kBIyaarMeNQtAQqCxuXaxznS9JpJcXFa5PLK4yDlJMT0nbFXpJv6b2tOmchYFgnR7inGrktDyB-xzileISzHh_4xO0kR1B9jsEK1tH-GHYMPbCG7sgVJ70MZcAQ3q3RcD9ku84fQsH5gtm2bItzLHBtDZYd7VQOKIurRmhrrNx15NidnnTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Q4HbDAm1YbZh0BNKgYs2PXBg1Fno4ECuF8iF7nkAyi00vRXQGMZ3aq0J7XPJteIGcPjWbvtnOfGfZqlm5x4G86u4fKvBQWyo_ll8BUR9EFrY_K3X61yuIR4F-Qns6rpElzAsggkN7gXBASr7ML6Pn-zJ3jktCbx4uoQetwNODO3l12CS1xsQGpeTMN6csfcswkbX1ox6-rMp_9iCxzKeF32UjlWNWp2Lo-CR9BK4JtI6Yb8cRIktWMVKE_8g1Gv5zUQS7bdQwNbYDw_DJsCLzHTiubxPm9xbEEQmliImFuhNolMYD2mZiKMs5p84FLPzvjXe_38RVMKSckBwfo5F5QtoEfygF63VHqTkqZJa7qK9G3Sw0HFOrIyQjXJwQwu2O8BhnxEHHGwB2ofSRboXUhQUNXSNHRQHmyeILZBEID8XhgGSIkHpZ8IO9SH03mWpeXMCNYjFpyjPOtOuDhDq5-B-Y65v2xdUN3Yb0pT6R0ectdLr2hPV8TW4kBIyaarMeNQtAQqCxuXaxznS9JpJcXFa5PLK4yDlJMT0nbFXpJv6b2tOmchYFgnR7inGrktDyB-xzileISzHh_4xO0kR1B9jsEK1tH-GHYMPbCG7sgVJ70MZcAQ3q3RcD9ku84fQsH5gtm2bItzLHBtDZYd7VQOKIurRmhrrNx15NidnnTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETj_eagXkRsNMJWlUCNWbw8_vS9QjN0u_FtchkppX4RN7X5wYeN79r0eNEI7XEkY0wRQnh7p5R97DIjSK14T0j1QYL33CFLkcp1ocQtPeE5JCX-hYVIncmwQKxVPAsSS99jlBzRok6_nneQ8fPuQMjRlwm989NaLIWf1SS6SINi1TKlf7dj2EASjXr7QljnwcV9IZlYBKgG5Ud3fKUlFug4TQSOwC_SU01NW2thK-L1xr2AladKikEDCYT8vpWVEod3Ew7X4oMeGcYHC1SsoaeC8iiELqpJwBlLRvpdale-YQHsioISeSNHHBzI3FEGIQAo0FBdV4l_NzSY_fV_cIvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETj_eagXkRsNMJWlUCNWbw8_vS9QjN0u_FtchkppX4RN7X5wYeN79r0eNEI7XEkY0wRQnh7p5R97DIjSK14T0j1QYL33CFLkcp1ocQtPeE5JCX-hYVIncmwQKxVPAsSS99jlBzRok6_nneQ8fPuQMjRlwm989NaLIWf1SS6SINi1TKlf7dj2EASjXr7QljnwcV9IZlYBKgG5Ud3fKUlFug4TQSOwC_SU01NW2thK-L1xr2AladKikEDCYT8vpWVEod3Ew7X4oMeGcYHC1SsoaeC8iiELqpJwBlLRvpdale-YQHsioISeSNHHBzI3FEGIQAo0FBdV4l_NzSY_fV_cIvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=TlGbQ5i9X6pypDlkOqxkysMIGihXZBc5tY4zipMLgzAAAgHTB5c8X4jAbAbKtV92lEullyzXr11WgkNqyOQE0lySFv5iH6FMmQOK9aQkg1s70YoOIEHUbJbQnPm58D46892MWnamkQ-yZGuiELxiarmTmklJWG7C2uAgo6zHTIqbZ8Kb_dicym2YAkjGVcBCOYhGne8mqrVFRBJG5fA96-ORNgMRtkQ_vQMEsu9iOrqsT3NFvaGe_GZ4LsGXBoI6vsC1MzzfOpIeSKCHW15IZj9RXZKyY7Qfyu_JLsNtEGQC4_TCLVMrZXLaQOwAOFWeYZFB5eAEp8qA_-mubM182Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=TlGbQ5i9X6pypDlkOqxkysMIGihXZBc5tY4zipMLgzAAAgHTB5c8X4jAbAbKtV92lEullyzXr11WgkNqyOQE0lySFv5iH6FMmQOK9aQkg1s70YoOIEHUbJbQnPm58D46892MWnamkQ-yZGuiELxiarmTmklJWG7C2uAgo6zHTIqbZ8Kb_dicym2YAkjGVcBCOYhGne8mqrVFRBJG5fA96-ORNgMRtkQ_vQMEsu9iOrqsT3NFvaGe_GZ4LsGXBoI6vsC1MzzfOpIeSKCHW15IZj9RXZKyY7Qfyu_JLsNtEGQC4_TCLVMrZXLaQOwAOFWeYZFB5eAEp8qA_-mubM182Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=dut3-mhZFi4G3xMME6_QmmJ2SBd2E6ZcqQ_5-0-TRPv8P6TD8mIDm0Sh_80pvDaCxdP4jO5XuEiwqtmkPCw9oqaFMyTPCxyZICmkwmFF10pxP36sCDkgZleBVHqulDKw7nIter0xB1PuDASnpS9k-TnsRE0G7FmgWTGzO0oU0K8KR3aRrpcR8vxSi1KGh67qdxwhWndqOpf2nzz9fCoBzTON5AMk-X4azM2OHcIrMpxwwleCDiVLvTBwvJu62WJm7z7YvllXVD4kW9FmH8BnN_eh8d7fbXnjkqm6qFtfegE0xy0Wsq6cvIGVB1fOOVGaNCf3Wo9i3NZAJ9SQ-O6MVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=dut3-mhZFi4G3xMME6_QmmJ2SBd2E6ZcqQ_5-0-TRPv8P6TD8mIDm0Sh_80pvDaCxdP4jO5XuEiwqtmkPCw9oqaFMyTPCxyZICmkwmFF10pxP36sCDkgZleBVHqulDKw7nIter0xB1PuDASnpS9k-TnsRE0G7FmgWTGzO0oU0K8KR3aRrpcR8vxSi1KGh67qdxwhWndqOpf2nzz9fCoBzTON5AMk-X4azM2OHcIrMpxwwleCDiVLvTBwvJu62WJm7z7YvllXVD4kW9FmH8BnN_eh8d7fbXnjkqm6qFtfegE0xy0Wsq6cvIGVB1fOOVGaNCf3Wo9i3NZAJ9SQ-O6MVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnvmrM0X5v7r-90aXTsq4G2f6BJB1er0Wg2gA4E_PTXz-QQp6RgeRVI3pTtTlR1IYiW0uA7BQ8yYPnjC3Si3sxldDU9atYWseziPmmKL7N9Sw6sA7iyJHEOjSy3AoztAzA5ECUM3q4JXbGcM-VftG2KlC-7tFBesSuNkbnGaCKxWxzid3Q4XCCS8jrrWzMSF6zYMzBi3ysQ6BH4AtoCBnBk0wEMnl2YvhXKPECrjiUaA1Mh4DME9-nv0aEvNNPtAeCwB-TgOZrnWihbciAHOitMmHLd1A3YPTXT2VIdOe4hNYKtmCKaDfz6Sio6jusyXuh0aRgHRNCD-5_TpxInwiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caA_-7zaIf0ngpX6MYZ1tnB6xQHNZ_aAA57ME_Yrhf3gNejO29Qtd_tUsFUS3cXuGjHZw8T-fQYVwY-gNXAQvJ7XrcqYoWFfsf94g_I1T7P2PHuSwdh-7pLZ9yvD8TkJOXJHpeIxo3sYKRUszXodpXM1gLy3pKcvCT4c3SPitM7gKgvmzhzlQPznKxDAUpHLqZnWjn8CNvVPo8TzW4oorsSOZuEiwh6lhAkNm3WsC9iI3NsOCeLuNJm8r0cnNhXhBRyB3pgXCOTMeVIY9-4LSitVXoJ-QiBLxy4GQ9uUqDq7IxNxXWD8oWYc1PGXahVOaENtispxAi2NYej4AXWHQg.jpg" alt="photo" loading="lazy"/></div>
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
