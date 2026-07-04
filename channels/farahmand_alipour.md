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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTjbgCJkleIVOisM6GX8PP0FVo5QKTn5h1grK8ON36GqfeBEyyofb8ObyZzmCaYM9gXrH3kwKcOCZjJZkb2CrrNzcB5Yfby1xsRLEyoLXlN4Kq2fsbQyj-vn1atMtsT2BL240C9opySd0BgdpRhuh_rhZw7NbA0wlEFlCBLX7xLKB-qDFsMttDLYu8tAAQylBiVYGOCQniM-HR-54biMYJ46A9rcifOnVaCY7d01K3dd3elaayP3X5RQjYmENp_c93CtkDi0t0CtKo_oJ-s_i8QlFsiH2Q_utYbLbditgSYnPKD_W29R7t_dgm0i_zzdsPwMwJ4stQhyk9-6J2Dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwvQxP7MWyGOP7Jy4AhvuaJFv9Hb61w4gpKTyBcBF6F7t1GtOXMxj-_GiBON2JVB_wwXTWfP6bDTk-g_9EMrxsq7f4sDpL2a4Ire73jXSh8akgW3hVulH-y5j7B9FXJNW4ZVZ7cqiROawcm3MNzNXVeyOxLhOmqjCm07SuFHzf82FBA2w1esHrBZkXggWWmJ9P0dZLCHUJ57ZK_1ha-X15pOKZ0lwfDLvSGeW2NbXdhMJTfg6gC3wj-OZwe4gOjgAFOTqQGiLWAjQqja_cc_2EzaMzNJ5E7jb9R2gIRvXHXojHyD1dPDBXB1vtrX8BWLbCyesP-hr5B6dBsgfy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh_lbi64GAKICIj1XanDDf9XRBHZ7iObnVrTHBw06VXmMkfIxIsm49by1SlEv3OX_40Gw3627dglrn2e1sNCsRIcJitQOocvTfhp2bfXtqtBmAsXwX8J6sigFgJ5dE6ccvCp9VJdl9iEDfjmxX66wTwELxzVESz89SfKpqSmGmq2lFcjb_uDr8Mc4WmNVQ0zXL0sxmy5P-ZRTUGXSOSyLqG6DhaG3e48pOlto87UdHwvbqmWuBIimIJhN_5bMmAQfqCVOIdaVtQZa0SfLrnbrjLoNEC_qpyDxeqdy8jfZurxu3lyGJFN32pSvA18JoY04mmAMJxWZI8bvrWa0DoiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlJGqIqJWfaFjL5JkqLHU5aMy1N3KccuehirxipIK2vTi5TSDhTPNWOMseXhaDKT_Bn6XYBPEHpasSi1HFQmybsKnZSmUZodId6FFplK4E1mN3OHDBnvman8Q3SlWCdVU4Hp2T9ttnS6ytk8LMSF4PyXmL8Ixm1oI9BJo1ECmLWTLg30Akyn_tZbZ6y4gu5zZtdexre_Uiy4ZMLh8Puuyk-IaOgBWcvxUo4EJyMBRLieq7CYTFmjHIQypto3K6ri7xf93h2QqgRg_E9m-XChjlCNwbrcCv29LUEUWwWchUPGSsAmSu481MOipSTSk7C-7rWBZfsTj7VFTcXNGjwmfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=E3DsOmT8QwG7PsrgxQJwb_tin6GzHdDeEEZhYMHD6Sm-w5Mm7kNR5Shr14JscU-xSScFdkqknafSLvzHmjYODcKX1VBJRBBu9SvWtk191zC2PdlwFq932WiGmmFP4581xnWra7m5I9J5K_8BFPLqIuS1JpCs2rTE85CqsHvT_pi24WbL4GrPN89AGsCMC9ExwP6cpLqi_M5oLc2--KgPECm_s-18te_RSrIgbexcXY3s4eDmkZXzg-BnBeiE7qZU43cSmqxO6Dvzgr42J0C1N1mu3eGeBtN6D0qfCXWVQZssPHFkSWFuMRcdknkkPI86hVYxUTbIjIEHoygfUXaOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=E3DsOmT8QwG7PsrgxQJwb_tin6GzHdDeEEZhYMHD6Sm-w5Mm7kNR5Shr14JscU-xSScFdkqknafSLvzHmjYODcKX1VBJRBBu9SvWtk191zC2PdlwFq932WiGmmFP4581xnWra7m5I9J5K_8BFPLqIuS1JpCs2rTE85CqsHvT_pi24WbL4GrPN89AGsCMC9ExwP6cpLqi_M5oLc2--KgPECm_s-18te_RSrIgbexcXY3s4eDmkZXzg-BnBeiE7qZU43cSmqxO6Dvzgr42J0C1N1mu3eGeBtN6D0qfCXWVQZssPHFkSWFuMRcdknkkPI86hVYxUTbIjIEHoygfUXaOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=M3KqxGcMJPb5B8_VI8kGC3CslSZvhPvVJ76KiVg0t8cw1Wky60cmm8cdWf8ZoEE8UxcN5VqdiNlKersP_Bls-yfIP11RU-13Sk2snbZDs1TzIFU4MsxXkmmmg2DOWSItKqIbisgfvlT-l5SIzO_wkKcqPrGM3bEMax0G6IMLA95V3exUUOtQgdE4_25MJR_vUoiU5l6m8tC5zzHkyoxRjSNGknG-fSwJIqW7RgewO1bGpUG2OFOImmjqqH-PWMsuv6V59iIebG2VjmLcgi1IGjfBYHJAVPeLgliqqbT_eXYA093ZS2U35OCg77sGAt9bDf2ZaPSbN1DLqjU-sSpWBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=M3KqxGcMJPb5B8_VI8kGC3CslSZvhPvVJ76KiVg0t8cw1Wky60cmm8cdWf8ZoEE8UxcN5VqdiNlKersP_Bls-yfIP11RU-13Sk2snbZDs1TzIFU4MsxXkmmmg2DOWSItKqIbisgfvlT-l5SIzO_wkKcqPrGM3bEMax0G6IMLA95V3exUUOtQgdE4_25MJR_vUoiU5l6m8tC5zzHkyoxRjSNGknG-fSwJIqW7RgewO1bGpUG2OFOImmjqqH-PWMsuv6V59iIebG2VjmLcgi1IGjfBYHJAVPeLgliqqbT_eXYA093ZS2U35OCg77sGAt9bDf2ZaPSbN1DLqjU-sSpWBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=bbaGSlzFD_K7V4MwPv8HeVehKXQY3Y1ie8Ef_9DvJR4rgYjRBSxpgc7SlTXvskaB33HvYQWgT94Olv7uhtB1LYRoOeqcNMXjJstoHSzz01vORLjlSlGxlQMyjnweZ7nVMwDIhL6Z9QyxKAm6wrT_XRWg2UDdKODHERfdOSMxuyLaIEWRLrw_ow590yr5XUSlbUZZ9ExcwYnS5a1byoc0b-6x-CEojFawF_jeQBngYmXqWYG0hHfTqfw-37AdlFdeNeEHkwpiqJAfse4QwWQth6Mdgi8c8ZGV8zD-cY-z2cgJDnbL6XyQBwEAP8Sj5Eco0byPS0zhtUo4TMiqUdzy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=bbaGSlzFD_K7V4MwPv8HeVehKXQY3Y1ie8Ef_9DvJR4rgYjRBSxpgc7SlTXvskaB33HvYQWgT94Olv7uhtB1LYRoOeqcNMXjJstoHSzz01vORLjlSlGxlQMyjnweZ7nVMwDIhL6Z9QyxKAm6wrT_XRWg2UDdKODHERfdOSMxuyLaIEWRLrw_ow590yr5XUSlbUZZ9ExcwYnS5a1byoc0b-6x-CEojFawF_jeQBngYmXqWYG0hHfTqfw-37AdlFdeNeEHkwpiqJAfse4QwWQth6Mdgi8c8ZGV8zD-cY-z2cgJDnbL6XyQBwEAP8Sj5Eco0byPS0zhtUo4TMiqUdzy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=udpKnCAWnbkos7-JXWptBle46u9cBpamzBa-qtUTabbgVszNNtp6qR9dY1UZ_R5RybgdgMjwZ24eRB8KC26lOVauNf81AgpALRTfjESRnm0JSMuWJLVPw-yvqiENTTW6I3gKHWGPCVBhmQL7fDPSWOe-Up4CNeuK1USJAXrau-TYOx0MCxZcnMgjEqnwJejLcbk2_X-rfzEFpC-dJMMUSvQmEfmMpbSUHnfavNz7qYOVqFD9TJcOWTjA1s20WBkPLAxOvYZ3xK6o5lTb3IzH15BZg2pQvOu_IWrAJCyL0Ri7nqUUXffP8M2UnOgo_KlZJF01xRQd_SXypYmVqQmn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=udpKnCAWnbkos7-JXWptBle46u9cBpamzBa-qtUTabbgVszNNtp6qR9dY1UZ_R5RybgdgMjwZ24eRB8KC26lOVauNf81AgpALRTfjESRnm0JSMuWJLVPw-yvqiENTTW6I3gKHWGPCVBhmQL7fDPSWOe-Up4CNeuK1USJAXrau-TYOx0MCxZcnMgjEqnwJejLcbk2_X-rfzEFpC-dJMMUSvQmEfmMpbSUHnfavNz7qYOVqFD9TJcOWTjA1s20WBkPLAxOvYZ3xK6o5lTb3IzH15BZg2pQvOu_IWrAJCyL0Ri7nqUUXffP8M2UnOgo_KlZJF01xRQd_SXypYmVqQmn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=hXuhKN5ALlWLvTOFW7vAAnSzbiD4HhkAgLjel6txE5k9nUjRrD7h8tKG797sgqQXTXUKz03qCejPZ8CyOLb3kOYJZfbA1eBlmoQYXUl3sd_NxfurMFSHwv_lb_ysi-XSzfSafP-5NsDDKvQF_r-QfjayWp9elRjYy_4kC98hks_uWhzqRyAdYzGBq_gI4z_C4gEdB8lF2Ls1ITyobmn3IR8aaQQodPc_lxn68Z-RHGIGUyCVVl1n1i6R0WzGzRyac9WRh4lcr79wT1I_V0TAYtHA_rKQ5pkBaFEAJ2MuFA2rVAwUyETM9whK6nGU6PCvF-KULFAW_fOpm8fCLR4PiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=hXuhKN5ALlWLvTOFW7vAAnSzbiD4HhkAgLjel6txE5k9nUjRrD7h8tKG797sgqQXTXUKz03qCejPZ8CyOLb3kOYJZfbA1eBlmoQYXUl3sd_NxfurMFSHwv_lb_ysi-XSzfSafP-5NsDDKvQF_r-QfjayWp9elRjYy_4kC98hks_uWhzqRyAdYzGBq_gI4z_C4gEdB8lF2Ls1ITyobmn3IR8aaQQodPc_lxn68Z-RHGIGUyCVVl1n1i6R0WzGzRyac9WRh4lcr79wT1I_V0TAYtHA_rKQ5pkBaFEAJ2MuFA2rVAwUyETM9whK6nGU6PCvF-KULFAW_fOpm8fCLR4PiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=seFPYiBCp4F_cCdz-LpT9bANrItbdsuYj7_HNNodz_2lO4YHR8TUAtMsmBlw7eaHmZ4yS892cGW6qYFE5G-xQGdyLLHp-sVQ0pGRycGEwPgMg50llWC2DtFwbPMPicBDVEKBonT6ivmkql5Puhmoc8D61rV1f_Gyo55BMVFGbWLxyP9fDfCuMMvwpfDDyvcKLVxS5b26FSOx8VLWDBk9cJggmFZt7FYmROQyU-sxTcAoKbON6vTgqxPskKDf-xcxG_pytuS4oswNFHkn60-zwQhhstsy6d_tMQwb_-lkGkzkkwzi24EoSBmpJiTFLlyarutW3CeMe_fjpGWSrGS90w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=seFPYiBCp4F_cCdz-LpT9bANrItbdsuYj7_HNNodz_2lO4YHR8TUAtMsmBlw7eaHmZ4yS892cGW6qYFE5G-xQGdyLLHp-sVQ0pGRycGEwPgMg50llWC2DtFwbPMPicBDVEKBonT6ivmkql5Puhmoc8D61rV1f_Gyo55BMVFGbWLxyP9fDfCuMMvwpfDDyvcKLVxS5b26FSOx8VLWDBk9cJggmFZt7FYmROQyU-sxTcAoKbON6vTgqxPskKDf-xcxG_pytuS4oswNFHkn60-zwQhhstsy6d_tMQwb_-lkGkzkkwzi24EoSBmpJiTFLlyarutW3CeMe_fjpGWSrGS90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=XCbEVl86GCx3lWJIUYI_lMmpOpBFybka7_2RtjVqeENv2MhFZh3P0dbcMV1ORCOsHteYmmMncL5U1AzfnlntkplFNZXWqJU47G-Q44DyiIcr-7o0SOVdnpxYMwmdI9tDS0SFD8wQ8eHR5UXU_3Ju0VW3D1fmdMgoImeBMl8z7UeyTm089XiUewxNTYP7hupGmmqQQJ9usOayG2yygCIwKsprNERdorZOfmJh6FC5-OyD0TzIgYgkf43IEVYjrC8455uiq6Rsy7zCNRAYFbGZ2hhuZCnrZEsS35Lsv4HfB7jtDZ79d8H6fjPbVvH0pB-92vgGMYAwU33xouNihdGwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=XCbEVl86GCx3lWJIUYI_lMmpOpBFybka7_2RtjVqeENv2MhFZh3P0dbcMV1ORCOsHteYmmMncL5U1AzfnlntkplFNZXWqJU47G-Q44DyiIcr-7o0SOVdnpxYMwmdI9tDS0SFD8wQ8eHR5UXU_3Ju0VW3D1fmdMgoImeBMl8z7UeyTm089XiUewxNTYP7hupGmmqQQJ9usOayG2yygCIwKsprNERdorZOfmJh6FC5-OyD0TzIgYgkf43IEVYjrC8455uiq6Rsy7zCNRAYFbGZ2hhuZCnrZEsS35Lsv4HfB7jtDZ79d8H6fjPbVvH0pB-92vgGMYAwU33xouNihdGwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDRH6185Vtvhu9UmNmr7-6mPKN5QdA0WhUOyhQiUQLemlOPHf0dxnX_2VUs_NRT63swz9BLXC5oz1s0Ck7zl7MIImsWUrvkGiXdAnNRyFC25i1nbO0RKPYhrsAOAhbjgNxWuIpDD5R1fOqLQzz6_WVf5lVpa3GMx9yg8ZV9pdLRE11o-zUOJ_cigkh6QkRtIrkLEXI4lOjLtLAWlJIljg95lNWGtE1jh2n7OdjCtrFHvnFkwXFEH4EWByNaf4lkhK7kls6Rney6vgsExx3WMWTiAdd5btNvLumXswH4eenpg0HRZHW_iwWtrC7Y3BKJv9mub5XCvIvUVaLTu_ssjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=WzDxTiIuPaxSPWFfrsX_pD9OQz53NeRyFeiv7Q5E49f-bnmuoIJ3StTuvDxQw-pC5FecHz2aeCVfaF0GDtlYwwPRpwS0AHvXmJDXME4vhKcK33oO1NnnZRWd3q3a9cPjLn1Eq-UQ_pBK3FEIYMmvLDoeX0hXubTVSn6_3mKj9J6lhPKRVB4TfEEhx2jwEj1t3nFXj8hEu8lg2Uu9WYYSFChaSiUGxyEJAVio55oPjzKo-7sNflg2FaK1tsYiENsjnKOCW4cwk9gnavQ8vqHocNiFprq8YZqD94kswVEoDLrB9gleRdZYBUCq0hlyOUID7tT6MrDD-5glOvWkg57HEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=WzDxTiIuPaxSPWFfrsX_pD9OQz53NeRyFeiv7Q5E49f-bnmuoIJ3StTuvDxQw-pC5FecHz2aeCVfaF0GDtlYwwPRpwS0AHvXmJDXME4vhKcK33oO1NnnZRWd3q3a9cPjLn1Eq-UQ_pBK3FEIYMmvLDoeX0hXubTVSn6_3mKj9J6lhPKRVB4TfEEhx2jwEj1t3nFXj8hEu8lg2Uu9WYYSFChaSiUGxyEJAVio55oPjzKo-7sNflg2FaK1tsYiENsjnKOCW4cwk9gnavQ8vqHocNiFprq8YZqD94kswVEoDLrB9gleRdZYBUCq0hlyOUID7tT6MrDD-5glOvWkg57HEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=EdoJ3YpdYqis-NJTM90fu7yr6_kjwlM05D1r310nVWinYfvnmrveo2nkqTzKB2BH6g__FN_X0ew6AelGdOp0IoaucBgJ-7LVglMzPrAv1RUNBcpVnWsIogOyZgkYVhV6xXITYNgjCgEmFVxjmzcdrIqqCbWavgShDaa-ic-1KOQDT1UMXMF-EVW8a13d9JuyvG50Y33ETP_eI6GDBk7cteVkXCL4JIH5uX0cTBBuVV0b3YNYV5lSc71gzuhIuRCIDwXIp2A6ArqtUD1CRO2YUciCCBHTTwUBLZQ9oB8D44EyJe8g8YhrDkQRDcS91mPNDTOg9FZF3yrOO1Nedc_d0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=EdoJ3YpdYqis-NJTM90fu7yr6_kjwlM05D1r310nVWinYfvnmrveo2nkqTzKB2BH6g__FN_X0ew6AelGdOp0IoaucBgJ-7LVglMzPrAv1RUNBcpVnWsIogOyZgkYVhV6xXITYNgjCgEmFVxjmzcdrIqqCbWavgShDaa-ic-1KOQDT1UMXMF-EVW8a13d9JuyvG50Y33ETP_eI6GDBk7cteVkXCL4JIH5uX0cTBBuVV0b3YNYV5lSc71gzuhIuRCIDwXIp2A6ArqtUD1CRO2YUciCCBHTTwUBLZQ9oB8D44EyJe8g8YhrDkQRDcS91mPNDTOg9FZF3yrOO1Nedc_d0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=a3XFD3XgQv5a_w2Jzvdi3bqrJLnNyTuw2zja-s8MJKj6IaB80IVytmato8t7coZBYVwHajRF3vtzHFRXGTgR4k-wigsyhppeqPIS6nzjKZZUW8Wz38U7jX-PIUs2A1ng0OU2RXePGaLyoZIHGh61hEMO9jYjydN-b5nmF6YJupSL8jAJt7rkxIjYzdLUFxTu9nuUb7H15WHqosj26peX84aowsOJ4d5D-05-WU77pZ-CZ6dO00Q0HZdOdGB5w_F-UPSC6RV6AeUO0Q1arisPWAVJTw_wlP-ic5bXftxvI2iaWOFsyQyazyw1ChMILC58ruAOtIJ3FSsRmT2rhAFYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=a3XFD3XgQv5a_w2Jzvdi3bqrJLnNyTuw2zja-s8MJKj6IaB80IVytmato8t7coZBYVwHajRF3vtzHFRXGTgR4k-wigsyhppeqPIS6nzjKZZUW8Wz38U7jX-PIUs2A1ng0OU2RXePGaLyoZIHGh61hEMO9jYjydN-b5nmF6YJupSL8jAJt7rkxIjYzdLUFxTu9nuUb7H15WHqosj26peX84aowsOJ4d5D-05-WU77pZ-CZ6dO00Q0HZdOdGB5w_F-UPSC6RV6AeUO0Q1arisPWAVJTw_wlP-ic5bXftxvI2iaWOFsyQyazyw1ChMILC58ruAOtIJ3FSsRmT2rhAFYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggjQmuIaVPrbQ7pLAP0V3NS-CP1NlpBadhV41-Mqn2102pFEjsgwzNokj2by3yJRvSFrpKxgKb4MwGoYWKRhzh1xQgvC09XEH9fHz9sap6bll7x5Y8JQ8CoY6JeHrHPYWfMDcfK1Qj83aPGLWCUzeLDEOR_eNrSFqaOgdYgr-lK98wLNDIhxYPNIwe2-jDthk2Le6OW8v9TsjAyCMq4Z9xMlpVNQngMAwjjMDYBb6um9G6yTLrOf8ijYxEWCfaygdWgiygLKByit9-Duto5iL_iGPCU5jj-RIwio97x5WZQUb2nJ_8CZ7Ucsu75lVU6rgzCam14plphLW5Dw8ixVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF0WCXYjTrJ0NP1nQCUQDTYVc3KpzPiaZGxNQuMnK6LonrzA_idDMhjQjAX3pgRyQh8tFuue5G1pyLRglSJIBvXDB6dh2hTmjdEo5fFFEJJP0nJwhIVmtTVJphbd0rgqORb0Cj9jlZfA0MNwq2NRFuPuO5Xf0aH05a9GORG2DMKoh9KQfxV8pVH0wZCCCB7Mf6Yk5lEzxCs_fKThN68LdVwoMiw6CLYKglRU9hkwdPSGcw1jLpvZrZjxwq-H4wbXrOIo096Id7AZvFEipNgmdS0hC0erqrAzNwflgvyjH_TjNXXQYK_t20JuPNDURjioZvEXsmJ3h5-wiKY8u5XCKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=FA4XbB9Gjk30uMNE1Z8WAy7YVhx9i2UZk_s7ZE_mz4uJdu9qYlf7S9wi0Zkf4QIZ4E694w7hXYUVf1hg0OG1FtmGVtcjaDmy9QprH7m5pwH5X_sls7hpB5_XwBZIZM3xWLJ1PIf5pyoT2r5RpaKlq8kLz6Nlqa7aCWKFzvb6-YUkHCNTcz5ca9DBPPBzqgoI8g6ruIeUciYfKjgJL6EvMPQuiDjBKZSmNBS0utF9U0aphnXVwAvhavJCpTRaVHjtGm-1R2yINlRVv9rQqzCsMzE2NkHb3R1KAjLYOWUaxol9PLCQfzVnV-409yqIoOIg46MJSQvKV-IqX9xcSOUyg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=FA4XbB9Gjk30uMNE1Z8WAy7YVhx9i2UZk_s7ZE_mz4uJdu9qYlf7S9wi0Zkf4QIZ4E694w7hXYUVf1hg0OG1FtmGVtcjaDmy9QprH7m5pwH5X_sls7hpB5_XwBZIZM3xWLJ1PIf5pyoT2r5RpaKlq8kLz6Nlqa7aCWKFzvb6-YUkHCNTcz5ca9DBPPBzqgoI8g6ruIeUciYfKjgJL6EvMPQuiDjBKZSmNBS0utF9U0aphnXVwAvhavJCpTRaVHjtGm-1R2yINlRVv9rQqzCsMzE2NkHb3R1KAjLYOWUaxol9PLCQfzVnV-409yqIoOIg46MJSQvKV-IqX9xcSOUyg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmqo-PUN19gaLRRimJIkghDtNdrqfx8uwSjJ_P2nJebB5j4SOL5HN_0YbpnDjDIZPZJhhpsDc3SAKjAbAii3mW6jCG_YrsKknkQ_NLNJmqBvFsEVimdCGF7_8gFQdFY4N5btBFXTw_LOq7yjxPzxYxcD3cJPmB5UN5jciximKTzJeaDzBbpGiWfjd1VnGXWuXYtY7q7GTVP-Phzjjp0qVMvOissxEnhywxzx0K0R0Xv--jo1J_LZmIw38fNIsj99x9pQMYviO3TGDSDxTgVQnggS3BKT8IR_vgCkc2amyB0bzIPr0KSip9SMGecrTlssRhIJR5XXCK4m4z5o-3KbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QW_bAQCK7RBF851L0G6BN9Q40kAR4VSAfms8bOqVhrvDgdyi1_c4RRc-EgnANeN44INhkkqS-LXvyDBkGWMw4oxMF3c6vKw48h59H0DyA4jr8vogPzDcIowe55RgE892WDxcWlIi9hBphFDV2xIZqMRCPBICoiash0D5N25TEwL4TDxOnfX0jHg8-McIP8zRjr3yzcCFsgVVxTu-2NcvlyMNNbne8egRGyE--aQCos1fTJTm52TogrV-zKUbBWUu3VFFusSZxNyLYOt1SIeSJrcr_gSqzGCsuKLSwruqv3sHJ8QoIrxDOZvu1EgAy8VyH49CVWkESk6lOKGMGU9Ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euV5KAT29S41E4yW_LasigGVGFGtZIKCOdkPZAF4DccvR5__QhQiQ_-uPS2Vvyt1dDPtHIOLpyA_7FwDw5QrmMmvz-xcftg7FSsQaXMRK_iSDcCuQ9uH1-PkASWJFVkXLPye97ThUnyyjaa-oVoUlaBKlT-qIZlPVun4VGmgC7l2QpdFVkdZqzHrJNTKFV1XmA7bmV_qAwTT33MlnenRjjzedW-YTpttXzgWeWEJ3uKe7Te8Fkt_zt6ytqtawMtmY_tKGg-4v_Mgwl3xeE0VqS7H__SQJx7DF80V_N_HIhBCkKzDLEIBs-IQcmPecb3FhHaplhy4LMLpnicObUjizQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAnTZjy1go35X3mESAYayhtpBxbq2BMY3Z6huRE_RhNeU1wXyEFA0_BPkzXNjZOIOmkG-U9Xj03peQ9-1-I-DNtNqOco3YlknoP5N-iIwfCO5UB_CB1NS0eKMwBmSrexKrIFp_I4m6oXCQLOEnvZtaNJ-ntIKzMlFbDw-K5C5HqbOGNj7kTGVZLG64BqFFw53oQq-jgDaI00V_QHU2-bzz9zPEhQoGbBnYfAkFCDeZ9ua-Cw8bkXlClgo97ww-rkZd9W-QOx4zC1T7DXNM0Q0dC7XJlZ085HnfeZzv3LNa5OXI-uxccnWDUyN90Y-cpUvO955pU2TlZAooVWQbUYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=bGbtVrM0e8bUoiwjCOxBSed5Ej_h0fAWBsgqj9FDT3wIb_iSt_sCmzEiEgGSd4qMBnpRXiumFLKV1hdlH0mdMgfdb6MDttj3FmODFRYYWKLhSLS4P1mSCe-8_u7lwMXsfI3wxCw0z5v3KZSu_R2B6gN1RmHuW-meKOBDMDnSUi9K5PXUFyi1H6gvgB47PAD194BiD1Hy1LtREz5qhK1eK4pobXkSyuZQpKD7LQGym5tW-gLFVuhrgnu-caADVP6ajQ8HtaFOS7r9bMQfNmOTMwFxOvVVyUyRmzmDP4EJ-O1wJmjluJBPxMc10nLBoBtQ122vKBTfh6qArqb9WesciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=bGbtVrM0e8bUoiwjCOxBSed5Ej_h0fAWBsgqj9FDT3wIb_iSt_sCmzEiEgGSd4qMBnpRXiumFLKV1hdlH0mdMgfdb6MDttj3FmODFRYYWKLhSLS4P1mSCe-8_u7lwMXsfI3wxCw0z5v3KZSu_R2B6gN1RmHuW-meKOBDMDnSUi9K5PXUFyi1H6gvgB47PAD194BiD1Hy1LtREz5qhK1eK4pobXkSyuZQpKD7LQGym5tW-gLFVuhrgnu-caADVP6ajQ8HtaFOS7r9bMQfNmOTMwFxOvVVyUyRmzmDP4EJ-O1wJmjluJBPxMc10nLBoBtQ122vKBTfh6qArqb9WesciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=oDMvLn0EujeuvCMW2voko_RHDlVAOGFKWH9_Wt_tBNcGiKEbgBqT6RYUU4mc0KLUO4H6hG3PuISSJN9W8a7OqEyv2onZ6ThuwfdFBaQeRRZ7IvUqh-8y9AfM0CkTKkuxkFtCV_uNItTS0R4Kv6UB8iSZD9mz-fh8aykqgVUdk6qlNztBQT_MNTUZXh82oRqml5HC3zSqohqgwaqFzWfqwZVPmbd-LGg_k-oLa_zJLt8hc_FxN3sp4bc7eTKpvHJVqWMBMpWwyxn_lichbr1qe3QRW7WbTrYI-PHzpfQsDXvjWhgxM9pfFJB_c2RE9W-lD28xSl_-sbsEThfbGDHXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=oDMvLn0EujeuvCMW2voko_RHDlVAOGFKWH9_Wt_tBNcGiKEbgBqT6RYUU4mc0KLUO4H6hG3PuISSJN9W8a7OqEyv2onZ6ThuwfdFBaQeRRZ7IvUqh-8y9AfM0CkTKkuxkFtCV_uNItTS0R4Kv6UB8iSZD9mz-fh8aykqgVUdk6qlNztBQT_MNTUZXh82oRqml5HC3zSqohqgwaqFzWfqwZVPmbd-LGg_k-oLa_zJLt8hc_FxN3sp4bc7eTKpvHJVqWMBMpWwyxn_lichbr1qe3QRW7WbTrYI-PHzpfQsDXvjWhgxM9pfFJB_c2RE9W-lD28xSl_-sbsEThfbGDHXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJRhlI13E6RCrqcPbJe_98tyhPtGqiXH7lxzbKMmvP4l4fJzrzgq7OkrJoCSlmjHlMnphEzexZZ-UozHxfTd4fDgNlYf7NdVJFqQYCki-RkEetHNOe3c1lU2-Eb10TpVd8uoMEtU5hxTOqnLhJlikcxjsJUrjn5ILOc3MLPCRDNply2OqmHMv4fFc7Sv7wIWP1OoTh9HOMXhzGYiDPTHC3mns76fpU9EtNwiEnoarEVIJNelvb1s4lSXLxR-1SkCeHypreIAFCXkCO-3eXoYaTGEGcTdCt5WOSnkX22vZtiMeGJP2WkTJotNJ_fFnddX9lcu6ZqOFtzqvpP-VCnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sz4NyjX--sZMMLGCNuexEw2ID5b_aTsWjon3B65e9RfE_3H4bM_dYGs6Im4vOXsu-j0uiXmp0H4qGh8itMqj5HFmGNpeKUshvKN_PmiWbYCs3lMdmPiY_IlCBk_vmgiAamHxqf4Dv5WYHtCGi93vFfwZEW25UipRfq9f1LOa4PHW-crHMAYkLA1eUbWeiJ4UQvsvoJaylkI98Y1Xudh4arViuh1M980zEksbMozpyDAWlobujvlOROOXZ0iz3VJNweKukXOCUC-muLUUHeePb6iW4pk92nLJ59x5d0cupvuF_ASzafBRYB2dXm2gF8GLl15hkiA4dnw9Zl1QPVNUvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sz4NyjX--sZMMLGCNuexEw2ID5b_aTsWjon3B65e9RfE_3H4bM_dYGs6Im4vOXsu-j0uiXmp0H4qGh8itMqj5HFmGNpeKUshvKN_PmiWbYCs3lMdmPiY_IlCBk_vmgiAamHxqf4Dv5WYHtCGi93vFfwZEW25UipRfq9f1LOa4PHW-crHMAYkLA1eUbWeiJ4UQvsvoJaylkI98Y1Xudh4arViuh1M980zEksbMozpyDAWlobujvlOROOXZ0iz3VJNweKukXOCUC-muLUUHeePb6iW4pk92nLJ59x5d0cupvuF_ASzafBRYB2dXm2gF8GLl15hkiA4dnw9Zl1QPVNUvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=gMrkMBhhEnDglbkrYCuig1VgtAM2IYnnIfp9mgCHKR-rwWMy4ZoivGE_58CTjo-9GHSMosAx3B26z7QdmxdAwgrzzwR3Qmxas4zr6njfJWUqWExRRIJEmxAdDqhmDGc_jjnyZGK5Hmr1Y82SaRpKPqgILvpIXaUsCE6QqKkWV1YD8hyxDJO3BheOOIV4dei3r4gUhYW8cS79Y8ss2kCvfcjhaNHZIAOL1o2DGl-ldihrqpfWx5l0ZI4q9kBd07pQEgcfp7aY54eJG79QpkWxXJW9XBvtYN-0w-78EaLHZhHgrL0IAwFgrEYRY2DJDNR7Wn88GDjZpm8L4GC4ISZQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=gMrkMBhhEnDglbkrYCuig1VgtAM2IYnnIfp9mgCHKR-rwWMy4ZoivGE_58CTjo-9GHSMosAx3B26z7QdmxdAwgrzzwR3Qmxas4zr6njfJWUqWExRRIJEmxAdDqhmDGc_jjnyZGK5Hmr1Y82SaRpKPqgILvpIXaUsCE6QqKkWV1YD8hyxDJO3BheOOIV4dei3r4gUhYW8cS79Y8ss2kCvfcjhaNHZIAOL1o2DGl-ldihrqpfWx5l0ZI4q9kBd07pQEgcfp7aY54eJG79QpkWxXJW9XBvtYN-0w-78EaLHZhHgrL0IAwFgrEYRY2DJDNR7Wn88GDjZpm8L4GC4ISZQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=twvG88jm14jrpEDE-sfLrrLi6RK_cV7KbR2ceewGLFWbDo18GqhN9gINrfBrow-H2R02IKQQ7QeQhf5XGdz7GS9w0fe7jRqj6wZs04xc1qctX5JQWhOmIF1JCeseCrIC3Hxi8BsMg_2qVZjif8eDwUFWs2ZbQM8uenJxvc9fOeyEOZJXC8LkzqOP8Ai1cgiruG2DlWlaXQ8fCN3JPkiz6a_ZDxxS2EAih_ltQrZ1seqc25IgJ3zCHFTQyaf8QW7Epgj864hioXTB128RwzWlCw5kEsOWLXmw3YHY8Eekqc-VrKdH29l0oiihs0pMy1X4VrXs0FMO57QOSSr7SkPpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=twvG88jm14jrpEDE-sfLrrLi6RK_cV7KbR2ceewGLFWbDo18GqhN9gINrfBrow-H2R02IKQQ7QeQhf5XGdz7GS9w0fe7jRqj6wZs04xc1qctX5JQWhOmIF1JCeseCrIC3Hxi8BsMg_2qVZjif8eDwUFWs2ZbQM8uenJxvc9fOeyEOZJXC8LkzqOP8Ai1cgiruG2DlWlaXQ8fCN3JPkiz6a_ZDxxS2EAih_ltQrZ1seqc25IgJ3zCHFTQyaf8QW7Epgj864hioXTB128RwzWlCw5kEsOWLXmw3YHY8Eekqc-VrKdH29l0oiihs0pMy1X4VrXs0FMO57QOSSr7SkPpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=eDJfsT__8jG5lfjZZYSCZDnc0zFNB8BYhjTsV_mGkw7_z2QpMpjsCCfNNeQflkbxqqQoeVv52_9mhstNXSf7AFW1h810YMX8HpnYFbtueXi1xqaEz7PVE5wDezGdEOZlo_XD3q7BecT7YSkff_bUzm_2L2sQw1Q0vQr7c9ejVeYpQGzFCTv7ajy_-7sHSfb5wst9J0MVsQRAhk-NKfUDPRTsl_cN9WBW-fpbY1XSY1ddhxtc39Bx8Bc7BiNa6q3SR2FghK3Rl7fudxUtQJqYrg4n5OHd56EwzYR8zkB55-5YbxNj022nuUMvkqnLqJdqfiU3akpRb0pxBx1Xx9CUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=eDJfsT__8jG5lfjZZYSCZDnc0zFNB8BYhjTsV_mGkw7_z2QpMpjsCCfNNeQflkbxqqQoeVv52_9mhstNXSf7AFW1h810YMX8HpnYFbtueXi1xqaEz7PVE5wDezGdEOZlo_XD3q7BecT7YSkff_bUzm_2L2sQw1Q0vQr7c9ejVeYpQGzFCTv7ajy_-7sHSfb5wst9J0MVsQRAhk-NKfUDPRTsl_cN9WBW-fpbY1XSY1ddhxtc39Bx8Bc7BiNa6q3SR2FghK3Rl7fudxUtQJqYrg4n5OHd56EwzYR8zkB55-5YbxNj022nuUMvkqnLqJdqfiU3akpRb0pxBx1Xx9CUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzfTBxHROYob6eKpkhlJIiAwOn1x9KEis5U9IpfKYEsz1tiJIFvUtpR2mBa6qmbQaWKQ6sZs4X1An8Rf-9yJNQ-Xmd0VYVyS7f8w0-WGYdPTcZR2JVR_42tLrcL6LncpB9Y7Yh2kBIdcyHoE2N4b48WR-2gcq_tXNe2c_PZCHyiK_L7L3qGDj93KE6jYrwOcGn0YQprrV1IeahyGKsjwnYC8nRz8rG6QlD-GY1LmqqH6GiZS8PA82JaafiFt6fIFQZz0YwZ3-A3lHVbdCeCBuwPc0Uds0_7mnSaDQn_A5KvISNizXcdEVKCH4iK2x2bS8tR3uWwpnQrfjAZvZUbLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kre8YVgNr9CLwU95RJKL6IFV-qXy97o_1GyGyxRw9926lwCsEj1pnxqH-Ehi9KZlkzfZ6UDzmImyDCYnX6EuvRBRU8m7huGfksUlv96mBJlDBpsx_HuU1KRmVjCW9vg7eW9moQn6uK_pxhQNf2sfBNIYZwKJi7jqoQO2BPklTY9GBs8CLo9e0HWVowEsyqR2Ci1PWCmX0FSUNnX3UG_VaYOrqG6KqTSr7x7KwwxXgNDkfiv604I7olXL4ARjK4mVYUY8d5GQvR-36VYXd16sVtQiQ4cGccMPwr-KIoKHkcW-KfTR0EBuH3efE8QpPrjyN_meKmtoUkOJajngAQ4iOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=cpE-bgvFKonoI_1Gc9akV12rlqYGNEqqhXT66dA9ybvk9fnjRQn8FqDV0SOa2eb1LVAkDOuRnB4pb1weXc-NBZESN2crtfjIq4XqzeNsetWuxrTC6tHhmdUkbz6jSfPd9ypnDGVFNzFB0tXEm7Qyfe28uzvocg9kbBNoZOV8LX6BZ9ysamI-HbbxBZ7-_9edqZ3Q44_yR96B-hugyGKOgadScj65lGM85gKRg_G2zyaGfJe2uXZTOsPyLc8rVVlD9GqnKtCCTSYP4ibr2-jzfqOqRhhbQvK2Ao02AUkxmR30evezuzP8umXOpG6YpXFUNn8oZPe9KTh6Y70VMnNJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=cpE-bgvFKonoI_1Gc9akV12rlqYGNEqqhXT66dA9ybvk9fnjRQn8FqDV0SOa2eb1LVAkDOuRnB4pb1weXc-NBZESN2crtfjIq4XqzeNsetWuxrTC6tHhmdUkbz6jSfPd9ypnDGVFNzFB0tXEm7Qyfe28uzvocg9kbBNoZOV8LX6BZ9ysamI-HbbxBZ7-_9edqZ3Q44_yR96B-hugyGKOgadScj65lGM85gKRg_G2zyaGfJe2uXZTOsPyLc8rVVlD9GqnKtCCTSYP4ibr2-jzfqOqRhhbQvK2Ao02AUkxmR30evezuzP8umXOpG6YpXFUNn8oZPe9KTh6Y70VMnNJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9au3VV80xM9yrk1qfHmIMOZjQ6v-MmFX4_ZssEJiPgfaKfWtIFTQaLh5t-0JYNNJbedQHAoyf6lHYDC9XkIahXnmAuovQUKxXfBIMxJVSeHcmU5BifL9KAVZTlESaXZnYau00GX1LBT6nA_i6Aovv18JTxs61QvagAPMfUNcsgeJ3QtukG19T1etOnSGGMJQDEWtBIb8hxgGevxAA7orf-QtYDv31L1K0Bw7xYXtbD2JYAMoIT3av76PRSwa-YbX7Bpzj-V44li522P0yR0QPRf2RUoZTXdV3ZcOxLtMxLtkHFBbsppkt-FlVKh8PkCEOHiR3OUsX8amlJSqMOw6XCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9au3VV80xM9yrk1qfHmIMOZjQ6v-MmFX4_ZssEJiPgfaKfWtIFTQaLh5t-0JYNNJbedQHAoyf6lHYDC9XkIahXnmAuovQUKxXfBIMxJVSeHcmU5BifL9KAVZTlESaXZnYau00GX1LBT6nA_i6Aovv18JTxs61QvagAPMfUNcsgeJ3QtukG19T1etOnSGGMJQDEWtBIb8hxgGevxAA7orf-QtYDv31L1K0Bw7xYXtbD2JYAMoIT3av76PRSwa-YbX7Bpzj-V44li522P0yR0QPRf2RUoZTXdV3ZcOxLtMxLtkHFBbsppkt-FlVKh8PkCEOHiR3OUsX8amlJSqMOw6XCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Z83Ir-7xJyT1Ky-aKxZxcZeY5aGsWUD22qRkYPdWAcDuoVX-7H5KAFuS1FuNVmnhz-1cfCv6BIlXyi0GkxawzKFDsn1ANP3eP6dD2z8TrKTLod_xECjjS1kPPfLmTCCXhjfKMgEzVPwwyczZftBKtfh5sslS2xBZqRy72IIDxGSNtJikZ2XEbXCyYB-dAozkj9UFPVXMS65zIzRNbfWoNDd-hlzEtX1EmYmNcfhxinAOAJSQrCromuac87VVKoL1D3SDLBi3HX9d-uMIyItuTAadvofkMdKZvovYDYbmUgREp1kEk5lDkVMFQZJTJujpsmByiaLl9RgfpfkGjRy4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Z83Ir-7xJyT1Ky-aKxZxcZeY5aGsWUD22qRkYPdWAcDuoVX-7H5KAFuS1FuNVmnhz-1cfCv6BIlXyi0GkxawzKFDsn1ANP3eP6dD2z8TrKTLod_xECjjS1kPPfLmTCCXhjfKMgEzVPwwyczZftBKtfh5sslS2xBZqRy72IIDxGSNtJikZ2XEbXCyYB-dAozkj9UFPVXMS65zIzRNbfWoNDd-hlzEtX1EmYmNcfhxinAOAJSQrCromuac87VVKoL1D3SDLBi3HX9d-uMIyItuTAadvofkMdKZvovYDYbmUgREp1kEk5lDkVMFQZJTJujpsmByiaLl9RgfpfkGjRy4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0drrLrri23AvJd543XuKxag92AqjFFGZYzdcE1Hl3IJGGrunqS4UvJVtXbIZQdIQKZJxk3L0m7qouy0ir6RnLaWo5OR3hHZWNArfHN0LxDVtxc2G344O-vuLidaWQvk3HOHk9_GIYYDw92fWJm1zkpW35XRF5DfUvhGAP7sSa6t2md72x7VTx1enGNTxaIGoFfV8jZ88aoRR-ggzUt5B7ecnvVE3HJ692NPxfM1k4ub1WYD0eP8G9ki4EQf3DnlibcRbNnyPJd_I0vJqLu-4y-VzwFxFD-NeCUujZqBpZqwC8D8rzDzS-d1T9-2wBSQavJcy3IITDiNoyHe9ycqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=PJTMu3gekctm_4VEXeN-dXTBdX5CwfPpNuQUvOHnhdJO0dfnC-G9y6zh-vqyrQcb0ae1c35XjRcH4CJ_1iHdatN-NIXFcOOg_xme-kXXsaLM9G-Ou93pW3Yvk5Sg4ZxXvOCo7pKxZpJCdq4ouViLXlZT5h5vzjf-FdJKTo-a77N0HQ1Ma3_bmF5l0V2teDEt3Usd_H-LlWSK9_mHrxe4kHWHiD6LLI1zxxd3odc3WjQIrhuT-dO3dGjslFSxIbTlb-nA6WAORUMa2mg85vehCPqabfzRh83R42MtZmVPPMxb7PSJXB9wg0nGm6YBqbXsZnm8fB9cJx7eM4av3XwN9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=PJTMu3gekctm_4VEXeN-dXTBdX5CwfPpNuQUvOHnhdJO0dfnC-G9y6zh-vqyrQcb0ae1c35XjRcH4CJ_1iHdatN-NIXFcOOg_xme-kXXsaLM9G-Ou93pW3Yvk5Sg4ZxXvOCo7pKxZpJCdq4ouViLXlZT5h5vzjf-FdJKTo-a77N0HQ1Ma3_bmF5l0V2teDEt3Usd_H-LlWSK9_mHrxe4kHWHiD6LLI1zxxd3odc3WjQIrhuT-dO3dGjslFSxIbTlb-nA6WAORUMa2mg85vehCPqabfzRh83R42MtZmVPPMxb7PSJXB9wg0nGm6YBqbXsZnm8fB9cJx7eM4av3XwN9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nJp3nzLLZe-91jgskg2U0CCNGp8TMTQzcaLMRasT4w4AE53tNjE_I8ss9GiEn1q2QYNY_maQWeP5bgIrnbvxKINDjacjKstss_gqtrioSVYBE44RuVz57MrDIqGW_ec-hgHjMcBDx018sDurU5XyYjQxLQ6ajLsdNwcYifTg9qaiH6BbqMq2iYR9yCKkaeyQRg0NIIyTR_nXaU1-ZwHOr8owMgz_QN6qHge8mskSnmGgX3tQ1aU94h8GgL7hZpHJTNZ4d0WpRbkzV8EPzLAmpaDEIYfeC5Vc_mLEbr6hXmk9rnFQ8L10_z3s9nn1JV5VnjWfzqVbXeSy5YtAqDRbDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nJp3nzLLZe-91jgskg2U0CCNGp8TMTQzcaLMRasT4w4AE53tNjE_I8ss9GiEn1q2QYNY_maQWeP5bgIrnbvxKINDjacjKstss_gqtrioSVYBE44RuVz57MrDIqGW_ec-hgHjMcBDx018sDurU5XyYjQxLQ6ajLsdNwcYifTg9qaiH6BbqMq2iYR9yCKkaeyQRg0NIIyTR_nXaU1-ZwHOr8owMgz_QN6qHge8mskSnmGgX3tQ1aU94h8GgL7hZpHJTNZ4d0WpRbkzV8EPzLAmpaDEIYfeC5Vc_mLEbr6hXmk9rnFQ8L10_z3s9nn1JV5VnjWfzqVbXeSy5YtAqDRbDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vf-iUGHsOZmH53Ae-D0HuqpHm3KvPmvdFkImMAL0pygh4URX1y9w9DM4ToTfpVu3zXVIJVv-8M-oKD88GeKZRUKJIBcbsOZxQHYNhM7UnYAv5R6VF1CQv8jEiq3dvMQTWp4AjGP-gCiFFupHEY7O-O4uOY02d1L28W3BA7AnwP7SMYG6wB0iiG6oDwF6bbtk_CMVvzx7CsImYg7RXzylx2-4N0ksfE_t7GB0VjFwcVeEfJQhT40K8Ufakw2mNlIt-MkdrVps7oACArJU3xIaSE750Vn1KRHGySl7UOmNXSppIM_gxVcmgDQbnRp5sqwiklOwAmXlVSHSEAG59mx5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vf-iUGHsOZmH53Ae-D0HuqpHm3KvPmvdFkImMAL0pygh4URX1y9w9DM4ToTfpVu3zXVIJVv-8M-oKD88GeKZRUKJIBcbsOZxQHYNhM7UnYAv5R6VF1CQv8jEiq3dvMQTWp4AjGP-gCiFFupHEY7O-O4uOY02d1L28W3BA7AnwP7SMYG6wB0iiG6oDwF6bbtk_CMVvzx7CsImYg7RXzylx2-4N0ksfE_t7GB0VjFwcVeEfJQhT40K8Ufakw2mNlIt-MkdrVps7oACArJU3xIaSE750Vn1KRHGySl7UOmNXSppIM_gxVcmgDQbnRp5sqwiklOwAmXlVSHSEAG59mx5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=vWeqh2_a-eGcaqwSpamZqh0tnn06jKYTHNYul17SzbBNCljgi5R5oFB_Faa1Zf3jPwcwR1nJLUwQ8YTVhuvqXAVimhRcYOC4eY9lNx6ouc78yeF-upIr1o_5RiDei2l43i7UD5Y6aXmTVT2yltw83e6qX3p1Wo3QEOaU3pPvrHsPIN3l899RgEcas3jbOsWf1yr_HhD1KmlEXdiNG57-0DuvxV5EmB4EUqoJmNHcXnIKXqsEjYJjG7MDWqXkoyAneTmVBS2Qun44DIgN3oxtCXPDP-MHb10mSeZan_Ar3D8HGYgxtBLNZGfTwF9WmIkqt4E3VDpeV0rxT2aUwe4Zlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=vWeqh2_a-eGcaqwSpamZqh0tnn06jKYTHNYul17SzbBNCljgi5R5oFB_Faa1Zf3jPwcwR1nJLUwQ8YTVhuvqXAVimhRcYOC4eY9lNx6ouc78yeF-upIr1o_5RiDei2l43i7UD5Y6aXmTVT2yltw83e6qX3p1Wo3QEOaU3pPvrHsPIN3l899RgEcas3jbOsWf1yr_HhD1KmlEXdiNG57-0DuvxV5EmB4EUqoJmNHcXnIKXqsEjYJjG7MDWqXkoyAneTmVBS2Qun44DIgN3oxtCXPDP-MHb10mSeZan_Ar3D8HGYgxtBLNZGfTwF9WmIkqt4E3VDpeV0rxT2aUwe4Zlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_OEbuI0wS4FGAEYR1msWb53dicFWbu9jZlIt0JT2AEHfcRlJLzdkLhnsfbAwLisvqs3baLvrlsdjmCo_BVJO1V9XFu8jusRzrTPVvkK4d4BMwyc4owXSw8hqv3PLWEA1ZsSHWHuqErDO6V8xVca4GiH6GQoEzN7j1mQYrX1e_tmub2QrfDLbb9sKTljqi991FGQSKCy0dmeM7-z_226ae-FYJGUK4g2h20smnpqBUah9yDVNA5HJPXNO4FYQ6YIolAooyWBXfIFWgWBdX2p1klVqlnJHUdzMJhF3OT9TAhd1ci4rqi01j7BVkIsbxFfmZ_OxiF2zsOlvRJDPgIaLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=me2fJfWZBZcOyR0nb2tdwfAgZsICnyaTFzUbvyvawYmw1mfyFv-WF8aXpv12HU07poFO0q8CBYYR3ZEPJLfEE5JrUQYtaGBmsxYn3BS0_IRHc04n6GgezGaFinP01jbVimDbd1C7FbCvyPDnWBShR2yXG9P8y1nNOhwmm0fPx63khslwlJEyE20R-GfKoAAJVS2Zzr9YjS3pAL1mtIQ5XkM5u-di4cQSLpnngTQs4zhzwqrntxLHfMzQqbNDVvYOOOpyCV0TAuUAu9GNf67B0VotbpuUcp1lSwLqkmFgoluHL3fOcbHi2WHU3VdNlmLfVzGkpY5rbG2NyAbOyQfTzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=me2fJfWZBZcOyR0nb2tdwfAgZsICnyaTFzUbvyvawYmw1mfyFv-WF8aXpv12HU07poFO0q8CBYYR3ZEPJLfEE5JrUQYtaGBmsxYn3BS0_IRHc04n6GgezGaFinP01jbVimDbd1C7FbCvyPDnWBShR2yXG9P8y1nNOhwmm0fPx63khslwlJEyE20R-GfKoAAJVS2Zzr9YjS3pAL1mtIQ5XkM5u-di4cQSLpnngTQs4zhzwqrntxLHfMzQqbNDVvYOOOpyCV0TAuUAu9GNf67B0VotbpuUcp1lSwLqkmFgoluHL3fOcbHi2WHU3VdNlmLfVzGkpY5rbG2NyAbOyQfTzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=g9OpocuoOxhJaa7B-i3iM_PfZTvaNAdHK1sSEwa6JnzGAu-i00bH0N6DLKJ5HxNCWyN3nBzHwM24ucKgfkEvyVu-K78QvVXj69AkpRmYYj-xb2-qqi1o3_HY5oGo30qoGtamclsUrmvXTn12zPaEvSPZZ3eN-jlxxz8PF0hatqpNcbHX09tzY0VqU3AluI5rGZZ5LLWKnGMAJsuZNAyeJzeiwe5qRpAUqFu3ZklYnOfkhMmK6dPAJR9E76Sz4dCu-bUWmmCs0exwk5ZsjA8DSbrhXfjYG70MhnkLMaI6P6zGNtuTelrJJqRacb1aFP0c09pXx3OT2K5Isqyo5lqlVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=g9OpocuoOxhJaa7B-i3iM_PfZTvaNAdHK1sSEwa6JnzGAu-i00bH0N6DLKJ5HxNCWyN3nBzHwM24ucKgfkEvyVu-K78QvVXj69AkpRmYYj-xb2-qqi1o3_HY5oGo30qoGtamclsUrmvXTn12zPaEvSPZZ3eN-jlxxz8PF0hatqpNcbHX09tzY0VqU3AluI5rGZZ5LLWKnGMAJsuZNAyeJzeiwe5qRpAUqFu3ZklYnOfkhMmK6dPAJR9E76Sz4dCu-bUWmmCs0exwk5ZsjA8DSbrhXfjYG70MhnkLMaI6P6zGNtuTelrJJqRacb1aFP0c09pXx3OT2K5Isqyo5lqlVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-Nm4MDvfXifTKrxHZ_4WYLBru9obDu5ZijKqyGxNVk6Y6WEiFKdhZOYnnzqkc1Pt3bJhLJrjov4Rshz7IXIzTyrvzc4VYkL82gH4lFUoPuwbo-29fwss6EUxjis9uL7R0DwPiEFXjo2QSmfKMM5W73Vn6W5mUihQZ5pN31Nnv2FiWn2pqGLNSAl-HNtOZVmV3qAVrXxL-DNKw_PL_rwgkxxw6mJ6WwhUSXuWvesy1OezopX2z9k0mtgjR_xuV0W1tDcqYmsKxQMoQDPEGe4Oa-pjjGqDvpkYw-1Pfb3hhNChUczRXWizwdEM6mjf-OUVYN6SVtkBStNPJFv2XxLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=QuB2HrDSwAANnvPCePgLVRikkHFUZH5YPPy7cvUHfz-kZ4CaKBvcYdh0cR0F8SQGSbFwdiWjYFffKgxxEhIzbXGR6SqM7KwZaQrp4wS04DBW1pFo5HphE5hoDhCRFLF3H0evSFfB7bmGWjmgv1kUR5s6ieqmdQR14_AzTS-CfMXuBmJduXtw6IE75fSkW0PKP4tKXTVBuYYpYD6pYblLXzK5yYabEiLIfjGMxYgt5gCH0z7HHui8eBYB0Eu4sRdZzIPDJ7yZHfCmIFPClIKVW2etwGs7EC-E6qp9Tp6xOpe3lDX6BAIwq5K_46xxF9VgjGPHeRyT8jV8psSmgJfixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=QuB2HrDSwAANnvPCePgLVRikkHFUZH5YPPy7cvUHfz-kZ4CaKBvcYdh0cR0F8SQGSbFwdiWjYFffKgxxEhIzbXGR6SqM7KwZaQrp4wS04DBW1pFo5HphE5hoDhCRFLF3H0evSFfB7bmGWjmgv1kUR5s6ieqmdQR14_AzTS-CfMXuBmJduXtw6IE75fSkW0PKP4tKXTVBuYYpYD6pYblLXzK5yYabEiLIfjGMxYgt5gCH0z7HHui8eBYB0Eu4sRdZzIPDJ7yZHfCmIFPClIKVW2etwGs7EC-E6qp9Tp6xOpe3lDX6BAIwq5K_46xxF9VgjGPHeRyT8jV8psSmgJfixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=m-7fpry1LBFMguPNayhwTbznsdcO2sXCj9sp7SGMsE0xXSgAz_gK4fzf6p65Z8UeIhaDUwkdcAvNQwJIzgIHOd2_8pfgXjgG282fJxkDHSYrA7APwhWFtbNa0jQsJQNFNP48_gUW95zBnl3rFXkFjI4xSZGQidSbeVtslAfvJIpccC0t3fk06a7MrqEkZYGpHYIc8-OyQMyZSgKLCdGm0vw9B62DKbX108uamMjqKw7jva19WrQvf5rclk5axgb2uGKnKGQP0T9Yqo9XWvfY6LbRgPxOFhP6ZuWtK9w7f8qn0jWmF8mkZNzvuLRXe-3D6GzplNob9MPKyXkGwknNWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=m-7fpry1LBFMguPNayhwTbznsdcO2sXCj9sp7SGMsE0xXSgAz_gK4fzf6p65Z8UeIhaDUwkdcAvNQwJIzgIHOd2_8pfgXjgG282fJxkDHSYrA7APwhWFtbNa0jQsJQNFNP48_gUW95zBnl3rFXkFjI4xSZGQidSbeVtslAfvJIpccC0t3fk06a7MrqEkZYGpHYIc8-OyQMyZSgKLCdGm0vw9B62DKbX108uamMjqKw7jva19WrQvf5rclk5axgb2uGKnKGQP0T9Yqo9XWvfY6LbRgPxOFhP6ZuWtK9w7f8qn0jWmF8mkZNzvuLRXe-3D6GzplNob9MPKyXkGwknNWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=CS4w5dQsJJN_PaszmhCbGOSFX3QE_CRVfC52vixqJshJB78mdhrzgZysAeglFCJ8HAfigqBVRrk5UJfF54ouVr4jP1x9K86cPW95gKiHj_7WbW9DJa5LYgfCN7CFeh_9VrkBQnEKz5aiVRgj9sNaYri00D28MXpXP6KJIr3cm8LDe4p0HR_Ae5dSlUnTtc-AJi-NpD-Irszo7g-aITFo0q_2SEQBnP2-elTgZLHyJ2_57a1usiPuqkl4peuTITzYKfW8aeydM6nl8ejA1dofu0r0UEziaIub0HGdL3VEA2qsuAHDTcJC7T_NdxHNYceOodalphlP439oBl8KCoVL-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=CS4w5dQsJJN_PaszmhCbGOSFX3QE_CRVfC52vixqJshJB78mdhrzgZysAeglFCJ8HAfigqBVRrk5UJfF54ouVr4jP1x9K86cPW95gKiHj_7WbW9DJa5LYgfCN7CFeh_9VrkBQnEKz5aiVRgj9sNaYri00D28MXpXP6KJIr3cm8LDe4p0HR_Ae5dSlUnTtc-AJi-NpD-Irszo7g-aITFo0q_2SEQBnP2-elTgZLHyJ2_57a1usiPuqkl4peuTITzYKfW8aeydM6nl8ejA1dofu0r0UEziaIub0HGdL3VEA2qsuAHDTcJC7T_NdxHNYceOodalphlP439oBl8KCoVL-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxSSArGDzLiinAQ_pJvF8m2DXcHvQr-ijTYHqb6d7TAqsQE4OB0WxB6n0YsaU31JBRAe8zN1CfgZmeaETwqIbmR4cSj6YG-3UgepAYzj8gQEapjwv2z7lSj-O6Rb-_M5nOuBPFNloRZtwq6Gf1yQjofCMuqgrYebIsgvBxRTaHkM1t0kCr_1dE4mG-5G5lSFsy1_Sz-CCHIz4b34XCq5V3Hq68Ejjp-f6oG4xghjf-7C60I4RLNxsadUoVt92BgbVfmfoIOpQUhW5jeUrx-DQVzQjxWX23Xnd0Vctn1ghgCi1Innv4Q5BScPMSc0psP7l8ndac19c7P3HbJaXNQK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLlBJ1_Q5YXJVLnzxgYEMqwi2kXqW2Zvx3MEMAZTox7fzp31ciHJMyVg4JtRZOkqWuSSfhLcmW5nvP-XeuEpCadXSDNqvo6BgHpdGUqVEHfJI6HqSi8-LJTnFw6Weri9hNAcYizJlyJF52w6uxGUzMvS0uCFjFC_YnhnQ2OQmnBei3vxlGGY3NRVUWJmSss1mKI786tfi_wgDGhupac11fFg7XdOp1ILfaTwqziQmvPSzkDd4vD6FOcAV6cn_LXgTWdXLf-ptuWtyWKLG7Mj6MMTvV_uoD-xKnKjoiMn54tNhx35ismip_s_9vmoNyCA-z-rta4sZ9B-kMTKTz_5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf-tyIbqeQmbIFNzv7tlrYAswop-6hmkrDnmI7XP1UFaXAEgnZLoIhnvC2nbXauwf9591HqfBddsMPcrp5BomNODpS6UnsfLTcnEOnDMl5uaEySkQsfjJZ5_LCGLh_ttjso4FDfGR3LkK7KsLE9-6oHL6ai2mskJhfuLUJWH3PzYm0XkB13Yrn5iubI0D3TzPparjgPY7d61rKXMzWmlk0DP4Dqyh7P1bpmYtmtK0-sovoFAugZ0a_A5dQgC5Ip-82K1e9dDSouHZEsijRvO413lzNvuSPdV0rByTpAp_0FoPSzTQrYMcoz_uQjquFpmyi_obLWmOnHY4afHC4AM1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=RJlwIEUfopTWIfeAkcAr8hbUe7SCqeDG1rE23uO6hlPXydqBnw4-Ky_PwoouJ_YLsK5fJ3Vs7XHXQ1vCIEDcFXS1mopjWud6RcXVv1FUoUuktQFtbWPMyMvNkzRTLUGSBiyy9weyLxr5NGO0iakzeS9rmw-1HlggresKparziuhri6XsZFsUYCWtxuKDDw6pOM9GcVmoQIl8AeL2lSdQ_frJxjel-blfaGD7ufHSIph755iozqqhPQGBM6q4N2a15i0FfYD8B30p1GaoiCV4HL5yeKkWhFL1QTJyufLHYIj-LMo8s5f5iz8oP_IAWEurcz9osmKS_IM9S96ncCn4Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=RJlwIEUfopTWIfeAkcAr8hbUe7SCqeDG1rE23uO6hlPXydqBnw4-Ky_PwoouJ_YLsK5fJ3Vs7XHXQ1vCIEDcFXS1mopjWud6RcXVv1FUoUuktQFtbWPMyMvNkzRTLUGSBiyy9weyLxr5NGO0iakzeS9rmw-1HlggresKparziuhri6XsZFsUYCWtxuKDDw6pOM9GcVmoQIl8AeL2lSdQ_frJxjel-blfaGD7ufHSIph755iozqqhPQGBM6q4N2a15i0FfYD8B30p1GaoiCV4HL5yeKkWhFL1QTJyufLHYIj-LMo8s5f5iz8oP_IAWEurcz9osmKS_IM9S96ncCn4Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVWWVrRj5H2Z_q8bFnmvVQypTb4lQLseTJeScNmcHd8X5uNTy1ATiu0CSPxjP-VN9rD_eNl6569y33nJL4ET2fZow7twaeyvXD3fijIPHimsF6msxvEmQKPam7aE-Dac0CLT_tO6wGcDYNE20NqSmgoliouus4PAE4lv0To7f9EPGgbnNQf2s-ONWMyS8bUfjHMXEgKiaXHmLXJWDxzNtSV5UmYtr-juzBXQ1JZTlgkA1ZLUXg1oxIMGiHitkWv42oBZNrxDXL5d9LEcMFkCBhqX5TQwR76Bh1wKa1qNC1odLS066Zt8qK1GKSVC_shjG5YeluNNt2HReiHcFR9GlGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVWWVrRj5H2Z_q8bFnmvVQypTb4lQLseTJeScNmcHd8X5uNTy1ATiu0CSPxjP-VN9rD_eNl6569y33nJL4ET2fZow7twaeyvXD3fijIPHimsF6msxvEmQKPam7aE-Dac0CLT_tO6wGcDYNE20NqSmgoliouus4PAE4lv0To7f9EPGgbnNQf2s-ONWMyS8bUfjHMXEgKiaXHmLXJWDxzNtSV5UmYtr-juzBXQ1JZTlgkA1ZLUXg1oxIMGiHitkWv42oBZNrxDXL5d9LEcMFkCBhqX5TQwR76Bh1wKa1qNC1odLS066Zt8qK1GKSVC_shjG5YeluNNt2HReiHcFR9GlGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=HeGDSd-e8rmCzQ7YJ5cXNlkgtDNBsUnWOBV6o8_2pX6P6-m6XChE2i9AWcYOSWey-cnJ1OFgLT4A8MFlnYdxQi5_TkjPGLYB86Q04EXwKtbH_QWu22-M-o1LVKDJ5pZPu5YP97-goN2VwIK42En61oXk428ZSi5YW2GzUuoe5S5TxxElLNe847lzFIVtZVN-ECdkQ80T6Avw1nqgTbLEukEYeAR63c7RdGt1snDBSqGRp7Vr0OaU9r48laePEjXjkHgxCTaetWMyIh4L2cimkArDGZsrwrWFpWXT_73jm05TzgubhyAzypKG28xa7sPGaxCVIGP5jiTZoguLOSSdHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=HeGDSd-e8rmCzQ7YJ5cXNlkgtDNBsUnWOBV6o8_2pX6P6-m6XChE2i9AWcYOSWey-cnJ1OFgLT4A8MFlnYdxQi5_TkjPGLYB86Q04EXwKtbH_QWu22-M-o1LVKDJ5pZPu5YP97-goN2VwIK42En61oXk428ZSi5YW2GzUuoe5S5TxxElLNe847lzFIVtZVN-ECdkQ80T6Avw1nqgTbLEukEYeAR63c7RdGt1snDBSqGRp7Vr0OaU9r48laePEjXjkHgxCTaetWMyIh4L2cimkArDGZsrwrWFpWXT_73jm05TzgubhyAzypKG28xa7sPGaxCVIGP5jiTZoguLOSSdHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUqihMKVLPO51qz_56Xb6WMO_Btcghb8gXnMvTDdk6J8wgbxvoxlpJzEMloXRx_GTJ2tKPc54IPBj-Iko_94nY2koqkKX5E62Twu1us8gg6XTOq9fjH7jWesKD4zKy1RGbF_LB9Iogcl4DJOLEN3HruB1Ts1x0BnvP3fRdG1ArI_Z1_3jDZkbyO1FZc0_ej9PJ6HNC4r9aLxOhBd2uwgED0t5EdNMZBlQga3KG6sf9r0jUVZOA4O3nAFKDBFVx3GmcAX6zrbqwgvOACiWVwZA_dKi_XIPFf8dwZs0Gd3UV2Md0gyQr2rknCyf8R6muY7JT24NNtowyG8J33H0oK7_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkIde2q63n48iFM7rUh2OiBtPq2s_m9ywLhxEuOTdgPRG6tAP3OBfh9Hx45iLNHhx1OeRA7ZKTw4_EvFmscdzVVan0m4P9M8EX2BtAFE7lPe2SAc0m_6h7qQyD4o20dliaS3f2SYZB5Ydcqn7wWkCv_X2pv3gizSlvH56XOd6iFyE2n91gYNTTarpfCLk1kW7dL6Cgt-g5Wpg1p5b-bkhQFDGneAMxlOdN8bgF_fO9nd6NT6_CTCzZUbUlWYBc9agKL1jpgCg92HzMfg5vH8A_OFlVUDvk3TpNDb97IB0PAjleJkXpjn-VM28Dt4w784-A1dDM9rrPhb7NpWmqiT0To" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkIde2q63n48iFM7rUh2OiBtPq2s_m9ywLhxEuOTdgPRG6tAP3OBfh9Hx45iLNHhx1OeRA7ZKTw4_EvFmscdzVVan0m4P9M8EX2BtAFE7lPe2SAc0m_6h7qQyD4o20dliaS3f2SYZB5Ydcqn7wWkCv_X2pv3gizSlvH56XOd6iFyE2n91gYNTTarpfCLk1kW7dL6Cgt-g5Wpg1p5b-bkhQFDGneAMxlOdN8bgF_fO9nd6NT6_CTCzZUbUlWYBc9agKL1jpgCg92HzMfg5vH8A_OFlVUDvk3TpNDb97IB0PAjleJkXpjn-VM28Dt4w784-A1dDM9rrPhb7NpWmqiT0To" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_wNUb6MlNEXndw1hVhfQtl8WDo8uccaRKwcwYP2z__Jfg3qutO7LAQBxkD3Ob0LKnoFQMZL_cAI1RJL_GynKhARlYFKPyeMFtSfyi2xwHr72hQ62hoeAFI8ozJOE9uJ7KueQ3gnlBaegKtnHZrK0kYwTIMHRAITY1PoFthrwQdGNVSk1mKcsG9eRZw4Z0Zm4pXGu3ZkuNqm1-ff6OEt4fio4pNr842wDVrTOgyEyizay67ORfGjQhLYSwmA6ZTUVcyudUmlLC-cOlF5BVyXmV8SEJVpy-XRcVJaxmVHDvvx-KW5g7u0-Jxw3dsnWVBv8_br2T945_4Tj-a8HZCi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=itoOQ0taRMD1g6eqGvZYJQtjMlMjTdPQUdw0y5ciMTbSt0PkCb-iK1DSfKAJcvBygayUFK8qWUdId5MKCZYb-9Dcyc3jS1kGciH9LTDCvqepLAgqliqLUkgQv7HwjyC7CIpymTPDTUdalmYrCtrvbkyfDIETb7K0hCLsaJ5YGEgIZA_IYlYZpdOWDi8lM_SjZ-v0EBfkWYiaFCi8Nv9u2G09cEcbSJ7-WwbQexvZtxxcqhB1eEUlThBrdHCxAezmDdw6cpTXX25GvPmhjM_mn7y2zAzgdQQQneY31FCfQxMbP4KXA5wpxT7FGOALUZXaF-HqV85a2HDeSlZ2Nl1I_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=itoOQ0taRMD1g6eqGvZYJQtjMlMjTdPQUdw0y5ciMTbSt0PkCb-iK1DSfKAJcvBygayUFK8qWUdId5MKCZYb-9Dcyc3jS1kGciH9LTDCvqepLAgqliqLUkgQv7HwjyC7CIpymTPDTUdalmYrCtrvbkyfDIETb7K0hCLsaJ5YGEgIZA_IYlYZpdOWDi8lM_SjZ-v0EBfkWYiaFCi8Nv9u2G09cEcbSJ7-WwbQexvZtxxcqhB1eEUlThBrdHCxAezmDdw6cpTXX25GvPmhjM_mn7y2zAzgdQQQneY31FCfQxMbP4KXA5wpxT7FGOALUZXaF-HqV85a2HDeSlZ2Nl1I_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UrjZfD9ky4QqxYCc10Tr3580iPfv9eqzmMI0RBFG-kBPiaT-t0_8PbW_qake52mnKtZPnakvyOqUq5rUwu2tONpnooOwdN4QgBmp2Om__7b05v_fXGA2j9XJ_-ardHeFrHdjnBgbtpP3GvtMnP-_TVV5tRfignyP5OfNdxd1EZ8aX_CPrB8iVxCSXXG3i6qIrr78MkrjgAOfkQlbF-r8QOess40EhEJaSZgfEBw5-xJEPgsxPaomLhGLk28kD5FtKnHH2p1hecYrSYcQhV9qXTPTPM2inJnDdAvi_sFXRhnKBSxEw1lGHBFMA6FEh8AVGg_N5DSKbaXgeoReuYu3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UrjZfD9ky4QqxYCc10Tr3580iPfv9eqzmMI0RBFG-kBPiaT-t0_8PbW_qake52mnKtZPnakvyOqUq5rUwu2tONpnooOwdN4QgBmp2Om__7b05v_fXGA2j9XJ_-ardHeFrHdjnBgbtpP3GvtMnP-_TVV5tRfignyP5OfNdxd1EZ8aX_CPrB8iVxCSXXG3i6qIrr78MkrjgAOfkQlbF-r8QOess40EhEJaSZgfEBw5-xJEPgsxPaomLhGLk28kD5FtKnHH2p1hecYrSYcQhV9qXTPTPM2inJnDdAvi_sFXRhnKBSxEw1lGHBFMA6FEh8AVGg_N5DSKbaXgeoReuYu3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=W3_1m5L7C__A5fxT_J9oRJF7Le8qSHedr0uXLgDru5AzN4GtAsVSnTdklZLY6rqtjCoaKzvDCUVUJ0LfQvVYryACxlWwoS4ypTluXQWcGuTZILihRPJ_t3WGZypj-N28BdB8ouWGIguMRbU18ZOXbmQr96DhPHmsZU2Bnu8GoZLVW7bCLqu5zmOhADATBIy7OycwRqSnrF00mEianQkOoWbTDeXyFmaGNChVrZtCByk4uNejSEamHNWhJyhOWMC4nYL3clGCIbe6p-XPg1ZvCimAql_C-UR0wgfFueUlAzFH_JV0RV_eOsXEmnLgJzyKWaBSjyNA6MgK95ocJVFWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=W3_1m5L7C__A5fxT_J9oRJF7Le8qSHedr0uXLgDru5AzN4GtAsVSnTdklZLY6rqtjCoaKzvDCUVUJ0LfQvVYryACxlWwoS4ypTluXQWcGuTZILihRPJ_t3WGZypj-N28BdB8ouWGIguMRbU18ZOXbmQr96DhPHmsZU2Bnu8GoZLVW7bCLqu5zmOhADATBIy7OycwRqSnrF00mEianQkOoWbTDeXyFmaGNChVrZtCByk4uNejSEamHNWhJyhOWMC4nYL3clGCIbe6p-XPg1ZvCimAql_C-UR0wgfFueUlAzFH_JV0RV_eOsXEmnLgJzyKWaBSjyNA6MgK95ocJVFWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0HbJl3VRENcdMX_aKGvB36bv9bE_xfCqiTiZznRP833QxqJjOlL3BfGscqZ3RC8_hVpd6KOXTw0AhBmmvjy9Q1gi5n4NbcnY1AtEoE44Bacjtyvv5BY09XfyHg24gLOKVPisOY-Iyo6rFDao6zsib9JuhDTP5cdk2zj4ypj637uTekYKX3iFQwxaqFVtJiIUlZGdXymZ4_NZ1rjB14nzGvvt4ugOORIC58c6NgLDQJkzkLV4H-cJ5WF2HYO-4DPGjxjySnKVTDMGmhkPJPJJ4k_Usp-EOhoTkKmkfaab2qImurIGrFzZWsSu1ozEvyshXX5Y1ZP3r5ZVMs4W3jlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kegjOzLv-jewIrXZNqLC62tCqNGfiwly2S2MS5xxpysifNICrqPwZUcVoX3dRHvzfiC37TrFDy7vX2g_qWWTx9SWo4rH6ZULFeB_LJg4gvjX2DLSVvnEzUE2GLUL4wseNnntGL9ARK4wGfOwDswHHtdCaPjqtx7OxoQn6pY_V8BiKpBPzfS0dmzVx238i1v2JdgTWBPmBpT3oIo6SLVNkQ5ZSUEhy3xp4W-q0-CXUGuyh95xLxkW6XX6heGpNjYIfT99mqEAWOKsvUq6zBuUlb08k6CRewVQ0b5V8I1lw113PbsvM4AV3r5oVChTmQjjYnt_kzHULeRCy86o0sCkNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=pMas7edb1mkvzi37vaS1mB4bN1qSRyWN53ml4lvfihWVN6J-Qs5s7BlaFC5FAylfjiiETO_jNOSY7-oGzYbFj5nR15MsSYig6iJBM6zj02BSK1QTicIh4TohBAs32ZzRaexUsx0htuonSlJaSGCjP5P8B8zpC9xr2EndH_8Gor6i3tYANuXvGgWj2ztAiCAHxi4-ZL_zB-tZnWMu1zaIOT2KUsRvLCVE5vgGO5L-Co3V_e2of0eqFgiNf7KvlH6Ujeu4ibdhNrDfG8HKSlWSB2loPAfLcDm_1BPM2baSnQmp5EFkhBS-0K78wQ4QlyllJiXa1TQiMsIT-o_wlVUovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=pMas7edb1mkvzi37vaS1mB4bN1qSRyWN53ml4lvfihWVN6J-Qs5s7BlaFC5FAylfjiiETO_jNOSY7-oGzYbFj5nR15MsSYig6iJBM6zj02BSK1QTicIh4TohBAs32ZzRaexUsx0htuonSlJaSGCjP5P8B8zpC9xr2EndH_8Gor6i3tYANuXvGgWj2ztAiCAHxi4-ZL_zB-tZnWMu1zaIOT2KUsRvLCVE5vgGO5L-Co3V_e2of0eqFgiNf7KvlH6Ujeu4ibdhNrDfG8HKSlWSB2loPAfLcDm_1BPM2baSnQmp5EFkhBS-0K78wQ4QlyllJiXa1TQiMsIT-o_wlVUovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1H9cIVjhthwbc7-RHr9lKfdtFB_hUSxNRwJsVvGiEOUkZfpEKSC4536DEh_CodQY22NJ5T7JoBIr4W6Ao9e01SD87p6n9XavsnclDa-akpCUjKPJ45xE0LUKaLnHbqAgbD4qZGalz-lzkyk3uYPUBK7DPr7wJIXl52onJ23b9HbU2cyF5MOvWrkzVwOV56FuTfEvehjtCw1rpi4lbh8L5mxTewsgI24YH0h7A9KM_dRpo7yDA8XvkBYcHVDiaHtvF1NpZ5T1qW4KFRQMlmgSyu2gjT1dLoP9wPXAyAZg__g0238rjJv9PDEjJsoIVaDo-_i3--R3GrJxB88gN8ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBgN3jqeuLb_jG4uPRp-rXKgC1GF1X4wTs0-N73u34eFS8dqVsZ1PspIAfC1f69470A2C7TuA3YhzBAdRoC6oHKiex-TH7TWjEhWCQLq4LL01LZjpaxnj4WDV0zjk-ujqCN8FEKoZtCd-qsG_jOAozjiRY9bzHv5anyZPuaC53Rc5J8PfQaMc1dj2In6PRXajg5HaB1sTIbb-upQd5y6-WidVJc-wmtHd3j2wDIMfdxBkXcdHwU1eOFW7KbaDXi9n4Ddr1kaVVvzqZ5EdYItPkWK40U8wbLaIcISVepQdCjKL2Tufm5qYYc-5V3wNpiqVnLepRgGC4GblZKDVYWlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cJP0uEQdudWwPBRbhhObzgMPs9E_qhiD_r9A2-ZyMPH2gSyJ2AtwgSxkz2x5IqRydVSao8qomatH3JXp9O4kABr918AXcPT-R7Qz3faHrj3w3Ib5fkGpzpo5nK0ZH0SRRCkZMd7uZVn_jW4Xt7YfBvlue0AgfDRzGSru0ekV8PC_bT_KjG94bm0jYBpwUaD_yIMKtF8sQdst-kwkq5GjwWWOQ3GBRk2xhOgwfBYyqvhzyRWMydxeusiYU_ChoAHMcUsWu5XG7eqFfCY_1pLqV8OoHaHq7sT4gJaRzhqLWHJsnIQ2Q1YbE6skGvMX7CLXVPTF_i8tykpRHYQC8aLZ0pLG4k11xEnxetEqTpPly_2HpR33oIy33Uli45VOiBDF2Z-lGRiIol-RyspP4sG47uPJplFJuZADOAp2-yR1reVgOTugHD89l1VwN37n_Nlmjv-rTr9u6wfd9e6AiogQ7ZkU_-SmZvxccP9TsxUwBoSJTpo49mQ9iqxnf9a-3mkUmAudODCAZIUJsNM2e952m43JAdrb1XbMSE0hYTe6DB_WEd9mRJHf__JZsLfEW2AiDKQtTuoxdv2m6GcosCFwmvyClQ64DuPoFc3YpvtkMh9WlZL2ZNdSDzFpaHIHooFSZBBwNhw1Tg2QBoYrhMCOkScXOrp3fv06u-3irk08eEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cJP0uEQdudWwPBRbhhObzgMPs9E_qhiD_r9A2-ZyMPH2gSyJ2AtwgSxkz2x5IqRydVSao8qomatH3JXp9O4kABr918AXcPT-R7Qz3faHrj3w3Ib5fkGpzpo5nK0ZH0SRRCkZMd7uZVn_jW4Xt7YfBvlue0AgfDRzGSru0ekV8PC_bT_KjG94bm0jYBpwUaD_yIMKtF8sQdst-kwkq5GjwWWOQ3GBRk2xhOgwfBYyqvhzyRWMydxeusiYU_ChoAHMcUsWu5XG7eqFfCY_1pLqV8OoHaHq7sT4gJaRzhqLWHJsnIQ2Q1YbE6skGvMX7CLXVPTF_i8tykpRHYQC8aLZ0pLG4k11xEnxetEqTpPly_2HpR33oIy33Uli45VOiBDF2Z-lGRiIol-RyspP4sG47uPJplFJuZADOAp2-yR1reVgOTugHD89l1VwN37n_Nlmjv-rTr9u6wfd9e6AiogQ7ZkU_-SmZvxccP9TsxUwBoSJTpo49mQ9iqxnf9a-3mkUmAudODCAZIUJsNM2e952m43JAdrb1XbMSE0hYTe6DB_WEd9mRJHf__JZsLfEW2AiDKQtTuoxdv2m6GcosCFwmvyClQ64DuPoFc3YpvtkMh9WlZL2ZNdSDzFpaHIHooFSZBBwNhw1Tg2QBoYrhMCOkScXOrp3fv06u-3irk08eEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wnP-dsNwkNrglmw-ESc6HSa0RZABdZMs9jrxldP9oJTMJH4kW1KQgPHJExhKrtwDg8M4ierD8o3OC8G9Bd_yhesg7uawaza869gTwsRB-Wlm201U-H3-h4sfz47WFTULeqbajLB5SJ95qhLvWAgpKiNyjiVmZpJ0sSwS-JNFvuVscRcan8twR9WowRjcIyQrfKa63P07o2TyHH6iB_fp_wfD7FiVWEyABmsAz_mqc2yHsU49p9MaX2ELrLxYPEYYnFfyplSsRU2_pFqxK-AtCSZanjl-E8zQlm4xSoMD4fvUfcmOdfp7FETl4n910pLGM3gVwYRdoMIF-NuIH95wB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wnP-dsNwkNrglmw-ESc6HSa0RZABdZMs9jrxldP9oJTMJH4kW1KQgPHJExhKrtwDg8M4ierD8o3OC8G9Bd_yhesg7uawaza869gTwsRB-Wlm201U-H3-h4sfz47WFTULeqbajLB5SJ95qhLvWAgpKiNyjiVmZpJ0sSwS-JNFvuVscRcan8twR9WowRjcIyQrfKa63P07o2TyHH6iB_fp_wfD7FiVWEyABmsAz_mqc2yHsU49p9MaX2ELrLxYPEYYnFfyplSsRU2_pFqxK-AtCSZanjl-E8zQlm4xSoMD4fvUfcmOdfp7FETl4n910pLGM3gVwYRdoMIF-NuIH95wB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=NQoCBQBRbIYJk9w8q9-Uv7leDOpx0fHdwN-Vk3bomlKaXNamxrlPNjpLmEXmQ1aH8h0ItWl44fUbE1qGu1OONrHLI6V6j9-fp7im6pJUtcSfi4keRFydNZw11niORBjA559OX0wT1uSFT87g7qd8n2bMud-b5XYxO8ciMt3-EfQQrwJZRFe6FMtxA3Y1Z-dllA6Bq0KBgYjlJLhJdAHUwqbPsgC7MdtV6MyoJEq9HE1_j2zW2nyAESXN1la81JCqzF_7FDF19xVQPk6TrvNNKOk9d3L1c5-n_h_2omH3fJCyWLFEN4MIBHBQOPqneq2QcCZzJ6M9OxklslpmySU5tIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=NQoCBQBRbIYJk9w8q9-Uv7leDOpx0fHdwN-Vk3bomlKaXNamxrlPNjpLmEXmQ1aH8h0ItWl44fUbE1qGu1OONrHLI6V6j9-fp7im6pJUtcSfi4keRFydNZw11niORBjA559OX0wT1uSFT87g7qd8n2bMud-b5XYxO8ciMt3-EfQQrwJZRFe6FMtxA3Y1Z-dllA6Bq0KBgYjlJLhJdAHUwqbPsgC7MdtV6MyoJEq9HE1_j2zW2nyAESXN1la81JCqzF_7FDF19xVQPk6TrvNNKOk9d3L1c5-n_h_2omH3fJCyWLFEN4MIBHBQOPqneq2QcCZzJ6M9OxklslpmySU5tIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=jJPeAg27QaqoDWet1FsJJMrUZyYFXcWtFd-edR02pH2rk6HLk2tlMQlcUthBOertHq6e-LXBpYF_vMfOiT62om8PJSWYgz2UnGxQioKzwUNrzX4TQeFO3YEvM5-B8wpDaJhzKij4WA-usdNeHpqd4ENvjRx4aGaWqO_rpyOcGZPt_KPEXrSBeGD-mckL10l53ICNRG-NQUPlv3EiIArYzB18ZOVXTO0l3kLuwtmd88_jtCOsTsEqOSxSBGnXh0Yr0lazGrj9jIjtXcT1yCmI88bzNdyA5JuxEi0A5q9nG-v1jBoU7sfERtPerVEEfkThnsN0WD4loLBIQBoBx2Y7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=jJPeAg27QaqoDWet1FsJJMrUZyYFXcWtFd-edR02pH2rk6HLk2tlMQlcUthBOertHq6e-LXBpYF_vMfOiT62om8PJSWYgz2UnGxQioKzwUNrzX4TQeFO3YEvM5-B8wpDaJhzKij4WA-usdNeHpqd4ENvjRx4aGaWqO_rpyOcGZPt_KPEXrSBeGD-mckL10l53ICNRG-NQUPlv3EiIArYzB18ZOVXTO0l3kLuwtmd88_jtCOsTsEqOSxSBGnXh0Yr0lazGrj9jIjtXcT1yCmI88bzNdyA5JuxEi0A5q9nG-v1jBoU7sfERtPerVEEfkThnsN0WD4loLBIQBoBx2Y7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY3et4kZP-8Dxj7DvJHV76019GVz9sU0K9CviCUdbLSgUuCqaphBl3HPFW3myKa1u6Vi5azTCJ-Q-SrmyHeyI6itcn9Z7xLYVc3hzEAIbRmnOkRierNMOiN5cHtg3BFjyr0B7Ul1nrN4DaHD9zSjuDPwb1vNmpEXcOkfAMHyoBRa8tiyPad6EoRS-_RAp5OG0Km_BJDjZoc9hY7VzElVtcQWt44OIGIoYnylokCEqh5-bEn_dfzDLGJYcDlXsLZ5Dmsmnm-jI_RUGooTLPr3yNJftDHmjg8waSHpvfsItewDnq-o_xTyyTAm-frgic7TGI4GazykM77G77Gd3y6ctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
