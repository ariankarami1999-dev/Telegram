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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 196K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 02:22:15</div>
<hr>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEouIJbfPNLRVsoAiKGSUYyHBOyK1EXsq_nBT4rC4EJn_2quDINSKUr8akbVFS6CYXr5zuY6UAvZF4eaCZlyGIRvXTm7VtEnR4qas830QudmUMQCkIJov29fOPculs69HNtVwmYw0uW0jqkt0tHwvCEWsFwl3fuAa3KDMJE3fDZvZNokrrmp2NcwShYSJAIylW-k05P4QOoE4MJLrig2kpewjF3wHKzToouF8VaIhlb3n9JNjhhcGniu1NdHeo7DDsOT6ERf5Si8-EjKBQUricC9MZnyJQLKNafrtzOaF4H9N_sPTxnc-Vaoeg08khunqGaKKPzrX91K1wnXd6BIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmQzLijl6-MWybeuasyOLJubHsI5xxwlyG4pM1bs_GD1DOl7kozm-gD00cv7XudprC-YJqhrXyEivzPEVXxesJePLur9o3gB7vZbax7O6FzLc7MX3B7_UC32eHjv4h9cFy21680veFtoIKWoeCrvVKaIFfaza4PlkQcP5EktdvetGS4PcAn10H1qbN0JelQyuE3OCHVvCXT0Ggnx6o28mKi9M84qxbO0R1S53QF_cEwcl6dhLvtlkztr0vLXjoVFmer2meu46m9F6ERBFdOz98Q0-uYmtbbrqd-hceyLFXWeEcjxOozrqrbyP5xsBF83b6tkiZaFfAZjF_jnq6uEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkPuOBvm2pcp4wvkDkR0AYEinFcPQy0dTzwElBzhzMQELX96htq4juR99ea78DGRG13l6OwlEX8BE6MOhsBbC6QYKXWlzGVMDCcxQ9OIZHB6FEIWEAl7emLzuxUYaKkc6UpvM4sbGuXrDdmQkF1jC1_Im_OoaT8-HZhLx3H_TAnNzwkjCy-8MtFuQDMRMdpaLthB2NanYlA2Xe15wBptm7vGPFSzNvkgc6pUdpW8iGOfVFl8aMeBNmKo3zUVV-ahnLLTc1tNdc3bjN6giKr-9XG79LoiHk2rwrwl8z78-4EpRQ5APZUaK5QqqWl_9vcH-SSIvrWzLA_54ugFzE86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=Wly41GEcem0DehmkaAJtvBLXAJok_kLXqNpYsXL1BoDc4ezel4Bhavrp9f-SCFIt-QW7F9vjUizDtCYCf3C-bbw8QhtCwgmdwtyxggPYBT1v7ymauHI-EOFi1yfLEycQ3oAbz00dU5mDZU4lqtVIp7JY7-grV_bH3hhzLB_MoAmjvxfVOo78hSIw4Hd26lh3wHfAFPqEFekZNdGoocwrSchtVmi4WnFJCQt7pGiyjjyBI4jQ4pqDcmCQIIQHRil1iX7fhy0IFrKxg4SdyDLo2-rJ-lAi5_QJjIocSydp4y-gRSwOwxnd3qNGrS-bmYnQk4wf3SiYfV4meFaPdZHcrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=Wly41GEcem0DehmkaAJtvBLXAJok_kLXqNpYsXL1BoDc4ezel4Bhavrp9f-SCFIt-QW7F9vjUizDtCYCf3C-bbw8QhtCwgmdwtyxggPYBT1v7ymauHI-EOFi1yfLEycQ3oAbz00dU5mDZU4lqtVIp7JY7-grV_bH3hhzLB_MoAmjvxfVOo78hSIw4Hd26lh3wHfAFPqEFekZNdGoocwrSchtVmi4WnFJCQt7pGiyjjyBI4jQ4pqDcmCQIIQHRil1iX7fhy0IFrKxg4SdyDLo2-rJ-lAi5_QJjIocSydp4y-gRSwOwxnd3qNGrS-bmYnQk4wf3SiYfV4meFaPdZHcrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=lqXQyBfrTcmtaNeMC02xiAx9sfxtUSJ9IwnYyZbascyaALbK5TGmnpFpy8sY6rQlEgSxF-aKMwbXNO2YUJCxL5CFR7a2qVy4RlEPBuM2cCzakYswgEHbIlq2ktuWrE7ZvvI3nbqk3ow-nU0XEcVapuisJsEMDkVZmzQEPQWPJyOo4ixk1yVJ8QkheFVi2q0fPKoLH-FVgm0V1_aOspeMQNhaQR40WruhUig9fRc8Yg5K8hI8XYJaYwGhzo-_KUXR6HYmsXbe9mewq6vX4kBvz2_XfL3KIOJzl_d-D3-WQz_BJPwzrFJm0KH2a97uIEyoDspxbLhnlxwSm4h6IFwDtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=lqXQyBfrTcmtaNeMC02xiAx9sfxtUSJ9IwnYyZbascyaALbK5TGmnpFpy8sY6rQlEgSxF-aKMwbXNO2YUJCxL5CFR7a2qVy4RlEPBuM2cCzakYswgEHbIlq2ktuWrE7ZvvI3nbqk3ow-nU0XEcVapuisJsEMDkVZmzQEPQWPJyOo4ixk1yVJ8QkheFVi2q0fPKoLH-FVgm0V1_aOspeMQNhaQR40WruhUig9fRc8Yg5K8hI8XYJaYwGhzo-_KUXR6HYmsXbe9mewq6vX4kBvz2_XfL3KIOJzl_d-D3-WQz_BJPwzrFJm0KH2a97uIEyoDspxbLhnlxwSm4h6IFwDtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7t-CHHefTDKyK6Jf2lerDetm2IzEVFuJYt4LT9I7EXaWrqtTfq6uhgMVlnq6a0jFz6gelNI6UjJNRBiOKnOz_Fn-PSZBC66JDYSXTcH2D9Q1qKizlcEo2vuZh-9NUjy6cqoxgkvj_K1v3YgwGQEqG68qKr4YmCcJm3KlaocnMG7n8fbRC1xs5awW-670o9J10t-3toA4nqGmCtrrQGX0UPiK6w9udSz0ZXAJnzUCq2DCKZZ8mFzf58iqusqf4gjeCE379EL3_apsILo_AHJl6xcZSh8KtuBzpyADiUTE8iDEX1wzq8e4pg-m2CMPdKQJ_V08idU1RP_0kotFwbzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=mfFNWRJxyaf62aOwBWoqdNY5atn45f3cFLHW5DQB5AC7wr4SJVSKpRV-BI_1KO4hOBbcGTy3eH9Lfc0lw26Z349Vfgkcq-qyyimR0ZWk4ul56dA2ytuo5IWkudXAkvlftkURhnHLihDIVYU7lVG3VV2PHY7NaZ5hfp09SO20S4UYppJ_BVbEaI3_3--rXtm64pLumTLDtgH-SzNdDqVJlpdjmneqCSHkgDIDbI8ZPptViqxKZuXYk9ncRHKBTvtpf49-tT7lSHM5nZgWZ03gew79N7AMJT2XeZUPzfTRM8Y6xymQL0mxpaRA4GjgQCMszs4qCcHeV4HQwPbH_p9bhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=mfFNWRJxyaf62aOwBWoqdNY5atn45f3cFLHW5DQB5AC7wr4SJVSKpRV-BI_1KO4hOBbcGTy3eH9Lfc0lw26Z349Vfgkcq-qyyimR0ZWk4ul56dA2ytuo5IWkudXAkvlftkURhnHLihDIVYU7lVG3VV2PHY7NaZ5hfp09SO20S4UYppJ_BVbEaI3_3--rXtm64pLumTLDtgH-SzNdDqVJlpdjmneqCSHkgDIDbI8ZPptViqxKZuXYk9ncRHKBTvtpf49-tT7lSHM5nZgWZ03gew79N7AMJT2XeZUPzfTRM8Y6xymQL0mxpaRA4GjgQCMszs4qCcHeV4HQwPbH_p9bhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=RVF9FpA8DSnudakxspoweJNDWhr98xbl8NqoNrWtIzFr5dFgouPR_scqLfV3nvl7b51A2ocqCdarpFd2Mum-bRUMMwFZsWJOFOzWWUtuUmXx6qIEDT5cwec3aL-LTlI2uAJ5NAfx53RN6M9sG-K7bGlOhezbiCvGUhGPRlX9wSnCCIe9XcLr7A_fl1KILocvcONOFMMlokLCVqpYqIOrAiGgZ6z68BEhQgUky-DZBPnGm89DniTTVfx2pWyHnpxvDL4Yn3DzU1YV6q8nSZuOXW0SENbGIfwJuI_hnsNUBiQLBRHimPfRc85vwDEE79BuUMnbgQ6QbaqspK8_s7dZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=RVF9FpA8DSnudakxspoweJNDWhr98xbl8NqoNrWtIzFr5dFgouPR_scqLfV3nvl7b51A2ocqCdarpFd2Mum-bRUMMwFZsWJOFOzWWUtuUmXx6qIEDT5cwec3aL-LTlI2uAJ5NAfx53RN6M9sG-K7bGlOhezbiCvGUhGPRlX9wSnCCIe9XcLr7A_fl1KILocvcONOFMMlokLCVqpYqIOrAiGgZ6z68BEhQgUky-DZBPnGm89DniTTVfx2pWyHnpxvDL4Yn3DzU1YV6q8nSZuOXW0SENbGIfwJuI_hnsNUBiQLBRHimPfRc85vwDEE79BuUMnbgQ6QbaqspK8_s7dZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=d4cQ_joXgBoD-zhdhHbIQoVjnUUrPJaWaEZoRn_sKHyRjObfkywu-cLta2n5kSDCAusqS22zOQKQrXUPpIn7dSuZkZMVcOLvdERLH9POKI4ykY-Li172zPwUTTW3KqPAa6h90tP-oaoYF6EVcP-t1e8ZQEK4KYJCN_zbmphiLVzOwxgBOg22B-J1zqXWMRl85T7ZlIit9a4I6wQExM_q1VR1CuhqbZdP9LFeSS9Gsq89ZR9j5SEC5mdJJHfa8pbQ8Ua5S2H2Pavj5rqaXInAP51WWlrP0r1A_2VEfdMENKlikiUYHhD-DZzIehvndFeMKcIp3yz86o6HyGpnuF9eYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=d4cQ_joXgBoD-zhdhHbIQoVjnUUrPJaWaEZoRn_sKHyRjObfkywu-cLta2n5kSDCAusqS22zOQKQrXUPpIn7dSuZkZMVcOLvdERLH9POKI4ykY-Li172zPwUTTW3KqPAa6h90tP-oaoYF6EVcP-t1e8ZQEK4KYJCN_zbmphiLVzOwxgBOg22B-J1zqXWMRl85T7ZlIit9a4I6wQExM_q1VR1CuhqbZdP9LFeSS9Gsq89ZR9j5SEC5mdJJHfa8pbQ8Ua5S2H2Pavj5rqaXInAP51WWlrP0r1A_2VEfdMENKlikiUYHhD-DZzIehvndFeMKcIp3yz86o6HyGpnuF9eYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=Zr48wTuyfKkIiwZoaolScuoewpAk-63KH0ke4ENevSWtsbSXRIsDLGY7Aa0mF29Ny7esXzZq5BRbfO2g4yw1yFX7zXIdKShjcHIqMop_kU-B43DHPeYzKepfOYSStm8o9dRNi2MLMiImXKxZRDsuBZGbhYRad5qTRanr3T5Y4-QYRvIM2yRFS-L2dbxys4FxXcw1p88LoU5FeE8a2aqbbOpd2T4cA_JtEq0UH0FaeoRjCb8f922BecwGudFU12PMeo40kMjNiF7w7Icci_BuR8GliTnnqMcvIJsBphHiIYLM3VVRpoERXPU28lComN6BIH90vh5pBMFtqeT2DKTDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=Zr48wTuyfKkIiwZoaolScuoewpAk-63KH0ke4ENevSWtsbSXRIsDLGY7Aa0mF29Ny7esXzZq5BRbfO2g4yw1yFX7zXIdKShjcHIqMop_kU-B43DHPeYzKepfOYSStm8o9dRNi2MLMiImXKxZRDsuBZGbhYRad5qTRanr3T5Y4-QYRvIM2yRFS-L2dbxys4FxXcw1p88LoU5FeE8a2aqbbOpd2T4cA_JtEq0UH0FaeoRjCb8f922BecwGudFU12PMeo40kMjNiF7w7Icci_BuR8GliTnnqMcvIJsBphHiIYLM3VVRpoERXPU28lComN6BIH90vh5pBMFtqeT2DKTDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckVu4k7auW6NY0LUnRH33lAjPyiqPM-GGUej_qe97MeNZSEQ5Tc45zwfWDmUV7N4kOO4As2TW7iOesTlJOvlGE0jYP48nMlNRqoSczH1McaSqCrSv3wNtX4lICCeZyZ1O4-3S4QDyC4PF3xOwKk-egma3erUpzd_jTit0UxSOuq2bRO8vkOaydaUfUFxDJ-kYR7Nh0PmqD7rHiDeAvZKN1YTb_r4E4tqUBpPvBcCINy8Ho9GIZXyQupMsKU_wkXK-w-hCb7bBIMqPd-K2_XyiFqL1VO3yqnTVm3eIB13pD35qa2EyMnvAp-U6_O75J03feYzQ1K_to3HZ5cvQEs30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C12DUM9EzqRCCs8eyDQnaeZ__s4EW6xqNiFyUvkl-b4hE2ljMN6D7n_RZc1GlsB0dp_vNjNZxjkkUHYzyU5Tkuc56wSJx7nFiR1oQ_RRyC4NoLZQrhgYQp8cH_AAtWFAD9A9FhfYc_ANNIT-t8GJiS6IXtOitzvmotLXLLggsG5pXtlg-jUbpB3Y974N5ffTirugXRvXN2alN1-XVF9h6V9KGK0ouwN5j6YVUbdnJPtiw8P-SeFCIoqx2UG5-7_PvdcM_hg-Tydbvjxb6vTjGu_HDA1w2QuFhKMKZqp39N9pPYeekyg_qAvUS7TBomdaIHuPBP2HrLzbLQpQgGHykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3qPXmYLn8wGNo5G2KF9O4UadVwLgwXwjffURIUCrs85uz_eKTDKE-U3zO07oXhQsq7cAAW7saFyOwkETyjj_UzfwLGcSwREhj0X3FjJfeajCaQ8SJWL7gLvhk6SXFvJcUjE6T7zLP0NXMqUpEyBJ8ACZ_bxydGWdSEp9knHofr21cdsM8sfmOCe4CB97FK2EQfsi9SE9gjPyatzwvjSHoZtIgGIg0X6TMb6a4ZtVdLUaO7xeipPDVKI9xF0epl9EcHSCMOqXWXNxnAUsy3uQI2MsZbdI5g5Otmap8GL_de6Sgdbf5GFW0FRSecA-lojnWloHhMnLtaDAhjzjWcABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx21IDHhODKk_9ISG5U9KBvhhI_iN1i8DvkpGgCcKDqCfC7nTemgGEVCzzH7hHcRX7eru_ZS0JYTEYcIo-pqfchAm7rsaarM791-GrH1XQRbL4VqXAGjs2ey5FYtTdrB2X2q6_UiH4zdbvM_tr1D3D2in_xrtcnN--3tadIBxTyIrsaLUvARHeNbeWc3MDh5GkQU-T_4sHE1kg-lmym4LMNgkGafPtTWga5L1uTxPp5FAZW-4ZaPPtfrjPbNWlxoy0yBZuhgLqnFE2keHYq-ylO69eE_8q-m-3sDaxBIg19in2xFYxGKV1A-aaIG1mijgAMf9t6AOiWCyOQRktWKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n61HcjhUsqBn1N2lTx5rHoUa7unvji7peyj1R5A2wZltdWD6jwn-5rRDLCo0QCuGva1Ohl4n1PaXw9341nfl8od0v5IH46QhQffvzK9TRf6fu0T_bodY2tl-7Bd2S4m9C7JBUWSnUJLWETOxzEoDUTz3wrXSR9R5k17MwPLQE7HlyZPTzRwVDx-BvYAdi_3MinbVYstmpasYTQ0pWpVwXRa0pwzo9WnQtONnwV59jRrV_sAoLqXZa6ck0kSVW-fVVfyWsNEoFe5WTJTCkBH2rRJ5bzY9lr0p23QD8b0GE6K6L-oW6EI40W8nkULPnw_Yl7ZQvtkfiZb8oA1wlwDw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G07c6pd8g2IMg8O9qLBMCKn791azpepjaiB78czcgWUExlT0eJKkute4ACLk06Ofn4Ey2ONQmfQETB_g9aAcUlI4WmFtPsfo2l1Irbom6JSIzIOcSjoc868-_QxZdahvkSuu9ERoFQ83iO75VUWPXnMil2MgZM0CxSeCQPCJTIBnHKLo3nbpFi7GJS5eGKsx0dth2nqxcSHNs1h656SheYxpWhYU1hQisQ8RYizCl2hyTxUtUMSJpydEws625MfJrSp3JdIUMqB9xG6i8WP5ZM5LPbpSieqBSe6usWwkfkNXXFzJXfVWXdm9ATfld3zmRIAj8SOv8BvvaJeFkndIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=T7A8BtG6hrErdIyPf3b7zREnCmWQp_vrgJK0Vh3Jj3Lu2TQQmH8l0zIPRB1l1NQGx6yMbakQ2QKEAcCnKlVoyZvBc4t2s8U2vXxKDSs4VQpfZZuNh3-11ctr3GTw94k0PKxvCAnfcFqNuaoOjV-fVinregJG1rQiyWnBxmtJMxCxApwc0S_dBbDRA_0CmzA4uftnI6KC6pBUVRCVVF_L8_XJgpZmCvo9klccPyextEmM23_Wj_RQ6tSIwK61CitDtECU0-EjNl-pGNyABhhqmoGrnQlpLjEwYGAxePVidvG9-IBpsWcQ40yN4y_8mromfa_I-RhpKhzAr6PZok9s5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=T7A8BtG6hrErdIyPf3b7zREnCmWQp_vrgJK0Vh3Jj3Lu2TQQmH8l0zIPRB1l1NQGx6yMbakQ2QKEAcCnKlVoyZvBc4t2s8U2vXxKDSs4VQpfZZuNh3-11ctr3GTw94k0PKxvCAnfcFqNuaoOjV-fVinregJG1rQiyWnBxmtJMxCxApwc0S_dBbDRA_0CmzA4uftnI6KC6pBUVRCVVF_L8_XJgpZmCvo9klccPyextEmM23_Wj_RQ6tSIwK61CitDtECU0-EjNl-pGNyABhhqmoGrnQlpLjEwYGAxePVidvG9-IBpsWcQ40yN4y_8mromfa_I-RhpKhzAr6PZok9s5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNy96DAGN8zQsWtX0XqIMaayhualDAR9Kf7UgSo35-s_Df8Q-JeG0Lu78jpmavCpWCuc1x64CgaMmr0ujuk8xYu8Y3Zu7qdPWwYxKQX76jh6TVPqLYyhj9-Ue-RLDU1BsMOjuoe7abB9QMX3TpQNfgpfzFKVNDF-JOVrTWfWUURqqELJo1jzCfR6ZXdNIEKc24VFUQZPEMeP7BimnkPaFd8_A3IzIM2vodxe5M21j3_N0ia2Qngl1q3EQPX1Sq2MaM4wi8fjTwNxGaBFVwka5H4AtxhM9T7gxeanRXlDoKnD1cHw1-NProveNIzAkcBOUOc5biU3Woa-zxVRMI-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2IxlWl2NnOjjsIv4jRSwlTVVPgN4Mz-MUaGP8t1wT47hDV7-gLLVvNkFJNPoA5morp34-2zbhhZ7Mw5z56uohACDhpVOu-nmmcvqDeV6mPXGcFtXWPdkBQa9QN9Osfwe1IQVVrD3GKIn8XsQcMoI6M3aJ7I7SKuTskzIqQRvE1cZY1kl2Now-vhOloNHxsLA6LMf-pHhI0dmZZIWAtCCvbHYpkWx6x8ov_nKppZRpJovFLnUIqvUINKYJPvIxDevHHQ2ssUxUigBFI-ogeQX1CI8wlP-hZfKje-1tuECSwqLLrD55pcSUpU0PjJAcTpG4TRJmjkmYUZeIg1QqEV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvStdV7bEvkyFemjednLD1LNjSXBht2mAdlCx3LqXMr-fmp_3c3so6cnJ-vTwzhxKr4iqv8rjHndbxNy6RjlE0dRF37-Ful7DhgQowVD22BaNl-Dv_AsPc42VZ5uMBnGGOqmOy99XZoty2XQBHq5MOUH6bzU2cd1povWy7JlIbdfsKOSFxh72CgNG9z5LvAGXqbTWhCWmnURC5pyIoejZDL4xa0CdmmknotS5IxFarj1WsckyyrcLL49ZYBuuG-qkv5hcJ_DRxH7fQhc0F8jrJNA3oyoxRAOtQjUv-fvSbmwRUm3fsjY6dJwaQIVmzo4TZGGm5Z_4pYyGBfeWp2L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpWhV9hOf7672TONyWDvUCiNIkb824s9mLLUx0KE9r_U_aq7vGRpO6cnjYwANQ8sd_MATEpmCouGorNMhSq6UjquIqyFfgLT9C7Q8op_FzACzrzUJ5wjjIiKEZUlGPF5-cbw-zwp3EVdI9Plmmbb-ct80nSuznQqSRshxot59n5Ul0NoZm1AtZ54Mg9a5VtYX2ajcQKBnxXGUMY9yJ_nt0bo9Z73VQp0Ap1P16FLnsjQngZqReXEqkixnwSubSyTv5_WA21XSA9eCFrvZg2xNiACsQj4cYVc-e9FG4TaLfmZB35HkKffV5JnDkKGY_TB15Bt3rejFTiWtitv16s5rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=avr5gKmzGOUGZkZ7GuoU4trLqhf5rJdXlOtIYOMkSUBpVL2ka-wQCHjfgsoqBRxaojcWSDMpBv4oXwhU7Qy9YVHmmkZXK_z_QWar_JZctNAc-HRxF9bBRcMlFg4Cr2vP902I5b-IEZ2Pjzo7lj_-v4KmLiv79iT1tSfMyRLLNNAO5LmjXIezUoUhfm0yN0-HCH5odE_r6uVCykHF30bW0ue13txnAjvjom0lyGtLg5s5S72wQKRUPRpswuCmeMEU2Py4DxtkkpCm272sij8Jx9X8KLWu7npkAfu5IB2dkFzWTU6p029Qc_r8qH_23ETLbv2hho65StXEtdKM9fN-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=avr5gKmzGOUGZkZ7GuoU4trLqhf5rJdXlOtIYOMkSUBpVL2ka-wQCHjfgsoqBRxaojcWSDMpBv4oXwhU7Qy9YVHmmkZXK_z_QWar_JZctNAc-HRxF9bBRcMlFg4Cr2vP902I5b-IEZ2Pjzo7lj_-v4KmLiv79iT1tSfMyRLLNNAO5LmjXIezUoUhfm0yN0-HCH5odE_r6uVCykHF30bW0ue13txnAjvjom0lyGtLg5s5S72wQKRUPRpswuCmeMEU2Py4DxtkkpCm272sij8Jx9X8KLWu7npkAfu5IB2dkFzWTU6p029Qc_r8qH_23ETLbv2hho65StXEtdKM9fN-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOB3J9qdHkd1ZKazpc7lmXW5lY14nQdpWQEDNaorB9T9dizWADwADq_We5BzSqrs5VB08b7Hj00mRbaAsca1KCx2sM7N26IufXlvv5l-2xoqTmV8P7CrKCGEAn10_nGeKLPUarnGKzGEEJ1FyJmRBkst_Sak_LLqwKuGgjCRlls-CAAdcJ44gaFddj5pm05G-1Rj-RyF6tinivRUdzEG0CGRVFGe6J0RYCll-U0rvTz36LjAbjuaMqKK5PYJbg9xBVs1a0bFCxQyQk_MaHuVJ64idDZDLX6t1eOLi4Wrdi9rxQ3nAph3LGOkl4wKiqrkXEcNvtOlLvA9hqYX06JG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnMeD_vwChwwYjRAQ-mkAgttOqxYp1yRisG8gyI-6FJkyI8-Xg8r4C6IkuDfw-TfaN0lUg7kuAqnD0InKNdwSSAHzLiEVxbnrKKGFqqVpHnteulwWYbyt339ELh-RxCO3YtAgvnF5GOXE42SHFj1H7zDpQBLh48o98OXiFSXyNQ5g8TlbsKmR1naL9w1RH87EmedpWveA3p7-vmpZfC-4z_9TC95Zgxo8CSY_v9cGXfjX8aakWEuLWpKV1n9PXa9fDgEMraKOoq7soYceQJ0H9sk396ESaf1OtflDbezIC4OhCo8uNTyWipo55G6EjPMCIlZEBLU_wagnh9P3zFqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=OtkGqC9b9tVvCanwdW5Quzkx8gircLRHmQM-FN84c0tJjWZA_3Jf36NO0KYP25n5zNEi7IuLJp0xz7LCWSp6zsP3jx-37jUqiJMBiYfKxzgj7Z8m10fDxPSP1i98Xav2rwEjaW3GYOX0eRFQ1gF2c8ODHkKaKLd6yDLocbtmdsXCpwG-mKm24SM0iU3JOy82CKGBiXcptwLZK2-zxad2QPuY4ysfOKwuoTHUMG_czxQbyuQYWBU5W3Cl29uY58AZ-TkZe_M7bipxocE5AtGeqYEzi3s2jiPixsSb00wjDq7mqapk6WztN5F-CtCm_yOPQ3y8N0TAZ6N_1pPEVcB3dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=OtkGqC9b9tVvCanwdW5Quzkx8gircLRHmQM-FN84c0tJjWZA_3Jf36NO0KYP25n5zNEi7IuLJp0xz7LCWSp6zsP3jx-37jUqiJMBiYfKxzgj7Z8m10fDxPSP1i98Xav2rwEjaW3GYOX0eRFQ1gF2c8ODHkKaKLd6yDLocbtmdsXCpwG-mKm24SM0iU3JOy82CKGBiXcptwLZK2-zxad2QPuY4ysfOKwuoTHUMG_czxQbyuQYWBU5W3Cl29uY58AZ-TkZe_M7bipxocE5AtGeqYEzi3s2jiPixsSb00wjDq7mqapk6WztN5F-CtCm_yOPQ3y8N0TAZ6N_1pPEVcB3dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEpRWYhxcYSLcQ-ym_E_SxwKI7LnJHaPJrFZJK510Vc92gREsMP9iPJY3kN2j201ZPEFXl_ABd8DlhGOt8KGQkicwVW2Ubui8_iT2ZCZ676d_mPw89_JbQpISb7To98-O75xC15oSOV4xMjN3vIx8c8AklQgOsu4FoXZwHcIJam0TPkahsTueuF267h7r5_1mSt-U9e4d074GuVpI3pncJLEje-kCrOlBDTtHC9hJpYaXhFiFdSCvVoi8dD8oTLUNOrjvqk4v-28ZSou6bbTzEBytqKbwJklu2euY3JZ0rxg7vmAzh_xCkc2Wvgg1KbQcR4TXnhGy-FhtR0t1N6trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XikciW089xmWNj18jYwllVigiFjs-U3eZojMiBxbQQLmjI-M9_CtkHrsUC_3Pxp8P7zv_2uoK_ciXFi-MZNF8SXC6x8AdHmQuHoMhLRlqwGnk_7jaWySeaMbGrtjo5oHMczo6xXY8cpYz01fFndWvFHTtjSbgKqHPda0uUdotRaDN2IruXiir6vPzr_7_4drq7Gvc_4m_54CYQ59mLETIdTs8lRc9OMJBVACY9XRau-LVCDOuDKJcUSmp1-QpIuXoJLuQnPgnGbQFAL8egrFshYI8EcavVrRh7T1Jv7XDa6iqh5x7mrfiQBTZeDqLbGNX0lGu61EADF7I29rJZEL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=Q994r09GB9Ksc6EVs8vEc9WsUgsz2vxKGUHwJj0YnEGJM6YVWiAK5ybtmYDrscAbbIij4Q8z2v4-flFeCkK-zqRX68ADqYPx1UieWLQfrjzF_VH042itrjjt3stYfaqYb8NZjS02uIthDICqHbdJ2YWOuDlkrxjp-H1PhKYqgwafUkcdZW7jnlrVTy2XAF_yf1oPGJXB4F4g-4c1b0AdygR0zHBWzw0qUAJeFt6BT12Ta2vuBq6tFKOVNAzWfhyIBZ2tsqtOJ-Il8VfLtS7Fpc4xltxPFsXGMITQoqBvR6hoQs-M6-0A5MtOQvJdxb7YiW4O1X86HP8wKTH191faiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=Q994r09GB9Ksc6EVs8vEc9WsUgsz2vxKGUHwJj0YnEGJM6YVWiAK5ybtmYDrscAbbIij4Q8z2v4-flFeCkK-zqRX68ADqYPx1UieWLQfrjzF_VH042itrjjt3stYfaqYb8NZjS02uIthDICqHbdJ2YWOuDlkrxjp-H1PhKYqgwafUkcdZW7jnlrVTy2XAF_yf1oPGJXB4F4g-4c1b0AdygR0zHBWzw0qUAJeFt6BT12Ta2vuBq6tFKOVNAzWfhyIBZ2tsqtOJ-Il8VfLtS7Fpc4xltxPFsXGMITQoqBvR6hoQs-M6-0A5MtOQvJdxb7YiW4O1X86HP8wKTH191faiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=oNaQ2vaFvusuXEksGl1p0Wf7fv6x47DzdSxrydLj2r0dlqfLwRpo-Sslr8rqfCTom_VgExldcprAlWCfjY7SX17dbUsMmyA6Nh0SR33_eICEn4lJ5gElppTToTAXWUhOMXmM4u2EumlNMI1X-z-HxVkw4oXuHzwEbsSKB5pcT60VuxB4DbsV7V8OjFuDf_QJPeirzz87h2k9sswYHT_YBkBiZxNRx66LfnhzTVTtq5uecIjYYegwDLBjZt0Lr8mjyFwj6XjumynJ69fno1FxGS1UIVLPdAJ4wyuSaXOVDYpuxggW945XV8qycvujvrlE2vzX_LodZgcH1kUrj7hMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=oNaQ2vaFvusuXEksGl1p0Wf7fv6x47DzdSxrydLj2r0dlqfLwRpo-Sslr8rqfCTom_VgExldcprAlWCfjY7SX17dbUsMmyA6Nh0SR33_eICEn4lJ5gElppTToTAXWUhOMXmM4u2EumlNMI1X-z-HxVkw4oXuHzwEbsSKB5pcT60VuxB4DbsV7V8OjFuDf_QJPeirzz87h2k9sswYHT_YBkBiZxNRx66LfnhzTVTtq5uecIjYYegwDLBjZt0Lr8mjyFwj6XjumynJ69fno1FxGS1UIVLPdAJ4wyuSaXOVDYpuxggW945XV8qycvujvrlE2vzX_LodZgcH1kUrj7hMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=PKJBVgrsg53xvS4rxZcuA-qvu98ASZYOtfhjIHz6HdSg9N_KvvZzPrxX0PlnLrMsQngGRklhOcNtsamddZM1G7XofBSkdeIZXHpeYthFd5vzfuIcXvanF7Nacfe2DD6fudDo5L1uZuT9iscClA1Pk7B9Ywn_LKI24F9UCq44GlzbuXepRURN9r8he5Nh9_wTAHXWnddNZat-ZUTvFQl0NpoM4ez1Kcp-bQIQjehBRczV7UdhS31PpPvLZrmoG1SCaMGax4cYy06-xcUQ5hPfxK5acfVTzLMhwvsca0-eWXy10E7DULQgx2UQ0zkp4wsHImvZdUDFgcn-fEYtQb0gKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=PKJBVgrsg53xvS4rxZcuA-qvu98ASZYOtfhjIHz6HdSg9N_KvvZzPrxX0PlnLrMsQngGRklhOcNtsamddZM1G7XofBSkdeIZXHpeYthFd5vzfuIcXvanF7Nacfe2DD6fudDo5L1uZuT9iscClA1Pk7B9Ywn_LKI24F9UCq44GlzbuXepRURN9r8he5Nh9_wTAHXWnddNZat-ZUTvFQl0NpoM4ez1Kcp-bQIQjehBRczV7UdhS31PpPvLZrmoG1SCaMGax4cYy06-xcUQ5hPfxK5acfVTzLMhwvsca0-eWXy10E7DULQgx2UQ0zkp4wsHImvZdUDFgcn-fEYtQb0gKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB6UOym6ibw1h1TIvzy3x1fkIRF641AD1q1clO13nOaMoQTWh7h9nMYdbGZSo29JEzHFuGfr725Sb5XcfJNV3T3NjYEK3mjFFfe4d5kNzH2fcFy2hprc_xe2Lfc_FHDK9F4GtuVh863QG6q--LYnexBP76v6Tm-CwpEA5yRHf9RA2Aikf7gvmWXdBezoXh2JSae-OEniH-8Pjp47syqSTv39u2Ylo0ZB0Ej4nt7AvoUZG_-Xq8clC1OYf3FC9t4MytcDM0EetbFOJ1XbmC5dOQnLH1NOY2L-9lz8mVlB2dHc77ulARieHyfgGuBSseg3Sd61whULPGpfwzdh0bJ6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=ne6nKTphQfULTvB09O78yRCLnICUKgXvPgSg6vipFpFVRCHR3WeeV6fD5657PqioKiagBrpDZPKoStrzp1bnRBdVK4WiWN4DXH45LnTyzQJxRLE01gNIH77oXJl1Agk5t8ZUWC69qFICVHK2c_5K1bYP8vKZpnNQN9U5eoPNRZudsw3DTSTBT0xFSQvu7KJGYI6E4RCkVzCO40kZuUHuEfwRZb97Ooze9VQWBxcdjx6G1PjnM75zL091rRUFiUeigBjRwPZixvnRdkcv963twjpSGz4aksMyTdTSe1eCAFjG5nY_ONRX-ObHa5TfPUJcAm7hgXI8U6RQ9f6_x7Vnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=ne6nKTphQfULTvB09O78yRCLnICUKgXvPgSg6vipFpFVRCHR3WeeV6fD5657PqioKiagBrpDZPKoStrzp1bnRBdVK4WiWN4DXH45LnTyzQJxRLE01gNIH77oXJl1Agk5t8ZUWC69qFICVHK2c_5K1bYP8vKZpnNQN9U5eoPNRZudsw3DTSTBT0xFSQvu7KJGYI6E4RCkVzCO40kZuUHuEfwRZb97Ooze9VQWBxcdjx6G1PjnM75zL091rRUFiUeigBjRwPZixvnRdkcv963twjpSGz4aksMyTdTSe1eCAFjG5nY_ONRX-ObHa5TfPUJcAm7hgXI8U6RQ9f6_x7Vnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=S_l0M4eIx514BYdgWZs3Rw2UB6CkK8h58kmemL7hj8ccBwMG8eC0qM0-9s_3Y02GexbZkXhcNDnBXH3kvkXsYngJnFTdZfqFR6nhMCOqIl5b-RJVfhLOo8QzkdupBDdDZJQprOIJ9_-U0240Dm72Lx8GqLhAHujFgx2QA9dOpyVQClxqYc3JdnJeApr7ixkaO1HiYhJC_vMpJXSosyHPXgZE0qG-3av8A5y27owK63nP3ZN2RyM2YtRonTRafTKponirs2AMguIWlfsVGv1FlDB4z90oykML3DIiRpb92gyJToRHEZjH3Le7WTanJ6orIl6a47BUqdgMg9OKczYKdp6GpFmFn3Acl6EwouqiSFFBm3cEiVmH9IL6l4sg35afR23gtL90z4Pa9Vca2Kk_tBzVoPQ9zZ7Gm291DLKO6OiN9N0vt4u0J48lHvwbxLnonW5LGfEI0X7aHenwZAhCUGRggIsHMUmepN1CLQDzHkqP5p0TbKbG-b2afXbvYSYPOO3_2VpRP058m0-XLruxHZXmGTDyXSzvpHchymYUsnvrjbX-cpaUD9hWIMI6wtGxMOTKNpPV8AZy00E9rFYlPXdfNrGMsANWFeoze5rCsQtOsu-Nfwnui3Jj22zkXfW-ZbX49B89g0A3c6G1h4okbxWiyj7I2yJb9bF8nlkJC48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=S_l0M4eIx514BYdgWZs3Rw2UB6CkK8h58kmemL7hj8ccBwMG8eC0qM0-9s_3Y02GexbZkXhcNDnBXH3kvkXsYngJnFTdZfqFR6nhMCOqIl5b-RJVfhLOo8QzkdupBDdDZJQprOIJ9_-U0240Dm72Lx8GqLhAHujFgx2QA9dOpyVQClxqYc3JdnJeApr7ixkaO1HiYhJC_vMpJXSosyHPXgZE0qG-3av8A5y27owK63nP3ZN2RyM2YtRonTRafTKponirs2AMguIWlfsVGv1FlDB4z90oykML3DIiRpb92gyJToRHEZjH3Le7WTanJ6orIl6a47BUqdgMg9OKczYKdp6GpFmFn3Acl6EwouqiSFFBm3cEiVmH9IL6l4sg35afR23gtL90z4Pa9Vca2Kk_tBzVoPQ9zZ7Gm291DLKO6OiN9N0vt4u0J48lHvwbxLnonW5LGfEI0X7aHenwZAhCUGRggIsHMUmepN1CLQDzHkqP5p0TbKbG-b2afXbvYSYPOO3_2VpRP058m0-XLruxHZXmGTDyXSzvpHchymYUsnvrjbX-cpaUD9hWIMI6wtGxMOTKNpPV8AZy00E9rFYlPXdfNrGMsANWFeoze5rCsQtOsu-Nfwnui3Jj22zkXfW-ZbX49B89g0A3c6G1h4okbxWiyj7I2yJb9bF8nlkJC48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq_e6XQKbVyr7DuOmxGvtk9bsLGBViJKV9Kv3qdxCqpD2sOko1W40Fm1h65yLC5SZEVr8Ah5FmK1441Q_wowRmB5rZHryZmtd4hhgQ0msIU7Ohhz33LuAfi1KYQnC5qwTIlh2bnrBOzUrJbQbHwPJqq3S9GKiHPZcONA0C3AZqOs0EtEv96rsaC83SW_nB_BPtWWeMuCNSzQsyPrlsmGBOjjEVWHRJqIkMQkjcvfGjQhJyJSLLdeysyMCX7hfiQmst_phVHsvlzo86zWsJPMoeb8Jeb0S_T6A3etW6jmE8zarLL68Y_J_H0LMEPs3NUEaDNpQ95q2LxP-nAQmKR9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLdk5xQ-o3tTW6x6KAerjbUG8_lavEN2ZLFYAE8dvNtU9QPc8ZP302sq0a_B1S7Me_6gDOLtEFzuSrQbyUjTJXpEXkQdl_Y3BXbczmW2UIZlPdR7_wMoyCDqNNhU2LfxF2xUN3y8usw9VA3TZZyiDmO2N3abgs6O6oxSmm4z3Z7_2NssCqH_I_tOEUOJNYI2bKaHzcKBl6rEHh9BooH2gu3IygB5J768AQZjoJcULntYhZ5E1ws_939UicnXiIU5Nd1rFDEEciHj56kDpXSZui9kGIWw17fblUZouG6r515HBp3IOkAh5qxa6Q1y4IZKAZwA6r393GgTkNbJmkHidQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpizKq9r5Xbb24PGxMQTKT5B2HHSxdRcfaxmVoqkjqhM8oeY21StBl_qzaPcRmFOrSHWPKJ59kb1gk2kr2gO68JXuH9KFbbYpom4LMdTk26XGhz6cqRjQBcbxR293BT93o3mHKc-NEGxmZR3igEMzof1lIVM2eNfWYxu8GeOuk7hY9vSC1ZTnGPPxJi_JNYO3xFMYyhYEbXI36tR0Bs0wrHD0yN-U1Q_gD-4vaRnmE_Q3kbuxEKiAb7PNHriLQFvlYABwFrGAFFYgNBJ5WDChfP-z_wfVM8p3CMSfFKMZhy6E5nnZE8P4LypwP9SjOhkeRpu9xYewOIAlWQ_T8dolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Z3D6uDvAGkTzI7MItqs08nAsolMq_msqCzudSx3SIF0Cnbo7FaDgp1nWNMRWF78Hc5lrC4zfw3Tq3aVCM7P1N9aWVlUko8_T-4rdXOrGL2wvPCTWN-NVqQVrc9ZXPC5rcPqJDX5prv8CpreMUBSQCEZvBLdvyd4nll7ZlA8OO4lR4UWuP3M0rENum51fV53OF-M6Xm5y-u8a6HwIUHXNWPp8oWKOnzSbOCf8sB1_Ffql772jDh9_cPpZvgJhtwWBLnkXSHsx9qz0bJqtYSqzkNuJTWI854EeJjrMVdCeDuTInigZfD6hrg1_fjy2WDCcgbYyAb9sNoV_JOiNfW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3OtOi3FByoDybRBtTdg_9GsyZm2A3IN3O8zx7jmUg_8v8u2hp_SflMPdII_yCeo42nKFh4xaPHYtERCiYTDksm9Q-E_cJt7hJmmYldPp0awYeiy7hYpN2SIcXfAchs0Qfrhivz8awNK4cMBi3JgZrHd10uS1Tm18XxJ0B3B61dDe0bS_jQkRAsLo_QtQ1OtR5mVcuRLhLBA5g1wJz48YEB4JD7yUuUhP_t7tGUuhagb1RPot-_fd3NT7urTwuJSwlS1zKnhRWiu1r3n4wmm8yyx5jps9t507mXOb5FV8KzNxxZqy76DCskIewGD9Bdpj3dvWEMzjC1FRNf4YcxHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=hcXIVplkMs14FAKaRA0APZV1qaeQHMETF1hBK7a9hONpyAurcrqCpc7oAO0rJnmEjxpLJr8Z2mChmCP0NMrIh-ktMkT8Eibe21g8R8NbRoWx10rCWEez3MmyVReL3IAX0bX-X5PrFHnkTsqobtH9rXyTR7RbWJDw1s9rY9F_so1TjYEJz7ybuokMIFoKLVaDH72CTXPF0LkVja9c0JQRUXXI5uDO9MFnmGd4p0-XRC-KFLnYAYsv7iaqe7MtuwcCZlx7_hlvViKHlo3AOLu3uMzy5o9ja_Qmup0W8G5B7DhDgT3JTGVbLPmJ7AfJL0g4v9ovUIEd9C5qTKVFB1bzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=hcXIVplkMs14FAKaRA0APZV1qaeQHMETF1hBK7a9hONpyAurcrqCpc7oAO0rJnmEjxpLJr8Z2mChmCP0NMrIh-ktMkT8Eibe21g8R8NbRoWx10rCWEez3MmyVReL3IAX0bX-X5PrFHnkTsqobtH9rXyTR7RbWJDw1s9rY9F_so1TjYEJz7ybuokMIFoKLVaDH72CTXPF0LkVja9c0JQRUXXI5uDO9MFnmGd4p0-XRC-KFLnYAYsv7iaqe7MtuwcCZlx7_hlvViKHlo3AOLu3uMzy5o9ja_Qmup0W8G5B7DhDgT3JTGVbLPmJ7AfJL0g4v9ovUIEd9C5qTKVFB1bzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=G06fj8bYaBqKIfH0qubilIhreLeVcYwyBWH8dQTD9BQV7H3YdDhEN2iGiushn13DNjPXVNzo6ZX3OVZjt0jb4DIT_OKwYXzXvt_dywXkC4VnVhXAGr4iYRb8dQJ78H2Vd4D1dObj2CtMpJhnbfo7dOsMADOj4xllzA8x9zL9qRB-8iQEEhur83qdJ5e5326-Gu_1uViwU7mcucGNRtvSqba8HB1DNO75K4sRue4wZpjbkRb3ndy0ERl-vFTnzPPeExX97i0HSQkvFmNoUVhFcrez7Rs8lUNoTZgUk9tkR4la9fhlGpNakZbswnWzikGKsQKCosFk7CwguRqxFKnX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=G06fj8bYaBqKIfH0qubilIhreLeVcYwyBWH8dQTD9BQV7H3YdDhEN2iGiushn13DNjPXVNzo6ZX3OVZjt0jb4DIT_OKwYXzXvt_dywXkC4VnVhXAGr4iYRb8dQJ78H2Vd4D1dObj2CtMpJhnbfo7dOsMADOj4xllzA8x9zL9qRB-8iQEEhur83qdJ5e5326-Gu_1uViwU7mcucGNRtvSqba8HB1DNO75K4sRue4wZpjbkRb3ndy0ERl-vFTnzPPeExX97i0HSQkvFmNoUVhFcrez7Rs8lUNoTZgUk9tkR4la9fhlGpNakZbswnWzikGKsQKCosFk7CwguRqxFKnX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvDXGhPY3Byfkpjm3NndP0O9j10AdtLQ7UoUdodf4eU1BVL7sJCq1WgU36-QxjDKDx0dpUHVuPpzUiQf9l3atpFUkac-7xw_AnC-tyKGY2hHhSPos6GjV9hySh6u58BIoGpZkfu5J1lacr4VbyhaVJ-UYQw_H243p1wU_nduKrG1IRYbcj_V7FppicVOXIhAcuMhw6cMhCJKw3tCyC2vdGHDNi_qQ1eOcL3lP6XSUs3D9MIgm-qBj6pPYR1wrTxaynZgSL4o6E1e6m-ppxSEOYO18BRuFJC6CPXh7lag4PLDV43kes4YNB9tcKiKfKbiNhMnINFWySrBx60MPACT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjC2DKcoI2DQynG6SCp6Nhx7p5FHE8Y41-bo9kJEBVsYxVVHBYzNP1gxCOTkjPtSIoIFdr_hBrsEBN6rbVL6B7vn2P4Gea1TiwguiIEcFBzhX3BQpjzoxZaVoFrbURw6i8V7B0aZ94Lej6OV7w0YZ3WMcuwz6mfLjKvNMltdT4vGVg2LHzdIqLK3WLCcm_PjUhmDqDFfXsFTosSiMzPWXZG0b9Iqq1dTMZBZS4HXqOZvLPTLkCJtdxD7xvn7At1XcqSPTYcKddjXzVWIKwWd2J3oP6tmJ-Z0rMmo7IIO61Zq4MdEAxOxnu2Of9ztusnZAl1bQxpaWeYd0b0pvCS1Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=MzLFqfQMQnwuETTQR20FkaNdFOGLKJQNozdsJWDNIg5_sR6SbMH3Qd9d7ji2QIueXc94vZSfuLEw9AzA7ci-yHohMZERNr-wDhozuacVmuR59YwLHoFU9xDFh5wEvAoGpPy6lkhI3NP_rNgf9I3IeLabYdbpM5_XtdIq19hJW6SqHbN0tQPcBNWHe9BsSXbExvDsOVC6sksR0WOwoboBC9As1KyTA4iBwaHj4BQT0SWIgFJ15yn_9HrQFWjHBCtmGZseNjsQhr_ntwS8KQhSwKRDaCU29vn0Lls8VFlbejht291Gs3eHOWUKnWsvvEpnBrTAVw7eKUO3aMe7H8LUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=MzLFqfQMQnwuETTQR20FkaNdFOGLKJQNozdsJWDNIg5_sR6SbMH3Qd9d7ji2QIueXc94vZSfuLEw9AzA7ci-yHohMZERNr-wDhozuacVmuR59YwLHoFU9xDFh5wEvAoGpPy6lkhI3NP_rNgf9I3IeLabYdbpM5_XtdIq19hJW6SqHbN0tQPcBNWHe9BsSXbExvDsOVC6sksR0WOwoboBC9As1KyTA4iBwaHj4BQT0SWIgFJ15yn_9HrQFWjHBCtmGZseNjsQhr_ntwS8KQhSwKRDaCU29vn0Lls8VFlbejht291Gs3eHOWUKnWsvvEpnBrTAVw7eKUO3aMe7H8LUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=l33qVwGRSC27b2P57jsI-4melRj98BwBHom7cb9kuIac4gy47jzJssUnuA-Q6VTX8yb1SObr_rwn8ulLabRsy4ibzSEW8HmdPbg9dS_U3IZ21yG6QF6ZuU0YbcZDbPQDAc3DVdBfZPc3W0CJzb6FKS7kf6F_3CN3oxcy0aljPLfwyZLulP6-TmxGOiXbDzpHpW0olrMyUMBAlz9h32iSzWAUUrI0RvzdeEmg3Bu3mhNpxbnntJK20PiqX_XxdcZ0BcXZtMsmLYT0mnIi351kTn962mBeC55ch05Dmff1j8jhScjEelEG9fmAf0SjI89oyRwbk53nJe4nTscMX3GEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=l33qVwGRSC27b2P57jsI-4melRj98BwBHom7cb9kuIac4gy47jzJssUnuA-Q6VTX8yb1SObr_rwn8ulLabRsy4ibzSEW8HmdPbg9dS_U3IZ21yG6QF6ZuU0YbcZDbPQDAc3DVdBfZPc3W0CJzb6FKS7kf6F_3CN3oxcy0aljPLfwyZLulP6-TmxGOiXbDzpHpW0olrMyUMBAlz9h32iSzWAUUrI0RvzdeEmg3Bu3mhNpxbnntJK20PiqX_XxdcZ0BcXZtMsmLYT0mnIi351kTn962mBeC55ch05Dmff1j8jhScjEelEG9fmAf0SjI89oyRwbk53nJe4nTscMX3GEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzTCeoald1jaTzulgbW4z1xnbqt20hMI6NHLGsjka3ab24vCTUUWLN6QxdDJHnUPvtAWqy1ztptmAgq1baFWEdJWblo6ilz1xNIlzjJhgGXb_tBLPUy0iFewj6kwR2DzJ75s-PnzRfUsffUFzTpR6kiOK300K4o5AVKIQyHTN5H--239fwuyxDx85ctoHe4sPhGL_imCePQlMxbcg5FutoNWShelM3vvQgu2f90D9xO3VtuXBJiZa0UHcBf-58J0y5CcJqRmBBvMOX3EQCkLAOYic-tO7HeykvwQwNo8SuixxHeyoW1HQqagaSPS8XBKGffTGNFq5-naiFru7Ho0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjuEVh4x71SbxjiMBElTq46js2r0-ueIz07XVhwkL3wLUWlxH3mnbhyrMLfQKUrKt33IaJSalTAmDS5YNRXiPaN-cyzo5krxDotto0B3vTLD_7qtMN-Z8lGhOdGDbOZ-0UyDYyt56K1pV43oqQ4cSfcHf1LqEokjFWkcVUbxJdCUoXzBq16UNtGSjhQIcp6VNxXB7hFgUkVRxqzVMXg4g3hSd_rHpLwt7J4AZBckvzMaX1KDrvarG7VuDz0M1ubeJCJZi7XBnMTNmapn4gjrp81HFtxim0i1DVp1pCseM8gUPPooPUHHTLQ2_j60NBL60sCv9Lf0WAjtOHvG8El0Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=kuA2mUY8J402lGQeCNI8NX_GdD3azQId9wE1J6dBzogQdEEeyjOsjMDHTYWKdCdjMwKOf7dlxo7ukMdTywMHSXwYIyaVKGf_htL0Kn9hVXKCCuMvgZ3ouX0WUk43I1cwvydeQtP65VCBDscDLO8SeT_VSIVVgmsC1OblfW_anh94LYDq2g9hM_-9JvtQf8Rf96IiCCAD1aLnY6jO16wt_Lhq4CiJ2Wjb4g-a1LvaKAizSfdhCmHWZ7yY_leFJ75gBXv23W7n-fMgrWSFOXzySCMPcjh3U9VxKBGNipF0DonVZPGyaDyns4F3Va9iv6BDaimaT8SouISrtxcyfiEw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=kuA2mUY8J402lGQeCNI8NX_GdD3azQId9wE1J6dBzogQdEEeyjOsjMDHTYWKdCdjMwKOf7dlxo7ukMdTywMHSXwYIyaVKGf_htL0Kn9hVXKCCuMvgZ3ouX0WUk43I1cwvydeQtP65VCBDscDLO8SeT_VSIVVgmsC1OblfW_anh94LYDq2g9hM_-9JvtQf8Rf96IiCCAD1aLnY6jO16wt_Lhq4CiJ2Wjb4g-a1LvaKAizSfdhCmHWZ7yY_leFJ75gBXv23W7n-fMgrWSFOXzySCMPcjh3U9VxKBGNipF0DonVZPGyaDyns4F3Va9iv6BDaimaT8SouISrtxcyfiEw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mLb-vCCAk-y8UWVrEgznpp7uN6D9T0O9kbXfD7yzSh-VxU7vD-fdNDLAbxhtWuDeL5YlMcII71KgNaxubtT08jWrqP6WxOuJrLZiiMf0WYtY8txwOQaF7ofaCrVSMLT1xS3mvnLaAY50UpAupD_7ZW6rg-XszNyOt69qtY_m5Jup9hTrA_3ZGSCMVPKXXYiCT6lmq-rxnjO_fXPrL4HBb-AYUN-a9hpaHdQ-sShjjV3NBdcoKO8_VNzEb7L4uJexlsrVWO9tkxtTR0iNykUzsOWRHJS0k2JoVTrcqEJk3t9ApXvUZUz3w4aCy9HsykrwOL8yL9GSlN21tVwlCRBhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mLb-vCCAk-y8UWVrEgznpp7uN6D9T0O9kbXfD7yzSh-VxU7vD-fdNDLAbxhtWuDeL5YlMcII71KgNaxubtT08jWrqP6WxOuJrLZiiMf0WYtY8txwOQaF7ofaCrVSMLT1xS3mvnLaAY50UpAupD_7ZW6rg-XszNyOt69qtY_m5Jup9hTrA_3ZGSCMVPKXXYiCT6lmq-rxnjO_fXPrL4HBb-AYUN-a9hpaHdQ-sShjjV3NBdcoKO8_VNzEb7L4uJexlsrVWO9tkxtTR0iNykUzsOWRHJS0k2JoVTrcqEJk3t9ApXvUZUz3w4aCy9HsykrwOL8yL9GSlN21tVwlCRBhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=BBm81QPHgniJTBlh-wFYVbcrZ8euNPd0p4SuLQr0aEMdLVLmNNJ0cIh0AsodaHsM5td2W_tudOcaZeUD6DNvoHa2ZWxGrn-RqLbNXceuObiHb69BtGpY-q7eeyZ46jDwjCafIss4XifcWDRaUghjLKXSI6rswpB26T-zCaVpL65gakTHJ0Y452Yami-g0i6ajVtmneClrdd89SL15DbcP3f1nV9Ufzo3zpLq0lfHc_ce_qMhQGxUCpt6H71yI_KiUBTkLbqTZs4Gxz7ZUCKWd75JU1b7VTSqaDgaKO8dCyyMXR-YNu_nemEQCIA5JxEJjGMQwEO_rceYqIqN0CXHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=BBm81QPHgniJTBlh-wFYVbcrZ8euNPd0p4SuLQr0aEMdLVLmNNJ0cIh0AsodaHsM5td2W_tudOcaZeUD6DNvoHa2ZWxGrn-RqLbNXceuObiHb69BtGpY-q7eeyZ46jDwjCafIss4XifcWDRaUghjLKXSI6rswpB26T-zCaVpL65gakTHJ0Y452Yami-g0i6ajVtmneClrdd89SL15DbcP3f1nV9Ufzo3zpLq0lfHc_ce_qMhQGxUCpt6H71yI_KiUBTkLbqTZs4Gxz7ZUCKWd75JU1b7VTSqaDgaKO8dCyyMXR-YNu_nemEQCIA5JxEJjGMQwEO_rceYqIqN0CXHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=DLQfIoVLk1Az52jjuDXZc1L6ojav-oGyoiVTCFC-JBCRx7hrAjciHCngCIm1kZVmdptEz5N-LyH6s8Ub77Q5OyWwbs51Y3Gmu-IXcI5taDDEqwgv-jKa3EfBWXRL4ugnf4NLeWSsc9acR-SF0Wc2FVjQoSspYSfbf0WCD7Ca0KOoB7ujOF3Jr8it067x-GP17dIGSqTC0JPawS2NenAWGMIJLeqd94TijVfXDGssCVDp6C3cGxDvc5DomyHrID3lZE7cVKwLiIqfJol5mK43JAzRqMDShh8rwJXlZ2XXlOD83ehGtgxcM9EyjKQNcApsk22AkdsBwcOInAjYUIW_dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=DLQfIoVLk1Az52jjuDXZc1L6ojav-oGyoiVTCFC-JBCRx7hrAjciHCngCIm1kZVmdptEz5N-LyH6s8Ub77Q5OyWwbs51Y3Gmu-IXcI5taDDEqwgv-jKa3EfBWXRL4ugnf4NLeWSsc9acR-SF0Wc2FVjQoSspYSfbf0WCD7Ca0KOoB7ujOF3Jr8it067x-GP17dIGSqTC0JPawS2NenAWGMIJLeqd94TijVfXDGssCVDp6C3cGxDvc5DomyHrID3lZE7cVKwLiIqfJol5mK43JAzRqMDShh8rwJXlZ2XXlOD83ehGtgxcM9EyjKQNcApsk22AkdsBwcOInAjYUIW_dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=F_RqNgwtXlIaQtlb--i5pktj6g6LGWOnqnZwjrMpJMFpt2zcUUEMJVjzBeCdP56G9DDN7r0zbsRM8UTtQYvM9RZdhxFxNwoJHoAST12GkmN9wrtr5zyFeiO2TCpixtt5F9qOUMABpxIQHulKNvfHSfesyQs1mHSPG9MpfCSjtuVRXMA6iqQfuSnWhQz3Zsb6ORcjdLNShtfMUkfEgLewcfBAJhHMecdXQQpBsgX6bPcpoNGDq9c5RrMa1gtpm-fcKdXrF_bHdibP9iucBMT9ZyPatJDkE_xBcxOSQ0I5V01Yfx3eWaC01chO6fcxKlBL6VVzEYyDkTr6bp9DdUNE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=F_RqNgwtXlIaQtlb--i5pktj6g6LGWOnqnZwjrMpJMFpt2zcUUEMJVjzBeCdP56G9DDN7r0zbsRM8UTtQYvM9RZdhxFxNwoJHoAST12GkmN9wrtr5zyFeiO2TCpixtt5F9qOUMABpxIQHulKNvfHSfesyQs1mHSPG9MpfCSjtuVRXMA6iqQfuSnWhQz3Zsb6ORcjdLNShtfMUkfEgLewcfBAJhHMecdXQQpBsgX6bPcpoNGDq9c5RrMa1gtpm-fcKdXrF_bHdibP9iucBMT9ZyPatJDkE_xBcxOSQ0I5V01Yfx3eWaC01chO6fcxKlBL6VVzEYyDkTr6bp9DdUNE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=koo00iQs-E6bJWXJ1O9ZwDOYFKR_RFL_m3WFoQKFgM_vI4y--ajW4wzD_k9Ndk1s9W4lptqPXYWexO2iOuQ7k146poNSfvbU_4d94qSqRJfaZ8WuUr-GvgLTImKik7wJnOdjB4Afd40f-Hym58W73EkiTohTeuNcQR90etzs0L_WH4Wkuwa3o_eOH-Y4RcGgkpA3BKMUTW_A8-uq0EXj2XSPL-a5WsCip1Z7BwR3AqTj-0xTvUVELI34L0gZeY0CyHJuz3hqCuwqJt0y1lE_RQ2swsci1IiNUG3uX2B3ag7srfBVxD_m2FGRatclT1mlhTrlslEPanYZiw2ezKlnJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=koo00iQs-E6bJWXJ1O9ZwDOYFKR_RFL_m3WFoQKFgM_vI4y--ajW4wzD_k9Ndk1s9W4lptqPXYWexO2iOuQ7k146poNSfvbU_4d94qSqRJfaZ8WuUr-GvgLTImKik7wJnOdjB4Afd40f-Hym58W73EkiTohTeuNcQR90etzs0L_WH4Wkuwa3o_eOH-Y4RcGgkpA3BKMUTW_A8-uq0EXj2XSPL-a5WsCip1Z7BwR3AqTj-0xTvUVELI34L0gZeY0CyHJuz3hqCuwqJt0y1lE_RQ2swsci1IiNUG3uX2B3ag7srfBVxD_m2FGRatclT1mlhTrlslEPanYZiw2ezKlnJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=KePFjL3kKeKejl4s6rk3NSKI88a5j5q59zL39UgHjdtkdzf-_AeV9BBTY1aRsOSKTyhLltVLAj1m43Ky6iLGBpv-5cl89QXBEloz98WvoPYqXDcag3-Z6ZMXz6Ao-XfS2RxkDUU3XEbyGHuSEIs5vYzCUJm_CYbZI2a2u9LDwgn9-u3Np2HwN5QK7HkCodXQxkuQYz-eArmXaxi58ibTCiwvba84m97qLtBWK0SY858o66k3PZmhAvOgj4zyhlecR1cWYNj0WF8c6rHoRmLCVEzn7K9VagwK_Np_nX5Ie65nQYeC02swl_bUSZMhetM_ueLIIRbmx0ghxJf9k4Dkvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=KePFjL3kKeKejl4s6rk3NSKI88a5j5q59zL39UgHjdtkdzf-_AeV9BBTY1aRsOSKTyhLltVLAj1m43Ky6iLGBpv-5cl89QXBEloz98WvoPYqXDcag3-Z6ZMXz6Ao-XfS2RxkDUU3XEbyGHuSEIs5vYzCUJm_CYbZI2a2u9LDwgn9-u3Np2HwN5QK7HkCodXQxkuQYz-eArmXaxi58ibTCiwvba84m97qLtBWK0SY858o66k3PZmhAvOgj4zyhlecR1cWYNj0WF8c6rHoRmLCVEzn7K9VagwK_Np_nX5Ie65nQYeC02swl_bUSZMhetM_ueLIIRbmx0ghxJf9k4Dkvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=QLfgjpYzLKepSIy-jR3bsKYOplNmsP3kfUJ2Q6wLFA_kive2-o67RnMRU-l1neqesvKCRPyyHSLmv264r4ahsIu9Ub_aHobgEpFx2raRl2zSZQtgkpNeOWGYMnp5JLP_NyP_L6Hp5eQlAmL7zJvVYVFkh9p8Tgc-9_Az8bCzzEDhg-F-WA4lVAZf0NXoqJc_4bx3eqFGzPxTJ0uCjRc8K-n9IKwc61v7V6RAgy7y_05Ktjf92uUfmi_CPSuIeVh-DE1gfEbBgNv3eZRPaP7mfSkSQyEnHI5y9RLICanVXETDhKqvHZVbrJKpmlO2YZ2jtifynWAyMbX4ls8_x_5_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=QLfgjpYzLKepSIy-jR3bsKYOplNmsP3kfUJ2Q6wLFA_kive2-o67RnMRU-l1neqesvKCRPyyHSLmv264r4ahsIu9Ub_aHobgEpFx2raRl2zSZQtgkpNeOWGYMnp5JLP_NyP_L6Hp5eQlAmL7zJvVYVFkh9p8Tgc-9_Az8bCzzEDhg-F-WA4lVAZf0NXoqJc_4bx3eqFGzPxTJ0uCjRc8K-n9IKwc61v7V6RAgy7y_05Ktjf92uUfmi_CPSuIeVh-DE1gfEbBgNv3eZRPaP7mfSkSQyEnHI5y9RLICanVXETDhKqvHZVbrJKpmlO2YZ2jtifynWAyMbX4ls8_x_5_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nfGgD2ulUO6ooPGS5Ich4RwAyE_CFQMv_GGK-KT1gsDNJgePKo39zHGU-gwFhqEDIGC71kOYKRM2db5vNAn24R1SGgS72PutWVQ5AJfSaq7CQ7yDgrRwSd5KDlQNo76HLUv9fDqXlw3GzCaLo0jsdKhCbSqlfW-nIUwNJ8poMFAeL8449-0KjTOBwCi2zKpOmvIeFCVNfmhFHIAtvyBspg0tz_Al66079ReUO2rPgGCMAqdUMjp8ZiKexCj6Rix-VkPgQ3AsnoId-HYMIWaAWpiYuTFpvE3vTXavI7r5Dlng6Lq9mD6pirtlA8tMzLJU553_YfKB6gZCSBePzSKxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nfGgD2ulUO6ooPGS5Ich4RwAyE_CFQMv_GGK-KT1gsDNJgePKo39zHGU-gwFhqEDIGC71kOYKRM2db5vNAn24R1SGgS72PutWVQ5AJfSaq7CQ7yDgrRwSd5KDlQNo76HLUv9fDqXlw3GzCaLo0jsdKhCbSqlfW-nIUwNJ8poMFAeL8449-0KjTOBwCi2zKpOmvIeFCVNfmhFHIAtvyBspg0tz_Al66079ReUO2rPgGCMAqdUMjp8ZiKexCj6Rix-VkPgQ3AsnoId-HYMIWaAWpiYuTFpvE3vTXavI7r5Dlng6Lq9mD6pirtlA8tMzLJU553_YfKB6gZCSBePzSKxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfAPBqg--Bh_uVUpwL-mQbHUnfq2sLAeFjS8Hsw508rfZ0A9f-dgAmITwl6tsu8HiETonHLCQ4COy3YwPI6XxbDh_SzKSlhQBIxKb6ubiCciVcuLp-jymkZuSh-Su_EsjQA_RY-xJ1aJmpQ_DKXjwPHiaf03mafM7ARR5ohf8WigrRg1zQwKqlLn41IjqIjmnmHJkQV4AcFwoag08T0b09TpzA_6_eyQB1rEJ51-bNeqtDrh8QVyqRQSgcFyc5exUT233TS1a_rO_3tf4Vfu0gwDCtLkzWQ0MZi8eygn1Sgde-TiCidHFqR0r5AV478hsykVvDh1GjRd2DuURX36yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS-r7y7xC6TgPj97s9JtzMCfgf9jTJwa8aBnOMubSgBRB6xBGF_j8u6iEkL2ag714JicQn-qa0c8yRhiCtRTOlUEAn9HZMHWzET32Mv9PjW-JyyoKJdQY6duPdXqWZRSumt2YmVRpX3XFPfaKcpGXiFFqXsDwsJRXwiblvWC5DNy_hY_brStkML8xbNC7Zr3G3FvGbsRWKOWFdwGIYGTCHX1D5R7AYSPgHvRM7NC1hGEHK2rifIuddW4tAh2zVnTV_dw6oS_jAt7tI5DWvcuN42ldECTLGTjEDWk1-T-YRuTBaBN7FkROs6i9J1uA7DwL4YA_sxa2BRIEgx90TEZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRVNgPCX5y5XUsqvlta33VuQPoqn_6LdThpTEQkAuIEV6EH0DzXJm0p1gBTzzJ7iNHRrovNPXxcbsC5vIwWeJBX1QrHg83BraH4J61iTSHfHaZ7MOCKoe8UcP0RCEEnFUmMtPFYblg3yTF1wABbBRnnsKWKDpY5EOeAy7PR2Z1zNQKPf_-_X2MBrFwTmsljngzVqxe1SzmqavvYdlH5CQ27_OVE7l5z6zcR-RzneYvnjP-1eKo-ueTavPWmHUPOAx7ANGUcmhVHYEoizAdAz_vmafzKDVmsSsmx93ImTBwrIYhXLtkIJzpgMMscv3l_FkXlJ0P6Iitx5CD_lLFdXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfnGZ03aHNIFB-dX4nGcdIEyxHYwv1O8SU4-j8Fcjihru1bb_MyashVd-5aDw84vnOInwFJo57ExwepjUBVzSrFL0ENoFwr_EwZPBnCYYafgOeJCokfmyQ8wLJSP3gv9i0cXagnsYY9dosWQWuS5kvhdZmcQszTSUXTaPB9q6PwsnxgDJ5zJMw7h-tXf-D9hbRhQDpjEqZdpN0c_TVf_fqF6gXyNnTIuk3ueyxMSbgNIkgXD2Yq2X--3ZShNbdqSVPy5lVyK5I-ez8uGZcEaH5IE9p_xuVx2mtHAEFRVZSsHIbVR23zfozKQm5bICPbpTM9JZ1Ej1Or0Othq7140_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA0y2iGnN3o7bjHReZB_XCjeW4h0fmJt8cQngjUf7wGuOFVLTmfOms7o0aoElvn7A3Qd9VCziqmWh_NFS-AaCgihKk3ngmZNP_NP78znm5Vcf5Y37QKz1tU9mCnp285x5VcA6odj92eZPb86X0yyG0E3tnlWEFGh2At7YyQNJNAj1Nmc-ZJLWcqWmkLcgeZyJimzYumOfdwV877B6JycqiMsPaSECPYry6s4t5bbufxfryoVhP_5SPj0NUEP99J04YqLUJ-BD7GAibwq7Znl1pqO5p6V_8B8e52_bKVtele44ORvUuQn_VQCPGfqPLSmEZbOPnAivZVzGEsnP_kJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgJvHyBR_VFHo5rmwUe_1c1IO1EeTM8Fr6_BQEI1jDqdvg1LxB36UibYtSqw7bnCD4Q7TOFBeQG6IOqGvXc8MSOPB87zCTGJ0th0R-5KE7oLh1xQLBUA4MTFdEVXXIJOK_wUqyAinkFkNauxYQG-lySVW4K3TUYiLm0QyMi6cSG1HibZvlwh9mh3QOw8_wh-cC4psoi117_7mJLOTZO24l4ZwPY0xsBXj9YrhSEKE4qEQlXVNMe1i-9BFVHn3AxyYAn0F22nwX1CxkeiM9NJU99j8Wz-ow7_zxoxDm_faDgQ5OUTKfmNkzK04oJ7MPYimVIuhP67kKEBnwfBsFLFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=gMw4V4wypiQeIVOm9AsyPIpV8-C5ZqWRDgVpCsD4x5oWwaoCuip0VC6ukGbGDE3YlwDgOV69cTpxmtmg6ZxL2-_1h-s8g4kSGX191MW3NdzSlip4W7EyQKW3qQcrqjbx3WOtLzzhHVLd3EzVe6NQ615w5DdiCv_N-XROMoKfwbmtLmJl2S-LZonO6fKIMhyjlwK6pOG0Urz_tTENGie_hu7CS3zVAvvne8ouQ7nMiGyJtsij5-CltVjD7ccqEAWk71-qpd5TbjvA1oa5mQRmKaSEj273L-pta0V0_M8eBJpENAUIDrliOb29QDQMhLjau1hG4XUmFcq-XIZhRqjBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=gMw4V4wypiQeIVOm9AsyPIpV8-C5ZqWRDgVpCsD4x5oWwaoCuip0VC6ukGbGDE3YlwDgOV69cTpxmtmg6ZxL2-_1h-s8g4kSGX191MW3NdzSlip4W7EyQKW3qQcrqjbx3WOtLzzhHVLd3EzVe6NQ615w5DdiCv_N-XROMoKfwbmtLmJl2S-LZonO6fKIMhyjlwK6pOG0Urz_tTENGie_hu7CS3zVAvvne8ouQ7nMiGyJtsij5-CltVjD7ccqEAWk71-qpd5TbjvA1oa5mQRmKaSEj273L-pta0V0_M8eBJpENAUIDrliOb29QDQMhLjau1hG4XUmFcq-XIZhRqjBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=UdpxSYG93TsiUOy5gvB6pjhvDyAtP-QabCLlcD3vqy3hn0tgV-6zwb70_SRs20aUWBcS49yhg5Aeh5MyPDrvGv5yR0iKVH3SWl75Sc65lh89wV2rWS07dNJK3KZC31YL0ey1FPi2ovLhdz8U0z3BvU5l6k0yFO1GvInY6S-4qyjM_yGpjB0EjTrChGv9eFvL6taiSe85XaE7Zbyp1xc1yGgwq4476TTG9_38VBkUxM_qo2SV7DzvV8a4L9FdqHaeGZ9Tbo0-Oi6PEUVuIKn7tS6nMINU4iV77E_J5hvBn_T5Ju3mz2ScN71lxnIiNRY_MVi1RZJmB2fpUbybhiIwKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=UdpxSYG93TsiUOy5gvB6pjhvDyAtP-QabCLlcD3vqy3hn0tgV-6zwb70_SRs20aUWBcS49yhg5Aeh5MyPDrvGv5yR0iKVH3SWl75Sc65lh89wV2rWS07dNJK3KZC31YL0ey1FPi2ovLhdz8U0z3BvU5l6k0yFO1GvInY6S-4qyjM_yGpjB0EjTrChGv9eFvL6taiSe85XaE7Zbyp1xc1yGgwq4476TTG9_38VBkUxM_qo2SV7DzvV8a4L9FdqHaeGZ9Tbo0-Oi6PEUVuIKn7tS6nMINU4iV77E_J5hvBn_T5Ju3mz2ScN71lxnIiNRY_MVi1RZJmB2fpUbybhiIwKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=UmLmwScO6BH4DomY4vhSJZ-6F-FFM7QlQILMN5zqqMdYB_viVz8TJWImp7a_xLwkcQsV7uKA6EFIBQtLpxIbqaW1AGa-ZM8Fg7oYZkwxTSs0uMqV3NwHGJ_fnJNOumGlq-Ddp9vS1Us0gxzYhG1HomkjpkrGTgImaLkljtYP2hKtVpO2YoWzSmKiO0DkGNUG3EPpr8RVaohvNs8CaP28VAAdUMclXaG4aiAXVc-kRrM0AYtfbCDbZCSCKU1RWT_qXCIYPh9VW9nojY-e_fC_6jqmrgbOPWMgTXKMsNQ6gKwI5P5ZhtNPzNj4zZGFOTy6-FZdhMuGLLQnIIVVd2bMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=UmLmwScO6BH4DomY4vhSJZ-6F-FFM7QlQILMN5zqqMdYB_viVz8TJWImp7a_xLwkcQsV7uKA6EFIBQtLpxIbqaW1AGa-ZM8Fg7oYZkwxTSs0uMqV3NwHGJ_fnJNOumGlq-Ddp9vS1Us0gxzYhG1HomkjpkrGTgImaLkljtYP2hKtVpO2YoWzSmKiO0DkGNUG3EPpr8RVaohvNs8CaP28VAAdUMclXaG4aiAXVc-kRrM0AYtfbCDbZCSCKU1RWT_qXCIYPh9VW9nojY-e_fC_6jqmrgbOPWMgTXKMsNQ6gKwI5P5ZhtNPzNj4zZGFOTy6-FZdhMuGLLQnIIVVd2bMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=ZDzxGpTUq7T4H8Wl1zUwJn-GLniso2M_D8VgnOWFxcclmZmKvUqXOrmdnzpUL-KaLGcg3PnbepYciFA2VU4AbVTi0WJLIri0d8GpunvF1TRj1b6firHY22GU8-ESBeMefmwTRXF9OUUS7ZS3aeoGJyBNzpG6fo5FuycwruvMVdo8pGwSqGLNPvvHeEZPZDgobq-ick7lYCOV6L9yX7ynF5EUY7JrObF1Ks7z5NT1yHJugLcf-7qLxWtk_BkO4aNLnYL9SFqdosf9rBt-uwBa0UY0J4uRBD5z4ZJy9Fi9fDade8ugGbz5OHFK4wmqRn4YIEj1kzO3uhZk_JQKaWQS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=ZDzxGpTUq7T4H8Wl1zUwJn-GLniso2M_D8VgnOWFxcclmZmKvUqXOrmdnzpUL-KaLGcg3PnbepYciFA2VU4AbVTi0WJLIri0d8GpunvF1TRj1b6firHY22GU8-ESBeMefmwTRXF9OUUS7ZS3aeoGJyBNzpG6fo5FuycwruvMVdo8pGwSqGLNPvvHeEZPZDgobq-ick7lYCOV6L9yX7ynF5EUY7JrObF1Ks7z5NT1yHJugLcf-7qLxWtk_BkO4aNLnYL9SFqdosf9rBt-uwBa0UY0J4uRBD5z4ZJy9Fi9fDade8ugGbz5OHFK4wmqRn4YIEj1kzO3uhZk_JQKaWQS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiFgwMieY1m6gogrJt6NUMpK-gzjNWkHcGjeIm9s6qiPaw71xAD-GbHpxWUfA-vcUv2VM59FWqqJhSZKfYq85qbNVxx7v7wfVUEwoE6-vEDFnkHCY_QdEVa-K1sGcJEXmxqlzkLk0nC6iUYbLGByyNgZfo-Qf0Gv3rUJO47yyKdnLAHQ_0qR-wcpYrZBcHzhi_ArmaeAp4gzsbjKWJq71EBjlpVKxWPkL01IQpQb4QXOXE469zdwFVmAJjcY1JCrMQzJcTweu-vjkSMaMU8NW_gGsrmSEYy_tXpvyRXwfZtFyom27Dv1YsXeLVgLzQWa2P3esVOs6cc1GZHuxB3WZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
