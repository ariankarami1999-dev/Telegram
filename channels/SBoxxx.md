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
<img src="https://cdn4.telesco.pe/file/K67_04omHfMzs0BKCtyh2ovMRvouwJRdcb03isYY8eISwCUh3NmOcgkJ-JzV0xE_4I4_zDWSxImkhnL2qZm5tbES85MDOvTXUQN_tfcYGiFey0Md33ePNm3kxdZoIRmIJOHk0aOPxA7pKXKgxe183BQPuiVc9TMhJ24ckWkW6U5mciSz-r4CQ002o4ghJ5NhfadHsbTQoUn5cf0HTTf9ME6A0iduRCtnTNMFzRq_4_TQ1S-6FtxwF3GYIktp4XOepv516dMA_F9-rqV7sC1At4JUNttavkF78bpNarhPXbHQWJ5tLp4S4oOs9Nr57pVvkaNoMtCITiXABZVB_GJyzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5dFOnxGbf4ufRK0-P0upgjY4VH6jTt-1rVcRE9cYLIbet2RBLEn3g9k44X8AqUzlEGn4bEHrw6B6LQE_BCYJrriCffbcWrFk54dnh4foucKNNttRcD-3RcECvdbkyGFwq_rAVxW5Up6hoIuxQuBpzWoROd-gRuCKdRK-GFojHHgd_c9XFX3ykIzzFB2D-PEUGZQrzfQLbDl_5ZM6nftnKl6dkuLMwzoqYwTDI9G_C7QNAWyWj2eSAETSRrooKD8eMNXzzq6H6OGJjY5ZbZj_tMC42OZS-LLpCXR9nc6RCLx1UgN8ytZMrE7V4eNZXu0UGe7tOY6ml7aP9BMo47Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ نیابتی آمریکا با بلوک چین در شاخ آفریقا هم نمود پیدا کرده و دیشب نتانیاهو اعلام کرد که اسراییل، استقلال سومالیلند را از سومالی به رسمیت میشناسد.  جالب است بدانید که سومالیلند از ۱۹۹۱ دارای دولت و ساختارهای حکومتی خودش است و اتفاقا از دید قوام نهادهای مدنی…</div>
<div class="tg-footer">👁️ 415 · <a href="https://t.me/SBoxxx/16433" target="_blank">📅 05:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرنگار:
«آیا گزارش‌هایی را شنیده‌اید که می‌گوید ایران دیگر درباره تعهدات هسته‌ای صحبت نمی‌کند؟»
ترامپ:
«چه سوال احمقانه‌ای. من چیزی نمی‌شنوم، ما در حال حاضر در حال مذاکره هستیم، تو چه آدم احمقی هستی. من در این مورد با تو صحبت نخواهم کرد.»</div>
<div class="tg-footer">👁️ 529 · <a href="https://t.me/SBoxxx/16432" target="_blank">📅 05:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7YVyeQjXZyaaUUbrATDEqd6CsUbHpr5BIz8dI5bPsWIRjd4ewHadiYAnnRnxXuZI8zAIEomNNvbbmLMBumOD2f0sysNIvjSdCw7sIJZxiHwaqLGsLftSytvG8ChrThzRFqF8QVm0I8P9kPSVG51uycLz336pq0NOyQ8oXhF6Zd3R9B1ockeWCguWyK-AYmkXJgCroX5lgWwB0p21ByK6qvTm41za939yvGRwKmPoELJcKOq97Ee79WYFgKPG1WfIIzgsiY_JHCPceLJgCq3z9E-G0CjLSQlx3d-Y8TU6ecAQcOwfDliZHz-MSF1GeGrOstgA4DvOdVV0YzSrbYzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!  سبحان الله !</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SBoxxx/16431" target="_blank">📅 00:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تقریباً ۹۰٪ از کشورها اکنون شاهد روند افزایش بازده‌ها هستند و نرخ جهانی ۱۰ ساله به بالاترین حد پس از سال ۲۰۰۸ رسیده است.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16430" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/16429" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkLhziZIoLTvFRzl6zG-8W2mmqDpm4hn5LfRihTvbGQaKXGTd0qCRm0s0X7S6TnG3IY5kDXvC_-VtsPtdl-smWjN_pzaALhZYFHnFqejgI9yZZbp-iZu6KGpODtEuqw20s9x0-jPu3W50MLh9q87or3Nx0EckSbkKUzSSHjdCkeNHNlpkuyDXftb_v4OSIOTY2PMZoa67vRxKEEd-UJaeF3QSBLHcc8P2HXk0W_BptGfeP00tXD2PvyUpRrrRF3apLHatfH8LOLVFVACfWFnt3WNnwmZ2yu_U-s5isAc4kxRRU6tOG-BAYKxGFbE8BfY2cKhSyCA0yZVuBm3aUCx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/16428" target="_blank">📅 23:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری تسنیم:
فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/16427" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16426" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16425" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic Republic of Iran, which was scheduled for tomorrow, in that serious negotiations are now taking place, and that, in their opinion, as Great Leaders and Allies, a Deal will be made, which will be very acceptable to the United States of America, as well as all Countries in the Middle East, and beyond. This Deal will include, importantly, NO NUCLEAR WEAPONS FOR IRAN! Based on my respect for the above mentioned Leaders, I have instructed Secretary of War, Pete Hegseth, The Chairman of The Joint Chiefs of Staff, General Daniel Caine, and The United States Military, that we will NOT be doing the scheduled attack of Iran tomorrow, but have further instructed them to be prepared to go forward with a full, large scale assault of Iran, on a moment’s notice, in the event that an acceptable Deal is not reached. Thank you for your attention to this matter! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16424" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLVSMXnjWXLH57ZRRnK2dKA7LkDg8HpDvybxZPF4M5L_xcNY2A74yvxYEwl6cN1-Wr6g1TCcKRqiHii7zpAPEc8wT-6thfI7IrxQl2-KZG52oSsZ6Tz3FeUTcU_LwDZXw3KA5ntyyq97BLz35yxgTP4Xg_IG6mrN1C787tiqzEDuWOnmOzLCMPo3yhKrfJcSby_uQcJ6URSRaTEnC0j_uxPT15QbiB7d3BBOWvPFaFNT-vqqfJircdba77X1ZuLZGkCTHEv-fYqu503UTiE1yhcODJ3BNZifdBllR88seEjPE6xNFqS43cRVHVDi-vyqQkvQbsDr9gMiH7zBM1IexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16423" target="_blank">📅 21:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
«رژیم ایران می‌داند بزودی چه اتفاق وحشتناکی برایش می‌افتد»</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16422" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♨️
پس از رد پیشنهاد جمهوری اسلامی ایران توسط کاخ سفید ، وزیر پاکستان ، خاک کشور را ترک کرد</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16421" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSckp3L5fCWAMFe4zOhmLNxqxGXweqDgA_Pu9pTLeY8p_0UPBdyOZ2TpBOSRsHRu-8hNWerFTejpru8-jupkbmtqeEFiL__aBpE1CxWeDWVh5A5IR4tOtfqA8vpR243mSB2j2GcP9hdFkApVeTKXdKPJweTgSA6TuktKfUwA-Jd_YbkwiPiplkfW2OC5mmqL5xHZfE3Qst83vfIJe_G7dQJWYWF2DRXU6v6I--VNX4Y8-fGoLs4O8Ue8Lfr8frWh9f5HRslxDK74kn4-QGTwUUzxhqT6lsHVgr8ffbszvcp5ZcnTVXRprzDOBTPmVZ56-uRFCj3EUhsLjPNuVJpteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16420" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قلعه‌نویی، سرمربی تیم ملی:   40 درصد عقب‌ماندگی بدنی و فنی داشتیم که 25 درصد آن را جبران کردیم، شرایط سخت است ولی نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16419" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16418" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16417" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16416" target="_blank">📅 14:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">احتمالاً زمان بازگشایی بازار بورص هفته آینده اعلام شود</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16415" target="_blank">📅 13:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16414" target="_blank">📅 13:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16413" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyhh15YPtqheFzm3HajxBFBscVMrA95XDRQvj3pb0XgX4ivzODArJjeFhpg4RLIMr_eyRdsPQU7SdCTou7tIr_gmjwQ5uilMnc4MTUl7cJgsqWOuXU_u7P2G1lj-Xqm9BbveIbDy1P1fwGnE18l-JOszoqAXLjptI5UaGIpXvi52g7Mac2ZhmX8nec1tZQPQyEpOtJm2AB8OHovjbwtdnV-yPilb3PWjzm8ky5TS09Wi_wxFtXySk57ktj3VVFQJJUMkIUScmr-GWsHC4TsX0aNPQXI1-fUy3XahIcNXduNvDN6NTnNjE6FvbLtyBYn2BWDxaRD5mEgvdHnqm_tyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16412" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16411" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COBI7cfIzy99UZMOCpxi9BaF1zbNkRv4h6ZZa_ogMu6evL-53OyYumx5aL100pww5AFmrrKaq0tLmG278olalPxqGnf7c0JAbAYynJfnG1v18rm0MmkU9AR3ud8uSvtsME-WDd8Hg0yqhevjVyWdQ4Oqiu1K0QiPqF3AkxeoX41SjVX_0AptXMLyBQPdD9f-IFeG7QdESdh13LLC7MLUREJhsduiwWduSvfwD7iUaOSPoLkcIqhJN5DDGR0YfyP7S7NjYf4yfWLCc49RpIs3YvBVRTYU_gCnuX9WJ89OaPchEGZGI8i0J7JQC3BckdMVo06yDBOWD6dZs7yUQYw-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL -- H4
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16410" target="_blank">📅 09:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcT_S1u17jS2lwruxbIYbUEWa6x220j0tTIh8NsytgbRHfZxAVyxxZ8jrE65MkhezFN1XV95MxvfATeiIFytx9NrRqHsa6FP3bpyuXAa-wrgnwBuZKF767U5FwDMkUEIzCGezuEBPZIB2uzTXAfRT9CxW9qJ1iAwBY1rvPfvdpwnC2Y7busE7OIvALndXjZHJmW4_or8pqJku4YiIjsYkJ-7bRfLrWoUvxfZt4l0fUwgd8bI_7wX_hfTVRVV-bRL1L1Oc1bWQUi964A2b1xeeKqbCN51Kgk3DBtQgfWJiWpr-w7hQTZ7YdSUVvpcXjwhCAzkjyvIeadCot8PrPgYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین که ترامپ مردد است بین کوین هست یا کوین وارش کدام را انتخاب کند نشان می‌دهد یا دنبال دستکاری بازارها است یا اساسا نمیداند این دو در دو سوی طیف سیاست پولی هستند؛ یکی بشدت هوادار تسهیل پولی (هست) و دیگر طرفدار متعصب محافظه کاری و انضباط مالی (وارش)</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16409" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16408" target="_blank">📅 09:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تأثیر جنگ ایران بر بحران انرژی اروپا
جنگ ۲۰۲۶ ایران با بستن تنگه هرمز و حمله به زیرساخت‌های انرژی، شوک شدیدی به بازار جهانی انرژی وارد کرد. اروپا، که به شدت به واردات گاز طبیعی مایع (LNG) و نفت از طریق این تنگه وابسته است، اکنون با چالشی بزرگ روبرو است. بر اساس گزارش‌های اخیر،
آلمان و ایتالیا
آسیب‌پذیرترین کشورها هستند. بانک مرکزی اروپا هشدار داده که این اقتصادهای وابسته به انرژی ممکن است تا پایان ۲۰۲۶ وارد رکود شوند. افزایش شدید قیمت‌ها، تورم را در بریتانیا به بیش از ۵ درصد رسانده و تولید صنعتی در بخش‌های شیمیایی و فولاد را با چالش‌های جدی مواجه کرده است.
کشورهای بالکان مانند
یونان، قبرس و ترکیه
نیز به دلیل میزبانی از پایگاه‌های حیاتی ناتو و آمریکا، نه تنها با بحران انرژی، بلکه با تهدیدات امنیتی روبرو هستند. حملات پهپادی به اکروتیری و دکلیا در مارس ۲۰۲۶، منطقه مدیترانه شرقی را به منطقه‌ای ناپایدار تبدیل کرده و صنعت گردشگری این کشورها را نیز تحت تأثیر قرار داده است.
در مقابل،
فرانسه
به دلیل داشتن سیستم انرژی کم‌کربن و مازاد برق، کمترین آسیب‌پذیری را دارد. این کشور با تکیه بر انرژی هسته‌ای و منابع داخلی، توانسته است از شوک‌های خارجی در امان بماند و حتی بر افزایش تقاضا متمرکز شود.
به طور خلاصه، کشورهایی مانند آلمان، ایتالیا، بریتانیا، یونان، قبرس و ترکیه بیشترین آسیب را متحمل می‌شوند، در حالی که فرانسه به دلیل استراتژی انرژی مستقل خود، در موقعیت بهتری قرار دارد. این بحران بار دیگر اهمیت تنوع‌بخشی به منابع انرژی و کاهش وابستگی به واردات را برای اروپا برجسته می‌کند.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16407" target="_blank">📅 09:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">تلویزیون دولتی آموزش زنده‌ای درباره نحوه استفاده از
مسلسل پی‌کا
پخش کرد.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16406" target="_blank">📅 07:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMoqCu6_TtAO4--FPhdNVYHth6PEV_FoBSgKgkCgY8CmfJ5qvd6yDEuUj4x1GUjxeOzw3PctdaKLst-Nl31Vd5YyNCrIUt1lYCHy26RJZlyjgLeSrUyUiAU2neEAiMHUbABq0CBMz6xVi2Ch5NpKraXwERVgfv_NpKQanO5ash5Zw1KHPEZlCt79568rRzroJvZtpeD5fcU_eHWb0cVDTtNN4XOUJ9L6_gThPQbjjjQRmYoMQyka1KUM7vAgze3Vh8hSRD0hEUqH6HXSR5MiGscUDd7BZTb3hvy3P1Um-fWD6-zWPDiSQPBJmVIHICqemyPO-a0a_pG2a1tUs6BZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  افت 45 درصدی نسبت طلا به نفت پس از ارائه تحلیل.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16405" target="_blank">📅 06:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdGSuKhqHZdSr-E6g2jkGfvT04e4BbXS1UuxG567nk5izVXxp19Mz4MIja-gR9ePX6GOsuWr7ReHrcx-G9RgszjNNKb_en_YPJ1AaZpZG-Otze9NZT2JwHzsu9NwLpUnKvnB1caAR1S-Z_Hzwq-gDu4E4XIZkxAWlzFYMRqqytnT638-wOUvK_cd1hZsqeeueoFJB4XTQyXN8p8DeOqWkbLkPImZkS7Njdp5xuW6ym5Z-Eb5g4lNKNEIbx4-TZ8-P0su73rtFkkkRbXcAHAk-GQdE8eINfbS938ZKIR-42k0g_CNpS8nzyeQzJ_I-0ii7L0C5__6tm8dB_Gw5f-3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشخص است کله زرد خسیس رفته نسخه رایگان هوش مصنوعی کذایی را که با آن کار می کند خریده و گرنه این همه اسم شهرهای ما را اشتباه نمی نوشت.  رشت = Majd? تبریز = Toha?</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16404" target="_blank">📅 06:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16403" target="_blank">📅 06:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش عراق:   اجازه نمی‌دهیم عراق سکوی پرتابی برای تعرض به سایر کشورها باشد</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16402" target="_blank">📅 05:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16401" target="_blank">📅 05:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBlQ7OqDQewGFCLppShKQ_8A_VwqJnYwyGFQP2aFetEKIk2rZVcXTIm40HQN-aznHmdy51wARdYIdrmcAv7TUnukXyzwKm2zqhPhluzo78khj6Mss7_6WgST6GTvoJLcPSjUVm6q9QWGQNeBc1Gdmb7ZT9QROHkUnCIf4CZI7pqXoaGMUZQq-WoFY4ZyeBSmC3OD7qgpokt-KB5_by5M5sl5StcgHQvP8cWp8eiWmYLL2eUn2dD1PwoD2SdlByWku_vfo8AqafHw6VAMZxf4Y4QSdG99-apfGVm469F3dODs6BPNjilJXgjKzInqzh87JjySq5VEmKsbH_bAtfg6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16400" target="_blank">📅 05:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2JJssb-hLKbd_Q8mZLCecvnL8WMEOdjzkhrr94mZhLNfMAw5vxLfKkGPib7D6wp0RbO-FDX1y3T6f9KgOGC01NgqBdtD7hXwn3Vo0Je43LNE5tWCba39PZQZWWF_J2sZlYsqNWcNLJUdRSbNuZ12kR44D2O1G0enIrr0ICCjp9xAel7KhZ1UxNnbr6EgUty-Saszmbzg9Y0gCIX0kgouIUjA4uwgrWQrSfSW2ed6gg8STlglyksLI_PVG4dZ2nD0CVlno9MOW2Sp6nmfatvI6pCXIN3MHZ5zo5bLthwHjfof0HvLR23b9piMvTQtMM1iAa9_z4537MQ9AKcZFsUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16399" target="_blank">📅 05:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124790efc.mp4?token=r6hYhDU-2GKfYgCU6LVO5TDZnGfVOBF2Yf1A4eoxj776km_CTxRv9UBDpRoCIsZDbX-D8URCPRRbL7X63-8OyjVPl-HnDhbjWRSym9hUMRWDbHak8MoXVsbSJVNkbGkjV-8LjB8TYqln5SBgrgOytYCB2kBU03KlKUX2euo1DAq50B2BG0isyL4LR103qb6q0ztpGt56vz79hxBhDgQWZvMkpFtfoJaUuqT_0LLkBF-TcabqNpVDqgrT7nbTKv_YHN2fXyXLdib40eToVQchIlDmp7Dze2ofLXecaKobsNnfg0YUX1M0gYC0SHAbaO7GtzajaX4MM9YLMxaCUeo3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124790efc.mp4?token=r6hYhDU-2GKfYgCU6LVO5TDZnGfVOBF2Yf1A4eoxj776km_CTxRv9UBDpRoCIsZDbX-D8URCPRRbL7X63-8OyjVPl-HnDhbjWRSym9hUMRWDbHak8MoXVsbSJVNkbGkjV-8LjB8TYqln5SBgrgOytYCB2kBU03KlKUX2euo1DAq50B2BG0isyL4LR103qb6q0ztpGt56vz79hxBhDgQWZvMkpFtfoJaUuqT_0LLkBF-TcabqNpVDqgrT7nbTKv_YHN2fXyXLdib40eToVQchIlDmp7Dze2ofLXecaKobsNnfg0YUX1M0gYC0SHAbaO7GtzajaX4MM9YLMxaCUeo3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
در ادامه تمرینات آمادگی دفاعی شبکه افق ، پس از شلیک های موفق به پرچم امارات در روز گذشته ، امشب ، نتانیاهو و دونالد ترامپ بدون استفاده از گلوله ،  بصورت نمادین هدشات شدند</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16398" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است! رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16397" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN1wMocndRoFtg5ve3MRZmnCjTtQMWBLcr6kB3ubCS_2TWaw90o7ii9ZComlRg5MgjEWkpZrrI0-lFdmX9-vuzmKuVgcUvU2pYVDckYvW7dHGKt38R-HkXeO8niZal90plEKKLcKMrmNwIM4gUTzFq7MAhUxpMWP311eQCVyuHTpSeOD3Xyur5-9uZ8kC1KkGhAkVjt8NQhegDjNXa0v5UI54rfsILwRpxfYCwQXM0e3t5UypZQsxM6vtpRz2GOMdEdFmbUABM-OTIvwT6sNYanJBOFLZ4Vv1wPivj2m-mTw0aWd9WUD5S9orJ6oavPmHXgdZ_YAFfeoQFFOF-70Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووال اشتاینیتز، رئیس شرکت دفاعی دولتی رافائل اسرائیل، اعلام کرد که اسرائیل با کمبود رهگیرهای موشکی مواجه نیست.
این اظهارات در حالی مطرح می‌شود که گزارش‌هایی درباره فشار بر ذخایر دفاع هوایی (به‌ویژه رهگیرهای Arrow) به دلیل درگیری با ایران وجود دارد. اسرائیل همواره این ادعاهای کمبود را رد کرده است.
رافائل تولیدکننده اصلی سیستم گنبد آهنین است و برخی اجزای Arrow را می‌سازد.
اشتاینیتز در یک کنفرانس گفت که گنبد آهنین حدود ۹۸-۹۹٪ موفقیت در رهگیری راکت‌های حماس و حزب‌الله داشته و از ۷ اکتبر ۲۰۲۳ تاکنون، این دو گروه حدود ۴۰٬۰۰۰ راکت به سمت اسرائیل شلیک کرده‌اند.
همچنین ایران از سال ۲۰۲۴ حدود ۱٬۵۰۰ موشک بالستیک شلیک کرده که به گفته او تنها چند ده تای آن رهگیری نشده‌اند.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16396" target="_blank">📅 19:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت اطلاعات کوبا تایید کرد که رییس سازمان CIA به این کشور سفر خواهدکرد.  به نظر می رسد اینها هم بزودی پرچم سپید را بالا ببرند.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16395" target="_blank">📅 19:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔘
پافشاری ترکیه برای تغییر نام «آسیای مرکزی» به «ترکستان»در کتب درسی
یوسف تکین، وزیر آموزش ملی ترکیه، در مراسم «رمضان در قلب آموزش» در استانبول، از تغییرات در برنامه درسی مدارس به عنوان بخشی از «الگوی آموزشی قرن ترکیه» خبر داد. به نقل از رسانه‌های ترکیه، طبق این برنامه درسی به‌روز شده، اصطلاح «آسیای مرکزی» با «ترکستان» جایگزین خواهد شد.
🔹
همچنین این مقام توضیح داد که مفهوم «آسیای مرکزی» محصول اوضاع سیاسی پس از جنگ جهانی دوم است، در حالی که «ترکستان» (ترکستان) با ادبیات علمی مطابقت دارد.
🔹
این تغییرات بخشی از مدل آموزشی جدید وزارت آموزش ملی ترکیه است. جایگزینی برنامه‌ریزی‌شده اصطلاح «آسیای مرکزی» با «ترکستان» در برنامه‌های درسی تاریخ مدارس در اکتبر ۲۰۲۴ اعلام شد.
آمو | مطالعات تخصصی آسیای مرکزی</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16394" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16393" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-K_3kimCHs0c1SuhKInY9OeIn9OxIuX8rXzraa2UlaPvzgoe9mad_CX2Xro_VnG0trstI2ihLhalfzmP_1VYaZKOhWn7FmPloLG3odi5E7LMBJUbUVJPpbmcxIMGW9BX04NJC4NoJAkQGW-14WifnYShzg-GR6DpeKfXP4-hZdft8Z_P7kb35MvQoIw6DuvxKovnbvd4GSVT6pG5Bd9FYBKLSxgd2wV0PB0ht_-qNPMHO6kGoq9zGn9A_ZmTkLK3lT-PiukjM7zY86CchvfiJwRyiu0LpY19mhJ7u2jKyai51WCajHDpiTEnaJfl9e-dyfWSrRmjYQ1wm8RzXNWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بدون اینکه خنده اش بگیرد روز جهانی «ارتباطات» را تبریک گفت!</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16392" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام: دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .   پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات،…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16391" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BONqKupdBCt8hmq74EJTgiCI9eMGL3qzTVQhfugXFibmrcgCsKw8LvvLYKZ8yNkdvnMXYWbTnW-lvZbw6Aej3oC6uodqxN7sJ4s8ER-a24LJi2qwahDVeYvj30vhyVtUk9dewg-Taww5rv_l_s-B_yaDAY45woOWjtAfLm9D9Jpl9DwPGoILCFT-dqjqO7NN1z15sPtvBZ_O0xAO4tPDbCNZyY6vDMEp61IglOJptw6MI-HIv2rpLJBGoa876-6MUmhKoXOVbgwMdU4AA6fzTBar2XxmuU20ZRVfaSCzuP_4TilgZm_kTM4EPh8BoAUdHslqNCx11yYRVPMzQ2CJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔑
حضرتی، رئیس‌شورای اطلاع‌ رسانی دولت
:
حرف‌های پزشکیان در مورد اینترنت «وعده» نبوده، شائبه وعده بوده</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16390" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsDNWK9JuerQIr6A4yDULgzyU-pKZJYiS9fcFq4eKqrKqNheX5RJR90LWRP_ai4bkFhfw1LDaVzLWDiZgjy3CZI65Mf4P6uu5RZefL7XOzphrlWwCozGmLz3Q0zbiGNSlA2KeZWdog3zRVPFMY3yLkAoVQNmObvhCIm_JB0Z-F9_4wlXf1n7kuPO0agPM9PeEf8BK5gJuXV0MX0An2qASNXTjEUKP9PtEJx0xdBkW67pdt8DBvOihI0oKjIcd2TBrELPNS53s6yQinXIXgliG8EzdlhKwNdKIftpNRZyaRLf5P564SVMXX7OnTKUudgOKoqA-QAxMJGuaEYU8t3suA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#EURNZD
-- H4
کانال نزولی در حال شکسته شدن است و انتظار رشد مناسب داریم.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16389" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی: اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16388" target="_blank">📅 13:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🟣
خبرگزاری CNN :
کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16387" target="_blank">📅 12:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی
:
اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16385" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بحران انرژی در حال تبدیل به بحران ارزی در بازارهای نوظهور آسیا است
نگاهی به لیست بدترین عملکرد ارزها از آغاز جنگ آمریکا و اسرائیل با ایران بیندازید: الگوی جالب ولی غیرمنتظره‌ای آشکار می‌شود. تقریباً تمام آن‌ها واردکنندگان انرژی هستند. بزرگ‌ترین بازندگان شامل پوند مصر، پزو فیلیپین، وون کره جنوبی و بات تایلند می‌شوند. در میان ارزهای اندکی که صعود کرده‌اند، ریال برزیل، تنگ قزاقستان و نایرا نیجریه دیده می‌شوند — همه آن‌ها
صادرات‌کنندگان عمده نفت
هستند.
آسیا با چالشی فراتر از یک بحران انرژی روبرو است. اقتصادهای نوظهور این منطقه نه‌تنها با افزایش هزینه‌های سوخت و برق دست‌و‌پنجه نرم می‌کنند، بلکه با
فشارهای تراز پرداخت‌ها
نیز مواجه هستند که به نوبه خود بر ارزهای ملی آن‌ها تأثیر می‌گذارند. در کشورهای آسیایی که به سوخت‌های فسیلی وابستگی بالایی دارند، افزایش قیمت‌ها باعث بالا رفتن هزینه‌های تولید و کاهش قدرت خرید مردم شده است. این وضعیت، در برخی موارد، منجر به تضعیف ارزهای ملی و افزایش کسری تراز تجاری شده است.
در حال حاضر، کشورهایی که قادر به تامین انرژی خود نیستند، بیش از همه آسیب می‌بینند. برای مثال، اندونزی به دلیل بازار داخلی کوچک و وابستگی شدید به واردات انرژی، با چالش‌های مالی فزاینده‌ای روبرو است. افزایش یارانه‌ها ممکن است باعث تاخیر در تثبیت مالی شود و کسری بودجه اندونزی در سال ۲۰۲۶ می‌تواند از آستانه ۳ درصدی تولید ناخالص داخلی فراتر رود — موضوعی که نگرانی سرمایه‌گذاران خارجی را برانگیخته است.
در این میان، کشورهایی که صادرکننده نفت هستند، مانند برزیل، قزاقستان و نیجریه، از افزایش قیمت‌ها سود می‌برند و ارزهای آن‌ها تقویت می‌شود. این تضاد روشن نشان می‌دهد که
بحران انرژی اکنون به بحران ارزی تبدیل شده است
— پدیده‌ای که اقتصادهای نوظهور آسیا را در موقعیت دشواری قرار داده است.
بلومبرگ</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16384" target="_blank">📅 10:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eadhRb5fhl18OUMRJHdUQRcg3sVczrhCz5p9UKW8v046Q8PNjTJer73AR8ZxkHtPYay6bSABX6xo_X7a9AcRuWcm9p-0DMBzCzfix8Fn-yTO2HPvkZXA54RXoVZNq547zKkgY_YMVHE4oiLSpeJnRz06j7rGtHsL53guRi5S1asAiBetdqt5Yx8tYIdJgT53YxzAGvc2rn9KJBwyF7mTSHd6pSigaZ636pBPzlVJ8jYsFIciKr4LTxC1sjSFHPQ7G0gzpWa2XoDnYNNkWVANa09DqdrJRG79hspfVMJxsYAtlQtBqLGXSyDJHYC-nJj9HqG6e8LfZ65cVOyN3KBB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCLh-iQbKBw7x0mFWv_64j4X8F6VZyQccvYjZelCXKICZqd-USkxOIqNnYk1jw6-46S9KQMJ-vxwQ7r6Zsc6lBDqoN5Jna2vGId1Rqc-kF4JMUhq_6IRpWDU7HyLeA4bnETVQ8qVwyxkc7bw9fuKv038KWBoWQfibsv5xZez8ake4lrxvp7ivch5gJ5_0YJburWQh_nLWq77JEv6_7Il_0LxH6mh8YFsjfWcj-md9TmkN8IJJswTQHA4y-mIJ2lQ6tNQa0HY7jn_XOuqC0Wak3EPGWKX4BeO5UcHLaBIcthLdwyjMnQpBcVX-xoEgrYAMdw_g-CebE88rQFCLLdG0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیروهای نظامی جمهوری اسلامی اواخر سال ۲۰۲۵ قراردادی برای خرید ۵۰۰ دستگاه پرتابگر موشکهای دوش پرتاب زمین به هوای  Verba (تصویر پایین) به همراه ۲۵۰۰ موشک مربوطه امضا کرده بودند که بخشی تحویل شد و بخشی در جریان حملات اسراییل به تاسیسات نیروی دریایی در انزلی از میان رفت.
همچنین سامانه مشابه میثاق ساخت داخل نیز در اختیار نیروهای مسلح ایران است.(تصویر بالا)</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16382" target="_blank">📅 09:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16381" target="_blank">📅 09:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehk4JRYzF0RvAr5B5ht23nwJ5Lqa98ilzPx6sdnOSFa0bdfTchSWwbvAVdSIfmQBzLVijEGjtOe_jHQMlG3i-0j8Geo_ImpA0Sebm0LkwQFB4CcTF6YCSPI9cytiNMIdaV7OgBETkgKlraH00Ae7IYvBb_Hx_eQJEXxdEfGP6dTDQqqwfL8tHE4BHaO-uLxnJ3QmrGAnCMdRqEBmAOYxU3piL-o569H20CfYSjCl8eKfD5zHtZqSHpC4Usnvwkk3SPYCoAECX3EYccrp0164ZzqS_UKOR7hZwRC3gMGoe4WPdxcu26SI232AQqIscKeCfntQqrusZSDykWPTy6Jejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16380" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzL0_Pl0iBTPno-lBOcpBh5cTE0uUhGTiKEv5mXQtXbWUswjsltdyrQH52UrghRI8KqYJc0I6vtM7P8fp9KBAa1oQMFBPRvoAzZj1e054XSeGfh49jhXlF0RG5aT0JlKMe1CNnBZiIhP5FGeyEKTJ8dev0SDMGOrleHo-nfo8DFjDyFbisPZAvCvibW-5r8TE9iO0fRLvmuop91TR0Eunl9vAbW-IteusIlq7f1AIhd2mP7VHGppVnqqkUplj8HcXMBEyDqcaOktUI1dyKVPZ240n9YUSt4xUhbNFY_0WqJ_B8hSV1xfpdaCNahNZVylZZc9GwQddTaC_IA57ZS3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16379" target="_blank">📅 08:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=BVeI_sWUIrecQcPdmSr46GNqybj7RMIN6Wo6E0Vt8OTfAC-ZzAk4Rf6HspCRkAYWY7V98KS7_Dg4tkV9NCJZR94XjEm_YZnQLmmBL58GfrVkuSzx84xcYR4vWGyavOzBAyaxFxrnPl8zFI79DGWTJMsL3enIAdpbAiQF2meGFz2Qfs3EFwHhG8xX7imixXL1ykwkSeQdptlg7007qvlpsOyq38WBwZ7xpcMiqR-y2ipFxnt5MfM_1p-xh3MzD1rBneLNwHOpYdR5Ad4hJTpVXpH1kNu9p-6_c8UCBSSx4in0KtCuMkSLaSPQgyqwhANDn4tj94HuidHOmtSSHGODsFKij1S8TeFF-UuGp1KXhWxZdnh69VHbmAcZnEwIY2jGDuo19SidhvkzUT6VsYfNe234fMI9H9FXUrwppWJ3HDjE39JeJmhNB1mFMibgLjwao3AkgAuaoadrvC1Ee0c24zMcTz4f1pCKzyg-7c8XYRrgnzFDc_AHyriuHU04ZAnaXSJstmNcJayd6JZapO8GRhd4-OLk5rxI_-A07v6EQKdhJjFapx_VkariPgDgYS75MLVn6UVRc2QXYtGeZQKOPUb7NB7iHhvaj4GCQfHAWLS9rS6hlY4gM_kNgIyKctXFno63GU6jcEGqOvnh1fOlX-E7ALtoxcVQI9U1btjhEYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=BVeI_sWUIrecQcPdmSr46GNqybj7RMIN6Wo6E0Vt8OTfAC-ZzAk4Rf6HspCRkAYWY7V98KS7_Dg4tkV9NCJZR94XjEm_YZnQLmmBL58GfrVkuSzx84xcYR4vWGyavOzBAyaxFxrnPl8zFI79DGWTJMsL3enIAdpbAiQF2meGFz2Qfs3EFwHhG8xX7imixXL1ykwkSeQdptlg7007qvlpsOyq38WBwZ7xpcMiqR-y2ipFxnt5MfM_1p-xh3MzD1rBneLNwHOpYdR5Ad4hJTpVXpH1kNu9p-6_c8UCBSSx4in0KtCuMkSLaSPQgyqwhANDn4tj94HuidHOmtSSHGODsFKij1S8TeFF-UuGp1KXhWxZdnh69VHbmAcZnEwIY2jGDuo19SidhvkzUT6VsYfNe234fMI9H9FXUrwppWJ3HDjE39JeJmhNB1mFMibgLjwao3AkgAuaoadrvC1Ee0c24zMcTz4f1pCKzyg-7c8XYRrgnzFDc_AHyriuHU04ZAnaXSJstmNcJayd6JZapO8GRhd4-OLk5rxI_-A07v6EQKdhJjFapx_VkariPgDgYS75MLVn6UVRc2QXYtGeZQKOPUb7NB7iHhvaj4GCQfHAWLS9rS6hlY4gM_kNgIyKctXFno63GU6jcEGqOvnh1fOlX-E7ALtoxcVQI9U1btjhEYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این هندی ها همه چیزشان کمدی درام است؛  مقامات هندی در حال بررسی طرحی برای رهاسازی مارهای سمی و تمساح‌ها در نواحی رودخانه‌ای مرز با بنگلادش به منظور جلوگیری از نفوذ و فعالیت‌های مجرمانه هستند</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16378" target="_blank">📅 08:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">معاون وزیر خارجه روسیه دقایقی پیش از قریب‌الوقوع بودن حمله آمریکا و اسرائیل به ایران خبر داد.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16377" target="_blank">📅 02:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16376" target="_blank">📅 00:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده است</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16375" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzZWX2y9tE_CsUwII9b949T-JXjgXCh_3KIL-t3uUBwworc4XUjzJfF9qBsIb0LDxJ8PGXR7ZSQxHVMpj3A32sMGqnMoeYZSkPWRqM6pZIItWIqA9Nfb2dMFJp9KFMzpMjOQquEt3WYc0Ol_h8nG__A0TwxQHP6n2OWhCiY7NyK4jctK1DOpivmnA6ygeKq8iKzkRR-_Vycbqk3c3a2ljA9qEqmFCzwwkFe8D5-xqV9k0AWme9dav_NfbPnMzumUcIwkqEuagTzJr12XCE0j1kdLVRjgqpYrv0vX3V9HlJpUkgGRwO3MNjwayCMi4B1VfTdIDBB90dyoaOdOQd9ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مرغ طوفانم نیندیشم ز طوفان | موجم نه آن موجی که از دریا گریزد</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16374" target="_blank">📅 00:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16373" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16372" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhiXM4bV3CnVDIJLPjiMf6xGtG4RKEFubUEYVWz_wZym9EKZ3Oq3gSwSFP7_XQalehZY2Qb3L-9XYQ61Q5VV0Hb7iGbq2Z2qu2uC8641hrotJE_PX6pnSxdRypGKRRv-8JDqk53qbIV-RmwZkZW-TIUK1RCwYIaN2e4AuQRWRxOluVQ-C-NUORzogk5xKy5KsR3_sSSI1XEK4UlJ4hg-ocs7FnNFnv_gPxhtdBzrClLUwi4nl-3pUeH1OfUvlA_o7LBGOA8kCcfGn_Z_YeU5g-r1rQBZMCn5MxM1XbcDjWUxT_SpvSpfU7xh2Tx9OLmR6nhHqSp6gQYkvuFad1o-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کله زرد ول کن این هوش مصنوعی کذایی نیست.  چه گناهی کرده ایم که این ور با هوش مصنوعی هر شب فرعون و ناوهای آنها را غرق می کنند و آن ور هم آنها قایقهای کوچک مان را اینطوری پرپر می کنند.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16371" target="_blank">📅 23:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭕️
تاثیرات اختلال سوپراپلیکیشن "شاد" و اخلال در بستر دیجیتال آموزش کشور</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16370" target="_blank">📅 22:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDOwm7MC0nxE4-KcIoiWoyZBe47l_EtrNVk9aklBtmUWl6hu-c2u8SERWqgC1I9D4FMc5qAFl4sKrK7HE4ISocm1hvBP1aKAkTQa6KELpzhqhVgn8Vk7u0G7xP-Xc045jV5HjPj-ZB5tR1p77q1R_XfE9gvINmmHLAXBIecFCYQjMCupUEkKvU_gDYZ4KY63tbALDGpfyGGm5pJsxQklay8wWVev0dZQ552GyZBlXD_viTD-Kqs-QXA1tImatKpcwH1fvUqkaO6oectl-_Y3GDwnXP_TSsTcqORq1b86_IEy428NJ4y_kiZI1cFDT6W1KEg4AmNfDHLWBpnRa9dtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر داگلاس مک گرگور از میلیتاری نویس های برجسته X دال بر نزدیک بودن دور بعدی جنگ</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16369" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بازگشایی بازار سهام از روز سه‌شنبه
‌
معاون نظارت بر بورس‌ها و ناشران سازمان بورس و اوراق بهادار:
برنامه‌ریزی لازم برای آغاز معاملات سهام و ابزارهای مربوط به آن از روز سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵ انجام شده است.
‌
بر اساس هماهنگی‌های صورت‌گرفته و پس از اخذ مجوزهای لازم، مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16368" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور:
دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16367" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام
:
دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .
پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات، حفاظت بهتری نسبت به اروپایی‌هایی دریافت می‌کنیم که ۵۰٪ مالیات می‌دهند.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16366" target="_blank">📅 21:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حالا امارات را مسخره کنید اما اساسا یکی از مشوق های اسراییل برای پیوستن کشورها به یک پیمان راهبردی با تل آویو «تصرف خاک» است.  نمونه اش پیمان با باکو که منجر به تصرف قراباغ شد و از دید اماراتی ها، وضعیت جزایر سه گانه برای آنها معادل وضعیت قراباغ برای باکویی…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16365" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16364" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa_Qr_dRjP1ztBk-b5AHFyrb9aIoVEjwWh_W4QW_d9-uhJtxRtA9lPuO6ObxYbQqvLZHWeSUF3j4iq9wLHG7VOKJapg77iSPx63pp0E_5QpWHRVzZT6NEPVu3IyNBWWUSfbvv0uxi7o2Yt2cMZnH_dr6CEdm8LWkgd2-oKR5xNzmuWoaSAAiie_znS7Cun7kts2MYgknXdKC3VeAyYZ-Y5qaibtLjoLmZ9HnI0EOeenrM8vlNd8a_zWHZo3ayHri1Y2eyFn1_1ec8rLNDQk7F6Xj6TpDB7A5gWTOwMq3SurcvdsPKHlK38HL_qSbLWk74DT5Q1V45g8pjLpy75K8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد از تعمیر سوپراپلیکیشن "بله" ، سوپراپلیکیشن "شاد" دچار اختلال شدید شده است</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16363" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16362" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16361" target="_blank">📅 15:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4nwg-qv15ZhH4O1Ys4KEjTkmM7K-VbtlwZi_qTCMZHEv2Ld8mRkGRo17-yveNXrRegY77KadFCDjA65GDRCGvn4ZCXRKxFm08dx0_fJd6taFYNJZCN1EzGetS0G6dm6BBQAmyjjGUk0bgRqmKJ_e9bBrQLst9WMTvLqU3zR6j7_Ae-KkJ9IdYPVhYoGsqI2mz84FYjT9sAhb9w-KDdMi3lZVApdsAtBzXyYKySvBxKzwDa8crw2Go5xvahZ16HBjx35FE4vwxw3rvXybgnRbJ7hIQH6gtkKJQcNR2CLbE05sgOIPk4XrougOs6m9Ha6qTw5c1uCmA9Yb8EW8sn_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحولات رفتار بانک‌های مرکزی درباره طلا
بانک‌های مرکزی در سال ۲۰۲۶ رویکردهای متفاوتی نسبت به طلا اتخاذ کرده‌اند؛ برخی مانند ترکیه فروش را افزایش داده و برخی دیگر همچنان خریدار هستند.
ادامه خرید طلا توسط کشورهایی مانند چین و لهستان نشان می‌دهد طلا همچنان جایگاه مهمی در تنوع‌بخشی ذخایر و مدیریت ریسک بانک‌های مرکزی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16360" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16359" target="_blank">📅 13:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxh8vxpYr0dlZgCBnkzrgv2ogRDMeXbVVIk_DXRb3NZJIKGGPF3qOpawcjbEtWmFNyC3-nLTatFm0gSaT-w-Xe5C6ifo-0-vwpkSuLFa_Uu35IpeKegFKtoRQe7mODEoFM4QqD-bCg5E1fC-isKHKOEWTb222A6qNVmXLptB45ZVrduw8_Sr5C-JtCO7L3APsB5-cv52WkhcTrz3f8OhsJp9J0rzVF95fs-ZWqVUIalglIsJ7neTp9dOQHyoKXOnUw_Xx7HzaRf572paQmvVzFICJ68a6__g1_ytRqu9A2NhE8a45yAbvHYMeyGPvT3nI1bmk_UtE02uDP7aJ-E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان تاپ کاور  یا تأمین امنیت هوایی را بر عهده داشتند و دو فروند دیگر مأمور اجرای عملیات بمباران بودند. جنگنده‌های بمب‌افکن موفق شدند مأموریت خود را به‌طور کامل انجام داده و اهداف تعیین‌شده را مورد اصابت قرار دهند.
◆ در جریان بازگشت، در منطقه مرزی ایران و عراق، جنگنده‌های اف 16 و سوپر هورنت  با هواپیماهای ایرانی درگیر شدند. هویت دقیق جنگنده‌های فالکون مشخص نشد و احتمال تعلق آن‌ها به نیروهای آمریکایی یا اسرائیلی مطرح بود. در این درگیری، دو فروند از جنگنده‌های ایرانی مورد اصابت قرار گرفتند، اما هیچ‌یک سرنگون نشدند و هر چهار فروند موفق شدند به پایگاه خود بازگردند.
◆ همزمان،تامکت های نیروی هوایی ایران نیز به حالت اسکرامبل درآمدند و برای پشتیبانی و مقابله احتمالی به پرواز درآمدند، اما در ادامه درگیری هوایی مستقیمی رخ نداد. با این حال، پایگاه مادر این عملیات بعداً هدف حمله قرار گرفت و از آن زمان تاکنون از وضعیت عملیاتی خارج شده است.
◆ با وجود خسارات واردشده، این عملیات از نظر نظامی و تحقق اهداف تعیین‌شده، عملیاتی موفق ارزیابی شد . خلبانان اعزامی با توجه به گشت دائمی هواپیما های آواکس و جنگنده ها بر فراز آسمان عراق،کار بسیار بزرگی انجام دادند .
به خلبانان اطلاع داده شده بود که به احتمال 70 درصد ،هواپیمای انها مورد اصابت قرار خواهد گرفت،اما همگی با شجاعت مثال زدنی راهی آسمان اربیل شدند .
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16358" target="_blank">📅 13:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=M3N4g7MHaRqAEnpoCAytqWr0XKgmSeRdzA9viyfz5y7MPzqvvunCo6HLsWCZi_eFHfE057A3hzuftm3nvqo8c6_yrd4tIfBithn5KRebQPLCpGGhzZUYdhkc2jVvLZWRdVpLfrao5Y_BjsXTtTz6RVyC9L_XgDw3Xdw_kvgOfyNiLgwII4w8rKqwKhWro8GCayMXKZdJfYbAbX6pbiHftn9fjaHKbL3EP3vHdUaa0rkHVP0mINcfe3ibod9Ct_O_WKpOEfESeKyTrS3rzhwE75Q-hpnwpY6HvikT-51DP5VzxZweNOZTsWK5jVIQNMnaDdbJl25nZMkRuatbXikBVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=M3N4g7MHaRqAEnpoCAytqWr0XKgmSeRdzA9viyfz5y7MPzqvvunCo6HLsWCZi_eFHfE057A3hzuftm3nvqo8c6_yrd4tIfBithn5KRebQPLCpGGhzZUYdhkc2jVvLZWRdVpLfrao5Y_BjsXTtTz6RVyC9L_XgDw3Xdw_kvgOfyNiLgwII4w8rKqwKhWro8GCayMXKZdJfYbAbX6pbiHftn9fjaHKbL3EP3vHdUaa0rkHVP0mINcfe3ibod9Ct_O_WKpOEfESeKyTrS3rzhwE75Q-hpnwpY6HvikT-51DP5VzxZweNOZTsWK5jVIQNMnaDdbJl25nZMkRuatbXikBVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اعلام_وضعیت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16357" target="_blank">📅 12:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JBFXkEWa3mrwlVaJ2LLfyfCHOsMANXsfWk7EsYuQXw4T0s1dPb0NQ0knI33DtenaikTT7pQ6PjuulOe_a_GGXIfRdUkUlbQimf9MnNJ3ZYtAbYS8a59TDnfrnJvlu6D8WTeV72S0Q8O7oQRPp1-qHkowxhxTypveS41uevybuMQhoLkRFPLa6M6m6D8tGuT_bTBsue9fRBOsB8L33Lg0mHDB8ksN_DPaZIJb0EDQiJFlb817In7rlqIV9ShYuE6xdTsRPKZuEfGcER_mS4kITwBocUa-ga0nLMk1UskqM2Ravuj2L0JZDVuePp6R-mgp3oYExp_hEX0Nic1QWyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16356" target="_blank">📅 12:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16355" target="_blank">📅 12:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به نظر می‌رسد ایشان از خوانندگان Secret Box باشند.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16354" target="_blank">📅 12:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=oZrchDIX2cmrsp90Vcwh4Eyw63BcRWsLUCVylRz2fT5mCHDoP3ghpJv-zI_a-eCIp3oYjU0gBXGhNaTKJlGOJxPGg6bhMixUDKSwO_hlYOnq1dDEmjKsDEYkiroc8ThX6lffDPXrghlN6zL_c2kWjdk1FpjVB-xEbFY_zWsI3iwkj-_lTpDp8f7gcEGdWIvfDDfunURhefDGwdgmfqZQE2buga2dJX_zIQXa1OSQPWEH4v3ntIqB9NPTjKWENe0Z58GNnV7rJqDJLR2EQjkW-afhIyQbg5-ZxZh9LqFNlaxqqNriX7pvkDHbRCAEZpTNjQXChf3AWCiZCCsGE9S0-ZUChJe3AYJpvKaRaWUYJuk8FsF-9z7wRN5UXWkB_Msir206KzdGMAFye4ThWJxvsEL4lIuGf9BAxUgTymhOBEGWtoKcHzxjP5a_8oEvJclncIhZLRobm8ALmTffLntk49ae_DXEPqdl2Yxrz-uxRDPu6UVhiZZOmeDjp0rozy1y_ARIGoYHl7jKZusghJPNNn5Wu-i8Y3SNcRDFGydLdtnt3iGpPj6vxZf994SQoVGbQbxJVWadkvOP9ZVUdWOxhZNsAvD-7QHHxgF62-d_h8_OrI0ohxDlFlz1hXBhhGojJhBh48RdjW-Bn2Hd3j8kku1Bl2vKM1C2I2X1nMdio4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=oZrchDIX2cmrsp90Vcwh4Eyw63BcRWsLUCVylRz2fT5mCHDoP3ghpJv-zI_a-eCIp3oYjU0gBXGhNaTKJlGOJxPGg6bhMixUDKSwO_hlYOnq1dDEmjKsDEYkiroc8ThX6lffDPXrghlN6zL_c2kWjdk1FpjVB-xEbFY_zWsI3iwkj-_lTpDp8f7gcEGdWIvfDDfunURhefDGwdgmfqZQE2buga2dJX_zIQXa1OSQPWEH4v3ntIqB9NPTjKWENe0Z58GNnV7rJqDJLR2EQjkW-afhIyQbg5-ZxZh9LqFNlaxqqNriX7pvkDHbRCAEZpTNjQXChf3AWCiZCCsGE9S0-ZUChJe3AYJpvKaRaWUYJuk8FsF-9z7wRN5UXWkB_Msir206KzdGMAFye4ThWJxvsEL4lIuGf9BAxUgTymhOBEGWtoKcHzxjP5a_8oEvJclncIhZLRobm8ALmTffLntk49ae_DXEPqdl2Yxrz-uxRDPu6UVhiZZOmeDjp0rozy1y_ARIGoYHl7jKZusghJPNNn5Wu-i8Y3SNcRDFGydLdtnt3iGpPj6vxZf994SQoVGbQbxJVWadkvOP9ZVUdWOxhZNsAvD-7QHHxgF62-d_h8_OrI0ohxDlFlz1hXBhhGojJhBh48RdjW-Bn2Hd3j8kku1Bl2vKM1C2I2X1nMdio4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها مواردی است که اسراییل را به سمت یک راهکار نهایی پایدار منطقه ای بوم پایه  — بجای آویزان شدن از غرب (و خصوصا آمریکا) — می برد و کریدور داوود و پیمان موسوم به کوروش و … در چنین بستری معنا می یابد.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16353" target="_blank">📅 12:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16352" target="_blank">📅 10:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استوری مشاور محمدباقر قالیباف</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16351" target="_blank">📅 10:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR6k0LKaoUiK4uKNFUNv35WhB8wQms9DGTa4WND53fTnuS_lgyedDhiRu2idr4s795JJOU_ze7-FFBgRov1lBZAx9x-8wyGezJ91QE1n5QAFDxAbCxeUOK5S1hNCLnnXFjWc26DOVAcledCkBhFN-hRmZFv1x_-9ibUReEI8vqScDq0SuDIxasSdZxaBQsgTmjyvzTxmJSgG23Zc_QQitho53bG9BdlcboouS7gME9UKWw5ZcRxY0hS_kc-1NiNwmLSWl8j-o3lSH8PUFIhI3gKcQ8MpwJr8HBPVQhe9_vXaC4Tt9xKhv2gMhcd1lIEemCyfe6-1vZsAYw4M6-w4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16350" target="_blank">📅 10:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpGpz5FcTjVlXx7bsaC4pOZcRWuAHjnDJjpXtq8lWRHHLpGkZqEfUkH6QzNw8-TlCh4iRYEH3umJVqrZj9gzsU_ieNnLFtQOqZwI-VS64bijZ35Aji-nEQhz0rrlZpsEbp07lJY0Pjc8q-Vd-6iE_V5v2Du4yJ-_dNq3VLIREm9bRM3oK6vwcVy8mWJMZfDacU1ydjNaEdGPj2iy--p6nOf4tPQ_gUNUiaOFzYWCj-Vp-GS67EltXOIGSK5c9GpRkA3tMnNgwRDvLd1oQqO8rFls9KLZaY9lLA0K6u8bgprN_kkh6-tjNOmKEvn6vRiFthjJErnXBfhOL3l8R-SjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16349" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16348" target="_blank">📅 08:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=CMrciAQPmXR1iv6oOBwAYKE96XJwetUXileY2QZSSYwPrXZYr1WV8c1huyLQTHDpSkbq3skGMBVhaEk6gxDTHVDUuQvx5XyRiyDGXIzJ4lLfTvaT2_n96bFR0XKU7Lh070kEO7BP8pLYxzrFuPD9V8U4M6fDoTKurhtg9Ujt9__8lHQmaip4mxh80ZwIGNShF5bkh-uQmCNpeOC7dzxifrIbFi0vNlMd1v3CderlFaOW4ZQzNtBWHMtRVkbl1b92YBREIv1i46RL8-ILTF1pZGYZRM11dGOEhp6YLHjK4EncA3b8SnK_LaF3fUKeWjKJSvEbUSUb6inTA-66Szjw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=CMrciAQPmXR1iv6oOBwAYKE96XJwetUXileY2QZSSYwPrXZYr1WV8c1huyLQTHDpSkbq3skGMBVhaEk6gxDTHVDUuQvx5XyRiyDGXIzJ4lLfTvaT2_n96bFR0XKU7Lh070kEO7BP8pLYxzrFuPD9V8U4M6fDoTKurhtg9Ujt9__8lHQmaip4mxh80ZwIGNShF5bkh-uQmCNpeOC7dzxifrIbFi0vNlMd1v3CderlFaOW4ZQzNtBWHMtRVkbl1b92YBREIv1i46RL8-ILTF1pZGYZRM11dGOEhp6YLHjK4EncA3b8SnK_LaF3fUKeWjKJSvEbUSUb6inTA-66Szjw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره سازی اورانیوم غنی سازی شده بشوند، شدیداً به آنها ضربه خواهیم زد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16347" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر ایران دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16346" target="_blank">📅 07:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8OBfzBLGPha-WfG54X81cV6gBR2F5hFxKGGSAysus5MQNtn6UU65oNAubrusl49S8cUVHo2_otjSUaAnDrQjN3BgRjyA48ntqnFrNiulEVw3j38mB2OSk80UpxOzWZL0r0bxEXKx75rpS5ONIyTeixzUsEZsDfIQgL6q1a4Z1PcKQt1d2dObyLJgMzKkQUYV5JTHSKtWBfGglCTnqMgg9zQ5AV6rf5k2ImG5MMNs4hJq-xnEEsy_JzqXoTv4BOGZ5wyvfBl9O0zP1c1F-ILuZpUpMgm_coK9JYBwnTC0wAem09MbYdC5yH7qojrsvhgorMLIoK74zLSbenvsN2EMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16345" target="_blank">📅 02:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16344" target="_blank">📅 02:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV6jobeg_nKexRG0ISF02GqwmtKoGXDc7aFivJMBPxX32evxV8v9btTEawuivyXdHuUNkgurmL9HViTl9mix3UvmXLxfsegAMaY4wUXXJ1p6PaxJ6GxSfH9ZGD-mmOF100LSYfpMGf1z4baM77xqdewRsVDI3QER--P4ouAJa_0aJDL7IXPC5YAY5ce7Vq8zLVRrD0PKK9MQOnwVgIp_2qpBhqmHA0_RflVEO80fK6maONgVBqWvaIhGk8A8fk1w_fMZyA3gPHH9tJ0NgULVf6guFaGz2UPOV5hEtB1wBB1igCf1WIXGiw517P5OgqO18fdxh2gZ0ou7wdeTmAGvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16343" target="_blank">📅 00:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حس میکنم دوباره سوی شیر گرسنه دارد گاو می آید که ولی خب.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16342" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16341" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16340" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ مخالفت خود را با اعلام رسمی استقلال تایوان ابراز کرد
من دنبال این نیستم که کسی مستقل شود می‌خواهم آنها آرام شوند. می‌خواهم چین آرام شود.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16339" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Adi1wdzpJLJOBjt5pUcb8jGjSJc3LrTX3eEVEZjgV4Sx6w4llhcHzEl8MhPJc3eSPJhrUBClvkVzeMXoGEgCRoB3JTn5cfgHPP2Yoc78_ZQyHMw81Zzr_nL36HJjsmnDCxxvt6Ii47ZG52G6Kgag5Tbkl79RTMyVzyoAt6BwGyBdixak2R-pv7yGDig5A0q7NtE_LZg81KzUrIzliEs88WKjWvkTYSpdbn7RJoewHLD5LMDH-I7koiCm1HnNnWdvOCmU3sV5lCocWKGfrhLwkalICAITxrkpSAD836VyE9lHUzALwVSh6vp9mYRDjWFdQdcPu6g1lgBZ-uykmZAM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16336" target="_blank">📅 21:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو:
عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16335" target="_blank">📅 20:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ولی خداوکیلی راست می‌گوید ، هر چه آدم توخالی بیسواد عقده ای که با قر و فر جلوی دوربین توانسته نقابی فریبنده برای خودش بسازد، در اینستا لانه کرده.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16334" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:  اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16333" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ای ایلان، ای مرد پرگهر !
ای ایکس ت سرچشمه هنر!</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16332" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:
اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16331" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16330" target="_blank">📅 19:34 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
