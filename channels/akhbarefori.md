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
<img src="https://cdn4.telesco.pe/file/DGShUanv8_LWDxyF8PR0FrPs1WjMxZyO4rPM1U5RMu0Zv7SL6Y73mjygwN7OfSNE69SMQ6NSEXslUJBgNdFjRjAEepWsdCUijUfUBpKrmLWAfsJNZk8WYywg_VfU7hqcP_FP1UEdb6fyEEz9ZWLEb9oiyY5NVJx8NJzPdtJYKTilhTv3skObCLNSSpxDVNmouCEKNmIIxOJjYXbofnan4D5swVqAOQIO1cUCdpJTUxoaDvU5k5RBo9rdkChHNbHy_bUsmR3A4JjaxJkVHngBWN38_LlzvLbu-uvvkiTux1bC2W6rLKZcXt_a_D4Nap2Gt2YBnazfEgwHk2fOHQ7zSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-656144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گل در دقیقه ١٢ برای ایران توسط سعید عزت‌اللهی
🔹
ایران یک - مالی صفر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/656144" target="_blank">📅 20:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656141">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c441d35b4.mp4?token=jdFIRbKwWlIgKSmVXocTdjD7UnueKSvYtpU-HnHGIJtVVFNJ9pash5dvHzG7F990Ovjetj6SoRMKfCIE0Ciy4lt5FcNNRuDS1B7wBoqZpZfHRcO7JEXyrsq7XE-wwYOSET6kwu23hHenvRRBvRLGdwYsUx-GVQV-2ybMWwAsQZT6A_K1zRcq5JlMTANgmWBlKsBD1lZVBwoADvVJlyXhgtA1ZoYRMII1Me8nCfW-Kz5aI8qD2BBxg7vdFcMFrj9sgdSnypMV5qEw9D0L6UteQKPkWIARHu0eLOVyR_hHCQPuHmLzr5bisKDJwav62WUkTfRcD967-O-goZcsG1lunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c441d35b4.mp4?token=jdFIRbKwWlIgKSmVXocTdjD7UnueKSvYtpU-HnHGIJtVVFNJ9pash5dvHzG7F990Ovjetj6SoRMKfCIE0Ciy4lt5FcNNRuDS1B7wBoqZpZfHRcO7JEXyrsq7XE-wwYOSET6kwu23hHenvRRBvRLGdwYsUx-GVQV-2ybMWwAsQZT6A_K1zRcq5JlMTANgmWBlKsBD1lZVBwoADvVJlyXhgtA1ZoYRMII1Me8nCfW-Kz5aI8qD2BBxg7vdFcMFrj9sgdSnypMV5qEw9D0L6UteQKPkWIARHu0eLOVyR_hHCQPuHmLzr5bisKDJwav62WUkTfRcD967-O-goZcsG1lunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت عظیم مشهدی‌ها در مهمونی غدیر/هم‌اکنون در حد فاصل چهارراه نخریسی _ چهارراه چمن
این برنامه به همت هیئت قرار و مجتمع امیرالمومنین (ع)برگزار شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/656141" target="_blank">📅 20:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656140">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b62330897.mp4?token=j7IYKMwbKQHbWxGbfes3VLO-iHZX1KOkLU9XHo0jZTh4dtD-pf5b84z04Ohq7YYWSE550FbDxPRP1m0tDPJk4QqNQSjxulKYPKNjqFyOko61HQHHUVO1_kxmlV4a56HdAcMHQ8VMote7VVoDUEaEqgWFxF7EBrF3aJNZuoCXNjSjdNCwOI2b40BHzz0-Bg6tA-iVFx7mFdBHI_Qziy_g2yTF4xc0thR16hsXHO2j9DoYEXTHFwAyz9FPyujqBljtM7de7gHS4T7PHM9qcQAqOxjdQUBKABcTTy2XfG_jLDhe8wfgmRkdj4r1NvMCQx1XnidHi758JWUSXb3sKOAScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b62330897.mp4?token=j7IYKMwbKQHbWxGbfes3VLO-iHZX1KOkLU9XHo0jZTh4dtD-pf5b84z04Ohq7YYWSE550FbDxPRP1m0tDPJk4QqNQSjxulKYPKNjqFyOko61HQHHUVO1_kxmlV4a56HdAcMHQ8VMote7VVoDUEaEqgWFxF7EBrF3aJNZuoCXNjSjdNCwOI2b40BHzz0-Bg6tA-iVFx7mFdBHI_Qziy_g2yTF4xc0thR16hsXHO2j9DoYEXTHFwAyz9FPyujqBljtM7de7gHS4T7PHM9qcQAqOxjdQUBKABcTTy2XfG_jLDhe8wfgmRkdj4r1NvMCQx1XnidHi758JWUSXb3sKOAScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه خبرنگار اسرائیلی به وضعیت آتش‌بس در شمال فلسطین اشغالی
🔹
پس از حملات موشکی حزب‌الله به شمال فلسطین اشغالی و فعال شدن سامانه‌های پدافندی در کریات‌شمونه، عمیت سیگال روزنامه‌نگار مشهور صهیونیستی با انتشار پستی کنایه‌آمیز، وضعیت آتش‌بس را به سخره گرفت.
🔹
سیگال در واکنش به رهگیری موشک‌ها در آسمان کریات‌شمونه نوشت زیباترین آتش‌بس جهان همین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/656140" target="_blank">📅 20:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656139">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9ea5df58.mp4?token=A3rqqei-2OgiXjmWRu9XVIyZFkedVKOYbIcb93ndumdq-M0F4nb8HJFqGRjUbCbfvMge2UTXZ5KJFDh2XyID2Xq8vG6HmAtXJs74SksYHJd9edomGxPyG89VRsXt7f2wmdix1XaLHcnPlyLCxH5jtrETAZm9ueZUCy8reHHMv-HHuaPy6aIgF8n2qATem8SQ57Zxqi75W-63EpwMASxEdM_e6qCxVq3712l-rPfujRC5l8j181BVBMET9itBrah2cmjyecgEiM5wxcWwVvdRVO_wEnJan5dbQ3jY18bdMAOBoBuswjuoBJLxZWtfBOkRbxERLkRACNZraPGij7qgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9ea5df58.mp4?token=A3rqqei-2OgiXjmWRu9XVIyZFkedVKOYbIcb93ndumdq-M0F4nb8HJFqGRjUbCbfvMge2UTXZ5KJFDh2XyID2Xq8vG6HmAtXJs74SksYHJd9edomGxPyG89VRsXt7f2wmdix1XaLHcnPlyLCxH5jtrETAZm9ueZUCy8reHHMv-HHuaPy6aIgF8n2qATem8SQ57Zxqi75W-63EpwMASxEdM_e6qCxVq3712l-rPfujRC5l8j181BVBMET9itBrah2cmjyecgEiM5wxcWwVvdRVO_wEnJan5dbQ3jY18bdMAOBoBuswjuoBJLxZWtfBOkRbxERLkRACNZraPGij7qgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری تماشایی از رعد و برق در آسمان چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/656139" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656138">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793266281b.mp4?token=vsIhPRF9FNqiMIfGK_-vN19RWS6-LxaGHrGowRcJEpf9LvoIZkQrQXuKBL0UMsbLRI1NRfNMOh9sraUTft6YGCYGnzH8uAQZtubdhcdTFlKJUqlxKvJ4oA7AE3iWDssfQCT27PlUtbbHNzAYb2W5jDpLScxbGCEHMeR_8uOpvCBYwlxN4yKFRKibe0w2P1CL70sMR9RlBJSdGpgd0NixEgvHFvjJY5o3jnkcnLdAhKVYWObv9r7bXmfjdXZYagHQZs-jJ077jUubias75PUUIfuVrFg3Y4pyxVu18QMAsH90T1DmSMdp9Srx3MNeJAHKMMpHJuAR7jkRJdRNEe7e_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793266281b.mp4?token=vsIhPRF9FNqiMIfGK_-vN19RWS6-LxaGHrGowRcJEpf9LvoIZkQrQXuKBL0UMsbLRI1NRfNMOh9sraUTft6YGCYGnzH8uAQZtubdhcdTFlKJUqlxKvJ4oA7AE3iWDssfQCT27PlUtbbHNzAYb2W5jDpLScxbGCEHMeR_8uOpvCBYwlxN4yKFRKibe0w2P1CL70sMR9RlBJSdGpgd0NixEgvHFvjJY5o3jnkcnLdAhKVYWObv9r7bXmfjdXZYagHQZs-jJ077jUubias75PUUIfuVrFg3Y4pyxVu18QMAsH90T1DmSMdp9Srx3MNeJAHKMMpHJuAR7jkRJdRNEe7e_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون مهمانی بزرگ غدیر در مشهد حد فاصل چهارراه نخریسی _ چهارراه چمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/akhbarefori/656138" target="_blank">📅 20:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656137">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE6s0nm-9mkcmUouLmJNUNCa84vx-l6U5g7c0W4PN1eCIG0H9yhAuYvkNKS_hIBvl79T3xqY9_q1ipRBcBKaPJodHPHFQ0LLN2e9_--pSblK-3VHzsBWn1apaeUT90TLlXgBKTobTXaFzkEIWqQmW4Nj0b2x4AZR4B7rY_Hhz12G5aybweMzWIU6txzHcdZVi3R2RoaTCf-PZetd9-S5ryR-TOYn3h01E8uIgvfdTgPc8AubLW7OWeoFMVSIaci2hGSBuzSBv1cveEoRUHooz-Oui2850x3qElWeZfuZbLu2hlaUX0eWItfPHd_ICF9DUo_U29Xs20lQDO-6oxzEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داستانی از عدالت، تواضع و نور ایمان…
🔹
در روزگاری که عدالت، جلوه‌ای از ایمان بود، امام علی(ع) زره گمشده‌ی خود را در دست مردی مسیحی دید.
🔹
ایشان برای اثبات حق خود، نزد قاضی رفتند و چون شاهدی نداشتند، حکم به نفع مرد صادر شد.
🔹
اما همین عدالت و انصاف، دلِ مرد…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/656137" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656136">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کشف جدید در پرونده سلاح‌های شیمیایی سوریه و واکنش روسیه و آمریکا
🔹
معاون دبیرکل سازمان ملل متحد در نشست شورای امنیت درباره اجرای قطعنامه ۲۱۱۸ (مصوب ۲۰۱۳) پیرامون نابودی برنامه تسلیحات شیمیایی سوریه گزارش داد و اعلام کرد: حجم قابل توجهی از تسلیحات شیمیایی اعلام نشده کشف شده است. در اوایل ماه مه، تیمی از سازمان منع سلاح‌های شیمیایی (OPCW) به سوریه سفر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/656136" target="_blank">📅 19:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656135">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727aca4cc1.mp4?token=q4f_g4u163LOr8rmh8M450ZG-A2CzuDvKkdIyRvegQd4lrqckr0SDb2cQAxAmrSNht7GqLD2sC5BJOD6oRgy4N0xh6A_T1aFhyQxCwB6zjvyfIxNBKSrCpUrrOhZQDW4TXA0zLi9R-lQSisuYOgCaZELD7C27wHslAtgzqle8GXo-Tw5tmrHbwzNR0qKSkivWmQBtAiojPYVqugaqy4KnErYNDcb7cw2GrktsmADAgGLwLdXV8wf6owjfGlSotrZh-M5ZwgBKmyxXu3OtbfH2cwCWUVBEoJqXxg2ELw-MpvbT3lIXsTSrm1rzAiPheddyMElQlaiPdeqrOTkrGCafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727aca4cc1.mp4?token=q4f_g4u163LOr8rmh8M450ZG-A2CzuDvKkdIyRvegQd4lrqckr0SDb2cQAxAmrSNht7GqLD2sC5BJOD6oRgy4N0xh6A_T1aFhyQxCwB6zjvyfIxNBKSrCpUrrOhZQDW4TXA0zLi9R-lQSisuYOgCaZELD7C27wHslAtgzqle8GXo-Tw5tmrHbwzNR0qKSkivWmQBtAiojPYVqugaqy4KnErYNDcb7cw2GrktsmADAgGLwLdXV8wf6owjfGlSotrZh-M5ZwgBKmyxXu3OtbfH2cwCWUVBEoJqXxg2ELw-MpvbT3lIXsTSrm1rzAiPheddyMElQlaiPdeqrOTkrGCafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سریع‌ترین راه گرم کردن غذا بدون تغییر طعم و بدون کثیف کردن ظرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/656135" target="_blank">📅 19:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuY91s5p9FYw0vWWRnmeQ9PE_Eo6AAdL1EWnbdiU7tQRd4Cn-z-z0vMQ8bxxALUFHF8C1ISHNJXHJ1OMKhmdH-_ZEbSUe045ufoju-XDtWVLv8vasqfZghPDFNX8S2o6sZgHEwWqGAcqoHp7rB06OA_AiPu7axZImIdg4QelVPSgYmKRQ6qQpyjkBN_r-4l8VUtg1glOk8mWGSUFeOtJJMnVUuVrkRaxAb_vTwvzQD5b1IJQ3YnkIMWNXnsD9v7boIOQZyci1A0NYoa7ykVMUEB5FbexIEolZ6bQA_NxvtxXBT8gcUZVqmsXt0behjD4jSSY5wcr-liTLjlScyPAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940b725639.mp4?token=IH1ezDMcNr6BbZ4nmHe-nHu0okWoWf40LxvzrMf5Xa4mPRtNbw1W3G6KlMKhs4_Q9nLwRfDbHCVFHdyml2tew-f9cKcmV7NOHMfmxTDpMLf908AuqFNZ2Ph_IEX0VZjJ6Qr25FhcyFmtmTuBk8Zef_FeoLvOrfS-5Ap3UdxzYU_R4F6MhBJ4agTFKtA-l_nlZjtB49L3g4SZ8Ev_SsCNGnir40qKuYiduNBUs1be60RkuKv3iI1rEpL1OU5qNn1zuoA8aZnHM2iP08k01hACg-IwvDW1zgijW_IXEYDDsuRmT8GDz0e4uVtJLJ5bLS4WK1acBpRF32HEeSeFbOoolA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940b725639.mp4?token=IH1ezDMcNr6BbZ4nmHe-nHu0okWoWf40LxvzrMf5Xa4mPRtNbw1W3G6KlMKhs4_Q9nLwRfDbHCVFHdyml2tew-f9cKcmV7NOHMfmxTDpMLf908AuqFNZ2Ph_IEX0VZjJ6Qr25FhcyFmtmTuBk8Zef_FeoLvOrfS-5Ap3UdxzYU_R4F6MhBJ4agTFKtA-l_nlZjtB49L3g4SZ8Ev_SsCNGnir40qKuYiduNBUs1be60RkuKv3iI1rEpL1OU5qNn1zuoA8aZnHM2iP08k01hACg-IwvDW1zgijW_IXEYDDsuRmT8GDz0e4uVtJLJ5bLS4WK1acBpRF32HEeSeFbOoolA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نذری عجیب و جالب گلس رایگان در خیابان انقلاب در مهمونی ده کیلومتری غدیر به عشق امیرالمومنین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/656133" target="_blank">📅 19:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676736e9f8.mp4?token=as_owYtPJLVzWtIrwa_Vys8pSz1ubfmMnmseWOcgSQlhTy9ggKoFCUH7VABAc5ZTIPI5DYInXpQRfHvasxXciyJnw_CfsT0_p1sMwRq5cLYNwgwKIPhkenC1gG7guibkBtaR3Dz5HJJPlt3e0LvyxO88X3RhgCOowthugj_GelH3I59m-mtTAiatUKuZGc5aw15D03_2bdJmBCyKhbwIR7arsCLXdYw4LjDXu_dRUCcsCa1cNCwEaUaIaiHlUQcFq6Bo9vWVDYmUENgs3KoL2IEh6rH79-XfYrgVrixqdd97LEvTLzDfk0huIRBMuln8srC-ytB_8iljUxgd6ycn8Rzll7HhnXOJWzYkZC6hkrTbbVC5KnTrPQepq6M4t01fKTwy7pVNGMygnw7ZeE1CDnY5xKy3GP1ffhsPEmAQ-iKnN9-7leyBVFm59vwhAw-wf64-zfFBJfXDvV4jRG05i3lziQGov3LTpDi7HYIjRwMxxZ7EPpsxYPQba5J1yPc4lZgBDXzFKs2kKEdYPrQnsrM8czyPI5QNROBNL0XRx03D9ZP7KL7RtgmBOGqisNFkoEMudFufQNL1C-DbA_ARGqCitb6ZANFTHQwvdvsNiJt_aKa-iXYe8uTSz5KLq_sL_7e1F0nh28_034eBsvRzWsurx_W_ulHN4gzA08sUiyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676736e9f8.mp4?token=as_owYtPJLVzWtIrwa_Vys8pSz1ubfmMnmseWOcgSQlhTy9ggKoFCUH7VABAc5ZTIPI5DYInXpQRfHvasxXciyJnw_CfsT0_p1sMwRq5cLYNwgwKIPhkenC1gG7guibkBtaR3Dz5HJJPlt3e0LvyxO88X3RhgCOowthugj_GelH3I59m-mtTAiatUKuZGc5aw15D03_2bdJmBCyKhbwIR7arsCLXdYw4LjDXu_dRUCcsCa1cNCwEaUaIaiHlUQcFq6Bo9vWVDYmUENgs3KoL2IEh6rH79-XfYrgVrixqdd97LEvTLzDfk0huIRBMuln8srC-ytB_8iljUxgd6ycn8Rzll7HhnXOJWzYkZC6hkrTbbVC5KnTrPQepq6M4t01fKTwy7pVNGMygnw7ZeE1CDnY5xKy3GP1ffhsPEmAQ-iKnN9-7leyBVFm59vwhAw-wf64-zfFBJfXDvV4jRG05i3lziQGov3LTpDi7HYIjRwMxxZ7EPpsxYPQba5J1yPc4lZgBDXzFKs2kKEdYPrQnsrM8czyPI5QNROBNL0XRx03D9ZP7KL7RtgmBOGqisNFkoEMudFufQNL1C-DbA_ARGqCitb6ZANFTHQwvdvsNiJt_aKa-iXYe8uTSz5KLq_sL_7e1F0nh28_034eBsvRzWsurx_W_ulHN4gzA08sUiyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نذری پیراشکی فروش معروف میدان انقلاب در مهمونی ده کیلومتری عید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/656132" target="_blank">📅 19:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آمریکا برای تبعه خود در کویت هشدار امنیتی صادر کرد
🔹
سفارت ایالات متحده در کویت از شهروندان خود خواست که احتیاط کرده و دستورالعمل‌های مقامات محلی را دنبال کنند. علاوه بر این، سفارت ایالات متحده در کویت سیتی تمام خدمات کنسولی را به حالت تعلیق درآورده است. واشنگتن همچنین از تبعه خود خواست که از اعتراضات و تظاهرات در این کشور دوری کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/akhbarefori/656131" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU7FeeuwCMZBe6S4Uc-nVkqw9UK1Qagd_Re1zFg9TTcxE-oPlevay4eAlJhLczKje0OggILQeNiyG0jQge2U2LB9ekACSXqRPdwd43o1-zBRGdUhq86dIlEdh03Pe8sPY7QuoO7zjbbRyDvgO7CKH_ROey_pAP99SpKedWUIy315gBGe1Qps9eoSAZWgnqysQ9ig8bNX0mdIbKaN3PsoxnFndNeWZ0nO6jzmkXm1mm7USr0ZZAUvJthP-QScMU-GoT_IYbAN9F_HqSPDBHuhnfojdUfJHR9_b_oeX8goVV3gtQNkzrTaPglrU3nXpNzQKWkCJzBv-wRCe22slXFB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پدرها بین دخترانشان فرق نمی‌گذارند...
حتی برای به دوش کشیدن پیکر نحیفشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/656130" target="_blank">📅 19:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
گزارش یکجانبه گروسی به شورای حکام درباره ایران
ادعای مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
آژانس نه اطلاعاتی از ایران درباره وضعیت مواد هسته‌ای اعلام‌شده، تاسیسات و مکان‌های خارج از تاسیسات برای اهداف پادمانی دریافت کرده و نه به هیچ‌یک از این تاسیسات و مکان‌ها، به‌استثنای نیروگاه بوشهر، برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی داشته است.
🔹
آژانس قادر به راستی‌آزمایی وضعیت این تاسیسات و مواد هسته‌ای مرتبط با آن‌ها نیست. این مسائل باید از طریق یک توافق دیپلماتیک پایدار و قابل راستی‌آزمایی حل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/656129" target="_blank">📅 19:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35080d7e7.mp4?token=rvwjxe3F1W50NXVac6Xw0ozjPWEu5J5fwTSs8thcK9KQMrjth9wI61ZNiHehady_Krw2lBOQIjbi2NMh8jQ_RJBYncXsVmlf_UHFAXTJU1qNG5vlbvBOuBlOJ5Tvu8tVvO_wiFu7nKoafN95J_1JwBBn89qLXfRvEig1Zwkxz2uWmHeNXXl0elgOBK5xiXoclWF7SUsa2D8hVZfjAAU5VoRJsq4HK4Q7m_o-6kCt8Pm9nWlpA46mgCunI56jsoRXfIWOPJRdNbWIk0sjwHwFIKNxC6OegoWhgXRzB7J39dJX2ZNlz6yarSsK5ojZe6AuQ7mArWoQxr2TcDIkWzxoAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35080d7e7.mp4?token=rvwjxe3F1W50NXVac6Xw0ozjPWEu5J5fwTSs8thcK9KQMrjth9wI61ZNiHehady_Krw2lBOQIjbi2NMh8jQ_RJBYncXsVmlf_UHFAXTJU1qNG5vlbvBOuBlOJ5Tvu8tVvO_wiFu7nKoafN95J_1JwBBn89qLXfRvEig1Zwkxz2uWmHeNXXl0elgOBK5xiXoclWF7SUsa2D8hVZfjAAU5VoRJsq4HK4Q7m_o-6kCt8Pm9nWlpA46mgCunI56jsoRXfIWOPJRdNbWIk0sjwHwFIKNxC6OegoWhgXRzB7J39dJX2ZNlz6yarSsK5ojZe6AuQ7mArWoQxr2TcDIkWzxoAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین حضور سردار حاج قاسم سلیمانی در مراسم رحلت امام خمینی، خرداد سال ٩٨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/656128" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ارتش اسرائیل از افزایش تلفات خود در نبرد با حزب‌الله خبر داد
سخنگوی ارتش رژیم صهیونیستی:
🔹
مجموع مجروحان ارتش متجاوز صهیونیستی از آغاز تجاوز به جنوب لبنان به ۱۲۴۳ نفر رسیده است. از این تعداد، ۷۲ نظامی در وضعیت وخیم قرار دارند. همچنین حال ۱۴۰ نفر از مجروحان «متوسط» اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/656127" target="_blank">📅 19:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50daff1723.mp4?token=Gz4IXRqCpKOaMg3Ovn6FV9N307PjjCrRPn7kVe3bEQ5O5M1nIhXE8AEF5V5EbFlEACUiW7ZvuzQGZvnSL6b6uvyfUc-OSMg9XIzl5IcErqjq1tsWNm5Nj210sy5NJ4iny_RQYRL6cWBnIkBQIHKer3Bb8T5zMjB5OTip-bERQthw-uumfyHHSG9-_60MlgqQ7FJUAW4SbFNhpH6lr48r6Ou4tgB7WpIJgnGcGLJcfVXzBUIbNybX5FuvxhwQhuu9WGYuwInuM_MUHq_QvJjoKqPyKLOc6KapNXjzvU6eyxMTkHyYr2ncnvcLCID-F0asGTadk60Nn4x4FZV_2-OGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50daff1723.mp4?token=Gz4IXRqCpKOaMg3Ovn6FV9N307PjjCrRPn7kVe3bEQ5O5M1nIhXE8AEF5V5EbFlEACUiW7ZvuzQGZvnSL6b6uvyfUc-OSMg9XIzl5IcErqjq1tsWNm5Nj210sy5NJ4iny_RQYRL6cWBnIkBQIHKer3Bb8T5zMjB5OTip-bERQthw-uumfyHHSG9-_60MlgqQ7FJUAW4SbFNhpH6lr48r6Ou4tgB7WpIJgnGcGLJcfVXzBUIbNybX5FuvxhwQhuu9WGYuwInuM_MUHq_QvJjoKqPyKLOc6KapNXjzvU6eyxMTkHyYr2ncnvcLCID-F0asGTadk60Nn4x4FZV_2-OGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیعت مردم مبعوث شده با حضرت آیت‌الله سید مجتبی خامنه‌ای در میدان آزادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/656126" target="_blank">📅 19:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=Ih_3yR4pOxOMEjxbQ9nfLQiHtTsBpUrlRiuTkeiyh9NQydBW_-u9cnVaiG8DnofqSe0GLWhhHnW0gl07Tn_0sX3EnXn75ET62F1ib9JaOYbxybkI8lI6u_y3miDsCgcP3lMyxX0c-Z_OkwCX5k3kdeXnDN6QnbSOBecc3HGH6SzPweQ2nFKkguyGtNpfnx5iS9Jx7RO1WKsrW9lgMI8c1IOE7k5fUg3vPf8lzAS1WTiBXIaCFT0Dcs8zUohL8NeCnsIF30UbJhz8GnfRnhT06LRMfkK8l9h34L0s2QLR4RKHOo_LgPCAwiMiIPb8bXFoCeqnnMD_wYGqmdCazEqBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=Ih_3yR4pOxOMEjxbQ9nfLQiHtTsBpUrlRiuTkeiyh9NQydBW_-u9cnVaiG8DnofqSe0GLWhhHnW0gl07Tn_0sX3EnXn75ET62F1ib9JaOYbxybkI8lI6u_y3miDsCgcP3lMyxX0c-Z_OkwCX5k3kdeXnDN6QnbSOBecc3HGH6SzPweQ2nFKkguyGtNpfnx5iS9Jx7RO1WKsrW9lgMI8c1IOE7k5fUg3vPf8lzAS1WTiBXIaCFT0Dcs8zUohL8NeCnsIF30UbJhz8GnfRnhT06LRMfkK8l9h34L0s2QLR4RKHOo_LgPCAwiMiIPb8bXFoCeqnnMD_wYGqmdCazEqBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانواده آمریکایی ۷۵۰ دلار ضرر زده است
ریچارد نیل:
🔹
به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینه بیشتری می‌دهند. گویا آن ۱۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود، چراکه برآوردهای جدید نشان می‌دهد جنگ با ایران هم‌اکنون ۷۵۰ دلار دیگر به خانواده‌ها ضرر زده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/656125" target="_blank">📅 19:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cq1wWfYq__VQwCAE3ed3HFUQR97rTXft-bLTEB5foA9o1Iy9srrjB-nXL6qjmr9Al3YG0eY5Dtn9UcMGT2RvXh8H8NsxufJYMS5qILHm1tLKTQvC0E3tZusnUjWO2tPHKQUwDo0qd2nri5A5iij8KO2sXkfffWPo30xuaGkfzL_nsGMpA9kFcVYSCg7AaNCbuVQ9ZS1-jOV64_oEwBj9UYIbMGwsH_CWO1Pu_dTv_Rr4xu2vwegKyRO1N_JM2KEW9YKq2DrxgeC1jUlDVgUJEF_cvWgHMYO_ucQXt4StMpdpwe6dK83qs4Bs5CJxP6xBNnCGMf1gtvAymovJzz1nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEldP3RkdNEoQzlqp1mnH8noRE8RUjRcZFX0a04kmrTIWDZQg6HaLjiaxZZcGhHk0lxwvsbyxcIBJrnarYwxi9NIQi0Hl8AsoreLNcC0FCY_iIRXMCsgi2EdKE5hXLfvFz_QgvPT_WBmosDTIxJ8wjaH35o-ybpJVkg75yMTR-lJd9Q68NwGs-2rF3iL7AVfadMJsQLAK8ZOZytzSnAyfNFuocKdYdu_oZzrvdQI8_03T418HGxIkuZ-OuiREXuUQbmW01TElLtBYA252bsUXfferUIo7xsinTT85ZA7spdM6vaSlQmeYTHzHExy-J0r3Bw2tTm3qmcZTaY8EjsZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHm2oOUBIjQ-mY1Cv6hMsJ-mqYSyQrn8YuVsRuHb1gZsWUzJvRR-PfzdANjpVaMZR3Gs9elnv5VSK_JxHhWEw0jnQk8BQ2zqNacnSpi4svhNT9dAIF-rBblS7bCVWVPJHLydAWLUocNcfotMmr2GnQXG9qmUOEyjPIIqupZwnp_hULhmnSAuJd6kXBUCmPd8QtlV7sJIV6cNDyGNcbimOJorpTzxy2vGldVQIQYGyrkxAbvxaIAbcJYMSA7omcmdGJk56ZqO3TovQB4fBkV8lIt95BhjndE_Jdexa0crLvMIieuJP7i5q6KX-jz83JEtmL4bhFcoQxbzM_RusU3wLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1h77nxUd1nj4EtLt8MSRPmZj3HUBReL-8KV79CmQg2kMBNbLsASPQnWPHzbCToD6FkomZLA7nm7t3PeccO8f0fzv7lfSvhKfoautZwWlDem1YBq9AIG9CQ1wN2YlGN7Ub4jIR2-FSAej24iF7jHNqTAh5nNxVbEspzIGWuO9s3Cm3ontiF2WscVYi77up_Z1QIbVSTl3Z3xcVqg5ksxV7qa-LzKtQu_1lxnfkCMuhcJ3GP-OELW-9gHXcaATAQ2TL7Odg8evPTjtJB87lAPyOEn_W8z-x4TO2YKxZ8-GqhbXWeEe5-BamaYS_e94HJvclI7MQ2mTrJfnayhu1D_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwb9N4zjlOofPewtni2TEc6k2AdqFPhlM5jqqp_p2irIOY2uiNuhaahzArP6_xohzMBtQ3oObIjG4ctF7g7KaZA_kpIm6V9z7ehGY-wN-uLYElLe5ooTMfeA4YvgYLm7237dtG9ol0K7nteVp5e7hc_IOmwQdyCnsDBsYeaERqipHEYVI7PSPg_Np4jQFc_VnzOWOpInq4VjdnQ-EYLjM13zTb8XWC1Zyj1_vOjbdmcCC_8TXD-7ZWmUd0e2qb24EFOePBPshjvZx8kvnpX-zRoDM6hQbw8vYUKzLrBvhw8UTjrHvemQgcur5bFtHrsR90oi3FDqXWHqj4mYvAfKww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
چه افتخاری بالاتر از این
که دل‌مان به عشق تو می‌تپد
و سایه‌ات بر سر زندگی‌مان هست...
#عید_غدیر
💚
#بک_گراند
#پس_زمینه
#پروفایل
#والپیپر
#امام_علی
(ع)
گرافیک های خاص مذهبی را اینجا ببینید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/656120" target="_blank">📅 19:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ABjVw8RetJYhmlqcE6S7_qR_cUY8XKXx84jtOrfQ7WRjhIRqk0VEw7KO70gy0gtuFpuCQIQclPgs5mlPbu6MjkB6bnBH3gTidD6QshDdownrp5TT8__0NUlFC5gM8xZhJIbHwAi2oGlpLfXm1DOoS9banieshZDTOODiArmbJRBzcQXpx1zhrMnujh_N40bAkYBPp1qpZOsVE1gSbzOzYK99DClrNZhcfd8t9fiPrcQrIqVSLcDRIQlgzO1aBrwGNKHYJYsjWDe_zXcs9hvTwp8g_PW46lP31hGtUZnYLNPoVdwcKHKcJFRjrQ0qomptQMxGZYKx5SYeOhOthq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تمامی استادیوم‌های جام جهانی ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/656119" target="_blank">📅 19:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdnVVz9-35ksaeqp2M6iADlJtSpKCe6t3gIXUnu33lUx7uik7BtNhDLs-lBcYt5OdYcEY_FXoG-39aGoYxaJg0ds4T0wB0lVPI9-seyMCXSAzKiWKqZ7pT1uuFYXSuE6VYW85NSlSyhjR10tQj5aFI5OOPh_3JZPapMeItiGE9wkACFoRqh9-FHzSW0vblYxQco6nkfmhY9X61dRFWxkxTc8Dq37Mf5hsyH77wVpWipXe3ofL1dbXYzrvQRnwm6e6VO1W7DQeX4ZhOhYv3Z3LjLEc8gcuxeKSg0-hpQptZo8DG6WDB8kYA4CAmZhmjcbt-kodxdf6Lwxe4eSktj9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردرگمی عجیب در اعلام روز کنکور و امتحان نهایی/ کنکور رسما بحران شد!
🔹
مساله کنکور در شرایط سیاسی – اقتصادی کنونی سبب ناراحتی و یاس بسیاری از داوطلبان و والدین آنها شده است. نگرانی از جنگ و تداوم آن همزمان شده با تعویق پیاپی کنکور و مشخص نبودن زمان برگزاری آن. این مساله سبب شده بسیاری از داوطلبان از بلاتکلیفی خود ناراحت شده و نگران آینده شوند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3219943</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/656118" target="_blank">📅 19:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
توضیحات دختر شهید لبنانی در خصوص کلیپ جنجالی پخش شده از او: وقتی گفتم مردم لبنان منتظر کمک ایران هستند، ایرانیان خارج از کشور به من فحاشی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/656117" target="_blank">📅 19:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3502ccbb01.mp4?token=UPRir0z1RGOr6tTP5TdvUQEc1kpBsj8iCyMrKnQR4iD29e5RrgK2faP7o2x2wQJNFGnBxEP7x6RUDPPWQl-MhXbIPaZTLo6g3JuO6hOxD27rzU6bFYOVmCxG4DUZABRHX-Yft4-siZlnHrGX3GIhFVYgSNiRdyrdgppgN2CqXT200tJm4bG4Z8vHdXnBRDwyzJQpvj5DOXDQ6wOFKD_jwzzIB6cYytOsFm8wi9oDROph3coOBnsxZvlC_BS8-Qny65Nyz2rgyWkT3ogfwo7fT3oMUbLdzLkpIk0rtgSRmGA1Vit7pIFmxfZyxvY-wfo2ktD9ECnk0BcVKIyASm_xdrLw7V95f3W-Y4FEyPdXgVAQkufig36DELArJJ3Gh0pTo6ONZhvvfw2KEKTjt9TejTK3AuVUB4-qkHK10uFH7VZsMN7x6GCLbv83_DD2qQGBwNWdeSm1lseWP13I1Lz7b6kBQ4lkOMBi-aiWCJXjW4tU8NyCEwrk_Hyb_ZRbV6iR_U2qJFQMMN1NLbCO4MkoglYkBuU2VR3f55dPIa5V70Uc76O5RPF5yAbVru_KmfQKLIq23FTrjlVn2AjfpS9jb026CZl5qiE0WPFvbYjBNHLYnPYgjc5rNscKADYtD9c0wgxMWFINQPbZ-GVsNpIE15bb3C7pBdqtAgmOVMyihJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3502ccbb01.mp4?token=UPRir0z1RGOr6tTP5TdvUQEc1kpBsj8iCyMrKnQR4iD29e5RrgK2faP7o2x2wQJNFGnBxEP7x6RUDPPWQl-MhXbIPaZTLo6g3JuO6hOxD27rzU6bFYOVmCxG4DUZABRHX-Yft4-siZlnHrGX3GIhFVYgSNiRdyrdgppgN2CqXT200tJm4bG4Z8vHdXnBRDwyzJQpvj5DOXDQ6wOFKD_jwzzIB6cYytOsFm8wi9oDROph3coOBnsxZvlC_BS8-Qny65Nyz2rgyWkT3ogfwo7fT3oMUbLdzLkpIk0rtgSRmGA1Vit7pIFmxfZyxvY-wfo2ktD9ECnk0BcVKIyASm_xdrLw7V95f3W-Y4FEyPdXgVAQkufig36DELArJJ3Gh0pTo6ONZhvvfw2KEKTjt9TejTK3AuVUB4-qkHK10uFH7VZsMN7x6GCLbv83_DD2qQGBwNWdeSm1lseWP13I1Lz7b6kBQ4lkOMBi-aiWCJXjW4tU8NyCEwrk_Hyb_ZRbV6iR_U2qJFQMMN1NLbCO4MkoglYkBuU2VR3f55dPIa5V70Uc76O5RPF5yAbVru_KmfQKLIq23FTrjlVn2AjfpS9jb026CZl5qiE0WPFvbYjBNHLYnPYgjc5rNscKADYtD9c0wgxMWFINQPbZ-GVsNpIE15bb3C7pBdqtAgmOVMyihJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزیک رپ دیدنی برای حضرت علی علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/656116" target="_blank">📅 19:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkp10qL59Sed2UeLlh2ayO0ONsYXFXKYEkYR-LVwr9kORavEMf54cQPnym4LzHACvPBaqOlVkLnB02Plv1x29BmmH24YnPNiTgVNNbyDY7SgkB1aVA7M0OpCur6InuxLIgI75RJoXwYI5rZ4BlXGtrCpBnTievWAzJnJ4C1pbZQ10diZLeY3BIjw7sWuv--w-hzYieAsSZzi7T3Ijkm0-UMin3yBm9oJVjKRzfixDtXPCtq0dI1UIE_pat4JH1UwC_SaoIxI9rAiw54p4SKOu6VK3mSGqBJiEINZvxMqHYXAVQpJrrl45MVmEYCebDxBWY7Q6RubO_4GHfHp-gWHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
فرصت ویژه خرید از چرم مَنطِ
تا %70 تخفیف
➕
%10 بیشتر
و هدیه 1,000,000 تومانی اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
📍
سیتی سنتر، طبقه همکف</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/656115" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp_PA2kD_4AvZYu13b9MQkeeJMgDRs9XSz1UoijI6U43QGoPnVq3HEADiJmYX9ktuxXiyFyuY3ghU0iCdHZp8IxIt5QRNwkWNgkYrJjV6OvQugfmj-z5YpwGQ0lxiLkZOKJB2VCcfjjRfo_yXXIb540jPDqE10WsUwVwyVJXjpV4flrKCOjefSWX57I5IGk-qwOX0ANZMraaQpdd2E4rWXr5TABOYk-egeeiVlgqRvzveB88JLvh9DNL34SVZxR74Tbc1r_-sWnHxySYQvAo6-8wxw5TRUJXiZvI3US94ylvlHFtqFFAIGTT1cwTsmlZYMLU5FYmlFCjY8Za89sU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ کشور برتر تولیدکننده نفت در سال ۲۰۲۶؛ ایران و آمریکا در رده چندم هستند؟
🔹
بر اساس آمار سال ۲۰۲۶، آمریکا با تولید روزانه ۱۳.۲۵ میلیون بشکه نفت، بزرگترین تولیدکننده نفت جهان است. این رقم بیشتر از مجموع تولید عربستان (۱۰.۱۱) و روسیه (۱۰.۰۳ میلیون بشکه) می‌باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/656114" target="_blank">📅 18:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrYvjxpHB5d8IKhDwxaa7V2SZMYrSQp_HX79A9rVuJjJY2dgxJer9N9TEj_vV4V4XcIfRNfZuyr3PiauY0dn_MTuzLmUjEq9Tzo9AnnCuNCG4FuO62XSP9JaRf1WrTDk4rnclztaTn6nAsdEXVoBbPaT1S4g4YxsQohFO96c5CY6n7rsf8RGmxASZcRLT1sfaZl3SG65wiurnIzj9klPShegt8XHoMEeQ8NMkjp-mmz1sBQOkQyqYGttjK0iTxbeZ281GMNblGNYXy8oJGCepW27GsM8wD2aRCpWsvMte5cZ5Htm9B2HVZcA6gILsPa0isfcZKws5eN2ATozO-hFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دعای مردم برای سلامتی فرمانده هوافضا سپاه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/656113" target="_blank">📅 18:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw2IouDTYPlu2wI8vFJzK-s5YGNmQl3M6uQ41ne0QLSydZxNpdLegkoHLhH1eOumCUCcziMTWItlLCexLrHGUe9Qlvl0jTH4on6Ii-FUOYAy3lmGvsUS7WhcP6h_P7_ZHCLFxVmzkPciBNI8Dq65PkIPQ4ZKNetw1U8Vnv6AkPSgAC0KG5cRmowy-5CxzOWNl-chF6bFNJe-1tqCmh-BcQ8zbLTsfXu_fwY79v4GSGY13jsoD6qLF34rwdRUKDyoFFn98_sRjSVPfTiUs77LwTaq2n3E3unH_9STnzbkzip-Wgqq0q4wl_V1IkeRhUzaR8j-gcCTKM1wlW-KulIRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/656112" target="_blank">📅 18:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0BNomBIHUVHfOc1ggHKdG7PrNt-upHTsDmilKm_Jc9d9Iv28eCYtIxSb8cfY0cAqaMFNji5tR9uc3IVl0RDw9uZapYy83t4oB9RdXubjwiQnryjia_mMcndFBjgNo_MLe51MH4B8IeZUK6vOkWo272cPnFAxFULyjUzEjX1LvY9Yeoent0vgm65J8jjL8P6pbWeZ_my6yA46LuNIlkft170SlwytcIbeZQXQryy82QrtAt9isEpmlUHJ-otrK9kLuJF997u-D0rGc2-f4lI0UAGgVgMFoWWAAxvoOvieiWZbDUlo8T6LpGh9M62tvjVFBTgz6pQVpxmXAvn9MKH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده اظهارنظر ترامپ درباره رهبر انقلاب/ نقشه جدید رئیس‌جمهور آمریکا چیست؟
🔹
ترامپ تلاش دارد مسیر خود را تغییر داده و به نحوی دیگر با ایران برخورد کند. شیفت سیاسی ترامپ را می‌توان شیفت "چماق به هویج" خواند. او تلاش دارد از طریق تغییر لحن، سیاست مقاومتی ایران را بشکند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3220287</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/656111" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYvq12ugkgkVfcB7gV1W7lKn5b7eHJvpALW3_0itertwPlv1M-h9avXC6SBA1Amo5olSs7PberuZ6OOykccrkuyYxP5iN9mN5ddAltg69RsaBNmCybTLUv1yZBHB7tfDZKFhA3CNZCcrOKk2ITeuXFu3FPdN7SfW-4a6MPAhamb1tQRIytHJVGUuXnCM8bZJD5As6cgVp6XblB-zgBO5kuEwYiiZKNcupJVJYpFtKuMBmaSrwfIAc2jf5tQSKB1FHBkxf5suF8BOWgIj3emnA4UCzKCVMNfMsg1Fj7gByQ6En_MKBB89WP5po2UsPkmqjejuEPHHa_BNfcO1nkCjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت سلامت میرحسین رضایت بخش نیست
دختران میرحسین موسوی از وضعیت جسمی نامساعد پدرشان خبر داده‌ و گفتند:
🔹
پدرشان به دلیل مشکل شدید قلبی در بیمارستان قلب بستری شده و اوضاع جسمی‌اش وخیم است.
🔹
پس از حمله آمریکا به مجموعه پردیس حکومتی پاستور، منزل میرحسین موسوی و زهرا رهنور دچار آسیب شد و به ناچار به مکان دیگری منتقل شدند.
🔹
پیش از این خانم رهنورد به فرزندانش گفته بود: میرحسین حال مساعدی ندارد و هنگام راه رفتن باید مدام کنار موسوی حضور داشته باشم «تا سرگیجه و نوسانات و افت شدید فشارخون موجب حادثه و مشکل جدیدی نشود.»
🔹
میرحسین موسوی (۸۴ساله) و همسرش زهرا رهنورد از بهمن ماه ۱۳۸۹ در حصر خانگی به سر می‌برند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/656110" target="_blank">📅 18:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f00fcfa3.mp4?token=D06VdG_cMECGGGZciLlcI3HSAhl_lkcXe5R_z7UP1-u2d2avKowd-GA3C0CB005aNvqUB0QpJnzQ9DC0Q8CgrhM2wCTkofQf5nCRS03m83SYdWvhV8tKrk1S5m4Bgd4mG6p6mZuGS1wYe9vBz20tvwQXfCvdL0zvHPoHoWNYrrYPZaEx0yAlOB16RX0DgJyFPaY0BsU30fc4Obn_b9-5yhdg7BfawRUBb4qstqOl50Z3HvuZ337bYLQUHWK20K5QEZojoCSFdyTb_gj5d4fQ3lnk1wwVk3xnWCGaLOHfuQzQnNqzgfHbVEpueFTPB3RSo9Edem6SCFCOfcCweJBN2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f00fcfa3.mp4?token=D06VdG_cMECGGGZciLlcI3HSAhl_lkcXe5R_z7UP1-u2d2avKowd-GA3C0CB005aNvqUB0QpJnzQ9DC0Q8CgrhM2wCTkofQf5nCRS03m83SYdWvhV8tKrk1S5m4Bgd4mG6p6mZuGS1wYe9vBz20tvwQXfCvdL0zvHPoHoWNYrrYPZaEx0yAlOB16RX0DgJyFPaY0BsU30fc4Obn_b9-5yhdg7BfawRUBb4qstqOl50Z3HvuZ337bYLQUHWK20K5QEZojoCSFdyTb_gj5d4fQ3lnk1wwVk3xnWCGaLOHfuQzQnNqzgfHbVEpueFTPB3RSo9Edem6SCFCOfcCweJBN2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
پک استوری ویژه عید غدیر
💚
✨
غدیر روزی است که دین خدا به ولایت علی (ع) کمال می‌یابد...
#عید_غدیر
#استوری
#امام_علی
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/656104" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj343Yz7CXzcHLj_hOlK6LUmlNqFPf_RR5_8JalSniwmndkP_QzLfSe2-5OerAt3FbNbB2GmWf9kr4gY9YyQwiIvZLPJzn4xDuCkZu-_TNh_y64QIoAx0N7PMvlHQ_r5MPK4ETxzgQ263nqk4anSy_xkesWWCL5UMZCZdpJngiqTFPJIScrLjdBv2hIK12IA_hNSZosonl2kB7ucFakpE0bdPA_WZ6hNDcMNPBwXFiApbKwluN3-EpeyIiNgQMaKJJI-v2E5KGWW3i9vRuxY2Z5MPkFTF21riFCPEb1xscuIzAWgSue2Aq0cYqPiXWqcNsC6zk5C4yA1n_EGCd0JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امام حسن (ع)؛ اولین سفره‌دار غدیر
🔹
اهمیت اطعام در غدیر چنان بالاست که در روایات ثواب آن را به‌اندازه اطعام تمام پیامبران و صدیقین دانسته‌اند. شاید جالب باشد بدانیم که نخستین کسی که در روز غدیر سفره‌ای به وسعت یک شهر پهن کرد، امام حسن (ع) بود. #جرعه‌ای_از_خم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/656102" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656100">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzVBnc9Zv2cVVaiPsfaU1l6gu3-8nIY1bRYBe0Kj7uKliGbuFRyFEmE8tR4RVc-aUbHNOm69p907dLV5VAuZ97XpzleT3ogNJAiOiRWqzy-NVQUXNqCT_fwBiDhoCmWppqQOUj2rdGFj892pIS0e0ePobVXogq3FCe90YGU0ukzuh_4TV8ha8pv1-vqfm2O3MJX_LEwy8vrjyOT0KBbbud_2BwMLv2_G4Udg54A8F_hA6fqovdmp4oeQxLIATzSTyUiO_xbEdbhFT4LQ8LS7yP2XqCyiVSEEpag2cMSniGQ-4hLMWSKxYjHxIHishIqvzacd8I3iCRlIkui2Bsj4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نور
📍
۳۵۰ متر زمین
۳۵۰ متر بنا
تعداد خواب ۴
نما مدرن شخصی ساز
دسترسی عالی
سند تکبرگ و مجوز ساخت
دسترسی عالی تا جنگل و دریا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/656100" target="_blank">📅 18:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9300b4e3eb.mp4?token=AgaNS3pwLf33jl1C5cjFaH4wxMdctVAc35gGGtf0gKPzNrm1egG04Q-TkfRI0E88tfsNlHKsuForNUVXx4LeuwQsVbUotJOnVuVJnuN2WoiQTTrJMZ9ywkaXWwJ8zizJatO6qmy9lA0pcW5uHAhT4vJHsnraEnMhhkJhspXvY6UXCjA6TCjd2lNkPGo28VyhhuG4p1Pi3vdoKxjd-Y66svnfBBEVo2d2gdaUjlmElFDIbZO8M4nFxqUehsOUbqFtdkT8GZXnVpVFcIebQqKMnn9wa7IiiGP906JQzO_jT6WjBjYlWIqDisMhDkUi3Xf-aCnFkBay6IoplN_dT-jquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9300b4e3eb.mp4?token=AgaNS3pwLf33jl1C5cjFaH4wxMdctVAc35gGGtf0gKPzNrm1egG04Q-TkfRI0E88tfsNlHKsuForNUVXx4LeuwQsVbUotJOnVuVJnuN2WoiQTTrJMZ9ywkaXWwJ8zizJatO6qmy9lA0pcW5uHAhT4vJHsnraEnMhhkJhspXvY6UXCjA6TCjd2lNkPGo28VyhhuG4p1Pi3vdoKxjd-Y66svnfBBEVo2d2gdaUjlmElFDIbZO8M4nFxqUehsOUbqFtdkT8GZXnVpVFcIebQqKMnn9wa7IiiGP906JQzO_jT6WjBjYlWIqDisMhDkUi3Xf-aCnFkBay6IoplN_dT-jquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروس و داماد موتوری در مهمانی غدیر تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656099" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656098">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بازی و تفریح کودکان در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/656098" target="_blank">📅 18:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656097">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz1bSPS7wVtfSMZefUNDsSwW7ZZNXxdHuEgNNFaFk8z-5AQ6ViSwqPGG3H4VZDkhnwppOOkb-H3tXPUSl8OG8PJYMRwCxq7Erzaj4CP095WYM4YGzJ-FiXXgk5a-6TaZyXf7cerR9F8FuyL3exYx2VDU5GCmEBB0E4xRrLv2KO8IvfKZWtIUndTaNlEfIQuUKqpSDIywJFcUbEssQLnvl4NPqUuNikeGXxMWxfGOrFEKoDJQhvdUDtXZNiIOkAJi5RsSsS47lLARW_VLRLSdJW_nrOhptVhSugMQCU4TPGj-bivDC_JxCur-z73FpfuSmyWQmGbwkiYuG99WudyhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال عجیب مردم از مهمونی کیلومتری غدیر
🔹
تصویر شبکه خبر از حضور میلیونی مردم در مهمونی های کیلومتری غدیر در سرتاسر کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/656097" target="_blank">📅 18:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656094">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgK18iXpqSkWA604nPTmDvYao4NnNRsIXUlDfwFo2W5dFDqSuBOSYmWhrQkhtRgtoxmTldmK6mPxiw9NOuwmJKnBEYO8_NY82aEZBWdGdkIlI6zF3JPRQHpfAdRr3v12rtl7GaX0VM73Cm8OZT2TuEI5hRPPc6OIG1_laMURgtPJlaj9Fhml5mV_vJhXsxf4RTF5UGeBT8xHu9Puaj9AYjPJN4_3JpV-6z2Ae8cypBTMSPT5MZFCio7V5-NSJGQGTH8WfI1iYwY7udptAlK-zBIJnGgl3zOb66bf5I9M7W0mUD2PS7cj_NbVfdB09xp3PEy8BKPC3XdHqLmTg0XRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخبار مرتبط با برداشت ۴۵ همت از حساب سازمان تامین اجتماعی صحت ندارد
🔹
روابط عمومی سازمان تامین اجتماعی در خصوص اخبار منتشر شده مبنی بر برداشت ۴۵ هزار میلیارد تومان توسط بانک مرکزی از حساب تامین اجتماعی، را صحیح ندانست و تکذیب کرد.
سازمان تأمین اجتماعی در واکنش به این خبر اعلام کرد این منابع در قالب خط اعتباری بانک مرکزی و با عاملیت بانک رفاه کارگران برای جبران کسری‌های ناشی از شرایط جنگی و کاهش وصول حق بیمه تأمین شده است.
🔹
در جریان جنگ ۱۲ روزه، با کسری ۳۰ همتی برای پرداخت حقوق بازنشستگان مواجه شد که با تخصیص خط اعتباری بانک مرکزی جبران شد و مجموع استفاده از این ظرفیت به ۴۵ همت رسید.
🔹
همچنین در جنگ رمضان، منابع سازمان برای پرداخت حدود ۴۳ همت عیدی بازنشستگان کافی نبود. در پی توافق وزیر تعاون، کار و رفاه اجتماعی و مدیرعامل تأمین اجتماعی با رئیس کل بانک مرکزی، ۳۰ همت خط اعتباری جدید اختصاص یافت و عیدی بیش از ۵ میلیون بازنشسته، ازکارافتاده و بازمانده پرداخت شد.
🔹
تأمین اجتماعی تأکید کرد همکاری بانک مرکزی و بانک رفاه در تأمین منابع مورد نیاز بازنشستگان و ارائه خدمات به آنان ادامه داشته است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/656094" target="_blank">📅 18:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656093">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">khotbeghadirpdf.pdf</div>
  <div class="tg-doc-extra">665.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/656093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
متن عربی و ترجمۀ فارسیِ خطبۀ غدیر
▫️
در خطبه پیامبر اکرم صلی الله علیه وآله است که درمحل معروف غدیر خم و دراجتماع بیش ازیک صدو بیست هزار نفر ایراد شده است ، بخشی از اسرار ولايت بيان شده است
#امام_علی
( ع)
#عید_غدیر
💚
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656093" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656092">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed301c9b.mp4?token=nYvaCLfrN5MtlVM8mqjuJobNhTWOoCQbaLGh8UV15GdTc5sfS8tJF4WXDXbtA9dFIRwkvidBj9JXWQ46t7pc13ErM5jlvHE5d9ciQBzhs0hNUeDTxVNN6u90-Wy1eIuhhZIhVdqioBx86nXta2aSgidY4jLYycHeXY3gNwSc7QWoOUgV_3qfN_JwwXs8cGiPalZ9nXUfaQKAnFvEv9TSpHVAJyPhIfSFrvUDx54fWnLx6rQWrMpH0-8i1T3B0VBMWNwj4OI0metNxSuK17gxBRbcR7UJJ-RRmR9C0gMZEyKYFXs0YSnldngxqdYeOExBLc4j5EyI5C4IrX7KzO1FBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed301c9b.mp4?token=nYvaCLfrN5MtlVM8mqjuJobNhTWOoCQbaLGh8UV15GdTc5sfS8tJF4WXDXbtA9dFIRwkvidBj9JXWQ46t7pc13ErM5jlvHE5d9ciQBzhs0hNUeDTxVNN6u90-Wy1eIuhhZIhVdqioBx86nXta2aSgidY4jLYycHeXY3gNwSc7QWoOUgV_3qfN_JwwXs8cGiPalZ9nXUfaQKAnFvEv9TSpHVAJyPhIfSFrvUDx54fWnLx6rQWrMpH0-8i1T3B0VBMWNwj4OI0metNxSuK17gxBRbcR7UJJ-RRmR9C0gMZEyKYFXs0YSnldngxqdYeOExBLc4j5EyI5C4IrX7KzO1FBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش نافرجام جوان برای نجات توله‌سگ گرفتار در سیلاب؛ ویدیویی که کاربران را متاثر کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/656092" target="_blank">📅 17:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656091">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deac8104a4.mp4?token=KDXsqhoyCKT6Y5wLt3Tj3kjfywoHMOGX7DT-YXCV8zlJ08N-UpG0vFgztgvr93XtX5M1IWyBzLY7at39dUcNRmBovSw7oGFc54iYZX90hBgj_3WLgdvYgEwf9zUVWXAOfBbO_mHE7fN8OPKWvcTtfaqtWOl79D809wqEDUigyKp-abrYUSlt1LjOtVc8FYxkLe6vJ6IgyWTEgf7CgMl7rflHa73U4Pme9kroWqxMotstdq00V77akzVMZN186zDUHLPbRObqYNHkxhCuA7LexMh_SW_ifQf77wpwVLZo0_PVlorjpdA4xsHAM-yYgr5O8pBYKosLa7DVTUU2rgZZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deac8104a4.mp4?token=KDXsqhoyCKT6Y5wLt3Tj3kjfywoHMOGX7DT-YXCV8zlJ08N-UpG0vFgztgvr93XtX5M1IWyBzLY7at39dUcNRmBovSw7oGFc54iYZX90hBgj_3WLgdvYgEwf9zUVWXAOfBbO_mHE7fN8OPKWvcTtfaqtWOl79D809wqEDUigyKp-abrYUSlt1LjOtVc8FYxkLe6vJ6IgyWTEgf7CgMl7rflHa73U4Pme9kroWqxMotstdq00V77akzVMZN186zDUHLPbRObqYNHkxhCuA7LexMh_SW_ifQf77wpwVLZo0_PVlorjpdA4xsHAM-yYgr5O8pBYKosLa7DVTUU2rgZZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران بی سابقه چشمه کوهرنگ/سرچشمه زاینده رود
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/656091" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656090">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8c2303b7.mp4?token=TLyqeKE-XL9vW80vcyyAwDVRJlyOgYgW7jyUZ1tg45ElQoQ96c-JQckaHqQMTiQo2JEVLx7wc5izg8qumhcRGQeK8NP4D8j7mU-ULOkprX9FvBNlAP3lGkCnU7JMr5NOT0nhFSZ4F9r03KuwIkqipFUZUMiOAZzQuDXy1bTC60IM9_uuy2dO5aQFLpjx5joBc0u17oae3llN6FMn9wQWgoZKc549a7JC_mN2jRQ_Ifk4-6mJxFDK6oQ1BERQAKI8zPaa_WWlS04hU0Haf5p6jZLu8NK595HyfyOeRa1JsMLb6xxk-y8nry6JT1FRjByEIyMFNMpLKA1bYJaBiqgUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8c2303b7.mp4?token=TLyqeKE-XL9vW80vcyyAwDVRJlyOgYgW7jyUZ1tg45ElQoQ96c-JQckaHqQMTiQo2JEVLx7wc5izg8qumhcRGQeK8NP4D8j7mU-ULOkprX9FvBNlAP3lGkCnU7JMr5NOT0nhFSZ4F9r03KuwIkqipFUZUMiOAZzQuDXy1bTC60IM9_uuy2dO5aQFLpjx5joBc0u17oae3llN6FMn9wQWgoZKc549a7JC_mN2jRQ_Ifk4-6mJxFDK6oQ1BERQAKI8zPaa_WWlS04hU0Haf5p6jZLu8NK595HyfyOeRa1JsMLb6xxk-y8nry6JT1FRjByEIyMFNMpLKA1bYJaBiqgUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنش در آلبانی پس از خبر ساخت جزیره منتسب به دختر ترامپ
🔹
پس از انتشار خبر ساخت یک جزیره در آلبانی توسط دختر ترامپ، فضای این کشور متشنج شده و اعتراضاتی شکل گرفته است.
🔹
معترضان شعارهایی علیه «فروش کشور به اسرائیل» سر داده‌اند.
🔹
برخی تحلیل‌ها نیز از افزایش حساسیت افکار عمومی اروپا نسبت به داماد ترامپ خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/656090" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سپاه: هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد
شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/656089" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در چه صورتی خطر ندارد؟
کامران ندری، کارشناس مسائل اقتصادی در
#گفتگو
با خبرفوری:
🔹
باید دید مبلغی را که بخواهند به کالابرگ اضافه کنند، از کجا تامین می‌کنند. اگر از بانک مرکزی یا شبکه بانکی بگیرند خیلی فرقی نمی‌کند.
🔹
اگر از طریق خلق یا چاپ پول این مبالغ مربوط به کالابرگ را دولت تامین کند، آثار و تبعات تورمی دارد که فوری نیست و در اقتصاد ما نزدیک به یک‌سال طول می‌کشد تا تورم ناشی از خلق پول اتفاق بیوفتد. اگر از محل درآمد مالیاتی، ارزی یا فروش اوراق این وجوه تامین شود، آثار تورمی ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/656087" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJnZDd3IKDkOH4uduM-C9CbR4kMiAhIhJXBs_zTHb-xEJ9BwYdl6n5qzVa0oB84dSGcf1Fp70OfwoUs-3zIdIEEkMPtPGeAVrisEL-Hu-1MaK5f9Fz5VbLc9hStbYEj2NTq5WBURtqPuNUNEuE8XviC7iwdV_F_8hyfGz7KC2rZIwIU1s5p4n6Et-ARfR2sGZGASypmtrzPAztvsBwH8uZW7DpK5CzWiHWge50aG5XuZGhSpQ0GW5q_RqVm7Q_fvkzdqdn6rWa4P0aHR8JLG6COH6wc_GpGCPgCRUGBHLg37b2ph5bVAf7vhzhUUuyMy5iMvUwi7h19BYJs-LXtp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نقشه‌ای از جهانِ غدیر؛ از نجف تا پنج قاره، یک پیام و میلیون‌ها دل #جهان_بر_مدار_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/656086" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV_yUNbUKsIn6dwLg9UBLhtmR6O1jDuA1Xa0tYK8ci1pI1trl1IncmwKln_YPM4SCS-iSAzE7qF_TAqQI_x0-JRS_zSUWnpJDmS38x5iUSKtMnhcfszDkf3njZfrAJPVlYVpvaZ9tTPiujpi6lIW8VCKgC7gEltkKAWHS6iODd8A_qwst8kgHhPY06qemYliYpvxNv-Ex92Sk1B2NOb_T1ClpGyJ6jDPARwVXCy2Qe8zcXzkbV8QZsQnzZ0uTuDqLrQHthTr9ZS5Ujy5hU-GhSOn2n8trZyu815cH9KNNK2JCLFcisIlrKsuKxqblkJsKg5IylYMPfOgAaGqgZ0wyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکره استقلال با اسکوچیچ/ چند مربی دیگر در فهرست آبی‌ها
🔹
باشگاه استقلال برای فصل آینده به دنبال تعیین سرمربی است. در صورت «فریز» شدن لیگ، قرارداد سهراب بختیاری‌زاده به پایان می‌رسد و آبی‌ها سراغ گزینه‌های داخلی و خارجی می‌روند. در بین گزینه‌ها نام اسکوچیچ هم مطرح است؛ مربی‌ای که قبلاً هم مورد بررسی استقلال بوده اما توافقی حاصل نشده بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656085" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران بنزین در عراق
🔹
منابع خبری از وجود صف‌های گسترده و طویل در پمپ بنزین‌های چندین استان عراق از جمله صلاح الدین و بغداد گزارش می‌دهند.
🔹
مسئولان عراقی اعلام کردند که این بحران موقتی است و به زودی مشکل کمبود بنزین رفع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/656084" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656082">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
زمان صدور احکام جدید حقوق بازنشستگان اعلام شد
‌
رئیس کانون عالی بازنشستگان کشور:
🔹
احکام جدید حقوق بازنشستگان تأمین اجتماعی برای سال ۱۴۰۵ حداکثر تا ابتدای هفته آینده قابل دریافت است. مرحله سوم طرح متناسب‌سازی با هدف تحقق ۹۰ درصد همسان‌سازی حقوق‌ها، همزمان با تعیین حقوق سال جدید اجرا می‌شود. این احکام برای بیش از ۵ میلیون و ۲۰۰ هزار نفر صادر می‌شود.. / فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656082" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656081">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sejjeel</div>
  <div class="tg-doc-extra">Meshki X RaaSaa X Mofleh</div>
</div>
<a href="https://t.me/akhbarefori/656081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سجیل
موضوع ایران باشه همه قشرها متحدن
تو رو چه به شیرهای ایرانی آخه سگ زرد
#آهنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656081" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656080">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت شدید تحلیلگر اسرائیل‌نشنال از ناکامی آمریکا در براندازی حکومت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656080" target="_blank">📅 16:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656079">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6hA98zQIfuV8cx6zH5wkcxMtMIK5IWx9Ahi3gFIPE6G47subTRMKxHg9ijOCyZ0VKeD_C1HUxBf4zhSYFZFWGU0Xcdhh7L-p9ZQ4BtWLnmzZpL5rL9WVGpUCMCR0EmPEQFwwHx9-7tlBUnSct9-REkzYQvpf-JgtVwT1-WYoQRw167cd_4OIYqIwhn6SvXrMGBd4Y_KEhfCoXI8XZUKunmKBpV24q6gKgUs32wm-OGcEZn-pd1Ne1OuESYQ4SpVo4fBY039KgJ37Z0HVGRiXD9c24hO_5alBJhxpY9qraC7H2k-VDHJ1Gg96WcEvPufHQR-Cqj9UZg1ug8-aoR1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/656079" target="_blank">📅 16:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVj7ncznE-6VSV0DlXCnevr2vQv4PLb427-AsOOomoHp9dI1Ol4GmuovVDIz-dpta8nuN4s64kwf6F7uXo7pUMdQ19v5hmFI2r45_HODUYOp9eN-RF0IQkZ4YT3t0c3nL-Eq0_s_llutzq2-kfdgm1DeuWm9Deze2wVFjGERhxYvpPa1QkVIMoX1vGX3EPWosLKb5JjOUX0pBkFEYM3z5HJgPo2sygU-WSuhqpa1s299BXjCENvlbAqqccDx7Coog1eujdXwA96KhWgcig-cuR0ZEsc31Vg0jQFKfi3-hHrMLEvQX_udt8Zhc4ZLB6LkkhIZZzqy8qtvFbuX91jLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: امروز  از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخرسی و چمن)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/656077" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نعیم قاسم: چرا ایران از غنی‌سازی صلح‌آمیز اورانیوم منع می‌شود؟  دشمنان در شکستن اراده ملت ایران ناکام ماندند  دبیرکل حزب الله:
🔹
قدرت‌های جهانی و منطقه‌ای با تحمیل هشت سال جنگ و محاصره اقتصادی تلاش کردند نظام جمهوری اسلامی را ساقط کنند، اما این نظام با ایستادگی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/656076" target="_blank">📅 16:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgFsJnBvZGsOeNweIveL5sFO1T5dJ0btmYUek3MtiIaacFK-JCRaVKNRRLbreAlktoq2qeq1OkVWpfqdJzqJ4yuYO3N9gt2-WfwcQS0yUmqrWQusul4PfYn-LaAoFOAGvGfAYJ5-kB3igaoAukhqD6A9zC5q0fhZOWJ6QvWB_z0A_tT_LuMG6guzYFCM2nEJdqkKkfmQpyBJHm71rnCZjChpnjmmOIFUQ8IGVF2swwpkBmWcB50yeoNRa3egmJLQdgrrh9gkGOvzaGDzA0yYNUyb5S6rTKjYZqPpnAqGFKjv20t8EbEQRg1HKiXWiLkvWK8YBh1C9Imk1C1vXJ8mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد
‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656075" target="_blank">📅 16:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-xi0KlR23bIRDDWKcLo3FX6bJYbOdVvogN7mYkzxBIQlXxODsiR5ltvYrF9j5eIIe92BWnBFalG6RObHtrYkkwII4jkxKaR8USj_B54esm_1vZWUQ3IDSjR4Rl1lG4VLS8Vf6UHJrzk9YUOSV-IKaRMjHlbwik514bpCIObu59hIzCXgq0MnKa7CfjjrI_U-V79oquuA9gcuWpz3m_9r7GwP7Yv-64_SFEFVKnZ9PzRKKIyjmSfJdXw2HTQmGntfqzyvfv-VpBueW2clkeN5PtrYIA6HD_4DqSHala502PNWK8LK9HIrWbkucIEHddiT5B-7N5CFDK52r2lTo3HVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ
🔹
سرپرست و دوست شما فقط خدا و رسول اوست و مؤمنانی که همواره نماز را برپا می دارند و در حالی که در رکوعند زکات می دهند (آیه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656074" target="_blank">📅 15:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656073">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-T4PIlmIYOx0lsg1VTRLAK-A5PVIocXAqe678Cdjjy2sgdfud0fiTGXyWzaCya7QMj8ieaWtPGt_r0aIdGag53q9EhfR8FtLSqkJb5meaOxsHOYnaeqwTrQ2nDX5nTz-7lgi2sI3yQH291FBlYNctPq9xAitrqkeO5mDR2RRmghl3Ahb7AJfsaVfBpN-e0AVYDyk-z-MjwaElEwSMv5pmJGXAtBsp6uoT3gcPE9BPFLqUt7klCcm2siuZOGKQFKVQU2ITAZVcBBkP2OqDAiUijpQc0lMIE1EFDVXtrzodxa3-DeEoxgoarxd_gLytJ-OQ87fPo72IQvInQCbaboKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رقابت نزدیک ایران و مصر؛ پیش‌بینی اوپتا از گروه ایران
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/656073" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656072">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o825FKf2yug5BHV7EyfJbsFO8xGVxeFVgEovLK3W4DkxYE0qAlFcin7YbMrH3A21O79KH0D3MGYUnazOYE73W-_Ng_dZjbksB9b4fhFAFRMtV-p8a7-p8pFxoR_2F_DDDQUDosbWjmpH7f2tRVOd6EEZgHrCCoXzb90vX27C1_JaE6wB0i0zpGFEO4QCjp_f8MpQoodsC4e4IaJXvcyiQlIbfdGKV1Tv2O5l_o6vdxyxXxPLTisj5b6LvgrQZb66RtilA8_C5FqZby5sHewxdK_Uie2IaGy7_3o8OxKlcSamWT_BT21b7ytdBwApDAeajxa87AsguAOZiRvnXGCT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعیم قاسم: چرا ایران از غنی‌سازی صلح‌آمیز اورانیوم منع می‌شود؟
دشمنان در شکستن اراده ملت ایران ناکام ماندند
دبیرکل حزب الله:
🔹
قدرت‌های جهانی و منطقه‌ای با تحمیل هشت سال جنگ و محاصره اقتصادی تلاش کردند نظام جمهوری اسلامی را ساقط کنند، اما این نظام با ایستادگی رهبری و ملت پابرجا ماند. ایران با وجود دشواری‌ها، از تمام جنبش‌های رهایی بخش حمایت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656072" target="_blank">📅 15:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPdgGptIDHFEwdqB8X7NBip2n_mi_JE1P36fjZE0Btjl-R6N4sAWc4xLcppMNeobGjGxXDkcBLA9YqFICChCWvX_pIyGwn7HhPs-XudZBdwpuZIS5BTrlcewovwiM2us3jBCt0malPTQifDzFMZhqY__VxG4q2AsX0wzYcYDBwqT_xVXY7tkqg2xmgAhv7drdZTt4NJf2ej5w-IpJ4YlyyiRZ5GDaJOXXtGd3MIavK3uk7dJL4GhhrBuZzdeJb3uDS-ULvE-fI5JsW_vttloqwhCPPbYbCGSIWUgyy0gX9ctKGLGY9YUQGA2syXNSitPHZuw_QonIFOHONjsRoe6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراکش در حال ساخت بزرگترین استادیوم فوتبال جهان، با ظرفیت ۱۱۵,۰۰۰ نفره
🔹
نام این ورزشگاه گرند استاد دو کازابلانکاس، با هزینه ۵۰۰ میلیون دلار قراره ساخته بشه
#ورزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656070" target="_blank">📅 15:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6D-Y8GukI4KYuOCa4Z9jyrp4QY0lrFbf5RlZucWuyVT5DF2iwk1A_VCBtkIja_UFWKif5wOGB54yl4m-oQ8wvfdNKnih7an4bu-AkV15t2rh6wdJvblb9m65zkZ25CHPWrTtyou8t5cGLBak6mFS1quy5-HeGOzsAwdKZVYN1aYbGsx-nhp1WdwFgzN_D88_J9QRHgZD_ceXXNdyornms7iUtFwDZR5LgzHcZgySpov2Ft0asoaUQhFMomXwAEFCbeTku2_QL2fgxkQ7j8F7GX35zUQ2djvd_TktsKTIu9EypYmt0j20YgDTVRnp6kZVng0RYz_F-G1bP543dOVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656069" target="_blank">📅 15:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آماده سازی مواکب مهمونی کیلومتری غدیر در‌ تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656066" target="_blank">📅 15:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a644f3f57d.mp4?token=gDQgzsKpskoJef_qlujAoKLee7BkYR1A-uiN0htEG37gEwVCU37cWioLbEfIoEJw9vNtYW42Tl7-xMUSv2erzYpV19gxN2r6hErOUW5O6BNJrSIeYNw35MH7F1uFUYvTuTFxrZNfgS6bUOKccVjrs6KFapqidp_D3a4zpko7qgLWMXM-8W0b9Sce2Bm0BjmbIxmq9mKTK5kjg3g4r0eyhT4Dgr35A6WaFb3rRCyB0dfUb6yyQ6ae3ZXYGqgPaC4GEfiRnJ2eGKufhKqku0fiasGdOReJlXgslR-keG2DoCLpuxoglGSGQ74lWU9F8VLkvDgLN68_IDA2XT0zg-inXHLiN9fzbFhSMU9wLK_5oCV_GE57-sUIE3BhhAqw8vNl4paNjEUBkiLqk2BF_QSSLq2BVfkilwoWI1w-Amj8XWSaMM3afauElEG5t_4D36-W3DOslcJYPV2ZAPeBfOztNIvv5QmOr5vGryvgb8mHH4RldAq7jucS-jSbDorJ1dz0MqPeGsDIBNktOMQgbPn7qCitrnEpTuome2vACo9CkS8xbQTyF-Korg8wuxJbTxFdEJqwSm_gXcyTbmsHX5cYeEp0S3G_42mZ7zwUSVdB3Zl62lX6zq3dKwbKDI0DhpDiuuwvWABHQmX18BI_eEnzKCwQgt2P2NlngLFv1pX8t04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a644f3f57d.mp4?token=gDQgzsKpskoJef_qlujAoKLee7BkYR1A-uiN0htEG37gEwVCU37cWioLbEfIoEJw9vNtYW42Tl7-xMUSv2erzYpV19gxN2r6hErOUW5O6BNJrSIeYNw35MH7F1uFUYvTuTFxrZNfgS6bUOKccVjrs6KFapqidp_D3a4zpko7qgLWMXM-8W0b9Sce2Bm0BjmbIxmq9mKTK5kjg3g4r0eyhT4Dgr35A6WaFb3rRCyB0dfUb6yyQ6ae3ZXYGqgPaC4GEfiRnJ2eGKufhKqku0fiasGdOReJlXgslR-keG2DoCLpuxoglGSGQ74lWU9F8VLkvDgLN68_IDA2XT0zg-inXHLiN9fzbFhSMU9wLK_5oCV_GE57-sUIE3BhhAqw8vNl4paNjEUBkiLqk2BF_QSSLq2BVfkilwoWI1w-Amj8XWSaMM3afauElEG5t_4D36-W3DOslcJYPV2ZAPeBfOztNIvv5QmOr5vGryvgb8mHH4RldAq7jucS-jSbDorJ1dz0MqPeGsDIBNktOMQgbPn7qCitrnEpTuome2vACo9CkS8xbQTyF-Korg8wuxJbTxFdEJqwSm_gXcyTbmsHX5cYeEp0S3G_42mZ7zwUSVdB3Zl62lX6zq3dKwbKDI0DhpDiuuwvWABHQmX18BI_eEnzKCwQgt2P2NlngLFv1pX8t04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابرپرچم های خلاقانه مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656065" target="_blank">📅 15:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUayp2gegAI5oocHtPqoEt_K3eVQ2iueipTUR4cv3K_KRAxOWCEPOSQCB51Uie4QvzFOiru3b7aYsiP4YPwy1V7mQ2stKafr-B39E48e0YwGjEs4kHREQUwDLQ_OXQLXO-w1YFoQWoxM20RdzSuZObMpjf7hvMCkilcnArsIwZDc_NJl8-CR-oCW9geSqX9UIDeImzTUy7Nij-QSdAEuaAqajOXA00Z5HVyw0dWKj1-sQnBvINxUimae8OfGW0gryRl9w3erBwt20GZcwsu-meQCbQRAF7ezQsSqSTDbkwiCNS9swKXDVdkwxqHPe2QhMBTm-R1wQrFNxwlskapKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار تصویری از رهبر شهید انقلاب به مناسبت عید سعید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/656064" target="_blank">📅 15:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس| خبرنگار الجزیره: حمله هوایی اسرائیل به شهر بیت یاحون در منطقه بنت جبیل در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/656063" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فیفا در آستانه جام جهانی ۲۰۲۶، ورود بطری‌های آب چندبار مصرف را به ورزشگاه‌ها ممنوع کرد؛ دلیل آن مسائل امنیتی و جلوگیری از پرتاب اشیا به زمین یا سکوها اعلام شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/656062" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مهمونی کیلومتری غدیر در پاکستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656061" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7535f633d.mp4?token=oHj9mo2QCRg6utvGLxzVU5P7VKdS1qH8013-zc5TbJ8pnq8pU_sdFIDCNu_ZsVXHuVcBiSPacq0O-2AtObUnCL2KzlrWDupLPCazE1IAKy1I3myfkCCxe0kfwzugqAjB6QBxWLwTl3thgknvfJDfUB11IYR_M9YsZxNUubmF0YmnVZaX-_APOIwWLJfE2obf7lLR3DdaJH_YIkkOAxT-1812Qn-_xBqBlx8rl8GoRBusdA4axYxkbX6qHDzAgHlH7lrJReStdsQw9VAJsPQjhtxG9CdJjUyF22-FqpiiMhn5R8tB1nQersjojrengQ6BCiPJAdhP5EjxT6-knLoiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7535f633d.mp4?token=oHj9mo2QCRg6utvGLxzVU5P7VKdS1qH8013-zc5TbJ8pnq8pU_sdFIDCNu_ZsVXHuVcBiSPacq0O-2AtObUnCL2KzlrWDupLPCazE1IAKy1I3myfkCCxe0kfwzugqAjB6QBxWLwTl3thgknvfJDfUB11IYR_M9YsZxNUubmF0YmnVZaX-_APOIwWLJfE2obf7lLR3DdaJH_YIkkOAxT-1812Qn-_xBqBlx8rl8GoRBusdA4axYxkbX6qHDzAgHlH7lrJReStdsQw9VAJsPQjhtxG9CdJjUyF22-FqpiiMhn5R8tB1nQersjojrengQ6BCiPJAdhP5EjxT6-knLoiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای خیابان انقلاب یک ساعت مانده تا آغاز مهمونی ده کیلومتری
حتما  پرچم حزب الله و عکس رهبر انقلاب همراه داشته باشید، این بزرگ‌ترین رویداد خیابانی ایران است که به احترام امیرالمومنین علیه‌السلام برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656060" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYQKBLtV8v3unvwAciZQVyHSvOKs_AcHD3HS7hk73aCONT8mTI4qZHSFstY6J8DJl7zAM7s5iZLx9YXCOxMCE38mE_ww1Ysp4HK-GDwk3bOTo6fQiANq4pyCLHz_LaVarPbCZQo5odzo0zw8XD0w-0CspnmsIqk5wkmT-__wAGyHXvA0uapV6C_67KzPfXvLgYdhZ8aRx9DZ29dfb24danWCRDSWjBcSA8jUp9PnB1cXFdX6evjsNryR96wVUhjUN3n4Sv03yEhtNo617Vui43QQ42dsdlLpOyZfbmsiXs7hzxtpSIO5uJKPLTTUK8qL_yjRjZK4989Q9GSqzZ6pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آب زاینده‌رود به اصفهان رسید  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656059" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عراقچی: لحظه شهادت رهبری در دفتر ایشان بودم / ساختمان هدف قرار گرفت اما ما سالم ماندیم
وزیر امور خارجه ایران:
🔹
روز شنبه پس از بازگشت از مذاکرات ژنو، ساعت ۹ صبح برای ارائه گزارش به دفتر رهبر شهید رفته بود که ساختمان مورد حمله قرار گرفت.
🔹
با وجود احتمال بالای جنگ، روحیه ایشان مانع از رفتن به پناهگاه می‌شد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/656058" target="_blank">📅 15:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دونالد ترامپ: دیروز، مجلس نمایندگان با ۴جمهوری‌خواه بد و همه دموکرات‌ها به محدودکردن قدرت جنگ من در میانه مذاکرات نهایی‌ام با ایران رأی داد
‌
🔹
چه کسی چنین کار غیروطن‌پرستانه‌ای انجام می‌دهد؟
🔹
دموکرات‌ها با سندرم اختلال ترامپ پر می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه به من یک پیروزی بدهند.
🔹
آن چهار جمهوری‌خواه؟ پوپولیست‌های خودنما، باید شرم کنند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656057" target="_blank">📅 15:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e520b2e2.mp4?token=aRrFbH3-uX9Vlgt7qf9zxj2fDCj82_SdbPgfp2IidNKwuro3fJDs0VP02ACUXTkgX9p-x7FXjIrxf7WDuoYLu0sqIvaSi1b1x3DZzfIGtq0EwxKGIg971Mtn9FUgGwpOIzsoA0y6qiLhXG7lx2mmlWB67Qaz1Py5L17qodBUd0u11hQJ8zx_NRbns-otmzxAVhsxCZ3EKJKlNwoUmlFc5EvrvD08iI6Ui_idelu7Fzz8WPNeWc25yiHbPN2x8IJVGEXksYnoKEZdew92oGnuGfMSazI4Bs7kpMC26EMa4rOx7SnUTwRlE1tYzAC4PvFUHM4NzB9BEiqX5lo0lMBq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e520b2e2.mp4?token=aRrFbH3-uX9Vlgt7qf9zxj2fDCj82_SdbPgfp2IidNKwuro3fJDs0VP02ACUXTkgX9p-x7FXjIrxf7WDuoYLu0sqIvaSi1b1x3DZzfIGtq0EwxKGIg971Mtn9FUgGwpOIzsoA0y6qiLhXG7lx2mmlWB67Qaz1Py5L17qodBUd0u11hQJ8zx_NRbns-otmzxAVhsxCZ3EKJKlNwoUmlFc5EvrvD08iI6Ui_idelu7Fzz8WPNeWc25yiHbPN2x8IJVGEXksYnoKEZdew92oGnuGfMSazI4Bs7kpMC26EMa4rOx7SnUTwRlE1tYzAC4PvFUHM4NzB9BEiqX5lo0lMBq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار؛ سخنرانی شهید علی لاریجانی درباره زنده و ناظر بودن شهدا، یک‌سال قبل از شهادت خودشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656056" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJLQN9wZBjBQv8bWhzLWaS4qwbNS7Ak3sgZP6p7tNRLtkMlzeLg3uOwEqk5DAQiWVbEp37DY2qpTNHODyuIpXBoqfTIVdDJOPiPkASlE1cwQyvEtGDFWp_GxTyDZwxGbX3PRO2zgNyxhKzHQMOZrPluAseaXMExbawe9MuAWb1HL1QBg0FHoc970xf6Aw6XlSFktWFTe_5k3fDQ4UZ275BIa_GuMJiaroQF1vOW07kGuiigy9jlCejPWktR63zUEosVgPn3LPpYC7IxKb9mcZwEvQwGWMvs0xFdApJ-38744WvAQhkXajwG8QJzCJJgNcJAnZxMbG7OasXkhejcesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک زیارت کمتر شناخته شده!
🔹
زیارت غدیریه؛ روایتی فشرده از جایگاه امیرالمؤمنین(ع) در قرآن و تاریخ اسلام است. این زیارت با دربرگیری بیش از ۷۰ آیه مرتبط با ولایت و وقایعی چون ماجرای فدک و نبردهای امیرالمومنین سندی بی‌مانند در تاریخ تشیع و چون نامه‌ای از…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656055" target="_blank">📅 14:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
چت جی‌پی‌تی، دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656054" target="_blank">📅 14:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون حقوقی و بین‌المللی وزارت خارجه: اگر حملات به لبنان متوقف نمی‎‌شد، قطعا جمهوری اسلامی ایران اقدام می‌کرد
کاظم غریب‌آبادی:
🔹
پیام‌هایی درباره توقف حملات به لبنان از طرف وزارت خارجه و از طریق کانال هایی به آمریکا ارسال شد.
🔹
آتش بس برقرار شده بعد از جنگ، شامل لبنان هم می شود./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/656053" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sxy2hsbqFyneYwJOzqtBv7Ibgs4Y6NwJY2PoVcXrdimEOdf_L3bRmOBDb4DgIWMFMqTH-i1x-bT5kLOF80pIxmUKDhvGM24ipTrWgpxmIig1mLwLAYLhvihmEPTNbRazk9pmoxA51XYR3_rg4-7ntINHGVEW534kxiUaMaqDvHl8Qjr_9fyPHSx7bM8OE8j7csnhUiRFJr4I1l7UkDRmPy_X8dInJUpWvc_rFe1Q8AVVdtuJyuVBPuL54v2ZX1pjZCz_Eq2S_1cbqqhHALILE_4ZEIcvAWI3t3q1VtDAXjVTqhCVd4HbtqEC-ht30MB4OFkLQ1zeU6HqDlu6UZGWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر روز بازی فدراسیون فوتبال ایران برای دیدار امروز مقابل مالی با اشاره به ۱۶۸ دانش آموز کشته شده مدرسه میناب
🔹
ساعت ۲۰:۰۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656052" target="_blank">📅 14:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFMMVFW669d-nFOw9fs09z4Y5nj35k6TmKYmWwxKNYyhYk8DkPYHY3zmKC78uslvVpcJJNIQy_FbzO6dXQFxRtoIUGxyhrRg3UjMYXxuugW43XwgdVUg6BnCyossA0C3g_oIVRdHfcUGl-NAq9kajcUgBwl8PynMPxIien2ji8ge4hFk9ZVurATbbpZraqa6qFpifWKPq6_BaQ6ZTYUXE6SDpDyOpKWN-nMBTxz3odcCmTXaBoTAsfaLyjCtM01RwjcXrLRmzsCYbFFROnftVFTs7XLGbmpMd7-RLl4TMuSJda4VQH4PfnKEUngNdWDbpsEm9zRbCGv6RMZ4ofmGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzZppaA_Y0HYYM87qbk6APb8cmy_hl6DRduysMuY11IzQMqrl1DntTLBFL6_5VcUpVVWnQ1cSIy9j2NAMuGZu9Ft2rQPic1VAwNzrDftSGjt62ndlwgQFhdXFxRFwPwWJRcVqX_eM1eqNv_KmhBJEkuTicdNYWPlD3DOGgiNJ2T43Le_kOpkSGB0YJziKXoF_n5f6p-uNolbqgppe53mYemZZq5iBpQGV_c5EApCFqQ-NlK_MaDdeN0101JhPce5HhsFF4a3iqSr3XoRnWCtLDR5jhVKC9TxkkwNdn8PdgOhps-_sEPzwDN8Uz0sK_9pDciIw970UwGjvET8C9rqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuXoP4-35k-J5NVRJD6IVQJtF6y-jU1-kxyJwW5j-MywHnfTBWghl0IdDiqBxOAn_15puqp9LP53DnmPWaIMXrVFejYROd0vIXjMH9l3UnXk5NtsWI9kAPRJGmKOfffhe3uTFkU-z6k7q7-xbGnVvLubzKQxFRdpu9Tj2zdV1gEEDW7cb7v6Ty7H9BbGf96-fU3AKXhV7ZxWvmjqQoiIeb92PI_TSfKspq3KWkJ17bm1rWmqklVLOWwOwxRE6rieDewD9x8Qg-7se-rf0E-EavaW0L8xByIjSU2aMCwU-IoGOGmWggN99m9IlgEi9gbDZGF48Uztk3JM7CL8UXZBlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دریاچه یخ‌زده قله سبلان؛ ۱۱ خرداد ۱۴۰۵
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656049" target="_blank">📅 14:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@abaratinfo</div>
  <div class="tg-doc-extra">Mohammad Reza Khameh Chian</div>
</div>
<a href="https://t.me/akhbarefori/656048" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">الْحَـمْدُ‌‌لِلَّهِ‌الَّذِی‌جَـعَلَنَا‌مِنَ‌الْمُتَـمَسِّکِینَ
بِوِلاَیَهِ أَمِــــیرِ الْمُؤْمِنِینَ‌ عَـلَیْهِمُ السَّلاَمُ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656048" target="_blank">📅 14:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تصاویر تازه منتشر شده از لحظه هدف قرار گرفتن فرودگاه کویت در ماجرای پاسخ ایران به نقض آتش‌بس از سوی آمریکا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/656047" target="_blank">📅 14:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e6263214.mp4?token=ojtD8l_0OBcG6AzeeerxuzK2y-q3mkixC-DEW2Vu0h_dX3FKM1sgvl8A4YKyFbmxWr5ieNbZr2TyY4Wwwblvpp3jup6AKCd9YLrIM8nb5xPmDAuXXS_Ijg6B-wbHVtWeDx8MGvV6oSvGPo8IclY6exqqEuEzbC1xa7xFgAtHY9pKegqeTHeb_uFx33VKABOnYgKX9-YIbqhv6JhSaV7Q7lS18XWq5ijNG3oTpup3oen3TZcN56UAQpgkkaIef23R1S9RRHVlfl70XXFdInLRjcbF8o2g5niY9MSGbjfHE98NSBgRvtXnUhuL5YQ-zZz9mfR5rt82vQU5bO2U-idWFpPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e6263214.mp4?token=ojtD8l_0OBcG6AzeeerxuzK2y-q3mkixC-DEW2Vu0h_dX3FKM1sgvl8A4YKyFbmxWr5ieNbZr2TyY4Wwwblvpp3jup6AKCd9YLrIM8nb5xPmDAuXXS_Ijg6B-wbHVtWeDx8MGvV6oSvGPo8IclY6exqqEuEzbC1xa7xFgAtHY9pKegqeTHeb_uFx33VKABOnYgKX9-YIbqhv6JhSaV7Q7lS18XWq5ijNG3oTpup3oen3TZcN56UAQpgkkaIef23R1S9RRHVlfl70XXFdInLRjcbF8o2g5niY9MSGbjfHE98NSBgRvtXnUhuL5YQ-zZz9mfR5rt82vQU5bO2U-idWFpPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یا علی
نام تو بردم نه غمی ماند و نه همی
بابی انت و امی
گویا هیچ نه همی به دلم بوده، نه غمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656046" target="_blank">📅 14:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656045">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4-ABJAvBJVLB7CNDVfdHQyBMP_P_LSZ5_d2zC3DK1LynKYYTszyFRbTqwOfsw3SEcfy8SbEggPvkUbV5r5lLtbJqeUCqiFFNjDc23yytql-1BlUv2Z5PO7b_e2OslgOTdzl_ufxrAC61IwzFhUR10v9ydk-uZZhKyWJQegzupGmxLOtnAd-KlJ7J65bX_HosiibN5njnH1RFx0soYYkqm495TM9retR0N-lCJjZKsrChPe8Gof1MUs4hsicXTyc0B01H0gjtiUjga8WmIlAoqP83JtwWqaGA2tpxDc77V1rvz_JkNIMFAao__fT4g-KbHDLnybe-wvxFUMKDA7ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهرابی طلا و سهمیۀ جهانی را باهم گرفت
🔹
دانیال سهرابی در فینال ۷۲ کیلو رقابت‌های کشتی فرنگی رنکینگ اتحادیه جهانی کشتی مغولستان، ۸ بر ۵ محمدجواد رضایی دیگر نمایندۀ کشورمان را مغلوب کرد و علاوه‌بر کسب مدال طلا نمایندۀ ایران در این وزن در مسابقات جهانی لقب گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/656045" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656044">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مبلغ جدید وام فرزندآوری از فرزند اول تا پنجم چقدر است؟
🔹
مبلغ تسهیلات برای فرزند اول ۴۴ میلیون تومان با دوره بازپرداخت ۳۶ ماهه تعیین شده است، این رقم برای فرزند دوم ۸۸ میلیون تومان با بازپرداخت ۴۸ ماهه، برای فرزند سوم ۱۳۲ میلیون تومان با بازپرداخت ۶۰ ماهه، برای فرزند چهارم ۱۶۵ میلیون تومان با بازپرداخت ۷۲ ماهه و برای فرزند پنجم و بیشتر ۲۲۰ میلیون تومان با دوره بازپرداخت ۸۴ ماهه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656044" target="_blank">📅 13:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656043">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZeZJK8FeRCZURIVNBTs7um9970CKMrnWFJE50bzfLmE2hG6opwh8SY0aAnZtXpTZkYoesJpEfhdBiinhLFcDe38vrRHS5oae2nBJk57F7nhrRG13hH6Cj-j74BTL8XfFXnQOOMMEyddJ3hNIh6e7pahMO8GLaNst_J-x04hQjZBd4ARM5LB34F8wguOucFjYWOjKGEZobZ6uVRPtLG96OQsRmtmgOA7LQovSTSxRK5M5n-aUvD8BisRYNF3NUVNipcekpF7dELLdD_VSj20OWecJA_Ywrs2_OZfq172D_jtOyFNgQRgPxdXOv8Zrk9Vl8A2eZfGx9T60NeEfGqWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز اعلام ولایت
🔹
هر کس من مولای اویم، علی مولای اوست، این جمله در میان جمعیتی عظیم طنین‌انداز شد و یکی از ماندگارترین رویدادهای تاریخ اسلام را رقم زد. #روایت_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656043" target="_blank">📅 13:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN0X85uKoGOJqzYzcpmbyz3Ydxr9CVF7GTAW2DRQoKBDVC3SLFk3-_bUvixGAJhvXgIt0Fu8QVryxP5TMhuYBCroVZEirOenmyoTcmmPeQ3fmWP10QBV-ddkOpIZpt2KaJGCbkrDeVIIQqhYCyVa0Pl86nZY9PSAuI3U8sd5cWy2GT6lIUQUR6E-PQUv8pdEx_ws28w8LT9HDv0FYYuJpnL5-w8H7RUi-8Zk5pizyEzH6SUkNPpXOh0qz6ONyVFGjHo-08D-UFNgqolYzmWjdIMBgnI9IF8jEF3DWrr0-06xLX_QlInKVZkjP0PT-Rbp4_lRAWUjYOvxCDZbrYVflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
📲
‌
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656042" target="_blank">📅 13:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mohsen Chavoshi</div>
  <div class="tg-doc-extra">Ali</div>
</div>
<a href="https://t.me/akhbarefori/656041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">علی آن دلیل رحمت، علی آن چراغ ایمان
علی آن که می‌درخشد به دل همه دوران
به ولای او قسم خورده خدا به روز محشر
که بود علی حقیقت، به یقین ره‌گشای جان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/656041" target="_blank">📅 13:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656040">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارات جنگ بر نظام سلامت؛ ۳۸۵ مرکز خدمات سلامت دچار حادثه شدند
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
۶۳ مرکز بیمارستانی، ۵۶ پایگاه اورژانس پیش بیمارستانی و ۶۴ آمبولانس در طول جنگ آسیب دیدند.
🔹
از بین آمبولانس‌های آسیب دیده، بیش از ۱۰ تا ۱۵ آمبولانس نتوانستند به چرخه بازگردند. همچنین دو آمبولانس هوایی منهدم شد و دو آمبولانس دریایی نیز دچار حادثه شد.
🔹
هر آمبولانس ما که از رده خارج می شود بالغ بر ۱۷ تا ۱۸ میلیارد تومان هزینه دارد. ۳۸۵ مرکز خدمات سلامت معروف به مراکز جامع بهداشتی دچار حادثه شدند.
🔹
۷۱۸ نفر از همکاران ما دچار حوادث مجروحیت شدند و تقریبا ۵۲ نفر از همکاران ما در طی دو جنگ شهید شدند که ۲۷ نفر از آنها در جنگ اخیر به شهادت رسیدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656040" target="_blank">📅 13:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656039">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
آکسیوس مدعی شد: دو مقام ارشد آمریکایی گفتند که در حالی که ترامپ می‌خواهد به جنگ پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656039" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656038">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی جدید از حمله هوایی به پل B1 کرج در جنگ رمضان
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656038" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656037">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی‌که ۲ تا دست میره بالا، ولی نه به نشانه‌ تسلیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/656037" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656036">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پیام تبریک سخنگوی وزارت خارجه به مناسبت عید غدیر
اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی به مناسبت عید سعید غدیر خم این عید را تبریک گفت و حدیثی از حضرت امیرالمؤمنین علی(ع) را به اشتراک گذاشت:
🔹
«اَلْعامِلُ بِالظُّلْمِ وَ المُعینُ عَلَیْهِ وَ الرّاضِیُ بِهِ شُرَکاءُ ثَلاثَهٌ»؛ یعنی ستمکار، یاری‌دهنده ظلم و کسی که به ظلم رضایت می‌دهد، هر سه در آن شریک‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/656036" target="_blank">📅 13:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656035">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای العربیه: مذاکرات آزادسازی بخشی از دارایی‌های ایران به مراحل پایانی نزدیک شده است
🔹
مذاکرات برای دستیابی به توافق درباره آزادسازی بخشی از دارایی‌های مسدودشده ایران به مراحل پایانی نزدیک شده است.
🔹
رایزنی‌ها درباره سازوکار آزادسازی این دارایی‌ها همچنان ادامه دارد و مهم‌ترین مانع فعلی، نحوه مدیریت و استفاده از این اموال عنوان شده است.
🔹
همچنین پیشنهاد تشکیل یک «صندوق ویژه» برای واریز و نگهداری دارایی‌های آزادشده ایران تحت نظارت مشخص، در حال بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/656035" target="_blank">📅 13:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656034">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تکذیب اعلام برنامه امتحانات نهایی
روابط عمومی وزارت آموزش و پرورش:
🔹
جدولی که تحت عنوان برنامه امتحانات نهایی تیر و مردادماه با امضای رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش در فضای مجازی منتشر شده است، صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656034" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656033">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFmj6uIwVw5ZU3NNStGa97MmiCnNNldl85Vvxs7xVyfLrukLCClgJ3y8WLRQ6NAyL6p5xynBkTVeKdbG0aA8_LrUOfbExjZehbm4li2-gabePzWR7eiDTDq35SbrRHFD1noVzao9omWRys-dA6BdWk9h1jHvb7z_d4nKO6yCvPcA82RgOHUWOh3DZu2djKuNhfHuO_3-oIE9VW0XGbwt6igSX5whHzz4dTbkFvEd4miik-hT5bIs5NY5F9RaEpyLHQBgPs9jaNuFZDaE8JSX_GyTIGZzBwrD8IoVa2U_ZgTWZHAbQIPRY5faT45UlW4mXU82GMcZWKLo5mc6lL3jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ ادعا کرده جنگ تمام‌عیار با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند
وال‌استریت‌ژورنال:
🔹
مقامات آمریکایی گفتند، ترامپ به طور خصوصی به دستیارانش گفته است که اگر تهران نیروهای آمریکایی را بکشد، پایان دادن به آتش‌بس با ایران را بررسی خواهد کرد.
🔹
اکراه ترامپ برای شعله‌ور کردن مجدد جنگ نشان می‌دهد که او ممکن است مایل باشد برای جلوگیری از درگیری گسترده‌تر در خاورمیانه، شعله‌های آتش کوچکتر را برای هفته‌ها یا حتی ماه‌ها تحمل کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656033" target="_blank">📅 12:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656032">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uknVBtg-luZYFJNSda2ak8gDtJRO9_Y1JIx6ZS9akGkfWapQu7TZRoOeLFJ8xrtxRVOkuXvZ48wSOF60W8WDcQZKgx8p6yRBNlIrbFP7nbh10zYbwZlEjU-dRrkmtLpF-bmSGBUAq0mF6YHEmLmOGsGx0yOoq5ywNefgSm6QoewM7oZFmhJGuz3QloYOacPVUXL8g93tCzP1FhOz2SfWl89-NY92fhiWh4g8k6ODqb0RmwduYR114o_ruElqabs9hQwcZWN0SWZJY9pqUMEA0AeDeOLX5jN6Bnso_NcJLsNfnGuyRxI3Xe1nvgHGjTb7amO3FJJbEMHTgqu8Rot3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ
🔹
سرپرست و دوست شما فقط خدا و رسول اوست و مؤمنانی که همواره نماز را برپا می دارند و در حالی که در رکوعند زکات می دهند
(آیه ۵۵ سوره مائده)
.
🔹
روزی فقیری وارد مسجد پیامبر شد و تقاضای کمک کرد؛ اما کسی چیزی به او نداد. او دست خود را به‌سوی آسمان بلند کرد و گفت: خدایا! شاهد باش که من در مسجد رسول تو تقاضای کمک کردم؛ اما کسی به من چیزی نداد.
🔹
در همین حال، امام علی(ع) که در حال رکوع بود، به انگشت کوچک دست راست خود، اشاره کرد، فقیر نزدیک آمد و انگشتر را از دست او بیرون آورد.
#اخلاق_علوی
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/656032" target="_blank">📅 12:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
آستان قدس رضوی: چند مکان برای تدفین رهبر شهید بررسی شده است
🔹
در زمان مقتضی به فرزندان رهبر شهید و رهبر معظم کنونی انقلاب پیشنهاد خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656031" target="_blank">📅 12:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656030">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0A6zsPHo6-O2d4fwd1GB8g_63bxLduIbTQ4vWqMURm91kQuUOIxl-7H1tLp8JsmZ2DimebeM3A38C8ExK-p7uzVhhOwAIYrtPBgRyC1QRM7n0xzqGbJGi-WM2QskvVYESSknL4Q28q4lue7BXGNLD_NED3LHRTYqqgdVcEOjx043mLwnMpEAAjsTq9hXyP46yu1gGsa4z_pWYEhsmDIl918P6O_mW2nGpKpvJ55jSGnkYOAnVIeu3XUVohhEYuQwIUnIBHpU7i1xKdXb88D0lCrfRaO2GzdAgaBnQEBgzcWLIAYf9PtJU1RGuKlsqMh7m_Oli2Lwpbh3yEmYs0PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: تنگه هرمز مهم‌ترین اهرم ایران در معادلات جهانی
سی‌ان‌ان:
🔹
ایران با کنترل تنگه هرمز یکی از مهم‌ترین اهرم‌های خود را در معادلات اقتصادی و سیاسی جهان در اختیار دارد؛ حتی در صورت دستیابی به توافق دیپلماتیک نیز این ابزار از دست تهران خارج نخواهد شد.
🔹
نگرانی اصلی بازار انرژی نه هزینه احتمالی برای عبور نفتکش‌ها، بلکه احتمال اختلال یا توقف کامل جریان نفت از این گذرگاه راهبردی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/656030" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان شیولوچ در منطقه کامچاتکا روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656029" target="_blank">📅 12:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp0jTrdZRr1Bk6t5br8dn55CH1vCMntYnorz1wN7u8se7QpbzHie87jfJH8XXrJEZ3zWYyKMTge5UG58n8PHzYaeWXZBdVt5xBrrWyiso0ORhx5aGnvLyP439arReRv7Q7fve57S5k0SDGMYbH1_gtovkWaTTp_ghPQvcyPYQLqytlXdLyNBzpeuQZqimf40G96eVQ2XyKzTjZGHTr3IRHRNlfSCiLnS46ofiTipt0xH3PwLG1nz0h5CamMyl30wxOKmCPPQBK9L96-1hpv7oqtR1AVgqjqMhX_tdhA4dFlWQe_Kw0jqqZPoOyzzRhpiCLuAVW6Zqqzdc0fpYD4b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکات کلیدی پیام رهبر انقلاب اسلامی به مناسبت سی‌و‌هفتمین سالگرد ارتحال حضرت امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656027" target="_blank">📅 12:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656026">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکمیل ویزای اعضای تیم ملی ایران برای سفر به مکزیک
🔹
با انجام فرآیند اداری معمول و صدور ویزای دو نفر از اعضای باقی مانده تیم ملی، روادید تمامی اعضای تیم ملی صادر و این فرایند تکمیل شد.
🔹
تیم ملی فوتبال ایران روز شنبه ۱۶ خرداد در ساعت ۱۵:۲۰ به وقت ترکیه عازم تیخوانای مکزیک می‌شود.
🔹
طبق برنامه‌ریزی انجام گرفته، کاروان تیم ایران در ساعت ۱:۳۰ بامداد روز یکشنبه ۱۷ خرداد وارد شهر تیخوانا مکزیک خواهد شد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656026" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
جزئیات رای‌گیری کنگره برای متوقف کردن جنگ ایران؛ ۴ هم حزبی ترامپ علیه او رای دادند  نیویورک‌تایمز:
🔹
مجلس نمایندگان آمریکا روز چهارشنبه طرحی را تصویب کرد که به موجب آن، ترامپ باید نیروهای آمریکایی را از خلیج فارس خارج کند یا برای ادامه عملیات نظامی در آنجا،…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/656024" target="_blank">📅 12:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی درباره‌ی تغییر جنسیتش: تا ۴۷ سالگی خودمو تو آینه نگاه نمی‌کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656023" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
دسترسی به اسپاتیفای بدون vpn ممکن شد
🔹
بررسی‌ها نشان می‌دهد دسترسی به سرویس پخش موسیقی اسپاتیفای (Spotify) بدون نیاز به استفاده از VPN امکان‌پذیر شده است؛ البته نه روی تمامی اپراتورها.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/656022" target="_blank">📅 12:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/casd51aG3RGW3q6UNwOc4YKawSncveQEQ6GzgD4fb1Rm5ikoy5E5nKrDiW0_rJ2pvu-J-bpmERwm_xQQChB3ruDEEjkl46iJEjhFSorv1ixLHAAVJXgQIy9T4rG3hAutfrRMcBp_D1B9XYaCEpfMj75s985qwMOFtzoigfrWONikCWrr9CcEUXrkqVCZRKWj62Lpuc5LD-5tyWdF4HuC7g8kvmx1vZGR61pQqdSNM4FJZ0AuEPWo3ic83XIKNsLVUKkI6rt6fUGcjPIXkWzzWpSRr5U4kue2YvWHHJ99Inuhj5pL1zvqJ305W7nIf5VBGWdEuVpHTkAJtt4Y-Put7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام دستیار رهبر انقلاب به مناسبت ۱۴ خرداد و تحولات آینده کشور و منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656021" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
دستگیری عاملان شهادت مأمور کلانتری باغ‌فیض
فرماندهی انتظامی تهران:
🔹
در پی شهادت یکی از مأموران گشت کلانتری ۱۴۰ باغ‌فیض در شب گذشته عملیاتی برای دستگیری عاملان این جنایت آغاز شد.
🔹
مخفیگاه متهمان متواری شناسایی و  هر ۳ متهم حاضر در صحنه جنایت در محل اختفای خود دستگیر شدند؛ متهمان در تحقیقات اولیه به ارتکاب قتل با سلاح گرم اعتراف کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/656020" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غدیر خم؛ رویدادی که تاریخ را ساخت
🔹
برخی لحظه‌ها در تاریخ تمام نمی‌شوند؛ از دل یک بیابان آغاز می‌شوند و قرن‌ها بعد، همچنان در حافظه ملت‌ها زنده می‌مانند.
#روایت_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656019" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
