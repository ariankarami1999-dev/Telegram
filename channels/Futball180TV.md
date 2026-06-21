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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 704K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-94960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBIpuNtGEBW7BeknQYNq7eqGPQeyCZcX0cXimhATdtf_D-nSLsDyh8Rq_p_Xa4s-qpBxKm8CxrQgVTo4UlGrBGc0hgXkJWLke_wdMMPhmGYfzmIf6MAX21evalfkIXfOrid2_9PQgMCXwRPPJfRNnuYcioEZ95byXk1AXcY9bZ1B6xW2jzJkKAQvlnv9LmQcDrer2hudH4u_P6eQYa7I4Iztw5itQNVDpPVNGU9om7LYfqKisxmfYWevCzEKgHkTFSBbde14gdmaGV7K7tdEm-XMFzCz6BgFFMSCMmAJTrhqkp8I0Kc-gY7EVcB59bw0LX0remhZ56dL_PxPcK-uNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
آمار پشم‌ریزون تیم‌های عربی در جام‌جهانی: ۷ گل برای کشورشون زدن و ۵ تا گل‌بخودی به رقبا دادن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/Futball180TV/94960" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI8vrdBDoKiXPMsp-0iz-8IFM2gBlV2mJx_Rvm7h7IAYoMCcTjeiqisx_8BQkkPA445QOTeZnESeFOo_HyjsY5Q-AGLf01tJHboEvKv_7OO1MNk0cIlis1kbFnumIJ-mS7X28f4a-CK6gPgfsQyF54mgzGfPsFNNN2CZ7jrfrPAPpX1MAGgSFmkD3Mo-2folijw4gtWhWd93KCu11fi4-rgwAL5va4-It0i5d9NqDa6ZKUMgV5ZPtRPhgfJCLEQ61WzdKvtnYr4sOba38ygSJliyIvQ2hRV7nGevjY9hQ9LlnyHfzLR7iyirkEiUueLlTlcaM5r8TV638jfkpWBZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
آمار پشم‌ریزون تیم‌های عربی در جام‌جهانی: ۷ گل برای کشورشون زدن و ۵ تا گل‌بخودی به رقبا دادن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/94959" target="_blank">📅 21:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdjHTnZbv1q2onjHFKdsMFHlTXPmpZicAMoVt1XAGI6HS9_VoaERX9MtWUHmWsav12fQwzmTvi_RkQG9diDt1yqCFCm8McG275T_EbrcAnVbK0oDMm77Ow4yQLo0EFpxp4zIRXpTop7VH3CMJ_0bNoY_Kj9B6eBAnDwl2zrmyHolI08j9jq89A2upSK3k5MjHoq29x194xxdp0sNQP92nmobYHJpefGlW6qVdZkBak_cWCL-jlIcMeMuYOqLq3z8zqNS6RVBqM9sGFvSuo-lhg9da6lltwGJwnQGhpUKWsecF-1GBQ9SUPTqlMafhkqRva2WiVZtWM_-oJLDDrvzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
تصویری جالب از هوادار ایرانی در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/94958" target="_blank">📅 21:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFuqEmQrKPrVRfVs5p4cedN39T3pmskv4FNesBSmfe-iUmop_-_17RZeDUWLYxTgm8VgF3amCZmN-MbvWkGwqtD8Tk6xKDgHEBjA1rKfqANa4F0gYZw8LR9eBlOEK74zFaqLHHPebnhSJ1UQpOAzc9z04tlNQ0_RY0rgOdwHvP-CVesqJgaHBUNPBdBHRuhUP0fpU4Tl1LjTZaUZd8c04chF6pLDPLIVz20scldZISRR8sxV1YJQhnRmkIMMAavwxKK2ulY0OwENo7JWghSnx9A8gOAmFBbGQ7El6UJS70IrWOJQvLaNtA7z8IgLBYcsW_ViaSZrGNsl8grTQ3K2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🇪🇸
#فکت
؛ اسپانیا در تمام هفت بازی خود در مسابقات بزرگ زمانی که لامین یامال به عنوان بازیکن اصلی حضور داشت، پیروز شده است [جام ملت‌های اروپا + جام جهانی]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/94957" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXNTBB0DwlMy-seKSp9Ct5mzM9frwmvidPZOLAsPZmZvY7v67WMm43XPXq305ooApDIcs5MhefcVgNVPg3vhJhKKVIgbzO7_NnZ0hizDSRADXEeEYF4Ki4gVmUu1UbNaQ9gDE0wIluLNeDvwDYBvOfY60qJmSJjXs165kmMQm32szAXxVMNA93bGI_ufzRnmsqZ5CNuv0L6yi9cv0uCNL1pnM4e_FctPka8nv3fp1KvOkNwBfmVRQDdMQ1I3eGTj2E7zVeHtJnbwvxdQSXsSAsl0zAAMtSC6sLWI-Xt_CzG5J68yTUT6S-Pi1pITwpF5mq2-bG3iHikPgrvWD1XjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرگل‌ترین نتایج اسپانیا در تاریخ جام جهانی:
‏
🇪🇸
اسپانیا ۵ — ۱ دانمارک
🇩🇰
(نسخه ۱۹۸۶)
‏
🇪🇸
اسپانیا ۶ — ۱ بلغارستان
🇧🇬
(نسخه ۱۹۹۸)
‏
🇪🇸
اسپانیا ۴ — ۰ اوکراین
🇺🇦
(نسخه ۲۰۰۶)
‏
🇪🇸
اسپانیا ۷ — ۰ کاستاریکا
🇨🇷
(نسخه ۲۰۲۲)
‏
🇪🇸
اسپانیا ۴ — ۰ عربستان سعودی
🇸🇦
(نسخه ۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/94956" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94955">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8XWeuDzbyqNJ1kDyi-CaLt9601-3pHGbrMdquV0V_Kki5Xs2MpgJHBQpS5hElnL-FPwpVe-XjDTgZz6VVfN0SLRE8Vrd-1TlKG6F1J6P_sxhwPyXOLJnHSFxSTPdjuDEtWm7EURJ20AWz3kiYguo1FCS_Clp6Kg1wm4cCwfXhDkpJLnY7uSPEldbe80Is6K8LTI4Oe55W3iJRpl0eTW1Lbt3Rzv1ROLsJvXNp03c-ua6eUC1Ec4Ne2VVIIo_zgTb_0NJg9tvro0LP-ugkex-hSFi5m8So_6WmlgfByh1mY6G2XyRmimgjqsd7nRCZnxxjN81Htynw2FPaiwDckemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی سرخ ها مشخص شد
- پرسپولیس آسیایی با چاشنی بمب
🔥
✔️
خرید اول سرخ ها فردا در دفتر باشگاه
🔥
پوستر باشگاه برای سرمربی جدید</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/94955" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94954">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNmo3gGuvY26ybpRMuSQQwbikFHZWxQrvC0st7o8ftw_ZdN4oI1s_XuvsS_j0xcL4cUhxLK1KkGwhBykyOCo-w66B-0qeoYx6pMvYzUHvAkBxxR7NFvMev_BwHSV0z2FKGvZJpQsrQ0ln0Cmw_EEHmhUtmyyapBD_dV3A43ZZsfC0yGswF-I94DfeQm8sSf5qHa12DkKELpG4Il9wuSnWAiiC8YPmntokUMK_FKBd16xsqOKSz6THq_AknrAydk_aXuE2kdY5f6R6YPe0TZZvAQLmx7MUgoxkNelPZpASb7nW7mAOIelWSzUTG8hyaYzPpI0RZnMS8mp9TjY-UxOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت هوادار بلژیک بیرون استادیوم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/94954" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf3e66b09.mp4?token=M3GnmawaKNaDQMApAfVM3Z1LFuTWOQpZIwa0h96llTbCj0MnWheZlpv_v8u6gfbW_5-CtACH4s5G8mmF7aT0NqmuepVPxPUq6RX9ySMgNDxV5appc-VZXt3tfyAC1NAIY6s6zNmoMecjNkfuoGwrEPM41ii1Ky5151i72RukVlW_88-Tz13GnsKXgvWhXlLqPE1vOMild3--DRS4nvtxEf0NoVv87D1dfx99k4J0nLVvDqxgXe-T1OOJCviVV-EDesz4Me69t81SAdxJBq0OAiIIQYDT2XLC3xj7uDTUMuOxiGQjqrKXXwFqoaV35CR-TLrri_OiIrlhgTenMBs--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf3e66b09.mp4?token=M3GnmawaKNaDQMApAfVM3Z1LFuTWOQpZIwa0h96llTbCj0MnWheZlpv_v8u6gfbW_5-CtACH4s5G8mmF7aT0NqmuepVPxPUq6RX9ySMgNDxV5appc-VZXt3tfyAC1NAIY6s6zNmoMecjNkfuoGwrEPM41ii1Ky5151i72RukVlW_88-Tz13GnsKXgvWhXlLqPE1vOMild3--DRS4nvtxEf0NoVv87D1dfx99k4J0nLVvDqxgXe-T1OOJCviVV-EDesz4Me69t81SAdxJBq0OAiIIQYDT2XLC3xj7uDTUMuOxiGQjqrKXXwFqoaV35CR-TLrri_OiIrlhgTenMBs--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ تجمع ایرانیان ساکن آمریکا در محل برگزاری بازی منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/94953" target="_blank">📅 21:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94951">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUzQql_YbVUwWV_2LseeNvnmXG8vIywa1EAb07WH9POQMadXQJNJj86pbocxQDSQomh2fCB5uAC23tYi-ZoQ0r5nfWWT5tS23f0xF4MhwBC76YLYUqxMLukji34t4iA12Bx7saDW4EaR8UBuNAAN6TkcHW0Y3_iLZQTUoHeK18J1M8J-pIQ-E9aX0PtUcrpnVRh07uCttPYfPAEv9LTwIgJJvmP8Rrsl5RUinZnBrdSDKNpBxk39MCOFS5MEfSITAXZtzjh13_RuM2DGv_hWapMcMJMWkZg1nigA0sRhQnOfIYNzTXjCXSgadaqdjztdN7Xt07DaRukjkXoMuNVQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
⁉️
بوی‌قهرمانی و این‌حرفا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/94951" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94950">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-wLwp6NrErQ40RKK_H5svTwJcWC1jEf8mweb3_GETjtiuxVJrg2oz7Wj58t5_liiKB6KAjb3ryAIhXxtp-NprFI5k66App1piSmu-_MSOnEZAlHRAahdS7MjZ913wHZRvtsi0gp-IUxgLp5bIY9CP_L5Lsn6MM35FAcA172zu4KyMFxjCHc1KICirxjm5TXomfw3CwjOQepaze2lgGgpa1xUZ1Fma8Cl8T4f1JZjOvN8GCLwh9CSaOcjeD2CSwommwz5WdCEgMEo_PbzLPZIwrIXocTP4GbGQa2r61-QL04_9ncoLLtPWyCT06cljxrrbEafvhhqj2MPBlc9EQ2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
در جام‌جهانی فعلی ۸ گل‌بخودی ثبت شده که تنها ۴ گل دیگر با رکورد تاریخ این مسابقات که در سال ۲۰۱۸ ثبت شده، فاصله دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94950" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94949">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZozdqDtBJLTo9PYdDeVLGExjiOtcaiYjtqMDW9mTp-_UnYy3RGsIu9E9DxxzXnMooo2qOAYqpNLDUf5Ng-ki1h8FZ25J8eOQMcG8Jm6tEb0GQANKk6TVrOKP-iRbi9LYUZDEGCF_LE_DXoD-w19ma51E0asBqcU440DwNWI5tfe2iTyJ0fT63bR7qgD6msj9PD7odejaDEO63vBiSXVH_--rr5wKXMFgrbCdk_E8fVmFK5cMXO5gEOe72INn8tYv2_XBOwtpOfy6fbAG4oqJmYp2THo5eDGIs-aZP-3CXlxjs1AwqjGF0LI_TAepN_P7-oPmz_7Xlr7a8OdvuYLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94949" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94948">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1uZUaTcyR7SMv8Lu-qCnekk6RsCwbjBfTCEUvEvImvY5TEFoFdyxbpvU1utvCyuLy7YXFxXgUyTOUxCg_QMNcMW41s0QT1uBcyQjQfA37fpSteejOUaV7U9cMcl-V-tOsHDbQ4EoCVG2WGP9apYpI_ipeOOzS2GES41Scq_IXJKwKkbPYxBAgwITLYU49H6s35emLnm1sCV73BlOl5SxVNxwD2o7PE7AAR6THRZaI57KHwync20H0lVJHt2nGx0aw24x4KOD41ixz7Q7JhCxbY5Y67E5mlFA1gjbL_wGebM3IGhHFlKApE2YzA2u_6eLgC4rWVhfvclrh_qfhSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|شب تلخ عربستان؛ اسپانیا با اقتدار پیروز شد.
🇪🇸
اسپانیا
😀
-
😏
عربستان
🇸🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/94948" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94947">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وقتی عربستان اینجوری لنگارو داده هوا دیگه باید ترسید که چه عرض کنم باید ریددددد
قلعه‌نویی خدا بگم چیکارت کنه امشب سوژه میدی دست عربا
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/94947" target="_blank">📅 21:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94946">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فران تورس
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/94946" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94945">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc6utYW6n0gKkBz1NqhnZaiy8NIp6M0r5uX5IqnlEEFZqrReS8g9CHKDyEV7P8VioOddr4WV6aslr5RBMsd4zrADr_P3gfADu64R6L9PG3zwsW11R0xvqJGOJ9DJRuPs_gSEG5tmd9NFj7zM2XyNiogtZ2CiwGXD5d3i7aqreTKYRPPku4FzvxTnevBQExL-hhcoHNYIBzIY4iSrU9kyEhP0R-Gm7qa4ZUJH1E6eyJxRK22WgnUu_K0PRTvSfCkK7kUXREiPkmmy6YALngAz6S0LGrGsP2PLy1sYfMwI7NldudbU-dGUykHFRKxsugQDKZC6SfxB69yt1UZkcSo4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار عربستان قبل بازی : اگه میخواید قهرمان جام جهانی بشید به عربستان ببازید
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94945" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94944">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOnYrajRCgKWonDEqaWXb78bnNxTPH0Hq-h8SJ8Pya2jX8L_gDFkhnKZAf2nOv3sTgPgbfqfAaBJxeGYZti-vftntd9u47pE0qdEgt7Gxdls3H1krmhLcgUW8phh3MBknc0jdJA4sZHQN1VIvwYpdIWc8yJKHVR-Yb271qXjez9tRdHymlP198TDePnJwlPzboShHKDggLFdBjnhYSyCxsl5WR80FXQ7Rm9fxyeT9w5atMZAUzAcYRXyPbHSB1BcOg3_hzKx3ZktQR8VeXMOMYwsMhhgClyd97XyMDt8iSYEeegUuUu4WQHYA0lBYLOTYfPUalQRYk1i5BobrmjcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🇮🇷
یوز ایرانی vs
🇧🇪
شیطان اروپا
🔥
تاریخ‌سازی ایران یا بازگشت قدرت بلژیک
📅
۳۱ خرداد
⏰
۲۲:۳۰
🇮🇷
ایران در ۷ حضور جام جهانی هنوز به مرحله حذفی نرسیده، اما این دوره یکی از بهترین فرصت‌های تاریخش برای صعود است.
🇧🇪
بلژیک پس از حذف غیرمنتظره در دوره قبل، به دنبال بازگشت به جمع مدعیان فوتبال جهان است.
🏆
یک نبرد سرنوشت‌ساز؛ آغاز یک تاریخ جدید یا احیای قدرت غول اروپا
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/94944" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
‼️
🏆
برخی از نتایج تیم‌های عربی در جام جهانی تا این لحظه:  ‏
🇶🇦
کانادا ۶-۰ قطر ‏
🇹🇳
سوئد ۵-۱ تونس ‏
🇹🇳
ژاپن ۴-۰ تونس ‏
🇮🇶
نروژ ۴-۱ عراق ‏
🇸🇦
اسپانیا ۴-۰ عربستان ‏
🇩🇿
آرژانتین ۳-۰ الجزایر ‏
🇯🇴
اتریش ۳-۱ اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/94943" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94942">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فران تورس
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94942" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94941">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللللل پنجم اسپانیا</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/94941" target="_blank">📅 21:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmdij4pellflAUiLbEOiQ_Ymc_Jl7b96f07TMlDZxbt6W6i6iMSS4CWcnxJztlAzPvJl-tJfOHUi1MTnsoq80tT6FgSF1sK4sl72wpW8pt777Eq88fFw_RPi3BejxNJ3auBOq47XzZ1SHiSmovI98GevF1dMbHI8bifzFW20U4GYQWdCah5mM98duafWEEV5QBYVCONrc_Wug4dVwDZkhsjRPMGjNlDNdBxIkk5Mlk7f750Ez9tYLujnncz1U0QyX2R-imHygLqQNZr_qOeBUvX97_UHv00G5gp3jS5-gZRNX9JDrd63EzQDGz2QoKnmmGLLDMLwbUPEYDSj_5exSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🏆
برخی از نتایج تیم‌های عربی در جام جهانی تا این لحظه:
‏
🇶🇦
کانادا ۶-۰ قطر
‏
🇹🇳
سوئد ۵-۱ تونس
‏
🇹🇳
ژاپن ۴-۰ تونس
‏
🇮🇶
نروژ ۴-۱ عراق
‏
🇸🇦
اسپانیا ۴-۰ عربستان
‏
🇩🇿
آرژانتین ۳-۰ الجزایر
‏
🇯🇴
اتریش ۳-۱ اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94940" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94939">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic2kXWtF3YXliPXEtfbXZBwkCnDsPR9xcMKES5LeA_KB9T6JS5hiVvD_i6VF4Syr2iOZxE6j1eNIyzCOaRhJuw8ka2To2KcIGpoqPs84-Yx-Mjd4kyjYXs7F37Eru97DA6Jd2UDr2RoxMXh1qk9Y2-ChVZxCKSb7rSj6beg7GqOCUejHzcTo897FtmoQS4130KdXZ1Dokq4qwneU_c_cAJ1XdvhwstvGS1AxmfLqr6xA0TA-3U2bnOphI2XwX8z5pfo1DmrR9HTgs4ldFFigx21FzI3l963x4Egeim8H8yhZPQ2Mu9DR8sYzqwTDbN582_E3oEYjuN86rZMozy-w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فران تورس در یک اتفاق نادر امشب این تک به تکو خراب کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94939" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94938">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt99B6K7PmN6dqNXdlLiS1BUNUcFFVf6z6MBL9dEduLEkCaL9XvTHfRzQq7XDD6XGtqhRldkIbsdiZedeDJ1MtnKUUa2F2iH7E-mH5W-HVnUSqTRoa_6-7V37z_DgYYFeAAvpvE5Rj2i1Ve5UL4-fh0RMRX3MHI3voi9h9W6jzkP7IjJz0gZSOtF0BkcVkW573OCZ1VP5DZLGse7tCkB51F8SU6qVXpOCoA6OJ0AV7urjtFdXn9MQ6Afpi8tj2eaZVo2KkApr161a8A3wELg-unD2tM565iEvOasU96VslSNiVlV428z6ekr2tzmkCQgvf8ZIYX4DZnRnD3sHeosgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94938" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94937" target="_blank">📅 20:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94936">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja8ttBPqttarxuqDKKOEspYd-YfQoJAUBjxuTyiHKmolwZgzCXYL0OqKSPmyoC0NCHy5xsXlPfUM__WHl5ltdy6v7wMnrElX14bNpOrYImPQEs2nboth_cRK27iK3kRnAjettlDEnQT9pBO-4zt8-KO3sM2tzA7JugW7mSACncaT_SFHzgOtDVRjPQnMRK5u5bhE13tMjaqGLq8AggSWYe10-pLrQ1SzBEjLASMKjq7hF7Ow_c7SRDXaZiPbJbSEZKMN8P7gEySA17Oj_tUVssbqVZHk0arQxUHfIX98WV6BR7kJe-W6QaFY9EQMwk2qOtc-w_XgLQUMJ2YG3BtoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94936" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94935">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c051daab83.mp4?token=e-l1tBCG2FSmjzq4aHj-Ubc2wsnVy3IHe2On6mcZfkEyHqoe9hTWybtWaHvx72CJh7_ZUgStYXtwI-4VexvGJRNeSu1lOyoaG_jDhdKrlgwA0OhArDyIlSEsXbHU_pUuiQ8OXRO37rDhz5-utk3aP80IhZQrZ_MdNCPojbmmbNxygpW8gYZ--iqFu1gDJrJMWfygA52_bVAj-2UKIHnODCn-m8zplzho8Iy6rFy-Kp5Hj37gNfzp2EQ660SQSLGabFcjFwBl27BYmX8X-JWHmTCXySK7ccTvE8oAlKsnvsH1oo4argS-E_sLjlCLxkxWG9uqbBBgik6e-mFnXieHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c051daab83.mp4?token=e-l1tBCG2FSmjzq4aHj-Ubc2wsnVy3IHe2On6mcZfkEyHqoe9hTWybtWaHvx72CJh7_ZUgStYXtwI-4VexvGJRNeSu1lOyoaG_jDhdKrlgwA0OhArDyIlSEsXbHU_pUuiQ8OXRO37rDhz5-utk3aP80IhZQrZ_MdNCPojbmmbNxygpW8gYZ--iqFu1gDJrJMWfygA52_bVAj-2UKIHnODCn-m8zplzho8Iy6rFy-Kp5Hj37gNfzp2EQ660SQSLGabFcjFwBl27BYmX8X-JWHmTCXySK7ccTvE8oAlKsnvsH1oo4argS-E_sLjlCLxkxWG9uqbBBgik6e-mFnXieHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل چهارم اسپانیا به عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94935" target="_blank">📅 20:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94934">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلللللللللللل چهارم اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94934" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94933">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلللللللللللل چهارم اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94933" target="_blank">📅 20:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94932">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیمه دوم اسپانیا و عربستان شروع شد
یامال تعویض شد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94932" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94931">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHgv2MkHB1qk5g0R0M_l81QCYjP9JvqU3zk4_qz8zDJhkhmQ5jf9gufGzd5Lwa16RUkrLHtPvqs1xtsv23pixNUmWzqxNchkzmMvJRXZfm_bSkmRP0pPbHRcHcKB9z1DEA_-SP3ZT6D_t2zfe3S_BdrNUYY8NiZtgut5hlHyp0b_-fCSdR2OoiCqJdPZB1xJPolUbAF6C1tJ0kKj0gFGLn3s3oTao3xYK55TddCC_n0uEA75r6JM-S1U-l6hqsxiatdBBfd6eFa_tnEwAl9nzWz6uqvzZ2v1FXObkHKwzrssb14CZ_VYGnF1tqBheZSbdGwcZQgnSbcAINq2j1-Zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وین رونی:
یامال باعث می‌شود هم تیمی‌هایش به توانایی‌هایشان برای قهرمانی در جام جهانی باور داشته باشند، درست مانند آنچه در یورو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94931" target="_blank">📅 20:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94930">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFlT2GBAqDynNTvaxoO1LvTn6LBpp8Rr1BeAOH-WPNPBcvOgdw6trBtkZH3Yg9J5pgMmb9h3-1FwrqdJ5JfwPKD7FOAFgNvQh82KUPq1wFGop7DUXQqxEg1uqDS6oZPS2zzbNpnJe_YknbaxusC2pCkpbhLK0iChuBkR5ILfnz2lbI0HjjjKmVzpYGnVPQJPiges586HFrmDBUitJMrF4iQQSkVDV70rFToPqscgKesC9YmxyJR44Bx1tzR9-3qAO6slHJulqOx0oXXCkcVVuUEXrfg0krSknXa37PaDutM92YIt1NR7_DU7C6fOrFgxMFa7K0cgJbgIDHr8eYfV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا برای اولین بار در یک بازی جام جهانی سه گل در 23 دقیقه به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94930" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94929">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94929" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94928">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptXZZ7m14ggHgs21sBPUj-ozYc9lXCuJKUkjIjJCwXu0KgvlIWxdRXp3ey2sgtvejvuRG1wGQlv4j7ZeKXiWCrv1MzUyTbaU1GF9ScEOZ19mdwgZRtwx7uhADCN-y4USoJOIEN2alUJpXkYEHicbAfhwRKgn-ujD2-QP49sWVyeA3Zhjr0bMXhJwXF_O8VsX88GMz3U9kBYlCRxhLJGuRmnR_87xTlneM5KajIzixoqEKzEs7vOk5vazeG9A6tTsqqIQ_5EVijzr95FMFS8MkpS2bzFNgv7cZ3EQC7JW7FtDCRfSOtdSk6ylfp4qvP1_v01KH_RlEL3MqCVeYpLLQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94928" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94927">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESS0IUpEYvJdSui1hQdDgfLyXviZheHtH8W92sf5mlWOq5EMXzFiWBZjttMJ-dKkvChCC1TejzDSyaR_yrvTYrsadO6Ws7ilFkTd0Kkvx8gXdGSEblWg7UoEK-5xxC_ypcikxdFNIVW2C1ugaMxzJ6AbSbm9kXZMoNrwwHsOa9tZ-UlXpmC51VK75-txMX42M0UE1AT4H5nVIAd3IkcLzuJq5D3plLuKfZtoNb-LJ86QRvHuqlAkMO4NgNKTdYtDmDAHwLdCLiPKZw0kxtMoTbVUhlFMBsXqgKmitPw9DgXqfQFPq5U2AOr16f1iNXQ9t_XyVkNbZP53pqy2yN8ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا، حتما حکمتی توشه.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94927" target="_blank">📅 20:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baLl8pIs-4_7YvHUmFrsiVyic7rRHv_iePeCVuorVdoSbFAnj2sGF9eQD3DhHdBoZ4YKtKw_cSpe0zraDnww1I-SoyqzsumW8s1poRr51UIODow_34EnbrZqWWyRxuXLgAIvgk-BjOzsThX1Z1vmyHHC2ZBmGga8woF0yZ67ZZYBKSdQ1ESMysPeBdxRIGF-Ur7jGQBdyRDyIul0uxVUeFdWf8JJ76oVBv9aPw3Sa60VZBZI68DBD1DjFICg6DuFxGGqsRQpL6fzNjvZkrETj7_srOCWbfeXfMReOUcfkJOq34Tf183mr64fmZe8Q_A0MBp1W9jZxmeRtanQPsJGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇪🇸
آمار بازی اسپانیا و عربستان در نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/94926" target="_blank">📅 20:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پایان نیمه اول؛
🇪🇸
اسپانیا 3 - 0 عربستان
🇸🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94925" target="_blank">📅 20:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امید گل ( XG ) عربستان : 0.01
🤣</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94924" target="_blank">📅 20:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD3vUvIS-ye3cINpFWLerj4ej59utkm0WevgUdkLhaKOyil0_JTJNVvCc8I8pEs6u02KJuzgE33VRpwQm7R_2fQAOOWCqWyHXIi1w1LkXnK3Xp4eOczkeemwrHypJ3G735B-Z4IuQl-Z17zFk5SthO7Nw-eSZsbKiy4o3mfacLX0Kq7QJY2DHbFU3MK167v7N4wojftxhkeG5KzFXhrHDOKPMl6DE5SJ6evC3SX05AeRrlW51SD-CVUYcTH2EreYiY4z4NANTDrBM9dNknk2PJE6b6v-fnQC2wCXxbi7IlUFK5qni56xxAvWmx4Msh47mW5xPzj2ZLRNjxzD-Ga77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
2 گل و 1 پاس گل مقابل عربستان در 24 دقیقه؛ میکل اویارزابال اکنون در ۱۳ بازی اخیرش برای اسپانیا ۲۱ گل/ پاس گل دارد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94923" target="_blank">📅 20:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIxGkcTq0IRqDmwS3Y8joBoIy2j6mSACSQWBpx8kcFJtP4cMuM9I3_3HukABbnFImUXInlgO931cvI08aNiFxMR6pqixmG4bBr3GuEeTkE7iI3fwleuniO62-cyeNSN8waqvis9DsgBQKbs8zKL9cEyA2PR8s7bKIbQkztUbfhkO-P6Q6AyOQiMOoB-H66x2LcNEmKXXBvXonZwdrVqVsNEVvP8A2Vhy32fRWrV-X2v5H5wjef5nMt-ujO21WCnFTLw7hSXATU5b5paecssWQ2j4N1ePu15E7d06bxIdRhzymbx0vJGxL5ni2lSe1Rs-ehTSjcYrHvfiaJwZzmHEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی: ۱۸ سال و ۳۵۷ روز
لامین یامال: ۱۸ سال و ۳۴۳ روز
👤
🇪🇸
لامین یامال نخستین گل خود در جام جهانی را در حالی به ثمر رساند که تنها ۱۴ روز از لیونل مسی جوان‌تر بود؛
🇪🇸
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94922" target="_blank">📅 20:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19139588b4.mp4?token=GGpCwp9GS4mY87PCG30WCAf6lIouTKxXRG3aXknrdnB6vWZc5zzFMbUXfEqzi2pP3Otv943eqIoUUy9eqOcBxpzeSZTYNBLOVfm6Qs-PylJfmTc7wEg0uMfkVf_cKP-_ly0WxmdmqG1Pmp1FwY8XOeF01__X8yLy9_uJMnhu2V-IJnFqDZifmEyobxD5oDiKAw2aZQx09lQAO0VE7ndVedCbh2Z-ye1YPg0ySU8V2Z7p5NSKSeAcng24nx4H7C4KiZ-uZKFaelGtYj0CFSpi4OHU8Nh43T4VV_9vFHuSSuDvNfdqHknbzaIoaIx_HVLfwoylpGDEMixVTs-UZwpAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19139588b4.mp4?token=GGpCwp9GS4mY87PCG30WCAf6lIouTKxXRG3aXknrdnB6vWZc5zzFMbUXfEqzi2pP3Otv943eqIoUUy9eqOcBxpzeSZTYNBLOVfm6Qs-PylJfmTc7wEg0uMfkVf_cKP-_ly0WxmdmqG1Pmp1FwY8XOeF01__X8yLy9_uJMnhu2V-IJnFqDZifmEyobxD5oDiKAw2aZQx09lQAO0VE7ndVedCbh2Z-ye1YPg0ySU8V2Z7p5NSKSeAcng24nx4H7C4KiZ-uZKFaelGtYj0CFSpi4OHU8Nh43T4VV_9vFHuSSuDvNfdqHknbzaIoaIx_HVLfwoylpGDEMixVTs-UZwpAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل سوم اسپانیا به عربستان با دبل اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94921" target="_blank">📅 19:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d28a05ce5.mp4?token=l8HnbglXECoHp1npw7sAQ082A0N5HGcFomZBahcBo1HBHfx6ssRmblgilihYAv8UwNZ9nHMBhYu7PPGcLWEOs5w3OXm2dJqbjLCxYpvEyW1GK7vvbnqy7d2qC_KjYvNcj7SsNBZOiFQNb_GvxOu8G7mf4xvGYT1L2Db6pynoUu7lAhFYztrp63maTC4O0D1e1u2ixL8VdPvYKr4-_FBVBsBVIPxlBefLEngwZ7fFGR3rppXyU6IIqrOPcFiojtmdL7PBDW8h1tcXcB36j4sNqcR3T49U4ZO7EPfs-eF2q4yDZ1FvgCnarBLwKo6YxipDBOl3uDySsqujK2HkpWGJA5U9dqujyZBahzidaZ_vRY6T1WRv3FTP_SPNOTInerAf9tEymDKA94FCQcqXU2O8IxgtRPappwDY0vq4WPjf8uSHoBUrQhycPFsyaLC182vgQvC65XYtW0XokARx0GX_iMQpohzVvew0b_qWiuMt1OSuyC_XJW9q8pRYt4-XA0-tDDA8f7t_kPjQcH1shGlLViwl5ECFzLSuo2n268pig8pK_Sh_PFuL9Cll_nkEEbFAbFiu3-89hXMc6uoKLAWuLqok73kx2ZOX-JJnPCENa7HRkhsweJ5vjFwRS6pFXs7OJdlLd80KMV5Iqi8K1fO7Gw6q7kUeuqYz5QqwA8UG8B4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d28a05ce5.mp4?token=l8HnbglXECoHp1npw7sAQ082A0N5HGcFomZBahcBo1HBHfx6ssRmblgilihYAv8UwNZ9nHMBhYu7PPGcLWEOs5w3OXm2dJqbjLCxYpvEyW1GK7vvbnqy7d2qC_KjYvNcj7SsNBZOiFQNb_GvxOu8G7mf4xvGYT1L2Db6pynoUu7lAhFYztrp63maTC4O0D1e1u2ixL8VdPvYKr4-_FBVBsBVIPxlBefLEngwZ7fFGR3rppXyU6IIqrOPcFiojtmdL7PBDW8h1tcXcB36j4sNqcR3T49U4ZO7EPfs-eF2q4yDZ1FvgCnarBLwKo6YxipDBOl3uDySsqujK2HkpWGJA5U9dqujyZBahzidaZ_vRY6T1WRv3FTP_SPNOTInerAf9tEymDKA94FCQcqXU2O8IxgtRPappwDY0vq4WPjf8uSHoBUrQhycPFsyaLC182vgQvC65XYtW0XokARx0GX_iMQpohzVvew0b_qWiuMt1OSuyC_XJW9q8pRYt4-XA0-tDDA8f7t_kPjQcH1shGlLViwl5ECFzLSuo2n268pig8pK_Sh_PFuL9Cll_nkEEbFAbFiu3-89hXMc6uoKLAWuLqok73kx2ZOX-JJnPCENa7HRkhsweJ5vjFwRS6pFXs7OJdlLd80KMV5Iqi8K1fO7Gw6q7kUeuqYz5QqwA8UG8B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به عربستان اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94920" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلللللللللللل سوممممم اسپانیا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94919" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چه فوتبالی بازی میکنه اسپانیا
🔥</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94918" target="_blank">📅 19:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلللللللللللل دوممممممم اسپانیا اویارزابال</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94917" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واااااای اسپانیا چیا رو داره از دست میده</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94916" target="_blank">📅 19:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94915">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19cda970c0.mp4?token=cP19WT08sNFANdl1uE_1jGzlSqkhi3A5u5ZvR8M8UTwHu60nfq1mcz63wNSDVXuV4Axbtmm3_ctRpcdk6q8gGQVUboRSPGDlXA_dv_cnFQz0-dxk0nfU_Snuc7kRXpZYrTjhmwV2jqBmc_U2YePKCAYf7NBIFh5dyEVl17aXZ8Z8k__BRSjXuBwoS9jXJWZjUKKytJiu-TlYvQ9PiZj6B3pQOQADEFDVxpzu22xRnltFKEwy7jpICSug-XHTJDh_cVhV0K5uGu5-uNhYzIOWvnMMUBCWZFk2uXLptiZ_2WY_Tq9YNung5RYfxWPMtp_55FBwYLXlQFbcRj-9-eSp7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19cda970c0.mp4?token=cP19WT08sNFANdl1uE_1jGzlSqkhi3A5u5ZvR8M8UTwHu60nfq1mcz63wNSDVXuV4Axbtmm3_ctRpcdk6q8gGQVUboRSPGDlXA_dv_cnFQz0-dxk0nfU_Snuc7kRXpZYrTjhmwV2jqBmc_U2YePKCAYf7NBIFh5dyEVl17aXZ8Z8k__BRSjXuBwoS9jXJWZjUKKytJiu-TlYvQ9PiZj6B3pQOQADEFDVxpzu22xRnltFKEwy7jpICSug-XHTJDh_cVhV0K5uGu5-uNhYzIOWvnMMUBCWZFk2uXLptiZ_2WY_Tq9YNung5RYfxWPMtp_55FBwYLXlQFbcRj-9-eSp7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به عربستان توسط یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94915" target="_blank">📅 19:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چقدر دلم برا بازیش تنگ شده بود
یعنی میتونه جای مسی رو پر کنه برام
🥹</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94914" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یامااللللللللللل جونم به این پسرررررر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94913" target="_blank">📅 19:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یامااااااال</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94912" target="_blank">📅 19:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلللللللللللل اول اسپانیا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94911" target="_blank">📅 19:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب بریمممم سراغ بازی اسپانیا و عربستان
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94910" target="_blank">📅 19:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYqU4CZEXXJAD7c1E8PFk-nkNgx4YrS-ON_6-ICTmBHGk1YYErcj3Ap7aQipZen0FbodprmBnOgGFv6EzHtkVPFjchg2VW9_38r2dYcNXrbuQqScf1rmczVsMB70hUbsZsxF_L4kMKTf3iZdFe0ZSqhsgMYt22zPMRuMI9dlytnLChO3IKmatEKEuHg0X7CrwQwS81iMRJkpXUqE6x0UooI3oRIO2tF3SympwMXcEuUBOhcdFji5pHdxI2yf4OlVFr1pDgj1KaeQ_4PUKQeWnWSR_1xTouXhjYmidvw9mEwvFFc9qRsI1m251VdapObDFJs67AAlsrvpKbjBFnXn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بنر یه هوادار عربستانی بیرون استادیوم: اگه میخوای قهرمان جام‌جهانی بشی باید از عربستان ببازی؛ آرژانتینم شاهده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94909" target="_blank">📅 19:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMHRQ_M24yk_oTpzZbzT3U5kDjCyXctBVlhPxwU8wvZBwvIzTWzzJfgEnBDsXtrdZx0PqVUZdP2E5FHRxtRCv6MLjN7ikAmq54XCzT9WJtsJHffclYJ0644dOxjZoEno4LW6hVCXytxjZsHletKJwbjJeB53NsmCZskkRCBZoDjsDIq6Vxnj6GtXArlhcLg6ans4lxzi3klVQq-D08ZuoDpN7QOpne_1A8yuOlRimv4XY2XsKVxp12drEHSLIfBD3UjMx--Ho9UiFUmEuyrGjv7hHwnORMTu3YyU4tRjWAF4ZYpp1XV9_hNSIGNSnCyzhXzl1I0mPVBWywBY9OjoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXGonKOyCun-DhZt-EcSCnWhEBDREYwQbBg7pV2ET43vsxo9WjdRx2tcgbgjBIVhwJbFnv-OQdfT9DJlAGVcg2LkcUnHfgFRRV1Ef5QhHq5oUjTv6Gfb7_3nMMUXZLzKlhedYwl7TctYPJS_GSeTIansJwFN6EFxzWsty8aa3YheMmtF-dCNmJ56pW5AA98nhsKE9cAV0Wr0sntUX7sSms209EnWIWAGthEno2nlJFZCmDU3pE7mxjryfE6wZ33r3_zNuxsXGjng9MuKBUDMfhs_-2ytfAWyvU0AMI2P_qEaAfatVkqgGp6x9AAgucoHdCP6Ql-3nMF0-27kmn6m5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUXQqJ6js6h3B0V46ckdu7bhof-C3bxokGtSn0NK7xY60Dm_RaNu9UENMVGg9Pho5iJY26Ky1qAo1g11lV-SYtmfhD53beo8FfduBfcUl5wP_DB4Ar_3UaV0pFFH9fW7ZYOxrMAUyQShgtAN6AdkDvq-8zpxvRVN6WVzNB4mnVZip2EGbUPHQlnKaVNP1WMLYM9rDclwSSvNoT6TRPVLTjnaabNTY-PJ3JH80WtCf4ExvYoAPV2iA-m-IxY97uETwEqReI2ogX1aRbyl-6qTzxAq_bALcbml5S3Hv7U1eZbulXKMOmxO_u8pBzAas8ZYWoUFweY3GUlX5Yq6fyfiCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
بله داشتم میگفتم چقدر به اسپانیا علاقه خاصی دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94906" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94905">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bc5c62d1.mp4?token=FcWqJtEnJGDlARrWSQuMxOyBsP42acl03PLxx-E4CdASAHlPVii30-WOwnv0Jt5GJKBc5TiTefNvCa-YrQiq8gt9kox4y2qRxddmAOYTviBoWjcyAvcoabmxjjAPG-T05JmVsKfTESNrNyFqxXZ2lv4Ze1SmVXLP3Q6p_K8KhjzKgBKpNcpWZ-4qMsaDcEAQmbnuHxFZEzf0lrnXuntPNRkbna8lDJJTMALIDNBqCiPDLbTYfzUmy5kgykuS0-wL_SU8qY8MA-d8451h6q_tT6f61445BZk_7jCaa9hie9Q5p-cHuWJKfoWBhkdM3XyqsRr2csCEysCVIZZqTsCZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bc5c62d1.mp4?token=FcWqJtEnJGDlARrWSQuMxOyBsP42acl03PLxx-E4CdASAHlPVii30-WOwnv0Jt5GJKBc5TiTefNvCa-YrQiq8gt9kox4y2qRxddmAOYTviBoWjcyAvcoabmxjjAPG-T05JmVsKfTESNrNyFqxXZ2lv4Ze1SmVXLP3Q6p_K8KhjzKgBKpNcpWZ-4qMsaDcEAQmbnuHxFZEzf0lrnXuntPNRkbna8lDJJTMALIDNBqCiPDLbTYfzUmy5kgykuS0-wL_SU8qY8MA-d8451h6q_tT6f61445BZk_7jCaa9hie9Q5p-cHuWJKfoWBhkdM3XyqsRr2csCEysCVIZZqTsCZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکسل بابا امشب عربستان فنه
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94905" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUgKnfMQ-TxNX_3Msd2jgSBv9tUdYcE1xyvd8TouDF1KVnY5zd64aCs8vhSfG6IevgzCxSwTQphiOUpt9sMEkPW4kgrNEZGzVgOYkUrx2O78jbFMYng4Q2zrOhlEaKcIdR5anjbgTwSMakOXpoF4-HTldA706bhBerBmzWnnNMJ0XQgwVMqFJlH4-CNWO_LDZ0_nICxRz9ilE7kzjyNMa1sriR1Tydz6zb5jCPWmxGll2tmg13gYIn6EaCJtJEwTiuVnczQpEO8aswWRZNXUSuk5sHwv66MqqXyg2EHKpGlGKTPwiGYz9eNvfpjFRJyj91jSim-mkkbof0Cuen0zPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94904" target="_blank">📅 18:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94903">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0996af99a5.mp4?token=MXAq8lUiKf_6dWDuPPmfucJ4A90s8E9zz5RrUVJ9I0Y-8SmvmoNV5ieGkuKZsV-g1kUJjD1mQ5RhSA77TCJGALmsXv6YTfFPdLkuXxQ86rQCGfb5ABQHpVpNut1Y27kSSUokmiHQ5ndrJsxCm9N6x2QhFNzXiO7wbFyi0qMhqN8TLLhx4DkeV6UXkJtRsShpw9zO_W_XDnnIE-G75mZaIHcHYVi5E2gK9oS4R9cDPeX5HHkL5zBqX0aVxNxUQ81PwehGt49jWmZ92OE4Yf4yBwfFwP5BlHohZOohSxZawoJN-PvjVgV4mBIivuzn-DT-SuCy8mHWMczm2efKNqzONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0996af99a5.mp4?token=MXAq8lUiKf_6dWDuPPmfucJ4A90s8E9zz5RrUVJ9I0Y-8SmvmoNV5ieGkuKZsV-g1kUJjD1mQ5RhSA77TCJGALmsXv6YTfFPdLkuXxQ86rQCGfb5ABQHpVpNut1Y27kSSUokmiHQ5ndrJsxCm9N6x2QhFNzXiO7wbFyi0qMhqN8TLLhx4DkeV6UXkJtRsShpw9zO_W_XDnnIE-G75mZaIHcHYVi5E2gK9oS4R9cDPeX5HHkL5zBqX0aVxNxUQ81PwehGt49jWmZ92OE4Yf4yBwfFwP5BlHohZOohSxZawoJN-PvjVgV4mBIivuzn-DT-SuCy8mHWMczm2efKNqzONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معماری این استادیوم واقعا شاهکاره و هرچی بگیم کم گفتیم
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94903" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFYG08LDfb7zi14BRDiMaIzs2c8ltpSVatn3xhnDxUiZLsiZ5mXHKqWJ5BEy4e_iD4s8ifwRpBZySxu8NURAMyIuPsekM8D64TvZ8OFXtg-NnLApnxcaYUdg_k6qOSuMM-ww9P5PeSvmkahkERnVOvBec0z5RTeprAd39jhRhz4R7m6ehHPBJj0zLEkJkzYxcRqwb8Ul8ABhfs5L0ZbBmqhxY8IsOgvbqv3QHMlL55K6pskN3o4fLkj1rB3brBnlJSQfUegL9ov-pS7z4E4LzfvndundLtpS7q0zKDOVjCba6BCRTYvGn17CLpBQhDEMJ1Alr3tXfDupC2AX918TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا پرتغال می‌تواند با کریستیانو رونالدو موفق شود؟
اریک تن هاگ: «البته که میتونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94902" target="_blank">📅 18:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396646f131.mp4?token=A8W_OaKrITtHFvv2uyDcN5frOGsEtw4ZJv6qpdLd87o-TGfN-UmhytPQ4U-ssYDxK_C4V1Aff9Zdn-EEbaVVIEEMTlHOukjMzbl3jlNpwTkNcMORolS-GwqM1z7Y8OXgBp2FAP_iekQAaI7UvGHoYKIYqcv7AURgt6Uy0njxX19R1wKK8AQreYk7X0DZVyEsuUtsppDBfukUtHXH_Xvrct8LMgwypUjneTfKiTpFg0cDIMWrMkPy5zN1fkiW17xUkH9HRoSTfmFWQlRL2NPwLNCNumo-7MwypATmQ_KcqjM9hDJeSB2gb6fEXHPVBCKu6HLcqIFZXT2afa1Jsoh6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396646f131.mp4?token=A8W_OaKrITtHFvv2uyDcN5frOGsEtw4ZJv6qpdLd87o-TGfN-UmhytPQ4U-ssYDxK_C4V1Aff9Zdn-EEbaVVIEEMTlHOukjMzbl3jlNpwTkNcMORolS-GwqM1z7Y8OXgBp2FAP_iekQAaI7UvGHoYKIYqcv7AURgt6Uy0njxX19R1wKK8AQreYk7X0DZVyEsuUtsppDBfukUtHXH_Xvrct8LMgwypUjneTfKiTpFg0cDIMWrMkPy5zN1fkiW17xUkH9HRoSTfmFWQlRL2NPwLNCNumo-7MwypATmQ_KcqjM9hDJeSB2gb6fEXHPVBCKu6HLcqIFZXT2afa1Jsoh6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
💥
سوال اصلی پیش‌میاد اینه که اگه این عشقامون یهو وسط بازی عکسا ازشون بیفته با توجه به اینکه لخت میشن قراره چه اتفاقی بیفته؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94901" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm7OtCaJpWOzhcdZwfPN9KPBUK5eCYdkMCkgSgH_txUt4vAyuhsqA1j4hF0SERWDJ2-OcfISrmIl90OrSejcXFbNharStLXs7c0Bo15LEDZRoU-HVdbSEzPnuJDIUK5RiRKM6QJkTT1YTfhBaRkrjUOLnwTwKaC1gHfsErwbyBSK1_qZLJ96bojgqUyr3ARoOn_aWB7-TR5eqXD71LMvLeVhzHF45bqpmFaY65xTLVrojRQQYqutaM5MCjB4MWTbbkFVOx8WmJwLBhsTjZtp8oP9eK8wtrmGQQF8SiyQQx_lfsmZZStYhN1oMIubtvHx65kADWdhxXAey40igPg0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژاوی‌هرناندز: "بازی‌های زیادی از مسی وجود دارد که جاودانه شده‌اند و هنوز در ذهنم مانده‌اند، اما اگر فقط باید یکی را انتخاب کنم، بازی نیمه نهایی لیگ قهرمانان اروپا مقابل رئال مادرید در سال ۲۰۱۱ خواهد بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94900" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F47VwnXNBzB7h9CjI_6UX0moolmx_UFUF4W693OmUh45jfCoZVC8TMbszrq8f9iYcUYSb6O_NbH2fVN-70Gs092_lwLE_HYBZiqoYceGHbfC2QQ9So_X_X7cbMIcgj2h6QnfH2Jhak_wnjqIMwu_FWpXZc56wlExZrUyNTzUVTXW3MDJVSQShXkebxqGADUTPIyoPTMkb4uDVasNnclkIO_BKN80dOxd-Jy9PoWkugL9uqYxHJe0x_fFjfP2KpsZ9QDRBfNSygp6tunhp4fzvrtuw-0CTQWY8bsTb5NosTB2GS3Kuk1E6oO5D7hAWfcqzGslYfAi02nBptHJzIA8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
اموجی‌کشورهای حاضر در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94898" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6HR80hwIQE9lb-Lbyjy9VQ50TXb6bsx64McjocHXOuY6Eog3ioCeyruxv1Uhstk1zAxwcWhyBq_hx0K20_NDW-mM79oL3vegkfGnc95BhcIwCsYZUUG8ZxS6cv9T0jwvhJ8wpOLLBbg8HfKtqe2bpUCPd_QNUZAPudVA2JTa1XvCQ6YbPfqMh05t776v-IZGNcT5WVgoS8swSeqPtcgUKViDUg8Nlw8mTxCz16XYsjQ6ViFZK8ybNN_v3JK1UFWqZhdUOMu1uSUAs_nQQbvUwC8lhT9FGrkDbF62ye5s30ybFNsEq92TNeclqJUntHPpCJQLVw02WhisOyP__DrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94897" target="_blank">📅 17:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEBLPQkMoe7Avi5PgfKyxpfzpSR_UxEiFRdDt_BMWo9vNd-2QxUxy9boM0_HOjZcZxWFazpKWNaesVKg0yI-5XxZXgkpZv1fyt_p8UXb4RtC-GCBCd2OvukDnaA0nHZ7iGZ0bW1DKPK79QnR-TFBkwtyRII4BNrKdoO_FP392AU-oDeP16YCZeiWFpNzoxSor9mq28PJaDTesIY8usfk5ISH-B4tltqA7jE2jUOnTztwvabI9vgZcpRb5BSwsP8Niu5vT_zq5bnbsoo6NQepZX4RRq89VLEsd6klCWekxetCFiHPNCzN35y2YUp0LVBvndpk4FLaBHFgu_b1tbsWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که بازیکنانشان تا کنون بهترین عملکرد را در جام جهانی ۲۰۲۶ داشته‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94896" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCfhOh-_kPlogEAOwCCMxuzV2XsF7Y3dnRqbsZDSPOL28WSzHT8gryUdHf8AVR3brxBae7KaUq0CaeobuFQVBoGhLJDBKPbrQWVhTRkgUKq8z6VWlVkGHkiNSaZQ4VazEQoZ-B9Z_fQuErbwCWciFUhVfVWOkqFQxklXYTmA5r2OS7zHf8zZVoqe4w2h7FKyLtM6fsig1fQBgruOADtcy7G33Ts1kwoIiKhCaUkuy6V1kZAG4iRgHh67JrHAsHv9OjysYncbTza_cWtwWHdaJjx9srzjqhYF385cFK_fphn_JnHf4uWn4cGes1elU80BQdhdJqzn4UNSTppkclDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سامرویل تا اینجا موثر ترین بازیکن جام جهانی بوده، اون هر شوتی که زده گل شده و هر موقعیتی ایجاد کرده پاس‌گل داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94895" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCHPXO6JhU9ve2WN1rlvGcns7xaDO1A85zJ8pNWpPrTP3UfgAbotskCF9Bt_c0VhduG1F9yrPp_q0IByiYEcbmVMdMXuFggBVi_nOntVvYFp05Lcv1CCElix-XVzzNE3TOH-S-VGGN55rXHVgvkCUuYZ8O8TY1H2Z1NJ3ul6MqXN8Q6ICXtP947AIqngYAH34VREjXHPEID6faLnVTpElqoX2xOzdmISvK7BpIuoQ-PX87pUQaOFY24zGiYbVYNZBx72rxIwfG3os7VhSZ-XjIfm2-z60AV4hVthYFbBEhKxtoG6ggKd25LWpWNSdQhY5Nz98ZdrwLtjBy0X_fJopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
در آستانه بازی ایران و بلژیک؛ تب پیش‌بینی‌ها در «همراه من» بالا گرفت
در آستانه دیدار تیم ملی ایران و بلژیک، تب پیش‌بینی نتایج مسابقات جام جهانی در «همراه من» بالا گرفته است. کاربران می‌توانند با ثبت پیش‌بینی‌های خود در این رقابت شرکت و شانس خود را برای دریافت جوایز متنوع این کمپین امتحان کنند.
🎯
اگر هنوز در پیش‌بینی‌ها شرکت نکرده‌اید، برای جا نماندن از این رقابت می‌توانید سری به «همراه من» بزنید و پیش‌بینی خود را ثبت کنید.
کاربران گوشی‌های اندرویدی می‌توانند آخرین نسخه اپلیکیشن «
همراه من
» را از کافه‌بازار، مایکت، گوگل‌پلی دانلود یا به‌روزرسانی کنند.
کاربران آیفون نیز امکان دریافت نسخه از سیب‌اپ، سیبچه، ای‌اپس، اپ استار یا سیب ایرانی را دارند.
همچنین امکان شرکت در کمپین از طریق نسخه PWA با کامپیوتر نیز فراهم شده است.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94894" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5da6167e81.mp4?token=TR4TI_3jItoDZmpFgvVaBH7Z5-bsTLYgQqErdu7iCNg9elgGikXxbEJO4P7wTah5aYGwj9HGdtLYpk6vGPxfEMSzQWguSlEOhAVrBCMqodsdPsv1rRmNj5Xkxtzd8iKNApjPRDYuxsaX5idMzeOeS0xlaJc9PDhrWOpmtMUE_1-tEVE5zHgiNF0dPG7BxbDZF3IALdcQgJ6XumYVc1c0vvRd64_VdIi_Ndc-SHVKFu-RangNGbngXneWwDvbOMD1zzX-9tUaJnB6t1jx0RSmv0peduwb_o9TZvdIENQ8poCKqSdy2fYiSt2x7bSdFH9XmqatzsuuPUn9B9xeDAZkTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5da6167e81.mp4?token=TR4TI_3jItoDZmpFgvVaBH7Z5-bsTLYgQqErdu7iCNg9elgGikXxbEJO4P7wTah5aYGwj9HGdtLYpk6vGPxfEMSzQWguSlEOhAVrBCMqodsdPsv1rRmNj5Xkxtzd8iKNApjPRDYuxsaX5idMzeOeS0xlaJc9PDhrWOpmtMUE_1-tEVE5zHgiNF0dPG7BxbDZF3IALdcQgJ6XumYVc1c0vvRd64_VdIi_Ndc-SHVKFu-RangNGbngXneWwDvbOMD1zzX-9tUaJnB6t1jx0RSmv0peduwb_o9TZvdIENQ8poCKqSdy2fYiSt2x7bSdFH9XmqatzsuuPUn9B9xeDAZkTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇹🇷
روایتی‌ از ترکیه که در جام‌جهانی هرچقدر هم خوب بازی کرد اما گلزنی نکرد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94893" target="_blank">📅 17:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbef46de48.mp4?token=TMssHvBl-BWslwf9VZ3KbcQkw5f1t-U9kuPJyrVm9Ky3smvyG2y489LgUmqFoIt_sSYTNv7U16ytcfwbicuOYIn4DtdHENVPxwahzyNCMp948gCYLu8Fh7fqRZjWPjRRAH6Ozj3sfJaSXnz5kslxSqW37AJAUGtJPyp1batxSLctitqmgpYwDbHr9NKQFU19t8KqWDObL7ypU_PsOGvf3CsKys3jFOtjstQ6UZW6Mb6W_3hwqzzv_Nd5o4knefzR0ZFmSSkJE81qLZXicke9C0OTfGFKkOlHbzLGGV6Eb9Kx9RrnYLv5HVQJEcjtcMV3dZU0EVMXjId1ZEh5w4yNErPcIwARMwyDpD_7rxJsn6HQFf_GvMq1bG7mmqqtWl_EZ74rW6ypiAfA2DE1sTjefpE-JZ3MtEbf3BDJicqx8uG3lBwsIxy3f-OAV-AKA_8HXXfX_6ouTBaZ4ycPgrvZaFsrWPnufo0Mg4aNWPB69LU4hzex2kXPFmxoPpMWgb8iXa3HTSMqgPk5cwM0gHkhR6a_Bb_fBj1p8rDJlgBoNUlamXp90ey5zFfiSf8HOArlYCxZGL8beCFO-7DubZKYwOkYhaxFu3rQVzToKa4g-BZfxFvBn5xTw-41aRuG3_w4Yny_UDGiAkeyKKo8-SPQ0ba9kW2R2GPdlQ9YORAyYT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbef46de48.mp4?token=TMssHvBl-BWslwf9VZ3KbcQkw5f1t-U9kuPJyrVm9Ky3smvyG2y489LgUmqFoIt_sSYTNv7U16ytcfwbicuOYIn4DtdHENVPxwahzyNCMp948gCYLu8Fh7fqRZjWPjRRAH6Ozj3sfJaSXnz5kslxSqW37AJAUGtJPyp1batxSLctitqmgpYwDbHr9NKQFU19t8KqWDObL7ypU_PsOGvf3CsKys3jFOtjstQ6UZW6Mb6W_3hwqzzv_Nd5o4knefzR0ZFmSSkJE81qLZXicke9C0OTfGFKkOlHbzLGGV6Eb9Kx9RrnYLv5HVQJEcjtcMV3dZU0EVMXjId1ZEh5w4yNErPcIwARMwyDpD_7rxJsn6HQFf_GvMq1bG7mmqqtWl_EZ74rW6ypiAfA2DE1sTjefpE-JZ3MtEbf3BDJicqx8uG3lBwsIxy3f-OAV-AKA_8HXXfX_6ouTBaZ4ycPgrvZaFsrWPnufo0Mg4aNWPB69LU4hzex2kXPFmxoPpMWgb8iXa3HTSMqgPk5cwM0gHkhR6a_Bb_fBj1p8rDJlgBoNUlamXp90ey5zFfiSf8HOArlYCxZGL8beCFO-7DubZKYwOkYhaxFu3rQVzToKa4g-BZfxFvBn5xTw-41aRuG3_w4Yny_UDGiAkeyKKo8-SPQ0ba9kW2R2GPdlQ9YORAyYT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
روایت سیدجلال‌حسینی از درگیری با مهدی‌رحمتی در دربی خاطره‌انگیز سال ۹۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94892" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
فوری؛ ترامپ: ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94891" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7563ec49d.mp4?token=RjKcrxWQ6C-8IjgQZ_fhO7MhFeehSsL1ewzikGoJ1TJQ79jbjAVvJC5sC3_AVKu-iugw5wRfGKLfuddvX2tJe01dn5R2OGiKUQO5E6xrctIJawxgGXYpWqw-6Ie-VhJwl4HVwH551gTOTCB7bmQ6e71tNxIK4A3AoOc74eo4YI0Np7emhNZm8ZDaOpGEerX0wFJ0paJjy41xO-sdyIFjaBsUfZ42fmuX_0Xcde0aIB4RUBrdaxz_5QycSUlFbqNdgoZ1LI9pDlVoQ0guFkdoIAuuregccH7MogguFmW8vLrMBPFWA_TGgzCfvKp8HTkIh_66kGCz_Czi9kQdYxiHFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7563ec49d.mp4?token=RjKcrxWQ6C-8IjgQZ_fhO7MhFeehSsL1ewzikGoJ1TJQ79jbjAVvJC5sC3_AVKu-iugw5wRfGKLfuddvX2tJe01dn5R2OGiKUQO5E6xrctIJawxgGXYpWqw-6Ie-VhJwl4HVwH551gTOTCB7bmQ6e71tNxIK4A3AoOc74eo4YI0Np7emhNZm8ZDaOpGEerX0wFJ0paJjy41xO-sdyIFjaBsUfZ42fmuX_0Xcde0aIB4RUBrdaxz_5QycSUlFbqNdgoZ1LI9pDlVoQ0guFkdoIAuuregccH7MogguFmW8vLrMBPFWA_TGgzCfvKp8HTkIh_66kGCz_Czi9kQdYxiHFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
ریدممممم حاجی؛ قلعه‌نویی و نبی اومدن وسط تمرین پنالتی بزنن بعد گلر اینقدر طبیعی شیرجه میره که نگم براتون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94890" target="_blank">📅 17:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0ZUROUnYTdEJO6Q5UJuE9Eud_OtH9McTASbB2vMnKEBMpVovt2jfZPzxefc-bAvMdYSoffEnKXN5WRw-gHuvhBehrKBQbY24U2EvEhhq-tnj_8CoG7XDYJvx3BEuIaPlMgfQ9RNN7ADUgvlsFJQKSWMcxll3Li_eIzKn3YkZUjfV1PW6MC4nGoHBkwV8UxzynDMytP4ftoupOLUXB1Z9QKB8-dvFGgfy2IFB_CrOE41zH_WHLdqO1sRvva9SO-8BMcxlwo8vX_8P6yCmch1PlHV7xn8JfNQGKSzPEKsHJ2weR56SwSt9DVafD-CRmo99xKb9dNfbPdBBDsYekMH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇸🇦
پیشبینی اوپتا از بازی امشب اسپانیا و عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94889" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e2a144d5.mp4?token=Pj9DxOZtQGIQnmvHtnkE9FgBHYJ0ZxRdPHl_FrOKyR1wk4Bks5UrLm3bwMbx2MybC3RcE3ZozI_iQiGQKP7lYPfmurQo8s1F6NA-DM_1Gjn7UuvOXNYN3VUoT2mTvh_nZvhYwym4NS-AeBZwP_8gDR-cBYahT4DCZtCRJfstOX-NILYF0tBstd_sMmudW2zkDskk3cNYw1IWT5Y7eoE74k0_FqFJfCuDRQVa2-pRCCaAyzLVK7tBNfgQA5RrlvKjb3nU0E0mmCILK-z3TI4VslLitHWVXceCw5yKDt2oX_jBA5S8X3c2RbTvO_vUVoUcdnmC5dMcazuuoX-gSk5OCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e2a144d5.mp4?token=Pj9DxOZtQGIQnmvHtnkE9FgBHYJ0ZxRdPHl_FrOKyR1wk4Bks5UrLm3bwMbx2MybC3RcE3ZozI_iQiGQKP7lYPfmurQo8s1F6NA-DM_1Gjn7UuvOXNYN3VUoT2mTvh_nZvhYwym4NS-AeBZwP_8gDR-cBYahT4DCZtCRJfstOX-NILYF0tBstd_sMmudW2zkDskk3cNYw1IWT5Y7eoE74k0_FqFJfCuDRQVa2-pRCCaAyzLVK7tBNfgQA5RrlvKjb3nU0E0mmCILK-z3TI4VslLitHWVXceCw5yKDt2oX_jBA5S8X3c2RbTvO_vUVoUcdnmC5dMcazuuoX-gSk5OCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
واکنش صادقانه مردم ایران به بازی‌های جام:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94888" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2kiQdhOOw6ev4mJgMUBxNscCtCyjnO9Zu1cRaeHLAELJcaLxHJKsBN7Sx_cQO6OAWG_yGqVKxIoPMP3aftDHFPDiw3O2v-Sp-Myl8PouIjsTyg1vX5eQh9Z3jTZg7IpC2xR_dI8xvVBOXplQzb2D_2ZWkcca-Wu331DwAPxpptstOIpwXO3N6yu_SuWpTN-eYSLQ0NxKQIY7vlhA-11Qx84nyNN-CkD8C5qWNrAmSFUF1G5qnbenwEFnORab7gTdaYUFW4b2JgKsdI0h7CKbBwxu0lvypQ9T_otM3lAnMepjj9YvzKgbHgfD7gouCDOYSdgk6NorzTPsy0HqozPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عراقچی و ونس در محل مذاکرات ایران و آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94887" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_sv7uNIqVRURCGd128D9R4x2GEVbF2IRQfJnKrtKDWwNUXJw5MZZEHzRzDG0JEK6YjcycQTSuuydG-Xt42sTNLoJ59zI4I8tZ5HuUfHTXfqvheNddNGvFNYe27pUHyFFl5vu4io8APmO32L1xqzurEdNhBcRzAcLMOHi_nETTpbCCG5RkvaU7Tr5N7P_57LIsKCW1YIjJByvSwRFeOKthV2PWCx2SFVU5AZ1vUmtV4PA7CTYWGoVqRaMzrkQpB4uGbV5poHNqfyPy0pJRkRrXnFgnUxxF8udAmOMgLVAUlM-xGCuIRb5kJyBE8gINRVJTy_m6EJCdyz1Kkh0AZ_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ورزشگاه آتلانتا بنز آماده میزبانی بازی اسپانیا و عربستانه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94886" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK3466GZVM91OvQH3okJ8QJdL_q9mYmFKfjWvxq74m5twTeBWNHC3qNeyi1VmlYGzVbyNJaAHXtVddRlmaWWs44iOCHQk1vyqEYDUjT8JsnB0o3LVqgl7-Be3-5tj6RyakAhFlhgqR631M6-B_uXRKLf1bV3BJ9K6s4sw6HZ9JGSehYup3CdIEp0Xq-yoM1vcxpbB7ViTN83Rr1BNs5120C6m3G1j2F2JGoJ6dkXSY6PFne0x8yuxAgBxjdp6fTSCCha3gfDNGTNLWr0AH7K-vnXiZKPrg2qQCa3AD0cmyvNsYgMc7XPwo4dUGNPuyZnwM7KEpH2tTZFtfxDN3hvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
موریاسو افکت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94885" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94884" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT85_b_cdV68_BMnuiVqYgKoAhUtUS1Pds5KmGIhz404q076THcFdrUbT4EnEO7CEbBuLnhMhJdQFJSKYlqgkKmSH-obZVuUVjqfFfbFEI5o_HmM02xP31yWRU_LYN32n3WXE4cZKIFHdVcKqZJcEMbIB12vBcHyVPfI642SCD0k3ZDnTyQZPlVsH7CDl9en8yZaUTRY1q6SB7CsnCP68ET-dFsri8-pRLwVLtl7epa8d1T7uymkClwtXuej_V2JFaUhuuUSDpkpNYz1z92VQWr_fStrMjIWW6r5B8Z2ody5OdiTE98jbOApWXWdMVnALPErgyvdMU4mjgrhZFNqpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94883" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a47a2cec.mp4?token=pNdnbBU_PlexSL78s25xVHQeYIHoDGy-5xWyQeakncF1KQZpwT6L97lN9ZorPT4kliqtBxUCSecxsRTfUXjhNy9-maAm1PAa0lqdvmpLpxIYqdJZUBA4wy8RrvUHjaFsfCy5a2RWi37EWGytv1bIZZMgjnNwKxNpFueMq0baCJjqWeobEN3O8SxfLkQxasAlrVu3hpkBNHRIJ_vbftYQgPQNucSbh2vsvmjLTT9yuoCxRYaWwlugjw7v1Xo5iADQmYEcK4n6MmHaltQlsKVSduUCcK9nolakOVVvXN3Ag83W1xPgeqSjZmVoq4Dbe-qA0yt6DoYNnjqiU3LQH0N_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a47a2cec.mp4?token=pNdnbBU_PlexSL78s25xVHQeYIHoDGy-5xWyQeakncF1KQZpwT6L97lN9ZorPT4kliqtBxUCSecxsRTfUXjhNy9-maAm1PAa0lqdvmpLpxIYqdJZUBA4wy8RrvUHjaFsfCy5a2RWi37EWGytv1bIZZMgjnNwKxNpFueMq0baCJjqWeobEN3O8SxfLkQxasAlrVu3hpkBNHRIJ_vbftYQgPQNucSbh2vsvmjLTT9yuoCxRYaWwlugjw7v1Xo5iADQmYEcK4n6MmHaltQlsKVSduUCcK9nolakOVVvXN3Ag83W1xPgeqSjZmVoq4Dbe-qA0yt6DoYNnjqiU3LQH0N_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبلا سگ‌ها موقع پیش‌بینی بازی حساس باهوش‌تر بودنااااا
❌
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94882" target="_blank">📅 16:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💥
👀
🇹🇷
تنها تیم‌ملی لایق ترکیه همین والیبالشونه. ماشالا یکی از یکی دلبر تر
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94881" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b04b1860.mp4?token=kJsAPF_c2meUU0buUcqD44mHb2faI5ElXyFACe9NGGXnK-Hc87FppnAY350zmFXPZ_7IYJy-AvNRTqvX7MYVqnswxLKf2qSBhJkJMQGdl5Yui7ejrbkbvJ4_vJF3heQLHx8jNcts8sV0BHojgtxBIuRJEjKrtL72GuxS8v_acEylLNN_c8cWAupcEpGZkjrQo28QOm5W7g49rjDWyIroArVjrzDYeInbbQMAWtZ8erAT79xaQ2lg8cB2kgFDT3xVj9-hiArt_G_TyxdJWholrlsp9mytUoI46hn8QIsZX9IC0TTDj0v0q12tfJjgYTce9cG_6_HzBoXrnROif9sUOFPvLdWw124UslXm4HWtr7T5XrlFKR80kNFbxLifcSJ6mkz9cjoV2bTK4RdjJIK0xJrwdTbxeIt0iDIkVFXVwW4tM_n-pNg6QdHohuh1DbDPoponukpe_HtyedJ3UtVr1v4AtzZRzR9eyA0qBbaiVrFZJ0T-Q1byISY_RSv9Yn06UkpjZS3wWK3HE9WlD3gWpQoT04lWvRu0ovyCIjmaw2EVrY88kyVvlta2WEdAsR4JfmqBjtHSpZfUTKQos-pG4IujAzGo6SexrcTO-kH-J8keatQ4Ai4o1nmMEZVJouCuco87oODLaEiXyxgAcjsKm5exTgMoNMBbKldDDqlJCFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b04b1860.mp4?token=kJsAPF_c2meUU0buUcqD44mHb2faI5ElXyFACe9NGGXnK-Hc87FppnAY350zmFXPZ_7IYJy-AvNRTqvX7MYVqnswxLKf2qSBhJkJMQGdl5Yui7ejrbkbvJ4_vJF3heQLHx8jNcts8sV0BHojgtxBIuRJEjKrtL72GuxS8v_acEylLNN_c8cWAupcEpGZkjrQo28QOm5W7g49rjDWyIroArVjrzDYeInbbQMAWtZ8erAT79xaQ2lg8cB2kgFDT3xVj9-hiArt_G_TyxdJWholrlsp9mytUoI46hn8QIsZX9IC0TTDj0v0q12tfJjgYTce9cG_6_HzBoXrnROif9sUOFPvLdWw124UslXm4HWtr7T5XrlFKR80kNFbxLifcSJ6mkz9cjoV2bTK4RdjJIK0xJrwdTbxeIt0iDIkVFXVwW4tM_n-pNg6QdHohuh1DbDPoponukpe_HtyedJ3UtVr1v4AtzZRzR9eyA0qBbaiVrFZJ0T-Q1byISY_RSv9Yn06UkpjZS3wWK3HE9WlD3gWpQoT04lWvRu0ovyCIjmaw2EVrY88kyVvlta2WEdAsR4JfmqBjtHSpZfUTKQos-pG4IujAzGo6SexrcTO-kH-J8keatQ4Ai4o1nmMEZVJouCuco87oODLaEiXyxgAcjsKm5exTgMoNMBbKldDDqlJCFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
جمعیت پشم‌ریزون دیشب آلمانیا کف تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94880" target="_blank">📅 15:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd444c9174.mp4?token=EBCm0iPZQTlhvHG_1__pMLiMR-OpVu5iI4-x378YstRAzHkMGhDRNF1Q6vHovlr9lJT3W0MS8SwUiaozTrR_ciq27F-utILNqbqPyIXB7EeET9qT29Y3pMJDjF0Y8NQx67Kpqc7CKk2n5NSXeZDE3NoVfuXFrCm57TsYNwG5-LoNy4tu3Ovn2Jb_d-wR9IshJ7DgC3abqcvY5SJuezXoZBsg7v6y637UO2CT1e4NIhlurceGNgaDQYkNMoS9n7UeQnnpUxiUNhQMSslTNQ7IxLA-AJnCCSvuBUxU_sXuobDQZPG_ssQYtWx0-msw6JltlPnn-I8V6R4GMi0E_Cr9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd444c9174.mp4?token=EBCm0iPZQTlhvHG_1__pMLiMR-OpVu5iI4-x378YstRAzHkMGhDRNF1Q6vHovlr9lJT3W0MS8SwUiaozTrR_ciq27F-utILNqbqPyIXB7EeET9qT29Y3pMJDjF0Y8NQx67Kpqc7CKk2n5NSXeZDE3NoVfuXFrCm57TsYNwG5-LoNy4tu3Ovn2Jb_d-wR9IshJ7DgC3abqcvY5SJuezXoZBsg7v6y637UO2CT1e4NIhlurceGNgaDQYkNMoS9n7UeQnnpUxiUNhQMSslTNQ7IxLA-AJnCCSvuBUxU_sXuobDQZPG_ssQYtWx0-msw6JltlPnn-I8V6R4GMi0E_Cr9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولیسه تو تمرینات فرانسه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94879" target="_blank">📅 15:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d5db04cb.mp4?token=HMM9WniHGvR9ow5Lp-RsqtLdvDhr3gvoPLdhMa2DhbHfgVLxKrjYn2Rczn4gbTuhPijFIVCqAaN2aBT8l_ZdxbXONmmiMsEEh66628UE6v_AUkPO4uu6sDIQ5cPeKKQa9QfMTxG3dSUL2yTTGLPS4tvChD5KEG7qIn9OUUxVSCAC-C-BYjUc8HUqASBAXAys-1CAOKXN7XUdXWw5JPvHWbqJ4WK_IWVhb0G-KQgcVpAim7CuPk6lsKCwpM-P3C3QFn3bOxBfj4L4-JDciEIKGMFsN2IKN1IcsIW5pAko1elgFIKb2Gsa5wuV6_SnbNGH_PIhLdjj4h0x5EkrGbRqdzYDOT3heH0aG5nUkIecKsmQQwyTh8Di8YudT-ZCJsE3BQdPQL3DmD_-Hm1C-wMIFVl9C0-s7s5hFbei3xpF_K1YOL6MqDevRwf3ZqpK2tT3e0HYsaggYlvMDHrDxFY8Nrm0jq3LfVcEYd6piLJ0qrtvcK8mM4-gg4A9pBX1GqSDQHkEyFa9LSfcWCasGFZ1LLeiEnKMf-aVG5ZJfiPhae8Ad001TpPPJwEKluAh2ZwwkPiPkedcMP3wvEnFTwxeovaHBddIuu3gcEk6FxwUo32fHSd3plxAn7dSz0aRBUQNeCKrbRy-JksNFbkOzV1nbLge8byw-ueFbC74aKnoos4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d5db04cb.mp4?token=HMM9WniHGvR9ow5Lp-RsqtLdvDhr3gvoPLdhMa2DhbHfgVLxKrjYn2Rczn4gbTuhPijFIVCqAaN2aBT8l_ZdxbXONmmiMsEEh66628UE6v_AUkPO4uu6sDIQ5cPeKKQa9QfMTxG3dSUL2yTTGLPS4tvChD5KEG7qIn9OUUxVSCAC-C-BYjUc8HUqASBAXAys-1CAOKXN7XUdXWw5JPvHWbqJ4WK_IWVhb0G-KQgcVpAim7CuPk6lsKCwpM-P3C3QFn3bOxBfj4L4-JDciEIKGMFsN2IKN1IcsIW5pAko1elgFIKb2Gsa5wuV6_SnbNGH_PIhLdjj4h0x5EkrGbRqdzYDOT3heH0aG5nUkIecKsmQQwyTh8Di8YudT-ZCJsE3BQdPQL3DmD_-Hm1C-wMIFVl9C0-s7s5hFbei3xpF_K1YOL6MqDevRwf3ZqpK2tT3e0HYsaggYlvMDHrDxFY8Nrm0jq3LfVcEYd6piLJ0qrtvcK8mM4-gg4A9pBX1GqSDQHkEyFa9LSfcWCasGFZ1LLeiEnKMf-aVG5ZJfiPhae8Ad001TpPPJwEKluAh2ZwwkPiPkedcMP3wvEnFTwxeovaHBddIuu3gcEk6FxwUo32fHSd3plxAn7dSz0aRBUQNeCKrbRy-JksNFbkOzV1nbLge8byw-ueFbC74aKnoos4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
شوخی‌های خرکی هوادار برزیلی روی سکو
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/94878" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf8lVgObQomP06x-OtJajeh3d_hKamqu5CNFWyYSgL7PsynTFGkNUHHXX71PkBjx6KkARKI5hIUyx0x8fGe5gNdvP_mRI4-j-VkvmdRqenS5tv4AVGTYOxm3J9-hp0GTrCR3emMjCoEmETP9_O09Sm6u4q3mX7lod47GOdCjTqUAIQoNaeSh8V1AKiAx9ej0jfbhE2NRD1LGBlwADEzD-KUaAX2afC-U40nJpzYIiBrO4XBsaZ_vgNGuoOo_l5S1YtHIVwfovyTu_xFrzKcZNOZzMZ5mmZ9YS6rODhdep81Qi337HYWbiFGxyLJx5OLoZHX4V73Uv20T8IugLkH-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ آاس: رئال‌مادرید والورده رو غیر قابل فروش اعلام کرده و از بین شوامنی و کاماوینگا یه نفر تابستون جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94877" target="_blank">📅 15:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b9907c47.mp4?token=iCtZhbQwNYgxeMircWnAXFRZAzBpP-TfXa2fpII9WOuFX0ZuqmYEqc6scwvKtI4qegORwD-lqaYd34BFkgDYdT1gq-HAPvcqQIA4gsmPt6zYghlfRb4ldVPkthSJhfzMRAPwFohZ_DyXscFzh67CkPYDV28bwRcTEl915X9nz3HgLVamKXK2GLzUCkXyMoHtRKZT4wiwQ56_RGIqwc-N5RNJDkBrfDaG-dErEYfhEx6xTDrkGBsYm09ibDCGQtuJhLgqk9-qjx092-cgrp0ukhIacAFyeXmM6uOxFtJnfP7i6kD0IuLoKogFEMQ5mQG7UcXcVpDA3e_n7Ic0t2WLtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b9907c47.mp4?token=iCtZhbQwNYgxeMircWnAXFRZAzBpP-TfXa2fpII9WOuFX0ZuqmYEqc6scwvKtI4qegORwD-lqaYd34BFkgDYdT1gq-HAPvcqQIA4gsmPt6zYghlfRb4ldVPkthSJhfzMRAPwFohZ_DyXscFzh67CkPYDV28bwRcTEl915X9nz3HgLVamKXK2GLzUCkXyMoHtRKZT4wiwQ56_RGIqwc-N5RNJDkBrfDaG-dErEYfhEx6xTDrkGBsYm09ibDCGQtuJhLgqk9-qjx092-cgrp0ukhIacAFyeXmM6uOxFtJnfP7i6kD0IuLoKogFEMQ5mQG7UcXcVpDA3e_n7Ic0t2WLtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
کنایه قزوین‌طور عادل فردوسی‌پور به سعید دقیقی؛ بهش میگه بچه خوشکل بودی
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94876" target="_blank">📅 15:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAdbXQXV18_Rs9eyemmRVG2v8ddun4rNxzq_mm_UZg2kwetdeqY1nQxCp1XBS7tcix-nGH_NOhMOALqMQ8ba4brKKOjeprzgVwElTAe0a6sGbW5XRppyV8fL2n2y3od-BCVMn6EiQtL7m8eioeozE48VMvcikTaHF5ZiDN_dQrPNGYOKxhnXCbLHr4x-pWqxtsT7QEzit5nw5WPZ-9DY7kOQQ3kLUDLENDdG4Eo1eelAyUP-D_WGutRuwxUCfZGCceifp0ZNtqeiDqEHXRcl_RZQ1GhhyVzC7ts9w9Jk8QGwM89s7vXI66GABdjHgaM-3IAkXDd8FRPt77Hn4qDYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
به احتمال زیاد رودری تابستان آینده منچسترسیتی رو به صورت بازیکن آزاد ترک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94875" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه ارتباطی بین برده‌داری و شادی گل وینیسیوس وجود دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94874" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0e690550.mp4?token=vM3vQf2p0eNhcwxpyrIlBpZBxjI1Qu8eOfvx68cNyOnMabmBQVK1q_Gbgq6ihOMzVKc1xwCX8bwKB3DbwtFu2kbzEVj5rCI-IbEqyLjA6s7_rOZOd3B1c3AWYtP1nyMdwfYP5TX1q98pC4v_x2-edd72weTCZSYCh7ng_MvWRAjcQpGFIyKf4lxDVMOnBHo42_k05yKpU2UpZuRqeQzuG-jDGsGiAP8sgfsQYvozVZ0Mi8Lnqne88edyp67BpzrIHJrNfjShCeu11E8msDu-upUtovsRU-Uhm8nvOJiW52r35A7bl8uDe2Rp1w9VeLZynm6ydSNUcpVMECstVFKW5hL6FIAHFR3fzDT1_RGQc5qeHg7HCoXnWEWlRiej4i3VOD72RRabj5zeS69KmJbDHw0VZdspjPH4cdxG4iuZXVHt-5dMovHZOHW_gVso9AdxikREsPEEIB7DXpNnuMPqldQiWVFViZuChwJOgua-VA2ivkUCOL-ra8xE_8Zl5NY9ys7qfXkOUcThGQVOm5gmmWi9pmhVoE70MXziffdDSx9M390v40w3xuSjUeiS17UAbxOvY9fgtHAaQhkrv7rQ1l26y8d46bcZwJwRhXVx1tOtVe5XK5gW1O9AxhZLJqzl4_UyoJUep5Y-ibcrHzIel3UFF9dSyr1KwINFu9LdRtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0e690550.mp4?token=vM3vQf2p0eNhcwxpyrIlBpZBxjI1Qu8eOfvx68cNyOnMabmBQVK1q_Gbgq6ihOMzVKc1xwCX8bwKB3DbwtFu2kbzEVj5rCI-IbEqyLjA6s7_rOZOd3B1c3AWYtP1nyMdwfYP5TX1q98pC4v_x2-edd72weTCZSYCh7ng_MvWRAjcQpGFIyKf4lxDVMOnBHo42_k05yKpU2UpZuRqeQzuG-jDGsGiAP8sgfsQYvozVZ0Mi8Lnqne88edyp67BpzrIHJrNfjShCeu11E8msDu-upUtovsRU-Uhm8nvOJiW52r35A7bl8uDe2Rp1w9VeLZynm6ydSNUcpVMECstVFKW5hL6FIAHFR3fzDT1_RGQc5qeHg7HCoXnWEWlRiej4i3VOD72RRabj5zeS69KmJbDHw0VZdspjPH4cdxG4iuZXVHt-5dMovHZOHW_gVso9AdxikREsPEEIB7DXpNnuMPqldQiWVFViZuChwJOgua-VA2ivkUCOL-ra8xE_8Zl5NY9ys7qfXkOUcThGQVOm5gmmWi9pmhVoE70MXziffdDSx9M390v40w3xuSjUeiS17UAbxOvY9fgtHAaQhkrv7rQ1l26y8d46bcZwJwRhXVx1tOtVe5XK5gW1O9AxhZLJqzl4_UyoJUep5Y-ibcrHzIel3UFF9dSyr1KwINFu9LdRtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇼
دیشب بعد از تساوی اکوادور و کوراسائو، پادشاه هلند به همراه همسر و دخترش راهی رختکن کوراسائو شدن و باهاشون خوشحالی کردن
کوراسائو یکی از جزایر متعلق به خاندان سلطنتی هلنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/94873" target="_blank">📅 14:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af848d920.mp4?token=JbfyzWWP8to57_3SnRSNVX_SKr57jaxV_5tYoOBg7hzwawRVSzsgUUh_9gQBXYgYNgVONT3mYDICZ4uOm5VfzcoeAXFrRB5VwnP-eIzN8JE_wqzmxNkFH9nuilRH5ANkh_R7cuCKq6VsPH0s6InlEMp2FDljme2Ypj8tVI2siWZM9x13jY2vfD72VAYiQYDJlnbXD9Wu7aj_jtFCqIapLXDlQOLtgQP6e_v3KrXWm94hITVvjTwQN-lI16fBcybvKCNFAf1hqrdC2SV03_N71jeW_K2ekL3RCwo8NGg8x7htlgngcD79TJ1SrTjS-w-8ufatIxzjfeLdUraoM3WhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af848d920.mp4?token=JbfyzWWP8to57_3SnRSNVX_SKr57jaxV_5tYoOBg7hzwawRVSzsgUUh_9gQBXYgYNgVONT3mYDICZ4uOm5VfzcoeAXFrRB5VwnP-eIzN8JE_wqzmxNkFH9nuilRH5ANkh_R7cuCKq6VsPH0s6InlEMp2FDljme2Ypj8tVI2siWZM9x13jY2vfD72VAYiQYDJlnbXD9Wu7aj_jtFCqIapLXDlQOLtgQP6e_v3KrXWm94hITVvjTwQN-lI16fBcybvKCNFAf1hqrdC2SV03_N71jeW_K2ekL3RCwo8NGg8x7htlgngcD79TJ1SrTjS-w-8ufatIxzjfeLdUraoM3WhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرهنگ علیفر امروز صبح سر بازی ژاپن اینقدر حماسه آفریده که کم‌وبیش ویدیوهاشو براتون میذاریم
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94872" target="_blank">📅 14:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKVwnpYl43FU-CzxLFZ0yVFjhmS4vzBj8eFSZy2Sf1pUwDKpxz_8GC42HUnzDx19vuQ5f64pS7ZMHr9YBGqjGMv31Du0fj_knWLpvtY3VDfFLHXiettCTg9af1bW_5kwLjmj33xTBKRPWN4Y97ROYefkr3EHNQkqu32RG14Ps2P-8L1i2Oit8-O1HOsMqPuEox5rBZ_9hjg0YwftFQfnzkPBQY_dwX5GTKZs9R6APasYYIUUsF2OyRc_cf5Ek2Q3_oDsEgppan99qBt_1804I4DnXK_ykiaON_TUWI1QKBc43L1B2GEPUo7QGXQ7W930q4sa5-T_rKnmxB66grZgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
تیم‌هایی با کمترین میزبان مالکیت در یک بازی تاریخ جام‌جهانی؛ هر جا سخن از ریدمان است نام تیم منتخب ایران میدرخشد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94871" target="_blank">📅 14:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufD5HGc7ERWMv-2W1Pn1H1CGGH3s6Xl1fFcT-woH5bYMFtB0auqagWRHpx3S4jx4rk_wpMbe2LYxLNHw28fy5u4hFcpArXLBh_t3RfNsYNdui31cKmIZWEQAitZEyh7V6FUOU2HoGc9Cezo3PUG8YV9S06f-PtWXUAk-HJ1Fm6ezUEkJ1J45h7MNqclNWXogvqBp2IA9cFsaYG4Z7DBYpJO1W116FUEuOKBUaTuWTf7EXEHuJQG-5Sf7QaVdiXgj46czA-f-G5HEEMLzmSyekJKzjOO9xpbrzVMhI4TwolSk7kkJCtYEWb3Ll9qNN0BQs5LvHvyNRSYmBYsVcgqNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - بلژیک
نمونده.
🇮🇷
⚽️
🇧🇪
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94870" target="_blank">📅 14:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTNDJU2f5qAGD6Gu2gaU4fw-DT8OYpISHsQwN-GHqZcOFa_Dx3e3qhAP97pKiYGzI61jMSOlclxvOYzgGh4ol0pWIaGRn-Qcbd4PEp28bqX7Y-YrYDEBNNP4S4ldgxg6MW25w31OZJidQHa6IiFVCjKpBFeEL-98nRnhBE4G9C2S37DpVMe0mGUrOxzJ0TrJ4KiJX9-ryzONuEAPXA1RXRu6wnlr_P7JXdtphpnc4-anKlGCR0RBKpED-iEU1is3RUDyalLZgdYEY4t-2YVIVaHXOyrEuKs6kS8DOPK13u50I_VKobNSqsdq8Ay_8-FdpJ2J8JX4cZhIePdR725U6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
امیر قلعه‌نویی: "از مربیان حاضر در جام جهانی مثل اسکالونی و ... و کاپیتان‌های برجسته جام مانند مسی و هری‌کین می‌خواهم علناً درباره رفتار ناعادلانه‌ای که تیم ملی ایران با آن مواجه است صحبت کنند."
🤣
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94869" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac5f38e3d.mp4?token=ozzCuZYwWZYl3yrFkLfMdCZdB7apYFxLEvpoZrWs2cOk0GP8flwpmzfHEv5O0r4DJfyLwwQE0EAH4PndFMKvMQrrFlK6BORJx4f_RWrpHeEbXsOntTFbAh0wUTHaopV1PTFVJwrLx1O-zaJkoMX4jgPWxPDCTPdqfqxQMH3EONWovsiJBciynADWqEOr0fK8r4BysreisA3Bbo6L_s2ZcgPdFYm80ROuKJAK1fwxSgex_G2B9hym8t_EObXyM9G0kpwZIKPaGnIoojod-0rS7rhNTWDfl1WU-B5lL_M9EPvbhKk5JYIjTMZYYP10krPemcx42Rxq45aHcAtMJTT6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac5f38e3d.mp4?token=ozzCuZYwWZYl3yrFkLfMdCZdB7apYFxLEvpoZrWs2cOk0GP8flwpmzfHEv5O0r4DJfyLwwQE0EAH4PndFMKvMQrrFlK6BORJx4f_RWrpHeEbXsOntTFbAh0wUTHaopV1PTFVJwrLx1O-zaJkoMX4jgPWxPDCTPdqfqxQMH3EONWovsiJBciynADWqEOr0fK8r4BysreisA3Bbo6L_s2ZcgPdFYm80ROuKJAK1fwxSgex_G2B9hym8t_EObXyM9G0kpwZIKPaGnIoojod-0rS7rhNTWDfl1WU-B5lL_M9EPvbhKk5JYIjTMZYYP10krPemcx42Rxq45aHcAtMJTT6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
فقط تو جام‌جهانی این صحنه‌ها‌رو میبینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94868" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmju-jnyi9MD8hiPyJMXr-MbdN5seu476zO21xB_EFCofqXLfP3V8MxsczHIBQXxVFge4k_fN3cbV0LGm-LUyI0HfZ15VSRh-c2CHvmEgPn1MmVXU0mdnAeySLdmVa5QL5blntXNdQwiPf6RxJjlOzCvIUZ4IzrAFKSrqamznX7KwdYu4RH9Qu4Rr1fYWjrkqnbdFqyp3acDFo52lgbbVcFqTVXRPm6hr-9mVXvdAAZgJZ9T_mcXg6oYLgKwzfdvFBBKmfJaeAm8VDC0TJmzGnixEYqt6orNkX0ZAzAEy0mWdUjrWXQSidu4Ca5vjQjyQVGZ0_iGAO43481XCJigMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✔️
تایید خبر اختصاصی ۱۶ روز پیش فوتبال180؛ با اعلام تاجرنیا و همانطور که گفتیم سهراب بختیاری‌زاده سرمربی استقلال در فصل بعدی ابقا شد. حالا فیک نیوزها از اسکوچیچ اسم ببرن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94867" target="_blank">📅 14:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvdYJRG9JLFAG2ZeLGbXgerNFoLms3zTwee_DnpxBArFxhxtU5IwCouxQEd5K9H1Dc2b4rtQKvolfRW0-OcL_V4tMlTr40ZRYrlUf0mbsqO39vYqsC2dl_T5Y77iY6IWGZdSJwNhhPvzilY4IlP1ODv_AzFEI0FE5ScDSALa2i5Lls8jZb9talyvczy5oM-OySK39eYZo48EBjCVHTTORzjjAP0JwyWfaWptM9Chnaz3Yly9Qiq81Nk19HJ-IymWXSjGhyxO4EZWqR7BF2ZnVjtOprUT0EIsaqdsxQkr7AfU2alad9C7KUgLas6wk1zCn9nx54BYi91_zngNnvH1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
10 بازی مهم تاریخ جام جهانی از نگاه اتلتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94866" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6We0Cy2GsNVIBeiVH5H9qDjJMsSk5nSLtcdsj5jMyAL1pZCayFmvi3P5QbWSMPjdr_xzhQDBumaVhWZ19q0w6zl9_Vu7Tio1Z3Zjb5pf8Q8v6YknQ0PPVwGp5SYM3sqA6yeEVmGYcL6YrgzGerHQJj8E5npZLq5OGRF0_hk8qN2MqX3gmXjW4T6xiYUxA4qz98Ycr9v6WrPVgLaxjv6aU3wkSGOCUfwOck1z8n0z-771FaHiLHoNRBioctvH7YWdWXhXb7qa0rLR4_QQtIP9vZdh8ZKkozRz5soTBV8hpQeME7FqkBalEviS1ZsqfigCgKY-WKBa-CuwkwVuXUk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
خودت را تصور می‌کنی که تا ۴۰ سالگی مثل مسی بازی کنی؟
🚨
🚨
🎙️
🗣️
لامین یامال [
🇪🇸
]:
"غیرممکن است. غیرممکن است. غیرممکن است. شاید بازی کنم، اما اینکه در این سطح باشم.
این خیلی خیلی سخت است. و همچنین نیاز به اراده زیادی دارد، برای من او بهترین است و هنوز هم این را ثابت می‌کند.
او نسبت به همه برتری دارد با اینکه ۴۰ ساله است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94865" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXcCJXX67ZICz5jZyODb0MH9cJ594bsiop3mIvQfz_wMquWMI0oXKoWcGMaMIFIEJHlykux41pq_Sdfd3MHabhu6_NG9uM0f0-ivpuVZrI5XxA4KTzpL0UMz9_YlzOYNEVBecmOrifaFM8qwP8DUpO4luKaf17T4TXVk2FMHdPEnfdL4_O13OrfGiQ_0RzGUqVF28cS8qeDoH7HF--h1tJzYug2L1A-eBXwUjDVJgq0PCZROwChuumGfzLIp_VL6RnEKfERQ6KPBDdKt3haCDUB4PjouUS2tg7LEANsX7msg3T2DyChhzqyxhhK4VkHWFWmNpxEg_snc2LKC2KRA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🎙
🇪🇸
لامین‌یامال: برای من گل یا پاس‌گل مهم نیست. فقط به بردن تیمم متمرکز هستم و سایر موارد اهمیتی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94864" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593635efc1.mp4?token=JKis0MtgpkwajS8fVOpavb3www5jecoeAcP-1aQ0ijG7spWnMmgeLFfYI42Q8avEK3rV_fEh_1cAsWgKHtEPoz9lOP-K0NKzwKJoWNTl2IqTkJkdd-8BjggVVfZozOxvANAED1tsut-UVNPIW4mZpVmr6-gkygI8cPhE3cPrwr4X8BhZnZgrFmNMg_FtmrTnlwtDlGU2ueQkMCK-dVWux_sXyHnvT5IrvCT1QFRAkWLv2oJJiBXcZYrB-_xhMSiRnWZ6DbKmzztLeOHL2NUkjHmXRHWh4n762-infCVBP5AO33euy5Eu6_R5W_MRkiwDn8Ozza_7XHfyN4IuSFgACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593635efc1.mp4?token=JKis0MtgpkwajS8fVOpavb3www5jecoeAcP-1aQ0ijG7spWnMmgeLFfYI42Q8avEK3rV_fEh_1cAsWgKHtEPoz9lOP-K0NKzwKJoWNTl2IqTkJkdd-8BjggVVfZozOxvANAED1tsut-UVNPIW4mZpVmr6-gkygI8cPhE3cPrwr4X8BhZnZgrFmNMg_FtmrTnlwtDlGU2ueQkMCK-dVWux_sXyHnvT5IrvCT1QFRAkWLv2oJJiBXcZYrB-_xhMSiRnWZ6DbKmzztLeOHL2NUkjHmXRHWh4n762-infCVBP5AO33euy5Eu6_R5W_MRkiwDn8Ozza_7XHfyN4IuSFgACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های جالب فرانک‌دی‌بوئر درباره تفاوت میان دیگو مارادونا و لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94863" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaOvieFm3bXrp2tWAFO-hJjkEfSJCcL0BOVv7_t6khSudVCRS6uTdr98oHq0jOu_1TbWhEVS4ZUfRT59x60L8eeakP_KSZn2KOpa2VjzMdJiahoZ9bMm5wxKmjUc-KHq99ynLD1uPPmJixwHPcj_qzsUXnIyPrBEIC2D5TsfNKt-ViOtNEZPL6T22WuDCXIFuyyXBqZjCacUevHGFutY38M5wsL-b9xcpdN-VzY5vmPXZVTXHmXnjUnnben-YwOYkveRfDNlkZrwwdTWH4erxDeLPpuV9mtKfZbj361PXLuiIPHc03MREsH6zg2jx0RmvZNM6niqGmak22gsyt2cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوری در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94862" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f56e9622f.mp4?token=lWgfER3SGv0Sb6vUqHRDMfzwGwXubCS9cVHjkkJ6uJ1ldxMBTIQkkLMIGRVHz95CnO8s79UibIszgwvtbRc69sKIpUpwEAH2uuDrvNCBCLrHk26uxYtkOVDMUxPbVM0q8htA0VE5ftbzhxNIlDsJMvJ1iRpyw1v8gkBVxoiAYCHDoqyXdAfBvk8MksjhoLQEQF5lGKG_cPzd-8J1QBqZl1FIsP8crL6MYA02wLlc9KEE17Xk-wLpNAPyEIOoYa2-ptSwyOtEGG7GwpClxHM4PLura1q8yo_T3erBai9UXnBRXFCHOixR4SI8jUxwfddk_GvhVI31vrxziPPg9j7OGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f56e9622f.mp4?token=lWgfER3SGv0Sb6vUqHRDMfzwGwXubCS9cVHjkkJ6uJ1ldxMBTIQkkLMIGRVHz95CnO8s79UibIszgwvtbRc69sKIpUpwEAH2uuDrvNCBCLrHk26uxYtkOVDMUxPbVM0q8htA0VE5ftbzhxNIlDsJMvJ1iRpyw1v8gkBVxoiAYCHDoqyXdAfBvk8MksjhoLQEQF5lGKG_cPzd-8J1QBqZl1FIsP8crL6MYA02wLlc9KEE17Xk-wLpNAPyEIOoYa2-ptSwyOtEGG7GwpClxHM4PLura1q8yo_T3erBai9UXnBRXFCHOixR4SI8jUxwfddk_GvhVI31vrxziPPg9j7OGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
انتقادات بختیار رحمانی از شرایط تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94861" target="_blank">📅 13:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87bdd188e5.mp4?token=V4oi_CNHhh0vic4UgLZcUyc63rbrWMFus5iK9En_j_7cfIFFr_mgFbggf6mcIwiDzAAejbMKgyZeeESM1KMXdzGF3O_SW2cHqQYZA22sVWsIIku1NgYP1TDYb10sCXgWFY8t_EDXmn-1bwu0Kcvt8Y4jQrN9FCBlzuPuNBVQVtkzYzm-Ack9pafh79E4l1dQFJZVRpxmoX7aVXW3B8QDm-TfX1ZIFvD7GM-YWMFkEQrWcqJqaffNmElF96e-CiqUMcL4NVQyt1PV1h43Vq8fs1o3r36WNlE5DPQ56_YFzMeO2x_s28eeR8YNw8JvMUmhzPznnT7PGURE0pntBMrwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87bdd188e5.mp4?token=V4oi_CNHhh0vic4UgLZcUyc63rbrWMFus5iK9En_j_7cfIFFr_mgFbggf6mcIwiDzAAejbMKgyZeeESM1KMXdzGF3O_SW2cHqQYZA22sVWsIIku1NgYP1TDYb10sCXgWFY8t_EDXmn-1bwu0Kcvt8Y4jQrN9FCBlzuPuNBVQVtkzYzm-Ack9pafh79E4l1dQFJZVRpxmoX7aVXW3B8QDm-TfX1ZIFvD7GM-YWMFkEQrWcqJqaffNmElF96e-CiqUMcL4NVQyt1PV1h43Vq8fs1o3r36WNlE5DPQ56_YFzMeO2x_s28eeR8YNw8JvMUmhzPznnT7PGURE0pntBMrwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
خب بنظرم دیگه از الان باید کارو تموم شده دونست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94860" target="_blank">📅 13:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgWgcaYlaJnGqfs4Gxc0ivPSqN3kMRsZZPpZNScyMYJ06LAt7QECwhSNBTxOxkGA4ygVq3ItY7wbPJcqZYv51zuBWoEdf-WGc95Fi-ORW_7tCGyOtWs0-7xCW5zcmiYH0OrCSU9zcBibx7LzOCs5fwuhx02lfcMrJE30kpki-ZzTfgVg196qMaW7HM1zn7WlDFK3ep7FlOH-Rh8NyfFO30ELooomE37JNokGRRmRBALise9aTjxIrJ6q1B0kZ2a00YHvfM54Zf9uC4Vvub0qA_doyCJjnPNnCyABp1nkXS0kbezH2ShWVXWQOEvY1oFNefzUfRF2qErXKstuoeKUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید از مدت‌ها پیش ایوب بوعدی، پدیده لیل را زیر نظر دارد و استعدادیاب‌های باشگاه همچنان عملکرد این هافبک مراکشی را در جام جهانی 2026 به دقت دنبال می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94859" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea2e5c940.mp4?token=UEj2YcNaDOjI6g1yucf6rTKuuAvaneLHICQk0AbJOz19SjG260usCsSBekoBwnGShxIZ9yIFqrawcaTfOPa8nGymbDvjohOfKa5H_w2hzyLvDIMdiKpl4_-ymQxHYYBN0eKfa538vBXX-1e-h8BWQs3pW9iWUw9bmB0k8o_NqpMpEVUWB0ee4bHUBq0gkekKDXukEMP2-xK6h_JTtOpWhMVODzWijXRKCMBX7ArqX948kNEDCCiMpPPJErY4Jf2z9_beWITqHWSs1ohlQ4x5bL_ktdYHMencZ7RfM3uCHw3HpH6HOzjjMX1yyLD2N2JZpN6VQAgY7UasXfx6ZM4y8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea2e5c940.mp4?token=UEj2YcNaDOjI6g1yucf6rTKuuAvaneLHICQk0AbJOz19SjG260usCsSBekoBwnGShxIZ9yIFqrawcaTfOPa8nGymbDvjohOfKa5H_w2hzyLvDIMdiKpl4_-ymQxHYYBN0eKfa538vBXX-1e-h8BWQs3pW9iWUw9bmB0k8o_NqpMpEVUWB0ee4bHUBq0gkekKDXukEMP2-xK6h_JTtOpWhMVODzWijXRKCMBX7ArqX948kNEDCCiMpPPJErY4Jf2z9_beWITqHWSs1ohlQ4x5bL_ktdYHMencZ7RfM3uCHw3HpH6HOzjjMX1yyLD2N2JZpN6VQAgY7UasXfx6ZM4y8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
روایت ابوطالب‌حسینی از پرواز پهپاد بر فراز تمرینات تیم‌ملی کره‌جنوبی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94858" target="_blank">📅 13:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4V5QB9l43GuD8WBdgJbgfuzsLwuPt7oTQGH7fzyie8jFjr4Ne3o1AyHcWc1h8BAES_6-as9Y_CFmGsjhSP315VRUvNtl9un97UII-5Lou52JW-RLse4qIrzlSpLIH_ECcLfwc8g6iAOqVMYpbTNtmQItcR2hokdhZl252VLoUEADH2CaVbMOdCM2W796MylTWycsGb2BMoqwwgCbcLhEJSEzHH24HyDuaPlTaRfyHtXY2SZpHiJpeFdsL5eSpuqQ1i-I333ST-NM5HVABXUlyZ4RjmORGpOzWpOb_DpOI2WaT5Kmy8M7vlxxYf2CH-2OKIt0DReh8Ygqjx3T6v8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل درخشش گلر کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/94857" target="_blank">📅 12:48 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
