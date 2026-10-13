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
<img src="https://cdn4.telesco.pe/file/S9xYJItOGVSgrARaqBGLz7W6s81Ki0sBw22li7E1yzrInTUSypoPBa-sOzBrSJjdMxVb3YJtIvBjF40kLeBl-ut3oxXt4Qoz7uZVqnvQjRTG7j_IgxcnbxmOZUGVhBvQTXdcje8-Z5IXo8qN-3VCKQNEkJg9WYUaRECBUb7AeZfeN1r_zkmSKoO73xuP1Xy5DtYGal19E6al4f2pwehyw7qocKqNwk-V3qJkqQpkuHe3vyYvs_R8ESrxigpbySp8kfa3gdIfMKuQXmHeVAKLPULRoCkZ7REuiLNW-mx013Uo41ionVX7VbVVr4AoLn34KT8q6IgjKGTBNdeoNDRoRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-468280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تگرگ در بشاگرد هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 330 · <a href="https://t.me/farsna/468280" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه سه از وضعیت نابسامان کمبود آب و غذا در غزه
@Farsna</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farsna/468279" target="_blank">📅 22:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ائتلاف سعودی وقوع حمله به نقاطی در الظهران و حرض در شرق عربستان را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/468278" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a00I6F83Dk5s7dRcBu5EOVJu-4w6CYAVSDpsCMIf4lu4JupYMOirum32fCuyR_ctgWbrtMc2-_02ePjIyLVLdRK0ORTYFPoPjnB6EZ0YeoWXEwerdLhf2KAlu_JtW3yyR33w1xa2tIhk_tw4XAwMVFgoeltix9MnH4wboLhDuf_dWlhKAPe4KtpxxzFHpZ2lPiSMmhE3Lz-hMradBTVj-zhgAaYE0NLK_QXAntiQJ2tQTgUjCxyex4Dnv6kBRT3XlFhECyLOdlal73pZnRER8SA56ATA4nAS-HUbWTjldkJ8BP3-s_EfMcnd8bQSfwkReMoLcPEXqZ0aQwWkERyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش دیگر در تنگۀ هرمز هدف قرار گرفت
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/468270" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">احضار مسئولان میراث فرهنگی همدان پس از انتشار فیلم یک بلاگر در غار علیصدر
🔹
معاون دادستان استان همدان: درپی انتشار فیلم شنای یک بلاگر در غار علیصدر و انتقادها دربارۀ نحوۀ حفاظت از این اثر ملی، مسئولان میراث فرهنگی برای ارائه توضیحات فراخوانده شدند.
🔹
هیچ‌کس حق ندارد به بهانه تولید محتوا یا جذب مخاطب، ضوابط حفاظتی این اثر ارزشمند را نادیده بگیرد و آن را در معرض آسیب قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/468269" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aba203693.mp4?token=KDG_9dLq075mpCdudnQKrsAWLMKIZJdUSacAz-ZLfm1PmRdTyKcjcGKLRFARo4TbiCXGY_zTAJ49cVoCSuUhGaKKOAwZC2Rxg1R8JvfCmqLQrFgNBp7wYOmYf6ANhM7aq361PrvU4i4b4QnTjz_dXhgPj1Ci67o_m_UbBH_e7lzd230onxaOGsd6SF1b9cQkj8qwD0pry2E_3IGEW5tLKh1NIgqZf1YLiWCiEDRx7JX1GpmAFw2cliVhf2fy8E0PxZ_9vmDGbQUO3iqY7_p5TuN1R7e9YQJNfW-CJTue8vN5dHpvuemoZ063c9f8jHpYyh5NYUUVsI9t5vLR2CV4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aba203693.mp4?token=KDG_9dLq075mpCdudnQKrsAWLMKIZJdUSacAz-ZLfm1PmRdTyKcjcGKLRFARo4TbiCXGY_zTAJ49cVoCSuUhGaKKOAwZC2Rxg1R8JvfCmqLQrFgNBp7wYOmYf6ANhM7aq361PrvU4i4b4QnTjz_dXhgPj1Ci67o_m_UbBH_e7lzd230onxaOGsd6SF1b9cQkj8qwD0pry2E_3IGEW5tLKh1NIgqZf1YLiWCiEDRx7JX1GpmAFw2cliVhf2fy8E0PxZ_9vmDGbQUO3iqY7_p5TuN1R7e9YQJNfW-CJTue8vN5dHpvuemoZ063c9f8jHpYyh5NYUUVsI9t5vLR2CV4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران شدید پاییزی، دشتستان در استان بوشهر را غافلگیر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/468268" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18c34af21.mp4?token=mG6GyHmSGYUVhcYqUXfKZFOSeOHj3854ETDKSobL2dULpbrfpFx0ApcOHz5zqZ9PBIb0nirpo0PaMTmL98fhQ6lJGAkVGE8AkXuJgTI1FULcMPIe4abs4_Ng94arFVAKV1wW0dwC74bAiS5_BVXETOE-6OD2KG6mrZsL9T_fO9AscqEXPVWmNAFYL43YMJjkDLTaA1Y37mNiXEpdNrhxFiFJrPlJrHQG83yOESn29oSsz8TQVPv1rgCY3mWJJBxoVuEypX9PKaz9gwTVvnjQh_P4C-RvjMchABA5Wu8I3syCj4_ItfYtutlfHxkxyE_NHxWTyJwh2fUrJ2SqpG42dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18c34af21.mp4?token=mG6GyHmSGYUVhcYqUXfKZFOSeOHj3854ETDKSobL2dULpbrfpFx0ApcOHz5zqZ9PBIb0nirpo0PaMTmL98fhQ6lJGAkVGE8AkXuJgTI1FULcMPIe4abs4_Ng94arFVAKV1wW0dwC74bAiS5_BVXETOE-6OD2KG6mrZsL9T_fO9AscqEXPVWmNAFYL43YMJjkDLTaA1Y37mNiXEpdNrhxFiFJrPlJrHQG83yOESn29oSsz8TQVPv1rgCY3mWJJBxoVuEypX9PKaz9gwTVvnjQh_P4C-RvjMchABA5Wu8I3syCj4_ItfYtutlfHxkxyE_NHxWTyJwh2fUrJ2SqpG42dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ائتلاف سعودی وقوع حمله به نقاطی در الظهران و حرض در شرق عربستان را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/468267" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88f2193bf.mp4?token=Nu8mLCJPI5c6PBTj0hUFi4f4JiE9m6w-wk2GGrIGk6LqD_nwYfRlJJQoXCWz8CcyAi1hk8fXk-FjfCtuHJ4CbD2oVvRqAAvE9rEMThO3ilsJL6PhZwbrzsFtxEb8KUpntB0fHHK0dGc25MMevzRlYwmyy_eg7dk7jMydUFqmkAULtDPJjQr7tnfQKYEWqEeuYWMX6SDEmPhvyfP68Xv9670X7Bk_gDlq9q-Q15sqVERPyf-KwjSoeddGbZ9E1JYxS6mBriFmMpix-V3GPGKgVhf3V5vlnNhQtzDBQCDIIC5_kt_fvbyXXA1aB5XGk01I0fY8h12NUQCIL9iYqTZfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88f2193bf.mp4?token=Nu8mLCJPI5c6PBTj0hUFi4f4JiE9m6w-wk2GGrIGk6LqD_nwYfRlJJQoXCWz8CcyAi1hk8fXk-FjfCtuHJ4CbD2oVvRqAAvE9rEMThO3ilsJL6PhZwbrzsFtxEb8KUpntB0fHHK0dGc25MMevzRlYwmyy_eg7dk7jMydUFqmkAULtDPJjQr7tnfQKYEWqEeuYWMX6SDEmPhvyfP68Xv9670X7Bk_gDlq9q-Q15sqVERPyf-KwjSoeddGbZ9E1JYxS6mBriFmMpix-V3GPGKgVhf3V5vlnNhQtzDBQCDIIC5_kt_fvbyXXA1aB5XGk01I0fY8h12NUQCIL9iYqTZfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج: گاهی یک امتحان کوتاه الهی می‌تواند درهای بزرگی از رحمت و روزی را به روی انسان باز کند
@Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/468266" target="_blank">📅 22:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ هشدار فوری یمن برای تخلیۀ فرودگاه ریاض و ۲ تاسیسات نفتی
🔹
سخنگوی نیروهای مسلح یمن: در صورت انجام حملۀ اعلام شده دشمن سعودی به صنعاء، مقر شرکت آرامکو در الدمام و نیز فرودگاه ملک خالد و پالایشگاه شرکت آرامکو در ریاض باید فورا تخلیه شوند. @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/468265" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
منابع عربی از حملۀ موشکی یمن به آرامکو در شرق عربستان خبر می‌دهند.
🔹
به گفتۀ این منابع، ریاض پایتخت سعودی نیز هدف حمله قرارگرفته است. @Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/468264" target="_blank">📅 22:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468263">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌  حملات موشکی یمن به شرق عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/468263" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50387948a4.mp4?token=L5voXJ-yTscoGwarfLZP9HLIv4arZANAntoRVJ4KeCRxlzsKmfsXOe__RXqe0E1-g3SsHRTHJTSvPUe_ZKblUxmGcfvcsRb7-bU1oVdagmJvMRdP-TeivjWcyP1fnUKz8nADXhv3yTY7_G01aF2RHUv2uOn5zeh5R5Z_nK7cNMfAu6mcfST7wN0slpsToprqU7jzlB-zZjISRVZ8jfh7O9nEFdvzD3ai4LKWP213YmKA2_qa3CxE6OQT9gh_Fc619azeqv_X-dqkM_arYqnqtxaz8NpvFDwUBMsh6GHwlTt5WWP0gjcsf_e-WnRqw9nXmGgFYenlYVPQNGH3ZBvDhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50387948a4.mp4?token=L5voXJ-yTscoGwarfLZP9HLIv4arZANAntoRVJ4KeCRxlzsKmfsXOe__RXqe0E1-g3SsHRTHJTSvPUe_ZKblUxmGcfvcsRb7-bU1oVdagmJvMRdP-TeivjWcyP1fnUKz8nADXhv3yTY7_G01aF2RHUv2uOn5zeh5R5Z_nK7cNMfAu6mcfST7wN0slpsToprqU7jzlB-zZjISRVZ8jfh7O9nEFdvzD3ai4LKWP213YmKA2_qa3CxE6OQT9gh_Fc619azeqv_X-dqkM_arYqnqtxaz8NpvFDwUBMsh6GHwlTt5WWP0gjcsf_e-WnRqw9nXmGgFYenlYVPQNGH3ZBvDhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایستادگی در دستان مردم مراغه ؛ دفاع از میهن در شب ۲۲۷
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/468262" target="_blank">📅 21:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a345b3c5.mp4?token=XZM7GRi5GCggxov8v5gX-lcxRmgunWB5qj_qeWHME4CZVLsCK-2cAYAis4GVhaRp9aAGVJJL1kDIhcmphSQ_YzWoc1uziRsH0MfuqyG1D4Km2_PRL3uf0Hl5F4viQ6TvsTrT1cC3tdbwPl4vBNhS5Y5pciVnXYKmAZHgGv2bcCXCFWVLfROF8T5ifupDBod8gVRdXJ2P0AI7ATABkx611cnCm_EDN5hgSuu8rtAt4S5H8WU1WR1m9qq4rThjUehUYQAq_d3zifIyKIG3Xo6n8kA1YaA8p5D9XwdVyHEDOKIA59Z3sH8YPSxhSfD2ppmVInHl6JQ5MeWMXCyFo_J4UZphozS8hx7pwXgB173LMVFCAv_tYuG9PqZ4xC_a2gAm9_DOwIKPQPSKldjdNtZ6e6yoAqP76C5mfFRztmNRLN1xnCNBGN9FxiAacFPg_UHN4BdX64GZfecOGuMcNHhdZMb0Oum4jsT2KYbQA0NZtMrA2HF2HkTKmZfQCHyUkMEoboA4w8mkx6qrM150tMRGHmIqL4pTIi1IbVqSObA3V0HTRBnv3EIAbnzAuCpWozaYe4Xf4NV1J-wcWJ_wm7i7U6UpfqXi-3UOWF3v3tG9EHvwab1_Wuwc0s-5sxuiSdztzTYgzKCcqsI0m6Q1IiyvCmgzAYxPkkkCRGQguVdeVq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a345b3c5.mp4?token=XZM7GRi5GCggxov8v5gX-lcxRmgunWB5qj_qeWHME4CZVLsCK-2cAYAis4GVhaRp9aAGVJJL1kDIhcmphSQ_YzWoc1uziRsH0MfuqyG1D4Km2_PRL3uf0Hl5F4viQ6TvsTrT1cC3tdbwPl4vBNhS5Y5pciVnXYKmAZHgGv2bcCXCFWVLfROF8T5ifupDBod8gVRdXJ2P0AI7ATABkx611cnCm_EDN5hgSuu8rtAt4S5H8WU1WR1m9qq4rThjUehUYQAq_d3zifIyKIG3Xo6n8kA1YaA8p5D9XwdVyHEDOKIA59Z3sH8YPSxhSfD2ppmVInHl6JQ5MeWMXCyFo_J4UZphozS8hx7pwXgB173LMVFCAv_tYuG9PqZ4xC_a2gAm9_DOwIKPQPSKldjdNtZ6e6yoAqP76C5mfFRztmNRLN1xnCNBGN9FxiAacFPg_UHN4BdX64GZfecOGuMcNHhdZMb0Oum4jsT2KYbQA0NZtMrA2HF2HkTKmZfQCHyUkMEoboA4w8mkx6qrM150tMRGHmIqL4pTIi1IbVqSObA3V0HTRBnv3EIAbnzAuCpWozaYe4Xf4NV1J-wcWJ_wm7i7U6UpfqXi-3UOWF3v3tG9EHvwab1_Wuwc0s-5sxuiSdztzTYgzKCcqsI0m6Q1IiyvCmgzAYxPkkkCRGQguVdeVq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی فضای مجازی: شناسایی پایانه‌های استارلینک از اولویت‌های ماست
🔹
فناوری‌های مورد استفاده برای شناسایی و مقابله با استارلینک، به اختلال در جی‌پی‌اس محدود نمی‌شود و فناوری‌های دیگری نیز در این زمینه به کار گرفته شده است.
🔹
هدف از مقابله با استارلینک،…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/468261" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaYqWjIveRSun1OWrawgvwKk5ozYBSedSh2DeJfm0zI0UFXN51FtdhfD5gQ7shM1p2f2KZFa8WtGPwadx6AFtnKI7p7rpT1NlH9FPyowLDcf8OAGYfj93T6OUwTKro8UP5WYczASajrBnGo-0t_6urhSeHbKRpjhO13Gzb2Cz5NUfsP0wnLOZyNQTRxBL_F47IetFG0Wq8e4rv3B9fDmvCdjGB7ChqoAhq7H6C-VkJ5vlDgUFAz5yg2qtFflRLupns8FDAyeazxytcQ1bI8121HfbLS_Hwl0lWBuJATg9XlDVgw8PZaKkm-1YVv5_2ZPyw2eWgf582xKhjSCRJ-e5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم اولین سالگرد سردار علیرضا افشار
🗓
شنبه ۲۵ مهر از ساعت ۱۵ تا ۱۶:۳۰
🔹
میدان جهاد مسجد نور
@Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/468260" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhvwazojONZTzVzn_m-UcoFSg_mz9ezSHXwoQtSefkNMO3dZzdz_NjR26Y2KegGuV7dnKKJ6d9M89MtXWcKSRVuJchc4FA8FrL1CroYCUWfzLhvG0pM6WbnmsAmZQtFaD99-77oEYHaSfQfy8IZmZA-I_rq--C2BMOhAUqN2Kwmpp9PQwWaGK__cVcvBhJN7HZdlDuP2VwisgtM1XRLZuJY3HSFvl9U6LFDCjx_Cfjxh97XYkMYb1bQoTHqUD6GsxY7NiXOh9fOHJ9hRhQ6hCH0T6b0n7sCEhIF9rzz5QENfrbJCYvVuRfCQ_7EzGpRe0RvF2z0dZcmt9bYvr7aV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای نامۀ تکراری منشی ویژه‌ی رهبر شهید
🔹
شهید سعید صاحبدل، منشی ویژه‌ی رهبر شهید انقلاب، در نهم اسفندماه ۱۴۰۴ در محلّ کارش در دفتر رهبری، همراه رهبر شهید انقلاب به شهادت رسید.
🔹
او از دوره‌ی ریاست جمهوری جزو همکاران رهبر شهید انقلاب شده بود و پس از آن به دفتر رهبری آمد. مردی که سال‌ها در سایه‌ی سکوت، امانت و اخلاص خدمت کرد و بی‌آنکه بخواهد نامی از خود به جای بگذارد، الگویی از پایبندی به تکلیف، رازداری و ساده‌زیستی بود.
🔹
خانواده شهید: حاج سعید در جلسه‌ای در دفتر رهبر شهید انقلاب حضور داشت که ایشان وارد اتاق شدند و خطاب به شهید صاحبدل فرمودند: «آمده‌ای همکار ما بشوی؟» حاج سعید، با همان سادگی همیشگی، پاسخ داد که در دفتر ریاست جمهوری مشغول گردآوری اسناد است.
🔹
رهبر انقلاب فرمودند: «اسناد را سایرین هم می‌توانند گردآوری کنند؛ شما به دفتر ما بیا.» این دعوت، تنها جابه‌جاییِ محلّ خدمت نبود؛ بلکه نشانه‌ی اعتمادی بود که به شخصیّت و منش او وجود داشت.
🔹
روزی نامه‌ای را خدمت رهبر شهید انقلاب برد و ایشان فرمودند نامه تکراری است؛ حاج سعید از تکراری بودن نامه خبر نداشت، زیرا نامه‌های محرمانه را نمی‌دید و خود را مجاز نمی‌دانست از محدوده‌ی مسئولیّتش فراتر برود.
🔹
در جریان جنگ ۱۲ ‌روزه نیز از آرامش و اعتماد او روایت‌هایی نقل شده است. در آن روزهای دشوار، هنگامی که برای همۀ مردم امکان فراهم کردن پناهگاه وجود نداشت و رهبر شهید انقلاب نیز به همین دلیل در پناهگاه حضور نیافتند، جمله‌ای بر زبان ایشان جاری شد: «این مملکت، مملکت امام زمان عج است و آسیبی به آن وارد نمی‌شود.» حاج سعید، در چنین فضایی، همچنان همان خادم آرام و وظیفه‌شناس بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/468259" target="_blank">📅 21:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb5ecb019.mp4?token=N25ofN9jAEI4gezla6zVY3vCNEN8DJno5cOSPviHcviy40ITBE7kosv8i0_ZVf5x89iBlvZUllP2idUMPIvrokQrqhrHKxeHgK8X-mU60Srid6eMuyf5gMCPyyzKVzpkdEWZhMJF5xT3K35ebHpAkZoECpTCyxudg5qbnaTRlArffDfyMCk20G9U68RD1ZjMbtnES-owX8MNuXldDnoWtygkP-9rTbW8-OYUDtqas8CdD4h8KyUlUhdMXDcCU7PpewY48Ol_MUBhjAS4vphTw6yluqpxtZMxk7LSGjTz0v-K1xGQF6z9aJ8Efn2M2WR0th9ZepW7f99Egtq-tXK4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb5ecb019.mp4?token=N25ofN9jAEI4gezla6zVY3vCNEN8DJno5cOSPviHcviy40ITBE7kosv8i0_ZVf5x89iBlvZUllP2idUMPIvrokQrqhrHKxeHgK8X-mU60Srid6eMuyf5gMCPyyzKVzpkdEWZhMJF5xT3K35ebHpAkZoECpTCyxudg5qbnaTRlArffDfyMCk20G9U68RD1ZjMbtnES-owX8MNuXldDnoWtygkP-9rTbW8-OYUDtqas8CdD4h8KyUlUhdMXDcCU7PpewY48Ol_MUBhjAS4vphTw6yluqpxtZMxk7LSGjTz0v-K1xGQF6z9aJ8Efn2M2WR0th9ZepW7f99Egtq-tXK4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وکلای جدید تهران سوگند یاد کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/468258" target="_blank">📅 21:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6e15db74.mp4?token=F-WHFddaLkveWJk0aEjdPfFRkwGf59pHZZ5YH412BOPcedwGmt7YYCt6pEwbHfz9Sropxccb4g1WxNENrOwnXZijZAYl-yzN8euXrutntjKzQrC9WTf1SKW2sD4kofTadfEVdn9T5mUeehXqmFayXtfPlp8a66FnJJSsN9cWKOPvUNif_AASOZYSPyPoFI9DnAZ9N3gXcQPL68_ABWlr3blP-ZGEc2629jAjIilDTSitXx-2EJEpg1YTfQWxMlLaUMVJVa1k58EnyaBbsld8E2rDVLTGCTt5CnReGbmoGR-tHqAWF4pHNYX3-APRV43IRh5gvSH1gUKP57HUkkvhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6e15db74.mp4?token=F-WHFddaLkveWJk0aEjdPfFRkwGf59pHZZ5YH412BOPcedwGmt7YYCt6pEwbHfz9Sropxccb4g1WxNENrOwnXZijZAYl-yzN8euXrutntjKzQrC9WTf1SKW2sD4kofTadfEVdn9T5mUeehXqmFayXtfPlp8a66FnJJSsN9cWKOPvUNif_AASOZYSPyPoFI9DnAZ9N3gXcQPL68_ABWlr3blP-ZGEc2629jAjIilDTSitXx-2EJEpg1YTfQWxMlLaUMVJVa1k58EnyaBbsld8E2rDVLTGCTt5CnReGbmoGR-tHqAWF4pHNYX3-APRV43IRh5gvSH1gUKP57HUkkvhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر همسر رهبر انقلاب: آیت‌الله سیدمجتبی خامنه‌ای در خاکسپاری رهبر شهید در حرم امام رضا(ع) حضور داشتند و ایشان در صحت و سلامتی کامل هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/468257" target="_blank">📅 21:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/468256" target="_blank">📅 21:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNL7ghhymSGAR6Tlz94Vl1IrFUgrw50kFPQZ2vsEhetwX1N47Cc0j_jcwb38xuhuW8Vib5L8CTk0BSX1RVHhPOBTTOUcv_XugMsSQXZubvjSnIayeAG1uJWo-D5zHT9rC6CDKm2RrkthACy4WF58o3d-KxqPXAPWwg0pceqDf2FJ419xxao1F4pAVQNN9jzd_phEMyplpYWFYzS487PvfAe8Kqnbb8nAIwbCmEM9unBepjI8AtrRb3w-pQKQGZYreu-SpztuO58OsYZ59_SGN24KyGxSYcfeRCgWbW3b3l_6YFgVp0UJou8Nw9mMPqbceqm19CUMc9z7Fz4Ea-mtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: حضور مردم در میدان در محاسبات دشمن لحاظ می‌شود
🔹
اجتماعات شبانه و حضور مردم در میادین و خیابان‌ها از مصادیق قدرت نرم است و به‌شدت در محاسبات دشمن نیز لحاظ می‌شود.
🔹
این حضور باعث دلگرمی و احساس مسئولیت بیشتر رزمندگان برای انجام درست وظایف خود می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/468255" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4e437586.mp4?token=AXhnaDT5EJyyV2RXtaoFCMrlCDXv2vDH9gHv-osoSD-mc4GWrFwx1wDqfxKuL9Oj3T5ap11yz6Q9gmynDW-GXzk9HkVcPyQglkU7LXNXx2D-dKwec6HN1M72i5ByoRiRW0ezJQG7FAw-Rr7CoufpLGJ0zYUhuuSiLYSgyuOMWTnXSfQGLMsueCp2K3zgTUa0mwRfcPUqP1RzDDwcs9jXt6t_Yjx5w8azthg7scDSS0NjedjZbIrW_LSltfzZ2UjkNw2uKeL0POhZDixSXG_0KM1pdFBxia0TGORSLhFLtjri6blK1oNCgUpXr4RrP3fuEtEiCOLe2ULVPy8iitjS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4e437586.mp4?token=AXhnaDT5EJyyV2RXtaoFCMrlCDXv2vDH9gHv-osoSD-mc4GWrFwx1wDqfxKuL9Oj3T5ap11yz6Q9gmynDW-GXzk9HkVcPyQglkU7LXNXx2D-dKwec6HN1M72i5ByoRiRW0ezJQG7FAw-Rr7CoufpLGJ0zYUhuuSiLYSgyuOMWTnXSfQGLMsueCp2K3zgTUa0mwRfcPUqP1RzDDwcs9jXt6t_Yjx5w8azthg7scDSS0NjedjZbIrW_LSltfzZ2UjkNw2uKeL0POhZDixSXG_0KM1pdFBxia0TGORSLhFLtjri6blK1oNCgUpXr4RrP3fuEtEiCOLe2ULVPy8iitjS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض کاربران به ملوانان آمریکایی؛ چرا کودکان را می‌کشید؟
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/468254" target="_blank">📅 21:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📷
هشدار تخلیۀ یمن برای ۳ نقطۀ عربستان  @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/468253" target="_blank">📅 21:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYZVAI6KR0nocAJwVWg1CAXx5c3KQVfTExquyp_EMU4Fs3csVRlFu03McytoHp1cwSzJRrNbVF4FklFMV-ViABlhKspgoIEju5eRvBxHxp0UZA1m5-H6iZ05YicuQsMBQzYC9jeC6bAwLftjFjhLz-s6ljhNEoPFVUe1ZBQSoSDnXE9yWZ3gpy7-Y1-euy5oRtK_qG5zX8D9_xTyX6msuPGIoS7AcpfsGiUOPjazP5eR0dMUHHcg_NY-nGbtcY5oI9B99nRKH_-dlyC5lIzZx69ffUsqNIaMSLrehnhMgOfZK9k9cwC_pTQAad9H3zFemQha1QcYfqvVrYpCLg2DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/468252" target="_blank">📅 21:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
توپخانۀ ارتش اشغالگر اسرائیل شهرهای المنصوری، بیت یاحون در صور و شهر بنت‌جبیل را بمباران کرد.
🔹
ساعتی قبل نیز زوطر شرقی و میفدون هدف حملات صهیونیستی قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/468251" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بقائی: عملیات‌های پرچم دروغین جنایت‌های آمریکا و اسرائیل را نمی‌پوشاند
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی درباره تاریخچه عملیات‌های پرچم دروغین آمریکا و رژیم صهیونیستی در ۷ دهۀ گذشته نوشت: پرچم‌ دروغین، شگردی دیرینه‌ است: اول صحنه‌سازی کن، سپس انگشت اتهام…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/468250" target="_blank">📅 21:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468248">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14358db62.mp4?token=suwtdIVoG8gje59FKJZ8aBDteGXXngnVkfp2ZZk5u2XS14ucaYtz1du6dNlev7LtjwGgxGou4YMPOziVzAsqle4JayaI4jtuiK6r0kiDwWoci7s83_V4_7KCNZ-ZBs8HNG2rz4hMKuT0oxDiAZIa4sCRouZlRNVLBtOBeb1v5afVg-Xh3NnN98s6h6wtPCd2e1EssdRNLGU3YmkS_cauqgLdAOD0c3S8gLk3GOkSDGZLqm1Ovhaa4_bVpAjgF0GYSQqBeML-DXV8jhPyK-dbjyYW8p03Ob8pBcsr90hNKBKnffZRfd1EwyxxUQcLQe1Ow9rupj-JChMIOyhbfWhYLwqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14358db62.mp4?token=suwtdIVoG8gje59FKJZ8aBDteGXXngnVkfp2ZZk5u2XS14ucaYtz1du6dNlev7LtjwGgxGou4YMPOziVzAsqle4JayaI4jtuiK6r0kiDwWoci7s83_V4_7KCNZ-ZBs8HNG2rz4hMKuT0oxDiAZIa4sCRouZlRNVLBtOBeb1v5afVg-Xh3NnN98s6h6wtPCd2e1EssdRNLGU3YmkS_cauqgLdAOD0c3S8gLk3GOkSDGZLqm1Ovhaa4_bVpAjgF0GYSQqBeML-DXV8jhPyK-dbjyYW8p03Ob8pBcsr90hNKBKnffZRfd1EwyxxUQcLQe1Ow9rupj-JChMIOyhbfWhYLwqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: امروز آمریکا  با ۷ ناوگان خود به قاچاقچی سوخت تبدیل شده
🔹
ناو ۱۳ میلیارد دلاری آمریکا بی‌خاصیت شده و ۷۰۰ کیلومتر از تنگۀ هرمز فاصله گرفته زیرا جرئت ندارد به تنگۀ هرمز نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/468248" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468247">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5895cf7046.mp4?token=KQkiiRPboP4gtL9eoKxyeixpE0_5JRry66tr1MawF4Ozo0xzBpaH1BVruMJmHWFndZBkbjDmBVQQRzXahu64w8bbmoh_DXJ18YW2cnhJxuB48ghHpDSGy9zdFd4qJIZ_FCV14_oSITDoaltRt2GNh7EBOW9LFjtI9ZfMdrHUxCL6Fuml_B1NKKsZS8Ar0IM7qwtqOcJj9cuGf-uoSB85vkqlHNhcSJoYeG6A36HHY1ZhMSfEbOZlLbFi3vn0pkl7WZ2BHD8jYuFax8_BYDY4gne94zWvBj2tgcnxfMzJ7DwelQkCoeYXKSBCVrEscz4e6NSQNhhNEAwNDxbvZe5n9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5895cf7046.mp4?token=KQkiiRPboP4gtL9eoKxyeixpE0_5JRry66tr1MawF4Ozo0xzBpaH1BVruMJmHWFndZBkbjDmBVQQRzXahu64w8bbmoh_DXJ18YW2cnhJxuB48ghHpDSGy9zdFd4qJIZ_FCV14_oSITDoaltRt2GNh7EBOW9LFjtI9ZfMdrHUxCL6Fuml_B1NKKsZS8Ar0IM7qwtqOcJj9cuGf-uoSB85vkqlHNhcSJoYeG6A36HHY1ZhMSfEbOZlLbFi3vn0pkl7WZ2BHD8jYuFax8_BYDY4gne94zWvBj2tgcnxfMzJ7DwelQkCoeYXKSBCVrEscz4e6NSQNhhNEAwNDxbvZe5n9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخلاقی، وزیر پیشنهادی دفاع: برنامهٔ دفاعی شهید نصیرزاده را با قدرت ادامه خواهیم داد
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/468247" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468246">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12ce974bc.mp4?token=Vf8NSgy82fYKKD2WQ8RLdo8UMjTztHz0KSJT0z43RSaBUlLssAcHrxnrstWzXnFQsW5dJOF04Zi1ST176Inb-dPsVumzS-KjoiNiGEkFcML6BFQ5N3I30wMZd7kwin-jWy33IoB51nik7W237bKukhl-Jb6K85MjHk5W3DFmMZtZKmHS-VJzXcEXTGQ1FeoEL5lJHC7MQ91ququAvegABF4Rsyy0XjJa36Y9hnj3AuSdgW8LbZUAV7uwBGYHtLgbum97NI-XU9xXwcBnFPUUFJQLt4KtBXbi3KKmtWee9_Lp8lUyFaL3MxoTEliTU2ZQmVK_w6j1DoimEtViAdf0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12ce974bc.mp4?token=Vf8NSgy82fYKKD2WQ8RLdo8UMjTztHz0KSJT0z43RSaBUlLssAcHrxnrstWzXnFQsW5dJOF04Zi1ST176Inb-dPsVumzS-KjoiNiGEkFcML6BFQ5N3I30wMZd7kwin-jWy33IoB51nik7W237bKukhl-Jb6K85MjHk5W3DFmMZtZKmHS-VJzXcEXTGQ1FeoEL5lJHC7MQ91ququAvegABF4Rsyy0XjJa36Y9hnj3AuSdgW8LbZUAV7uwBGYHtLgbum97NI-XU9xXwcBnFPUUFJQLt4KtBXbi3KKmtWee9_Lp8lUyFaL3MxoTEliTU2ZQmVK_w6j1DoimEtViAdf0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: امروز آمریکا  با ۷ ناوگان خود به قاچاقچی سوخت تبدیل شده
🔹
ناو ۱۳ میلیارد دلاری آمریکا بی‌خاصیت شده و ۷۰۰ کیلومتر از تنگۀ هرمز فاصله گرفته زیرا جرئت ندارد به تنگۀ هرمز نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/468246" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468245">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826bbca047.mp4?token=K516ynEN4ndcgAAYaLt34Sm7AFppz6vNzD-Mbwzc9L7XlQsMBSXsTzP2Xdg0yCXW8ROas4zw3eo5qioaROIFrcBqeUz9Azd7fVrQiInmdoBiFUNJnNNtpCohSwoO7QsMpDrohs04Mg54d54P6xY0fuypZ4rJuzComl1Y49mh94gSnN-qKj5dQxAvvi3VctLjAU5Ix0nApV5WOGcW9mgrC1lGrOKcF797FNi9KDuzEoo8eD_r103LsD5FlBn45j3xxJImDGxPXoPBrU0K16QZWNe_oA886Azh72tMm9EcP23uXTpR6cr0tVevxV6AfPC_FeOa3Oq_W5wO2-5kWqYjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826bbca047.mp4?token=K516ynEN4ndcgAAYaLt34Sm7AFppz6vNzD-Mbwzc9L7XlQsMBSXsTzP2Xdg0yCXW8ROas4zw3eo5qioaROIFrcBqeUz9Azd7fVrQiInmdoBiFUNJnNNtpCohSwoO7QsMpDrohs04Mg54d54P6xY0fuypZ4rJuzComl1Y49mh94gSnN-qKj5dQxAvvi3VctLjAU5Ix0nApV5WOGcW9mgrC1lGrOKcF797FNi9KDuzEoo8eD_r103LsD5FlBn45j3xxJImDGxPXoPBrU0K16QZWNe_oA886Azh72tMm9EcP23uXTpR6cr0tVevxV6AfPC_FeOa3Oq_W5wO2-5kWqYjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: نقاط ضعف تاکتیکی‌مان را تبدیل به نقاط قوت کرده‌ایم
🔹
اگر آمریکایی‌ها می‌خواهند ببینند تنگۀ هرمز باز است یا بسته وارد میدان شوند تا ببینند چه کسی آن را کنترل می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/468245" target="_blank">📅 20:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468244">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئیس شورای‌عالی سیاسی یمن: پایان محاصرۀ ۱۲ ساله هدف ما از جنگ با عربستان است
🔹
المشاط: هدف نبرد امروز، پایان‌دادن به تجاوز و محاصرۀ سعودی است که از ۱۲ سال پیش آغاز شده تا به نقطۀ بازگرداندن ثروت‌های ملی و بیرون‌راندن تمام متجاوزان از سرزمین‌مان برسیم.
🔹
خطاب…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/468244" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468243">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06655cbfbf.mp4?token=EDKs-W4jWkqO9bVqiDkFgMM2pUFxxglGXlAkWBZ-CIPci8kWFGcSQEwsh4i3SRksEOD9jt2z2x67RzoTg8jDW95zmPtLJItpycHlzErVFbEx_-67lTNIuF9UbJ8WtBjOxSIy5ww7x4PXLwoyPJBwkx0ld1o2nHZjBt0uzx-IjisTYYA1gjLGDRJRwxZlJ1F7v5N6tIBUOGwgozHGdnXqsTOIt6B3N5wrZz4BTN2Br2vD6XXGOEfgYd96j2kol3FRZKFKQkUu60QWd27hwNdcK5VURATpO5Udt-Dj5PR8EKYcASlZ45VK-HNcPY3SCmGUVkfplJEQeFw08siax3lfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06655cbfbf.mp4?token=EDKs-W4jWkqO9bVqiDkFgMM2pUFxxglGXlAkWBZ-CIPci8kWFGcSQEwsh4i3SRksEOD9jt2z2x67RzoTg8jDW95zmPtLJItpycHlzErVFbEx_-67lTNIuF9UbJ8WtBjOxSIy5ww7x4PXLwoyPJBwkx0ld1o2nHZjBt0uzx-IjisTYYA1gjLGDRJRwxZlJ1F7v5N6tIBUOGwgozHGdnXqsTOIt6B3N5wrZz4BTN2Br2vD6XXGOEfgYd96j2kol3FRZKFKQkUu60QWd27hwNdcK5VURATpO5Udt-Dj5PR8EKYcASlZ45VK-HNcPY3SCmGUVkfplJEQeFw08siax3lfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: نقاط ضعف تاکتیکی‌مان را تبدیل به نقاط قوت کرده‌ایم
🔹
اگر آمریکایی‌ها می‌خواهند ببینند تنگۀ هرمز باز است یا بسته وارد میدان شوند تا ببینند چه کسی آن را کنترل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/468243" target="_blank">📅 20:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468242">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3928d27be5.mp4?token=TO6umVw0x9eZF8LUTiiVEYMFB1aGOwxXK7RIrXLqYw0KPgJA7oTmAwuQQsOvXeOrxsj624D-0d0Cp_a9TRQ8aIye4KPp02YG4gK1-24YXSFbUqKCs8pW1rbT1i0l6_GKDFndQc6IIacAxd54ujJIVbnWz62qNF0_Cy7MdzE3UyN9qywF6TEfxX8BxG45LmSqUrmiObLwki8zBiAnOPJr12hryBURk10-FwvcKuk_QiJuOgZFRtNBVZQ6ASkRI5Mwlp3hEfkieQHzf8I-oOZ4r9XXwda1un--V_MeZLOIgXmnOB3UqrZ-gxOoqMZ3IBe6QvnqXS1bvAn1_7e8fWA3HzOGfZw5V3VcMVs77i9C__Cj-pzwX0HuVXDyUPXhJMe788CF74VuDBtcCYMGwIqZTvnBRO3i58KN784FNAKXuI5DM4Dti_vLf0Ao85kKEmc6VGGvXvsbGTwTRc0Ervv6nh4xiOwDYhOfQ1THdvEvfZk2B7jPT7LP0lg3WGZtdalJC6cJSMkbc0asvZfo3QOkDXy3O0CwAXg37NborpQC8apH78fBETzblznqREgKN02IpxFPl633MXSQtG0A-I4s_5oDACjS6Cm5MmaQBOTTk8ddfVQHU9kcLiTsBepptnWQLpeyPY3F6fpj2dgNvrEqKr6IcRsxxBLfNMmwDZGc_uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3928d27be5.mp4?token=TO6umVw0x9eZF8LUTiiVEYMFB1aGOwxXK7RIrXLqYw0KPgJA7oTmAwuQQsOvXeOrxsj624D-0d0Cp_a9TRQ8aIye4KPp02YG4gK1-24YXSFbUqKCs8pW1rbT1i0l6_GKDFndQc6IIacAxd54ujJIVbnWz62qNF0_Cy7MdzE3UyN9qywF6TEfxX8BxG45LmSqUrmiObLwki8zBiAnOPJr12hryBURk10-FwvcKuk_QiJuOgZFRtNBVZQ6ASkRI5Mwlp3hEfkieQHzf8I-oOZ4r9XXwda1un--V_MeZLOIgXmnOB3UqrZ-gxOoqMZ3IBe6QvnqXS1bvAn1_7e8fWA3HzOGfZw5V3VcMVs77i9C__Cj-pzwX0HuVXDyUPXhJMe788CF74VuDBtcCYMGwIqZTvnBRO3i58KN784FNAKXuI5DM4Dti_vLf0Ao85kKEmc6VGGvXvsbGTwTRc0Ervv6nh4xiOwDYhOfQ1THdvEvfZk2B7jPT7LP0lg3WGZtdalJC6cJSMkbc0asvZfo3QOkDXy3O0CwAXg37NborpQC8apH78fBETzblznqREgKN02IpxFPl633MXSQtG0A-I4s_5oDACjS6Cm5MmaQBOTTk8ddfVQHU9kcLiTsBepptnWQLpeyPY3F6fpj2dgNvrEqKr6IcRsxxBLfNMmwDZGc_uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروسیِ متفاوتی که قصه‌اش از پشت دیوار دانشگاه کلید خورد
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/468242" target="_blank">📅 20:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دولت روش جدید شناخت پردرآمدها را تصویب کرد
🔹
هیئت وزیران در مصوبه‌ای با عنوان «شیوه‌نامه شناسایی و گروه‌بندی اقتصادی خانوارها»، سازوکار شناسایی وضعیت اقتصادی خانوارهای ایرانی را تعیین کرد.
🔹
براساس این مصوبه اطلاعاتی مانند درآمد، املاک، خودرو، دارایی‌های بورسی، تسهیلات بانکی، مصرف انرژی و وضعیت اقامت افراد در خارج از کشور، برای گروه‌بندی اقتصادی خانوارها مورد استفاده قرار می‌گیرد.
🔹
طبق این مصوبه خانوارهای کشور براساس مجموع درآمدها و مشخصات اقتصادی و اجتماعی، در ۳ گروه اقتصادی بالا، متوسط و پایین قرار بگیرند.
🖼
اما افراد چگونه می‌توانند به اطلاعات اقتصادی خود اعتراض کنند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/468240" target="_blank">📅 20:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSn8xa4EC57f76OqjykQE4L-W64nmPmBzJVo144IqLQdMVu1OO5zpAN6UshqyZEqfw9eFxIDyl3808plB_KQJ81zOCnsk7Auqe1F4AOnQhDzf0GKFDGUvxu101pIeyDGX_HvImIKqRKz7jdVYityVC9noZAzyNaxehCGuug2chviXtfK5V-ewNIo6kGcKpitror9LOHny7Y6WMhqn0xguJjlNS3pKriHt21Aerem4yZ3M43C9DJVjh0DkC91017JWnpW3icmJxgqAoQTvrGXX2Fp7Ru5V9Zcx3TAnyM8V8Y0S_e4d6Y6nWRTHOGRH8wkgTqxTEz8NmlROr7uV3PqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس شورای‌عالی سیاسی یمن: پایان محاصرۀ ۱۲ ساله هدف ما از جنگ با عربستان است
🔹
المشاط: هدف نبرد امروز، پایان‌دادن به تجاوز و محاصرۀ سعودی است که از ۱۲ سال پیش آغاز شده تا به نقطۀ بازگرداندن ثروت‌های ملی و بیرون‌راندن تمام متجاوزان از سرزمین‌مان برسیم.
🔹
خطاب به عربستان می‌گویم: عاقل کشوری است که در تجاوز به یمن دخیل بوده، اما قبل از اینکه خیلی دیر شود، از جنگ خارج شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/468239" target="_blank">📅 20:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2114dbac.mp4?token=klLEo3lcQxkIzyzksVxh0VgXMMo8wr_eRkbAECwXr5HJaceaU-yCJ-FNx90OlX54Rf9RmvNNqo9j30rivhUBw7VtL_h4gLVo1QTLMSIqVJeLL1hKgop7YoZAP_LZCy-bf75I6N3VFJ4qKC4sLo32Osnd5Y7AENaMAwMeZ3hgofjaS881g11PDdi9fVzhJ0FD1k-oXkgMM6sJ0wztfHwgHvWCfvdrvtv9aC1O11JZ--4pLt-Y1qZadwErr_d3vuU5arzexBhgPbmzl59aC9SVHPfRzltW4OY9pUk6grrP2wiR52CunceEu5PhxtMPH9vnsd_4oPDh82U0RIQJuADV3J1BkIQzvjz_4-bEhaSiLSJMhO2qD_YEGM3d0hgRLQff9QM4PlXxF4pPz9vGzjgWsNdY-8oYNaf4oH2xTcFnvbiQ79kwMAC7d91NveHxF3LN0DlNYkKw0XBP2Icn4aCWxYsyo7mgcGv3cPmDpNZ4V3dykCr7pumoFYohMt4jCZVDXv3h3n2Fnb1m7YTCDDypm4FkKvJBilYO5cb8P4YUm2wDlgG_0zN45qa1L_BVvVL-uXW35MvW3wBr7jZw8GvikWG5SE8gcA6FidmWhFUN17L6c8jIpv7BGifpqh0KlKF48KYtMf-dnuI0ObeiPzllIiVLW91ZpHn3mSogjQUOSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2114dbac.mp4?token=klLEo3lcQxkIzyzksVxh0VgXMMo8wr_eRkbAECwXr5HJaceaU-yCJ-FNx90OlX54Rf9RmvNNqo9j30rivhUBw7VtL_h4gLVo1QTLMSIqVJeLL1hKgop7YoZAP_LZCy-bf75I6N3VFJ4qKC4sLo32Osnd5Y7AENaMAwMeZ3hgofjaS881g11PDdi9fVzhJ0FD1k-oXkgMM6sJ0wztfHwgHvWCfvdrvtv9aC1O11JZ--4pLt-Y1qZadwErr_d3vuU5arzexBhgPbmzl59aC9SVHPfRzltW4OY9pUk6grrP2wiR52CunceEu5PhxtMPH9vnsd_4oPDh82U0RIQJuADV3J1BkIQzvjz_4-bEhaSiLSJMhO2qD_YEGM3d0hgRLQff9QM4PlXxF4pPz9vGzjgWsNdY-8oYNaf4oH2xTcFnvbiQ79kwMAC7d91NveHxF3LN0DlNYkKw0XBP2Icn4aCWxYsyo7mgcGv3cPmDpNZ4V3dykCr7pumoFYohMt4jCZVDXv3h3n2Fnb1m7YTCDDypm4FkKvJBilYO5cb8P4YUm2wDlgG_0zN45qa1L_BVvVL-uXW35MvW3wBr7jZw8GvikWG5SE8gcA6FidmWhFUN17L6c8jIpv7BGifpqh0KlKF48KYtMf-dnuI0ObeiPzllIiVLW91ZpHn3mSogjQUOSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران با حضور و ایستادگی، روح مقاومت را زنده نگه داشتند
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/468238" target="_blank">📅 20:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5CvDGzXGwcWwYb3VIlnzyAllkwDSaWXj-jPVg_Knb5fuSZkFswAKUGloi6_MJETWGNdLVHAHKqJWotpGlWbdz3zEky8uWMF6s2FQeG_xUPVSQIsMIZH9hwxTZBpxjSCXAYGGvLDMLT5BRhnY8JMWYrTr1rhhTQFD14iNJ86dQN4cus9KNe8jk4oB93bbWsrUsr8kIacybf5xI-rmr_P75ArcCbSc5YfubB0f_0W32eHgn2dGP347kdfWP-Ei3sGXp1GO337fkR-TwFN7MgBqfdGG_ANiQXh2G9oKqAyXFLdwrz3ApvKNa0yWPZ1Zik2v91Q0buM2B-Yg9e_EFcGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/468237" target="_blank">📅 20:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn4u6Be2OSLApoIrIquuaB-so1eD98tSYA89FMPBBXyENWUgRzMimwVB7gdQutIWFpUs48Eo2Rjfr2MZgT_HLvl_mwQ992y_9aWnEac0ZRTYoJsVuITZBQD6YdUOZ7gJA1XUq-gyCXHBTp6QZpKKMoI3NP7WQWqjE5RTHZCgNcF1iHck3zEIKJ8sjX4Wrdfvk12KR77ifmVqZuDeFcwL-xBKJQg2SrZHnMENLB_qagOZxrtnvy17JwdntfVs_u2grvL03DgDXGy7FFNJDCaDVXgoEIjKi_rbhxtmxRsvEqEWhraU5KCZtyK1H_9t9RZZ9g1AUDIQ-tUMIFhSyLx9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
توییت فرمانده نیروی زمینی سپاه خطاب به دشمن: ما منتظریم!
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/468236" target="_blank">📅 20:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a524a3bf0.mp4?token=PjKiC6i83p9IOWHrorMiidRMMz3NgpBAQOSGvXHAPuMPLUg6eYcEDW9DAHLEyGdIYInzvhN558gp_qH5qytkpfTyFN9v7oS8YEPCHj7rYFW9RJx1HaC7dXmgWNJr8Ew4QiQMi1XejuOtXHQIS_S8iTkYpALTEgeDyyjhKk6RZCkkmiqhu_LOo5Hs8sza25K4E2wxZ9CSduFs1KVbhGvQyzolR5b4H8FMOIaHXFFiujxeuvmpEm1NZVdeUBB52hG2o_TzQXALpg9AXGtq0CFN-Uy9qC-f1OxKxIdJfhRSbsKkLPOPJecVuZZ7Hu4IaRlii2Jatxi8WEvSBQLBeFC9mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a524a3bf0.mp4?token=PjKiC6i83p9IOWHrorMiidRMMz3NgpBAQOSGvXHAPuMPLUg6eYcEDW9DAHLEyGdIYInzvhN558gp_qH5qytkpfTyFN9v7oS8YEPCHj7rYFW9RJx1HaC7dXmgWNJr8Ew4QiQMi1XejuOtXHQIS_S8iTkYpALTEgeDyyjhKk6RZCkkmiqhu_LOo5Hs8sza25K4E2wxZ9CSduFs1KVbhGvQyzolR5b4H8FMOIaHXFFiujxeuvmpEm1NZVdeUBB52hG2o_TzQXALpg9AXGtq0CFN-Uy9qC-f1OxKxIdJfhRSbsKkLPOPJecVuZZ7Hu4IaRlii2Jatxi8WEvSBQLBeFC9mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: سفرای برخی کشورهای خلیج‌فارس از ما برای حمله به پایگاه‌های آمریکا در منطقه تشکر می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/468235" target="_blank">📅 20:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNgObpl57mVSyhcahJWuNjz4lUq3B7aPJrbBxxsXDwr22fi7aWDewLY4mBcxSrH1Lx49dxTHTk5AzvBJPOenmZUxkRyxZx5fSbsW6dZIyo_gcyC1LzFxZQmStAqQPFFtGdbdIKyTO_e85_ZIcl8JLFsRpdxHP6aIRfBstFVFXLJmPiLcxmNTDICNtqtRcfkMrBxnfGv0GA1OartUfmBaEnLBiX5yr4s1W8JpCXBER-gjOzzuUTWNX0oFllCmYQExN4FlleeKvYX4RIUDJJWlLTGHCBLOVcrXwO3ti8gB3huLJPuYwG2L5URlRK985ypsIGsmPehZXJe54a5wPY9CVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقاومت ترامپ در برابر پذیرش واقعیت
🔹
ترامپ که در تلاش است تاثیر بسته‌بودن تنگۀ هرمز بر گرانی بنزین در آمریکا را انکار کند، این‌بار مدعی شد حملات اوکراین به پالایشگاه‌های روسیه عامل اصلی گرانی بنزین آمریکایی‌هاست.
🔹
این فرافکنی درحالی است که کارشناسان اقتصادی…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/468234" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آیت‌الله قربانی امام‌جمعهٔ پیشین رشت درگذشت
🔹
آیت‌الله زین‌العابدین قربانی، امام‌جمعهٔ سابق رشت و نمایندهٔ سابق استان گیلان در مجلس خبرگان رهبری بامداد امروز پس‌از سال‌ها فعالیت در عرصه‌های دینی، فرهنگی، علمی و سیاسی در ۹۳ سالگی دار فانی را وداع گفت.  عکس:…</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/468233" target="_blank">📅 20:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9422bdb92.mp4?token=SaurHBTLrePSmllsrljKnnw2Ub10X6QKTQaB8g2B5yrvPmVoWAdvmGRC8cj6XP9yVmH3C0NGj2bAa3cYdyLf5LKk3SU9EGokwE_eHDKoc5jOz_u9F9PscZDxH0ewLYHttAHqw8w990vY0nuhqRK-HakzmzM0uzvVB5S1UTxazrXLqakAQXQJI8Q0xSFe79A9FMGXjTn2WH-UGFK2_hIZIrCsGGw7Ku__8wCDAP00jtmRc4a2i8Ceh-BdLuqlalpaIm4I_px7kFN7HHDvXZXH7WAuqsInFYlWdTCXSG59cLmpJH8MiO3dCOMqdvGAKOcr85QKBGko-1hhCAdgbU8hFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9422bdb92.mp4?token=SaurHBTLrePSmllsrljKnnw2Ub10X6QKTQaB8g2B5yrvPmVoWAdvmGRC8cj6XP9yVmH3C0NGj2bAa3cYdyLf5LKk3SU9EGokwE_eHDKoc5jOz_u9F9PscZDxH0ewLYHttAHqw8w990vY0nuhqRK-HakzmzM0uzvVB5S1UTxazrXLqakAQXQJI8Q0xSFe79A9FMGXjTn2WH-UGFK2_hIZIrCsGGw7Ku__8wCDAP00jtmRc4a2i8Ceh-BdLuqlalpaIm4I_px7kFN7HHDvXZXH7WAuqsInFYlWdTCXSG59cLmpJH8MiO3dCOMqdvGAKOcr85QKBGko-1hhCAdgbU8hFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/468232" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afd1c67fb.mp4?token=o6RHB-i_s1cT_ZM2h8KLKnaziPcGpZLT7vaAvZC4OAHALDMZnIWB50jBLKxZe8nzsYi-dJtgIhQA1-jXqKiKf9rED_W6wN_1oppmVk5OjLbzIplD3tjeGE5QqG7LuhkT3uy5fY506wri4bqAUgG22JDgim3c73Iet8FP7zs0kklNUHAvRm3jPLQlCmsrNYFUqFqlgaG4gNnInE2aVj9Q6aZxTjFnz0X6GoUFrbD96kwsQ_iYX1EthxzH2w2Z7oxPf99MTIfsb2vUN4r6c24OPrWW3M_xjTigqioUkFp3ox__H7r58XDkGId1ffgCKVsIMLA3XuvB9TwhMJ9GhnGcgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afd1c67fb.mp4?token=o6RHB-i_s1cT_ZM2h8KLKnaziPcGpZLT7vaAvZC4OAHALDMZnIWB50jBLKxZe8nzsYi-dJtgIhQA1-jXqKiKf9rED_W6wN_1oppmVk5OjLbzIplD3tjeGE5QqG7LuhkT3uy5fY506wri4bqAUgG22JDgim3c73Iet8FP7zs0kklNUHAvRm3jPLQlCmsrNYFUqFqlgaG4gNnInE2aVj9Q6aZxTjFnz0X6GoUFrbD96kwsQ_iYX1EthxzH2w2Z7oxPf99MTIfsb2vUN4r6c24OPrWW3M_xjTigqioUkFp3ox__H7r58XDkGId1ffgCKVsIMLA3XuvB9TwhMJ9GhnGcgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/468231" target="_blank">📅 20:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b87dba00.mp4?token=YkrkHMKp-Qe-EMAXX4AAJ3Y-mxOqpErUPxwGO73uS6-5Hx0gXcYirTcdUPVNWurXGyS3RGcqrW_uzsWxIe-20_ObI05xFZjctUkO7w80tSpkvAsmGihcRzTofURHYwFJB4DFryibu_siU2YAGBF0_xtxABtZsqrmKyeDSMaRPi-H7LVBaFQ4NAaIxP_rt7_NlJwQxxuayO-znzAcOLthYX00T5OZ5xBNkbdGttduH5XFAANT8-2FQOYMyCxiNUnJWeyb0jwd4R9c_SGRGTaWG3alPnm9pUiutxNfMZ3EISts3MsnhJ_knqfiHm-th9fu5lL2pRKq0oNp5l5ls_tzHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b87dba00.mp4?token=YkrkHMKp-Qe-EMAXX4AAJ3Y-mxOqpErUPxwGO73uS6-5Hx0gXcYirTcdUPVNWurXGyS3RGcqrW_uzsWxIe-20_ObI05xFZjctUkO7w80tSpkvAsmGihcRzTofURHYwFJB4DFryibu_siU2YAGBF0_xtxABtZsqrmKyeDSMaRPi-H7LVBaFQ4NAaIxP_rt7_NlJwQxxuayO-znzAcOLthYX00T5OZ5xBNkbdGttduH5XFAANT8-2FQOYMyCxiNUnJWeyb0jwd4R9c_SGRGTaWG3alPnm9pUiutxNfMZ3EISts3MsnhJ_knqfiHm-th9fu5lL2pRKq0oNp5l5ls_tzHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه هم مانند ایران گرفتار تحریم و جنگ است اما ...
🔹
روسیه باوجود تحریم و درگیری در جنگ زیرساختی، ارزش پول خود را حفظ کرده و تورمی تک‌رقمی و به مراتب کم‌تر از ایران دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/468230" target="_blank">📅 19:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6504906783.mp4?token=D7K-dOZjjdY9LV5-uS6P9ou458fJ5I9V6bzIUdz0TZb_83UwHntAOysw-0dfS9cmNFYrjLcezaK3pYOJA2vYyUf8x_hXDWK9FOkn5vlR7FKW_blhiIIl6pnNCK-OBqBNjHNENUdm75w45PBT6T8jMFEjsWj_gZQMKSg8Y07XN8QXvwuZogobsTw0kHv3g0uptlnJUBn-tPnTW0gg-fnt6ndYRM_opxrlNjM_Ymyo8-_kbo9qz_yYJKe1ZMRJd-M6_DpqHOkJj-j6ydSheZwLqsK32kMIMZU7QUwC6y_KskATUiXJh8JoWkjLzOkXdsi94WgY6KMKSsuyKb2Exu0g5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6504906783.mp4?token=D7K-dOZjjdY9LV5-uS6P9ou458fJ5I9V6bzIUdz0TZb_83UwHntAOysw-0dfS9cmNFYrjLcezaK3pYOJA2vYyUf8x_hXDWK9FOkn5vlR7FKW_blhiIIl6pnNCK-OBqBNjHNENUdm75w45PBT6T8jMFEjsWj_gZQMKSg8Y07XN8QXvwuZogobsTw0kHv3g0uptlnJUBn-tPnTW0gg-fnt6ndYRM_opxrlNjM_Ymyo8-_kbo9qz_yYJKe1ZMRJd-M6_DpqHOkJj-j6ydSheZwLqsK32kMIMZU7QUwC6y_KskATUiXJh8JoWkjLzOkXdsi94WgY6KMKSsuyKb2Exu0g5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ممکن است از ترکیه بخواهم در پاسخ به اقدامات یمن مشارکت داشته باشد.  @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/468229" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCsh1GJeiMAAxywQCYGRSm_8I42RhaU8QxWLlQx9jVbhu2XbPaGyKqs14MXVf4Y1T_iTz-ZQPpe20Ei_ThI4Sgup7GAt9zrEJoYzwUhGjR8CtiwHG094mXBt0KKP4pW2Jmz7J0I7M88k10YdjQhPRjypkwWKK3lGdiEDARq_4x1e2ws3B_4WcRP5FQpWroGQODy_8lpwvXSZzTmep5sbyFRIYiHhYtnzSKG3DGK67dCnV_iiYzxUrV4QbLFcv9Vwyh1DkACSxCA1f7ILBnqGkyCQ__Rw1KlKRHbkfB03U4P5QuYff8TV2f2m0Y6QWcNZ7LT5RVkjeUrv63pnUo9FQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/468228" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOefgmlPTgaDK9LG4BUFaLGL2LvduYBpf8Jy8sE3dYC1ggtMrNbIwFEACAsiHMZJVzIRww6GW7kKoZ1B6f5-UP9Xasj2oCk9wg9x4l-UCcUHgro_09FHGojqMLojFpIWRCloIZRSf5ZWXaNCK2Y4zvApufFnDgrLOCyrDZPfIEe72yYIbzthHrLUb8t6i1JmZQHs92G54pHD5pdibM1GwZSPP_YzXcnM7z7kSAYpEeRDcHEEHI3fbdMZIqIZ1_6MLh9XStwpQB_WoOnNRgGs2uKhVOkz5LU8ji2L9SRm96D4TqmYcOYVNrcuKjhuwnMgs1EzkHI3xn_zNH0ToXE4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpqDTc3PK8nxrCjyPBRMlidA76F9WsvA-QMC36FvU_3OJiPaNMKMmSWHhVg5Q1BKBoC3E2G2U-EGLlc8AjWbW_8q2NAo6pVpGsjG2Ybn3Xj7H3qlyjWS6Y-gocxi5lW_EiQslRfeYDbALRYS59sRakLohCZT_BIGB-vC0gqmVHlwoveTn95YIi9oNNUWslCDwyunolmUMMcm5Gv4K1UtvBBZ4fSHPlsBlDVKOEj-G3QdEH3GZWV6jK7STX3Xnro191WgSbg0za-hzgxNj3OHw3jV49fmIW_T8GOsiAWoL8y4r_OCW8JXKumozgoZVHUgKPaxboRJrozQq9VfC9Ugkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADXFuinxbi_MuLwu9eFHaFSw14FIjAOZ5cuB9_GVny0jyGVundydSpZ9-1-0IEd2872TIMe46Aep1ZnJnZ178aLinItwnjJR7M6PEYZSu_PTrkbsBY9B7U_26gSc7dNiybyp1lB7ftwQvc7KRY8i5kNVaR0tmaF38nP-x2LW5SIrwlNgI_pq4zWL3us4SisXxxEEWUDkvXfMueqACX6veM7NiwsH4pZRncCT5-3BLAAb7nhoEIp7grl9zuKYeiQ23nj_nOQNi35R6VaOcnsjS4zPOcXfX3Wvcmwu2j0l0DYTsfAO0braC1H6-pILsRlxsWUHU3-ye7QdNG-rXxEfAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ‌ونشر آثار رهبر شهید با خانواده شهید سعادت
🔹
در ادامۀ پویش «اول خانواده شهدا»،  رئیس سازمان تبلیغات اسلامی، به همراه اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب و جمعی از اصحاب و اهالی رسانه، با حضور در منزل شهید محمدعلی سعادت، ضمن ادای احترام به مقام والای این شهید، با خانواده معزز ایشان دیدار و گفت‌وگو کردند.
🔹
شهید سعادت از اهالی رسانه بود که دهم اسفندماه ۱۴۰۴، در مسیر بازگشت از تجمعات مردمی در تهران، بر اثر حمله آمریکایی-صهیونیستی به فیض شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/468225" target="_blank">📅 19:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468223">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b335b37f5.mp4?token=v5pWVPmOBjEB_WpOvSpycr46_mBqFzIA4qT3rzJNPp2xE91UYCzQWVHKm4NmWHqqOPX_amikPHi0vOANFx6w9W7Pjuli8LeUfKVxuxpzH7BFnMLrT70wv9o4ZI52zunwTFRF71IAKAdEPUp9BCB0TWOhvMWDH-13WKdMe0--6H6rVV2eFeGWTH71SWcc46-_3Kz96-0IdNp71m8PaQFfcy7LrKFRJIf46kTnQxrAXgUE8S_DhRhXxVaE0EZdcEIblWCiC3znPpYs1HoUZRgn2NI-1yauEy0_hIiLOIC2FiCKIa6dG5oA70bDb0ML39XtlMPfaax6bykfBOerhL4W0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b335b37f5.mp4?token=v5pWVPmOBjEB_WpOvSpycr46_mBqFzIA4qT3rzJNPp2xE91UYCzQWVHKm4NmWHqqOPX_amikPHi0vOANFx6w9W7Pjuli8LeUfKVxuxpzH7BFnMLrT70wv9o4ZI52zunwTFRF71IAKAdEPUp9BCB0TWOhvMWDH-13WKdMe0--6H6rVV2eFeGWTH71SWcc46-_3Kz96-0IdNp71m8PaQFfcy7LrKFRJIf46kTnQxrAXgUE8S_DhRhXxVaE0EZdcEIblWCiC3znPpYs1HoUZRgn2NI-1yauEy0_hIiLOIC2FiCKIa6dG5oA70bDb0ML39XtlMPfaax6bykfBOerhL4W0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سازمان توسعهٔ تجارت: ۴۰ درصد از افت صادرات دریایی را جبران کردیم
🔹
در سال ۱۴۰۴ واردات ۴۲ و صادرات ۱۵۵ میلیون تن بود که ۷۵ درصد صادرات از خلیج فارس و دریای عمان انجام شد.
🔹
پس از محاصرهٔ دریایی، انتظار کاهش ۷۵ درصدی می‌رفت، اما آمار ۶ ماهه کاهش ۳۵ درصدی را نشان می‌دهد و ۴۰ درصد از حجم دریایی جبران شد.
🔹
پیش‌بینی می‌شود در نیمهٔ دوم سال با اصلاح رویه‌ها، صادرات افزایش یابد.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/468223" target="_blank">📅 19:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468222">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c7998c96.mp4?token=bbXH_Mon-ALWEZJnic8OTmOYe0ijyMJMUrppfz19wL-QQU3BA4JqYoo9uj9RuKzuUWOjbBR9CzIn0a_ymmdwjQiTqfUfrrQ7zlCeFlSMKpSgnouDjn3SIBJtrJhlzgP8sQVM7PJRshlHx3fcDLg4qfT1gYM-Nzx2Vviaq1PeaM8l3HZ_zg5DBNGOOX9jv-Xu10lmyhVhfEiQlJ95QJt3k0HpyZ2PUe-lecYLwQzLys4vPAPbUFmC5QKBd1EmA4TAsIlwvti_TEemy1vHGynIyzEMssqGllVqj6B0V7gmkgbRvBT8WZOfqmMB7Y565YrLajGRp8pKITUv6hMaS18YjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c7998c96.mp4?token=bbXH_Mon-ALWEZJnic8OTmOYe0ijyMJMUrppfz19wL-QQU3BA4JqYoo9uj9RuKzuUWOjbBR9CzIn0a_ymmdwjQiTqfUfrrQ7zlCeFlSMKpSgnouDjn3SIBJtrJhlzgP8sQVM7PJRshlHx3fcDLg4qfT1gYM-Nzx2Vviaq1PeaM8l3HZ_zg5DBNGOOX9jv-Xu10lmyhVhfEiQlJ95QJt3k0HpyZ2PUe-lecYLwQzLys4vPAPbUFmC5QKBd1EmA4TAsIlwvti_TEemy1vHGynIyzEMssqGllVqj6B0V7gmkgbRvBT8WZOfqmMB7Y565YrLajGRp8pKITUv6hMaS18YjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سناتور آمریکایی به ترامپ دربارهٔ ورود به جنگ علیه یمن
🔹
کریس مورفی سناتور دموکرات آمریکا پس از سفر به قطر و عربستان، با انتقاد از نحوهٔ مدیریت ترامپ در جنگ علیه ایران تاکید کرد ورود واشنگتن به جنگ با یمن، شرایط منطقه را خطرناک‌تر خواهد کرد.
🔹
او گفت…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/468222" target="_blank">📅 19:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468221">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU1WvMbOz-REdFOyVE1ZLW_yC8xJRFIMIQEyjxDkqapHOQvwMdszFWeFY3Xuz6sDnXVM5GpSmv7LNxed7Ode3CKCLi3FQKM_zI_NKpvVHUM4Q5egiDxGjBB0hAfMlRcl6wxgnQoWjcdgVgGY44509hzj3DrwbwThlpXLL_brSYmb-YSfz60rdPKV-z9TusrXkHrk_4_nFX9OAFKzQfwzvXCzTTNn1KdhVpehxGkOeYkn2douvkhCDhPvBZt8ZNRdbtvpMxB5WvcU3mBoC69GqPPL2HbSFjYIettepLhQMcMcwjORy3EkhyHnUZTXwprGI5b0VBi1qPTjiX9QwoCmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف شقایق نوروزی: کمی دیگر مانده تا رضا پهلوی گوی سبقت را از منفورترین مزدوران تاریخ برباید
🔹
«باید اعتراف کنم که ما تو را دست‌کم گرفتیم، قیافه احمقت را نگاه کردیم و با خود گفتیم این مگر چقدر می‌تواند در مزدوری از بالانس زدن در یوگا بهتر باشد؟» این بخشی از اظهارات تازه شقایق نوروزی، فعال ‌رسانه‌ای و بازیگر خارج‌نشین دربارۀ رضا پهلوی است.
🔹
او که این اظهارات را در واکنش به ناراحتی رضا پهلوی در قبال آسیب دیدن یک فرودگاه در عربستان بر زبان می‌راند، تصریح کرده که پهلوی‌چی‌ها تبلیغات‌چیِ هدف قرار گرفتن بیش از ۹۰ زیرساخت حیاتی کشور در جنگ اخیر بودند و فقط کمی دیگر مانده است که رضا پهلوی گوی سبقت را از منفورترین مزدوران تاریخ برباید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/468221" target="_blank">📅 19:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468220">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a947198ba.mp4?token=kvw3Dc_YwB_UpzsN5en74Ye6RqZYXyhp-5_ezd4atWYh-S9Ibz5aZzDqcS4FTOyjsJhi6BdcBgdKLzbBOPAs-PMlIPiT75AKrxZccFMW91IYUXjCq32fvLWhjQAMBfGWeondVotS0Jzd0iZKQyNCHvBQE5RJZmpp0OS7BrYA5DNaEeUtFkmiK5kkwKAvqD3t2AY0FlE2TNHDTkr0cB1t-TcibHRswpVoqP3AHDPl7o2XnH_GCKIkLmqFi-QqjKgPqDPmLbcMcGOo4Y3NfIDT0GQopeiA2BdhJEp-GUdz6FjLAG8F3dHFa-jAJDtbakwft1wvnUMwAb7KT37jCQ8N6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a947198ba.mp4?token=kvw3Dc_YwB_UpzsN5en74Ye6RqZYXyhp-5_ezd4atWYh-S9Ibz5aZzDqcS4FTOyjsJhi6BdcBgdKLzbBOPAs-PMlIPiT75AKrxZccFMW91IYUXjCq32fvLWhjQAMBfGWeondVotS0Jzd0iZKQyNCHvBQE5RJZmpp0OS7BrYA5DNaEeUtFkmiK5kkwKAvqD3t2AY0FlE2TNHDTkr0cB1t-TcibHRswpVoqP3AHDPl7o2XnH_GCKIkLmqFi-QqjKgPqDPmLbcMcGOo4Y3NfIDT0GQopeiA2BdhJEp-GUdz6FjLAG8F3dHFa-jAJDtbakwft1wvnUMwAb7KT37jCQ8N6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترفند صهیونیست‌ها برای ایجاد بدبینی نسبت به مسئولان
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/468220" target="_blank">📅 19:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468219">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS81_RFuu8jBMLWeXKiI-dTRxrucHZfe4_Szr4fh05ZjyDOWAf5Pbe_ySG3ktD_UcPnKvoR-RVELpR09NM8AsPJxY0o8l19s-s8R4MsC147zMeLFjtlISkdh2YSE5HoGgoN27NKkyFmkR74X8QIZltz9RmYKWmpzDRJKqq1BrUGMCR_06gid81oCGRAHTbdm5q63h1BJE6H1odijKivkLgGgWQw4MKx_CE84JAq6PNMsAGpxCtDZcgsCnwpBfJVxT5-26__vsO0u42_eqwMjgew8RRC5E6D5pBsN_2P6f4l79_lqDwgMc-n9EHzNXTqrV1ZPEUfcaWiaaywQTuh6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال برکناری هگزث توسط ترامپ
🔹
«دومینیک میشائیل تریپی» نویسنده و تحلیلگر سیاسی غربی طی پیامی در شبکه اجتماعی ایکس مدعی شد که ترامپ در پی برکناری «پیت هگزث» وزیر جنگ آمریکاست.
🔹
وی در این پیام نوشت: گفته می‌شود که ترامپ در نظر دارد پس از انتخابات میان دوره کنگره، پیت هگزث، وزیر جنگ را بر کنار کند تا با انداختن تقصیر جنگ نامحبوب ایران به گردن او، میراث و شهرت خود به عنوان «رئیس‌جمهوری ضد جنگ» را حفظ کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/468219" target="_blank">📅 18:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468212">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjh913RTC8_O8a7mCclpKzfyfHtCQ1QFdqhcsZlX6o2_hoOLkDbNU35YRKC-eQBm28Yjf6oglM6b8brFY70KmGNXMUj0W_WFc8Bh4yJ1K5MDe5j-gez0TWfg0HVsNqtfNE49_HsbdLxBz0bgbZB44Hn8FDYZGzWglMb_hsU4pWg--9bIuWksBe7FN1xd1L6jkvYuQ3nyVDupAyc8HAVewYU3WO4km0C6hZX0CL_STAPrR_J5jeAZ_VASks2OpzGTbV9KYSbM9H72ff8I3uiqwav-jf5CuVCA8q7HcsSX5LGAwFsH9dadjm9DMThsjZbJlgDCySpy0ALMSKY_P2e2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBCgsFOq5BP51K6inLMg-68Xqt-DaxPLmrXt9oGraKfmtu3emSoHq_YB82g9CQfh4zBOOuZYhmUx73QpjzGAmV-Qf8GLhmmarJyU8hfoLQBiI4ewwo64Gi51Db20bwnvt9CrOV2Q6TducSoOC6qc_48fjtnpT3FefkozCUy4oMrLVIVztwwn-PvDZ5swkXj2WUI09GbzJ6UlsKU0FM873nbGsEQbnZG9M5B4pROnZINCo3tczmuGxjLZQxA09D6sg0OlYGSkh8D1TRDEkWVoAf7HqCoR5TVaN4YwH7cQnI8h8bE8UpR-hppcUt0XfkWoKkDil-loh3ElwNG4h7Ebnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrCnV24zVmpSIXGjU6bMt1E3sE3DJUJyVIYBwLAwDBZa4ExuKJGvQaJTFlImC9YqMgbL-TOJKhZNxzilXpR5roaNj1Txsb8mqDojp2jt2fFpv57qv49yU7tbp0yWtWwlmpzQ3nRuBmDplfyhBu3pDDpJtYSJg2XZv0tFdiMiItVm5A3x33U0Ei-0zDecvFoVk27u-oObjKlU6pir8QVNrnuJxBGJd6B2hkmcj6DLF8f4HWOjwD-ItHAYfjsTq6GZ_4FbgUNUc_jTW4f2HcLS6dM6n4XRiUMrMjbQYkezcFhhrQBaaWzBffdbd8AzY99P5IopNn5q8OIRPDi2nuy_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmQhbk3tPR_xmSwho-PIjbcti9uyF9NFEPTn0AUeUnEfiB5fnjW74HxStXYiMXIYxhcKtopfIyAWpb0JJ-Ke2fNwlLU1kgJm6Z2yvnozlCh-viKVAzu3tLcBw5AtJudrs4IWAIBZOzpkbpK_UNPuxF5VjI9NGrqaBrNCq503B7PRPsldZD14yoS3iXNyjcT7wgAIPR_3zHpRCklO8644EESTKUdJtcIXAPEDX9DPdOFwp0k5lZTvAUhg0gtmKHGf-6aYMT2FyQcEy9LE8ITWKorsnDCsdQ_7dc5ngPiEA_Mo81Zu5bM8gKPzP7_Kz7884MmVo3ixm6NZtDP7gRE0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3b0iDrVLcpV4KTD7XErBiV1OzjWR0b1m6LQL41ldhc1rc4Im6IqHxZCgew75isIFCkr4Jj2ui93Fl0Mdz7bWyNdn-P2P7jJG-BK_sTrBan3f1ptZ32a4ffNR6uEDuY78khLVvsciccnCQsubbLJneH4VaczGMyRQMDwgFpF8uHDgicqXx_o_3psc39uFgY6-q7rcZeEF7_Be3g2ot-8CPZK4d7vOEvuCccpfp2SHgO3Tc8Xx7P70xacRNDaZ_TV9V4ufHeWBgSgKbuZSqSx_17FXBcf4S30UK3SNKX3sfVBr5pURZep9Hn_jcD-I1lldnjJ8R46amYsweu9t2jNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agN-joE6QFT6TTe0mxrKbk3BxdPrgihda0o7I34RKLufPkbLtgD-h8qFUJag7zFNfkExXV7ZUSxfxFFtezP_TMs-CwXkKF6v3wBbHMUATihz2kIS3WOVKY8E3GVx4cl_EKNmKK95ORK4t8kdbl_yJ4xyU2uQVSsWuPqMXRgiamIiEpBoLrtQJyXq1KA9PpyGbJ6nxT56XSgMOQzSKB4XXmqgyORfd12uOmw-jpiIRq7D7PyZlXoFBbaQvVdHmcRrj7hTbo9OyyDifFOZptMKO_96TD6Eah-EaXE38ia3JW8oWv24i4QZPkBISGxDUGKAC-F9FywzMwkIttIRs52QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-4JkbtP9q8xz7XjddPtuE479J3mEfl4YrorMCc6ZeYfO9eG9HDTGnhW7iKY2Z5KyJwfuHc8CdwXhS9DeZYzD92zus6fzwVtO2p63cbc8z67rsBcggkvpi4p6Nn-YOUn6HRO5y1jJXIoqsIPoSuFCGkKH0C_SdyfaX3rnWZ3yRbqRbw1xR4ZkK8ZJLSVr1BDyrA0Lu6IXAQkWojbTI9boXIOocZ6tjk3F8S0-GzZtCTBtNxucFBNFO70_qo7BJd-dzY2HIUiebEF39Y8C2n3r6-JN_YEUiK98RTWRi5ifsSRGL_UhH8Fp5LjlWAA8ArJpwL4L2z_ofw-e4hX817XLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
لوبیای لرستان در یک قدمی بازار
🔹
لوبیای قرمز، چیتی، سفید و چشم‌بلبلی از انواع لوبیای لرستان است که برداشت آن از اواخر شهریور آغاز و تا نیمه اول مهر ادامه دارد.
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/468212" target="_blank">📅 18:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468211">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/468211" target="_blank">📅 18:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEUht0VVdqCU-ftAV-6xGFvIkJrCW9SIx8hGwk517IPlSJnYNTNd0Gd6gD-jvSEogZs-QNusNoMExCP_LRDKuwI4uy5IAqYg36pjtAs-WHYil3upMgoA7EwfWiY-KdXt-nz5wKYziylu1SkTXVklIXh1QUzOrXbMuXlDKxuuVy-vBkJPqZmpNNDgP3ZpDcz22JIHbDNK0g_o05K0eHY5qd4eZ_FKr5tOULseE9M-kEuKGCG6_4vRJRPGbKF-nVteEtPgCo3qiEeDGTQkSD-4OUJI3aPyp85iW5q-aSFptT-yhEecBgwkEs7_XNdSXHe3YA0xHEcAxo-wNBHYtNDczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز: آمارهای صادرات نشان می‌دهد دلیل افزایش قیمت گازوئیل و انرژی تا حد زیادی جنگ ترامپ با ایران است
🔹
البته حملات اوکراین به روسیه نیز در این موضوع نقش داشته است. @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/468210" target="_blank">📅 18:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468209">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5ey28pIntceRPHz6MhdUSdDL58Xf_kvftz0X0tQ6_PCtX6QcYJFQOymRL_jT7zJxEulPa5v5zbOns6yOEh6HecPu_BplPWfG6tcugK5-l6TasysqOSPEJ96JYFq9J7rwV4XXa0LFWIY6geJOg5Dgv6qCSfrjHtPMqRxBPa9pMgi9xDmXg-D0O0e5-kLyFrljFGiyPIn2ZU6j4tAbtKW21w50Y8YkQ3pIu94LzUm3bRqSZs2qqcLLPg0xpFW5OqmtH4rHxkA5jD9QfT5f9WZtxZcU75vENOs-xQxjDsUCZ6YEbbW_Z2w4MfPv1h_jg6SH4ZgYogivAs4Y5EiFhcyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
صندوق‌های سکه، طلا و نقرۀ بورس امروز یکپارچه قرمزپوش شد
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/468209" target="_blank">📅 18:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468208">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D969c6KQNy6w4JHAkeTpUcoKsHHANAcJ6FS7nDNYOpNbBJHUdm2ngRg3boH2f8rMrvi_jCLWnEAuQRmm-iSZIARk2ssWvCWDUziq5wqr_wuwgcsa-825-nlmwddH9x5ZPjSYaWEUm03o9k8FTKRAqvoPxc8Y13qXzAy64BmeqTRsFiAfQcC92TTZ1p0PjMeE2dBBItmKoxGY-7SIVegkAMnbiTIChZqQ2pDUBmjcgFg629eWglkZX2oA0A67bRDTyxdB2xZv_imJfsOHdzGgwptUkjTNJwppdw0-1gMM9qD9sQe9U24HkD_677VxsBVuVv-4J1YCGwYYhtjoqTjOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/468208" target="_blank">📅 18:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468207">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf4dadc0c.mp4?token=RPeQ23xU11QdCf4vir_lc3L5VTzFpSn57Q6ymKeEzoDDU1q6QMoJlNmVNuu1A4tr2IIWh9Jvp4bh9EJ7rVZkZVWRfEsU3eXeZSg329ko4RyVOexBrOHb2h8FGijU8lTMmRUcZe5AunSGlwZA7PhJbe8luXOaeR6vKeMmyn2JQ6ZZtHFv9HOtJ6ZQxHDH26nNXoLzhaGf9LUUxQsmECbeVEBJCt0YjmpdMkBRMuhwHfHOzhqPFoxKL3r5N4XwJaqirXbQmB6EpUDt4ibAD-59QNVkr74CyraiA1g9Kvi_8MSXbx5g-zIAcB_338vCDVM0GtcOBmkcISB-mfwdhURvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf4dadc0c.mp4?token=RPeQ23xU11QdCf4vir_lc3L5VTzFpSn57Q6ymKeEzoDDU1q6QMoJlNmVNuu1A4tr2IIWh9Jvp4bh9EJ7rVZkZVWRfEsU3eXeZSg329ko4RyVOexBrOHb2h8FGijU8lTMmRUcZe5AunSGlwZA7PhJbe8luXOaeR6vKeMmyn2JQ6ZZtHFv9HOtJ6ZQxHDH26nNXoLzhaGf9LUUxQsmECbeVEBJCt0YjmpdMkBRMuhwHfHOzhqPFoxKL3r5N4XwJaqirXbQmB6EpUDt4ibAD-59QNVkr74CyraiA1g9Kvi_8MSXbx5g-zIAcB_338vCDVM0GtcOBmkcISB-mfwdhURvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلی حامل ۱۰۹ قبضه سلاح جنگی در مرز پرویزخان توقیف شد
🔹
دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/468207" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468206">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgP5Ho4Z9t34G11LDhM4uhpdtlCci1f1dFUweMCZTu1zTRquKPVSMCp8pAcKsaLklSMBOJe7yIBb7yh_TBvePXF-5MDpPtSegGpuDuMk2x1MKPT18FUA6Rugobv0jICfMzQwhEem1z0bBqUzwKzxg8fx_tHfjdQslDqoLTpKuvzE_7cqPK9GWmFAyj9paGnDmhsQMSAb1xP_nzH1DW1uJRozC1O9RV2mTddSwrc7SVnzsi5qI7nS_2VPvcoM5qN3Rwk__MiswESnewwAcwqrFYA-SxOEGs6wa4uQcVjpWXgiycqg66c1D-tWyTAGik_Kgw1Qy05HGqkhMLGSIqiUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی ۵ پلتفرم رمزارزی به خدمات بانکی قطع شد
🔹
از ساعت ۱۶ امروز دسترسی ۵ پلتفرم صرافی رمزارزی به خدمات بانکی و برداشت غیرحضوری محدود می‌شود و کاربران این پلتفرم‌ها امکان واریز و برداشت وجه را نخواهند داشت.
🔹
طبق اطلاعات رسیده به خبرنگار فارس، تصمیم برای این…</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/468206" target="_blank">📅 18:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468205">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0c3bea69.mp4?token=WY_NrzfNr_-MvF9C-1huRSBKND0RKT3abB8U4PZ1U9jeeSUp5G-TY7RrHy5H39JQsz_YlnUCQYZSaaxGWBI8cJHigcvcIDKZ4HCzpMNqIa3JDsI2DFag_Lng-oZQBp_HliY0ISnV7mEUZTprhiK5k0YqJBWdHvkwVO2MmlWYp6ltRMYdEyYkt6JdBMdoRY_0RcTe-q6D4zmoZoLK8cBI4CW6qbb-QzZlchKsxXyx0ahYFEttyS13wJxJe9mAIzCScO8pSge2Sw7nbYdhcC_z3XcLRXJ5FVaIlciUtG2WvkaoqQfEKtxUeUk2oJ-rc9_UEmztvuBWw6-R3IUPHEe3pBWPSHEMjcjPHz8iXhT_MG2xS_dXqTYY_Wg2o6rucXq0TpUHRLYPv1-QsLiB0Pq3nBfpXVBA6N5OVs1V4q1DqBwfs9EZj9Pe7_XgBDJtAOVSPIaUAVNU6CGLdHg16Cr-mJdjP7x5wZ3GYwsJBjrGu6m-6nSxNWipKy9_eFxymfjlAKk330t4KK-AdknDTuE47DXkmp14xJYLS6Bq5ITKmwZgcLUq6wTPK555vnUL9GzV1XlAEipNn6KiJ5kr0NhvxDbh-xQZv46xTPHe2pw52YAxhX6nG8wx9uzC2jpQpZmmUKdMN7UbQjgVKHxGrr0HPrSC5MltBfbjr-XtazcPpbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0c3bea69.mp4?token=WY_NrzfNr_-MvF9C-1huRSBKND0RKT3abB8U4PZ1U9jeeSUp5G-TY7RrHy5H39JQsz_YlnUCQYZSaaxGWBI8cJHigcvcIDKZ4HCzpMNqIa3JDsI2DFag_Lng-oZQBp_HliY0ISnV7mEUZTprhiK5k0YqJBWdHvkwVO2MmlWYp6ltRMYdEyYkt6JdBMdoRY_0RcTe-q6D4zmoZoLK8cBI4CW6qbb-QzZlchKsxXyx0ahYFEttyS13wJxJe9mAIzCScO8pSge2Sw7nbYdhcC_z3XcLRXJ5FVaIlciUtG2WvkaoqQfEKtxUeUk2oJ-rc9_UEmztvuBWw6-R3IUPHEe3pBWPSHEMjcjPHz8iXhT_MG2xS_dXqTYY_Wg2o6rucXq0TpUHRLYPv1-QsLiB0Pq3nBfpXVBA6N5OVs1V4q1DqBwfs9EZj9Pe7_XgBDJtAOVSPIaUAVNU6CGLdHg16Cr-mJdjP7x5wZ3GYwsJBjrGu6m-6nSxNWipKy9_eFxymfjlAKk330t4KK-AdknDTuE47DXkmp14xJYLS6Bq5ITKmwZgcLUq6wTPK555vnUL9GzV1XlAEipNn6KiJ5kr0NhvxDbh-xQZv46xTPHe2pw52YAxhX6nG8wx9uzC2jpQpZmmUKdMN7UbQjgVKHxGrr0HPrSC5MltBfbjr-XtazcPpbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین روایت‌ خانوادگی از علامه طباطبائی
#کتاب_باز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/468205" target="_blank">📅 18:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468204">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">گروهک‌های تروریستی شرق کشور زیر ضرب دستگاه‌های امنیتی
🔹
گروهک‌های تروریستی در جنوب شرق کشور که با دستور رژیم صهیونیستی مأمور به ایجاد ناامنی در این منطقه هستند، در هفته‌های اخیر با اجرای چند عملیات محدود و غافلگیرانه و بازتاب رسانه‌ای گسترده، تلاش کرده‌اند تصویری از ناامنی فراگیر و ناتوانی نیروهای امنیتی در مقابله با خود را ارائه دهند.
🔹
بازداشت تعدادی از عناصر کلیدی، هلاکت تعدادی از اعضا، کشف و ضبط تجهیزات و انهدام چندین خانه تیمی، نشان‌دهنده اشراف اطلاعاتی و توان رزمی بالای نیروهای حافظ امنیت در این منطقه است.
🔹
یک کارشناس مسائل امنیتی در این باره می‌گوید که این گروهک‌ها که در میدان واقعی نبرد تحت فشار هستند، برای پنهان کردن ضعف خود در برابر حامیان منطقه‌ای و اسرائیل، روحیه‌بخشی به نیروهای وابسته، تأثیرگذاری بر افکار عمومی و القای ناتوانی دستگاه‌های امنیتی، به جنگ ادراکی متوسل شده‌اند.
🔹
وی ادامه می‌دهد که نکته مهم دیگر این است که وقتی گروهک‌ها در میدان نبرد توان ایستادگی مستقل و تحمل ضربات را ندارند، تنها گزینه باقی‌مانده تجمیع لاشه‌های متلاشی‌شده برای ساختن یک ویترین بزرگ‌تر است. راه‌اندازی گروه جدیدی با نام «جبهه مبارزه مردمی» در واقع بر همین اساس بوده است.
🔹
این کارشناس مسائل امنیتی تاکید می‌کند که میان وضعیت میدانی این گروهک‌ها و تصویری که در فضای رسانه‌ای از خود می‌سازند، فاصله بسیاری وجود دارد. حجم بازتاب رسانه‌ای یک عملیات، معادل گستردگی توان عملیاتی یا نفوذ میدانی نیست و عملیات غافلگیرانه، حتی در صورت موفقیت تاکتیکی، به معنای برتری راهبردی نخواهد بود.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/468204" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468203">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIr6eImLOPW8t6t2_Wk9vqoJM7d_EKUre67jxXwZubsMHA9XcyMt0J5jHSB5_DTq-XNSK9WppUo12u8Iq2YAVMIsO9NKp35ZzPqU2pVvkX18hz-crdCDdvjUoJNYuFK-bJUGKVbT-XhAoJwZQs9EJ879IbhnaIUM3qlbL73fzYIQuW2uoEPFC81n3OI6W9n5yuJlikkJNsnqBAh7DGPK9ZUG6Ke0bcEIwgTdk9wmvIeZe2rvI3Z1C3uRg2625RdCInMK_ZMyOsg3lizkGfYBK1B0Iop17FW0Fo1PV8wGNWp6KXZYl6LUr0FIOjFLV-yQAKYCRz9HwOfYj2ELTOOjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
برای اولین بار در ایرانول انجام شد:
✅
دریافت اعتبار ویژه مالیاتی برای دو پروژه فناورانه
🔶
سرپرست شرکت نفت ایرانول، از شرکت‌های تابعه هلدینگ تاپیکو اعلام کرد: این شرکت در راستای توسعه فناوری، ارتقای کیفیت محصولات و تقویت فعالیت‌های تحقیق و توسعه، برای نخستین‌بار موفق به دریافت تأییدیه حدود ۵۷ میلیارد ریال اعتبار مالیاتی برای دو پروژه فناورانه در حوزه روانکارهای پیشرفته شد.
@tappico1381</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/468203" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468202">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQD5GFlvOf5bkOX1xJb-3mxrJHdBFYUoz-Vuf5e4M_CG7lJ1GdJx6C5SA4ZHyp40u-QuBTHkQ7nWm8Gy5fh0igcdC9UZSZkRl8QYAq-ONKEDrUJZwHPr0pd3bMG8nhm_fs_hoDsr9yfB7oTWcedblzh_H0bfBMZDEMwG1620Ie4aAfuAojM-zS3YQeEQ0iCTIR9I27mWTF3tcyHQ-xEO6YT2S3e67GRchVdDSvMyMbk2hKYvWjwqWmEa3ahp-mGvjzLoSjZgF_0nV9BTL-GTx24Vg4gZ2z8tdXRWTJEDxl82v1Si6cmWF33rPup4hBdkv1vn5eLmQOxmDyhJbS8tAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرصت سرمایه‌گذاری فولاد مبارکه
در حوزه ساخت افزایشی (3d Printing)
🔸
برای اطلاعات بیشتر کانال صندوق سرمایه‌گذاری خطرپذیر فولاد مبارکه را دنبال کنید.
◀️
برای عضویت اینجا کلیک کنید.
|صندوق سرمایه‌گذاری خطرپذیر فولاد مبارکه|
🪩
MSTID.com
🆔
@Mstidfund</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/468202" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468201">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/468201" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468200">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbXFkhG0vxEJT5ooMgeyVGYSxybs8lBfQicc8_2y_gPGvIuyKZ3kDlTRiqoDSXIJiOT9DZr1DzYZHqkJdjHiCmjFrGmR4-9wUt43AUbCYHY5zuz29_-vSpyyGQ2A8Y_Bz8z9LqOH6KiFJoMP72a5MvZs9qsjSJcMbL6qUQ18TBPb_yNmeJuYBbbhxoGJTadE1DbH5ApChYkoLX_5nWyaP2PZKg9keEoAHMDGCUOvU6Th_DkxlWsyAtp6sjY9tceCqPLY4IJdVd32AEyZCNsDnOqq5Z40yg-PYpuXvJbLLVP7pXX-EfuxvF_Zwx8VidrNDK33XF4RebFZW1JUQ-92gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان فاتح دربی اصفهان شد
⚽️
ذوب‌آهن ۱ - ۲ سپاهان
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/468200" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c704e3ecd8.mp4?token=UgyR6nF3NBGVz9Eclw2QyiDr4zWt06zvhXtx-lOTxLJxi0sFwouPS6J0sv2g_JD2h3QyK4WG4eLhshKvUYuH-Rlg2ALaV3hvNUgcS9xIu0FuMWpyThWut_PLcy_1ocAjGHEyCIahAD3mj2cODC8_FgyuI9AmES6cAKp3YgA3TN4TL-bdR8ygC4XGwoYahnzKi5JiStVjkp25j1G4Ehe2fkxxq85eOm7MnLIrY1_rlmDAiyQWhvfAorDI1vY_ws34yjB67hNb_8t9tlnrXDfHmd4sRaXOV7I_hL6VoXTaU0vaBAAYb50z8fPm6NcZL2bmQ2qG5_mjmUWEucRTS7Q7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c704e3ecd8.mp4?token=UgyR6nF3NBGVz9Eclw2QyiDr4zWt06zvhXtx-lOTxLJxi0sFwouPS6J0sv2g_JD2h3QyK4WG4eLhshKvUYuH-Rlg2ALaV3hvNUgcS9xIu0FuMWpyThWut_PLcy_1ocAjGHEyCIahAD3mj2cODC8_FgyuI9AmES6cAKp3YgA3TN4TL-bdR8ygC4XGwoYahnzKi5JiStVjkp25j1G4Ehe2fkxxq85eOm7MnLIrY1_rlmDAiyQWhvfAorDI1vY_ws34yjB67hNb_8t9tlnrXDfHmd4sRaXOV7I_hL6VoXTaU0vaBAAYb50z8fPm6NcZL2bmQ2qG5_mjmUWEucRTS7Q7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/468199" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c4818c08.mp4?token=nK8w_dmPyM7YGnDUIsanOF969DOgODSyeh0EpAW4qnzXNQkSNZvGk_IHDfuH1_9IFD6T7D5lmvTRgQc_RC5DvlkyzEg3hSy1jqBEOLTv4ksufbAO8cVmUboDnsLwxY8jOwUVjUG1T1ywrgialv2gpdE0cnKOx0E9Dlz1fhb3J0CpdLcXaskbnyjKKtWY6vDtyEG1QGpnw2JCxq_UqtX9Mx3zLZCMxjsReNZEtSjdD_gTBoPjjk_83UxoBmtIEthRb6XJWY8uW4LozctRbtk1x0bap45BrgHiGGorkYnYMIczXe1Qyq3m4zIiPYv1Qv9jJGAm18R3F-09EXoERqFJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c4818c08.mp4?token=nK8w_dmPyM7YGnDUIsanOF969DOgODSyeh0EpAW4qnzXNQkSNZvGk_IHDfuH1_9IFD6T7D5lmvTRgQc_RC5DvlkyzEg3hSy1jqBEOLTv4ksufbAO8cVmUboDnsLwxY8jOwUVjUG1T1ywrgialv2gpdE0cnKOx0E9Dlz1fhb3J0CpdLcXaskbnyjKKtWY6vDtyEG1QGpnw2JCxq_UqtX9Mx3zLZCMxjsReNZEtSjdD_gTBoPjjk_83UxoBmtIEthRb6XJWY8uW4LozctRbtk1x0bap45BrgHiGGorkYnYMIczXe1Qyq3m4zIiPYv1Qv9jJGAm18R3F-09EXoERqFJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخطار قانونی قاضی دادگاه منافقین به نهادهای ناظر بین‎المللی
🔹
قاضی دهقانی در پنجاه‌وششمین جلسه رسیدگی به جنایات منافقین، به مراجع اروپایی و نهادهای ناظر بین‌المللی درباره ممانعت از استرداد متهمان و اجرای اعلان‌های قرمز اینترپل هشدار داد.
🔹
او تأکید کرد هرگونه…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/468198" target="_blank">📅 17:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOmdJQcro71XUWMDBpIN4ZQ0C_vha0UoAWnyKV7m00xvVJflkWwmBKRDCoVTKyDPS-yjue5zk7DkpKc-gkxTM6Qu-U4ZtPQhJ9YVlIPnrfp60EtMaaP14dB3GhJU8R29w6p7KOATRi7LQbfm6AaeAIT5t9VUhNy_x1s3FOz38ncUE7dhA8sfmMYOJ7NhUc6wHh85CNTGWuDF4xNIDiwVlr7oaygVfIMqt0yMQldbe7XlFRDTMtkTZN01FTfEohK8QSRAgBEebCG6F9JaG3Kamfms0eZ1BTLWXN_IGhuRWsTXk4jDQnhRduU65z956bBCRIKahtSDpM7cS3btdDp9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv7TeqRRg35H6-dUP4x7gUPs8YK_-0RnY076oqHL80nHtvScIS-f8SQT5DOMWycrkgHQhpJqXWAnBONIyVbaZs2p_yg4u8Mxxpx8bR_815lj0Sj3emgt9qz5xDzukoDvGFPFpzGSokgTMLQMoGDPLBEQMXgXf8M1f-97MEoKceKcd7mLeV5kDx37WqPsBY96PjpIhaYkyY9uHSw0iVWeEzYAleqmulNzBQfmWMSfCc_T_kYlDw6Srq_AAuEa7r2G-bs62Z0wFJOuGB8rVl7ez9g70GAlV9gtzwhsbYKVBajY64F2gNJ-hRjg1A1J8Q-IRRdIGiulcee18PGM5utRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD2br8_P5hbd1wiDhqQhn40duII5f82sg7I2oGcK99lCJg0xbWqps5pPaEjfAIuBjqZMhizic1YPdIaE9p9r_Q0bjToX69tblSI4j4KOJwvi2K0sod77O49al9f4YC4pAWskMSQe9dxAYtwV04TXXarfoFn1-DYGLwFxjFPTBzPdzRugK7wKJ8KgJv4mbOJGeI1UT0C3AIxCNKKO8-f42lO6Ug4yfAbNq9Fn-DvCP0Qymnf2eVoO6o0CZSYeJfLKwobK8Ca-BIojiuCJGsslR-OFedN2QG4aUPioXshU4JyUkqDtqoJqKd8dCy1-iFGkXY6lpmdfz_ghqFyVqwyACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ هشدار فوری یمن برای تخلیۀ فرودگاه ریاض و ۲ تاسیسات نفتی
🔹
سخنگوی نیروهای مسلح یمن: در صورت انجام حملۀ اعلام شده دشمن سعودی به صنعاء، مقر شرکت آرامکو در الدمام و نیز فرودگاه ملک خالد و پالایشگاه شرکت آرامکو در ریاض باید فورا تخلیه شوند. @Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/468195" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeT2OJv8EY3RhVWnMpi7V496ywsk1LctAwTIK9G74Qt1sMQq7UZq_kL0QB6Ndu2BMIUolDPjsDrGhgVkqd5CtZYm3F9FOjHMYVZWZ42r8SR8aD-wKOXb6bjuk2nRPmZ0GI2vxzggcfzQnDuwAoM9FL4IyKH4kSYr5XegZqwAkssCwMZr2UHY0nypE8GdJ_7wk4ZMTwr8KYMBG4vJC8kZaweJQAw-MAoafC-OMiNxxmMJvpQdyobT_J9PsGAc7haPrWyxFnfa7mAbQWrvySdYWN50BOdl3F7G3PgVozNrQQPSMI2uONbFK3JIp1pV0ZuJiVxXgKVWKKvszY7sWgAKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ایران بیش از ۲۴ دلار گران شد
🔹
جدیدترین آمار دبیرخانه سازمان کشورهای صادرکننده نفت خام نشان می‌دهد که نفت سنگین ایران در سپتامبر (شهریور ماه) ۱۰۵.۸۴ دلار به ازای هر بشکه فروخته شده است.
🔹
این رقم نسبت به ماه پیش از آن یعنی آگوست ۲۴.۵۹ دلار گران‌تر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/468194" target="_blank">📅 17:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e97599bfb.mp4?token=gbR-G6sY3Dm0Yjy3aowT6gA7IjxLgJiPzalz7OCSn4brfrDmZ2Ncb9an4hL_rIe8Fxlb3KSfAdI1KRp_glbUALcqrQs9sCwJsYywwFATrXjlqilCnyZki4hXWJ2ZrgntE2RDRoQfkWYhF0rEJNztxBbN-xEHBu1kOJIMhfidHEqVjSmx4HkM5dpD_VO6yXKPxaKvwcmstUr0a-kPcLMj3P1Z_gNDVl_VZKlEvJGGfFo9nlqVf-Ghkg5SFTjpaJqgVkoFsTrwwX_dqhd181da_ApU5X9HmvVy0tE_LJxLe3LigiPfMZfA3_Vl5cUxWaWn86fBi7cEnnTR97lu8Optxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e97599bfb.mp4?token=gbR-G6sY3Dm0Yjy3aowT6gA7IjxLgJiPzalz7OCSn4brfrDmZ2Ncb9an4hL_rIe8Fxlb3KSfAdI1KRp_glbUALcqrQs9sCwJsYywwFATrXjlqilCnyZki4hXWJ2ZrgntE2RDRoQfkWYhF0rEJNztxBbN-xEHBu1kOJIMhfidHEqVjSmx4HkM5dpD_VO6yXKPxaKvwcmstUr0a-kPcLMj3P1Z_gNDVl_VZKlEvJGGfFo9nlqVf-Ghkg5SFTjpaJqgVkoFsTrwwX_dqhd181da_ApU5X9HmvVy0tE_LJxLe3LigiPfMZfA3_Vl5cUxWaWn86fBi7cEnnTR97lu8Optxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌گرفتن نفتکش متخلف در شرق تنگۀ هرمز
🔹
نیروی دریایی ارتش: ظهر امروز یک نفتکش متخلف که با خاموش‌کردن سامانه‌های ردیابی قصد عبور از منطقۀ ممنوعه در شرق تنگۀ هرمز را داشت، دچار آسیب و آتش‌سوزی شد.
🔹
یگان‌های عملیاتی نیروی دریایی در شرق تنگۀ هرمز، دریای عمان و دریای عرب با اشراف کامل، رفت‌وآمد شناورها و فعالیت‌های دشمن را به‌صورت لحظه‌ای رصد می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/468193" target="_blank">📅 17:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468192">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGgzF12VSmIdYmzf7RK6xpH2MllmEIxlmhXIP1oF2bhlforJZrhNLLFdWrGYxbkfyDegd8kK5aawrrZ-1TKJwagIUgMntAG3GKk9HL2W-bFBa78oBnWJaV9MHbXDNShx_wmFxuSBQfa50_yPtXI9qXNLVfkmT-55jrlRCplgg--8O6UiV5oagtf3Hn8ZojXwDbQn-39CtPn8pFNPcUBm4TUe3-1xvkCEmiqhJbYB5RS5RZ_0hO0PlmBfXfkgpC55hEa557PV2doeI-nrkSLnfGFDRIIyoJCTNqMKS4iiIloIEONJviBRrWFWy8dq52zfEu6A_pf9bEZIqLCqfHAvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان هدفمندسازی یارانه‌ها: مهلت ثبت درخواست افزایش اعتبار كالابرگ تا ساعت ۲۴ روز جمعه ۲۴ مهر تمدید شد. @Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/468192" target="_blank">📅 17:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
المسيره: عربستان تأسیسات شرکت نفتِ غرب صنعا را بمباران کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/468191" target="_blank">📅 17:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📷
ائتلاف سعودی برای مرکز نفت «الصباحه» یمن در صنعا هشدار تخلیه صادر کرد
🔸
سخنگوی نیروهای مسلح یمن در پاسخ گفته هرگونه حمله به صنعا با پاسخ کوبنده در ریاض همراه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/468190" target="_blank">📅 17:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سازمان برنامه‌وبودجه متولی جدید کالابرگ شد
🔹
معاون اقتصادی وزارت تعاون: براساس تصمیم دولت، سازمان برنامه‌وبودجه به‌عنوان متولی اصلی طرح کالابرگ الکترونیک تعیین شده است.
🔹
تمامی نهادها و دستگاه‌ها باید برای اجرای بهینه این طرح با سازمان برنامه همکاری کنند.…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/468189" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Slg2miskmuCs2YiILX-GvpAl61NmZJ4Cmjv0ANmXKZLLdG_8S5_GYTqNX0o8SwMliJqsm8R3M7WsRkSpeOKPtQ9Q9JDO6brYdSE0PZFKWgRfznt_nfhH50rnUPsy6-TPXIvNc8EolSNSISUUyzHHpuxWEdExo8b_MLTPKyanUt6AeqN6jy833RMrv-ODyT1T_8PSQ3WAgmV6hDFGajbUwshESxsVjRJJpbSsE8ALFdQwgZtz844dLkLCt8k-y_ViRz8etnwX4l_fkyKSwl0Tlpef9ueaNfu5PVU55YgXdvu9tpeVOLccVZQt1Ot6Vzo9iU6O3FVSAKZE44Y4pv0nKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/468188" target="_blank">📅 17:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkJ8mLKwlVv-2zEC28ddS7Db0DrEjyysa739uZac-Cae6ttAnKtUxLSU719Iamb084XWLEOV0oB5YwKD_VUnG38Wg6YjfzQqcgWQ_WObOkh-tfcAgUWZs6P35bDNvnIKKZOw0hGzGs0jZNFjV1uG9G4oFntxg5PfvCYvOu_JtOcf5x76WZe0bX7VQsByKSxvXkKn8pkGl4WPJiaISexNS0Nou_7qSnJ155o_uj_4damo56G3bZd7TvVIlFiokZf67m2A4eWhTz1fwjGCp6grjgRF3pDcK3A66edXuf8xLtrk6cwAjRxSSgdkXEmtf3dn-rg2Dmf2C6urtAs2hI5N4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
هشدار تخلیۀ یمن برای تمام تاسیسات نفتی و فرودگاه‌های سعودی
🔹
سخنگوی نیروهای مسلح یمن: به همۀ کارشناسان، مهندسان و کارگران تأسیسات نفتی عربستان هشدار می‌دهیم از حضور در مکان‌هایی که اهداف نیروهای ما هستند، خودداری کنند تا جانشان به خطر نیفتد؛ چه مکان‌هایی…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/468187" target="_blank">📅 17:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شمارهٔ ۱۱۵ اورژانس تهران قطع شد؛ با شماره‌های جایگزین تماس بگیرید
🔹
اورژانس استان تهران از اختلال در شمارهٔ ۱۱۵ خبر داد و اعلام کرد: شهروندان عزیز در صورت برقرارنشدن تماس با ۱۱۵ می‌توانند از طریق شماره‌های زیر با مرکز ارتباطات اورژانس استان تهران تماس بگیرند:…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/468185" target="_blank">📅 17:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY00cFmh40Clsn0KM0rHfndJ3zjTMCSJsJ-XsDeUy5MAbIVPoDqIRTq1MWNyMbsJbojQAVlcMrbC9WmUTAnG-lhNCuuLZmf6ILws3KWVVIoiU1wt9H7SMJPpfxmaxvAIxLSVHm-_Hay1Ha_aOe4mr8x0-5O409OqUFcWUtq8U7B9nScPBJPi53M_vxqceVV5aXLDDf36BmLa-yySYk-wMIqC2yQ7u1DtZ2uBuJNXMVD3Ss6NzfYdXRwa6z5Q3rcXsQvIt6pvJEJpzmEs5U6dzJSgO2pPrq3CdShGXF2XAFKsyaQaioGQDw6IRzVFzJxgCry166JOt2P7jgyFu1Fv4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: برای کمک به دولت جلسات متعددی با رئیس‌جمهور داریم
🔹
رئیس‌جمهور به این موضوع اعتقاد دارد که سازمان بسیج می‌تواند در پیوند زدن مسائل مردم با دستگاه‌های اجرایی برای حل مسئله، نقش مؤثری داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/468184" target="_blank">📅 17:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسلامی: برای برگزاری انتخابات شوراها منتظر مصوبهٔ شعام هستیم
🔹
سخنگوی ستاد انتخابات: همهٔ مقدمات و تجهیزات لازم برای برگزاری انتخابات فراهم شده و منتظر ابلاغ مصوبهٔ مربوط به برگزاری انتخابات در سال جاری هستیم؛ همهٔ استان‌ها به‌جز یک استان برای برگزاری انتخابات اعلام آمادگی کرده‌اند.
🔹
زمان مشخصی برای به‌روزرسانی فهرست احزاب اعلام خواهد شد؛ سامانه‌ای نیز برای ثبت فرایندهای مربوط به فهرست‌های انتخاباتی راه‌اندازی شده است تا احزاب بتوانند اطلاعات خود را از طریق آن ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/468183" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP_J5gADmfpqtYl6jt_u8NnDJ22sHsnCb1hRPRC1i9hEoMANGfClMEhJl2flzm0ZRi02UnROeiyDB-XfNvO7GGW25dna6crFmPkgFZOlR7xMKcYF2EA4gAiemq3qk8FHpXa-wrpxUqjxKU5lI6w2aiyAXz_bjZn8nv1-0A2qv5OnRBUX6Qq32savcVzv_5Rw-H2ATRWXlttU13u-rK-8UTpFUz-JAFawTKE2aJFayL-Fht2IJGSU6Vg4kAoFDo-jFDIvUFP_gE-GKi19jifJSCVOVSwPMzw3j-JvGvU3dPEx06_omW_AxHoaXzrEFJnVjyXMWMaedS8e023nZJtAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف مزرعۀ ماینر غیرمجاز در یک دامداری متروکه در استان یزد
🔹
شرکت توزیع نیروی برق استان یزد: ۸۳ دستگاه استخراج رمزارز غیرمجاز در یک دامداری متروکه در یکی از روستاهای شهرستان تفت کشف شد؛ برق موردنیاز این ماینرها به‌صورت غیرمجاز و از طریق انشعاب‌گیری پیش از کنتور از کابل ترانس تامین شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/468182" target="_blank">📅 16:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsVPpwL6GhUpIGvXsgmOSs9IcmpmE4OCTd37BNdu4wD-Ih9iNPZCqC3xkBLki_hb1LttcrP07pDuEVpvfX4tuB7hAatziY_6M5CChNJybtwyZA1c1BhWBjG30Vnn1AtnRpz5LRM3AWNtTdcPUuZxZ_AhjcLyovvx0_e5KoZsgxxtSZHYNpGXcXWAf1BqQQk1yQLnB3sojSjEiMKExNvF66s9G-fs9Z81gqOHcoDyL9qXlxZgMgy865vvOHbGiqNZlFZ3cSa3sAL7iRKBNFwtI_6TC5Mud7yB3buibDEroo6uBasdiIrvP3oLVdDTkYI_ml7zbyV6Kl5grmKTcyW41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرخواندهٔ هوش‌مصنوعی: ترامپ یک «مجرم فاسد و سالخورده» است
🔹
جفری هینتون: ترامپ یک «مجرم فاسد و سالخورده با زوال عقل» است و اصرار او بر استفاده از اصطلاح «ابرهوش» نشان می‌دهد که هیچ درکی از هوش مصنوعی ندارد.
🔹
مدل‌های پیشرفتهٔ هوش مصنوعی ممکن است در آینده از کنترل انسان خارج شوند. حتی اگر احتمال وقوع چنین سناریویی فقط ۱۰ درصد باشد، باز هم باید آن را جدی گرفت.
🔸
این اظهارات در شرایطی مطرح می‌شود که اختلاف‌نظر دربارهٔ نحوهٔ نظارت بر هوش مصنوعی افزایش یافته است.
🔸
دولت ترامپ از رویکردی حمایت می‌کند که آزادی عمل بیشتری به شرکت‌های فناوری می‌دهد؛ رویکردی که منتقدان آن را برای مهار خطرهای احتمالی این فناوری کافی نمی‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/468181" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9ec853af.mp4?token=NThHmrZDCOrR01n57LiE9xvkkMXOsVhAkT1MVh2jiZeZJcDjkxe70mmyXS1LCbHY1VJvEWS5SmR7bOIAgrhDLgRfgeKvAPf1R5KHJKI7qzFZk3afkuSoDLFeccWWv5KQS4SPFfXAzdVwHykEL6xl8H3mcOFf0Dok2gDgOWESZabrRaG3DGkszGei03TjyYBgTfjq1fwDg5Wdk0J7lT97U0pd96u-E0e-SmZHslLs20wW7KDVTHEgYL0wAm8VKf-CljR66abvSsERq3CcSQw0oFVn8Jv9906Lml7yTV4gHg4rC5D6oB471ewyzpotkJ9Xk6uyl7UxXMeLm8RgFtjc4ZjV04Qb7k4JysJ7iAv-93cjv8o-mXQGUHbVT-TUMwbZ1QZ8KgToUDyMyedkMp-UTsD78YIbxegzuNOOL1l3piSZgwRlDBf8VGOZXuzE7cjitjuy9sIs1pKBfn4Zd1riAKOUHQ0ca9LncKK_7iwnB2nIOfp3T6hmGiskKUIHImG_ZUIF9Gex7CqaCKX8gwIY3JvIyqI5BroYfQKrx2C8o9p7UzcL-5o5iJKeedy4bDFQeCh5C9dCEjGcvIntN59CyJsM4KIhUHNW8rQQ0PG2y_bwtbNqPZRU3FNZCbZ6Um16UopFFRPxLyeyy-3YDLqnAPGqljQZ150HGn7RcVsxxGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9ec853af.mp4?token=NThHmrZDCOrR01n57LiE9xvkkMXOsVhAkT1MVh2jiZeZJcDjkxe70mmyXS1LCbHY1VJvEWS5SmR7bOIAgrhDLgRfgeKvAPf1R5KHJKI7qzFZk3afkuSoDLFeccWWv5KQS4SPFfXAzdVwHykEL6xl8H3mcOFf0Dok2gDgOWESZabrRaG3DGkszGei03TjyYBgTfjq1fwDg5Wdk0J7lT97U0pd96u-E0e-SmZHslLs20wW7KDVTHEgYL0wAm8VKf-CljR66abvSsERq3CcSQw0oFVn8Jv9906Lml7yTV4gHg4rC5D6oB471ewyzpotkJ9Xk6uyl7UxXMeLm8RgFtjc4ZjV04Qb7k4JysJ7iAv-93cjv8o-mXQGUHbVT-TUMwbZ1QZ8KgToUDyMyedkMp-UTsD78YIbxegzuNOOL1l3piSZgwRlDBf8VGOZXuzE7cjitjuy9sIs1pKBfn4Zd1riAKOUHQ0ca9LncKK_7iwnB2nIOfp3T6hmGiskKUIHImG_ZUIF9Gex7CqaCKX8gwIY3JvIyqI5BroYfQKrx2C8o9p7UzcL-5o5iJKeedy4bDFQeCh5C9dCEjGcvIntN59CyJsM4KIhUHNW8rQQ0PG2y_bwtbNqPZRU3FNZCbZ6Um16UopFFRPxLyeyy-3YDLqnAPGqljQZ150HGn7RcVsxxGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیزات و خودروهای مزدوران سعودی هدف پهپادهای یمن شد
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/468180" target="_blank">📅 16:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تاسیسات نفتی آرامکو هدف مشروع ماست؛ از آنجا دور شوید. @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/468179" target="_blank">📅 16:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777bcd045e.mp4?token=LrU3D2GlXKPG6zmk0WSilZX4obP8QXlz4hiARuyxY_Epi5Bd2sCNkFfiet9G80I6jlEwYRWp2bpHTWqwu-hltcMRh5hX9rp0tTzLNQHK4MOW7TlenT3wEZPoQ28x8G_AOBX_XNYFwmdz2-NBWh0Opq9d_3vJHWTOMegPrGTXzSgX5il_S9fXjXYEGy6aEC_yRjBLcLYngjjkD3oNyt521wxjmONJE0U2MaCNUin9IFaDO_JfRnR5PcW_C0DsCf8wtLZD_Uzo8Wquk4VOcFjyEh582fjHZEr93LO_9OE4mquLWxxDQKKtWb4F4O8hv4i6gCUcRGY5uL4QB5eMcEzT0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777bcd045e.mp4?token=LrU3D2GlXKPG6zmk0WSilZX4obP8QXlz4hiARuyxY_Epi5Bd2sCNkFfiet9G80I6jlEwYRWp2bpHTWqwu-hltcMRh5hX9rp0tTzLNQHK4MOW7TlenT3wEZPoQ28x8G_AOBX_XNYFwmdz2-NBWh0Opq9d_3vJHWTOMegPrGTXzSgX5il_S9fXjXYEGy6aEC_yRjBLcLYngjjkD3oNyt521wxjmONJE0U2MaCNUin9IFaDO_JfRnR5PcW_C0DsCf8wtLZD_Uzo8Wquk4VOcFjyEh582fjHZEr93LO_9OE4mquLWxxDQKKtWb4F4O8hv4i6gCUcRGY5uL4QB5eMcEzT0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
چگونه بانک مرکزی نقشه‌های خزانه‌داری آمریکا را نقش بر آب کرد؟
🏦
اسکات بنست،وزیر خزانه داری آمریکا چندی پیش مدعی شده بود که
اقتصاد ایران تا دو هفته آینده فرو خواهد پاشید.
دیروز موعد دو هفته‌ای وزیر خزانه‌داری آمریکا به پایان رسید.
‼️
تمام این اظهارات و سیگنال‌فروشی‌های متعدد آمریکایی‌ها با این هدف مطرح می‌شد تا
با ایجاد التهاب و ترس نسبت به آینده، روی وضعیت بازار ارز ایران در ایران اثر بگذارد.
✅
در این وضعیت به گفته رئیس بانک مرکزی
طرح عرضه ۱۰ هزار دلار به هر کد ملی
به بازار این پیام را مخابره می‌کند که
وضعیت ذخایر ارزی کشور پایدار بوده و بانک مرکزی می‌تواند نیازهای ارزی مردم را تأمین نماید.
📣
جالب اینجاست که در مصاحبه‌ای که اخیرا یکی از
معاونان وزارت خزانه‌داری آمریکا با بی‌بی‌سی
داشته، این موضوع توسط خبرنگار از وی پرسیده می‌شود که
چطور اقتصاد ایران توانسته‌ با وجود ادعای مقامات آمریکایی مبنی بر تمام شدن منابع مالی ایران، در بازار ۲ میلیارد دلار تزریق کند؟</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/468178" target="_blank">📅 16:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o68ih4YEYJq5rQwMX8NqtIftGnpnqLU-HyQaegw_x0pCcb-LWMIqeMaCuOTq1_oI6DcUHOF5vWKtw30AIMfJcOfOsCkAstU7WX90xpnMAeQm0kKthwMNKS5a8aaFkR77VlR9WVYXAWwwbNfyaLKa1S3wxXYsA8puAVWkZ6gTFUDEQCf9DEkQCTMvCIhV_lU7Azd5L4CiEdKMDWzuEBS-X4BxbhTUExDKkJGtUqWbKPrRD-Y5ds_MVf0KRaZmJk6vUs2a-ORsLhgkFFfVemN06k2RkowQZD8uA5DPTSLupmf1mM3TOZi2WeuhEiJB47DrE7RbmGe6A6XHyqg1anVLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
نسخه ارتقا یافته طرح ممتاز بانک تجارت با نام ممتاز طلایی با ضرایب و سقف‌های رقابتی رونمایی شد
🔻
تسهیلات
«ممتاز طلایی»
در ادامه مسیر طرح «ممتاز» و با هدف توسعه محصولات، افزایش قدرت خرید مشتریان و حمایت از تأمین مالی کسب‌وکارها طراحی و معرفی شده است.
🔻
این طرح با بازنگری در شرایط و ضرایب پیشین، تلاش دارد ضمن ارتقای مزایای قابل ارائه به مشتریان، زمینه گسترش دامنه مخاطبان و تقویت جایگاه رقابتی بانک در بازار را فراهم کند.
✅️
ویژگی‌های طرح
:
🔵
بیش از ۷ برابر میانگین سپرده (با بازه معدل‌گیری حداقل ۲ ماهه)
🔵
سقف تسهیلات مشتریان حقیقی تا ۷۰۰ میلیون تومان و پذیرندگان و اصناف تا ۵ میلیارد تومان
✅
برای محاسبه آنلاین و اطلاع از جدول ضرایب و ثبت درخواست به
صفحه طرح ممتاز در سایت بانک تجارت
و یا نزدیک‌ترین شعبه بانک در سراسر کشور مراجعه کنید.
☎️
مرکز ارتباط با مشتریان
: ۱۵۵۴
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/468177" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/468176" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468175">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سازمان برنامه‌وبودجه متولی جدید کالابرگ شد
🔹
معاون اقتصادی وزارت تعاون: براساس تصمیم دولت، سازمان برنامه‌وبودجه به‌عنوان متولی اصلی طرح کالابرگ الکترونیک تعیین شده است.
🔹
تمامی نهادها و دستگاه‌ها باید برای اجرای بهینه این طرح با سازمان برنامه همکاری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/468175" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📷
ائتلاف سعودی برای مرکز نفت «الصباحه» یمن در صنعا هشدار تخلیه صادر کرد
🔸
سخنگوی نیروهای مسلح یمن در پاسخ گفته هرگونه حمله به صنعا با پاسخ کوبنده در ریاض همراه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/468173" target="_blank">📅 16:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1438fa524c.mp4?token=hnjmi5SxSaAUw7fmoE_LPxSzE_XA_foCgvSvMs7k5E8kUNJe0LweUUFBS7Z_teR64h5yGinfL31Qg-iBYxVmUiK1dDklCowqSo3vbck5w6vwuAaXC7XBf_uL1jy2TjSr4uVS-JumZGCPeXZ9yQdNclAxYAJZ429IFZ3C1LKnAhnM46nxUKEZX9AkfJlMiEzsZsUJm8aW1akWc0OHUC0uGulCodRdvMoMiLEMeDD-nwZ8cqyKXV_oMiTqtlI0kI0YiKEzQRDjJRubW5_EzhJnj_uv3ZeZsKFxZLU0c2OfmvFh5v8QU1ikkh1WaJqT_g4NlbZEgY6wHhIDlzo0r4Ln7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1438fa524c.mp4?token=hnjmi5SxSaAUw7fmoE_LPxSzE_XA_foCgvSvMs7k5E8kUNJe0LweUUFBS7Z_teR64h5yGinfL31Qg-iBYxVmUiK1dDklCowqSo3vbck5w6vwuAaXC7XBf_uL1jy2TjSr4uVS-JumZGCPeXZ9yQdNclAxYAJZ429IFZ3C1LKnAhnM46nxUKEZX9AkfJlMiEzsZsUJm8aW1akWc0OHUC0uGulCodRdvMoMiLEMeDD-nwZ8cqyKXV_oMiTqtlI0kI0YiKEzQRDjJRubW5_EzhJnj_uv3ZeZsKFxZLU0c2OfmvFh5v8QU1ikkh1WaJqT_g4NlbZEgY6wHhIDlzo0r4Ln7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سپاهان در دقیقهٔ ۲ به ذوب‌آهن گل زد
⚽️
سپاهان ۱ - ۰ ذوب‌آهن
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/468172" target="_blank">📅 16:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-sg5Z5jAOQcmMq5bQsDk9AqlCv9cwLM5ci7d5x_JM-PuJk_KiMGR_UkMfGbKskOd8psqom1GWfRJrNbSgTAu2lfTbOsRC_Rs_5_hb-PSaKsUt4_TGYC9wCKPSLyl_o0bIVKWKd4nNSnLbJ6Y6jowLQVcmVb6erUKuCicCQzeDCbT5kdzO_XzhXbiDyLUyWPS-eXpaIYFu4x_nbevtij1zwpOw73b857W9qt5pYRHmQulv2_UMCjCfGpOpPU8y2yY2ZVQVkJnNPUJwJ99yHQKMBmMAimUT-tHZ0llqwzZd1qHoBhl7ZBPVOmITqVyBjxZkOfw2JJGnrx0IgNTfIlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار ارتش یمن در پاسخ به تهدید عربستان: به هرجای صنعا حمله کنید، پاسخ دردناکی در ریاض می‌گیرید!
🔹
سخنگوی نیروهای مسلح یمن در پاسخ به عربستان دربارهٔ حمله به صنعا اعلام کرد: هرگونه هدف‌قراردادن صنعا، با واکنش قاطع و دردناکی در پایتخت دشمن، یعنی ریاض مواجه…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/468171" target="_blank">📅 15:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
فرماندار مینودشت گلستان: جسد یکی از مفقودین سیلاب کلاله کشف شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/468170" target="_blank">📅 15:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e555ede2.mp4?token=EbeQoCeOSAJ3KCpT07G5e7K4okPbDs7x_ADi-gbKxATpZ8C3DblrTRgBZ1yNsXKC7K5vRgdqR4GTtnLZI22yM1Vc4ZmgKUVCLVn93oXKOvzf4qCs1TzMmpsLmYoBAAsjbaH38LHuhWaXewYllB1jipPKKrDGY38tvf6k4zd_LgpmvKdSp37GYz1-hkjTD3lbVHPoP3HgH-fUXi6WNZJgD-M9qUI6Q7cFCU5K97AIYs1l8Z7GZufIgnuw-9rgNlQSsVrGCKL7G44ONjp9kSs770XYVlgHn14wwGTcr_VXn23zKZi6HDsHYHf0PuZdFXbaBYApOFit79z2iYZME0NGdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e555ede2.mp4?token=EbeQoCeOSAJ3KCpT07G5e7K4okPbDs7x_ADi-gbKxATpZ8C3DblrTRgBZ1yNsXKC7K5vRgdqR4GTtnLZI22yM1Vc4ZmgKUVCLVn93oXKOvzf4qCs1TzMmpsLmYoBAAsjbaH38LHuhWaXewYllB1jipPKKrDGY38tvf6k4zd_LgpmvKdSp37GYz1-hkjTD3lbVHPoP3HgH-fUXi6WNZJgD-M9qUI6Q7cFCU5K97AIYs1l8Z7GZufIgnuw-9rgNlQSsVrGCKL7G44ONjp9kSs770XYVlgHn14wwGTcr_VXn23zKZi6HDsHYHf0PuZdFXbaBYApOFit79z2iYZME0NGdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل سازمان هدفمندی یارانه‌ها: منابع مورد نیاز برای افزایش مبلغ کالابرگ از سوی دولت اندیشیده شده و این مبالغ موجود است
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/468169" target="_blank">📅 15:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACx3CWpRU_vmdL-qPSIqIZIc2ms2d3jJHy1WMVnnWyUBiSoZpNsVBo5fLDbf2kt8Nmj0RND3ldVRpq7MndTmNlDAUfFti7-KKWM4NRYV1i5rTjj3st4c9vonWKQQ6encipskJa4xAeMCHCyoFDU2KMKW0ofAK8KCiJcDVNRVAw6Sf4coi9Wo_2QuqXE_wGv9__-caVl5d0-yiwvZhHEPuMD1tlyud2Vlu9C5l8B_6gJCKICobC8Fu5zt8YkkkhnLAc5VLwrvHHQ4USBz8dazlQzuXBQ_-_VX8K3KswFdACyXNi5LNNcuSSuDpAKDSe2-zAaESdHHaCUES2VUuKisfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار درپی حمله پهپادی به پایتخت عربستان
🔹
منابع عربی از شنیده‌شدن صدای ۳ انفجار در شمال ریاض درپی حملات پهپادی یمن خبر دادند. ائتلاف سعودی هم حملهٔ پهپادی به این شهر را تأیید کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/468168" target="_blank">📅 15:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468166">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شمارهٔ ۱۱۵ اورژانس تهران قطع شد؛ با شماره‌های جایگزین تماس بگیرید
🔹
اورژانس استان تهران از اختلال در شمارهٔ ۱۱۵ خبر داد و اعلام کرد: شهروندان عزیز در صورت برقرارنشدن تماس با ۱۱۵ می‌توانند از طریق شماره‌های زیر با مرکز ارتباطات اورژانس استان تهران تماس بگیرند:
02146015981
02146015619
02146015948
02146015734
02146015732
02146015873
02146015613
02146015703
02146015648
02144896391
02144891399
02144891525
02144896345
02144896376
02144896389
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/468166" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac849176b.mp4?token=NOHRD1wtnVZkB4joMP9u05mvs6RmXpNIQLwyXjbbnMzCev2j3HsWR4Eujvs3qj5t1JK6kF29Kqghjc6u3ystsrKVkua6ZFi6hzc2llwcss5eiE2ZQBOYStMhM5fwS91ESIYtiqID7F5H4A9atl7jFckMmG90iTpofm_QVRbvBHBsYh3ExZH5_HIrotXFhXR1pSNewd4pUBjWmf9Mc5lc_ezgf9YIPH8euJ2jCVAX9lP0Vu6La_67EM0Tknjsw5yLIFa3z7guQIgXInWngL_IdrIJggQQFsjMBWJiVoxQ_Nxj20jN0Ji-3TkIyVnK56cDSkF9xHWyAzuIz4_trT4pGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac849176b.mp4?token=NOHRD1wtnVZkB4joMP9u05mvs6RmXpNIQLwyXjbbnMzCev2j3HsWR4Eujvs3qj5t1JK6kF29Kqghjc6u3ystsrKVkua6ZFi6hzc2llwcss5eiE2ZQBOYStMhM5fwS91ESIYtiqID7F5H4A9atl7jFckMmG90iTpofm_QVRbvBHBsYh3ExZH5_HIrotXFhXR1pSNewd4pUBjWmf9Mc5lc_ezgf9YIPH8euJ2jCVAX9lP0Vu6La_67EM0Tknjsw5yLIFa3z7guQIgXInWngL_IdrIJggQQFsjMBWJiVoxQ_Nxj20jN0Ji-3TkIyVnK56cDSkF9xHWyAzuIz4_trT4pGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت نفت: تعمیرات اساسی در میدان گازی پارس جنوبی ناشی از خسارات جنگ تمام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/468165" target="_blank">📅 15:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468164">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b593f2b44c.mp4?token=ebunEcrdvuaTV5UxllNCqveD4cW8uby1nj_INKOUOU9VA0htND56HTkc5DAwVPUKX8i_21PZRGJXyLsxVmEr15CbTLRBKehJEAUzHTmvzNMWX65VDT4rWMIWPPbPRbaL5sm22WZFeSBF2hBpanEYwgYaukZUXlDZgBlofyQ8Wnmp_CQ6ffcLwjQafJuOxrgJ9PDnp-F-aGvAvU10Pcq6VOoxSOqn1TwsLTyInKfBsIwCWRtAv6NHiPRLhUuLLzwZ2gkXFG7bPbLQC_g7a3EMEdyVTVhRWMrzIZ6ma2k5D9W1honr_MFjGt8r89gDmjaXbpMemV5Zep5nZwTVDSzaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b593f2b44c.mp4?token=ebunEcrdvuaTV5UxllNCqveD4cW8uby1nj_INKOUOU9VA0htND56HTkc5DAwVPUKX8i_21PZRGJXyLsxVmEr15CbTLRBKehJEAUzHTmvzNMWX65VDT4rWMIWPPbPRbaL5sm22WZFeSBF2hBpanEYwgYaukZUXlDZgBlofyQ8Wnmp_CQ6ffcLwjQafJuOxrgJ9PDnp-F-aGvAvU10Pcq6VOoxSOqn1TwsLTyInKfBsIwCWRtAv6NHiPRLhUuLLzwZ2gkXFG7bPbLQC_g7a3EMEdyVTVhRWMrzIZ6ma2k5D9W1honr_MFjGt8r89gDmjaXbpMemV5Zep5nZwTVDSzaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: شرایط برای بارش در نیمهٔ غربی و جنوبی کشور مهیاست
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/468164" target="_blank">📅 15:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468163">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xej_j1pwAjpKCahOIXM_dFNYvkjbeU5Fkw-gTHGxcp04N_Z_CgDMASJZBmsT49me5gHrzZ2oXamCsgpGZ840XmcTNHPbjjYN_GWQKmxZc-q7KLj2McMKQpC_hWZNTymEUQn1hO9Apm24uHAOo0wppvrviaR0QL1shWQ7qMXgH7vIYhY3PBOR09iNFDWEdDu0Gf30DJO7YJedk4_QE-rRgjqeXT0sx2r1sV_FmAXwD2ct5OviXeEhO_vOn-JUkwBN_aSy1jqTLQ3Lz6zir6LNe8eMrmqFto-uK4zJY566J-f139ku2X6LQZ4wBVnW0V8tGBXhFD3_RixqU0M0_TDM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس من|
موافقت وزارت بهداشت با تعطیلی مراکز جامع سلامت تهران در روزهای پنجشنبه
🔹
درپی انتشار گزارش خبرگزاری فارس دربارهٔ اعتراض نیروهای بهداشت دانشگاه علوم پزشکی شهید بهشتی به تبعیض در تعطیلی پنجشنبه‌ها و فعالیت بدون دریافت حقوق، مدیرکل توسعه منابع وزارت بهداشت از ارائهٔ پیشنهاد تعطیلی مراکز جامع سلامت در روزهای پنجشنبه تا پایان سال خبر داد.
🔹
چند روز پیش نیز علیرضا رئیسی، معاون بهداشت وزیر بهداشت، در گفت‌وگو با فارس اعلام کرده بود که موضوع تعطیلی پنجشنبه‌های نیروهای بهداشت در دستورکار قرار گرفته و به‌زودی ابلاغ می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/468163" target="_blank">📅 15:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار درپی حمله پهپادی به پایتخت عربستان
🔹
منابع عربی از شنیده‌شدن صدای ۳ انفجار در شمال ریاض درپی حملات پهپادی یمن خبر دادند. ائتلاف سعودی هم حملهٔ پهپادی به این شهر را تأیید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/468161" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64be7e8a46.mp4?token=k4UCplyme2Xg5nQU4LtGJs9iSAM7KJF-YOjbFHRtqpchZHZGSPNLOOk-Ak6xJ-jZb7-RPtI2K3Z8iTE3v1S_GgvNVQfMEaCYh6OCWltdS8BznwTtaDbVgIPZXQBY_NswLrBVsh_KCVrs4PzaQHRBtR5Lmbz45iDP889DWkE-XXydHZoT1XUPRloDqrirCAxJ5K7s7fvQZbaXOEYwkILyLjCaYbfZqp_JBAVX9nQ_PR3OFrYv5F5yj_8LePbkOAHGGkvEPtZi9p1zop06qD9HlZDK3Vl0lKBdFIxW0qrj_V2xMBNG3h32prWCwHBumL-P03fG4VLI5udKdOBvzyB6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64be7e8a46.mp4?token=k4UCplyme2Xg5nQU4LtGJs9iSAM7KJF-YOjbFHRtqpchZHZGSPNLOOk-Ak6xJ-jZb7-RPtI2K3Z8iTE3v1S_GgvNVQfMEaCYh6OCWltdS8BznwTtaDbVgIPZXQBY_NswLrBVsh_KCVrs4PzaQHRBtR5Lmbz45iDP889DWkE-XXydHZoT1XUPRloDqrirCAxJ5K7s7fvQZbaXOEYwkILyLjCaYbfZqp_JBAVX9nQ_PR3OFrYv5F5yj_8LePbkOAHGGkvEPtZi9p1zop06qD9HlZDK3Vl0lKBdFIxW0qrj_V2xMBNG3h32prWCwHBumL-P03fG4VLI5udKdOBvzyB6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز آمار: نتایج اولیهٔ سرشماری ۱۴۰۵ ابتدای اسفند منتشر خواهد شد
🔹
عملیات اینترنتی سرشماری ثبتی مبنا از ۲۵ مهر و مرحلهٔ دوم این عملیات از آبان آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/468160" target="_blank">📅 15:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHuUG3RVzRtWsNTZYDffKMRwCsT3fK73yCNR9Dv1IMp26jl5KBbz3peF3fysl038vo1vxDFagKdaBEkQOVo2XkUxHHYDTsq4Jb23GvMMcMkoaqIPSZ4bmyXxGhUAlVWNRAq5l3pQ0LJY2sNLdegKOfL-hsE1rqilgwr-Qo5-FEnbnrWQp9dyNT4TCeLpLmdh34ESmsVcQX-1bVUqibm6RZ2XovT17NRExuchLuKwjiAsUMeULca0mGO9IkJiR7IEke5bPZeW2iqVxi41Bdt8BjG9EWC3qiMW5z15C1YrmUncMywKj0d4ykz3bR-w4QnSA7HH9EB-XdCgHdDW2uJ7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور: اقتصاد ایران به قدرت معامله در کنار قدرت تولید نیاز دارد
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در افتتاحیه نمایشگاه صنایع خلاق مانوین در اصفهان گفت: تولید محصول باکیفیت به‌تنهایی برای موفقیت اقتصادی کافی نیست.
🔹
شناخت بازار، قدرت مذاکره و کسب سهم بیشتر از ارزش معاملات نیز اهمیت دارد و صنایع خلاق ایران برای حضور مؤثر در بازارهای جهانی باید توان عرضه و معامله محصولات خود را تقویت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/468159" target="_blank">📅 15:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468158">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1902b1ff2.mp4?token=bXy9FnmcfoIXvTrhEUTrGyvM44_XHyFAMJYap-7FT8J7FUtSb8XJsD9E7sk5go8SgEqE370ojr9dNv8kcXH8hk_tWSVjMZ5G8fevPQ2MaZfonen4_GbOQdJAISUOndC5hhEq9jDuzLm1gWWNOBo_8tlUCfVuRJ_C4QpYNX6DBE4YyWc-7Cu22VvuEiXnjA037zfPZuVIJdULa7Nofs10ih-4OiIejDEn_GD3dSrp6CpiXyUyvmPKA0wL1D-yjBd8D2bHE72KsJo4vlrOYwPZMyJTxu-dOnkrTfdCfPdonHfQoxfEgf-qPRHRkOGnOpFam0ONSlffi5D1rKCEZvBc-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1902b1ff2.mp4?token=bXy9FnmcfoIXvTrhEUTrGyvM44_XHyFAMJYap-7FT8J7FUtSb8XJsD9E7sk5go8SgEqE370ojr9dNv8kcXH8hk_tWSVjMZ5G8fevPQ2MaZfonen4_GbOQdJAISUOndC5hhEq9jDuzLm1gWWNOBo_8tlUCfVuRJ_C4QpYNX6DBE4YyWc-7Cu22VvuEiXnjA037zfPZuVIJdULa7Nofs10ih-4OiIejDEn_GD3dSrp6CpiXyUyvmPKA0wL1D-yjBd8D2bHE72KsJo4vlrOYwPZMyJTxu-dOnkrTfdCfPdonHfQoxfEgf-qPRHRkOGnOpFam0ONSlffi5D1rKCEZvBc-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشبیه ترامپ به «سگ نازی‌آباد» توسط سخنگوی وزارت خارجه!
🔹
بقایی در واکنش به تغییر موضع ترامپ دربارهٔ زلنسکی و حمایت از برکناری او: این مصداق حرف کیسینجر، متفکر آمریکایی بود که گفت «دشمن آمریکا بودن خطرناک است، اما دوست آمریکا بودن مرگبار است».
🔹
مرحوم جعفر…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/468158" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468156">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a3859fe5.mp4?token=kvXY4FVTEs5ZmRnYqbYjhCi0WVCTRErWy329SrNdBA2BFKTjV1FRcGjpRzarIq1Z6sfCFg4np1JfltYapvIyTcG07rZoOXAuaBBTXnXR-_VUCUo2Zk34DVzChIvhnfB9aVchU3p_xqAeyESm2DpeKH6UWwO1CX799ZO04CtWJTOItEk4uER7I61_jZjC2JdXSJ2KrCOquoDNElk70V70GHuZzq43MTtIIAHMV2pVxXwTvOgj0uJ79b89AsubP9c7tL-TGPcqz3LEW2H5LZ01dfY9SYtrkXKgLa0-bsmlyuzvCXO6azyLsQIJeKLJzkGrSAw-ciVUg3A8ShlLkFHdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a3859fe5.mp4?token=kvXY4FVTEs5ZmRnYqbYjhCi0WVCTRErWy329SrNdBA2BFKTjV1FRcGjpRzarIq1Z6sfCFg4np1JfltYapvIyTcG07rZoOXAuaBBTXnXR-_VUCUo2Zk34DVzChIvhnfB9aVchU3p_xqAeyESm2DpeKH6UWwO1CX799ZO04CtWJTOItEk4uER7I61_jZjC2JdXSJ2KrCOquoDNElk70V70GHuZzq43MTtIIAHMV2pVxXwTvOgj0uJ79b89AsubP9c7tL-TGPcqz3LEW2H5LZ01dfY9SYtrkXKgLa0-bsmlyuzvCXO6azyLsQIJeKLJzkGrSAw-ciVUg3A8ShlLkFHdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل سازمان انرژی تجدیدپذیر: برق سبز در زمستان ارزان نمی‌شود
🔹
در تلاش هستیم تا قیمت در بازار بورس سبز برای سرمایه‌گذاران جذابیت داشته باشد؛ البته از سال ۱۴۰۷ صنایع ملزم به تامین ۲۰ درصد برقی مصرفی خود از منابع تجدیدپذیر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/468156" target="_blank">📅 15:13 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
