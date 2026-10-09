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
<img src="https://cdn4.telesco.pe/file/akACXgWgq8TrOfKTGn-Ja7LZj12HrceEVcomPGCNpytXJ1UUN-32DA2txMwU87sakSXA6yWue0CsxfDcGzj5m_vt0JIhsSn-lwqS92Wu2zZSakZFvZ-PqS_YNkwZxsGh0iVKtwqzbny_tBIWzCyd5L8_oYKwq6v-CfgJHl4Rpllmk1aOmNO57FB3q-zfELqO6-KSIBhOXO8TtwvKCjsJ6UZGlG0CvJeFfQarrcZj-76QD-Iht5oBVifR4t603YnbVuAII7uDBt2EG_K-S5rQ_6raxM1XFmksCwfBVuejsEQzK_0nPPFXmBC_zi2R4eOezqbt6DEJvDTbfcja3SOPjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBx153U7zdyIGDXvalf892AYrqUe-OuzXBpInG66sAEK2034ZHSWZ18uvYwfwpNoiZXVyxKi2WgOCj2B9z3O812rfZtP53HZFG6XwXlJqoYQxpcBBqJTIleklGbbJNGC99iW24In7EkuBAwcrwPatXZyWzn6P65gCNb5tLMx86kiIFB5UkXh71CoAbphraRe-Ls5I0N-Tx2j502keKGRPpDXOI4x4MAh9vAs3QvV2-bvmO6F-87fGYPHs9kkShTlb6ioaWXTjKf-duO0VQJNGC-suecVd56Ehzvxggih11GZ6G8zgwXZlxt_Fr2PmKUmyYd1aig1A-6HKHvhrCToaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=VXpnp_Va_PnP53tMWdvuHTfSxCJVeXs4OywKbQTRW1RKJoyit2Pdj3a_0OWwfnDIQfFthJomkh_gRGpxXqUCIV9WvfNPvuWIkoV8nrkLJVcVXaoVgJnkuKfmtpK_kVPV2_L8XKg0q2-ovvxx8vSLo-dFv8XiwLPVKg_oAgQQAdzNtjYKOvSOtzYYFiuGXmvVZRrp7bnlGbB302gEOAbd9L2iUm1uBllKX3lk-9Ar49TC3qQDh1LxO28zN6RytT-ohxIDMNsGAH5Et3TLLLnRw6THkTx94FUeHHx2xveVoBve3N6kXj4PfJNrTNwIgt-cjLq3HcWGP9DCNcwUMAR9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=VXpnp_Va_PnP53tMWdvuHTfSxCJVeXs4OywKbQTRW1RKJoyit2Pdj3a_0OWwfnDIQfFthJomkh_gRGpxXqUCIV9WvfNPvuWIkoV8nrkLJVcVXaoVgJnkuKfmtpK_kVPV2_L8XKg0q2-ovvxx8vSLo-dFv8XiwLPVKg_oAgQQAdzNtjYKOvSOtzYYFiuGXmvVZRrp7bnlGbB302gEOAbd9L2iUm1uBllKX3lk-9Ar49TC3qQDh1LxO28zN6RytT-ohxIDMNsGAH5Et3TLLLnRw6THkTx94FUeHHx2xveVoBve3N6kXj4PfJNrTNwIgt-cjLq3HcWGP9DCNcwUMAR9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=KuOjf-eYzaoGMpeAanVUgcxUshKmGiEAQ_C2C0fEgk80JDmBHv7OL4UzA25w7768DBNwNzRc5gPVy2_PQr5dbBKtf03p3A2Hg16za8WOkOo32S0gcF9P787JP51JfM_8fhh0DxFtS1XahpYnCtV6CJQkY4DGvGAC-9vuZgpDbGGMFLgO1WG7r1hSLpY2IVpn2FKOpbEkiPy1mHEBuaK6Vnnz7dr4USp1Gt6RhNfYBP-95jZ_svZgk65cR294nbJoO21IFLo4fGaR6p-OPm99-4E1OTww-MBnlWTWYDx6Sy808_hBo1wDM45Hwj40nGPJf_bEcZFpXBJl6oYHPGee3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=KuOjf-eYzaoGMpeAanVUgcxUshKmGiEAQ_C2C0fEgk80JDmBHv7OL4UzA25w7768DBNwNzRc5gPVy2_PQr5dbBKtf03p3A2Hg16za8WOkOo32S0gcF9P787JP51JfM_8fhh0DxFtS1XahpYnCtV6CJQkY4DGvGAC-9vuZgpDbGGMFLgO1WG7r1hSLpY2IVpn2FKOpbEkiPy1mHEBuaK6Vnnz7dr4USp1Gt6RhNfYBP-95jZ_svZgk65cR294nbJoO21IFLo4fGaR6p-OPm99-4E1OTww-MBnlWTWYDx6Sy808_hBo1wDM45Hwj40nGPJf_bEcZFpXBJl6oYHPGee3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=JucZ9Jqk-VsJU5gtW8BRcRT4f2vIeIu-WFzayYC4MftKKLdJFqjxAHJk7eNjmoXspC_-WrmkpCVEGu7xkLfHsICblsroplgr1ZVhFwV7ts08np5eYCEPW-8Jgo9rSjZQpdr6AbdTgv_MwzerZXlQHnT1EL0rvUXUdAzXQXTQJbhy-F2y-GkoG2r9o_508kPVltGyI2nYOBAVJnCzt8W2e0H6_9r7-snNvOCjGgs4aW2lUJTT7inayav_1fiqGL0zzVCA40Q3_g-BcTc3SYk8R-lkrVZiznHh03WSzNqtUAuMHxvBUMTVWXxjQ520nZbtLEKS-Xq5NwLvk9nX6wkqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=JucZ9Jqk-VsJU5gtW8BRcRT4f2vIeIu-WFzayYC4MftKKLdJFqjxAHJk7eNjmoXspC_-WrmkpCVEGu7xkLfHsICblsroplgr1ZVhFwV7ts08np5eYCEPW-8Jgo9rSjZQpdr6AbdTgv_MwzerZXlQHnT1EL0rvUXUdAzXQXTQJbhy-F2y-GkoG2r9o_508kPVltGyI2nYOBAVJnCzt8W2e0H6_9r7-snNvOCjGgs4aW2lUJTT7inayav_1fiqGL0zzVCA40Q3_g-BcTc3SYk8R-lkrVZiznHh03WSzNqtUAuMHxvBUMTVWXxjQ520nZbtLEKS-Xq5NwLvk9nX6wkqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=ZbLxWo5Fyo46P4jJEnZG1cmPzo0q1Gw_-j-XLPy5MygOa3FVIFX3MsmCWvkh7f3B7NX81XllEUAtrLkKHs-4kUjTtS74rNAcK9dlBRVQC1z7dzzSdcOh7mBSlz-NnnMcjeT01a9ARy4HA1cVQh3zgcbVLf72n-4xbstzlvLJ7FS578lNOHjfv-Rze1EhPx2h8n44555HQVxQf0yfnQbyuLuhl0HHexNRDPcPW6DjaB-3qDwtjCxsx6t4UL5ulZz3kK-exbcsskkOT53fuz1Vxuw8UFhY2QpCXFt63wEZmcE1E0231MSDeKnNDPApIFDQs4fLoh7h6MBbacyXaVHH2Z-6Gs0Z7vD9c5blI0JLkc4k4zeGBjTfjA6V0pyMK-WSNeD6uXudQpEDJMc6u6kgNeAGLud4dbF3HODV-2wONZis-ti4Hrzxd181ANOxPYISCWra9qJQU9z23yjou1YwNJov-5rlm7nkhLglwxxTtzqgon7BHnN_k3-vSJd2SrRraiqA-YH_f4Xh90Rr7Pm41VCeml0OIji5d0jur9vtGZmX7bT5pE2vXoJ5nZx2IT__lULXtv7Pej1y922_THgJ71wOultl8QwBhrgLMJCWPHbqBBm2-QXzDfxhaEaNHqIvGJ-KNS6zGHV9fTBhPlpP_2n0goMBuq5MR-p0Bs1uKL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=ZbLxWo5Fyo46P4jJEnZG1cmPzo0q1Gw_-j-XLPy5MygOa3FVIFX3MsmCWvkh7f3B7NX81XllEUAtrLkKHs-4kUjTtS74rNAcK9dlBRVQC1z7dzzSdcOh7mBSlz-NnnMcjeT01a9ARy4HA1cVQh3zgcbVLf72n-4xbstzlvLJ7FS578lNOHjfv-Rze1EhPx2h8n44555HQVxQf0yfnQbyuLuhl0HHexNRDPcPW6DjaB-3qDwtjCxsx6t4UL5ulZz3kK-exbcsskkOT53fuz1Vxuw8UFhY2QpCXFt63wEZmcE1E0231MSDeKnNDPApIFDQs4fLoh7h6MBbacyXaVHH2Z-6Gs0Z7vD9c5blI0JLkc4k4zeGBjTfjA6V0pyMK-WSNeD6uXudQpEDJMc6u6kgNeAGLud4dbF3HODV-2wONZis-ti4Hrzxd181ANOxPYISCWra9qJQU9z23yjou1YwNJov-5rlm7nkhLglwxxTtzqgon7BHnN_k3-vSJd2SrRraiqA-YH_f4Xh90Rr7Pm41VCeml0OIji5d0jur9vtGZmX7bT5pE2vXoJ5nZx2IT__lULXtv7Pej1y922_THgJ71wOultl8QwBhrgLMJCWPHbqBBm2-QXzDfxhaEaNHqIvGJ-KNS6zGHV9fTBhPlpP_2n0goMBuq5MR-p0Bs1uKL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=qq20IWlTPKrbCuncMHzsmQhmvW_vFaY25uZuQYprY0gaaP1cr6_guyaeElwq5yYBep5bLTvHu7eNZGy8fFan_hV_ByocTpVjiLeSVHe1pNoaDzRzDhfvlyQF1LaQDeue3CtD9FhOjpc6N7qeSxndFalpfbKqCacaEbW7-A7h-WiAp0htV0Q9Wb1mClOgLQhn-rjp4WXsn7WqgnZNIZ5ds0aasuvj3EoXV2bo7IFgeLUvEjzmh4HzyB51i4nVxWsj6BosL0RO4cTPV-BRKphKGmEDEzVtioWk6qkolB7h2NGXfHs5MQiDhPEqb_kN3nK6exvMfg-bDE_y2qeo9UvMTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=qq20IWlTPKrbCuncMHzsmQhmvW_vFaY25uZuQYprY0gaaP1cr6_guyaeElwq5yYBep5bLTvHu7eNZGy8fFan_hV_ByocTpVjiLeSVHe1pNoaDzRzDhfvlyQF1LaQDeue3CtD9FhOjpc6N7qeSxndFalpfbKqCacaEbW7-A7h-WiAp0htV0Q9Wb1mClOgLQhn-rjp4WXsn7WqgnZNIZ5ds0aasuvj3EoXV2bo7IFgeLUvEjzmh4HzyB51i4nVxWsj6BosL0RO4cTPV-BRKphKGmEDEzVtioWk6qkolB7h2NGXfHs5MQiDhPEqb_kN3nK6exvMfg-bDE_y2qeo9UvMTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIqkSNtisBzGIaIVGgcHTmsc8ECaaRwK0KmbhE7uKkLrj0429bFimk7kD_3eFdY4xhX4CuNkHubUQGJLq98koy7MyNyuCYOJNH43XCRXit2G9_tkIS7alHGOxvecoF78mEJQh5My17sO2iB2mmf9vyArPLewLxgoHNQb1jmJCl8l74wlk7ELuUFc1mB_jGrIKHGfriDMir4gxhJFBGe8xN2zq_K7M0kNwNGiyf8OfTGGUvdcsxURJZYQL2wotPU9EkZlIRlQK4VLYN1fY8y1SZE9VVmSrx-SDd3-A3Wc4OXppunTN2EbEbc3Ri-Xi9ckbYkMHvxi5EX_8s8NPSa-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FafT5U9Ts6n5scDIYyo-UxbOs5gM057a5iogxaUixIto9jwsP5mwQgSq6lZi5tVi-QNaqmg-TIAvlGYWGh2JF2_017cZDTzeqoQ5H6HKTBBWbmOBSMLg3eINyu8np1xDWu490gqciRkYNkgypvucUasL2ZKxQ_lhMt8wndhrflrXFWqn2y4pxdGCQBDIJVeql9X-uT094_8JMC73LjsWTwlLKOq6ygo29qlrnmGq0sQ47qaKOfd-qHRPgKNBkEuoy82r5iE6ir6ErhWjo-C3J3JRyCZM6InmspZnqsfHuJ0UAeCoqJ5wIOAR8BNeghYNAxDKAIjPiT17HB5J-JsiZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWapV8zx45gJHJ6aBlFN4-gythig3R4DE6g1v-ZO5vDR4LSzzrJDYmMWz1mVLj2egAwhYa1SFQvsdvgz7Kq7az78FBf4Fvg5y0PooAeErZ4qdaYANc6mvTggQ7Jj_WNlHjueOB68hEWCFRva6CbQaiFX1OOh-hLAXPL3GGz3qBLiVpewnPpDcqfjwUhzCQQlEapUe85oY-bNgAer_5m1vjeQbfz9neuh233Bt5JqZKq_tyHBF98bsTtUm_wN3aIcTozpXUjfbLRPOreWCre46YKkvaOr6ehzrwmcEG1uAXmCocUbSHHG_-dfm9twlTUVscJ049eT0L68Eo_xtq61Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUtoE_qNZ60rSy4vIwfIzHNgKQ5oNsFIvgGraN9wHIYZ9NlUdtif5eSFtIth2OGHZbQBTKB_yOQmm-xVVPT_5rLPrpSrpeYjM6CQMsnQwAI1gxwqwDy-Kr3Ij1kQqHKta0ZmWf1YFFDVX4ZYC2Ixo5eLQpW4EPzIR6Clu-BMn8PoEj8DIq5EmbJCUgBwkOExP-_7hSF6FnAi7oTyWXPtrw-UWWOZ0_tmFTP2-ziWrMSzH63pTTVf0TZHRq-0h7QhXWHQqAXgKfqSfuEOhWZoh4viGwCgrtpM-3lqugNZNGeCFiYKrez_InK9kqrdKUwRRD9mMDi6eX-6MNezS2PnOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsQZ5lqFrOIjpgZciHtmQA-DroRyBUWI5H9rDicPXVCZs3D8IIpj8QcA3yIoDusRCP131Vr3dGbvgKsPnmY4uif7RBCiUbkaeV3-j4VvSAzgxNypQ4SZbQBhR3H58FwqRUSq6yw6KsMxNQ1zyL8i2O-XeglTRxCyb_Uo_Buxst5xAxod8YLQdaq1qdKfICZ5GKTUxHpE-386BWtsOY39cNw5gAkhBVCHSID_YJL9qPOBT75NdYqWnIGuHoPHKGOaa0mCVHSEPkeO_sS-367dqSBit7cIFJFnYiVt7TQctRHvYUqZaePf2D4DOV8WQrNBCEm_66dEnFmIjuTc46gGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnIQvhpbTSYkZEa-JX4xr6dmQdNhPqQLtddYH2dPSBqj7SeFTx6U3HZd70R9hDKEwEPmjrDo9N4u0GFV4Ucvho6Yu_-czA5KZAI7PA3m6KWCJxN96PGyKthL1AoRs_RLgKp9oA4gdgUkx8D7XMDm876QwS3XLydNV0zWN-LPYfHzN_1HFb1wua8NYPWTYRAdSPg74XqlGup0WnxYTsthxUjHQdboMJ9teJx4cPD2BKB9ky6gj5q5icLBF2Lup16KCPTacjjOoTepgeIBWgN0NByssTLfiBZOQn9CNQQLGJidI_JtMHV6MyJpOCmryrDcISByY6RvdWycOGu3h1Gtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=PgRyUHNvYn19tOMByyBJBM_Iabew5nJCI0C2yQERKVFcxwVH9a9b1w9jLA_5k-lK5ITXYUAPmKCu7mPW1DBTSlEmYBR3n8---kbuBblBwV2XH9NyZWJsQnbhE5CjxBqsEntAz7EiPu-PJWh-CSa-cQPkm74hHyOgaeb-JPSfF7VBcZTTVg5MS8pooN7TbSBzKh7HBCqGZE36Ak2een5dwYGvxhHwbvNG7AHYCIkJtNv0tiBMDlLlLSaegS7CFff2OG9i1XwFGX0bVyE3fAaq_qon1cwLLPn1MbuHKYWKJNnYyi-6VAuixnJT6vmV6ZVpymS1Xk0dBnX9pgCjGiTCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=PgRyUHNvYn19tOMByyBJBM_Iabew5nJCI0C2yQERKVFcxwVH9a9b1w9jLA_5k-lK5ITXYUAPmKCu7mPW1DBTSlEmYBR3n8---kbuBblBwV2XH9NyZWJsQnbhE5CjxBqsEntAz7EiPu-PJWh-CSa-cQPkm74hHyOgaeb-JPSfF7VBcZTTVg5MS8pooN7TbSBzKh7HBCqGZE36Ak2een5dwYGvxhHwbvNG7AHYCIkJtNv0tiBMDlLlLSaegS7CFff2OG9i1XwFGX0bVyE3fAaq_qon1cwLLPn1MbuHKYWKJNnYyi-6VAuixnJT6vmV6ZVpymS1Xk0dBnX9pgCjGiTCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY4AwX2Kce5hHFjomLMVe62l3SmJ8xcF8fHJqLucFyAYRyp61lRWZsPT_ptgkdxeKOsggYRrjP52nCMHWpDttgX1PXf2jVE5xDAuBnIHRKg26fORivrxedEwRWlEsnN7hgAaDtLOHuLyHHaelJbf8p4Lx0XWXz5GIJhoQ-x0VbPvHG8LmqKhdIv9d1CqgkzeJR9HrVHOQ66jBesZ3SxIagpPrlDyd_lLdPMnXWVtq-XHW0xVPS_6Nt8YVZehow3l0shPatHbfWx1Yd5D5KwdqaHIAiwL3-dYgkZRStKvq1_pU7853I0Rz1rbOjYqoTeROAZzq_RIR4rpeV30x2ke2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=r5fTn9w-T4xrVXBXP16aPrtP6n-XYSX-yVutRpA5O9c-D6fVbQcLODxBvx0G4TCRGBSEY1Kc1k1gnNVqf38LcF7-0bze9vpgsX3k6ycUECXGpz9P8if3PYs60vS2lA0Xj36WPoD7rfmW4845Ax2AbKzvp4vPqNEhi8U_VIJXdLDUuCfVO8bkYP0dzDMR8ZSxdfxFlHUEijuDMJtVNJ4nqz2rhMf7Nt-DzEEnFhHrFv7Im9OqCqUn0X3nDBlMMVypX5-VCPW2JTofsRp8gbPc-xKUOMFQysVOHZjfloFjc2VcWRV3TD_g--z_RJCEbIgRw9MPO9jW0sf66lsi7pwR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=r5fTn9w-T4xrVXBXP16aPrtP6n-XYSX-yVutRpA5O9c-D6fVbQcLODxBvx0G4TCRGBSEY1Kc1k1gnNVqf38LcF7-0bze9vpgsX3k6ycUECXGpz9P8if3PYs60vS2lA0Xj36WPoD7rfmW4845Ax2AbKzvp4vPqNEhi8U_VIJXdLDUuCfVO8bkYP0dzDMR8ZSxdfxFlHUEijuDMJtVNJ4nqz2rhMf7Nt-DzEEnFhHrFv7Im9OqCqUn0X3nDBlMMVypX5-VCPW2JTofsRp8gbPc-xKUOMFQysVOHZjfloFjc2VcWRV3TD_g--z_RJCEbIgRw9MPO9jW0sf66lsi7pwR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=jLyRNWb9izGho30X-DYzcj42C-m_DCvYpBOy3vq4MeRj57TyEWbiLykxMwr_guM6wLXSG3ArEPg6yew_Qnm84lo0S8NW8cANTLS6LfxPQDlY-QyvcYX9kni2T_Rothpidr6tPUekYRZoBlNmFwbDzpWZPHI86HW2o03PNTuO2vHwaCTJsp2cDuR62V-GOFbtBpDmM1IpgrVuPy4On99k-x37ZnB3zOgfiK1qUJ2IpzzTAIixgyVAVLb28kVUxESlHR59moCJm3F-knHkpRqoiNwpRFsBpehaAEFZgOCrqx0uUGuJZNadmk_SzIo9qTt2WvEflI6rM6F9adtBAhPLQauiWOf0R2ZEL9SDcaxhmhwqC7oY1gf3bBRSjAwbyZTwbp3sCBUdGg8H8ptGU7xapZZ3WkmSgD8PDlIKJXc4VtO1AekBYWP03vdqK5FXHTGiyq5RAFQ2AiNyEOmVQ-Uz34zIciGBpK6ndmpdZEzup4N8ukC1Ks9ckr1inbgjrRD950gbv-6wHQL1C_VA2OKYA92lDTp0uj-xIKfy8ocSDUgnMyI5nUs-KF2eVtgixuPRkU2QWJHePSk8F_DawDF-b6W8UyIKhLxZUNWSSpmMZvcfXmeORvXsLuAo3bXywGwrcGGbuse7PhCcr95IIJixS95XVMEQqvw3QCAw54SCzWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=jLyRNWb9izGho30X-DYzcj42C-m_DCvYpBOy3vq4MeRj57TyEWbiLykxMwr_guM6wLXSG3ArEPg6yew_Qnm84lo0S8NW8cANTLS6LfxPQDlY-QyvcYX9kni2T_Rothpidr6tPUekYRZoBlNmFwbDzpWZPHI86HW2o03PNTuO2vHwaCTJsp2cDuR62V-GOFbtBpDmM1IpgrVuPy4On99k-x37ZnB3zOgfiK1qUJ2IpzzTAIixgyVAVLb28kVUxESlHR59moCJm3F-knHkpRqoiNwpRFsBpehaAEFZgOCrqx0uUGuJZNadmk_SzIo9qTt2WvEflI6rM6F9adtBAhPLQauiWOf0R2ZEL9SDcaxhmhwqC7oY1gf3bBRSjAwbyZTwbp3sCBUdGg8H8ptGU7xapZZ3WkmSgD8PDlIKJXc4VtO1AekBYWP03vdqK5FXHTGiyq5RAFQ2AiNyEOmVQ-Uz34zIciGBpK6ndmpdZEzup4N8ukC1Ks9ckr1inbgjrRD950gbv-6wHQL1C_VA2OKYA92lDTp0uj-xIKfy8ocSDUgnMyI5nUs-KF2eVtgixuPRkU2QWJHePSk8F_DawDF-b6W8UyIKhLxZUNWSSpmMZvcfXmeORvXsLuAo3bXywGwrcGGbuse7PhCcr95IIJixS95XVMEQqvw3QCAw54SCzWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=Rwd9uxZyR-DI1SHitK4GhIXqZNyPiCywtKcMb0mTa51qiEKgtIH8Uszu0BtzHgzC8bAWV8dy5qM3crr1mOhPy2nOqTxBLgNaQzt2G8GDAxh0zj5N5ArGalNkUa3jXGwpM1xPBWm1mjGRrsDTYVgqQkSmBhRjXyyLvxE7Y7OzOO6XbqvVem1Gee90e87-a9mteyRMYDPuWR9267TuM7qm3VY631Ko5NAZ35vRfzrXfYg_XEKPXzFwg_ErXGBZ7y1kNChFJsMDNJqwZ5jGZPNGE14pDM3q4LpHqqEkTR-dHWiapZWi1DlWwimfsGtids4bn8wB-VrlGmr-URpTZK_agA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=Rwd9uxZyR-DI1SHitK4GhIXqZNyPiCywtKcMb0mTa51qiEKgtIH8Uszu0BtzHgzC8bAWV8dy5qM3crr1mOhPy2nOqTxBLgNaQzt2G8GDAxh0zj5N5ArGalNkUa3jXGwpM1xPBWm1mjGRrsDTYVgqQkSmBhRjXyyLvxE7Y7OzOO6XbqvVem1Gee90e87-a9mteyRMYDPuWR9267TuM7qm3VY631Ko5NAZ35vRfzrXfYg_XEKPXzFwg_ErXGBZ7y1kNChFJsMDNJqwZ5jGZPNGE14pDM3q4LpHqqEkTR-dHWiapZWi1DlWwimfsGtids4bn8wB-VrlGmr-URpTZK_agA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=nQfMlLggqDCkRST2IJZ0JBd-DOVSXmyO4876VJTd-eTBn6oSxrhtp_1XGj2U4E0H22eXqna2owq6okhJgukyOEH7flO_AJH8aFt9-Kc9t06leSOmawCNmbJ1jIh9ps6SfMCtjC0_1QGiIwzSqMky5AvY_6zWNoqJxR3D7ht8qhVjGp7_KOZzchVFcXYwn0AmPEd6oTwpkHAvXxl3Kw7OaWTd9ohRRdOg-KWm9v2LS29NlhxiQ6jq8CzZOEBZSYROu4uaMC3hKgVtMU_ENNuh1p20mVjPbHlmii7T6yo-5W2h1C8jSi-UCUjNpfHC3khnw7f5-g5jiK75xQZPCQ2L2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=nQfMlLggqDCkRST2IJZ0JBd-DOVSXmyO4876VJTd-eTBn6oSxrhtp_1XGj2U4E0H22eXqna2owq6okhJgukyOEH7flO_AJH8aFt9-Kc9t06leSOmawCNmbJ1jIh9ps6SfMCtjC0_1QGiIwzSqMky5AvY_6zWNoqJxR3D7ht8qhVjGp7_KOZzchVFcXYwn0AmPEd6oTwpkHAvXxl3Kw7OaWTd9ohRRdOg-KWm9v2LS29NlhxiQ6jq8CzZOEBZSYROu4uaMC3hKgVtMU_ENNuh1p20mVjPbHlmii7T6yo-5W2h1C8jSi-UCUjNpfHC3khnw7f5-g5jiK75xQZPCQ2L2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNxGZQNazei6XsIFj-_4ZNVVh31ks08-AUwAIr1BUKX7VRvyROuMrdJ-L96qD-mmDzlXZqrgXk-JS6Ncx0H0QGUVyIROxggVpTfBQJ7HVgzuhgwFVXe5rcA94Lyp2IY4BG9BKZIkE9woT0Coso_83b7EGsyGnZ_GD_iBRyn4ceyvePgupWBC7-ro8etQcJx6yvgMtA-oJEB9DTJ65WiM8fhxTcv0_bwJahsCOR1CfORrJyDsX2yZE3tfKmMss0V4-hJdHtaJc5IQTkQo0LemhfQYwXj8AVFPrRweKrHrwWxHWPZNA19dpgrLuBc77f0it-d_eLOfI5jNFv940WaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WHwmyWd3Ddhc8Cp4mnsS61RJMzp7oFDE50QlL-vGLlLMz4o6uwvB-xfbiKxkRdrMux08RYvc-yHb_RKRAK4oBF-zK5mUetcvGy-jOOr-hJDmLj-jizAlr2vmc3s-NV2NbQK6IAWvR7OtSYONAplfM9v11QvZQfJb3GtbVRE3zYxVjqzd_JSwz-qGmlOWp3qgaq_7sC7GP_346VMkurNomV0db6ghw-YxJnf8epLEMm_N8vQYo_vOHzYtt7KTarpP0TWzSZONAeME5ZOFe-FtOQdig8cHqRnLGpGWJtWwFlTijeL0E11_vOymcsKffUG0z0z23GG6b-OkgaGNXuEP1vc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WHwmyWd3Ddhc8Cp4mnsS61RJMzp7oFDE50QlL-vGLlLMz4o6uwvB-xfbiKxkRdrMux08RYvc-yHb_RKRAK4oBF-zK5mUetcvGy-jOOr-hJDmLj-jizAlr2vmc3s-NV2NbQK6IAWvR7OtSYONAplfM9v11QvZQfJb3GtbVRE3zYxVjqzd_JSwz-qGmlOWp3qgaq_7sC7GP_346VMkurNomV0db6ghw-YxJnf8epLEMm_N8vQYo_vOHzYtt7KTarpP0TWzSZONAeME5ZOFe-FtOQdig8cHqRnLGpGWJtWwFlTijeL0E11_vOymcsKffUG0z0z23GG6b-OkgaGNXuEP1vc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH1wDFk8qxtvuH3HMoLvjco4drExwpXBnCwvvps9UST_7APK-gphUA3jzJwQyoRNvEBbCnPBGOiahgD5dukOkcQFpc0t_7LKmQEMZkl3C6VhsHMJ-x_9y_Xnqzw5x0qKkgF2VGLThol-b2dNjY7CoTzSNf2I9my64jgGkigaVu58e7jtpPbxf1jRaqtbwFZkzvIKGz_-aGiNzAyEw07Fg4hnF_dgz5bhVRIMzTAiPJJJdxWbFMObQciZXeY6EH_msZxdRQi7gt553fclD5pgki_ni3zNaRq-GC4o_7aACG9YhfbkC1XMi_GgqzYFEJas2av-Qe2W4VPDplzsQlh0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g98-HcKDiCyWpPlBJ6TAnixx4WOnzz3MxfiAVLiV6Nl8-BWra9ME_KQDtD2TB8DTMCXAbU0TpbWw48SfM-p--rlRnKduzOpnaGjmPsQDzWdcC9WxVQUDFeE9vPjf9q2R_NuasdbnqG_2gomzm6aGUddUXKgB1ZZWRMhu7QX1pfU3T00NP9WoT1QjsqsIiOiWMtMOHPSQzH1Xb9M7bZ6acr2B2pQBwjWdqci3CQalFmuAt9zmF3vn8ZwLrpr5VeioNAJldDnA4b8JaqomQiEdXalEYhiLKJ0G-06ncBTME3jmqB2GTJISpHwl5fV9IJs91lkZdt3QTwv90uoNpGdrhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=QzUmmcWROe8FcnQogc0rcoyEXM11fWw-WV_hhN5Lh1yEv2KPMQGH5aio_i79cIS3_xf_HrCTHd_A2RNkj1c_iRoOc9E8CG-3xIZXnqvjrc0ikL2sGp5GR3OsXjSWlhSXvUMcK3wgbHiUVL1dMgA8kfv2AF-tlogbu1LVuZkzz9iW9PypNhqkypD-ICcWIicGDtHg8Pr7-XZZ1PQEQoJ5RTdPix391_kTWvlqoDPjUoZhEfuMUulOWuyx5v6phkExZuvZLWCxnmw-Yj2Ct2B1rI0zznZ15BHtKAkMC5WpV9Kj--NuWSFwgK7e1w1MZWVjk-32zjwWg3VcPwplsn_fizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=QzUmmcWROe8FcnQogc0rcoyEXM11fWw-WV_hhN5Lh1yEv2KPMQGH5aio_i79cIS3_xf_HrCTHd_A2RNkj1c_iRoOc9E8CG-3xIZXnqvjrc0ikL2sGp5GR3OsXjSWlhSXvUMcK3wgbHiUVL1dMgA8kfv2AF-tlogbu1LVuZkzz9iW9PypNhqkypD-ICcWIicGDtHg8Pr7-XZZ1PQEQoJ5RTdPix391_kTWvlqoDPjUoZhEfuMUulOWuyx5v6phkExZuvZLWCxnmw-Yj2Ct2B1rI0zznZ15BHtKAkMC5WpV9Kj--NuWSFwgK7e1w1MZWVjk-32zjwWg3VcPwplsn_fizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=lf9cF9sW9nYnS3_b2klicl6h7PGJaHKXzzOJhmVvY4E0pAycwXHgs-mimoxTgeCJT5gI9114-nHTVkmObWniwN5o-LHd2YMcv-DARCeJUarADbFVygbXsDA245hxmf6hvKLV62h_FsnQmyUtF6VpSEy7JwWgCOj77N_smVPDva1x6ZZiINMTo6oBspyhbJqppDKVhF-RptyBX_vuPXkY1yKN1ye8xM9A-EH_GgeYBtb83ibLLQ4fx9ZPFUBw7sdXasKsIkCC24EtEwPp9nhv8nLoVxNxX13mPkPLr9NATcwZd7u9ZDrHdCqlwm98uKV-62dI8TE3W3T_zo4De4FvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=lf9cF9sW9nYnS3_b2klicl6h7PGJaHKXzzOJhmVvY4E0pAycwXHgs-mimoxTgeCJT5gI9114-nHTVkmObWniwN5o-LHd2YMcv-DARCeJUarADbFVygbXsDA245hxmf6hvKLV62h_FsnQmyUtF6VpSEy7JwWgCOj77N_smVPDva1x6ZZiINMTo6oBspyhbJqppDKVhF-RptyBX_vuPXkY1yKN1ye8xM9A-EH_GgeYBtb83ibLLQ4fx9ZPFUBw7sdXasKsIkCC24EtEwPp9nhv8nLoVxNxX13mPkPLr9NATcwZd7u9ZDrHdCqlwm98uKV-62dI8TE3W3T_zo4De4FvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=i1YaDY7PbrXBvlxsU3qdIBlIriCYdAfrAP1IhHg7Sxo5KiexZ_Ktw0ywNXEA5ru4a_9PgnwQfmgi0WcN1KDdkMD1ZLO7nSkHca3gcpX1Y0_ugjPX4arjBNuHBAbpHE_9YElnZqM3VN3JcbhpuDVpA6aPXgWzhygGWmSTnbniMtp5Yd-hrECzEAHjI_UYw9MUKygcKXOA8GfUNPIql3TrVdv69_gUlVDxN59NqMFs9UjNWE0aIJTPL6fAZpmLxjTv5ucr309jefOOd_w9vWj3Z9OtppHQnYw3e_CUP1Xi_qQrNbn22nlz_F_ug0lVecyoIxWIy1CLtvHUAsXY-Cb_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=i1YaDY7PbrXBvlxsU3qdIBlIriCYdAfrAP1IhHg7Sxo5KiexZ_Ktw0ywNXEA5ru4a_9PgnwQfmgi0WcN1KDdkMD1ZLO7nSkHca3gcpX1Y0_ugjPX4arjBNuHBAbpHE_9YElnZqM3VN3JcbhpuDVpA6aPXgWzhygGWmSTnbniMtp5Yd-hrECzEAHjI_UYw9MUKygcKXOA8GfUNPIql3TrVdv69_gUlVDxN59NqMFs9UjNWE0aIJTPL6fAZpmLxjTv5ucr309jefOOd_w9vWj3Z9OtppHQnYw3e_CUP1Xi_qQrNbn22nlz_F_ug0lVecyoIxWIy1CLtvHUAsXY-Cb_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqmXBd6Dq_C5wZTnrSFLqfm59n694ngFVhBYT0JYoiuT9-Yd5zWOGUv87Bscg4Z9Sj_MfiwZ3gRK5OcgCvDXfRdyydqGkPsLS5T6R_psMcr6Vrx5ODfz6Rwyc0Djq2g3SfP0DzOsULnY8kKzGqxsr-e-3ODLxAGK1rDwdMI2MWljUkyguSypnFZaCJ1v2NxrXotbv1MjPtV3ppYKlSenGlmby6EEgN0zprc6fZD8IcLf9DigS0qPPWasAfltyqoH6gKgJs_9FXSZvBYjomfqxHR2E6WoAnBMgHYo20XY3wreuxjHesCH1fWT5DOOLhaig_bdrE-wMr3KatkN-I4udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntNjQ7n67OjUPAFJP9jEntg8ORvkRq8OIBddaQpNAvezxdMeMcVIU1rcM_vz3G-i1JKQu9gdEsQm__Ik7dAzVShJq8pJ1h71uNAc7s_lPeTtBdNXPxJFtJBXgcaXJmRONxyKdK3A1rKrx1rLaRhwRsKt6n_SeEVYEgNNFPK9XSxOlD_J-on_cu-bccKMEJzSuSZ4fYpuIdvH17qJ2czDwEeFwwT0as8aLm7El9D__QwQ6qBbFy7xM_iGr-i-S9PI3pJrW2ek9sJcfO9arnxwa-3sGVZ1sboImAInx2zH4l3akjHJ4fbk-p9JQWzUg4sZWUTIf8wwmI0-hTOyiZnIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EH4IV-COpx6M7OzVc3FG5Fm8ryIxeu_bV8idWbbes9jsy6hvHRCU6PxylcnC8GrOrKOr1kQHECzMzicaS_Wo2jxUl8bpuj6ZKLX2MIWvlljF9y39UWB91B-YKekdK1BiVleUOG50pekMu6Y_WYQjnmM3HNh3sWSx4BUm1ycEaA0jPVmaFJIWMU9oHWlWchI-4AU8fK6WclyF5JMKxqeLbx6fQuRh9GP4jCX5jw8gKy77YMYw8YGXi839FyQAynMnPJdO8wmcKMIA677DgKv2Yf5bgXvk8lS5uM_VH5VHCbDlzriLB6zoUMbG465PoO0BroVmJ_DkAMmvoA5UHEm1oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=fEO6D7s95CcEh1mY9smQ0dW4l3QecrorX5dMwWGt2s0ahQo9sXvheaPFHMrmSWKryL2_Fu-MPFIFwUA2Ryz8mV7EVmAsTfmIrgYhKihllSSQfvRsM60FxCX8_u4Kf9KTJgMLUWwzembSk_cZCw4J7OTTTduhWLn26nPZvr_anNpti9XJIZLEiNfeWUIbdusAT4F9CyJVux6kOo8X0kJe535JFNqthjeM8eXp7PffNlwfwE54k0-XX_Y4PwKj8mRYlHEOxtiaVU7JFsDtbMaqqphp8FzT71kgDfSVSBkLhV2Zttupg5yO5yHqbJEYjCNWSpwGXMtgXd_m-6XifVlM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=fEO6D7s95CcEh1mY9smQ0dW4l3QecrorX5dMwWGt2s0ahQo9sXvheaPFHMrmSWKryL2_Fu-MPFIFwUA2Ryz8mV7EVmAsTfmIrgYhKihllSSQfvRsM60FxCX8_u4Kf9KTJgMLUWwzembSk_cZCw4J7OTTTduhWLn26nPZvr_anNpti9XJIZLEiNfeWUIbdusAT4F9CyJVux6kOo8X0kJe535JFNqthjeM8eXp7PffNlwfwE54k0-XX_Y4PwKj8mRYlHEOxtiaVU7JFsDtbMaqqphp8FzT71kgDfSVSBkLhV2Zttupg5yO5yHqbJEYjCNWSpwGXMtgXd_m-6XifVlM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNIT0LhNCFO5mEigBv4-btzrx9N0_5dnDTC3K1yYK31JdJdU6ra9QS1wfkkw7pz00dI27IazhCDVvoqhqHG4vSRL6ICA_qiSLkSDbzlbS33ujLCLjrv4f8PY-Zi7dAKCwUh9sd5ufYbDGETYtRsUxmCan6o7xDgXLrCWvNouPRfcPEK-C1LIHxjW9xF1DSqLAlkBOlO9Hvs-xyNCFfW72fjZosCIbKdkp5bSmZIIsOgJYvPTmZKecEQJ0NkDQMtINvjStjFG17f15-mCc21Bm4TU_ZfQkuGvE793BMFKpxyGn6P4velmMlX2Rklwh1DnHvKBiqJoGt2jgrkFuZ2YPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bI_GEZwhL-Q1tRVzhcsL2pefBUZCLmTjkQbZUbPIh2itvJx8KlXQF-AedPLIVBixkkd3OaPRdziUT8k-HxIEDpveTwC3p5muGHAtqWKSkPfymCc_LVEU_e7U-6aQ2uRIO0-vy35Gg-o88zuR1eRHOXaC-w7RwYXxb8D9hgso14JqOd8gOLdCpQxMx022pibpv1S1lrg6pBO6PN_pmYncCf8GpnL2gsOQmMrSr2zGpUCIXvM4BlTOmon2sRekQ0vhOQWUBiedrAwFlnK1RMMtEKdcJVjmO4klHLDE7cJtW4gKApLHdmSQI23OoGhjC0yCiv2YFt7NWeJtAwsib2g8ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bI_GEZwhL-Q1tRVzhcsL2pefBUZCLmTjkQbZUbPIh2itvJx8KlXQF-AedPLIVBixkkd3OaPRdziUT8k-HxIEDpveTwC3p5muGHAtqWKSkPfymCc_LVEU_e7U-6aQ2uRIO0-vy35Gg-o88zuR1eRHOXaC-w7RwYXxb8D9hgso14JqOd8gOLdCpQxMx022pibpv1S1lrg6pBO6PN_pmYncCf8GpnL2gsOQmMrSr2zGpUCIXvM4BlTOmon2sRekQ0vhOQWUBiedrAwFlnK1RMMtEKdcJVjmO4klHLDE7cJtW4gKApLHdmSQI23OoGhjC0yCiv2YFt7NWeJtAwsib2g8ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=KucoVCTPGDUrxgEtOhNKKB13J2c4GEzPjieAwC8U2X1YbjTVtxPpeLpJlhcwlc4PXd6sxV87xwVu-obZwJgwkdqsc4e0DbMKdeotMJlR8Qqan3Do3RgbzAVcSLGtw6JBnE3aVqaTWnpPx7Df_7WPJjVbDxt8gTUPj84aBGoNJe6N034CWsASAh7hzXZnpF00LtfgH_YpRU0MUrXutBM3SSKUv-xGmP3N0Ug5zueX0jevEYXo-pZG44u0_2gp5sn3FHEck8KX7OuIo3uZSsY5f-DTE_bMTMbZ7KgYXxzc93juWnYk7x7qhLstVGKYvNXWdz05-8sT2EgDgN9YllsEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=KucoVCTPGDUrxgEtOhNKKB13J2c4GEzPjieAwC8U2X1YbjTVtxPpeLpJlhcwlc4PXd6sxV87xwVu-obZwJgwkdqsc4e0DbMKdeotMJlR8Qqan3Do3RgbzAVcSLGtw6JBnE3aVqaTWnpPx7Df_7WPJjVbDxt8gTUPj84aBGoNJe6N034CWsASAh7hzXZnpF00LtfgH_YpRU0MUrXutBM3SSKUv-xGmP3N0Ug5zueX0jevEYXo-pZG44u0_2gp5sn3FHEck8KX7OuIo3uZSsY5f-DTE_bMTMbZ7KgYXxzc93juWnYk7x7qhLstVGKYvNXWdz05-8sT2EgDgN9YllsEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=KQCrTAkXFZJ3aqsKE6jdbP3mYWGD00P6RYsNkOPxijDh8PmDpniJCO2hsbXpiYVf1wblPrAon2vFlLXoQm65_Bch8GlohfNDZhLh8TNOB8iqRMBjDHMGLjUHrOP_JZ3cXqbrq3HuNdyYnVwuSv3mtTfneAY5WBtqfkbSEYu3GSnA_BHAbhUEi-5tmcxmrw4AsJoCZM8SlAAjt-TgS4lK8XBp8hzIeM8rxa7FkjvhaqrN0P8OX0SaelitvKrC8Peni7Tysn5YBUWk_rusNNOu5Cz5BiJjqYRiD9uAGfVYuCTzt5OZUCf9l2G0pB8_buDj7c5OQquIGC-KooSjy1j-jGjUGzU1c3xkLuA2_YlmlJGrIntim1k6K6d7U_NTK9cAT7x1wONzjMzw0MdOncp73sd8t-jAdv-2FsI_uqm1yv4abh8BSXGlLkJK1OK7tOIzGvn4Mx9LHo_m5nIkowQ2Y0o1mc7uhTrEPOnB5Nb6ihHFky8am3gkO3OP6X-zqhaYDj9iPLAuskHsih_VOfZCTh5mYIoLAP3-X2U_tQXQdFnPqXq7tuNmS37alsbb7euEIm_OBSP-8GV0ff3oVJbioezwV-PrXI89CyccGpreFzZ8UdIpw1_9ohvao408tZvN2effKQaQXRtZa4Iprg20lDGPVcXTzCCW-glf_TNbwis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=KQCrTAkXFZJ3aqsKE6jdbP3mYWGD00P6RYsNkOPxijDh8PmDpniJCO2hsbXpiYVf1wblPrAon2vFlLXoQm65_Bch8GlohfNDZhLh8TNOB8iqRMBjDHMGLjUHrOP_JZ3cXqbrq3HuNdyYnVwuSv3mtTfneAY5WBtqfkbSEYu3GSnA_BHAbhUEi-5tmcxmrw4AsJoCZM8SlAAjt-TgS4lK8XBp8hzIeM8rxa7FkjvhaqrN0P8OX0SaelitvKrC8Peni7Tysn5YBUWk_rusNNOu5Cz5BiJjqYRiD9uAGfVYuCTzt5OZUCf9l2G0pB8_buDj7c5OQquIGC-KooSjy1j-jGjUGzU1c3xkLuA2_YlmlJGrIntim1k6K6d7U_NTK9cAT7x1wONzjMzw0MdOncp73sd8t-jAdv-2FsI_uqm1yv4abh8BSXGlLkJK1OK7tOIzGvn4Mx9LHo_m5nIkowQ2Y0o1mc7uhTrEPOnB5Nb6ihHFky8am3gkO3OP6X-zqhaYDj9iPLAuskHsih_VOfZCTh5mYIoLAP3-X2U_tQXQdFnPqXq7tuNmS37alsbb7euEIm_OBSP-8GV0ff3oVJbioezwV-PrXI89CyccGpreFzZ8UdIpw1_9ohvao408tZvN2effKQaQXRtZa4Iprg20lDGPVcXTzCCW-glf_TNbwis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kbLSLgqBAIVwB1e8zR3kDulZJqI-NXTIZ9urahXOSO6w-OCeMh_gj7_LZ_BIiiw2bYk7SRPMZLLDTnn9DOx3cIPaDJUbsKGfQfnDSgKKgwTRNYA_n1s74MfFCaBm1RF6Ad50wr0lhXkX-9Hfrv6s8SBJXnKnWqzt7HriEVmhBhIUzqKXN6zniNnsM_LU28dhW6BnQEclyS-iyPintDgtnbdDQnQBbgCKeihBTlLJh0i2eRP2iQ9c6jAdyfWwbvLLJChNSUE2ah_zDCr0oOjs6IWIy4MAfQejnOQ37IDxSTftNhPnJw2X3Hh7fk_WODNwDVlA_N8ou7Fxdw0NsWJnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kbLSLgqBAIVwB1e8zR3kDulZJqI-NXTIZ9urahXOSO6w-OCeMh_gj7_LZ_BIiiw2bYk7SRPMZLLDTnn9DOx3cIPaDJUbsKGfQfnDSgKKgwTRNYA_n1s74MfFCaBm1RF6Ad50wr0lhXkX-9Hfrv6s8SBJXnKnWqzt7HriEVmhBhIUzqKXN6zniNnsM_LU28dhW6BnQEclyS-iyPintDgtnbdDQnQBbgCKeihBTlLJh0i2eRP2iQ9c6jAdyfWwbvLLJChNSUE2ah_zDCr0oOjs6IWIy4MAfQejnOQ37IDxSTftNhPnJw2X3Hh7fk_WODNwDVlA_N8ou7Fxdw0NsWJnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb_kk_tH9BVgKKk2A53FvYStzmtTtJIP4j8lXB3s3AbkRKtEvZonyXMtQFdHhQavcprdSCYuGJneVJIVQSOyqN_qyJRcnvWdg5Ii_n9izEHNc9skeUsYn4d7mALAM9Y87UIOkF_8WUkN-VmEJB3MdPpuVVCZqF6bwHNmDUq2osNfT2ZAsdrOyUnONEwzDcjSYiEfCgIyl_26roRzjWfb_-JgJiqvOhZeVkWARI6CAFDx5QO8YwlDIJkIJUVu5YxWMTvUKjHHc8pQU7IJqwDb_fVoYX9C2Yn_gwiCL_kBqkjizoo9_-U3BW3VsxNw97zpc6W2KdbwhKrowDl_SPx1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLt0nzhQkmQIkQB4JP6JhhnpQvgP2jpfOYmKQ1LvQk3opHp3MD3dA4FmC4Hd-tyaDJbqAAoUcxnF2KGIXQbHgfDk5TXgwGLIy-f702_0wgpSRbW6_8oIZLn1XMnc0wEzIsODbU0TEKN8WHoqBYr6fLHASNxk0_QEzg3g4k941VfwRFHDsNnFEWER0Ao7sJvN-8NQgBSv2VIdAdhWlaHNLBBujiR7qg3r0fAM1GDhficm6khL3DpGB5ZKducZ0P8GOWgsaMWRC9_-mSNxMsw4y1HOyxfAc_LPIRVzsCQ6NUPbPFNr1TmYpqxOoa6hngRYfpQFvGoLUQBDjDvu5z49rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS6nWGx_PBuQV5KZfM8BiIxkQIl8b5UvjUpjY9wMQQ76Gqpttm82xpP_5OLxbAbrLEzBf4jFPaWeFbnzHmp85BRXkJKkcSBlizS-dEqYqfcK4QlU0TzehCdkmLaL8xbqzMa-Pe9UEWVGGtIk0pYJdlkRb5ljd4jjsdwzdkpKe1Wicxcek3TIf19ds46bY5eZIMPUs8eo1A0V8ZTVk75PxRkG5p5eUz8WpFX_LN5xXS-EqHZi64xF_9JerEt5OCvXpT2qZZyBBt7X09Bx8up5Deez4GP0jDaRYUoCASJD6U1WOjyP0M8e_37rNfxyEkYYZ_Lvs9CyN_CLz-MUWXNBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Zzo8LRqA3lXwgO4CnWlv-cuNoL6fmv7BgzSG_z2k-Dj1QQsc_y3wtiq84XgLU-7cX721b3wXw6AXDGppjjPtlOQqg4v3ICZ0-S9y0EWHgAn8jcXF8LBS4GO0IlCvYi8QcW2A3OwqrjDMFu6JJiuA3gmgQji-w5WJDFEYYZf3YGcC7B5mPmIBHZLxqrLz9WvJI7DwtBOoA4zZ_rHR75HShC--78bJOh3b5TEv_Ez5J6BBOVB9EgcX_7lMGaM63yJ8tQEWTftY8u5PVbGO7c8MJ2x8PxI02GYXX2SvyUIgz7JjazP-dQp6T2Hbhx5vstMIWLZ4RQe2q7B-mdeXvVzA.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTOQNxumEKqRvfZcrxbUK0DkEWVpIejKwgYdSttnOug-jUgt1v69GW3iUJkDV8IW3SKeTFl4n86QcxX5izpODZxQbChwVy8jR5vUpr3CmgpwfQmKLYeCae1WeD3Ai8QfVsAkTREQKb5lHSxQzMYf5-a1XD9ytZmDyb9392Dv7KruN3Oq3rVoKTbqTZfUcKT14bmGBIUEssf6jZtR1e8ql0BwB1Q_NEY9JCket_zZimoVFtk03V520ieUt3IFbpzU0bK_lIBirOeuXI3VDwN-iCSWizWjM17HDQmgNB7XSyLfUZhsaylzza9_A_DDTOLQZCRC3FTrAolquVjxsN4NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujkkTVcRF5RMeNtnIzsNhf1xJ5R14YI4wX8Jgr3yom3md1DcbLLzIetQFx91e95Fd5itD3_sMxdPG_ybb19OF6oDjJ7CqNBCXNIbwBAO308Iw7s7Cx66AMmW_msmrFyjx_iGh-WkX-fpux8phHiRqCa1C5uEljlgzC4c4_bX0zwU3_xYBZ2xUrcY9HZ8Ft0ozadnEAMkuBTh9tQGrFNQ3csNNYRC8QdJzhpviQzHaPOpGPtX7Mzn177mlH_aUUC9bW4v-KYJWP96XaDeCkW8R2Zh-84dD0-JpXeB-jvovmYMUVj_v72679HjHqIXawXd1h2oQSHAivBVCe6K_1abQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=nFtp0yBszikM82iW8z7K_IPJMIebdJvsrKXVj34YX0594IpWKtkXiWmwciZ-zGO6yp-kuigoz04t1pKWA2Zt64a-l42Moz1DrWxqoM0OmuHB1dZZcAAEPx1RbW2fj3mM4SUu2hKnGtnHV-RLCHMCrTWKPSDrT1On_hzLLyzRe_h7Gb-t8Ihm9dvrjX8L_U24pOKN2JmU8lI-0hRakl3Y-7aTluOo0Boivxxk925XIbeozb94ark_ZUOakOXBPWxkPHtFZquDZ9R58a_iltiE2AljNkrJnZplbbHN2KPrwBIcsCA6SiLTEroqrLssf28fwzwtvsQakQpgiTEyDgBO51EDy7ZBqwBERvlA1TWWOv2BTpnqGuIwD7n_Pis5cKDW2xr3JHIh9tZGfrmrfwBf0TY9xLDsdr_97s6Esdk5CvomeILUmhbjZPXk3k5TbnI-rMR2KQWdxYrZLv-9Mz64mxfB658cwYOnSINka61Ho4kHZOtZt0TKHAIRk4mZEogfUGBZ8g-P0Em51wo_oX65k_MjZI2VmJHxUiWG1kqL64hlVxQ6Kvtu60-urXMqVSKdqu5tA7nHImSp8HyrLkCwFPx5ygoa5CNWJyaizqxgKJjtJCsOzK7z2n8ieFL2KnyBpukpeHnpY0dUsmRPD4HxPtuQg6FS5sZvQHIWXshUlII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=nFtp0yBszikM82iW8z7K_IPJMIebdJvsrKXVj34YX0594IpWKtkXiWmwciZ-zGO6yp-kuigoz04t1pKWA2Zt64a-l42Moz1DrWxqoM0OmuHB1dZZcAAEPx1RbW2fj3mM4SUu2hKnGtnHV-RLCHMCrTWKPSDrT1On_hzLLyzRe_h7Gb-t8Ihm9dvrjX8L_U24pOKN2JmU8lI-0hRakl3Y-7aTluOo0Boivxxk925XIbeozb94ark_ZUOakOXBPWxkPHtFZquDZ9R58a_iltiE2AljNkrJnZplbbHN2KPrwBIcsCA6SiLTEroqrLssf28fwzwtvsQakQpgiTEyDgBO51EDy7ZBqwBERvlA1TWWOv2BTpnqGuIwD7n_Pis5cKDW2xr3JHIh9tZGfrmrfwBf0TY9xLDsdr_97s6Esdk5CvomeILUmhbjZPXk3k5TbnI-rMR2KQWdxYrZLv-9Mz64mxfB658cwYOnSINka61Ho4kHZOtZt0TKHAIRk4mZEogfUGBZ8g-P0Em51wo_oX65k_MjZI2VmJHxUiWG1kqL64hlVxQ6Kvtu60-urXMqVSKdqu5tA7nHImSp8HyrLkCwFPx5ygoa5CNWJyaizqxgKJjtJCsOzK7z2n8ieFL2KnyBpukpeHnpY0dUsmRPD4HxPtuQg6FS5sZvQHIWXshUlII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElIjQTvaJ1CYcW4jp6KCcQ70DHcuWqfinHQwXQ7S9Zgo8IhZq6sK1Eo33tiA5KqXRG8pjj4DIoWRue3lp4HveUPpxul2X7MG6WQsES4Aj9cKZwtPC2nVyMYUntOMK-ldCiPNPz6Li-2GGi-m5gmvrcM96oMikzYOG-U41pFkUSY3BEylSZSAYy2UntVTMIRezL5ys2wEFxOkxqTRjrrcshl_i0tMvn9zQrX2NpmITjGQHGSRQekV2jDBz0LCAnnqKQT52eL4MqDrU_OlHbCsgEC04pkYJUR_l50SoJcEbZthcC4NvkU0OYv_X88YkA8gOXQ15ePu1t7x3FWEigM-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEAa63naLmKfc26nSCTCaj8KDLA04PNrQ3S3gM7BPtM4bCf59SvNs9IcBQfonBCOMduj150M11EXWIgpSAOmkzrA2kgEzmva-ZB-DAqO4M_GhwHCBkOUmLTlKLN0ZDjE1hgYK_qwa-452ADpz12gP3d3FKwXv2tkO4Jh9a7gNNBORWWvO439NHRSsvIjASl_8q9n4G3Ba6AG2A1H4sz8tfYfvAeYVJRvZ5hyDybyctcOXOtDOI4dFYAE0wJRRVo0vAvcHiGB_EdcykadvjJpuiv8bJQwaD-HKYP8_oYMsmN3pvd30caQPa-1DmLCN1VjI8FuN65eXcB_a2BBWkFh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=ZLIWP85ts-r_KCv6djqVFOQ-P8LW6gJTxHERRuQHov0WJ2E-MSVrywT_ya9RYBmxlTyXRsKsSB9D_VgtzR5Zxq1dgqIOhWOfSDpn_i9oGAu__ss3CXaS6XO89231CqPjd8ukOqX9q__0GpS_Yr5VJHLPKDOwERvn-3RlMcNDoO7jrKq2BSeq6MbS-gm2PF04IJc3YqsBfdVFsVuXlH6WzZxjvehF3IcSkb5AngWUFq7qGRTxMf0EAGtjqdZPbdya2Bzofhn9-_sjktYpEoluUnS9_ezfKNxtsQRLa9EO0PCitvuBViEOcWXrRhHWpRAkLgBaJDBJku5oXlk_1Vh95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=ZLIWP85ts-r_KCv6djqVFOQ-P8LW6gJTxHERRuQHov0WJ2E-MSVrywT_ya9RYBmxlTyXRsKsSB9D_VgtzR5Zxq1dgqIOhWOfSDpn_i9oGAu__ss3CXaS6XO89231CqPjd8ukOqX9q__0GpS_Yr5VJHLPKDOwERvn-3RlMcNDoO7jrKq2BSeq6MbS-gm2PF04IJc3YqsBfdVFsVuXlH6WzZxjvehF3IcSkb5AngWUFq7qGRTxMf0EAGtjqdZPbdya2Bzofhn9-_sjktYpEoluUnS9_ezfKNxtsQRLa9EO0PCitvuBViEOcWXrRhHWpRAkLgBaJDBJku5oXlk_1Vh95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=kknByJqpeBvz5YlbIJ5mvtyeBLGiqbSw93j-vepaC1kFtQETEvrjtKUcgA7AGZrG9eb9P9bFaduAG7LuMnrAnrtY4kVpvJ7Mg1jwWmxwqfMWtJheUoDM9uQsd3YpV8uVgSNF4xmxw9V22MrToHAy4XMQZWsYyVJfrY8bQXU6kJGnk_lYuWJYW2JUmHFZnNibsvoYfUic11TJBCYGXWE1fHTeE_MlrgIJQjSHreO3iTqlA8-GKU4K16KOIanP-xuu_gzOuoFiVgCAhHc-YLtvtxcc5VW_mmKBQXg6p9MR7VWEdeQp5aGmX30N52k2iydkGBiRuvXzY-NsiS5BVpIeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=kknByJqpeBvz5YlbIJ5mvtyeBLGiqbSw93j-vepaC1kFtQETEvrjtKUcgA7AGZrG9eb9P9bFaduAG7LuMnrAnrtY4kVpvJ7Mg1jwWmxwqfMWtJheUoDM9uQsd3YpV8uVgSNF4xmxw9V22MrToHAy4XMQZWsYyVJfrY8bQXU6kJGnk_lYuWJYW2JUmHFZnNibsvoYfUic11TJBCYGXWE1fHTeE_MlrgIJQjSHreO3iTqlA8-GKU4K16KOIanP-xuu_gzOuoFiVgCAhHc-YLtvtxcc5VW_mmKBQXg6p9MR7VWEdeQp5aGmX30N52k2iydkGBiRuvXzY-NsiS5BVpIeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=XFEcrKeE8g-KJeoPGGPXh1RlLNybCBuNcl9F1F4sg2J5kF6uS_peBLl6aZ_dgAUuMsBAbGC46wPsreVFi1Ec4qk3JxqwVC7S8iEwhWhDeRU5QVzS2oSKkpVTodA1m8kw0BTX2EGaVBvA3UAJ_YM74Ad2zJ-M128tIABXCuNWSrLw15ITIiyKhrkvsw5JyRHn2MeckzXiiN_XiimI0khaj6na8N7apudrkcPi-c_yp7vA-a6VB__jC6G9oY26rPfc-XeAC5SZsKttalQISkM9NODzqYlqY_-t01Wl79fMUrW32vWB-kbNqBYF30VYleBsg2Og0gOi1mAA_odIWUh9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=XFEcrKeE8g-KJeoPGGPXh1RlLNybCBuNcl9F1F4sg2J5kF6uS_peBLl6aZ_dgAUuMsBAbGC46wPsreVFi1Ec4qk3JxqwVC7S8iEwhWhDeRU5QVzS2oSKkpVTodA1m8kw0BTX2EGaVBvA3UAJ_YM74Ad2zJ-M128tIABXCuNWSrLw15ITIiyKhrkvsw5JyRHn2MeckzXiiN_XiimI0khaj6na8N7apudrkcPi-c_yp7vA-a6VB__jC6G9oY26rPfc-XeAC5SZsKttalQISkM9NODzqYlqY_-t01Wl79fMUrW32vWB-kbNqBYF30VYleBsg2Og0gOi1mAA_odIWUh9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=rmW5Kxj0-KifOUxG7snOBlnLotNm3h5viijv93tD9hqI1ddwrrN7kwJ9BT82FImN5YNGJ6ntYeQI6em94hZtOm9xh4rRUyxuZS5IpwPxAOOkxt7OvMh6w3bBiYT07A9y7FEugUu7G91bcE27PCzYTw3Pbpp0P4Cl9Zbwo8DM3xPDRqzwLxs_7DaoJ6XPIMaRXQyBlPL18Ab1Q34EqxhM_-OPFwNjJap6Nf61Dr2T8C8-dHofcFb6ZmEX-F0gTipU4aV_oyCAisaDJwTmyyvJo91Dcbbav7ddkEcsz7KvRD-fGY6VovGQX-j5HsKlZhRk3JHlMM6BDRgcApz3YWN2nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=rmW5Kxj0-KifOUxG7snOBlnLotNm3h5viijv93tD9hqI1ddwrrN7kwJ9BT82FImN5YNGJ6ntYeQI6em94hZtOm9xh4rRUyxuZS5IpwPxAOOkxt7OvMh6w3bBiYT07A9y7FEugUu7G91bcE27PCzYTw3Pbpp0P4Cl9Zbwo8DM3xPDRqzwLxs_7DaoJ6XPIMaRXQyBlPL18Ab1Q34EqxhM_-OPFwNjJap6Nf61Dr2T8C8-dHofcFb6ZmEX-F0gTipU4aV_oyCAisaDJwTmyyvJo91Dcbbav7ddkEcsz7KvRD-fGY6VovGQX-j5HsKlZhRk3JHlMM6BDRgcApz3YWN2nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=pIImJujXE7bf1pr4IW-7jN4_Vqo2pNqUXizru2vsWIbgTI4tJShpNP0xYFgNimgk27Uuyekl9tV-jJmdRx5rYNaQIZcx-17WPuWM1gBenpYov1UyWB2Z-nuE10yTw_faW2zMarS3M-xPEh4klrkNF-kAeVDyxXI1JEcvCDZU0EYM_UfOhb59xr3E5ZaHZh-vsAWjcmxrs-EIu5kzvK6mJ07ZW6McrYpy5Hn4f6P8iBz_X8M5xjxzTo9g4F54QyThgmTCFumaFsrNqvQtIe8DcDQclzzFpQo8CeBt1PrWPkk4Y8O95FPmfKlde8NZcbixK4gPENd20c6WvBgUyyEnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=pIImJujXE7bf1pr4IW-7jN4_Vqo2pNqUXizru2vsWIbgTI4tJShpNP0xYFgNimgk27Uuyekl9tV-jJmdRx5rYNaQIZcx-17WPuWM1gBenpYov1UyWB2Z-nuE10yTw_faW2zMarS3M-xPEh4klrkNF-kAeVDyxXI1JEcvCDZU0EYM_UfOhb59xr3E5ZaHZh-vsAWjcmxrs-EIu5kzvK6mJ07ZW6McrYpy5Hn4f6P8iBz_X8M5xjxzTo9g4F54QyThgmTCFumaFsrNqvQtIe8DcDQclzzFpQo8CeBt1PrWPkk4Y8O95FPmfKlde8NZcbixK4gPENd20c6WvBgUyyEnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=anYWiKEJjEUrmlmWt6jheVt04tiz0dQuKeF9YksScdpFu9AuOsOH9waei-KO0ADRW_SAhncJL1mrlsB5PCbDaSSO6jUegSbssfdyQO83m574IeVM31bExVl7c8ORlJ4WogMNpqCXXj39UeSBq-JIGnvD6DB1K11sVp7vrwPhxKzTzbc8oeOiz9BJK0OYNSO-BwdLw4qLNFtSyX2zK0pMBZav48-Zp9FHbpN7yxjvIcUnBH6a-eBqJKXbARdDBjZfYRFUCdbpQBAe48GF6yuJjZcrz3l7oGTLXVXQ84vbnglvnC6DtRXxPnjL8ERBJtlnRQAKgIrc3UpbEYNmKR2-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=anYWiKEJjEUrmlmWt6jheVt04tiz0dQuKeF9YksScdpFu9AuOsOH9waei-KO0ADRW_SAhncJL1mrlsB5PCbDaSSO6jUegSbssfdyQO83m574IeVM31bExVl7c8ORlJ4WogMNpqCXXj39UeSBq-JIGnvD6DB1K11sVp7vrwPhxKzTzbc8oeOiz9BJK0OYNSO-BwdLw4qLNFtSyX2zK0pMBZav48-Zp9FHbpN7yxjvIcUnBH6a-eBqJKXbARdDBjZfYRFUCdbpQBAe48GF6yuJjZcrz3l7oGTLXVXQ84vbnglvnC6DtRXxPnjL8ERBJtlnRQAKgIrc3UpbEYNmKR2-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJZ9GPmuq6uBw5lxWkP_CjGkssOIjxgZ7wUrV68pxs7UgXCYbRBvz2oApxTywsdArDtxDiNDMh5KOGlbXmnESORQp6xxnTIePfoHO5P5Dv3gVIYQCUfjl-sHNGLYiqMlm5WvKGIe-ksSHmRV3FayDZf6ypCSFoBS2DqHhfZzZztBO0EtOsEe_2-AdU6YwwOCcjpztLjqI--tqCyCJ_k5sxHOEnqXU_Q8YS7HFggMtZpwyLjVFhKXxL-WtlsxDHw1TSCQuCms8Lepqv7NnjdpLtUXwQUSYw1-diCqxG81pWixA1SpGBH7QeJ-CSchXfnol_WgcX5OfP-mOw35L6rRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=JoCx4a0q1wPT_w_juxgdiC4JZoIFYM6VYdGT-Jrl_POpZHqo11gUbEpzOn9KJRa8GvNGCvcNHvGviI_7dyqZTjtZGs0DUlnAyGsP8no3eq8mE_w6Y8Wv4nXRRV6b5x0MJFFjvquO7JKKPTdfYOsAPVfnlETozUXXGnT0cUhPtzqvC30ixiZ3R_QRB6EGtMCAQg07CKhcvVtibFdeLDxBDjoCp0oaEJ2cProu4TR8CHKbs5zNplW75yRe0lN8ycSDGsPYkSNQzjLrjIN_2qlqaH7kr2dZpv2aumq9xSsWku8lY6JQrWxgEbKXK5t7yjQmmOrgq4xfZ16VIzBpu6ikSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=JoCx4a0q1wPT_w_juxgdiC4JZoIFYM6VYdGT-Jrl_POpZHqo11gUbEpzOn9KJRa8GvNGCvcNHvGviI_7dyqZTjtZGs0DUlnAyGsP8no3eq8mE_w6Y8Wv4nXRRV6b5x0MJFFjvquO7JKKPTdfYOsAPVfnlETozUXXGnT0cUhPtzqvC30ixiZ3R_QRB6EGtMCAQg07CKhcvVtibFdeLDxBDjoCp0oaEJ2cProu4TR8CHKbs5zNplW75yRe0lN8ycSDGsPYkSNQzjLrjIN_2qlqaH7kr2dZpv2aumq9xSsWku8lY6JQrWxgEbKXK5t7yjQmmOrgq4xfZ16VIzBpu6ikSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehvtVRjFqNl4JE1XJluZe3mwPLmCCMKxXpEhaNTHOu6Q9zI7PpcBYUtZdqRdN0E_TvLjGlLyF1m-IKx3CnXob7-RQOuV47AMyWIyQMxSkGtf_mb6ZesUMSP9Ay1P5wL-aFMHGtZ4FKj7OJdMpYLpZ8cnuVmcYGG9HcKl8YawiwWQ1x0RTbHo8A8gI9z67tdm6TdauTiSU1v7x28bo69Yq7jo3zBB_IfshP6bhLa8IKLtm6b7w7mAtit986v7emOCTBYNS53_QerCcZaH_wsK8TIcDcqmGtlQEjbhUBR70GA5YoEHalI2MuUpja26S4AZRldKBsb_E5VkHMpmM1Z_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBAUHrCQ0li_r7KI_eJklpUkyGZ1Ob4F5L22GKSM1EsiW7MLwBeqQ4Ehz-Q-nQyaRXGPTkqCevZss1cLFWMVOeS5FQkdpDunGJpH5_AFVxibZ0n7HZ4NSy46pW4WHQ6DaLzjwFLljo1VkdCWkP5LsczUrXfNF4DHF04kafTCQgCwltIN5d-8PgqmNugU2eIusgYY9mW1hx2pajEm7XMkynw0PY0BCJrhVkweuGwOGKv_q9PG7uRZ6tkmV2gtKFWp9sPZOLoTotYehwRvWmO2eWgVF89dR2gFvF33xqcP-eVU0QC-f5w-RBNTMfayKFDRAYSsFNsVo6_pf4b_3YyAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Nm2Vnz-pbN9psk9bjR-39VXROMs7Lxxqnt4NDfLVZJyRVqC6xYZbs_NnTSb2m5scfF6a9pNHFsiu_UXi4hDrxyTcwhB-NsTMojn7fTfNoJugZ1UlgdfRuy18jK0B1J9ghIoUyJ22MC9astMX0vQuTpVja5yXigh2BFLm1mDaideHrmGbnBAibXsSeZUP2VtOA40arHL_L9pNx6W7Nerl3AwKG2T-Y7it2N067xHTvq1ZMH9CRIxVkg-2ZwOKinWITw-NQDoaieIwtCP9skUg5EQ_yt7it6adhytb0z9cqNWQusuJf-2eHeBabAxxnuTpEmG1wJXUVThenGU1lt51kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Nm2Vnz-pbN9psk9bjR-39VXROMs7Lxxqnt4NDfLVZJyRVqC6xYZbs_NnTSb2m5scfF6a9pNHFsiu_UXi4hDrxyTcwhB-NsTMojn7fTfNoJugZ1UlgdfRuy18jK0B1J9ghIoUyJ22MC9astMX0vQuTpVja5yXigh2BFLm1mDaideHrmGbnBAibXsSeZUP2VtOA40arHL_L9pNx6W7Nerl3AwKG2T-Y7it2N067xHTvq1ZMH9CRIxVkg-2ZwOKinWITw-NQDoaieIwtCP9skUg5EQ_yt7it6adhytb0z9cqNWQusuJf-2eHeBabAxxnuTpEmG1wJXUVThenGU1lt51kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=gcPFh3Y_rm4jLEC8meTCgr5hYXm41iOcHONsflEnDvpmERJi4HS9wk626I41RxsSv2-RuD3roSWZTY9wjEM_iv04C0FGIbmzJcYym-KBlFe0hnTi9s74PzOh_Rzwoejf9CJNViBhH8eE3XaJ3AOnvYInhLaXdpZpaae2TVRdYthutuFqcq4fKQx9Xc0DnI15haestssWM3eK3cSm07h9NOJ-YRWW4lQ7ZmH-nm7qFqVioqcQhISo_iHE9raYCCntWCOXexWRkKW_PsoydM_M4-PBqJB7bA1lxX2EH-p1tHoWwlMsQeFVwMeJeFezHdjyEcBvSA-6xpjKF8-pkzN2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=gcPFh3Y_rm4jLEC8meTCgr5hYXm41iOcHONsflEnDvpmERJi4HS9wk626I41RxsSv2-RuD3roSWZTY9wjEM_iv04C0FGIbmzJcYym-KBlFe0hnTi9s74PzOh_Rzwoejf9CJNViBhH8eE3XaJ3AOnvYInhLaXdpZpaae2TVRdYthutuFqcq4fKQx9Xc0DnI15haestssWM3eK3cSm07h9NOJ-YRWW4lQ7ZmH-nm7qFqVioqcQhISo_iHE9raYCCntWCOXexWRkKW_PsoydM_M4-PBqJB7bA1lxX2EH-p1tHoWwlMsQeFVwMeJeFezHdjyEcBvSA-6xpjKF8-pkzN2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=EQOIbziqsPZVdlrPG-66g6UkAPTfQ2c_TGkAi2J8dVkXSQ_Y5CHgxJsrhOebFk4N2cuGLtjlPG-1VzyW8af3r8_Q3CtFEgeJsPwfkCVNQq3Mj_lwD62zRLU3zAfeRG2j4kqsmFsMVmALCU-TVJdW8R_q9yHhVf54FnqrBn0Gv7N9-8mAZD2QlnisaZ1fNJnvDe3WLDdBsAsfXpArEy4qe8CEvbRZOl161g-VO-FJNENiF8lbUmY_6A-6yXluEmoyPuHfTQA2nEOGf0a6PKedj9xkCJwGQId6UZZ8MQnOEMY9WLiuyihRuMQcqf6_Q4GDxoGemTZxfBITtJtKNVCncA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=EQOIbziqsPZVdlrPG-66g6UkAPTfQ2c_TGkAi2J8dVkXSQ_Y5CHgxJsrhOebFk4N2cuGLtjlPG-1VzyW8af3r8_Q3CtFEgeJsPwfkCVNQq3Mj_lwD62zRLU3zAfeRG2j4kqsmFsMVmALCU-TVJdW8R_q9yHhVf54FnqrBn0Gv7N9-8mAZD2QlnisaZ1fNJnvDe3WLDdBsAsfXpArEy4qe8CEvbRZOl161g-VO-FJNENiF8lbUmY_6A-6yXluEmoyPuHfTQA2nEOGf0a6PKedj9xkCJwGQId6UZZ8MQnOEMY9WLiuyihRuMQcqf6_Q4GDxoGemTZxfBITtJtKNVCncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=Vfqz990bZiwMe6ULGQX1qDHp0qJIzP0sog9kBgrN8Vaa2kLxnX0S8FIzlxdc6bF8dogd-LrIs-uGqXg9WgpC4mIUssvXYtKvesZ05mS-K85QRg1cYqPxZOkjhh-I1vyQnc8K8nvhKVFXzb05TAB8IVpRb68rr5G6l_GFJnh800Ya0Q6nEYyXHcQcq8kDZiIlrHaNtplubZw9vsXEWPiJF4YjpRCPA4YWnhsdQt9zD1igOIk5hs-5At-ZjSBgrVTgEOPPFnUS7WI20SoX_88p7lzjwADcI4ExXiQA40saP5MKBHTm4-9fyDIfHfrPJkBzKulnXCWDm2Gmv1UcebG2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=Vfqz990bZiwMe6ULGQX1qDHp0qJIzP0sog9kBgrN8Vaa2kLxnX0S8FIzlxdc6bF8dogd-LrIs-uGqXg9WgpC4mIUssvXYtKvesZ05mS-K85QRg1cYqPxZOkjhh-I1vyQnc8K8nvhKVFXzb05TAB8IVpRb68rr5G6l_GFJnh800Ya0Q6nEYyXHcQcq8kDZiIlrHaNtplubZw9vsXEWPiJF4YjpRCPA4YWnhsdQt9zD1igOIk5hs-5At-ZjSBgrVTgEOPPFnUS7WI20SoX_88p7lzjwADcI4ExXiQA40saP5MKBHTm4-9fyDIfHfrPJkBzKulnXCWDm2Gmv1UcebG2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=kDK12GpoW3JBuTTA0fCaAGqhkF5C8hyjlMVAuLkfYPX9av8Y1Zsc7qdJ5SaKjIDI2qskRhU-1YT5jyoxrwNv7kH8w-e_LziKvoq1X7WECYDxiKsBf8wBQ5hdhfVq8PLpENeBydoxRf6pIjFcBT3kll2R1TYFvp7fY47iqopLkQ5Fxah-RO5j7hIyyD0lLsRb6L2AKAWEZc9h8y_rYC0Zwr3C1anE0RQN4U12vtem_WI392rr6l128Bn-X0VM-JUkbBc6-D6478RSA_WSvsqkjQU9RBQbhdqhha01zWNdlkDWneByY2BnZMf2-xD8IAqklJ9uPasZku23Boq3VV52Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=kDK12GpoW3JBuTTA0fCaAGqhkF5C8hyjlMVAuLkfYPX9av8Y1Zsc7qdJ5SaKjIDI2qskRhU-1YT5jyoxrwNv7kH8w-e_LziKvoq1X7WECYDxiKsBf8wBQ5hdhfVq8PLpENeBydoxRf6pIjFcBT3kll2R1TYFvp7fY47iqopLkQ5Fxah-RO5j7hIyyD0lLsRb6L2AKAWEZc9h8y_rYC0Zwr3C1anE0RQN4U12vtem_WI392rr6l128Bn-X0VM-JUkbBc6-D6478RSA_WSvsqkjQU9RBQbhdqhha01zWNdlkDWneByY2BnZMf2-xD8IAqklJ9uPasZku23Boq3VV52Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=a_ZgF_-ayeBl67a-SlzqAbgzAdn6peN7CJNGMKMCMWwW_moLLICZGzxp1uEuETTvDXPaVfVA4u2m8caihJ01w_3eAp1G-DRtO4D0wDzPaxC1GAPxtrnohI6Byql9cbLzVMNrl--NgbmI2nbi77aPUnqORhIh2dAuLGbZzDwakynOO5tvMyA5xZLUSwulOgbShDUOL1dNM-q1uNED8Zd3tRxuhtDQjd3-6kYojQQKPHnoV_QOAaoHZUdvJ66K6HU-CKf3rmsqlKtOiK0rOMtqkIGpYUW30zjJ76D1hiFSz3L6z7KH8SUUW801syeBMoYy04_FXoxIXJSdYt0mWhyogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=a_ZgF_-ayeBl67a-SlzqAbgzAdn6peN7CJNGMKMCMWwW_moLLICZGzxp1uEuETTvDXPaVfVA4u2m8caihJ01w_3eAp1G-DRtO4D0wDzPaxC1GAPxtrnohI6Byql9cbLzVMNrl--NgbmI2nbi77aPUnqORhIh2dAuLGbZzDwakynOO5tvMyA5xZLUSwulOgbShDUOL1dNM-q1uNED8Zd3tRxuhtDQjd3-6kYojQQKPHnoV_QOAaoHZUdvJ66K6HU-CKf3rmsqlKtOiK0rOMtqkIGpYUW30zjJ76D1hiFSz3L6z7KH8SUUW801syeBMoYy04_FXoxIXJSdYt0mWhyogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtWzYFjQixXaBcOdm-amysyIj90FD5zfgSgEmDHXhS5Yx8YjjdY812G4LuOfHMNAGhq2XQUVK4rVpqn3P5zRbqVV5BGm4xcT3Kdgd3i54KxqXFtqQyf8EWPwSPmZCY9izGV1xNMzC579r48_-U8fpbx1h_zexuYpd6GjxhmBGdr8BV7dbXmO3bT4keZnT-lzHXO5O8DrZMSzfU3yUfS8BRSVFMgcBgLp_HiG4Qo2d7N0BTK-CKSc7QzR6FMxM-zj9xSran5x48RWrFwe3wknGV6s2hqmpv1EmxLeEYbisjFtQ-E15CASWzY7ObNjkWT4jdWpRG_6GVmkndMyVQsVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=aEc4eVffb1UwWXMMsCoMLj7k2vib0oH2oPPEWvgMRODs2hA2KUnWijwxnCmp-Mubd8FuZNL8LGoVL9qUrC3E3Du8u5Utdx9syUWqNLTKVtsgogFVCXh2b0WzbphlF1YCd7pcqBaFDqbspPOVlm4ClvWmFwoHCGr6IcrjcHY55Y_SVxdJbD0GK9PmsJFdEdqZ-iFrLI39b-1UYKewJz_6bFHKRvvf7SlBbPdsDj1bUsVAKuwIJX5WLW7NTcMUucNkmLNGWyU6hMntR4e6Q_gi24QgsXRbRfe36SSghHjBWOGoFg1Whk3d5SaNMVJf6FQYcKDhAeF0ABbBRjjeZsh7kItNaSmfeeK4ElhBipcO_DmQyX0kD8kWPV6dbLGXQ6gPnUf8JZEd9I1QppKR64JcJT6ImnFF_Uf7FC9XM4OpHGKEEQCHVTuI9PdKLunus4psoLfGr0K5caMdT65RXQRDmHGRjLyUXwqp2GJhRjxSV6_Z9XFUFJmVqfuACFjDe4MegsYWwx72fTFZAp33RgBRXb8zke5eXGjtteVCtyf2YGUSWiJyIyNy0LdxZqWAKE0q0C_wC1Rb71stES324fdQInRbQ0QfoQEEbK1RvpGlxl-pO4wglck1PcKF_nwIjmvdm6LWyMopxWkDDgBmu5zOj-DO8sODgQBxYcNy2cznNG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=aEc4eVffb1UwWXMMsCoMLj7k2vib0oH2oPPEWvgMRODs2hA2KUnWijwxnCmp-Mubd8FuZNL8LGoVL9qUrC3E3Du8u5Utdx9syUWqNLTKVtsgogFVCXh2b0WzbphlF1YCd7pcqBaFDqbspPOVlm4ClvWmFwoHCGr6IcrjcHY55Y_SVxdJbD0GK9PmsJFdEdqZ-iFrLI39b-1UYKewJz_6bFHKRvvf7SlBbPdsDj1bUsVAKuwIJX5WLW7NTcMUucNkmLNGWyU6hMntR4e6Q_gi24QgsXRbRfe36SSghHjBWOGoFg1Whk3d5SaNMVJf6FQYcKDhAeF0ABbBRjjeZsh7kItNaSmfeeK4ElhBipcO_DmQyX0kD8kWPV6dbLGXQ6gPnUf8JZEd9I1QppKR64JcJT6ImnFF_Uf7FC9XM4OpHGKEEQCHVTuI9PdKLunus4psoLfGr0K5caMdT65RXQRDmHGRjLyUXwqp2GJhRjxSV6_Z9XFUFJmVqfuACFjDe4MegsYWwx72fTFZAp33RgBRXb8zke5eXGjtteVCtyf2YGUSWiJyIyNy0LdxZqWAKE0q0C_wC1Rb71stES324fdQInRbQ0QfoQEEbK1RvpGlxl-pO4wglck1PcKF_nwIjmvdm6LWyMopxWkDDgBmu5zOj-DO8sODgQBxYcNy2cznNG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Vivl4PYWvjdlFoxrN-uIPSqC2dKSup3R3SvesmaSiZSNhZgxHUpPMO3O454F_LiFhrLawBGt4rPpgVsmTrpiTYzc0CGTtHuE-TWF-UR4vpTsV5I38hnaXd4ylTpRqrKvhwIQTlFnTOrg-P99WS4ACvLu8STUOeDhtK_tURteXqlN3yR9RG1NysimjoZtAH4OEMQCuYtGXVbfjWzJYW-3GS8mukHNak2oopNSPDRvs9jSUnp4B0iN5afxQIAslMS9Web27zbHg8ku2pBVbbfSAAUHvOFPsJrQDRcO7t9T46SLLjuBaaRFPafLFte12jYzTCteMR59fY06CqBxnfGs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Vivl4PYWvjdlFoxrN-uIPSqC2dKSup3R3SvesmaSiZSNhZgxHUpPMO3O454F_LiFhrLawBGt4rPpgVsmTrpiTYzc0CGTtHuE-TWF-UR4vpTsV5I38hnaXd4ylTpRqrKvhwIQTlFnTOrg-P99WS4ACvLu8STUOeDhtK_tURteXqlN3yR9RG1NysimjoZtAH4OEMQCuYtGXVbfjWzJYW-3GS8mukHNak2oopNSPDRvs9jSUnp4B0iN5afxQIAslMS9Web27zbHg8ku2pBVbbfSAAUHvOFPsJrQDRcO7t9T46SLLjuBaaRFPafLFte12jYzTCteMR59fY06CqBxnfGs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=itJcgoVvJLe7IcQnBD249lw1m45adMn7c1MbScQrV1YZZ6Omn34oEZQLH4txp1PYKNxUN7eMFvPyjaDNZ-xzblNljgMcuOm_DgEfkdLyZ0wuaR5-T6s1dcqvEahM5Nm3qLuofoYAwNBAZeKfu8aCFInd4RzIahMpX_gWzDYzt2xzXCEsnGtFbFvxm7e124RcR8k9nW41lw8KHMa4yMePufgPIv1r9eHYpKXH-Df2rEd76dluz1FnDXHFRZHWYVZQDC3M2L7mhhh35M0VYUgVwPHyFMkEHfS7JbgXJFaEvxUbqMSIEGRqiAfxLVRlc3HfU_pS7GaHs5swHkqfGXL3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=itJcgoVvJLe7IcQnBD249lw1m45adMn7c1MbScQrV1YZZ6Omn34oEZQLH4txp1PYKNxUN7eMFvPyjaDNZ-xzblNljgMcuOm_DgEfkdLyZ0wuaR5-T6s1dcqvEahM5Nm3qLuofoYAwNBAZeKfu8aCFInd4RzIahMpX_gWzDYzt2xzXCEsnGtFbFvxm7e124RcR8k9nW41lw8KHMa4yMePufgPIv1r9eHYpKXH-Df2rEd76dluz1FnDXHFRZHWYVZQDC3M2L7mhhh35M0VYUgVwPHyFMkEHfS7JbgXJFaEvxUbqMSIEGRqiAfxLVRlc3HfU_pS7GaHs5swHkqfGXL3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=Rvbkdrd-FgXT81OhZI6IxhUEEwAeOprS6j-fNLoC1sw34L4bZBSw8wIoEH-0TFMdbA_mA7r84NtxBjSa4b7wnHQ361hvf9dEh70qSk2JvHZXZm0sS77DK7UamdR9SH3N9x-40VVnkFtx2WcPum9XdEOd-J9c-s2g40tVnbye6g5Xx78hugJjJQJFyN-8on6OksQQ5ypJtldW09m1k1gKsa2VINr6zrbGEaTd9ixG7S8naoAsMFhD8cvFcG8S8M8vJaTF0E0s2yN0oSkci6HKlH0eMY4Z3g6VS9GgGrDFfIhRxuZqRWVcfDpft-et9lwC0PpQufgIgFgLyMm72GOiTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=Rvbkdrd-FgXT81OhZI6IxhUEEwAeOprS6j-fNLoC1sw34L4bZBSw8wIoEH-0TFMdbA_mA7r84NtxBjSa4b7wnHQ361hvf9dEh70qSk2JvHZXZm0sS77DK7UamdR9SH3N9x-40VVnkFtx2WcPum9XdEOd-J9c-s2g40tVnbye6g5Xx78hugJjJQJFyN-8on6OksQQ5ypJtldW09m1k1gKsa2VINr6zrbGEaTd9ixG7S8naoAsMFhD8cvFcG8S8M8vJaTF0E0s2yN0oSkci6HKlH0eMY4Z3g6VS9GgGrDFfIhRxuZqRWVcfDpft-et9lwC0PpQufgIgFgLyMm72GOiTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=Oy8N9MnT1miYc_B9-jgwxvWM1LTX0QMXTU_ZbsQzCUMdT1hZdXp-5DZ_bD2ZmHNj2nlz98cTvWb2LX_ZSB3zX_YRdQgEK_UKxrzMxvOzUqmk33Eu7YL_QHAKsqrgp-7jkEtkrXjnvIOY8wo5jgf-3lmS_9VHI75f-wIbdb5GBV-Ekfz-G8qanLcEzOnKJj2-IsNi6u7cX6xJjwc5R73J3VhRwq41A7exFippyE2hfEojMPTAleLb34bTwDq9ZVw8zf-yELzk3lO49RhO87m1Ds-rVjfZGuhH_y6DlEkTPMTJbERMTNVUZ0zZH7bt-eq5PQ0Aib0Fu1m7dJcvtOYcPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=Oy8N9MnT1miYc_B9-jgwxvWM1LTX0QMXTU_ZbsQzCUMdT1hZdXp-5DZ_bD2ZmHNj2nlz98cTvWb2LX_ZSB3zX_YRdQgEK_UKxrzMxvOzUqmk33Eu7YL_QHAKsqrgp-7jkEtkrXjnvIOY8wo5jgf-3lmS_9VHI75f-wIbdb5GBV-Ekfz-G8qanLcEzOnKJj2-IsNi6u7cX6xJjwc5R73J3VhRwq41A7exFippyE2hfEojMPTAleLb34bTwDq9ZVw8zf-yELzk3lO49RhO87m1Ds-rVjfZGuhH_y6DlEkTPMTJbERMTNVUZ0zZH7bt-eq5PQ0Aib0Fu1m7dJcvtOYcPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=HpFWDJPehXxg2ILZOlOnoepWCaN4eVg-IR-L1iAnVLXmlLnyX9DJqRrgcyKmQSmoE19d5hPhqjNhk2StoF6VMQomyw6HCs5UG40cApWlhdoD6uuAlEURse-POaXUD3XSQ9aq19ojKTUx_Sp0B6w2itMMB7Xyc9z5gAl5_D2UfU6Sz-oN7opyWXLelBOGMH4KgenvsbicVzBWd6hUT7ZEufW87wZZAv2wVRZm0N9qtGbhyhW5_fKo2b7X9s-OfMeRnjhUHkkmFFH2zpTb3wJY-RyamVAoR75_bMTVKvAepywTwQ426d3CrkPi338-Jal_NjgMd9yqYVeK7RHkbGiTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=HpFWDJPehXxg2ILZOlOnoepWCaN4eVg-IR-L1iAnVLXmlLnyX9DJqRrgcyKmQSmoE19d5hPhqjNhk2StoF6VMQomyw6HCs5UG40cApWlhdoD6uuAlEURse-POaXUD3XSQ9aq19ojKTUx_Sp0B6w2itMMB7Xyc9z5gAl5_D2UfU6Sz-oN7opyWXLelBOGMH4KgenvsbicVzBWd6hUT7ZEufW87wZZAv2wVRZm0N9qtGbhyhW5_fKo2b7X9s-OfMeRnjhUHkkmFFH2zpTb3wJY-RyamVAoR75_bMTVKvAepywTwQ426d3CrkPi338-Jal_NjgMd9yqYVeK7RHkbGiTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=j7IBMzaxookbVromSkaJdUgbQGGz6rE_boURAP_1KoY0gwEl02ZoyYFCKsYIQP8NARZxmS0CTzeUXkcbvTgHH6CVqxLTaVOOJ9jwWwyBVTTvDCUx7cicIh40n9bzOAaSyj8RbhRwQC4kEfNgx0iv5PdAkzotgwc8hUS4n2l-cjr6gvhJo89W7UU5hpaGk_FWtxk_ymJiF6RZxQosRXKpn3vfFX_1T-G9KRi97mqCTM5hjf9NJRw6XBcL1Fvogb60HEkPE2pL09LaIP5PqKajeLeoHa8TCYpd8cLVrIkXpH-Gx20rkxaL2o6DWoCcMp-DBqaUYUkCtKBBSk0fnBRAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=j7IBMzaxookbVromSkaJdUgbQGGz6rE_boURAP_1KoY0gwEl02ZoyYFCKsYIQP8NARZxmS0CTzeUXkcbvTgHH6CVqxLTaVOOJ9jwWwyBVTTvDCUx7cicIh40n9bzOAaSyj8RbhRwQC4kEfNgx0iv5PdAkzotgwc8hUS4n2l-cjr6gvhJo89W7UU5hpaGk_FWtxk_ymJiF6RZxQosRXKpn3vfFX_1T-G9KRi97mqCTM5hjf9NJRw6XBcL1Fvogb60HEkPE2pL09LaIP5PqKajeLeoHa8TCYpd8cLVrIkXpH-Gx20rkxaL2o6DWoCcMp-DBqaUYUkCtKBBSk0fnBRAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=PwLb5npR9GHMuTRbq-a17n9xi0AYZdg9clzEpZyDiSYYT-RNUUyyF_PntsbwCPmz7m1zHSRt3NNrDwEWSfCDdLQ4QLEDrJGDljd3wiIMZh5TCD5a-z9vMkhpbGwUc1nJknZONEi4U-QAKnQ0mNNgqqFym7eYKMwJmWqg6kOyhdmlihiPK9A1GBON3x0buc-0hHkv33mTgyT7OIlCwVmFF1b9-EpNRhIgWby_zFTKm_o86dmgHe2zI-O-ZLNFOb33ag_6Go2r_kcjpIbQ7l1_DCBwQlWuV5IdP-wGsnpg68xYrGnfyVrebiaf55YGWb2Me6ci1ITWJdio-zmta1aVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=PwLb5npR9GHMuTRbq-a17n9xi0AYZdg9clzEpZyDiSYYT-RNUUyyF_PntsbwCPmz7m1zHSRt3NNrDwEWSfCDdLQ4QLEDrJGDljd3wiIMZh5TCD5a-z9vMkhpbGwUc1nJknZONEi4U-QAKnQ0mNNgqqFym7eYKMwJmWqg6kOyhdmlihiPK9A1GBON3x0buc-0hHkv33mTgyT7OIlCwVmFF1b9-EpNRhIgWby_zFTKm_o86dmgHe2zI-O-ZLNFOb33ag_6Go2r_kcjpIbQ7l1_DCBwQlWuV5IdP-wGsnpg68xYrGnfyVrebiaf55YGWb2Me6ci1ITWJdio-zmta1aVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=K_xiyWzA4uy3ty9Zw23RJaGJXN8wvNORR9OVT6UAOOxjO0BnQjJecwDpN5RopTpwbqqlz9toUu7bkbZmIXGsmBz-yXZYLE571aHIP8u2i5jjfXNUSqnYpuvPtKlmOynwh0UYKNRKr2ld8KL5vGy3tzZ1D-0LQyx9NwoFkVpr2gPH-sCsroAAvx2Xs-MW38CAgfKFeSVIheMaInwi-NScQqQEAq5w6wUuIYdtOiCEEY4bJl9SBplNEGduP8cBDqMhekIapaAizi2UKlo6gzR0CTm6JsI10Wf2kgPAUtGdHrs09VogHElr35ImVsVq6BjZpnzGUcI9C0bDa_bFmydj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=K_xiyWzA4uy3ty9Zw23RJaGJXN8wvNORR9OVT6UAOOxjO0BnQjJecwDpN5RopTpwbqqlz9toUu7bkbZmIXGsmBz-yXZYLE571aHIP8u2i5jjfXNUSqnYpuvPtKlmOynwh0UYKNRKr2ld8KL5vGy3tzZ1D-0LQyx9NwoFkVpr2gPH-sCsroAAvx2Xs-MW38CAgfKFeSVIheMaInwi-NScQqQEAq5w6wUuIYdtOiCEEY4bJl9SBplNEGduP8cBDqMhekIapaAizi2UKlo6gzR0CTm6JsI10Wf2kgPAUtGdHrs09VogHElr35ImVsVq6BjZpnzGUcI9C0bDa_bFmydj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=WGvG2xtfroASPdMUUN0Z01Gu09y_TpVc75BkeB_VAKp_w_8ANaNasC--5r2TjATZsaHGTlB9-eHCOaz5vOHrRCbP6uClian4qa4edEeQrnxk5Cuz_wMDSBF7H0uv1mo3KUI8P4g_Lh9mFpXDesjCyFzPbmw1cxllF_2Uhmy-Nn5s6fPvy9KPs98Y1Z0ve9Oh6yKwpaArjqOtM_QgBVEUjU4F5dw9SGfbK4Vf8GL6KgVqD8jQUzsSWe5CvtGn8mTY6KVdHUTb5dMcYO0he08mozkDxuFh-BKNRk5nMSn07H0pAlv9FPmfwQgPjJLjvRBcTZEGURGX_h3tXl7wT4_jLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=WGvG2xtfroASPdMUUN0Z01Gu09y_TpVc75BkeB_VAKp_w_8ANaNasC--5r2TjATZsaHGTlB9-eHCOaz5vOHrRCbP6uClian4qa4edEeQrnxk5Cuz_wMDSBF7H0uv1mo3KUI8P4g_Lh9mFpXDesjCyFzPbmw1cxllF_2Uhmy-Nn5s6fPvy9KPs98Y1Z0ve9Oh6yKwpaArjqOtM_QgBVEUjU4F5dw9SGfbK4Vf8GL6KgVqD8jQUzsSWe5CvtGn8mTY6KVdHUTb5dMcYO0he08mozkDxuFh-BKNRk5nMSn07H0pAlv9FPmfwQgPjJLjvRBcTZEGURGX_h3tXl7wT4_jLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj3s0RivEcfG-Qqza-VFbbHAuPpzGeslvXEUCfgK2thQej3BSgPwT_iU9wSzOnK_TT49XuSIJUbLqj21YiazIjekAgpFGe056k1Iof1r1qfXYKRIrHabvDW5N7yo4YI9PvI3H8XKIvTdlRrcZ8m0wxz9S4qbIRrj946B15NH59P_Nj1aZA1Ya6RkdmMd0K8jr0H3_C7boEFLA_ms9aBKR1Urubp5oyJGLMJG-9A7wTHDlL_A2io49_rAaUVL1dRA-HdZM-sNnRWdtC3PadY7QNQf4lAy7o5wf7jG4fAkY_oUMlfuKmBcSQ_0XuPi_Ctfq2qmokh3dZE65I9IRA7cMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijxUlL--FON7WLVVousQG-94_Cdp8NdnkBgRtnimedYLARIkpy9t-9eebfDM03YBNegfNSGEW6gt4-HfMcJkrLYH_wzvm3BL2M1QJDgcRZYXQq1As4rF_C0iF2n3atXQTHyp1sE7MCjTPun3VhoP5Zm0mbWBWp35Jt3jykN7RiHwvpMK7nVIg-tlJtzOAToDJ-28_N9G2PTICZk37bGQfKyc69GHASaqBv4nxFj1bXlaZVWTmSYyqP7mX_MLaOl-pPOFdj2wVfG-ZQpb3O3ZAas3wsrIaJAluPqxxxhZCtanp8RYNWNd9AyLgrBzaH-bZoyU8jdPVQ90tkSg1_5Ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=eMfXJKb0-UI-TNhz0EDPko6VUn2LJCi8QHb0CNv-quebsSJdCZYleolKL-atjF5nUYooFu07qY8gntfi3pyk1FNBK81pol8naq42naerEkRYs8PwnAZZ_Pemqc7hGUcgmbEH--B2w17TXDYJyYKeSX3wWsnI7J-1Ey2IzgE-tfO5kiZD1frSK2kgyq9i4_48rGQDaMeV3OmPMRWqxQ_XErWJgJq2eJDtkMIjAQg3mPCN8-DX_35HnssrcPLavrCZpII-b60qoNKSMPOKZQIZcdUpKXRU-dZEmKJLbnDgFis36O74uEf1ZR_tln7JsBWJxmfmVPwmK-FuTCTUeVngDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=eMfXJKb0-UI-TNhz0EDPko6VUn2LJCi8QHb0CNv-quebsSJdCZYleolKL-atjF5nUYooFu07qY8gntfi3pyk1FNBK81pol8naq42naerEkRYs8PwnAZZ_Pemqc7hGUcgmbEH--B2w17TXDYJyYKeSX3wWsnI7J-1Ey2IzgE-tfO5kiZD1frSK2kgyq9i4_48rGQDaMeV3OmPMRWqxQ_XErWJgJq2eJDtkMIjAQg3mPCN8-DX_35HnssrcPLavrCZpII-b60qoNKSMPOKZQIZcdUpKXRU-dZEmKJLbnDgFis36O74uEf1ZR_tln7JsBWJxmfmVPwmK-FuTCTUeVngDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7FC5xRPu51dqRGhU4ddsqRimGCw_6BYeMBmZnPS9akOF_AotR5_Qj2R38lXvDDhbWs3tfkt2N6Mr86GxXL_bmuLaWjImXqPbhlEghZjS62u1-Pd4tz2LYoTTAIUlr2OosmamrMPTn6_rsRCdye5Vegz58sUGqFT2j8tCnZAz7lkFj2w1S4Ic2cnpxkUdS1zQuV6W6gGTBciIjw10IC68JZNFIkxhT8LT3GG9SBa4KvsezGDehX7FPWsNX9yhgEeIhtUlLeKlHPIQ9YcAo1UEYyyh3Bm_Orot-htdtwllPQ2UOZ1mQCQEzw6JtqaAbmJeVclnCkkgQGGVh-ZVcSUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiTjkArM5RFNKjcJ20EdPH9A-rZsYt62uab4OnXolI8hrcaDB-4vAWTm_PoBpyv4_RKBA32t6C2wtLzpYAeRy19jgXr6w1RnlGuwMN6TR2yeIEhVmJQC1sGt7071F5PqLkGsrD378DORXAQfnYgsfbNiKJBtn8Wnnsq3fPxIGHd5q7lheUVKUzxnkgUtwGbJHe5gUi9EOVobShSjEGiiCyLvrDDG9-9p42fT_sQdZKZ1FNNPA_xrT5UruyQL9inF9jJFwgYL1GvhU00qP1b9O6KN5DPqk0NLl-RYFUcW_M9pvOijcSRlcXusyUxd6OEuzevbhB6BLXVd8ZbeHnE0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY9g8dlIAIiH7WwY7i8Ej76jBvK1uRTkQnUiSKLGgHBaoVoKyftQblA7aLaEwZ2VtrDy9d7rGZy8THKzWE9MCSmV9gvWMvWx3cpNtNxbXZ7hlcWyHAx5RDNdpMKcB83hX2chmYFWv0ZJMKIGExunbJZ90rdblwkMMkOLk_rK5iW2L6FIwTt6rM806dOZAZ0GlmnMYFU3-f-oJun6oWxGmf4pGeab2-V02OPx0maP8mWpCmMQp5d0GclIKewPXr6Om5zLEVvp5yl4rlx3wb6HIza2KmfTsc2Iy6RaXX6EmGB40A7X19Oz47NJdPOy0Py1Q_KP22radl395-p6Y_9Zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=XblDc-xWX6Jz4z2FKXBTkpr3JrNQQIM5vNzsAWndQpuw5HFcRBF2U0xa6JLK_rt5H9ajlgkKONtkN6lLoIfEEsk5Pknz5JbzOEct_UU85g-KMW9N1HxTJZol1SOn-lYIMycNcVAy3DmHCQGi_wJRHT6S0mt8bxOMEL-BUUTPBmT9fIAvAfdaN54K_R_KiZfY32MT7Jrp18XWBDtsxdro6Rri_HiKSR_9dPT_ndrB5Yc0kTpgdiEeBxEQWoyilSd0gp2T_QkkJRzQyBoN47_RzpcGPMcWKt69zqPvg4Y3E-FnjvVDqE-ILC3XI0tIo4Ybg7CAUpLrqMZog956qK4o0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=XblDc-xWX6Jz4z2FKXBTkpr3JrNQQIM5vNzsAWndQpuw5HFcRBF2U0xa6JLK_rt5H9ajlgkKONtkN6lLoIfEEsk5Pknz5JbzOEct_UU85g-KMW9N1HxTJZol1SOn-lYIMycNcVAy3DmHCQGi_wJRHT6S0mt8bxOMEL-BUUTPBmT9fIAvAfdaN54K_R_KiZfY32MT7Jrp18XWBDtsxdro6Rri_HiKSR_9dPT_ndrB5Yc0kTpgdiEeBxEQWoyilSd0gp2T_QkkJRzQyBoN47_RzpcGPMcWKt69zqPvg4Y3E-FnjvVDqE-ILC3XI0tIo4Ybg7CAUpLrqMZog956qK4o0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=o5ZLozkszMg4qalNiv6Bo3aiCxyr8My2TpbS8ptMoAnFnCppoJoAnvORxQnXT7xAL34rB8F7h2ALGgfXg6pi8HEuEU6pExfZM1ZJt6-Men6yXAYrT_JstIhxXSEfoqtXXNGuTXXYFXI8buBEKNgWk-Isks4-tTVeeVzZW84jAwAvzyapnpBntrGZmRS2hEaPH6eRM23HQeClhNOSL9N2CJXTGqqSwmW_5fKjtTZ2bVfoMIcoOaBngOeG8Y53WWGRTv5w9aRnlrodLfqpjBi9wDXnv-0PCf-w9OLVJSTCo_Yg740M4a7rFAS_gqX4iBC5Uta2r3BZmSUZZ5qCf3edmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=o5ZLozkszMg4qalNiv6Bo3aiCxyr8My2TpbS8ptMoAnFnCppoJoAnvORxQnXT7xAL34rB8F7h2ALGgfXg6pi8HEuEU6pExfZM1ZJt6-Men6yXAYrT_JstIhxXSEfoqtXXNGuTXXYFXI8buBEKNgWk-Isks4-tTVeeVzZW84jAwAvzyapnpBntrGZmRS2hEaPH6eRM23HQeClhNOSL9N2CJXTGqqSwmW_5fKjtTZ2bVfoMIcoOaBngOeG8Y53WWGRTv5w9aRnlrodLfqpjBi9wDXnv-0PCf-w9OLVJSTCo_Yg740M4a7rFAS_gqX4iBC5Uta2r3BZmSUZZ5qCf3edmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=XW_0oNja2WTyxn7kqWzBYZsXMADbQxC9f_nWahr829oKnTnLFbYWRYOrU70UE-z65kA15CBCJuwSclN70If9wwC1_EP7jpE9JJHILKVSKKY6nlVYUoLnaU5rCC3ADgRTmfF9Jk0-CkdXeCmWjuBR7XzeS-pYUcYzBUeR_8qcPa9arFKh71xJ90hbtbjK773CRCWw5BlZGg0R27uENvEFUvQxAXlGKW-VvzGoyG84W46FPSV8v1IS380hhbCjBeBDSqPtQU45Q_5BCOoY9WCleirQpAQYxtZFpKClaYRHB0omLOlu5hDVqWKypUCZgBExSqW-TlbIuHpUqFbdpjabSL-ma-Lxp8-fpiQunDBvyFV697dig5aAGw4Fr0tYlup5e_JLpIEVMZ5_bsjI3KMhuxP4nyONstnT9w-SrVhYnCnlMOGz-ojB-fLIiMEVNScVAUAK1t2rCIlqX73OJ3X6RhrViiAHPKvSCfbobPs6BqlsnGMjqn2DuXdA8FsTvsgxx1gUDeCOCKnI0TQdyiSO3Yj4FQLSbuHK4gtL6qz9kbMeKx5ITKPTOofd7__n04veMQFYpoQta_-GxKj_OYoM38NfcAoZ6cjThvwKPzBq6USngFYlAtvhUv9mlSECVkD6mHCJJZIcntD7VVjKM9G8R0G3LsUSh8vv2njkHM1kZCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=XW_0oNja2WTyxn7kqWzBYZsXMADbQxC9f_nWahr829oKnTnLFbYWRYOrU70UE-z65kA15CBCJuwSclN70If9wwC1_EP7jpE9JJHILKVSKKY6nlVYUoLnaU5rCC3ADgRTmfF9Jk0-CkdXeCmWjuBR7XzeS-pYUcYzBUeR_8qcPa9arFKh71xJ90hbtbjK773CRCWw5BlZGg0R27uENvEFUvQxAXlGKW-VvzGoyG84W46FPSV8v1IS380hhbCjBeBDSqPtQU45Q_5BCOoY9WCleirQpAQYxtZFpKClaYRHB0omLOlu5hDVqWKypUCZgBExSqW-TlbIuHpUqFbdpjabSL-ma-Lxp8-fpiQunDBvyFV697dig5aAGw4Fr0tYlup5e_JLpIEVMZ5_bsjI3KMhuxP4nyONstnT9w-SrVhYnCnlMOGz-ojB-fLIiMEVNScVAUAK1t2rCIlqX73OJ3X6RhrViiAHPKvSCfbobPs6BqlsnGMjqn2DuXdA8FsTvsgxx1gUDeCOCKnI0TQdyiSO3Yj4FQLSbuHK4gtL6qz9kbMeKx5ITKPTOofd7__n04veMQFYpoQta_-GxKj_OYoM38NfcAoZ6cjThvwKPzBq6USngFYlAtvhUv9mlSECVkD6mHCJJZIcntD7VVjKM9G8R0G3LsUSh8vv2njkHM1kZCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMiJ95-8shegVwI9IwWTuMDo4hPcTd_Bl_sCMUanNa8MqPXybbXrqygTk2XJhLDocTxXYqFp5UTGkG8KocApyYrE9HixEVLSwLW9xuzOA5iREetx-VcJ-ONZwXp7GnfKjSRPhC6xljv1_8_ibsL5PaGuF_teMCWXPMGi27_5VfEvhj-zJLAJK1Q79X-aVvRH33zRzwLgGBWCJNjPmIuwp4MC5wfYju4ZmUW6IqMjerwxLpgXpLwM5jj1CtjoSDq3CdtN4OIcCHGibqD_erwwTEsVuBD7FTRJKIBpeISHPu1hulDPCpc_xbjLNUTISAyU8H2kfrLtYrQ7-Q3-kyjoeFIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMiJ95-8shegVwI9IwWTuMDo4hPcTd_Bl_sCMUanNa8MqPXybbXrqygTk2XJhLDocTxXYqFp5UTGkG8KocApyYrE9HixEVLSwLW9xuzOA5iREetx-VcJ-ONZwXp7GnfKjSRPhC6xljv1_8_ibsL5PaGuF_teMCWXPMGi27_5VfEvhj-zJLAJK1Q79X-aVvRH33zRzwLgGBWCJNjPmIuwp4MC5wfYju4ZmUW6IqMjerwxLpgXpLwM5jj1CtjoSDq3CdtN4OIcCHGibqD_erwwTEsVuBD7FTRJKIBpeISHPu1hulDPCpc_xbjLNUTISAyU8H2kfrLtYrQ7-Q3-kyjoeFIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7XXidhwIX6CTMW-71ACHm1vD6Y_WDPHhvKVe-u1SRB3OecpgWq_pqz0lSD4_f17FRfoKcobNDPz2ZB7SS0qHisjNkBc6WU1NjQZHUqWROC4FPpVrrZmWYDNQYnrVLmGgi0pWuT4cKLRrf4JttloCZyMzDOcauJ1C-VYo0xSIpL19Ft8RfcEzAXInH4DFu9QMAGjcS2p4XTsTuLQ_NgDz5fywYLEZcw4UmSEK8Px28EZ5q82DZ-vdFMvZyQ0tvKE0XzAoYtYE0CxDrHZFPkme1DCaUTt5H5JkeSqWi2wKX_6WAbF1UeVwXD6Cr0AjwIuxv-X3iKJCw_J1WIwkZCdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRab8a2bf8GS9LX0A_NlSVGsQ42lMJ1Cq-0A6pf0IKbCTOni4EqxgH2_Jdlw9yNgn4yyEKh0swSK8fE3LInwYssBG_054gQ9vR7o5Bh9eS8nCUnGk-etx0IHlODsalBX_3Xdc1cN4rK50_4Wah_GpiTfuDCoEoH6IndjJ8gls8JawbkBWdqGvAA_amCi_4jmMjEkv5pnLYqrYFNcRlTY3T4GwVwRHpunogPqSOHtF0IqBZ9-zyxy-d0hAvJmzetxWKnnqwwagdBU3_OVv7hyxH_UzuY-s6igwRlLY65vriiw1YPOC57EjVTeyS9TKTghqyf8U6pKzbIioJmqqEzhDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=PGEvaB4MewMoq9SD63cdXlWSN0LwYFFm-ywzIcZdDq322QFhrrm5KIxBdRhSG0ts4hhNvUat5oB2bC3ZC2Ox3vyfb_2FOIxE7NmVPkBlKKxzvfnEDoIY80cjwvH6RqAXs0ZjcZphTwFElFuWjlMKzocyMg69wezJqQMY7F6uyJSoWNAKrbUIzUawdlYxidW2YX_MbDhmCcDjg4rpUKGjEiZtaYVeOihFGnscTVf-wn7oT99CDszQ2oK9P0l34FHOpzg_2W52lXcEv1Ena-HZx5V-FsaX5wviN6yROuuJz-Xs1D-x8BVRZnq1oB7G5XlvW0tNwib2_-7bDDU5n8E4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=PGEvaB4MewMoq9SD63cdXlWSN0LwYFFm-ywzIcZdDq322QFhrrm5KIxBdRhSG0ts4hhNvUat5oB2bC3ZC2Ox3vyfb_2FOIxE7NmVPkBlKKxzvfnEDoIY80cjwvH6RqAXs0ZjcZphTwFElFuWjlMKzocyMg69wezJqQMY7F6uyJSoWNAKrbUIzUawdlYxidW2YX_MbDhmCcDjg4rpUKGjEiZtaYVeOihFGnscTVf-wn7oT99CDszQ2oK9P0l34FHOpzg_2W52lXcEv1Ena-HZx5V-FsaX5wviN6yROuuJz-Xs1D-x8BVRZnq1oB7G5XlvW0tNwib2_-7bDDU5n8E4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=Fi9lWTuaSr4hoTiI3IOMXAy2ryuOEqc-qglv0VzBgxQaQQPQXHgGlj2ey3cCqzkYBDqElbv_waMkEKllDmVhBSY97Y1hHfvK2L8r1bM6vorZt72X7wALuHo1sFFcBHhNT4Cnk5rrkCpXjKl4QpZWYpPePKmOAjOd3pUO16EWBv10YoHOUPfOSeVapim9jL8hQXKoAzoKzHTOHcIwR7W09cX5GFgvWB_7_5MvFtH6I29F2Xn6jjyXb_ueeyoBVQLHbnJM5XXWgoDPMBG2iUDsqO81H8pEJMwa-bmfg7EIlQsk_3rQuJK5kOSgPPSGtfNcVE8qoyqVAN9B5UjCB5kx1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=Fi9lWTuaSr4hoTiI3IOMXAy2ryuOEqc-qglv0VzBgxQaQQPQXHgGlj2ey3cCqzkYBDqElbv_waMkEKllDmVhBSY97Y1hHfvK2L8r1bM6vorZt72X7wALuHo1sFFcBHhNT4Cnk5rrkCpXjKl4QpZWYpPePKmOAjOd3pUO16EWBv10YoHOUPfOSeVapim9jL8hQXKoAzoKzHTOHcIwR7W09cX5GFgvWB_7_5MvFtH6I29F2Xn6jjyXb_ueeyoBVQLHbnJM5XXWgoDPMBG2iUDsqO81H8pEJMwa-bmfg7EIlQsk_3rQuJK5kOSgPPSGtfNcVE8qoyqVAN9B5UjCB5kx1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p77PQ_dilxsXOk8TRnBQobYTcA8uD5_INx3PB9aQypVs6NF_N8IpxhSvASjsSV5wCkT9iVgk9SEk-ZFGW14JKJ8APR6VY0SH9NhXI3pys-qFN_j330ewDwtEBY45JULdF62y47nh6VVZU6UiNgef3TBW-omB8C3Km4P_OLjYvzR3TO12z0PG01QlDibuHmIRT3LZsq2ODelwNbDNquzboHZcoNysr2gBeHJYsTdzJP6bqm_F7krhKnzIvbg8vLMteeCdsEf922SOin99YWxZxJ3USY4_eCZMU659ITBDN7hbusfBlkkmQ0qur5QTtBIk7GJM_jlX7YVomY_cDPnSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=Cv27NORdmwKBg58Onewj_j3WO_MsYnOCMUV9W8MiNTLEo-I9o5IQ_2ylZVR31SeLAgNf6UCJuwlFlJZxni775-yJlLTJH9o-34HihrmJQp_4KYlOHpfwCJHuZdSKk31ZlAQDSn8LX88ztrcRgHwTtPHB_gmolekjJE5GbSyskeS2FA9-y2pPCc5flo9917BRvkBjrtpkw7A5uhPvguW6jb3idrbBygAzq9IZa2HmEkUeu36CbqF60uNnQ-vBoQGtwK31ROv5o_IcNniMntUQK9zl38g-vKW-M7FyQ0b4KhWjmWNyefCJFyiwJCaAVAn_xL1TBlfli2In2feB0PnPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=Cv27NORdmwKBg58Onewj_j3WO_MsYnOCMUV9W8MiNTLEo-I9o5IQ_2ylZVR31SeLAgNf6UCJuwlFlJZxni775-yJlLTJH9o-34HihrmJQp_4KYlOHpfwCJHuZdSKk31ZlAQDSn8LX88ztrcRgHwTtPHB_gmolekjJE5GbSyskeS2FA9-y2pPCc5flo9917BRvkBjrtpkw7A5uhPvguW6jb3idrbBygAzq9IZa2HmEkUeu36CbqF60uNnQ-vBoQGtwK31ROv5o_IcNniMntUQK9zl38g-vKW-M7FyQ0b4KhWjmWNyefCJFyiwJCaAVAn_xL1TBlfli2In2feB0PnPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=uuy_kS1b42WtrCMz5oA20zKvy_RykUtbtvycw0NXz0XBR9O_Yx31T0ZoItKRZz7SbTAFIbd958yQysby1rvkQ8h7kuhKU7xAwmXtcGSUCVRQuB0bdcRjCDBkLx2WUVCy7X0Qe0GmFGanu_t1USpXuqCxV1Az2s-OT1h1px1YEm-6G8cjKGhnb_u37k6xIUV0dtskQvqe1-5zeuemDY7U4STNXXYNc6fGzgMGCHqaygdQNVhs3RUh5cX_ey4EdozjYaIPYzh7OhJhZjPWvfzdTDitkm_wlHo27Qo_cXzZf5S4oQB-gBZf1djE0UxgnwPtjTmV3MdBZX_nwaW2kRiDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=uuy_kS1b42WtrCMz5oA20zKvy_RykUtbtvycw0NXz0XBR9O_Yx31T0ZoItKRZz7SbTAFIbd958yQysby1rvkQ8h7kuhKU7xAwmXtcGSUCVRQuB0bdcRjCDBkLx2WUVCy7X0Qe0GmFGanu_t1USpXuqCxV1Az2s-OT1h1px1YEm-6G8cjKGhnb_u37k6xIUV0dtskQvqe1-5zeuemDY7U4STNXXYNc6fGzgMGCHqaygdQNVhs3RUh5cX_ey4EdozjYaIPYzh7OhJhZjPWvfzdTDitkm_wlHo27Qo_cXzZf5S4oQB-gBZf1djE0UxgnwPtjTmV3MdBZX_nwaW2kRiDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=dPf4fQZESb7pdQgt-L9P_AF1lEkFccUUtwopGRTrfveOJ-3M6XKykpcEWfjg_IP48NVzuomitwe-DyP5hMP8ieNIvW98iqGSknPiSgdd3wYKibrlrP574474qWK7CEBvwFBtrMeMZajTvtLq_y5YTMRVDJy5xk8TndOM3uh_Te9-U6C1nzbjyaFgHa6l6EGF4PmMO8xoDCrcbo3LQyGqT_s6VL4ZGbvG755hBPiT5Z0Hl8bRpQAHLTsruNdvUA5pVWgYEy400qc9pahy3WeovX8NvGM5A3fp984uDxayZXDognUFIk9W2R7gSvmpIUHr56b73UMtDaAc7FVa8N8p3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=dPf4fQZESb7pdQgt-L9P_AF1lEkFccUUtwopGRTrfveOJ-3M6XKykpcEWfjg_IP48NVzuomitwe-DyP5hMP8ieNIvW98iqGSknPiSgdd3wYKibrlrP574474qWK7CEBvwFBtrMeMZajTvtLq_y5YTMRVDJy5xk8TndOM3uh_Te9-U6C1nzbjyaFgHa6l6EGF4PmMO8xoDCrcbo3LQyGqT_s6VL4ZGbvG755hBPiT5Z0Hl8bRpQAHLTsruNdvUA5pVWgYEy400qc9pahy3WeovX8NvGM5A3fp984uDxayZXDognUFIk9W2R7gSvmpIUHr56b73UMtDaAc7FVa8N8p3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=nRgsYcSlWHQNvDSGceR3ve4pPSG55IKTCzMTUDhtFGmEk1RnLPTHdq7Vl1pOXlCMNMBt1I1qqAt_JfepFAjR8fO0rTdMY2W_vNcPcANWx3pX857nzI7S4uUfVhgIX39c2-tpOhA7U9t3iUXCshxOJyc3ORTaM1Xodoptd0Uv8YKzGjcpLrANLJcdtmoViL-7UNkO9BhKu7Ubbq3YTeHxEOEqaIbK21KlHgKTrBwzV-D4n71kQ1CMjk8MyvCYEyyPOje9JtOYDgOMULpQMhaaEVXUL_7OEv6P2mIRxKrB6O_akUHsxnDuUJEF0vAgZnH2Yfvs8IDxqGLFF87_N44JSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=nRgsYcSlWHQNvDSGceR3ve4pPSG55IKTCzMTUDhtFGmEk1RnLPTHdq7Vl1pOXlCMNMBt1I1qqAt_JfepFAjR8fO0rTdMY2W_vNcPcANWx3pX857nzI7S4uUfVhgIX39c2-tpOhA7U9t3iUXCshxOJyc3ORTaM1Xodoptd0Uv8YKzGjcpLrANLJcdtmoViL-7UNkO9BhKu7Ubbq3YTeHxEOEqaIbK21KlHgKTrBwzV-D4n71kQ1CMjk8MyvCYEyyPOje9JtOYDgOMULpQMhaaEVXUL_7OEv6P2mIRxKrB6O_akUHsxnDuUJEF0vAgZnH2Yfvs8IDxqGLFF87_N44JSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=mQTSRuesj-UxS9mEPZ7NDcWfEQ7HkIx3dQsP0gYXUeWndsIe25AXbZsoGB4gs5tC8DGhFDWuW8T6oykYSo3Oag7vJkfVSAwAv2vlHfNY-M_6iu2uVinCURak_wBKH10GHxjqFN9GZJv0X_-MrqJt7gCosiaujykVzdGipOq6aBNcs7NrX4yL31YncfNw_fc0Rtab1RSOfNuN_gNdLFvl2Sbl32OyFBC7BitxkS521n7huYLe2XMzFizgM5a14ZC6gBaEsrTqBe8WabfsUyyhnxt05iUqY28DoIRPQameIGRWFSSrQmWFURzvpRKJisgTFNdCl1L-TPdbhrBcqWd6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=mQTSRuesj-UxS9mEPZ7NDcWfEQ7HkIx3dQsP0gYXUeWndsIe25AXbZsoGB4gs5tC8DGhFDWuW8T6oykYSo3Oag7vJkfVSAwAv2vlHfNY-M_6iu2uVinCURak_wBKH10GHxjqFN9GZJv0X_-MrqJt7gCosiaujykVzdGipOq6aBNcs7NrX4yL31YncfNw_fc0Rtab1RSOfNuN_gNdLFvl2Sbl32OyFBC7BitxkS521n7huYLe2XMzFizgM5a14ZC6gBaEsrTqBe8WabfsUyyhnxt05iUqY28DoIRPQameIGRWFSSrQmWFURzvpRKJisgTFNdCl1L-TPdbhrBcqWd6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ewOSJjQH4llZ1zDT-ZKfwEyGYRmbYNqYSt2peXa2w4Pxc_vxN77K9zphj8DWzvjDKBk7xDG2F8wg4QH-l8h3vq8Dtg-Q9WBefKKroBgILmL1CCmwwNVIGnrBwrtL5stsIMUPE7k9muxoe7NnQHjGjw561IlqI9LF2UYXa56QTz3ssH0UVO_NNwBi7c1JBB5hiP866dcDOa4_uzCiX6TrUdytLFiWdb2rwwt7n0pRX_e1_MILoL7Z2RkWPn4vYtqcLXf262rdZxvnHmRw5ZTDFLd_LrntCGjW0NaOK7C1UsNGB34A8-l7uYu43evtNp8-jdUri0_y466yuBmo276kVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ewOSJjQH4llZ1zDT-ZKfwEyGYRmbYNqYSt2peXa2w4Pxc_vxN77K9zphj8DWzvjDKBk7xDG2F8wg4QH-l8h3vq8Dtg-Q9WBefKKroBgILmL1CCmwwNVIGnrBwrtL5stsIMUPE7k9muxoe7NnQHjGjw561IlqI9LF2UYXa56QTz3ssH0UVO_NNwBi7c1JBB5hiP866dcDOa4_uzCiX6TrUdytLFiWdb2rwwt7n0pRX_e1_MILoL7Z2RkWPn4vYtqcLXf262rdZxvnHmRw5ZTDFLd_LrntCGjW0NaOK7C1UsNGB34A8-l7uYu43evtNp8-jdUri0_y466yuBmo276kVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=dQUW2Iz6mrXNSmA9TYG4tMhGBH6FrbfIwEyIQMMfnH6LrLLZRbVHnl-wdk4vN6aYVlQNK7AF28qPbHBctPU_3E6WRVU7oj8Nxs7iUTRS665R8bYWoLmshJYrox0vrPcd48iXodoHoKbXolT0xEdeGhQb_XZF0C61sqtVZZ_aEEHXcaWwisX0CmMlEKi0xqlatnhCIjo1Qise5Wb4MymYJtrknjdCKFNXxfqazgeV1HhcZ-EnDFdxL76qfbmz9WvNj2UZxOdpJYGiRpFPwRYfDIIDCWydUwXloRMjz8pCoVSBmZLL4LOWioYG5T6aYNclhn7BOzXRKIEBTMMIvSMfWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=dQUW2Iz6mrXNSmA9TYG4tMhGBH6FrbfIwEyIQMMfnH6LrLLZRbVHnl-wdk4vN6aYVlQNK7AF28qPbHBctPU_3E6WRVU7oj8Nxs7iUTRS665R8bYWoLmshJYrox0vrPcd48iXodoHoKbXolT0xEdeGhQb_XZF0C61sqtVZZ_aEEHXcaWwisX0CmMlEKi0xqlatnhCIjo1Qise5Wb4MymYJtrknjdCKFNXxfqazgeV1HhcZ-EnDFdxL76qfbmz9WvNj2UZxOdpJYGiRpFPwRYfDIIDCWydUwXloRMjz8pCoVSBmZLL4LOWioYG5T6aYNclhn7BOzXRKIEBTMMIvSMfWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=RiWdSHP57EdmHFkViLatyadiaQYgAFNVCyLTiR6dEPkX8yHxtEeNIl9wPli6khvK783LfwNWurksDOW5D3kIlcJr5gCBltZqzo5SNCa1GgTBIZ6_pbbXMMEUD8FZ8WaxOcuf80ATIQWQRqJragGO3r4yVoyNj5hg_S8l-jp5EhE2YWMbmQ8vSaBPzg9l6WS0QGOLlii7oeDTkkonaUCRVrGD7vnCVvSy9nyiJlmsbDh68kN1mcx9xm_6niCfNtVx_PhRbJ5cV-CVkm_vDoDnKTdc1wZC1Z32ga3eVti9o4cwXMoLHbPnBG-Ih_luKIQrnz_IHWPI1sZW5CAbwHV6pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=RiWdSHP57EdmHFkViLatyadiaQYgAFNVCyLTiR6dEPkX8yHxtEeNIl9wPli6khvK783LfwNWurksDOW5D3kIlcJr5gCBltZqzo5SNCa1GgTBIZ6_pbbXMMEUD8FZ8WaxOcuf80ATIQWQRqJragGO3r4yVoyNj5hg_S8l-jp5EhE2YWMbmQ8vSaBPzg9l6WS0QGOLlii7oeDTkkonaUCRVrGD7vnCVvSy9nyiJlmsbDh68kN1mcx9xm_6niCfNtVx_PhRbJ5cV-CVkm_vDoDnKTdc1wZC1Z32ga3eVti9o4cwXMoLHbPnBG-Ih_luKIQrnz_IHWPI1sZW5CAbwHV6pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=jGG_HUGPhW3JoOuO4_WrMJDmbLnH9rLmIhrcROZnBEgGW1NXjDtnmaaKYs1-g_eX-d2Wu72ntmygPTuQh8DWXNSZM9Hy631KILJusTuzdSEqPCdVD07y8Ah2b12U5-cjf0ero2liBU1VL6iB-GMe8UzGU5OKrcvSx8WHXgd5VnWO0hFbSriMx3IkJ0si1SZnqGyU-zFdx-DIqxG-UKxMhayLB3VJw7QC61VFAtQ6ABJu7HrXsjKJtxI_dg5L7rPduvAyZYsjgmx_ie0Tr7Hz79zxqSnI5iFR-ITfF8G27i1mqS4Xtw-88B3PDZ_8N9QVod1Mm_bw8fFr6NCw153VPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=jGG_HUGPhW3JoOuO4_WrMJDmbLnH9rLmIhrcROZnBEgGW1NXjDtnmaaKYs1-g_eX-d2Wu72ntmygPTuQh8DWXNSZM9Hy631KILJusTuzdSEqPCdVD07y8Ah2b12U5-cjf0ero2liBU1VL6iB-GMe8UzGU5OKrcvSx8WHXgd5VnWO0hFbSriMx3IkJ0si1SZnqGyU-zFdx-DIqxG-UKxMhayLB3VJw7QC61VFAtQ6ABJu7HrXsjKJtxI_dg5L7rPduvAyZYsjgmx_ie0Tr7Hz79zxqSnI5iFR-ITfF8G27i1mqS4Xtw-88B3PDZ_8N9QVod1Mm_bw8fFr6NCw153VPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
