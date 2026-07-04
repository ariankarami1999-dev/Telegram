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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 04:34:58</div>
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
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh_lbi64GAKICIj1XanDDf9XRBHZ7iObnVrTHBw06VXmMkfIxIsm49by1SlEv3OX_40Gw3627dglrn2e1sNCsRIcJitQOocvTfhp2bfXtqtBmAsXwX8J6sigFgJ5dE6ccvCp9VJdl9iEDfjmxX66wTwELxzVESz89SfKpqSmGmq2lFcjb_uDr8Mc4WmNVQ0zXL0sxmy5P-ZRTUGXSOSyLqG6DhaG3e48pOlto87UdHwvbqmWuBIimIJhN_5bMmAQfqCVOIdaVtQZa0SfLrnbrjLoNEC_qpyDxeqdy8jfZurxu3lyGJFN32pSvA18JoY04mmAMJxWZI8bvrWa0DoiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=LZzo36ugUPE9x4hb4x0BBD9N2LuFGsIwPmD9duB-rjhGjP-PMCS1OCgC6YnSxhPG6ZWh4WHYFoWcPj2rMr8lvXtp90f1NJ4_vWgUxuwKQb7P9w10cvFlnZmu0l5rBsvVuFxW9F2B1eg-HCkDdysXIiAw6VFYph515jZYfgomtEZyTUVFI1zMcfXc5_wrju3YBr-_NgC79rSLkaiWzfYDsVypKroAVUeSDdib1RQ2P4tcDebRC-pPWprCbkwKbbaIAzmyVBqXcpvJ58ZEkz9pwtd4qfGsI26ERY7gjik25qk1r6LIX_Fk2Vi7i7dynBREqLXN_dkVL-azBPW480zglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=LZzo36ugUPE9x4hb4x0BBD9N2LuFGsIwPmD9duB-rjhGjP-PMCS1OCgC6YnSxhPG6ZWh4WHYFoWcPj2rMr8lvXtp90f1NJ4_vWgUxuwKQb7P9w10cvFlnZmu0l5rBsvVuFxW9F2B1eg-HCkDdysXIiAw6VFYph515jZYfgomtEZyTUVFI1zMcfXc5_wrju3YBr-_NgC79rSLkaiWzfYDsVypKroAVUeSDdib1RQ2P4tcDebRC-pPWprCbkwKbbaIAzmyVBqXcpvJ58ZEkz9pwtd4qfGsI26ERY7gjik25qk1r6LIX_Fk2Vi7i7dynBREqLXN_dkVL-azBPW480zglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDRH6185Vtvhu9UmNmr7-6mPKN5QdA0WhUOyhQiUQLemlOPHf0dxnX_2VUs_NRT63swz9BLXC5oz1s0Ck7zl7MIImsWUrvkGiXdAnNRyFC25i1nbO0RKPYhrsAOAhbjgNxWuIpDD5R1fOqLQzz6_WVf5lVpa3GMx9yg8ZV9pdLRE11o-zUOJ_cigkh6QkRtIrkLEXI4lOjLtLAWlJIljg95lNWGtE1jh2n7OdjCtrFHvnFkwXFEH4EWByNaf4lkhK7kls6Rney6vgsExx3WMWTiAdd5btNvLumXswH4eenpg0HRZHW_iwWtrC7Y3BKJv9mub5XCvIvUVaLTu_ssjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PY_7EkNwMM-gt33Pdu3-H31w2oHuxx0sNEqZa5Hh8xpciHa2qKO1iSfW6ybdqB7nHvHcwzl2hKAqsWdRvMbHBgdO11-Mqbw137tODOtA0yFtDLxnOGQ54R7-XjW6iE5839FtRGTrWhrM_ptmYjkBN6FmjtGduwOPe3cf10BtgtCO34ZdXi4FXxfDX883lDRt8OyGhV2mrLrFMKVnYfsGYCzndbDjvhJkHyi7MRZlhkAONfnadhbGNQIYAJY1GRZl6xx4BZeSmef5lgDAHtmJHFxWGtuJ6hNrkfvDhDo_xMdoRnPYbapxqeJjfFNPVxpCCnzMqV6MIcTCv4DF3lTDcw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=g7dQ0ZVfRfOYCVmWEprFkp1AAl08Vh5d41mEYzXoZ0roqrQ2rnKdlatoMp1Sbe1iGwOBDCjZoHfcyrKN5z6JTQHnkW7VWPDfQCxfRuylenvyCtE7YTtVvGqIsOnf21PkFn84hTX0keom5bTpaK9qF55psLbxZBONKp-_pbWjDmCMGsiL0X-OUVPwVYMfbgakISkdtZMgxoufRTnbalVmVa0QaTtqKlbj6eJE4aj99mZBEUnXz70x-k9j7lCRu_8XsTIlnFo7-M904OT6x6JhSGz-5citKeRDhWCijbhSXI60D7ZmqBrOMzWXKNDetQLAcL9syZ73HHgOKuRKCoHo8Ttf5XJaH-YDdsKkA7UmzCjEYUUEXl43ndhc8XHaQFCboWCFmSR_zvNrXdsHO3qOd4hVNtL1rWPe1c_1bGnCM-ovfLXwMVpwEOTIwXwfc2G9p-0UkK2XrIkVF1rFgpC5Zw8BnaJ8t-bKNXnHHYCN4XrCdvy5RtERCJH54mveOqSUULBxY_VA-fkF7jkzoDui787LZIYM3FgWdU7ir2sr303ppVA96VkP6nb8VsfcT_IAtae8E0P7OGESTnHibWk0MHjqQxnUBMZ4gOKSeCgLXH1yNAXgc0Qk4fyza1yF-cle5EZ2cwAxSNdOc-3s3YFz7mF-8pP5TKEEuhheGoPcUJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=g7dQ0ZVfRfOYCVmWEprFkp1AAl08Vh5d41mEYzXoZ0roqrQ2rnKdlatoMp1Sbe1iGwOBDCjZoHfcyrKN5z6JTQHnkW7VWPDfQCxfRuylenvyCtE7YTtVvGqIsOnf21PkFn84hTX0keom5bTpaK9qF55psLbxZBONKp-_pbWjDmCMGsiL0X-OUVPwVYMfbgakISkdtZMgxoufRTnbalVmVa0QaTtqKlbj6eJE4aj99mZBEUnXz70x-k9j7lCRu_8XsTIlnFo7-M904OT6x6JhSGz-5citKeRDhWCijbhSXI60D7ZmqBrOMzWXKNDetQLAcL9syZ73HHgOKuRKCoHo8Ttf5XJaH-YDdsKkA7UmzCjEYUUEXl43ndhc8XHaQFCboWCFmSR_zvNrXdsHO3qOd4hVNtL1rWPe1c_1bGnCM-ovfLXwMVpwEOTIwXwfc2G9p-0UkK2XrIkVF1rFgpC5Zw8BnaJ8t-bKNXnHHYCN4XrCdvy5RtERCJH54mveOqSUULBxY_VA-fkF7jkzoDui787LZIYM3FgWdU7ir2sr303ppVA96VkP6nb8VsfcT_IAtae8E0P7OGESTnHibWk0MHjqQxnUBMZ4gOKSeCgLXH1yNAXgc0Qk4fyza1yF-cle5EZ2cwAxSNdOc-3s3YFz7mF-8pP5TKEEuhheGoPcUJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdLmm7ZZNbsEQPlMyDpGEdp7HfyM1tKVv9o4LSQVMOJDVARRZWKDISgBg-4gc6Apw-g3RKentC5NKEQjb8z6yRtzo5katDYB9Qj_JXNSJN6WLo4fyzIelyXOUnfwW5DW-znjJhzfrpSkyCjOegXKsI3DHC8zO3msxQE-l47jHJULqRECumC0QJY2l5GEz9K3hJdQz3rS9RgeZEzr__XeVrWeiUjmv8RvBU6wingm041VXsqC7aPYhHTIL5heJjWXLintTP32vhy2I03sUgiOkLkSul9msbW9iftW2f1QsFxEX6bMIbFyxVmDqTMmZKm0ALek_IWElV6miRoU5Zwo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfwIhbgTB-dvuX67SLJwtZ3vPFylUiCEf6vJTIbM1jrFe3UhWH4Zy93weKswbHzboMZoGV8JZ3C2nUjdX2IMZrFILC50oxtxAMi7HjtZixTspUF8CiheVclgwyAkodNlQ6TjKNloJP4pAA09V3ZLALMp3J-tJgRaZydNrqKVgKKpt0KH3ZAtGwIa8upvjS-F2HlR4qrPfQCfeZwAH133_VGJ3szKdnXwFHCk8BYfBOnv68zbZDWcPwEOqwX4EOS1MIzmsPSq6DkJUcARA24qHFo1FElNbk24fxGM-QSea2e2AFbXUqIwRHnYnrT6oYnkA35rkXvJNLxYKVXms21VgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E41MfH8nSkqu-ioGj5R3sR6r_jiiRKRoeM07IqFUmGNxlFMDg73hojYCWwpjqCaU0MAkpr6ej5VBp4UN9RptcHAaJJxrLaBasz46HtFNPtq17CXfieI8h8lcap6pOMbsF5TFCkbhK7w55_QcgiBOrOvwB7JmbIu7Dq6WJx9vE_QRIXhHJwD_PywVPWS_0rvs1SpXksCgiy1hEX9SR1StEGzLIvmejA5odw3sHRaqn57J6G1OS4bpKHMKpuiCigxUJKbpXHch4hh-7Fy5Y42uGQvO7x_6ZRW5GfGD6hoTULKwfoo6U7PSGjV7Jjr_jNsH6hXktj0SlmboexdefWYVgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvc7YG--2grqgEFT9YiqqXJeacbzyyAe_3M1L4Pl75zYFwLkIw_GiKfvBUBc_hBMmBPnb5qHV3ECr8BuLAk45mIKg9TkknxiZbe4rKnSVxH7kuxUzf6eV4SefDTHbuG25SjPF3nNw6L6GlyATGCrJSkf2-cUTQdraOyr6WhlMzgSZkevQOn-PsYnfNdTQeBUa8_DCa8zIRLGOcQspeAZLLlSHWWJROP-3ieAvKYTm1gl0c-J4mzpEqwCQ0YacZDRKNQDIPD8rkQo1n5B1aeHCLjBO-lsikEpmUYwYUDg_SBfWSBld8cqTPvrj5Wt7kydXQ2XLWdXkVPUC03n04T4KA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZL9sINVMkfDAW-vnWyEC_05RCzYRaRqWjSaz3EG2ChJesEn3MHlWuSRfu_Th7xx7Mqru99g1MEhjM0FAQBHOYsfVH8aXgYTFhKJ6I0fi7fBRadgCPDtsdMuScdnH9-sRfDNXJZVuwbVak-NUfnmMOC4SyhpiTjCvoRL0xtlOmDHKCnPO4AEic1sfOTFAd0g3zMnLe80gzuJHGyPMRbeB_PNA9leHpkIt_mVzcTRoSDc7roGukE0KJWOwun70_8D2HQD3RkZdZHS5JpMpYs6b1fIHglpm9Xp8bx0eEKuZMMv3XS6qRZRVd4SoRifzcLUMQWybGrmLCE9togU10wWw3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZL9sINVMkfDAW-vnWyEC_05RCzYRaRqWjSaz3EG2ChJesEn3MHlWuSRfu_Th7xx7Mqru99g1MEhjM0FAQBHOYsfVH8aXgYTFhKJ6I0fi7fBRadgCPDtsdMuScdnH9-sRfDNXJZVuwbVak-NUfnmMOC4SyhpiTjCvoRL0xtlOmDHKCnPO4AEic1sfOTFAd0g3zMnLe80gzuJHGyPMRbeB_PNA9leHpkIt_mVzcTRoSDc7roGukE0KJWOwun70_8D2HQD3RkZdZHS5JpMpYs6b1fIHglpm9Xp8bx0eEKuZMMv3XS6qRZRVd4SoRifzcLUMQWybGrmLCE9togU10wWw3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=r2IN8Be_4qh1KAH_Dt987jxUsYdtRayzeQMOLD_o74149Fs-pkudPnSUOGsxPaGBzQ2FiIQSTyQrBrtmVWgwHJRNcAz1tv0bR2G3EpOCJDvemxx0B-kyKAc8Wa3RpkTM8VwuVJqkckcUIzIpVy0h9xGu2Mep_JMflaRmVBwuu77_oC2cvG-o2OZ5j5YEw_9MWuOIuP_DxteA3MFoEKPSsexAxo4RxZnDOhIzcqcstyBn5PFAR5eSuWqMhRd9qzSzg13qpIagyv2RSuRpbDMEpSNE0L2nEKBsuo7P1VGwsp_aadOnPYCjmEYYxGhViAdfx7XA8cdBSSer2I55bZ0TAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=r2IN8Be_4qh1KAH_Dt987jxUsYdtRayzeQMOLD_o74149Fs-pkudPnSUOGsxPaGBzQ2FiIQSTyQrBrtmVWgwHJRNcAz1tv0bR2G3EpOCJDvemxx0B-kyKAc8Wa3RpkTM8VwuVJqkckcUIzIpVy0h9xGu2Mep_JMflaRmVBwuu77_oC2cvG-o2OZ5j5YEw_9MWuOIuP_DxteA3MFoEKPSsexAxo4RxZnDOhIzcqcstyBn5PFAR5eSuWqMhRd9qzSzg13qpIagyv2RSuRpbDMEpSNE0L2nEKBsuo7P1VGwsp_aadOnPYCjmEYYxGhViAdfx7XA8cdBSSer2I55bZ0TAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mioTLlYmduMf8E5XaRyZ_dUNQd9yzodUfrmFtS1jX31c-MT61TD-f25524ZDO_XVf-EazH_ENGQv2yA1ZR4KX2ihZGsPr8-J7JaEwZb-lU8bxZ5VQPp7ZlBtB7gLUp0kjzBXr9pd4BJ28HJlDtRO9yTGPRqUriUkoNnqEgWtQ_4a33zLWuK8EvG89KlswdZCqqUxL3B0kkJE4V83c6ZEmM8CwR8gBiBHIOTvin2X1-JjgUflHhTlvp1PoftIzidJzdQtT0Pf_6apHHMfF2HaXLr16zxpudTV-7802Rm46JpoEpzA904ryeuXyTDD_9fe1y4tym0q51Zv_8flywgIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=MWp_ZG9OQYwOB0pqQfAIIzj8Je8aQPSR4rtheEpDEtUlIDZXuvZ_v4efC41iKOP-5KlR4Hmt0GAm7R6C_iwLz0fHUVAeYOg5b_fnRbwD88ktAcFHCpWEojWDmGdreNHsrZLyyXLUyvnt18tIAT9EmJpAcwGXm4rHGkAJyEuJmD1qC8sqpG1qIW4BhEKa-oR8qs8K5SGf6Zbj0NASdtmZiQPpxFDg53hbYJMhfj5J61UPmooH0sEFlw4l5gsyoQHyYF4RCbp5rWI5ACnty8nCpLsnCrrA2mcE8Q_epPj9O6WCDDclZoieVdyX-8__U1aVKG5GnsDPWGmIlZyN0nNZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=MWp_ZG9OQYwOB0pqQfAIIzj8Je8aQPSR4rtheEpDEtUlIDZXuvZ_v4efC41iKOP-5KlR4Hmt0GAm7R6C_iwLz0fHUVAeYOg5b_fnRbwD88ktAcFHCpWEojWDmGdreNHsrZLyyXLUyvnt18tIAT9EmJpAcwGXm4rHGkAJyEuJmD1qC8sqpG1qIW4BhEKa-oR8qs8K5SGf6Zbj0NASdtmZiQPpxFDg53hbYJMhfj5J61UPmooH0sEFlw4l5gsyoQHyYF4RCbp5rWI5ACnty8nCpLsnCrrA2mcE8Q_epPj9O6WCDDclZoieVdyX-8__U1aVKG5GnsDPWGmIlZyN0nNZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vRiuIeLHw4iJCd9rAkdSrXLWY6TrGuNtWOEAOvLtYyPlSTuPKFeaOvjYLCI05QmQU3HEtnsIGhcqQ7FQ1vsS9MvvcfhUtpsGbqd4zK170qG7CNg9AtJOR4fBf30yqR-no5Pw_DLW1Vek93IQKPklRt6Yag2nO58D0aaWfaTmjkeIkbXeNSvTCyMDfAn7tTpmQRZtz7Y-Js2Rk1vatvzx9y4-PHNU6ooQwFxQHLemCGK_XHwArolC47WctG45zdD8zT-0ILIDfc80gWhh_XYrt3k-YjqoIu2CNw25h_jmnyk69nWUxcd0uucUG-LH04ekw96_hBMZYb2TiBmjglphaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vRiuIeLHw4iJCd9rAkdSrXLWY6TrGuNtWOEAOvLtYyPlSTuPKFeaOvjYLCI05QmQU3HEtnsIGhcqQ7FQ1vsS9MvvcfhUtpsGbqd4zK170qG7CNg9AtJOR4fBf30yqR-no5Pw_DLW1Vek93IQKPklRt6Yag2nO58D0aaWfaTmjkeIkbXeNSvTCyMDfAn7tTpmQRZtz7Y-Js2Rk1vatvzx9y4-PHNU6ooQwFxQHLemCGK_XHwArolC47WctG45zdD8zT-0ILIDfc80gWhh_XYrt3k-YjqoIu2CNw25h_jmnyk69nWUxcd0uucUG-LH04ekw96_hBMZYb2TiBmjglphaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=fnKuFgVWr9lT5jjgdb7Tk5bMqy7x7Z8KKXKxmImx0nteKoniEkeXeCDGG-Wll2Ys-W2_3QjNHLboLpDzypXnCtp8poeqf5MAHsZw9GFLWCBzLS2Jw283coOtFTwBa_zYrAGrDCKdB-QC54fyvaekvh3f8fu9yTfHbmS7gJfc7edi92d85-FYjZf_SDoUZsagAh7C9kX9I514Otn5jdc4s6OkytkBICCJ4TpzzjoyZ-Hq70P7lEach1-_AeIR8FtJMT0CMrjzstiQmTDtUUKISp26gnp6I_uT3cPB6BP0sw1oJ7qKL5LN4NKu1jQcavwQfrsJexxfMzLZGY1QRoorGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=fnKuFgVWr9lT5jjgdb7Tk5bMqy7x7Z8KKXKxmImx0nteKoniEkeXeCDGG-Wll2Ys-W2_3QjNHLboLpDzypXnCtp8poeqf5MAHsZw9GFLWCBzLS2Jw283coOtFTwBa_zYrAGrDCKdB-QC54fyvaekvh3f8fu9yTfHbmS7gJfc7edi92d85-FYjZf_SDoUZsagAh7C9kX9I514Otn5jdc4s6OkytkBICCJ4TpzzjoyZ-Hq70P7lEach1-_AeIR8FtJMT0CMrjzstiQmTDtUUKISp26gnp6I_uT3cPB6BP0sw1oJ7qKL5LN4NKu1jQcavwQfrsJexxfMzLZGY1QRoorGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWOJ4c7V7uXXVwslnrr2mvgd5IeNGzbGbjsi4q9Zkpb3OuERlzOJtXSaV-mD1UOFGWi5UVGNvYvtFZW89DKrouz3YQzHqt4QNC6CMdD2wiEgB4oWpkCpzk4qLiy5b8sFwmg6XeeFxVPw1odoxKKzxPXaz9dkL1_BfnQ9OS6wHP1RKYAJ9HLF25KGHOYZv1Y31ypr6P2jMqeUI3n4NDIMmQOe0qt7ZB6VAOwt3RbOh2jDbFIIoq93SHf5ux_Nr_YXcDxTmgcarAxYDa8adnfIViJHWdIGr3l4IN9qOYOXQ9uRYygUTtwm6dCM219upB5OyXPXxNcgPVeXsUNnEKk45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atw_VLAr5ZjjSDI8mt8CaPcRyZfJmTmU0_YfFDXP2f7y08-aazySeEq5KESzAdfgcaI14AQiCwdjnouNnuqNP1UfTTyQd2AA2LVr5hT_Ef8EWPvdZuQzlalPmKYhM_0yfj74dQMrZjUoKDvXaQcR93EgnFfZluiWPbIefVoXp9g1Z43MSAm5u1JtKs7aCOEKRPY5TidiYovZU8RxdzjP0tLY-P3YO57RKIfA48ChEzCJaa8ajlId-BUIvZ0lqYjezR2R3avXfSX4qTqnhoN3nkCkCZ2rD78j6j_rUloJmrGkneMMC7aeJgKnE08m417zM9xJfxZ3xEfyY7M5OGl8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=k6gthuR4QkdcdxPyorVDzSx-Q1URNoPkXmJvEnERMOyA7uzUhfgB0regfSfQ431YLjtdqQuXkGmDK5mfx2fgpQVpOnrJInPlcWsmECILUflLnhuyaPQeNZXhoV3KW42qp0KkkOpWptHNu3Hsx9lPZVRmz_XT6w3pbvRMdKkMzYMl044A5Mxz-ZusDrqSZDfGfDVqK1rVrWj0HHwoKzEj-McFwyMKDTe92ivp8Txc_5PFuMuqzNW8Hm1u-mlwvF_9-NON237yir2HxG8ebmruPt2NiwSai0Bi3G4FKNrvJKcNyuPs0HK3KNq4TAlzbQH6B20arOUe4HKc-3K_tUwvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=k6gthuR4QkdcdxPyorVDzSx-Q1URNoPkXmJvEnERMOyA7uzUhfgB0regfSfQ431YLjtdqQuXkGmDK5mfx2fgpQVpOnrJInPlcWsmECILUflLnhuyaPQeNZXhoV3KW42qp0KkkOpWptHNu3Hsx9lPZVRmz_XT6w3pbvRMdKkMzYMl044A5Mxz-ZusDrqSZDfGfDVqK1rVrWj0HHwoKzEj-McFwyMKDTe92ivp8Txc_5PFuMuqzNW8Hm1u-mlwvF_9-NON237yir2HxG8ebmruPt2NiwSai0Bi3G4FKNrvJKcNyuPs0HK3KNq4TAlzbQH6B20arOUe4HKc-3K_tUwvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZD6f8mXQlAmM-IHsEqEhxN-aCJ_2BKjGBXYc4l3beOzAYi4psTJzdmIHpPrRL74b7VvaJ4nKq942nnrnJkWbz_mWj4C5iyPTadbkIAg29vQdTBmP7rxUL-JfjbZi1n3AzSpDiJ2a2qQmreA21s8zlconsJEmJWwRBd5Zbm6DK0OqzdlHQEkq2YR9fxFAWBXbeklhKxyTA84RqbG2IZN_x9Ror9Y0E5_MPWE3LWw7g8Ba1tPJwzTI8gO_I_8EK5SC-rRFJ1n1udAxZxfmTagH7rqp_eW_zukbPlxgIlrUGd_cFla59eUItYkr7Alllo3oYUmB3BPun_hQVOPGwdLBfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZD6f8mXQlAmM-IHsEqEhxN-aCJ_2BKjGBXYc4l3beOzAYi4psTJzdmIHpPrRL74b7VvaJ4nKq942nnrnJkWbz_mWj4C5iyPTadbkIAg29vQdTBmP7rxUL-JfjbZi1n3AzSpDiJ2a2qQmreA21s8zlconsJEmJWwRBd5Zbm6DK0OqzdlHQEkq2YR9fxFAWBXbeklhKxyTA84RqbG2IZN_x9Ror9Y0E5_MPWE3LWw7g8Ba1tPJwzTI8gO_I_8EK5SC-rRFJ1n1udAxZxfmTagH7rqp_eW_zukbPlxgIlrUGd_cFla59eUItYkr7Alllo3oYUmB3BPun_hQVOPGwdLBfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=QWKqaw3_pRkd9c3acXeYI41lg2twQlWNPKEU8AC2gVoUCkV3zTT7Bxtoa8mFjtUPiqed7MCRmaUAQGEoOb4tTv_eT4UpXz7z1Zy7CK6D1LGZ5KntI0eJBfaPo8O5YiMKCvEFWZNKuNL6A6HcOl8HAIDTAMJPzd86VKF-dcAhvPnD85eqqyLBaQqziIbUD90AfAkcwKWSSQkK-yYmzZ061GNQ43vgIGU1F8QAdeXjliYacfvsDjys_GKP4C_JjmOLrBCYWltzChL6GMXpybifk7emW51RWhLw6KWRT3BnhIPS4723Ceni_dIHck6fPhyMg4VrcUORoewIamD09rRMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=QWKqaw3_pRkd9c3acXeYI41lg2twQlWNPKEU8AC2gVoUCkV3zTT7Bxtoa8mFjtUPiqed7MCRmaUAQGEoOb4tTv_eT4UpXz7z1Zy7CK6D1LGZ5KntI0eJBfaPo8O5YiMKCvEFWZNKuNL6A6HcOl8HAIDTAMJPzd86VKF-dcAhvPnD85eqqyLBaQqziIbUD90AfAkcwKWSSQkK-yYmzZ061GNQ43vgIGU1F8QAdeXjliYacfvsDjys_GKP4C_JjmOLrBCYWltzChL6GMXpybifk7emW51RWhLw6KWRT3BnhIPS4723Ceni_dIHck6fPhyMg4VrcUORoewIamD09rRMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrxnteMEbtU-DEHirTpJiXME6gfeor_pE0q7bkZ9kPn00KQxnqTS6OXbFDNJgqzoIz7i7n_SlYEsp1-7Pe2IVSS9mSylxcWoo6eWhU6xdrzLKzN5z9pVsfcVpHm8DcVJmXBMK5Osmnp-wENFp4bMfJxY9nrH0wwHIS5sHwjYHfbVgUPP0g7hYNea_wE8pqTCtRp1XMhjSM6WkOTWyCBG7mq68CQpnoWKl5aRTGfOVUv4v0TllVuAu-Jn2GL7_lrinM0dc7hI1oGHalaTlfPL3swrrAtfw7F8XuqIUCbb-1_GK8YGnw3U04ylPhqnL2kkWRhShSgeeRX4I1hCvNv3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=l4IBQKmV2B93uJmvHEBwQC8IukkLrkqiy9OIO7xXymKftJn44hPAq7kqBqrJdji2_liqcYv0SHV8W6M_b7CP01KbDamdAMemVt-UPJ4z6gGkrzvpO5fxqDVomRrtC30VMdjJJwUREi0UVvClTsSfPP1I1ov-hvuOBjRlJjwX0-BolJE315xY5GUjOZS9hywKzuCUq_XYWUwE59bdgpJv0miFTs7bm9Bx8U-r0523QskYYZ_nJfcanQ0tSbmjxOAiyq7mXlzdOi8ob1lhFFpTvBJNuknjW7xSFZt0astlwDOICIDCUVs7pvTBcl8mVyIhYSli0viIXqFveZEOaWadkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=l4IBQKmV2B93uJmvHEBwQC8IukkLrkqiy9OIO7xXymKftJn44hPAq7kqBqrJdji2_liqcYv0SHV8W6M_b7CP01KbDamdAMemVt-UPJ4z6gGkrzvpO5fxqDVomRrtC30VMdjJJwUREi0UVvClTsSfPP1I1ov-hvuOBjRlJjwX0-BolJE315xY5GUjOZS9hywKzuCUq_XYWUwE59bdgpJv0miFTs7bm9Bx8U-r0523QskYYZ_nJfcanQ0tSbmjxOAiyq7mXlzdOi8ob1lhFFpTvBJNuknjW7xSFZt0astlwDOICIDCUVs7pvTBcl8mVyIhYSli0viIXqFveZEOaWadkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=m4iLDU5N9oxh4-LZOAPDWwC9d5uuHKKeG5slIO-QR_jSlpvTlHYZDMhhXqAow8eds4q6e-pt9NoEv8fUrpHoA3WwbuEVxuYYxrXqYZTt1WLWHNFSBjiwuAmq96kcvC2HJq61R2liO9QyAbCXpJqHXUvXPUjgGjr33Y2dmpMvS8eslXt_iqFxPR-h6TYwMzT9hQnkD8y6nnSNxVUMSg_X76Glij-L3L1PNJ8rcQMYtiRcJ-O2xiHGkyBfi149YhJpsqHIWdQ6lAeVCGBEvCF3ZzwncWd4IySGnEeNKTKCI6gh_HSlSwv9TUkybhLPwzivhrbCAV5-Ce2UanSNh6DUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=m4iLDU5N9oxh4-LZOAPDWwC9d5uuHKKeG5slIO-QR_jSlpvTlHYZDMhhXqAow8eds4q6e-pt9NoEv8fUrpHoA3WwbuEVxuYYxrXqYZTt1WLWHNFSBjiwuAmq96kcvC2HJq61R2liO9QyAbCXpJqHXUvXPUjgGjr33Y2dmpMvS8eslXt_iqFxPR-h6TYwMzT9hQnkD8y6nnSNxVUMSg_X76Glij-L3L1PNJ8rcQMYtiRcJ-O2xiHGkyBfi149YhJpsqHIWdQ6lAeVCGBEvCF3ZzwncWd4IySGnEeNKTKCI6gh_HSlSwv9TUkybhLPwzivhrbCAV5-Ce2UanSNh6DUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KIbHGvwM4CskFkECIkdRPpMplitS3ECP8G-KZA-mxhvd_hPz26j1EaUcjBxZUKkzbvr-Io2N0OthVG8c_0BZZkl5xFOdCMtV8XkvXwlsOjJudQE53Gp6gUZgZ0M9XcsnaHHP1ViaTBs89oqGIFcB8VMVDVRuULcpPqcQ2bLrS2duXh6AWJEk2LHvURv4nr5XWVP_Mkcbti7B7qwkemQU1hy3voD4NgaWbFuK_ZnknRSd9rwt-ycgsaWanCVEXvRS1NSNe9b2pnTLZzGWML8iAf6Q0LM7-51dunkTb1UngFtkDUIOmB975flmqzdAAoCQXQ78UZMwubB2erhzxwKakA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KIbHGvwM4CskFkECIkdRPpMplitS3ECP8G-KZA-mxhvd_hPz26j1EaUcjBxZUKkzbvr-Io2N0OthVG8c_0BZZkl5xFOdCMtV8XkvXwlsOjJudQE53Gp6gUZgZ0M9XcsnaHHP1ViaTBs89oqGIFcB8VMVDVRuULcpPqcQ2bLrS2duXh6AWJEk2LHvURv4nr5XWVP_Mkcbti7B7qwkemQU1hy3voD4NgaWbFuK_ZnknRSd9rwt-ycgsaWanCVEXvRS1NSNe9b2pnTLZzGWML8iAf6Q0LM7-51dunkTb1UngFtkDUIOmB975flmqzdAAoCQXQ78UZMwubB2erhzxwKakA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ikbuh3p6PHO850so41XmegH3p0elcJHngybclADLanFyW7xlBIoCb2bkVeVgNqmG4QoQYdaY7no8mGX4LAXBGlKc4R3Y4v1ZpNnIp1eaAEd3kOvV_aPyIR4QOdk6zOmNtUTvlDgJRum6cxK-8YZVsDr9-AgIPKBQS6j8yDyYFk_VmgnUR51a3rs6tLH1kXs76sxVrFDTSEA_py7sLuCh-DcbkWc7VNxM3lUIpc-O5fZn3gIbWt-rQDq8VwbGDAcOu1dfCjokI7iupcAIDkbOn6xKicQ6hLIGWsx9jbw-ioM_RJR_Pa4JVidBjS_BCRxZI1jP7VavUEbzPFejWaIFWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ikbuh3p6PHO850so41XmegH3p0elcJHngybclADLanFyW7xlBIoCb2bkVeVgNqmG4QoQYdaY7no8mGX4LAXBGlKc4R3Y4v1ZpNnIp1eaAEd3kOvV_aPyIR4QOdk6zOmNtUTvlDgJRum6cxK-8YZVsDr9-AgIPKBQS6j8yDyYFk_VmgnUR51a3rs6tLH1kXs76sxVrFDTSEA_py7sLuCh-DcbkWc7VNxM3lUIpc-O5fZn3gIbWt-rQDq8VwbGDAcOu1dfCjokI7iupcAIDkbOn6xKicQ6hLIGWsx9jbw-ioM_RJR_Pa4JVidBjS_BCRxZI1jP7VavUEbzPFejWaIFWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHYtQFraOOrLffyf_uI4CRtXgfEqLWZBJaQOJxtl935NFh3zf_KD9VqKr_nferqoDlY3FPG10r_MObpKZN5LBDCzDK7S5Fd-H-M-MOKHxzUI49Ch6io5sZBL2px-9kzC2XnyyzRvnqLrQI7PY0k0Q5JGKPeXVxlKC203qc1ehsru2lVEZFhTihiy4t-qaasl4QSU9CdJoHpE4IH_rC1W6Tz_sTksJ6ux_-B_BXAjYKP9t84BrtSzWIlNQ1IDMBbc6ZxCRLL78A2MfEdED4xGfnUfjxBzKsvdXEjLVab-fsaQ9Fuuk98YMgPZ0JRfWM5WswA8Mpst5-g3o0ACuh3dsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=atx3aSDgrImzfwsbZDAfdDp7WESdrnEcXgLQTr1onVUejBarAPQO1uS92jx4l9bLppNGdvm6rIly-rnWZSWqPak_uQ8rt0iX4bB4UiqTdOzPNyWOZcsVC4nPo3sjOItVIGJQ3urCsav0TKeLnwImMpgoZvF_7UoGc04aD6ptnyDjbR6zM4kte3XUH7wirJKOzEYEZZWbQ0zlaYfzcCoPkOTLO2FbUCn1hlFTw6k-DchVYprdVAThg2mHKD0i35GgiuFCKUUSMgw0mBFVh3EigR2dAxG0AylKUU5QgWULdC7iZALCPO9ARCSt_R-LZagF8Ha01dhee1DoydXdmKIcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=atx3aSDgrImzfwsbZDAfdDp7WESdrnEcXgLQTr1onVUejBarAPQO1uS92jx4l9bLppNGdvm6rIly-rnWZSWqPak_uQ8rt0iX4bB4UiqTdOzPNyWOZcsVC4nPo3sjOItVIGJQ3urCsav0TKeLnwImMpgoZvF_7UoGc04aD6ptnyDjbR6zM4kte3XUH7wirJKOzEYEZZWbQ0zlaYfzcCoPkOTLO2FbUCn1hlFTw6k-DchVYprdVAThg2mHKD0i35GgiuFCKUUSMgw0mBFVh3EigR2dAxG0AylKUU5QgWULdC7iZALCPO9ARCSt_R-LZagF8Ha01dhee1DoydXdmKIcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=sD4VVBzEreYSoatWUPs8HG_VHT5s52alOi94V3gyKHriA7wK343X_EMYdgjJ73ggukmc59OU8PIHefufeZ7QW-P7OtwK7B-m9fF5TFPz_jBEg1T6dzxfm5YEkwdhosar2cLBCm10ujtnGfPVR__60Rnua4uvf1aAC9cd-9LSvqM-k9CYlk_LmZvSw7wVuEd4EAYHiNHVIzmxC6FoupNLXSVevrt0z_h3eMmfVlmzxzKCe9LRk2N_22-rpMC3C8HGq-QSEaLwaV_yGkNdqGHZejKCrlIpHfvl9psOyhExfWeM-B17biSVP--I3PdSg3OnYMsqBB-zimh6PesCqt-bxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=sD4VVBzEreYSoatWUPs8HG_VHT5s52alOi94V3gyKHriA7wK343X_EMYdgjJ73ggukmc59OU8PIHefufeZ7QW-P7OtwK7B-m9fF5TFPz_jBEg1T6dzxfm5YEkwdhosar2cLBCm10ujtnGfPVR__60Rnua4uvf1aAC9cd-9LSvqM-k9CYlk_LmZvSw7wVuEd4EAYHiNHVIzmxC6FoupNLXSVevrt0z_h3eMmfVlmzxzKCe9LRk2N_22-rpMC3C8HGq-QSEaLwaV_yGkNdqGHZejKCrlIpHfvl9psOyhExfWeM-B17biSVP--I3PdSg3OnYMsqBB-zimh6PesCqt-bxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY7kdv8ln2EzU44HDa5M4oQeslVHTkqPjl3dr_0u8iW6Kuxz9lqEfKJjjYpubD_GPrPK3BsMfIbrXwXjckMqtjDDBGtnETqDVFX9qk1QMdZhVu44r9LR-EfU8ZaBbQoFe98-iTotRFeaOb4IG7XQ_AzGqrvJhS0OSJAqeiLe7SB1Kk4dPincPRnSUovN5m4kyTdjS8xFGqBB-AMwpIprZNcGfSRxX5Q8FoJ2PyjmnReKfoei4qGEri0Ud0qRovh2k5xkurAfE78BP8oi1HC2vnuAA0wQzwENv0I5DugK7p9QI_rHjNAJYeOTUbupgux4ScN0QQ2D9Nw0pTOWlQWICA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=dYLFBeS-p89UjUVHpgw6v4VXl5xUJMmydomTMvEkNRPIGa26ZAQNLG0CXFWdVNqP_3-Wn59v4-twjzYpupQv50x30Bi5DN6PK7LlIORwZJLdAHA6UIO1Qy4kiiKDIiIJYLG1GAAlPdP_1ypuNr6eov7S1PhHTjQIXFPLNUQBXHPzCPMoROgt41g3UfaJC6fYYIfoQHJK4jItaabzvqXp47yNeHRTRb5I3x2tQmGYUu0_RG40kvCTbi6MistBrSXS9H_B0Rrw_gqvnKfeUMlelXMXRDPIfO3zbH2wY-_rVIza3h60Ir5VnESaRb7klVIOHqwI3m_aHMuPZtQyZ8xEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=dYLFBeS-p89UjUVHpgw6v4VXl5xUJMmydomTMvEkNRPIGa26ZAQNLG0CXFWdVNqP_3-Wn59v4-twjzYpupQv50x30Bi5DN6PK7LlIORwZJLdAHA6UIO1Qy4kiiKDIiIJYLG1GAAlPdP_1ypuNr6eov7S1PhHTjQIXFPLNUQBXHPzCPMoROgt41g3UfaJC6fYYIfoQHJK4jItaabzvqXp47yNeHRTRb5I3x2tQmGYUu0_RG40kvCTbi6MistBrSXS9H_B0Rrw_gqvnKfeUMlelXMXRDPIfO3zbH2wY-_rVIza3h60Ir5VnESaRb7klVIOHqwI3m_aHMuPZtQyZ8xEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=fRBAfvvkyLacBF2VTuVpJPTkW5omobJv2Ei7sCs185fgHdoO1RHhWBaxKMmnk9AhB-GJKu7EwH8CeDNXKpnIRvTJuz3Bg95RY_oP62i9jU-5hDrO-tSj_WRnqEir-HoEWMcBN5hRDua3fgbHrEmGqbLWOHw6DuWLW8atUgwy3xXkpWVXA-N9Dg4r9GKkGxQciPJOZhRVe3pwFWQ8IEwY13rAfk3VTV7wELpesjl_ZgDRsVvQPHdm6u74BTNBWB0v5Fuhpf7PBBAEdHjYNp093NbN1PgSx3Y5SJGziWdbpdIKkRIX2hYrThHwucEEkbDtRux3U11KpcBydv0bMCPz7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=fRBAfvvkyLacBF2VTuVpJPTkW5omobJv2Ei7sCs185fgHdoO1RHhWBaxKMmnk9AhB-GJKu7EwH8CeDNXKpnIRvTJuz3Bg95RY_oP62i9jU-5hDrO-tSj_WRnqEir-HoEWMcBN5hRDua3fgbHrEmGqbLWOHw6DuWLW8atUgwy3xXkpWVXA-N9Dg4r9GKkGxQciPJOZhRVe3pwFWQ8IEwY13rAfk3VTV7wELpesjl_ZgDRsVvQPHdm6u74BTNBWB0v5Fuhpf7PBBAEdHjYNp093NbN1PgSx3Y5SJGziWdbpdIKkRIX2hYrThHwucEEkbDtRux3U11KpcBydv0bMCPz7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXCjs5cv7YqlpAVuJuQnSCBEA48QXzGUtYkuaBQfGezXSm2O0IRNHG05vgFeIxhMyFi9LdaPkKBm0vgdAKgvIN8yznZK5VPd_WcKlJY7_ocadlyYrs55cb-3yKopEi-lFzWy3ASleMFU0l5ZU0sKmZqqJTTeDxmJEWudEaCNMfOVYG3J2Uz2riQvo80u3m10WnUuUpSqlyarLDq1lFqqB2AtoL5OHL33vqQgIHWDAFQxWvr1O_lmO34y9NDjWAgT73df1HpMHN7qYtDMsebarvC8fSrifKW6qS4o8DSeO62t9eXEGXrde36rNFScG0X_9-ZOc7y6aDesrgZaPoLHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTRjvVZPVG1on_N3lI04-RPe_KAPL2L8DV75Lqvc9tHT7H75qD2byuS6OCJLsx05Zh8tZxfV0hGstpq3R6B5bi3nCkp-Hftrptit0Kae6APcDQYc4g8_M4zH4sQJzD0K8MAkSdPbnCY8IG3TM-mMomEPBd8qKHfGoZndetXqADJN2Fqpw8AvZdaHQnGGWsg3XYflrkrDOF2tqOctrSqxJREUZersqeU9J1YA2kox8CIqbWQ-qudehVFWYwGP_dRl8qP--q9Nj-HG7PbDEiVm1CarKfU-1_hOWZeJwlfTMecmoqQSkHEZhg0EkUSpkVTqRYhTZpEmJjtlR_J2O-Kleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9fKJq4CGj97eKvUR1CVQdeQuPKA5Vaihgj9shP3fJfMAaxeooBXg9lIyevDuWpSeQEeLyinDE0Gec5kbcBU9Zkgk2F9qPyOEGKygxAGZpFFIl0qEU2bCnpMeDM-eLMU1k3bRY5a0I3zm6x69zD3UL_ICJc7s4a1xU5mPYtVVd2MDcRwA5XmXItVlVazVHTW95hpk5AStMPj4AjYLPqLEmzA2zDPFCGju8hdTHa-DyjrhHp7Hs06JwaelCMPhkjnkjkU3vlBYXvjY8n8m2QqG38GcWLL4imbIy8SjHBp01uy0kInnVSzQzfOZ8cyLFEX54AfN2vEAqLoj9irvMKheA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DnYziCI0OLkAQvjNaoMby01i-1xn2HKFy0QvFPq2YAdwYMK-yHd_hEREWx68UJCykrI42TnxEIAm7-wst2O_Ji5J1F0plq66RkMAvsHKKJEsae7VJxa6Ph6TQieLih8wQz8HiFG8JZlGUUlHtSOO7D6o2Wzcb51m-WLcEL3HQo9AYjFHraV-u9nR539qWkNRI6IaNqwnZHXs5x6jJ8wV6AwKFYOmElTgAOhIoAeZy9S_LB4KUcDHKiDFf4uXNjklnVjqR0C7iE0mC6_9z35u-E9JFY6IzxEGFeWxnb3xjR7DQLoQFeg3v9VaV6GywsxBQhGIdzXj-feea_N8BrYx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DnYziCI0OLkAQvjNaoMby01i-1xn2HKFy0QvFPq2YAdwYMK-yHd_hEREWx68UJCykrI42TnxEIAm7-wst2O_Ji5J1F0plq66RkMAvsHKKJEsae7VJxa6Ph6TQieLih8wQz8HiFG8JZlGUUlHtSOO7D6o2Wzcb51m-WLcEL3HQo9AYjFHraV-u9nR539qWkNRI6IaNqwnZHXs5x6jJ8wV6AwKFYOmElTgAOhIoAeZy9S_LB4KUcDHKiDFf4uXNjklnVjqR0C7iE0mC6_9z35u-E9JFY6IzxEGFeWxnb3xjR7DQLoQFeg3v9VaV6GywsxBQhGIdzXj-feea_N8BrYx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWCQgsW7Zvz7IXpmsQyDS43yS1sM3gqI9A3FpJY-exOw4mMjRLtz3txX3T403L5FGzTfUa9e64T15qdJ0Gf5FWBMEVFKZ7sc7tZyqMNHgq69cWf9wpyUWP7c5eoRx6OVIk0Cf8xbARknj977cgrHnzjoOTSC06AQZxml1PuWeQAyXKHtyWhB0WNsbpWH2leOwcArcm1m1A2n-vQcoZvve2EuMCIBVoNm2hhdy2L0HqG_rVEZgj1rdWGH-ExAGe-vz7-ckarwQS-lBZ6g4yvXl3czCeXTlfzQ9tidMvlmqOek0eymtUAsMbVxUcw5LTyrZRmj6o8jd77puzjm28y_pao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWCQgsW7Zvz7IXpmsQyDS43yS1sM3gqI9A3FpJY-exOw4mMjRLtz3txX3T403L5FGzTfUa9e64T15qdJ0Gf5FWBMEVFKZ7sc7tZyqMNHgq69cWf9wpyUWP7c5eoRx6OVIk0Cf8xbARknj977cgrHnzjoOTSC06AQZxml1PuWeQAyXKHtyWhB0WNsbpWH2leOwcArcm1m1A2n-vQcoZvve2EuMCIBVoNm2hhdy2L0HqG_rVEZgj1rdWGH-ExAGe-vz7-ckarwQS-lBZ6g4yvXl3czCeXTlfzQ9tidMvlmqOek0eymtUAsMbVxUcw5LTyrZRmj6o8jd77puzjm28y_pao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=T7pcNtoqj7SDAuUNMni8n_KhJ5bYwFWH6pMoI3-p8vA76oSSPz1laNXfKsTpPLYpC2LHzwy_dISwbHAyoINWqaw29_HoENwbp0rTOfLpeS6EytKicVwFEFoD5p-dLCggO0zMZwWR9C_7cU9L1xg6yZTAU3GgdQecyg_i0WAxfAxaFnJX7V3KxW2zpd7jnirao_3VhCfBvs9YjmVtEEymOQKCKCrFzNWjvG2gJyK4XmUtrZaB7XCmbsYW6cxiXgSqUEfSNmgVLS2THd_va6FMKHtMMMCCiCF4tbbshni8Kmt5gFJRjfwmJtcQt4g_-Y3pmY5Z0bFKbbbDhCrCp1EE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=T7pcNtoqj7SDAuUNMni8n_KhJ5bYwFWH6pMoI3-p8vA76oSSPz1laNXfKsTpPLYpC2LHzwy_dISwbHAyoINWqaw29_HoENwbp0rTOfLpeS6EytKicVwFEFoD5p-dLCggO0zMZwWR9C_7cU9L1xg6yZTAU3GgdQecyg_i0WAxfAxaFnJX7V3KxW2zpd7jnirao_3VhCfBvs9YjmVtEEymOQKCKCrFzNWjvG2gJyK4XmUtrZaB7XCmbsYW6cxiXgSqUEfSNmgVLS2THd_va6FMKHtMMMCCiCF4tbbshni8Kmt5gFJRjfwmJtcQt4g_-Y3pmY5Z0bFKbbbDhCrCp1EE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOaQzm-BD-frejTauk4oYC8nRxBWsWz9l_voR-QhqVA4Rz1bIdpSwWKZ-zmwJXp2ijujcTc6uZHflCNqlbSLurA9UFOLKD7mEC_rWm3sd3nv1rHu3qNjkUoTtqktj1C7ruPs7V9U4Gn5tYaqlGakaK0cD2RyuDf1W-tMSYyBwDIQ_4dszD9jpJwcd8LhoUqeVEX-50rhSEVZUBGUmSBrmgQFn0bwGPDkgpAeJFzvDi_uDZIH_V0pIMQ6CZEuCkOpXCGtEPWi2bVBYrnmxMj0q50sZggQPW_4-XTWIULML_QYYG1y6X7egC-QK-_XG_kSTe6Lrob-qnPIVdcahJ5ZYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiUq9pLM-_WZwC9h9SmicIvVszFuMYzdohffg6SfR4Nbg8m8EzSrx5zFQ-1j0PgSqsrvKEjImV94hkB-fIrdEzkR3j0LqB69NRPevajGc3MQcQqnC94u0NzVGPILZBdJjc1nLvnXGvEZo4ykkpDO_eKTdz9pa4nhcKcYvI6nYVM44ZawkttHAHx_2QozStVmN_1Olml-k30L2m05pWRiwhtV_YzhvG_XSndZrceH_NTlgSgS2y7OBU1Gf-z56yyl7h7EdnBXXX9yx_JrtwE1KDchpqrM73W3uKyOaDj31iXr3egCGS8b-C-eEnKaSpe_JdmXynMae7Iwy9oDYDb7Ngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiUq9pLM-_WZwC9h9SmicIvVszFuMYzdohffg6SfR4Nbg8m8EzSrx5zFQ-1j0PgSqsrvKEjImV94hkB-fIrdEzkR3j0LqB69NRPevajGc3MQcQqnC94u0NzVGPILZBdJjc1nLvnXGvEZo4ykkpDO_eKTdz9pa4nhcKcYvI6nYVM44ZawkttHAHx_2QozStVmN_1Olml-k30L2m05pWRiwhtV_YzhvG_XSndZrceH_NTlgSgS2y7OBU1Gf-z56yyl7h7EdnBXXX9yx_JrtwE1KDchpqrM73W3uKyOaDj31iXr3egCGS8b-C-eEnKaSpe_JdmXynMae7Iwy9oDYDb7Ngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=H2C7wWSz3ovZHm-cqbJQ7inl3ajIUDHWHO6LealWkdTAO3Sj9UfyFWKaT_ySO8qX8DHAiEXamhOH3RT08mUe2QVaGUc88ib-ih_n-dUhBboN2ZlcgvdjcvjFLwU4Svo8999cvMFo5i6Qqx0xWbwvF6Q4WiF2OQlaWeQ5cmBkXm-OyKUTYwS9IuJFzfXuucKFMQI_BQ_YOcKjitDW9SsK0RyKgxTzQjkN2acFNXRKnevZibkh02vfZnq-4ijEPjXDsNGUXOkGHNBOmdW8tW9aBZFlVVE2zUong5QoFrka-QDy-JpBKMUkv34gwRnhxXol7xhUCtRjEk0O9wabpqpK2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=H2C7wWSz3ovZHm-cqbJQ7inl3ajIUDHWHO6LealWkdTAO3Sj9UfyFWKaT_ySO8qX8DHAiEXamhOH3RT08mUe2QVaGUc88ib-ih_n-dUhBboN2ZlcgvdjcvjFLwU4Svo8999cvMFo5i6Qqx0xWbwvF6Q4WiF2OQlaWeQ5cmBkXm-OyKUTYwS9IuJFzfXuucKFMQI_BQ_YOcKjitDW9SsK0RyKgxTzQjkN2acFNXRKnevZibkh02vfZnq-4ijEPjXDsNGUXOkGHNBOmdW8tW9aBZFlVVE2zUong5QoFrka-QDy-JpBKMUkv34gwRnhxXol7xhUCtRjEk0O9wabpqpK2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=sm9c1D7h5bh8tRHi6OfG31hgop5_QgunCuTXErMx6fmhG6OaFbFtVgyVwQaxvprzToA-WjjOKh8cxVxr9Y1bmSNUuPgI4KDFvSHtDVCodwLYii6SmLvw8tUVAE3MRvF0p6oP4en4a9MoDyM4imgKvrWuYLdbSa3-J9Uwc8YB5vUvRX2JMoP2jB9SdtG5UpvjbOXrPf5BYfzYe2bMd6DyXU7BCAuGtp3A4sRsQveux06VW0uVuf4ayn_OzO48Cn_cGNMXZPi6CN2RjNzrp8oRW-_aBgSdFnUugrvYzHo-FqhG94-2CmEcW44wAMF_tI5q77y3DbmvVbsuXy4cR3tHtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=sm9c1D7h5bh8tRHi6OfG31hgop5_QgunCuTXErMx6fmhG6OaFbFtVgyVwQaxvprzToA-WjjOKh8cxVxr9Y1bmSNUuPgI4KDFvSHtDVCodwLYii6SmLvw8tUVAE3MRvF0p6oP4en4a9MoDyM4imgKvrWuYLdbSa3-J9Uwc8YB5vUvRX2JMoP2jB9SdtG5UpvjbOXrPf5BYfzYe2bMd6DyXU7BCAuGtp3A4sRsQveux06VW0uVuf4ayn_OzO48Cn_cGNMXZPi6CN2RjNzrp8oRW-_aBgSdFnUugrvYzHo-FqhG94-2CmEcW44wAMF_tI5q77y3DbmvVbsuXy4cR3tHtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=cShXChAeDOSQUMYHKGZyalzeZ0dS6FZdoOy6jsYWCPIglutJup0EgZHBKaux2DtcbnYxJB75DroJBhdJYhxqpFlkqZMMGyZJUGB5WFdJFP9LzmaquxeEtcepFwyntx6-Q3FICw-pnM6kTwbdTXelL854kGH_Ynr2tS9_Fx5mwKhFpWgylxK7MlgUlS7jb0Cj5s8G5jfGVChb2Ug4m4H38MbxTAhJFIb7GUCoW_z9WRDWPGc66pWtbDBpF44o-gLJZ8hwwqTp9feuls7KSW6hhkxMibtQrMKECyqFpKWHnpnBi5WmI5dyQNiqSkRBImCsBZH67ZggFZh59tpQNe_Oag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=cShXChAeDOSQUMYHKGZyalzeZ0dS6FZdoOy6jsYWCPIglutJup0EgZHBKaux2DtcbnYxJB75DroJBhdJYhxqpFlkqZMMGyZJUGB5WFdJFP9LzmaquxeEtcepFwyntx6-Q3FICw-pnM6kTwbdTXelL854kGH_Ynr2tS9_Fx5mwKhFpWgylxK7MlgUlS7jb0Cj5s8G5jfGVChb2Ug4m4H38MbxTAhJFIb7GUCoW_z9WRDWPGc66pWtbDBpF44o-gLJZ8hwwqTp9feuls7KSW6hhkxMibtQrMKECyqFpKWHnpnBi5WmI5dyQNiqSkRBImCsBZH67ZggFZh59tpQNe_Oag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3OyxeFUeAuGYlSI71m8QDvI0X-h6tfSFvgXTImA-Zo7--azJAZDxqtRRDqvwDiES2xgtJFnsJ5nImQgP2Ne6B_r_hwjZaQAVXBkLAEXy_iVt1P-lEfQYEKWaYaNAf_DecMmPFVaSsxOHe0SUUzu2gZSdxju7unAM1jtFf20DuIYJg7s-nGk-w960XxATksyvJtlXjivBdw2DQXnBKROIuXZxDtTP31tbYqCX5YLHtNPI-TXisnUVoOsSy-i4gxOXTMfr07Y3P3l252dXdsAc0Svl0dPedGpagCgApCEAkx0FHB-DRDBGWveY8LKv53NNv1OM6R9erDwvpZne6wvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2LvJX0E8BY1K2tJy53LCgdjzoN3nP6HfutfbBW2I7I4vKfDKpTcodBVkahjkJcj_lO7WzY2L5wUMKn0wrMcFY0dS9AJM-r4C2MqogFnRSjHLKZK19xOi-cuqluMKO5f1uS5SZBPDzTH6TN1hgT1tU4VzDpd020nhbCIcog6OFohXrDUQb6SVrJZ7aFqTiEfSuu00a2JTt4KVbtB2JWcxlSmw32BUaK-mQ4t6D8kPkjTW4O9sy0DjSFGM7BvnOK6bByKppjnGfU2cVyO9bjQ_wYCWi7BEpFYVMPkpEgRhbK9JvtQy2wM4oyDzU4Cc1o4LpyymaoOGfYnjQqA-FNnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=nIQkYrhOWicaMQAKrXxU15XD5lZoaUSFffmSnDKQuAYxJVPJm2gnN3JADEjyhhitJuSwOIzvUlU0TvMmVY0vJHagscUHHjFy_UNIDwaoUld_i-cv0aRzu_xQTGvyYoQibbQpeZwDpqTfRs5ctgEkj82ynmbNsS3iUCqCmpfTfcmdn-SzWbsZmY1qwnseQChN69vEgze4Y-FbRYKNT-SZW3K9BKRIkGYSLF6b5P95rT3ImdaaFYv7dQGfrBa_1wmLs-hqUx2Pg6-fbDW3cCEzEWGefudiWFcGrpKVYLYBP_HlfdjsLWr2untV7Yr8E1171s55xQsZbUPTtFthyBOCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=nIQkYrhOWicaMQAKrXxU15XD5lZoaUSFffmSnDKQuAYxJVPJm2gnN3JADEjyhhitJuSwOIzvUlU0TvMmVY0vJHagscUHHjFy_UNIDwaoUld_i-cv0aRzu_xQTGvyYoQibbQpeZwDpqTfRs5ctgEkj82ynmbNsS3iUCqCmpfTfcmdn-SzWbsZmY1qwnseQChN69vEgze4Y-FbRYKNT-SZW3K9BKRIkGYSLF6b5P95rT3ImdaaFYv7dQGfrBa_1wmLs-hqUx2Pg6-fbDW3cCEzEWGefudiWFcGrpKVYLYBP_HlfdjsLWr2untV7Yr8E1171s55xQsZbUPTtFthyBOCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx9exegr_RSNF6piSd2ErMA68tMC_JTanSWAsn-Hngzwb9lPAYNJHVpulM7QU5VrRytlD4iXDqR7Kn_SaO7UYCnALIJR1XrLb-1oJhQSs0ZTFncdcgCxj1rqe05dho1bC6XjRxYQF9NH41viWYPT-VWzUaNZ4yPL9ECQ4-hzpNRTCWZ107qlqsu7TT5JfBVjQh-J6XjuFnyOkxvQ0UN7J0VLE1FYlWMlw_-9xGGl9fLgHpUMYXWRaaVZSRhIkmaAe8isL6fJIphW6D2F6C8a4f6zPof4zDXfHMqzZpOlUgVhz9J8CIU0cIS86XVw0QU6bwX7N8BnTZmdl1I5sBM7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbdwcTQE21uZ9ocQtPNRJ5_ZZObzlQ8txLm18ATeI5R7k5Y2cstCJDUuUGkpqss5iRe-AEnl4vIUKwlBXuDCl0EOgbGvNeJKPpZK5GBNkD8rv5h5FgS1MOGm3XJXst3_HygD7jn2bYeJsyyG0wQkdyRwrD_x4f25CrMxMjKOAw5X2odZDvB0N6wZLKuqATBPJqKiHZT5FmkBXoZwvliaNLO7i5KmPSVcHiwCP45xtx9VcPPFcbbqd-j4f2iyrKCUP96M-T4L2tg9T9s6KPSXrMZImun6y2ynGnUpooYdrgG0E7RJFGRGPTePLuZfvXq1zi5H5W9JClCe9qb2zpw_-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=uWPspegeE5zqssewpKTg-SFFXR_-S1FGVR6fECKI7IP7Gqu391Ik3Bq_vu5zbft4IGgafvq181DfX5OCGhMJeHkgiMwce6zgxwrle_jKSkbbKFEMozIYseA4ntzunVW3E3LzmvNz1M-4puZF5M3xI1CiLnr9ySvrbJksGr9an5_U3SMASzelSs65HtiNYDDVRb7M3MOBxKJ5BjGRcG2eIdMAoxx_BvBZqSXIzZIWS7m8nTXRGKZ3qYZX827wt2QETnG1KJy30lI16YfXMmawjzOTtqBh0yAjcd796bklDjNr-ux7nIK8PfdudZoBeH89Kl7WithQTFOmXF7OY-fsYWvutFRSyHCRH-cLlcumCCCe99hA1tDhSqlzYAL4UHhDkA-AGmyzocvlbUmR7qQo12mGf4horzO690px3m_KMvRhT2ij5AjIbokhXGaGPrdEg9xEXMB40Shm5BC8WcPGoSlTnnGNZcFN6fPbJE3L5W27o9ZXlIQHJT49-pHycYWU5TZeqL4g2cP7LoVgfsVsVx7qZpWyOsRZwj62CW5ieRhIsnb1zp9aVCu_HITyvjM1uhHL2yUllLN4pRgku7AuI8di-GJrGRl340W4DXcaEYt-awRmllQPPU7JGD5XaBkckadNj2VqNq_S7n3gJPwVxtuTectxU1qEhRIfO1F7fpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=uWPspegeE5zqssewpKTg-SFFXR_-S1FGVR6fECKI7IP7Gqu391Ik3Bq_vu5zbft4IGgafvq181DfX5OCGhMJeHkgiMwce6zgxwrle_jKSkbbKFEMozIYseA4ntzunVW3E3LzmvNz1M-4puZF5M3xI1CiLnr9ySvrbJksGr9an5_U3SMASzelSs65HtiNYDDVRb7M3MOBxKJ5BjGRcG2eIdMAoxx_BvBZqSXIzZIWS7m8nTXRGKZ3qYZX827wt2QETnG1KJy30lI16YfXMmawjzOTtqBh0yAjcd796bklDjNr-ux7nIK8PfdudZoBeH89Kl7WithQTFOmXF7OY-fsYWvutFRSyHCRH-cLlcumCCCe99hA1tDhSqlzYAL4UHhDkA-AGmyzocvlbUmR7qQo12mGf4horzO690px3m_KMvRhT2ij5AjIbokhXGaGPrdEg9xEXMB40Shm5BC8WcPGoSlTnnGNZcFN6fPbJE3L5W27o9ZXlIQHJT49-pHycYWU5TZeqL4g2cP7LoVgfsVsVx7qZpWyOsRZwj62CW5ieRhIsnb1zp9aVCu_HITyvjM1uhHL2yUllLN4pRgku7AuI8di-GJrGRl340W4DXcaEYt-awRmllQPPU7JGD5XaBkckadNj2VqNq_S7n3gJPwVxtuTectxU1qEhRIfO1F7fpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E67JCsPWQZB5gtdIwiCBcfZEgD_DR0dYqp3FtyNyVcpDW4VHK9LjcZpaf94RElf0A69_j-MnswwD06AbRgeHrDpeVoFtyxpxlzOLNpg6lzU6GzAckkpWXXJULIt38_exbHfI5ixAErakQzNu6jLGapCe4ebhA42Mbw0x08JM6MMGDKvhFLhBeToc1fXLoUDrOaCbUdiJw8-W_bpPA4DXKFbuQ0tw2mABL3UDDkIfAv-MfnSkXcYE8FVtWzygZaYXdwoCKiCuV3tVg6iGwrOrG0mqIQmqmJeVPk9HTJUYn6eFeRQhMvgiwmqyuCU2Oq-ZRoNoenNFCHo173aqnTFdgvaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E67JCsPWQZB5gtdIwiCBcfZEgD_DR0dYqp3FtyNyVcpDW4VHK9LjcZpaf94RElf0A69_j-MnswwD06AbRgeHrDpeVoFtyxpxlzOLNpg6lzU6GzAckkpWXXJULIt38_exbHfI5ixAErakQzNu6jLGapCe4ebhA42Mbw0x08JM6MMGDKvhFLhBeToc1fXLoUDrOaCbUdiJw8-W_bpPA4DXKFbuQ0tw2mABL3UDDkIfAv-MfnSkXcYE8FVtWzygZaYXdwoCKiCuV3tVg6iGwrOrG0mqIQmqmJeVPk9HTJUYn6eFeRQhMvgiwmqyuCU2Oq-ZRoNoenNFCHo173aqnTFdgvaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=bmqniNYzQ821QLq6rfXd0nRelBfq8VtSMwTkkT_bnthI0X5kUu275Bg5nnB2IYIoEu6ENP-mLfseq1oXeFtKBQuyzaya9brzy89DUGSarBQUd4H-EzJ2TK1BHwRDrMzUuS3frPqqS_WcNRAsqz1R_8phMFJFPQL4mdENBYVEljYRa1ZAeFNf1Xy0Xom2ENGyKmkwcRBEBBjlQg9FC4hDyDQyTsANNqaH-WfgOz7auSpScp0787HVz93ExazejsL5oUptTGRH1gnzfzSSgQIAzktUXA19Pv3LMTs-CuPG6PshTHUkO6jNcy3Le19gHQDqLo9KHVKE2KdD_NfyWr31woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=bmqniNYzQ821QLq6rfXd0nRelBfq8VtSMwTkkT_bnthI0X5kUu275Bg5nnB2IYIoEu6ENP-mLfseq1oXeFtKBQuyzaya9brzy89DUGSarBQUd4H-EzJ2TK1BHwRDrMzUuS3frPqqS_WcNRAsqz1R_8phMFJFPQL4mdENBYVEljYRa1ZAeFNf1Xy0Xom2ENGyKmkwcRBEBBjlQg9FC4hDyDQyTsANNqaH-WfgOz7auSpScp0787HVz93ExazejsL5oUptTGRH1gnzfzSSgQIAzktUXA19Pv3LMTs-CuPG6PshTHUkO6jNcy3Le19gHQDqLo9KHVKE2KdD_NfyWr31woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Vi1waXolDUmRDEoYfMYVKUxsr3cW0OLsfzp8OYuAf8lQ6ktSqY7FRa7RtpzKtqAS3IWCMs5mU-ZeKw-8Jihv87QNBB2g9js4wBKhIq9DIa3XBh7Xw5nXRHaDbN6c--JNGFlv4LzgCULr-Y2zQKRI1SCtUoP8ZHsmbdmtZzDcJpefaI8vF73bEoPo7LyLINjwcnzVr2rjaOZZTb1u-XXXBSaKsCRn2S5jyJE6Ws4KgfJHEKC7FffLDjHo4Ex2HoyQxH68_q-Lc198M4O-yG-8cya4_uogpQwfdhdadKcIX0vIGKzEnB-TyIyDUStOj7VmOO_ZYrLLgg9YtZitr6Q8vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Vi1waXolDUmRDEoYfMYVKUxsr3cW0OLsfzp8OYuAf8lQ6ktSqY7FRa7RtpzKtqAS3IWCMs5mU-ZeKw-8Jihv87QNBB2g9js4wBKhIq9DIa3XBh7Xw5nXRHaDbN6c--JNGFlv4LzgCULr-Y2zQKRI1SCtUoP8ZHsmbdmtZzDcJpefaI8vF73bEoPo7LyLINjwcnzVr2rjaOZZTb1u-XXXBSaKsCRn2S5jyJE6Ws4KgfJHEKC7FffLDjHo4Ex2HoyQxH68_q-Lc198M4O-yG-8cya4_uogpQwfdhdadKcIX0vIGKzEnB-TyIyDUStOj7VmOO_ZYrLLgg9YtZitr6Q8vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSWPVNKB8sDEIm7vgyGvQpP5zT7aFTths1YYe0hJJTs18WzvDS2dG23p2JNOqd61eYxuEHttrHrd-1VLLD8g47TbiHVcOpjbwGFDPSdtRsThR2L5B_S-vRBXIVWifbHcMccwvtH6ey92rsO_bkVux2vUCBbQsd8Tfp64CzDjcPQwh3jMhVBlwTjKyQerzBYWJihzN7dJuU3h6y2u2FH2HyvQMVc7iPQ7eyebYL3p1qnFQFDwQPskgJoMSFPPLidZraAnnDSP1KEz7KyQei9l_wdp-TwcMuwj8EdJuRU_RjkggvlC2unDuQLR1QzOFHluK41oz1Nc5lNynJlhGJ19xw.jpg" alt="photo" loading="lazy"/></div>
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
