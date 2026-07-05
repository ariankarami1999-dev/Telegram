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
<p>@Futball180TV • 👥 632K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 00:18:48</div>
<hr>

<div class="tg-post" id="msg-98378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پشمام چه توپی رو گرفت آلیسون</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/Futball180TV/98378" target="_blank">📅 00:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igZtKM_QDsAuBzOLw0jyOSLlGFHB9UxEQ8gla2yTPvOyDtWnXUuEDfG5AuwcZS7k4zNKsHpWYYAhZB7OlruDzXm6VgRHOSdhbhFcHyoN6NfsnGerKS8VcawGpuqojhuFBTC6JiEp0lcUcYNk8vWuYzFlnump39azamd1Go_GqzwwOhqiUHYXPi_HU4uyDzjSmuBJZJPdOsIyZp1Aj3flUvtY01LZAQFX8b438fP-g_cUo3kNspBVtyBRz3u0cqS8J2bG9d-hjBb7r4iOYsG8SHlLcjLqj_sn_ZsfsKOx4BDB81gbkDWXaRq4IhPaYe4a8LK0EpYGaRA-Tyd3aLz5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/98377" target="_blank">📅 00:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: قطعا در ترکیب پرسپولیس تغییرات باید ایجاد شود/ به بازیکنان جنجگو و پرتلاش نیاز دارم و از هفته اول یک تیم دونده و سختکوش را به زمین می‌فرستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/98376" target="_blank">📅 00:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdfvVJeYs9fh72NYYPxQlOvnOawBwq_hD_7RY3eRRlqImXPBVRl7ISg7WtT4MUcl3j61nLMm9XvKArJLdpLhN8rYPTh7vPqe_U6r9hShS1Ensakr4boCDNF32mcLtUZ_zC0BVkqMM0xh13yEBG54LzXGDdbytnfWIO9oM2IXu0qzNYkFfOGWjjjT620Ci-9lPQ-PRlwdG3WawiTIg_CB0WUkPD5CN4M2o40pIUXhrzxg1OxuE2ksE-XNBU2x9IFBH2W-Mg7vjoOqT1Oqq8UUtrajbFpFo1sZoH6-wGxcRXdFBJw4eLSNNQEN9NawgK2d-hWRwYuwUTBJSw4luBtxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برزیل تو 40 سال اخیر جام‌جهانی در جریان بازی هیچ پنالتی‌ای رو خراب نکرده بود. در تاریخ جام جهانی برزیل فقط 4 پنالتیو تو جریان بازی نتونسته گل کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/98375" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلتونو به این خوش کردید که کونیا برا برزیل گل بزنن؟</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/98374" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بریم برا آب درنگ</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/98373" target="_blank">📅 23:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRjlns5fjocBhXr76mdifeIAq1uN5Z-Le44B0QES83gx79d4QHpJNRfWGuO2LyT1XNUODfjSsAVTxIdhN1zvM-P1t0VfJTQ9jz0HQ-xODkxuysSuWhXG5PytMKQiXTSB9hwNHKW3N1gog0vNGKfkzvuEmdkXTal64Hm-cntmFS67UoEdtePQK5thYDAeQ3-I13PFMjy3fDhRdPBAlMr-_5AAN2xQuTxO6_p6ol8ES9ocWrf6FbarSTNjEhk83fyeF4SmH4u4yh2ppgZIKs4_EJiXsOS3qupp2RVgDtcyUvcfMFur4IsKB4HrumKbomcY2jSI9evWUjK-HK7MFVWCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که هوادارای برزیل از اون میم معروف که جدیدا ترند شده آوردن ورزشگاه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/98372" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjRCOtwCSc-rDBE1F7FndqC468UGOtdO618mL3V3pcpsDIcreo-ydEdukwT81JjoKk14v2npi_hEwB192j_LORgCwsyaU6HbM-OJgkXvvtmWYuZAkx-Clv6KqDGMhwWqYBnpmtGTCo7sqjkJFd3YXXnF05zY4gAz8fscPAt-sfwuXm_Py4vg3PhTxnuo5eiibQtrL3jeNWGNY3mD0otOGzjteXGdAISZ-6o2oM-W9UqVXzCJbWRhhfjm5jDvT3XZ3OBVxlvzEqkw1wuych1qD5qPBt76civTOYEkxaTozxBqNFlL4G5OlwV6zpjZEQwfttAWZe4b2QZ2NYqVjnLj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/98371" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/98370" target="_blank">📅 23:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رییییییدددددد گیمارش</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/98369" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خراب کردددد</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/98368" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گیمارش پشت توپ</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/Futball180TV/98367" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پنالتییییی واسه برزیل</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/98366" target="_blank">📅 23:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خودش رفت ببینه</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/98365" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پنالتیی نگرفت</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/98364" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miMDrKIDEcL_Rc7Zr-b8zL9YkXByDB3ZQ979R4PO6E6GTSodHZ-ADLfquWxYx7hY2m18gdnHQcY3cMAbn1A1mIkRSAj_PsBK_HMOsls9gzRixSq7pTyHHcclrTpQ8EvEweA89qLzSZJBaJhkPC4FuQSEJDo-TiCWJtcrJ-lJIr6___36rPC-cv1GskzK_bjgE91nrOjZjNVpE42HChXWfCVZm1mHPferJqt4I4KDoS3tsq3mTHOLxNxzwaxV_68aku_PdFhtbZuKqKWzTghXgtQP5gOn5pbORUJoXrC5KPPeKRLVo8uBBddZecPg3H3kvrdC0fjG-Ql-gzTzdV8KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/98363" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: از کودکی هوادار پرسپولیس بوده‌ام و به عنوان یک سرباز تمام تلاشم را می‌کنم که پرسپولیس موفق شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/98362" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/98361" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلللللللللللل اول نروژ</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/98358" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بریییییم سراغ بازی جذاب برزیل و نروژ
🔥</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/98357" target="_blank">📅 23:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF_SbUUXvAj4GH1Yi9xcCqfTXJU7BNNUwWZDAmBn8JybkbH17OWu7f2mSUs7r7HAsJ7IwiL0Tar1rtpOI1vA-k9e2gugukP9WVMepjvWlg6mUAW36MgCd5jCeUYW6bZj0D8ZRNC9I-AYB4tIoGwCsaljad_Be7vFRfeCXVeWP-pSzljPy94FlZiFWDPdynFwlqRyQGrYLOgALKF8e5G7GAiVndEssLq_079pMYSP3070sLhwfMLN5Eyagd7qwBzCJNNoCChPHvd7BgaixOZrA3Y_has3HL4ajQ1VMRWZOO58JkYmN6D0SjFYh163Aw-nxQnc9B823ysM_ENYAC3cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پدر ارلینگ هالند:
شاید روزی انتقال هالند به رئال مادرید اتفاق بیفتد.
چه کسی دوست ندارد برای بهترین تیم جهان بازی کند؟‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98356" target="_blank">📅 23:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrACBxusC_g45iarAfNxAHqtWxsacpJ_HgJsKz9P3j-t2mbc-BbPJjiQ2JCMGRi8ZEOu9BqWlpNi3LyndrbfMioFnMJjhvs4akOj9769fM2LtlHgjg_bOGSUXUEdwGIdUChsPy16zhw6TE7WRrzxSq_TO6kPISPP4IPwLywd31mAJKdwocEg1vhfHw_7rMwCswm6zKNXXo_HCS5yeWwKTOtbaa_scSD5TCfWGazWsvVCW6765ZXezUe3rtKNNW0DbIvw6woVeq9csiQXlircs5ypqd5YalCw-PLmb_f8IOU8hTPnAG_bK_kZLHeaQ1T14B5bY-DfKyFdr3xRQdDY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD_wRfKVPCC_nRcQw3cvbr61vJfZTUottLW59Pvl-MYzE6dP0VxZK3o9q_U1Q810iXnDwNAljSyJvqgHjVuf5y4CPE0O47V3zAHtFb-Z19AOVockqdelI0CysWXpJLLr-6JKKD8wjLetFbxlhYGpEA4WsqN1wCWnoOZbsKU7VzDdEcWe8RMo1zKD1e44JK5gmop-jJn9BLOO_IBfYbOv9_pWm05OgLTB5YYfCiM88h2MEhcYdM2z08YR5CUEHyx6np4_VOCh6wlfv-Kh4KfonlFS-TNPKAM805KZum9nRXTMWEx4oDzcxA2baJn5teHCUBXPnzY7keoJEIEbwxpWWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
آخرین باری که پرتغال و اسپانیا در مرحله یک‌هشتم نهایی جام جهانی به مصاف هم رفتن، تیمی که پیروز شد، قهرمان جام جهانی شد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98354" target="_blank">📅 23:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddtdYqNig7VfFPx8fC4RNcgFBfWvWuvz3w9h_--mytznaseqhwEcvN0Jpw_59brtVtsTbfsVa1h0cShThi_YIkUJC5COOESqX8PkWdktMyG43NHgANzwgm0jdP-V2SbPlWlnJECczuzEjVgS2A9U0D1jQ0jd30HKpMw_mTnvx20mEP7AM9IqxF0p1MEk3rOMYeyUhnbvFi9SKJTmpqr-fTAdWvyx8jFb8sje7I027k5vG2lMidY3dpZncrFNWe5OO3Xm0P048rXAq62TfG4Su2ACdlojta1EBAX5SpO9KeYhCabwP-163WHqEYbJQBEzLu5hlTLNs846oCEyLh5FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مهدی رحمتی سرمربی گل‌گهر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98353" target="_blank">📅 22:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeXgW2sik8UdZazHNH8H5FjXlQi-nxDQ-tggNunfLh12hnQQ3daUC5yZhpuvr7Kw0meYW8BjFchYZ2dQ5qgdTgSvSEwjH2mAId8NNBoU31ttZKKzSIyGQCdbpXaWiGglEf8NeJmD4BleA_RVueovk5v48tk7ZPHIf_FDKFY2QaCDO-ibhPAzzngbwox-7o1kBxp8XchJEWbg3wFRJZDN_EtjHiTUfqMEpSUla_5Z35-lC5FcWjbrT_ap89Adc62I1YlfSxVzRa4svhBCshSVpNf8rVHG9pTl2YlkPNalpYLHlRQuNsTwBRNlMLh32CBWAuUO_jWWTq1uyyt6BxdOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bF99ZlzLxljdXp1ZfJxOO-VJ26DLXfipe03j1Ed7CbiOh0RNpgrTzBAgoOoB-C6ufKYmUDqSS_YATn8-RgxFnSqpKN2xIber-haEnn2H6j0CZAkmnAA9z4Fh7-CEk4bJlAY9qTjgeCQhINDc0aXPdWTQvIbTDmCC8HCOvIu6QiuU1SnNcR1WqxuRouODlkFf4oWgIob6WFRavefSmZk4ohlWlkdVXMTNAgJ0USIu1gmDwimLrPW1f_5xRsGBGa4Z1KS3xDE7qJxDszzRgDZe1v_kiYD8HtkCmVpcSOiCfZ9P62j6Y2jTziQDsRtskR4ZJ5TxKKpQFwWj_Uz8tZX2mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇪🇸
پائو کوبارسی:
همه میدونیم کریستیانو رونالدو کیه و چه کارهای بزرگی برای فوتبال کرده. اینکه بتونم کنار همچین اسطوره‌ای توی زمین بازی کنم، یه خاطره فراموش‌نشدنیه. دلم می‌خواد پیراهنش رو بگیرم، ولی می‌دونم کلی آدم تو صف هستن!
🎙
🇪🇸
گاوی:
اونایی که از کریستیانو رونالدو انتقاد میکنن، معمولاً طرفدار تیمش نیستن و از هوادارای تیم‌های دیگه‌ان. هر کسی که کنار خودش داشته باشه، احترام فوق‌العاده‌ای براش قائله. معلومه که کریستیانو یکی از بهترین‌های تاریخ فوتباله و هر لحظه می‌تونه نتیجه بازی رو به نفع تیمت عوض کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98351" target="_blank">📅 22:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇦🇷
خبرنگار آرژانتینی خطاب به کریستیانو رونالدو:
🔺
من آرژانتینی هستم، و اولین چیزی که می‌خواهم به شما بگویم این است که از شما برای همه چیزهایی که برای فوتبال انجام داده‌اید، تشکر می‌کنم. همه ما از رقابت شما و مسی لذت بردیم، و این رقابت یکی از بزرگترین مسابقاتی است که فوتبال در طول تاریخ شاهد آن بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98350" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrIfDKTRQXVQ6H3S-O8vOCW-9rJZVJs3CnTDsvAYw5raf-NgWjKZpiwMpxCe2r5BB6RNmLkkXa6HKjmlx3m6IJ4wDS9yA7BpHsdQRxgdwPBkXaPGyWpiE8sbdjxzzNMHkk18kvhcvEhpvD2P6NzKIk7OdsIjulCLvG7JHmuP06PdoqXztjwrCBykba6Op4_tqqvowDx42K3bjET9wT7rhwOyieUxYzAryGx8ztB_Z9GCzX1j0i9-OkzNmM1-3712kNqHpDJa9PbqJ_BV9l3UNVsZkQuPNI3u68xzprK4hOUT27l46iFWGRG8cVLx1VxZe4KKsuMy5iElg3Ewq1NVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
ترکیبببببببب برزیل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98349" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRMW215iVr258td5lTF3jaElxW44nI1H3c0jI3O0uGSLkaZeFtZHkUiFoyQE35QgxstzhmFqXhBv03Hg9ug_rJPUiehNAuNPBSHS-kP_2NgKchLm3Wa8YDLixwuFaLHRrx3-ZZyrUwHbuKHI5ezW5zc_OpmjOllu90KpOsdL-Zk0ekLAkfqLVqUBUlEjZ8u9EWt36eNFpQnHQRF70mlt3gCRto97VTFOqqPVs9D9sXKIhufzaNOF2Gpn-LAXdUROACzwBIvo2R6Q1zXfztTQITjIee9uY0T7Zq2hXQZDuZWOxMSLaJSadWq0ytzqu_2vfcVmwZkk7KODCeFJqIBgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
ترکیبببببببب برزیل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98348" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTxjXyY2oMwlQ3Iw54abxbMYxW8haKsJe0NzhWE5xOvjAKMBU7J2oWieGb-rtR6I9liEO4sDPfobmEfbz91Q3ZkWx4ttnX5sjy979qcJIiK9y7-BKtVkX5AC5Ic-nx45pRIQ12bFpt9LWTS8la_jZGm3c1cB0nYehyhiDU0FquNQS4nTjkEX2fQFy-N2aFgdEwbAguWPL8u8bk3jBuLx_oaH2_-FNBTu-7SD4wxkeTAFZHfby2ZTBhhlg7sECVrBFQpM3J9GoZ92ddTNoHKZKXR8OOWO2LMYgvuZl5KpWWMP8uqHipRyxjIckne7J1u8TLn6VlPeliwJXa0UjP8ZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
کریستیانو رونالدو، اسطوره فوتبال، درباره لامین یامال:
• سوال خبرنگار: می‌خواهم دوباره از شما درباره لامین بپرسم. می‌دانم که شما علاقه‌ای ندارید روی یک بازیکن خاص تمرکز کنید، اما پیشرفت او را از سال گذشته، از زمان فینال لیگ ملت‌ها، چگونه ارزیابی می‌کنید؟ و فکر می‌کنید پرتغال چگونه باید جلوی او را بگیرد؟
‏"او بازیکنی است که آینده درخشانی دارد."
‏
"
صادقانه بگویم، هیچ بازی کاملی از اسپانیا را ندیده‌ام.
"
‏
"
فقط کمی از بازی اول، یا دوم، مقابل کیپ‌ورد را دیدم، اما زیاد نبود.
"
‏
"
با این حال، همانطور که گفتم، او بازیکنی است که آینده امیدوارکننده‌ای دارد، عملکرد بسیار خوبی ارائه می‌دهد، و فکر می‌کنم آینده‌اش روشن خواهد بود.
"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98347" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDN3uqE8rHSTIX1WAZH2QPC-gYIqO80kHO04N041_iavjtlH5cCG1WQBOlrfn-UHSZtdmH2KqS_VmbgH3pcOijVNr3CsDvnIBptWtTbWxXP7JqYt8zQVKDBJxYbSbO-HKuoK8eNPx05P2Fsa2XNnmjYJBZqjyyK8IaK0VRnvm1-tkzhGfzyoaGuKT1ijh8Osgu3KLupIlYqUNnMeqFH3Ym4Ny1XlXjiucrGA66UneTJAWfxTU4UXI7Mc7e5HeJt0UlKfBFfmVH1gkxdzFZ9VpySJ9sK0KSprarxE7Zd-1bE8bMWdIZT6JCHZjVW2SllsRgd4vxYEGzB69xAJFx8ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇯🇴
جمال‌السلامی سرمربی اردن پس از حذف از جام‌جهانی از سرمربیگری کشورش برکنار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98346" target="_blank">📅 21:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98345">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq_dNXbcW9tIwQeSW5u1JYIsy56Vkl6li_78qEXFeeLuk9NZvjM6HWzWxDybMCcbNkA9cfiYVEUiU3KcHcVZHZuuXSLlGSTbFKM8uTCzwu2JWUYj8KUKjB4M5AgyZM6D5V3FD3CkeqSPa8cDc5mc38aVg0Loq1eSjJ_IxqZ8HI3IQuQcyq-dVmVoxrtBwwNjTc8N0sXHJ0ksymX89Kp1JhPXGOHFCb0s8n-OmU93jZTmjS8147mt7G3QdEDkWvxKsJ_Wu0Kmv8LFZCzTHhcneHkrasGmAjyUhmjFQ6nkyrXs9cJ3EiUyKqk5AqNBy3x7D0vT8mrjWWsywbqp3N8z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظر کریستیانو رونالدو در یامال:
او آینده روشن و امیدوار کننده ای در پیش دارد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98345" target="_blank">📅 21:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo7ULaN8_O2cWPaekOaFtlh5auYroCv0DnDcD6Z89kqxmV6iWXeuWp-105KCG9ANl4HvbnXDntpwo1qxlg1vO_Ah4YM-vLFGyOneTFQRirZeYqu3dGgl7csIOKm4ZXzB9PE1qllRNSxwvt-jAwf622X4v_WBvzRSXi3t4v5VbqGVW3WPhWe17LQTfIIrUoHoXJQjs-T99KyDPxPOK1RfNw_AZeWnlEl_5O27Q6iKcPV7OegTSyOl75YzADXwJYFuu6jFZJeTfSl3uZwzUnzstc_OQQFBKhliEGlaQFFLukThbz5fLMR9AgUbRrxRWxrV7zuc9xWHG52cxeSCMr9r9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رونالدو: من زمانی از فوتبال خداحافظی میکنم که خودم دلم بخواد نه زمانی که رسانه ها دلشون بخواد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98344" target="_blank">📅 21:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98343">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys_Hc91sYFkFgLLGN1IhyREqBgZ0TYgJ0xRGoHIL93VONCUDcxuUPXkQNxUJNYsNcYS1n3tikOwJ5LjYeN0wGlaV5yPff82PiAAtPG9CYcIqMBkvttshTuVNM2mEE_ID-bMG3J0ZFZocQwZ9wtHLPHgC75UNrUOm2Rgpt2Ff877-JmQnZXT74ul7C7KzA0EdobT9GFLxmMne0V9s0WvPo_exGrG7gxhglbuH4m5zttTWAfDn5b4NR2suBq5ykLG9AqZLFUERqE7_kUpJb-SekHbuUizspAqKxCeLiFGM3gqVAWECdbAQCpUvSiY713A1W_wDzzfICNQuLkhTFPUXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رونالدو: من زمانی از فوتبال خداحافظی میکنم که خودم دلم بخواد نه زمانی که رسانه ها دلشون بخواد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98343" target="_blank">📅 21:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98342">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhJ7N0qa7YpP9-5DUmL1ItoJHVJHxPgjBIPPFFK5LrWN6L7cqheN8jlH8HdSfPupoKAvzGKNCZxr6q0_pzTuyPR1tXNlwYzi7HwvLjQPalJTUhMpvBIULXcmBqI969V1CMNRY36Lmd-MCn-Na-OTWmSey1VU2NLoR0GXuRd3_Nf0tI9J-BAOEP82iA4Az3llALuVliaQOU_QNpp3oJX66UP5tycKuQ_iNM7wUilDJH3qARyWbt1szbxjfXboMnsOrjVZncCJwjDbxMREIMT_iLvfRtWIOnu4b6dqaVf3O_-icOho0oUvx3qyoeOC2NAea7hngt-EawjLAHblxJgOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
نخست‌وزیر کشور کیپ ورد پیشنهاد داده است که روز سوم جولای (روز مسابقه آرژانتین و کیپ ورد) به عنوان تعطیل رسمی اعلام شود و این روز به نام "روز کوسه آبی" نام‌گذاری شود، به مناسبت عملکرد تیم کشورش در برابر آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98342" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98341">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha7dRAk-2VvXO3g-hudbpFuvuhwBwwRw_oF9VvFOJT47UXSmfJBDd9ab1QS5u28LObf9FVNTQc4fYS2ZGPFPn1Gf1oIo1jWORw2dLm9EGPV-VkQb3SwBbkF5kzO7eMJivAkEAlzeWmmgM5r3GmfCB88rE1fvus_JMjsfRDhcmYka5jtdCleYb2Ku_4-PA3o_xv6nN0jgKP7F488dg4VaPFnlDSjIGuSuNr_OhNEd_VYMFpe5Ov0TjIwjF8IpH1IWLn5xAoeRmqkQEMAffNmI7kdCHQBSggvcAg2TJdrPXx425MOTpaUX9zrxu-v_q2gYZjN_ly89BEpzN1UD3W8ZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
احتمالا عمو ترامپ بازم دست به کار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98341" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98340">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFjGqv5j0qBl6M_N8uQQdyxCHtuB4VSexsjxFlrVa0__-RihiZqdp-gRn2FpJ2KCCykWGetBag8Elqp4flmKXCYzNFYbjDZMlYfqcOT_7AVZ1XGPcYktnSmFElHzUDVfPz2KXFlzpqmg-aumKCLWktT7QDEdvUuCHVdk045iAZ2JFWuzg8eJVSf1Z-Knizi6NW2_Mz4RaPqebvA4OchHkiX0MY_puOU8qGa9gQ_njly0aQN9aHFiI4gQhE0k2fsSuhf_S4xpIJmofipukgI_2AuhN7OilwhqmbAR89WRdhpbe99uDCwmsIXh881KuQ8_BUZf_kmEx5-viArLacg-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انریکه:
بهترین تصمیم زندگیم قبول کردن پیشنهاد پاریس بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98340" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98339">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98339" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98338">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0amoO0AIe-_QzSwGZvjF4l2r9DteHpIL4xI2wynms1BZ7ugpASDs5Aic99b15geXEzgrD7Ee4wbYG7dfgz464FnKHyid5TJC0UapVP7O4C3PSKzVem-sB81v9Mlme3c3_eJXjY2hS7DQqaA-7oTF3YC2m8YCLKIrORdQ_bXhElr_wWxyyWYz36-1WijjV9nSnUTm6fy9OOXuVj9lBuT2Il2TWaySeec9GDyGR2wQgguW7qQc6jFuqN2XBLuEoJb6NX_Bu2Dnohf2F8o4boO5Oya3YotRj8gNOi5l63anCkZw2go6Q15PQpiqXVau3yxTvQDzFqkGVmEHRVD4jQ-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98338" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98337">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
سلفی ماموران امنیتی فرودگاه آمریکا در بدو ورود کریس‌رونالدو پیش از بازی با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98337" target="_blank">📅 20:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98336">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
رونالدو در کنفرانس مطبوعاتی قبل از بازی اسپانیا و پرتغال حاضر خواهد شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98336" target="_blank">📅 20:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98335">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaaGVHvQzkjHQiHGtQ06VqtCtijvka3Kv6DQerB9rrWpGYEIDKq0hEoEJGs-iZZ8YNbkaRSAkzfQHXPMhY3Lm_SjaaTUoECQ-P92ld8eUj34dI-SozWAe3p79ufUOiJQXb93bCk183tma0GVRA5kwZyi80Z_2eyHhoeqMA1y4lgU9IvTlMc0drLve7BD1rPqs2KpoPS1IgDU8z3AyO1bgyLC13a65Lal49YqyFP7ZO9I-2ew5006RLAsrAdVjMBCcU1gBUZOvny_BEOadc2F2E8amg10Eh6pRmabCv2DmuPayMZ29w3A5jRlAPbr0Cw-ARTFSRGL81zE2Hvo0lE13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری و #رسمی |
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98335" target="_blank">📅 20:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98334">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW04WFGxa6IDwBTU4ghaBDLiJaq29PUHBZxM2oz7dF9txgacRI32NJueNFcsyGRB92_vNsmCc3pBR0pagTK-jJqZI1p6yb5cxUJuPJT41E1okfSw1UTmlu0Qgqw1IqrFcdmZ3P1NWiR51ar6r_3M5mbiC-r-73VeRAfXPyclBqgSKvyfSmNY2pdGwzcYYsNKqKvOW6l1z71uNMPXW9rJ181FJRKDIi8o_g0po-x2fy1bUIViVm8o-loIo4MJiw7IE1kjwGRzWJgCiVdRaDMIjyRIVBNkz-idXN8ETIs1O-XIY8G2Vn1yr7Ips2BxvaW9WV5Hwaefcdq_QIN4wCa89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
و
#رسمی
|
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98334" target="_blank">📅 20:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBl0vKiDG8PrQho9fyzQxUhWdYQVq4685yWP8GocJgtRFMBzvK8BEXrm5SbS1aYH1tNjx5STw7WO3udYjMO7fyEDCpyELHr8cSQKaogMZmkw640XwjRjH8o3TbtcpDTYm1XibhSPvMjbfuptcXwJERpSdAj6M-bpKCI75JnHu9KvypXuJS68RvkjRuA_hoL4F6P1oikNxwBKqbcWvEtQyD_h0QTCCYrCTA-uDqCx7LxPgTmjNN3biV_GJYePNQRLosxTWcg3K3zk9m1RrL9mcRP6FXpo2n9diVzgFzE7XcUhpN-_zfivBAXCvaAj_sEImTXPqwkt0JgkMbatKOBTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98333" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🤩
#تکمیلی؛ مهدی‌تارتار برای تقویت کادرفنی خود بزودی یک‌مربی اروپایی را به باشگاه پرسپولیس معرفی خواهد کرد. شنیده می‌شود یکی از این گزینه‌های تابعیت اسپانیایی دارد و در چند تیم مطرح لالیگایی عضویت داشته است
🔴
همچنین تا این لحظه کریم‌باقری نیز در کادرفنی تارتار…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98332" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGhkJuJWyKmHVKCuxIKNUV6FtkU7aYdbEvceqoUXq4_yW6wUKyb9uac3DKqeGAkV2oqwEJzczpBZuKOLCQTatSfD6MD5GK5JDZN9h1XvjvqzckTR22dExqCnPOyBIumDGFKbVI41tAWGfr0Glb5sl56fRS-MgUrgQVwVhDU9JBPXEHVlRh_i8OVLGPDpurTz0cKwayY4jSYqXpq8KtSU1RIDseoeuB9-MjCX-Gf7m9VPog9RcsRtLLSP8QWHuIhEuzOYjOPsmxzg-1aAZIex_qX8nXrixICeK82ACE7UmX6liHBo43PhzjFYYF52jBC-k-rIDhWZ9pMfq_Vui9X9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98331" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZtblVgry6yC_PW-MIdaZeW3q86k1TdIWAlmLE4cXLvKmlWqKepDYel44amg_7ctXXT-CIAQR_wXvhZtdUB70PZKFZag2U0M189inQEZU5xnT2nrfqk1doEUXttbB1C8nOCqtP65N6Woeo5Iwam--C-q9C2FugfU5fZMbkRAsDZTMJ0RD5x63bVV5wbLmHpGxV42WZjLO1_iEpVnl8VlszyHtUzg6HlJS3-s2MG7jSj3OXg2-IJKFJgF2CO3aJjWEjUUR1eIqR14YVP6UWSIBBJ3YZMeGl-v_sub3GPlmonLqjcO4oZQgWOsL2Z1llUXlV5WACh-12XETj0s4nmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب مشترک بازیکنان انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98330" target="_blank">📅 19:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_PQ1S-zSxqrVpzyvo4NwIohrRid_LkYhMOyXNgNZ9MTbZZPHsiA68sbmlw32pdVT23fTisYJD14Jbg4H_hSshLnrCqs2jW8Qm_oC2o8PoR0NqTGCVoSj5zHDXUhlALkxUTnF1sQ6GUhXKf3jWL4EA4QwpQjQ7U1nTeBQF6QMheAbgLC3wC9JsY4AoBm8IGMSwVlAzNGAx79L4YFBFS0PONaSAXaExTtprc1YSuQRxtgWllqma0Sp-QxS91zLWA209TE_RPODcH3HaNnIuHPCGAhAsXs4y4iCAvll0eUMoNY1k2O9PnBvHQ9EThAkNbL2VsRcrq3hSFgdvhd-0XeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇲🇽
عملکرد تیم‌ملی مکزیک در استادیوم آزتکا
🏟️
• [89] بازی.
✅
• [70] برد.
❌
• [2] باخت.
🤝
• [17] مساوی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98329" target="_blank">📅 19:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy-TtPi1EX9TRBjoSbel_WDQ7H79XCr9yNBAW893ztSYzqESeZynbNOW7nPVZihwRAoxdD62wI19xnKKLKOKomg2w_DG-IXNDJ5CFLdNtcC1KFeCZ_3CXYpZHXeij57nw9j37kouB6-Thu5rcWwBzl-UwsHIMDTRlIFRV97SHawtfOt9-cMVgqKhRLr3zc9sRA9LHWOLWo2yTb7xKdpYH0PemTPT8vKd4fZRxi83xVNj-mdyqMRGw3p9sfM5yFNlmcDcx_GhaPRPT_vKdP_j-YjnsPM1QQmHi390_B-kPAV5dKAv7XZb5qqzv4YKCaOLU3DzUozkOSmE7b6Q0i-yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98328" target="_blank">📅 19:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7mhbs-fkHeVcmYC8teJL1xRuxbEQCWGrMzzUuX5GrOHsH8Wnc1TXp3nRpu8SuS3SxkR3a16PnirqKwligl-WUGvkpJHO7VODggIoX7F1WWXRnAHNGBltVLsj3JfIiP79qgedocwYbqw5ussfUCnGT1v2laYL3FogW116j36TMVjvbu__ucCLI3tblisa-Wz8lBFF1TFFU1Mc7NM8xTqqQqoAFf-WszJC2dsMyPhpAs_i-8Xgtv7vVzIGo92te3ujxg-U58uwLi_xdjstQEOSjCs-VpO23Z9IeDs108hc6yHVE91-3yzW8zo7FRd82CmbJzW9mCCrKebvsGnezdbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇺
🇩🇪
یک شهروند آلمانی پیامی برای لوکاس هرینگتون بازیکن استرالیا فرستاد، پس از اینکه او یک ضربه پنالتی را در مقابل مصر از دست داد:
‏"آقای لوکاس هرینگتون، اگر روزی این پیام را خواندید: یک قهرمان لیگ قهرمانان اروپا، به نام لئون گورتزکا، 31 ساله، که برای بایرن مونیخ بازی می‌کند (تیمی که 6 بار قهرمان لیگ قهرمانان شده) و برای تیم ملی آلمان که 4 بار قهرمان جام جهانی شده، بازی می‌کند... هرگز جرأت نکرد که در زمانی که کشورش به آن نیاز داشت، یک ضربه پنالتی را مقابل پاراگوئه بزند و شما این کار را در سن 18 سالگی انجام دادید. شما بسیار شجاع هستید و در چشمان ما قهرمانید."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98327" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_tWOCzSVaGBav7-QdxxSoWZWsp10pi7KrH521nezScAGJ_WgloFSLQAnIk3IJTZ0VXa3NNEk2FSrC7MwfATIm7cfqJv1rHR2BoxHKW7_u8Dgm1fmTabvyWVZ7zMqk7t0vD1qrEpA9wYQJ78Mk4qrqZTdecTGvvHmqKBN8BD9Nwfy-iPA41WJ1T0Swba219n9g1ZIPMd1TjQYLQ6AWwtJJEKHr2e2-l1yKK6428GHTUYmAdf62ro87_hs2lVbnCjWLnpK5nYP6GKSR41cFomaxR544Ft-wdVITzFGUGbJKaKvJXFUHBVHT5YjYrC6N-5UTOu8FM_-eeGowXkXGFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانس فوتبال اعلام کرد که کسب توپ طلا بدون حضور در یک باشگاه اروپایی امکان پذیر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98326" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98325">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98325" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98324">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98324" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHE0xR5nq8M058P5v25yVi7cM3j51E-vnR3drr7m50V1LirpK7kBSaKM1umyBhk8-hEmlhw9GGF1hPdsV-qu9jhlGtQmbZQXX2iZb2OTliXS7kojWHclvuIlSC082isX-XaGsZZ3HfPBi4a_-k8yC2xe5GiUszQIhPNoGhqwb1s8ms6r-3bz3du-ZyWjRjCoJHQUwzWoif5obucyeraTAgHEW3Jz2SuACQwFHN9FZZ8uM5TdrWrT2sHvupDDx_DTs8kqg21xe06HLEsoQdDO8uRXveXMhSEi48Cgs8-Wbbrr8FOkCwVTOAeC-Bglb96FVEQ_8wgIFisZQypYbcJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇳🇴
ترکیب منتخب و مشترک بازیکنان برزیل و نروژ در آستانه بازی حساس و تماشایی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98323" target="_blank">📅 18:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EucQ3z1OcsL8A6E2oKyG5eaYiJPvpVNJbP3XLzLoPW7dZ_sWyuFbIhQfkYdjYRyR6Bqx-8FaEuXE4mP12cxo73r9CRxQdsXQat2hzGra92eVAuGm9FK30IRatYGVxfTlwLWcp1EOWRR7ftBHONOef5TVRmvjho62F7iZdCqhDULeun0CPkSSfKM4z-4FrR449N_dQryh-J9DI6tVkvaxpuYJsWnXi_dbfstRaOD69pPX_-PX9qLDIqCKxUnwm4zhgNiEBRJGnvk1028I34pxNsunfwkYEYlNxJ7sAnytzrFJCq9cmnFTE3x1TCav7l9x__m1xl57fqx2jK5djMcNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بیشترین تعداد بازیکنان از کدام لیگ‌ها در مرحله یک‌هشتم نهایی جام جهانی 2026 حضور دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98322" target="_blank">📅 18:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jovvk8XhU6dlGWYjPhaQBky0_hFjdYSaOjOFHBsjt__RQu5ZqeNHJbAXvM7p1yZGuyqDo92WLG6WZiCGKI4OQun2hsVhjm4_lTUlZF22LC8bTLh7NnprhuXR0m3NEcSG0GExEyDdQUvcIf3OAX17fN1PQzMe8ROfAX6SnJPpe3wz39neG2kNuyhswtSgDFrBOFS7OD-73-Ivb9XB87bQnsAAaKdaq3sG1IGxkLwJoHdCB2mH1k8XEdnPFsd223I_AsiM4mNPugiJPJwTNv-VR91V6We1eoFLxo_JcsqTqF7j_lziF2HYAaCD-g869B6xe74MANUAaJAhErAdIrA-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه الاهلی عربستان در آستانه جذب فرانسیسکو ترینکائو به عنوان جانشین ریاض محرز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98321" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98320">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98320" target="_blank">📅 18:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98319">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98319" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98318" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
👤
⚪️
#اختصاصی_فوتبال‌180؛ در صورت حضور مهدی تاتار در باشگاه پرسپولیس، جواد نکونام به احتمال بسیار زیاد جانشین وی در باشگاه گل‌گهر برای فصل‌بعد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98317" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD2smHWO8AKjH2V4M7NKFOquvojr6_lV1H-V-zvEX0u58GpNRmbGHMz3JRtEVpOoQRnIR928z2Wy_ZUAp3uGaRJ5vn7ZjuaH9qRuKmMob18ALjvJRoc4l1kEBIZAeJWzf8j_k1pgOsFeRaXupBMaOZRpvgx61f0wtuniNU7Je1RXURKMpEdMPgOkoT-4_V-40yC6C2VXQWhs1RUZmSJUNgw1-ILVXlwczaU_w2wUbd3Z5QgMFvy7mU6YoPOJlEy8XmH9QssfscVt8m6YQVsxZDrBNmGRtS9Zf0vMSRzoYq1IXMtCK2ywLxoYqNJ00FqPax9IlTJuCGVCRpGyK1y0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
💥
گلر کیپ‌ورد و یکی از هواداراش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98316" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcqEzPzJTxW3MCkvJVgb3LELmLm0nWXHmeu4u0CNgb5RPXZ5yZF7ZKzC1OLyBuzAmWtGJVPguLG2J2WOX8pkw4TyLSdIHnqhxClyMMWGLc9_0zlgFypZXhPOhVCTGzmvHv98CoYZpbZAcXYpiQ4EcO-qNjS4MVZDa-jxizaomoqepJXEd2d8TUqGFWMf5AdClBeELX9KqstRLOrBqJSGr9F3V0VgfCtDMVxXJlyK6pJpvqh8mTyS89rbTbAtog391ahUvDEOGsqSNcJ6y4Pv66KmQhQ_kg0oJLI-jOv6CyQQ1Jyvf13aoq0SAavY9XQDg1Mqye-c6zDo3s6tnRr5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
دختر اینفانتینو رئیس فیفا دیشب حین بازی مراکش و کانادا با کیت مراکش رویت شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98315" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98314">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98314" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98313">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98313" target="_blank">📅 17:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98312">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98312" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98311">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98311" target="_blank">📅 16:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6IpgpBlEmUda0DhgZiKFGzH4_CEBqrW2q9sYNuCm_mHpGg183cIaSbgv1y8iZYAgfJCEewnroVhtPbVTqKkk9mVFyVALzSJkKfZkf9JOFYFbSf6ODCwsufa3-SDUCOXDuLW91PxaIkwqAS1HhQVUiAJd03Y-1lczg8d7INb9V-pAvnHDxbNTRLI03UFd-4N6rCIzVmTjtK4jxPrDE7RVwdFFtVc8E3PlWZaSYSkxF8QQsenXh86X1OCSGLdOFiGavkq1zN8AllmLIiVNp1Qivr3lelgiSPMJPJjzWEdc0DkI6GD_70ATwJRcTAYXoViGBX-EpGua2TkY_Uh4cCb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
📱
بیشترین فالوور از بین دروازه‌بان فوتبال؛ گلر استثنایی کیپ‌ورد صدرنشین شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98310" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98309">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98309" target="_blank">📅 16:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
انتقادات شدید مجتبی پوربخش از رویکرد عجیب صداوسیما پس از حذف ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98308" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuA_4gqxMSs-pzxNn584Kryil4aNBRlnPpMDczuxmXVyfsNNP3YF0SuGZxNGZEehvNk7UhqDnQyEzDgUTbk9eSws-l1rRDLpsmOMNBK9GpTP0e77Q3SiqshfxY8lJdp84EZnoK0hoZTVDyToo_L0UYVh85Wz1SXJnlpAVom-jnp-wgy4v1nIDU8k1fgzaC13MURm1_WAg1DL5Sh_ut4iI-C20CBTQ34YO9g-BNtDKTZAWvUJjU0YHu0EQmxNwQh7sMpSlVQKoM2TJqBIvMERYr5QiadJbKnfrkl5CzaDolCf9UorzRt7NmBAAEWXQFLcizBUCMoPc7LK8QX2iMjXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98307" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98306" target="_blank">📅 15:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98305" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaXN0KR8xhTxhz2GTBQYQKGIFYKFouASZiydjQFQ1EK723h2kPY_3GRoqH-7N-QG5DuNEwgVwlxnqo2FxdroBWOxDNLOi_bjezE8enB4yxmoRHoUXJg09a28jYvwZRMqZBRddCReuOctCloC-1y8iT7sDT3R25THmFfqVbW_o_wOOUalVree-jAScaRMzAmBF085wXBwARaMxt2jitc9c7Tz4ACQU4o-zcA4aMmPOV9v24qEAQCOJKTkjp_4XbrSmyZMzxNhYfdLTxHGTQk8wTX3WG9U3kHtK6JPd6Xl2vnHEg0YkoTRUlBOtYG4mvMiNFO2-9mRcESmarx-DLU3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
یکی از دستیاران مهدی‌تارتار در گفت‌وگویی کوتاه با رسانه فوتبال180 اعلام کرد که مذاکرات پرسپولیس با این سرمربی درحال انجام است و پس از توافق نهایی با گل‌گهر و در صورت رخ ندادن اتفاقات عجیب از سوی بانک شهر، این سرمربی به آرزوی دیرینه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98304" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98303">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98303" target="_blank">📅 15:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek4y4_dUdF0nXxBKmDg6YkDXROBBs3OnlLOL-4LeUYqoMKiwn2m4DzctPj3KgMdYcrEZTaJ1g8WDM-DqlZIGbLa1lwUMNJmCZM5XpfMudLfyMq-VVn9MMNQVWIX8yh4nCQ4nWylgUcyBRNn6tE8wqFYydLTtdhl6Jkqn8C-itHNmUxarS1B2JcIxwkIwUaqEHZWdWXD2RgkQbMon11Y4pY9qxmBBBsugqK172jFssRoXn6q-zHkGEHkrFsQSngzMEm6U7t5XN2YLBZWdQfPnN8JxDXRUtd6Haep-53W3-uR9hbeuqNBL_4xrb9EBCCczeQim8SKDYy-1RYAZAPJotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل 3 سال پیش تو دسته 2 پاراگوئه بازی میکرد و با درامد فوتبال از پس هزینه های خانوادش بر نمیوند
حالا بعد 3 سال اون دروازه بان اصلی پاراگوئه شد و مقابل فرانسه و ستاره هاش فقط از روی نقطه پنالتی دروازه‌اش باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98302" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98301">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98301" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98300">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98300" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743a223544.mp4?token=GdspqFvS7qaL5EyhWoH9C4cuwMBGjQsL03r1e7diGolovg0Zor3sjwPYFpBhTPjZhyJBXe0bEm_gnsHSr3CO82wd6UdllBaXbkLv7bRiH2YuNekoGfSUUZuBHY7GB90HOeWb5Plyv1BTMdGAA842NfMLLANa5HSQ32GQlGVJnO9ZyhCzrfcBL0O5MBQsH0p5qFeRfuVqIv2YgfCzjebKGJq34skKnKbxwfnRluBOqh_n4uL1DYkpmrE6KaoD-XTh5CwuK9sz56yIx-P9QtfZoxJpFl_iHRqxHwFixuF9AWEMB6UzOiW6QcprDLLusInYM-Ns5RTmLbSWU35IHrM6jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743a223544.mp4?token=GdspqFvS7qaL5EyhWoH9C4cuwMBGjQsL03r1e7diGolovg0Zor3sjwPYFpBhTPjZhyJBXe0bEm_gnsHSr3CO82wd6UdllBaXbkLv7bRiH2YuNekoGfSUUZuBHY7GB90HOeWb5Plyv1BTMdGAA842NfMLLANa5HSQ32GQlGVJnO9ZyhCzrfcBL0O5MBQsH0p5qFeRfuVqIv2YgfCzjebKGJq34skKnKbxwfnRluBOqh_n4uL1DYkpmrE6KaoD-XTh5CwuK9sz56yIx-P9QtfZoxJpFl_iHRqxHwFixuF9AWEMB6UzOiW6QcprDLLusInYM-Ns5RTmLbSWU35IHrM6jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق کیپ‌وردی‌ها توسط هواداران آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98299" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=VhmRsbudPa9F7fTyd1WJBiWPSg-QBa_4JdE-xLEscPGBbzrgID-69UulDZwUcq59puWL4yWDqk3LUv3NhdpJL9S4sMpTCDcr0lUyF1mJXs_STH4U2mtj3ao_4k31h30xEQovuusZcR38p5e0AGe5AseMAdKevdHyJ2oo-GfutQzSrZJoJuq7Vul3PBvC0F1PICf27Y-86PBRvXzd0vbkUxZ_jiLQ6ayLrID7Wg5hdEMGUFFp-t-MkZk54_IEI2f0gGkK7_7hmcEJkpAndz9Gl4V4i8yyKM4d5u70JX8cee1dJ9-jtWpWp_htmnlnCbZYAgIJF_d_49VWVU4Rw1lTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=VhmRsbudPa9F7fTyd1WJBiWPSg-QBa_4JdE-xLEscPGBbzrgID-69UulDZwUcq59puWL4yWDqk3LUv3NhdpJL9S4sMpTCDcr0lUyF1mJXs_STH4U2mtj3ao_4k31h30xEQovuusZcR38p5e0AGe5AseMAdKevdHyJ2oo-GfutQzSrZJoJuq7Vul3PBvC0F1PICf27Y-86PBRvXzd0vbkUxZ_jiLQ6ayLrID7Wg5hdEMGUFFp-t-MkZk54_IEI2f0gGkK7_7hmcEJkpAndz9Gl4V4i8yyKM4d5u70JX8cee1dJ9-jtWpWp_htmnlnCbZYAgIJF_d_49VWVU4Rw1lTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
خسرو حیدری: یه بار تو تمرین تیم‌ملی سر توپ زدم کی‌روش نزدیک بود کونم بذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98298" target="_blank">📅 14:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7nQ7eedBRbFfUEgGxaMVTpil4EvQOJpWcdcuqA1EVbtMLqCpr_MiXomsOwgYB5t84KUA6KJHRscHEOnmTkEK-PYIZRDmWWTuPJDMiy5e4L_VTce0fGEkI8mD_rdfz_oDfS3NSjkKUyD30jhWeFGNq46Pu-pMhFaJtLEBJsqWeyNwLG6kJ8D65mSIC6mLMdb_IfeFCvoukVSyvWeDC4D_I6CKTBJN7Bhut4J2C8p5exSpo55xgYKiDfQ4T8FWL8oKJYKyn6l5zQJUsFi3mMXHmgFrZMjXgIyX5vQl-ePlYJuHYrLijdIFPWxWQsMjIwTAGzG68nPV867eDZSwctJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
محمود خردبین اسطوره پرسپولیس و دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98297" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbCynxt9twVno-483uxSO1fCWKbVDySYlrUP-8PdVV03Bm2q6UpHlfCU_gPzK5PIHLzSX9TbqNJaJgSdRdUdMGNrc3Gdc28XHMarGqu9uTCDaVXapglgPcszj_tqvhaMfcmGd1w-hWNjSINM_BgCp9SIKXszH99_aFTCBpCMOfLEgHwcR3-SmMae_sRBXpEeI0jUtH_sceT_2eYE-Rxmz6s2cSbh7UFOEFl8H3uJj8w1j1cPFK5YPaP5ROOyQky36kYNQ7uohDlFI3FF1L7_PYvMfXl6C4CnZr88XN0O7qaF5hPZrCQskdjaJOhefpvj8NKxcLsDfQUEoRQq8vsCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
پیشرفت چشمگیر مراکش طی ۱۶ سال اخیر...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98296" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRhRpC0mtdPj9RRmn7NTWl4_AERvbuUZi-vIgl05_s0wN5KOajR9g5DzvEFIuL1iyrpGcL5_PdZxrnaaVu6ePa_lZm4-4HnHQmx7ifGcj52-M96Y-hOU2kMl0izSE8LzusxRBmyka1lq5rt9YWC1aiYeyi2b6kh2p8QKHX23iosGm5KoXyuNoy4dAQRBp1qjniwMRBA7wOdsx7tNlrkwUr1jhgYt_rFu8i5twppXf-zX9YMDos3FGDI0JWfgb8GUitMnk1VB49uH7MIuodFX1y7Fz4n23FYkinl3PMiQHxtI0bzRA00epv-GakhAN8vkWHes79sslrHUqSfSzwrDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گریه‌های علیرضا دبیر در مراسم علی خامنه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98295" target="_blank">📅 14:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4H5zDx11WQi5EnIwZTFkCfVriaxnp48vEMZbxEb0LVqKaCZtEJRlbU9bAnwakyLNtuoUPhywNvbcjM1nslbN3covSwzwQ5wNPEM_frEI5bTemMz5uKB6eYtULMLXEgn5ZpZjdG61qrr4j-qHvcqxDUJ4ZsWq_fFgzTPnGTwulqEn9xXSXrJaSQH9iFn3ERcj9iues2e5wo2-9iIAaK0rRTBpWKCUHGo1L6aKnDdGqv-mD4qgdLgx6U3p8IQnRwExX96BguGpdyNCt8nz7VsejQi-ayb-8YLiXuO3CPH_Nrp_XnQZ1nOUlReWqfQL_jpWRAU_B4PM9vX8PG44hQplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ دومفریس مدافع تیم‌ملی هلند با عقد قراردادی به رئال‌مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98294" target="_blank">📅 13:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=WkhcGoHui0CtloJPG_y313HfKwXTC5fLbQjHRc8EpdAAl5WdX7vcMMFj2x9zayq3Jl-zStB9Vr4euHRdjfQ-_Z9f3OHIj03EkGZM0iYnsy2Q9qD8c-mewHF3URtcJu1oOpppsjrAZf2pNkpxcqIiaR0T3i2Su8-vX1H9KwC-uiyLBCLb_0idayqC16ET6nvNbKZa9Dr5sejV11vhtOJCkti85q1hv2YYA4keHWEXa5UddlV5A8l9QMb0xf_qE_h-UZ5fcgU0Pi7bW22z_FaMRaEx4woe1uF-4RMMoEjeZe9xwaNqpHNf1NuBsB6yj7GCM4Q7ti-bhIoKRQmnzZNhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=WkhcGoHui0CtloJPG_y313HfKwXTC5fLbQjHRc8EpdAAl5WdX7vcMMFj2x9zayq3Jl-zStB9Vr4euHRdjfQ-_Z9f3OHIj03EkGZM0iYnsy2Q9qD8c-mewHF3URtcJu1oOpppsjrAZf2pNkpxcqIiaR0T3i2Su8-vX1H9KwC-uiyLBCLb_0idayqC16ET6nvNbKZa9Dr5sejV11vhtOJCkti85q1hv2YYA4keHWEXa5UddlV5A8l9QMb0xf_qE_h-UZ5fcgU0Pi7bW22z_FaMRaEx4woe1uF-4RMMoEjeZe9xwaNqpHNf1NuBsB6yj7GCM4Q7ti-bhIoKRQmnzZNhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماجرای درگیری معروف علی فتح‌الله‌زاده و مجتبی جباری را یکبار از زبان خود فتح‌الله‌زاده بشنویم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98293" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbksF7g2rbfAukLQbQmX2FX0s5caAqwCH2fEo2c7_kh5d3te2pfT84uEX67ODn4Jb-LNteF82UzB6XtjXaXRtIn5Gdf9xAKMqg5O3VTJ73AChWmJ92DVUZ-bOJMSpm1NpQl9zXevDO2vRipiU_pTLTYrmHGtJtPW3gQE-jlcTuCTTQdkKnNm-e0_yoTKpdHEuJ-c0-BOdVi0k5SgBQ7vqjJaUv9sl82ffqN7MNgcXkldvyuy84mCb26Opu3vhaO70XEasyT_2rEgaN7-8yd7tDJCY2QVyi_PLfde0tbxfBRlnrq4km20EJcB96zBeYIv2RiMYdmUawtObWzl69ZKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کلوپ به عنوان سرمربی جدید تیم ملی آلمان انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98292" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98291">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=jCRECiEE3LwZOzJqPVB0Ugkgpl9bfr5NaHJRXoqC1BYeTOGXf_T1_u6OfMoJEsXYYbpEi6uFGRA9TN8fAKO_-UBn4x8GyuITtzNFuGAq_ahC8NttLPNIMZS1ELr_rQYZl1Hko7ywUNVvU_0BnTjNQHWMqiv8ghWtLYjzK4YNm1Sogv4UNivRjpOApllnxabrzSdsH3zP5c7l8hv-e8PmOTTtCIrAM9Cj2xnP0amuCIhViI0BWBu7K6ghJrS6irlvS6Zuig1q-ay9RCdfJ8xno2zkuQT941lH3KJ8Ki_Z2KdxmVN14S67KNviLXmQVftLHiydSs5ZDdlU3Jvfz8_NLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=jCRECiEE3LwZOzJqPVB0Ugkgpl9bfr5NaHJRXoqC1BYeTOGXf_T1_u6OfMoJEsXYYbpEi6uFGRA9TN8fAKO_-UBn4x8GyuITtzNFuGAq_ahC8NttLPNIMZS1ELr_rQYZl1Hko7ywUNVvU_0BnTjNQHWMqiv8ghWtLYjzK4YNm1Sogv4UNivRjpOApllnxabrzSdsH3zP5c7l8hv-e8PmOTTtCIrAM9Cj2xnP0amuCIhViI0BWBu7K6ghJrS6irlvS6Zuig1q-ay9RCdfJ8xno2zkuQT941lH3KJ8Ki_Z2KdxmVN14S67KNviLXmQVftLHiydSs5ZDdlU3Jvfz8_NLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از حماسه تاریخی محمد مایلی‌کهن در گفتگو با عادل فردوسی‌پور
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98291" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98290">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98290" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0306de1296.mp4?token=Tu4XvpK209lfAIi2Cv7rv-uraoxwCQwCsqbi7Q5H4qd2Hyw4Dklb5Gof6EGeLnL16gisFzTmGL_ZCABu2II3qoku6UzNwYSeDOkGily_Y0zXZW99-jnj1Fq28kmNyk80oKQ2ui2WXyyrWtefdBL09IOnPGMHI_iGipdE6N0gP-_Ogx-_yJ_9pyGVjT9Kg7JPFF07ko08o81H_zUCO5bMWomhZv8JUaDG4q4KVJrEQ_6Do7qAE7ougKngikaNe6JpMCv6Pb84xjg-jhAy9S-rUGGJ8nV-rPq9S68gRuTpb0goH8YtXQXLvRZDs22JH6T2JbjYAfG6jCeKVlCRPJca2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0306de1296.mp4?token=Tu4XvpK209lfAIi2Cv7rv-uraoxwCQwCsqbi7Q5H4qd2Hyw4Dklb5Gof6EGeLnL16gisFzTmGL_ZCABu2II3qoku6UzNwYSeDOkGily_Y0zXZW99-jnj1Fq28kmNyk80oKQ2ui2WXyyrWtefdBL09IOnPGMHI_iGipdE6N0gP-_Ogx-_yJ_9pyGVjT9Kg7JPFF07ko08o81H_zUCO5bMWomhZv8JUaDG4q4KVJrEQ_6Do7qAE7ougKngikaNe6JpMCv6Pb84xjg-jhAy9S-rUGGJ8nV-rPq9S68gRuTpb0goH8YtXQXLvRZDs22JH6T2JbjYAfG6jCeKVlCRPJca2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇻
نام ووزینیا تا ابد در تاریخ جام جهانی خواهد درخشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98289" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شادی فوق‌العاده سمی هوادار کلمبیا بعد بازی با غنا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98288" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8g_66ZAeXG736CbiR_3HS41Vs_DLQ4a0E1o1o9gs6PAQDETJeHCDljbeWE8gidGKacQTk4a1_b-Nos6jeyLtQe9Fxaysm5Qzioo4d_CHMQvnIsjnal7m8Hz4yXRUF-DRvysBUUwbr35LOvSns2fBYhc9xUv68V9VvPw6VM_2LtxKE3M4R9niC9l8avD4oyUFs4Cl_uDvIIcRZFmAB8SlR0Qck6RTHXSIGDKRgIdXRpz5BGJWyuoJLzTOw32SM72U63pjw2T30cohqwUiVrhRYIh9-d3uLUqta2pB8ftjh5oJZwmzUZXloNLPd6ZtJjTSLduNg8S-8swWg3GQPA4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=HDQ4uqmyhExoIa0FXct6zeSGb1wKDqlO6ufOvwjoMSoTIndjVK_U6gfnnqCQWwQBsyOShCvpV_GlpwIr0MT0Pm8e5K9VQFrQeFG3ykicuRss0ZshnsUi9rxPtaTWEOpA7XTEABIJRaAqCNeapR9hFNnRs_Z-DYN1G5V6na5thwfp6KWNUSoX9AaM_V5N87TGpSV2RWfvRZSMRXbsKzKa8FGw1M5qoAn-SFnhrOlw1G8JHpzIqQxI2odN5OjkdYrbgJVEpZxA5eW2zrh6Iqx67GCSTaFue76q_jhLEAUnhw7tM-RuydFGkYfdYbSUWwCysy18KDu-_idYQV3y1AD9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=HDQ4uqmyhExoIa0FXct6zeSGb1wKDqlO6ufOvwjoMSoTIndjVK_U6gfnnqCQWwQBsyOShCvpV_GlpwIr0MT0Pm8e5K9VQFrQeFG3ykicuRss0ZshnsUi9rxPtaTWEOpA7XTEABIJRaAqCNeapR9hFNnRs_Z-DYN1G5V6na5thwfp6KWNUSoX9AaM_V5N87TGpSV2RWfvRZSMRXbsKzKa8FGw1M5qoAn-SFnhrOlw1G8JHpzIqQxI2odN5OjkdYrbgJVEpZxA5eW2zrh6Iqx67GCSTaFue76q_jhLEAUnhw7tM-RuydFGkYfdYbSUWwCysy18KDu-_idYQV3y1AD9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Ro1H0nDIpGEccCEUZ-CiQD5t0k9EeYsIM30mQpmDsv3P_F_mpPaD5DkKPzJALPnwQdIKPTrDvHJ0ydmTUEme07wcfNjkyy7hxXU05nYqGVRi9WCl9gclvWWxtu-husWVyRRV1T556LqVjWTNSw_HFcYIevAvYqq5631zia4ceM9e-dVyqRIFiqL86s9-G8y4tnc7WKhVmjvK5VeAZIevdpR1TTclCcqrRC33Kc4efe5amj8wyFzavBOcCbXurD2GKvvvzALfbVwOyw2EiO_4B2rgcdszheOzr4WyA5LdZS9yQFleQIePwnfr4KNbXd6iGXlhGzPL-GeUY96_CIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=gWQgNL4JvxgtIoOYDQV4ahslR-HFbQ__RLCFK8h3g-JeepjiuZ_ZjUxSuyTBG3toRwFi9W4OSQWGXkWR5Hd6llChj2cGOX7sUmZBYHkT2Snn5dYFzNp3b4jGXMAVOzt8B6_htGDvR99tH19b1K1BBDonmmEMnc1LpiE93Y_N34U80TfMD5Un2yk85bhMJ7irq2w9DWCu5JNWiYxIoUQZOPyEP2AL-Ujaoslra1SJkk4_AMFYBmbC1kG0kPtc_5FiIgO_EH2T5vIOZKuPoUcXcPKgZ7HjE9ftZ-ylr77FcpcU_HyVBe2zyGE8_YZutXxSxskwpC-DZYZ5yoHumaPCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=gWQgNL4JvxgtIoOYDQV4ahslR-HFbQ__RLCFK8h3g-JeepjiuZ_ZjUxSuyTBG3toRwFi9W4OSQWGXkWR5Hd6llChj2cGOX7sUmZBYHkT2Snn5dYFzNp3b4jGXMAVOzt8B6_htGDvR99tH19b1K1BBDonmmEMnc1LpiE93Y_N34U80TfMD5Un2yk85bhMJ7irq2w9DWCu5JNWiYxIoUQZOPyEP2AL-Ujaoslra1SJkk4_AMFYBmbC1kG0kPtc_5FiIgO_EH2T5vIOZKuPoUcXcPKgZ7HjE9ftZ-ylr77FcpcU_HyVBe2zyGE8_YZutXxSxskwpC-DZYZ5yoHumaPCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bphdp9I3lJ3U1M_yBbrlaHCTviaiusVByj56Isw_u4pdJhGWugRQ0VKREZOqZdMql89mZtczkVv2HPTy4MjblQkaw37eXCHR0yWPRHCRkgDJgzrCD0KCKLCtMp-oFOrJvWo4rjhWThVuAxeY6IFWX2z8J5Ow1XTdDm3BoPuijhDe90XgOkgEDwuweNI-eDlI5b4kDQNMdz85bTfI6dxcgZmKAEDpPWM-3bt5lixhVj2KjcQGuAb2fijY1ojDQ-ZWf8kHDJ1sYzVUA7c9LWwhwUF7cKMSrscQq-VtDmqcaPE7YTScx9cPtyJ8r-yZWbbOODjrfWEIyjfGOKzmQ-Z7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=MuJMpy-FzJ3LvQgwtPr59_D-PeKS4oollshPwoP-T4kQtbsINUT8kCDqbwp2GZ9V3wgADmBA8r6vKHyCwcU6mGPu0t8SHf_KcAzRi3Ro_D_3YM6EoNDquds5kKIDfx4SFvTzssFI6d0dPKFJ9tvJoz4OoNM1NklnCmE-Am_6HfyaNGrZtxrvK19qfmwMxeD00hw8fE-fajIaDW74-TiW0QZlqpaO8aS_9lIAZ4Hrrn85PHn2Bg6ksU4v5FjodokrQJAS-ls8ykmXTaro_UgNjr1TfKVOo-VJkslkdK1HOVud-yAigaFMyvrW3OHcrfcOYq-26nZT8kkwrmCflFyuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=MuJMpy-FzJ3LvQgwtPr59_D-PeKS4oollshPwoP-T4kQtbsINUT8kCDqbwp2GZ9V3wgADmBA8r6vKHyCwcU6mGPu0t8SHf_KcAzRi3Ro_D_3YM6EoNDquds5kKIDfx4SFvTzssFI6d0dPKFJ9tvJoz4OoNM1NklnCmE-Am_6HfyaNGrZtxrvK19qfmwMxeD00hw8fE-fajIaDW74-TiW0QZlqpaO8aS_9lIAZ4Hrrn85PHn2Bg6ksU4v5FjodokrQJAS-ls8ykmXTaro_UgNjr1TfKVOo-VJkslkdK1HOVud-yAigaFMyvrW3OHcrfcOYq-26nZT8kkwrmCflFyuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=cPP5o-7okqwbcGN0lEUA1iSIX5Ao-Mq4C78oK4aMwdKRQ4BUICcy6jBsYJHW3a9JkZR0m8qrK3AmYuSgUj5lOyA6umX4cznnJhaS28fjL_vWKVXWVwsyhLuFwy_dy06P-Jee937_Z6fb0-lHBCUqchBnt8SnTeJwTR4VDqIDuYxwiYIHf0CkWHyzb__6xpLOYxcAMUfGrgF6d3Oa0mJupxePTwnOdXwbbgXMPO0MJaFPyPpf8wHRbxDcs8zCvbfcV2DNasx6SJW_WeeNlKWY3EK3NF5ZRaEn2k5DHyPwdnCPuxIsdW-XImBwP_YFixwsU2tofWuOyhLi7aBFUe-54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=cPP5o-7okqwbcGN0lEUA1iSIX5Ao-Mq4C78oK4aMwdKRQ4BUICcy6jBsYJHW3a9JkZR0m8qrK3AmYuSgUj5lOyA6umX4cznnJhaS28fjL_vWKVXWVwsyhLuFwy_dy06P-Jee937_Z6fb0-lHBCUqchBnt8SnTeJwTR4VDqIDuYxwiYIHf0CkWHyzb__6xpLOYxcAMUfGrgF6d3Oa0mJupxePTwnOdXwbbgXMPO0MJaFPyPpf8wHRbxDcs8zCvbfcV2DNasx6SJW_WeeNlKWY3EK3NF5ZRaEn2k5DHyPwdnCPuxIsdW-XImBwP_YFixwsU2tofWuOyhLi7aBFUe-54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=NS9XDRbPde5mMwjdw7FCxmIgz1z1eL4DhQQDRdvmbaQD7O5HGOBUB3d0X21Lo_ts5xU1vEfqXqK5Sc4sHrlX0DfqtoS8ztNrqJCNIZqbtrxBmGBZ1hOf0-aEeDyWtzQ6KmgQu90yHOqgdUwLD3KjjmyjkiOJ0SxO1XYcktSy2ZKUlVuS6guPsZO_VILSGxsh8-WF2UqNeXEDfME7KHer7yqMcXGox7c5aB-K78y7n5irYRBVlo_V047Wy4h0wahqauZYkX07qK9S-l-eJRKN5XxBysZlhmXmyYEhU6lV0oWEv3M4p2BDxlfDhaS_wchqDHnkUEy4UYzTmqw6iq_xfAQKGteghH81lENNxjmlgoe84e2YiJOVnSmhc1gSW7sKXrL8ZCycL2K-EZYWuJMZ5zc83hCZ7LIrNV5T9dj0fzYSOCVQ7hqb4IDbO2XWEbKeHGIQISURQus33qGEDaV403X7QU2h65Q-36uGreTmIo1wK3Jp_aisbyU0WeyV_xu89kEhXGlSV3FG2DvA2kdn4U3G0KZhb22ZVa6cr-_QQ93KJjqnxacmNFUcSLj0Rho5i4-MtKWb9RHeTgEQWZk8gKlKgXEUqywOoGcqWDejl7lAKN19907wAoU8esWtr0q2KNjlLZ8oTU-8ZKka_jte_3vwYtc_dt5dVZFgt6F-EcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=NS9XDRbPde5mMwjdw7FCxmIgz1z1eL4DhQQDRdvmbaQD7O5HGOBUB3d0X21Lo_ts5xU1vEfqXqK5Sc4sHrlX0DfqtoS8ztNrqJCNIZqbtrxBmGBZ1hOf0-aEeDyWtzQ6KmgQu90yHOqgdUwLD3KjjmyjkiOJ0SxO1XYcktSy2ZKUlVuS6guPsZO_VILSGxsh8-WF2UqNeXEDfME7KHer7yqMcXGox7c5aB-K78y7n5irYRBVlo_V047Wy4h0wahqauZYkX07qK9S-l-eJRKN5XxBysZlhmXmyYEhU6lV0oWEv3M4p2BDxlfDhaS_wchqDHnkUEy4UYzTmqw6iq_xfAQKGteghH81lENNxjmlgoe84e2YiJOVnSmhc1gSW7sKXrL8ZCycL2K-EZYWuJMZ5zc83hCZ7LIrNV5T9dj0fzYSOCVQ7hqb4IDbO2XWEbKeHGIQISURQus33qGEDaV403X7QU2h65Q-36uGreTmIo1wK3Jp_aisbyU0WeyV_xu89kEhXGlSV3FG2DvA2kdn4U3G0KZhb22ZVa6cr-_QQ93KJjqnxacmNFUcSLj0Rho5i4-MtKWb9RHeTgEQWZk8gKlKgXEUqywOoGcqWDejl7lAKN19907wAoU8esWtr0q2KNjlLZ8oTU-8ZKka_jte_3vwYtc_dt5dVZFgt6F-EcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=s5p3w7njRP3Jk7veX2KWaSyCLf58mhvlopEnROMhJuao4lMAaq1ownYSV-MS2iBzPcLj-LVRAN1y_H1r3ry_UvGRfix5kdUy3TqD2LpbeyIqw5oAj2RW35hJWhJ9QPIxWmANi2TmK-RJfa1xIafln3_bzDL116NGXOHgwf0hp9tUjpv6jcGDRbKGCWMkjuepGbkWvBGJPyG7FuauSrJKcuLh7AixIPbWMLjtyawIRM1XGMo2WVnYRDDlRvanq4UVgR4WnQc4-h6FPhjondpjP219SYrAwXtC3Qyf_z9Tr98P1_wHy3lG5xZjtR18sQIyljiXem3u0rORHCcZw1fCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=s5p3w7njRP3Jk7veX2KWaSyCLf58mhvlopEnROMhJuao4lMAaq1ownYSV-MS2iBzPcLj-LVRAN1y_H1r3ry_UvGRfix5kdUy3TqD2LpbeyIqw5oAj2RW35hJWhJ9QPIxWmANi2TmK-RJfa1xIafln3_bzDL116NGXOHgwf0hp9tUjpv6jcGDRbKGCWMkjuepGbkWvBGJPyG7FuauSrJKcuLh7AixIPbWMLjtyawIRM1XGMo2WVnYRDDlRvanq4UVgR4WnQc4-h6FPhjondpjP219SYrAwXtC3Qyf_z9Tr98P1_wHy3lG5xZjtR18sQIyljiXem3u0rORHCcZw1fCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=N2wvNlpSe8u7NebbbNldcicRHnDYZkEGDPVYEgbbmKjyyGLiyVv2ngffTHd_VNt5IgL735u_JGaeK-OgA73tLxCTzmWQiOXgtyrmRBwuAvVScB5uPtzVCB5BGWiuplxA5J775PfxVCvSABaUg-qWuppiSSehUqsA_t3SPzNE_1JVpwtUrZOX00OGRcxNQINPtyXlztaQI6aer903K1L9Z2wDwIL3kvErIyPKliE1Xk6s_WJCPs-KMWVJ3-YBGoC67d-O8x-w7ob9UW6QIS_yvSPA02MGTYQVeEy6JNJx6sCl1Isyn522U0ldIbMVBsMJdSq8rSZ7oPUMdEQa8_4IJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=N2wvNlpSe8u7NebbbNldcicRHnDYZkEGDPVYEgbbmKjyyGLiyVv2ngffTHd_VNt5IgL735u_JGaeK-OgA73tLxCTzmWQiOXgtyrmRBwuAvVScB5uPtzVCB5BGWiuplxA5J775PfxVCvSABaUg-qWuppiSSehUqsA_t3SPzNE_1JVpwtUrZOX00OGRcxNQINPtyXlztaQI6aer903K1L9Z2wDwIL3kvErIyPKliE1Xk6s_WJCPs-KMWVJ3-YBGoC67d-O8x-w7ob9UW6QIS_yvSPA02MGTYQVeEy6JNJx6sCl1Isyn522U0ldIbMVBsMJdSq8rSZ7oPUMdEQa8_4IJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=AOg-Ce06jjkEQyYY-I_38HRaA_dm_F2HaEyZHbx3oEpTj-tjdWb_a4JPziyfAZM1bJ-xN3MdIZq4-SRngiefvBCqBMgi4MhsAHj1EpyweL6wBVFpapkobML-1ArLRTfgND_tfy9ahX8X1UQgQYvOKgil0veY12NPqIqm0-LCSgZ_kK3596ZAvMda98jLp3mS0MkbsvbjWbIOYidQkHbn_Zhcx54FRj_yWNtoKd4PfeTm2ALRlKPRaBAvBnukkTjm2wfe83Ips_vXBjlkBD0NM22zLcfuD2cpUZpYg0TPs5tcPWRmBB0LTbHDKn6BKgE_Cmv7DqcItvGAIkNYa2BQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=AOg-Ce06jjkEQyYY-I_38HRaA_dm_F2HaEyZHbx3oEpTj-tjdWb_a4JPziyfAZM1bJ-xN3MdIZq4-SRngiefvBCqBMgi4MhsAHj1EpyweL6wBVFpapkobML-1ArLRTfgND_tfy9ahX8X1UQgQYvOKgil0veY12NPqIqm0-LCSgZ_kK3596ZAvMda98jLp3mS0MkbsvbjWbIOYidQkHbn_Zhcx54FRj_yWNtoKd4PfeTm2ALRlKPRaBAvBnukkTjm2wfe83Ips_vXBjlkBD0NM22zLcfuD2cpUZpYg0TPs5tcPWRmBB0LTbHDKn6BKgE_Cmv7DqcItvGAIkNYa2BQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
