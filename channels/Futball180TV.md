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
<img src="https://cdn4.telesco.pe/file/IZgFYV1Q5_nQsn5dmYSDx0WQtMMPmzET3ggE4V01UXwBL_JYrkByZjdAuPFLjLJaLZqReprC_SWaTF0_bx_-NOCIIH35g3u5HUWW_EYSYd4RGwVQWW7Dhf46IUhE2JPatGZbiWMJ_FkRwrONoDFoc8XwVl9lWxcHAduYSpOm8xlAturOYXY-dP7uABF9ekzp8mhYos_jwrgT-Ov4ZhrYiE-x423BbxDJt6MWTJ98DoEL7bJX8hgvMsLEQTVJl_cJ4jk-RXM0WI21svxAggVfQl2uwxWzURDPVtBJF32-rGLhFlNwetOspN0-fDKED8vFL9ElkURnoIc7XZ228G1EvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 125K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxT6aj6UXE_F93jeoilM8jP4El7OUgoLdsbFG20Mi6mV8KYmTDvvsnbA04pXSdpDa7WfW8AKaJ3c1pDtRG8c1Bf6OejUKDBHSqDPP80y4Kq_B9Ij76HkyoUc0qP_DBF2QPjnxG5VgwPw76stp-1LN8t8oE1Gxrg4hvrRZXVoFJHebfp3G5Tabd6eW0MTJZhpxGgW814gqgU351cMO38GXrFP_wu9fxIPAMF01Wtjht8IUFBSwmQEioXYaD-8ugTt0cKt0A9lCArF99O9MArjVgJTBzs_oO-nIWqKRkzTGlCCccmX1b3Q3ju3MD6wcTd8QInWBF8e8Ps0X1tcuudXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLJdzcvDyb8E0n8Pr7FH1jNHQ1B6BHJwX98nK6ZVAuf7EyvtzbBIaGW-5J0QYK9xqpaqdih2Qz3VoftFEW-QdnA0sdLqD6AsomntC6Azr35TuodTAdwEiJ0e5QSApDKqTNA35jFG9vucaSoud3Hpvfb-pn7BRQ_rHobPn-XDSX03SkyLj0N2PXMj5HASomUEwQ0RJvFvb5cK8WXHxM_arJZXzykXc7vKFSv_Q-QBHql8beO3eJ5qVN5npcdrwT5ltIsyMT3VzRAzunFWM_OdHj4dwgz-OabWs_deIYZdj5yhm6_QcYpTs9-DBnCeaWoP61Xu6iJ0EhVPphAQgztnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0e6MZtwTp3OsNdu2ob7pqlesHH8g6uCYZJidgSawb88rOB_buoUAh8RqDcviaiJ6PpbYS_3cW3i5PsDs8XCZTx79xBZwCdyED7MGS-jL83HCcAHGoQfeSKCF6qHR6hVxwD5nMHV9DOhaivDoQdbybpFrjQP7BELDWxIVh7w7biRxJL4PzY07mruF5HDWgmbylSa9DfDVSgaZKyyEXAuMOELMeYkGw89HuJKSJt0sfrRolMGzAoqtEreAIreXgrogkf8xCBTPB1W0kUZfz-1t_Sq_cpnNsEY0weD24NfCw6KENbQp0Ko6ody4coKe6YCWGJat-FCyBqS-lQ_QJ0hDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4MOMxwtYBQA74Uzo5G5h9iOA3dthJGRI3rk5XmoQE13PjYVNJFQqDO5keUek80MiqmZ4hyXf45DR2ntz9dXKC7rk4qG3c4qZyvk9jKDuD2iSQmddrapleJbGZyzUIft8NKQKT1D4GXCWVTccMHjVCft-KysvFeuBTIEKcsRSMD6-7LDGdyXzT5yAMgstgH54rgsPRp0goyJW7s49wNmuQA4mq41ikVSMtSf2F_qjraqXc21YsK2ouMc_0cVX4u5Uc36uwkhY6UNrHknn56C4CfKC-D4vndZdW7fu-1vHnfSuysTUs0G5TOGJKF8rzOQnqwUIfm67no5T80DyEdWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGL69um6NUdbpOTiZCih067x5jPAMApR-ZbO_K5KuaXhDNGk9A4AAdW0fc5YTXU_PXvfWAGuSLmywTt4uhL6MBYObqw_M5OTOzEcyLkIW01sKxgY-fGeJY55oNvzztProIW9x_FnkIIBvczYZPSPByoyCp34O_wXxdS2-PBc5PoMYFZgiIlAa9JkcGXjtbzM3nKxPyiVWfXn_CirnTQASR8dkNyf8hnzADKv0ysVtrt-oKZmHdxPLS4aSAQyeejoVssNL4kogpEEEV934cW0KYGspkcRfZEhe72zGVSpIwoEgNSMJH6sSUeRfsoNXST5qdL7w47KqYRbLmjpxolgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQk1NKMDRFt0J9nq3ByaSt4-BpIeIhX-iNq_eTJ1V_sU2TJsApkwswQUu_hqQ_Af8BXlO0ZapHwo6th9oDO8VCSCDlG7hErFl4JNPuEmfQ3OQkKm1rSBweY1xHUVHs1vCWWTyEReri79ENsdhPxDDNjxhWtD6lrRt96usQZK-0qGRTWrKLrTzsexXtlTv1qtMFZu_RP-FDHvtoLiR4HCf3UOMGz82oRy60W5uuQ2GNAGDtIoCKrxzgtFhC9eDAyqaMwI-MKC22fYca9TzDAVqEcYq4EmPZ7tCV3WDzKUG-rw95yfqNlUEu3GOObnkefBi5cka9rA_oFoWckEEF6wgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOtnfsdVBul5-2aq4i4MULShb6MnvLTIk7yAmMacvi_mDAgL-Quwr_T2fxC_Debv9XxhmpAgaWi5RH2_M2T493rA7I2_2dS8JhmJh1QSBQgCbDZgKoGbXdY5OIn46lRIKFAQVtS1nxiRR_j9hErZWxp8leVY7aY0dbGNMrJY6Dl3dOyXfl5OFw5CLT8q5boQO-oaNBR590WVENsFACeLt9YLQHjxVjkbSp-Xe70on6QwlELhffLv8v_IpoGqALCrJWVEoPCRXZCGm_DEtmkI_nXxqy6v53jJiMBZyQXEt2Sb7sX2rknzpTrnc16u9bUEFtkEMDpGyQxPdRQjy6w0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=qdNxl4TOTlfXIlUHBb1wGdwG0wPG7Mqn-sHVjr0WJjDXmUcVv7EQ2zo_unGTbOS97FJ59z1Ca0qvHh37ONCB9i67ERtPC9paMXHAm3Cg2m-3oVStOO32yXuzbv9aIxNZpaI448kU0k40o33tch7SPN7pD_Bn-bf_VAcdp6nA_SkwoVfpxCYOKo8F3xINXQpMiAqD9GQg2KC7kjjotMggZw9D6fMNPHrpVoQ1ul0mJTpxY0Y6gvMODs8ep7Yv4OKbSc5d28kkMYC_wsjs1SzdCgKD7w1LlQa471_XChgrS2NgV5LivUBmb31NoluZDffk7nq-niUp6HN2tEyEkwJy_hA1rkDa2XyWwnFu58TNInWy6T6KDlZJR7i6Bz1Zo8Rhbs9lhlaTLU2MGCwm5idfVfyo7enS80SI9m213DcsK7Y-pzV8LMqjx0eVZHAMh1lySb0NGAwxolz0CZt9aylzI2D9LSQQwOHAvoOSH4vIWQpGGhx-cpS_nyrqo9qQHo8DQlgeAX85bKAl_DZx3bf7qXXPtcRo5HWFk06E7QR9pCM0IlDVf_Lf2MDuT01zVnJpCQDG-imtZSRLaJbs5D1UIHGwobTaHUns-FbZc5j4O7JvMKG6FWOk-UKepFQvHh6qK1v0GXptzhphkaHDxbXB9w-u9c97DNUNdIPe48EqSzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=qdNxl4TOTlfXIlUHBb1wGdwG0wPG7Mqn-sHVjr0WJjDXmUcVv7EQ2zo_unGTbOS97FJ59z1Ca0qvHh37ONCB9i67ERtPC9paMXHAm3Cg2m-3oVStOO32yXuzbv9aIxNZpaI448kU0k40o33tch7SPN7pD_Bn-bf_VAcdp6nA_SkwoVfpxCYOKo8F3xINXQpMiAqD9GQg2KC7kjjotMggZw9D6fMNPHrpVoQ1ul0mJTpxY0Y6gvMODs8ep7Yv4OKbSc5d28kkMYC_wsjs1SzdCgKD7w1LlQa471_XChgrS2NgV5LivUBmb31NoluZDffk7nq-niUp6HN2tEyEkwJy_hA1rkDa2XyWwnFu58TNInWy6T6KDlZJR7i6Bz1Zo8Rhbs9lhlaTLU2MGCwm5idfVfyo7enS80SI9m213DcsK7Y-pzV8LMqjx0eVZHAMh1lySb0NGAwxolz0CZt9aylzI2D9LSQQwOHAvoOSH4vIWQpGGhx-cpS_nyrqo9qQHo8DQlgeAX85bKAl_DZx3bf7qXXPtcRo5HWFk06E7QR9pCM0IlDVf_Lf2MDuT01zVnJpCQDG-imtZSRLaJbs5D1UIHGwobTaHUns-FbZc5j4O7JvMKG6FWOk-UKepFQvHh6qK1v0GXptzhphkaHDxbXB9w-u9c97DNUNdIPe48EqSzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh2O1SEiULrXLD1HzZo5PpDcAi5WGw3ItSWdv5eyhjsJs5kEdatjPMWvSzu6IXVY7SR5op_eXzYq7kB2HYwZTtKC26okyTDyHswzAzGP_aJnmbbRExnItoqPkhz3VzAFnBBPJr-kAiCESzsEbCK4D4eP4aYyBuaxIE6Nh3fje7sHzwXSgCdMHYcXMvT0Oy618sPtmyQ7i3xBGOWpL-nf6VqaLY5jqPumJ9jgYE3ADpML2I4_6JJG__aHMmDKvFhZD31nFjOAIvoEVm2F1t40ZZAaBpS2lbDkBtxG-VjUkH1Bn94myiRAbwAmzBh_f8vjsyhv_CX0jc3zLjkxI9AWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=pxQpQPvxm0RHnXxkEu7M7tNjuXqtRmaQBjphwnxMaSm5XZw0Ai-KP5CU9Bjn61o1uC9wuLuHbMVH1Z2bZTKVzTlYXWJbzd9Z7dASbNWDHH7PQ5rsPUF67NSrxzGENX5Y2QLfkjy2Wx6MEXtc8PsB-DJqLRaom-Lz4EcxR5nnepX_91zAyHak4viXwMjUVFiWgqdv7IlGVRs6Km4fAxwY6vHXSKy4ZQ8q_2Nua1qxuUvDGCBABxJaQwxBxPe-eIL2OkqiXLxjY8VCvNMxLaMByyDupOwIwxXVBI79IrnXu-tMJpJuB4cJYzDw5dZwY72Ypa6Tv9kPQNMYJc-lt2pUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=pxQpQPvxm0RHnXxkEu7M7tNjuXqtRmaQBjphwnxMaSm5XZw0Ai-KP5CU9Bjn61o1uC9wuLuHbMVH1Z2bZTKVzTlYXWJbzd9Z7dASbNWDHH7PQ5rsPUF67NSrxzGENX5Y2QLfkjy2Wx6MEXtc8PsB-DJqLRaom-Lz4EcxR5nnepX_91zAyHak4viXwMjUVFiWgqdv7IlGVRs6Km4fAxwY6vHXSKy4ZQ8q_2Nua1qxuUvDGCBABxJaQwxBxPe-eIL2OkqiXLxjY8VCvNMxLaMByyDupOwIwxXVBI79IrnXu-tMJpJuB4cJYzDw5dZwY72Ypa6Tv9kPQNMYJc-lt2pUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncP7O5Oi1Z0MEbXTPUOtEOyV58pgfotvQPcrjv-6f8tfm1RBoRRl_ufPGKtKWQp8EMdCKOaYb0XYI8hlhfsB4e9NyBOVvLoatxMnDnvRb_bkDygFUMnZU66dI9M_4k0g-ZPLV6HB9Lb7Wc1_kxHhIkrh_oAXLmmpSY3hr9AvBJutUmAA1aSmS1RdM6A504mtnDIsTsY-vLYmEdn1Kq9sDWjjwKkudBeH34hDH-dwzTSKlnujRbDgl8pFw2rUiIPQqDCuw7WzXkkUu8VG_1fuAb3hh-2uNLmNOnq-tjibkKsp9YuS6b7ShKfjvdGiyz5DCjZfLmoa7IB9HlOEnzMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt4bEe5TI7h2DkyizJaPUaiLjfT0MWx26QkotumHjZt4Ihb5f4FYw2hwVFbnWmNhZxk9Y5jZ_GhBVCTUrvqRMEURkBAzSIb_drlbUWXW_lzbk8FGi11zsRCYagGtPwH5HmyVevVLOPgdafeHDFy3vNvL-DVZLL3-SjCladgfUrlA4w1J3A20GpK60FrggF0-5DH3gmF7VESnERx2_UThk_coYreHGxv2ztzuC4M6Ny419OnIOrldsJVTQwbOHX0PVC-PgnRkCH20Gku6mkAl7RFQ-EszUb4O5F1FtBy7OM-dCUSr9dNRZ0eAliQL6LeHeUuM1LFU860Sfdmh57bE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idxc_ejw8dwFLmFVPOkxKZRLxfgpNtAKbtPsLHRmlzOU5ImokpEPGcgohxcGVzbxlppZuumRJCWat8qlmI9foIruMxsqBg4bBL95veiNsl-UnBlAlEPqzZgZz_532IcXbbpEb4nVNyVH__pb-9z5lV4Cmab6Ve01BTNUKjpiz5WCxhF-z2bU1Y7LjvoaRs2R-CH7MT-8vg6-_V7Grxx0OQVbulERaMgEEZYhwd9hvYrcJ6wwCRv3Ui9KUlcJl_NOp-emvF5yVIJJquCymHQy6xRwv5xhyR2X6D3a5X6VI6CQLz98T73qrtRbf_W-d6vk8sOEzKXOrx1gnNXAQNRXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
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
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL_nUgdpOmViHaBQnEtibc_toeL2jvnS4fXiMk_qhHdKvjz3W9yD4FCD3vNoOYSYqlXKMVJwFSnWTQq-L0ST-YmPr9kl_nLPHMi1fjKMjDdfsiwXgnQMxfOev2sFU8d6HUfbiCwjqaLvnxtCnImEQ-XL4R3tbWuN7gTDy1aBhQnKayYC26SF-cDIpUX4BiPDo4R3a-zkatdWbjjtySUPWKlYjPJxB7e2tU-L95we1mpUPKdgzC0t0J8bp-I8ls9Mgzxtm2NxE2th0V1gfiUB4K7r1XRDU6wFUpqVshoppz-3To2FwC84zU6nFTDlqGzN87q5uEBY-pmh3d42dw5Xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6XxRBo8USJiw5wZeR-XB9Rb3cpLaUQXsO-Gy3-CpKhUsVnKvljmwchMz_YOeqqsPMlVsGYkSqxNWe-74MR8GNwjZl9Uzy57BzbxnvOcSZBeWAbeYJUTrJlFkKorX4a8HrnUcIvZVWFa-aOeQJByMxHlAzZpDRo20dWRIElHcL8hwHqQm1NI4qBT_5_wtvxoqSIu6bV8NfcOQr0eYbbL9PnE4LO9rV5-04Yl-4b7_XQCBqtqCw2T50OIm6tfjunsyyH94xZYDbLp0l0p3_w0yLJmEIjYA02uAxJg-tB1uDa2AmEEa_9pkiRVYetoQq1mwA-T4X-UQFwADzYnIy9Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=Asbf4GVzwv10xa3l8PuiEYk4KUvhmH-2So2IbSI3HHX-x_Jr9ioOJaC_n5u3vmqgSkXdZcg2PccAv6Ha15NqAq99f90W-av7JzJ7OGvUK_bTMGvtAmLj4T1FPgr0vDq11ODrLBKIIIBr2w-URz_xS77kNV3x_NVg50PcRndf9hs-1gFlRFS5EOnoJERBvcW-PsTXqZcNznrZDFw0_rm3D6UTNYirTVLmPNAvt3YruRNm6R-9HzOOhbP71xcDLgjxhfPZbR-OaKIRNhamng7wPMLt8vFYk3WNu-6KcklHiiByUSaPv8tZRxdhJYPfgQIr8GD1o2H_qJDWqn6WlRjiT7nT12PkGzl9iC1_GmS3Z7yg6MJMELuztVU9v9aPCDkDN0FB2RBb8Do5XdMmE5E4ZvUOJwLdcDaOpvC5PTCsWYzUCWcAh4nz7oKzH_Xk8Ls-BORDAqQTtbNod4i6rPchLAk0PRmGDuSdko4cEfotjBPa-40pOWO3AoO6giNbvrq7G7Ggf_zSOWhF-FrmMvjRTp6-ywwrzc3WvA-CyRB1-bfvRl0JGf6DviMQ4LDTL5pZ2keA1bH4pIy_BgpnBfcJzEer-hdgtUFQcOosPuzpONRfJCIepVKJisjqBhBndaSgv6Liq2Uq3zZ_AclqSeN5Q07fAjrDaflCwkGGFQEKBYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=Asbf4GVzwv10xa3l8PuiEYk4KUvhmH-2So2IbSI3HHX-x_Jr9ioOJaC_n5u3vmqgSkXdZcg2PccAv6Ha15NqAq99f90W-av7JzJ7OGvUK_bTMGvtAmLj4T1FPgr0vDq11ODrLBKIIIBr2w-URz_xS77kNV3x_NVg50PcRndf9hs-1gFlRFS5EOnoJERBvcW-PsTXqZcNznrZDFw0_rm3D6UTNYirTVLmPNAvt3YruRNm6R-9HzOOhbP71xcDLgjxhfPZbR-OaKIRNhamng7wPMLt8vFYk3WNu-6KcklHiiByUSaPv8tZRxdhJYPfgQIr8GD1o2H_qJDWqn6WlRjiT7nT12PkGzl9iC1_GmS3Z7yg6MJMELuztVU9v9aPCDkDN0FB2RBb8Do5XdMmE5E4ZvUOJwLdcDaOpvC5PTCsWYzUCWcAh4nz7oKzH_Xk8Ls-BORDAqQTtbNod4i6rPchLAk0PRmGDuSdko4cEfotjBPa-40pOWO3AoO6giNbvrq7G7Ggf_zSOWhF-FrmMvjRTp6-ywwrzc3WvA-CyRB1-bfvRl0JGf6DviMQ4LDTL5pZ2keA1bH4pIy_BgpnBfcJzEer-hdgtUFQcOosPuzpONRfJCIepVKJisjqBhBndaSgv6Liq2Uq3zZ_AclqSeN5Q07fAjrDaflCwkGGFQEKBYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQuOf9zKMtDanEhDpsQz_IxGPuPaK2sUv-2rNWvvUrdXO-M6KMsY5In0I95a-9zB490m7QPfke_2DStvYOFG6uk9fm0sgPwfuHZ5xhFF7c-E8k-TimNkcRMeHsAzdNg6j73dGcyQUkVxKBJ1-9zA22Rsui6knNAAvhnTEax4Xk0YVUx_pcy52iGnnxbp3rshlo_Ukjxj36psT3uxScuVjpmPrGdM59TCtVSZqE1ztWNo1Pabo_vY05yRRu8WvJ2Rnj7Nce49hL1q3eQcNxdv6RS49ysWRvk8MWdtcY0NlDO0bcfpEsqCd0R9wBcGI5eXQd4Hj12L9NiKsySUyMT0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=I8KaePELBoj-ZQeB6JxvMqdDA258fdRnHeRqnVMlhUMNxgvjYnaXjaXrp2O6dXxTbNQj70THBHp_0KnxyJqy_isysYONy-ZpynEbcrEK6wRRLZB_SUguas58KUwpCqGVPg80vsle7m-i4Q3YtmLF21tk-kT4zOAl4SbeaBgW90JVa-VhtHtJfKBF_oolQc2Hr64DAUC5o6AMa74FCEYt_VvKGSBbNJSmO6TUcf-WSY2zRCqlwSVq4dApvMMPg5x3p-LNm7y01FKtgQi9LjSgw_XRIUpu1_EbKyRX6qCWjRX4WABH_q2nuMeu4erTUKofjZKRWWqUaAgV7vLl-9YLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=I8KaePELBoj-ZQeB6JxvMqdDA258fdRnHeRqnVMlhUMNxgvjYnaXjaXrp2O6dXxTbNQj70THBHp_0KnxyJqy_isysYONy-ZpynEbcrEK6wRRLZB_SUguas58KUwpCqGVPg80vsle7m-i4Q3YtmLF21tk-kT4zOAl4SbeaBgW90JVa-VhtHtJfKBF_oolQc2Hr64DAUC5o6AMa74FCEYt_VvKGSBbNJSmO6TUcf-WSY2zRCqlwSVq4dApvMMPg5x3p-LNm7y01FKtgQi9LjSgw_XRIUpu1_EbKyRX6qCWjRX4WABH_q2nuMeu4erTUKofjZKRWWqUaAgV7vLl-9YLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAHjgC1rI3Klg6_5JYdbsGSuO1SIx5WZSDA8muxaknH4BO9x1D7QnoCHRtrD1nFQu2ry4SFLl60WSK97CYczmW4cB8PdYmuPQ5qhuq2nUnPodjtndwyM4Dqre9YccFzzdo2rxz54861NfHcn3M6WO8ul8c2Gd_iD2LLQ2lZVULgj4-ec9xavw84fAlxoIk2NoLsAIQNujLRWMvIsyKk-4rTGKz532EM6GS4JCll4g_nFDflPJ803U1Tz-OpEMIdKBxmXXOt_iWXet7_cz6RNckhxkrKCThfzw7lSyX3nIBFMHaaWFm8Rl_jP7-6iN871aOooud8mxef79ELrZcskwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltYrzwvfHEguGO8sh6AeVhIeOiAq010Owh9udRDJ_L-8WhLSrka4vqd_dWpM2upAaVgDV5piZ_P9NmwN2_H1k8mWakmp50ZHxWtb059ABbvkfRnxLeBdC_U4yyorHtiFyMmkTD5ojB3CEKeczkwFlSO_Z8rrZ-iT5ntHYZ0yt38RM2JAgjvdGIQyEkWFkrIq1luEd80fIxil48CKQ_xBCRRABbGL9c1tEptVRFbjp2UVlxkYVH2ea7Otcp0pkpbko03NUDCfVBy3ETTVIsuDXEkRIt_9bNVkxt0xhTv6do1OU98-6gq7IJI1rwcQC5p_eJCQ4W57nLF-E6CzFp-xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=fhzVUJGbTYIktxEk8DClkMv9PptQx1wbMGXfCjFIj6CIvw4UCU_tZYng9FjDD83cdbIHZhiSgjLzK-FaSaFEkrMuozAEuRElZK00u7-ZceHZpD7hHZQzkSftNndnF4F5hru2nsGArgNWdJSkfq1Rj8zmSw-vEEjR1EOkdqzssRbR0ImqBVzgDbzxw2wx2EzuSM4b2TbENGdBYrMxOyD1aGug4btm_dw6fzshRw7_0L3UKD1nzmNzv4HV9v3Kav5OpDtyEx6a9X3nRlbfJ6nNJJYXOFLwLWQAF57Y_4fE4qcH8WGfT6J2gRITXhzfuNQx7gfoA1jnk1JLfwy3xNAp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=fhzVUJGbTYIktxEk8DClkMv9PptQx1wbMGXfCjFIj6CIvw4UCU_tZYng9FjDD83cdbIHZhiSgjLzK-FaSaFEkrMuozAEuRElZK00u7-ZceHZpD7hHZQzkSftNndnF4F5hru2nsGArgNWdJSkfq1Rj8zmSw-vEEjR1EOkdqzssRbR0ImqBVzgDbzxw2wx2EzuSM4b2TbENGdBYrMxOyD1aGug4btm_dw6fzshRw7_0L3UKD1nzmNzv4HV9v3Kav5OpDtyEx6a9X3nRlbfJ6nNJJYXOFLwLWQAF57Y_4fE4qcH8WGfT6J2gRITXhzfuNQx7gfoA1jnk1JLfwy3xNAp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl2RsmGF_50hUmT_HnqnEVmBDmlFUJmtLyQnzLp9zz9OzdPMbTCmE015rWGvusqtM7fzX8IiqiL54KJEdXvbLHqIZZMJHdwiHe6UjCA5g0Rx9ZmUp3rDHknqxmFXVXDrbefUeGEk6wbC_7rWt6oVRQbWc1UxCddzqOVMH38qnHpNssbNFvDra4DySa0Ldbq5_YOPaU2VTbmMM9rmHvIBZNVYABrZdIpLAItVV9x3_eAYEVCysdB3iTioVfrro6NZpCO0MlrCQHvOcSk8BTQn3hzUr6gW08dkfYhbcCeV6GtmotMvxRIuyRGooY_8Jr_EWgz7kKLQEyO9fj1ko2F3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
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
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=LGu_yvtfb3jfgQHzZXCU10sSXY4HKXb9vvhI329_b_Wf5J4U-8KNWwiTUeIqq_ywpwGer8MVQEiTJmqnZZ6rFSqGQoD-I79mFjdUhWaiEdEtfMYrQ3DLKimK6-22Ivb_KthgS0fqA-IRIGUbKBCAITZq0YL909pxFuDeaxqLwhvosgh-k-D7wEKVLlpnz1pQgKBUiD_h14XYMHaLsBnN_KV-Q9y4qy8aicBexb-CyYp8dVZoe7Z8BcHnLjUctCDQKhWWPIiAHQNeDyGS66NjXv61oBKrbQEyQQdZcfQVdbzg4zLTaOo0Tsx7ueEzw3Sk89YnPTUVDXP_awMf-z6NsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=LGu_yvtfb3jfgQHzZXCU10sSXY4HKXb9vvhI329_b_Wf5J4U-8KNWwiTUeIqq_ywpwGer8MVQEiTJmqnZZ6rFSqGQoD-I79mFjdUhWaiEdEtfMYrQ3DLKimK6-22Ivb_KthgS0fqA-IRIGUbKBCAITZq0YL909pxFuDeaxqLwhvosgh-k-D7wEKVLlpnz1pQgKBUiD_h14XYMHaLsBnN_KV-Q9y4qy8aicBexb-CyYp8dVZoe7Z8BcHnLjUctCDQKhWWPIiAHQNeDyGS66NjXv61oBKrbQEyQQdZcfQVdbzg4zLTaOo0Tsx7ueEzw3Sk89YnPTUVDXP_awMf-z6NsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4l_MlOE7F7Q4CfCv2fSIFnVnyrgVgv5e9BKf1UQ2-rnU0D2y3g3iQP7VrG-6h3RmDxqWHPUqwuhlYi8IH0hL9B8dSPCNHP8vfZiJxx931FVTMzaE8S34lBNqQCh4xu_9HxoOj4sSYoSu-DHUANOXAtYD-4NrFYORfwtRnwNp98oaBRV1v6pWw5V0hQkE11b0zB7x-IS1-uJPHlDLMJl7ihxh84K2nzm139M_ih-4D90Ea3kNEzX7avnR_JoM84BPzwKZzBzD9iwP4Cwx1_NgzJwIARvxQyFetD1wPXZNvigzrlO9Ht4sAo9U4xG1oj-cMf0szhZ26_W9rh42nTyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=U1gMvqtUuCpam39mRVG94NE1C5scI7KkXKE0JkWETjgdN_aSL8RJiFACAL4Zr_69lCI_LyDPNvDtmtCgbuQBY7GHhbpDP_-zsEzX0iOGuxky1Am4kK5EwJJ0o0cB_-ch3GVPa_Y3CGlf4Cy6MHTKgBkTs8BPkhw2ZFG1KBLl7KqqtcWRxeHNcuKpIMO5Qeh84M5VuaSNwrcBwrt5qiADRadyRRG1Dr0jRlHvw-SyscsJwWeFe9MpnbvozQ5oK3WxcyOymXMV8gCHuyWZfdmjmMIoQmACtk8lynJ_LyDla9wafi4VP_44Aa7Bxe2EOUlyTH5nmXyhJCmQOfAeZGz7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=U1gMvqtUuCpam39mRVG94NE1C5scI7KkXKE0JkWETjgdN_aSL8RJiFACAL4Zr_69lCI_LyDPNvDtmtCgbuQBY7GHhbpDP_-zsEzX0iOGuxky1Am4kK5EwJJ0o0cB_-ch3GVPa_Y3CGlf4Cy6MHTKgBkTs8BPkhw2ZFG1KBLl7KqqtcWRxeHNcuKpIMO5Qeh84M5VuaSNwrcBwrt5qiADRadyRRG1Dr0jRlHvw-SyscsJwWeFe9MpnbvozQ5oK3WxcyOymXMV8gCHuyWZfdmjmMIoQmACtk8lynJ_LyDla9wafi4VP_44Aa7Bxe2EOUlyTH5nmXyhJCmQOfAeZGz7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=f9Cee1MSf1891WRmPzUtKl2yDOM8oPqgSaFDvMZkhyiIbMmZW3JF2nsFUDNiWFEdr2DFzYw8d61e7lEsOEkd7uHOWhEvcOtPiVhYmj5_6qTxztko8jgH8-RW2zuKEGV4Ftv9tiiiYSse6Wsoj7iiA2P8YHbp31NIwxvjm7uTw1pPPGzL-7gn3fQjr6bm9oP6Kpil1Z1LA6-2quE74YHP7haoMn59oT5Eslt2E_kzyWr5N9jluziAaB-19MUScxJFXh5w1hxVaMJaSDPszKOFRiy-xaP6WTQsL3sQKUQ16oKi4z523eg_1Eq3fy0vcjFsWiVBEs8BrC0AyUNDu14dFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=f9Cee1MSf1891WRmPzUtKl2yDOM8oPqgSaFDvMZkhyiIbMmZW3JF2nsFUDNiWFEdr2DFzYw8d61e7lEsOEkd7uHOWhEvcOtPiVhYmj5_6qTxztko8jgH8-RW2zuKEGV4Ftv9tiiiYSse6Wsoj7iiA2P8YHbp31NIwxvjm7uTw1pPPGzL-7gn3fQjr6bm9oP6Kpil1Z1LA6-2quE74YHP7haoMn59oT5Eslt2E_kzyWr5N9jluziAaB-19MUScxJFXh5w1hxVaMJaSDPszKOFRiy-xaP6WTQsL3sQKUQ16oKi4z523eg_1Eq3fy0vcjFsWiVBEs8BrC0AyUNDu14dFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=j3fTroUwLSWg9uUWcJ4GBqOBoTHrSTzs0IqbgwLPlsZkk8uCyuuMVvrZMqGICSEMBzFqGIzFDNokCsM2vYUfWF2Rm3WELZtCCbcIaKK07weltyzYD25oICtqCC-iGCxGYt0rMWDMZVguJzZ209l21A7nbkaZccp7aMB-6m8PvlQVstA7XFqx0xzzeRSmnQKO5rMWMtz75n1TFkroawoFORS1lascFQEovvhkGFCew6fhM45UCx---Q0ITvH_B-14kRf-9CffKpCAvbRGYWQUWzcqzfze_rYdCsoTP0ZQiqXz_Bx8UvL4jpsk9xtpSdqsUW0QGKxAKw5m5tFmIJOm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=j3fTroUwLSWg9uUWcJ4GBqOBoTHrSTzs0IqbgwLPlsZkk8uCyuuMVvrZMqGICSEMBzFqGIzFDNokCsM2vYUfWF2Rm3WELZtCCbcIaKK07weltyzYD25oICtqCC-iGCxGYt0rMWDMZVguJzZ209l21A7nbkaZccp7aMB-6m8PvlQVstA7XFqx0xzzeRSmnQKO5rMWMtz75n1TFkroawoFORS1lascFQEovvhkGFCew6fhM45UCx---Q0ITvH_B-14kRf-9CffKpCAvbRGYWQUWzcqzfze_rYdCsoTP0ZQiqXz_Bx8UvL4jpsk9xtpSdqsUW0QGKxAKw5m5tFmIJOm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnqXFuUmeYlOmPTotvpTNlZFBI60hldjLwIs6zrRCH5bgkT589vYbKOOYskBeedaPuxus2HHnIg9lkEtl_gc21lQ82sslUPXVLxCaOHAd1RH9Womsza9UYO55MmLKNbF8Xs-vj-GfzKujISj4F3mSd5br2zHw77J0EvcX3Cebs0HTf--ik9flSKtvWU-eGKhGG8NSYvCaI-aS51lODbPHvQWvFVZR2K2P-pePN36u_fVgLN2gP-KnRVGsz3DyvpBxf-JTtHdhmMbA3mS0jS0oPqAIfrCtxgXF-hsMBcY_74eKYKftLrUeazQeFRW8pxM0cawkQMPzxJU6fgCLdkr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR5aKuAi6Jw7hRpKfSNIO7sM8KSKTisOThh6tXNeN_Lr258nKPt0bau8fZOVIrt2802E1QOhUJhjq5_QFKXv38xDJ0pn_3pQ1sa8kcW89j0PUlJKrR-XEWUhYJANlmdIt_UmIM91MhvxBYirCz4puippqQJbu7O8Cw2sCaXfGHOD185tWphWZFprx3MeSppGpfxbtOXMt8HUriRB7vN6yEX80ciO3wFvzCyo_lFvNekaqvkQMNFXQcPT2W9I_8o-_R8kiyV39glAAiqlxUEVJ25wK7X3_J0kImRunBCo1_A11rd79bzNxRbTzd-l5emnrscGIpUW1qjYMBkenBDvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=tj1iijCZGXdNJqJYubZNA0DgWbrk2OiEypTfVJbPTkKcisH1cXEBcEpcjfTo-pO_j6Ld7FQt3bbasH48DKVXLcd5Ub5I-g5kBMKkAw2vgfUz7CEXNR5ZbN6da-GLdfxIw1SjP4TlrsWmdLur1wb1DZkcnoKwegVLoTMzbIRDdnR2Hd7rnXSg7Uxf9QUCA4et-yQ90LT8CJBwr7FRikJXKIxQ66kNs-aKIhMhMx7ICY2WL8gfI7m4MP75YdXsf4hL7WMbITSJClvkg2-iiXN3lMJyNBHFe3BTgh_PXtTC0nPUM19knkezHhMRP1ZSJI9qpzcl_1d3i21tNnSndD_BVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=tj1iijCZGXdNJqJYubZNA0DgWbrk2OiEypTfVJbPTkKcisH1cXEBcEpcjfTo-pO_j6Ld7FQt3bbasH48DKVXLcd5Ub5I-g5kBMKkAw2vgfUz7CEXNR5ZbN6da-GLdfxIw1SjP4TlrsWmdLur1wb1DZkcnoKwegVLoTMzbIRDdnR2Hd7rnXSg7Uxf9QUCA4et-yQ90LT8CJBwr7FRikJXKIxQ66kNs-aKIhMhMx7ICY2WL8gfI7m4MP75YdXsf4hL7WMbITSJClvkg2-iiXN3lMJyNBHFe3BTgh_PXtTC0nPUM19knkezHhMRP1ZSJI9qpzcl_1d3i21tNnSndD_BVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQJWXQrFqY46iIlYzanXQ9jm3GI5PpkvHkWjq4W00yiR1PJvRjtiM-Yxcc6QCJecIFut_GZaCOyvnBUBinkunB7eRZ1iySF9xrK0BYHkJc6ETMCqMuaoK_6Sj9KO7IaAMCWoiRBfyZVPw3oZXLXq088G5meVHPBvlm01FGAA5Yad8iwnFk9134p-bgO0XwzuhHBP8tOAHwK8E3Mz6-jDym7F8GGPs-pjtbkc6tToFtUBNIq0X8Eyo22uV56roRPvcb77PMHi4vFtH1kxtGwBwabHsQCEX2VenFlejIITfrfbLv9XypewcBw0TY9YddGw8ZTdivMzZnw8AUhdumYZpLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQJWXQrFqY46iIlYzanXQ9jm3GI5PpkvHkWjq4W00yiR1PJvRjtiM-Yxcc6QCJecIFut_GZaCOyvnBUBinkunB7eRZ1iySF9xrK0BYHkJc6ETMCqMuaoK_6Sj9KO7IaAMCWoiRBfyZVPw3oZXLXq088G5meVHPBvlm01FGAA5Yad8iwnFk9134p-bgO0XwzuhHBP8tOAHwK8E3Mz6-jDym7F8GGPs-pjtbkc6tToFtUBNIq0X8Eyo22uV56roRPvcb77PMHi4vFtH1kxtGwBwabHsQCEX2VenFlejIITfrfbLv9XypewcBw0TY9YddGw8ZTdivMzZnw8AUhdumYZpLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-aKEvlMvoBc6g1cE0npr_ozTFEPCm1ZGUvG_eQm0RCRMpe3XtHV1j9HXxtxr9VdL75f04Kl0fPHr_PsJXHHnyn4NCmRIXgs1tkBFcSD8-OtdS1r1cB-GUJtPARDbxwyoDaU2FOMxPcMzRB7MrNkYcVrL4hjnSO6b1bVowIyegb3SdOzXdGiWNVPddnSTobLAQ5VWZ6Pnpb8yqwFEodCMFIJMMckyx45op8NiTb8XLCLklJhdZpV5i7WgZoaYh_sVftd6OkiiuvJWqTCIPGLN2j05fBVCpmb3UmOE1IU3_TtivAdspyHMG3Yz26Q4ZeqWcZJ2tnKT64db1B82ZaQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LYkgn1E2HHr5n5NSOxAcT1AC47CxWR-nYJpGHKOudDIZnrIj01wkPDhLNRHESSbdQJ3NZ1PUX2mOLG-uw4KTwyUQAGGEh-ksW8qsD2jwdZbM_GHkqu7Rw1wocCqPVA7fOOgC0tcwbPD3lMnqEFMJpm-B8Pq73GeEwZ-QHJWRZEMnqlZetYzM5839ELf878Ap-iYQo4hkUdIJMahH988uU4fyNDFjT2jpqRjnnKYlSbh_eUtZECfhbLq3douYtpZtiO8X5eesGOpC0i2MtYWT2trAQXNxuQ0LKIG3v-ARhEQAngf0W_xGKHMOrAo-6pLN4rui6QwoQ2kOqQZYwTOMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LYkgn1E2HHr5n5NSOxAcT1AC47CxWR-nYJpGHKOudDIZnrIj01wkPDhLNRHESSbdQJ3NZ1PUX2mOLG-uw4KTwyUQAGGEh-ksW8qsD2jwdZbM_GHkqu7Rw1wocCqPVA7fOOgC0tcwbPD3lMnqEFMJpm-B8Pq73GeEwZ-QHJWRZEMnqlZetYzM5839ELf878Ap-iYQo4hkUdIJMahH988uU4fyNDFjT2jpqRjnnKYlSbh_eUtZECfhbLq3douYtpZtiO8X5eesGOpC0i2MtYWT2trAQXNxuQ0LKIG3v-ARhEQAngf0W_xGKHMOrAo-6pLN4rui6QwoQ2kOqQZYwTOMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1nEhaoRiiXpa0FAm3qbSaZkXiedI2SxSVb7TwyCqtxH5DoiGoz5LYNyTjrDy1XIDBSvZg_MsaBe7zfyil4PdxgAdOCEgl59CGnCgDoeChgnx1egBr2-i0NTwyoK4BWhHiF6K5_PZVMyvhjzDPjI06j9ukplJVS66aUlSChiIJ4kp47-v3b-RYMSbEuA2dwbNJdHc35DFRu8Mmvjs_NCreflC-NK7BrQZ9R34KuutbH9kK0Bc_gHb1ErLgKz-AVSzkXp2v45GMUyiJaJc7QZ6QM64FimXi-ov6UwTOMZ4Y8FboabcE0ibpNskRUmYPYlSWgPLoOgGSkOrSeGg50sQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwAmM0OcMB_h4VwNWXrjKAhelrK9xrTDM9FN3l8qnI6vVK-zi7oCM7pK6EIsvM04AnxnD9Wg8D-laW-jxR864PH8Wrd40DbANEJWc0-MkfJJ_ibX-3_Doflv8-N7qW3X6iSL9T6Dh8ZFerkQw_PPMdw7OLbYHHMhlqDk-SVNi49U-AwnlInIXSUvek1-I6v_HYmd0uV5ks9UknUiRkxzP7AsKn9u2065t-7Y-97R9t4cRg2CFJX0vVQK4x0-vcg7ztJOe6ogHMmx9g8qa2TmwsUugKuTX0Og9JQ0BZAlPwomDe5WcfOiAIysChmoWhRJKYUmrjt_q6eMzPkk2SXjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrTGVY5TDEvU3boXVgvbDq31FcN8gysARbt9BZYdMjxIvSfmyn8qIlcnNdHlRwqMn4v2KNA9TfZL5Pd_ZBDpysW_TYzgTNtfs82zlgjDZwO5BzQ20oz36SEFAbLzZXiSQZjKyLhpwsOHmeF_USrxvPiHG-nmNIpiKeme7P3M78PYNEUqub7dLPnCQlaVKnMK1T1ocsUZ9qr1PJqbziLbmRazwUh1t49X-RMUAUiglbdSb3jK9mPHnS3eFJg2OI6GBnKQgDM8caob_e4BLq77pGptC9v0dcpVmW6FT9gZQlWJA-8sWP7MqZEBPbur04Z-34DRt-d6rFt1kn5mVRPUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=VABr23qGZsgp2pcOvWGcP1BJkHnDKaMoFyZcCvKscuO7JBQJ3BiyTSN3lMD04eGV-oQWIx11D18cdG-H2Zo5iXWJJLyZJyJyoHFL6cAjp7IwvzDBBeG54tFnDgeTF6RmCkI1MTtGlei07wd7oqgc0BQLQj7dZ3JxDw09g-ojZKabt-d6_fU4DKrAjUCM-8Gzq26_lfc32EjMAmTJD2FfmOp59MZefxxTtZATurkxx9e3N0gbgZvXFgVyORHuANwUlpqJhcqLyzSiJ1bHoFw74u6ftEcsH66nMbcN_AzOhmNDcxZlDd_URKPnWBn59GktIdh0LhlwU26XSi5gqydC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=VABr23qGZsgp2pcOvWGcP1BJkHnDKaMoFyZcCvKscuO7JBQJ3BiyTSN3lMD04eGV-oQWIx11D18cdG-H2Zo5iXWJJLyZJyJyoHFL6cAjp7IwvzDBBeG54tFnDgeTF6RmCkI1MTtGlei07wd7oqgc0BQLQj7dZ3JxDw09g-ojZKabt-d6_fU4DKrAjUCM-8Gzq26_lfc32EjMAmTJD2FfmOp59MZefxxTtZATurkxx9e3N0gbgZvXFgVyORHuANwUlpqJhcqLyzSiJ1bHoFw74u6ftEcsH66nMbcN_AzOhmNDcxZlDd_URKPnWBn59GktIdh0LhlwU26XSi5gqydC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRswqBMFkc_d6zzZQ48M160egkIrmk6IAoXcc1_atc6pEhD1XeIf2UeLRQGqp9rVR6XCv991wdQoX2LFcev4HDCupD_yXl9LjAhSelLDgFFf4kQx0VJNcbV3VzD-YUEMhvhpoRBZIFuevWn_JMQvFHMHx6wF_b6iGxC7lwCPP0J8jPp7anzMzucV7hesPBBsI9d7ZGBqiKoXfD6XFk-1HydUZcZeqAOPogAe8QfsacGNFiiAlVPWIJunlRi9nnFQ-f5dsaMzeJpLErQh_HC7kF5WgCU3K_a4KrfC3CFavxmjgaXnFf-NhSLF7qgeCPhqhtpvIe06NJoi18yxtJLEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=PqLY4Up9jtzubqHWP1W5LL23T_J9nKA4TSuE2553j0vDZrLlGo4rOtQe_qZG1K29VBuUxWeyDLTruUV7hBfo_GFyIQ8vev16BjwnTqTTYvI--a-fdOr3VC19A5Dt3L6WfVixUcvJ-imhJ-10Ho8JFeiOilo42oi4XQ3sQNt4YNrKMX_bRwGdN8JPjqEfVuzI6gwW4J27i6x8e59zm-oxLzEcY1xfSB-Rsuf63Cq0FLGyVJ946S9YT6FvEilNLYfGozm_EQJTApUxOpt9kNdrNYK-fQnhzM6hPJBlLyBhvm9yZ6i7lBymI99K4rBoCT6SE5LErJSkcrNbttyzNn-Eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=PqLY4Up9jtzubqHWP1W5LL23T_J9nKA4TSuE2553j0vDZrLlGo4rOtQe_qZG1K29VBuUxWeyDLTruUV7hBfo_GFyIQ8vev16BjwnTqTTYvI--a-fdOr3VC19A5Dt3L6WfVixUcvJ-imhJ-10Ho8JFeiOilo42oi4XQ3sQNt4YNrKMX_bRwGdN8JPjqEfVuzI6gwW4J27i6x8e59zm-oxLzEcY1xfSB-Rsuf63Cq0FLGyVJ946S9YT6FvEilNLYfGozm_EQJTApUxOpt9kNdrNYK-fQnhzM6hPJBlLyBhvm9yZ6i7lBymI99K4rBoCT6SE5LErJSkcrNbttyzNn-Eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=CBHQf5v7gSF1kqVh8rOFFQT6b9VDAbN3poxR_2QT-MF4vOV3V-H4IM2QX0FowxfErnPgJeYx2-70bUbgv0xavPPvBr5pfbytnmsyNzztQfQ9oyPLXJWL7wBJGr9Kj1OoNLdIIO9_oB0K05wi-59KAiJuqL51jxRocMHSWCMpKjHg5ASPcUwRmsiQVUeHCvMjl7T4SludN_mhiDfH25fiHeWZU0T04wwdJwFFr4ln05gcEBttcKsCtwArAPPbUpKZg666q1s6QL2X0GSv2DJZKTG48ljuqzC8si4JDmV_ZjuBZ5JYZtSBljORK7iloJ4iZ-Bm6KcbmKBuOlEvb-xBXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=CBHQf5v7gSF1kqVh8rOFFQT6b9VDAbN3poxR_2QT-MF4vOV3V-H4IM2QX0FowxfErnPgJeYx2-70bUbgv0xavPPvBr5pfbytnmsyNzztQfQ9oyPLXJWL7wBJGr9Kj1OoNLdIIO9_oB0K05wi-59KAiJuqL51jxRocMHSWCMpKjHg5ASPcUwRmsiQVUeHCvMjl7T4SludN_mhiDfH25fiHeWZU0T04wwdJwFFr4ln05gcEBttcKsCtwArAPPbUpKZg666q1s6QL2X0GSv2DJZKTG48ljuqzC8si4JDmV_ZjuBZ5JYZtSBljORK7iloJ4iZ-Bm6KcbmKBuOlEvb-xBXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlbqtWqsLiygMm5zbCPSz42qItbRg6JbqtIkDgVIUdBpomqcRpErZiicSMQF5_jNp4Yvs2l8G0mSeHY_GvUtryu_4ig-Q3UuR7HjGFGFSC_0hfPrjGjDicGTvDsOFgOf_8sBDxVeWzNF4zdsx20DOzA9O8R-mzEZ9PBJ_IMWkNwglG0FICm_iZzqx5M4Sx334jUILTpnByiiXSuqDT2uvWRySVBKWY0JOU28KHSOhkZDc9puuktWz8SI56f2K-vALfiCGB9uF4R-OZSbBn95f4qcyQxEWbggnvnl2X7yrhlTbwwp-i8-Qi2_EbUlAEVg_tPf8Gg6nhMk9RLhtweBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDZaSSC4xy5yitvD-TlCvGtAuBpKj56sxT5ejZrq8YozpPY05ZUrBD5q0pTnbQ08-zMlHR5wXAHNduetMyc6Q0IU1izuRMi-kX4O1vGANKK9HaV9MzMlmAXa1fsO9IpLZwHNOHJpzhUILYIb21j3ScRyNitc2WIinFd5GNC7mDoyGP7oIvpiFuyFosT_G_3gGcfvXWuIjO5FogwlXHXAJdQi41FN6s10WH7QgBnARwSu-v1PvqttO4dogW8XbDXPT-nfc7P8bvKwqkW4DwInkSwG9lvEDmH5JHlFnAVgvxRkKR8-hI3wiMSYFDJgSd13InkmWXxf3XQUc7Diqt9eYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=bFj1WE66WtxDtuJmyJn3bZ602YvRwTPKkAEFmqXatIWCFWMP1mk-rHt0sti5--08FXTareL2l4JYUIyKngqds85qx9SbQR4l7l_nZyVJHqYuxKHLqu0wRXczHaJ2gBF8mJp2zC4zESrmZ2Icy6kjQpn_VUik-FZuMN0N9XJURZGulsgxnTRdmaQ8B4AIZvjulg9r8XZifPyL4aC9tSYEumQ7Y7C1tS1iwLMtyVMoPSXEgilIuRj8-XvrsPbf-UuiMTIjNDXaAbXeQPRW5VjZSQwr_BdPd_S-MG4KH2NijUTjl_tT0A_1PYkoVlerjPktjCw8lT6MwrwureJNVAFdlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=bFj1WE66WtxDtuJmyJn3bZ602YvRwTPKkAEFmqXatIWCFWMP1mk-rHt0sti5--08FXTareL2l4JYUIyKngqds85qx9SbQR4l7l_nZyVJHqYuxKHLqu0wRXczHaJ2gBF8mJp2zC4zESrmZ2Icy6kjQpn_VUik-FZuMN0N9XJURZGulsgxnTRdmaQ8B4AIZvjulg9r8XZifPyL4aC9tSYEumQ7Y7C1tS1iwLMtyVMoPSXEgilIuRj8-XvrsPbf-UuiMTIjNDXaAbXeQPRW5VjZSQwr_BdPd_S-MG4KH2NijUTjl_tT0A_1PYkoVlerjPktjCw8lT6MwrwureJNVAFdlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI010NaojiLuciptx_t_eS_-x74KNYfJwZgX2YvxiCprE-puxyRpiHY93wkrFNcheFh25yLZJ1nUQUgtzNum5CCJDomFQ-nY_7sxVKm5xNzE_3Nd9G-mk8gWk2r3dtNQ8gSxZ9sNj7MtKprPf_G9aSxt2wc_-UgN5u8vdPlsgFn6tsh1aUwiJyswY71oKwCDNJpsvfhmT9aTxvCYq0-T3b2z4tH_K4bz9d9JBCt56QwN4AeAC6Yiq-YkCol73RfA5cMhq1E77EpTu4CERcvCUHa__EPuhPw-JUlRexe2zd2BBmSNXgzYmhz8cuunA3Fs5X8_QZeEeeZWkcYVq9ho8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sor4xGGiwfv1yGM94uXFHjlVJrYcHO3J0QCgRYISnHl2LsT-JHBm5QmOkLCvp2arhPUmRbdok5fYrlqActjt0TSNS1ylCfp7G--0dxpXpqXlsud4ScMGGiSILS0QDvSM51LVNWec2tv6plR8m9Ya_PRZFOIC3l6x7aJTt6ujHH0w2E2hoC8oSi1yzGYIf6MrWf7lgm76YcDKlDuWYUTtK3ivio0wA9Wz8x669XHhLOkV9lbiaeAOcFzNRyscs1lebE_cfl-OqdWKgHvQG3UHIBaKPS-aTGyxDjfOOyDl2Eabq_X9elBQqWNIHzp2q27p28wdNKQlQ8D_ETIgdJ8WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=kj2vK6B5Swfkd1lJaarkZvL9--dTSdLX8pvANNMYq9ktIpsCLdHGpQ-8WnWttX49VnGMyYsgXdzojEiH2QPyZfF6UAwcy4zvEkimyBUwyB92uwuxBfYio0e2vwYaz5WUSlw7kEO3WOKuyQSx8s7b4Aek_JU6n1PB3Ri3SSKCg-D0pmTVt-1CLskIQ9_XmGN12-c3GmrfDmswWLLQtZD5C5i2vQfSFD_RgtFarsnytWKxyaX5LtJ89SWL7iM5NayjkrnCB0LkxNG47O7Wo23kPPdLvQZF_fj5sZJntVCtMgvIyVgyQX8iEP0Mfj7oKlJHFit2EdBhjDKYATKCNYKtWTX0GqYdapThPaPzIBNdOlMMH5Tr3D9rgJeicH8kiZOmGpG07p4t8W8FfCFkz5EdWGw7sTxAe0oH6aqXH63tgQ8t5nOLOT6z3-AKSLkJWAudqPhwXuYW56Pd23YW1_HB0SRoA5219yiQvaqnVdZnAqRkIg_cSkQI--TFC-4Plqdyj5bHqwlHvIk_TTPqTxqe6EiLP4Ud98mI95G2naxs1mHz6gQKH-vctnT7xFnpz42CouMDk7JozubJmvu21VL2T8UXea-icbO7ZPYzPNPx3holgF1I33GZPtsKKDD-aeeBnSOFBnEj1sYBRAVL7sZGLTcjYQ6Zmxas6g-A2e__0As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=kj2vK6B5Swfkd1lJaarkZvL9--dTSdLX8pvANNMYq9ktIpsCLdHGpQ-8WnWttX49VnGMyYsgXdzojEiH2QPyZfF6UAwcy4zvEkimyBUwyB92uwuxBfYio0e2vwYaz5WUSlw7kEO3WOKuyQSx8s7b4Aek_JU6n1PB3Ri3SSKCg-D0pmTVt-1CLskIQ9_XmGN12-c3GmrfDmswWLLQtZD5C5i2vQfSFD_RgtFarsnytWKxyaX5LtJ89SWL7iM5NayjkrnCB0LkxNG47O7Wo23kPPdLvQZF_fj5sZJntVCtMgvIyVgyQX8iEP0Mfj7oKlJHFit2EdBhjDKYATKCNYKtWTX0GqYdapThPaPzIBNdOlMMH5Tr3D9rgJeicH8kiZOmGpG07p4t8W8FfCFkz5EdWGw7sTxAe0oH6aqXH63tgQ8t5nOLOT6z3-AKSLkJWAudqPhwXuYW56Pd23YW1_HB0SRoA5219yiQvaqnVdZnAqRkIg_cSkQI--TFC-4Plqdyj5bHqwlHvIk_TTPqTxqe6EiLP4Ud98mI95G2naxs1mHz6gQKH-vctnT7xFnpz42CouMDk7JozubJmvu21VL2T8UXea-icbO7ZPYzPNPx3holgF1I33GZPtsKKDD-aeeBnSOFBnEj1sYBRAVL7sZGLTcjYQ6Zmxas6g-A2e__0As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph8D0LGn6hwfIW2-uG72A88MwBVq1wa7vaBcFqeXVofIGoCJo5o0x7D30pWKnDM0NsLxQLpLChPn2vC4NTw7rRlTc-Rc-Qk8LZnzgcCQ1z36TUJ40HIyN9pzzGp5X0CclBp4qd77cgtizR_3vBii03XXe8Dv1LDGyu5EuNirvT7L3AD38iBADg-tVH6u6sqmVuhZ4IfStFTAJ4OHndzE61FlB955GlsPDaVRvuP3RjosZttKoUTmWWQP1tYH1whee6aGavjV43jafH1L9SeKoTH1lcjcaoHKjkYKNeVT384l2mLIqyOEWD1QEZmRU0yh6ot4v9tzy9LLc-wgbTdn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=k27J3XBSynTbblOU5M_E4T1VSfs0YQbRqY35JzLwAKfTzIHqwykEOSuWXqg1Ctl8uix7gLcOc8i59ULzElFYL_iFw4sTi3MIN2WkTHebuOpcuDkL5Y9LIyaOOkgmG0G1frNaHY1hQMAqh5eHl1ERbh-Tm6t36UXHCc6qK7sJPpz6vvnCv-lilnc5IiqRp4hvqFDbQHaRDq-F89CF_ksXShkiPOiBIIqSsgkKSmFVVPkR8cpmMmWr4zQCoSfzMRjm72mC_UfsmQwIS0r1ftXN7gqJ-xPNeAD5H3re11Jr66oJUUr2D8ur9UDMQqhBmGN_Hhv_e-2ifTvA_qRPeMUHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=k27J3XBSynTbblOU5M_E4T1VSfs0YQbRqY35JzLwAKfTzIHqwykEOSuWXqg1Ctl8uix7gLcOc8i59ULzElFYL_iFw4sTi3MIN2WkTHebuOpcuDkL5Y9LIyaOOkgmG0G1frNaHY1hQMAqh5eHl1ERbh-Tm6t36UXHCc6qK7sJPpz6vvnCv-lilnc5IiqRp4hvqFDbQHaRDq-F89CF_ksXShkiPOiBIIqSsgkKSmFVVPkR8cpmMmWr4zQCoSfzMRjm72mC_UfsmQwIS0r1ftXN7gqJ-xPNeAD5H3re11Jr66oJUUr2D8ur9UDMQqhBmGN_Hhv_e-2ifTvA_qRPeMUHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q66gL9UHxzmaiHm2zK6Jr1LmLPp6azwL-zsIJPb-5Gf5gzXhrjP1tJ20rREC6kMlpO67Njh5Y_BC41rDdVcj6wyVYBlw3O1-RhK11JkA4ximQxgrcgYpp7NDEvwYOf_z-5H-230ZwdzGjvYfwX2Oux3oEXCThYnQQiV-ujLy_olNl3Frn-0qdWq2ziOQSqatvMzd-6v9xneDL_BEGSrsIg32ilWBekUvwFvRgwe6jwoN6kaMk1uGgvsriqCxm8JwHzwQi_5oHCf07pamBmdJp_eYeIFNwsETilZJEuk83MX8B9u31GFBVGMM0aGARTebCf9IW9YAle6olgiTImFRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlCljLzvpWPsxTsvYrt28kwE_Tk04o4TMrLr_rzb8_kQUlcIueojha6M0veK5jlSsJl1Qh1hog2fUli1utvZpTrmWBcEn-aoSHwauuhSU9nGg73uVRtuJWmNNs2a6aOUXW7sGHBPph4rbpW04AxLI7BBxrhh9cn6c8hPRlgHq4ywHQtT25AFvYLhRE1RhUQZ0d16cH5HhHKKryzy_ps3L2ObGSeNfIUbixKqyh-TUSRMd03ZAjZnabkoQku0ktdA1iqqvhat2UioIfwYR44BoamiLw0flzsj-e_jnK-fsGHy9TQTGqnZEIefMMmDhYw62rd9YhWIeXWS_9gR8nukqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBI8bjJnJGPFKNxxEh5KzI2nY3Diuu84hZAz_75O4d7dI4SYeXBL2RLF_B1gLhoJ9S8LAnoaoOoThk32Q0NRltsItEY1tSnZLcn6QaCMQTqZlepyDkFa3-yHuZ34Gdw2F29H_G897SQsnuz3cIDY-G-pBBi6HMsykoMl51eI6uCA9D6E2PXrUHjrjMksRazS52D8_CBF9yNt4A34J6O_TS-Ica22KxnQYYTqtgBL7PPP768_KvDoc5BOc1hGFSZu8jlH9e7G4eCfROqBstXTv22j8CEwwu3HBdZs7Z5u7rWgS4iSgox31cL1empebFqxGoJw2jQ744LunbWAnt8YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/by_D6tcg0zqjsagg9dTahx3xJaf72ezg_nMA6lEYMhJg89qbh9_ojpriaqe2hCeFJAW4e64Fdo_CexBVkRnjMOwDbEHvTP4jWJbcmgrj2ygZfiklBEKKwvM9ZFhqwph-wxnicPcVcW5UIo8HfdZeH7D_umsTuVCCB3AO5lG-T1P65p-PgQwzr36B8TM0yKeZcI_63NYY4Pp9o_sRjmsy8h5AV3vYe6JV9GQBCKWvhx7ZMQWn-NMtN6EiM4AkWtsuMVU3t-boLRj0Jkc4eCcPkHBztVGIYuNt-QSNOvap8i0Ut21wgYrLLo7NRLyTRcgIhL9KlavZlfhe3Xfhro5DyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke0eLDgABFecSEDo61JieWaQMt2krg5hnHtu16qfZEbRkgWEyju8r9QA3DUa6kRYX-Vxw_9HMw7_1IT4U9zNJVLwK6adk7qrUlIcq3h7rv6dB1RVCuFzwL8Mcb-NhapxKjcDrHqxyDa2F7K65JvP8U1MYnv2x1cjC3KfZYEJUsnmnTBQL79Azk-TW3Jq13oKiqkMP2ezIydtCPnSiSaobpk5TBTxQZ6UYQ2pd-4MQYZmeKKA3gLZ6lp_cSq0FP1l1AXV_pGQ9M5gAAQHTDtIZ6Yek0AEDz3ut9q4NFu8K8pvetE-s0j_Ll80uDBueyKOdwq-uvFh_X3fX_0HvWQQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyhuSk_wnhtUx9OPmQpSCO0wl9mA_hBo_QryYOTYVgchACFMvBLdq57BdNkiPI4WemJI3Pe92rBRyvvDNSFFWawgiqRqbyV7kGXLskgStoL4X6steN3VQxh3jkvB7zMLryDB2bW6Ej91rrpvKyiv1-wRLMcSHXC0NPVg1xrJLixnJYuTF0tl2_891PDRno_-zvpz-iNGskPP_GB1iPjJZ-1rednEpP7cEY3mXJmelEo6G9-j4Eb9-2arsP0n1_5pG3kFkYyXSdz41o4a-fVp0eEauvQZ_yJUhArwmaShKk2Bm1r7ud87CW674aKV31ZiQmAA7BBBHUm4eIh_lk6-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6mxz_D5k9KVfwBMioCtHgl-1CovG9jBVHNmLhCVC6rXHbLpkqRIOo9sD3Oejt0xZfbTMJ2QjviNhzCsDlX4d4Jeg-72us4Cph2BtYunCokWPQH6v2C7mlKO-YZM4zdKI5VM5f1M7y3fFXXoA7OM44Gld8Zquk9Bi6MIvyPdL-KdnR3at6XRi_zZjN9SLlEQ_vwrvRwQ0pTHt1mzI3ZfEOEaUQ9NzznjLeW9PU-xcbCbbaQ3uYN-XRHs2JlzvKa6skCjO0cpCm8d79YhhfPlEwm4iggcLhc87EsQGa3dm2pAMfqLDIkuKifk_zEpbl7-SLs3UcpFpfHP9Saf1qR6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvUg85Rb4Qsv6GVWmvX-AED7uEP5hmnKQAG3CvkzoW54LQAuHXRLja3QOlHeEbK7Y61rJ2Mbk2nH-w9U5ybPaqqFA3KnqTz02CYY4Hd7hGHRjpTom9zVG-y7EQgePOgvK6YIWksUxafB-e3LRyx5UBKUuJF61sDZDA8LTCzCoxjtjadjFnyGMlce1EHwiGSY6PEW-Xux8-gaaRkXyiGbtHpFIJvvP1V4Ys6Hk-IEg6YvJtu_A1gNd8BNfLbLbYReQ2O7fzkjvjUdxrQfNOyMXnuaQB1JuKt2ruLftsJSlbQdwrvLopOqFBd8jJTqBpyVVFUl53zZ5mYKKX0-gfTnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXasDu3c307X0vYKt6m8Tibwm5HcLmP0ImvN0XJG0V1R_877_Y9PfvxolZ454DfG0YVkYK3Yjk-AN7XD_K_d5FZRdKmNpTMilV52QDWsuyqJUiDQ8QwPjghH6NzOc0893593lroT8wktvLgVX5v9QTfu7lFFpUIlu2g0Wy7a-14h28MY3IMCZfvyYdqm7Iu5dXF64jLrmorJQAiVuOzBrfc4Fmlc_wQ9j4pi5bD5t50s_aJmWbaJ2ea65uv1Wz3P9U_bPCO6-8_ReluWGh8lRdA69BmragpVALk2pFckF_2L-y6939B2J584vdY8rVB2su7AuT0CTrZyD-QZs0XGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUQh7q2sbb_p2EeSollCMfAdi7TVooH0Cw4JF-8_ai9Nrp57Lkf5J9109pCiJyJElE_G-ePx6JnkwIJxR6Dx5NWZJx_c3GVQ9WydgyXER-oE9Zrg1jGo8iV2yyL5e9oA_Lynx_HrpFk0kwPWgDpMZ8mFfKYvLz-oFIUxBu0CLbM2E3h_qyWjYm8B55iYJhVCdp_ZNRVl-s1e8tYnNoS2HLaF8pkvgoYodi8BXLJEcWMK0a6fgHGon2Zu5_D_PtxSAv2Nw3FVGk9T8s85RFfllUwn9iP13xkHetCDnqp0SA2olz0kMrioky-4yGYasx0JwFvWTHL7sK--HbfQWTzGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFluWUEUkd_X1LqHQqCRMq5RFKPcqWH1ohCi4Dc4pfetf2SyjmHhL6-1MxeujchT847lhTKZHtPEg5zH3RxKwQOW2HsKozTodisKyzVMeuvNPTR3-wFAMPN1TH2e45xUWF9ryntZBrf4mndcvh1Est2bTtaURGfd_gcA7k3Y0PdxpQJVJLyzxAirehuNDOkcq3dlk-YDWL5_8SEayNMxUZ3gtCcCtWuOdXzGYRWKP_hvRN5qLsnLJlBgHPYJye18VZJhkXEkicfxnA0uUXnPC7W79gfZpjaq42Wokj9gJpWh_QnSY4QyktTXjPkk8QThnbHGXEWkJbDtdYbFH8BRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDzAjgL1pxrf9kE5EH_fAMJMkw5VAqFLVrNMZqTmwEgQUBfBxqRx3a25SfxFIkChUb14WT22cfJyzNc1UVaY0vb487N2_rwPPXIIc3F2xJb8VtThB1KNoE_4FK2Zw6ECFYr7mS7ggTtQz_GQPRtJU5tr7MknexEgBSIL2pHUQbDgDdeysMee22gXyzXUkjEfzl10HPffbcdawe5ZeH4co7cwkWquiM1GYK2ChhBXrgjG5SJgNuNW-IAUV29QH9rQw53USrzZ73NbgwSnnQXCyUO2yo1NQ9rZUolBDLuMMjurnMqeQShgdCMkErxTc9u-0FgPn6F83FHhGeUGlnn6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=uzVHOHPbYtZtvTzWVOPk7XUm7An1AwxhcDJF9Zw2zE46mYzMsWNLAMIorAGYe4YDfpOQeiIkvfNB8wYcJfR1-TkQeVNG3MZBS9pMLrUAp1n1mKW-i5_V9GwteVDicQxDb_W41pgPRahYI9aKocgWkkbH758z8089jg8I3Eykxm-4JO65oOPvX2VwUdLdpCNqlkbdarW-NpAFiquLrBQkPpJR0V2-eR_l0Cv1WSCoTo1Mzu5pqQbgiq8F6qU2Xk_vLyEuBRoiyltcPA0z9-fVaBp5unDZAYAEv6rIVY3Z-pY-B2YKRAgrXyJfAVgx83uKC6Ke5LJ1AMa861ls5F5ncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=uzVHOHPbYtZtvTzWVOPk7XUm7An1AwxhcDJF9Zw2zE46mYzMsWNLAMIorAGYe4YDfpOQeiIkvfNB8wYcJfR1-TkQeVNG3MZBS9pMLrUAp1n1mKW-i5_V9GwteVDicQxDb_W41pgPRahYI9aKocgWkkbH758z8089jg8I3Eykxm-4JO65oOPvX2VwUdLdpCNqlkbdarW-NpAFiquLrBQkPpJR0V2-eR_l0Cv1WSCoTo1Mzu5pqQbgiq8F6qU2Xk_vLyEuBRoiyltcPA0z9-fVaBp5unDZAYAEv6rIVY3Z-pY-B2YKRAgrXyJfAVgx83uKC6Ke5LJ1AMa861ls5F5ncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGTgLYVTNAx67JHIdPVNt8Kcg4EbnekH5r-K-bw2wjNWHJTlcUPFAVEJXe6xQnYJmn9UGkAYnAdEUfXYo9ALgV-6FyyeDnq7VJAkQlaWuq70iVHvBeXDLHb86zc0CaPwJAiMq_120hA3weWWWqAzYNOg55tqEa_5k6iStEjYUVpoBgHADc6p2978X7rM0N64t0ST5Y8P6Mvp5XG9zM6I4WzB66DHXlNhp0xtplk0t0tM7gzzOYn-zMEJSz6Ns1H4lZgfIJZwfZQmZ-ZDADVOxknOAI8EY8HMEAi-Vimazcc2WrJ5UTeRp7VqxfpKiB8F7jLQwqE68_i1nN8NoIM9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJNOEukCyYL6oVc5-fhysFK9co_4Pe7bmklNFBH5xNNUhJWW-fnWCEnE_gWS7MT5wggPJNbmWJV2-lCBlfsx9yggnHOiHOI5PHrVF7aF_jtXzGttJfvN57xfgwNwFtiqfMv5MGaGQ4-eelUSPcNPs1yT2alN49gQyRAahYvKULDfPd8_QthvNtmIKaigzPlINnwFcfvNvpSxCjGuikAXxjGSSw6Fxb7PyD4hs0GuBtC7z4jLrVhTkY5KmdBd9izn7Ah2aijxdZ3IoPsY-6AzxYVpZU7AsX4Vln7urMcANPbPsmT2kD_bFoNeXwgwniIFHKakxLlZenJzPjzeNwMMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdKCjYQ_iFwuRMOMLKAqBt96CDbfibfVXT5sfKtUJXPvUyNPui0Ytov3r-nXixawj0_cboIyd0-tLJnk6WnTqaqXrb6OO9ETBZPC_x8--vR9bqxZCWAy0oc32yba5fpSCjbd6T28GEtnoR4KGz4lpKq4OAUhVl7UEHisAVM1-InY_jOqnxbnpjJUJ0gMGkLyZ7eo-XzUscEjmm9fAF6f9Fp9dVBYACWjh4vUMljriALZn6nHyK_mAC2Uh_gUEt7titx8ayLcMPC7QEWvqk3wYurZnvf3_HNdyGOEoslk7z2Oh46E325oIee4s75qi_TZ4T0mCNZ52yf0_Z4XqdaSsf2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdKCjYQ_iFwuRMOMLKAqBt96CDbfibfVXT5sfKtUJXPvUyNPui0Ytov3r-nXixawj0_cboIyd0-tLJnk6WnTqaqXrb6OO9ETBZPC_x8--vR9bqxZCWAy0oc32yba5fpSCjbd6T28GEtnoR4KGz4lpKq4OAUhVl7UEHisAVM1-InY_jOqnxbnpjJUJ0gMGkLyZ7eo-XzUscEjmm9fAF6f9Fp9dVBYACWjh4vUMljriALZn6nHyK_mAC2Uh_gUEt7titx8ayLcMPC7QEWvqk3wYurZnvf3_HNdyGOEoslk7z2Oh46E325oIee4s75qi_TZ4T0mCNZ52yf0_Z4XqdaSsf2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=aDY0fPQWyRoX5n9cLBS8cfE9TXY-H1V0e-uf802RMc-faejDyHLQBksIRSlSn-bHK1YLkjLF6pGJIV7CGXXE_9a7NslU4wSPd2-tIHrPpExmfffLT39Ufhj2vUqT3fEi32ilwwFM7qCcge04ONpKNk2g2zCQdbEjyAWHfgx-Jp3dv6HLS-OFgdXlvzdZlEirs8BzkLUiWgOp6SqE9KzFsEycphwuiyqroIy611j45YOu3DEqFnjLc_gYsqzdDRkotYcnFvycPJobkIE3GByd8nP-1FCO5D0aOIDhztEt6_lnKn5LPDYxiM5Mm36Rml29PY5joZrJzFLBhmacUfkYrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=aDY0fPQWyRoX5n9cLBS8cfE9TXY-H1V0e-uf802RMc-faejDyHLQBksIRSlSn-bHK1YLkjLF6pGJIV7CGXXE_9a7NslU4wSPd2-tIHrPpExmfffLT39Ufhj2vUqT3fEi32ilwwFM7qCcge04ONpKNk2g2zCQdbEjyAWHfgx-Jp3dv6HLS-OFgdXlvzdZlEirs8BzkLUiWgOp6SqE9KzFsEycphwuiyqroIy611j45YOu3DEqFnjLc_gYsqzdDRkotYcnFvycPJobkIE3GByd8nP-1FCO5D0aOIDhztEt6_lnKn5LPDYxiM5Mm36Rml29PY5joZrJzFLBhmacUfkYrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE0dkHo1WC44QtdVG3fydc8ls-WlYE9Dg0FAshUGJrIUilCSde79GbG20uM6EyAa_nge0OEGykV0C9ZTWuPzHe_Id0FAruzjatch7MStwq1evoR6yP3dxGQGVR_YCjr9Z26r5XWf9uhRtfmqyrGz__DIF4_vVCvK0TJgBV2MUvFdhMcZZJQAz_tURj41o4dgx5dGkH_fbQAVLzkxdtc2WLReDIKjkDn4kRThteBg7KpvaK1vepLeBCg0VFs4nuD1Bl4Vp58qqkNnGbF2zlqdbPM2tXUmzZ8s2nFsSwEoRVY0MPWceFxTCPJfAFfkbc2_HAwhHDFmsyyU18uthKRLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGO_9EOQlXf_gRwE7q8y1ca3o6tTx3L-jWwDF8vTyyqEYEmtU1Cl0QPd7xKZOhrbjb75wgBRFBUYga9oL1okpH61AgSrqBJxAMQjgLfHtnE4iYYv10nMrKCE44HgSNuP-SWImpmBLO3c66I4axFTQYII5rjrVlRRVeKfSH-fQdPgcWUQX5MrtRMmbQuvrTp-78pT-mihcHBCBhOuTOj_ZJrI1hueDJh98c7qyQx_-FbUtnmdmtPBkZS-L2uYms9k-P1HWjgi3Iuw3ARyoTo508uO8l_63_TBzeKVLpJ0wC5T5gZHkKo0cD-hplWPqW5Os_0ykAXcTBkhYKyOO3kl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz_TWOR4Dr59a0lqVUwtY_HvWR844gng88dtEAUY6J8uSRFHjzoAtF4ZH-EV74d2WnRQEb9C_hV9XQ4-2jlRJiCMlbvIsi7WAiquMlZeoCCXS7eYx9gmlsVMRb7AuqfUXrFQwqPEdfPrDvkhMfDRz3YtT_8QFG0jbedbO_D3Jug5ayh7N-2dmyueygIZttsl0Folh7ODgoTBsKwLyZE7pMFQ6F4zjIITya2d8J3d7HE7Wlb89Tyk9_xI5ZjcyaSpRnUbC430MmArnG43La3bS78W_cmPYhQRpYKjcOn7kcjun90hdoaLVaLAWUwJyT0Yq1lZHg0TMW58m2Zr6OTsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJAZ05nbEJ5-9bQBPCMS5MYIpOtGlcYxDymqESXYaxET7h6Z--5AC2u3X6MuMgPLgIzqJGMmAy6GsTSImVqywkJiF5rpESrulCM7Ez3yiJ-8ulsbwekoAlP6T6AmwmPgO9TRoYt8dgCdSFFkQnZCec5l2y-xYmv0EZb-i4LIaY6KUDcpacH-w6WYRdLyYUFxfg3_ZkB9UJfN26cm1I3Gmf0m4t3dZLOSvG1sR9J9h5uYuncLZFaGXM5EfZko5jPwBvP6y-afUjx6V8ODLYMbchJtfrkWeIWjxs3O23deCD1q4kF9OnsYBzLeAr8exsFIEWEp_txRjcHClF6wxKyg3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALsHrvIj8gzn1fxSvbaefKEEk5CsMfZ7-bRP0etyCJBYWaCigGD3SAWa6KVxQVLk_4rYExnpIpRerbh4__6u2ZgQNOQfQIHfvgSt42hIVVX__irNYtgaEepVGsW-uSJNBN5o4coMnXjqskJ8OtfgWn_P775xA_5km7YElwSwOYKLxtGAjr9bV5IROLO6y26zb7I-cxICEMBgnXwVb3jdKn61tXZHIfskcFTsaJhVKH0WDWcW9E718_GmSyRlM0qAMM1a_OI0Bz_81LHJACqkS-oskzdos1jL6QPYrBG4mWvUAJW-4gbkaC9c93qKsRyLyxcElCyr_5F8JbmLSIpErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7yzOASoTls24U99c3ENMr-1H2LdR-2Ng9tr8mqzGKrRefEWkswQL4QmkVBITBv7G5ayEpO8GORduqJhT3u9DW-vzNGN8pXidoSALRvmyJ5a7holWH9maW-Rt2MvIETN1a9Ndd66wNeRwgnPYdpNBXPsxPQh7iqcHzZHHGhlMWBfKy27yEL5sxbGF5gGw37JWPDZalrTguFZqRf7GAR_mJbBpYdtpKWfr5Dg32QhvPdyxOF6p_EjCK2JVsjNXioyoKFtdrEx5gHyPVzPCvvt9DzyPoegzYTkwsuGVKspjsdGQgs48b90NB8nBoD758j9qu2_bJi-7fiPKstHuDONCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
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
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPN7TvKRCHAjR4K-O6ZozkMZEIssq_F47ES-OKNxPdwCTlh0n9cFJR5fnqkxd8kv0y24N7wBQoPhwZ5bn8vBf-iighQ7g5PdFv2KR_rR5mRGtgA4FR5S13ZbfjQSOGBTuJXUq_qSqBPXo-QOR27QdYoAptCz1k8gGPBpX-xwdIwUXFMfY_Iw_RuAYp5x348vHqTMOtyFZRwUGGaz-OYoVWCEw6fmuM2DsqJnb6VMS41f8hykBIMOPJHsPpO3rPOOk2XGw_fSi_OCXb3UpintCVPU7pjfuA0_qt8W4ynJvBIMxWCWaXeom2SlkV3jhCOyaWKJzpbHIO3moI2drCJK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE0eFnQTclTFQ8mk0ZCbPBi0ebxhALI9c6RosJZEsX_hETqYu3jQJS4JVytCXKaX6lswxhN7PXMpdd_Ifcp8vbpBiHEDFttdi7Nat-3h6_gMEg2JSvPb1HhE6o8jH0qqpR0RsDCpwthD9hwWc1ReZ24fkEBDftrqESp95YpIuAKWsQ66AxTUGAAFYo9JumaqFNaWkxoaU4CXbvGTMlFhqU1F0eA1nB9kmb-oFVa2lkSrqM9oDZ-lDsk-liShsD1bs9IN6jgorgQbu515kaA0WfstY1H0RuEzb_vS9yZvzrVpcA3tsylvsjmwVT3AQc8rXZg1Kmp8KNEqYBedbXrDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
