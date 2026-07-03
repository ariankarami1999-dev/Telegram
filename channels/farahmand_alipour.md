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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 00:05:52</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Gy2L97td1oZWl5pxWeLIiBZ6xAZRKtav9XVpgZF0srKbRS5f9kcYzayXQd4SLy2WmiP8HKziDdz7OfmI9-jbx8JYCNNHTZ11ePqPNlEjHJnNxUCgguAq_OvRf56K6XoFXOBkcLWLlLzvlj-ZZkUYcWoSsYOR8Yl5c_FVOB8if4Oh_cu3mPiMtDn8cvV5IGtKsmnqN1iZIc9axpt13Eq3HXMIwgbgi73qGHJJk28vD8o9frx3u0x-_xpcVAtuVFYub_0CUe0cg5lcOFDduKw2l77CN0DOvN7fGFdz-GmUdQUigf_C-Jgk30zyARDGbp6qkShEF6uCpg4S9WjPseQDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Gy2L97td1oZWl5pxWeLIiBZ6xAZRKtav9XVpgZF0srKbRS5f9kcYzayXQd4SLy2WmiP8HKziDdz7OfmI9-jbx8JYCNNHTZ11ePqPNlEjHJnNxUCgguAq_OvRf56K6XoFXOBkcLWLlLzvlj-ZZkUYcWoSsYOR8Yl5c_FVOB8if4Oh_cu3mPiMtDn8cvV5IGtKsmnqN1iZIc9axpt13Eq3HXMIwgbgi73qGHJJk28vD8o9frx3u0x-_xpcVAtuVFYub_0CUe0cg5lcOFDduKw2l77CN0DOvN7fGFdz-GmUdQUigf_C-Jgk30zyARDGbp6qkShEF6uCpg4S9WjPseQDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KHVPPEt5qSsh3WLxn35RhaGSdNFQ3RaTJOmJ8-Cze8SyD6jbteV-oQitjqg_HZlEuGqnLIhb1GEWIJPbxMlSg8Iv-WKmzX6eRdv48NW8R1XiwoIqmBfTPP3vVw68wrA1s-reknqFu4sVU_A56eMXfNlZOgb5xeg0C17e-_xVpyuu85_IZafjX80HIQ3O4SKyCjpA7rvuRxtnGNxbfY6xTYmcrwqL06dPcHQRwEKQwKQ9RYbsVautg9sd4an6DL534dWi7KJZypxA8LyYZodduX2tDexfxErGoCyxwqPnGCOEvPcTsRV57TCZxtvBFwYmQ0rWXYc5-fGdePIW875BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KHVPPEt5qSsh3WLxn35RhaGSdNFQ3RaTJOmJ8-Cze8SyD6jbteV-oQitjqg_HZlEuGqnLIhb1GEWIJPbxMlSg8Iv-WKmzX6eRdv48NW8R1XiwoIqmBfTPP3vVw68wrA1s-reknqFu4sVU_A56eMXfNlZOgb5xeg0C17e-_xVpyuu85_IZafjX80HIQ3O4SKyCjpA7rvuRxtnGNxbfY6xTYmcrwqL06dPcHQRwEKQwKQ9RYbsVautg9sd4an6DL534dWi7KJZypxA8LyYZodduX2tDexfxErGoCyxwqPnGCOEvPcTsRV57TCZxtvBFwYmQ0rWXYc5-fGdePIW875BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh_lbi64GAKICIj1XanDDf9XRBHZ7iObnVrTHBw06VXmMkfIxIsm49by1SlEv3OX_40Gw3627dglrn2e1sNCsRIcJitQOocvTfhp2bfXtqtBmAsXwX8J6sigFgJ5dE6ccvCp9VJdl9iEDfjmxX66wTwELxzVESz89SfKpqSmGmq2lFcjb_uDr8Mc4WmNVQ0zXL0sxmy5P-ZRTUGXSOSyLqG6DhaG3e48pOlto87UdHwvbqmWuBIimIJhN_5bMmAQfqCVOIdaVtQZa0SfLrnbrjLoNEC_qpyDxeqdy8jfZurxu3lyGJFN32pSvA18JoY04mmAMJxWZI8bvrWa0DoiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIinIAdX9QXQ0ufqVe9spDuHARCXZyg2rHAIW-0917dGsNMcjrVBKQMr-MwxN4hZ__WosrnIFM23uxZ3BkNTJlxfuc70fu50yNMRs28_YY4K5dJVlVGvxpIHWBR1dQRq_5MiVYbJ2UtJM8DIoZJ1v6rOlsGApvoxLwpowl5jttyCqFBusv_BgwMgLJiynAIK0rnXHJef5cbSIHTX_o4ujbT2pnQn3wxekWNsD5VFEmYgQgC0w_IHOk09_DlZLVzPxHkfVArGEeD3P4IHTU4cd911I3OEhNy6e-8bsHjdEqjwprEwbAcJ1y9_pdCZC8k8wfWcedJu_P16d7cZ8RxjYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vCI5_30rIYovcv0IUuJztaMr7GBrY-H8JtOtqIkPDquYS8K5Pp466xpTiy_sMqqKAK5LQvfWAAzLe4o1AtvLtQHEFvb9tjdqXDcRgixSPHIbj427RaeEUXBLNi2G23D-Oa0pc_I5UoWzvdwJlNWHnSQS7zMi7R1XwCcWXK7KrNMHuVgIr8cvCTRyU3GiZDQSbaJe6Qs5WfVJrxhD2MV3n8Iu8oMI2sGGutOPofU6JDkRCzJi6hngXKv0B_Ah6BGfI3S3susmCpsI-GWGrmi28kdtR0bGGTUOGqTzzLdykZ21oO9T5YGm3z-MFRuLaPYICBCnEjX0Aq4aYdTeiNidEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vCI5_30rIYovcv0IUuJztaMr7GBrY-H8JtOtqIkPDquYS8K5Pp466xpTiy_sMqqKAK5LQvfWAAzLe4o1AtvLtQHEFvb9tjdqXDcRgixSPHIbj427RaeEUXBLNi2G23D-Oa0pc_I5UoWzvdwJlNWHnSQS7zMi7R1XwCcWXK7KrNMHuVgIr8cvCTRyU3GiZDQSbaJe6Qs5WfVJrxhD2MV3n8Iu8oMI2sGGutOPofU6JDkRCzJi6hngXKv0B_Ah6BGfI3S3susmCpsI-GWGrmi28kdtR0bGGTUOGqTzzLdykZ21oO9T5YGm3z-MFRuLaPYICBCnEjX0Aq4aYdTeiNidEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=ZeF7Vh6i5MjLQEV5649yjfHgDEZsMh_xTXBvwIHJzUvxSnBg8d9GoBsuFSnfHvht2eIb9zPklvHElhlF5Ieo50ASI33cm48_BpH1qUqHLYk7GIixUPFWCgIjwnRznQtqsZFKNVxWroWxb8o8s4i6Yl9N9QmYG-fxxL34w-EG7FhoZu5GREdfcKpyOZVcfPqX1ilTVzfYLnXMcewSnoRP04or98cxYE9tor4jdE9tH9xm3fM-ePgWLSJoaMGj532M1gy86nkYgRcMjjhTOCiOGY0SoIROBCrb-xhBcNOLwoObzDfjSl2IIBx7Y6r-jinEIvHqVR3CEq27nClqZaaWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=ZeF7Vh6i5MjLQEV5649yjfHgDEZsMh_xTXBvwIHJzUvxSnBg8d9GoBsuFSnfHvht2eIb9zPklvHElhlF5Ieo50ASI33cm48_BpH1qUqHLYk7GIixUPFWCgIjwnRznQtqsZFKNVxWroWxb8o8s4i6Yl9N9QmYG-fxxL34w-EG7FhoZu5GREdfcKpyOZVcfPqX1ilTVzfYLnXMcewSnoRP04or98cxYE9tor4jdE9tH9xm3fM-ePgWLSJoaMGj532M1gy86nkYgRcMjjhTOCiOGY0SoIROBCrb-xhBcNOLwoObzDfjSl2IIBx7Y6r-jinEIvHqVR3CEq27nClqZaaWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=pNZyrR0Pa-zqOSr5NQijgosZwWbsE1LWQ071D34aYfjZPysi50gv-kWA22TkJftaSjmfPak_xk4mUPQxOzkUpphjFP1RQXL-OzHBXMwJi3wuYvw9Ix_V12quBm3wksyWL14whe0AZgjBmxo1muilyNurCvkLg395AKmbeA4YGfL2EDzm2LVPxVmRUki1Lwu2ZGpIeh7j-ThD5k7y1kezxpjg2z8tDWhBLfYhCR4H3UJ2M9qt_YdcMAOOyqECtUocLRFebz8G3GTSwmS05PMZnmFIZedwi-wwDpiJiVJck3gNJlIlr-HE5k1k6YDP1QDzyiDCkzusEgKKvE0_GzkN8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=pNZyrR0Pa-zqOSr5NQijgosZwWbsE1LWQ071D34aYfjZPysi50gv-kWA22TkJftaSjmfPak_xk4mUPQxOzkUpphjFP1RQXL-OzHBXMwJi3wuYvw9Ix_V12quBm3wksyWL14whe0AZgjBmxo1muilyNurCvkLg395AKmbeA4YGfL2EDzm2LVPxVmRUki1Lwu2ZGpIeh7j-ThD5k7y1kezxpjg2z8tDWhBLfYhCR4H3UJ2M9qt_YdcMAOOyqECtUocLRFebz8G3GTSwmS05PMZnmFIZedwi-wwDpiJiVJck3gNJlIlr-HE5k1k6YDP1QDzyiDCkzusEgKKvE0_GzkN8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=GGqT6aA0U7q4HQ1PY_CToXCfSFHM2tD_cAu8HB6ZgyaG08aKaxt5dht_K9zEaD-mf6PKxDhrH6KPEzZAle2Wfj8QK8q3Lt4_61KJkHypawKNYs6g1kpRqCLgdh9nPogRd2RZ1z9EOv1YlbrgFJ8LJIpSIJdMNAfEfmvdHmfQ57DstNSAg4Wy7_ZSQ_XSCz9FYtgiXlh1kG_CMWUuTXx4uhKJeNKa_2VQCkjtL8uv1e61woLaEnRO-8u6o5tYiO5QDv60F_3EsJkJ1ubRRd7fs3qQY4YTTHrGyC4OdTVPZ73hxvgGvP9Giy91CPQLJBjPXQcG6G1mQ6JsjXItoyKFDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=GGqT6aA0U7q4HQ1PY_CToXCfSFHM2tD_cAu8HB6ZgyaG08aKaxt5dht_K9zEaD-mf6PKxDhrH6KPEzZAle2Wfj8QK8q3Lt4_61KJkHypawKNYs6g1kpRqCLgdh9nPogRd2RZ1z9EOv1YlbrgFJ8LJIpSIJdMNAfEfmvdHmfQ57DstNSAg4Wy7_ZSQ_XSCz9FYtgiXlh1kG_CMWUuTXx4uhKJeNKa_2VQCkjtL8uv1e61woLaEnRO-8u6o5tYiO5QDv60F_3EsJkJ1ubRRd7fs3qQY4YTTHrGyC4OdTVPZ73hxvgGvP9Giy91CPQLJBjPXQcG6G1mQ6JsjXItoyKFDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gXvXZLWb7xdPXXu9O4StaPhfcV8wmVxsfdIIVvrDYHH2Mb9gO2sf4hkK049B0aVaZX4Mv5y3rPgtZmrlR2vGN0rGQtJg_pal9tTFgoTX8Ey8rXTTikpEuMq8Mrfw1_J-ySvjLtSu7H4owoos2hZth-_AOQ-twEQR1sTRsrQkwfGJeeiHlsnOC3CzCOaEWRtNbCEol1_EMMTFmnbE09eGVaeBJ5Ar1-H8I_JHH2yfW8CDUK1_gwpRCde8YCmPuqV1XOXrjkgw-fh-arIlcX0KkAbLgssmA2_y_t_I1jlt3L2Ecy1SlD6p5jWeO9Wdg0yoOrvLgIUk25UzXhFXiEOs6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gXvXZLWb7xdPXXu9O4StaPhfcV8wmVxsfdIIVvrDYHH2Mb9gO2sf4hkK049B0aVaZX4Mv5y3rPgtZmrlR2vGN0rGQtJg_pal9tTFgoTX8Ey8rXTTikpEuMq8Mrfw1_J-ySvjLtSu7H4owoos2hZth-_AOQ-twEQR1sTRsrQkwfGJeeiHlsnOC3CzCOaEWRtNbCEol1_EMMTFmnbE09eGVaeBJ5Ar1-H8I_JHH2yfW8CDUK1_gwpRCde8YCmPuqV1XOXrjkgw-fh-arIlcX0KkAbLgssmA2_y_t_I1jlt3L2Ecy1SlD6p5jWeO9Wdg0yoOrvLgIUk25UzXhFXiEOs6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=seFPYiBCp4F_cCdz-LpT9bANrItbdsuYj7_HNNodz_2lO4YHR8TUAtMsmBlw7eaHmZ4yS892cGW6qYFE5G-xQGdyLLHp-sVQ0pGRycGEwPgMg50llWC2DtFwbPMPicBDVEKBonT6ivmkql5Puhmoc8D61rV1f_Gyo55BMVFGbWLxyP9fDfCuMMvwpfDDyvcKLVxS5b26FSOx8VLWDBk9cJggmFZt7FYmROQyU-sxTcAoKbON6vTgqxPskKDf-xcxG_pytuS4oswNFHkn60-zwQhhstsy6d_tMQwb_-lkGkzkkwzi24EoSBmpJiTFLlyarutW3CeMe_fjpGWSrGS90w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=seFPYiBCp4F_cCdz-LpT9bANrItbdsuYj7_HNNodz_2lO4YHR8TUAtMsmBlw7eaHmZ4yS892cGW6qYFE5G-xQGdyLLHp-sVQ0pGRycGEwPgMg50llWC2DtFwbPMPicBDVEKBonT6ivmkql5Puhmoc8D61rV1f_Gyo55BMVFGbWLxyP9fDfCuMMvwpfDDyvcKLVxS5b26FSOx8VLWDBk9cJggmFZt7FYmROQyU-sxTcAoKbON6vTgqxPskKDf-xcxG_pytuS4oswNFHkn60-zwQhhstsy6d_tMQwb_-lkGkzkkwzi24EoSBmpJiTFLlyarutW3CeMe_fjpGWSrGS90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Cc2ZomLxCXKlsfU0Y7j-HmcgFVBFsQlHDWUk1ItbFvKJ4Pv5QpSwJ-3O2CU2IHlG4Ur9utytcAYJaqHgIXdRpEXsUqjEX2m1ZzHfnreb3sClsiVYdjB0u2g75InGxbnhb5-E_iAniwKn6wK9YBnJmrHCZWb2lhVsBipjFBIFgt-vfnbAKKzh3SEtXNbarQEssMFgc1folrbmhe5X8wzNXtvgLixg6hfoliS1uZQqB4POnFzRZSmxfYj4KTk04UXU3x2TtuCIneJ2ur0Mr6VxS3KC0CMcCUA8vguFe_8l7APZSSp5zC1Ls65RP1Lt3wYB0H5ElnBd95dv7w5tS2PA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Cc2ZomLxCXKlsfU0Y7j-HmcgFVBFsQlHDWUk1ItbFvKJ4Pv5QpSwJ-3O2CU2IHlG4Ur9utytcAYJaqHgIXdRpEXsUqjEX2m1ZzHfnreb3sClsiVYdjB0u2g75InGxbnhb5-E_iAniwKn6wK9YBnJmrHCZWb2lhVsBipjFBIFgt-vfnbAKKzh3SEtXNbarQEssMFgc1folrbmhe5X8wzNXtvgLixg6hfoliS1uZQqB4POnFzRZSmxfYj4KTk04UXU3x2TtuCIneJ2ur0Mr6VxS3KC0CMcCUA8vguFe_8l7APZSSp5zC1Ls65RP1Lt3wYB0H5ElnBd95dv7w5tS2PA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPgp96UA4tU6roxOZ5MMjuAXHqjBNmad_NpAMqwepNk7EZhQ2smBBTSmtnfl4L_HtwcVGrh40mY5KbOA91ZcXux3mg1QDBDeB-1WaoKq-y7scZjutRwAH0PsJT3cZuS-fNsCR2xm1bFpvLI99G6N7HlQbmockSw4Smz_zsE2JVnvNxSALwW2IcfPc1T_YD_cgZye7fUVdl-8qLciPpOajrMW1-Xi30P12Qqg_hFTxfs2AMJNkSm0NQhsnUlgSNCDeGU4uNOkjA6tQRQS2b5DKUS5B9ngv4MjOIrpDSQz5j87On2Cy2e6r2b6pYHjZuUNhqsbTAPpVzFX58RqCHVmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=CTx9ITN43_hiZbWO3h7oG0RvtsavKJdhxuZGlyXqQYMza7BbzOdK4zGATMCeH9a1umX0-GbdeFvn4U7_DIaRyPPGObajsZ0ppZpgnLJOD4fWFVF5m1EhHlHp7cTFfbuaH_UMk6eVNzAS3mmHzqQy6EdXKxzc_I0xqZpQUE4RxAY-e9_RAZ7eHrU1-GAWVZkXByu-4rMVvEiy7MwsLUqGbSTJCO90z9WkBX2Fpq5kSuLeG9YFDrrP_CQ45teEik5itUhJ-8I65NuFxbRkRIZ8AfcRLD9eUxRc--F-qZf90W-MTV4fbNv7i3AwWuL_J4xFm5Z0RnWPkq0U_SaWLeTQxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=CTx9ITN43_hiZbWO3h7oG0RvtsavKJdhxuZGlyXqQYMza7BbzOdK4zGATMCeH9a1umX0-GbdeFvn4U7_DIaRyPPGObajsZ0ppZpgnLJOD4fWFVF5m1EhHlHp7cTFfbuaH_UMk6eVNzAS3mmHzqQy6EdXKxzc_I0xqZpQUE4RxAY-e9_RAZ7eHrU1-GAWVZkXByu-4rMVvEiy7MwsLUqGbSTJCO90z9WkBX2Fpq5kSuLeG9YFDrrP_CQ45teEik5itUhJ-8I65NuFxbRkRIZ8AfcRLD9eUxRc--F-qZf90W-MTV4fbNv7i3AwWuL_J4xFm5Z0RnWPkq0U_SaWLeTQxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=As2Ct0GXRmwr8SuUhF3PN8sfgYBPmOREXf2zGR1c-cXmi23ErBqF7JGYq-Y7cI44oNZhkM3lvVZ9CRhye9XikGrYRhTYlVGyaxvMJUCgey0u6BsFI0BZp8fk8-tGVc8U73jJRltoRkB8QHt5pzhum1wvL0BbEpjB2drqOjtotxiu-GNkOfRhZdwBK-q99mma5wtf66jzijH2NiZNdRHE_XEzFmZe2tZVlCIZCrJtH56L9AfySULKeOMwcbiLIc8yAIJQ2ub53icEuDwJy3VOi8SZ0wjwN3N6uW6nQM2BE6s9-f2yYZOF8EmGsYB4JFH__9EV8brJKJICCU-hULza2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=As2Ct0GXRmwr8SuUhF3PN8sfgYBPmOREXf2zGR1c-cXmi23ErBqF7JGYq-Y7cI44oNZhkM3lvVZ9CRhye9XikGrYRhTYlVGyaxvMJUCgey0u6BsFI0BZp8fk8-tGVc8U73jJRltoRkB8QHt5pzhum1wvL0BbEpjB2drqOjtotxiu-GNkOfRhZdwBK-q99mma5wtf66jzijH2NiZNdRHE_XEzFmZe2tZVlCIZCrJtH56L9AfySULKeOMwcbiLIc8yAIJQ2ub53icEuDwJy3VOi8SZ0wjwN3N6uW6nQM2BE6s9-f2yYZOF8EmGsYB4JFH__9EV8brJKJICCU-hULza2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=S6PHkSd11QbJxxq2U-fBMGJD5DOCVvywlF7I4BD3-RPUOTAA5tQCJiRQ8erMUnesVkL8oBnZbzBXuG4vLjf2-0OEm5_2KnbRbW5KPtkaREA7yZ3FYkqgxuuOwozo4HKr-fBunJVSbO1HlpBoXcyfF-aiMtsBxavv2OvKobtXtlmVGgZRKvgI8WvCAgpipGjGAT7OhBtLa2-SCfN-8KiM85aYrUVlQPkmYL-4aVvLe0manqMMfywfN5tLhWyNz37qkYhkdGmEjZqL_vRDGG_DQTftguXKVjUhk_-tH-Ka-43vKojBcLTAfinBcLEsXcRS1cvOJZoGg1Cx3gi1V2qHPL1jSqxEZJY2DPPHPDXdCjI8J1MAArHAWVumPo_GWTz3Cw6XuraAzBxvDDHGwqrmPS-QJOvec1Cenu3j3RLcA8-ziqgkifxWVTnej5luh0AsF1rG1ifM6dh6-8VtE7aaWxSt0dwxt3J_MnmV-A4dRN6C_uj2nzXHW4g3peCjEw6EtCPegpHJtbshatMQOWU9WzLCDI7hQiD1JeC8_7GrI4kPncsCtyZpRevIJ34MYaHAK0evEhCsZTysRQmwjMmi5eRZkpd8DQDidQDio_6EU-3jbkbJpYoc8mlT71mvPN9gunD4nfuEKghxQdzNOQcGf2VcCiRtTpd_ckqmQO3E6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=S6PHkSd11QbJxxq2U-fBMGJD5DOCVvywlF7I4BD3-RPUOTAA5tQCJiRQ8erMUnesVkL8oBnZbzBXuG4vLjf2-0OEm5_2KnbRbW5KPtkaREA7yZ3FYkqgxuuOwozo4HKr-fBunJVSbO1HlpBoXcyfF-aiMtsBxavv2OvKobtXtlmVGgZRKvgI8WvCAgpipGjGAT7OhBtLa2-SCfN-8KiM85aYrUVlQPkmYL-4aVvLe0manqMMfywfN5tLhWyNz37qkYhkdGmEjZqL_vRDGG_DQTftguXKVjUhk_-tH-Ka-43vKojBcLTAfinBcLEsXcRS1cvOJZoGg1Cx3gi1V2qHPL1jSqxEZJY2DPPHPDXdCjI8J1MAArHAWVumPo_GWTz3Cw6XuraAzBxvDDHGwqrmPS-QJOvec1Cenu3j3RLcA8-ziqgkifxWVTnej5luh0AsF1rG1ifM6dh6-8VtE7aaWxSt0dwxt3J_MnmV-A4dRN6C_uj2nzXHW4g3peCjEw6EtCPegpHJtbshatMQOWU9WzLCDI7hQiD1JeC8_7GrI4kPncsCtyZpRevIJ34MYaHAK0evEhCsZTysRQmwjMmi5eRZkpd8DQDidQDio_6EU-3jbkbJpYoc8mlT71mvPN9gunD4nfuEKghxQdzNOQcGf2VcCiRtTpd_ckqmQO3E6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=nlrd8M3_8E1Cdpf9XCPgztAJjIth2Y7uRksSehLNlXkxfxsGlES1HI9bfU45OpJIyy-TC8Kk813-v1znNtw5GHNm4DW9VjCwCD0yQ4SwQVTTSsdelyn8c8_OiSjV_N4YykMempbF6YMtcR9znWL4e-Qu6mmrgFgMJPIz0PNlWeRAaDaid3FUiVMyhaTSXQnqGnWW8YhOe3DF8LA-1NgnDzWtFJNClm1cvgac5iMAYto0ULeBb992E69KZ_IIRWpfwU82D_-v8PWjEpoS6L3-bXPh75HDMFBvqls7LkhDIi9A1Gt9761bgokXp314PCbkNeZTOYZ3oph3r4mG2OMJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=nlrd8M3_8E1Cdpf9XCPgztAJjIth2Y7uRksSehLNlXkxfxsGlES1HI9bfU45OpJIyy-TC8Kk813-v1znNtw5GHNm4DW9VjCwCD0yQ4SwQVTTSsdelyn8c8_OiSjV_N4YykMempbF6YMtcR9znWL4e-Qu6mmrgFgMJPIz0PNlWeRAaDaid3FUiVMyhaTSXQnqGnWW8YhOe3DF8LA-1NgnDzWtFJNClm1cvgac5iMAYto0ULeBb992E69KZ_IIRWpfwU82D_-v8PWjEpoS6L3-bXPh75HDMFBvqls7LkhDIi9A1Gt9761bgokXp314PCbkNeZTOYZ3oph3r4mG2OMJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=I9OmpUHBZOtxLAA0gkNk_tyWKxXdrf-dZBc2DeOUIVQcMlv2NuSx-6rk1TktX1pYRvfo_GWXic-M6TlDBc4p013zP3db-sBakjKHrjvS9cBXhB18B3I6WlOfpoHbg6ffqmreWz2iMvBSFBArrjxwI9S0cNNHwT-Gk8sJJpOk0m_nBY-G2tNf9l2gIHadx2-HlMlLUrgt-Q7mEvLijd9se2q-a6yxjeTrX9ludQL6mhZDcBlkUv6WlvMehYsDXkmStvbR747Otmpr2kLWDkHv0gbL4LliEPT1XpH4WxLK5Snebe5QRRcQTZ4TQvJdsBOsUySjRd7ZOJ6h8_9OWICWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=I9OmpUHBZOtxLAA0gkNk_tyWKxXdrf-dZBc2DeOUIVQcMlv2NuSx-6rk1TktX1pYRvfo_GWXic-M6TlDBc4p013zP3db-sBakjKHrjvS9cBXhB18B3I6WlOfpoHbg6ffqmreWz2iMvBSFBArrjxwI9S0cNNHwT-Gk8sJJpOk0m_nBY-G2tNf9l2gIHadx2-HlMlLUrgt-Q7mEvLijd9se2q-a6yxjeTrX9ludQL6mhZDcBlkUv6WlvMehYsDXkmStvbR747Otmpr2kLWDkHv0gbL4LliEPT1XpH4WxLK5Snebe5QRRcQTZ4TQvJdsBOsUySjRd7ZOJ6h8_9OWICWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxDyhn1qc91Rhj5kueaQ8CwbrIS8S332m7ZaPVLBjOixGy3S-TbOAyG1kPBRXlP8FS6KbOOJlrGT-CozXReFJs_QVxceO_ECgioAxU3OanWvhYfIfLkUXNQyckh2SJWUDJuPtfBmsNdsrJr6k_iq0cr6IYybZtNk_6HoCd9uSpNiX7zV4BLp6HapyGUIGhpH6vUUoydfHKody6KJIMemYDetRK2fpqk5U6AYK-_A8Eq2wRfyG1nCsPUYVDsQX-T1EF-XmEKuqja8ZnHHfIQJ4TIYDWo1CVslGtYdYYSLPqBVomi3FNURoReI9UwUKZeoZ4AT9jxkcjkuwhfNpjbBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opRcMc84YO0AG9rTE9ZvDu6bIhHVvkKzUvnXycJEf1-kfSk1tM2hue30tG1KeMtbv68UXrp8aCH7D7irU-sWTlw3qBf6-89V2h8fAECW5-GLG5bfmbRRv-cMRATtG1xa4yLLnBWCiM62Fno-YMeTcH8LWehCBDJJR3apMwNdO_ajZ-yRZyKTXX9pnah82oupoWrwyU9RQAAMpwxJy6jeXVCUEgVs25piCPjKdvigSFm0EgveL4kFBKN_FBC6tXGmPM6yCxBvRUQsAhMTG9cr9QOlpCPxyrlaFV1SBxR48fLaICjkkOcKcjsKL-8gdKn9GhIXUvJauPKl_bDLovioXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=gln1lR40VoPTOJPclznbfwXbHRB6fnzWMAOKAf-EkMJOGLP21TyDf-oaP-xwLhezJlxn8XvnnSDOohLfTgKPzYvmEmDA3UQtS6lW6yayYNrvNaDUeoZdbT1ClDjFt-i8q0_AecOYkA1CETgb0jJNQsP7y2vtJpN3LDnJc8er3AnWDpc6V_cLB3Yl0PAbpjRmiKuIdkJjpBWgBIEGyP1yLk2PrYoqx-YhrZJJucagurQ-Z7PtjF6OMhuceARuNE0ktNChBDiLjqjad8lvfEMXDoj4hAwSnOpy_s63rmuOjRK-qtkwoByzTYIwy0Q2rNwz9bnA-hYhA2RTC5hUPRswwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=gln1lR40VoPTOJPclznbfwXbHRB6fnzWMAOKAf-EkMJOGLP21TyDf-oaP-xwLhezJlxn8XvnnSDOohLfTgKPzYvmEmDA3UQtS6lW6yayYNrvNaDUeoZdbT1ClDjFt-i8q0_AecOYkA1CETgb0jJNQsP7y2vtJpN3LDnJc8er3AnWDpc6V_cLB3Yl0PAbpjRmiKuIdkJjpBWgBIEGyP1yLk2PrYoqx-YhrZJJucagurQ-Z7PtjF6OMhuceARuNE0ktNChBDiLjqjad8lvfEMXDoj4hAwSnOpy_s63rmuOjRK-qtkwoByzTYIwy0Q2rNwz9bnA-hYhA2RTC5hUPRswwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjAw-soE5Dkyq3gbcCtO-M7Yluj2sGOTeYbIx9hzcEJfhfmfeKRfAB6qYfCzkk7q6AAybJuGWbRUEIo24yCRzzA3KzBGOgD3JNtOFPukGYXthm473KrISf4HXtjchlol5I7QIMclNHyp2Qap7Gj4YMpssjRY3E-GRSuBHBlxphUpS8hqTabuQwiaLQIT7AZCf66eNx6NTwA5tnfW3N-szvWPwonFr7lD9uCmC9ZPVIDm3ayTkvQ-o0H2WRwivCha2vp_XJfIiCWA8nL7yPre3BbZtH4TJ4jdVUCOoDMHD5VO2m6n48mjUTRik8zrOVQTSv8bDvTT2i6fRrTAGbu97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vm6hgn5FdDBrE5Dcj02KvBVfJD1lx5em79zdER2AekBYpT6j6uBYWzEuoUbdPotgbKnTFM4rEQ9dN1eL26H61irHddnY4Jk8Mj1M9pKus40ikj4ugiqZqhKsopD78HGhRH7Ih0GQS6kuy_D48Qhw2pXP3NXZysaPB5m-Ma71ipE5nuKoFBYsHEYcI0dJKs6OCnr46mmpRuJuIcVG0wTGzImUlbpOEJcwVondoegkqFIb-IgvyR2VT3S7yatmEY_4LoAZNTefqIbYGMufjXkDubrzmgCGkvk6aMzl_SbH77361_kpLtO90okiVRiy_8MCWgWNBG6b25JcHTnvwMZO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HknGfYUSAWvoSATw7vWdWO2p_2dGyJWGpjC7DHA_V13z8IF0h855QWaitIoGu8a3g_HCeCNaOuEZWarLV4VfpoPWYz4tHrlakrTMB__SXk5pGLySg71U63qNOH56QY9gj2yYXSWlsmGqFc_16H0eYHrnKZldM75PBRlWX7cKHWibYzchiBm-SMYP-Ewmr30kZZFfhO68JA6ItWIQBiG5DALDaXlTF9urc66xhGCMIkgDHn4ld1_PnnQYstK2mNkrkY9i8AQ5ZtCJPHM9xHbv8LXAKNhPv1_Me6Qr5TvSdHyGExOm7_FgOQAc0a3qaCvdc1tHtLk6OQGc3MSsChrgvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCM54wh3YzMRXFCe_hBBkoC3YW0ZXbMkRhjZgXBCfanp9ICpBQoM00-eWAa7doqkp6dGsu47rYFeq9t3poG1wIt3zii1VWCtOm1DvFrie_118npb7Us7qbFeNNKOHIFdotj7AbqPM816mvsD_-eyOy1YZQwOWUcskGJskZVNwP6hSgA6jeTK_rjj0klEg_BZVysKO179bf1o4UixgoCHslVtpBQMa3nGBSAbnZXgaE45oBNDG-1Cnd5C6fG0vy_auKPkqdTF-0i-ET7ie86_Ag6PMDJyR6xye0XJVYpm2DD8E5zWUkb3bN-XUxtiJcq-piCCR6BfhVzDvqmiEqRmVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Y2sd7ohgmJZmW3RRKyElu43MWqaMDvsCfs6yk1FgRoGSnCGr8ncNIM8pI3RrjdD4gJWnSPxHkBdyfahQ8Q55jROE-bI8ynSIcKcUuzVq9gzyQGe8h2WE90SjrJGzdB6IKaAng_4Lcfv38iKzZ-8gdjyvHg97Vy68P1tGyx2i2T8Hcp1DGgFAASVjzulMCdTym_YSwgx93lj_G5dSVOBx7mPrwr-AnGe2jSRdZZiEbZcKbc8QwVhSjL8J497lmzrKDO-P08mlbIfG7BT6yakDwMoPimQ1VDq7qs3qW8dlKYuLmH8RNYWssgOKmxd_HLtwmSJXDcGCwqWntrNgll4F3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Y2sd7ohgmJZmW3RRKyElu43MWqaMDvsCfs6yk1FgRoGSnCGr8ncNIM8pI3RrjdD4gJWnSPxHkBdyfahQ8Q55jROE-bI8ynSIcKcUuzVq9gzyQGe8h2WE90SjrJGzdB6IKaAng_4Lcfv38iKzZ-8gdjyvHg97Vy68P1tGyx2i2T8Hcp1DGgFAASVjzulMCdTym_YSwgx93lj_G5dSVOBx7mPrwr-AnGe2jSRdZZiEbZcKbc8QwVhSjL8J497lmzrKDO-P08mlbIfG7BT6yakDwMoPimQ1VDq7qs3qW8dlKYuLmH8RNYWssgOKmxd_HLtwmSJXDcGCwqWntrNgll4F3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=PfqSjH9opoTXXuL1rm89qNElFQu7rUcCmROJ-GhD_v-zqMfwuLlma6o920wqETsOPZ4DItbF51X253ap3hPEZ7tP5Rr5JVmC09TwvQCrKrCEEJJhYnBRKdXKpfIFer2pGcfr7j4uDsSbjQ5naICVgIOIfIG6e3FrsMAds2VxZ6YbCGEo_zR6J7zCeHUmN6jbSsBMOoJvze2F3jIB23NptTIm3PBv2pC6dWolbcdySNs7_JoiN7WMJX9AlKfpid1ZryIQg--UeiLn2ho_GQFGmZcLcXxGQLXcykM2MesblOvGUR6fPX9J9V7XmSAfSODux--ALsiN1CGdvQzZKtiTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=PfqSjH9opoTXXuL1rm89qNElFQu7rUcCmROJ-GhD_v-zqMfwuLlma6o920wqETsOPZ4DItbF51X253ap3hPEZ7tP5Rr5JVmC09TwvQCrKrCEEJJhYnBRKdXKpfIFer2pGcfr7j4uDsSbjQ5naICVgIOIfIG6e3FrsMAds2VxZ6YbCGEo_zR6J7zCeHUmN6jbSsBMOoJvze2F3jIB23NptTIm3PBv2pC6dWolbcdySNs7_JoiN7WMJX9AlKfpid1ZryIQg--UeiLn2ho_GQFGmZcLcXxGQLXcykM2MesblOvGUR6fPX9J9V7XmSAfSODux--ALsiN1CGdvQzZKtiTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjpy_6sDaEdZ2YxDOOHpRPLkluimnFvcAmno08dXC4zhQWXjIhtY4VbcAnetsZZskGWojid8b29WS8ONHQPoWBHtKVKJNgontxga90mKxr0_P8FFCBrc47sbgJKQ1sLPucRsnHikdsVBgmjcsSGdakvL35Y2HfEtwIrDFIasMzp8dhd1-EXSCtJfKWxL5zyqDx3Zt-rnh_cH09bNYpHrz_DWF14g0FEccS1OkySrWqgsk9IjtLWFZ4Huk9ClTQ1EVRhjmuT6mUnCY9tlDkDL5vRV2Emstz-SNH6Pt6rMZ_3SlMc4grRMr4cCUbqYOA1dNgf5-KlGfnf8aA5Pf-G7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ZNm3Uam7a27n5tpEr8Dz0JeuXyYjnqobYJXAR2ylhOX8vnfuk50ji3O3ejsNLbXLTyJKFR-jKcg6bfg58yzyPo7kazEGJU6H7krLH1vb896r5a3QxtHyQNLs_Gfv_bAHqwngWgxxvZA2qpZwa5mBQV7V0bmvUY0k6CG0guyU-3Il66MXZcbYBxbCnlG-jDi7G01_ntj0VBTJmZt-Y-xAPLvK8fN-kErOMCUhb75cbYEnAl6-XOGeticNfPS_OkA7ssQANOyZVxtyJB-ugjSx1I_p7oTgHaRjbEnbVR0XZKJyeXpDItwvoqmeVygyYFnCUPk8gw91yCJ5pGxFXGEfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ZNm3Uam7a27n5tpEr8Dz0JeuXyYjnqobYJXAR2ylhOX8vnfuk50ji3O3ejsNLbXLTyJKFR-jKcg6bfg58yzyPo7kazEGJU6H7krLH1vb896r5a3QxtHyQNLs_Gfv_bAHqwngWgxxvZA2qpZwa5mBQV7V0bmvUY0k6CG0guyU-3Il66MXZcbYBxbCnlG-jDi7G01_ntj0VBTJmZt-Y-xAPLvK8fN-kErOMCUhb75cbYEnAl6-XOGeticNfPS_OkA7ssQANOyZVxtyJB-ugjSx1I_p7oTgHaRjbEnbVR0XZKJyeXpDItwvoqmeVygyYFnCUPk8gw91yCJ5pGxFXGEfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=RAHvA6BRnWKZWSwzJYgQT5dF2tnQhCohJ8TP8603otWlE6c1DeFmPZzaW-e6-9QCB9jXaHUdRjfdVhKPjhETkT7wntj1uqig07A_WBRsJM8A1F5vrosz-3zzasf0vaQqMrNnDjPzk1yKe2zncr9EeJoEjXQLJ-UkePwyELmcCTHvLE9Bhhgiuoy8TNK9FJhkMQV1vM-Xg-VeUAoU5axJRTcYuRIDBRbwKu5QqCvRioUIxhM4WHxkhvanAem5REgtZ8k3dK7r56QOzXO7gJXjrch3SECVpM3GMgCldGu8wp2oqqrD62-QOpQlT-YS1z5I_clrc4H1j-WCJJchoY-vXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=RAHvA6BRnWKZWSwzJYgQT5dF2tnQhCohJ8TP8603otWlE6c1DeFmPZzaW-e6-9QCB9jXaHUdRjfdVhKPjhETkT7wntj1uqig07A_WBRsJM8A1F5vrosz-3zzasf0vaQqMrNnDjPzk1yKe2zncr9EeJoEjXQLJ-UkePwyELmcCTHvLE9Bhhgiuoy8TNK9FJhkMQV1vM-Xg-VeUAoU5axJRTcYuRIDBRbwKu5QqCvRioUIxhM4WHxkhvanAem5REgtZ8k3dK7r56QOzXO7gJXjrch3SECVpM3GMgCldGu8wp2oqqrD62-QOpQlT-YS1z5I_clrc4H1j-WCJJchoY-vXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=lijWgL0PxLL62LZ9MxAJTTvVkjB9NNeZM4uq0EEZCmUhHlph6XBkdHJBaw7NJnckeKxGrspKiPgjTbnW6yu43OS57bvBExNGInfAwMI9pExA7avZ9w77YB25B9fNZAZu4vcx9Tu4LPM5tz6h8OQLJHPz45jIFwU8DccmFb1wf_I8vu8embegjd9VcsfruGhabSrM1TmERefwz9iKW_4iHnrbQLnfFB9_ZZEoYDUDC09IjFLStPUYYkQz257NQV1W0MAd7chgV78q4VRrIqiVXPVDapTKkZNA16PMx0ZYZa-JczX1Oz4xfuDS-miItAUJb_yujXoJiXwZ02l_uULn2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=lijWgL0PxLL62LZ9MxAJTTvVkjB9NNeZM4uq0EEZCmUhHlph6XBkdHJBaw7NJnckeKxGrspKiPgjTbnW6yu43OS57bvBExNGInfAwMI9pExA7avZ9w77YB25B9fNZAZu4vcx9Tu4LPM5tz6h8OQLJHPz45jIFwU8DccmFb1wf_I8vu8embegjd9VcsfruGhabSrM1TmERefwz9iKW_4iHnrbQLnfFB9_ZZEoYDUDC09IjFLStPUYYkQz257NQV1W0MAd7chgV78q4VRrIqiVXPVDapTKkZNA16PMx0ZYZa-JczX1Oz4xfuDS-miItAUJb_yujXoJiXwZ02l_uULn2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=UuFtl2qdZ9kZHD5ABtWtrb_EZUs7klBTur00ZQyhk50KHBgFUFAR-Q578-R8b5iNRMQTNOPv9yr3Urj0tJMacdFND1MtWF_FpYJ7qHh0bm1UI_b98M3LBDVbYk1uD43iJjr-tIDjvc9MavkaQTOdHcJqj6nNxD0Fhgcd8oBMaQWIf8J3FG7hwgAR6lz9qbynh20Yvt-EaSMZkfrpzUm8E5XjVmsdLomUbi1ddfnMOWBkfICK4dZyF72LS7NwD1OGsKm3fzAEhvQUGxOdNDM4Xuvx15NXLLj3LHoJO3jJFOkmGSwHVIKi8q3M00z-Oo_hScKh1McIIQuGIat2wYd9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=UuFtl2qdZ9kZHD5ABtWtrb_EZUs7klBTur00ZQyhk50KHBgFUFAR-Q578-R8b5iNRMQTNOPv9yr3Urj0tJMacdFND1MtWF_FpYJ7qHh0bm1UI_b98M3LBDVbYk1uD43iJjr-tIDjvc9MavkaQTOdHcJqj6nNxD0Fhgcd8oBMaQWIf8J3FG7hwgAR6lz9qbynh20Yvt-EaSMZkfrpzUm8E5XjVmsdLomUbi1ddfnMOWBkfICK4dZyF72LS7NwD1OGsKm3fzAEhvQUGxOdNDM4Xuvx15NXLLj3LHoJO3jJFOkmGSwHVIKi8q3M00z-Oo_hScKh1McIIQuGIat2wYd9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWOJ4c7V7uXXVwslnrr2mvgd5IeNGzbGbjsi4q9Zkpb3OuERlzOJtXSaV-mD1UOFGWi5UVGNvYvtFZW89DKrouz3YQzHqt4QNC6CMdD2wiEgB4oWpkCpzk4qLiy5b8sFwmg6XeeFxVPw1odoxKKzxPXaz9dkL1_BfnQ9OS6wHP1RKYAJ9HLF25KGHOYZv1Y31ypr6P2jMqeUI3n4NDIMmQOe0qt7ZB6VAOwt3RbOh2jDbFIIoq93SHf5ux_Nr_YXcDxTmgcarAxYDa8adnfIViJHWdIGr3l4IN9qOYOXQ9uRYygUTtwm6dCM219upB5OyXPXxNcgPVeXsUNnEKk45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXsbrWl_-ypmwZgwbH7FwRC-h_pWp81QdOrDV_U-hhAWH4BBOLZxm-fPutaPGIkrVZDblpOoV4GGesDM1QhL3vbtXhMqEcgLSJDq2DIvhmgxFSJUK6JfAQNer4bB5S6PdfMZ5Aojzi7xeOVne4Qu4ELIfzvDCTeoG3MvzgjNU2ikyLI0tApv747nivMLGOE-QKONGbjQyniI_nbY8YXDuZxhVQH2CNUeVplPNnpHztEwcTNMQDKD_LMPWuRyDXv4mj9qIA4qOE0B3K9tpDn1X5kAex4M-JE-tvp1NZeTlo8BI5EJ3cAt711ddMuxyiccxwPmp6aYD7KNEjwWqXkvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bBxlC5K9Vv41Ll4nMBHHhhAhAsmD6gt6xMJ3cdnqFSXBhEzj7wDS13bXLjj2UkNsM-xoqyCxnIDIgTAIXfgR3XNaBbqEvzsIa9Gltk0uQ_w6x4Jdmofbtm3_3z40Z9AtH75D5eRkzdsqR4arTYeBkY-BJlyCvnRsaKDfXF5NzWi8cQOoUcRagfcCiq0RQmJjYvTwun8J-MqBP8xw3P7LN4HFOT39-dh9MJOSMtVp0Cm2onR0wn_sfgk_E28hMEs2ssPJi7fYu1ZTBYolajougOXyOydmyy_l90SWxLiX5g0tGyJoDj5n6O1BYazEuTPN4LaIq_PTNiz74abSd9Q3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bBxlC5K9Vv41Ll4nMBHHhhAhAsmD6gt6xMJ3cdnqFSXBhEzj7wDS13bXLjj2UkNsM-xoqyCxnIDIgTAIXfgR3XNaBbqEvzsIa9Gltk0uQ_w6x4Jdmofbtm3_3z40Z9AtH75D5eRkzdsqR4arTYeBkY-BJlyCvnRsaKDfXF5NzWi8cQOoUcRagfcCiq0RQmJjYvTwun8J-MqBP8xw3P7LN4HFOT39-dh9MJOSMtVp0Cm2onR0wn_sfgk_E28hMEs2ssPJi7fYu1ZTBYolajougOXyOydmyy_l90SWxLiX5g0tGyJoDj5n6O1BYazEuTPN4LaIq_PTNiz74abSd9Q3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mBxrpguti9IoTv73HBK30PALUPGHcx-w4XxRH29LdfTnn5MwGtOMDxpFubZVlv4K8lTBYZBTHfZPCQoOHXfHg2_beWpSCMBdMSoERnE-Ynk9CmknO97SKkXfGqxUTczM0g1ZHWoRYCiltEiHpkQ8RGciIVp6HkqLaPmcsQEcH3ANt8oQ2rYdCjR4PuN46iHxGX5mk4dgd78NrxsKI6nKTH9GhmGKqtId3KT0a12cN0Ged_A-gFFzywajkG7ZQYdtIr-87o4IU0VfW2pZLFWkY2LXWHNsVuvX2KdDTTSAQh3qWYtbTOCuTN1ZvQiKxGLZ8Nfy6brURzyuHpPGb0maf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mBxrpguti9IoTv73HBK30PALUPGHcx-w4XxRH29LdfTnn5MwGtOMDxpFubZVlv4K8lTBYZBTHfZPCQoOHXfHg2_beWpSCMBdMSoERnE-Ynk9CmknO97SKkXfGqxUTczM0g1ZHWoRYCiltEiHpkQ8RGciIVp6HkqLaPmcsQEcH3ANt8oQ2rYdCjR4PuN46iHxGX5mk4dgd78NrxsKI6nKTH9GhmGKqtId3KT0a12cN0Ged_A-gFFzywajkG7ZQYdtIr-87o4IU0VfW2pZLFWkY2LXWHNsVuvX2KdDTTSAQh3qWYtbTOCuTN1ZvQiKxGLZ8Nfy6brURzyuHpPGb0maf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=QHNdzxwAMg2EDHoUxpdcGgw0golctWb6wfiH_5zKY83_nd4QMcXvQJn_9PTmQCdXepGmR16T98CYiF3VD8egMMt-zwqIZpYhcwZJWRGFOqRv1ZWeUZ6f2J0_fEuk4mPEvyWPwdiCNziTVoOk1Thri-lib3nWO5fPn8OFb8KIbtAZkdkqd7bpT91O5yDDOYcgwHAP6iltsfdjCGc5NXdk5Y-fIW0ox3Nk5vH-X-fqwT31wtEleQDYK5xbDxcQo2FxHFgXTMQytUGLFUFzjQpSZUp9tywVfkgRYVbECGmvczZ1jX6qu2MKhuisrEj4iNKSPZv8ahop7NJIuZPFGm5prQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=QHNdzxwAMg2EDHoUxpdcGgw0golctWb6wfiH_5zKY83_nd4QMcXvQJn_9PTmQCdXepGmR16T98CYiF3VD8egMMt-zwqIZpYhcwZJWRGFOqRv1ZWeUZ6f2J0_fEuk4mPEvyWPwdiCNziTVoOk1Thri-lib3nWO5fPn8OFb8KIbtAZkdkqd7bpT91O5yDDOYcgwHAP6iltsfdjCGc5NXdk5Y-fIW0ox3Nk5vH-X-fqwT31wtEleQDYK5xbDxcQo2FxHFgXTMQytUGLFUFzjQpSZUp9tywVfkgRYVbECGmvczZ1jX6qu2MKhuisrEj4iNKSPZv8ahop7NJIuZPFGm5prQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqlEI-edDTZ31wBrVN3dC-20p87qjQB-gTOIi8n0p7j7NTt9SViGvr_q10XYcRsAyCb1iWBF7qeM78Lo5XFr5DHXUYP0NAsZAF9PH4m85AT_a0v_CBaRvIxeM90595a8cHnnwlK43Ad0xY14uuucxhyXhoQQ3_oemUak0VWBWn64eCfq0A72PJb7tOpoI5c9ffzcA-sIbeeSjysXmXbpqxY3zCnntEJu50eQKWdg0h9WCJBsFRjn7uM5RAZayRDOjgL3jDeT3MzWz6pBSeH7bRTgv67YV5BNj-B8YM_9nZY7pBOAqCdZvlkoLL2hI6AnpPczZ_ziZHoMN9EqfffW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ADvRM3ONMZyMOx1Nc3SXvpHTYd97obxXx9NS6wEVdlfa3EfhPXrJzAYpkKZA_VzAt46zEgaAMM09y6lNstEvH5opkSS9SBQOY_IAV85fJWJzwlNvE6xC7Z6s4YMOHQwIm84wxMxHngaZWRZ8Z2rPnCKqTOpsCJqprV97WM__-gJPPWi3EghH17eLXBUmJarVaPZ0-eQdhET9whKcxyjd7B7tXX6n-vWj8KIjD7SjBANLVZzjBuCueymgNG85DreJUSCTFtbhXrV8vigbMcM04vheBy5No9Qm_Jq-rKPLYq88X-dIWH6kWqhR22gyUelJ3fi8K0FEyaUwkS7p9M7f_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ADvRM3ONMZyMOx1Nc3SXvpHTYd97obxXx9NS6wEVdlfa3EfhPXrJzAYpkKZA_VzAt46zEgaAMM09y6lNstEvH5opkSS9SBQOY_IAV85fJWJzwlNvE6xC7Z6s4YMOHQwIm84wxMxHngaZWRZ8Z2rPnCKqTOpsCJqprV97WM__-gJPPWi3EghH17eLXBUmJarVaPZ0-eQdhET9whKcxyjd7B7tXX6n-vWj8KIjD7SjBANLVZzjBuCueymgNG85DreJUSCTFtbhXrV8vigbMcM04vheBy5No9Qm_Jq-rKPLYq88X-dIWH6kWqhR22gyUelJ3fi8K0FEyaUwkS7p9M7f_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Il99g6NWSTjZ55Qqk8kl3TcJLCRYxQTi0ZLa3G05ggGQQcDRaopZAKJUxFmN5x_UOu7NyUnbr2ShnoPQSwjJJnJd5H0smO1Q5KWGmDSGY8-biQfHM7CihOvi2-oGohTgY-qbWy82f6xMOimo5HyOruzzLmCPqZeYMT1FcixzorlbYOMgwZtr-UsFgG2JKTM8p5h0PFPIjoRquST-HMbjaH6Fc2nx5zcc7mTUYT-5HegMh_W6ZJJ_Z_nn98kN2jrwU75Vb1gcLaAxBNfgWyeZRjQ8p9woEKiaAbLV-7KPS6OGfOvuhaFO8uOc97WchrRdrMESj7TcUDNsRdBXbq_wmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Il99g6NWSTjZ55Qqk8kl3TcJLCRYxQTi0ZLa3G05ggGQQcDRaopZAKJUxFmN5x_UOu7NyUnbr2ShnoPQSwjJJnJd5H0smO1Q5KWGmDSGY8-biQfHM7CihOvi2-oGohTgY-qbWy82f6xMOimo5HyOruzzLmCPqZeYMT1FcixzorlbYOMgwZtr-UsFgG2JKTM8p5h0PFPIjoRquST-HMbjaH6Fc2nx5zcc7mTUYT-5HegMh_W6ZJJ_Z_nn98kN2jrwU75Vb1gcLaAxBNfgWyeZRjQ8p9woEKiaAbLV-7KPS6OGfOvuhaFO8uOc97WchrRdrMESj7TcUDNsRdBXbq_wmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KObaspg07NJIaZdcukFUv9RcfZb2cupCj1sXT_wknQtVp7myhv0r4iEf-hiVUxSATq_jUYmEOUc2G1gvA1sB2LV8TzBA1vqquizXUxzKZxY2YuXygCNxUFcB4U5hBHIbHb9dtW00W86KRSc6ngKJu7xzLKaXKvuJI5buFI8JXPvQuLfsOowyRbw5RJfox3xRqc4UPA8XdywEd5noRkHo9NuQJ7AFJ_EagHeNP65u49IbxN2hlApGOcoADoDM_V5EdkjDzOjg_DGz-S-950NXXUfXBwbzcJNg_1sEd2_C3-0M9mGQBZUwV5ryq0Bk8JTbI5GQM-H8OEFXjVFhVM9kKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KObaspg07NJIaZdcukFUv9RcfZb2cupCj1sXT_wknQtVp7myhv0r4iEf-hiVUxSATq_jUYmEOUc2G1gvA1sB2LV8TzBA1vqquizXUxzKZxY2YuXygCNxUFcB4U5hBHIbHb9dtW00W86KRSc6ngKJu7xzLKaXKvuJI5buFI8JXPvQuLfsOowyRbw5RJfox3xRqc4UPA8XdywEd5noRkHo9NuQJ7AFJ_EagHeNP65u49IbxN2hlApGOcoADoDM_V5EdkjDzOjg_DGz-S-950NXXUfXBwbzcJNg_1sEd2_C3-0M9mGQBZUwV5ryq0Bk8JTbI5GQM-H8OEFXjVFhVM9kKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=RiNpUjvAKaqQ210wy_5mtU5wunXmYsywmRzq3mdIBLoiisaJPMdtaRWAPrIIrrD8KIs6GVPiHQT9827UDdolQeziZ9mtD8ktwEq0q8J1SpFXpAxy9I27mEVNakffBYwkxzdofHliR5KRmIg70jZ8siaZkVZNIG0dKiT6bpDpAfewTO9svaiHERUGU8bidiGcNaGqQlVLZvpfyDtLX9eD3Ewh-mGbftVF5eQuX1bMgSACji0ppZ6lUQbF8eXYkQKEsYLDMhJ_ElOnEJnLcyx-lJqpnUa_Xf8jNA4GZbGw6sfhRgPmlSJjLNIExupkk9Cb74S9EmvzotEXEBwrpaXLGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=RiNpUjvAKaqQ210wy_5mtU5wunXmYsywmRzq3mdIBLoiisaJPMdtaRWAPrIIrrD8KIs6GVPiHQT9827UDdolQeziZ9mtD8ktwEq0q8J1SpFXpAxy9I27mEVNakffBYwkxzdofHliR5KRmIg70jZ8siaZkVZNIG0dKiT6bpDpAfewTO9svaiHERUGU8bidiGcNaGqQlVLZvpfyDtLX9eD3Ewh-mGbftVF5eQuX1bMgSACji0ppZ6lUQbF8eXYkQKEsYLDMhJ_ElOnEJnLcyx-lJqpnUa_Xf8jNA4GZbGw6sfhRgPmlSJjLNIExupkk9Cb74S9EmvzotEXEBwrpaXLGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6jESdKwVbBWuvjSBrd3VlqitLkO4GPjX5MGi2gsEuJE-lsmP-LSJbduozC60tnjslkQtBTHjdZPEX4L4-IE8BEsYtv34j6EhVihgotkaexvRiOXNE0DeAGHZT73wPaQaGPNb-DqpjdCZR48a-IjnE9cNj_9qU8oGjxlyQ3rttcUFq7h55hg69WEQfy7MlvhFJwOLNdkUEQswPEu-hby4s0pcZlfGqTfgS4lBwIfhDF3VUHxKTHt_WLPjgFDf4WnoPupI457eL785Cwr5cfI-iQyNzsYabvE2qAjbZBpl2Cdg7Vm1kfJR48pjqCcegiEx7ePGH-PX81eT9rLZD1djg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=Sjkpoc9_f92KD1ziMaCliNr_kOkfRiOZirbFAkms1omt9BCZUO8A9KTEgz58V0ugQzbpvPwUz2Mha43l4u1aMgSTwwjFNsoemYBwwaiLX_eD-kFvQLAsQUpI7ma3BWUhSj3D-bS7RDwNQyci6RpZT6lyZVcII2o2jZAo8cNnRbDHLZl-rS9XabA0YoY5GCkdVDEMOB7vhUzXZRqeHXJypx2iao0hGtwFWJ8tvM_1yYTC9vRWwTlXD7yB6DrxTRyi06c6jiocSFXWYt0weMC9I1NRNyvrY1KbYzBQ19U7gUrPXFnVycVwCJ5W64XSjxNSBGmfj61ln-aGRr4R-wWqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=Sjkpoc9_f92KD1ziMaCliNr_kOkfRiOZirbFAkms1omt9BCZUO8A9KTEgz58V0ugQzbpvPwUz2Mha43l4u1aMgSTwwjFNsoemYBwwaiLX_eD-kFvQLAsQUpI7ma3BWUhSj3D-bS7RDwNQyci6RpZT6lyZVcII2o2jZAo8cNnRbDHLZl-rS9XabA0YoY5GCkdVDEMOB7vhUzXZRqeHXJypx2iao0hGtwFWJ8tvM_1yYTC9vRWwTlXD7yB6DrxTRyi06c6jiocSFXWYt0weMC9I1NRNyvrY1KbYzBQ19U7gUrPXFnVycVwCJ5W64XSjxNSBGmfj61ln-aGRr4R-wWqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=APbBqJTZ7n_enwZT8cLPf4cWOGT4Z9BHUfbVYeSXkvBkTrxnONjMUmekL0gDG7NsQQKci8jimgfqatBPJbY9Y3IUgIPksUpdW-ItRK3iyVgvvdQQIx-iGg-Mf8gdQMYbtXT23NuRSqx5T4wNgz6jHjAJmiH7kCtoojHEQAdRgBQTvo5WNwOT7BPtaYcW6WuvT2A9-DSWrUQE1_yXmjmhLbTqC9nuJACWOEiY5c4NpigUVIe2qjfXmWgIbFWe7h1v1yyvc91W7Qk3qbVzwyj38xH04KgGPebM_1MSnhCusrWNtfdgWQP1qyOhG8n7J9SkE6X-iu72r9wTsbAxFPcbBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=APbBqJTZ7n_enwZT8cLPf4cWOGT4Z9BHUfbVYeSXkvBkTrxnONjMUmekL0gDG7NsQQKci8jimgfqatBPJbY9Y3IUgIPksUpdW-ItRK3iyVgvvdQQIx-iGg-Mf8gdQMYbtXT23NuRSqx5T4wNgz6jHjAJmiH7kCtoojHEQAdRgBQTvo5WNwOT7BPtaYcW6WuvT2A9-DSWrUQE1_yXmjmhLbTqC9nuJACWOEiY5c4NpigUVIe2qjfXmWgIbFWe7h1v1yyvc91W7Qk3qbVzwyj38xH04KgGPebM_1MSnhCusrWNtfdgWQP1qyOhG8n7J9SkE6X-iu72r9wTsbAxFPcbBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIixMOizUfZEOVyv6LZ1fWEwRCAY3f2C87Bf2PQLePIqbezZRZ6lCj09isJw71sP-8htGvloNGtRURd5NScrl_ZFHBDgewX2s6rQEOlKCaJzb8Cs6VvZHcotF8pFTJiEaZzIi3UWMCCvqOm3q3pYFL8DReeIDlRZiC9aQT6M5joYRDL9QNNxzh27kyYmRYXMS7h-ZG2_Rbfc2uuZoBTNLTbgPLyGoYjVIt0lvqZ6J9z5gEoMQoT5jWfoRQeIDaiXaz2u_NywCctxGL8OTzuTykG_MRryVm06Roc4cdr6wLAQdvL-Kj_6iHQ62twsxmLX5T95yfUjSoWWrdIhQp6iEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=cQsUmeZL6jMF_0WekUN3C_defqB8eMfalYxcvOHYdozSls2I87bC0rPCgICD4sngrhEuMxX_L54lSGrooVz0MWqm598dFxwI1fffgbIj1PyK5IVG2kk63S4N-oZvtkUzzz8KQ2Ji7vC7GA9R9JNXEU0koWAQqMwNOJZNcwR_uPK8NmcBx0zi7_K_1f3bTFhOQspnnIVVofZsbxyfZaipf2KAo9pqX4NDwb_0GVCeVYrI5_0LXWlxCsl0_GeJLUBKG8i5-zUDAXQmahHPlkrCCK0jUI4ro1ZeJ6GnMvDBbgJr86YUADjaP8T7cYVdU7ljkjqdLJ2fX4WFzGjfirmTlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=cQsUmeZL6jMF_0WekUN3C_defqB8eMfalYxcvOHYdozSls2I87bC0rPCgICD4sngrhEuMxX_L54lSGrooVz0MWqm598dFxwI1fffgbIj1PyK5IVG2kk63S4N-oZvtkUzzz8KQ2Ji7vC7GA9R9JNXEU0koWAQqMwNOJZNcwR_uPK8NmcBx0zi7_K_1f3bTFhOQspnnIVVofZsbxyfZaipf2KAo9pqX4NDwb_0GVCeVYrI5_0LXWlxCsl0_GeJLUBKG8i5-zUDAXQmahHPlkrCCK0jUI4ro1ZeJ6GnMvDBbgJr86YUADjaP8T7cYVdU7ljkjqdLJ2fX4WFzGjfirmTlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=N9_QcBj92IUpnp6Ol4zQu3SIsKcSiYzD9VWaLmD-ngVOqpROXbW3GS-455LS_YBiDXvJjMzLh3GMyvIrPYwcLGDvNkOp65Ym4zK7zYMAVgDvsQNE4us8yGc9wJyg2r8LDe7IKBJ1FtD8oGqnSv4hlP2m_foJxFqM-7pZBEpopeEGjhxZ-IdHomG3y_xGObjpAKtZY4n1tgZgKRJOZbOcXI03uCwXbshD8WAVcP4r7Yy1T_raJgc3DrebAUJoixudlASwLkRzvyO91FUSMDqYoRnlLpvjDci0Nq1u4yV3M_8CYfZuFY39-RV4GZq1hdmRalG_mTUr39qdDXgR2uufXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=N9_QcBj92IUpnp6Ol4zQu3SIsKcSiYzD9VWaLmD-ngVOqpROXbW3GS-455LS_YBiDXvJjMzLh3GMyvIrPYwcLGDvNkOp65Ym4zK7zYMAVgDvsQNE4us8yGc9wJyg2r8LDe7IKBJ1FtD8oGqnSv4hlP2m_foJxFqM-7pZBEpopeEGjhxZ-IdHomG3y_xGObjpAKtZY4n1tgZgKRJOZbOcXI03uCwXbshD8WAVcP4r7Yy1T_raJgc3DrebAUJoixudlASwLkRzvyO91FUSMDqYoRnlLpvjDci0Nq1u4yV3M_8CYfZuFY39-RV4GZq1hdmRalG_mTUr39qdDXgR2uufXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbBMwElCEpptxPLEC7P99vz-nXKXOJRgH4rW5HMaANEslGEtePdNukq00MHImO7tlcfa1mxfuadbhrJZpgq3PWzDYvXutfphJVe_K0VaRmzXDQ-3NcDaW7222583NTaHwCbxogCeaiXEBuLuySCESvnagA8MvmAPLEgQExEsWobkqYP1IXnsLIYLS-AOm6lpJPGp5ChGdZM2OwRxEyY5wQWy8O1mXru-wGz-K9-he07C-_tz6BnKBtvdgTe3BpvHC8F1RVTrLVitBSQB_KQhYp2xZsPm-uU55kAbTOBWVfgxejM8BV2fwtWxdyOlEt7spYUsZY1urOmMf2wB_czQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmaiibtmVJ9lJ46vLsjhwKQ7YVhetfAUiwf1yDsXsOhK0STzga12G_d7a0eNQY2AAyTqwz2CNT7lrYnoGcKFzXWCh85ZEms4pdZy4SO39AXz7tUhEgr1Eddom1i_VH0jhzBVl8oqDR_vMyuRqhbJCqMnjpBNvHOeKkp3Bg1q-K0yYA1bBMUSKGkNbZO_DCCNh8ZOSUOfd4uW2H_k58Ml3wuE38tqI1GdB_9TDPkICr6NHGbUzjEYYvwZ0WqSU-_HbmJQxbRyYGiz_FTu0fgkZG9zUccVvnYyuJgf6lNRNNZkaB0V73V2jexgLeZSTfcwMvEx70HLhwijYXONBU7mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-_jtgQI0Cyyh9LxhNXMG6D1Aah2ClwUawlfgeD-sb8888yTor4J4QV2jQZf6lhEybq0gNreB0MqboIQlxjinf9IkNEz-0hllmR83s79w-esxanrIYWLxLxk9HI0cZqX84BFHn_OHpO6f01FFdydmBX0GSczQ7iTrAb5ztPCTrVqbgX8QwSuyEFTpkwqp57FlXdPmLtHBo5_RFTZjKMBsKUHBhyWaZ6agvkz5NXF8GOOnv9qdxX4fkGsosd_etbuCu_NikW5kUCcGfYtRYnpDREeyydY8rgCuh3-e_eLvZgHzcdSKzumx4zu1Z4zKzXDgY1ejbUOB_RXU1N8dngtBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=FR_9Fz3pg2W21RmjG6qUe6aIHAXlpTv3Texu-vBkWCGmp4ELuxy1162MgMXpDH4Ue1y8A2wsmMeC52L8oJxtkTIs7YUJ4RDZB6Zp-l8iU2qtHAlAmKeW9oGwxPQK7iAc6FhkYFxLW0RPt4nh3UUw22WZcJqDQh4dqMJ0ACO2TYolHAuSja7eVbLQii1htzFJovnfp1SoTfI-QnoRF0YT4ZSy9lYVLc84Hpu-F52LHvTuuMbfSnQIavW_LPgRPfYihT7ZpGrt6AqJ1BWh_dlgbn-SHm2iAIqPcW405Qs2FpCYpTc_U2nODpMB92bgnO2LGlVoO4bNpx3dNUVCqp6B3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=FR_9Fz3pg2W21RmjG6qUe6aIHAXlpTv3Texu-vBkWCGmp4ELuxy1162MgMXpDH4Ue1y8A2wsmMeC52L8oJxtkTIs7YUJ4RDZB6Zp-l8iU2qtHAlAmKeW9oGwxPQK7iAc6FhkYFxLW0RPt4nh3UUw22WZcJqDQh4dqMJ0ACO2TYolHAuSja7eVbLQii1htzFJovnfp1SoTfI-QnoRF0YT4ZSy9lYVLc84Hpu-F52LHvTuuMbfSnQIavW_LPgRPfYihT7ZpGrt6AqJ1BWh_dlgbn-SHm2iAIqPcW405Qs2FpCYpTc_U2nODpMB92bgnO2LGlVoO4bNpx3dNUVCqp6B3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_7U_bVoNgBhJwpT-GyfqMR36iFua064sZMWKmi-iVMUbUVr9y8tVqBmznSb-Zi07dC1yrqJBDmSyJ8tdrBMuz-NxvhNNmgSJ4hUGn6mar1bVyv2_Aa_BoyEiUZiLCWxJE8owaiaFBaBpHda6Lbhn-NJAdx1Dtg22-bM3-qzEy4yCB186SeMEDpBkB0sjeafpzd7EBNI21TaP32TDg_c3iXC4IGQClIAtj7MYoG3PZfTfnQVpNBdfIt7f0oTyHEMCgajAMtS_vWd22q5134HYcKPB9KpFRfkg7fTswLybpVVqH4ikKSOW6CCs_WW1upz8_i8f4a4rql_NAysp_NEKSx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_7U_bVoNgBhJwpT-GyfqMR36iFua064sZMWKmi-iVMUbUVr9y8tVqBmznSb-Zi07dC1yrqJBDmSyJ8tdrBMuz-NxvhNNmgSJ4hUGn6mar1bVyv2_Aa_BoyEiUZiLCWxJE8owaiaFBaBpHda6Lbhn-NJAdx1Dtg22-bM3-qzEy4yCB186SeMEDpBkB0sjeafpzd7EBNI21TaP32TDg_c3iXC4IGQClIAtj7MYoG3PZfTfnQVpNBdfIt7f0oTyHEMCgajAMtS_vWd22q5134HYcKPB9KpFRfkg7fTswLybpVVqH4ikKSOW6CCs_WW1upz8_i8f4a4rql_NAysp_NEKSx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=h82zGXsE9vWbHmvNsyZYcPsBg6kn46biD4-Qz5TrvzXJ-rCCrnUtkxN0GVml_h0HB1pT0USzZN3d46U8qx78Wo9hQp14UzT_Jhhwhnx8RAu9nt5sJj3xGFuPvPmzktb8hYY7LgoAOdSBbK1F-sUG0orV9MbWvz13aNO6Twah122coQI-BZPzwG7xBYCv4kY80kTU6syPsLjuf-zlBtQjmJ1cjI4khcOMBTmIH8ttGa9SLtRAbeSlUIlIcWTs4zyy5z2AlhGPOVgg5poqphHdr3RLAhe9t2HCqgywjs4KPfooK03wT8rC-o3LlVkzsEzKEI18B2XcSlRp_mdJVfjZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=h82zGXsE9vWbHmvNsyZYcPsBg6kn46biD4-Qz5TrvzXJ-rCCrnUtkxN0GVml_h0HB1pT0USzZN3d46U8qx78Wo9hQp14UzT_Jhhwhnx8RAu9nt5sJj3xGFuPvPmzktb8hYY7LgoAOdSBbK1F-sUG0orV9MbWvz13aNO6Twah122coQI-BZPzwG7xBYCv4kY80kTU6syPsLjuf-zlBtQjmJ1cjI4khcOMBTmIH8ttGa9SLtRAbeSlUIlIcWTs4zyy5z2AlhGPOVgg5poqphHdr3RLAhe9t2HCqgywjs4KPfooK03wT8rC-o3LlVkzsEzKEI18B2XcSlRp_mdJVfjZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Doobw0VSGp-l9nrwWzXgRV5rAlQ5ZexWqol8VOV8XbpcE_EKKew7crMnSDbSNQMj_1WF12nQ4QzjgQFT8oosagfB9W_Tm55vj6RFphB0c9HkpmgAgRh-Eje_q-sVN7pP8PQqyRVDb4ezH0VKOTVnmExcSmQfV5jHSyUXlYbkJ7fOqeUwGuxDecxPtfhOlIDomfY4_HGaRmicOVHZku8b1tEs7qUmq5PhyqWWkIDiipC7RHjKKz0RW0c_IXH5sA8p1cdp4H_vc9KWco17G5lA5KDqFSnA_6InIl0UXt5v7FNIMBysPmsbw-8LI3WxO3lnpwFAecTdLZCb_OaNNYwJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTmX8-s45Gm6uq6ON6jVQwOXebGEXkxL9vTxohkL0hDzqY45EP9JY_vmKEMokFLcobnJQSqWf5IIfGxHOzISRUeJ1yD-ZcbPW-prki__oe8pLtJLUjBGAaWPwbamqOJv2aZssj24ZM32blnW9397PlFI1rcApbTe229KYvpBWElcVuNVrLN-L_uY67Hl9qntEWdTBfFV9ljHPiX1E3w_K7zcWt9lswGNTahOlC7jKnhI4LGzkqfG3SFr-ixwg0IOy46e0CcppXrxvSOILGivi2d91xsrORBivP2C0gC1tYHKImZn7vtBNY3UWhxf8h8Ky7Lwo2X2HD5KobYPHMKn7rOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTmX8-s45Gm6uq6ON6jVQwOXebGEXkxL9vTxohkL0hDzqY45EP9JY_vmKEMokFLcobnJQSqWf5IIfGxHOzISRUeJ1yD-ZcbPW-prki__oe8pLtJLUjBGAaWPwbamqOJv2aZssj24ZM32blnW9397PlFI1rcApbTe229KYvpBWElcVuNVrLN-L_uY67Hl9qntEWdTBfFV9ljHPiX1E3w_K7zcWt9lswGNTahOlC7jKnhI4LGzkqfG3SFr-ixwg0IOy46e0CcppXrxvSOILGivi2d91xsrORBivP2C0gC1tYHKImZn7vtBNY3UWhxf8h8Ky7Lwo2X2HD5KobYPHMKn7rOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=CQjZ1ztwQ8UlkYyvaSxPnDfK78oJf4w5mBX48kfi_fj45_MCaUjy-KMTS6L9AIgonf3ug9XjcfWAXOIRtgmpAyKMYYY-COeIC6uB9M0D93-GG9G3J2omT3_RSlNd1tZfUWTPyPe-Kk9YknCXUYImV9A4XCjPe23aOSTssCvHTYya-Fy5kaFLUpnVDN9U-TozTm4L91EDuvoY1ck9JYLteApwtnH9b49m7o6qoUbNMEqyaEjpY8Ty6XdCCOgHA0lYWq0ZyXZXA4zIHgq1JXewDPkGX8HfgAUfC82IhRimCSCJB4ULGQteJZmqPfftmCjCm3ENGPZMDZ9l07QJ18Zwag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=CQjZ1ztwQ8UlkYyvaSxPnDfK78oJf4w5mBX48kfi_fj45_MCaUjy-KMTS6L9AIgonf3ug9XjcfWAXOIRtgmpAyKMYYY-COeIC6uB9M0D93-GG9G3J2omT3_RSlNd1tZfUWTPyPe-Kk9YknCXUYImV9A4XCjPe23aOSTssCvHTYya-Fy5kaFLUpnVDN9U-TozTm4L91EDuvoY1ck9JYLteApwtnH9b49m7o6qoUbNMEqyaEjpY8Ty6XdCCOgHA0lYWq0ZyXZXA4zIHgq1JXewDPkGX8HfgAUfC82IhRimCSCJB4ULGQteJZmqPfftmCjCm3ENGPZMDZ9l07QJ18Zwag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=KU0lNJTz_kl9ftOpmMDAw1uniTexlRAiJPhoHn1OSxuyZ3j2pFVTojgCDEMmLaHseFdLwNZAyY9nJPk1eLbr-nIXEM_6aMWLc1GXaeJa6IMKYGlodlE_299gqrP2HcTmgycrJCpO5bXw9Dcjz-06s83TYfs82qdCtEQY4giqeNBPtfGI8p8lk619cHGhk3ylrbHGnm6mJzxXkYBaIY9jih35YHijZ4kybfbF9-kG5Q-TcwOBr88-V4e3xCl3ZKXDs355ZRxtECPFd-HJi5VAjjLESAg3zcqcxgAiMIePmdXsjnQWo3fSJk4hLhZL8kuozvoX4roxaePB_drJSxxh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=KU0lNJTz_kl9ftOpmMDAw1uniTexlRAiJPhoHn1OSxuyZ3j2pFVTojgCDEMmLaHseFdLwNZAyY9nJPk1eLbr-nIXEM_6aMWLc1GXaeJa6IMKYGlodlE_299gqrP2HcTmgycrJCpO5bXw9Dcjz-06s83TYfs82qdCtEQY4giqeNBPtfGI8p8lk619cHGhk3ylrbHGnm6mJzxXkYBaIY9jih35YHijZ4kybfbF9-kG5Q-TcwOBr88-V4e3xCl3ZKXDs355ZRxtECPFd-HJi5VAjjLESAg3zcqcxgAiMIePmdXsjnQWo3fSJk4hLhZL8kuozvoX4roxaePB_drJSxxh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Q_LxDFfJO8z2DkihZFJd-kbr6-3yH-g7vM8zaGXRsooii8mS2OQj9rbxxWrcxH7OQekkEFtGjZfy33qkCLTVKrewnWQ3L9b9RWnnel20fmrpq75hbo13lrXe6xQx4NRedHgJC5RIQxXnykLxpoDxzxn5lbsqhM7f17xf_rkQn9wIgAHLlJWTxmSbf5oZI8WsQaTfwIcJNP9f8pO0K1E_R5FTpvPhxJZbdBUQcWfoirjjzOdLqYeQ1YHRmOHMBNSvsSCQ-UUefn6NBHHGrS1JNIggMqkgRm46PEZSCXGef8-FsdTZDLdqqwkGW7rn1w47To8SiPHNovqYOZKvul8BZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Q_LxDFfJO8z2DkihZFJd-kbr6-3yH-g7vM8zaGXRsooii8mS2OQj9rbxxWrcxH7OQekkEFtGjZfy33qkCLTVKrewnWQ3L9b9RWnnel20fmrpq75hbo13lrXe6xQx4NRedHgJC5RIQxXnykLxpoDxzxn5lbsqhM7f17xf_rkQn9wIgAHLlJWTxmSbf5oZI8WsQaTfwIcJNP9f8pO0K1E_R5FTpvPhxJZbdBUQcWfoirjjzOdLqYeQ1YHRmOHMBNSvsSCQ-UUefn6NBHHGrS1JNIggMqkgRm46PEZSCXGef8-FsdTZDLdqqwkGW7rn1w47To8SiPHNovqYOZKvul8BZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dETs958P5zXKvKrysdGLRhocibp0m_mBYrGqetgS9wZKMdQ7rF1aIOwcpwWZGul-44gwQTX4WxY2h56vYr_bWB06Vgz-ogm6v--jcKPfeQQEjzYZ0yZjgbteBkYMeZYOi2YOZDdaTbt8tkFh_AOVWiVyn0B_gtWJE2cTEpOq5IBksBqqGbj1NLeigp1c7cUlYpnaz1tWykTjuEpE2KgvGnobeEyufL6qkSfKjDrszSMlJE4A6A1TpIWY9PkXgSSvIuORUJCUD7-C9iJ-yHIHJKn6_izTpaBRcSRhO9xlqp3WwF4NFooxMsNIn3vD1R-VOEGEauVNQ6EIlLL4P7UaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5vaNqXA_Z0BuAngV3Upge4shQziGzC9Nx_qCVhlcPBSu6b2WHXygDCqVuRRRHS1F02SFyRn4qifPX1egb8yxY17l7Fc3Oszns-CeTHG966Uo2ZsO5aXT1DQ48ZTRoUe5zIf_Rnj57fFxPiQkcY8Ta9DrXdqSQC5IhKO4Wnc1JvofWejJhcv-UsPmAN7HrsbFFsw3QG42R343ZEuUv9gjJeq3ibJ0cJCAvog6lx0sjlarbLCBOReulEDv7tixF6oYw_pKX4MH_iEznkPZPyorfK0R_QkctRNSdIlbK81q6Txz2d_pghp2LnIbVzDlqGqYetj7yg2CD8nlpz_gBsVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=YwLFYrV9pvXq632VmK9IVUppT0l1ek0i4126k1zm7JJiLriCnwzKzbllDJkUzr1j4xs1g1BAuDSo7gaAkyEFPeQui7t51M4rH9T8kX5BOxxMfvnS3hIlfpCCcvT4ivSnKJZDQgcpJfDZDOHbbNMrKPe3Pge0DmsV8_4TshpaSKwNAjXpbkVjQN7OKMtL18hKrUT1HvvFbWxLRCk-H-cYtsw6t_GnDibGfJWdAC5YNCnZn_pLIHFylZMU1m1ZMZMXtTfIF56OayBBBW3mLpRa7tyb4ph_MadYDDi7RAl88QEiC1cjmD8fUmTpz-IwBw5OYQvjH7yI4qn1HmJUn5658Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=YwLFYrV9pvXq632VmK9IVUppT0l1ek0i4126k1zm7JJiLriCnwzKzbllDJkUzr1j4xs1g1BAuDSo7gaAkyEFPeQui7t51M4rH9T8kX5BOxxMfvnS3hIlfpCCcvT4ivSnKJZDQgcpJfDZDOHbbNMrKPe3Pge0DmsV8_4TshpaSKwNAjXpbkVjQN7OKMtL18hKrUT1HvvFbWxLRCk-H-cYtsw6t_GnDibGfJWdAC5YNCnZn_pLIHFylZMU1m1ZMZMXtTfIF56OayBBBW3mLpRa7tyb4ph_MadYDDi7RAl88QEiC1cjmD8fUmTpz-IwBw5OYQvjH7yI4qn1HmJUn5658Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLnnx2cIjNK-CFVgB97P50DeLNfQd5I-Z3vFHvZ6kr7lv6kr_ohvrKCU5xkq_joBSsxQ8t1Cur2KqQtWJbYm4dwAKUxYHm5PnChNmwlzjTdzoX9ZsRe3QNsacFk3N-S2xLAGydBPau-FJeaKQz6FPnszKwPJcV0D1d3QEiiXrMhg3X0y9t1AjtgoDwUFqij5UTfd5QOeUaajQ4hphcQPkCkXMWLOVmq2dVcVCUjUKxTJEZY8DhFvmE5wMTwTylFacsoj2IKZxDP3tvvc6nV2Q2gAQTyM5li-NXVkSpeA_3hLJMXpBDE4fw6tO4I4zexvByqSUIRj9FkSSrrLW-TVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdiB1XbgS1Cntyf5U8eDUWck_1L2-Mk5p3vAD2tLxivVLyk_uvjr58B0xe9JmIY8H9okem4zA295JEf4hf0L3eIDboouENngfsOQmVcRgC7EjbZFs5odLCVhUnZx2MtKU761ETpDEYxbsbWq7Q1Dn99i1vQ4WkJMGmEokzmwLdf8UB6PJpYqQY0FYFQR_kXiGUI2w8A9HKs6bnxk8QkS4e4q63Gj9GUD_M3tDQtgATjtVV_PpxVzo4Xt9BeHoopTVuK1e9FHLKw3ZaH4HXo7-KekZ6CAm0wuqjOEa6Jm3F7IjQbPQS70Lv2A2Nt8JbAd0Aex6QLZjU0furPbs4AcJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=MCFXoxeBedTqoV5XQke6jnub5xKY2qZndoPHXCNU7y2RaPTsRfYaFyKucvjhDACP3LVSb1e_1ydELQGLq0vxwsZNVEtfE5ku5TdMoO_kWE9BZ78n3NFOydw6XKHz-tMBf8VYmleRZurTbl3m1_QXxdgo5nBTkHOMy8DYL03GPUY8evcxJ2y5CpQKVm66LWafTWPiDKW02DPuD7SxwMKwAnI9Nk3CwiT-oDpZrMPPAyZB51coM3gAiPp8VXo3nCbsFnjdlP7lo3KVjklfnz3OjRFk_O7SXc-xfcDmc6184Ec3O1HgDuH4fJt0_jwdJ2-DLHIbsNE0UcGjLvHw4ideHAkw7b7r_5MObm7Kw5-4QQMCCTeQCBJKgM4Tf2-EBw0av2NoZ00BIib5NL4StoYkX7PJQGjX9ktWzLxFyEpf8Lue9Y2vW9_P6j3xxd4MplzBXiDy3lMAEv5D0oGWFkp1qpoJlJjaTJlDlwz3OiGCi3WW2wKSKfvXoh3YDn7f220HyDxUMYnOyCNoOhp14ohfrRWjT02c8sVSjaWTEskKKxYEyojCODZOCFZSU7SW_VetBwHuP_Xl_j-_iknlFXkrFADznudQtroKMY0Alxu_iqlTmaWWFzNh9XiKP8WSo0gcyDdBhvJQRE_g-uwUswhX35pqG3_7DybtY1F1zgUYn4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=MCFXoxeBedTqoV5XQke6jnub5xKY2qZndoPHXCNU7y2RaPTsRfYaFyKucvjhDACP3LVSb1e_1ydELQGLq0vxwsZNVEtfE5ku5TdMoO_kWE9BZ78n3NFOydw6XKHz-tMBf8VYmleRZurTbl3m1_QXxdgo5nBTkHOMy8DYL03GPUY8evcxJ2y5CpQKVm66LWafTWPiDKW02DPuD7SxwMKwAnI9Nk3CwiT-oDpZrMPPAyZB51coM3gAiPp8VXo3nCbsFnjdlP7lo3KVjklfnz3OjRFk_O7SXc-xfcDmc6184Ec3O1HgDuH4fJt0_jwdJ2-DLHIbsNE0UcGjLvHw4ideHAkw7b7r_5MObm7Kw5-4QQMCCTeQCBJKgM4Tf2-EBw0av2NoZ00BIib5NL4StoYkX7PJQGjX9ktWzLxFyEpf8Lue9Y2vW9_P6j3xxd4MplzBXiDy3lMAEv5D0oGWFkp1qpoJlJjaTJlDlwz3OiGCi3WW2wKSKfvXoh3YDn7f220HyDxUMYnOyCNoOhp14ohfrRWjT02c8sVSjaWTEskKKxYEyojCODZOCFZSU7SW_VetBwHuP_Xl_j-_iknlFXkrFADznudQtroKMY0Alxu_iqlTmaWWFzNh9XiKP8WSo0gcyDdBhvJQRE_g-uwUswhX35pqG3_7DybtY1F1zgUYn4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6xLyekvA_czyzejmC2-0W5S2XnmRvRtMCAKKPliMKSMZ7utCQ_1JzguFuZsKGauIXCbzPue4eKN9BEsBJEk1tX7UAa_VZeF62vof1W1RmpL2cmEvGTFzJjkc1NZ12hdlE78tBVCz4T50u9gOR03Wpo4hXN4tYmXFW3HBBqMWnQVv32iDdDy0ObgHSmwiHhCvpAzEw-sD7_gp14-GaOxI7lbS3xeEoWcZ_ceBWcorV8URgy6oXm9r-HB37xDsnNBuTx8fL4Pyp-fcAMU-8JTJxz0cK56ZE_UBL4ye6t_VUQS8_VSEk76QtQKh2olUQ7qwI_DpEKPFLuqqT2Vc9O85NO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6xLyekvA_czyzejmC2-0W5S2XnmRvRtMCAKKPliMKSMZ7utCQ_1JzguFuZsKGauIXCbzPue4eKN9BEsBJEk1tX7UAa_VZeF62vof1W1RmpL2cmEvGTFzJjkc1NZ12hdlE78tBVCz4T50u9gOR03Wpo4hXN4tYmXFW3HBBqMWnQVv32iDdDy0ObgHSmwiHhCvpAzEw-sD7_gp14-GaOxI7lbS3xeEoWcZ_ceBWcorV8URgy6oXm9r-HB37xDsnNBuTx8fL4Pyp-fcAMU-8JTJxz0cK56ZE_UBL4ye6t_VUQS8_VSEk76QtQKh2olUQ7qwI_DpEKPFLuqqT2Vc9O85NO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=WZROR1xu2Gl5Axjjvkbq_sZDSZFbGNNuFQa6KWfqainy2RrCi9EDFgm87YNU3zYeG_cjl1QkcS8kUdIExM1hib0BkpA9PJTuba1hfcgmFGrSq1OuHjjUpDw3moBSm1SbvL9V-Xtbczdvz_mxnIPlIk8-DDy2GNVWCIzhGZ506tsu9-cqQh1mWk9FXHUQzmGpeqbffNczOn1SGEeetTJ93bezUCB0d07KVoKtbCrTagyZhwpLmrxmglEOFUBWwjCesIUJYi6_PXLCvvkjc10lj0sIHO_44uYRaxub2G6OTiOUS9DB-3Hgyq_uqnwsS_P0P9oWkjl2UGZ8_BtCmDkAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=WZROR1xu2Gl5Axjjvkbq_sZDSZFbGNNuFQa6KWfqainy2RrCi9EDFgm87YNU3zYeG_cjl1QkcS8kUdIExM1hib0BkpA9PJTuba1hfcgmFGrSq1OuHjjUpDw3moBSm1SbvL9V-Xtbczdvz_mxnIPlIk8-DDy2GNVWCIzhGZ506tsu9-cqQh1mWk9FXHUQzmGpeqbffNczOn1SGEeetTJ93bezUCB0d07KVoKtbCrTagyZhwpLmrxmglEOFUBWwjCesIUJYi6_PXLCvvkjc10lj0sIHO_44uYRaxub2G6OTiOUS9DB-3Hgyq_uqnwsS_P0P9oWkjl2UGZ8_BtCmDkAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=ezCiGsG0CCOLgQcA9MDJujUakZG856TCCaeM-9BiOh-BwzCYeJ8Q6KRUvsM5SXM5xzxLOY0d2ILdempcKPR9vHOz5UxrDMjRFN--TgUaEnu2bax1_01fz-sOIHzvPlPve6rD5lalPButQGTtgabl6mISVX7TOvEOGI5zuX3i042PJEeDDlcGE5Pu_6a1eQCsAwes5xTNiMGFCf9lm0FxXz-PYs1zylHBOv913S3IZyG6sBMH7CN10pAj4uQCyvAn0t5bK0yO1RHX0XL6RSKdgm0alY1TOw2jBLMolN0dwXTuQVXpWcYJEFGzGLg4XvgTtjRcisB7RbS7YmLr3kfNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=ezCiGsG0CCOLgQcA9MDJujUakZG856TCCaeM-9BiOh-BwzCYeJ8Q6KRUvsM5SXM5xzxLOY0d2ILdempcKPR9vHOz5UxrDMjRFN--TgUaEnu2bax1_01fz-sOIHzvPlPve6rD5lalPButQGTtgabl6mISVX7TOvEOGI5zuX3i042PJEeDDlcGE5Pu_6a1eQCsAwes5xTNiMGFCf9lm0FxXz-PYs1zylHBOv913S3IZyG6sBMH7CN10pAj4uQCyvAn0t5bK0yO1RHX0XL6RSKdgm0alY1TOw2jBLMolN0dwXTuQVXpWcYJEFGzGLg4XvgTtjRcisB7RbS7YmLr3kfNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an-FK3fkgoUjPQZncPh1aeUUxoaxN--fI0FPmkdk4Zh6g0LqsoMDGbFAX_XlNrSdwpHjok5Zahawvln9ct1UTA7tLSJfpmFieuWNfoElj-Qy1n5UQJT8esoiYkEKmJGgAXgjOA0JtSGiQAVx4seUuiOIp5oAkvUSgl6Uy2igjREPdVosWAUL6vSb9_eG3YGeZQN_r9gfHIPBxwOpI26fP_Sco61wAaKOaYMfWoNwFPU38fg-4WdjB2xIPVDO45xBy8vqR4dRgFlI1Q9OpGrPfYIbqvbOFT8zIiZvtTaV0l9aEnDx-tcCzyagZ728J2jd1K5gWwtG_gmYMDs7aU9d4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtTb0F9nCA-WDxWj-9JpAJ6qua5yLidJfX2ZY2AzAe-6y6-L8ssnILNJHZY-FS9z8wic_sEP22x9c-Cte_Xf_6oRdKoGvQZeAi82hOMEjE7EJnyMzGpnRMEBCndGDfaWcMz546zHd3JmQguejRdJOGP_ofy9I17z4DYDOVDTYxg1VIjlc495jZxyNCg0gD0aKNG_MO_NQoK473pg_7qDHWsTfOp9c38E30CIL-ojQqHi0bfKNcBIWL_eUDb7m8QKtdjnJd2P4F5JKP-JYvBaucefMsR_tN5pT7jxW-c0hEcUTWwJGmTwlOEH46WX0noCunfUN5Sr_HzQfiZX13mLNg.jpg" alt="photo" loading="lazy"/></div>
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
