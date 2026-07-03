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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 22:33:56</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrtjNCQ7sysvrI7qaZV8RfgB_gwOjvKPHhyXb-k0nv6HO19_LPyOGqlJ3ckqO1Qw_jlTLXmqPuFRg0Ut4kDpJM5RcNW_xD7XawoniQBESIo1osoit8vavunLbbZI8qIuQQ_Yr_KO9iY4H3wnOBmJG43FaWTio3HE8UdnnSkF4IpvO6dr5p5A9CvkR_jPF5J5Xg2Nhw7CtqUcZHiiwkOdAkVbYa-vZtpjaA3FMMl8Y-muKEvBnrdT4yNDXxRIzbgHwZ4ktaZlQfq1S1dG6MxhT98UyhbabmOhvHJ2EHq1jcybZP8fRzAK7m0Usalf5SBoqHAPr50WgKNnUzFcUTmtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIvRlzbaJkTUwPsUWS7sWzlix8I-jMzGzF0Ehexiz_-Bst6mOH5f06XksaXyzgYQ8MBkfTLDoPKL7OhGRa3_tTRqecNM4syUqZOTmK4ceRd74h2SEI7cUETMAopeEGRZBzm8GILhNb0r8toPDb88f76hqZOvQm3V5aqpcs2JB2iRUYtCQ2I-F6WnRAEWIGgEeh1VlKaWpiAIIj2Lx1UCOFbNpApA5PkMR_Q7M4-w7wLT739PLkTCd82j99ZZ8eltLXfYo6CDnnbuXW2o6rGDvh7seIyzIRXEQdpzabzDKjEcslMJJPyBDwplVQGiDnsDhT3EAyZ0j8v0esXGnQeeXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=A8yEtRxnqrLyLI0IlJ1PwnVrOdFlH7aoSSrYW29FB65oBjupA2kZq07W3JO4voVonEu10aWATcqBn7jMiaIX7HGSF3cEx8vsErdxj2RTzwIqMplLEy7hLtY64U0Nj9GyulCenTtHjXiT-Jx4dJoCPWz6aFFkQbI8R9hfmi-tRKBMu66TNpnEHZRZOURA-lXHF2OMupOU8fs5JSBRXGkaalI2UQGxOxcOwUVpPC6KOOHYvfgYtrXUy7OfAkU1NVqEL3As8LBN1x5ntoHacjlHiYbVBXt8Gy72bmFEEy0AT51rWhjcwASrwDXvBOrm5qRFmjNsllbwk1GmlcAPz1m9ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=A8yEtRxnqrLyLI0IlJ1PwnVrOdFlH7aoSSrYW29FB65oBjupA2kZq07W3JO4voVonEu10aWATcqBn7jMiaIX7HGSF3cEx8vsErdxj2RTzwIqMplLEy7hLtY64U0Nj9GyulCenTtHjXiT-Jx4dJoCPWz6aFFkQbI8R9hfmi-tRKBMu66TNpnEHZRZOURA-lXHF2OMupOU8fs5JSBRXGkaalI2UQGxOxcOwUVpPC6KOOHYvfgYtrXUy7OfAkU1NVqEL3As8LBN1x5ntoHacjlHiYbVBXt8Gy72bmFEEy0AT51rWhjcwASrwDXvBOrm5qRFmjNsllbwk1GmlcAPz1m9ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=AO6GV7WMWNL_f79RaLYdED0vBcnpwn9T28CNeI4xnGXNQNLK534ZWN7pzBKOriq5zM597cyOHG1AluemCwC15OTL0X8XHTpio0xmskBHyYRKLgiWWts74_Pnm-jSVLfdf4_NFZprr9Ov3NVweHySpyD_sXu2chM7XMo_xZXPK65grCD8rK-Yp9R5jBwRMCRoJK2RImYsVNzPg3glSbAvh_7ZeS118OLPJhwFfCfvlTgIKO4VxsOZpLZs5-R9vxsh98Hrsbb_9qStWaY9GcSXM2Le5f0gRaAFSRpnmjAUsQlZ5T4y-o42s6TR3tT9mrYNU-DkKIcnFSnqgfrtnK6SXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=AO6GV7WMWNL_f79RaLYdED0vBcnpwn9T28CNeI4xnGXNQNLK534ZWN7pzBKOriq5zM597cyOHG1AluemCwC15OTL0X8XHTpio0xmskBHyYRKLgiWWts74_Pnm-jSVLfdf4_NFZprr9Ov3NVweHySpyD_sXu2chM7XMo_xZXPK65grCD8rK-Yp9R5jBwRMCRoJK2RImYsVNzPg3glSbAvh_7ZeS118OLPJhwFfCfvlTgIKO4VxsOZpLZs5-R9vxsh98Hrsbb_9qStWaY9GcSXM2Le5f0gRaAFSRpnmjAUsQlZ5T4y-o42s6TR3tT9mrYNU-DkKIcnFSnqgfrtnK6SXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=GpFtJGG1S8xh58deEVbvTYhkvBholpWm2o1YIiV7rFszSZ-GacPT0g_sw2j34-Q_3sh0VvIGwHlHdOOdWld5kNc3Olrfdz2Ut08t1swgsikEP-5NgwZAAAWRMSPab8Wi3MDXCHx1c6XACIX9twFtlqgska3EM3yh916zwlwh0f1wcezEDOgI8OXcLIJn8eSzRApDGN1FWtwdymI1vQ-mDVt0tn1IFW_7MBCsD_lAvVmjmBQRJ-J3ekNvMeJZVFvINE29S38wp-JSzFSN0Ew-B2SZuDzRqM8eARQR8NgcLrmIPLo0366z4CKTd3ODM9vLaFuC8G6WlSse34eMJbeKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=GpFtJGG1S8xh58deEVbvTYhkvBholpWm2o1YIiV7rFszSZ-GacPT0g_sw2j34-Q_3sh0VvIGwHlHdOOdWld5kNc3Olrfdz2Ut08t1swgsikEP-5NgwZAAAWRMSPab8Wi3MDXCHx1c6XACIX9twFtlqgska3EM3yh916zwlwh0f1wcezEDOgI8OXcLIJn8eSzRApDGN1FWtwdymI1vQ-mDVt0tn1IFW_7MBCsD_lAvVmjmBQRJ-J3ekNvMeJZVFvINE29S38wp-JSzFSN0Ew-B2SZuDzRqM8eARQR8NgcLrmIPLo0366z4CKTd3ODM9vLaFuC8G6WlSse34eMJbeKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=V0Ev7V6_NDwCQXOEbS6omQFWB6XxqECR4IRgVJqhH3nncbu6vX4JTXK9npz9rQ5eu1_kGf4LKNFk3LrljvIMtG7vmKU_ss0mVNrny3xNSmu76TWdfDnnXY8rUNgLaC3kjZjBJuMRw4f9vY0wv7jPRCW-fcX4QDV3e1GubP4mhr_stW9u5NUjpr-uaHq_KoxF9R2lyWPYY9QnrMMNApziKf86SC451QazWminb8dZ55f6ae9rpR2t25E7SjgegPXyu_eFOYV7G3gpwklsrWDbxLZR2KZ-U1rLiarfN3u3rvY2xZARzVayMI-ftctPpX2QidjIbkORuHao6rlux8NtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=V0Ev7V6_NDwCQXOEbS6omQFWB6XxqECR4IRgVJqhH3nncbu6vX4JTXK9npz9rQ5eu1_kGf4LKNFk3LrljvIMtG7vmKU_ss0mVNrny3xNSmu76TWdfDnnXY8rUNgLaC3kjZjBJuMRw4f9vY0wv7jPRCW-fcX4QDV3e1GubP4mhr_stW9u5NUjpr-uaHq_KoxF9R2lyWPYY9QnrMMNApziKf86SC451QazWminb8dZ55f6ae9rpR2t25E7SjgegPXyu_eFOYV7G3gpwklsrWDbxLZR2KZ-U1rLiarfN3u3rvY2xZARzVayMI-ftctPpX2QidjIbkORuHao6rlux8NtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QxXOVeYcF6HxarrD3f_jrzlXAtRJg5PM3_K4prZleAvjAjEbLEBFb8qcpAf7hMiXZarMxrwZBhqPCZeiVGoEV-ryUqwBb-cNsn0N-tZJwE-yzBQeuY2Nmz6tABxySEJRcVZR-x89yqUYrXMbGe_0sPvcjESRcqVPXz2dEt3OfwtXDExbaZ5QvH5OTm4SwjV_jkO_JTF5T3rDbt65NZJPee5di66FwuhNtr9ESFJjIqgjJALZtLMZYRc47AeYr6k0KvQU6mmc0gPVs8xCknTxrnT9p8nUSaAjpogiLZth-_bps0UM0vY4l6D72tomlFv6ze_eIW7lERIplmZXXkMNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QxXOVeYcF6HxarrD3f_jrzlXAtRJg5PM3_K4prZleAvjAjEbLEBFb8qcpAf7hMiXZarMxrwZBhqPCZeiVGoEV-ryUqwBb-cNsn0N-tZJwE-yzBQeuY2Nmz6tABxySEJRcVZR-x89yqUYrXMbGe_0sPvcjESRcqVPXz2dEt3OfwtXDExbaZ5QvH5OTm4SwjV_jkO_JTF5T3rDbt65NZJPee5di66FwuhNtr9ESFJjIqgjJALZtLMZYRc47AeYr6k0KvQU6mmc0gPVs8xCknTxrnT9p8nUSaAjpogiLZth-_bps0UM0vY4l6D72tomlFv6ze_eIW7lERIplmZXXkMNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=RNy7xsM1ugTz0yurKMSPGm79cgP2pE3WJfD-holrJfL2dY1sbq8JCVxEs7jqf3aNCExFAwkpXw_BtcUUX20GTs9sIfQeyz0Mz9-xvieBhJUhR0j2AKMluUYXQ6EpBSgzudj9h9rPhsb70Eu_LJQisgd1msUT_sJ2qcrgIpcB0gw5CauEhkynQbvLRj66Kd3Wey9-4tM_XcDKfsG1pSN2HUJrSyvRd-7pchIMZ62Wrbz5Ost_9jCZxP_7hGb1m-5jy-ZonISh1fnbyPXoAmjsWV_WfUyvbDpRhQs_5XIomgqK7SmIKaJ8QEHXbbNddQU57Kg0XaPCUg9du-bZz6iN4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=RNy7xsM1ugTz0yurKMSPGm79cgP2pE3WJfD-holrJfL2dY1sbq8JCVxEs7jqf3aNCExFAwkpXw_BtcUUX20GTs9sIfQeyz0Mz9-xvieBhJUhR0j2AKMluUYXQ6EpBSgzudj9h9rPhsb70Eu_LJQisgd1msUT_sJ2qcrgIpcB0gw5CauEhkynQbvLRj66Kd3Wey9-4tM_XcDKfsG1pSN2HUJrSyvRd-7pchIMZ62Wrbz5Ost_9jCZxP_7hGb1m-5jy-ZonISh1fnbyPXoAmjsWV_WfUyvbDpRhQs_5XIomgqK7SmIKaJ8QEHXbbNddQU57Kg0XaPCUg9du-bZz6iN4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=fVqfjHsJL9-aEEJVPPrKSy3IhFmB9QDzQcpos-2xN_HqFQbBFtebz11WdAlHstBFvQWJXU0pLJ53TfAVEewu18iIGJbRwF7MwhSA1VtGqKZ2mog8Wj52_6okk-BMhIIgKRu0y7GTj1cDTRM4yCbNzMX5baB2JbfY1rAQCTk6vWuhNBzw_Q0kVLvDGARlxaOZ5DlFtY9L3AGpriAR9d0I7DY2IfSIdYluO1Z6Im7OTGMCv4Rvn41E1qPS2o6uzMDlHnQxnZZu26WsV9cVX1Y9cebYVGHUbATzby3f_UmUO6ggO88JQlguLBm0i8ECusJwPoEP4r8PXZxMZOlSzksEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=fVqfjHsJL9-aEEJVPPrKSy3IhFmB9QDzQcpos-2xN_HqFQbBFtebz11WdAlHstBFvQWJXU0pLJ53TfAVEewu18iIGJbRwF7MwhSA1VtGqKZ2mog8Wj52_6okk-BMhIIgKRu0y7GTj1cDTRM4yCbNzMX5baB2JbfY1rAQCTk6vWuhNBzw_Q0kVLvDGARlxaOZ5DlFtY9L3AGpriAR9d0I7DY2IfSIdYluO1Z6Im7OTGMCv4Rvn41E1qPS2o6uzMDlHnQxnZZu26WsV9cVX1Y9cebYVGHUbATzby3f_UmUO6ggO88JQlguLBm0i8ECusJwPoEP4r8PXZxMZOlSzksEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPH-xM3aXDQV1iBi9DETwk-4CewfI_gOPq2OC0zfCo5itU_mM86tiUmyc_d6vui5vuurYJ_FTNQlIG0mgV1mlr_om3TLWuYQoozEPBg-yawlBchhfANE3WBBClH3I265hEKCwrA4CHMF6sqA-L88oS_mgN5bwweWR9A8ilURd3EeS-HCctM2W4sLSQ6K_hFys0ZPNQvaulrMH1di2DYA6qvr9_5RC18N9q8wsjS0kmF6awtDaF3a5CH9TdND3pbB1QIEPDAOQE3YvC7GMuJ0f3ss2BwTdpgW--S26Y5hoeq9O8W1ph0uDdeQSm13ElBOEAblctnBlPwOIAN_t_c8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SXbXJinSM0ZKZFX9lvCdNcZb-5jTLkPA5ENztlqOVG-yoE6lWZpJzKb_yR8hMrEHKLYR6vDLwCrh-d41HxIBgaY0lkYKZ8wuZbx7lbcUPUTgxX10FCQ6jbAkSShWsOXUAFGrgQcfoS2NDv95QzqvMXoH94o9QRjWmKrRYScoUrr5CF-v3qMzwHo8wHzvykbv5ZCvbs9L5Km1WpNj3hjDFTdmz2Fi9zceB3OMeWFqHCHUu4J7OwfcCHOwKLxxfHi4ZUPKPDV_rHSDucXhaWrHtOEkxBhRf3KGHhXUpjLoe_VyNb3W-PbOeXls86WYjT8AY04zgevN0xlN2tvZzrz3UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SXbXJinSM0ZKZFX9lvCdNcZb-5jTLkPA5ENztlqOVG-yoE6lWZpJzKb_yR8hMrEHKLYR6vDLwCrh-d41HxIBgaY0lkYKZ8wuZbx7lbcUPUTgxX10FCQ6jbAkSShWsOXUAFGrgQcfoS2NDv95QzqvMXoH94o9QRjWmKrRYScoUrr5CF-v3qMzwHo8wHzvykbv5ZCvbs9L5Km1WpNj3hjDFTdmz2Fi9zceB3OMeWFqHCHUu4J7OwfcCHOwKLxxfHi4ZUPKPDV_rHSDucXhaWrHtOEkxBhRf3KGHhXUpjLoe_VyNb3W-PbOeXls86WYjT8AY04zgevN0xlN2tvZzrz3UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=A__JE6Jf9PipkGq0hPnXUBNsIloGIIsPpYet8AFf5KHPHW0nasHSzdTFsmJjERjvuQhGxQhhPPFA2B-RZNQgPHKsoGYitKRfDItJ9kU566D3AXGbAATL-ieXWwM86pQnUbNyeWlah95torHypewakCaQPsiKStI6uWXqS4lqt4byI4X5AJgdrgXHRv8M-UvABxTt5HdsMlk6TA3zcNc_isKJT3WzaT3JuxZTSXKCPAXkW8nc3J1e52Kv-6xaA9eeXzfe4_G1-ijp8LvVPdkgSLTT7e-twxox2185EbnIkZzgoskxWtB7E3RNkJU7J1C10zX-SraSuO3pscmwG-aw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=A__JE6Jf9PipkGq0hPnXUBNsIloGIIsPpYet8AFf5KHPHW0nasHSzdTFsmJjERjvuQhGxQhhPPFA2B-RZNQgPHKsoGYitKRfDItJ9kU566D3AXGbAATL-ieXWwM86pQnUbNyeWlah95torHypewakCaQPsiKStI6uWXqS4lqt4byI4X5AJgdrgXHRv8M-UvABxTt5HdsMlk6TA3zcNc_isKJT3WzaT3JuxZTSXKCPAXkW8nc3J1e52Kv-6xaA9eeXzfe4_G1-ijp8LvVPdkgSLTT7e-twxox2185EbnIkZzgoskxWtB7E3RNkJU7J1C10zX-SraSuO3pscmwG-aw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=NAACe3CdrI1niNsh7TxuRrKuMd6Fl6b63HFdh5MUgukgU-MONhgT_v8W_xnYIinH6bqHvGCiA_hfDRE_9xcrmVlkDw-8W6yfA-razjbzZ7pAlM_TIegtqOCy-u8KBeZbeFU0w7XGuYxAfCRCZSdtcey8A1JUfy6hLlngdPE3r8b_3v4Jx6YEihbdO6mqBcYPMQZ4q8EZm30LChwIn7zsPHVawn-Gld7DO7dpNC_-YLtI0b97YIsCkUoc-zj274ky3hgw4ojdomda1bP0WjcrL0b4uNmRka4UGC9gf30bakWQI4Rk_b2QtTB8UU387WXOhB2ammW7fNj-stbi5v2fdIo3a9QNmStYhpH3nKzGRnsKT2xnzMlpzvd0NVmZjzh3w55JtUidHvKz3fTyckp6U9zMyC6T8UZe06TIGZZFtXnnt34aEKyvO4QyKaZx83CL6PGuIszP-XzYwr5BkFEEdMdjVjUUIOKRukecCwN_lDh0XLS1KONTKIKtem9aFX98oBzcAC3TXBCe31EF6ZuHqKTCFm2U4iwBIrJnpU5txKfsKhIAzT3y08POWHDg8MeYHPCWg_PEdxK-7pSdxokd5M4f8MHHKDC3QpzxZsWq6288zSzFyRgasoWO2TeT6qBdzmrSaFOEyg6MOy8mwnXyrViVYiRrLwmzJjVhLB5ZM_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=NAACe3CdrI1niNsh7TxuRrKuMd6Fl6b63HFdh5MUgukgU-MONhgT_v8W_xnYIinH6bqHvGCiA_hfDRE_9xcrmVlkDw-8W6yfA-razjbzZ7pAlM_TIegtqOCy-u8KBeZbeFU0w7XGuYxAfCRCZSdtcey8A1JUfy6hLlngdPE3r8b_3v4Jx6YEihbdO6mqBcYPMQZ4q8EZm30LChwIn7zsPHVawn-Gld7DO7dpNC_-YLtI0b97YIsCkUoc-zj274ky3hgw4ojdomda1bP0WjcrL0b4uNmRka4UGC9gf30bakWQI4Rk_b2QtTB8UU387WXOhB2ammW7fNj-stbi5v2fdIo3a9QNmStYhpH3nKzGRnsKT2xnzMlpzvd0NVmZjzh3w55JtUidHvKz3fTyckp6U9zMyC6T8UZe06TIGZZFtXnnt34aEKyvO4QyKaZx83CL6PGuIszP-XzYwr5BkFEEdMdjVjUUIOKRukecCwN_lDh0XLS1KONTKIKtem9aFX98oBzcAC3TXBCe31EF6ZuHqKTCFm2U4iwBIrJnpU5txKfsKhIAzT3y08POWHDg8MeYHPCWg_PEdxK-7pSdxokd5M4f8MHHKDC3QpzxZsWq6288zSzFyRgasoWO2TeT6qBdzmrSaFOEyg6MOy8mwnXyrViVYiRrLwmzJjVhLB5ZM_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=HRx8TiqGYEURQBcgNmyqL89LXArfVnBrE_jHi5kWFdaJSXcbWi1TSGoMXuCkLm1nXOb0DMA_U152wjWcKYqzWBmIwjzuFCTlMihKkB7PouR59Q9REghzKHAVFQ66H0lK9NhHdteyIoRkdcovhWEpOmGQ55-7KjAV2OC9fLTMTRlkwV5yqP6oFxkc-uBbzl8sRrZsYtzdXzXk6z1_o_2_xvP79VGqlWjE_vI27sOQRZB7bo9NXoghq3kWgp1gwd4GjCzcrHDbNVS0v1bxQr5TXV4rPWZf0eNsu41TTCOoRpv29kk3MPsNmUc4-yoIWnW5YSGS-dmerPZQa9TX0deSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=HRx8TiqGYEURQBcgNmyqL89LXArfVnBrE_jHi5kWFdaJSXcbWi1TSGoMXuCkLm1nXOb0DMA_U152wjWcKYqzWBmIwjzuFCTlMihKkB7PouR59Q9REghzKHAVFQ66H0lK9NhHdteyIoRkdcovhWEpOmGQ55-7KjAV2OC9fLTMTRlkwV5yqP6oFxkc-uBbzl8sRrZsYtzdXzXk6z1_o_2_xvP79VGqlWjE_vI27sOQRZB7bo9NXoghq3kWgp1gwd4GjCzcrHDbNVS0v1bxQr5TXV4rPWZf0eNsu41TTCOoRpv29kk3MPsNmUc4-yoIWnW5YSGS-dmerPZQa9TX0deSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vC7QVLpRpWGg3nXuXFcwLNQDUYSAuE0YZrRJ2PPPDqL8ci5MnIjjGTRUpZ3S8csDauypaKLY-RSDEyfWCZBx8NjuSN9RrzLSqUsX74lI3h8u78vjUJ_XFQKR42KMYa_9IuONn7cjnBxV5NYzX_qe_acMvazVHUYH20lyS1YO-y3DOiidfpqp-Ow8dqq-9qC53Ji06lKPxwFYz6gWKCMvIkpGNMbSDOl-cG7ichVthcQp62NBZdOTqirW6GV1i6cD_soH8vP5fzldV-qb41p1RQSJxICDQwLWcwhApsMIBZXCEiKYls2Splkrkq4S0w38Oege-TSOumLrzfMuSUTMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfcUwGj3w6Xv-G5akXC_HeFHs9dqV4Ue7AedsWY2wVMNmDSWMecTOLjPlCtCGF0KKZBJoGTICCvG8_Ts-rg9lLbNR7FAMg1NE140Wg8XfC-bG1tVzxVvHNXkto4-TkZ90zxPTyfb7TWORx0_1EgagP8XhXVaKYk8uoQufPcmOPE_aEf6CeOCtuXnP63D1bcGXmnwLF0_FKHuKK9uEdGNE3ueX1HAkeOD85cpa8nH-dY1t36IMJVp4i6wtM9efBAK0eBHvPNf9hah01ZbEh9dsSV91Y2XyJZPnzrcbzW71C8iLsXKtl1oIQy8wcTayg6le1UVG8uPrF77MHl3BUaUfg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=gRrutFOIsbt-X7c7ooWyEU4mHECWxmKpCSUjY5IRDHEkJ-bJIBuziBalJkPUSt4MBOFYkvdH1cTZFv_GT593oMzpfBJPoVU3QU3mtszjpoFoaEXlTj1elZDi0inKqZXNuaeh7rdJW9i5YGQpBcm_umldLts0qLASggnvaXFH3unQIHnDHyxxzkxrb3h1mL9XlU3Lr0V2B0-lWM3grhMdu-lykCVORV28Yj0T9a8ngWUBU3unyNUKU5EJGwtccSGxdpANPbY0DACmQAehdmHj-7AuWn3MOg7xEDNyHtfYwQmaonCRJqH63XGYvW89gmY4ihWNYywZhon6_1vZevlelHuzcP3UNv4QDiHuG3StiB2mI1dSwotI_UVnQqX-_fMOMchcbIBkGeiRrvYsAwP3riYR4HsaunqsmfVWWjJG6AZfT1c0lVhKcUNx8ju7gqe7GlPAPLoWngvSTRbAjOIapKUrMFXhXCdun-0_iWfiecizDbSM9Z_jz8ejZoEap79wKOyRTynJnHjKMnsSBuVCydUSy8SfknvOVelf8UQSirVDuxrhJa-N1X7TMO8k4hHaY2mDetyc_sPkkAENN5odSzOE3adS_DHFH-N1QCfEaHd3i5SCy2qes1-RTyfGfa0Uuzy9gLantXllGoHC_Gxcp6Uebg6X7c-MakrAv87AWfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=gRrutFOIsbt-X7c7ooWyEU4mHECWxmKpCSUjY5IRDHEkJ-bJIBuziBalJkPUSt4MBOFYkvdH1cTZFv_GT593oMzpfBJPoVU3QU3mtszjpoFoaEXlTj1elZDi0inKqZXNuaeh7rdJW9i5YGQpBcm_umldLts0qLASggnvaXFH3unQIHnDHyxxzkxrb3h1mL9XlU3Lr0V2B0-lWM3grhMdu-lykCVORV28Yj0T9a8ngWUBU3unyNUKU5EJGwtccSGxdpANPbY0DACmQAehdmHj-7AuWn3MOg7xEDNyHtfYwQmaonCRJqH63XGYvW89gmY4ihWNYywZhon6_1vZevlelHuzcP3UNv4QDiHuG3StiB2mI1dSwotI_UVnQqX-_fMOMchcbIBkGeiRrvYsAwP3riYR4HsaunqsmfVWWjJG6AZfT1c0lVhKcUNx8ju7gqe7GlPAPLoWngvSTRbAjOIapKUrMFXhXCdun-0_iWfiecizDbSM9Z_jz8ejZoEap79wKOyRTynJnHjKMnsSBuVCydUSy8SfknvOVelf8UQSirVDuxrhJa-N1X7TMO8k4hHaY2mDetyc_sPkkAENN5odSzOE3adS_DHFH-N1QCfEaHd3i5SCy2qes1-RTyfGfa0Uuzy9gLantXllGoHC_Gxcp6Uebg6X7c-MakrAv87AWfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubU2qlKXKuPzC8NxfveXMTlxgQzZ_AnEhXryvy2nw82DjjM4DqxyRNd5thbyVL_wniqzP2L8b_Eoa7xqfchzVkMcFL_77PiZ6M4qsPES-lEgm19Je0r7AlnbHEfCrZ2SEOx9e4Nl1cgKNE9ptJzCMOCPJLEDJ6ga_crTAvkfnfYHVoLbeCVVunK0jXdOMhROn5o9Nh7Sevpk7a9OFdzsdDWcGXNQrMaW35dWud5CJQOQubfgRNseVVIDukSzEKrBnrXUt0FfWLkRImSZLA_g6db3tKb0fwC3YWmGJXmebWjsYdwiz789Qv1qE7I1smsslIr3Rog5XySRI4MlgqRQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELa0G_oB5GILfUNdrtbsgCgfANMp3axLKq3EKOPe7fhgaDwYa_WYkS_FqjqJFmfuKj0Z6iuG_GVDwMJ5pjHtEacxw6PhJvo70nX0nHS9fM53YN-pvEfL_pRWsh27hxPE5WLRmiWQ_a7lq9NgHs46YsLzCLFNGMcD2ikhWznvYi2NOwgWTCbo3J6NUlSCMCJahvEaJFpZkd9DoX0QawsSeqeEyC4gNwg44LVwewDfDXSrTWPviFm1eCRcJc4fYV8gKeuszWz_ycVwWsdEiECrVdLYZ9QH9I7_NChIybmYNbHe65pzcn1do-139DGmeiaWcVJSW30LuM_wv8qLnLu_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmD7EIznRk_aJN849y0aPAbDfTisZmrsl-aBszXJfdA9C3neEyrJodtjpu_zZMk6RU11xqUWUxy8RoHKp-apyHOcGgxpOaZiFEIZ7b5G20IAtGGUQFuDtS9U1mGo023uXJSVEDFhXh1WW2XHKPgHZUn99uwORDfrlsZ3gZvguMWW_hUQr1B6EmycMYBrQDJcX-h324IGD9Ifg4UCleaARdyWJjj7b3SrfZ8QOcZ-7A-pKEISJdurgu8XjxKiL49NraQJC04Idjaqhfw3VNY5vT86clu1SP4_u9LGxIXmO_vyfB8viiGe5r4d_BEeNeKNVLoqOiwhix7mW6OEgFj19w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkGZUu1re_B2Wusy64oiB54WATnzLiSM_nqRD8hOYi9v8Umz_jnFJiLN72oqkmO1AcfiTWrHSvKbrB-K649qBBeoZAqoSgtFOUgRXGNl0PDXEUFGf6tTjHT32WJZj9bpOCzPQKSqKBY14pBEbkqm9Kr6LHtBc8vWpTtSn1O1WVg5mpy_llcnV2ZZlAndnqSMGXKLztKI_M_eZxaTAfML3LfqrHsMAUgfutOcVdQet6DKX_rWwZC2YBM854hhqWWEMaqbgPD9yYPC1buhlariLiky-QRMy-SFVkU0Vr-LnT-Gcv6YnR-1XjnsRnchxwoktY4KlO3r1A9tQAS67n8lew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=eQ6ayJhp5MpP4sIdNOcNftPVAR34G1F9LQTdbNQCdNaEXWUoNLcyEQBfYsKEyxANoxM2RDtaCvjv7JXOo-p386EdL38d3NYXfFCM-zN19Z8vvY2aMJHXb4LBU8GRo1r3C41usKiGpv7hBVNo1USTkpTlmXwK4OGWwyC1qVRvA4wV5V9iA7mKqv8yvMxv6jtTJi2H8o3yQJTu7Jc88tIKqOQ6avF6Xp-2z7fZ41sqBFnJ0aQhmb-bFa3BPPpSH8uki5s9xdJnw0cNyp2eqp8dLLV-B2qhl8xGiniw0dnXHBx3CmytDl3iyQBpK4TfHghjrzlAaZD0hFshayRKOB1yrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=eQ6ayJhp5MpP4sIdNOcNftPVAR34G1F9LQTdbNQCdNaEXWUoNLcyEQBfYsKEyxANoxM2RDtaCvjv7JXOo-p386EdL38d3NYXfFCM-zN19Z8vvY2aMJHXb4LBU8GRo1r3C41usKiGpv7hBVNo1USTkpTlmXwK4OGWwyC1qVRvA4wV5V9iA7mKqv8yvMxv6jtTJi2H8o3yQJTu7Jc88tIKqOQ6avF6Xp-2z7fZ41sqBFnJ0aQhmb-bFa3BPPpSH8uki5s9xdJnw0cNyp2eqp8dLLV-B2qhl8xGiniw0dnXHBx3CmytDl3iyQBpK4TfHghjrzlAaZD0hFshayRKOB1yrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=izDodW92NJnaQVGOwjd2lnybgLK1wuebINtWimhSAWovgZulgL2AzjK8VjZJJkqFItuOzU-7Ap9dAiejJVEjt5oHv4tEa33F5RkHjfCTHqEyvQXNqJ6KgWvYgP7ajm12z5baMemi_uzvcKWU3_9el4ihJDPHyY-zvZOPxHOf_hUO1QS6WHg-RHfI2fEz1qETcjd8vNKazHan6rcPo_ctDzgT-yqFa8z25U4wE8K7HTykYiWbX9hmAul_yDnotLMw8Xq42bnpI--FfOv7a3zIEsy-VAwsGQmY1MP6z8k-G9djSq7d1xgHlpq414kHRfm0BVkTFriVAf-f9SIVWxSZJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=izDodW92NJnaQVGOwjd2lnybgLK1wuebINtWimhSAWovgZulgL2AzjK8VjZJJkqFItuOzU-7Ap9dAiejJVEjt5oHv4tEa33F5RkHjfCTHqEyvQXNqJ6KgWvYgP7ajm12z5baMemi_uzvcKWU3_9el4ihJDPHyY-zvZOPxHOf_hUO1QS6WHg-RHfI2fEz1qETcjd8vNKazHan6rcPo_ctDzgT-yqFa8z25U4wE8K7HTykYiWbX9hmAul_yDnotLMw8Xq42bnpI--FfOv7a3zIEsy-VAwsGQmY1MP6z8k-G9djSq7d1xgHlpq414kHRfm0BVkTFriVAf-f9SIVWxSZJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwtEP55r-_0FLkGUjeLtnusiqm6vZRMCWvOvFrikov1Eug3koSNXOvCz32yle61tp75oH0Pzeiw1VVRwEkBqcsIxlo0rpDTKnuo4r7ksV5otMSo3qgtixZqnLFAmEj7g-TJkrclI_hATSQ1a8eXeP0p4Gc2sMpR-lECjeKWjWFz906mjxKU9XWIzQf5z2_jjSbQfUjt2e93ZL9XLAxUTRkFnch_fSLAW_bDS5k3Yv2bmcJUIZnwPnWMtnN_GBd1NXl9TIxuOECnH1pfmIfkLFl0WQDpSfLISeK-3qyBY6SZOFTemZqwuQhQdgcdaOMw73crFkfFIGoyeiHlzKQK-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=BHu26XvuCqCI7UzpYzZsiLL55XDjjOLZS-pV6I8ibQBwKNxku2WrMEIOyw4ycI4fZ5l9bC9uWomvGaKKibtAhCbxu2DaETX5F_e2OXeD34Q8K0uMlaqcqVN4lf5jAEKuInLeDsC9Ys_PXD4nA0FKsg-SGVgxuBllzaJ1eV03Dqw844Jz1nMcLEB_5W3Pjy_zukqjhesZDr4MxYFyAdvr7Q3X2MveHoFpHAjI4g4Bgivzt8uUl9kSjlhkjHMEF_uQjXgwDEJYMJIDBs7CNuLVoY36dFzjdrErfQ7AalJTy7qrIatU208j043cHVrwrbrvOx8POwYIxvyW1NLBwJ70ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=BHu26XvuCqCI7UzpYzZsiLL55XDjjOLZS-pV6I8ibQBwKNxku2WrMEIOyw4ycI4fZ5l9bC9uWomvGaKKibtAhCbxu2DaETX5F_e2OXeD34Q8K0uMlaqcqVN4lf5jAEKuInLeDsC9Ys_PXD4nA0FKsg-SGVgxuBllzaJ1eV03Dqw844Jz1nMcLEB_5W3Pjy_zukqjhesZDr4MxYFyAdvr7Q3X2MveHoFpHAjI4g4Bgivzt8uUl9kSjlhkjHMEF_uQjXgwDEJYMJIDBs7CNuLVoY36dFzjdrErfQ7AalJTy7qrIatU208j043cHVrwrbrvOx8POwYIxvyW1NLBwJ70ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=iyDg2z-KcwFOOs3vLjvpdqzakKPz-tnW-Vl0h3uEV8Qzuf9skmUbZ-GbvOeUXPydFEmzNgSkdcFK3zx0IDJ3TLbCatcoDKWaeoAJisYY9lyH9v2bdLyrHFS6HiyGJJjaq2F_9BC89F949sVlLZx7jFCntTJroeeIzQUqMdfYcTgT7KU-GpQScjfDJIm9kwsQK9H1B8zqpA5_Xz9GepLE-KHKG2njRirjWIHoBdv4r5fHStJN-MuSquiUGpL96zVMiEBpbPU2_NMPeumu8Mc7cO1Gim-sRKOqiM9s2kAj2ybl9cfJ6JWjzs5eICVNzy26UOdCRbYqS1xY1oGKfLk1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=iyDg2z-KcwFOOs3vLjvpdqzakKPz-tnW-Vl0h3uEV8Qzuf9skmUbZ-GbvOeUXPydFEmzNgSkdcFK3zx0IDJ3TLbCatcoDKWaeoAJisYY9lyH9v2bdLyrHFS6HiyGJJjaq2F_9BC89F949sVlLZx7jFCntTJroeeIzQUqMdfYcTgT7KU-GpQScjfDJIm9kwsQK9H1B8zqpA5_Xz9GepLE-KHKG2njRirjWIHoBdv4r5fHStJN-MuSquiUGpL96zVMiEBpbPU2_NMPeumu8Mc7cO1Gim-sRKOqiM9s2kAj2ybl9cfJ6JWjzs5eICVNzy26UOdCRbYqS1xY1oGKfLk1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=II_aK2M51SKB6vw6wvpe78KrnmIqFJGmwmXXBsVkotln5rM2aepVkp0kMizh2ieOSjLUR4cnZmByZI6fOGPcebTNgUvOGFYnSrL1032iPu0yfamEeAiY3W26b-M8rTKteZIczYE_2a6aNGCbtlJhz7s7sxmRyNkV0IUxFwKCQAY4kjGbvqLsLAD0IQ42EeEQ6LcM5-LiqpbLDaRgvMO3aBmY_VMw3jx6lCUlUt55HCymchyCaJj15JYhq2DTMPQJgb48DsLIQV_5bF3n3LbkkC7D0-F5A_q0idIbxFctsuX69VU-_aLyoHGAlHqCRajMUI03zzhkNx7aiNt9_kDurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=II_aK2M51SKB6vw6wvpe78KrnmIqFJGmwmXXBsVkotln5rM2aepVkp0kMizh2ieOSjLUR4cnZmByZI6fOGPcebTNgUvOGFYnSrL1032iPu0yfamEeAiY3W26b-M8rTKteZIczYE_2a6aNGCbtlJhz7s7sxmRyNkV0IUxFwKCQAY4kjGbvqLsLAD0IQ42EeEQ6LcM5-LiqpbLDaRgvMO3aBmY_VMw3jx6lCUlUt55HCymchyCaJj15JYhq2DTMPQJgb48DsLIQV_5bF3n3LbkkC7D0-F5A_q0idIbxFctsuX69VU-_aLyoHGAlHqCRajMUI03zzhkNx7aiNt9_kDurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=kCP1zjg0OeKCyHPSJk5FW6MlPU--_ZYJEY9c3gUKwXHYGOBC2FUz2_AGXEix0wd46bCq9_Ov8wb9wbS1OLLuQ4oqBBjdJJ4xUR8kZ1jy-INLUzkNyfG0GCA1ag4jw2D0EdYkDNUUQtnoJAIs-7Y4kS-8Ys3g9YIRBqu8rtOdpIsDZzrzdWiZjFgR92aCyDZ79-H3PFKK2gbFClA8Z-i3R4AvRDYVVDHQwTCAkYhV-akHvrr-xD3Esp6_U6-fEJ1qiKB_ECqd2cr0rAmNyykJ_lhRYrep9zBkhnSqNQOW8lyQP9L7Jfz3dvoQ_DjNtWxczTOrvOQ5Qwj9ToHPeebV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=kCP1zjg0OeKCyHPSJk5FW6MlPU--_ZYJEY9c3gUKwXHYGOBC2FUz2_AGXEix0wd46bCq9_Ov8wb9wbS1OLLuQ4oqBBjdJJ4xUR8kZ1jy-INLUzkNyfG0GCA1ag4jw2D0EdYkDNUUQtnoJAIs-7Y4kS-8Ys3g9YIRBqu8rtOdpIsDZzrzdWiZjFgR92aCyDZ79-H3PFKK2gbFClA8Z-i3R4AvRDYVVDHQwTCAkYhV-akHvrr-xD3Esp6_U6-fEJ1qiKB_ECqd2cr0rAmNyykJ_lhRYrep9zBkhnSqNQOW8lyQP9L7Jfz3dvoQ_DjNtWxczTOrvOQ5Qwj9ToHPeebV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3ihVRV7NOhYCYvsn-VQ-eEr-N8UWYjIAOoo1QwaG36mea4QKY7pdVx3yiATDZwdbXPobCOSIVqNoWeCKmJSAHafzQurYNczit0wBPvGBLnMUMSUt-P988jz5gttm9MRv8h-_4VDa2GP0LNVH4jMVM_zcnYnCCab7SKm-bZTineAqqDXMLuLBBQMR9LAxYq4XFzZYn7GszwvUEtGj4MjKzkLsAVcQJOV1rA_A7nlUiYLp6ecYPPqHO_IR3H-p6_IbmAZum0SoB3K9Y8jtf-_87cZm0mtQ-81hLKr3JXJCqObD6HB5G1q9zl9crhES5CUKu7un1FJQG1bxpTZudgdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYAkNuFuoEyCi7po5N7A4B22H11MATVXzJLs0aw_ELdcz6KVtb9g6ULf9Q97suC1etaAKJS7zjkhORT84H6VZkQxJ-wZKbbcwGkDext2vmO65HTXLO3yx7FTtMDio59MBhnRDTuaf9hogk6sRt_trJ39_mg2xZD-BwlEhMqZw4KU1cy1ykoidKlzI5bX8yt58VQBI30sE5ApplZ3g08SoCj_nqUvWrxa3wZKZMXm152ONJaqBOlaqhJpaSal8AttjVmoMJUvAnWX3OcU3qDjTALZhyfJzvElBgRez4ERGusdxvziXuLi_X8ld83lxawxtcKxTahyeKTAt7cVmKsEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=tnfbBj16I2TNkg2kdn714vkFP9wlv5X0crYxahCvI2DvE9D6Td9C8oiDdL4KUQSyD89WMlsLB5ZxAWpMHh0cWeuaXWzGVs9ogjD1jvUvWhXSfUXot4NMx-p11YzMWfC89RUGH9BFurgKOuVLOug7BTNjnA1yAqwmTbTsB5OmkUE0SYivlavzNByqYXZQwEHxXfNvVMOHVLjRjwHcj4BBXrR-rlPkIc5AAT0oKPa1d2avT6_wbK8C1c54R1iNZuicczplsLVdk1Aug5kSnVSeqKbl2XtDrcHkai71YBXVvJlhO0_nTQ11X26g_kRsvEpkESYSL86qOY0cFW3QJyKEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=tnfbBj16I2TNkg2kdn714vkFP9wlv5X0crYxahCvI2DvE9D6Td9C8oiDdL4KUQSyD89WMlsLB5ZxAWpMHh0cWeuaXWzGVs9ogjD1jvUvWhXSfUXot4NMx-p11YzMWfC89RUGH9BFurgKOuVLOug7BTNjnA1yAqwmTbTsB5OmkUE0SYivlavzNByqYXZQwEHxXfNvVMOHVLjRjwHcj4BBXrR-rlPkIc5AAT0oKPa1d2avT6_wbK8C1c54R1iNZuicczplsLVdk1Aug5kSnVSeqKbl2XtDrcHkai71YBXVvJlhO0_nTQ11X26g_kRsvEpkESYSL86qOY0cFW3QJyKEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TgVeUgYjNjBcxHIwPRLXqirPakm0SlD2QqGYT3Pm01kOPLsSIVVDYqj08w6gZk6NhyzMWIuMmeJsvUjnUatMbXrIQ0oLAqEhNkLN7A5rybQCGhSq1FDGWMVeDfoh8MargDTpesB5wJqkbeWqKox0tWyY-cCtI9dRiw66P2a8hjrwYJJKjXDpoCRd_LDd2cTUyHZd3vESXlQrAGORFY2J9wIaV4CCeL4Fx7qG1P7TdUCVAkdzHQ6TAYY4N-CiubqyZIEG8rHtGGvn0pxa6P7Beg8xSlzEq9E6vcMGtzlaMylXl3XlHzru_aeIQ5fVa3YZlfza-WnNtjriv8EZLQpS9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TgVeUgYjNjBcxHIwPRLXqirPakm0SlD2QqGYT3Pm01kOPLsSIVVDYqj08w6gZk6NhyzMWIuMmeJsvUjnUatMbXrIQ0oLAqEhNkLN7A5rybQCGhSq1FDGWMVeDfoh8MargDTpesB5wJqkbeWqKox0tWyY-cCtI9dRiw66P2a8hjrwYJJKjXDpoCRd_LDd2cTUyHZd3vESXlQrAGORFY2J9wIaV4CCeL4Fx7qG1P7TdUCVAkdzHQ6TAYY4N-CiubqyZIEG8rHtGGvn0pxa6P7Beg8xSlzEq9E6vcMGtzlaMylXl3XlHzru_aeIQ5fVa3YZlfza-WnNtjriv8EZLQpS9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=sDZWFNxSqhhYUWwJpmLc-XYpDDPIBeMP5S89nRO1KIkTXm4J_-qkaQ1LaogLSD6zQL_p6qGbjSilc8XxE_Nc0ftg9309aiNcIuvGgRr4Etx9ftLpHhX-087dTJwwl8UWdc5snSu6lFfsn6_46qASotJVM5VBOX1O5A1ufzQzyotnF-F33p270E3E1tdA99I5YmWEebkaUHncteuDrkfPivz5f3_UrVVWtfMpzcIl6vs2RaeG3AjZm0hxcCmKFGF_XHEvLEGoq1aFD8zf2nFYRXY486sH2ytTx3ZVSUSKi-qwOboi1SoEBZ2atZMUfFYB83fln6nf-LEj7_lqZUzBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=sDZWFNxSqhhYUWwJpmLc-XYpDDPIBeMP5S89nRO1KIkTXm4J_-qkaQ1LaogLSD6zQL_p6qGbjSilc8XxE_Nc0ftg9309aiNcIuvGgRr4Etx9ftLpHhX-087dTJwwl8UWdc5snSu6lFfsn6_46qASotJVM5VBOX1O5A1ufzQzyotnF-F33p270E3E1tdA99I5YmWEebkaUHncteuDrkfPivz5f3_UrVVWtfMpzcIl6vs2RaeG3AjZm0hxcCmKFGF_XHEvLEGoq1aFD8zf2nFYRXY486sH2ytTx3ZVSUSKi-qwOboi1SoEBZ2atZMUfFYB83fln6nf-LEj7_lqZUzBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqNZarHirL4fVUTPwcmoVA2jLZ1UVhMrWDBgTV0wFbPjVdbvoTSG1Z74071-nxk97UX-fHfmliju9X-jqlU9lGUWdOuXAyFEbXXCSY54bo2kDtu0xtgdXGwwT6vssb0CLvUrrv_2NXMgBKvyDUfkc2gUUjGSxhgLxMOHmM2IzwSAHY1VUO71Bu0PJnBl8juDe9Gh6dHcI5UVltVmgTDUgtRbCTXCwFZLZ2iH3ZnITUARe6A4sqbgBdlnLBvRrqTJXH11ix8H3lnA-Ea-UXVoNqzEWemlnJVGGj1Sx6047LAqZ62c5MYdxir03c6XAFPfxwIQYHFPTbqM4oA1VzPatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=rNqQHaz1oobVrMWXGy2OwWfd8V7FZHAOb9UNJuxIDWiA3qYYh-Frv64zbbejJrie3vY8wqXQk6KvM8URpLc_3bIR0mKCNwQ5JxKE_cAKsZlMsOqNZ16MhrgMvC0znRWiAzS1L1EaxUVHMoA00xXaL4u2xOZ_gTz455P7SIbhI_Qyx2RxGxuNy-bUguSBu_zjKJt7nXmrj4BDMwuYXYkp1IMXDiD3VuVUBtsCz1wEvEVZONyb1WYLuj70e6l1lzbDe-qNRcaQLT1Cc1s5miduIFq12V7VIdFfZ1A14Cn-J5ADDSgPP9EuAFggtUvbNizHOXba6UN--CUqkTFq8JPm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=rNqQHaz1oobVrMWXGy2OwWfd8V7FZHAOb9UNJuxIDWiA3qYYh-Frv64zbbejJrie3vY8wqXQk6KvM8URpLc_3bIR0mKCNwQ5JxKE_cAKsZlMsOqNZ16MhrgMvC0znRWiAzS1L1EaxUVHMoA00xXaL4u2xOZ_gTz455P7SIbhI_Qyx2RxGxuNy-bUguSBu_zjKJt7nXmrj4BDMwuYXYkp1IMXDiD3VuVUBtsCz1wEvEVZONyb1WYLuj70e6l1lzbDe-qNRcaQLT1Cc1s5miduIFq12V7VIdFfZ1A14Cn-J5ADDSgPP9EuAFggtUvbNizHOXba6UN--CUqkTFq8JPm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=vH0qSMBRXUdvFmw0CoKUdB1qh-nnXWfXyJUm-rspaalpguZgyav_e9IZu5qnjvHmM-mPXeaIoIp1c_1OXV3YGY9W45eryjqqR6inbHqNWP3ODm7etcnEuuZ9Wfmz1w45X7ejjnkL_gaRC1h3nXRx2EH9wli10kh-Mbgl3zxcpPp0ubn8ePfrOq2EI5CKjPk1sk55L28H_dE-f7DDqAT1MfTKP1KuML_8ip7v6pgFVmUj9fKFeswM6kS7jOe5L_NUOcgAMhASVrMY1vFgM02unXVZrNXk01us6XaA7-_2GUREEFNmyPLP_vrHM0wAfDAguDDUmB6raxrb1A8pCQoayg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=vH0qSMBRXUdvFmw0CoKUdB1qh-nnXWfXyJUm-rspaalpguZgyav_e9IZu5qnjvHmM-mPXeaIoIp1c_1OXV3YGY9W45eryjqqR6inbHqNWP3ODm7etcnEuuZ9Wfmz1w45X7ejjnkL_gaRC1h3nXRx2EH9wli10kh-Mbgl3zxcpPp0ubn8ePfrOq2EI5CKjPk1sk55L28H_dE-f7DDqAT1MfTKP1KuML_8ip7v6pgFVmUj9fKFeswM6kS7jOe5L_NUOcgAMhASVrMY1vFgM02unXVZrNXk01us6XaA7-_2GUREEFNmyPLP_vrHM0wAfDAguDDUmB6raxrb1A8pCQoayg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=sU0Z8Fu_2FjTLZ-ocqAw8Q-s3CRUCtNzaNMtT-3wVGFp2MpqiulkL_z75s8o8hNlVAM0SuLYkWtKO3RhbLGMS2MaOq-Pb1kXVO0KyFihiCVWMrdVzSbEvQKUR9RmIq94IyDqt0COYNU4DbC-JaLpC2LC3h2gn4FHxdnk8OGXqYtJS0_YLNRUnyVP7JnAwFAShw2gg5yAKbnQrsFXyyvkTkeFFYHSuBUFE-_nCvzqdPQRszpL9BY89DpOdoSSji6i9eElcM-aKp8_bRiF20HLFPXJ-Ci4N9SllGB2tnxQvoxbOgSwRLU8ZPaq5uC5kGreNAqtOBV-aqn5AXQ70xNzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=sU0Z8Fu_2FjTLZ-ocqAw8Q-s3CRUCtNzaNMtT-3wVGFp2MpqiulkL_z75s8o8hNlVAM0SuLYkWtKO3RhbLGMS2MaOq-Pb1kXVO0KyFihiCVWMrdVzSbEvQKUR9RmIq94IyDqt0COYNU4DbC-JaLpC2LC3h2gn4FHxdnk8OGXqYtJS0_YLNRUnyVP7JnAwFAShw2gg5yAKbnQrsFXyyvkTkeFFYHSuBUFE-_nCvzqdPQRszpL9BY89DpOdoSSji6i9eElcM-aKp8_bRiF20HLFPXJ-Ci4N9SllGB2tnxQvoxbOgSwRLU8ZPaq5uC5kGreNAqtOBV-aqn5AXQ70xNzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=iTyqjAPZI0N77u3gef3MXTEmimSdPx5FvU_w2LFm8REwgpOBHcceS-G1jSXSgrS7KP8oBSAJyrxepUMPu5RkpBaOkB3H2-_ZgKZxL47cTio0kmHxhac_Nv2_Afj68BX6d_Lv1BfjoAPMr5WN7lHEzjP3hEYo2Rq5AldxBP2dHoEKn8et83d_KK9SdUKuXRhzss0PqfhoW4NA1pECYzSKt_Oo99DoM3xjpCFAIh2oEMvaJlZXNNoETsYiTr2v3JTf0JfHj-jY7Xienx4WAiRiPISGiyvz3fyzZ8Iiv3l_SkXZyj4SoaRraN9l2YCOSlb2jkl92BsPc14uvaBNotpalw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=iTyqjAPZI0N77u3gef3MXTEmimSdPx5FvU_w2LFm8REwgpOBHcceS-G1jSXSgrS7KP8oBSAJyrxepUMPu5RkpBaOkB3H2-_ZgKZxL47cTio0kmHxhac_Nv2_Afj68BX6d_Lv1BfjoAPMr5WN7lHEzjP3hEYo2Rq5AldxBP2dHoEKn8et83d_KK9SdUKuXRhzss0PqfhoW4NA1pECYzSKt_Oo99DoM3xjpCFAIh2oEMvaJlZXNNoETsYiTr2v3JTf0JfHj-jY7Xienx4WAiRiPISGiyvz3fyzZ8Iiv3l_SkXZyj4SoaRraN9l2YCOSlb2jkl92BsPc14uvaBNotpalw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH5TtpCnfH6E-E4EcvDbb-U1DQSGg8O-Xsz5498Fg0aLB18GNnmCG99KO1w_m5klgoZ2HErvsrjI3dau_AoPsd5TyZL2K99m3e0wfAGIklVlIG7Mrk-Fr-H-wPJspCSRcs0KXkZSNZDgz_tsreXGEIrORxXb91IjnVMzRmoDe_PF7OKdD4OcQtiXFfYyMslZVH3qCW18TvrfHApUMN3sAySnoVeECvOLB-7kl1qpKL3qS5GkfwROTHRH77wcGNhStwMYdIRjM7-cm5Z-Gf_viDGqn9kIBHJWrbkehKMUImGjxvNmzzswyS-MvquOAng8I58zPGe6nON4QTqXrga4jw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=vf4RI42sx2ylCe3O6lECP0VcJlP_u8EeIIrQkZA1g1xXC5sb5WGY2JY09XK6_A9guJkYLegQHA9wD4yocP_TwGffPsmEm-JRa3tqB88dR1BzPpeq6PAb5NLO9r5VWWLkPeRh5FCT_t1NB8gma6LZDbqiF3jEi6KNzL-nJqfPKQ3KNGzkMW9_1CkJKcDVhSLq7cDjkxL_4RpQal5wpU_IFFZLt74YMdap5ODc-9FnwP0_xnwssqQ_He-TSHkVXrgtgEz6790IEoF-a_IafKPpWGgziewuG9GifPXnmYiTwU_gBimgHb88R3yNihfKsljB-d96HYx54rlGngrGqKmvRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=vf4RI42sx2ylCe3O6lECP0VcJlP_u8EeIIrQkZA1g1xXC5sb5WGY2JY09XK6_A9guJkYLegQHA9wD4yocP_TwGffPsmEm-JRa3tqB88dR1BzPpeq6PAb5NLO9r5VWWLkPeRh5FCT_t1NB8gma6LZDbqiF3jEi6KNzL-nJqfPKQ3KNGzkMW9_1CkJKcDVhSLq7cDjkxL_4RpQal5wpU_IFFZLt74YMdap5ODc-9FnwP0_xnwssqQ_He-TSHkVXrgtgEz6790IEoF-a_IafKPpWGgziewuG9GifPXnmYiTwU_gBimgHb88R3yNihfKsljB-d96HYx54rlGngrGqKmvRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=NJP9dbgb5ee0yr3uCwNsS-reW7DznfM_XKTVKsP_FO3me2oGAwdKFxkh0j23cDKyzLelRleTUf2W_3JJtxvJrXclpiYI1PDVqH9Xcsr3rHAMteLmEQVVsV6bWg3KTNWWz1zZQauayRCeX99HbggZSaidT1wSSAYcKOKYbmXefqiwLIYcteZlCe44NvFF2v9c0RP2zJd7KwX-zK_8ND4UYuhA9zjGHi5sYL-I4U6tD-opMO_YnCOV0RLlcIPgN74glvjF7ZGzRcSQkLVZ2FL6LFy5zK-dBa4_SH2kwPB-Xz1_Ijyr_NXIXaZ1HGPRTTVdWQHyoaH8CV4jmjlipGNNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=NJP9dbgb5ee0yr3uCwNsS-reW7DznfM_XKTVKsP_FO3me2oGAwdKFxkh0j23cDKyzLelRleTUf2W_3JJtxvJrXclpiYI1PDVqH9Xcsr3rHAMteLmEQVVsV6bWg3KTNWWz1zZQauayRCeX99HbggZSaidT1wSSAYcKOKYbmXefqiwLIYcteZlCe44NvFF2v9c0RP2zJd7KwX-zK_8ND4UYuhA9zjGHi5sYL-I4U6tD-opMO_YnCOV0RLlcIPgN74glvjF7ZGzRcSQkLVZ2FL6LFy5zK-dBa4_SH2kwPB-Xz1_Ijyr_NXIXaZ1HGPRTTVdWQHyoaH8CV4jmjlipGNNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/couipev4n9sg0zj8prRD5qFmMdSd2jBNDMvfbCdnhP0DJGo-nM9aNJ8FVi3Ge3mok3FBx3leYsQp81yVVzUyJ1yGaG9UuK-RMUKIuxhSRYidNblL_CoaCuppgx8TkWUhqLAGmp7uuBYuhiOS0PJdwpKswDXDpqEuoDamUG0tsW1xLL7NB44EMO0nbBoxfO94t3dtxJVV3COaT6-3WrjI66kDXYV006qcOhJ1iHVA_K6lLmg8882Bqf1or3Ffq5yUIcozEzdIDFoQ2mldaZAmVbHYtF9I77p5fG_DsSuDgkZ4g_wyZOwkgkZMSBONNuEHRjzlDsXG_oJHGmtlzmoGKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=LCDg9ykEKz14GiRS1NXFwOoAn3tLxxDogHtHWqxaEGlJ0pRUcUqB66t5esiblNYDF56MuaT-evTu0Ae7wq_rmpVmoeUaBucsh0wP22FeKUeq1DWuEoxS04ZwFWtgH36YfKpJnIwfpxiCcYBcpf-xtfH6DajD4CK0HhVJ9Opi1a3Shw3wipPV4iH3XU4XlrU0t67ZIdCLE4wv7ZCCPm0pXgRQnsyf7i8wh5kwfsHKT3Go2S4VHbjSRuT-bBovj5JV8w0DleFCqOwvUTgDAMi1clJpS2JY3690wPT9LdmOYmdrBDpQgsOVlrnhZquQS-eiKh66x8TBi_NHreIVJCb4nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=LCDg9ykEKz14GiRS1NXFwOoAn3tLxxDogHtHWqxaEGlJ0pRUcUqB66t5esiblNYDF56MuaT-evTu0Ae7wq_rmpVmoeUaBucsh0wP22FeKUeq1DWuEoxS04ZwFWtgH36YfKpJnIwfpxiCcYBcpf-xtfH6DajD4CK0HhVJ9Opi1a3Shw3wipPV4iH3XU4XlrU0t67ZIdCLE4wv7ZCCPm0pXgRQnsyf7i8wh5kwfsHKT3Go2S4VHbjSRuT-bBovj5JV8w0DleFCqOwvUTgDAMi1clJpS2JY3690wPT9LdmOYmdrBDpQgsOVlrnhZquQS-eiKh66x8TBi_NHreIVJCb4nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Kd0KXSa5UCYXfr9vG7ikRrffC1iQJ1WhYrzv3T3Vwd6K3xeLcWseZjlVHQ2iti5GwMjWpEMxu2n8vptFu5OT38-8Ar4OD6AOFw8j9W9SkusdScz88NfvMuSayY7fwHCormYB1Js9TREZyBk7xEhgs_1h8fHCQCgSZ2aMZp3P8fb4GD0m9gjeznkBcmuNGO1bKjky1ycUesNWOUYFkl2D03Da_Bakt2Sc8y3wDz9MxsZFrodjM1e5-_kEval2AjmFaKzV4QjfiCg2UN1W_IR6kPM6vDNT4jFoclF7Ys_mhbm18jcdqoUhhozFj8BAOAj6jPqHISIELkv11bwTgTNcZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Kd0KXSa5UCYXfr9vG7ikRrffC1iQJ1WhYrzv3T3Vwd6K3xeLcWseZjlVHQ2iti5GwMjWpEMxu2n8vptFu5OT38-8Ar4OD6AOFw8j9W9SkusdScz88NfvMuSayY7fwHCormYB1Js9TREZyBk7xEhgs_1h8fHCQCgSZ2aMZp3P8fb4GD0m9gjeznkBcmuNGO1bKjky1ycUesNWOUYFkl2D03Da_Bakt2Sc8y3wDz9MxsZFrodjM1e5-_kEval2AjmFaKzV4QjfiCg2UN1W_IR6kPM6vDNT4jFoclF7Ys_mhbm18jcdqoUhhozFj8BAOAj6jPqHISIELkv11bwTgTNcZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIPmSS0Rb3cy1RgcTUNjByriv_ixCUMCsQ_pVq6C5kni-ojS7FoFkMwoDOqljpCynJjylBv0Ern4QrUcbGhoFk89Sy_t_jIrmoGmLCcoG95vprejNcA0kT_P_7IiokpcTx__7Q3PlMKnxxRx5wcf3OEuHxkiGPRL41gS32ZcgM2sRbvloIUkUMG00zGSmjjnFf3q5u5by-8ftP2_RczBZ1S4VH0SK4GG5mJz_Rba80yaZ8zFBpnmznvtz6JFe5Vt3PnozzKU25InYVDGYEx3wFOLpyZ77Dd4lxatdUidW9C1FLAAFMB2neLUU6bkFggR1jANvYhq7CRWDV9lwqdztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtBlAulc5oq18G69UfwoE5gr4ovqDs7vBFJ166d63cEUpLllMZF0oJ9t9DgeyhAqFrtU_TwMy0uVgUt09ce8NxkdHsZUNpyNRzvo3Tqte48o4wf7d3QaAmByF4Sy6zz_UMeyjDl8T3VRmr4hiic6WOloZU7n7qgqDNfhtyWhpQsxwRyiAMAeVZGdRvmlv8oEO3A-Ogx4YtbwTU3IornDVjCE7o4aIuHn4d2AYydIXZ5Eq9FK2W6QcpjSCwaVNAddNhtWdjnS6WfqxtUAodyQfWroXNR1n1xpmeisnWlxmJ78MXmlMAVW1Lnr5LkKYEFtd54QeDs6yVfmLa2y6Jofgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lerOB1yAHSwySU7k8zMbpjT0Js7wPtRApajy17YHgss8aBOurPqKm2QaT2aA8ac6l9KueaUKcTCzPGXFL8oIr3A8IVwYt-rF8Yc-8IfADUf7kpOGFg7uf0PVY1Rk3AK-ShlhLuRBXC0PkvHvR-Ic649LWu_gttt-Cf4lHbdnk92SZTERuZgr5c2xD7Yb71_FvNzfyIfizcsbsarLCWt6gkopDuEcGm_ZtnAw4AiCrx46xegCzeWU40u-pzKafiLGn9Xk6lqIJ75xXfOlvKsktdpLbuwgQBRHvky5MBBQOPxabzvrUiHx8jXDUZwCiU84qWNMYW70kiXFAfEXwhFdPw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=K1XZauJdnAmux59mDQQxfDjEvtR2QTocgUBSY76OvBa_zHpdO97UgR7wQuaeTn733Y7h3xD_sbPloYiL1ozBaSdWvnB8YOzP_j52_gJ1LymTksRLb6RJfP32rOgj4KSYajQTLNLbfrG9MMquxWebPmoB8V38ZY8EeSyAlVk4fE1_PiWSykhiiED7Hkw01hkQF264GtdlSJcrSwxAKGEiQG-r4fHHB8VEC3JKr9RtPMYv7yV0MryNg8KK2gpUYSl2X1KfqfCKNosJ71ySwjU4dYAvi1GYhXwFTY_0n5Iil8vt3JCUaWcszv50h-QLN1vPF7QK-zRPOIIy5J5M_Q6l5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=K1XZauJdnAmux59mDQQxfDjEvtR2QTocgUBSY76OvBa_zHpdO97UgR7wQuaeTn733Y7h3xD_sbPloYiL1ozBaSdWvnB8YOzP_j52_gJ1LymTksRLb6RJfP32rOgj4KSYajQTLNLbfrG9MMquxWebPmoB8V38ZY8EeSyAlVk4fE1_PiWSykhiiED7Hkw01hkQF264GtdlSJcrSwxAKGEiQG-r4fHHB8VEC3JKr9RtPMYv7yV0MryNg8KK2gpUYSl2X1KfqfCKNosJ71ySwjU4dYAvi1GYhXwFTY_0n5Iil8vt3JCUaWcszv50h-QLN1vPF7QK-zRPOIIy5J5M_Q6l5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZe-N2-NFkmdp3fY_AVb1Ay0w0c8lHU54WYavAWnJ3NOYQIygCZRgrwCOer-rqzjeEKNxIhxMglIymDRUA1cq0vvbUc8N2HjQMPvlJIFZ1Or4N-PwXHAPyacEOK5rRnM44_LZCxVWw0yzFmPkKxp-mY-qQVif1rHK4S99Zi770R7P_XR8ydCaHXIvH9dgFUhD9bPLd6Q1j_MOo8oMXMM-Rf2yKdaELDRMvu7P4WzGSaFI9Y00QE6rMEir1hm_VbKNZlScT-y1qIpyAgBE1ENDc9R12WtTGPXH3-D5GRV3a5SjHMEM5xcIEVg9LIBw6VM3BPzROSsDiJIQ2oMBH5TRL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZe-N2-NFkmdp3fY_AVb1Ay0w0c8lHU54WYavAWnJ3NOYQIygCZRgrwCOer-rqzjeEKNxIhxMglIymDRUA1cq0vvbUc8N2HjQMPvlJIFZ1Or4N-PwXHAPyacEOK5rRnM44_LZCxVWw0yzFmPkKxp-mY-qQVif1rHK4S99Zi770R7P_XR8ydCaHXIvH9dgFUhD9bPLd6Q1j_MOo8oMXMM-Rf2yKdaELDRMvu7P4WzGSaFI9Y00QE6rMEir1hm_VbKNZlScT-y1qIpyAgBE1ENDc9R12WtTGPXH3-D5GRV3a5SjHMEM5xcIEVg9LIBw6VM3BPzROSsDiJIQ2oMBH5TRL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=GVFR6KYCkJE5m_az7b9fwFbGobvvn2BgVurPMSFy9cLTT9xHLmuiFOXanRDTFrO1BKNNYLE7QqPhc3osz8q4-kaf0IcC_7_7FvOnK1zToFMzD18U77CLj4LnMCyKf_-5tVI8gcTW720CloI0IXxOO9B0KJHCOd9pUYTgQ7R2UrqG5emHMjKht8z9fDk5lhgEFS3LZLtSvAE9kCP_Iudp26RCiCmjBFDN10VlDa4HQADJ4ned6sfTxHAOW9Ta2g3cKhfcnGNykrgaNqnO-LITqpfubIwEafuaxzperIDbcMEzisTyjRbsiX1GmovrmpfSqtrPbWcf9C05_6lD5OqgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=GVFR6KYCkJE5m_az7b9fwFbGobvvn2BgVurPMSFy9cLTT9xHLmuiFOXanRDTFrO1BKNNYLE7QqPhc3osz8q4-kaf0IcC_7_7FvOnK1zToFMzD18U77CLj4LnMCyKf_-5tVI8gcTW720CloI0IXxOO9B0KJHCOd9pUYTgQ7R2UrqG5emHMjKht8z9fDk5lhgEFS3LZLtSvAE9kCP_Iudp26RCiCmjBFDN10VlDa4HQADJ4ned6sfTxHAOW9Ta2g3cKhfcnGNykrgaNqnO-LITqpfubIwEafuaxzperIDbcMEzisTyjRbsiX1GmovrmpfSqtrPbWcf9C05_6lD5OqgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUYLzeIsxgOcItm3zNnTnnV32E0aQVtkP6gPZwYvhRUp9QlfjoBvbY_pZQOOSZ7Zu8DhAoPUFrnpLkNtp3uPW9GyYYoUaUFc7OHTfcG1xl1GryEBMJKTZcsg1sxC8L4DtIecjuZ9pNdyDH4Zx7DxddtbgVFTfnlVyXH0ZB5O-v6obMEbOXjiBx5FD2qveSKNp7BtONdkmnggFzOSaWNXwOKCcAjmqRpKveQq9a0hmN0C7IP4eh9cs8ArIkc28P2ZadhA_T3hu60d3Cn2akM9NcPF24k-pqaXhSnt2euzzoEU8Gqvroz0h1wSj3fQckiiyXmOOqMqQo0uabrcESx2Yg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=dEvxQ19wkbj8GoAc7MuqTDcNl2M6ZOd5Uz6V3Ui4cACqVaGx5288xWltEgiMgUv58BvhHz0LO-D8_jNemQ3nDKoC0FY4LwRvkukXxgHf-dCQgxnszgPv32RGUThn18ffi5Bw9dejT50U22lUnyJT_FiV6S4QNmqcWxngbSWjmTXCLvQ5Z8Qjh7jmq3S_SxSsWk8h6_YD3hjEl8k9kPzO0S964aCocxdKsldcZm2jkh8oTC-EbO9OrBKQYSZbt5FcaQ8eplgNMSo24iW-fbdLRh_ggHIro1PHkPQodP3tG43N-lRhkH8rI7lj6N6ObtUErkoIRZYs_TfLyzBn85uQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=dEvxQ19wkbj8GoAc7MuqTDcNl2M6ZOd5Uz6V3Ui4cACqVaGx5288xWltEgiMgUv58BvhHz0LO-D8_jNemQ3nDKoC0FY4LwRvkukXxgHf-dCQgxnszgPv32RGUThn18ffi5Bw9dejT50U22lUnyJT_FiV6S4QNmqcWxngbSWjmTXCLvQ5Z8Qjh7jmq3S_SxSsWk8h6_YD3hjEl8k9kPzO0S964aCocxdKsldcZm2jkh8oTC-EbO9OrBKQYSZbt5FcaQ8eplgNMSo24iW-fbdLRh_ggHIro1PHkPQodP3tG43N-lRhkH8rI7lj6N6ObtUErkoIRZYs_TfLyzBn85uQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=BmwofFR3sr_pTHxPXCAmn58dAygvEIBz32tbZYQGBq4pJavjXi_MepY_YOWm9G_Ks86A1RewcAmvuEEkJoWuVoQ03d9QPyZPZw8o8Iy1eiKPiYoCmn9Kd2Q-r3OuSgyDZzmCL-7jJI_76fW23CxlAWBAlLO7ORy9lbRbOu7goQ18sn0gvMClhVpnUCqM1JpjSBBB9mSWkO5MNJhjIqx_XM8gVskW3wpMUbTHCK1wchltZcpzexRm7xFB-ESxD0x9UW-VsQO9krg43EaF0PihwzGKSvfgfZNDpQyT3oiws5me8uhY0YpiRR3wI0Rjv6CSxJa4MHUy2hBNtFCTE1N5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=BmwofFR3sr_pTHxPXCAmn58dAygvEIBz32tbZYQGBq4pJavjXi_MepY_YOWm9G_Ks86A1RewcAmvuEEkJoWuVoQ03d9QPyZPZw8o8Iy1eiKPiYoCmn9Kd2Q-r3OuSgyDZzmCL-7jJI_76fW23CxlAWBAlLO7ORy9lbRbOu7goQ18sn0gvMClhVpnUCqM1JpjSBBB9mSWkO5MNJhjIqx_XM8gVskW3wpMUbTHCK1wchltZcpzexRm7xFB-ESxD0x9UW-VsQO9krg43EaF0PihwzGKSvfgfZNDpQyT3oiws5me8uhY0YpiRR3wI0Rjv6CSxJa4MHUy2hBNtFCTE1N5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=cRZh_G5Gf0NZ6NzWlLdVBlLsD4ciseUL2Ix3kx4Ns3rl0SSHb1TNYOo_CE2HCXV4p5l03w0BdO4TEgrQxhwa76RcTcdP4myy80DpGA9tt0rVAhzuTP5y3j8zR5Ufl971klIsnCsWqUrCaXqiLN5Wg4BsmYeJVvyi9pvnXZUVtOfSrDE3VqnAy4XAhdHhfraXjm3n2n-ppO5g116Mbwcxvn-a2ZmV0fYK4DGwDjsqvTh2UoVxwhoAa7-laJB3rGW2lwLZwk6sq5Op0YU9nW13-MPD9DLIqO558iaaMNpph0hsokJ0o1F0rEoW5Oc2nO9KSY6OeLhPeSgujBpw5TRfIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=cRZh_G5Gf0NZ6NzWlLdVBlLsD4ciseUL2Ix3kx4Ns3rl0SSHb1TNYOo_CE2HCXV4p5l03w0BdO4TEgrQxhwa76RcTcdP4myy80DpGA9tt0rVAhzuTP5y3j8zR5Ufl971klIsnCsWqUrCaXqiLN5Wg4BsmYeJVvyi9pvnXZUVtOfSrDE3VqnAy4XAhdHhfraXjm3n2n-ppO5g116Mbwcxvn-a2ZmV0fYK4DGwDjsqvTh2UoVxwhoAa7-laJB3rGW2lwLZwk6sq5Op0YU9nW13-MPD9DLIqO558iaaMNpph0hsokJ0o1F0rEoW5Oc2nO9KSY6OeLhPeSgujBpw5TRfIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enpZhMcwAb-AX0Gg3Uy-n3Ukj8K8D3ykKpOFpeAqG5d8qQhyq9BkoELI7H_df_OJbvwxqRFt6Z1wDXaTENGjU9LUKIC2a2M0XEU8HF6jPDP-IcTpI7VD4Tku1TqdJ4vtJ4AnlzJtqnOeRG2AlNPPmojLYvc1Wf9RYRTYwWFFnQBPbj8dcpDTLklsLNbzA2BqSQRijwpWzIN6lu1HRq1vP4_UkUIPxMjx_t_KpE-r7zPMn5iGVKqtYDsmC1MqlA-SMeCL5ze16aXMpBEyz2nDLqFpfS9TImvWDFoP6P2feT0E-VvUVm28LBytnhkm7g9VuT23-Tynyjg150qIl3F23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihh-UtAVEU8JcuUBr90eDywSr8Ba7IhQE6LAMzueeqwKNhshtFLbIWbj3OQaZ5GtxXFa_5FeykfjgBGjht-sAQyD0Nqw4eijEdraQq_sQGDm4lz9sWiCPOqB6vrDThwvkwBVd3fS9LPpKFyttg4N2v9XSVBZLLZuBk9GiI9kZxbdcsQ4nNMDCfTRN2UOzJJ4dBqBd2oKfG2VcITlg-sS7MDevDzmfhn3qDcGLCL8UVuup_Q6hUhqPxFZ0UVmGMFqsznYMj5v3cwhCDSKrj_29S8vRotNahAjgG78_v_31KpeRBSOxqYzp5qc3bbvaaurAHfN3asHAanA5gmtx1k33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=If9h4D0NezJPsQf0jNHGqXxzWbjx0fDThmAb5Oo2m3WmH6hG_pz0XpuIZkj_fB7KTmwfGFXiGfVZQxMXSZSUTNQX3G4J_XEjVYjh0-LGlvDEu5SyAy4dtMOXVsrvfmYpvUdcpWxI5BzbwaTQx-tyJXlOxPsQ6VGDq0k5Vi49GZdvgXLI7gwIDtTxidWrwP4Hs_MyZQYkInogBZzjsx_ST-lqIjSGeXVa71RgcFgkJjnDwq41bN2LwMYogr65r7-OZ30bdOBD-keysSM3JakPi8GpGvy_HCOVGULMqPlFMEfhec77VvY1kEdBuMj0DjmSvyLBVPzYa68Cf2rDX_AMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=If9h4D0NezJPsQf0jNHGqXxzWbjx0fDThmAb5Oo2m3WmH6hG_pz0XpuIZkj_fB7KTmwfGFXiGfVZQxMXSZSUTNQX3G4J_XEjVYjh0-LGlvDEu5SyAy4dtMOXVsrvfmYpvUdcpWxI5BzbwaTQx-tyJXlOxPsQ6VGDq0k5Vi49GZdvgXLI7gwIDtTxidWrwP4Hs_MyZQYkInogBZzjsx_ST-lqIjSGeXVa71RgcFgkJjnDwq41bN2LwMYogr65r7-OZ30bdOBD-keysSM3JakPi8GpGvy_HCOVGULMqPlFMEfhec77VvY1kEdBuMj0DjmSvyLBVPzYa68Cf2rDX_AMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIZ1PrEj3suOeLxVToolcA8kWEcxA9SH37CtoTJ05gpRk7YEXxSCYVb-P-0DIRZRfLyuPzjmyv9d2HWYmnksfN6Jv7MrLiXyWWWT5d9PRZ3XdJnqkL7h9rbOqcgziL45xrLrvKh83-Ph3MlhO13DVqskaXPJHcMrHeToQ20uf5ifk-E8fvSZNYuvLvwlxcKC_V8FkhIpdeKRASbYLRVgLkvZ9836IeJCE4Hfy1B1re_mN3XrzLYJLoaUnjjZKPvfAk6vg-C_yFoUUCFB7u40yPhWSbEEzB0FAp3MybjRXbeaSihVr_z_T7R6a8nKerML3hRH-vmp9CfvrxTFCW2RkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_lMQkzW9hB-DEJ0EZFIZ8g4oSOBcvcWPl9e7_34QzhmJhg7XV4yLlFgELHqNuyyn7UE7ELGmIqLlffhOBnneb_Zw4mnIetUeH4nO5H4kQACVhrfXybuxnUUewvvz756RFPsXjlaLfJFjQvlnh9j8XuhhSLeYgoX8UB7K4wB9HImnFWLF2vbRSyRcr4MmDTZsVfFl-hSS3HKAl0gF08RqazoMpVUkNqUjWYdy_-ZmG8kaSJxUHAPmDQR6dn4McP_9gizuIMqaTD40HxYmvj-MFa4Pd_C70BVOotOQV4vyx0W-agNp2awwVsARYiynmlm6Ie2dwhn2pyplUnruJYOHw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=OY0xi9n6x8Szh4LqBPP3JmG9WNrAhbxQU7F8claSD8ANabhNnvRYUb6aHjhQCCMgjSmSc86nUXbGsB7tT4DvGEEhVODYaPLYwIqzZbjUq9PEcSYx8c94nQxxnFEcRsfcAgqgT7akuUUHZAAkr6abaAmpCOa4lc-CbfTUpAtVrfwXJT87_mPoq1SFUHVd7ZRkv1S5D-b6YpRegV4YIC2SsWTyRetCgIYRJYRIG8-ivp98nTLmcMWkKzi70LpjOyWGI3P79P8Fv-Ced2v9blhZ_nJUHMRV03dOcjzFlxanbjF2mJNXEhQIQ0R3u-odE-MBgJjXYghpQ7JcRBkDjNHH9avV4RLuDsUxRAFhsXOoPL-8wviDi8sy1jB2xiVGXNJ79_kFfxM1Kn9FWZ9bOmhzRv4vnDRy2jEEjA3YGj7bn0p9-jHMOmlWZpYBHW7P8s3f0mhGhoaJjGr-8QqyDvnarLhVFRqp41SuuAMQo-NsNey35mQH_VijkiH1PGYLuMIYG7OtXL6Q03m9_B3cXNakwcwXhivgmiJd4U23mb68ZwmzO8Yyq5uKkW9V79Ig0Sfm9U4j7CRKqVsciC2txIcJcI2iTZgcQQTDOiXfozxKOXBibxFGmLx-KqApaVKsgUG1ows1haWsfrCmZe1kyU8cOIMoQJNEY-GrFT0nYlSGPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=OY0xi9n6x8Szh4LqBPP3JmG9WNrAhbxQU7F8claSD8ANabhNnvRYUb6aHjhQCCMgjSmSc86nUXbGsB7tT4DvGEEhVODYaPLYwIqzZbjUq9PEcSYx8c94nQxxnFEcRsfcAgqgT7akuUUHZAAkr6abaAmpCOa4lc-CbfTUpAtVrfwXJT87_mPoq1SFUHVd7ZRkv1S5D-b6YpRegV4YIC2SsWTyRetCgIYRJYRIG8-ivp98nTLmcMWkKzi70LpjOyWGI3P79P8Fv-Ced2v9blhZ_nJUHMRV03dOcjzFlxanbjF2mJNXEhQIQ0R3u-odE-MBgJjXYghpQ7JcRBkDjNHH9avV4RLuDsUxRAFhsXOoPL-8wviDi8sy1jB2xiVGXNJ79_kFfxM1Kn9FWZ9bOmhzRv4vnDRy2jEEjA3YGj7bn0p9-jHMOmlWZpYBHW7P8s3f0mhGhoaJjGr-8QqyDvnarLhVFRqp41SuuAMQo-NsNey35mQH_VijkiH1PGYLuMIYG7OtXL6Q03m9_B3cXNakwcwXhivgmiJd4U23mb68ZwmzO8Yyq5uKkW9V79Ig0Sfm9U4j7CRKqVsciC2txIcJcI2iTZgcQQTDOiXfozxKOXBibxFGmLx-KqApaVKsgUG1ows1haWsfrCmZe1kyU8cOIMoQJNEY-GrFT0nYlSGPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E61hKKIq2hn2cjev2OLOYS2LNq3cG9dGFTdqNTFSSQ70SA--B4bK_485qQvKXUbxU-lHhNEvhevHkDtAm06f0EsZpe7NGIbWtpRdEZijDqdd2LP05M1lxLIOLDdYKrQgcLT8BN515P2tszwhkdO1SV40rN7ZHRlcf0YXnSspG7jN2Oe9z_ukx52P6fFc17jhwpg8DNHybpo1RHAhgPP9ZAvbBqsurkU4bDG8BBdd_BO5RI5Yt68XblWIXCxT61b6tO4HLxHTVBoBkfp7AnIBYyDf3MStaIzE91CKrp3eydH52Kpy0ScX9OaVQ3Pq9R4FIz1nlaMLjXJb9HKFAzRevSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E61hKKIq2hn2cjev2OLOYS2LNq3cG9dGFTdqNTFSSQ70SA--B4bK_485qQvKXUbxU-lHhNEvhevHkDtAm06f0EsZpe7NGIbWtpRdEZijDqdd2LP05M1lxLIOLDdYKrQgcLT8BN515P2tszwhkdO1SV40rN7ZHRlcf0YXnSspG7jN2Oe9z_ukx52P6fFc17jhwpg8DNHybpo1RHAhgPP9ZAvbBqsurkU4bDG8BBdd_BO5RI5Yt68XblWIXCxT61b6tO4HLxHTVBoBkfp7AnIBYyDf3MStaIzE91CKrp3eydH52Kpy0ScX9OaVQ3Pq9R4FIz1nlaMLjXJb9HKFAzRevSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=IJJKsSmez4IC17JtAlYdr65uJ4Ai8FmJOt8BppHRijZ7FeQtCSTfgzr3MP5mR5z92hq-b3hRROTlCW1D1C8F5olONuiHxy3y_szCXh_WTSPlqm-r-d8mTzAtfM9VwbC4WILRQcbq3g-mBWq7ITjEGUQ6JADXjuC2JCFwTma3XmnW7enmmOzAIW4mZXGPH4IaRglsxvUJMgfUR7BASlNcZPSrnEklqR7YMYmJedKuwWORz7BLKQ585UjOO5mJ-t_vw-DtBLIgimXBg8q0wTwebevD9mJYzO81S9b1WlJHwTmHob-4lRLCFx0hdETm7wemtOVOy2OAxfMnEGjsbLXXfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=IJJKsSmez4IC17JtAlYdr65uJ4Ai8FmJOt8BppHRijZ7FeQtCSTfgzr3MP5mR5z92hq-b3hRROTlCW1D1C8F5olONuiHxy3y_szCXh_WTSPlqm-r-d8mTzAtfM9VwbC4WILRQcbq3g-mBWq7ITjEGUQ6JADXjuC2JCFwTma3XmnW7enmmOzAIW4mZXGPH4IaRglsxvUJMgfUR7BASlNcZPSrnEklqR7YMYmJedKuwWORz7BLKQ585UjOO5mJ-t_vw-DtBLIgimXBg8q0wTwebevD9mJYzO81S9b1WlJHwTmHob-4lRLCFx0hdETm7wemtOVOy2OAxfMnEGjsbLXXfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=n7XRZ5kiZXiMaj9b6j3mahtLZAe3g8mIEiuFDNObE670gc7glEMIAOn8ZlQXcHHWKRJrsuA9E-IXOSg_6HisNCUyiGwKJvI0pVhH7PY2gRTYJt-3rI5j3dZi6rfaU7yp27cFbbKdBBS-lyO6jBjZgESRRtT4EvCtOgF8QtJMiaDnqGSzRKhuBy0ZVUjAN-2UGGcxR6wbz8_UaGl49-nYqqb3sV6iOMv4fZyMl201VyieqpT05XU4gBy2t34crkiNuEu-vGpvNP82usmQhtWBrPxYlP_DGsiVq3dsIDflBYZoXPiy_T4hDYFr9n5oT8D7ZCoubcU0PoIuMQI7_SegBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=n7XRZ5kiZXiMaj9b6j3mahtLZAe3g8mIEiuFDNObE670gc7glEMIAOn8ZlQXcHHWKRJrsuA9E-IXOSg_6HisNCUyiGwKJvI0pVhH7PY2gRTYJt-3rI5j3dZi6rfaU7yp27cFbbKdBBS-lyO6jBjZgESRRtT4EvCtOgF8QtJMiaDnqGSzRKhuBy0ZVUjAN-2UGGcxR6wbz8_UaGl49-nYqqb3sV6iOMv4fZyMl201VyieqpT05XU4gBy2t34crkiNuEu-vGpvNP82usmQhtWBrPxYlP_DGsiVq3dsIDflBYZoXPiy_T4hDYFr9n5oT8D7ZCoubcU0PoIuMQI7_SegBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3yovhSRNfsAizqAqdS3BKL1nhReShR1sKSgZeFltL_qnAK6vgv3WrzlqcLc32dshjENTJO3RoQf8gIONcw8hcTgg2nOZKSJ_N0dFH7vZ4cayLZQNn9wyBqDrR0vwdEZH0svLGdL-ASdhrOddS0wLBhUVQwmKoXBztuQYdB7TRx5nCppL-8Zyh5cNOt6Du2ds4xRKd9rlGwLw90Gj1F1htag111y7l2Zb5KGZGddsU-ijGL70Pc1wfLI0fDAdKwYipyqVzA6a9Z284f0thD-Cpi0DILJzH5ZurW5ANWgZZhbMYxHDsbyEX5IarzOfe_z9RiP29t5b0zBGFpp9Y0kNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfmn8pRyRIG0MG9bR96TorniqBxHO6-21MVZkxM11Femd0sTObyS1h6dRL5YjHv4Qg35pAIFN44XXMcNyIOa5WRIuYUXJMrdsknohVsOko25l1SKRmNiaAUQVOmPcJoA6-_4bRrgtHwy9OYmTO9draatCT0dX0oKVezWKQDi8UPkq0Tap2zMB6rGhMDr3GthvrGlPuDeoRa6M023eBCunW8Aaurxg78sV7f0fX43SZ7hiaLbILWQ3FSlIlBYnraVGlBA647GW0mUSTbx0eMnkUFWdvEUf4lrHXRMnF6IkuFhiNbe1wtmCgUPyi2_lpUaT2PxSGvaqLyVWJ_NNunEeA.jpg" alt="photo" loading="lazy"/></div>
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
