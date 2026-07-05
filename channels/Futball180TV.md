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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 634K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
<hr>

<div class="tg-post" id="msg-98326">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_tWOCzSVaGBav7-QdxxSoWZWsp10pi7KrH521nezScAGJ_WgloFSLQAnIk3IJTZ0VXa3NNEk2FSrC7MwfATIm7cfqJv1rHR2BoxHKW7_u8Dgm1fmTabvyWVZ7zMqk7t0vD1qrEpA9wYQJ78Mk4qrqZTdecTGvvHmqKBN8BD9Nwfy-iPA41WJ1T0Swba219n9g1ZIPMd1TjQYLQ6AWwtJJEKHr2e2-l1yKK6428GHTUYmAdf62ro87_hs2lVbnCjWLnpK5nYP6GKSR41cFomaxR544Ft-wdVITzFGUGbJKaKvJXFUHBVHT5YjYrC6N-5UTOu8FM_-eeGowXkXGFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانس فوتبال اعلام کرد که کسب توپ طلا بدون حضور در یک باشگاه اروپایی امکان پذیر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/98326" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98325">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو آخرین تمرین انگلیس مقابل مکزیک، رشفورد لاشی برای کونسا شرف و آبرو نذاشت
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/98325" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98324">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیکی ها 80 هزار پرچم تو ورزشگاه آزتکا قرار دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/98324" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98323">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHE0xR5nq8M058P5v25yVi7cM3j51E-vnR3drr7m50V1LirpK7kBSaKM1umyBhk8-hEmlhw9GGF1hPdsV-qu9jhlGtQmbZQXX2iZb2OTliXS7kojWHclvuIlSC082isX-XaGsZZ3HfPBi4a_-k8yC2xe5GiUszQIhPNoGhqwb1s8ms6r-3bz3du-ZyWjRjCoJHQUwzWoif5obucyeraTAgHEW3Jz2SuACQwFHN9FZZ8uM5TdrWrT2sHvupDDx_DTs8kqg21xe06HLEsoQdDO8uRXveXMhSEi48Cgs8-Wbbrr8FOkCwVTOAeC-Bglb96FVEQ_8wgIFisZQypYbcJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇳🇴
ترکیب منتخب و مشترک بازیکنان برزیل و نروژ در آستانه بازی حساس و تماشایی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/98323" target="_blank">📅 18:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98322">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EucQ3z1OcsL8A6E2oKyG5eaYiJPvpVNJbP3XLzLoPW7dZ_sWyuFbIhQfkYdjYRyR6Bqx-8FaEuXE4mP12cxo73r9CRxQdsXQat2hzGra92eVAuGm9FK30IRatYGVxfTlwLWcp1EOWRR7ftBHONOef5TVRmvjho62F7iZdCqhDULeun0CPkSSfKM4z-4FrR449N_dQryh-J9DI6tVkvaxpuYJsWnXi_dbfstRaOD69pPX_-PX9qLDIqCKxUnwm4zhgNiEBRJGnvk1028I34pxNsunfwkYEYlNxJ7sAnytzrFJCq9cmnFTE3x1TCav7l9x__m1xl57fqx2jK5djMcNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بیشترین تعداد بازیکنان از کدام لیگ‌ها در مرحله یک‌هشتم نهایی جام جهانی 2026 حضور دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/98322" target="_blank">📅 18:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98321">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jovvk8XhU6dlGWYjPhaQBky0_hFjdYSaOjOFHBsjt__RQu5ZqeNHJbAXvM7p1yZGuyqDo92WLG6WZiCGKI4OQun2hsVhjm4_lTUlZF22LC8bTLh7NnprhuXR0m3NEcSG0GExEyDdQUvcIf3OAX17fN1PQzMe8ROfAX6SnJPpe3wz39neG2kNuyhswtSgDFrBOFS7OD-73-Ivb9XB87bQnsAAaKdaq3sG1IGxkLwJoHdCB2mH1k8XEdnPFsd223I_AsiM4mNPugiJPJwTNv-VR91V6We1eoFLxo_JcsqTqF7j_lziF2HYAaCD-g869B6xe74MANUAaJAhErAdIrA-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه الاهلی عربستان در آستانه جذب فرانسیسکو ترینکائو به عنوان جانشین ریاض محرز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98321" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98320">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آماده شدن استادیوم محل برگزاری دیدار حساس و دیدنی مکزیک و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98320" target="_blank">📅 18:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98319">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
🇧🇷
هوادار برزیلی و آرژانتینی کف مکزیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98319" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98318">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98318" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98317">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
👤
⚪️
#اختصاصی_فوتبال‌180؛ در صورت حضور مهدی تاتار در باشگاه پرسپولیس، جواد نکونام به احتمال بسیار زیاد جانشین وی در باشگاه گل‌گهر برای فصل‌بعد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98317" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98316">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD2smHWO8AKjH2V4M7NKFOquvojr6_lV1H-V-zvEX0u58GpNRmbGHMz3JRtEVpOoQRnIR928z2Wy_ZUAp3uGaRJ5vn7ZjuaH9qRuKmMob18ALjvJRoc4l1kEBIZAeJWzf8j_k1pgOsFeRaXupBMaOZRpvgx61f0wtuniNU7Je1RXURKMpEdMPgOkoT-4_V-40yC6C2VXQWhs1RUZmSJUNgw1-ILVXlwczaU_w2wUbd3Z5QgMFvy7mU6YoPOJlEy8XmH9QssfscVt8m6YQVsxZDrBNmGRtS9Zf0vMSRzoYq1IXMtCK2ywLxoYqNJ00FqPax9IlTJuCGVCRpGyK1y0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
💥
گلر کیپ‌ورد و یکی از هواداراش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98316" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98315">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcqEzPzJTxW3MCkvJVgb3LELmLm0nWXHmeu4u0CNgb5RPXZ5yZF7ZKzC1OLyBuzAmWtGJVPguLG2J2WOX8pkw4TyLSdIHnqhxClyMMWGLc9_0zlgFypZXhPOhVCTGzmvHv98CoYZpbZAcXYpiQ4EcO-qNjS4MVZDa-jxizaomoqepJXEd2d8TUqGFWMf5AdClBeELX9KqstRLOrBqJSGr9F3V0VgfCtDMVxXJlyK6pJpvqh8mTyS89rbTbAtog391ahUvDEOGsqSNcJ6y4Pv66KmQhQ_kg0oJLI-jOv6CyQQ1Jyvf13aoq0SAavY9XQDg1Mqye-c6zDo3s6tnRr5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
دختر اینفانتینو رئیس فیفا دیشب حین بازی مراکش و کانادا با کیت مراکش رویت شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98315" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98314">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇻
بازیکنان کیپ ورد در بازگشت به کشورشان مانند قهرمانان مورد استقبال قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98314" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98313">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
هواداران مراکش پس از بازی با کانادا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98313" target="_blank">📅 17:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98312">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqN-NiPDiz5v4olc0DtaoSr5cLjkMgQl4yacAVAj47EZltHOmOnxku3nq_C596-JzYVCuTOz8iQXVU67ydAI9mXJsDNXfDfLradCdZJ91iYxmu3-537N4t2AuWY13Xzxr9_fRalXvl5-pG9pXQoZzhQlUztsXqqSEGK65hCWo8-iiwjLyrxf4Laqqv_tcK6jDLfgH99ME7g6Wg2XPSxi_EW21wIYn_hwxeFTs5D5lnBlu3fO6mRo-s-bRv2VnN00GFU83UmikELjnzGnLORl-ZfGTaQUdm8fWvOXM4ipW0ZEAqQ9uFec3JJzIU8pZvWB160IfSn6WZRmkFSh0xr6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
دشان، اولین مربی در تاریخ جام جهانی شد که 10 بازی حذفی را برده است:
— در سال 2014:
✅
مقابل نیجریه (مرحله یک‌هشتم نهایی)
— در سال 2018:
✅
مقابل آرژانتین (مرحله یک‌هشتم نهایی)
✅
مقابل اروگوئه (مرحله یک‌چهارم نهایی)
✅
مقابل بلژیک (مرحله نیمه‌نهایی)
✅
مقابل کرواسی (فینال)
— در سال 2022:
✅
مقابل لهستان (مرحله یک‌هشتم نهایی)
✅
مقابل انگلیس (مرحله یک‌چهارم نهایی)
✅
مقابل مراکش (مرحله نیمه‌نهایی)
— در سال 2026:
✅
مقابل سوئد (مرحله یک‌شانزدهم‌نهایی)
✅
مقابل پاراگوئه (مرحله یک‌هشتم نهایی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98312" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98311">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
🔥
🔥
▶️
🏆
برزیل
🇧🇷
🆚
🇳🇴
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98311" target="_blank">📅 16:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98310">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6IpgpBlEmUda0DhgZiKFGzH4_CEBqrW2q9sYNuCm_mHpGg183cIaSbgv1y8iZYAgfJCEewnroVhtPbVTqKkk9mVFyVALzSJkKfZkf9JOFYFbSf6ODCwsufa3-SDUCOXDuLW91PxaIkwqAS1HhQVUiAJd03Y-1lczg8d7INb9V-pAvnHDxbNTRLI03UFd-4N6rCIzVmTjtK4jxPrDE7RVwdFFtVc8E3PlWZaSYSkxF8QQsenXh86X1OCSGLdOFiGavkq1zN8AllmLIiVNp1Qivr3lelgiSPMJPJjzWEdc0DkI6GD_70ATwJRcTAYXoViGBX-EpGua2TkY_Uh4cCb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
📱
بیشترین فالوور از بین دروازه‌بان فوتبال؛ گلر استثنایی کیپ‌ورد صدرنشین شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98310" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98309">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyh8UmyoFTiOMZDcMEpE3TXxLfgrkSlH3r-lpXrVBSutja2A28Bga-xwY_AxKsXCyXDJ4qsO99r12ER4TkSpEE_uUmTH6bPDTLT5_Q_97VewGM1ooRkoP_zC6XnYJpgRyRQLeLkZiL5X1pVl3-RB9pQBHKOgki7eQR93d-HnFim5fPSPGz61waBwQfb4500MfRyCQaLpFPyDWH5pkfjR9oHhDEa728pE4VPe217Np0-3WpHTOn6gAn1CJNYqTO-aPqdgQRlGjtvzQQaZqsbHX6BQZpAQ4qUPZg44GuoC_FvgMYAk3s10i4zFQ1yWn-FlUmeTCuVf7NH6mJLtW32mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🏆
صفحه رسمی مجله فرانس فوتبال
:
امکان برنده شدن جایزه توپ طلایی بدون بازی در یک باشگاه اروپایی وجود دارد.
👀
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98309" target="_blank">📅 16:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98308">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
انتقادات شدید مجتبی پوربخش از رویکرد عجیب صداوسیما پس از حذف ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98308" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98307">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuA_4gqxMSs-pzxNn584Kryil4aNBRlnPpMDczuxmXVyfsNNP3YF0SuGZxNGZEehvNk7UhqDnQyEzDgUTbk9eSws-l1rRDLpsmOMNBK9GpTP0e77Q3SiqshfxY8lJdp84EZnoK0hoZTVDyToo_L0UYVh85Wz1SXJnlpAVom-jnp-wgy4v1nIDU8k1fgzaC13MURm1_WAg1DL5Sh_ut4iI-C20CBTQ34YO9g-BNtDKTZAWvUJjU0YHu0EQmxNwQh7sMpSlVQKoM2TJqBIvMERYr5QiadJbKnfrkl5CzaDolCf9UorzRt7NmBAAEWXQFLcizBUCMoPc7LK8QX2iMjXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98307" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98306" target="_blank">📅 15:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98305" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaXN0KR8xhTxhz2GTBQYQKGIFYKFouASZiydjQFQ1EK723h2kPY_3GRoqH-7N-QG5DuNEwgVwlxnqo2FxdroBWOxDNLOi_bjezE8enB4yxmoRHoUXJg09a28jYvwZRMqZBRddCReuOctCloC-1y8iT7sDT3R25THmFfqVbW_o_wOOUalVree-jAScaRMzAmBF085wXBwARaMxt2jitc9c7Tz4ACQU4o-zcA4aMmPOV9v24qEAQCOJKTkjp_4XbrSmyZMzxNhYfdLTxHGTQk8wTX3WG9U3kHtK6JPd6Xl2vnHEg0YkoTRUlBOtYG4mvMiNFO2-9mRcESmarx-DLU3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
یکی از دستیاران مهدی‌تارتار در گفت‌وگویی کوتاه با رسانه فوتبال180 اعلام کرد که مذاکرات پرسپولیس با این سرمربی درحال انجام است و پس از توافق نهایی با گل‌گهر و در صورت رخ ندادن اتفاقات عجیب از سوی بانک شهر، این سرمربی به آرزوی دیرینه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98304" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
هرچی از این سیو بگم کم گفتم. گلر تو ۴۰ سالگی اینجوری جلو مسی غافلگیر نشد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98303" target="_blank">📅 15:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98302">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek4y4_dUdF0nXxBKmDg6YkDXROBBs3OnlLOL-4LeUYqoMKiwn2m4DzctPj3KgMdYcrEZTaJ1g8WDM-DqlZIGbLa1lwUMNJmCZM5XpfMudLfyMq-VVn9MMNQVWIX8yh4nCQ4nWylgUcyBRNn6tE8wqFYydLTtdhl6Jkqn8C-itHNmUxarS1B2JcIxwkIwUaqEHZWdWXD2RgkQbMon11Y4pY9qxmBBBsugqK172jFssRoXn6q-zHkGEHkrFsQSngzMEm6U7t5XN2YLBZWdQfPnN8JxDXRUtd6Haep-53W3-uR9hbeuqNBL_4xrb9EBCCczeQim8SKDYy-1RYAZAPJotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل 3 سال پیش تو دسته 2 پاراگوئه بازی میکرد و با درامد فوتبال از پس هزینه های خانوادش بر نمیوند
حالا بعد 3 سال اون دروازه بان اصلی پاراگوئه شد و مقابل فرانسه و ستاره هاش فقط از روی نقطه پنالتی دروازه‌اش باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98302" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98301">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98301" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98300">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98300" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98299">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق کیپ‌وردی‌ها توسط هواداران آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98299" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98298">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=dJ-wUf9a_Sw06UvxyZoRZBH9TNqcXwjsz3yRVgVGjL6M9MrLVmoSZQNaUzFmUNkb1xv0iRLHrvoCezLZK8P4za1QCPWxZXgdQcFcXar6FOXLSArH-frrEeOwxyhl6-_e5VyVtDXVLA_M14D-k7Cyozfui6rH08Ln7Bu3G9M_n31OmdA-oWUZypB9OAUaUILD0TrK0ilS5HD6Geq7IM32ghWvrjMzZAVA7gdg6GnsBs6Zg_nUDisDZZHamCqBdCRPOVpLubuFbLpweVBkCLUZ_Gpoed4EfG9gRWm3YykX811G-6KOxEnAZo9e0euxQOBewm-0Mr9X98j2okZV88CQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=dJ-wUf9a_Sw06UvxyZoRZBH9TNqcXwjsz3yRVgVGjL6M9MrLVmoSZQNaUzFmUNkb1xv0iRLHrvoCezLZK8P4za1QCPWxZXgdQcFcXar6FOXLSArH-frrEeOwxyhl6-_e5VyVtDXVLA_M14D-k7Cyozfui6rH08Ln7Bu3G9M_n31OmdA-oWUZypB9OAUaUILD0TrK0ilS5HD6Geq7IM32ghWvrjMzZAVA7gdg6GnsBs6Zg_nUDisDZZHamCqBdCRPOVpLubuFbLpweVBkCLUZ_Gpoed4EfG9gRWm3YykX811G-6KOxEnAZo9e0euxQOBewm-0Mr9X98j2okZV88CQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
خسرو حیدری: یه بار تو تمرین تیم‌ملی سر توپ زدم کی‌روش نزدیک بود کونم بذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98298" target="_blank">📅 14:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98297">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH_iMm_2je2gvNdcxuAMJFMq03UNbRuzNHYmxdQxN3xtXPOUjtM1XjGEUMmh6JYLwOMIA6YWdopN_l4R4ATp3wHu21VIw6ZnIqFVWkPWRgCLFNCEI4BkL1MXmzZT0YOMjTtxKf-ZKLSbEHzfOSVBMyRUwz-jUogXsTGeKmKHsWfWtdYQFlX4QPZJSFIaQoOSjWGOy8RFM04QSsDmqE-3QgQrcnOQvEKZ6dUjrpQqkH4JtgZZx1JOpvHjrvuGB5ikMoALBQGvXR4C44zHnhbzJrw7K7pgOI94CAN5WShU7YvvusOHjo3aDYpAhsWEYdrYFMXRGwjUFHNL925d5FuLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
محمود خردبین اسطوره پرسپولیس و دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98297" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98296">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj67DE_06XHTjDitDTe_2iaEQDxnJKfCXn3RXAF7Citg-r-czqoiWeb3lEYUH_0ZhIDkQwMB-EeBqDuBf9MIPPhjSukQDiVNSeoo7tkm0yEx-HZakoFdnJ5IPll-RXgzPetjJ7HhzFqJrkd0aqRPl5ScYQrrw4g-WzyLpq6yjEi1LX76I8oZ2EkeIsySSWPqmcI15DZsQ0tMR4OvQ0JbBD8G1cbxkfhSh7XnslrGSPGsJCSHPubyXPPzOIdpwXMVioCvWh-KprbItMKmFuTgjs2hVDVUR94o20A86wAVfIToMDXjUlm-yUofCtTj9KlKw1OUuLYlDHO5LvEd302sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
پیشرفت چشمگیر مراکش طی ۱۶ سال اخیر...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98296" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYEMmqfSHvCfEqSXkEuCpf04m-ZiM11aywuh1QYNskCOxw848X3qRzUiM2b_5SVG6vFIiiLjKF4i7UpVEX30AsD9Ccqr2My_7jQMfYsybOI5JVk92ReKmUm_tD4dSUbJc3U0im_5rlsICb0W1FOZiwhfpjb_4owSBck0It2jrm0ZI_raKzLo99yTXXiSsS7vaIugUflRcYAe-F_Ay8Z1NJ_w4-ju42ik0Ahm4K9m9S-tCDta0EBb8sYvfPpcxsozBGv-g-Nnd5g_TcahzpGshN2c-yuwnZG0bSooRdBYCS5KDKe2n29MCcFxon1vd7sL5P1boZKHqvfKYz-8DaqXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گریه‌های علیرضا دبیر در مراسم علی خامنه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98295" target="_blank">📅 14:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqWP_FYf3MAJVSzpaTwskltNVFU0PytGzXGDrnq6XzXTr2icrLn6cc-2enUDWJndpEc_8pL7S6_4SiZkIobLoFGQ54fJHhvThe3k7YtbH4tuMOCwblhsMcUuQzLdqAnmBRRB5On9QGibB5eJ9CNdTJ-SyO6S1ufukH6b1GTbVme-VK8QHOxwP0WZ6d0340xvmqeuNG_lns2SbW7Q_XSR09RSnDh9gkZLxwwBRoE0nTqsQPsnDvAbvVpkH46tLY_FKaR19oGXO8i9416mN40p1jf2OC-HYswu0JVw2VR9qVv0IOsPwDiratOQuQHEpKB3joLzBAt-kL1FG39t8MuJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ دومفریس مدافع تیم‌ملی هلند با عقد قراردادی به رئال‌مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98294" target="_blank">📅 13:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماجرای درگیری معروف علی فتح‌الله‌زاده و مجتبی جباری را یکبار از زبان خود فتح‌الله‌زاده بشنویم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98293" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP5MOl29kAnpu1nvU9Lgqa7iXwDMgEawYVEXuTSJ2IL46-gT41rSTIJFE9mNMgf7o_4J5iNQvKuwu0k4fpQsIVgnZx14ONaXXnw45O5eBVXYeey73106AkMTN30HI3jj90jVpFCyj0BpShKjtt1xNblecCnjJpbRhQg60Gp5fwiGleCbpGIiDUuXTq7YitjwiQX8FPiIBx8DalBBOH9oB8RlM2WC9twXNQyp_c5cmsxA9mcy_FxJoeOfRkcYJ1qhmmcOR3HnFviONseN0_7Hib-_g7r6m2aLeBs2AziJMUGRLjaJ8oBkFLkxBUNdFp0ItMnOFemrRMNUT2n11MeWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کلوپ به عنوان سرمربی جدید تیم ملی آلمان انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98292" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98291">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=U4B7T-9-RaQDrwVtLCd4fzHsh5TS48mARH31SXRB6kRpGcEGpKSyIpW8Me5dz7qAGoyCEsVXgfhhx9Z-IFkJ2vKHNi5zv1GuZi0k60AOx0686_G0Pch7M6vM2KRyeFHYB_gBWxsSTEdHhShtnPypekT1tlUQYtpOGqWiNW7jDlOSRHqshj5AZgPvkblbjHnx-iENapl80fjaCGgGPZ55URaCfqzEF-0LrsZT1iLUCsK8FweziaXYAneSBArUFeIMe68PCJ3frZEWMt9hiWLEIa7jKF_nJvUAlhScigOMjpeGFGtl_taivoO5sVN_1Xdq9MbSTkgjotsaRxbAox8RHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=U4B7T-9-RaQDrwVtLCd4fzHsh5TS48mARH31SXRB6kRpGcEGpKSyIpW8Me5dz7qAGoyCEsVXgfhhx9Z-IFkJ2vKHNi5zv1GuZi0k60AOx0686_G0Pch7M6vM2KRyeFHYB_gBWxsSTEdHhShtnPypekT1tlUQYtpOGqWiNW7jDlOSRHqshj5AZgPvkblbjHnx-iENapl80fjaCGgGPZ55URaCfqzEF-0LrsZT1iLUCsK8FweziaXYAneSBArUFeIMe68PCJ3frZEWMt9hiWLEIa7jKF_nJvUAlhScigOMjpeGFGtl_taivoO5sVN_1Xdq9MbSTkgjotsaRxbAox8RHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از حماسه تاریخی محمد مایلی‌کهن در گفتگو با عادل فردوسی‌پور
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98291" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار کیپ‌ورد: «ووزینیا شوهر آینده‌مه»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98290" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0306de1296.mp4?token=SFpcA5gy7gFoyc7JUddCtiBIwN5bQq3K3DCsjDUXbZGu3iDa-GEd4qcaGtSoCa_ILepqswClcRO46LhuQ7XEgg7v3kKqKpzSWvNM2-oslomSRq8eNT8AoBJQZWMIE4n5jLkt1PsA7CgNdKdzrHO39C5idMag6xbgI10chUMTXNhS9uoNF3DhxRgNBDdq5O4YYMDiU1bhna18-A6WfmkeTnbCdFFo73bR5qXMFOzNKiJ4dYTvczGeKYfLaKZ6YsF0hYjnZNCNx1r12-mW9GhFOUH12mNNi6Uk01tZngVSITM1i8POuEmL9S0KIuAk7NvyIl6WXfj_5xMbGc3gT_dGug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0306de1296.mp4?token=SFpcA5gy7gFoyc7JUddCtiBIwN5bQq3K3DCsjDUXbZGu3iDa-GEd4qcaGtSoCa_ILepqswClcRO46LhuQ7XEgg7v3kKqKpzSWvNM2-oslomSRq8eNT8AoBJQZWMIE4n5jLkt1PsA7CgNdKdzrHO39C5idMag6xbgI10chUMTXNhS9uoNF3DhxRgNBDdq5O4YYMDiU1bhna18-A6WfmkeTnbCdFFo73bR5qXMFOzNKiJ4dYTvczGeKYfLaKZ6YsF0hYjnZNCNx1r12-mW9GhFOUH12mNNi6Uk01tZngVSITM1i8POuEmL9S0KIuAk7NvyIl6WXfj_5xMbGc3gT_dGug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇻
نام ووزینیا تا ابد در تاریخ جام جهانی خواهد درخشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98289" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98288">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شادی فوق‌العاده سمی هوادار کلمبیا بعد بازی با غنا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98288" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI8ni6GQ3Qm1j2oVa8vrdR0JpFhtVg4yv2PM3Q4WH5zTYfzrVmdPvSjbwSi5e5o0JgFeor2W1rdDbLJ7rTV91onSMkFfoNscklBC6pQI3PNz3-uESdiWrPUSNgZqC0EW7NrbAlF57_BDeSIelMuGaC4zqJe1aL-4RY3nSdJsjQD6RHKXh1GLHTrNhKuqioraq2jPgYeCkS1NnGdmsZprx0weYvVzJ_RA3_yHQtLu5GltUmksKbIOCPA1057YRt29-5zYi_t7HMGdAtWOWQktojAzUJwTrF5Vo0_gsYbc1K57_8M97Ik1auV9GpIXyTNGf5XcnLC5c4dl5Zb1BXQKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffH_tjK31GGdCRUXpjb9g76eGU0VmzSsUprV2ENK0jkhDVBNwjVWcSm94RsjDFETRmoE_dSwn-8vqViUQ29fRqoxb5Wfot6Xh6jFfX_JLV8zcLBbnB7AAxJ0FqJslLWOhdmzWoa2QQbvMn8skP_u3osWErE_BGt4NoXk2eeZdNv1z1KuhjJUfHjlSTz7OHbbMBxk3ZmDCv0Z2p1eMqKh9li0F0SM1cCHLtIAddVHVMogiysDgx78FmX-vA7ZRsqi8vQ8cMkemwo7KfSQB6tSdoPWL_N4IzLpTRpuIMET08hw-PQDgI569oT9Q_dQXuklYPbdms5vad-3K3QZJHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=QpqbcB_wlj7nNHxXVv-xTN3E0WgT4ymOQ88FjLHxdhvkBLqEhfO36Fo_JBtBqOr-9ueUQiqgUPJUOLnqHX_arCqXeLAZngnreKnM7RgwRKc06E4kRihTnCo9iIBT2BAy4z9PTwjPK7Uy7SwI1pWruAdb9wRyABit1LA9y4X36w5M97USt9_BN2J0cEFOKZWQ0_Pka5Qgmp1PD8IgbSDHKZci6tFiulmPVyagqd7IHPSLAiHJXwhJ5uaHI2kiTI8P8OwyFGPrHGmCYphg48WZj9uaAnPtpZ9qLzuCjyJA-tHMT5rjOJVQOXJrlTf5XJdUS8RctAxpHZo5oTMkDbqKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=QpqbcB_wlj7nNHxXVv-xTN3E0WgT4ymOQ88FjLHxdhvkBLqEhfO36Fo_JBtBqOr-9ueUQiqgUPJUOLnqHX_arCqXeLAZngnreKnM7RgwRKc06E4kRihTnCo9iIBT2BAy4z9PTwjPK7Uy7SwI1pWruAdb9wRyABit1LA9y4X36w5M97USt9_BN2J0cEFOKZWQ0_Pka5Qgmp1PD8IgbSDHKZci6tFiulmPVyagqd7IHPSLAiHJXwhJ5uaHI2kiTI8P8OwyFGPrHGmCYphg48WZj9uaAnPtpZ9qLzuCjyJA-tHMT5rjOJVQOXJrlTf5XJdUS8RctAxpHZo5oTMkDbqKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXm-_g46rvEisb2Hi4vFXN5i6ZUR5DvZDDN8hEBiOrZdcl42rmXLyJ7xuGTvAEK3KU--OBQkPhNxnVgrUtqvRMJbMk-7QqWv4ov7TFQ3woEve7oVpeiDpEIyvQZtHxnZ-TinH2613tdFk1B5M3yDT1pv3mzFiR-RZKehUvjFCatblW1B6F6e5r55cR4tBk5Tw525fW8UVWkn9s-fesZHJYIiZb-C3ZGvTwnWyFwo-mV0ZtVBPey2oA34Yg0CkGaFlbBxoTXMUClOq4JfRgnlTSR-y-EWaYJwPheAnksTbsbwiHWmOrw-T2Pxjh2Mki8rxgarct8le6BVTU00Q46Zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=l7vmSAG11ookkqz1uvn5s0qfeMd4qLLEiEFZIfpZOosoyPuZkhIJdYKa3G972kotgW97cZwT45grs9wfk7KW9NBL9qY0iKYLIjBWqxCXHlMIkDGOMLAV2Vfq6KjweURicIiX5DFqFJ-pyT8qPU4iMHlvzWn7DAGvOyy9KWY1Jc2ORBLlJCb5GVgNXQW54G7E6P1dmfRddtgqKt_g--PbgQUTEHCpk2iwfFFe16LvCNXiMUG_7SKQ38LQCX_Lik2_zE_TBAulj8bFc46oNJutis69IX2S8iyah_jy4_hbjbIV_UQFtVDbPdJ6_3nIy_h_ttHfvOs-iKKhRBH9Btc8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=l7vmSAG11ookkqz1uvn5s0qfeMd4qLLEiEFZIfpZOosoyPuZkhIJdYKa3G972kotgW97cZwT45grs9wfk7KW9NBL9qY0iKYLIjBWqxCXHlMIkDGOMLAV2Vfq6KjweURicIiX5DFqFJ-pyT8qPU4iMHlvzWn7DAGvOyy9KWY1Jc2ORBLlJCb5GVgNXQW54G7E6P1dmfRddtgqKt_g--PbgQUTEHCpk2iwfFFe16LvCNXiMUG_7SKQ38LQCX_Lik2_zE_TBAulj8bFc46oNJutis69IX2S8iyah_jy4_hbjbIV_UQFtVDbPdJ6_3nIy_h_ttHfvOs-iKKhRBH9Btc8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=V61MjHQe6OnpN9mjXGRwiRyKbQIugTBrqQy2ypFX5FNBXy5TswTvI5asj1qewmX4FZ7QthCO8bxo0Ns7gkmPUXsVV35J1_Fx9Q4QTcgQsG8hcRdesBSn4HlinDUB-g2hoKCg5TD6wDOQ1CRIFt5Ocqd5coVhdgIIhXtdSymj9vM_EHPfyuzwBvP6cmfAVWl0VouMbc46Fmo6URTs7fIcFCTBAF51YPydXJMBN3j7z7RQmhI9Rm1gYDezJf3811wKrF955qfk2BD_zDlBr4mrTh_bVxSuaeU0w8X-GdLf6jvmH4r-7UFfEtcQDwFYwGHgN-_9h-om7T3uoT00pGZmVAmOIT_pa2JF7gQML7R_2KiqVVTyaZy7DTPejlTbS0NBKPZ13Ypi9GAv_JoLP4CafaTdVKDCeM6L2QMrM92e75aUIS0wcAqyGWuYcgTgr_rDGb_04LmbGIrFjL-yYZlnoUF62CWn5OrZX0tE21CAuRtVBdGMOHIOhXqD3oEd_33O9aCJ1X_W9ksNSAsQJJNyvfb2h8UgzSjbCuU6BliydU5vCQ14nEp-jYQkcmBIRs2i4Ik-0fGIa6J77pbk1sFIDXh2iEFb-oTGgRjqoVe1unRNJN73SFKLJyt4wlfs_KLjA1ZaKnma1lxVpFeflGBaGil_hUcD4bQf8gcIVce7Qm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=V61MjHQe6OnpN9mjXGRwiRyKbQIugTBrqQy2ypFX5FNBXy5TswTvI5asj1qewmX4FZ7QthCO8bxo0Ns7gkmPUXsVV35J1_Fx9Q4QTcgQsG8hcRdesBSn4HlinDUB-g2hoKCg5TD6wDOQ1CRIFt5Ocqd5coVhdgIIhXtdSymj9vM_EHPfyuzwBvP6cmfAVWl0VouMbc46Fmo6URTs7fIcFCTBAF51YPydXJMBN3j7z7RQmhI9Rm1gYDezJf3811wKrF955qfk2BD_zDlBr4mrTh_bVxSuaeU0w8X-GdLf6jvmH4r-7UFfEtcQDwFYwGHgN-_9h-om7T3uoT00pGZmVAmOIT_pa2JF7gQML7R_2KiqVVTyaZy7DTPejlTbS0NBKPZ13Ypi9GAv_JoLP4CafaTdVKDCeM6L2QMrM92e75aUIS0wcAqyGWuYcgTgr_rDGb_04LmbGIrFjL-yYZlnoUF62CWn5OrZX0tE21CAuRtVBdGMOHIOhXqD3oEd_33O9aCJ1X_W9ksNSAsQJJNyvfb2h8UgzSjbCuU6BliydU5vCQ14nEp-jYQkcmBIRs2i4Ik-0fGIa6J77pbk1sFIDXh2iEFb-oTGgRjqoVe1unRNJN73SFKLJyt4wlfs_KLjA1ZaKnma1lxVpFeflGBaGil_hUcD4bQf8gcIVce7Qm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=b1WMcwQnlOhmgoMuwKjD1hPmC2EBcOTsnxOU-6Jz91MpkyL51Ed-qvX8Fy7dGZBkK__q3WJZcnrF_6LVcS9tyl5_OFac1b51pyE2q4Lm2PfiklWKda_0HKjwAcsYLwrYMzIXXro6OUisZKngy0zOJyYF7EYNBzysqT0LRNziU4EC8rxgaigPOxevF9AJLyf0UWSCSo1fpWNJaxLErkUZCC3HcoX7qs7dMo_GpsHCO5thVcfYoQlh0IjU9EHob7i445QODDmnfZKGVeuysPSi0vuKpYcziOwrBsOjKW5OYJRRqvMeHxxH9KdotvwxhrzagByr3Qp5QWjFlUAnTUYuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=b1WMcwQnlOhmgoMuwKjD1hPmC2EBcOTsnxOU-6Jz91MpkyL51Ed-qvX8Fy7dGZBkK__q3WJZcnrF_6LVcS9tyl5_OFac1b51pyE2q4Lm2PfiklWKda_0HKjwAcsYLwrYMzIXXro6OUisZKngy0zOJyYF7EYNBzysqT0LRNziU4EC8rxgaigPOxevF9AJLyf0UWSCSo1fpWNJaxLErkUZCC3HcoX7qs7dMo_GpsHCO5thVcfYoQlh0IjU9EHob7i445QODDmnfZKGVeuysPSi0vuKpYcziOwrBsOjKW5OYJRRqvMeHxxH9KdotvwxhrzagByr3Qp5QWjFlUAnTUYuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=LoBAX8YRpTXV_K8x7Jfj4OIBvt5F6F2MRGfxy1jJYcSpHrIEciYer1Azl_RUdKSwmmcArXFQjSvijuQHPadtzgWpVkD9LCFTwnH9eY_0mVVN-YJXCQSFB0odicEXAwsKUp7sa8RW5ncBO5q5kZ_7u_5QumX8z_sMlPn-UjmvKNKkm_e8HZ11zp62MXdaaeaddgBtgQzxHmJHgBpMr8diZdFetHV0kitG9cH0o79xNmd56MDvFc_lXaS4EeAdDnQhR5Mm5TiKR2oxdd9Yii5aj0sGdZ2nev0NG6Kqao8rj98LylJca5QEwv3j4vQOikc5HL7zfr6U-ZCvwpnlj2lO1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=LoBAX8YRpTXV_K8x7Jfj4OIBvt5F6F2MRGfxy1jJYcSpHrIEciYer1Azl_RUdKSwmmcArXFQjSvijuQHPadtzgWpVkD9LCFTwnH9eY_0mVVN-YJXCQSFB0odicEXAwsKUp7sa8RW5ncBO5q5kZ_7u_5QumX8z_sMlPn-UjmvKNKkm_e8HZ11zp62MXdaaeaddgBtgQzxHmJHgBpMr8diZdFetHV0kitG9cH0o79xNmd56MDvFc_lXaS4EeAdDnQhR5Mm5TiKR2oxdd9Yii5aj0sGdZ2nev0NG6Kqao8rj98LylJca5QEwv3j4vQOikc5HL7zfr6U-ZCvwpnlj2lO1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=ZDzfeusCPLTO-cmqItkF6EFSrS_xlvHe_q4ikQhMDUlS1kBjdeosTnIP0GRLG4XTEyw8aBP4ImHtFLycoG_F87HyPUmHIAgPVT8lanE8OkzX6Hg-OdqAR3z8D-nksEcMLL-odyKxJvl4qqXdOPkFSErEVKQSfzynpZs-CYYdYdN5K70U7Dmkj9Ib3y-TslrgT-KLCK7ql13utzwUS8Lv0_DpMO1XdaUJHvxUA3TfJF_fJUfUJW6uefDGChoBLjcfF9Y3HcakQ_6gE3zbmWb-wWd3RQn4YoYXPYkxUlR44UjN_AKGf-Fgcm3AIjKgJ-6d0lJUfrshnh6c2AagQzDCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=ZDzfeusCPLTO-cmqItkF6EFSrS_xlvHe_q4ikQhMDUlS1kBjdeosTnIP0GRLG4XTEyw8aBP4ImHtFLycoG_F87HyPUmHIAgPVT8lanE8OkzX6Hg-OdqAR3z8D-nksEcMLL-odyKxJvl4qqXdOPkFSErEVKQSfzynpZs-CYYdYdN5K70U7Dmkj9Ib3y-TslrgT-KLCK7ql13utzwUS8Lv0_DpMO1XdaUJHvxUA3TfJF_fJUfUJW6uefDGChoBLjcfF9Y3HcakQ_6gE3zbmWb-wWd3RQn4YoYXPYkxUlR44UjN_AKGf-Fgcm3AIjKgJ-6d0lJUfrshnh6c2AagQzDCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPnaXXxChmMPmVmx6VbIIVE0tvCX-vHONrF91CZ933r3ctAHIABzfxkuHmF5vWxn1uO9uKr3dt6slWdckyp8BpRNL-pp80C8EcC15O6WirOenuDvMArO3Dx-_heBjEaWxI8MlfQ15WlbpmRHPW5cgehPMoK_WWBxwY-OoAxQYCMyaAPbLB2NdPVcO_gwSNL5TSFXf3_Kik7GL4xtfuJqqzbTTeoq8MElYdUEtv5UAq2QTV2nsqw3iYhBlTC50PU5eOuuBc81uILJe9n-HKt2yw0TN4xUJ-Dft26xirxa0UDx9benoAixOMlVtnryiEpPydu_lYLv-H2LYPoW8EOFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzZGRPJBzQs5N8x4xEwrw5yb5meeoTsKMhUp6YW5U5L51F7zyyLR1b3AITyRO708-CDR94uVuuZ84Nsbnl5jcKXhW1y7QskDvHZ-zqdRmom7ZPwvcokhZBEWjv7u63XEoKKf84UJKZUb3sHEqteJoB8rbpByOAOu8rw4mIdMdjj04iW8fudS8poQCvfuwPjk1p7CNC4ae3Ks7gj4_D1by9hv2NEXf4ekbJ3b5SHhuF0zM_HcTtjZMQLQrNMgYUjHgUa-shY-QKYkkkC6OtGlSzDKm-tfBu7_Vul0aicdyN8W4uzSlrmMCcYpIL_-mBuK-KKtDIqyJjK7siMUMVccbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=bnSQ4ui52dFtqFuEqUYTfzOSJUUKpC1QNj-gYhzCJsowHL2qMaxSszmvI2IKr24PO5wlxxWcYz_PhM20x-qKm4gfYwCOv35uaF52C_DDuzzLMY5gin85wEm935m6NrmUu4bA67MxMM6qTsQNol-yBlgCinFczyu2Fuy40Mw34mvulcm6r2OaV6GdmFBNHte97xKKDivg-djy6-R6EiNECHVT-IhE-Dfgjua3kpKU16EyYFWQsvRUrq7p5uHiwgERDN5O_l21R638YoRIKEdbxuQSxqGvJ2mAIz_gGxq_nv8eTh4N-ZzgV6S1K1RZfuiiRr-ebrLDgRyHj--Y8tIoRo3NjsGBHA5d56E0srhEwWhBQ_IOt84xe1BIG8dMdIS1CFKxYy2QzZ1ppMI07lOwOQER4Pr2G8SV0yqtp7PKovPoLkoSNyeoQusUZfUk3frK6hZ9zC7_12A70Eq6i0eH5W91XXXJULNbVPB38RKrtZux9Tmkszt7Qad8YmbtGc-DQwAkmp0Tk-bBqeW4WuRtHnLeqvHPbYXj7tw7wILu15MfnWNNJnxz36Cese18r7yktvwa4iyvuT2Eg3qCFOMPyJFZQgNTrMpgo9gfH_XKvHTMobKkp3DqZ4tPQZhPWRpthgb8RIJFG6JpTFhy36fzwi3kHWTTCLh_qdfzEU_KkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=bnSQ4ui52dFtqFuEqUYTfzOSJUUKpC1QNj-gYhzCJsowHL2qMaxSszmvI2IKr24PO5wlxxWcYz_PhM20x-qKm4gfYwCOv35uaF52C_DDuzzLMY5gin85wEm935m6NrmUu4bA67MxMM6qTsQNol-yBlgCinFczyu2Fuy40Mw34mvulcm6r2OaV6GdmFBNHte97xKKDivg-djy6-R6EiNECHVT-IhE-Dfgjua3kpKU16EyYFWQsvRUrq7p5uHiwgERDN5O_l21R638YoRIKEdbxuQSxqGvJ2mAIz_gGxq_nv8eTh4N-ZzgV6S1K1RZfuiiRr-ebrLDgRyHj--Y8tIoRo3NjsGBHA5d56E0srhEwWhBQ_IOt84xe1BIG8dMdIS1CFKxYy2QzZ1ppMI07lOwOQER4Pr2G8SV0yqtp7PKovPoLkoSNyeoQusUZfUk3frK6hZ9zC7_12A70Eq6i0eH5W91XXXJULNbVPB38RKrtZux9Tmkszt7Qad8YmbtGc-DQwAkmp0Tk-bBqeW4WuRtHnLeqvHPbYXj7tw7wILu15MfnWNNJnxz36Cese18r7yktvwa4iyvuT2Eg3qCFOMPyJFZQgNTrMpgo9gfH_XKvHTMobKkp3DqZ4tPQZhPWRpthgb8RIJFG6JpTFhy36fzwi3kHWTTCLh_qdfzEU_KkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq2Z6hLoVk36Qd0_7rOnxXEh-SfAXjxXe8ZajAGBsNTt_n_J8j5hab_n3f4EqgZaqEXDaootqYA-6TtX8jCSKRqHinvguWe5AYcMqGUAYrSbnVJithFzosHfOhiGMfYiPuCDsRcAijpfdjLyO5lQTTZJe9btybodu1BAH_Sd13fR_hFuE00uv9UZXhLmEfrR375WS04zuc_30md1vQWnCyeFrf1G2eo5igaFUaE15wL7HtaTNrNWrOkMR7I3rRpojq7Pb7LE5XqGzqdCBDTbQG0pv_Js0GyFjj888hsnknxbBnBGwqR6Bz4nlJbZnFDensBSaFV2vybW1uoou6nzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX09PbAjlVk6sHo9Ft0yM4tEGmbQ0qN0c_QTO22mSe-4xpKIVQEo5UDrYhSvIg-bIaCokAwxQTZu00l5HyahwPMp7zmxQ3GHOHq-Ze81JO_RvULUK05-Ywuv5ocwNN3F2c6CR88LkR0Hg8-GEiMSioRdrJTJzAaZVHkb1gvcmT9MaODGbyOBOpzrD6pso-mL8bQjJPrz_eIQs4OQtqMw_TGTinnS40u_vP9v9aULC1nrTmFTEsP2S58gcLugFKuxLPaWq5L9otnTA5FUhgPrFkfVsBF2vrZxeCHWEHIC9jH0hz9VDAwilVZoPIS4ThoMSnX8Pdq-E0Kqd0UdlWi00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=q8ZpyDnrDQFITBLJ8PANQCqBOh5cfR6aJezo0OgIj1002zU1-_mAypxlLD47NsF85n6nXcXZa8vHaWGW6FKIA8c7rAbQq81-MZJ9mQG_t1nYfVam9D9vxE-08wcXAlbIsIj1ODhn4DWl8GnblC5VBhD86cfL5YmzQCk2Ku6KH7PuPzyqQ-EzifUnqFiDWf-qYhiAwMR2hqsCP9MVBucGwl2yAYEYmipreaJLLiPrp52sr2CfgIFUSIJwnOG1DdhYv8mCUlpKT4ejZXLXIjontwcV1D8dEYtIraE7leeE6s6IUWi-lIfbMjZcxsvxaz9d5t0Y4e97XTy3J-KQ2BrCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=q8ZpyDnrDQFITBLJ8PANQCqBOh5cfR6aJezo0OgIj1002zU1-_mAypxlLD47NsF85n6nXcXZa8vHaWGW6FKIA8c7rAbQq81-MZJ9mQG_t1nYfVam9D9vxE-08wcXAlbIsIj1ODhn4DWl8GnblC5VBhD86cfL5YmzQCk2Ku6KH7PuPzyqQ-EzifUnqFiDWf-qYhiAwMR2hqsCP9MVBucGwl2yAYEYmipreaJLLiPrp52sr2CfgIFUSIJwnOG1DdhYv8mCUlpKT4ejZXLXIjontwcV1D8dEYtIraE7leeE6s6IUWi-lIfbMjZcxsvxaz9d5t0Y4e97XTy3J-KQ2BrCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNkfh0TbQ1Z8R2txq_2rqDKbs_fbWTrDCcNyMP-I8w-qbWTEeanejl7yQ90BKrVpateGNp6i-GceS0u-0cryhTE1Ml7H7Z0f59PfpA11XLOWkd2Hs4LC2Y7D1rweXKHr_KabcwCp_8JBQpwckoTeegYEq2UAyZ5m6kLe7igIJoupXhdD0bYT2xNOGLM1cJoejrRokknv8Njg2_spy65wlbjanZ6W9AwKBAzKqKI1OoEmKl1lQrCrJ2i2pDLM05e536EKZtzrE6fxRQM_Q_AJQ9XXF-YbcxXJue3eA-obJCMtHYO4jy3_edybeFwMvmcHQqST-IjUJuwfiRuqe7ejVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB_N7EmUzPGRJIghjHockEmMlatht3QKgRiylAhmn0N10H5Mc2LB0DIPaNPd7cgwBikoOp-P2hCNF6VR_Mz52IZXP8ptIPXO8C3oUDIo4aMy0nFcuw4O7uOV8-f-W1cJUn1GKaZpMLNmZJzZVN-JSQ0bLU4btd2gLXvd3tjfMcTzgYd0X0NXKyX5dhZfyoMDMb79sSYE4dT0nfeII3SfkzGQpYq5xlG8cuCQxLcUFr9CHqWtg1S8TEDhqLbgQpUAw7W_ERmKjqrYtcFQ-Jy6p3y8tpXYqz222Ixo9p6aBmIApPJdssbAXRq1E8iEw9bFRLGY3PM495oF3TgOYkHLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYjY6rBAWbE1sXKwGegvt8UMAqlCTjFXFUPNMQNjtkRf9rbmUjbMWOKGffccOSIspJuwVjXD-rKhjATYmS2_9U57yVAJQWMfHy2zUKybcx2-qa3hE8RsBASONbWSJHcvBWZ9kwEX7ygd-Rjn8u5nMuI2zV2tQXtK429prESnCdvuMpEmrE8eo1c31PxuOdSMU2ZbpApIK51ondhL0d06wsZKFzsRJUkb8w0jHv3a8ks4YBpubrKkzYEivjVvdta3jvkwg9RCrhJRNuz_f3Bea-Jgkraw1Tb2Fzlmds628DraqGk4tSlnNj-BSyx0bF12Xw1NYWW4IWrTdbxRs7qnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqarpbxtXHsN9ym4Kk65rBVt4iGWGapiMYTZruLdlPU0ZWflMSmouJ4SHRqKBqbXenMsatQft-ix0jACUEmXuCBF8HbrfF1fhurm0XHrHX2yNW3iqb8lkjvH8XQyPiM8FlgbuR7u_h92zAkH02yCP0SKhIHhg0l0fNR9HwfAyoOQ3vI1Bwp4S2KucVr0UH2r4K4uzhoWOJ3TEmYYPB2svnHlQaDp-slxnF7_9MGP06IkZAtguLbqu4IDPvtQrMgPZz16lElIBG_K8kBvD4HFGrTZKfoND5J-vYzn5L8zOIiXQCrIrPzSDq3mV63rLiKamjlkMqfZDcs_l44QOwkVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUfP31lV1Ew316WSGkKKj8arfDl0ssG_H1Zc7pDaU_c91C_FkJq3nWY8PN6OaBTTEI9tcX2Pw4940Ttr0tHFMHkNl7QwUXorhLA1-gzY-8iumyoy0rRCuMSwGIamuecrLJ8bJ11gemMyPqxWAsalgiVs8eNMTR34DGde-zCCxx7ORFJg-mWcej4Qw5Ns4_myz_pA_eUn4vp_OMn84N6l-qEalCeaNK3u5oxTQWvt2EDPtaz-1Abdf4_GwyB9aN6csb8c8VjADp2KWw8XEfkcPYy6a1PCx6TkKYUHR50yNYvFQp3lnlzLQLkWushQDp6mepKsDGcYHIdTZ3b4wXISyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNr4qGLi1gZcwDNbmKlOvohhv-rja4Uqi2aARZ59_bViU-i7Z9ckbzC_8r3cXvlwOFUYo2f7RafxBaTRzS9hGSxXSqI_-HY8UdiOiwF5m56GMTpuRXIg-oIjSmTa1UDv7iBmP8OznAO7Xo2G7-5GSkhIVqdXCCJthTfPIsnysUhsUyMnAZH0U2SNdAADuLbvXQLWAlhQ-2Z0Z892b8SKxsUABwEq1LGsLdzGaD74POrrtKKZsbgRoZZBb1GaXy3YmGh4neHf7K8_r51ZJ0FzzKhK39mNbkS630Z0aQVgF_fs_gATFiZDqYXJP6q4ctXwGlX8yjq6g3ygIHNAenadEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ2TAuzn7pmDhN8Tpb9gNu_YOch9S2jqG3C_goPWkUfFzY7x2V8O6-EaNEAZKgySDGBdquUE62kxZlKnudpqDVDXGBAmuKBaEkl9oEqGDMZjCGCpg0l4lpcnUBQmmnkssOSdUOydpL5v12kSLtsZb8cojkl5kPlhE-glmf_zBL4ej1g6pyZ1JqZUprUJk5xfAC4PMm_Iej5qCMytFAAVvo9SYbGYOd9rGXFbLcopAdLsVpQPIjClzVYBSZE0453qwNCzocCnAlTyhYq139grHxYwTkaej7mz69ihrN3WiWvi79B0EXnxIyQX2OfXaUOxeZdiN4jViqPcsW3slCLjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMJXIDMk7Aoi2qCySeOuaCmE369EuKY1b2BqrAt8f7aI5y2PNrFQ9goooxYUnqVvbDqdKYGxS5iRQUVbzxMFegnKfUYzikBbbScos28t5mbTZ_-M2szaoyBp0wlqyOVQgXDe1fMFzuV28jnYGovY3As4SMh3Uh3TRZSEgCaJUr9G8PqNa7sTQZTfKYtwliK9lkKGLQ0QGpomhyra-4atnZgfpXR4TZA4vp7hGgu0hjuvddo18oxTX5aqwmjLR1685V_IuNObhaHQmNSGT_HhERZZSlutKJPoSrKWHbHkfObs690EnOOKeCLpxkzlkF4K45iOiVbGFxg0KbX6-0-Z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nd8nTY-mdXpThmFLHi4FNf-5R4BGJ7iKYOiKHTIae5B9Fp8mYpLhBmkXheOwIARZWKrD7R-Y_OlUTOCHaszVLC0FAv-toIxM-0-UPNZ4OoEDZ2QHljHU0A8kbrJf_OheBMkWYchIZN1voKdFTu0IgIxpnMoAI3WUbq0vwg8sBRtmX_dorQtJDkOjHc6nRZk1njmdyaxDSjYZmrnqet0WbXgq2KP0c-pwNJBhqyaYe3iCGbn08GqvWrSPLL9RoGVXDIJvXXxo67mS8WZNCBodzATUHYCRUatUDAcT6TGo230Aloam_buvlD5lUNIH3vobR14tBnuGu74UIkGZ64lbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-TrdWhOmwNDY5zJZ1Ar217urXFXjWY9N2oFB9CHgH_6Y3j8LeUglA75B3bhAalUg57GU86REC0TRD3ggmVhggLU6UM4tbm1AT_zzXcLz46G0npWc7prwtwaHTqNkNuu4-jBYCMzif6k_qXgATmiqhPrlCXjizeiJhyrowKezbrGhNxfgtGxMk6BpPlQiWeL0SZeCwlm8eYeMt-QgHNWVWrbmYwLFUb-x9QrwqOVyAmPa_1dmWGEnT32u0er6t1VWif0olaklycIkhwlAgRLWCyRnRJp7cVhULfreJYyWm6uaFAUcl1kHgPSrLzSFWkR9OPWUyyP1wVUgZ3bPmU_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GckP-t8H_43oLYGwPyB1nY1UnVARsA77DHWmVAThcqz9XTLAdVdbjfqpbKPSrz9UJVX0wO6FvmxLQegwlM9j-Pr2SZsA1W3julxoDd6-0ypRJSUXS7RmNu2bndPtPdsN1Ppk4A5JEMpfxkpMf-3FF4D2xgi_DleJR4PmfrUlk6ITv-NZNMxU2CBq6sZUdgfnASUXExYtpNzmbA5Wkx7Lv5nnS89EJok0yoNdoXZWkGknIkxv7J_SMoRfqJVqGA6KpVtIOYlQbUf0_-cAzE4B9exHJnwPIBDS2p28rm3KhxwOXdkmrGAma-hA_on9MBLufaOQYC63N6JNCym06Fm4HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1qzNY8HZVfIf_0W9OnoimYNT0Fm8v5NuHldchda3Qw7-coPTqRbfGgFmDqUTiGmeIc2TUlnG_g6zSCzetouCrTR5mvethP3vjrb0EBZdmHhG7n-TrO6b-ad2VC_8bFJF3hX9swVmva_X2Bl_DvxpbdTcBWffDfVdBjDL-mYZ-H3ambkzNefTfAfy6SJ0hhb9ZvnDEizwrVnBcmY4qQyFoyyg3Dw3lsOu_brJTqLOhnGnN0twqL845eg1L1f5No-kp5giQhaB165mAwYLTEYzkzrPdgmsmMsQ7qleO-RFAv6ziR2Aj2bJ7rwJ5xzXAaOu-QOVrtLYVH-8vhAB1cSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvGieTBhbfNKruGHoMGltv9wRC4q0H5tNHJHaFIYvhdLbjxWXgvuOEI2lvxG7uJtPB4-5SLEPBXah73aVoMQSccny9II0RW4Npg4NXZlWfz3sdjrsIL6rnvQgsTjdzqHbdHeQCc3Md4gE9WyBIsS7r05-aLiDMyxo_Aizksdolwjjf7SKnF8BhVK9FlGExTXSv3v_3qo-Y2C9u_6T3w58y9SicioukUm_WvprbZR3MCawtlzVIDkMJs4-pd9vm444lM_UJM6zXLMabJGYKUURrluTggZawxmrLoD9OQvIMENTXpmgdd0gTLe8BGqcYuH96SFXCk8DhDkKuYThrFW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/modiFEbFO1kdp3LaaoPFpYmegkfe93r-u7lggxAtW-5cZ-z2Bm7DU8W6HyV_8t7b5Y2ar8lAy-Ju3a_PyDXKWvy7mUpwyYB90lDjL5APMe02lrDrrglEdQtpMyiHMo1rgnz9wX3xLvsTLFAeI2suxGbMyZGVDQjHDysWhRDwxDdMDp3ndqi5fbAG0P8kCl635MESgpU4P-qsj5R3Ex9XH7kzm7j29utVbWQdRSBcF-J1slbdGV668EYGsvK6aQzfhp0Eh5fz8IY_MqVAW4c_xhADSWWn2wmBLHZMiwqhOYpuADggdOvgt93LvTe2Ui09a7ZICNcZga4TPzQIqpc5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmkycbjrmYEyRrw9gnxbwW0dfrQFF2zn0gzBjYkXjaoMK6rUYicFmoZKnhxJUeJCHFLh9O_aD4x9bP6X3lzOdqGNAGNZtb7lixdnMVs_AN11b9rtUarZFQA5UhBG8o3dbN_Om5l_27fmCQD77__1ITlVDzrG6QHRbnDvS2t_S2AOOvVU-aLRg8fPkmXTCgYD6jN8Sn0dbGkxzeCWdDElZ5-WXZOe1IxT5m0ASRbzJ2AVfJsTkfwX4xQqcav2-ozRV26MBBnA3HVqz3wMbRUEYU0cpCeE_n7wH1PHR0t1NTvsdy8Lm4-DwNzmAzfBZ2FGGMpd6msL2XdWqUsKjUHh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=X5vTyvkuh7xzzPHZTLstbbLxROHvG5vFXIc34MXXvN9u-uGnq-9glMwBm8N-FQtDpyfqbeIScOJoGRCyu6HNeq17zWSF8vz8QUj-bohLX8Bn6sxUJDkV3340aN4Iys5llAdSwf6hcZc0LS_ajG7wkQTV0JRiUL-zvTURfxBf9pElfsQVwyyelmaaelWXwSiAwUcZAA-7tzdlw-BqLE95kgNXPFlbbZot0pLcgOptYAllgNDV0glxuymxL4_ac8p-nma0ZaZvqvhgX7SdEinqDOw2VYULyWYmfZNyKvK1AuysTLOsya53LDZShcvYlIPyC67vp3iwgTqnzRHQ55as-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=X5vTyvkuh7xzzPHZTLstbbLxROHvG5vFXIc34MXXvN9u-uGnq-9glMwBm8N-FQtDpyfqbeIScOJoGRCyu6HNeq17zWSF8vz8QUj-bohLX8Bn6sxUJDkV3340aN4Iys5llAdSwf6hcZc0LS_ajG7wkQTV0JRiUL-zvTURfxBf9pElfsQVwyyelmaaelWXwSiAwUcZAA-7tzdlw-BqLE95kgNXPFlbbZot0pLcgOptYAllgNDV0glxuymxL4_ac8p-nma0ZaZvqvhgX7SdEinqDOw2VYULyWYmfZNyKvK1AuysTLOsya53LDZShcvYlIPyC67vp3iwgTqnzRHQ55as-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiNRTlq0BA0G5Cr4ZbuviCsp-DRq2FH6fuFXOSlk-PVJ2URdnjiQBkENpb5XgUXzFwuh23eoL7EjNIcLNs1ZDZ0smjaZSTEydZHxKlFJ-2xxNjttkWen6InFQEgjcDZVfvD99eyTssuwJtQiXE-B3j_BJLXFINZ-_ixTFjqB7RN5tFTS8G2GvEe3FF_PMjHtgg97yrRyGSXz1Pe-u2tsVOdFOeSztosPGnmZydD2TYosPt6IvAdbxFwyLz8nfh9S9bj9-0BD25hHVsW-ag3fpbly1S_kvyFRJqdqK5ORs7EXgEdgOugYG1-Z8nogb5eCnzs6C67dspA52ui-XSHLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=PgMdHedwZ-TOYzBC7qVRmgy5VyAqTcF6Fsbcta881QIkm000l55IYb-gjVjRF1IeH1bCSWTkvqEzfZpzCxgIdXpl03yGZNFPloLe0WhxgazzAMUY-C0tTeaZ7OEDULvehMEKsyVySvhcz96mPrUtA-724QOYn-kdM9VExlCOXxa-vJgDva8pofwASlHJTggCANjlT7k8D3_cGg1IWuWnUqpDJ6OvBKtONFZGI04BW2Jpm0vbBYbqu2nkz0-PP9xUejxlIrkDar1dEAVGc4VSFKWJ_qlK0yIF_tS2-vKiT8lPLu1SOokS7pbr0Mtnm539mjygk4BM167iCsR8-9ZnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=PgMdHedwZ-TOYzBC7qVRmgy5VyAqTcF6Fsbcta881QIkm000l55IYb-gjVjRF1IeH1bCSWTkvqEzfZpzCxgIdXpl03yGZNFPloLe0WhxgazzAMUY-C0tTeaZ7OEDULvehMEKsyVySvhcz96mPrUtA-724QOYn-kdM9VExlCOXxa-vJgDva8pofwASlHJTggCANjlT7k8D3_cGg1IWuWnUqpDJ6OvBKtONFZGI04BW2Jpm0vbBYbqu2nkz0-PP9xUejxlIrkDar1dEAVGc4VSFKWJ_qlK0yIF_tS2-vKiT8lPLu1SOokS7pbr0Mtnm539mjygk4BM167iCsR8-9ZnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TMWMU4X23_NWEE_Av38t6KtfuITVLKJHkCa1a3JseQ5yHqSLNQjjHvBOKHRwJT48nT8eeFHuHmij_Dj3q8ldqWcwIu1YdgJQlOg6XZAiG1QbQ-JpltVZv6VBwFuYPAJ3RCzg6RLBhiUUjQKV_crOLzGHKLvZ0kEzwhhYSIZuXHcojIquIl446eKY70Ij_2aevgtbRssKdfxjfiJY1U2keA8DSqQ9vwBI0UYaCC02jDM6F5fQFiDQsml9U3IyfU28pNiE8aXZnllo60txF-BaR-21SwaDqIgFRnNnayBohFR_pa_vnGEI5tqWeBE1v9hH0GOswVYUSUj8MTJ-mbRiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gwcgC0IQiYdYpgllrdjFokyjSsn616eNspz4ZW4SJYcXHWtFscM2KIcirALSNb_WHRYaXTsX0YgTBP6L_8UtyMW4_tRqkbpwX1Y9ezjRUvOH9krqGp3_fEMymbUJBV41D4XCErp97TE17pk4obBBxloTBzR4GjmpfdySPBzW5GxZauUZQNSYX8Wt0FcgrI7xXtcDDp-1uIBj6ogMqHrkwaY1mQsa5nb8VR6wOkfXE2RMBOXKzYJRDJT38D7CN2yJ3J8CtoLFP8mXnuKaws1YyYB60nBhihdx_TTEu3gJez_ospWz3-F4wzuu2gGwzvWX0sp2jvgNEJh6Rf4L7jgQWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4-usyhsUBsqQ0DMYKwJCnpXprsILqzNRpa-ErJAMerJvQmPUZjCCwC8a-ptlkLw3xjL9kCmfKhvOKTjS6s4R7yC4BPk-dlAE7D7rRCLlOPou8_5wJh3C6Q6_7jIeOMJRsjkqd0It5vYWXvmBlsA-0sbNVzqmevKhzDmBsf9aZUiaTx_mva0z4DOKPdPIWVLvbwfwwIMyjfBR1H7wmx1H6iphZaoY-upygDNqQd1XMer08NXYbHjpelAV5vJGykMQKlJ47iCsHBjbCncnRIjfxROiHB99vzcy4WeCenqbNK5uI-SNYw5AeIYruaaseGIM46Gz_7l8Ed-LHpURFvpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNHJVJls095JHy9Q4mP5VCVTOj2snt9bbsGuWhBCprgpuuXDsUtp74Zd3sZTmX-EpXb66tbe4rgtUU2VxTm6Fy4PGnm7KhhXyVpP17TFB0z1L-MRm29t7x6fY-ZiayUL1dVrmIs44UNw41NPWVdqpbUsqNfqEZO-ptW_P8sk2n5zCwRRBdElTyu6pJdJidihkaJQniBvqH83TFYUBTof-KyENtaaQakdOMwrDkNl1IIyi0ndeuEjVCpjkAQWQZxmRfFMdqdd0taJZdawv5uJ-2uwqYAS4xQjcWGf4BpO9eLdAwDJzU4pSs6RVhOyhPEsQVh_c4o3wrv6Ah2aGlY21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjqwxjztJZX8xVEhKifICwedLextJEISvmxMjvUXjUq14QgRHeRVp6gBCTURgMec85hAUK8CpCFc_TiiDwhzZPhGAefWFYemN95tAxuAGj5EDf36lwtS_q9DvErF_Glvc6LGty5CudYe7HPBm1o6XHcqiWrF2F9SgBYx2EvcP0VhH6-246FX-XlRmrFLmRhSOLpcl48I0Q05SEG-S6rQIoB6gFfzRl4jcIwSO-Z6Mny9ilb0bnlSgVyVmcc0dfFZKpk3beJafjEy0_gtUdudRkGxOTFjIgreHRRfkr4JgBN5CIxUPVTOTVU1YCO1kmHVlFc_h6rEbM90ws_XBPGMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saz2gzQZIlzSprUkF4-HsqxcxpAv2zEauPf2jN5XIK_WuL5vYq41AQ_aioFcagXGaq1KEWkRgwA_1uipm17rQLOyeJNkxx0sR_aOcp2T-YWRx6d0iZlfYTvXPAmJjVMdj9Ly1w7mkHeTKi2JBLeQxtx17il4qIv3VM4pbkyOYDmzM5SMajvWIEfHT7ZCMPFS9ZdASKDybG2Z7RDShkW9qJbYqq1kQASVNZPVZX2bKlw-VFMBP7psRyY_RgsHBn9epZi6kH9x41hCZtFkXtt--BYHoPcWOJqgiSuHdi0q3RKqRpv5az2tFyyD0OuvUuQ8oM2dfFtgZEbP5eqmEaQxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgFnKomvB_-4gzheXsRwDdJRyB7ZjIzrbEzeDPKhAl6qD196kf3JAdvcx3e75sHS9FYKns75C50lVqwnvkeO7SEGGMPy05krEyaGew8w-l0h7xZwpSNg6jvlmkNF1eu0P-ORKfYLduaKGSCb8RF1htFLESSy0cyA9ap8tfHRKlujvDNdvMyLe77mg_tkDRRZYhP3xaiitc9iRW_lAWh1IXXRLkqbxu8zKs-Bycx15Nnzk2EjsGpWOIV2e5G0n3gfixkUCuF1eSoiqlZ9UF2FQ5128wxX3xn_crpTZpr6USKdl9_cUEH4sN7TqLJ0rnXGKaZBfH69kQovZLJV5SArQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuEkUe_SBHLJs0idnBR69sJv4YR8JLOp0VnVAUyPprp4-lJgMMNVLp5Jspxm8THDac4fnZOXQ1_c85tOGGCL9BwyoWlbeloat5MVJESgB6K1C8R283RC4dqUpCk7CymF7pkJIjs19vT9Cx6MB7YaDxJ5mjNPv3x8bxrcoLkRSXmVaJPWDMK0IakV8gZKFBurVDCBPhYeAiAyLuZb2HSzWRMC7WKFi7tbkZQ2yEj393LxYGER9YIZpTz6EVUHaKfA_8lnnexlSctBnpRNgvYfKxFGN8m8VYPEOBzL689oucVeXao82JhIpp25ty7iyfZWphLTQYUOfGTCTaG4EeThXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYZ2XRA2uaTnThcmvBzt7ih_Shlp7t2M9Rt_etgzG4f2TEkEIiY28TgklYJ6IJBa1JKA-XBneNFuqieS4QHfjJTCx4UcM8LZvoDgLG41cdGX1XHbgIFMX4d2khmrrX5iNUJuQC8ZvfFvMtZN_AEspZ6IFBYClHw9XkB_ERbh394topgncVc1ffYzCgQvY7xXQtkeENTNOa9XuEue2GD0ij6nqu4TEMMg2M8oAD4KdL3Om25cA7tAM-B-oWCv4lFx59R4h5TEd76211rFtDaCuRVGPaqFGtIMVDU-NTr5ZproWDzCrhpP_-tUYmemKNKyAvsPKuoYBrr4cmfgjGiJZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyx8vanzNCpsKKD22gitpf3SVdO-EZGI_JRvpVKkXdQktnllBecfThLRIg9nfen1Ryr5yDX5TdBuxqznSk1g1PNtLFW02PL7aGIYgB_Zravmr7oXClI_ArT4fBSmYGMEjh7bQoXqm3pxFokkbNsBprAtpAuFMF8Q_NGgHY6i_ofUY451IRvyXIyPCJikrfMfkf-QQelvCR2CZLtj4de2ygAtAsU9TaiEeuTUI7yEpIbBI0YnKEDhUrzOQuMz7Po9XEPuR3eggAIKMvJk1LeF4AVMPlq9NsqWMF_k7KHOnZMF_pfHQwqZBtmbtJVNu4T30GzhndEdnev5scoxHiPZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GibZkR3-oxnYZRUonptUNXgu0x7_YrYjCi8pefsuRKHqSs81Ec9pTdogRGI2MhIz-lxfrIsI4ADSmpQ_3i3MaU2_5C9r3tWHz4J4St1xzLU2epO4xWn-KfiOQWrj3JnUTU5_AJ5mfsQvk4TVcmz2uV_2keoeygQLnXmaETZGuIkOBjJ9rj3ctwFGsOFwV01_aRHkbsg47ThKX7ke6GTJu4QpWrYZxVqoxJruqlcdbliJkvY26CgnsSc5pMIln5YQt8OXo9j1AIPTkRKUbqhjyG4SsELU6lzrX-q-mzvftAcBXU7zVYfy6e5qs_cEqW4ALtwKYPIFQ3DRvLv1KljGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC5zkA3ut_r21e4edMX2L_gmf-OyHTM9ZdCe7tA_hJPQpM-xrNBSNcI8_geZjfvEJwVlkhMGEZdJSR8IWyr20DymewLJjMOWUPNnkF2hofHO3Fkh6I-PlrKkDpnYKMUhboiU1NgbsjRo4eKsChF4H3leeXWHqxa_dKB5PskGPAM1tDsqmjLuG1WLUjEfjh4MU1JUw5pCkTHz8oh3FfmmX2WKyBOy5jXaF_POZy-u1yr0yZYDZbPimf_uobgW760Zc-b-1HmZNXfeQnPlu96bWCjQKzWs1nrB4HF1woDGmCC49WIZa1kZRhj-M9GxPvn3TNYAbUf4bacHeGGE2HQqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6nj5QoiUySZQ4JD-3GLuT6Ef7JgWfJJD4Xka_8YWCgyZ5hg-Y3eeaR4tROL99e2LUEHlVPBKxI8QiUfmkC0KKuNf8zS0FB05WnIZmFG4oj4YrAUKn0zU4mpmK0NBcA8ZvthMkDWD5b1NcqbtMYAy8LWf_Rr_EVA79aGdtrD0r2L5I0EoPIYRt2gzO189SW54mwreL0g2sJRPbKNdpKRWY4_y-cbP7enpATZ_vheu74JJoAB6AcaDQchFifsukr2dHLhpSSzA4DJdo1w3OLzqrtX7nDdxiTy4-u2zeeMMISstFqua-7jZqS4mkcqY8T6DnOrS4uk7cNikAknt265wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgmhLFwSoLx2D9_djQKJTPSu3ttHqdXzIllj7NKzTHsDQu5wFBdhp07t-izsPgnM4n6vvEsWJCE2cklJ-yY7-fdnF3kSXTgvO-6IlWzo6cSp-SThJjQltkWaGhIRgG1y8chHqjVfpO_PO37ICcMtJ10jZOFedq0tAvXnqOgtVTv_uaxj5ZLyxBCTdPe6KvZQpo-UuPg0gbS4-zoRf3NZgCBJ2RYpdZzHZgBCJWbXlqPCKZcqry45raaxgnsb6XWuR1aVX-7yWd6eMmTNopkaRpzEETcwWAgmxfY6ID4wunhNK3RE_Rp0CFl6CO0WX5IKz_8Xp9rnLCt7cTnxFNaMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0fPDM3KJJWOXW1gecYwaquXFbwR4LwCz1ISzvM7ulCKp9IDIoL7L7GkvJ2hf7dvYS7ii_ri567fLtBw_7YTxon3Pc7kWSsDtD8He2PedIB-LHWYXpHEej-VL0kESqtOe2bPV18j2o9p4QTq2BOWuaTACQodSfH8r51mb5g0O88FdAQq216jagEyTW6-UKL5hEBZ1Un4NFLodAXdHypgAdh6wkUzzl2bNfjN2MYCsK4MFy6InX68PPY21KdudQeQSLfOawicv9TIQrl4ZOZ9PaHoJAfbWCCiVPrKgkW0H4n7q3lC30wZS3E4gies_o30mINkggQreeuzRCkE2Eid6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBPuHX3fJF56eR7_ld6uTPPfu77wrhGw_rNPorxPE-UndUKGTrPpDa5uYqXBSXzh48Re3Vadd6MS6S7wXvx0zLmYpHtfH2GPZLwJK5Z3TaADeadoYo_OvN8cvnvl2odmqF2Io17ll15M3x_DL5xp5Vkn8qPYU2VKaJ6jhL7Er6sNPJf9EA0Itf5PdU_Y8bfwhBQ7fvp5s8VGjdSVnxFGrNkXmleLHQA1cCa5T6Bng6rUI7Es-8utZxguv0emOBAg8sQkTU20xRF5NvnA3pTaVsb6V3FaeWv_pfI7ctXk-fFkdOVlh-3rABPqI9FjBrr8Ce32FKuY4CdSysE38erC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
