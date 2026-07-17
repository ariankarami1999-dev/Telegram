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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 565K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 19:23:01</div>
<hr>

<div class="tg-post" id="msg-100643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
در سال 2020 جناب وینچیچ داور فینال جام‌جهانی توسط پلیس بوسنی و هرزگوین به اتهام قاچاق سلاح و مواد مخدر بازداشت میشه و پس از تحقیقات گسترده و یکسال ممنوع‌الکاری مشخص شد که این داور بی‌گناه بوده و تبرئه میشه. حالا پس از  ۶ سال این داور با انتخاب فیفا قراره مهمترین بازی عمرش رو سوت بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/Futball180TV/100643" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1kR6gdTMlxnVnYpoU3aLWN3_SlZ9Vblcw02ujVaNfTMrpXp-S9KvlPso8yApwE8UUD9sVOIZiBHFU66HQcNj09dYvaWQOehgjR45u3gXb7xChbaO6YNm6GW_el7bD9WwzjuR8xTMEd-gjaN2KuRwk33X4DJvnWhcKoQEBjXkEnw49k2l5NlhVOX-vc1E964vbY1FqjJ6MnP5g6Ob5JMpK2RIZizj4ae0jqvk05OdKaPUaLbqwo-BHuOtEBzkQB0qJP0a4hJimJIdy2d7BpNoo5YHxv9F8cVKkNlF8Lr6rCFrZ5iv8k71wU6BwerTofRV00eJdozEbqm9Gys9r5x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJ2vUtdGqlLg6hZfK2gvKjiPdatyuRL5yzxMRI_brSI8YI3whwP_-czFzn9DLFFHRt9emFBFNDZhbFPrKCz6Ay6VEb1T2Cr3ReqIIOPbmzlYwSoHJiNApDnUcRmL9I2eIOTZi7DF7BpmCcLQ5hD2Sv2PGrm8lZz33KMc0Mq0klXwKBZen0BLlBHpj0pNBOpP_z03w3AryceTbwQGxqVmZ0ffrTid5TseYCya5aedH4ESDe44DQm9GUIve8E8O0RsePV2embmUMgRXc_z0f_HHnBzvjqoqwzB95TFizoJWjwy9GNCt4aZzDLWVfDYyx3CM2o4gaTo8qOzisrZVlcwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ووزینیا: من معتقدم که در آینده لامینه یامال، مسیِ نسل بعدی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/100641" target="_blank">📅 19:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7ejRhSwAvqkjrluSonhS6xaFtAtvGIS_BnEd0gZ1pVDIDVF8iyDlhwV4zpS_wPs8cOHwDtil5GKwgn5Wz-YhehZhlJ2zdrZvBWDpXbXKmi2pZQhbqzhFjBhvJxExbmpN3AypAuc_P5kih5BJoAfghwJl3IVkMrG_g7FyFoaZdPyVxaMH186TPv07o9A5nwb2BhVd8rtia3IwiBGfC7OF6wbboGiGGOFXRUNMu2QXCcY-5DbNOeUb6gIlj3-NVnKcPmuiLxDA605hVUMnF7G41iyq2iup_rCkgvba6PwROe201sjloIpD8s_GyLWN6sDjp_HDUNVoJ-XoQqcdRcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌‌های‌ملی اسپانیا و آرژانتین در فینال جام‌جهانی با لباس اصلی خود بازی خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/100640" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2BMWhbhXp557qwaQfV7RPqcfjZ1-Hhs3e_MubC34AbIeneXsIZd6nkH8NITHJVxvINlQTd3kg_cNnkJ2ZlV_gLq1KGui6S68E0Q6y6tV-iGwkw3IrK8MhXJI8kHl3fV_N2FolihKsrFMibNfOS_71nvRL2C3Ty86rpzWKQgAPKtkB2WSQ3cJ1x_BNMYo_SjeFD-EDVludLNHlFyAKWuA1KH_Oo5eKckEJKnAVCvS6nHnrSMZfK7jyh7WyGQCRetmbTHSSgpz5BXacwoPW-q6ngG_KuymfUSDuCtdMy7ii2qPROWTsDjAWyFsL8zn4BOhnw4VA7TUKubeFXjAXb2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل Marc Cucurella رو سرچ کنید یه گربه با مدل موهای کوکوریا تو صفحه ظاهر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/100639" target="_blank">📅 18:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100638">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm2Ew1ZdA0zkO5WW34ShEXTrYgFv3WaUmMQR-DVBVw7SnAgqvexTgYzzlaVCceEdnkXnqZrQFNnoQ3v2q5eWAcqrUmmDIVceKV_AffdlgRdGc49i8UnjTxdZUQrx0NyBuTzG8CX8tvLJu2Z-IpHGabzR9gqBEAkUFvenUcx3MduRMbxbJy29IKWUCyNXfpU8Xdg9dOyDjAp4mwll3dufloxSqTugs2z4a3PtTWDV36LVtvavLYdUU4mjiyw3f4ZaTOIDfiPp_J-rwtW6EthEE_iizj_kj6emIKyab60JVPNrIhJK-J6ttbIqiTEUpFm6FlhxYEoAfzGtNhae1EapqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
• خبرگزاری فرانسه
🤩
:
🇪🇸
نخست‌وزیر اسپانیا، پدرو سانچز، که در جنگ اخیر بدلیل مواضع مخالف ترامپ اختلافاتی جدی با رئیس‌جمهور آمریکا، دونالد ترامپ دارد، در فینال جام جهانی 2026 بین اسپانیا و آرژانتین شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/100638" target="_blank">📅 18:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100637">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
❌
ورزشگاه آتالانتا هم به خاطرات پیوست و زمین چمن این استادیوم برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/100637" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100636">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
🇪🇸
تیزر دیدنی از بازی آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/100636" target="_blank">📅 18:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100635">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند پیروز قربانی خطاب به علیرضا جهانبخش: من چندین سال داخل باشگاه بزرگ استقلال بودم و نیازی به دیده شدن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100635" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cNLBk4rla9FMMzFPV1NpIPsIpqqIv7_NuDqcc3OQvesYAsjCqUR8TJJjZ5hhcPBCOWWElNFu9eE3235rAGmlNgHoTz0RNIrNAl3e3xyJbWErzgg-yzhD3rxUiEItovX-_9U59cg0BTKc5I0nqs9VPseo9WOMi_YuIAvXEUohKpWZo4Ffr0UQMAc9cuMPwBG1ubd8_PzT4BhyvFBIOxEVO0pXdWBMjtVa3Hoj155aYHgrK6JvfLyP-u_I0AzfZF2okdjyiIo9g2pRCLNHCAn1Q0Vokdqk7uWNah4GTSvEHCWuBx6Ks4Uy4ffxl4CVJprvYzY53osrVa3_pTyn4E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZlBJTHLvNMqZ60o_yous-NehCHxFMGfKaGXgKYxt_4RiKi515MsFRoN4jKtpGvdLtTlwC3kAyudv9h68u3iIQoO5qzc_IgDUbbXtpd1WTyb0KgX7QLCFVgBlAzh1X7UU1YdUaiDY7BuGO4luVvFtVBaQXF15ykycKptlZ8qZBVnAjq-Nh7fYPsE7NYs4NDA9H5hKjArtNuOF_RPRYXT1hEbPL5sqG8FKLbklD6I8bAr9ejByPBAJ8yqqADzla7PzjXxFlbKrf6bek-uupd-Yqwg41fRY7AerSuT90v4Io-zLEGCli-o_0tcqfA72GYDRtwuOTTtwu2ef53WMbBsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbCZPPPjRYbyQ00KX-9_kC1BaoyJWvcF3eKxmTXpJCFhHIPOUM5j0nKuYCF2ctJhyQUkrE6iobAUNRum6ndGC4KEjGKpRlTWUiQlCje7hNeuYxLRNmHDLWahvQoohrsJzGy_pp9gwIqUC4bgx67C4wb-DmaTwUjuc_Yx4xCA6OlgCj9wPvTIA_RMCLQr3OGlc_ciq89IJ1mYgFZjuW8GeFDxm_Mx6MSR4acGMB34pEiMQklsqvQRmJErkNuufbzOHmv_4BGOZ7o-20hSaf3IqNyLS7PJN3-9bH49CkpSxizeXjh4oo-nkGb4J_s78Hp5syrWwBeCevTBiV4epNC78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh0w6D6bBcnkWxPPop5S59BVBqv7aJJ5bJoyVcKeVOCaAYRg7feQmPUz0HFacayvQZiqKkUh4e4NAjjeqIW_BeYPn6GtNpt2L5UytQ6R0zJmDPobBGVf2cI_gEwNIhpaUwYaShYgUWZEP80aIEUsAEwOkTtPYPnMYU5QZ6TzYrOK6HwnAOGmj04UNgU__wJf9_rYppyH6-4KI-Szdsr47REGD7MadLsB7y6vMhnj5KbbRkihxLgwwU4-olp83AANfy9mSF0tm-FpQ-dp7zj3ndqj6b7hATO4OLIJPKnb-Ely0COVMAe17FmqHUO_KEby0GCVoBOrXtRDYv2Yv4MxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-hu-AgAKaqpGN6V4jOaGWnBgcEljykL7fxccrKp6VwGPO8RCmSDF9iJ6GrZAHbvUROg0J6BJnZlJQMDdmCUrNYxg_otgCyobXzyAmmBbOV2SyjW6BqsvcN6729j0lONnZNHW_HqCVE7x6LnJHkyHvEuu3cM_TVk9Gs1wbKSrnfRu-b5y9J2qEpAzOK5--0a21bcv6N2DRTDRkYImPg2G73he53gkCdyuDWHM2cmFO6of1I1QQrMpFHxLZbvBiXouaDFgGbN3Qwmxmvrc8waF89QuDyz4XfxD1P0aeZxmsNck2BLGIPuAwu27jhh-msje9Nkyw66KCUtAH8mTxt9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clev_jEt-rpOi_WsmJ6uDCZVOl2anTf7Hy_nUVigH-hW61IZX4X6sQlUujw6h9yVJplAbemACvLa481dgVN83bD17UoS0DjfxTo0j8KVhZlU-e0BEXonnWJhAIPUxROmmWAaSDy3dLTQGy7EdYhw_aAUaxweEykd2IAOItE4Qlt3pfImcAynieveIS6p_o0mMNDi4qEvN21hWwTuXDHhCbDCGFS8QFfhzQ5LxZ6kAQAE72bYOQltWeYvcAdIlgusemvScFrUskuvpp1EbqQcx0Af5aDH3G4ppUce_kzm-1whOesAz-G_FhNpVlSBKPJyghAaTehKT3DX_LdbCEm0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZuZRRrPqGJqT7GIJe7e2qy6bRhesgJkdyiteScLT1-dVo4flCk9AidamU3z1TS1F6m86vIyG6oyTHfZhz6jqCLsR2Q2yyRDlaeIMBYvz5jDzdeJ9Qf7CA9GIqm5eoS6gUhN6o1pgr8imLNY9y_XR-g6Bpq5J5C2nfg8b6BbLlYH8limEwdX0XI36o_y10EiJmMZ3nOuZmX5F7QfVmYOoXO6CP-mTsDLmB3RYr8ksAksLmgYSK5pfUTJuXeeLRJup6g2D2DZBYNBpwD4xsxuWrCXh0p0qODImbgU6-yUnBvRvKx0RqZoinEU5C9i18GqTN-tRa9tOhCpx7o80nwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7V64SVBTclIvsId_1yYdlXKGq1pBzlf7yzUOfUBIZaCGjeE7ZjFb8yzzJVBHHPQbJZHqK1gPd9GqK6INBlQP4x9l_FUrayED8jOO826PeRSNhgg-bKJsyhNC3mt_857S6UCpeSm2sb541rmMByyg3XOaeQ2_ccM6NxqFiC3jA5QVp_pcMqo434R_wyW-weAl9HM8mqUAYVppyQCgIxCvKLVBssBDxIVJQgsQbqPqH6VxicoXc-z2GaRTulvzTbvILogF8NRkRw4X95QfbkIlj-ke50KavIo7cc1ba-zZtkcykqmjeopMJHc2sM353HuoObNyLVSfZLYi7pH-xjGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA2l0LPH0MC659R2ooDQSER5ra-PTdpi6kvs0DGwsE7GFxQJ20MFg19VUYdw5ujiXS3eXtewNHe4RPhlPJdSzhgMBC08vOxuhGTQftvayFbXTJ1yEWC3Gvd5uMuk6L_oPHToJtEA6_Boc-x7wCx0tS-17GoriXZRnFW9zbCbvS8KQ-c_MhJiJMbjqTYGA0GzW9AGi_UivFkzrwxVdk9rENLEFWNgBmsILQr8DJIgiTUgUGMynLLBF426x4wlPf1_UXiMbBoktuWcbCt0MU2PERlj79s4FtkOFPNpOiR3lnzM7nTSHrBypi29KpJU-Xfl7pfUdFS2wUHbmAFk2EUzRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=qr_LAXiwlokmUQYdbmQ1aT_wJduZX2f1GaUE9zsk_395yZQL_VJFrSkYRd_Qi8VGorRRgZyto-m3r4-nAEs4_vXOuNIonH3HIIwMTRH6nRm5fn54AQ8G5GAKqxPTwj6SCLr5mXvWCPDDiBXhHKZs2xrAEMjwqzfrfMOIgdPP2Pctz8cZpgZ7KewCPNZ11rDXMN4bEjYDL2qfl8FQ5NayAP0u_UdYDCiiky85kadH7qx73c3Y1KXJ89t9qZaHhMo3I0Vr3PGyCgqiLX3_ES_vRVm6EYcoxQYFw2WV045zGrJd5F7aVsLJU6vj9d3imrYusmYq45MgDSDQWQIM_DinEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=qr_LAXiwlokmUQYdbmQ1aT_wJduZX2f1GaUE9zsk_395yZQL_VJFrSkYRd_Qi8VGorRRgZyto-m3r4-nAEs4_vXOuNIonH3HIIwMTRH6nRm5fn54AQ8G5GAKqxPTwj6SCLr5mXvWCPDDiBXhHKZs2xrAEMjwqzfrfMOIgdPP2Pctz8cZpgZ7KewCPNZ11rDXMN4bEjYDL2qfl8FQ5NayAP0u_UdYDCiiky85kadH7qx73c3Y1KXJ89t9qZaHhMo3I0Vr3PGyCgqiLX3_ES_vRVm6EYcoxQYFw2WV045zGrJd5F7aVsLJU6vj9d3imrYusmYq45MgDSDQWQIM_DinEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=SmADOarocl1o2fng5BPV1ZND11aMVDWyPB5VJpSipdfRgsAYyyYi-YyXR423xpqZy_2OCKHCQDiQt3suD-nvPjGQMrwuUZgylGp5BqnH-eFKI29XgQdzCgxN6Nhhklc7FNyjIy61fhN5J5TJOBO8cEommGxwMIJzUB251FOgCrF9sX7DxmjEQQyQMw5y8Ci6A3jWEYdtzP6E7e9ONFsQ-0EmYjpwS5UckgficoSwTXVqgY2Wjbt2JPLFQETnkyL_ud6IcWyWrBpuaG5zsSLLYE2f4GRRQw__wtY0OmwKZMhRKml8ix0eb8VSTjilOmUVZxIMllyxfdAUZpeaArJXxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=SmADOarocl1o2fng5BPV1ZND11aMVDWyPB5VJpSipdfRgsAYyyYi-YyXR423xpqZy_2OCKHCQDiQt3suD-nvPjGQMrwuUZgylGp5BqnH-eFKI29XgQdzCgxN6Nhhklc7FNyjIy61fhN5J5TJOBO8cEommGxwMIJzUB251FOgCrF9sX7DxmjEQQyQMw5y8Ci6A3jWEYdtzP6E7e9ONFsQ-0EmYjpwS5UckgficoSwTXVqgY2Wjbt2JPLFQETnkyL_ud6IcWyWrBpuaG5zsSLLYE2f4GRRQw__wtY0OmwKZMhRKml8ix0eb8VSTjilOmUVZxIMllyxfdAUZpeaArJXxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=CeXxs3yEfyPXltIdwPrdcgRA7_jn1W2MpOX-WGINodcGQ2t_3M2YKPt8-FHBZRIOg3-zfzaisBoxwSAhbeBvH-q3375YhpCJnfwHcAIhunVqmYiPpDPWb7hQBKUUCsPfsei4bHPCoi10CapiDRYi_5XMwWITHgp8wlICyll0x1dbHGKgIqxC-8yxJXjzrkLp1yDlbtUzNanS4V_74y41vd0HRv6PflHoIdph0IgghTP0iG_cHoDXi91JqGfLQdBqqGZ67fo8ydxJaRvFddxN0QjQOJeMtrEOXsLxKwzLX-_6rNLa1ayLPFNYkEqKBC-_h9nrZzXl382LI8ou55ZKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=CeXxs3yEfyPXltIdwPrdcgRA7_jn1W2MpOX-WGINodcGQ2t_3M2YKPt8-FHBZRIOg3-zfzaisBoxwSAhbeBvH-q3375YhpCJnfwHcAIhunVqmYiPpDPWb7hQBKUUCsPfsei4bHPCoi10CapiDRYi_5XMwWITHgp8wlICyll0x1dbHGKgIqxC-8yxJXjzrkLp1yDlbtUzNanS4V_74y41vd0HRv6PflHoIdph0IgghTP0iG_cHoDXi91JqGfLQdBqqGZ67fo8ydxJaRvFddxN0QjQOJeMtrEOXsLxKwzLX-_6rNLa1ayLPFNYkEqKBC-_h9nrZzXl382LI8ou55ZKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBpWUK-c0rStIInSuOu9pR8SC_7lYzcBnn9701h75FLXv0YeRFQAbwQ1FsIPSyMZYCQBvT5gJQAVOPVcLr2Zmg8tLNv2wk5rkVql5SxAQ0bm7Yw-OmpY4_aKda9adNeNlxzyrv-sTtXkCWJqppr8hMp6E58IoF-Kii4gpkSO8JnwvlYHolCHrQ8NgorguXSIB_c_dbAau2vFnJfk-RjvxgveSkdd5fG1e0U2axKvoVF-Fi5K4z-qIfXs8PvSRPY1kbJdvAwmq389BFw8LdTOM31e_E-GIkC3-hctwqT3VnrJxbWqP8lnYmu84GytFfXltlF0KlVOkfjQ6GXaskfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJgqluH5NFwKO37giK-x_K7_nLsN6EYPojUSckYpIKjekOf7g5KzU4_LyqT6ItmPkiLvt4ePiRIfrOTJlXc0wm3KnAzYl7ydvm4LPnINf6IcAW0EdBUK9SPkVQg7LqbKOgTX1ITV1V8q5aTaL_ODTLnC5doOTiC-KpxaFfA2zijXKv4MZygwAv5z-P-yIJdNK1Sd4cpeoOPhZ0ampltHYd-ySs_cIPaCNtNHqQRjuLGHEdpqVrCJxSW28c8A2UMcbnEEYqBMyt6Gk3w16Kd7XhFwlCYvejd5ag_URTm1NVT8xGvSk5fhxvMiCt2fS-JaoIUAsNhYwBRzFSOSvIipfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHIctPbU4ynji0GN1F849NrpI7DLvJSLm4kjYK9Hhvfo0c3gd_ygJ43I-aMWfsQQEk3PixE3JtDAr6KbfVtGNj4S4LFY0p8xSWzMv_g-QTEuM2wmBW_wPOTT2-nNfdzuLfM7RGdDERa1h4FS8yx-J3Nl6sD78uXWROVg2fdRSTn01lSk2jz0frZxj3UPe77yzLxa6kz0C3-e7AgYzNT2mzUmSXrfTzSifoFfgeAH8gWYGyCNCwdU61ywHrwYJvaeW3NXFo6AhVygs5i0JKoXQMKwQDtYStQYrEToHHBlJVTtNQk_I2Zp0VZtn_aQPmO9sh4pVQwTpS5FCp4JEfG6Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7P-9mcGcasqI8aNXcciXJyL_qdQ1PhlZru0gyT3He6L_eJrSgAK6EVREmMaJTKpLs806PxLn0Y8PULd958TgN3Q2MCFWyhxUrhcSNKxNBm6IqrguJUSGrNEstUcNogzzIhMSppsnXYgkXdTQ2IwbGYl5HWq6nrawHaZU6---JllgclRnzMdBVtV0e-UCDlabuVWPxxaV2rrtIAxXY0p2FzeXYnQH4ZbjJcPBrY9AqElkodF-Kuk-M_1Ukq7bh7oBrI8N6GB0HZjDjyZoiTEE11oN2XYyzcXExQtGKX_szZbTIiOCbbRymP4uYUsgRlMJfBtYMnCf71SQ3hGIH8mpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ME4at6msWqzdnDJGSRy3w9NUYx0IQ8Z9IF96-GFhL6Ol75A5RoZ5cLFsYAW1g0c-8QpdrpxNMAGTAG9YlENvbvnvnCMYWTPrzNkyXayeUSjy53MrsnV77xE7xtAbA1nkMOwd_rzxpkgbXlSQZgKcPxNd5CK55u9auexdeAiD3oSyKzIRCl6YuOj3ESOnS-KUztBDj5QNT-TdUN5FkxpLWQykHhHz5lrlZUzlzmKnKg4ieqsf9GAAN-OhQFSLkn6AeWkw2YVnbTN9EHSsMecV6hxLbuwlvibLfhLs0NW53q5puAY0_aCX98LT6xKIwCkaRfyv-RQ4zGmVlfKwxoxEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak8vzl-gSQ0qCEH0jcE86XBPCrCwi19otWFB31PGyygP2HNPWyMnxsKK2iOnD0L38BUZWzEx6-VKPfvbXlXtOW2KkbYfhRGCLS2733Sp7IJNP7OycUd-KFXHYnTO_7tSogdhlcGkCFHxWSlUq6uN9GZ7ptLuYwo3zFEwFb3aX9w8v8CYveB_1BHMmfC_Zrzg6VPcQ7UGRf7Q5X7j-o7w6lNq_po7m_54N31XXKxeE7bGbD8jyfXrFwLdCOoya8s1fQy7-bIVYWdt_3JFYLq9TA1ZID14lpHqc0KEWm92caGeACVodPQLA-TDlwkUnTt-j14ENefmGboBLh77T4flmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y5Xm4Kdg3Ac886lnp-We_ebgegHcm6k1Fw3c9Et4zx02QmK3IeTtzXVKbzAZwQQLjB7nkbXc0lO6BHmMkO_qi4UESFjrt_u9LYlEpk1B1sjRAxj8PsjIvox2ZcJCcvndGyP-IFSJA2GmDKw3EFQ6WRiXE1jL7AnR2jkgnnHv-5gm2TVnOZyIc2Cpl2dswPxqpwfUrkCUUWn6Cr2xNBpZgl2cWzavxoP4uYULpFIXgXI63ExFyi1EtZknHKX6gucnoPGGQkdaCqWrrBKof3O2xv4_jqMAryIxFBVX5akCLDtKBkgIyjZDHSKlBQcVXT2Z-Qx4Zsv-4nc8wzmDLpbCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmESXx-iFucvH4h8tqnLRmDwFQl9YEvN9kBPi3S7SqWRZdSGyS7YwPh0n3SI96cUoBSA3C2dxh1cp7L1dHhdQdXNgAfDFPwC0_VKLzWkQWFQDmeMLaoygTvrksI4eff53c-1oWZMTpwq7exa0Uz_LIl9lVzSmWujsxc6oIGXiEkphNI6_lSGlVMFgjjbC4shRw0SQUhXn6GimO8dDFNNXQRsP1HTGiQ0LQ2UraZCdQFiSxrKBPGvdHpDDZMuMZdrt-SOzG2WVNvP6VYsvJ96uF3HOGprguyezeAqaa8albOOZ9j9aSscdx2PtSSFVCJDHKJJYJhcviwSSrZbcr74eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt_nDZz6GdtgHHJL1bkOOqN08nCMCbs2XFz5qCN7Fnbcc3jEZPrOZTt8tPxYQBzwSZcSAPIsSVB6GBn0fpXE_sm4io5q_jGxHvJpIx0eJtbCIwl1uc0P3LOTeEQpIlnDFOvPSyvxctrQNZh0hhnAmYkLAcJtzVl0FUNwXpVR8ZzYr-nld5ccPXv4scSTuE-YVGdnyWm38ncjWJW5PpQ8Syh-y1r1raT1n9QCpoJ07ut3tyUx4VJ1PkcmF8fTN3cKdubPHTHgBuB9hly9uvRxGdYzym3Y1hauRdMZp8KS9STzZmlf5leN8kGOLg8F15JykKwgu85mjFplZiHbTDzfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPXE9RUkO14mQANbusYisZ7eJozUlzZqI-fRVOXzp7aKXICpydLsgCzgCmUMUL8-DhQiYhHNK6zopT2Wi8DtIDcuw3qPivqv77sKTbN0Nz6jY3VyagEuToYgMg1ADH5ZWCNl2SJvhzKPbelpkZjgdjpXATfGyE5OQA9hNN49uX6rgc3bpGQz_tMISevurkChHnf2cyhBUtGtAbM1H970eEp8-hWBjL-hp064nTgiFaxXzgJIJ8fT1FMka7xfZYDxChWgvKvfbr1syj5bY8bycqazP7YwxXhVa7RyqLxkoVZqqR54l80YP2lUh_OAgT3DsVyVqwjH7XWSXvbDHXRAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100576">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100576" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100575">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdxrkMZDBpLUy5ReRHCpUl_yYjPS-T_kh9iYJ45acCwUWPCjEhNnRYJuZm2jj9vv7PgEenDZvIFVcu7vuXboC6nU1zSbgDdhW45kLtXIgIJsAbybnG0Q0NKUJhoj7MrNR7jM0UCKG0dGjsoGuQLQPAp0iQAQIjK4izoLIuDEvXKnNFB0XUGIsF8VErlqplnIlAWwD_s2wqew7bAAYXKFupApEkdAzm6VGYZILA8kx85eLQxKx9H3x8Q8yE4KjtnSnwtA3Sg1U0e5cCyiZOxlU9uiXXD7BPLYDpZntlgBI3o-6iAt3_q5dhpU6j8llwPTZfvk7xvoUOa6Y4efDQU1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100575" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbNOuqJDqJo9CRFMZ33N6asN5--_cS26k4LyFlLwc7LJQ1Y39YuZnc2PqjW2bDKEiClez0jzl8vkJeG2V3yBcbujbG1qHJwF85gDLZI909aySCB0S8KzA2QhZBBZ_QpDr2iFKfw08dI7OdlOsbdvaFWIBQDh2uxV_HFqGHjkty6mhW__oeAGmzw-GHugaOTCkZ6ZGnzwb10Yr9LblCCyncp6b2_OFgGyinH6oReUUwAsGGPjrP5TL0Y7M_mZZhVO0acSrxFjghnyMwn9svreTn5HrErjXQllwUAnzHIjZL7s9Q2HuDE8aayPk4FTEzzVXYaQodA_P_HoYUsrxcO4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/httl1_oj5NQSNTZOOkHKtVVX_FINKnMKPpvnHKxxaMho8s92Xh3xqDIjg8okBbizS_kzq8tu43_tlEIcxBiX8XTH2WF_YgpoUDrnEGMtXkS1uAx-5SUP_FaEfs33WMgAnqYIYKNFiFiQegeyEjzhcIju8PB-v0ZzLbfAN0EFQYfy6PRqJ1HG1H798Uq_t0d8_wl6beC9WOHVsXw84bM19DWf4gEkAnHrPWcELR99JzjTS3UeCwOBEDt8D-7SNz7Q6Bp-ktYhGmXE0gtqeuBEHjN1GkToz0ODYs8zIbrrgG_bCPB1OTjCZa7UfQUCWAluBIkRhNKiL4MX7jbkrve6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKSuXxnuPDu2rhl2njwNIwkc788NwgMih_UGoQSOrJOTAzzLh7Yk8XYlv-5RTQHmIBmMN869GnhaTsj7l-98-djhTKxDk14Ghr7kiUdxld2X16NVrbge7XNTj0deXXFRqUq20DkGhUMhNQbvvMQwHT7FQ8XoUHvX6-eKtFlPulaEPlMskxpIINC9vpF5Yu3Hygl-Bj7R7xD43j7cDKrIAAAL6PYXtJf-ZvE8pmiwwSep-V-RiUZe2mRcmXOWydha2BmBb3MJmMxNbeKl3QOco-62sdgh7u_fiAt3Ap7vSslSe7j2qZCEX50YNoxbODuGkbTM2KuLUMRIzzfLwLIseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSStC8a7FryHm5bRzPfOdWya3RWBQ5soEwvxRV_2O06vpji1u8dQP7eTXwHiMpCfmzCbeUQusi07B8e536RsEnx4ZH2kOOAzgCSJuHpZf9IDELSsD4EdogDSbmwMdJcBglE0MtfkBDT_7Xw8X-oChQ43tljgyQuOcry8Qr5ru3uEeVHkXGUNKzou1SGOxKr4f6-FBIhVzPeAbEzhl5TaHJ4Q3ugI5PsO5I5p4neYZaSoLzRe8DHwWr--_ObMoE6sj0lVF4f6zOQQcjagJ_Sy50qq_kcGkvklfFTp8nomIPkFxCeuusHcRbhUIzdLS0DP36KC4BLwxfV2XXhdkNCTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4VMY9CPbsB6oe485KsOmEsvpwi0F8SyC3z_IBC-bZwkaJGeySvBG-YUhkw5SUSpR__oN9ULj0SGk3FeBCPnO3HW33Q-USCyV8ox7-_z4TjoQeydp8oD-rNixHrPlVCRKhIYVo7_6RVH6Ean5xli_iGYNHbxkjdsYqpvVr4pq7xtpqnJYC0VBJadjOqroRgc5WLy05tvFfehfwOjKWHTvsklzdochqx_t7eI_p2CtLu1mzaOsiYZL7DreyhZHIBazRYVsYImfsFEPsSf82Y7o1oyXjGyK3l-5MIzzEM8fwcRk_JrjZnE3etTpx0tPuzdF9bGw9UwrCVj3q-u759tyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsFd9j15CMYMTbspfy1O98ya5j9Zxo1qmF-iPQGDjHZiMsqzBh-Y3W_KUi8PoOCASVAQSZ42LXbOMjUyBGSg6JnOmXg0ekkAEFB7IPYQdt84JMkSaXIMqVV2VviGgulJVJa_1ajIuxS5UWHddFRL0KpiIpGPdhonhAhFIrBMRK6_hFbVfesJjS4eQ3TpFIBb8v2OjsIbAJxzSIaPBERHH87CZ-ZayMyDx8WgaGOSA4VfYGunBQL6QSnRfdG80yjqDrz4lW5TBNAXjb0JbokbZCfRsD2YuV0YfIu23TW_B7yO3K2J1-zz_L4obt0I0BC09ODjoeUE9RfKKMeVF5FEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAqfhxiEpSAgqMcjdIjXrqSNII01bfBWUhAvmeUMQZoqB1zNY2gZssYHbVL0hXlGCIIGrO56TDFrm7X12k6RPf_1YHPdGNTIyFCNMqISBHojONvI6uAvM940Xo_ykOEzn4Z4xQZLXNteepTfPNTvMUV7Wz8uQDcrdrAKQtV_WnG_IXPsWrXYA6pjjjCPg_us_HNc-MTdgtWHwFOV2j5H0QfwcUcTiCw72VijkVdy1BlV_YIgoE8BQsG_LGaKDu-f84uT9TBH-64AKVLo8A39NUNn1sGDUSOtSruYuPuc4FoX1COvjG6R-36tUqT9W7K6AwtXK0kmqPBGIYpsJ8yfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=FSG1Yt3InAnEcmcKwbovbvSh0JkMQjVHnHVL-tsKo5uT9izJOBIzspxoL2IEo04IsKMx4eNBUGaSN9_abv-78fT45-2wRw4SYZnaxfV4MzgEGcNgX0SHYmKSuDmmykBbkiYDc_uuiZicEJSokh0YEtmyuEyzYtNkXSQZhtf6YFfsUzmh8OojF9dPBHijZ0REzxpiNcDmM_cinZNrI8QAEga6CSnv1brqGJsExwyqOGh1GiJoXglHOy19snkJ2TnEEiSFYeUkYAL7hJYUXJaNWvk_vvmgz5AcF-bBZ207gSTKoUQJwM980qVCqQBTGfH6UWN1xyN1bWxbVgAnsfrRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=FSG1Yt3InAnEcmcKwbovbvSh0JkMQjVHnHVL-tsKo5uT9izJOBIzspxoL2IEo04IsKMx4eNBUGaSN9_abv-78fT45-2wRw4SYZnaxfV4MzgEGcNgX0SHYmKSuDmmykBbkiYDc_uuiZicEJSokh0YEtmyuEyzYtNkXSQZhtf6YFfsUzmh8OojF9dPBHijZ0REzxpiNcDmM_cinZNrI8QAEga6CSnv1brqGJsExwyqOGh1GiJoXglHOy19snkJ2TnEEiSFYeUkYAL7hJYUXJaNWvk_vvmgz5AcF-bBZ207gSTKoUQJwM980qVCqQBTGfH6UWN1xyN1bWxbVgAnsfrRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=sX-8zqXsVWynmUnBUfn9c60p3Nj_I1oBpRgOOTp9IKo9WK9J-mEulvr3eFlYiJLI4fRvFXC9B004DFOGkQMBKWCJFFokWyNY0mRlsaBRfPH1eD6GBEHMBj0goYyuvJwc5Tvf05X7sZxF0RAbg27qk09NEtx_GvggVL39Lnkdhxc1YRP4HGtlFwmvhpEafXwhHxaFGIl5BDsg4H_0BBvuEzwGE-PUwSKs60JuXZTfNEXyzEDuD3LNLcQYgM_yRvFhYf-58g3ytzsXaXhItk2CIB-2VcF77UHviFqCWcuSwlbLVNZizs7HpOpWXrx3SJgxi-NGGMIkO_SBXzorVQ1qkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=sX-8zqXsVWynmUnBUfn9c60p3Nj_I1oBpRgOOTp9IKo9WK9J-mEulvr3eFlYiJLI4fRvFXC9B004DFOGkQMBKWCJFFokWyNY0mRlsaBRfPH1eD6GBEHMBj0goYyuvJwc5Tvf05X7sZxF0RAbg27qk09NEtx_GvggVL39Lnkdhxc1YRP4HGtlFwmvhpEafXwhHxaFGIl5BDsg4H_0BBvuEzwGE-PUwSKs60JuXZTfNEXyzEDuD3LNLcQYgM_yRvFhYf-58g3ytzsXaXhItk2CIB-2VcF77UHviFqCWcuSwlbLVNZizs7HpOpWXrx3SJgxi-NGGMIkO_SBXzorVQ1qkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etaNzrExHXW7vLlXOaAk1vpIaIx4BPYBpZlQMVjpoQ8fypfhWhcC-zq5foisrkP25Mf09V6XlQWhG7VG0szhNw_DfebWAN9EFpQSuTiIU1jKVzrbodlwNJpGQdhenBe-kyfqhrNVMjEyHfInzCkNyTNhmYMF9rfJ6fFdpYiEJV9ALEkhZGzky6iOgWCTTuxPsqJTVFakHrNeTlWy2AJsoO23TRO4_nKNSjse5AVNceJ80b0JEXNfHEhRaVzkmuCU2bPTTFpdOavZu7SvAZalm5ZqjXMxB2kO9JXr5DqDZbW4N553jti4mmCNaJ7GQZ5UEX1wwzLry5pwuyXsmRkh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jFyCgRDFHC4sgfBUAWrcM0p3PrzdYQ3ogxjEgRjlTp1ee4dv_TrH2FAChlhU3-1coQpEGe-AJz54TGezdyYsrmpoVzyBrWdyafu74sYoA5r3zW7ZWcjfmRQPE9ECeT2BpesrxR_yAsi27FPPTbjDDsrPtBdontE9hK5nCFkZGW3nq87ASMzqghwgEJJIaKsDKJ1fRpOG9xyLVcwHTGCg8kWl2VAZGjKoKTpQfRqZKqPYW2_CQPD9A7UrBT1k29pzSlWEVuJxtW2q5-QHF6J0in8ZugM9YN_rfXzB8kR8eF_jRgXqRfM8WB3GWJbhViMMdSYRcGadro63TrYVetpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=f-8XMAMJEsLGDKJgoMyI_1KC_KjDSMQ9I__uy0dRbxYoqneK0RPywQqlFAL_asvykq6HTIqOY7tuHDlOtpqPSDPPO61Gs06_bLVTMnrx1MbdAd0yD9OUojHRkKCzOxgyg643sRSu-v0C_0aS79kGkGGvCQl98m2XEKoEuPzHcG5hcaSVsI4Szz7ZLpPF1enFMSRY-IT4wr7ToP8L_ro4giAUwL7G-qLw5YfGzYyjMEqmvsKKrGosxE9Lvh3I6y5bKQW0VSgnS4HwAyQSU1fSVpnqdW04Wst-mHoGGrPuUz1nGdKCJVEb8FodkD14VvH9J6k9KgjPTDzqt-3lRFtZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=f-8XMAMJEsLGDKJgoMyI_1KC_KjDSMQ9I__uy0dRbxYoqneK0RPywQqlFAL_asvykq6HTIqOY7tuHDlOtpqPSDPPO61Gs06_bLVTMnrx1MbdAd0yD9OUojHRkKCzOxgyg643sRSu-v0C_0aS79kGkGGvCQl98m2XEKoEuPzHcG5hcaSVsI4Szz7ZLpPF1enFMSRY-IT4wr7ToP8L_ro4giAUwL7G-qLw5YfGzYyjMEqmvsKKrGosxE9Lvh3I6y5bKQW0VSgnS4HwAyQSU1fSVpnqdW04Wst-mHoGGrPuUz1nGdKCJVEb8FodkD14VvH9J6k9KgjPTDzqt-3lRFtZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1HCHRareEQGA3ZFjQJgWeoN_gqAg7W0V7asKTmO7yJZFV8dV6RhVQAHN0_AiR76bi7XTfn5OLsO-2eeKxjOIfQWzqOP9a9iKYbx2WAerb5tajFdMXy4CW-fn3InDTZocxihXKmzJClB3m3oSHDa9WZQY_fq3dKITjIuTm9-stOsL1yQq-TpTaGl-t83NsPqZrD6HjLzcFZDqE05QXJekNXR1t_QOXngAdNWK12rFZEtpClMQZlVN4X8vJzpOgg_tFUuVbSye_sCLmYsyTHvbBJENZhdwREyybvSUfTUeioPk8UW0RZgSbIGgGutF48ES8aMIxbh7QJiCa62EXji_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDog0mGEQQTmSMrQYWOGMpG7ksjmQEp15_tRQIzRQvSh7BNoQsqBtSsjiqt8rzre1BcyWq7XZHr3Ncgfj-UofRsZlw_mwhBHHgkE3y_ioyApTc_Tmdrh1uQGQO574xjLpiAI3EhU2dv2PBCSuSFqOZNydaFPRJKkfRbAtN9P9TIda1KT7wl0CpJcf3UzbPRvlpn7ALD496zmChITN1ehjQzgy2_JEV032AbF0XgwEdE5GYZf5MgksurNjKI_Vx2ZEiYnSvVbtu609exCVZkvN4rXORKWruNMEVVoKYA5-avlmya3cGraUnsjeg-yiVp154ZKlOV3hZzsd_DERyardg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luurSg-AEzeji3gQHSWdVmRDGz0xOcXPVEJNQEspmkRs0eEUPvAfaa9qXhqsJo8iyvyEKuuNHL_kFVASnrr6VW4mysrgISJgGyawIHcxJpXCLe2TNUOhHH7trBQsAouO7H0DCY-gt1LEcWfcmpo0fSaXUV38DmkFasW_JDRybFONIA99ugfiA3eoUz3XpueOEFBAZnYkM_9X807y4-lyi0CRFzfaQ8cEiMMn0aGHILSRTagt1lCUHwcU1Aq1euY3XLhM-AXjJ2T8kr9Esb8mD2UD7gX-poU5qtw-9P7ZAXCHan3kz0C51R4FbS8BYu2Kn2FCAqrnnBgQ7-aGL4tbgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzO8VJvi5xlocjks4w0GpZnUTqLRI3eqn422bNcZwq5SjTjbFSkHCUTf6TTijD3uqnIQu7O4CLUH1uaoIScqNNQIH7bStYCUSMkCZ9H7Kzsoy_kZWo1H4WPNs3sRAkyw8T4c_GUOR-ZAY34F3ZMXa_vhkwc42sg5yf6dvB9EZbfC3MhfMMvTJSAZMAZxWiPq06ilbLjAZQRjtW8uSHsjgPBcrsIks-Bsxe5YEL88CmQk_dGpzb9Wli13R6hLnAP9s2LGdUfgHyaLctDsiamQcFIjijeLWvScGqCZExZxNH9cBxW130ljf3rl9WzmWiTljS1n66wwRzJF6kTtvWvbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHs0tmD2AGKg3F0ZkWt95TgvqIfuMpX8hQhKqCVj4fAcUBNvt36gTkAODmqH91WlgrQnqpQakNAf5nfFXAflOygl8d8G88mCLrigUuJxOWyaqmX4IQcgi8ac8QVdLHVVILzeQ7LatcaQQ_YQ0Hkx6LT-x7Ub13HXW5WF7w4Fk8qTT--x3wMzlugL-NqGlc_4H0UiQPwhufZM7z7bP6UHJQeUzo8XFXpbTRd32jbmUhlEfoSoOxk59NK2fp-idH0HksM5cB0SVspuS4V7r7cwfuELqASEmNT3bJxA8YKoiSh7lonPajwtnrBTCxg8AV4YT8kLCgaZeBrs_fQ2biJCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGSlP5K-cLcnKR6j63S5BAJPXUIzIvfD0aRPVfEnhfvD2n7RQb0dZ0ZWGS_TGeAd9qaQ9dDUwWgWbYs_YNJagssLHlcANWMw9goVNpQbohq7-AtJBtOkJS4AwP3iKi41wkaC4GBUsSlk0ObJgdf9BKA0bE27Sh8YDj2w0OLs27U7_xZNbqcvNigNiJUfKqDRJmpbE0UhrI6n_QUDT6fdwxIw8CxSTQGjsOouGaZKWMTWulJbq6JzrsENifRB8QjayLelceHo8X1aIf9wHdCcuFf5ehczxzZFIPOV05A-ujXl23v7xdbAeT8hs8qLU-wx8VJ2OCMhs4szseoakCG3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVmZVEaPzMiT6fSLhEppz8ZMelg-XCho9fhSGjJvFbXv2ocTx4AMKzwnVfZSYdCzOcyYosh8GZ_ZOLaY-_Es1G3NCYvwiaHuhDWLfpy-2d2KwxkZblypO7AZi-268weR5B9iuh5U_fyUaq5pu-_eXznkpQU_4hoI05-zhqzFNGHL-m--aE5JXlkqF8t_QNVa05sYwuvBQtSCC6XjzAI7CYuVHz4ptk2ujrlIUuaivdpEYqyHiTBac0NlI6WVsHdtkVPNyXSXBCgt92IZ7KxkEiMFpRTg-Qiu6ehmgBO547M_YKfl22SxmhdL9TUehGWBn9_bz4DC6uwR9fqXEKYE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYbY7V3AtQYJXHqG348tsveN63YyDAWRTx52mZT4Q1hB_v7d7Oyz4cHXS46dRa7TiFrozNCCzuZR1I7hBAkGWeqjyOBj3zDzlGlMYgftTMqEhrObpSfYXX57O-MiXKeULUhf7QUMcw4h4rH2MTOgM1fnOPnGGMCiUgM8kJcSEQONnK7wIbs1gLNoD4Q2AtzWAuYRUwr1RRdLCITj2yrMfRSGICBGe0cBShEr6vZTMPWC9KVcNlPqgKwSF3EzdCPX2caywXmZiJbcQNLGrT7SML5XJro_6DTiHbTszR-R2FEU7lmX-47zoHUTeloirwm4zCXYxOLoIFo1e-gIbe9hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXTkxhrxGSQNkyq9wDcVq2txn3L61SNLoeUBV288cZrUx21VPTjpRJo__ktDA3uM-kiNjIF7hI5HgYTNm8ReftJlPIN_t8rHCePwMncvmsekiLi5a1t0-4f78RrJRXpLzdRzwEm8zW3vNbrFtrqcleYgU6_xDRi-T0eHpzk37n-FDE2B1Iud_u6_FTgNgsEm1k6y-xTcKtAOueI8EkBII0c32PAo78oRCIm_uIVrwbLDT_jnLtKiPG5XIiZyudO2zI-b_IHlpzPoUiy3oFHNTFGzdjrE20OhlvV2_08SwE5bmtkx6UXwtWF8IQfyIGv8ZRJs2IumM93G0Ou-yL2Rog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXxjct4oWgsuaCDbRs2ayuYAccLrZLXuJDLFyrX2ykgCEBUTWdwyhg-b8a47_i5HmwoUYAhjl4xe0U7NpR8nKP0L56qO-RRXpSlB86OrwYoZP6iawRz9O7aDx9WJ-bC3MhMwwab8JW4On6ehtQzLHsZuaNNQxIOI1JAq7JxBGM-iyqRiUfuKl73Q7fSIQJ49hGAXsSffAy7MEimy4u7L-xxqD2OCbpzvOdJA3PzP61uMqJO4yIW0wJtHFsVDve50Dk22d0qn9MALYuoLHTJy8xtCWTs84wuSFcB4xRVKfVrdda-Zu48mYtxZPr5ry3QleD7YwzhwB3Fr77_fWqD94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXg78yJsSdaWwfP96z3nsHNW_ddvyUOyDyFp0LfXLCIpewdxcbVu1MNvbE1vGv3zDH7S1y3hARbS6284zlUwxUeBnVrQ2jffpL4fb4Z7Bw5jO2lPHEdFhOKKAmYn9Bgr8fADCHr2ArtCpMe3GImfFPTFr_oJcvJO4Pr1s7ElpeSupo8kZ32AbgQrWzzjpnLukU7qXvpXyMv3tnw6Y3mqZ5jX-9yS5F_Oc-kJicvrp0Cfk9wfeVfOA3EtFxT0PyXEi-gEVe41L0sCztRAACwvNAfChkN_C2xqsXF44gBFzb285JEhLQlEPXDP9zKmvRwa4el9Rhnhclzz8KRPSz09Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXIQgPuMh1k2rQ_gPxy2sVyd_ULLM3hrW_DTCM1thtOyylrXgnSZg0HxTvyuqH25pd8zyoR0sq9flw0A9DOQ9WM4GTLlkepphmnIHiqGoNxOHTMI0XALVGRqeopdQQLPQcVgRoFbDEip4gYYxf3gP2AegeThgu19R6FqK1PB_4p6stHTRMSMa1NFRrJjfHLfjXiCY4gKohqAsOFrmryKZNWxDrr1E630O7ADIx2PYpEDJYMXuahpKDHj9yS2xp87OK4e4H13VxjR-XOpB4hR34ksRakH0IUc6lBZwkkdMu2eNiGKkfNAsK4l8jwXf4tjY2F0l_vOptB-reCh3Odsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhw5N5HKUR-fZSuj7BinMneKbJt1zJ6xGXlzENSLFnI0Tqgp_GOcnNgl7tIwcx9INQsCHJnoav4WxUeUuinKKvpIo0YEurnf8_NbRIMMHouKm2GHPWdGhuQuSTeilDWFUjX3lb7y1mjz7siQ6zRVMxVO7d3OzT9Z8p-edtfPWZbzGNxmQlRwvxRfniJSOP8SHhgApJ-gZ8YNAgsuO33_mnaj01uqHq4Ce0-KtteIGcgb20RZ1cProSimIXcmOjDls19rx1n4AX_JB1c0Gs4eR5Mhg5SMpCMB3VPsY2DAS_kLSZEtqjOw2U4aUpyCkHXb8QtaHZh1V1llhK27tY99Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=LPHgLG0PfWSb8WW9N_-SWKSE_SlJ7TUg6vpnTtAm5Pr7QkR_gtOas0Ly5zVR7etJvVuZsil-yUen3Dhg1RyATXcbLK9pCVEjm5IzvwIUxjtug27uj04k8R8NacWSfAYl5hUCVDYd6aCcV4Rft11iWhtHq5TcMLRg78lLJiNPizDli2NEEG6kQznK2hHoAt6_fx9XLbfVgwOFZpXbWHnJpdPS0s1NbM758OCp5jW8w5Yi0JKoNRosWriE2AntK_D92ftK2XLDss1gJp1crbzvU9pVAmmgfPHlVVDlV7-UlsXgjruSFHIvsTfRvDuC8x3mCRCfiL2wtTvXFdI26_LHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=LPHgLG0PfWSb8WW9N_-SWKSE_SlJ7TUg6vpnTtAm5Pr7QkR_gtOas0Ly5zVR7etJvVuZsil-yUen3Dhg1RyATXcbLK9pCVEjm5IzvwIUxjtug27uj04k8R8NacWSfAYl5hUCVDYd6aCcV4Rft11iWhtHq5TcMLRg78lLJiNPizDli2NEEG6kQznK2hHoAt6_fx9XLbfVgwOFZpXbWHnJpdPS0s1NbM758OCp5jW8w5Yi0JKoNRosWriE2AntK_D92ftK2XLDss1gJp1crbzvU9pVAmmgfPHlVVDlV7-UlsXgjruSFHIvsTfRvDuC8x3mCRCfiL2wtTvXFdI26_LHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqOBhWriz6gC7cAH33XcofQuWmbZDYJujdvUojTs9Ix-N1GE631UJZBuonnfiwAjnw38ioSZr7Mon2uyEEPMdcXl9dfz7r-PC6Q-NeT6sDCUhIapcDU8wS5BUN0YrnEHGiLyhDuRDjLQBw3tgPoF4T5oO6Q5NHcn-djCu6m4wth1RLsx_xPwHrO59cgSCpX_VW64g3XcCqVdAoDbly2MFYI-2ZV0zolSnyL5gbUp7h1_7xn1wxqCKNi2jTV3CZt7J1KX3vgHbuRW2sX2-gEFJNHYSdIC0ZcgHSaWjARGIoI4k2UOcPMNDi8VMXtW_heJhsHghcQdQCtqCy3vViWWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0gg8LJ1AWReDaVYsLIykJmNsxiWIZed7Ur0owc1In3w8sciUSpzg9aOOqZkTlSqZZIb0FgV9UQaXJUbpccq2mBLozO3PTz6PBzUK17VQClWtnppDETADrj42CywAARoULzzfwjj5MKa46oxeiAL6zSNY_7MydMOdEAC39JF_qTPAuwU3lzx_gwx-NB47SV1AywysoIIfM74UiaTei8xR5BCeHQErV7ZL9xI7rxCa_aa6LD9EgydPDo7VtxZsK3ngpx8nAaL-T_KP2zJcWiiiKw4NmqdoNmGdCY6QCWv7KjYx16m6LbcSwOhafq-z-2kqgj_hLvn8yXKBN7xoG09sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3iI6d4VnFOisVyWCDobZi5ltepeN1S8gcP5IGirwGTFQ7kIdxrjdodJwWFPFWLVss3lSj5PDqxC4-kwXKwqJ5BMSt0iGcCM1teFsYeYasEY-01H2yD8l62Qvo2ifnpf6HJkXtCvjL5RraOgvsuYw11gdpbKeISmqwCR6sEacwCY8RpjNjQSUV5dfkgoTmx9YXD3ZLnJNd_yRsxL4ObTy53SJ1zifY_ZdGIQ7e7XVpPOZ_XVqqwgMj_RgVts3fzgrcM315aZEEuLBoezp2dmo13ESPUqk3H5RUAz5UfV2W4ixJvzx40V4Vk20MARIKtGvNhWy0Pvta2yD6sBTqJbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=tBzwVmMtVw298C8Jld07aTaUfVQ1jG74F9s9VCYiTjhoEDLScKGvfYuliP9i_qFzDKqQJoKM5Ar4EmLhTRkd_3-WvX_RxWswGLTZpxEdzJzbhpLQP8tA_ym1C5uIQHDXc0i6EzvxHMV1ThcvFnPgSCOist-YXOLNdPKnRzW2FnI-b1Tco35dSpeCe7N8Kz9DkEBtRbRZZ7M3MSns9z54hc-Id4KGa42JeFHTvrA8yn-o1p07FtMkEX6xQ8rIFWFU6U5uAcMeuZN1MN4J3F10RsXER20o43ll-ICWTFrwWG--q-6Xqh_R4LVKPqjpjsptZpDNzx3Dl8ev_r6Y_ES7tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=tBzwVmMtVw298C8Jld07aTaUfVQ1jG74F9s9VCYiTjhoEDLScKGvfYuliP9i_qFzDKqQJoKM5Ar4EmLhTRkd_3-WvX_RxWswGLTZpxEdzJzbhpLQP8tA_ym1C5uIQHDXc0i6EzvxHMV1ThcvFnPgSCOist-YXOLNdPKnRzW2FnI-b1Tco35dSpeCe7N8Kz9DkEBtRbRZZ7M3MSns9z54hc-Id4KGa42JeFHTvrA8yn-o1p07FtMkEX6xQ8rIFWFU6U5uAcMeuZN1MN4J3F10RsXER20o43ll-ICWTFrwWG--q-6Xqh_R4LVKPqjpjsptZpDNzx3Dl8ev_r6Y_ES7tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=SIEcFXgiVCOHwXhw8p-bOQSRRI1PeIPe2DiIzYl13GFos7bIBSE66JrFCmL2u-p0r5gqeRKtqwu_8cel0ZKtwkGs33DHQ3WYvPCZ9Qi5jkSFF_hTXk4lXsIwBY-qhhhowYDcBX2jnNLhgabdMGc3NUAzoPtqk_3XKl3cE-4JxUZy5sqNOeewHTaWwvDmfDn1CB8E2FI-TrUAoAfZRgKcSDs6faLMli2zdZ1L6HArsHdwTlw_89MiL_sBOCXHKWRUG7CgFog99gRU5IfRrO9y5cMZz1pXA2EOAkc8IPBaleaaS7X6asZBO9WlFHDiUTL2jiVYCLF6qw4o8WtD-zJGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=SIEcFXgiVCOHwXhw8p-bOQSRRI1PeIPe2DiIzYl13GFos7bIBSE66JrFCmL2u-p0r5gqeRKtqwu_8cel0ZKtwkGs33DHQ3WYvPCZ9Qi5jkSFF_hTXk4lXsIwBY-qhhhowYDcBX2jnNLhgabdMGc3NUAzoPtqk_3XKl3cE-4JxUZy5sqNOeewHTaWwvDmfDn1CB8E2FI-TrUAoAfZRgKcSDs6faLMli2zdZ1L6HArsHdwTlw_89MiL_sBOCXHKWRUG7CgFog99gRU5IfRrO9y5cMZz1pXA2EOAkc8IPBaleaaS7X6asZBO9WlFHDiUTL2jiVYCLF6qw4o8WtD-zJGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd2VTzyD1AhzVlUxfx-Z1h0P66K3SC_Tgj3WO6Zfif5thZJSumJVn8qL0qL3-zPBWYnQIbLQtRanX_iOHH118kRQJxykJl86LRaoXzA9VOtgrtisgl-XQ7kvENyErNfIOMjZQ1NiIXmrYbb4XNv3vLKQhl1grS_QOQmWbZlFHojRWKcPDs76sL_DTR8Dh0YzX7nUK5inNnpx1NbTsCEqYH2Yb2uJUuPGUPOalWSUFI-QcmBxCL53Vc7I1RtkUdeDzrzGU6eQnqhyyqn7PC9LRN1Rl7QP0KINegMJ2LdJGhbzc20shWoZYQm7-YEEldE9awh1g9qcJOZzBIcDYRxWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=st1-r5x1s_T3ND1QjQVBhrIHG6nGQ2yKuXaYAUJywYOQ6ZbJ8Ar17VxZIQ2rUmWVr4rJOBbQwBum3gk6GO3HfLUwOzsRaYQhUm8h23QMmMGLIUcsmoZpwWtYyQUKKpZmZPqXwcHLKaHf6Kcp2e3dJTO2P3JX0fy5GHt-lrfswIxpNUdjfutRWIf2OpCQ53vmaSlf2At3rzHg38WjKi4VKVDVdiliVqR8Lg7ShEwbxI1w70qqwuZt-behFOmMxVuCONUeT-jnwPzxYk13d8xncXZkPa7cJqR8IroYUwDh6az6tm9uF-l8Tm46SRusWsM1WVy4S9GAE5EnMKgrWiClXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=st1-r5x1s_T3ND1QjQVBhrIHG6nGQ2yKuXaYAUJywYOQ6ZbJ8Ar17VxZIQ2rUmWVr4rJOBbQwBum3gk6GO3HfLUwOzsRaYQhUm8h23QMmMGLIUcsmoZpwWtYyQUKKpZmZPqXwcHLKaHf6Kcp2e3dJTO2P3JX0fy5GHt-lrfswIxpNUdjfutRWIf2OpCQ53vmaSlf2At3rzHg38WjKi4VKVDVdiliVqR8Lg7ShEwbxI1w70qqwuZt-behFOmMxVuCONUeT-jnwPzxYk13d8xncXZkPa7cJqR8IroYUwDh6az6tm9uF-l8Tm46SRusWsM1WVy4S9GAE5EnMKgrWiClXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPgB5haqO1bOwNYpZ1s1Rxynsvz0FRhQlZeMa6jBfONd48KRe6ScSGzVOVrPFoatF9eCFSzxEL2S1K0I3w1fiQMduKMcd2slybgSRtNbPbK6JG088k7lK1QHqxL7YgAMqR9SZe6hp17x7KzHvmm8KnxNpBWJgbmjgfQs1Nx10IW2MIB2vUyBEAynZmyyky2uESNrVzyQJiCmXEGVpAqw7K7bcnTBJjzAFMt7ZzSkTQTkB935PaxeG9Ho6dgBnz8Mt1we3nLFV5z808OTsKfWETUlyuZQBUcPSlwx5I6lOnWk3tYj4-L7gxeTkb7coWXwoMLvXHZY8irbz5342O7-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sad4O0zw0PJ_iYaQisVGGYAVdlS6CIHP2ritECTg0gH3pNNDs_x3Od7rzVaB3DXOhjfwfooGp7ydwJxqJP5GpqWXuGWGYWoe2JG1eSjzLEi-nnzUn0chNNuNwFKiUqXr_MUZxi5j8Jr_C3VeqbcVBOLCGLyZoA8jxkE38LbG9RZJGr5cXrVoECJHUXcL-Jb6NBGhRfE9sTzRUQ3d1VZghW8ClC6f3uRqawbrfDtBcnXYQBrIax9n5L8zt7en_rdF8dDgD70yWuicOdh1e_esf1Z82ToJE-aMjoo4M4dKvtkDuovQi3dPeWkcfvfkgd60CyKb4UEM4ooJVJANXD2spQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=CBq6kQzHdn5CcRfko1i02QzbWbXz-TRKuEqjwWp85XF89Xl6tmH-ymQvhrT_RIR-Ox0mo8F6UExo3JwFwx6QzebZ9LRBVN-mh92cJ1Fuv2Rc7FmvBxk-PI9D4Ny5BY8v1nqaBSRjRL4jCVKg2Y327Zd0MRrPMHwVFOuAoEtmEVTYIhlLa7uL80KM1Wjem8kIRSPWdVXPTkYyDqgcyne_b0uHbltp4ff3yhjD7GLCliuWqfLPS72uQK_O9CzsTPVJF8S1NpQlIZCJxy90XjO2M1hoxip_8hd-xWvGrfZAOE6UOdHi59OA0BqrOzTZkh43EVf_DnD48hIQNDj8P3V0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=CBq6kQzHdn5CcRfko1i02QzbWbXz-TRKuEqjwWp85XF89Xl6tmH-ymQvhrT_RIR-Ox0mo8F6UExo3JwFwx6QzebZ9LRBVN-mh92cJ1Fuv2Rc7FmvBxk-PI9D4Ny5BY8v1nqaBSRjRL4jCVKg2Y327Zd0MRrPMHwVFOuAoEtmEVTYIhlLa7uL80KM1Wjem8kIRSPWdVXPTkYyDqgcyne_b0uHbltp4ff3yhjD7GLCliuWqfLPS72uQK_O9CzsTPVJF8S1NpQlIZCJxy90XjO2M1hoxip_8hd-xWvGrfZAOE6UOdHi59OA0BqrOzTZkh43EVf_DnD48hIQNDj8P3V0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYWzxiF-vEglxqgu7VAgRl2cscCuksRLLteI1rMvCVYIQdYMXuuO0OFcyYsSTiLbFYYt1Em51EL80yzGST5DTbbgvmvIMZw5mECsEegwWIXgV1IhLkyghwZr8NEIjecRD7qZ4jMSh8KHPTGgPqHpovCSCjKoVCJ3P7_MveaNpO7LuKhXK5HnnivC4roZGqk4-uZIBII8N7keHmD7OgcGUhzz1u_8u3PfKDYoS6A_AUBP9JqLfs2FhP9tgcbxhUgL0x8hP3smfy8uTAfYCYggsK4L44Pws1sLiFaNbqvfjQfcD4NNpM3Q4RpoNOjCc5ljdyOxBhrVSQ7pZUehqmxVQVrxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYWzxiF-vEglxqgu7VAgRl2cscCuksRLLteI1rMvCVYIQdYMXuuO0OFcyYsSTiLbFYYt1Em51EL80yzGST5DTbbgvmvIMZw5mECsEegwWIXgV1IhLkyghwZr8NEIjecRD7qZ4jMSh8KHPTGgPqHpovCSCjKoVCJ3P7_MveaNpO7LuKhXK5HnnivC4roZGqk4-uZIBII8N7keHmD7OgcGUhzz1u_8u3PfKDYoS6A_AUBP9JqLfs2FhP9tgcbxhUgL0x8hP3smfy8uTAfYCYggsK4L44Pws1sLiFaNbqvfjQfcD4NNpM3Q4RpoNOjCc5ljdyOxBhrVSQ7pZUehqmxVQVrxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
