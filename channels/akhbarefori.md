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
<img src="https://cdn4.telesco.pe/file/jqRLReb-Sf6T5r-cVPeX-o4MqvxanT6ox0uT7__ptx-MBmPzLmQJYZYVdbH251QaI-DInTg_DnxERcYOyWyRm9lw-8_8gR8PJB0mW0N6KqspXiXYdVbEQnzIjnnMndO9qqFJn0EG0ae1SWv6s6w-sAhLuvLHX5VaYTTbAHjKYUO9YnyKSuAfJRQO3puFWrWOpNvphXwlDFez9eCuLQi4URgANsPmEKsbDA3VX-LA1lZ6dtBzwEuKeoKlLPVwRaoxh5rxBzH-NXgTDIX8yqegHaIkoocn56cG0IbDQTRKD8NjOrJ5SCnq4scN7f2twXHnitmAnerJfoT2JIqWw3q79A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 13:02:44</div>
<hr>

<div class="tg-post" id="msg-681076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEhcNs613-5V66ao3idiM4mfqn0QykHBTuPqxJ1nhTxKYTSI5izA5-s5L5FcLFNKojT0dkdb3AuYODKgsVqFVsCYi4kiJlt75Vl1Hq4BTjetEq9zDfVTwoPYyvZ6CTWlPFe5P1uPGR0DdQyNPJ8xdk7x6laxzQNm5bVmnCPe0OVDwsTUHLXqsicnOmKrikRfy7lyg57Em6LeP5M6SSmpWdFGjlTcZIrDkiLFfsdKyavDtAhonfcN6Y6fcNPyGZxxy8wnNYEKzov-TtC07HLTltUbqKFFU09-dDCvx-1_1MNeKi-aPvn-DFfm0PApSLWz2fppQYOsIG_Nk34pRAatqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rj2oSZds8o1ET8TNxZgg2pnFxzu6m0CVHX0ia36Q89e6LBVSSD8GXLwkC7WStyj1Sqm1GeqzWl93tl99tSW2WedTDM2b3uk1lM3gZfCwpapeQ3gJJ9SK1iyhYqjuMDyNh4dGfLRZa9mQYt-lj16dI0ZiQJUpjjafbHhVIhLb1zbMnht7FGwC2Z4V_ZYIj7hBLPjTUumXzNtHAXLdRVO1YUyTJF9NcE3VHlLzcWU5TGbqQm7iSkGTeTic71P7yV2IfP7oOnGWj8W5J5enPNH6zkoCmhnwsaCl5Leot8LGmwty37KxSdmNP3mGvZLpQdtCbHiXnE_x7Tx3LsArnOc4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie-BcnJqKM2Gbsc2iQTpIl5tAlcluqMlF_3nnudfB-Vg-ijxY9J6tuS60axJwFS_fLoz3jlMyp1sIxngIyqMkGzVkPsaAFcSmDsOWNc_QVST5-ZThxlvKKWR-WOiF89vrAamLy2ArTeeW00a8JkPcoe5GRESPnBxchFn9rE-v4fG704tTTxcEe2MLcqDKNdkR9G83aduSpjXQZDb-AnQx-wWs9-Q7lAsuhXk0WWuwcmgyX4YWck-qRqa69uJ_h4MGGizYl854Kz1YyIZBXz3DcNypMzZ2rO5AR8Hn7Q731cHJtZHYrCHTLlAUrX4Aiaol6reHIEftgo_24NumRW75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGtarh_Iuxu0dV36OSwgEt98EOorciQS6I8RL860yiSY0aZMUF7N7pMkWXiUDFNGbCs9wWr9FNIXYfcfGMiOWOWDgJm6GBIR7fHtkjbRSqNh79SumrN6k6BjCLIEbMVbxYgL2nsTERzjp8EodJXojZqhDCUVzi_OcPFjcU6nxiOcs7V2we_DTm-TPvasaAj4_4txTbQ7r-V2Fy6hpj7evVO8H0tbMp8dHatvRsJVgD3mzbPlWbGQ7btsW6xzhdOTeeTl7YY2SGGd0NrejiFsF3XFj6hApxEuW6oC1UTEvrDEVX75N7qF9o-wCx9Dx5Ug3KzcxJ9TGV6gokGazPeEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euF44qYASNIT_wF2lJZgf3878fhby5c1hMP_eWj-lNqu3scvUtvR_0R9GuF-kEs2jCW3e2wFl-MZgvIiy-8koqFh9qU1J4HgGd8VhLnU8yW1xvamGcWnsIn03UzWccpB2ugnXfDYnaB7CGmQi0J2NKAvwlKTf29qq3jGtaWevBDtmYFtOFxiKNjwgUxLYFJkRdsYFq5n7QaLgQ0DdZVoahzWryaNAvVp3A4Ty2Oij2vO5i-S9vBcpwxK3JxipTiwU1ycinFmMN82C6i5ou9P4elLa9yCX_Q2eldAmdCiTTnW_RqTXlQdgXqK7KfSBea6PPuKgRpfWdiNjInT8xlbWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
احسان خواجه امیری: پدرم عاشق ایران و مردم ایران بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/681076" target="_blank">📅 12:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجلس برای گرانی بنزین به رئیس‌جمهور نامه نوشت
هاشم خنفری پورجعفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
نمایندگان مجلس با امضای نامه‌ای به رئیس‌جمهور هرگونه افزایش قیمت بنزین را غیرقابل‌قبول و مردود اعلام کرده‌اند و این نامه با امضای اکثر نمایندگان قاطعیت مجلس بر عدم افزایش قیمت را نشان می‌دهد.
🔹
افزایش خودسرانه قیمت بنزین در هر استانی غیرقانونی است و استاندار و مدیران حوزه پخش فرآورده‌های نفتی آن استان مسئول آن هستند و باید با آنها برخورد قانونی شود.
🔹
چنین اقدامی تشویش اذهان عمومی تلقی شده و هم برخورد اداری و هم برخورد قضایی را به دنبال خواهد داشت زیرا این اقدام برخلاف تصمیمات کلان دولت و مجلس است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/681075" target="_blank">📅 12:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f8a6ab92.mp4?token=qo03Xqm82SfRISNp_UE7x5zTzDkeLHWyoHIGHKyV0vqGgSZRW5MjnD_jJdIrwvPOjisN_1czubYB57hl1jrkbfZCaURgMrnHNE8AdmtLG3W-vEv81hcGs0v2sUABn9io2H1uvAd_pRXpK8z3Usnu8OY04UjnM8VWBQL16XzfWT1bJXN3HMqk3ZneQ9eIHRtbC2CpHrC9UrRSnzALO7Ubi1sxRJDklo0T466CTyPWM2iN0wrJyDDsv4TGZ1CKuE0eBoRZ4t8qthLKx934k69U3XFDJNY55sMDs9xhC_bGZz2CQLekHE53LXXJ4Yh7sbvEQaUpQXEsaM9ynFTK8_uYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f8a6ab92.mp4?token=qo03Xqm82SfRISNp_UE7x5zTzDkeLHWyoHIGHKyV0vqGgSZRW5MjnD_jJdIrwvPOjisN_1czubYB57hl1jrkbfZCaURgMrnHNE8AdmtLG3W-vEv81hcGs0v2sUABn9io2H1uvAd_pRXpK8z3Usnu8OY04UjnM8VWBQL16XzfWT1bJXN3HMqk3ZneQ9eIHRtbC2CpHrC9UrRSnzALO7Ubi1sxRJDklo0T466CTyPWM2iN0wrJyDDsv4TGZ1CKuE0eBoRZ4t8qthLKx934k69U3XFDJNY55sMDs9xhC_bGZz2CQLekHE53LXXJ4Yh7sbvEQaUpQXEsaM9ynFTK8_uYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت آبی مسجد همت تجریش؛ این ساعت بدون برق و باتری کار می‌کند
🔹
آب در لوله‌ها جریان پیدا می‌کند و با تغییر سطح آب، زمان را نشون می‌دهد.
🔹
البته تنظیم دقیق جریان آب برای درست کار کردن ساعت، کار آسانی نیست.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/681074" target="_blank">📅 12:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681073">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا ناو هواپیمابر جدیدی به خاورمیانه می‌فرستد
ادعای وال‌استریت‌ژورنال:
🔹
آمریکا در بحبوحه تنش‌های جنگی با ایران، ناو هواپیمابر جدیدی به خاورمیانه می‌فرستد. قرار است ناو هواپیمابر یو اس اس جورج واشنگتن جایگزین ناو هواپیمابر یو اس اس آبراهام لینکلن شود.
🔹
قانونگذاران نگرانی‌هایی را در مورد گزارش‌های مربوط به شرایط نامناسب ناو لینکلن پس از بیش از ۲۵۰ روز حضور در دریا مطرح کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/681073" target="_blank">📅 12:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681072">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=PkGxcjaoOOZ8o2jD5YJ4x4j9OrD9iP8tW-xL6EN9aEhQPyCKQQQMX1Mn_w5HeRoZ6UiWczwBE5BQWqDEyfVxBoDynUut40qX1UKfKuPfq85Ix751bNvKdgUKTD352Rdzs3R4ja3LBSmcNzRSO0OV0AEpCUibVfqd4PQMbO2oYAUX070hpuP_Vc0iy3pHNLvGE2t6DB8eIyVRZTslCKMghrD2K-fdDGf4R0eVmRAT5cZT2y7IbQ_Q65JU3Z-yoVM5eQobmJysk_Do6KJftSH0dhBM3xT2d6CbjBHFOF8PhU-hLhTTH5rqQ04AV0yLs_h2HaTXoN-T3bT7V3hce-OaQ12-vrkuIImMD2slgpRy9ntaJhl2rMurCEgaIQnVaWmzWbqykWD1d4x8fGvyFWmuKBoba0PqQx7IgCfxSbtis3kXU8XZ3kTrkgBmQ6NihxBmtetg9pSO3zPclxYxQroKE3YIm1G-mFdsqJCuE9fxJgKxpBDweSmezMXkxIEr8e2hwsbI-9WzyQtOJ39eZbVbZtRNIHfIFdejYa8t5kUImryqsVYGCJwOqupitB4trxufTHQRdOjFRBp6RhshU1PQrEpMiumftHQk6LizkHcoPr0KHcHQn6VsBw1KeS3sHxrdqhArXXka7C3YaeMieenDUEdDMxTU1xrrDmLFn4Zo6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=PkGxcjaoOOZ8o2jD5YJ4x4j9OrD9iP8tW-xL6EN9aEhQPyCKQQQMX1Mn_w5HeRoZ6UiWczwBE5BQWqDEyfVxBoDynUut40qX1UKfKuPfq85Ix751bNvKdgUKTD352Rdzs3R4ja3LBSmcNzRSO0OV0AEpCUibVfqd4PQMbO2oYAUX070hpuP_Vc0iy3pHNLvGE2t6DB8eIyVRZTslCKMghrD2K-fdDGf4R0eVmRAT5cZT2y7IbQ_Q65JU3Z-yoVM5eQobmJysk_Do6KJftSH0dhBM3xT2d6CbjBHFOF8PhU-hLhTTH5rqQ04AV0yLs_h2HaTXoN-T3bT7V3hce-OaQ12-vrkuIImMD2slgpRy9ntaJhl2rMurCEgaIQnVaWmzWbqykWD1d4x8fGvyFWmuKBoba0PqQx7IgCfxSbtis3kXU8XZ3kTrkgBmQ6NihxBmtetg9pSO3zPclxYxQroKE3YIm1G-mFdsqJCuE9fxJgKxpBDweSmezMXkxIEr8e2hwsbI-9WzyQtOJ39eZbVbZtRNIHfIFdejYa8t5kUImryqsVYGCJwOqupitB4trxufTHQRdOjFRBp6RhshU1PQrEpMiumftHQk6LizkHcoPr0KHcHQn6VsBw1KeS3sHxrdqhArXXka7C3YaeMieenDUEdDMxTU1xrrDmLFn4Zo6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته ارتش اردن از بحران‌ها و معضلات آمریکا در جنگ‌افروزی علیه ایران روایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/681072" target="_blank">📅 12:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681071">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BriBaspa62D_FBE4gYmQl9i3Ek0TRPIyLivvYmnzYTxsT7xrFgTY5dZIKs1U9jjtWrB0gtrpLSwXWBGP-TGetuip3GkEzQBIU4fvH9lcYeXXZ03G8lKPXwJwp2IkWTrli3JnQPWALCZmTdB8Wku95hjnqzD8wKVSTHDgLeQduohw5WWURk-fyGL29p_U4c9DNkev4l2wWtUCXY4XOzY5OPFt9y2urtR8Q7RUPpFcjGefeVN4juvVHCN8lQSkcE9REKUkEM2Kf8lzJnLZakVfu1NcFv9TWGbgfIUcgnvAyeVyisPlO9F-1UtkdQheiHNiKHfI-qIMrtzP2gHvVsh_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت جهان با ادامه جنگ ایران تا چند روز دوام می‌آورند؟
رویترز:
🔹
برآوردها نشان می‌دهد از آغاز جنگ آمریکا و ایران، بازار حدود ۲.۶ میلیارد بشکه نفت از دست داده است؛ این رقم معادل حدود ۲۵ روز مصرف جهان است.
🔹
از سوی دیگر، با شکاف عرضه حدود ۵ میلیون بشکه در روز، ذخایر دولتی باقی‌مانده آژانس بین‌المللی انرژی در بهترین حالت می‌تواند حدود ۱۸۰ روز این کسری را پوشش دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681071" target="_blank">📅 12:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681070">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کاسبی باورنکردنی با پارکینگ خودرو در تهران
🔹
این روزها پیدا کردن جای پارک در تهران به یک معضل اساسی برای بسیاری تبدیل شده است؛ اگر سری به فضای مجازی بزنید با تبلیغات مختلف اجاره پارکینگ خودرو مواجه می‌شوید.
🔹
اجاره پارکینگ در تهران با توجه به محله از ماهی ۳ تا ۶ میلیون تومان و رهن کامل تا ۱۵۰ میلیون تومان رسیده است؛ داشتن پارکینگ حالا به یک سرمایه جذاب تبدیل شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/681070" target="_blank">📅 12:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366aeedc1e.mp4?token=IRXeFQu0d9XhtZtwnPAySzn34ZHX2Ez-bxjzUMAqXur4gfZ3-SvTHSxoUvZ8QgzBkJd_JU7ySZVfWBoW0oySw8qQooZdB5y3LXwxrVP2Eia3ohwsXDvzh3H2L5hXJJaGMVujHFlZD0eXBpTQJX3Tq_NVzVy6YEchCZMBRkYa-61djpNv9fPxWL7BVyNJKQ7UwHjEetyjAZne5cIxltQsAVnqV8cME_4KzM4eY5az8biDdbWh5Gqjl7fdAa8l0oAZskEeWZBXLbmlkl7ewqzdrZg3oqbdagif7AGJX7CjTxKXenHlnv_RtFesKEFwV3aUUkLnzXdLa1XhfiBJnCX8Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366aeedc1e.mp4?token=IRXeFQu0d9XhtZtwnPAySzn34ZHX2Ez-bxjzUMAqXur4gfZ3-SvTHSxoUvZ8QgzBkJd_JU7ySZVfWBoW0oySw8qQooZdB5y3LXwxrVP2Eia3ohwsXDvzh3H2L5hXJJaGMVujHFlZD0eXBpTQJX3Tq_NVzVy6YEchCZMBRkYa-61djpNv9fPxWL7BVyNJKQ7UwHjEetyjAZne5cIxltQsAVnqV8cME_4KzM4eY5az8biDdbWh5Gqjl7fdAa8l0oAZskEeWZBXLbmlkl7ewqzdrZg3oqbdagif7AGJX7CjTxKXenHlnv_RtFesKEFwV3aUUkLnzXdLa1XhfiBJnCX8Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعر محمد رسولی در باب فرار ترامپ با ماشین حمل غذا
از ترس ترور نخواب که دفعه‌ی بعد
با خاور حمل خوک باید بروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/681069" target="_blank">📅 12:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تلگرام ۱۳ ساله شد؛ بیش از ۴۹ میلیون کاربر ایرانی
🔹
تلگرام ۱۳ ساله شد و اکنون بیش از ۴۹ میلیون کاربر ایرانی دارد؛ ایرانی‌ها بیش از ۲.۸ میلیون کانال دارند که سالانه بیش از ۹۰۰ میلیون پست با بیش از ۱۷۰ میلیارد نمایش یونیک منتشر می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/681068" target="_blank">📅 12:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2795f234d0.mp4?token=eQYjjVcM24pvjpVKitJJwFvRxEOogLBUz6qc0dLJ7R6cp5FrwPhUc3gkgVNxoBUxwcWJbmEXIIZytsFqGd96khczmoobWfgyhBEP6GJmnk6s0lAP9cmkz-FJU8w5rFxGLeVY6UXJUdOFd-ucnMbqgvsthQ6YuQ1VI87nvBykG6Bc8aTaccfH0MXx_8ERgp4uRW6ly514arT2UlW32OrYi-kw39OK2e7aVqoylz9vu1OxlVM3BC_GTTgqbxAu54nun9wJQdvSCpUzDiPZKuiLBFUmeWm091FnFtkyBhhrwya6T1D9zEzTpiXlCoFHEyeov_X3QQd8R4i5fXJO8YwqLGC7gH4uz65XEuBSGDfn7f2OR3Tj2SucSymnOMj1qTvjGzFUd5cU4PLiW5wV7_eXjC9T4A_O5m6pU1gRHIIYTKXYHxiU7EGhpbrVJU6Whx6K6QF9KE1nLd6waFyiLXwU5pU-MRIU_UdpEzGPxh0J3WlmV9YpGLPs6AS24aI4LcT0E5tH8BNzwpHQiiDaCD_gkhV2Qt8XZjuF09zzlB-kTZLwlOQ7AgAH2kTEXzcsGuYiOgWaQQNu8kknV9i-SoSiU_6alR7_CFS_kuQog35ziQmfuFTB-FTRl05WkPZFjgGz7Iea7Jh0K6ZaFHhcz3zLSkSB6hLAshL3GezFPipcdG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2795f234d0.mp4?token=eQYjjVcM24pvjpVKitJJwFvRxEOogLBUz6qc0dLJ7R6cp5FrwPhUc3gkgVNxoBUxwcWJbmEXIIZytsFqGd96khczmoobWfgyhBEP6GJmnk6s0lAP9cmkz-FJU8w5rFxGLeVY6UXJUdOFd-ucnMbqgvsthQ6YuQ1VI87nvBykG6Bc8aTaccfH0MXx_8ERgp4uRW6ly514arT2UlW32OrYi-kw39OK2e7aVqoylz9vu1OxlVM3BC_GTTgqbxAu54nun9wJQdvSCpUzDiPZKuiLBFUmeWm091FnFtkyBhhrwya6T1D9zEzTpiXlCoFHEyeov_X3QQd8R4i5fXJO8YwqLGC7gH4uz65XEuBSGDfn7f2OR3Tj2SucSymnOMj1qTvjGzFUd5cU4PLiW5wV7_eXjC9T4A_O5m6pU1gRHIIYTKXYHxiU7EGhpbrVJU6Whx6K6QF9KE1nLd6waFyiLXwU5pU-MRIU_UdpEzGPxh0J3WlmV9YpGLPs6AS24aI4LcT0E5tH8BNzwpHQiiDaCD_gkhV2Qt8XZjuF09zzlB-kTZLwlOQ7AgAH2kTEXzcsGuYiOgWaQQNu8kknV9i-SoSiU_6alR7_CFS_kuQog35ziQmfuFTB-FTRl05WkPZFjgGz7Iea7Jh0K6ZaFHhcz3zLSkSB6hLAshL3GezFPipcdG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش حرم رضوی به ماجرای جلوگیری از شعار «مرگ بر آمریکا» در رواق دارالذکر
/ تلویزیون اینترنتی مدار
گفت‌وگوی کامل
👇
▫️
https://aparat.com/v/rhz4415
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681067" target="_blank">📅 12:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7db719237.mp4?token=LH8gtpYPOEe6zBPaoy3vYhKgegxQ4qaU4LW9I7UtxwVlxXjkfUhiw76XRl2geD6C6--kuZKHLzt8AHbFVssO6zqQ1pjQl6qeSZPawvw7kYOLbsd_gVrFD9DIub1sqqWsY8FuETWY5dh7HTMbh4YQCeqg_YJfkLWYIRUDpd-76MOc6FP2jcxL0-ax8DfDkaOskBfJPAQdpZ9AYe1SgRhLDgjalqkZHoDQ1tErKphriRwKN6vukQ6kdWHrCrEDdAOEGLvx99UmR2LtVMWmtABgE-JurZq5Og9xTcNRIas82JlHOKTBgci4tHpv4Dw5V1W9mBD9QHwxMelmE4hJ_J1LAHD_YcsQFOa0Uvg1TG32f61iYkIaKVFHY1ty32F_qxwxvcU-YP66YExfKJn-lLmL57SftnCr-nY3zuoPCZWL3np2nszXVoqtqTrE5X43ErtFE-_tMpkbsixq0AycmgszxtCfQvBL4Tp57vM_sFZj8RpwPxow7RzzkxYuq90H69xE2dIgl23_84jEpHvtckFsGdrj20iXbC97rq0ciFsdN-YfMsVcdeDHXYDBUrwA-BBy5DTr7kydnTUiTYkVjHqbDJP7-3JGyylx4hNUtQuZf8pkQo12Je6jKGfGPEv1sJKELJhFj_wdwi54qf7nWeMQP5uxCUmjx2NFOSs8GEKBGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7db719237.mp4?token=LH8gtpYPOEe6zBPaoy3vYhKgegxQ4qaU4LW9I7UtxwVlxXjkfUhiw76XRl2geD6C6--kuZKHLzt8AHbFVssO6zqQ1pjQl6qeSZPawvw7kYOLbsd_gVrFD9DIub1sqqWsY8FuETWY5dh7HTMbh4YQCeqg_YJfkLWYIRUDpd-76MOc6FP2jcxL0-ax8DfDkaOskBfJPAQdpZ9AYe1SgRhLDgjalqkZHoDQ1tErKphriRwKN6vukQ6kdWHrCrEDdAOEGLvx99UmR2LtVMWmtABgE-JurZq5Og9xTcNRIas82JlHOKTBgci4tHpv4Dw5V1W9mBD9QHwxMelmE4hJ_J1LAHD_YcsQFOa0Uvg1TG32f61iYkIaKVFHY1ty32F_qxwxvcU-YP66YExfKJn-lLmL57SftnCr-nY3zuoPCZWL3np2nszXVoqtqTrE5X43ErtFE-_tMpkbsixq0AycmgszxtCfQvBL4Tp57vM_sFZj8RpwPxow7RzzkxYuq90H69xE2dIgl23_84jEpHvtckFsGdrj20iXbC97rq0ciFsdN-YfMsVcdeDHXYDBUrwA-BBy5DTr7kydnTUiTYkVjHqbDJP7-3JGyylx4hNUtQuZf8pkQo12Je6jKGfGPEv1sJKELJhFj_wdwi54qf7nWeMQP5uxCUmjx2NFOSs8GEKBGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وازلین و خواص باورنکردنی
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/681066" target="_blank">📅 11:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e0c351ba.mp4?token=ENuiizpYykBW6vTh5IfVgnKUSLGm2yc4Unq6Wb0gOl8LkCtbTvMWr1TGEx4D6AqBBepLS4JpWOPZw-Gk49GK0Za2f3BmyA10m1ThBpQ2-B5CPkxgbZ8Y1fTsai7kesF2NPpuIx7szxyFsQyobkITKXApXx_9QtAR0vMjafI1dgFNFvYG287K4J5rP-QT5gxQcLD1Ozkh8kKHy9HzgSLMQ60vK6DsFzqAiueGXDmPyIgNfbkfGGIGJfER3dxKrG1dJ-XX3PVLLIK1Z_bFTPI5xf5QIpck6JMEoyfhOXrwntwz3kX0JODjNOBE7NryrByLrmeJ-5_9QOJ6xfodk8qLwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e0c351ba.mp4?token=ENuiizpYykBW6vTh5IfVgnKUSLGm2yc4Unq6Wb0gOl8LkCtbTvMWr1TGEx4D6AqBBepLS4JpWOPZw-Gk49GK0Za2f3BmyA10m1ThBpQ2-B5CPkxgbZ8Y1fTsai7kesF2NPpuIx7szxyFsQyobkITKXApXx_9QtAR0vMjafI1dgFNFvYG287K4J5rP-QT5gxQcLD1Ozkh8kKHy9HzgSLMQ60vK6DsFzqAiueGXDmPyIgNfbkfGGIGJfER3dxKrG1dJ-XX3PVLLIK1Z_bFTPI5xf5QIpck6JMEoyfhOXrwntwz3kX0JODjNOBE7NryrByLrmeJ-5_9QOJ6xfodk8qLwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
الهی با آمدن ربیع
به دعای صاحب الزمان
🌼
🌺
زندگیتان رنگ بهار
و دلتان رنگ آرامش بگیرد ...
#ربیع_الاول
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681065" target="_blank">📅 11:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f023a6a08a.mp4?token=AQ-EjdEWBmhsxYHDaTm1ly4TEKnxUvqWxZ6CtnqijfFyPXljCFxx-swZh7lkTtlCHtc707OiTCNtgzVZUKEr1UiXo96XO2iKBnu0mAB-C2NPHl6gVnrJ0JTeThEc0CZJ2HN4nzumpIqBWnJVHjAV_LF1ytbk6iPMgOKTJ4o8Zt_HK2WLymKrxqUUwaw_WwWQwEXarxd6nr7AuqBt13YAhbVcHozrfyBmX4F9Y859wG-GOhXU35BrZBvoV3ENqkKMkQcH-xHqt0TGIdjNr-VTrc96Ql-wy66xREBVihwkZxDQwZaIarWmrXfco6ejYaBhgMoOr8P72hqlkenHQq4XZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f023a6a08a.mp4?token=AQ-EjdEWBmhsxYHDaTm1ly4TEKnxUvqWxZ6CtnqijfFyPXljCFxx-swZh7lkTtlCHtc707OiTCNtgzVZUKEr1UiXo96XO2iKBnu0mAB-C2NPHl6gVnrJ0JTeThEc0CZJ2HN4nzumpIqBWnJVHjAV_LF1ytbk6iPMgOKTJ4o8Zt_HK2WLymKrxqUUwaw_WwWQwEXarxd6nr7AuqBt13YAhbVcHozrfyBmX4F9Y859wG-GOhXU35BrZBvoV3ENqkKMkQcH-xHqt0TGIdjNr-VTrc96Ql-wy66xREBVihwkZxDQwZaIarWmrXfco6ejYaBhgMoOr8P72hqlkenHQq4XZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهسا بهشتی قهرمان جوانان آسیا هم شد
🔹
مهسا بهشتی که روز گذشته در ۷۷+ کیلوگرم نوجوانان با ۱۱۳ کیلوگرم در یک‌ضرب، ۱۴۸ کیلوگرم در دوضرب و مجموع ۲۶۱ کیلوگرم ۳طلا گرفته بود موفق شد ۳ طلای دسته ۸۶ کیلوگرم جوانان را هم به دست آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681064" target="_blank">📅 11:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkul6AYP4tIDm_4aVdWoT07u1-R5k6zEamMuI4_bqrBJxnHG-rFwjz5GJiK5Zy48xqS8uUrQhyvs4VjonebiXqQy7jwJCDjQzCoB4y7xbNUbWIA11geJDyohovQYL6oiLoL__CYSnZ5u9jivGqX9MLPxAQzMqRVfQQq145uDqPSwTR8u9wjbfkqvAas1z9EdqSinCD0XGOvm42Ki2mxvVLfVKr62ozR_Y022MdXPSOJ1YlC7hLlpTxUTPymVycsjuQrM698FKhdp9qsvaqXHEfL7Jrq36Bm9Tn8R7lDsbNdd0P5pp5AEGFHv9s9yDv1bfSBnYmOovvIHjqUHnkT5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش در تنگهٔ هرمز
🔹
به‌گزارش سازمان تجارت دریایی انگلیس یک نفتکش حین خروج از تنگهٔ هرمز در آب‌های نزدیک شرق شهرک بندری «الخصب» مورد اصابت یک پهپاد قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681063" target="_blank">📅 11:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تصویب کلیات طرح راهبردی تنگه هرمز در کمیسیون شوراها
سخنگوی کمیسیون شوراهای مجلس:
🔹
کلیات طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز و خلیج فارس در این کمیسیون تصویب شد.
🔹
بر اساس یکی از مصوبات، عبور تجهیزات و امکانات متعلق به آمریکا، رژیم صهیونیستی و کشورهای متخاصم از تنگه هرمز ممنوع شد؛ دلیل این تصمیم، اقدامات خصمانه و حملات این کشورها علیه ایران عنوان شده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/681061" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f34d6e01.mp4?token=pvuXCGUeViIYB_xdRnmk_fP9W3mYgvIjasnJmoy9ApcWfhXnujmm7eUaUHq0Ta7ZpwnPlco-fqLspC75fzKSVNnxvyKMPDEwo0hQg5ZOlI4bG_tqVqV-uVtwWdOZKhYkt53FsuuQuC78jJ-lCUj7TY6Z3Zwmjhk1_PnX4wx7GAg1JSvQKCesvOfFJQYZohAdCXrvE-RX5Ip1ip0GoEgmsWUPWTmst7mJPGdAjQtDBMjlEaNDnj1aHk8TCv6Qo98_Z5ZeT50VFV6iF2b5FJ5lU2EVvn0TrOKoqHOehsyV_LDfurTcjylrQPefzqi6YrGKkfb-wdxNu1qxcuJXhWQuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f34d6e01.mp4?token=pvuXCGUeViIYB_xdRnmk_fP9W3mYgvIjasnJmoy9ApcWfhXnujmm7eUaUHq0Ta7ZpwnPlco-fqLspC75fzKSVNnxvyKMPDEwo0hQg5ZOlI4bG_tqVqV-uVtwWdOZKhYkt53FsuuQuC78jJ-lCUj7TY6Z3Zwmjhk1_PnX4wx7GAg1JSvQKCesvOfFJQYZohAdCXrvE-RX5Ip1ip0GoEgmsWUPWTmst7mJPGdAjQtDBMjlEaNDnj1aHk8TCv6Qo98_Z5ZeT50VFV6iF2b5FJ5lU2EVvn0TrOKoqHOehsyV_LDfurTcjylrQPefzqi6YrGKkfb-wdxNu1qxcuJXhWQuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت رسانه‌های صهیونیستی از نادیده گرفتن ورزشکار اسرائیلی
🔹
تلویزیون اسپانیا هنگام معرفی ورزشکاران دوومیدانی، دونده رژیم صهیونیستی را نادیده گرفت؛ اقدامی که با خشم رسانه‌های اسرائیلی روبه‌رو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681060" target="_blank">📅 11:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f818b96367.mp4?token=TAf-SEjBRbTZIhxA6uO9B3IeZI9cHU_0QIbM4Skj7f_UMMgZ5GaAzsrWh3Ha4u6NNpUiYtwjU2kYe6PULfVQ4RhDmUtI_gC9GZt4CWvccCogISEBSMIqOYdCEzAZCT7H3g5qvj5g30Yj5Vlg73Er6nv89XgBlFuP2J1V8m2snhjv0NyrUx_9xXF9UQ612NWuYml2WuMrtWzXu6z-ZLPefTRNw2I6xvtW-MU5fTmGr81uoD8JLOkJ8yhAfWv1RIkgDG-4MZxollXvLYYexKYPfMfVv-a-ODOEV3q0BiI2YTBawHF4cyd6NGkVtTKHMAycGkE-XYcWr7I2ECo7VurUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f818b96367.mp4?token=TAf-SEjBRbTZIhxA6uO9B3IeZI9cHU_0QIbM4Skj7f_UMMgZ5GaAzsrWh3Ha4u6NNpUiYtwjU2kYe6PULfVQ4RhDmUtI_gC9GZt4CWvccCogISEBSMIqOYdCEzAZCT7H3g5qvj5g30Yj5Vlg73Er6nv89XgBlFuP2J1V8m2snhjv0NyrUx_9xXF9UQ612NWuYml2WuMrtWzXu6z-ZLPefTRNw2I6xvtW-MU5fTmGr81uoD8JLOkJ8yhAfWv1RIkgDG-4MZxollXvLYYexKYPfMfVv-a-ODOEV3q0BiI2YTBawHF4cyd6NGkVtTKHMAycGkE-XYcWr7I2ECo7VurUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عروسک‌گردان هنرمند خیابانی؛ اجرای دیدنی برای رهگذران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681059" target="_blank">📅 11:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904302f9b2.mp4?token=v6rvxx0pG1ldBGBNXSu6FvYxsrhXSssLHbh7iIBTgrQ8qH_zXNfKVstR5j2ffbRkJ_aMlmIfNXHLlmZfMvGvDuXDuoPbPbpvV5_klmCcA9Xes__vw_ggbY2wR8u2beWb2DHAk5LklBeFVq0263rhkEffWWnLouxNBZt3-hXKIEDzMc4k0MBmYsXeZlsG76Zj6WbnPlc_9g_z_QfLAAaxM7bD0975kHh0L7jkSysNX4lIQMRRcEhn52Ib31LXlsmVn_sdM20CtqhgToUuESvxrOXj5F1ZDAZGbuPObFjnrpX7-qeorvAZ4-M6tYzfi5UuEIkM0OlRkvRjIFf3ZNMjurfyIuqRMnyg83oStpRc_8q0dYJDzr4O2UAMs6-8kNekklkUuGe4UTamIUJv2m2Tt2oGL_tUSU-6X4AAbFxZHdCCSqCsoOijTCaMoIrwZ3iOJIifDbOUVPBsT6HwjauuVZuX0EAdoKs6YAyDNpfdMVQo_47Lv42YYnPW9HK_vQ1ufl6V2Uw5bNU35-QI2wbDFkfEOVxpyykzKiGmXfQzH6a4xTJnr9ypIFZ0a4eH27-i2-eMxWX5PTjo9YhFUjsYaYd4MTFGN0kKQZltLEx6JzYYN0x-qYYULGxt39Eulei5Q-lno9wVUog8yCTDX_FpxNyRqjWEtWbiQysBii5TltI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904302f9b2.mp4?token=v6rvxx0pG1ldBGBNXSu6FvYxsrhXSssLHbh7iIBTgrQ8qH_zXNfKVstR5j2ffbRkJ_aMlmIfNXHLlmZfMvGvDuXDuoPbPbpvV5_klmCcA9Xes__vw_ggbY2wR8u2beWb2DHAk5LklBeFVq0263rhkEffWWnLouxNBZt3-hXKIEDzMc4k0MBmYsXeZlsG76Zj6WbnPlc_9g_z_QfLAAaxM7bD0975kHh0L7jkSysNX4lIQMRRcEhn52Ib31LXlsmVn_sdM20CtqhgToUuESvxrOXj5F1ZDAZGbuPObFjnrpX7-qeorvAZ4-M6tYzfi5UuEIkM0OlRkvRjIFf3ZNMjurfyIuqRMnyg83oStpRc_8q0dYJDzr4O2UAMs6-8kNekklkUuGe4UTamIUJv2m2Tt2oGL_tUSU-6X4AAbFxZHdCCSqCsoOijTCaMoIrwZ3iOJIifDbOUVPBsT6HwjauuVZuX0EAdoKs6YAyDNpfdMVQo_47Lv42YYnPW9HK_vQ1ufl6V2Uw5bNU35-QI2wbDFkfEOVxpyykzKiGmXfQzH6a4xTJnr9ypIFZ0a4eH27-i2-eMxWX5PTjo9YhFUjsYaYd4MTFGN0kKQZltLEx6JzYYN0x-qYYULGxt39Eulei5Q-lno9wVUog8yCTDX_FpxNyRqjWEtWbiQysBii5TltI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احسان خواجه امیری: پدرم عاشق ایران و مردم ایران بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681058" target="_blank">📅 11:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681057">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
لحظه حمله آمریکا به بیمارستان شهدای خلیج فارس بوشهر در جنگ رمضان؛ پرستاران نوزادها را نجات دادند
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/681057" target="_blank">📅 10:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681056">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هاآرتص: در روزهای آینده آمریکا از هر تلاشی برای استفاده از زور علیه ایران فرار می‌کند
.
🔹
شرکت ردیابی کشتیرانی کپلر: روز پنج‌شنبه تنها ۹ فروند کشتی از تنگه عبور کردند.
🔹
پزشکیان روز استقلال پاکستان را تبریک گفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681056" target="_blank">📅 10:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681055">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
جزئیات نحوه احراز سکونت مشمولان کالابرگ
🔹
افرادی که پیامک احراز سکونت دریافت کرده‌اند و به دفاتر پیشخوان دسترسی ندارند، باید تا ۵ شهریور از طریق کد دستوری اعلام‌شده، حضور اعضای خانوار در کشور را تأیید کنند.
🔹
سرپرست خانوار در صورت ثبت‌نشدن محل سکونت، باید تا پایان مرداد اطلاعات محل سکونت و حساب شخصی را در سامانه ملی املاک و اسکان تکمیل کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681055" target="_blank">📅 10:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681054">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b369c954d.mp4?token=KSqeLv7vf6vWhxrpENqZ87TuwUIxzQ3oRfc6AlHNTAdPBHiKKxM6XMG3kFBxCJ_CAetpuj1NW7r10foJK4aNKjQQSJhlntDpECx0gF9p1_LsucIrWN7wz3QNecw3QRbTxu0ml1NGxuSNrNSmBa0_VW6cLW9F8Nxqkvql4gKAelQ3NFbKOJhESVYIl99qhHH87SyospD4dPJ_HBovyE8l1GQJMGRzXkvMTFpZXjITy_zS5km5j94Y3Cjf2R93RZdPY6eIMhgD5lqQnyaeKHqpH-OOob8tagfJqD58FmerrD96UN6gBqLroU44098VTKxmEG1qP8wh4SplZXW3FfMi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b369c954d.mp4?token=KSqeLv7vf6vWhxrpENqZ87TuwUIxzQ3oRfc6AlHNTAdPBHiKKxM6XMG3kFBxCJ_CAetpuj1NW7r10foJK4aNKjQQSJhlntDpECx0gF9p1_LsucIrWN7wz3QNecw3QRbTxu0ml1NGxuSNrNSmBa0_VW6cLW9F8Nxqkvql4gKAelQ3NFbKOJhESVYIl99qhHH87SyospD4dPJ_HBovyE8l1GQJMGRzXkvMTFpZXjITy_zS5km5j94Y3Cjf2R93RZdPY6eIMhgD5lqQnyaeKHqpH-OOob8tagfJqD58FmerrD96UN6gBqLroU44098VTKxmEG1qP8wh4SplZXW3FfMi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امارات ثروتش را به آتش کشید
🔹
تصاویر ماهواره‌ای نشان می‌دهد امارات گاز طبیعی خود را در فلرها می‌سوزاند و به‌دنبال ناتوانی در گذر امن از تنگه هرمز، صادرات گاز این کشور به صفر رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/681054" target="_blank">📅 10:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681053">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423325cef0.mp4?token=lDZyi8b79Uu8PxiRH2gtQW8Asxb0ks58jqPaMPc8Hsbx0tN6botUuKBckd0Ksqk6uCt5UyCLSXmZ3L63btJIrNodP8qE_NLc3cwXTmGeo3ss333oBwe0a7o_Jk3tWzGWLWoRXtFhvRhVXzZS3CU3BGRMv7zliF_vOIkbz033bzR7RFdsWFtxzV9UcRQ6_yn00IdmQDYBGWJLuTh5ZL-uAg-KcVAb0iDV-JlzhRvgl10PJNIrX0_P1GC8uUSp9jCv-CTsENXvN-bw_JUon9VWvPknfTpHtRdci8e0qKZpQoRDL4Oz_8b-LBjxYPaUMwV0Ux2Vcnm0t9eBUDLpp33GiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423325cef0.mp4?token=lDZyi8b79Uu8PxiRH2gtQW8Asxb0ks58jqPaMPc8Hsbx0tN6botUuKBckd0Ksqk6uCt5UyCLSXmZ3L63btJIrNodP8qE_NLc3cwXTmGeo3ss333oBwe0a7o_Jk3tWzGWLWoRXtFhvRhVXzZS3CU3BGRMv7zliF_vOIkbz033bzR7RFdsWFtxzV9UcRQ6_yn00IdmQDYBGWJLuTh5ZL-uAg-KcVAb0iDV-JlzhRvgl10PJNIrX0_P1GC8uUSp9jCv-CTsENXvN-bw_JUon9VWvPknfTpHtRdci8e0qKZpQoRDL4Oz_8b-LBjxYPaUMwV0Ux2Vcnm0t9eBUDLpp33GiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاس گل دیدنی نیمار در جریان پیروزی دو بر یک سانتوس برابر ماکارا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681053" target="_blank">📅 10:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHx0g5c3vAbDl0f6SxVpUL0JlZOwntbuYzCMKD3g-ZKumtjT45UEmkAD2VHCypESvrhIEJbducEvh7khj1P4StDB3NAzn0rUT5rdKmLHlwpBEbSiXa71yfWuJxG08ytKZj0zVeFzQvALs3R3BjN6fzuqr1YaU76sY-HVHRE-PXaAvcCIjxRMC9HaSkApowisHXBp6KE48S8TD_AWeUtSQXR_IGQc9FY0wBp2ICZz4jeu6MLAbKICxVMmuWxIfnSaBWejneUWYP4jlPNmrVP04WaT-wVAiF7zO7mbBlY8lmRpvTY9LD0JwUCRScJKXQkqiF3K6fpy1MvIan6kdj3qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دماوند سپید پوش|طلوع امروز صبح
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681052" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
آقای ترامپ! ایران نه ژاپن است، نه ویتنام...
🔹
یک فرمول قدیمی در واشنگتن وجود دارد؛ بمباران کن، هزینه بساز، محاسبات طرف مقابل را تغییر بده و بعد پای میز مذاکره بنشین. آیا «مذاکره با بمب» در برابر ایران جواب می‌دهد؟
🔹
این ویدئو روایتی است که حالا سردمداران…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/681051" target="_blank">📅 10:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3543f5d98.mp4?token=Sr7rtSzmeWoclEcdVEjcE4egiY499FsUN-w2R2emr-5nSbEsu9ZONee8uV3z1YmyIzXALEuHFqNFmp5gOJLTQPapEsSEgqlGVQhM2Suvv8TIDXiE7io6GXCxk79TJHPzRAfcO0u3_kPvfpuqqqs0LobDjKTd9ol9ibwp0EBBCrbbaioV_VTOKT84LyMSAopL7lnGv9tiUxQQ-0yJ6om8jrfm84yL56t04T1ADLIpwPjXrT1GzvJigLDD0l6PRt0wFRR4jgaD_xRijD999IXuH7t21E5_bFA1DPEOQz68iRunfzGxXSIJ-b7KFvHhCP2aZCAcwE3jhPoHraXqzX--LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3543f5d98.mp4?token=Sr7rtSzmeWoclEcdVEjcE4egiY499FsUN-w2R2emr-5nSbEsu9ZONee8uV3z1YmyIzXALEuHFqNFmp5gOJLTQPapEsSEgqlGVQhM2Suvv8TIDXiE7io6GXCxk79TJHPzRAfcO0u3_kPvfpuqqqs0LobDjKTd9ol9ibwp0EBBCrbbaioV_VTOKT84LyMSAopL7lnGv9tiUxQQ-0yJ6om8jrfm84yL56t04T1ADLIpwPjXrT1GzvJigLDD0l6PRt0wFRR4jgaD_xRijD999IXuH7t21E5_bFA1DPEOQz68iRunfzGxXSIJ-b7KFvHhCP2aZCAcwE3jhPoHraXqzX--LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ پهلوان آواز ایران
🥀
ایرج خواجه امیری ۱۳۱۱ - ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681049" target="_blank">📅 10:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اعدام همزمان ۳ نفر در آمریکا با تزریق داروی مرگبار
🔹
برای نخستین بار در بیش از ۱۵ سال، سه زندانی در آمریکا در یک روز اعدام شدند؛ احکامی که روز پنجشنبه به‌طور جداگانه در ایالت‌های اوکلاهما، تنسی و آلاباما اجرا شد.
🔹
کارلوس کوئستا-رودریگز ۷۰ ساله در اوکلاهما، دارل هاینز ۶۶ ساله در تنسی و جرمی ویلیامز ۴۲ ساله در آلاباما با تزریق کشنده اعدام شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/681048" target="_blank">📅 10:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f43352a38.mp4?token=Vj8v0zGmBqz3skuGOeDHSepAYMviUN0xkViCnaD1bcShm5f9fQIt1xf1Zq8jquSf-7xLMaKDQaNwrvPGKlVg87i59ZEbtcKIowSpPR_I_H_ooC2D_cyy8johDaMpvEAMiTWuGym-9sbYPzZ9bXOdNa1H5LDzUYAubHN-W9HDLgIurIHVJNc0Cs7BwXZpy2ljd6trHBbLv5hQ-z26jB5d0zrns_XeqP-5vAHPMCeWdgYJNiWr2A9FkHElpS37FgEcYwE4n9TagfgGvwiCb3xSnsqusmEj3yguyrTGnpNW3Cn0DqjzjsDG8r6MNdqlYRj5NETtPXqvqQvFHOH-2lniWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f43352a38.mp4?token=Vj8v0zGmBqz3skuGOeDHSepAYMviUN0xkViCnaD1bcShm5f9fQIt1xf1Zq8jquSf-7xLMaKDQaNwrvPGKlVg87i59ZEbtcKIowSpPR_I_H_ooC2D_cyy8johDaMpvEAMiTWuGym-9sbYPzZ9bXOdNa1H5LDzUYAubHN-W9HDLgIurIHVJNc0Cs7BwXZpy2ljd6trHBbLv5hQ-z26jB5d0zrns_XeqP-5vAHPMCeWdgYJNiWr2A9FkHElpS37FgEcYwE4n9TagfgGvwiCb3xSnsqusmEj3yguyrTGnpNW3Cn0DqjzjsDG8r6MNdqlYRj5NETtPXqvqQvFHOH-2lniWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در منطقه وست ‌میدلندز بریتانیا
🔹
آتش‌سوزی در وست‌میدلندز بریتانیا ۱۶ هکتار و چند خانه را سوزاند، ۴ نفر بستری و ۶ نفر دودگرفتگی کردند. ۶۰ آتش‌نشان با ۱۲ خودرو در حال مهار حریق هستند. راه‌ها و قطارها مختل شده و تالار شهر برای آوارگان باز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/681044" target="_blank">📅 10:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8d9f800d.mp4?token=PPQ4B9vKrlQ0FIzT-erOg4wYHFcG5SjNL8fNkJpXslwIhMlAu6XnjWykAABxoOoP5mafOfqlywfB9RyVVheAKBIORAm_kMHsuXLud-Vb0JtZL34wf9fx4m88ePLYkDCtSa6u0a-KpKohNay5y27jKYMXKOw-F9pzIMpUsF2DS1qSVVMFCawnHF9XeemZ2oYyWHTXa2m1PjypFRWNPAG1-P5R1giLnulNZTO1z1W7meZfYs7KXJU_FcJ8jtWyNCcl0AgdydYIBDkZIkIrO3_U6y5WSA1ASMB_QMsxPxOWwRc8-traqCYr505k9mev1df1RhunKFBGoUE3wyVztMlHKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8d9f800d.mp4?token=PPQ4B9vKrlQ0FIzT-erOg4wYHFcG5SjNL8fNkJpXslwIhMlAu6XnjWykAABxoOoP5mafOfqlywfB9RyVVheAKBIORAm_kMHsuXLud-Vb0JtZL34wf9fx4m88ePLYkDCtSa6u0a-KpKohNay5y27jKYMXKOw-F9pzIMpUsF2DS1qSVVMFCawnHF9XeemZ2oYyWHTXa2m1PjypFRWNPAG1-P5R1giLnulNZTO1z1W7meZfYs7KXJU_FcJ8jtWyNCcl0AgdydYIBDkZIkIrO3_U6y5WSA1ASMB_QMsxPxOWwRc8-traqCYr505k9mev1df1RhunKFBGoUE3wyVztMlHKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681043" target="_blank">📅 10:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681042" target="_blank">📅 09:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e21c7e90.mp4?token=d9NcZvJ2PsihkTrrX6SUSOJsvsw17JfZuaITPCIoe96X13AW5TRY9wHNJWkqjI7M04Mtbsi9za0kYaSOTRXcFJNdO_D5KZ0gkraO8dnJI-lFFaYZWTulDB6JkCPIFzuXuusziJfB_AYNUpRlxVMJzV9HC-tO5Mtt90bsnpjdIMWgRq24begRWeHcZCOx9-6frO-sCfk7v4Z07LFRr1vGtnsmba75IUcPizOGey1lUHtl7v1x6LjQwofJ9IwZMfmKSnZ73a6M8MMrxTnUowWWh35nTfCZXjj9RjdZ6UFs49YiAC91MK4Iw0nEi0deNzV0chNryGgM1BmuDtrCUyPhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e21c7e90.mp4?token=d9NcZvJ2PsihkTrrX6SUSOJsvsw17JfZuaITPCIoe96X13AW5TRY9wHNJWkqjI7M04Mtbsi9za0kYaSOTRXcFJNdO_D5KZ0gkraO8dnJI-lFFaYZWTulDB6JkCPIFzuXuusziJfB_AYNUpRlxVMJzV9HC-tO5Mtt90bsnpjdIMWgRq24begRWeHcZCOx9-6frO-sCfk7v4Z07LFRr1vGtnsmba75IUcPizOGey1lUHtl7v1x6LjQwofJ9IwZMfmKSnZ73a6M8MMrxTnUowWWh35nTfCZXjj9RjdZ6UFs49YiAC91MK4Iw0nEi0deNzV0chNryGgM1BmuDtrCUyPhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنجکاوی خرس قهوه‌ای در جنگل‌های رامسر
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/681041" target="_blank">📅 09:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681040" target="_blank">📅 09:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: در هفته آینده منتظر اعلام خبرهای بیشتری درباره ایران باشید
🔹
ما اقداماتی را اعمال خواهیم کرد که در تاریخ انزوای اقتصادی یک کشور تاکنون سابقه نداشته
🔹
این اقدامات ترکیبی از انزوای اقتصادی در سطحی خواهد بود که جهان تاکنون مشابه آن را ندیده و همچنین محاصره دریایی است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681039" target="_blank">📅 09:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نگرانی رژیم صهیونیستی از توافق احتمالی با ایران؛ «دست‌مان بسته می‌شود»
تحلیلگر اسرائیلی در المانیتور:
🔹
اسرائیل نگران است توافق با ایران، تحریم‌ها را کاهش دهد و درآمد نفتی و عوارض تنگه هرمز، منابع مالی ایران را افزایش دهد.
🔹
مقام‌های اسرائیلی می‌گویند تهران این درآمد را صرف معیشت مردم و ثبات داخلی می‌کند و دست اسرائیل برای اقدام علیه ایران بسته می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/681038" target="_blank">📅 09:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5ef514aa.mp4?token=mTNjBfLehQ7qxIQfGOKNHqxlgnpj-oZjZms19s8E4Z4WeqhWG7HDD_zLGn2qcCmGj7DLhpmm0vz9Cnl0pgYgEUC7kqK2l15-CiTjNf9TPKsEVnK_-WbKktO7iADJtNHVUiTm4pQNosEXSl-yNblYjM5VitEybSZmQ7BkxiPQPWRFg2pZLPw5AtsxOIjYqskQSxsKBsS_UWmJZZpICe_4XhKsCkwxS3MF742vZl5O4h9mf0-2fMkTFBuhd2vLo0JvQoaGJeUqcSHV8GBA-_bnLioe42tsmx6aFSel8WTeo8qt_s2XdNUnfWPJYicT25z-DHGI4q9Sb_I6ZbAkaTuMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5ef514aa.mp4?token=mTNjBfLehQ7qxIQfGOKNHqxlgnpj-oZjZms19s8E4Z4WeqhWG7HDD_zLGn2qcCmGj7DLhpmm0vz9Cnl0pgYgEUC7kqK2l15-CiTjNf9TPKsEVnK_-WbKktO7iADJtNHVUiTm4pQNosEXSl-yNblYjM5VitEybSZmQ7BkxiPQPWRFg2pZLPw5AtsxOIjYqskQSxsKBsS_UWmJZZpICe_4XhKsCkwxS3MF742vZl5O4h9mf0-2fMkTFBuhd2vLo0JvQoaGJeUqcSHV8GBA-_bnLioe42tsmx6aFSel8WTeo8qt_s2XdNUnfWPJYicT25z-DHGI4q9Sb_I6ZbAkaTuMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵۵۰ هزار فریم برای یک فیلم؛ پشت صحنه نفس‌گیر «بره ناقلا» که نمی‌دانستید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/681037" target="_blank">📅 09:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جاده چالوس یکطرفه شد
🔹
رابطه نسبی یا سببی با استاد میزبان برای پذیرفته‌شدگان دکتری بدون آزمون ممنوع شد.
🔹
زمین‌لرزه‌ای به‌بزرگی ۳.۳ ریشتر، مورموری ایلام را لرزاند.
🔹
فران تورس با قراردادی به ارزش ۵۰ میلیون یورو به پاری‌سن‌ژرمن پیوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681036" target="_blank">📅 09:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUozSpxrsAwT0vCfWq6s9ure7A9P-tO1u2eh2KW29E9OlZ794i_3Cvmj1QZdpox83x9xXMhGGae6XghHeigMyGzO6XRqZKza8gwMgNjQC2i112huOQNWsyvLXQRwCk2wgTWmVWkWncxHqzgwjm_FIqyyeRtce4kt3Qk5Qdf1R074kmnROAEpFzjYIFWBFJk5r4DSjqBjHOItTPmwsyuzrEk9TGVFY4avcHdcW4Vi2l0FeJail0jiQSCqh5LS56_DqDlGu79ldVoZQyq3OAIS4sVbTc2H2iHeWDXZZ60nf6XO0xa8n2LyJToD0tlShb5mBqy2Z94_HomADG0e9jOlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/681035" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq1ujbjBwUjuItNi8Fm3zwENOLSP1JNZW3D5YcTExAelDVKAk5USgEMAqmy9e0RNohPUqEO7qargL-4cfh_5ArJofUduVLQwuO_DcYfWcTZXowvOBD3gfdjebMWoSn199N0L9utQucarKm7huObWaknyL5cOSqRRDPfDMq4eE47-3RxViW4Lqa8BCgZpAipEIYG8xdmfXrQxJoElz0yhGaEjf6KUYNQknwbg6PX092qHhea6OSzln7QnPzDx5J6k5cCHHQR93CwMQkyEKa9EEO6SNbSN_zDpnPQzb6Bg1cvC1pyvgMhbiAdBZTLG-3GQyHicBAlugaZkejM7mYWYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخالت آشکار ترامپ تروریست در مسائل مربوط به فیفا و خط  و نشان برای مخالفان اینفانتینو  رئیس دولت تروریست آمریکا:
🔹
اگر فدراسیون جهانی فوتبال (فیفا) به هر دلیلی به فکر برکناری و جایگزینی جیانی اینفانتینو بیفتد، مرتکب اشتباهی بزرگ خواهد شد.
🔹
او فوق‌العاده…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681034" target="_blank">📅 08:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae3e26fc8.mp4?token=Ih1i8z1oWEHpjtp9h93oWBH6aPREuuv9jSzyyB13uxaptgqZoaHv-tnbXXpBTD8r-dpY68fAp6mdJ4HlRP309XLYte5WYNj7I2v4tpNpj4bRkW-MfGigcO9A-hytrS-TNKuvDbMfZMMvojILNOT4VI7CqvJS7DReVsvaXdBVPs1IehldgixORDaQcjRiGI3r7jZPM2Afu3Z4mY0bW96PcJzPWj0ofre7rBxPRArpjgITw6Szdt0FhC8Rn9t3624ysiPiwzZVmUiJrPL6lydJ-ZRL7GLTaEH2wHOC2KhBNT8bLnCajD3OZ_CNl2faMK95yLdo0UQFn6kcvCcmTRK1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae3e26fc8.mp4?token=Ih1i8z1oWEHpjtp9h93oWBH6aPREuuv9jSzyyB13uxaptgqZoaHv-tnbXXpBTD8r-dpY68fAp6mdJ4HlRP309XLYte5WYNj7I2v4tpNpj4bRkW-MfGigcO9A-hytrS-TNKuvDbMfZMMvojILNOT4VI7CqvJS7DReVsvaXdBVPs1IehldgixORDaQcjRiGI3r7jZPM2Afu3Z4mY0bW96PcJzPWj0ofre7rBxPRArpjgITw6Szdt0FhC8Rn9t3624ysiPiwzZVmUiJrPL6lydJ-ZRL7GLTaEH2wHOC2KhBNT8bLnCajD3OZ_CNl2faMK95yLdo0UQFn6kcvCcmTRK1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681033" target="_blank">📅 08:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2jWlgb4bTU8_RHaNVjVqH-rG5APO55yKvpkCGxTSm5K74r1C09CWbmqcVXsLD_vSz4Nr2bmU8_lgjfOOcEnR4UQVdAy6WTDRI771-H5O0E3sQ76sFXBvF9H7nV6AMcpFqUcCs3F9vVickzFX5GN-lIvDIhN9266KqTwlYx0-xBVmSalzpAPtDy612-_CjIhVle92HY5w4vNZu-4cIYUGPAbK56E9dWMcUBG2ibsdONpnwQeoug331JPU-tQ5AH1Qv0WdKbozcvCXEsiWEKaJrxj6n8Dffxd9j5oUpfGx6Ggc2GhA0kMbVzp0rzHE8wnRaNy16K3Erk1rgvP-jCv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای ترامپ قمارباز؛ رئیس‌جمهور آمریکا حتی برای بیدار ماندن هم مشکل دارد؟
🔹
جاناتان راینر، متخصص قلب، با اشاره به کبودی دست‌ها، ورم پاها و لحظاتی که ترامپ ظاهراً در بیدار ماندن مشکل داشته، درباره وضعیت جسمی رئیس‌جمهور آمریکا ابراز نگرانی کرد.
🔹
او خواستار شفافیت بیشتر درباره سلامت ترامپ شده است؛ در حالی که کاخ سفید این نگرانی‌ها را رد می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/681032" target="_blank">📅 08:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f277ac0c0.mp4?token=hvf-cwx-y0aRX-6YIpNxe7OXjeWWxdDm7UFViOEjocS-EConuZRZUazeMOPIlkNHwbMfRyzLyJFOSevSAHBEliRUGIqyF8ZvuTOAVyBkmjx9etB12JBpbZ6uh69O78684rZ-svc9yaT5OtMEznnDmcLrsC5s4wOxBHlcVUuzZEeoVLa-gpoIMR7GvSDRyNvwfBb6ojJViSZqA1uqY7shMkJdYKBcs9bU1b2oVRJVVsxiXxuvQ1X5HXTOSC6G0SypRwLDqXZcDGHr5iCWVk5KAkytWSZT8uNvPBa2AuatyB_5QVNFKHWiiw3vcumwaXTE0QaSYUOFE281517jMfsQioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f277ac0c0.mp4?token=hvf-cwx-y0aRX-6YIpNxe7OXjeWWxdDm7UFViOEjocS-EConuZRZUazeMOPIlkNHwbMfRyzLyJFOSevSAHBEliRUGIqyF8ZvuTOAVyBkmjx9etB12JBpbZ6uh69O78684rZ-svc9yaT5OtMEznnDmcLrsC5s4wOxBHlcVUuzZEeoVLa-gpoIMR7GvSDRyNvwfBb6ojJViSZqA1uqY7shMkJdYKBcs9bU1b2oVRJVVsxiXxuvQ1X5HXTOSC6G0SypRwLDqXZcDGHr5iCWVk5KAkytWSZT8uNvPBa2AuatyB_5QVNFKHWiiw3vcumwaXTE0QaSYUOFE281517jMfsQioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری با عکس یادگاری
🔹
پلیس فتا از شگرد جدید کلاهبرداران سایبری خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/681031" target="_blank">📅 08:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d7aa7044.mp4?token=CN3ZX65AawCi5N9rdqwaELtvKOxqBcTv_tejIFCnNgH5U2nPLaMo8CpNQfqniCvHjnzDKygB8VmGh8Ph7GUHKLpbaoffTANZIRMPPZsx0FDr7Tkl5z9jn3fYRFt0T3LuiphKI2-QhvDzutfsFJyuVQLX_xH69DhZuv0x1N_8gsXVCzcF_8wCkosIivl1cOFxyF84_bQucV0UJyiocztpz2B6BzZ0VYKXm2Nq91c9YmuzDuVTQTZj8PX8EU09DePQ1F4nvjMV9omMLHR8LyRjhW25GMyxXqpGzCaVBwuhr2b8u3QTmJ1GwCsMPRL6ueVYN6av9kIb9HeJzHreUHiKSRJmE21l3xLhCPvg5XTDPYU4Ic508-WvVtrZtWM9O9NxeSjANN8ple9ZrwRarbxZduhtI3i89IPZnY5QQ8mp1cqiRZ8y2GZtDarM3V4zdSK4d6kg5pCEKJIhbgDKzWt_VSGrzKLRbQYe7oXxMJ5a1vYCSPf4959APj3f3Detw4uQ4SdZ7wsLT7H_zC5IGXK62qVqcLtWRIoArrIFlC_AoOaDkplLiUfDtioTjN3tYj59D1QzgCdxe475m33e6wVBjIzsUR_WulvYywHpH5J4LNIuozBzVntweGUoqlDVplsFd8v3q-wssv1FX_rEOjHyHRJVUxJnDsoT34k7zpTaDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d7aa7044.mp4?token=CN3ZX65AawCi5N9rdqwaELtvKOxqBcTv_tejIFCnNgH5U2nPLaMo8CpNQfqniCvHjnzDKygB8VmGh8Ph7GUHKLpbaoffTANZIRMPPZsx0FDr7Tkl5z9jn3fYRFt0T3LuiphKI2-QhvDzutfsFJyuVQLX_xH69DhZuv0x1N_8gsXVCzcF_8wCkosIivl1cOFxyF84_bQucV0UJyiocztpz2B6BzZ0VYKXm2Nq91c9YmuzDuVTQTZj8PX8EU09DePQ1F4nvjMV9omMLHR8LyRjhW25GMyxXqpGzCaVBwuhr2b8u3QTmJ1GwCsMPRL6ueVYN6av9kIb9HeJzHreUHiKSRJmE21l3xLhCPvg5XTDPYU4Ic508-WvVtrZtWM9O9NxeSjANN8ple9ZrwRarbxZduhtI3i89IPZnY5QQ8mp1cqiRZ8y2GZtDarM3V4zdSK4d6kg5pCEKJIhbgDKzWt_VSGrzKLRbQYe7oXxMJ5a1vYCSPf4959APj3f3Detw4uQ4SdZ7wsLT7H_zC5IGXK62qVqcLtWRIoArrIFlC_AoOaDkplLiUfDtioTjN3tYj59D1QzgCdxe475m33e6wVBjIzsUR_WulvYywHpH5J4LNIuozBzVntweGUoqlDVplsFd8v3q-wssv1FX_rEOjHyHRJVUxJnDsoT34k7zpTaDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک پست: دموکرات‌ها از پنتاگون درباره شرایط داخل ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» توضیح خواستند؛ این اقدام پس از گزارش‌هایی انجام شد که حاکی از تلاش برخی ملوانان برای پریدن به دریا بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681030" target="_blank">📅 08:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/681029" target="_blank">📅 07:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCbmoY9s5vcfKsqk2glWskghDw0WONkS-n3RIWIXPJnQjW11yNpQ25KLHxGnmvhHCV5O5SSBlAFjtTJ4G_55SK-tcZC9gIYOHGzFFZD9SlLN2OwM5jPjS-r9Y9dco1MzaFsbk3DQ8jmhS8HtCuJx3a_BO7RX_de84Z--K_3DpE2iUiGYHmktz02OWgXAa5SS_A4qYMfxnzAZdeUwWHfmiP8r7RaAvAmS3qKRcGREna48OABYYugmLtgOj8hjAmdaK8OgEspTqnF9OzgbfWOkUygaIbzXle0EBoL3GSvlOiHgpFzlbYj46EYhEit3Ew9LaOScvJQaVzyvnQsJ9-Cnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیه میزبان غول‌های اسپانیا؛
سوپرکاپ اسپانیا از ۱۳ تا ۱۸ بهمن به میزبانی شهر استانبول برگزار می‌شود
🔹
تیم‌های بارسلونا، رئال مادرید، رئال سوسیداد و اتلتیکو مادرید در این رقابت‌ها حضور خواهند داشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/681028" target="_blank">📅 07:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrmJpyR29r-IxNXBBeMb7SXZ4MPJ_E5Iynb6JkMRPTBQPWp2npc-fRWuwN95M-9OU847z_wsa8z6Y7zE_pgDUe--coehsa-p41YMMMFh9ir0MC2rOyzKtJcVCzK9qXB9YwArayZi4Rulr9cUvWA2W0oI6jpvqpfWnHGw7Ua9d-K8IuiusxYxJWRfBTstkaA9alp8520Yz0RNFD-yfGSg5DNPJKGmonmDu4K48tOJry8k3fzmEA4bP1VMk5spFrFWn5JIUwAtELEgwVEMxK8xmeBk44QvbuxpALjb6A24-dCfIJmx_IluVIHh1dJjGZMSO2K-9BR6N_Al5qM2eb-UPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل خبر مرگ خالق چت‌جی‌پی‌تی را منتشر کرد؛ اشتباهی که بحث‌های زیادی را راه انداخت
🔹
گوگل به‌اشتباه سم آلتمن را مرده اعلام کرد چون فردی صفحهٔ ویکی‌پدیا او را دستکاری کرده بود. سیستم‌های خودکار گوگل پیش از اصلاح صفحه، آن اطلاعات جعلی را نمایش دادند. گوگل و ویکی‌‌پدیا خطا را تأیید و حذف کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681027" target="_blank">📅 07:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d201298a.mp4?token=pOi5zaxc1-YUo0E2n7T6BpTCF0BL3ZiXkC4yhDyBm0IJszs0orofxc5bRP52n-NxUmZXMRV4ZRPohjjM2jzvwEq0ncNnhC2ZIIM-U3UmluQA39Vxbt7M9Cx4FO2btf5MGQMBKdTe_NdxYghL7xd9Vb6fGNtqqN-KDSjK_KF8BwvzyMH0GLDS2oANqIpwBfa8WPJE_p4K3SzORGkj0qWDxmEvkz0db4RfjeAA9FJ_Sh4tFyT7P5hZZp2wqN66RxWMjADh3BBxq0smC8EMPajuTd_8Ci5XJqrlNfcMTJSkxD-UxBTxokCEApNsfHxGQp2KpFs6wdmAGSg1EYpnfs7OuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d201298a.mp4?token=pOi5zaxc1-YUo0E2n7T6BpTCF0BL3ZiXkC4yhDyBm0IJszs0orofxc5bRP52n-NxUmZXMRV4ZRPohjjM2jzvwEq0ncNnhC2ZIIM-U3UmluQA39Vxbt7M9Cx4FO2btf5MGQMBKdTe_NdxYghL7xd9Vb6fGNtqqN-KDSjK_KF8BwvzyMH0GLDS2oANqIpwBfa8WPJE_p4K3SzORGkj0qWDxmEvkz0db4RfjeAA9FJ_Sh4tFyT7P5hZZp2wqN66RxWMjADh3BBxq0smC8EMPajuTd_8Ci5XJqrlNfcMTJSkxD-UxBTxokCEApNsfHxGQp2KpFs6wdmAGSg1EYpnfs7OuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/681026" target="_blank">📅 07:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23dd90edfe.mp4?token=H4IwGHzJk--WGjAdDvNpdVkJcImUbQsbvYEw9otcIYN_dm5twB8ObVzeW4HCnzG50nQ8QsZIwgZ7kaO8p0XuyC7uVjzTEr4xeJ3b3uUucSZIiQ7oAsq4_EARjOq257bq_MYo7YTcuK1BDbUXbaWn6tJ33n9g3mfYzJSVuHTvrb9rRuJxuMRzPBiQ7_y3iokZdNqg4DGhmvepBwmUQ1GMebdQ48kTJYBPSGl-YVXxlam4NGTYo6yyRm83Ngel8_wKYcEQQXWTDUOMkrpEq_Wdf4N91_omYpzNXsiO1BRVFNZbARpHpJuB1u4w57RdHXzuweNMTRPqbWxX_-wcVzWg8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23dd90edfe.mp4?token=H4IwGHzJk--WGjAdDvNpdVkJcImUbQsbvYEw9otcIYN_dm5twB8ObVzeW4HCnzG50nQ8QsZIwgZ7kaO8p0XuyC7uVjzTEr4xeJ3b3uUucSZIiQ7oAsq4_EARjOq257bq_MYo7YTcuK1BDbUXbaWn6tJ33n9g3mfYzJSVuHTvrb9rRuJxuMRzPBiQ7_y3iokZdNqg4DGhmvepBwmUQ1GMebdQ48kTJYBPSGl-YVXxlam4NGTYo6yyRm83Ngel8_wKYcEQQXWTDUOMkrpEq_Wdf4N91_omYpzNXsiO1BRVFNZbARpHpJuB1u4w57RdHXzuweNMTRPqbWxX_-wcVzWg8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپهبد شهید حاج حسین سلامی: دشمنان اشتباه نکنند که به خاطر اشتباهشان هم خودشان و هم دیگران به دردسر می‌افتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681025" target="_blank">📅 07:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shs5NLzUsL-osizZprtz2p6eOxULs3plFI27EMueA0qblV-y0DpAQ6hS8xV4Go5XQCu_CnFdKu77yaRgBWp1392ipWncYyd_UuCoQ0jVxuK4yihRQh2wDPwdFkdDDt4fW5E9vzaF4Tsx0U5Q2n-yfaRexMG-N7LHTMixv3pF9B31wTB48Tt63yoAMnFEWMXF5-ni4cltgWH3VyQ66V0Od8GhRlNLN5-E6_PFYVFCOsi32aUV3IPxduubLgLEPjQd3osJ7cAlgvr4KqdmwD0i8yibAhReCObqL0CNJzTCB469OnDwR7H0gp5y28wFrYglcon3TPVrXqAvg8Eh0xdf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۳ مرداد ماه
۱ ربیع‌الأول ۱۴۴۸
۱۴ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681024" target="_blank">📅 07:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlfDwI044nF45pLQPb3TuFB3KbnXJ0cDFu8BmstXWks1aWWOpSSt6gtrivsZEf9idT4q8eFxzzbruOga81VNNpKYc9xEwiHCIWlVm9__eiVbUvXtquyXPOdtN_EtdVYnxXaq-7-bA9BpwATSLHsQJz-N_YaTHT02vFRu9mi0hl2nPvTX61a1RQMAgjjTR6wTdpzEUNf6GB9DdpqGfE1c7C2Vv6a1DV58RQTdbztmhLnH-MHGz2pGeiQMUBaHnMofdl_ysaNll0mbwOygOHF_YpsGgqnBAN03JTq_s472UoLPzK2adSDoWdheA_zuTw3mUhogCYGzksDeuPQN3tschA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/681023" target="_blank">📅 05:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عربستان: ۱۳ کشور به طور رسمی به ائتلاف دفاعی دریایی پیوستند
🔹
وزارت دفاع عربستان در بیانیه‌ای از پیوستن رسمی ۱۳ کشور به ائتلاف دفاعی دریایی خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681022" target="_blank">📅 04:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
‏منابع امنیتی عراق: چند فروند پهپاد در اربیل رهگیری و منهدم شده‌اند/ بقایای این پهپادها در یک مجتمع مسکونی در نزدیکی فرودگاه اربیل سقوط کرد که تلفات یا جراحاتی به همراه نداشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/681021" target="_blank">📅 04:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
انفجار‌های شدید در اربیل
🔹
در پی حملات پهپادی به نقاطی در اربیل، سامانه‌های پدافند هوایی فعال شده و همزمان منابع عربی از اصابت چند پهپاد به اهدافی در این شهر خبر می‌دهند.
🔹
تا این لحظه به طور دقیق اهداف این حملات مشخص نیست و برخی منابع هدف قرار دادن تروریست‌های…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/681020" target="_blank">📅 04:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681018">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شدید پهپادهای انتحاری به مواضع تروریست‌های تجزیه‌طلب در اربیل
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/681018" target="_blank">📅 03:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZFvryvPsVOAwiLK8GecUCWDhbegvawOUqM15iUVs9PcxSWEnM51vBHA-ONuXWErwgii3Z1aRMfqwiXOu3bikXTIa1n0NIN5FBE0XYo00ErQFSBb1JnDvbDzg_AgbkXpSjiipIBWmpNQxmuVPlYZ6b7G9jesnSJfxSxZ8Z5MwGC_tcWQQl2esk2GNfWeCQSM--xE0vsBKlbus-YJVv6QRQXBFf_3-9_wgjqmQFKFf2TFVLhbFv5qKb0xnN49TUoLWQBkxYp6QsNUzPPIYpzERMsQUCXkRtMc330BZqM5UKViOKFXl9GPKFR20R8fTvhASFJTD1XL3p6rQsYfo-IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشینگتن‌پست: آمریکا ۲۵ درصد پهپادهای شناسایی خود را در جنگ با ایران از دست داد
واشینگتن‌پست:
🔹
ارتش آمریکا تقریباً ۲۵ درصد از پهپادهای ریپر خود را از دست داده است، زیرا جنگ ایران زرادخانه را تحلیل می‌برد.
🔹
این پهپادها که هر کدام تا ۵۰ میلیون دلار قیمت دارند، به طور گسترده در اطراف تنگه هرمز مورد استفاده قرار گرفته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/681016" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35e3c637f.mp4?token=WKy1ddjM_OBzMAZD_uAfWgHO_yHtanPeUlwivPB4tzYO72EZDKOhDGZX0gd0FggGzOCki7A8qIZIw0aQGlvbJrN-EAnIe9-F_1KSpjXDKdOFvoE7Zoy9oClhx7jxvwBDC0rDHnaabNx6MVoKE4gRBkN04v_x1GQ02YZjw9mGdyEW9umzV_ayM79SE7E9oK_RRGAmdI6ZXaOah6OvLONMq2J79Y_cJgPctdXiFaZ_dh23G5mcmpVSnBudPkeqBuIl-SzZhKpa6JdFYK9XivuWO_77VNH3B2gobectFKAXPCbgNe14PU2gRhSPHM08uxRVcNPLjrk8_v6HFHXd1kq9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35e3c637f.mp4?token=WKy1ddjM_OBzMAZD_uAfWgHO_yHtanPeUlwivPB4tzYO72EZDKOhDGZX0gd0FggGzOCki7A8qIZIw0aQGlvbJrN-EAnIe9-F_1KSpjXDKdOFvoE7Zoy9oClhx7jxvwBDC0rDHnaabNx6MVoKE4gRBkN04v_x1GQ02YZjw9mGdyEW9umzV_ayM79SE7E9oK_RRGAmdI6ZXaOah6OvLONMq2J79Y_cJgPctdXiFaZ_dh23G5mcmpVSnBudPkeqBuIl-SzZhKpa6JdFYK9XivuWO_77VNH3B2gobectFKAXPCbgNe14PU2gRhSPHM08uxRVcNPLjrk8_v6HFHXd1kq9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شدید پهپادهای انتحاری به مواضع تروریست‌های تجزیه‌طلب در اربیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/681015" target="_blank">📅 02:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فرمانده سنتکام با محمد بن سلمان دیدار کرد
🔹
خبرگزاری رسمی عربستان (واس)، از دیدار فرمانده ستاد تروریستی سنتکام با ولی‌عهد سعودی خبر داد
🔹
به نوشته خبرگزاری واس، دو طرف درباره شماری از موضوعات مرتبط با همکاری‌های دفاعی میان عربستان و آمریکا و همچنین تحولات منطقه‌ای گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/681012" target="_blank">📅 01:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سنتکام گزارش‌ها درباره تلاش کوپر برای حمله به ایران را تکذیب کرد
خبرنگار روزنامه جروزالم پست:
🔹
تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، به من گفت گه گزارش‌ها درباره اینکه براد کوپر (فرمانده سنتکام) در جریان سفرش به اسرائیل گفته است که برای ازسرگیری حملات علیه ایران تلاش می‌کند، کاملاً ساختگی هستند و صحت ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/681008" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa556d2c4.mp4?token=KNdh3C1IDcaFZShip8SyVvknxHBRi9__ksvRjvJNfOE6N0YsriJjVUkpqHZcd98SpdRzaLsxaPxaaz5pInf8Q85A-JvY7a2PUn0SHyUErBHYER2Z_Y1gkuMipZ9x-Zy1iWJitUiAMNSsxiDcVwFO1AZlIpvodxmPIaeNRjkVAd0bSIm6bk0aaWfFDaY18rADTS4i91JgZZTXZQQWGR3Sq5vvJ8w2CNdJvmAOsgR1JuRmbLO2Ye6GdSFqcLE_JpO4Pa1UVRxnczCQl1mj9eEKEYxlhOPLG6f0US-Q_GADhH7WZahYvF5puflMUOHbjUPBEyClhGDz69VLm7hBB3_3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa556d2c4.mp4?token=KNdh3C1IDcaFZShip8SyVvknxHBRi9__ksvRjvJNfOE6N0YsriJjVUkpqHZcd98SpdRzaLsxaPxaaz5pInf8Q85A-JvY7a2PUn0SHyUErBHYER2Z_Y1gkuMipZ9x-Zy1iWJitUiAMNSsxiDcVwFO1AZlIpvodxmPIaeNRjkVAd0bSIm6bk0aaWfFDaY18rADTS4i91JgZZTXZQQWGR3Sq5vvJ8w2CNdJvmAOsgR1JuRmbLO2Ye6GdSFqcLE_JpO4Pa1UVRxnczCQl1mj9eEKEYxlhOPLG6f0US-Q_GADhH7WZahYvF5puflMUOHbjUPBEyClhGDz69VLm7hBB3_3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ونس: قیمت نفت امروز نسبت به روزهای ابتدایی درگیری، به طور قابل توجهی کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/681007" target="_blank">📅 00:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680998">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyVgcvEgS5EREpz-RrWuGq6DVQBuWb3Ka7K8pMK9F3SD5hyckxEUWPm_bjptvxwWNXFyEJVCMU5LY-sFwgQy3YMLRfE9V790TA-C8RqIE06CJsSBUzk187zeRjWgdHNAZBsAncXIOC-JSywKP4gvBaGV4-QuGWAD6ob3eM0bhH21rUTCeEMB7btSER-Hjhkkqkbrwdv6HjlF5QeESaD87aayrCDp8ewxLuifYtYvyZlA59ifzwEZbHwVAHNfneIBDAEn92ohgzbu1L62rTpSIJF2EHHNJU7ZdzIrEooTM6BQTPeHYWKPeCSG7B8c39MKSqxBwbxZIkob8w7W8eYIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxiwLjOabwAbQIbMXSfmenaNWKpK-IWUoUcTDrIBf3FY0Eq3v7UXY9GeS7veVflwGZVeC-GK_c0givts66_2vkaff62qZTRkY3o3SSlusOt1dHeMdwV1Fx8_0f2xbbrrLyVw_x4VVpwpl6ZAyFYdsh1R4Uhct_HG2Fa_zsmne18Piv-lMw4uCt1sKMbxJoCkaOyNxEyj7b5iz5_NEWROstOUArYIo004SHvDdPU_NFUBI_VuTol-89bcvLtEQgJhljkfGOiW9uVDX_tDLLfI_Hx0Vy91OzmMAyTLRTHpM0LiAMPL1a8PvLr5SMt9VbOq55spzH_f5HeWAEnNc6Y9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovnLx_RElkOB_b1BqoFXtWFUP_UWio90KEdiJA7XUTXR4Z05SgcAeGmfT7b6lmZ3geZ8NxdXFl0ndwaD8Md05DwbGpr4JJA0rU8D2ahnsY25iyZb45e0YRw0RNNWGPXSpKE0lEaWTw3KowVhvLcgOgJ6SCvPdkAaImLinCg41BOWG1-Y2_Qi49yKnKMRoTrIK6DRWdh_Berkx7bYklGtCJcyyV1fGeEOgDnTeIFXY9f3-I0VT0r4dszstdcPUjb8axiIAIm6WeB11K54gDqf-e5wH_ajjcDoJwyynRQLkmkMCBdyIAj4xVI_4PokXCCrNNAqoEDawqXOEUHAII7qqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCyG1o5H6rs4uy7rS8tJ3eS5S-yjVWQY8wfajnJjjB_aSh4raQ2T7DNjWyqq8B2DWyk5hjPSVieh6HlRiA1e7dgT_aXMbe5YEa1xKIBuLXZmpYK_DIE-1eX0tVaTZ09lLrMOopGF1AFVSjcEbX6yU0JJC8I--5aqoZUyM9Ki7G6cMqegLq8GvbSdN5Bx_9Y7F2GbaOOpfvOzfOtbNkg26ZT-0XGeuaMiQS7cUpyrKTecgw645Y6LrSdMrQbWyJJHfeIjmTiiiwsgrZ2MzcWSYhEwTtd8yDgVBRZ3d-52NprJmpZaHd103Wgm55F1wyEDxGI0R6TA0FML3VVsN28DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf3YXo9NHoOctFqJph2fT19-Igu-15wPQeSSaPu1Zx510HwuRclATNe_fwkDPNpDDVyEAALl7S76w0sYlF8aPsyqZsYL4Rp2iaKNjmRWIoRhKpPhBSSIlIMX43-5igP4Zu7_wQG4cjq6wAmOpc7n_xgKvPXcURfsvQIh1xq1lMoJz_gEPCkSe55n4HCzpSLYva7du_roXv627f5yWHjy7kFEdRh7Gzo-XmsPDgaZG11b4DW0Rj6N784Up-j3IGDjNh3r1WYmNhrZtW0BET2Hyfcxic9Ljx8QyxTuaCExqU-fCNJea2BRzKGzzmV4updZqYY_GfBoP_NO2Ks9-i7QNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLUVRQCaXZPS5LRudk-j2v3_nt456wx3G7rnBJFhClVCSWIC4OXOLE4XbbWm15PvuvtRWV0nQfUyGyaEtGXgRCnQLMT8TnTLgiuE50B7K4b4DXbPsbOqZiRgk7emACR06g2SS7L3VhRSooumgxeEYZDOirxfcVQ7wkAFL4L_3zxDYw1109Iaif2IWT3_B__hSjCWNWW9ty7_ZzczPceWWcgY7y53a7XXXgvwePnvT-TwhXzYx36bBU_IsT338i7NCNRivYHkUpEUsBNg4PhU5Lvg4FmGSXUTGILjd_WG_16CoTOzh9aAJ6OTNhHaeU2PWAOutiD4t6F6EbjoygQKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_HlfjTklYLFFz2Ljb2sYnN39etnPsNtMMOiU8sDeGnyfCNYVJ81gjPnLBiy9V_a5SLcd4vvJQyupZsr9a1OaPnq4u-EpRzGAuoIgyBdzzdVgahqMe6nSTUu3EFimAdZlYHgTOLdjNY6yQJOUmwUdeeu708pFp3_D2isEEdG-etTbzWeovmHWII065B4PHaXGTNGKyee4SuT26P4cfKhZ0SANAKpQRvZl4dHvDXHHXgdGgqFirEF56UDEqaObfWwVQUexkNJg_dx5YB38wTiZYZ6hw7v-8HkBH-zGfin457j5DvfdnoKyoSkV9ianwVWOgLtAYqW52sBCwf0jxFWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFNvR9TcRUk77KyTf4bYI2FiW1B3vHZarBxxknYZFQJB_ejnQFodlHnOJC762Js1HPwzl1OFe4FSw3gb5VGFvN8qVVjDmXkYcbszadLCsA4mMq8q4F8pmXFHijLRlqgiwRB3fZ1iuFrG5Z5i9fsXJHVzkL8CUsLiT3vh1qGoUyoYkexkCbG5Hd8888wcbF3UePYBAVlWBgjfEK7OHfMziiZ4uaskJEZVbcnXP4EXsL05ExBic_PqKK1889JhaKZE1OoLFBS0Tqmn2rH6FjMJFhg2k-lnEQn5wgGG0G3BxxGcgDih8mC9mWD5NKKGpXxFIGx6sQMve3CU7QGrCNDoaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ردپای شهاب‌ها بر آسمان ایران
🔹
بارش شهابی برساوشی یکی از تماشایی‌ترین پدیده‌های آسمانی سال است؛ رویدادی که در شرایط مناسب، ده‌ها شهاب را در هر ساعت به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/680998" target="_blank">📅 00:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای امارات دربارۀ حمله به ۲ کشتی در تنگۀ هرمز
🔹
امارات متحده عربی مدعی شده که دو کشتی متعلق به شرکت ملی نفت ابوظبی (ادنوک) که یکی از بزرگ‌ترین تولیدکنندگان انرژی در جهان است، در تنگۀ هرمز مورد حمله قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/680996" target="_blank">📅 00:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrEE09NlkNADrnKT-OKySAssUE_IGNyBQt88O_nnas9eH-AIf8V99yjn4v6N8xh-oCoHWN-YqCC-QwsqQgSjmttSjQfkZ4z6yVDnJH1KVw3IKJuCwgCurCLQrda7jK9vkV3kSfaQ7T8Y6wmxXJ4anQmjdBN-s3MumWPv2QggTx39tLnES8vrPv94O1giwZdXpIyCTf9c3N7_0w4oxTgmuQDDLvo8BDbV2BgCA8u-Dz6C-hXUe3r9YvSPB0NPh9Xxy-74wwvNbHYw1JYZM7Nk3i5N3zq9T6hR7Mcp0gDyAjAx64UCP8luEi1oMwuuoQjPCV6tAMk74Wm2W2NVUuV3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندازه مکانی که ترامپ در جریان عملیات «تاکو» در آن مخفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/680995" target="_blank">📅 00:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680993">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSmW2TIMczNx5pCJfg8x62PHnc2oE1tQr-vQoo6JsR8a9M8C3WJ75J_6NHvIMAvWNM77fcRwdouHhrH9vg1RTnAxth62uREdVR0z_NYEfx_ElOwX2VvrakjhBn-kIBzD_df6IgEIqbi4CxakT47MEYBpsAt0uNX_fHcV_oZaQZgoJx2Hu-KOIVxiCRKut-XgoY001rxnLB0s77vjcihUiG31rOVKoDPnnbqfJRIZF3fRKW7L4XzobLo4EzGxuCn-VoEe_diJVgmlOUNLpQC2KPaueIdZZMIr7e6brNabQ7sW2O1kX51G4MkbklBTIqjX91_D3O2qxyOD1HsU6VTS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط ملوان آمریکایی از ناو «آبراهام لینکلن» در دریای آزاد
🔹
شبکه CBS گزارش داد یکی از ملوانان بال‌هوایی ناو هواپیمابر آمریکایی «یو‌اس‌اس لینکلن» اوایل ماه اوت در دریا سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/680993" target="_blank">📅 00:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnDfnJG53avTYNySzCCr8z56yA4ahGnlI-HOe-VCIib8h1FWyiAThXdn-KMp9XM66HgfnHmMVF3y3B4hVSTSoJswDPijywizM5zIc5o2Au2DAEPnCMi4nBj0WmhXmWOXwLAGaA0GeWriXTNI4w8rzP3rOJtpLW2kvQJCsih50bzj20XBCRYglxvj1DTdjlzrApxbA-d1URhcC96edO-Uk8IqZwkR1V5EGEjFyw1U2p4tmhqaHlFr44-OQNc2Shg_bUWXh_4tOwjkVwYPOfmpEZLegxqBvhGObgvnuA0TdSn_oG1SVE2wbND56aSmIng5bmTva_h__A9w9yHHjc7TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsWRivLHgY9gfcFo3qRA3MyN9xSo45o_T_7Za4Lp6sVqM17RkEtRLsz4cBDxG7ylo6xIRZP8x6OxUI6e7EY_ckalN0fcsyZPAs-UuEsAQ2tNhCwZCOFghRcrzTLUaKJ198XivaXc8z9W_0i-GvU6bT28sMKh1sU-ewVoecgGg-t4_9M5dQLDAqZTohd9vKGBoDFrPT5HP1w2x6rvLZnnmW5u9StPNMqSmGuJ1Ytby3JLCchvbOa7j5Drhp5BkRbyqmqzHkxEDE5FsuG4o-efgAGuM80xPpP0CduPh2Cx-nQpcryKETvs7_JkjKjEvJ6iu5i9fEC_rC5-IBVGA9ICmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازسازی فرار ترامپ با ماشین حمل آشغال غذا
🔹
نحوه فرار ترامپ با ماشین حمل آشغال غذا سوژه کاربران فضای مجازی و رسانه‌های سراسر جهان شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/680991" target="_blank">📅 00:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای جی دی ونس: ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند  معاون ترامپ مدعی شد:
🔹
من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت.
🔹
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/680988" target="_blank">📅 00:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX9ujDk-nrr45d8y_YCaWZvjqtzKXkoiDaJz_fzs6KF4oDsvFgzVLys8EqqoVM7TGgqzMupgKi6gP_a7L8relktvt9_GsjZbDD_ZsNuOhnOpqniyzkJwYbPDhH-y6K5xrou-dWOKkAnp4ND1nUTGB7iOvaWldlWIu5z8b2mawW7BnNni9FkAvQMGm0kfp9pDlHw6enjNS99zZklCBPyChLL7CGGD1gKg5KCDi7uFlt6r04-0NDsbJDya3mhACiiRD5LGhbkySJsFsFmO7yPnIdb9TuTG_yOgnrtsOUJsO0oydbtLxOKaBFa4DSYlxuCovQgueDyynpl8KnSr9jeVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از شگفت‌انگیزترین کشفیات زیست شناسی اخیر
🔹
اسم این موجود Bubble Snail در آب‌های گرم اقیانوس هند و غرب اقیانوس آرام بیشتر روز روی شن‌ها راه می‌رود و کرم شکار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680987" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5nabu1p-wtkEBfs_u3jpGpJJFe6xvJq6GU4f1WrR75gggjYJSN2_4dLOAlfKkXSs2jVOQmMTyvaFBEeRzG9OtDuXBXNXwy2CoFn0WebMm0XzRyzYBgl3_BD2Wc722UMQRyiEjt1G4c5rXUe05mFkdyo-v9tHc80YLnChP2oludQXK2cp9btIKxdE-_qs4_3qXMpaQ7zVSJ5iY-nmSpLuJpmaiUQ77_RcO2ebHPRad-veEKywF5PkBtbtD5Fd096m-altjpkmlgFRqInGozUOBQV7shChRy7Ipd3H6rKSAVFIfKTZ-fvx1zvg8pQByJ-Js8k8hdT9z8SRT3GVUWLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایده های خوشمزه و جالب با هندوانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/680986" target="_blank">📅 00:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f939645d.mp4?token=i4C7bDoXiWq-ZkswcFMQfhuwub5y5pVRU7P0pwY9QrnJAlojasm3HZ7dtxq2gLGKNuUWrcLbIsneyETklHFMqBC9VM-FDTlxL5HELuxVW_R9wIPjaBCY3jDIZeujh5o1SIuM1n4kRKrW3VmmN_d8D26ymB4hQQH0b0y0IuiFY7pNIjq2VXGO73rNfSOoS_L0t0yL7Re_Fi5Qcoe5mR_pPZ8DwGe8dwlbs8gYWSRWzvU4-ZSbUrdB0UpH-O2ymyrB0tLpKT1_byPJWSpb3WRRjPHh_xL3w95zMRd7jWxeyL4h2Hng2StGqnuYgD97tz0_p4LOLRxsdq9051UXxE5LYhYGBCypjVode3lceeZqo9WiCNR1LiZKdGZaVtVtUhTzyi24anIt_Mg5Vuoogzmv5lA1CA441JCQOwD5wDmQjzlcwhSN8eg70qyCUiz1wGUFUL2-BcMYoIZOWT9fhTuvLZPx6mcuSH_foelWTwqSc3FOufBVslHoq_dO7vgkEAxQIGkpVAI6dj3aV9Au_oJ2mxz8DqHFc-ovI2RVCXfUy50uSxeVEyyXq7Tt400QsedSVZeFdmCN54nl0-JOuhVip9jCB2hfI2ov0ZxCvDio-R4CkQKAo7nolCELv3a_dOPax5VW5E0p1e2Z9XI1mvSBZRh6oBH0PrZWAaTv6jpJXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f939645d.mp4?token=i4C7bDoXiWq-ZkswcFMQfhuwub5y5pVRU7P0pwY9QrnJAlojasm3HZ7dtxq2gLGKNuUWrcLbIsneyETklHFMqBC9VM-FDTlxL5HELuxVW_R9wIPjaBCY3jDIZeujh5o1SIuM1n4kRKrW3VmmN_d8D26ymB4hQQH0b0y0IuiFY7pNIjq2VXGO73rNfSOoS_L0t0yL7Re_Fi5Qcoe5mR_pPZ8DwGe8dwlbs8gYWSRWzvU4-ZSbUrdB0UpH-O2ymyrB0tLpKT1_byPJWSpb3WRRjPHh_xL3w95zMRd7jWxeyL4h2Hng2StGqnuYgD97tz0_p4LOLRxsdq9051UXxE5LYhYGBCypjVode3lceeZqo9WiCNR1LiZKdGZaVtVtUhTzyi24anIt_Mg5Vuoogzmv5lA1CA441JCQOwD5wDmQjzlcwhSN8eg70qyCUiz1wGUFUL2-BcMYoIZOWT9fhTuvLZPx6mcuSH_foelWTwqSc3FOufBVslHoq_dO7vgkEAxQIGkpVAI6dj3aV9Au_oJ2mxz8DqHFc-ovI2RVCXfUy50uSxeVEyyXq7Tt400QsedSVZeFdmCN54nl0-JOuhVip9jCB2hfI2ov0ZxCvDio-R4CkQKAo7nolCELv3a_dOPax5VW5E0p1e2Z9XI1mvSBZRh6oBH0PrZWAaTv6jpJXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناسان فرانسوی: این دیگر چه اقتداری است که رئیس جمهور آمریکا مجبور می‌شود از ترس ایران بین ساندویچ‌های مرغ و نوشابه پنهان شود؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/680984" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBcfunMdeeT8gmVo0G0ThPZsArfjR_Z8nCdZ-_r3caaCOpm4Ck-5KmMJpHbVKcc179AkhxPpgugnmER0Tn5lvBsGhQv1FuG1VIyB5WEVw0LVrSaRsfYTb_4iRIIFqh6ostCB3Mlrvb38kJmi_c5kfqtMCfhUyc6P4nRF7vxp8shXiDaIV_p9fOyQNgM2UBbOdUyK9WkM3SI863oTcRFZw4vT3RqaCg5kgZ33vpjsRx96rqa2laxW9Ohc6vvBb1vAo8XpwUL98jaPPljFOkdjKScjIpYM3eqQ3hc-zdpZz8LrtdRcPCwSHBdLGffVgC4SJfU7EL_06_q_JRdBWtiTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/680981" target="_blank">📅 00:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3320b0f7.mp4?token=QDVe0dZgHumFtZ3e4m6sJpjNyobNShyXckkotNx2fWoma-pFuQOJURic7WYW_C9fuK6EEPXVD_psVhXB3AUpN3sWwrkq5xP1P3s0LJjM19pMUfhp23fs4gEQwpnGzF4Bn5sDtJm989UYfxt-CNXLWe72Enm6GW-ouN5o39oR7vvvTeXA_LSnVolaBUyzJZA_NDHQ4WZTlLozsj3YysgbFoByIKpL-Vl7_jv63TCehS1_84P7TK3KvbOdUapRf_1cPOHJtRGYq1vO3Uc8PhqPNkfvurv-upOincPU6w4uG2SapFFAR69IX-2VRVSUKmrgRMotWS9tLf0Qzuzy7RDrvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3320b0f7.mp4?token=QDVe0dZgHumFtZ3e4m6sJpjNyobNShyXckkotNx2fWoma-pFuQOJURic7WYW_C9fuK6EEPXVD_psVhXB3AUpN3sWwrkq5xP1P3s0LJjM19pMUfhp23fs4gEQwpnGzF4Bn5sDtJm989UYfxt-CNXLWe72Enm6GW-ouN5o39oR7vvvTeXA_LSnVolaBUyzJZA_NDHQ4WZTlLozsj3YysgbFoByIKpL-Vl7_jv63TCehS1_84P7TK3KvbOdUapRf_1cPOHJtRGYq1vO3Uc8PhqPNkfvurv-upOincPU6w4uG2SapFFAR69IX-2VRVSUKmrgRMotWS9tLf0Qzuzy7RDrvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف ۳۶۹ کیلوگرم کوکائین در اکوادور، با عکس ارلینگ هالند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/680980" target="_blank">📅 23:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای جی دی ونس: ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند
معاون ترامپ مدعی شد:
🔹
من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت.
🔹
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت و گاز را برای مردم آمریکا تضمین خواهد کرد.
🔹
مشکل این است که ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند و توافقاتی می‌کنند که بعداً از انجام آنها سر باز می‌زنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/680979" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680976">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVKH1bJIks-rQtVUFLHkNh0xvz8TzAW_ZUx9y3cSEex84WyEBxN7PRd0JjzKTd_MrPZbouxyFKVGEYcyGn3pROYQZgzJrMOc7ZEjmm2Onpv5pHnO1XIXSvWcCE_hXVp8hbEQZnqa-4wltj6i2Cnnb5x3RiAG_sgCigux3wEo6XB579XOfGPGXmPEk4feGi_XFQwZBsmevQz5VUPtym85o0zfGRygtvTCCnkuvNPK56vcnmiUS7C86yFLMYJKeeb5LZyDboncfMpSrWQUKThq_nqHZFDbBC_miIs_iUlMzloIqvIjRIm7MeOiMAdNMQTh4jNhdq9p9OaZR6xofz3bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VknIdkUCA9pSHGwoMnMBrGuUh8ErLs1ml364sjJd-iRCbM7JeDutTqRowzS3lpZPs1YcFfeYxzRwZ2-KvEDBiRXUYMvrvEjIpbOYjfJZJsnOZSbyTU2wgFwRbGCC03X5LbMIOZNgB1KVJBOnj7zWzv3cRlZvDBFRoUm1D5y8DrV52XE5aYLU3pvOHsxGDA8bIWXOD9cUsYRf6EyTNJG5XBrWjsMyoeZjXNRZoI1SwEdr0QILvW-sUr6U2soZ3pvWPcxlKVqDWqTWeEGPLxmiPVlrDefhnL5N67RxaOoZcJInnXzuoxJeTb3YJi6qLv9UlrNG4M-XmDLZqM7q0Fdwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXwEUYR4p7_nPaUQQEyvOwE81x67XgVrrfuqDGasGxMMKYWlkeL5vrwGsxSa1Y8ewnA1KVQUtzNwtMSTHQKUkImaG3xubGAWRstwQvlAdg9szgxn_MYmoc8SB7ZjdF6EnzpPAgFXTfGYo4TEZOe2GLaYIecDrutjaW5yFr-kwKI0I3oXGaAEw-G3kUHHAB5f148SSJe6fJYBjXjhC3JKAYDt6BDw-0XqzEAKV7x_UbzYFutbXxSmcZsNgIH6I62r4okAoamZY1sBwKLvP8DmJdUM0YgOzCJuoN6rUXD551hlPSnP0RJi71K0THRejZWc-2nkSamvt9uuFPtFwAXHSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ارسال تجهیزات و محموله‌های نظامی جدید برای اسرائیل ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/680976" target="_blank">📅 23:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxA5P0iKzd5tZ3GGhVO-VeCJjeA5ouLdnXLBdhjizLsO4RyNCooVW7V14PQkP-tiOocM52-pNawxuOREE2FOEY2h6E3shQF73LZbDeMCqLmJGXJvRpfMPBtMDfda6Aa_FQTigt2uTJ2Jh9sZcxFuf6NLMgBusgqO5GJM-HYqUAxtInobhNp26sfqIVuWP7HCcoLj9b3fEi0-_mS1fZ4SAi8rljnLtunOXJKqmNtn6J85T1dB8btBVOBOOjNSbU3y5IdE1-edhzMdyarOzmEXCxh8CS_HtWcamHLBTYhl1TyGGLaCtHTMmeLTEIYzBk-VAJiBnKJdY_tl8nbNyoYOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل از بازسازی سریع صنایع دفاعی ایران غافلگیر است
🔹
جروزالم پست به نقل از مقام‌هایی از ارتش و موساد اسرائیل گزارش داده که سرعت بازسازی صنایع دفاعی ایران پس از جنگ مشترک اسرائیل و آمریکا علیه ایران، اسرائیل را غافلگیر کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/680974" target="_blank">📅 23:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atcokEY9hYkSri80a9FEJxYAe5Ef7R_GJJnLuUn6jUYRNJDxxAvZUl4hMkoZtgqEJFJEuEy8_uaMjYIGrqivxhUV-oBmltABfdpQ7ibvz_MaOwALRfUYs2x6EZqw30jKW2itw4dttdB10Dv_gxXPoKhKMQz_rk1w35oWn8TdRGS-3zKMPpkw-AEjRrYnLadgr229cKuYDOK-2246mcf50mKCmZw-LmkEkk6gBFmKvWRYRJvtiayta2NYlG2-BKdYu7AxKflA5e5v0_LuLgt_8MdBKGj2JiEPNWoB13fsYKobUZKvMO8ZY0zyq2d8a273N355gbN7uiQ2d2FSiWNQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23aff7a7df.mp4?token=ORDl9Spkwqc-tFT7Y4_5vgAykfuGujBGzEFIDVKwi8JZn_WtZ7RjXO3P_uDQCJF6LlRBiSe1S4rKLHxuz1-gkZFYvfrdyGIHKRDUCaDU2VqKrW1OcNLSlpBkVHmBihl231UhzA0QE0o7YsjKEfusE96Hk7q8Uz6ebCVU5UZ6-1uemQphIJWi9chDqE9ao5PLOeQbuienVYlvSNL-x6NpBbMlIoWr9-f-KHX313rk764zY9oFlAiI_g4OYsdnnJG4x7qVzzZrvQ-p41eBEo89y3ijiv7nz1QNHGJ8CWpOmVLpz4kdJywT1flWlgzZ5ucgKPGfyJrl0BwaY3nmD02QQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23aff7a7df.mp4?token=ORDl9Spkwqc-tFT7Y4_5vgAykfuGujBGzEFIDVKwi8JZn_WtZ7RjXO3P_uDQCJF6LlRBiSe1S4rKLHxuz1-gkZFYvfrdyGIHKRDUCaDU2VqKrW1OcNLSlpBkVHmBihl231UhzA0QE0o7YsjKEfusE96Hk7q8Uz6ebCVU5UZ6-1uemQphIJWi9chDqE9ao5PLOeQbuienVYlvSNL-x6NpBbMlIoWr9-f-KHX313rk764zY9oFlAiI_g4OYsdnnJG4x7qVzzZrvQ-p41eBEo89y3ijiv7nz1QNHGJ8CWpOmVLpz4kdJywT1flWlgzZ5ucgKPGfyJrl0BwaY3nmD02QQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌رسانی که با سرعت کبوتر نامه‌بر کار می‌کند؛ پیام‌ها در راه گم می‌شوند
🔹
یه مسنجر به سبک کبوتر نامه‌بر امده که فاصله شخص و دوستش رو حساب می‌کنه و هر پیامی که به هم می‌دهند، دقیقاً به اندازه سرعت پرواز یه کبوتر طول می‌کشه تا به دستش برسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680972" target="_blank">📅 23:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb02fc38ef.mp4?token=LTv1CXJy9FOoFpcgrobAREE_lKPTUk8KWQ9-wjnO4UJZhfgk48UXM2fuO8xcWcJKY_xIraBXZ3NgtQt_rDAcaTJmya2wg8xZIaMv1fFKwUzVKWqcBpIyoBwtXLjLACynoJEMAILE9vK2kRhtBbYH5BF0iGLf3bb9ufpdkCacUDcZki3xO8PEcug4hW4wSL1vwWqkc77uP-nBWI1ieowZLRdYVeZWshkFMdsvRkpsFOqzzju77wJwEPMtrcN9c025UJAfjyw3hQOUE3ZaEzBRSuGFThs85Ar3o07aU8nc0ELOLuobV5hIDW0XXyEaO1QmwJaH8JqKZ9Wg_Y2tV6eBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb02fc38ef.mp4?token=LTv1CXJy9FOoFpcgrobAREE_lKPTUk8KWQ9-wjnO4UJZhfgk48UXM2fuO8xcWcJKY_xIraBXZ3NgtQt_rDAcaTJmya2wg8xZIaMv1fFKwUzVKWqcBpIyoBwtXLjLACynoJEMAILE9vK2kRhtBbYH5BF0iGLf3bb9ufpdkCacUDcZki3xO8PEcug4hW4wSL1vwWqkc77uP-nBWI1ieowZLRdYVeZWshkFMdsvRkpsFOqzzju77wJwEPMtrcN9c025UJAfjyw3hQOUE3ZaEzBRSuGFThs85Ar3o07aU8nc0ELOLuobV5hIDW0XXyEaO1QmwJaH8JqKZ9Wg_Y2tV6eBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/680971" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFzKgR68L7UCIQ06CvAEB5DqmdHIwDVA9OFGHV3u3-R4OKY6Jph5lt9gMAhJSNqbqDz794i1sORGc2T1y2hd9MPZ_pvHrVw7MS4bGcnJ6ko_IkTA28uy0T0Q2d7EzdK9adxTDjL1SrXVRKGJ-6hrzXnGZ-dEy7WxWA5hgE_w3IDjgKgj2qpckE_8fDPoD97HLoLQXB2nsnujJSn0MgDNFQxo_zyUJemehzgvJy3Nm_R2CLW7CPJ6hMF1J4U6OlgSkcjSZKrzvtYa-mO0LBADoF4G2NoMMiwBbGHDfDNBMdACvGlZD2KA7745SV6ZALtFMeKQ2vgcGmq_WaSdG2eR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrfVxCSYI2V_Q9t6XKME1F2u7ViSCvAYotomiedTRupUr4YrDmXCqUMOrwm8ju8uXqlLhKaidP7jwzCPLzH20yegP7b46r4fkXiJmWU0KN8VLRJIUlkTbbnwoNyoSZQd61ux07xZf1s8PbJGE54Ad46yJJrQ0uCIxi7gaAoE94VRrWw6KnEDxt3se085v2WBddlvZD8sYhAQFIryVJ9kBHjTATnPZqbBMyitwvJLk6l8D8AmqmmkFCY80B6hc1jyPiOHUDtPHTrpyD9wSWgKzyx0Vjft736hICohzC0gWinRjkM8BW9HYXXFbsiPo71jy3EItWEVRb5KUTbJL_cC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzmkWSTbpTuvNPzDvAiI1tXRZ5Nn1oKoAox8BPCeNCVInfNBXfc2VUeEqwS54NxzVu3667NCqhCZ3_agCFxaGyycl-xqAoah_7UryEj_97CqkIJRDbX5fQQ_J1zRFjxI1xldnWers4XbjTEwDenR6Qj5qxpjaN4A15W7LP1r8tSYaKV4zQ7C8kAZkmki3vTFB6Xmozptbn-qbC_Ecsmi5_AHO0G7E_LzF6SJlYCkjsi-ZyG7FMwciFh6ZZNmgHvqFmokfyyObRBxyzAEhpPtnUX2H9pm06SKnwAaaL8dukPj3wjs6r9m3JmaBWV34u99lpsA4_ebCPFmPNOfw3xk_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت کریستیانو رونالدو به تمرینات النصر عربستان با موهای نارنجی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680968" target="_blank">📅 23:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65ed2a7e1.mp4?token=vzRdfuvaGWi4pGj-GAYOZdPceeWCRegMWqTLsuxgRB9HOa0LpPtamVbYwCLnoYoAIoxjjtld6iGOQ3JztFgV0cPqce0_S9DGvGeZBPJQrcW_j8FrQWQu1qB1d04cTOQC8mVXSUqeuGBP2ReDES4falY3qOovU_r60Xmy1IAYbo3FG46GCy5If-LGHdhFMxSNE7IQbAMo9ZEIiEdDEhNrRmRmHvXQFdc9jq8SymBfkSP8S8_a2Kib21S8JfHN-M8h8sSAd7TpE7l56kmHtD2Uj-C5jr06-6pZUYyKzZNDglhECqJh_eS_OBwtrHDeNpWrMo1IzG0AAx6jjlF1f5s4xStQpA8PQnfYlKFZLskZdner2Mnlua5rLgxEqSFJNe_fby64LTV3-I7HKbOJQ9YYibnxTL73dueovDmU6Tiahohvtu2xmEhXELfP1nhlto14JvL-GdujupSlu7ymYxMPksXn71XyFyMUtLLTHhPV-Va3Zj4m5gWEjqoJvWDMz4kO55K42gkwbcrUQnjww2CkLFlZCf2z-bp6rudZFsxefAIeyenEBUIwiy902nCtiZRSrovB5Fi2QqrM91Adhdw5HAM-kaqeCJ2n4-dRrBdqZzDoStHxuWhG5j_KkRtp4s8rhjMDZ-93jmGciuy3_qe3ZgmmvZvarpHK1eV1OuldljY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65ed2a7e1.mp4?token=vzRdfuvaGWi4pGj-GAYOZdPceeWCRegMWqTLsuxgRB9HOa0LpPtamVbYwCLnoYoAIoxjjtld6iGOQ3JztFgV0cPqce0_S9DGvGeZBPJQrcW_j8FrQWQu1qB1d04cTOQC8mVXSUqeuGBP2ReDES4falY3qOovU_r60Xmy1IAYbo3FG46GCy5If-LGHdhFMxSNE7IQbAMo9ZEIiEdDEhNrRmRmHvXQFdc9jq8SymBfkSP8S8_a2Kib21S8JfHN-M8h8sSAd7TpE7l56kmHtD2Uj-C5jr06-6pZUYyKzZNDglhECqJh_eS_OBwtrHDeNpWrMo1IzG0AAx6jjlF1f5s4xStQpA8PQnfYlKFZLskZdner2Mnlua5rLgxEqSFJNe_fby64LTV3-I7HKbOJQ9YYibnxTL73dueovDmU6Tiahohvtu2xmEhXELfP1nhlto14JvL-GdujupSlu7ymYxMPksXn71XyFyMUtLLTHhPV-Va3Zj4m5gWEjqoJvWDMz4kO55K42gkwbcrUQnjww2CkLFlZCf2z-bp6rudZFsxefAIeyenEBUIwiy902nCtiZRSrovB5Fi2QqrM91Adhdw5HAM-kaqeCJ2n4-dRrBdqZzDoStHxuWhG5j_KkRtp4s8rhjMDZ-93jmGciuy3_qe3ZgmmvZvarpHK1eV1OuldljY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
فرناز، بعد از دست دادن پدر و مادرش، حالا تکیه‌گاه خواهر و برادرهای کوچک‌ترش شده؛ در حالی که خودش هنوز برای ساختن آینده‌اش به حمایت نیاز دارد.
🌿
در ادامه پویش هفته گذشته، این هفته نیز برای
تأمین مواد غذایی خانواده‌های تحت حمایت مهرآفرین
همراه شویم
❤️
.
🏦
شماره کارت:
💳
6037991199529904
💳
5894637000012820
💳
6037991199500038
🔖
شماره شبا:
IR710170000000216780692009
📞
*780*35260#
📌
اگر مایلید کمک شما فقط برای
فرناز و خانواده‌اش
هزینه شود، در واتساپ یا تلگرام به شماره زیر پیام دهید:
📲
+989101785282
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/680967" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
پاسخ محکم سپاه به ادعاهای واشنگتن؛ دریادار عظمایی: واقعیت در میدان است نه در اظهارات مقامات آمریکا
👇
khabarfoori.com/fa/tiny/news-3237494
🔹
فرودگاه کره‌جنوبی؛ برنده غیرمنتظره جنگ علیه ایران
👇
khabarfoori.com/fa/tiny/news-3237470
🔹
از «شام لوبیای» معصومه ابتکار تا «عروسی در باغ الهیه»/ روایتی افشاگرانه از عباس عبدی
👇
khabarfoori.com/fa/tiny/news-3237489
🔹
نوشته‌ روی موشک ایرانی خطاب به اعراب/ عکس
👇
khabarfoori.com/fa/tiny/news-3237446
🔹
سناریو دولت برای بنزین چیست؛ با قیمت نجومی مواجه خواهیم شد؟
👇
khabarfoori.com/fa/tiny/news-3237426
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680966" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b408def775.mp4?token=uw2nz0R5WjL6pFpnG4tkv3F4ACTXQz_GlXt0fyYqVKwwzxg6HnaMaPWm3PpVas-wYBQ4A1NFqBJD2zkE6f_Jy-ueD33eWuUJ2m3nW571v7SGMNA6lhjwEX2gIHhO_jeCvJiikmwQcfTLZWjvoUJ2glDVw6RHUkntzMUIymUy7TaXhOBTvI366Cfirml6xF5xgM8EzH8wL1BfcqYQ-1fwVIo0YKk2XaGBg9cXq2V_RkWdq8Z3FS8Wm3VHCuV45JnxyExKk3Zj_-g6tGJMktR-aEr41rq6eJzHhepOD7GVGWL4aFf_umksypODLGIiOrPx1Qn1hqPd2HSuFo8uyvHW6of7MsGNUXQikq19whMpKYugAvxYmm0F4CxOkFEGIgEm6JNXlfppi9TQ4N4UdqVhBPOqOmh9YaPqFAl_lFAc8a31vAgFGSI_4X2IjMPPCSIvaaEa4HTNuQzoYcCiizSwzSmZce3_Y6-KSBpru4dEMUUuWODgafylYLEUzMTrFBsNvPduSxEqNQr8FCHBOtriApsmffsP0W_PkC6-K-2osq5-TL8fSBvJaoS3MLzYl3jdKaGL3eGkk3fn5WX2FiaEuDTIdfct-kXUjAda9hysN0FbZf89WVVNSkesb_M_HclTMi03J0-77S1q4_Y8IRDFY5Bimc2PB9UzV0FllOlrzlU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b408def775.mp4?token=uw2nz0R5WjL6pFpnG4tkv3F4ACTXQz_GlXt0fyYqVKwwzxg6HnaMaPWm3PpVas-wYBQ4A1NFqBJD2zkE6f_Jy-ueD33eWuUJ2m3nW571v7SGMNA6lhjwEX2gIHhO_jeCvJiikmwQcfTLZWjvoUJ2glDVw6RHUkntzMUIymUy7TaXhOBTvI366Cfirml6xF5xgM8EzH8wL1BfcqYQ-1fwVIo0YKk2XaGBg9cXq2V_RkWdq8Z3FS8Wm3VHCuV45JnxyExKk3Zj_-g6tGJMktR-aEr41rq6eJzHhepOD7GVGWL4aFf_umksypODLGIiOrPx1Qn1hqPd2HSuFo8uyvHW6of7MsGNUXQikq19whMpKYugAvxYmm0F4CxOkFEGIgEm6JNXlfppi9TQ4N4UdqVhBPOqOmh9YaPqFAl_lFAc8a31vAgFGSI_4X2IjMPPCSIvaaEa4HTNuQzoYcCiizSwzSmZce3_Y6-KSBpru4dEMUUuWODgafylYLEUzMTrFBsNvPduSxEqNQr8FCHBOtriApsmffsP0W_PkC6-K-2osq5-TL8fSBvJaoS3MLzYl3jdKaGL3eGkk3fn5WX2FiaEuDTIdfct-kXUjAda9hysN0FbZf89WVVNSkesb_M_HclTMi03J0-77S1q4_Y8IRDFY5Bimc2PB9UzV0FllOlrzlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دولت برای بنزین چه برنامه‌ای دارد؟
🔹
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🔹
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با قیمت آزاد فروخته شود؛ درست همان چیزی که قرار بود در کرمان اجرا شود.
🔹
روش سوم: از ۱۲۱ میلیون‌لیتر، ۳۰ میلیون به حمل‌ونقل عمومی تخصیص داده شود و ۹۱ میلیون لیتر باقی‌مانده به‌جای خودروها به همهٔ مردم اختصاص داده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680963" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDU2Ns32Rvv-sZ0tf39UooGL_2HUodxcF0N3Pf9-_Q6x_rx16XM1tUIBniKQHoLoYp1N97KQ85etYcY-8DHV8drkzWo78RWomwDFDFZWgsP0GLc-Yo1VZ8BJWxa9k7XIerfYyHRWVQBYimOhBZhMwyJlJ-dPP_UmdN_G7wVKQr_oq4NqvbIt42nlGCvhSYf2ksBWk3iV2lC-gqKhvcXQPcgBl5hRLUNKOasvJc2YOO9y5yZTaa_fQyX8kVLxxkQgor4vGXUEIiF20aJvmnxNrTnTmHNZ-nZ2jnfv9jvjBMKW3Gw2dJaDm-aApRNp8wKM8YMYcOkqDAQssPZhh4o0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوتبالیستی که در زمین فوتبال مُرد، در سردخانه زنده شد!
🔹
یک اتفاق کم‌سابقه و حیرت‌انگیز در فوتبال نیجریه، نام چینیدو اوزور، مدافع تیم کاتسینا یونایتد، را به صدر خبرهای ورزشی این کشور برده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237312</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/680962" target="_blank">📅 23:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680956">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
فرمانده واحد سنتکام ارتش تروریستی آمریکا: هدف قرار دادن زیرساخت‌ها در ایران قواعد بازی را تغییر می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/680956" target="_blank">📅 22:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsYw3mqUaIRnJZeszDUSPVM30J39hh15m1-9fEJmhd-rkBCqcqy2uIhD303MRG3LDw-TQuZlLWDJirah3QWOfemsWurVdqM7jTMSmw_76IJ0_smUuGczEX1Eh80yZ4uRNtIPGfJFUdfeHjkxwSpXO2B-PaBOV3YxqmYxh2yIBWqIaMNUKC6JiZNcM1WvhlV3CJKN0zbqNTgUztkaW3lqyBfioA1uVtTAsq3w-WhlldlOkUwtu9a0QOH_CoYkK7R98WL71N71sDsLnsGNByeaWsbHSDmY4EkuLc6C95MkzzMbhHXSCoD-6K6-A7tGgIWE_qz2NS39cYygmS1QU2kIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/680955" target="_blank">📅 22:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دریادار علی عظمایی: واقعیت در میدان است نه در اظهارات مقامات آمریکا
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
تنگه هرمز بسته است. تسلط ما بر تحرکات کامل و قاطع است. هیچ تحرکی در این تنگه از چشم رزمندگان نیروی دریایی سپاه دور نمی ماند.
🔹
واقعیت را باید در میدان دید نه در اطلاعیه ها و اظهارات مقامات امریکا.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/680952" target="_blank">📅 22:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC3zTSMy2cYA4U1S019MoOVkDn7Fw_KXp7eYPFjEDHicK-Upw_DKj1Ml0Bvyyc4EH7--3c9g2QuLsHA8eYiO4LyxH-8BUmrakHqZ8ayMkq3AH8NmzNeWdysjDBDrvxb2Z5DLGjqiipd14S3Y2BArIfaYjKCpAz0dLyln6ZEqsffZn_iWl1zVSjx-63vMmVCnu85qRbmhZ2qtDcW8DCOwlpxoTqsVIIqG9zMJRlrd02Cr5rDRY9APalaLuXEXdE85nnWXaZ-Nc2YEZ4lwt6nPewSkp8escN3hnQErj9E0hk2p1EAVhjpoPgP677IZCNkGWQ5VtNklis5n5Ml7RChOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: هرگونه بی‌ثباتی منطقه‌ای ناشی از اتکا به نفوذ خارجی با واکنش قاطع ایران روبه‌رو خواهد شد
🔹
تا زمانی که شما در برابر دشمنان اسلام تسلیم می‌شوید، حاکمیت شما در معرض خطر خواهد بود و جایگاه ملی شما تضعیف خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/680951" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fed294f.mp4?token=ayaRfa5ZLPVNvQAnoBZXRzZU-NtUHGlPrvjpfDVaQAVdx_i85lAGzXYsGMfJCHMkB2gIo1IbxQPRxa5qXKH7mUIMzmoj65LC27GcXNQMs1_uPhKqaoUtFqNCzQ4LLBxkMkTYPFfH-hGMj4R7NQy9Gun3f8jFu3QFD4JgzC3OkXrXOZ_wMebxskN1XIaKwisj2U7mq2d9i9U8umC-bBPfliTZ4KVp1plVC1Jc0EOdp2BVYL4lienF5H5waEo4O67WAphhMunoaZjJ1SHAdOAAmBh6uuyNgZRJWK38qCrY89zzQa1PtC4xu_WDVybTNQZ9ZvPM7Pd7VNHd9jAc_C0gXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fed294f.mp4?token=ayaRfa5ZLPVNvQAnoBZXRzZU-NtUHGlPrvjpfDVaQAVdx_i85lAGzXYsGMfJCHMkB2gIo1IbxQPRxa5qXKH7mUIMzmoj65LC27GcXNQMs1_uPhKqaoUtFqNCzQ4LLBxkMkTYPFfH-hGMj4R7NQy9Gun3f8jFu3QFD4JgzC3OkXrXOZ_wMebxskN1XIaKwisj2U7mq2d9i9U8umC-bBPfliTZ4KVp1plVC1Jc0EOdp2BVYL4lienF5H5waEo4O67WAphhMunoaZjJ1SHAdOAAmBh6uuyNgZRJWK38qCrY89zzQa1PtC4xu_WDVybTNQZ9ZvPM7Pd7VNHd9jAc_C0gXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیین شام غریبان شهادت امام رضا(ع) در حرم رضوی برگزار شد
🔹
آیین شام غریبان شهادت امام رضا(ع) با حضور اقشار مختلف مردم، زائران، مجاوران و خدام حرم مطهر رضوی پنجشنبه شب در صحن و سرای این بارگاه نورانی برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/680950" target="_blank">📅 22:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=pd0uUSnXAa-KC5JTb6w_sY3tsUiSPMEgCzQ5Vvzjski5QrC_9aJag-81fDgNEB6PVDYu2mGcQdtKKOu_M7aMIUGz0d-k3Uabi88oOyx33t8zNfOJbQDZHO0tlKODsP_uoPpyulAgjoRJk49Dh-7srkiItMbqWh5xRKCrsGQqMJCruY1amSo1rGbywoTerBlSORg-yuhJWRKO2RsAk0FpRG8hB_ml7j3F2wsrz-yLgxL9BpK39sBHGGs0Bwm8vbnfmCcjPJuF_vQAGYKsDQ4kxFbExKtKMaMyYqFc4HfTMzTtjD-S8gGa3Me_jrucXJyQHD-HQqVTyPLIyhTQ95BoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=pd0uUSnXAa-KC5JTb6w_sY3tsUiSPMEgCzQ5Vvzjski5QrC_9aJag-81fDgNEB6PVDYu2mGcQdtKKOu_M7aMIUGz0d-k3Uabi88oOyx33t8zNfOJbQDZHO0tlKODsP_uoPpyulAgjoRJk49Dh-7srkiItMbqWh5xRKCrsGQqMJCruY1amSo1rGbywoTerBlSORg-yuhJWRKO2RsAk0FpRG8hB_ml7j3F2wsrz-yLgxL9BpK39sBHGGs0Bwm8vbnfmCcjPJuF_vQAGYKsDQ4kxFbExKtKMaMyYqFc4HfTMzTtjD-S8gGa3Me_jrucXJyQHD-HQqVTyPLIyhTQ95BoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است
🔹
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، چند هفته قبل از اجرا آن را به مردم توضیح می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/680949" target="_blank">📅 22:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شوک یک تجربه مشترک؛ عبور مادر و پسر از رودخانه‌ای میان مرگ و زندگی
🔹
00:15:30 وجود جهانی زنده در هر دایره از ذرات آب
🔹
00:20:00 اهمیت خواندن نماز و منع شدن از سبک شمردن آن
🔹
00:40:00 تجربه نزدیک به مرگ مشترک مادر و فرزند در عبور از رودخانه‌ای طغیان‌گر و گل‌آلود
🔹
00:50:00 رؤیت مرگ خانم بیمار دقایقی زودتر از وقوع آن
🔹
01:07:10 رفتن به جایگاه خودکشی‌ کنندگان بخاطر کشیدن سیگار در دنیا
🔹
01:10:10 شادمانی و غرور شیطان، بزرگ‌ترین رنج و عذاب گناهانم بود
🔹
01:15:00 غیرت‌ورزی برای اهل‌بیت(ع) در دنیا، کلید شفاعت‌ام در جهنم شد
🔹
قسمت بیست‌ونهم (فراز و فرود (۲))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/680948" target="_blank">📅 22:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=tIu6nghavSeozDJpn9jZb9Y0Bm3P71uFvQ_qhFQJMiRkL9jhTpqJQX1Ez_vmnjvU0mV1lpqB7qBkWcx_JKuxPOW_WtPUaLF-nfIImWzJITw7LtiCVIY7ZRG04AmXvw6RxI4pi62l90qnw1SqYuMcGrzKE-5qNHqTedAhrULPlXc07Wm_90z9fSlnKuabZepmYK-17I-_hpdOzMscHopOd5-a3MEJrcN0veNOs1UFNZDdQumHxlFTdTV6LypEACl6eJTLg7mtV2Hjmzv68IuWa4fQFk3yG6M9QdyCn_9Ur5pZzpHCmYMlCKqStwXtGI5p-r9FJK6OwhNHqs53zgDhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=tIu6nghavSeozDJpn9jZb9Y0Bm3P71uFvQ_qhFQJMiRkL9jhTpqJQX1Ez_vmnjvU0mV1lpqB7qBkWcx_JKuxPOW_WtPUaLF-nfIImWzJITw7LtiCVIY7ZRG04AmXvw6RxI4pi62l90qnw1SqYuMcGrzKE-5qNHqTedAhrULPlXc07Wm_90z9fSlnKuabZepmYK-17I-_hpdOzMscHopOd5-a3MEJrcN0veNOs1UFNZDdQumHxlFTdTV6LypEACl6eJTLg7mtV2Hjmzv68IuWa4fQFk3yG6M9QdyCn_9Ur5pZzpHCmYMlCKqStwXtGI5p-r9FJK6OwhNHqs53zgDhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: تا الان هیچ تصمیمی در دولت برای تغییر نرخ بنزین و سازوکار تخصیص فعلی بنزین گرفته نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/680947" target="_blank">📅 22:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آی۲۴ نیوز: ترامپ و نتانیاهو از زمان دیدار در واشنگتن که به دو هفته قبل بازمی‌گردد، با یکدیگر صحبت نکرده‌اند
🔹
این قطع ارتباط در شرایطی رخ می‌دهد که ترامپ همچنان در حال بررسی گزینه‌های خود درباره ایران است
🔹
در عوض نتانیاهو تماس‌های مکرری با جرد کوشنر، داماد ترامپ داشته/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/680946" target="_blank">📅 22:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdbecbe41.mp4?token=ChzhLTPsCt-RkYVGEk97fR78_O3oS2YAB-2cU_l7JaBruZ9XyitLhsqxp5vHw_Mci-8rJjafGH3Y4lVW6IcqdcLdb4mg9Qzi3FxSfYk-vIryYx30FHyiYi7dn8xVqWLptHAH9sXGGhNvCGt_Pns_afcNF_hmq3zD_vQQ9qy3QnozphgKdjiYfVfwwVthMchINavQrsKob9nKQIpqMm82DSPdddVXvJxcgLfqQRRKjh_IJ8SPpFateUilJkPe5uCmKVJIy9zQFb_clVu-FVOv4K4ovWJ9zK--jjoyO-aVrDjD9csE_tl1wlcYNayH828VKcD5zghDaQfFUbhCp00FEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdbecbe41.mp4?token=ChzhLTPsCt-RkYVGEk97fR78_O3oS2YAB-2cU_l7JaBruZ9XyitLhsqxp5vHw_Mci-8rJjafGH3Y4lVW6IcqdcLdb4mg9Qzi3FxSfYk-vIryYx30FHyiYi7dn8xVqWLptHAH9sXGGhNvCGt_Pns_afcNF_hmq3zD_vQQ9qy3QnozphgKdjiYfVfwwVthMchINavQrsKob9nKQIpqMm82DSPdddVXvJxcgLfqQRRKjh_IJ8SPpFateUilJkPe5uCmKVJIy9zQFb_clVu-FVOv4K4ovWJ9zK--jjoyO-aVrDjD9csE_tl1wlcYNayH828VKcD5zghDaQfFUbhCp00FEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی:  اجرای تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد
🔹
رئیس‌جمهور تأکید کرد از اقداماتی که مردم را غافلگیر می‌کند پرهیز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/680944" target="_blank">📅 22:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbxsfON0MW8UfK8lDTKnVW_38_XBgVdUPsqOYpMKwUMv_seOk89fv49DAYniSnartFKDZ_CBtzLbx8hmIox9wubdOQ0sx-pqEpWY4X-4721fQvDkweExjqiPqGp2GoKLPZMpv7nUiXXrrigBTcIUj5KeazQ_-RcZ3GI2_62hAE8ZyGG5qRwPVUElJuXgP5YRagHZU6e-9qFU60AG8lQQTG48LExAvlyxSLJ_LpyTQd_XnaApHIrfYmv7SG1eRJfmzuu5WlVf-LdngAHcKehb0ZiIpE3HGP6-uVoH-B_XCEdEbPfe2OHlPTzbQuJSKjO3BysNWxQl2klVkJIfdXa22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردا جمعه ۲۳ مرداد نخستین روز ماه ربیع‌الاول ۱۴۴۸ ﻫ‌‌.ق خواهد بود
🔹
گزارش استهلال ماه ربیع‌الاول ۱۴۴۸ ﻫ‌.ق از سوی ستاد استهلال دفتر مقام معظم رهبری منتشر شد؛ بر این اساس ماه صفر ۲۹ روزه بوده و آغاز ماه ربیع‌الاول ۱۴۴۸ روز جمعه ۲۳ مردادماه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/680943" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رسانه رژیم صهیونیستی مدعی خنثی سازی طرح ترور وزیر جنگ اسرائیل شد
🔹
شبکه ۱۴ تلویزیون رژیم صهیونیستی در گزارشی مدعی شد که یگان نیروهای ویژه ارتش رژیم اسرائیل موسوم به الیمام با متلاشی کردن یک تیم مسلح در جنین، طرح ترور «یسرائیل کاتس» وزیر جنگ این رژیم را خنثی کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/680942" target="_blank">📅 22:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
آیت‌الله سیستانی شنبه را نخستین روز ربیع الاول اعلام کرد
🔹
دفتر حضرت آیت‌الله سیستانی در نجف اشرف اعلام کرد فردا، جمعه، پایان ماه صفر است و روز شنبه ۲۴ مرداد ۱۴۰۵ نخستین روز ماه ربیع‌الاول سال ۱۴۴۸ هجری قمری می‌باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/680941" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سقوط ملوان آمریکایی از ناو «آبراهام لینکلن» در دریای آزاد
🔹
شبکه CBS گزارش داد یکی از ملوانان بال‌هوایی ناو هواپیمابر آمریکایی «یو‌اس‌اس لینکلن» اوایل ماه اوت در دریا سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/680938" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e3638fee.mp4?token=bopA37R-geL_mpDeuBXWNKPw2gPiLIKlhDYrRCJh6cI8CW6oCzylz2rZKR_rLxEae3_avU-xcXZeCgWJ0GYK_Ndxqt32U-Ph8vD7OOhLWAfYUFLFmoZY_fCYinXuvy9QHYPz_1DHEwhSiHGPeseMlaEvdmlJmyZ1dpJNJKniyNyBKe3h9NwKqNJPiWQ5HjA5yhQBBObcfCgufV-FVPRlG8Ba46sk2AQ1qNZ7HSYG0QhSJypV3Odc_kdCNO-E76Zb_0e2RvM0CXLyBDucl8SlmFSjwTBIfwkVrcUD1d_THfYeJFAE2kVd9ximprElunMG-xlgtQUCw4oFYCbSm2gC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e3638fee.mp4?token=bopA37R-geL_mpDeuBXWNKPw2gPiLIKlhDYrRCJh6cI8CW6oCzylz2rZKR_rLxEae3_avU-xcXZeCgWJ0GYK_Ndxqt32U-Ph8vD7OOhLWAfYUFLFmoZY_fCYinXuvy9QHYPz_1DHEwhSiHGPeseMlaEvdmlJmyZ1dpJNJKniyNyBKe3h9NwKqNJPiWQ5HjA5yhQBBObcfCgufV-FVPRlG8Ba46sk2AQ1qNZ7HSYG0QhSJypV3Odc_kdCNO-E76Zb_0e2RvM0CXLyBDucl8SlmFSjwTBIfwkVrcUD1d_THfYeJFAE2kVd9ximprElunMG-xlgtQUCw4oFYCbSm2gC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب کامل یک انبار در بندر المخا در حملات انصارالله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/680937" target="_blank">📅 21:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmP6Pa5fpaqNCxqZKKOKpkeCyVOImLFANDfqnItoW9PzibonajfPgQJDclvwhgz7KpURINoXAG1wlzbzOhLhJrZ2bmMntXLlzWjdDjQDpF2ZhmS1mbCN8BVO0vSv4btSIg5mrO0zOIW8xnC9neEPWXXulF-sQC9x_bi9fmfAQm9TSGvs9QCTWReZBmsgH3ab6C3RbxUhDW5W0-jmnfac0OpVhyBsYwW3enJM1lihmTd8GQc9YUJzSduDIpfLthoy5OUh3JHloNpP0S4kF6cJeSf8IocSONS_ug4s-8zNDj-SM8OvbbHvOoJcf1bGXbCHsPmNf1YDgD_ois3zWzmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس جالبی از شالیزارها که شکل خاصی را به خودش گرفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/680936" target="_blank">📅 21:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
برای نخستین بار در تاریخ، دختران وزنه‌برداری ایران نایب قهرمان آسیا شدند و پسران نیز عنوان نایب قهرمانی قاره کهن را کسب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/680935" target="_blank">📅 21:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خروج قطار از ریل در انگلیس
🔹
یک قطار مسافربری در حومه شهر «لویز» انگلیس از ریل خارج و واژگون شد که این حادثه منجر به حبس شدن ده‌ها مسافر در داخل قطار شده است.
🔹
در این حادثه دست‌کم ۴۰ مسافر در میان آهن‌پاره‌های واگن‌های واژگون‌شده گرفتار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/680934" target="_blank">📅 21:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
منابع عربی: نیروهای مسلح یمن با دو فروند موشک بالستیک، یک مرکز حیاتی در الحاریکیه در نزدیکی باب المندب را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/680933" target="_blank">📅 21:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40103108a8.mp4?token=Lr3YtBaaYnH58AQYFPlo8SCcwmH4FcRPjyLPp0f-6rTL_mhqtEVIKi_4pe98J2iACX4m_D9EdfKZgcV96f0AObRhDZdB2cByR4MCUlPl9aMhcgrhb5jn5ddKXNnwkoE_OJxPmiRlPh6lu_1xnWXqALrtDz9st3ynAAVs6vNYhbG9TJI_hzQNlT7qlNZu_aLihFBobyTHwEfA2m85mqXqkoO_zQUzWTZEpBZlea3gDNaocO7i-4YlJFlqwoHWpGWwTyZ5Qp38LjezQ4oxWUZH2uSQ2mvDqRu6taJ3XbAu-_wcc8MCzabxcg3GBScCX6YyOY28OpgQFF7woab55b7Nfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40103108a8.mp4?token=Lr3YtBaaYnH58AQYFPlo8SCcwmH4FcRPjyLPp0f-6rTL_mhqtEVIKi_4pe98J2iACX4m_D9EdfKZgcV96f0AObRhDZdB2cByR4MCUlPl9aMhcgrhb5jn5ddKXNnwkoE_OJxPmiRlPh6lu_1xnWXqALrtDz9st3ynAAVs6vNYhbG9TJI_hzQNlT7qlNZu_aLihFBobyTHwEfA2m85mqXqkoO_zQUzWTZEpBZlea3gDNaocO7i-4YlJFlqwoHWpGWwTyZ5Qp38LjezQ4oxWUZH2uSQ2mvDqRu6taJ3XbAu-_wcc8MCzabxcg3GBScCX6YyOY28OpgQFF7woab55b7Nfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش فایننشال‌تایمز از حق قانونی ایران در تنگۀ هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680932" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1dcfc4caa.mp4?token=Oh6I33KofQ9SfwKOEbTldWmbfTUwutwYbjmIg4izwGOKfd8QoJyyUG1Wo9FTtQZV-2p7WSIyyRusIDIjaDTdapokLvE1hy6SiwjJqxf4PpuNTwni4RkC5_xSGP6f6MOv8SPwPDV4FYuCQkTSkKXQARdTuwfXYEzD9n1Npr9pgZvRFnZr94TE-8bNvdOJrkyqxGiQZG_0VzHvlPV7UPtkIpq1D1ubI3OiePXocYJX_0ie0z2xEmyzUMA1N6lJrsrrDe1quIBuwjrSjb44z8Zi2-sTe7k-VfW7YbwWUzDCzLc3wjaA1k1RRFvIbcvgM7GwGznz3C5PMbK8nSCj8EUfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1dcfc4caa.mp4?token=Oh6I33KofQ9SfwKOEbTldWmbfTUwutwYbjmIg4izwGOKfd8QoJyyUG1Wo9FTtQZV-2p7WSIyyRusIDIjaDTdapokLvE1hy6SiwjJqxf4PpuNTwni4RkC5_xSGP6f6MOv8SPwPDV4FYuCQkTSkKXQARdTuwfXYEzD9n1Npr9pgZvRFnZr94TE-8bNvdOJrkyqxGiQZG_0VzHvlPV7UPtkIpq1D1ubI3OiePXocYJX_0ie0z2xEmyzUMA1N6lJrsrrDe1quIBuwjrSjb44z8Zi2-sTe7k-VfW7YbwWUzDCzLc3wjaA1k1RRFvIbcvgM7GwGznz3C5PMbK8nSCj8EUfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشیدگرفتی از فضا به شکل عجیب دیده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/680931" target="_blank">📅 21:13 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
