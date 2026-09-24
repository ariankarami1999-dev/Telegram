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
<img src="https://cdn5.telesco.pe/file/UbdZzDUhN6YrwJFWDmoS48VBAiyD__74kPyYOIB9zHvCE1N5WBCYy9QJmW8wHmYgRGpjqaK-iWB1AS_VscG_5bHWjIj32zok8JJXo3RgGKT0A5XkAPsu3YHxyQ2JlWFXljevnhF6gEExAbGf6fvaGAHS3_pGrfoarR7QqKB8GvFL9-e1GaKKMEUbW9ND2G42Vp0vsJzkuNaiTFGVQu6Re-T0MgOEBVr-zkFyx4ExjoU5dRg9NGH1sHJAt94eO6773wnZbonD1qOfQjMqQES6fUt9KtaRsmyoecZSK4Ngo6r-iZveeVb5tL9PTMtxB10lU8OEXSHAfzgCLx-TakQsxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 402K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMSNekmPkNe9-cbkgvG3unDZu78KWxMZwNrD3SrWlhgujXfpV_x8XWV28i2PPFSQ3opgU_IoNRVamPUcIj5uLyRCf0waTCM7eqZ7lfOGaPsUha3VnHVFecrpKTKn1ya4mOaY-nCbLIm7XrWBuKQsbv6TJvgbn-RbZtDUsoPEPuHWs4eCYMB0nxT67Cvwr6HKRGV_oIdb0Xz1cT6OeYmbm6b_Tv3r7MkqOhYNTmTf5zO1jrg-euF7LZyKzIG0Yec6kRWSLUufzUZxenc8Uva5A52KKcPRUqNqq4HiJqJTrvuTSDtp6mtr191ZTgPI07QWLZNDv77yib3O7ptR7zmdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyI124zXF8Li1Dua_RRfEq2fFamnI9dHxvXHCEOCjI5qKywx7FM5Rsq9UtN4orWkh0_jfOnSWrUYPoien2td0aUw-1HKDKp4J4BtveNaQTQcuM8U_5TyCOY_Tz_ENzfYfqkcGHsclyELnp4ekgcl3UqwcMMnq6HfHh0_vmbYO0VvJ0EcCEnoRlk4W7oZZBORQ4DUPvhlsyzxVkgxD4r_-O1sDljZh7Aq3mYAdk7kHp9YSv5-Tkm9ONakKoVKpv5Dq6nWMm2k9WOozZBTSZj4D0K5iIcWHRBrvGnpkKgsAnIGvkiVPMJe9gLw1ckG0l7TANt54B_qWwPPCA51yDrpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVOrQYhtvphSiFd_q8aNhcABNUtzT25_T21IbH1NLv6Zin-9Nhm4AUi5KqYcrrjbMbVv0gajDuPES99MAVf_vOrQIt-LBM9CQzF9uuY-c3lFpDzgOtgN6Tm--PuWgMRT5qijuDQQpa3qbnuRI5irNqbXMSUUR0kCp1KVphfYyOxtoMJG8kpGMPwskqM37a91w0uazEK2Ty8dnVnCuzddWQSB8uYu2g32D9JKY6IS1Uf9eVTZtS2wVaJ4nTGEspgsoEOfogu8H3YGM2dxE9l-PWv7Fnz8HmgYAyaFjAzVZ_k_iaEpTqQ9NoFCsYr0T0tHd6p1jiL35g-vRoE3ZvEJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0reSK_lgKex5d6ORxyBXlSRlq4ZXaP_0O3Aeg4wSZlRp_0Dyk9iLfV35JKt8yA9DJJgdU94VjTO8N_wRHrj8RG5RFvYerMAZNrpenNWFwJIPuMEHzF1o5fw0cEi_4Sw7m-fFDgxqocumdyGS-1l33Xvn1DOtBMbsr-HzZdxbolZGGlO_aKlt8Hn7SjQkhyJhKAqO8nRXmFnjdoESc7ykGQ15MQEI0E17os5aYFWOfV3w5fHFuItZtpJi1VuiFi1GQPk5dha2Ej2AOX21RFhbHC1SyPbOJV7clSyFNLmSis1-Xwwnwi8EWnSpV7z4UBuCHECSZP4DPaWLIFkPNVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAglttjaBE3tCxmYoWQN7yDqyDpOEwpm8dWNpBqF8CkCPmSCOWSqudyxYUaRBUhvt3LLyXUQuHTx6h5fexgr-wDKjzX9UQCVP9zw8MVegZ-HwE09bbtXhqsm8RSJWD0FqDZ_QKnWargj0WR_odxN0bPyAhjUHSYFeodiJGueU2lTsB1OU3qUPRJrSpm62IgxT9lPceseBRCsBEBSf6_EDoxJIoOucD_6KoRdotZdIvw4drCKco5pVvuqlJd6CBgwYcQ9-Dvf-09DbGqaIOgM2yfblgHaZwYSzJE2ldayR1yXH0bb0W_COZ1rZd7vYuAeSIor0j2heEEEzADcK28kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/107184" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egh-fpgP70qDOg-bmO4N5oEnOGUc589W9QOW9Zylnxlu_PyRvF7xvTUETBoPhC5751j-WmXav6ufKnx9MPfY1nFKUm2_4sIRoSTLa6jkwVY72cKB848ncusUnW_Z9qgLJABSZhELXuC60Aj_YhjzTKTza87slEMLQm5uuPl95XbKqj9xHYETaHS0O840erOz8D8UkEXpPHS3zdhqyPUIweZXihWlfHaiywGi5QmYJqBeLJwlyDxiau2lRVd32IuzOyXu2J8ldBMES7A_DYfBqHdaJojf-GdnPOWaUc3UNwcX07H6NnZCYbZ5JujJfaJnEGCvfDKj3qRkSpMooE3GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/Futball180TV/107183" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmAsgtqQ6-9x1ibRo61hJbl0d78XzWc9F90BzQtSoFDhRTeoA1m40M3u5tkxOl57sgh2VjkVb9S4XD_oRUXi5jyibnka5ZbNEUa6qx1j-5yTwje3-6YxiIUwh62ski1aRjPbzpsel5rHiUt5odlOvz0oQdIRqd3fu74_AA23nxkUxnYw7yjhGvs-qWCAJKZoNZ9_jTMFvLhLBpQYkO4_67DgYOKIR9NQmQBYs-0fNOtK5_Evvdt39w5WDAZEk9fs6I1_RSmmMWRv6_tCGLe9VVURBxrQCYOpC8TWLuqgAZNOyJpRo4QxzKKKu46XymHbhl6WIn-6X5kyet5hpm3kMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
بازی دوستانه؛
ترکیب ایران مقابل ازبکستان
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس اکرت آینسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/Futball180TV/107182" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سوال‌کنایه‌آمیز خبرنگار ازبکستانی از قلعه‌نویی بابت عملکرد ایران در جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/107181" target="_blank">📅 16:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👏
🔥
🔥
صحنه‌جالب از بازی کبدی دیروز بانوان ایران مقابل هند که واقعا محشر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107180" target="_blank">📅 15:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIwtIH63myBroea_PxGxEX56xiJ3Lcgx8Fo9F1XCIp0JA4GDR9_B05lQA_tVNfpfJwm_rQRqFa8ZsIwjpbvKZaxjY1Dq5QQft58n1kPHtrbU8IY9_HYc1yW0z80KDsN2F9qR2ELVqDHMkDZj6SBeafccYqZqqzNYW0O1Il8JUpmi1_reGjPHRNV0YH8pkg00Du_P3lHwVmGWKvhuHPOnxb7ov_t6R0OvibzVAwyQIzB8I9ahIOKWx0RCbUh44Kox2HKV3v9elmSBsnRl_VfD6NSoJ3umy7IWK8EVgVPeoMIxWPaBCIGjwzTc7RlU468RUaxeKL68RI-lEo6z4eLKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری امیرحسین قیاسی درباره لیست جدید قلعه‌نویی و عدم دعوت از مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107179" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
مروری کنیم بر ادن‌هازارد نسخه جام‌جهانی ۲۰۱۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107178" target="_blank">📅 15:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773eb10873.mp4?token=MX9nmbYAIUh1IIyFQPpn5thONrb4TguGIIsyQzAxtn_r2om-zRGXFK7a4aILlK6fR86T2aFNhbzrpygkc92bgMyoogoju1cFn_EelEoU97CXDJ6uHouiDZxJh1lvqvyFjUX7AzkhsVyXThu6BXSww0dj_w8vd6TWG2YO_Bbsp8tc3oR4EzywsjaC9T_B94UurVCZ5xjD_AIDIeRcD9DRZmIeIFKBj4vnrHN9oBA7wT3GTz3j9oya1Db_I971iLs6Lkve2ZJ1Hxpxgdb71RwpaB6cb_p69Ey5bAHzEtRqoiUfdTkhUyrw4ASUa94GLpotVvGD6jfeLoov4QvU33gUtSZJOewHA47LdarbX4qagZimHHTH5MjHn9o0vc0gF7t7FPEZXHh5CECG4XWKQBv4Muq-JESCMXizMQPPKiW0Fk-TfdvZMCfMr8wFEBJy8mO51J7u6TfXksJczVnEBmKqvNSWwddjet36aT34Ov6cikaHABwi_Dj0npGN0RuTzJfU8HIB5__pOZlkw53ckRW_u4ssWwZtJBhzCPX4jwVLvgIV8giXw9xcBHA-oysGecj0NUbt0Q5-IBw4ic6TqOvMy186HLFSgH6pJiOlVYjcvfxwMXuu8AgJ6uxrLNjT0BXyAKzKiA-SbZvyXGp7gczVjGllSKeQhCF9aBZCr1yiFIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773eb10873.mp4?token=MX9nmbYAIUh1IIyFQPpn5thONrb4TguGIIsyQzAxtn_r2om-zRGXFK7a4aILlK6fR86T2aFNhbzrpygkc92bgMyoogoju1cFn_EelEoU97CXDJ6uHouiDZxJh1lvqvyFjUX7AzkhsVyXThu6BXSww0dj_w8vd6TWG2YO_Bbsp8tc3oR4EzywsjaC9T_B94UurVCZ5xjD_AIDIeRcD9DRZmIeIFKBj4vnrHN9oBA7wT3GTz3j9oya1Db_I971iLs6Lkve2ZJ1Hxpxgdb71RwpaB6cb_p69Ey5bAHzEtRqoiUfdTkhUyrw4ASUa94GLpotVvGD6jfeLoov4QvU33gUtSZJOewHA47LdarbX4qagZimHHTH5MjHn9o0vc0gF7t7FPEZXHh5CECG4XWKQBv4Muq-JESCMXizMQPPKiW0Fk-TfdvZMCfMr8wFEBJy8mO51J7u6TfXksJczVnEBmKqvNSWwddjet36aT34Ov6cikaHABwi_Dj0npGN0RuTzJfU8HIB5__pOZlkw53ckRW_u4ssWwZtJBhzCPX4jwVLvgIV8giXw9xcBHA-oysGecj0NUbt0Q5-IBw4ic6TqOvMy186HLFSgH6pJiOlVYjcvfxwMXuu8AgJ6uxrLNjT0BXyAKzKiA-SbZvyXGp7gczVjGllSKeQhCF9aBZCr1yiFIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
۵ پاس‌فوق‌العاده بیرون‌پا از لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107177" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🐐
جوری که دیروز ژسوس سرمربی پرتغال از اسطوره فوتبال کریس‌رونالدو تعریف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107176" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_9fDMeU9m9MAIiDfVJZHTheArLCh0xoxAU0tQDUnMKbmbHyWZiE1IInGaMGeo6MAo99xUlA_4E53CXPGtVaL9y_scoqb4An3fAUQFgT2NGt_lyacX5u0qpFcKpo3BQ6Hsdc00IRzx8OSM-lv2CX52reRlA1Joa_E2pSZFjdBe0HVZQtYoYWK9S20YI3ztq4768KviJ8WvQqKqu-y4OQj1_1B_T2vr6tZle4TjpamTy7z684K5dlDrnVb7Dn8dfXtP3xgE6zYCXRGnIcwtDCNFLsDhB1JSfuCrAF2_wmNpV_BVpDWUA141mmZne0UO24XC1TN-MXiquUv2NfPooIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=p_vc_O3P8Ksl6I4xrTlMXQI7xeGQoO0da-LpWyuw42pXfSktrPRsHkEKvlUjZz7XN_KAvwGJOUcEwRbcRyb124bZ_BVpIrCW7AihHaZI5V98A-dNm3Phh_uWrqtg32v9qRcwVx2yhcHfuCsXphHrU7jVNsndFZJsOpJuIuape5C0xGL-Z89qu0HgO-OVBURAxYZx_vO4fVuUvFLq6CrhHN_PHMZu4gwkwk8_SbJwsANshO4H6jcBjdpa8UjWIR1rM4v-cjC5cEOFa3epnEsHQY9uiU801gFTC1ufwnjqBMI1WtVYJf8D5W9w0e-SQ8vmL6IpDM0Cc-2TKmP-hqGDpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=p_vc_O3P8Ksl6I4xrTlMXQI7xeGQoO0da-LpWyuw42pXfSktrPRsHkEKvlUjZz7XN_KAvwGJOUcEwRbcRyb124bZ_BVpIrCW7AihHaZI5V98A-dNm3Phh_uWrqtg32v9qRcwVx2yhcHfuCsXphHrU7jVNsndFZJsOpJuIuape5C0xGL-Z89qu0HgO-OVBURAxYZx_vO4fVuUvFLq6CrhHN_PHMZu4gwkwk8_SbJwsANshO4H6jcBjdpa8UjWIR1rM4v-cjC5cEOFa3epnEsHQY9uiU801gFTC1ufwnjqBMI1WtVYJf8D5W9w0e-SQ8vmL6IpDM0Cc-2TKmP-hqGDpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mXWq8y58JhrKD63lXjPJPXH-Lf_yG6Xv8ZY_TMcHiUFMZum5rLqkQhBORXN0IvFNWKVDj362gP1PVxwbU1VD5zuve0xmDRctGxQ1Pudnv8u90jbotsUP8PeSz_8sZ3RSqDoZM1yztIY1YHOHYAmR4NboL6WNmoHpY0du6XUDtm9KMbyzSu2uZIGhHWboa3_aM75VS4w9X2o-gac9bcrkD8RQQ12ckGyhxoBlyQa6Ri5eKaISf_tHdsuoMJtQYy4sB-gHutZEtB1c9rHNgmgIv2c6_ozlC9FMWIipnxe2YdBLWAHg6AtfGWYMQj6LztUjHfgG6Zue36x2xKcaJc2o-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mXWq8y58JhrKD63lXjPJPXH-Lf_yG6Xv8ZY_TMcHiUFMZum5rLqkQhBORXN0IvFNWKVDj362gP1PVxwbU1VD5zuve0xmDRctGxQ1Pudnv8u90jbotsUP8PeSz_8sZ3RSqDoZM1yztIY1YHOHYAmR4NboL6WNmoHpY0du6XUDtm9KMbyzSu2uZIGhHWboa3_aM75VS4w9X2o-gac9bcrkD8RQQ12ckGyhxoBlyQa6Ri5eKaISf_tHdsuoMJtQYy4sB-gHutZEtB1c9rHNgmgIv2c6_ozlC9FMWIipnxe2YdBLWAHg6AtfGWYMQj6LztUjHfgG6Zue36x2xKcaJc2o-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNT7HOpqR9hbmUK-e7y-5NbwCDm3Ooo1wRsEG-1TYvbcHEO1J1yfg6bq4PRxCiXh5kjXAzgCmI4XGhPlaFfukPcW7wx5Dop8NufAYO24ltAH7Z0raolFDxJacVzOPPC2AcaFZa1cB83VFOr4zeHA7gglFiuD60R-Z9rUeUlMiggG1zRWF3T5I45RLoA0jXa1_A7OKwgtSy6-zHq9FOl5pulIXSQmWQsqaJXsXlHLXCTofPQslyLRcXJ4Dwf9cB6Qhlro-pMfzb2q6IAHT7iBNa1WW2f7k8_8YBQK-eHcxCWwoCBhCg7M7D-0XNXWinPTX2uM96-JKzLBGh9MKijO4ZxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNT7HOpqR9hbmUK-e7y-5NbwCDm3Ooo1wRsEG-1TYvbcHEO1J1yfg6bq4PRxCiXh5kjXAzgCmI4XGhPlaFfukPcW7wx5Dop8NufAYO24ltAH7Z0raolFDxJacVzOPPC2AcaFZa1cB83VFOr4zeHA7gglFiuD60R-Z9rUeUlMiggG1zRWF3T5I45RLoA0jXa1_A7OKwgtSy6-zHq9FOl5pulIXSQmWQsqaJXsXlHLXCTofPQslyLRcXJ4Dwf9cB6Qhlro-pMfzb2q6IAHT7iBNa1WW2f7k8_8YBQK-eHcxCWwoCBhCg7M7D-0XNXWinPTX2uM96-JKzLBGh9MKijO4ZxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-ehimdCifZ0Ca3RR7ZxGEcX8Ade8_VhPq-NNcXgpKk1gvkrQfARLYt6AZSFRS1-q9j4pcqTivFdGJkh1ckgMhrzB0ManxTqC8MxifSTWEs4Lwi4HaJ_XuYUZBpMZ29QXrHwHwXKK_XfVD7pO8RM5l3CJ_GFB8rHVYbXhhOi_H0DAY9gqVP_IzX64Z9yl9DlhT-EdMuTbIFk0E0Z9fJH4T4ZSummVSglzDkiQiCLM1JWgZiVqJGqvWxw39-trxtxlmjU8SVXjhXt4MHvqQpHeM9G0kzVc9ySrYWvqifMdqj7TSBlemoA7GY_Px9Tjm1Tb33bQb02hSCRFx41mJ_a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmpyqLS2veDegP46-1rnTKlspx58bd6FkFyXyvOpPBceWM9rMVQV6qoh02XFjuh0dVgS3bd8QySgxl2463GxuO3MwmP9l_ObSPoAdNJWa8CFd8yZ0xQphadpoBYpKxzee44_Adf34OjKDisUFjEAHjZYrw-Hyvzz8omt50Tf_7tltpgW2ypjVCUqE8SVIjc9PthuYUBpIM1X-IRf3WlMmIEdBT5--RCCbx19sK4CBW2Jp3i3wqdxdM-furB4owl5VVIG4y6_uitM5Af7eJ1Hzt6JHcJZiHI1951mL3n0raptEyFXGOdJdPzA_7oa1o3rPguL_kSiiug9H1SfEKmZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwpcrcaeaXhCrY7ipgdlHZM6VRO7V027AcXIU1GAKrk90JSTfofyVAyY0MK4hd3-PwKYAR0L6WszizBmTlw0C8y0IkOH5iuzIBMAxnwMzBdiWe7OGXFnKP8Xu4FKVmwFD4F9HwmVu2wp4uZvjss-Haw_3qi3veWuPY5okFzeG-VvF4my49TemEKJakXvjjCm4EgANWErYhHSY3q7GJTrvEwgOsWMHwxFjf8SPUgI9fmqLXXj0jCqcMzcjNjbQbMXrziyld4KrItFjzTECnmJNAxb-OceFD3MrYVseHwKQYE9u7zxv39acwrG3DgYAoTtTv0cmLw9IZpUfugp2-EnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو از یک‌تئاتر با حضور مهرداد صدیقیان و فاطمه مسعودی که حواشی زیادی داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107161" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«پسر بد» در روز اول مهر الگوی دانش‌آموزان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107160" target="_blank">📅 09:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
علت‌احتمالی عدم‌دعوت قایدی به تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107159" target="_blank">📅 09:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKtX1CnBvLG75i3lVVgmubd05odZE6d2Ab2KBYMzvchu_pFwTFiV7ehd8t6EjsI_qxqA_UKTgIpyJR0r3C7-6NxN8g1OJDretzpBquLn6_k9RgohyfDnVDXJNRsNbcSdewGdyBMomK1dgQKopHBvuC41yLJqCeT3uuF8_VLsnukIrRuu6p0tdpBGv3roscLBjn_IAjLgmHpW92poBtY30inkcqqPJK3KDTkphG3V7x9f4urke3WR4mAZQKYvy5cYPDCoR-IbReYXLo3ziprnKbT8Zm9sQnSW1oAeoNuRAYpOF4ejX4lkhr-dUD7bIU_FJyTlUfTLARZrXZcN7NHX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آخرین پیراهن آدیداس برای آلمان پس از ۷۲ سال
؛ از ژانویه ۲۰۲۶ کمپانی نایک اسپانسر ژرمن‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107158" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107157" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NogNAHJ821GyP1Dbve0wQiPpYVoq-lYUDaTbHYaSXhYWznh0tG1shQy8YV4Mo6J_b--ja27dQWbV7nUI-nlLigoW4JF2Iz5pkwTw4DYadOC79MO9vl4_JxB25GcXeYunfEn6Q-KY-NZsc0D4K8ix55bk__9NjCT6r2mQddPirQ013Bes_i_7rVBn8VBJ11YJTlkKwjOgnmChzpN-ig3-W7gC41wXLkoZ2RvLYgLVa1OGjYSYyNKfwKPakY-geBU2lQAvsfGVLHqZqdq8sv9Ddf2oByV9tjvp7eYxO0RrhZQPH2nR8LYkSTgg3yN9g8o-ZtCfeqlDmQyAwMN5UTG2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107156" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E018_kEzcgc2HGTFqX1TxUxbnfEjCCOwoIw9uzyiqI7mmMPEwlvUF7HDyDeGO3iZdJKeGHKtOE2dGNbEoPtROYKbQks7CQgph7PgNqRLw359-kX_SHpyAkkdR94HjsrBBha-zQZlPvIM6rSCGVRemM_sNDI46a9GEC-47ABCiwizduN87OjgflIJij-W3qts34mhnTeCLm6WccQd-8mTJIi66h5VXL5d2MLoshhwOpID7-IwAOYIPSzN2_t0zuuCozfThlWDyerxga1iXSfgVBmLqJc6leOD_bQ7tYh3WSxCng4WkDl_ZUNDd7N9CHbmHLpEiKQijTvUW5R6BEXJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ژوآئو فلیکس: درسته امباپه و کین فصل فوتبالی خوبی رو داشتن ولی به نظرم لامین یامال خود فوتباله و کسیه که مستحق دریافت توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107155" target="_blank">📅 01:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور بجای ۱۶ مهر قرار است روز ۱۵ مهر برگزار شود. این اتفاق احتمالا بزودی از سوی سازمان‌لیگ‌ اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107154" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IswTuVo_pttjK5MubWPB0pPXHTXUyGtVxXOEZA9fdKFC5ONzm21hEQu__Mdz8nxOzDoZHk75SGjT0zzMVKLyRu-en6b5ffAMQ2X_ebtovxTAFGfpLiIR2iuy8wO9Ng4vxXcz5hMjnyuOoMTwM1e0jj_SD1ryHIj-XHGNg0VD1mnVPJ-ZVxoUrN2Uvs6kDgwEQ3kh_w5_3VTPbSexXg0G9DMtQ_ilfNcjwExazfp7DjnNv4sqFda85CXTn4he55qhVxZP7ioyF5F2DKsgXmw9iSqw261tv1OpOOXmSppkjp4zfpqhy4p8U6Uas8hGKMYe6nmSwG-jZ6DtJ0PRA8AQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دیدیه‌اندونگ بازیکن سابق استقلال در لیست خرید جواد نکونام برای تقویت تراکتور قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107153" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1cBvc3WMr7s-Vel_4SghPzCxkm-NhjU-7jVoDk2ypFsaXVvc-0_T5QcNECKLJHIjb5KncQvHasjk7Na3gokyZcuTZru4Oo_l_VIVQFB1K0lXSv4dplZuCAhm68tvsvSZeYk_VuGD03M7QqF1v0OaOjezArl2XPZlWYrEPl9B4qS4roBqf061_6SqdimH-ECJXZGZmXmfbR0ueT-C6SNwCnO8m_32diXPhkO-ctmyhX61BJDzCD5bZ8SPuyHSkfd1cLkpXxl0dHL2oihpZE1lO2AST_TPZ7WdRq230hpEEH6OUm5YTO14bifT0Lc6C_phRPac5nmIEEBdmB9D9K7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHIiUhZy5s6ZhEEOzkCZv611ej7A6KTuid1n6-6kfmOdF-MZVF0kjpy8XHVMQiXJbv-3jNa51oNxX6bb-3hBJHgm-3Cb3DhbnhYvCpjJ5ONJwiLIcu5ACEx9ZUit69ZSyKhNoDrqWi1Q0iJGeekrTM4OwJtFy3UvR6m4y3-LUDO_QrhYEdtibUYFg3gv2W9on23zwqPH0yTJfmi7FNOD1ZP5ml7L7SMlGaWh2EoPHOpnY0KfenB9JJ8E5aOaIa6kb980DNuw2DrDuCdsp3w4JTtICL21OLc2kjwXtDrPoLeOFlRSFDO3NENsBK9orQq4izn6yeBJKZcOd_2pUo3d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=JfbGazzy6ExbnLQkQsOw6AJleK4bsKzZds2ZDKhvYte8dblmpv3S6k5_2VrXbHWHv8_qy-plz4uq2JxVkW67p1OVrzESlmnT_LQrdJNLFfzn9MH_8_gelWfqJiGJ7PEOGHNrhXuH69fkXS2J9UXvKeqf_U79fBQ1e2nxoX34mSHLnZfMhHeW7McIXAAWOa1SBe0zQUtO-sEXVNKepj-7qhcWgjQya9IFPkGdUgW8-xUuEeB86qlPkjmBHJg2aqb-K1oio6CGhOmUmuzvgWtrTa4PIJMZ0csA2rkOZs8fvWG9rcqrwK-skIW9Iruhc3Z2wh0RxWrLVYNODWbChlTqhSNIqdiNyvD45NHgHmJHp-0dx4a5Pe3ef9uNcVP4tdViDeTxt0En5TGRCwUsX4Ypp7Bjuu8TSNo9Mqc3kOSF4Uc1ap2CDtm4L7v3kW8cCmZrPM25u7oEWJdfEjJvwyIx8LXjeX51WgwF7OACaAecXmLS6WPEPyGbqA1vbtZBqAAREp7uT-dHiFhgevBxyZoMEWMKaU9osAHnYi8l3MywGgGI-2Jtpg6OQnadewJALfXS1jmZ5b9QQz5MOxXuajurSG5GXtBOQSPtFkrqL2tyNYh_ZojXHuQy2WawQWzTfSfnn3xCUoVqU0NQfZ5IhpRH6FJOllLH_uZFJIzixsmZKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=JfbGazzy6ExbnLQkQsOw6AJleK4bsKzZds2ZDKhvYte8dblmpv3S6k5_2VrXbHWHv8_qy-plz4uq2JxVkW67p1OVrzESlmnT_LQrdJNLFfzn9MH_8_gelWfqJiGJ7PEOGHNrhXuH69fkXS2J9UXvKeqf_U79fBQ1e2nxoX34mSHLnZfMhHeW7McIXAAWOa1SBe0zQUtO-sEXVNKepj-7qhcWgjQya9IFPkGdUgW8-xUuEeB86qlPkjmBHJg2aqb-K1oio6CGhOmUmuzvgWtrTa4PIJMZ0csA2rkOZs8fvWG9rcqrwK-skIW9Iruhc3Z2wh0RxWrLVYNODWbChlTqhSNIqdiNyvD45NHgHmJHp-0dx4a5Pe3ef9uNcVP4tdViDeTxt0En5TGRCwUsX4Ypp7Bjuu8TSNo9Mqc3kOSF4Uc1ap2CDtm4L7v3kW8cCmZrPM25u7oEWJdfEjJvwyIx8LXjeX51WgwF7OACaAecXmLS6WPEPyGbqA1vbtZBqAAREp7uT-dHiFhgevBxyZoMEWMKaU9osAHnYi8l3MywGgGI-2Jtpg6OQnadewJALfXS1jmZ5b9QQz5MOxXuajurSG5GXtBOQSPtFkrqL2tyNYh_ZojXHuQy2WawQWzTfSfnn3xCUoVqU0NQfZ5IhpRH6FJOllLH_uZFJIzixsmZKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=CQ7TRjfrHuSLsiD1EhhaRo7pq0JEvLTPZ1yewTgeOC4RjNsSpTGYat2cv9bPC4iDLZhodAn_cnrKhr5PUNR-iHjLHnxdgFW06MW3tCz3n88F_1objD1T5IFKJi4aNZp_-KeFvbWIcDcGBvHZ-xV6A1zf3Zmf69SCwtPElx0ivG-B7SI-TTkPlH1OHnGn1XE5svqjnkjhqjM7nnOqGOOtxNKp0SSWmJll-nS4dDDFxWFCOodG0ivVJde637fxzQt-StkteFQCO5q4CtvhK0POzJ2pCuciM71nUFI-t3-IokM2HHtDbPtMwBXK2xcNkC35c3dqA-oexGieTo8IdxeGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=CQ7TRjfrHuSLsiD1EhhaRo7pq0JEvLTPZ1yewTgeOC4RjNsSpTGYat2cv9bPC4iDLZhodAn_cnrKhr5PUNR-iHjLHnxdgFW06MW3tCz3n88F_1objD1T5IFKJi4aNZp_-KeFvbWIcDcGBvHZ-xV6A1zf3Zmf69SCwtPElx0ivG-B7SI-TTkPlH1OHnGn1XE5svqjnkjhqjM7nnOqGOOtxNKp0SSWmJll-nS4dDDFxWFCOodG0ivVJde637fxzQt-StkteFQCO5q4CtvhK0POzJ2pCuciM71nUFI-t3-IokM2HHtDbPtMwBXK2xcNkC35c3dqA-oexGieTo8IdxeGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107146" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD5yRxuy1tLOkxa-zMyYeG4pDiqGGk3a84XCCG9zFRFepP1UDmOlerM9HX7MSFZ3LFq3CMEWVTFlvCI-bIz_V6oPRhkknAStH_Rdt-vaRIsEzKQe6dKE8xq4hIjQt6VA9ZM2iL2LA4T1uaT4YQsNXnkth-bAVbCkPyQlVl1lIGbvJ1pxbTxDBC75IV8FpunPZmUXHtzbK5O-vJzk1_Wbn7n2YxMzWkbaGUea_Ba4rLkw06Dljbm3Tcoaz5HpcNy9-RpCpzBWQnQQ4pgn3rSjax1pI9jCHELXo5fSjE1dGMu5kXX3Ow8IRlX71TZAjX0_CeYXfYJWxgAPMEVnP4jCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107145" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=lsx4jF_7dgvmrqO3W2mBD03yAnfy2djfuY3-63mf0R4ASwR7PxLFBooJs-gCXDB-vfbYBRwqFYw_xzeV7LWPR2WLTgl1iTJSVVV5e0GrR7ZO8DfV5IQ2zOGrtQ69snq-hHWOA_IiYlFqLaf23_TPmFE2HRblKpNv9CX1SojB1RnGrDurWf-C1xhhcHNePAOj2M7Gtzltqfs_Yopnh3H7JicttzhnvBoEkC8lbiVg_5CefvftlzbfL-Z45pFc0zyFI1BgNZH97F5xGKNzTqhd27sksKOyqV5jqEyQ5q0wIbxDqMASJhMUsWgrbZZiKlY4P9vGcBATTh9GaLmIwvoXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=lsx4jF_7dgvmrqO3W2mBD03yAnfy2djfuY3-63mf0R4ASwR7PxLFBooJs-gCXDB-vfbYBRwqFYw_xzeV7LWPR2WLTgl1iTJSVVV5e0GrR7ZO8DfV5IQ2zOGrtQ69snq-hHWOA_IiYlFqLaf23_TPmFE2HRblKpNv9CX1SojB1RnGrDurWf-C1xhhcHNePAOj2M7Gtzltqfs_Yopnh3H7JicttzhnvBoEkC8lbiVg_5CefvftlzbfL-Z45pFc0zyFI1BgNZH97F5xGKNzTqhd27sksKOyqV5jqEyQ5q0wIbxDqMASJhMUsWgrbZZiKlY4P9vGcBATTh9GaLmIwvoXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=qPShpYnFqKThB108EoRPWroXX2LAKszgGSLkMj7ztgTaIk8ve8iEKzOsRQFnMErSKPika9PNjtyNJQzXZtIi1PH6IFsWhewCaAdbuNguxlt7Opp09ubkPFS4ckDVddPTryp-lJzPsM3pPYJZ5x7T1jXqw-EauFlB2Ccvebrwk9mVCVhO2GZHQR_XZK_czc5gleXtZMPTgbsy47CyeY-yu0Aa9JMqzAk4rj4jdNtJxsFGOFr-oNdEKrlDP6f_0SthA2vPtdAMtL_8p6k1LVyZdgbhrZzKSxx6c2hLbS92VaJsgtkrGMoLKW5pFvejwWS40EmN5srbguD_fVMpl4NsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=qPShpYnFqKThB108EoRPWroXX2LAKszgGSLkMj7ztgTaIk8ve8iEKzOsRQFnMErSKPika9PNjtyNJQzXZtIi1PH6IFsWhewCaAdbuNguxlt7Opp09ubkPFS4ckDVddPTryp-lJzPsM3pPYJZ5x7T1jXqw-EauFlB2Ccvebrwk9mVCVhO2GZHQR_XZK_czc5gleXtZMPTgbsy47CyeY-yu0Aa9JMqzAk4rj4jdNtJxsFGOFr-oNdEKrlDP6f_0SthA2vPtdAMtL_8p6k1LVyZdgbhrZzKSxx6c2hLbS92VaJsgtkrGMoLKW5pFvejwWS40EmN5srbguD_fVMpl4NsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv5qPfpXYmZ56fZ65z29UDR42wr_aicDtxCguS-8sO8m9eEHcENjSH1NPicdyefo9DuQWXgWUGmTpMlQNJ0gaVDKYaJcsUXy20Tj4K3zRjRslbSydMW0Lm3T4xa2yKo5SAvYKAEFjxbr906yHBgRhFJmtn7-E-0p1Dmx4NuKf24yMzy7ds1j2D7daK0JB6ZRw0h5dB51R5s_trUqrAsVDo35dpvOi-U-ImWAc3jsulw6lWCg49nNmacAbShsfbi32STXpU4k2OOsnFJBVzYGLIC74SQKqaElHeEMDOJrxx9PffO-OaObfziFMi-8sHyRYcY87Lx6F-86QNlIPAIHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rf0CN7LLi2rjPYbgJHch2stG1Mv164YzK7R7ttAcEDf-P9w1FBD9X-0Rgxk-9G3m-IE6JBJ_uQ5tphOcZBAXOeoLvJ2sb-Ae3zUVMRJuJzy7lBCPTt9bWiX0wFWRYErkkiVWEyC6cKVmS35pD5YAl-RoY6N0pzUftwUB3qK58WnaMbCzL6uUDDmU4No6cdtQjkxzoKTpP14A5_nKOwz2ru5yvBZOJ97LiN-rg6p1xMnBEQQIT1cicrChQctU36GI6hkyqoucikQhQ4bD3sv-6ky3lZw3A4u6oNgFXe0drOd4S8gsqUdI8p-8VvS-U1gOHGUHbzMcJXN1HJWJILQjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=FEsqYirGAhZb6EtxqAgf6DexKf8YRIxeppY8zRTk4ebTN5-uJ_NQr_Hp8aNHPZOHbWzHuj5RwOW9b68ev7O0bQN0egwl8Pwd44spbeCpSLiL87B2JqRk-IIHXAr8Tz4kgknmNlpML9rD3YaRG6Vrr686RwKoDh8j8_lYQuYqNpNfT49K8E77sLna10yyhCtFyMTBDfJtOLNxL5BCl2ZB-jakVEO1duz2rn91-5aYgTXoA_9gVbOxfgbmKlvUG2mwmJTdFJ_b4PQBiSFLm1aapU9c5X_EKrv3wjDeQIBwQp-j2KaJtGsMpFtUKe4GMC_Cl6zLuQjkj47CBYkwDiAb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=FEsqYirGAhZb6EtxqAgf6DexKf8YRIxeppY8zRTk4ebTN5-uJ_NQr_Hp8aNHPZOHbWzHuj5RwOW9b68ev7O0bQN0egwl8Pwd44spbeCpSLiL87B2JqRk-IIHXAr8Tz4kgknmNlpML9rD3YaRG6Vrr686RwKoDh8j8_lYQuYqNpNfT49K8E77sLna10yyhCtFyMTBDfJtOLNxL5BCl2ZB-jakVEO1duz2rn91-5aYgTXoA_9gVbOxfgbmKlvUG2mwmJTdFJ_b4PQBiSFLm1aapU9c5X_EKrv3wjDeQIBwQp-j2KaJtGsMpFtUKe4GMC_Cl6zLuQjkj47CBYkwDiAb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=ENS9EQQce3obC84GnJbBNJjR1iJLtqAHb3ByLNzMpMOhLQVgJ54BDyQvQU37xOsmeXHzsMUzjeLZ99_XVpTV9ftuxbmf0GLw9rdvPK50UnEZFL6pL6HQ6acQpkWuzjkNdwZxI2gasujsPy5JGj_guCPN6fenYKoOisw82wtvk36ig3W6uSNsewjDHbLik2QzvsckZY1j1lRoJwlhJjP4AvKiO1m6I1LkjiB5II5_mjgSVQAknyhivQJrZaG3Pp4GfyRuIZeF5QMwkKWJRm3XbWJGZDYvNg231jBfNWjun8XsyTVXmqD9EIIL-TPMWpapOnA_YRREDDOn8TlUpHkzsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=ENS9EQQce3obC84GnJbBNJjR1iJLtqAHb3ByLNzMpMOhLQVgJ54BDyQvQU37xOsmeXHzsMUzjeLZ99_XVpTV9ftuxbmf0GLw9rdvPK50UnEZFL6pL6HQ6acQpkWuzjkNdwZxI2gasujsPy5JGj_guCPN6fenYKoOisw82wtvk36ig3W6uSNsewjDHbLik2QzvsckZY1j1lRoJwlhJjP4AvKiO1m6I1LkjiB5II5_mjgSVQAknyhivQJrZaG3Pp4GfyRuIZeF5QMwkKWJRm3XbWJGZDYvNg231jBfNWjun8XsyTVXmqD9EIIL-TPMWpapOnA_YRREDDOn8TlUpHkzsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=Y6AWMRlaR4VXenqLw8BZmYrfcQM3_JMJoC_QeWkLlmzPjb_upgWr8EroSlaAhHn7OK80n4ATqsygJiMZRdiMmL0YAaJzVhZaneaB4fWgwLSbFn1Qo3UVbLJVE8A1r4gSgIjfiG3OTGER2aehxPUZ8wfCgGzsyPzbYJFT5WbU2bWWF8mDnYNf56ya_yt63voc5tYLuf3lFpF7AG2aUwioB-aWxw-i2hKTblD0EVC7S4c2XyqAG6uROAm8CNXfhcSmBvaAIZ0hrMT_aLUgXXXN7hGue7BWtSzfR7-fkjzfioWX1qv7UvRi7fq58zOq6XC62BIekfjMZfEmq0z_gkrOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=Y6AWMRlaR4VXenqLw8BZmYrfcQM3_JMJoC_QeWkLlmzPjb_upgWr8EroSlaAhHn7OK80n4ATqsygJiMZRdiMmL0YAaJzVhZaneaB4fWgwLSbFn1Qo3UVbLJVE8A1r4gSgIjfiG3OTGER2aehxPUZ8wfCgGzsyPzbYJFT5WbU2bWWF8mDnYNf56ya_yt63voc5tYLuf3lFpF7AG2aUwioB-aWxw-i2hKTblD0EVC7S4c2XyqAG6uROAm8CNXfhcSmBvaAIZ0hrMT_aLUgXXXN7hGue7BWtSzfR7-fkjzfioWX1qv7UvRi7fq58zOq6XC62BIekfjMZfEmq0z_gkrOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=ocbuzyLIAFNGTVillhqKoj6RqIa2nNXdS7Og0jdQGQ9AOtwJyya_4SDzg9GjuhZ09w80rE5juNk2iCkgF3TGmJIXQZtqAyCeFgekELztazt8OMUEnFxk6k1793YvmcmkVQ-qqpEGc1w0n8ECDoOrYuOso6KzAsNw1PLh3zj8q6ce3DgwRGE8hK2KxsoRLX21VWFb732OpFpK5jGydSnQSYUL1ZsNaa08ULQZxB7fhOk30NZODe3ucUk69sPhr2ZxYkEnUtyJL2g9dcGntrOLp97lrLpdXl8fHe0Uv3RyKTzpTs2VLKrPWF3-y3QrxWBiMxKo0CNxgM4SKkgly_bfxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=ocbuzyLIAFNGTVillhqKoj6RqIa2nNXdS7Og0jdQGQ9AOtwJyya_4SDzg9GjuhZ09w80rE5juNk2iCkgF3TGmJIXQZtqAyCeFgekELztazt8OMUEnFxk6k1793YvmcmkVQ-qqpEGc1w0n8ECDoOrYuOso6KzAsNw1PLh3zj8q6ce3DgwRGE8hK2KxsoRLX21VWFb732OpFpK5jGydSnQSYUL1ZsNaa08ULQZxB7fhOk30NZODe3ucUk69sPhr2ZxYkEnUtyJL2g9dcGntrOLp97lrLpdXl8fHe0Uv3RyKTzpTs2VLKrPWF3-y3QrxWBiMxKo0CNxgM4SKkgly_bfxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=XCRUkGnyEoql-0k2SOsjDvxAi6azzqSecOQMAoSBAYv0F2EKtjHx3ZohrgspFLtJXm8pihMNIyT9XGP7abOJ7ojKZu8MZcrrkbaYCsfeLkIEfN952c8Wi6pObc9whHqhXr5ossjOJoSRGnQOTi5jY--NUn0vAVJC3EAryaGCzGEpXZFScevoDasi47EQF_KF0ar38jYZ8M-IpYQZUzNh4I_Xc38ZQ5lI1DN4tloBD0Mr0H0H4P9xQSnPh6fTZQCFOP98gVoCeGdCZg1ONW8dSvsnaFH8zKiM7YYCFIiNxNrCJUEPTbGJfr6y9--qPtIgjmLg9jXUTyJIwEZ0lIZjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=XCRUkGnyEoql-0k2SOsjDvxAi6azzqSecOQMAoSBAYv0F2EKtjHx3ZohrgspFLtJXm8pihMNIyT9XGP7abOJ7ojKZu8MZcrrkbaYCsfeLkIEfN952c8Wi6pObc9whHqhXr5ossjOJoSRGnQOTi5jY--NUn0vAVJC3EAryaGCzGEpXZFScevoDasi47EQF_KF0ar38jYZ8M-IpYQZUzNh4I_Xc38ZQ5lI1DN4tloBD0Mr0H0H4P9xQSnPh6fTZQCFOP98gVoCeGdCZg1ONW8dSvsnaFH8zKiM7YYCFIiNxNrCJUEPTbGJfr6y9--qPtIgjmLg9jXUTyJIwEZ0lIZjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaP8rcJrw2oJVZP9Dq7Ydu9LPQOHNlTcTuX2squPu-ZdfNZILi06I4-TeewfxZOpe0cZ8aHtZcJHS0sgISfBifV1VG3K-vDFjiE-1l4IIHEFwD9HiPcHB09YbaumcwdcfdJDSlh5ZNz2yBFSAzX18e07bS87_N2C4Tv51nPvBB8dKe6xRiA2HAkYaCNWgNF2DsnMYZaIoOAt9xpTFNHRr9kdZC9tk0vS6rnE1XzfeOWSmxwzlmLjZ1pYzT0wZ-4j7xeRKwOam9gOVoPOtgKzrhqeDW8Ln2DGvzBsdbeZI7GebPdUHkBC0H9s_Z9BzUprwleC365JloLm3J9-wQAAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=mL-z62pBA-CFQ9SnxuYr7LclT5Ytu5E7ptA0KSz08CQ5xU5dNl0HPQJ7sKtz9lPBXu9sszjnUZr51amt0pf7fc4q1RTmaBh6gx8qbLFqNMPr1D8Wn5Hwo_zKQfFnYUF6MxxID1X-OohWrErqk5fiV77EgaWlyaxPRHK7uhAfUgWkLBuh7N_7LAsTBMwtgs3WYdFEfnB0H_eUMEXJvkk-rn04ADjkCelmfjs_KRacb1gs9R1WPmd3LCSEX-vRCH-ye2PPgb7ZKdoYNXmI1A7SO0XqRrP_gX3r3WmjoNfPOtogw8fBjIbx2S6ARpgH8Fi0yeQTVRO_LB2895dhcO5qKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=mL-z62pBA-CFQ9SnxuYr7LclT5Ytu5E7ptA0KSz08CQ5xU5dNl0HPQJ7sKtz9lPBXu9sszjnUZr51amt0pf7fc4q1RTmaBh6gx8qbLFqNMPr1D8Wn5Hwo_zKQfFnYUF6MxxID1X-OohWrErqk5fiV77EgaWlyaxPRHK7uhAfUgWkLBuh7N_7LAsTBMwtgs3WYdFEfnB0H_eUMEXJvkk-rn04ADjkCelmfjs_KRacb1gs9R1WPmd3LCSEX-vRCH-ye2PPgb7ZKdoYNXmI1A7SO0XqRrP_gX3r3WmjoNfPOtogw8fBjIbx2S6ARpgH8Fi0yeQTVRO_LB2895dhcO5qKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107130" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5mDLioHVXDa5sJYuLS5DHjK-7gVr6woeaY61O71I7yio2ViLWGLQtUMIlLT9MYHKhwCY49hAmyH4IRYgu-Ag2j8Eh634K1YtkGm_6JViLmm1N52ZJyirfHFbKvRrwrU6BF0xCysAiHSD5q4WLAvgrT-bR8FGCNID1ysIB0DuvskRvjPR351bnXoi0iEACOO9pGk8548YcGwJ4IhesGVCQnR5Hvd9lnxyfjaHTS-YdmRSO0DWv3HZdcEQiZqa19MI50ziiDZYBqTuZC7i_R9aQdU207Kw8lQHIhTtKEZ7QWAcwap99S6HSZcy29XeMLWcLggd9b3DegvLOoLCZ7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107129" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hDkrbFic-sgntXShjcbFuwYZK7sMsLt7QKTEi_PBpSI4egYdYJjV_-JcYh-Zpry5m1kwlshdl_sQZXbMaZFiysihx00TpbAJHJw6Jbs5tPVR3eOGT7YqgvYdKcARIHHl9yRBE7N9Bxfpkvj8EIXmRFKRbXErwfSJrk0d1ttZ70v60k5JzkBgK-dhvh8ZxYmw_5jcN6orNEpRy2GFDPpm24mkpeH72Aytc8-ck1IBwO-XrSgetF2qZUhc_Ykn6Prr-Usytpw7Y3xe6kghLU3NcPPyr08Me7gziOFrSAwCbCRlCl9nn3uk7NiQ7nyfo6eu0sG8zWOXV3sTrLOsjXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScxbbiUVXypw0CJBXFC5PRKGWn2B6bW4AFPVuzTqQxLUwMw7gqBPtt3DQQl0TQGVAPT6bqJiHFNC4u4HQi2O6znrGzfwrNasuCedEZ21mkcbt-xt6YXyQst31Wg9CZUIN1i8Ua4mTbJOewj2i9X3mKulNZWZZYDK6rLuU6vYAwfJt5g5ym01V8qXUE8brF9yEF8BvKeT-ptm_Xq3xAHFf0_YxU0LZj2Yrc4lUGP8HaN1K-ZrctZoCtWbpSF_glt8lpktmK_M9qmZF27NVRQWry85QcXnrFbpzyMJzNgHZn2zEZxPSWlxMBrEw1XHdHmVYix5w9QJs5Hi7LIseLD_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF9GP3EG01UGfTH59sAus8lbyADLEiWW0B5wNod2flPJyZs1mv9a0caPMfh_c7MbrX_COMES8DnqeZTjoiGXBplw5QmQol2WuQ4-cgJd26Nf-a4AfVIQzx0g7VsQCV7b9235_62R0UiCrTcOaBqvDqaSzO8Wj2MAikt-zWznoeb44QEdCpJrFKY82gk-5X17tpxg6XW1kNZw612kmUO5OI8TyL-TRQ-Jqh1OsJX3nb8uDQSAzsuCTvwdpYihXJWA16aWa-evOmL6aBAKclJD7jinji4ATBEqiaULWzd73GeT3b5FWpbYPdzWR28DPQYt6AcO6cRtwT1SZ5P3Rk8sug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=SN6uuCqPZE39o-rA93QsDjj6E_6G4Cd9PqUebS1KMB-qBtXpVIFoSdhfaD5YQot0kK921_Z6e9HHNmSqnA7exiI5CBr2fWxROL7hIwWDA8Ll8v7yqIaid8Lis4WIM-Gpgjhr1ql_gfkD-5134dcqnNdM8g0LQmS2OSl23uXL7hT4DIBJCQIxXKiinH78i2UCm2Hi00QhcgjCbL2EfTvCLXXjo0cojwJzO0xX9ANzOlRl6YVgVYdWx8RprOUKug5aEQE9dmYcs-hiAuQfdl7RgwmUESk_vVVQDkwTSUrWje0wzc8EePLZW2DVe3yT5s-Ml_bGeZTnGD2YpCAsauBz668fL7uQbkYgEXjxEinXan88p7rmzGdssGGehaYNPOtiV3e_3LonfHkMSIMA5ryqomD5TfmmWv3Z_hGyep9GJ6NPzk-Dn9u6uL81D0HiiP2XG9upC_kJLFVydYUUaKF64nxBO57lSvaDQs91HHDWtKuH7nJxW29ZuZaOstSxjQclJTeHkQ_62pECLWK5d39Yf6UXXIjpJnlHkmvqhAB2mzZy5qBHwXeh5zgo20m_5Y-jSySe7CkchSyBxP29mWvd-BB1MLeKT_ptIVPTYD9pR7N-B8g-vMuzZ946J_gNsOv4HpLsDEFMFH9IpGUwwG75IhORvK6M4w2T0OAfZeISYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=SN6uuCqPZE39o-rA93QsDjj6E_6G4Cd9PqUebS1KMB-qBtXpVIFoSdhfaD5YQot0kK921_Z6e9HHNmSqnA7exiI5CBr2fWxROL7hIwWDA8Ll8v7yqIaid8Lis4WIM-Gpgjhr1ql_gfkD-5134dcqnNdM8g0LQmS2OSl23uXL7hT4DIBJCQIxXKiinH78i2UCm2Hi00QhcgjCbL2EfTvCLXXjo0cojwJzO0xX9ANzOlRl6YVgVYdWx8RprOUKug5aEQE9dmYcs-hiAuQfdl7RgwmUESk_vVVQDkwTSUrWje0wzc8EePLZW2DVe3yT5s-Ml_bGeZTnGD2YpCAsauBz668fL7uQbkYgEXjxEinXan88p7rmzGdssGGehaYNPOtiV3e_3LonfHkMSIMA5ryqomD5TfmmWv3Z_hGyep9GJ6NPzk-Dn9u6uL81D0HiiP2XG9upC_kJLFVydYUUaKF64nxBO57lSvaDQs91HHDWtKuH7nJxW29ZuZaOstSxjQclJTeHkQ_62pECLWK5d39Yf6UXXIjpJnlHkmvqhAB2mzZy5qBHwXeh5zgo20m_5Y-jSySe7CkchSyBxP29mWvd-BB1MLeKT_ptIVPTYD9pR7N-B8g-vMuzZ946J_gNsOv4HpLsDEFMFH9IpGUwwG75IhORvK6M4w2T0OAfZeISYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=Q4HfPd4zB7dg5jWX6pReY_b4VOG5SaHWrxxzkZ4n_L7I3tt_NYp2ckrgdis4Eu2KP5mj8xys4a-OnzE1-vZsjW-3H66qjF8Ym3woqlNIOXpSsdQs1XF2XN4VmpfNCDDFJxYdF--l3N86N-qbcPwuErrYBI5tv6tvsmh8Jsxn8utR2dJ7HkkmFEuOIJIMtZJU38WTj3JfK-gy8TCmxfe389C6YXk1Gzc87ilIrmMqGNjQ7HI6cY04TuY7ZBLjmIRt-9ryfcwH8GDxnHaKcSAbnDJ45W9PtCACkb_xFYrCl0Wt48wVW-3gwEwpGxO741uzAFm5IqXQbqR1eRltczeLAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=Q4HfPd4zB7dg5jWX6pReY_b4VOG5SaHWrxxzkZ4n_L7I3tt_NYp2ckrgdis4Eu2KP5mj8xys4a-OnzE1-vZsjW-3H66qjF8Ym3woqlNIOXpSsdQs1XF2XN4VmpfNCDDFJxYdF--l3N86N-qbcPwuErrYBI5tv6tvsmh8Jsxn8utR2dJ7HkkmFEuOIJIMtZJU38WTj3JfK-gy8TCmxfe389C6YXk1Gzc87ilIrmMqGNjQ7HI6cY04TuY7ZBLjmIRt-9ryfcwH8GDxnHaKcSAbnDJ45W9PtCACkb_xFYrCl0Wt48wVW-3gwEwpGxO741uzAFm5IqXQbqR1eRltczeLAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=UOTHoinQczL5d8EyTwBd7sB0ajMXr-LEiyaoKYgjTC9YfV0T350GAgIjlNi8ucdrzqCKk3cnClDhtrkiocnYhd6wQbFxW9mojd6FHLx6Y9IyrEKPvAi_tdEGOw6QKWo9535vSkYloPp3au0LdJwLQQGEWM8A56C9HBWpPkBNfxXi795YQQI5DZ7x_RQQ93WS2aJYriwLM49MqchuTE_atb9XqI5c7gW5QTyPxKYIUE0-D06QjMYOXHlIYeZOcZJ26tAldnJn9vkXgjymws8dMtU94pxlE_6eXaIy0rggxrPxQNiAICz52OYHt-b1hpeGr0CH2vDFe8S_88E46JL5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=UOTHoinQczL5d8EyTwBd7sB0ajMXr-LEiyaoKYgjTC9YfV0T350GAgIjlNi8ucdrzqCKk3cnClDhtrkiocnYhd6wQbFxW9mojd6FHLx6Y9IyrEKPvAi_tdEGOw6QKWo9535vSkYloPp3au0LdJwLQQGEWM8A56C9HBWpPkBNfxXi795YQQI5DZ7x_RQQ93WS2aJYriwLM49MqchuTE_atb9XqI5c7gW5QTyPxKYIUE0-D06QjMYOXHlIYeZOcZJ26tAldnJn9vkXgjymws8dMtU94pxlE_6eXaIy0rggxrPxQNiAICz52OYHt-b1hpeGr0CH2vDFe8S_88E46JL5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=O_yxsixbg7ixLoGrPwFJfRLp4mXwpgd28a4bzPTXVuYXTRgrEgUAXgPvzNTYzjsN7_tvKphrNd_FcZpgH1cHt57uzpEO8LaMRvwZsMXx5Ay5e_yrPVyUfby8ad3nlGcj237dnPjR-KWZ1ndB7vyiPLot2Ts2uKJjO1JNTrNRXURRKDWOSqof3F3GpRuwXM1-nxkuGK0z9caaSIvQ9cwQ2BkrQJ77Aw9gLvU_CFatovH2rba9mvYsqooS3rZ4Wl9S2UYf58T5yWNCDAF_iEBzDFktKWFMCueMzzG1bpqsCwibRbTWe0EexY9-cHE8RuTCi_aoXcpDqlH62nTcbivWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=O_yxsixbg7ixLoGrPwFJfRLp4mXwpgd28a4bzPTXVuYXTRgrEgUAXgPvzNTYzjsN7_tvKphrNd_FcZpgH1cHt57uzpEO8LaMRvwZsMXx5Ay5e_yrPVyUfby8ad3nlGcj237dnPjR-KWZ1ndB7vyiPLot2Ts2uKJjO1JNTrNRXURRKDWOSqof3F3GpRuwXM1-nxkuGK0z9caaSIvQ9cwQ2BkrQJ77Aw9gLvU_CFatovH2rba9mvYsqooS3rZ4Wl9S2UYf58T5yWNCDAF_iEBzDFktKWFMCueMzzG1bpqsCwibRbTWe0EexY9-cHE8RuTCi_aoXcpDqlH62nTcbivWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=PY1DxxOVjDTMfS_5dZN5twMQ9J9G4fm0bW9ZRW8WbHc5qYz7C-cN0NGAvkPcdD_OjSNj5oanGuIBAm0FzMrM5XfdpHgraoDHRZSYZE5M1luBXy0KHqGLY__C099Hz8j0pEwCADrwElPaeKZpoE35GX5yxYR_jmHw_kj1zctkqqm2QGpvLYyGOsKqSxcbd10BGHBs68731DBKGF_q60CoDaWRm3INff8zfFKhsWXitUmCpfVyyyU2WHVMZrEvS4fqYJJWhXVOmm0rGAZ0cgSsYEgZisrk_6l9udsVeFxuujOIZYslGWpu9lJnKxUS-aFLJ7m1RfxOP-9R5c_40TRR3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=PY1DxxOVjDTMfS_5dZN5twMQ9J9G4fm0bW9ZRW8WbHc5qYz7C-cN0NGAvkPcdD_OjSNj5oanGuIBAm0FzMrM5XfdpHgraoDHRZSYZE5M1luBXy0KHqGLY__C099Hz8j0pEwCADrwElPaeKZpoE35GX5yxYR_jmHw_kj1zctkqqm2QGpvLYyGOsKqSxcbd10BGHBs68731DBKGF_q60CoDaWRm3INff8zfFKhsWXitUmCpfVyyyU2WHVMZrEvS4fqYJJWhXVOmm0rGAZ0cgSsYEgZisrk_6l9udsVeFxuujOIZYslGWpu9lJnKxUS-aFLJ7m1RfxOP-9R5c_40TRR3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=hIG4fDTiiRsHgIXwLUuwD-94RLJbnCWsesryiVDNw-ntKtvzyIPXajm2QWwkVRDwkuHvQ9glAsjbbwv-AhKoqxsdrCD_IV6Z-pFgkBic1Rh7g-21DDaO8fEslhGYIqHb9GtbJtpciMsRMHC9hFFOKXU_eQRx4NnhsTR5oWJejjc_A4aMq1uUZD5kYHt9wl1ey41OtQCNSJcuom330-E_iMZf6JGYGqjSfGn225rKX0m9RDfgBcZoDBOaclZWBsy-wD_WdyDO1UR6DxZMa35oBXkHoVArS2QED5Gzx6UQwMS9hpY6lbWb6YXi11Y7bwx_2_P0DzHB-5642lNTJ12UWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=hIG4fDTiiRsHgIXwLUuwD-94RLJbnCWsesryiVDNw-ntKtvzyIPXajm2QWwkVRDwkuHvQ9glAsjbbwv-AhKoqxsdrCD_IV6Z-pFgkBic1Rh7g-21DDaO8fEslhGYIqHb9GtbJtpciMsRMHC9hFFOKXU_eQRx4NnhsTR5oWJejjc_A4aMq1uUZD5kYHt9wl1ey41OtQCNSJcuom330-E_iMZf6JGYGqjSfGn225rKX0m9RDfgBcZoDBOaclZWBsy-wD_WdyDO1UR6DxZMa35oBXkHoVArS2QED5Gzx6UQwMS9hpY6lbWb6YXi11Y7bwx_2_P0DzHB-5642lNTJ12UWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=JInD8vTNF8O8Y6fmAuVAUm3kTGCn4u7smqu0KRYBB24l81kr1IJSOgOd1JZQNEOKK5lWoyan5Vor4ZMlCilNuBCU4Juvl0XjGn0zu8QMjBSZCzFrXFV5fgfyHBT6UoJpjtJPpTj4_o9eOLVxUsunWWP3qKPseG4rGIu-q_8y7Deb-OZiUaDuQV49Lni6ljiTKojTAyM8S9vC5KSsvLFKPnvjEHEcoMuAdRHzqP8LeP7q4EELreBSl2QKP_2UutyqGTcHmTAQ-uXDlDFJmURx-PZlh4kZEFdl6IaJuAzhTECBgA93rUjYgBJ9rYlLDisxYVKgI11BOHi9J-kw8WJt1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=JInD8vTNF8O8Y6fmAuVAUm3kTGCn4u7smqu0KRYBB24l81kr1IJSOgOd1JZQNEOKK5lWoyan5Vor4ZMlCilNuBCU4Juvl0XjGn0zu8QMjBSZCzFrXFV5fgfyHBT6UoJpjtJPpTj4_o9eOLVxUsunWWP3qKPseG4rGIu-q_8y7Deb-OZiUaDuQV49Lni6ljiTKojTAyM8S9vC5KSsvLFKPnvjEHEcoMuAdRHzqP8LeP7q4EELreBSl2QKP_2UutyqGTcHmTAQ-uXDlDFJmURx-PZlh4kZEFdl6IaJuAzhTECBgA93rUjYgBJ9rYlLDisxYVKgI11BOHi9J-kw8WJt1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC5rbRYndVX9DytbEHUkMH-dnMJtOu0srXyVAmxOs5G8p6B71nL3rbdR-UvTudpbkB3RztMWo5Zxy_2MkxCSf9_W0T7RThC7kB-r6FVYodfoHbW8LhTamLecyy8QTUxjNI_uhSqFh4D2MPu5f9ebMQoN9dQUhSLjHHfZlI6kfBkKLYIixqFEwppsUuwJOblve100-ooRKD10Glp63-A5gc1Zn3w1KBX_GVMxvqxCjZV3iBeSHOwCQzHYUMuzF2VbN8c_z-0Xy8Lej2C5z5hb0AOPpkHd5-L5rYBtsgwQmyySkdDjKmGsXKWYdMbbA2G85WirFc9UvpF2FBND3Klimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBf2_T7Iyz03ntCnVQxMQF_7XcxmdMeKmYFbhZV28gS9JQXmMQlqvqGuDW2gDNZyqkj9ynWqQ2EW1pgX0ZnnkzWoTwv1W5ey2Js6hFgh0qAryVRihZVoRl1Aqfh4AeeKDWNMQLuYlY7qJdaSkET4Ckpr-XPlekpWIsBu8C8ecVqPa4es9k8vVtIFTlIBcwm5aCRyBuDE4RCUpRK0_H4Ttt0rcYtA4tU_R8fv2pKrIJZe7QLMojn0-ujDC5X2U6Bmj5DQ0D6JOvp4eAUic-Mo8bL1uT7Jpq4EdQfg1VJtxSQrq4XRlKGEkh72lgOCxOMMTd3gFs7IboO-M8zlVAY9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rByK4BHPkRmdAUfbMiUit2Wmt8stpQIQqq2p0Hz1Ow5WQg_vU6wPFH1naIqHZZXAfpr5AWk4-i-feda292LbhwqPFAcjYkRMeR3BlQUbGpda4WbUi1LOXA9m37s5hfuaPDm2NLJ7kCHxTLZGut7_XRlVEd_XAFMZvEZtfh8qukZIlWR65XxtUhW6CxvlV-q3R7X8JWrl5ULYnOwwlEDCWoyzBtZHZJda-cFPhJFPMwl3ItMrAEE1OOI3A2D42GTvUVqy4H4CXM6SKeqmyRy-E4bVn-rJbYHvt4soQH-ptczbe8i9Or-F3fddCP6Uy_6YJoxrAX7DmwvOEdvdNHaU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiaQn95i2nP6DrOCuGONiva6YmBvECVkghSxb6_57_bl6dCo7KACMC_MU37o-CCvG84fbE6gs6ERzFCghjVnBLpjanK2V3L-shvrmt3ks9OLW5vpdpzqulD9RajXIOiqCbw4ezQnFiHalFzjuCDH2eiG07diQIlazrzpWZnEN2DeFjuF0uNDFx9lMMgUMIGBvIVAd0tr2-FrF7gl2ojBdH7DLmCe8igKWvQEyN2KklVI35mUemEulvyiji4eW_uAjBwIR1byq4Dp7ebv0nV3aWm_sHUkcKpewsCN4gkbu44xE2cA95H4EOctPX6oDXgRO2L2ICDYy0IWDOTUMLJ4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iElRSCnI-eHRiH0jF68jcMNCAzXXdU1MbQxT_2_SvbDUtXxUzfR6vKd4hGDkU2Yl4RLUKtDGf5-T70RstNnR1kfU4KzzCd75D9bTscTbWqs5nvfWfYJ2_pN_DfGIY0K9cHtUnv7z_rtON9ieeKqpFwtGsMCS9s_KDcXAgZtmbFIDthcYtCxfLv44LWnGdrU7VLKf4Q91n4MLcysgmJoT3C4ERUUW4SDw-IsDUShN4g0oKR9q7DO8wDo_V-1CeKKbjQ644UoUN5DeHJekSih0yU259GlYuds9796_zGFgJ4X9-iipqvTSar4L6FOKfXC7lbzWEMS-oHecR8mcrONnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=s7FS2EyUVKJEVJbylOnBDXAFziKj9ouUfLjBal7W1dND7Y10HwX_EJmXRO_f34IdLMGOG2Nr7AWEim-KI1T1TQc2Jtjj2qnyqb_9K9XuN7-IGbn6lRyl5d_upXWnTJkzz3sMhTSfQFg7yUbqkHcQgjT30LzWEOyOOzjWmIzAtLws8OTXvGlBt8OvPBKnlaSXxcfmN46aBIvJqdaSy8UU7NKn9k9IPUkb3y2hWx8rFeR2sQTkZFRDotdlkxJFtk5HUKrksJOdBk1P0zQp4khwTOzBN2Aw1oBm3pmywyhlDQCWY1YhtzjMWQmr8usW5EcFSp36h8upNMStrdvmYOdDpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=s7FS2EyUVKJEVJbylOnBDXAFziKj9ouUfLjBal7W1dND7Y10HwX_EJmXRO_f34IdLMGOG2Nr7AWEim-KI1T1TQc2Jtjj2qnyqb_9K9XuN7-IGbn6lRyl5d_upXWnTJkzz3sMhTSfQFg7yUbqkHcQgjT30LzWEOyOOzjWmIzAtLws8OTXvGlBt8OvPBKnlaSXxcfmN46aBIvJqdaSy8UU7NKn9k9IPUkb3y2hWx8rFeR2sQTkZFRDotdlkxJFtk5HUKrksJOdBk1P0zQp4khwTOzBN2Aw1oBm3pmywyhlDQCWY1YhtzjMWQmr8usW5EcFSp36h8upNMStrdvmYOdDpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjZhrftP0dyGIxaWw5tdVjn6ah0f2cphIqxqqdeDLqc0KqwPWikMkGc4pey1pTE6m7Y4Ch8tNG2IxN8Zux1uXLXof-x89IQGaswxEV1fHhvfyHp-JG1NvkHFCtXUlxOFxrYAhLJk4t4mM_fMk0yihtU0GzjZMCvx_Tfotehq02jbTmmheZsGoYMkFJQwWpY-fBQD9shUgfTRbpoHhN0XRhuNPeZMKcFUXyIyEVill9fWRpJTysRrcNQfCVhT3m6IoWp9MrAKBSf050ne-eD8lHo7eLB8SjED9mfYuy5aUG1FDAldow2H-WaS4ZoIodLhjDCX3jUpf6CA6wioDi-AsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdmbZ_ZdcpVuOeh3rsWyB-X9tt__48KgU3d2MW8efwS8MLZISMiKIDKnAHGiL1pVjigIOwV1zQdgJArsshlPYFoQm-wvZ8ft2KHheKIm4NVK7PrP3fTzpQMz95rUjq3YIrj5-7kFnikb5x59CpZT9vZIHoFMXTSRAbrrHKKz7hBqhWNSM-3syYwgXeJ4g2Mcn91gAIIUv9bthNeVRRwGqrDKVO-egyeDwdBM5JI0HQOqTyBse3rBx5ROstgJFG1eH5Q4UV0_1HkmtomzcGj0beLAJ-R_fepIJ55V_QbJerd3LdkB2lfgzuAzhFpwEmc6qqogoR1odAU-LlKZYIIXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=jVPRnaVoFfslsn_EVmTbOChDP5yWTchdss33TlYYog1J1LqhrDgoESs8eFeC6gZQd_LxeRgY8ACN45D6TAZLqzyzPxex_mT9VV3njiAAjt-Lnsal4cwEZ-wN_wY_OALG9vkdChR9L-Cm5zUW6c0q7X3g2uu5xI9oRceBIKdHkuHVa0op3UWNwJeuu5xDS--bqeZj72Kod3OhzUY9NRwve2nwr8XIvYRNWYNdvA1EyzOetZU5hAqyWdd7LrFA_og5h2KfzLPtPSD1QE1OeMue3nsyloGWKPQS8CJo2jY7TVpLedb92pSsympGhMePv9Aevg7Zk3oIPy04D6NMGmFa3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=jVPRnaVoFfslsn_EVmTbOChDP5yWTchdss33TlYYog1J1LqhrDgoESs8eFeC6gZQd_LxeRgY8ACN45D6TAZLqzyzPxex_mT9VV3njiAAjt-Lnsal4cwEZ-wN_wY_OALG9vkdChR9L-Cm5zUW6c0q7X3g2uu5xI9oRceBIKdHkuHVa0op3UWNwJeuu5xDS--bqeZj72Kod3OhzUY9NRwve2nwr8XIvYRNWYNdvA1EyzOetZU5hAqyWdd7LrFA_og5h2KfzLPtPSD1QE1OeMue3nsyloGWKPQS8CJo2jY7TVpLedb92pSsympGhMePv9Aevg7Zk3oIPy04D6NMGmFa3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دیدنی تیم فوتبال الکترونیک ایران به حریف ژاپنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107108" target="_blank">📅 11:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX6fJ06zYwKZkXvG1SZ1RQZ6AusCdyhi-me_F9aEj8coFM-H3HlmAXYJ7EKJ-KDFBPi98CY1zJNX2PqescC8qssWrqlYrxiRrrDjK77tdY8Pd7xeZmw2emzn3y8_msFSCZgvxucRKPky4_zwQ382iJrkIvH39gYWp-2XqjMaDe0TVMrGtfjoYEnHTXUOwIN6ZslyDtZdtbnOld3cf8MRXJ9IP9MS0_dhmyYmHhHyO5R0FEBH_j09f_SxfFD2axAgLm88xnPEd0bNGaL3eLg4W8L1N8Q5Mps7WER0WwrfdFUeKTUOsuRKCgTDB9u-njIpUVTRsxjRY-XXGsCEEaURFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107107" target="_blank">📅 10:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g79s9z-WR0eb7pG6Y_-1UhM9WYcz5WZla6pBs-cX-MTz8iNVS9mZKoMlHOetzxbcOYp-vUqoHGkePntsPeYHnE9wRfl129Mvnc1Ulv1kFK1azx7jSyatWXVTwQQU-g5-nuv-mghNVTMdD_OOrPFT-zn_GqC_Ap836vXWitkZlOh0eLSkmxWcdf0GNn6H7hteAzQmlG4O6Jb51gglNuXOr2KTHafKsmQMib_QXw93W7oISJjgBLFyue03QxepPN8JEBaeh4fdE98D1sm9ptdrA82Bydgobk8LHSMzbf5Uvm6tVoYl9FAeJLc0ZvnVemQm514j5ZDEP9RwIrGgWtHZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107106" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcsNtDoTsH-GWw8xmYvFNLSXGYnE2dKf7ciror-hMrtE00yqXKq9DbYV9HzSbvT3hEEmN7nEcuMZLiTr3oPBkewbdb0BrLwP_8Z6tZXEPCmMVn4F48_-2Y1-WPfGe7FZ4R8y3j1okQ9Rll3LR0VcEl5_eez0MmruWHnOCajXrJcOdpCKTky7TSMs9_EtelqbDzZ3y2D_Rfzdz9ZZhWA5aoPiKLc2rTRQxLscR2onQyLFMTWYE6yMQ2Xkc6vMIOdPWOCgvYXOTULnKi-obxgSudWT3GIi5U__08dNpg3oUxsGTgrXUM81ZVUWiqCnr6bLxWCroBVNLzNtES38wS1VYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107105" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=Tyi2iMNgj4aT4LWy8MnR2gHw_aIC88wDZih4F1N_8C4jLg5oKDkcLVvfPbIhYUU50Abu0Dp6akOO0Tsu5lflCUjufVzx68oJkdJR8dT8-kIs0xTRTrEysgrP1H0PMLFBcbquy5GujvJSQIHJW2tpjS6sSLcfg16IO5-A366eBUIAydxO4w3Ua5sSCRsgeJ9a4DIDBsdeRoOP5GVUPac1H3JP4NtSbzY4R9t05NiJ6UKXU6OTIoH2Y2XT5QqIdbe1AoIJOmjPj7i2196PjKHfEfwwrjXBUPETTDu101wKUUzk-F9a_qRjGpuM90UUICFGLhgukybm4YqqpwXiI0z12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=Tyi2iMNgj4aT4LWy8MnR2gHw_aIC88wDZih4F1N_8C4jLg5oKDkcLVvfPbIhYUU50Abu0Dp6akOO0Tsu5lflCUjufVzx68oJkdJR8dT8-kIs0xTRTrEysgrP1H0PMLFBcbquy5GujvJSQIHJW2tpjS6sSLcfg16IO5-A366eBUIAydxO4w3Ua5sSCRsgeJ9a4DIDBsdeRoOP5GVUPac1H3JP4NtSbzY4R9t05NiJ6UKXU6OTIoH2Y2XT5QqIdbe1AoIJOmjPj7i2196PjKHfEfwwrjXBUPETTDu101wKUUzk-F9a_qRjGpuM90UUICFGLhgukybm4YqqpwXiI0z12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم کره شمالی به ایران توسط چونگ سونگ(68)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107104" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگگلگل چهارم کره‌شمالی
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107103" target="_blank">📅 10:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=ApL7GcIgCrGOdHSHgx052VZluBVlDE4k-JDRhKBnRnhWTyQWdBiffDoTxwbJYL11CYD52ynTT0VFd5EpJDBV04ZyvVKkNRnCbJlcF676PstCTaEPyFhhqVt3AXSbRh08k9QxrDZYuXCuZDjXlEJ3GburP69T1_OnKq3GdUtYCSmbrPd6cc32mTxZJ8zocl7qElnR0FmgXORhN-F_o0oUugSmsN2G3omhw3_qDKUk-DlWvS9ztPcJr6KG5W1UOj5crNieufTxu5AZFTWnBv_ie0_KNVollGUY_VpLo5aaAeLaga-nXko7Lv9ATHfMn9DqL_4yRs83qLPu_hD5-AgBpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=ApL7GcIgCrGOdHSHgx052VZluBVlDE4k-JDRhKBnRnhWTyQWdBiffDoTxwbJYL11CYD52ynTT0VFd5EpJDBV04ZyvVKkNRnCbJlcF676PstCTaEPyFhhqVt3AXSbRh08k9QxrDZYuXCuZDjXlEJ3GburP69T1_OnKq3GdUtYCSmbrPd6cc32mTxZJ8zocl7qElnR0FmgXORhN-F_o0oUugSmsN2G3omhw3_qDKUk-DlWvS9ztPcJr6KG5W1UOj5crNieufTxu5AZFTWnBv_ie0_KNVollGUY_VpLo5aaAeLaga-nXko7Lv9ATHfMn9DqL_4yRs83qLPu_hD5-AgBpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل دوم امید کره شمالی | را میونگ سونگ '44 امید ایران 1 - امید کره شمالی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107102" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23009325d2.mp4?token=u6gkVmcwlV-b0_pN2Kyp1RImece-NrDzLpI4-ta7O3Q08l0_5r37hL40tTuomtmVn48gXM2E9L9J9NhBzSE23duJTTHpKwsBXLeEKOSTxg26TdTQBeabyRZR8TXqxy3ipFEgjH3AG7ZMXhREZTNC98zApStWFci9b9QSD9e7hpB2-DuRatcal1f25Udxo6uSicWLPMc3IxaW3QUqY5LExZ21hOkkRidz7zjyj4b9o9Ikcy-K2eigsSSFpgy38OBP5xI0wqfSfwzrw_MtqfR47sUFbFP4mEJAieZEOum3ROG6Sq3vWvZzYn8qFqXa8JbFg5IwIewSoFXJzZ_CL3NiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23009325d2.mp4?token=u6gkVmcwlV-b0_pN2Kyp1RImece-NrDzLpI4-ta7O3Q08l0_5r37hL40tTuomtmVn48gXM2E9L9J9NhBzSE23duJTTHpKwsBXLeEKOSTxg26TdTQBeabyRZR8TXqxy3ipFEgjH3AG7ZMXhREZTNC98zApStWFci9b9QSD9e7hpB2-DuRatcal1f25Udxo6uSicWLPMc3IxaW3QUqY5LExZ21hOkkRidz7zjyj4b9o9Ikcy-K2eigsSSFpgy38OBP5xI0wqfSfwzrw_MtqfR47sUFbFP4mEJAieZEOum3ROG6Sq3vWvZzYn8qFqXa8JbFg5IwIewSoFXJzZ_CL3NiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41 امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107101" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=dB5U0rytZJUtzk2BftO61RpSGOrx2sPuNereLIjG2xkHfrQWm3BJpdL7AEnSdmuaLPKx_2b2V_SvvqXNp2evNIjDgklAbyj56dT0bKBb8ujJa8-1Xy7ZLCjvgd0TKA13E9xAbuQDgJCTN1tJFvRGRxJDX0FettLrFha6qvPxVtN6EIjmHyXS9TZt-NSESP6fG0qJHQSHrAvUnfORvECV1d-0W76c5vcV-wSCqiKpjcM4TWA7HxNM6jDTvH93wTB8Iar6u8X7_37hHRo4L3ed8T836vlNRak-ICP2ocgIR0AoQZDtbzgPBvmWuF3eqK9gU8tVvuFTQUfNYVfe22ZlLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=dB5U0rytZJUtzk2BftO61RpSGOrx2sPuNereLIjG2xkHfrQWm3BJpdL7AEnSdmuaLPKx_2b2V_SvvqXNp2evNIjDgklAbyj56dT0bKBb8ujJa8-1Xy7ZLCjvgd0TKA13E9xAbuQDgJCTN1tJFvRGRxJDX0FettLrFha6qvPxVtN6EIjmHyXS9TZt-NSESP6fG0qJHQSHrAvUnfORvECV1d-0W76c5vcV-wSCqiKpjcM4TWA7HxNM6jDTvH93wTB8Iar6u8X7_37hHRo4L3ed8T836vlNRak-ICP2ocgIR0AoQZDtbzgPBvmWuF3eqK9gU8tVvuFTQUfNYVfe22ZlLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41
امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107100" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=FX4_B_4XF5S090feMz6RClzz4kq4tGYwp48WUcTh7rlw_SeaPC_Lu8d-X7_U9bumJFq4raqCONPwN89VH9-xW8I8eKIuvu53Rw16hFGjso6ug_D0lKGDsQpyDkGqN-4y9Sv9YLaSxd29AZ77vvblONHPGMoCIupxhCT7aH7FM0PvN0m8xdcyvq8F2j0hHUjtRZNvtApl_602lP6lEkY4JxM0wFrfNfynqCkhBrVRY-4LoYZNS7UBCfwUKENcOfoGzyIIsOlVuSE3suPl1vpRq3d3rhOaC_xkyBpuZVWmjkz9YTkFMXz6DnZVAhsv5CcCYZrHwUVOCMoXb1skn2B3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=FX4_B_4XF5S090feMz6RClzz4kq4tGYwp48WUcTh7rlw_SeaPC_Lu8d-X7_U9bumJFq4raqCONPwN89VH9-xW8I8eKIuvu53Rw16hFGjso6ug_D0lKGDsQpyDkGqN-4y9Sv9YLaSxd29AZ77vvblONHPGMoCIupxhCT7aH7FM0PvN0m8xdcyvq8F2j0hHUjtRZNvtApl_602lP6lEkY4JxM0wFrfNfynqCkhBrVRY-4LoYZNS7UBCfwUKENcOfoGzyIIsOlVuSE3suPl1vpRq3d3rhOaC_xkyBpuZVWmjkz9YTkFMXz6DnZVAhsv5CcCYZrHwUVOCMoXb1skn2B3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول ایران به کره‌شمالی توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107098" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=jVQO2NqOHdxiGt6iNjMqvgqxsyrUIiXoYGrHXp-SCBxDLfx_V4r_AX-5YnbCL9dOAuXz88F4LPL8L8EFOMca85UuEfxneegMQFbeXMHbnnoSf5MPe7Gmidoc5ZFQrh3MixDCYQ3euaTpq44BcXtJnjpHAUalaiqOLo69gEE1OrwyDjlPCZzATm9m1_Fp7SvzPTz9x3R6e-D-7K36r8JTkHmDWLW9MLzxAQVfMNzaDYX-UrHBoIGkoZJmraRHi3jJ4x8IqowyeMpbz80CFcen_f9IChMl94Qibg_f1BIa4TmO_6ap3E2zn6sqgD_QT-fd22W5YxiOCv7W25xpluoifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=jVQO2NqOHdxiGt6iNjMqvgqxsyrUIiXoYGrHXp-SCBxDLfx_V4r_AX-5YnbCL9dOAuXz88F4LPL8L8EFOMca85UuEfxneegMQFbeXMHbnnoSf5MPe7Gmidoc5ZFQrh3MixDCYQ3euaTpq44BcXtJnjpHAUalaiqOLo69gEE1OrwyDjlPCZzATm9m1_Fp7SvzPTz9x3R6e-D-7K36r8JTkHmDWLW9MLzxAQVfMNzaDYX-UrHBoIGkoZJmraRHi3jJ4x8IqowyeMpbz80CFcen_f9IChMl94Qibg_f1BIa4TmO_6ap3E2zn6sqgD_QT-fd22W5YxiOCv7W25xpluoifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
دلقک‌ترین استاد کسخل در تاریخ سرزمین ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107097" target="_blank">📅 09:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=oXRCd-sYuke5XEq2DdV6cZP6208pellRiqSn3vLOMT1hIFkBtmTeFh1bnxIjN1YvlIl2vXz3DbXAHlTVDuuPNyUfnjOw4UCh0Gl8oAvIaj3Bsv-wIz7HVLmADWd24QAe6Gv8FIz5e30sJnXhshYZStTQyfYGcB0K4dN259DnlxiAVBZLkmJ3C_p0ior1dgaUFvm0bORMUnqZnFB7TXlPEK2pJCDtjn1xL2B8GT7SssbZb_tIWSVJTgKO-coUCb_BONJQDaehFaImuPi8SSA7p0oCHQQ0vXCoN_iMlkcUyrdPs_BaWuQc4xPNldoOtwjfoMdMGW7jP-8-DhkAw1I1pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=oXRCd-sYuke5XEq2DdV6cZP6208pellRiqSn3vLOMT1hIFkBtmTeFh1bnxIjN1YvlIl2vXz3DbXAHlTVDuuPNyUfnjOw4UCh0Gl8oAvIaj3Bsv-wIz7HVLmADWd24QAe6Gv8FIz5e30sJnXhshYZStTQyfYGcB0K4dN259DnlxiAVBZLkmJ3C_p0ior1dgaUFvm0bORMUnqZnFB7TXlPEK2pJCDtjn1xL2B8GT7SssbZb_tIWSVJTgKO-coUCb_BONJQDaehFaImuPi8SSA7p0oCHQQ0vXCoN_iMlkcUyrdPs_BaWuQc4xPNldoOtwjfoMdMGW7jP-8-DhkAw1I1pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هیچکس نباید قهرمان شود؛ خیابانی: فصل گذشته باید از تاریخچه حذف شود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107096" target="_blank">📅 09:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud49Z2-CIkHEtAqFUE2S2uEB1591Jk2D7U_dmo0w5LKZ3holG9B1Q18qF9lieeNnTet1IEvz7OdEYWMrxIV8fsRrLwYWhz5z3pOSKxP7RcLBI_CkQ_WjUqIrMScHbbSNkF80S9PA7IjY1uhN8wtEQaOMt5M0egckq3RHGsXdoIN9LoLOzKAWWhUJVBpnIevdgb6-k_rrsZldmQJU5S4tkrpivU1nmnR2VYcQarIrOYAkzqVjYHnY1vDXtAXmMauaAvAApkAQm5T59rZsMiCmcfKBiW2yJmkTtDwEnLww7i72mZ7kVqvI9cKL2e7PFgJRrSJhGTTR26vwiz-bBnONMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_t6uB8X-1vzGriV0xt92h99iQZ5qltIP4rsS0TpME9MkHzxVydD6Dv0a6su8fc4RLIusf3aMfMeAVc68JDk8vslNdZVF69tRkk5u3s1XlMv3YGBCDWTC2hQV9Bl5vS-l_jnqp0uUhmpZ3nf92fIr0qZWnAJCv1aSopUgL-xte-kg3jh8-0V7LiDDOSbiXwFwKzWcVpNDaWBw4I_k_vtZo1YsDmbYxpAduEJPhJwDeJuu_iYlmjqyGI5VFrg54siIdujGOZzDkR9GphrK68uglp1bxFlFYrtIFS_P8a73xgBn1h7zKiZHCGODnjgZ0I2YAhcFEnuhpMdeR4yFtzMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
