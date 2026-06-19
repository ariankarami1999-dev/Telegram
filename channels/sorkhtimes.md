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
<img src="https://cdn4.telesco.pe/file/ukZEAJBMMhkSxDtsSVbRABZ5TUsLwFYXoB5eu2isOrqbKmL5tMt6LLymnYYC08wLo0L1rs6aSlpnvSF2Fb4XAEfjdYq1ch5FIgyQf88J1W_k-NeeJEOwPpirEceAsXrrfHEGFsReuSJvF_GBFiLCfo2_YxjnBngt9zGTh9MAVsdHmgR2JjO5uVT8X-CtYY5fLIi_oWmr9po2AloYZV1xAPWniurtsb-X8Rv0ZkpSJnJqJJ84pk4cTPKrln6Tm9fhCTp8wjIUWoK_cB0OxWx-NgPXwg8TbkdEiZRY1ZCBlkw0wzGv6wHWTOxEiLAXGMQIFVBrlP7f0D7_vUqS4j-O9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 23:41:36</div>
<hr>

<div class="tg-post" id="msg-133907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
#فووری؛ ادعای #فرهیختگان: اگر اوسمار با پرسپولیس به توافق نرسه تراکتورسازی به صورت جدی میره سراغش و برای فصل بعد اوسمار رو جایگزین محمد ربیعی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/SorkhTimes/133907" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/SorkhTimes/133906" target="_blank">📅 23:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
بازگشا: ما فعلا با اوسمار ادامه میدهیم و توافق برای فصل بعد با او به آینده موکول شده است یعنی با توافق دو طرف تمدید یا قطع همکاری خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/SorkhTimes/133905" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=G3ex4w4DX-IbKFAWt_zL6uGFrrbJi6J-h-jGSmb24lBRNOmMEw_bX7NjdDbEXSkleSVJKVylRUq6WlthW3HkT1X8qwr99ou3HijGMvCFZKGaM1c3B-iNIqpYMXcTTa0Fxc3Wv3W1-TCpsGmO2iXtH58WuiPHQqJ0rDu1ZcBYJ4LNTgoVHm4zkiv9oqTEv-oJYHFRqyYyYnNtsXpTUfbG7oi9-OQ3giuPApgX7sQHjsM0xE1GEWk1d9fe4ibEzW4oc7fdTCKx89nnSDCt0HO8qogFMdMLadcfZ3KtB79wbL1gyF9jFUIfMxpsWIa9kFMSNbExmxo804jEZ04rNIJLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=G3ex4w4DX-IbKFAWt_zL6uGFrrbJi6J-h-jGSmb24lBRNOmMEw_bX7NjdDbEXSkleSVJKVylRUq6WlthW3HkT1X8qwr99ou3HijGMvCFZKGaM1c3B-iNIqpYMXcTTa0Fxc3Wv3W1-TCpsGmO2iXtH58WuiPHQqJ0rDu1ZcBYJ4LNTgoVHm4zkiv9oqTEv-oJYHFRqyYyYnNtsXpTUfbG7oi9-OQ3giuPApgX7sQHjsM0xE1GEWk1d9fe4ibEzW4oc7fdTCKx89nnSDCt0HO8qogFMdMLadcfZ3KtB79wbL1gyF9jFUIfMxpsWIa9kFMSNbExmxo804jEZ04rNIJLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوسمار: اگر بودجه کافی باشد شاید ۴۰ ۵۰ درصد پرسپولیس تغییر کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/133904" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/133903" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/133902" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=if1ZMpDx-17yYgj0u-LNAj9MyGVfXei_xIl5j4EDm2ZzgxFHaDwhfniWRQa7KIEv9c8yHn_OIBWHXpSS-eBZ1sbGB0rhcb6ZQ4Dl54iol7ldV2eF_3tsMMKw5FM47IELR-dEY06S6AfgNIaiq8GBgSIRkkborH5ha7AsVEiwDOzuExnObInVdYB36SHnOFYjd5XovTeIIsDfU-eJOBI62QyiEafZYc11s0in0JMl0HV-YyQRz-M635wa4l-CZQFUCo_GZQiCx4o3uUuWrEqTVCzKZHf3W0BSHXPflMSYiCKNqwg8JHVtx5cbUmUC2FcaoF2TkcS98h_jRdZeJkxJF6zQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=if1ZMpDx-17yYgj0u-LNAj9MyGVfXei_xIl5j4EDm2ZzgxFHaDwhfniWRQa7KIEv9c8yHn_OIBWHXpSS-eBZ1sbGB0rhcb6ZQ4Dl54iol7ldV2eF_3tsMMKw5FM47IELR-dEY06S6AfgNIaiq8GBgSIRkkborH5ha7AsVEiwDOzuExnObInVdYB36SHnOFYjd5XovTeIIsDfU-eJOBI62QyiEafZYc11s0in0JMl0HV-YyQRz-M635wa4l-CZQFUCo_GZQiCx4o3uUuWrEqTVCzKZHf3W0BSHXPflMSYiCKNqwg8JHVtx5cbUmUC2FcaoF2TkcS98h_jRdZeJkxJF6zQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی گل گهر سیرجان:
🔴
برای برگزاری تورنمنت سه جانبه اگر باشگاه و فدراسیون فوتبال تصمیم به برگزاری بگیرند ما هم تمکین می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/133901" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=GaVbVjkwznwdZJop1MJI9rbBmUNeAImRxsAlIHNmZu-c6_Q1a9KTMS6RbjTXbZFomiUAioJOIsrWLKozSuRyVKE58Q_GnSA-hZwFWKAHA79KsCbxEqfz7msuTtGIi1Okm4CmgxTt3Oj1mhTuAszGTpRVtqVMicnVr4TwOWrapylQouyJlzH0KxDugBTXcKOa-GY_fS7uVFWDSdStlgGtXHvcI8eUP4AhvNpOqQSbXy0l_3-Ur2o4UalIXSr9xcN5rnja6a-Nshy0iGSHSMi9jSFPwB2REpmHhLi_tVyJHHiLMkMmVsDBfkdxIOupSTcmqjbDu6T6g3R4TPu0gXIcr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=GaVbVjkwznwdZJop1MJI9rbBmUNeAImRxsAlIHNmZu-c6_Q1a9KTMS6RbjTXbZFomiUAioJOIsrWLKozSuRyVKE58Q_GnSA-hZwFWKAHA79KsCbxEqfz7msuTtGIi1Okm4CmgxTt3Oj1mhTuAszGTpRVtqVMicnVr4TwOWrapylQouyJlzH0KxDugBTXcKOa-GY_fS7uVFWDSdStlgGtXHvcI8eUP4AhvNpOqQSbXy0l_3-Ur2o4UalIXSr9xcN5rnja6a-Nshy0iGSHSMi9jSFPwB2REpmHhLi_tVyJHHiLMkMmVsDBfkdxIOupSTcmqjbDu6T6g3R4TPu0gXIcr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اخباری سرمربی چادرملو اردکان: ما از فردا تمرین می کنیم که پنجم با پرسپولیس بازی کنیم
🔴
چیزی به ما برای بازی با پرسپولیس ابلاغ نشده است اما مدیرعامل از ما خواسته است که از فردا تمرینات خودمان را شروع کنیم/ مجبور هستیم که رای را تمکین کنیم و بازی کنیم/ به بازیکنان گفته ایم از فردا تمرینات آغاز می شود تا پنجم تیر مقابل پرسپولیس بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/133900" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=bYcBy_h18OQG2vvxXk6Sj2v_YdEE8kDNMTNHTQ0W2SlpQbCbXJMuun0-NhzL3wTL8Ca8EUN59zRhRqqSsFYV5Q982t4sMIopLcjxsQ3XLp6pEiFuecHnxc7EJI2uw8JYayAT36RpthJ4wLyJTdW61doZNof1mhmx_z7iTrYWBZNJLJoLryE2s5bvp1KM-Dq34rD7fYGAY0QIndigjGSpsFKt2iHbWdCwI_X8dQTSkJ4qrS1Y0LC5EhSRZ_fJO3GDxXV6xZxHo8uipmBOTTJ5unTWvSbIlKFY6mVkzw9LnwsjqLLuG9ke24W1FG5rvfo0NY-0XUCGYgWqcJmT71YNvTH-nvq_ZCvLkqK78Gnq1he3YaOqnoImWRaWONRlySMdl07QfGVixXLdMLx6MVAqDnh7xnX76WFw4UNEB3ZFY7S3mkfIcSKR0ikYa15X3Q0XDfjIsP2kaBxph7gCL6qyEnq0FaG_nz6En3eFa9_A_PV7lmCn4mpGwR0dFswKievUjmEVl2Rgo7jGqptZ5yyeKaWXLmlbNRHfTZR2Goj-2vOT-_0AX8NvjE9aUNyy4a9LdsdZpc1mGxZHhpDNHME0SwCVxZ_CVcV14-2BNSErxiPZiPIiEC0k1rsIOMhjh8fo8IikAe_11jLizCAve9Xcoa6futqsRQweHKyxvDz1RVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=bYcBy_h18OQG2vvxXk6Sj2v_YdEE8kDNMTNHTQ0W2SlpQbCbXJMuun0-NhzL3wTL8Ca8EUN59zRhRqqSsFYV5Q982t4sMIopLcjxsQ3XLp6pEiFuecHnxc7EJI2uw8JYayAT36RpthJ4wLyJTdW61doZNof1mhmx_z7iTrYWBZNJLJoLryE2s5bvp1KM-Dq34rD7fYGAY0QIndigjGSpsFKt2iHbWdCwI_X8dQTSkJ4qrS1Y0LC5EhSRZ_fJO3GDxXV6xZxHo8uipmBOTTJ5unTWvSbIlKFY6mVkzw9LnwsjqLLuG9ke24W1FG5rvfo0NY-0XUCGYgWqcJmT71YNvTH-nvq_ZCvLkqK78Gnq1he3YaOqnoImWRaWONRlySMdl07QfGVixXLdMLx6MVAqDnh7xnX76WFw4UNEB3ZFY7S3mkfIcSKR0ikYa15X3Q0XDfjIsP2kaBxph7gCL6qyEnq0FaG_nz6En3eFa9_A_PV7lmCn4mpGwR0dFswKievUjmEVl2Rgo7jGqptZ5yyeKaWXLmlbNRHfTZR2Goj-2vOT-_0AX8NvjE9aUNyy4a9LdsdZpc1mGxZHhpDNHME0SwCVxZ_CVcV14-2BNSErxiPZiPIiEC0k1rsIOMhjh8fo8IikAe_11jLizCAve9Xcoa6futqsRQweHKyxvDz1RVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/133899" target="_blank">📅 23:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/133898" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
بابایی مدیرعامل چادرملو: پرسپولیس با گل‌گهر بازی کند، نه با ما
🔴
اگر رأی کمیته استیناف به سود ما صادر نشود، باید حکم دستور موقت بگیریم و پرونده را در دادگاه حکمیت ورزش (CAS) دنبال کنیم.
🔴
به این مدل تورنمنت‌ها اعتراض داریم، اما راه آسیایی شدن همین است…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/133897" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/133896" target="_blank">📅 22:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/133895" target="_blank">📅 22:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/133894" target="_blank">📅 22:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
تایید شد
🚨
میثاقی: پرسپولیس 5 تیر به مصاف چادرملو خواهد رفت و برنده این بازی 9 تیر با گل گهر مسابقه خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/133893" target="_blank">📅 21:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/133892" target="_blank">📅 21:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/133891" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه برای پرسپولیس بهتر باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/133890" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
اوسمار : امروز من سرمربی پرسپولیس هستم تا روزی که باشگاه تصمیم بگیره و بخواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/133888" target="_blank">📅 21:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
اوسمار : من با آقای حدادی جلسه داشتم و گفتم که علاقه دارم در اینجا بمونم و این پروژه رو با هم ادامه بدیم. نه از فقط از نظر مالی و هم برای باشگاه و هم برای هوادارا انعطاف پذیری خوبی داشتم. اگه پرسپولیس بخواد میتونیم به یه نتیجه خوبی برسیم.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133887" target="_blank">📅 21:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
عادل : خودت حتما تو محافل و رسانه ها این چند روز حتما شنیدی که اوسمار تمدید نمیکنه و از پرسپولیس جدا میشه اوضاع قراردادت چطوره؟
🔴
اوسمار : من هنوز با پرسپولیس قرارداد دارم درسته تاریخ نداره ولی قرارداد برای یک فصله. یک آپشنی برای تمدید قرارداد داشتم در مورد…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133886" target="_blank">📅 21:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
اوسمار : لحظات سختی بود برای تصمیم برگشتن به ایران، در مورد امنیت داریم صحبت میکنیم چون خانواده مون ما رو دوست دارن و خیلی سخته استرس رو تحمل کنن که ما اینجا باشیم
❌
شاید راجع به فوتبال صحبت کردن برای مردم خیلی مهم نباشه، خیلی چیزای مهم تری از فوتبال هستن…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133885" target="_blank">📅 21:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
نظر اوسمار درباره عملکرد دو شاگردش در بازی ایران - نیوزیلند/ کاش علیپور بیشتر در محوطه جریمه می‌ماند
❌
اوسمار : به نظر من میلاد محمدی میتونست بهتر جلوی نیوزیلند بازی کنه چون پتانسیلش رو داره. علی علیپور شاید اگه بیشتر تو محوطه جریمه میموند بیشتر میتونست روی…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/133884" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cbc17f2f.mp4?token=esofi2GClfCxxuyU1I7TNq-cwrPTXqLCIXytjLJ40L0er3KfD51rEq5BgNrP04JqnhGG3HGzXbEQYUdNJzwywfQhGhf0c8GJiupq8KJa8MIGwccWEP_fEGxYOERCrYp-y0AN5v8MuoDeOTYUplebMebzfS6hVitSMhx1i6qVwocW46ui_FNbelDDAgXPyDf7CV8imlHR2MlfU34sLS0HucM-rTqrzezPGIzY_WWynVdXsc50AWRtMUvCoJxXnryQ-eIetBJ7GeAdhG8DgKBB9T8X7Tkzq1cnBMQuehGQG7mhHFBBLDy0_QvFDSbrt8PjBOdBNMru28_NRWOWJAWpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cbc17f2f.mp4?token=esofi2GClfCxxuyU1I7TNq-cwrPTXqLCIXytjLJ40L0er3KfD51rEq5BgNrP04JqnhGG3HGzXbEQYUdNJzwywfQhGhf0c8GJiupq8KJa8MIGwccWEP_fEGxYOERCrYp-y0AN5v8MuoDeOTYUplebMebzfS6hVitSMhx1i6qVwocW46ui_FNbelDDAgXPyDf7CV8imlHR2MlfU34sLS0HucM-rTqrzezPGIzY_WWynVdXsc50AWRtMUvCoJxXnryQ-eIetBJ7GeAdhG8DgKBB9T8X7Tkzq1cnBMQuehGQG7mhHFBBLDy0_QvFDSbrt8PjBOdBNMru28_NRWOWJAWpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خیلی دلم برای تیم ملی تنگ شده؛
🔴
پورعلی‌گنجی: انتظار داشتم قلعه‌نویی فراموشم نکند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/133883" target="_blank">📅 21:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26db6eea.mp4?token=Is8lhP-8lnYHD5ZfLo2dg-9cPPYNBmC7JzT75hFQq6qIU_uvK6Osuq4rx2NEYXCdUnnyn4GuQ8zLPUmhkZwb_CWRPhw2Zsawfo7j5m-zo9VWqMQN0sPCvh3YxwDVp9mtEdOv-9fGqv5I8URXXOJ1VO0EKC63BTK_CdZ9g7x9tyFT83QcBaTaOWCHTzQSBKPtPUjdBRIw9Fa8ffo21Sfr23zvYdWFTZDpKJh-m5DxkLo4mcMl70j4Ch0QdTxY9cJCaRGib8WYK_elGmYJdn4bIvDvM1GtEj05HDKDOe2GRZ_VGa-oOwKAA0Afs_fXElJvs6IGBAR9TYr-FJ_7Ekr02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26db6eea.mp4?token=Is8lhP-8lnYHD5ZfLo2dg-9cPPYNBmC7JzT75hFQq6qIU_uvK6Osuq4rx2NEYXCdUnnyn4GuQ8zLPUmhkZwb_CWRPhw2Zsawfo7j5m-zo9VWqMQN0sPCvh3YxwDVp9mtEdOv-9fGqv5I8URXXOJ1VO0EKC63BTK_CdZ9g7x9tyFT83QcBaTaOWCHTzQSBKPtPUjdBRIw9Fa8ffo21Sfr23zvYdWFTZDpKJh-m5DxkLo4mcMl70j4Ch0QdTxY9cJCaRGib8WYK_elGmYJdn4bIvDvM1GtEj05HDKDOe2GRZ_VGa-oOwKAA0Afs_fXElJvs6IGBAR9TYr-FJ_7Ekr02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نظر اوسمار درباره عملکرد دو شاگردش در بازی ایران - نیوزیلند/ کاش علیپور بیشتر در محوطه جریمه می‌ماند
❌
اوسمار :
به نظر من میلاد محمدی میتونست بهتر جلوی نیوزیلند بازی کنه چون پتانسیلش رو داره. علی علیپور شاید اگه بیشتر تو محوطه جریمه میموند بیشتر میتونست روی دفاع نیوزیلند فشاره بیاره اما در کل کمک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/133882" target="_blank">📅 21:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
سه چهار تا خبرگزاری رو حسابی امروز خوراک دادن و‌ پول پاشی کردن، بلاخره وقتی ۱۲۰ هزار دلار کمیسیون گرفتید الان باید خرج کنید دیگه
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/133881" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUV1_f3mtUBRk1Um1IW6c8AwakVTHAa9253i3QKqyIvbuCTZlcXDHV0yQwg08YvjR8fB_LIjpCCjw2nvR8o-27bnNV0FpwgsLApr1cKqTtw_REOCPy8TvE3Thh0t9r9zoIJ3inQMPlZFiu4M03KB1mYo6OeFBXWqTKdUT7w4QLktPW2L5tTWdEYnLjgZpKgSKUA5O5L3no_0n8WBYUeJ8YrF7J7nckNKtOEoOS-jsHyGt-wIx0zvCMVJt26YjmK8Ny1BknB49LNTp4yy985fPV0USNxnfVs1NUqyKgahXKZnu1sER2eiI4m4WOC3UTJScG02akkI8N4RrUimQNYXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های جذاب و هیجان‌انگیز امشب جام‌جهانی رو با بونوس ویژه وینکوبت پیش‌بینی کن.
🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133880" target="_blank">📅 21:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea592625ac.mp4?token=VJ2nlNgTm7k_s6o2SuDbEStkJxdCDPPuRZMUumqBQtMlWS4Xbi-bnqh3tKbodIcAUB0znOhDe_h_mMuSyrOOUNrputLcYYJ2uCIx1sneVgfIyiqMKgxxBfZFkDRdc5V3ydzm7jF0rBl3nSMIdWJhonFZSwHYBX71q52rDN6zI4iGunBiK9HfzJ60_OnF1_52gn9oq24bcwP1xgG-uHNDFeiZKYQg1zXCCgR3zVF87Ny6ATL2sQ8eq-Pb-Dramyu5ShndmXFqs9t1K25eYL24o3XgRuS_-0q8YC1ZTzRsxmJ0s-avxKFqSv4QJQSMXQ2q_CyZZ88l6Dxwk7sOzJoY7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea592625ac.mp4?token=VJ2nlNgTm7k_s6o2SuDbEStkJxdCDPPuRZMUumqBQtMlWS4Xbi-bnqh3tKbodIcAUB0znOhDe_h_mMuSyrOOUNrputLcYYJ2uCIx1sneVgfIyiqMKgxxBfZFkDRdc5V3ydzm7jF0rBl3nSMIdWJhonFZSwHYBX71q52rDN6zI4iGunBiK9HfzJ60_OnF1_52gn9oq24bcwP1xgG-uHNDFeiZKYQg1zXCCgR3zVF87Ny6ATL2sQ8eq-Pb-Dramyu5ShndmXFqs9t1K25eYL24o3XgRuS_-0q8YC1ZTzRsxmJ0s-avxKFqSv4QJQSMXQ2q_CyZZ88l6Dxwk7sOzJoY7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوسمار مهمان برنامه عادل فردوسی پور شده و چند دقیقه دیگه میاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133879" target="_blank">📅 21:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823e8b1726.mp4?token=Q1uOaZX9p-2N1oIXtAIeBHn06uQI57bRmAwk-Xm4gpTGgBeQivhBvLw6A-Q6_V-ZNAxCgGgV6hIgf1bl-TyX3NbZVNyiXVZxpAlxVT4CY9dL-nQkejUIT93n9zmF0xyV6MYMeU7XVcT2DOuENifsozA_RMNUzQNrrzz2HLBRE9BUpHxYqmduwOZkOPqKO5e13m9nAI-8WKmuSxb_GZ8Uf5vx9MR52MA2vGVNBwa1RqgGhA50yjWAVEu7MAti9Ek8Sp0t_GniyyHtjobFHmNSF_yfUBoU41qnllO-fxwLOquTpafwoyITyjl5Vi2scMl52GSQVWmgqIASMA0Gz2IiHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823e8b1726.mp4?token=Q1uOaZX9p-2N1oIXtAIeBHn06uQI57bRmAwk-Xm4gpTGgBeQivhBvLw6A-Q6_V-ZNAxCgGgV6hIgf1bl-TyX3NbZVNyiXVZxpAlxVT4CY9dL-nQkejUIT93n9zmF0xyV6MYMeU7XVcT2DOuENifsozA_RMNUzQNrrzz2HLBRE9BUpHxYqmduwOZkOPqKO5e13m9nAI-8WKmuSxb_GZ8Uf5vx9MR52MA2vGVNBwa1RqgGhA50yjWAVEu7MAti9Ek8Sp0t_GniyyHtjobFHmNSF_yfUBoU41qnllO-fxwLOquTpafwoyITyjl5Vi2scMl52GSQVWmgqIASMA0Gz2IiHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مرتضی فنونی‌زاده: پرسپولیس چوب ایجنت های بی کیفیت را خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133878" target="_blank">📅 20:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
آنا: اسکوچیچ به زودی برای قرارداد با پرسپولیس به ایران می‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133877" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔸
🔸
🔸
🔸
ایران ورزشی طی یه خبری مدعی که شد مهدی ترابی و مهدی هاشم نژاد در استانه پیوستن به پرسپولیس قرار دارن
☝️
☝️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133876" target="_blank">📅 20:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133875" target="_blank">📅 20:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
|
#افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست شد.
🔹
طبق قرارداد فی مابین اوسمارو باشگاه پرسپولیس،مدیرعامل باشگاه برای فعال سازی بند تمدید قرارداد اوسمار باید تا تاریخ ۱۰ اردیبهشت ماه نامه میزده و اوسمار هم تایید میکرده، این نامه در تاریخ ۲۶ اردیبهشت ماه ارسال شده تا تعهدی برای باشگاه ایجاد نشه….
🔹
تا اینجا همه چیز گویای این است که فرافکنی و جوسازی ها بدون ادله کافی و مستندات کامل به چه هدفی منتشر شده.
🔹
حالا قضیه از جایی جالب میشود که اوسمار ویرا در جواب نامه باشگاه پرسپولیس اعلام میکند «اکنون زمان مناسبی برای تمدید قرارداد و مذاکره نیست و به صورت مستقیم اشاره به جنگ میکند»و از تمدید و مذاکره بر سر قرارداد سر باز میزند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133874" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133872">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚠️
ایجنت های اوسمار چه کونی از خودشون دارن پاره میکنن دست پا های اخرشونو میزنن بلکه اوسمار قراردادش تمدید بشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133872" target="_blank">📅 20:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133871">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚠️
ایجنت های اوسمار چه کونی از خودشون دارن پاره میکنن دست پا های اخرشونو میزنن بلکه اوسمار قراردادش تمدید بشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133871" target="_blank">📅 20:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
🚨
🚨
اسکوچیچ سرمربی پرسپولیس شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133870" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
برانکو ایوانکوویچ: مذاکره باشگاه پرسپولیس و اسکوچیچ؟ بله شنیده‌ام. اسکوچیچ انتخاب خوبی است و برای او در پرسپولیس آرزوی موفقیت می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133869" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
فوتبالی: اوسمار حاضر شده تخفیف 400 هزار دلاری بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133868" target="_blank">📅 18:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
🔴
#فوری
❗️
قدوسی : اوسمار برای پذیرش این پیشنهاد شرط گذاشته است که در صورت بروز جنگ، حق فسخ داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133867" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⛔️
فووووووووری
🚨
تا 72 ساعت دیگر تکلیف نیمکت پرسپولیس مشخص خواهد شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/133866" target="_blank">📅 16:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇵🇱
الهیار صیادمنش در تست های پزشکی لخ پوزنان لهستان شرکت کرد تا به زودی هم تیمی علی قلی‌زاده شود!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133865" target="_blank">📅 16:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🔴
اسکوچیچ برای باشگاه پرسپولیس شرط گذاشته و گفته برای آمدن من باید آلوز را جذب کنید و باشگاه هم به همین دلیل پیگیر شرایط این بازیکن شده.آلوز بخاطر اختلافات مالی، قصد دارد از سپاهان جدا شود
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/133864" target="_blank">📅 15:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
💢
💢
#فوری
🔸
🔸
🔸
قدوسی : اوسمار درخواست باشگاه برای کاهش قرارداد را پذیرفت و قرارداد او و دستیارانش برای یک فصل از ۱.۷ میلیون دلار به ۱.۳ میلیون دلار کاهش خواهد یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133863" target="_blank">📅 15:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💢
💢
💢
مدیران باشگاه از اوسمار خواستن قرارداد 1.7 میلیون دلاری (قرارداد خودش و سه تا دستیارش) رو حداقل 400 الی 500 هزار دلار کم کنه تا قراردادش تمدید بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/133862" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
مدیران پرسپولیس در یک هفته اخیر مذاکرات فشرده‌ای با باشگاه روبین کازان انجام دادند و در نهایت با این باشگاه بر سر انتقال قرضی کسری طاهری به توافق رسیدند.
🔴
اگر اتفاق خاصی رخ ندهد، طاهری به زودی با حضور در باشگاه پرسپولیس قراردادش را امضا خواهد کرد./تسنیم…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133861" target="_blank">📅 15:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⬜️
⬜️
⬜️
⬜️
فووووووووووووری
🚨
باشگاه پرسپولیس در اردیبهشت ماه قرارداد اوسمار رو رسماً تمدید کرده و این قرارداد تعهدآور شده است. اما مدیران باشگاه با این وجود رفتن با اسکوچیچ صحبت کردن و اگه اوسمار شکایت کنه مدیران باشگاه پرسپولیس باید غرامت بدن/ فرهیختگان
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133860" target="_blank">📅 13:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSw8Jw6vNlqBTHkJKsHNTQbxhvsb2gyg1rcOYkXNKR5ONb0E2Jqm9Zvu_18SXM2kPlDYIn5UPBP_JUR5GqfFD35cAi_Wk3nE2LQaaWjIu4jNLRIWSPwQsAwQ42jfCuy-9gKKafl0sujKpceV_yc1PEimQn4MvdhNJm4K5ENEPJcLizK8FZbjizkJy-7KMKWB6UHJ3i6UxmsVLFc7UY3WiasNrsCCAFxYNhhWDsyDpzLqE5SDcWiH488MxArxQblbKyrDsPkKQVKEH-EJdRz8UAGgUiOCxFGkU9UyttcHFoTvYtGUk9-faL9flXjG-_FCHSNLKR9vEX7qmlPZh1W7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
خداداد عزیزی که این روزها ارتباط نزدیکی با مدیران سهام‌دار عمده باشگاه پرسپولیس، دارد به مسئولان این مجموعه اعلام کرده به دلیل همکاری موفق با اسکوچیچ در تراکتور، رابطه بسیار خوبی با این مربی دارد و در صورت نهایی‌شدن تصمیم مدیران باشگاه، می‌تواند زمینه حضور او در ایران و نشستن روی نیمکت پرسپولیس را فراهم کند
.
✍️
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/133859" target="_blank">📅 13:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
✅
اسکوچیچ خواهان حضور کریم باقری و 3 دستیار اروپایی شده/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133858" target="_blank">📅 13:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0j0UaNVkMoE7RoN-L6yhXHSf9ZaZNzmUmAmd84lu1VNHTa6-dkaWDkVDKXnmLdut6nESElSUcL5AFpTfocl68PFpbKAbI83cYgCGEkfb1DSV1pQvEVMNT_hMKh7kqFNVzNlOxF9hf1sq_NCGUn3pfMqBfCT07u29wSYkjH81ek-jm7wA4nW7wpmwktXZi_1QZKeGZRH2vCOzGcKBawwJIbpWkBC-mvbm7zEagdo-nNVanbpAzE78AFugmEF38zhkDcpL6bJxv8zE03-7W8U4Ed1OlBEk-oJowScXZaWpfuiCR762LL6sfIRfNgENrviyhD88t44fLaHvtg5hcrSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این بار از همیشه جدی تر
👀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/133857" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8A6ZEVu4JfY6OFOdMSGM8EQJ1t9G5RfiBhgeo0mTrzzLVaWDGGCSxBclbcskgyh28lKrPj-DUt1tbU8NIaPMvkfkMEj7eFhGcdZeD7XEKb9YbN_G8wyjNPGEkQLhe1_gyMlEYuY111YNy0a-Gy-BZA7ayrmA7L7jA3R5Y-YDiEf_ZTrIrgihBBXg9SQivnhXZxh6VmSFeUjlV1SbiN_I29EdBRGaAa1pb0eLf3ZlY9gZy9pHlje257xmKopBZMMH9QHmhBGiD6ixGrU5kVUHlMAEbQz09ID_hvNSY9z_padqUJyD3ORqaVnDNql3rWyq9TdPvrfFC7tn9vtCsYMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حسن یزدانی با کسب دومین پیروزی خودش از 3 مسابقه مقابل امیرعلی اذرپیرا ملی‌پوش ایران در وزن 97 کیلوگرم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133856" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
جلسه مديرعامل و سرمربی پرسپولیس برگزار شد
🟦
🟦
در این جلسه که محسن خلیلی نیز حضور داشت، در خصوص قرارداد و مباحث تیم صحبت شد. قرار شد طی دو سه روز آتی، باشگاه پرسپولیس نظر خود را به اوسمار اعلام کند. در خصوص تمدید قرارداد، مسائلی است که حدادی قرار شده آن‌ها…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/133855" target="_blank">📅 12:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/133854" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Chejo3RpCXXRIFt4dBMvXJ5uVHyFyJlDxNG7qOexebYsJQ6UJEWYBhFSUCKAGYZn12JWuQlsjlvxxu_hSDN-4NqJRUuBwemgI-zdggGw_rvXZJmhIefUvZxDvCedWi-SVaDrlVRVwHbm10mtp6vubipDR5mE9NUqYKKioVMKgGMCM9wG3uIjJp2G29IxdnfDE4a0JHdX77wYZdKxH4xFPW3dM9yUlJO3L40LYUV1b9hWU1Vujf3_0PFkVB-G_RGjCefHIngdlVaZ4iCtD1PapNiaSYQhQvo36PK7AhVWUcZeSoTVCGeDnstBEt6AiuDZ3ktAWapJ3i83gT3BopplUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
فووووووووری
🚨
تا 72 ساعت دیگر تکلیف نیمکت پرسپولیس مشخص خواهد شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/133853" target="_blank">📅 12:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMhyeZZ6NrszQ_f06cxWmLUjWFZIQ6kH7I2T3pkX_B2Gy1u91YODbtSzBBojwEnAIbHSz0iOuAVqwUYvp6yb-_MT3IB29euba8bbahaGgsnO_BZvBuMFZBwLWh7N_dZbChESyez-doWmCd88qL67rB37wOCFgu1iQfMdyCNgQ7m6Cm9CuEieQyWg7hkRaCJSkwhpdh4mxxakxoaQsZwltAuhORDy90BXI_7mpc5J7kC4IQe5Dc8KPlCYu2ENxDxjxLLDDDAlPF8rhM1K-LwYIECjhPOX3fNQ-Ug4CFODBC9YbBmOSzN60eEPWWwnwkwWPPiDUWR3vhEdjl9Q2bBhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فدراسیون فوتبال رسماً اعلام کرد تصاویر منتسب به محمد محبی جعلیه.
🟡
فدراسیون فوتبال: «در پی انتشار تصاویری منتسب به محمد محبی در برخی شبکه‌های اجتماعی، به اطلاع می‌رساند تصاویر مذکور کاملاً جعلی بوده و با استفاده از ابزارهای هوش مصنوعی و تکنیک‌های دستکاری دیجیتال تولید شده‌اند. این تصاویر هیچ‌گونه ارتباطی با محمد محبی نداشته و انتساب آنها به این بازیکن ملی‌پوش کاملاً نادرست است.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/133852" target="_blank">📅 12:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
پرسپولیس برای جذب قرضی طاهری به توافق نهایی رسید/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133851" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
توافقات پرسپولیس با کسری طاهری انجام شده ولی باشگاه اون رو بصورت دائمی میخواد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133850" target="_blank">📅 12:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
❤️
رسانه‌های بلژیک نوشتند که تیم ملی ایران بخاطر سفر از مکزیک به آمریکا، دچار خستگی شده و این بهترین فرصت برای آن‌ها است تا پیروز شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133849" target="_blank">📅 11:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb299e65f.mp4?token=kth5iwE4G94tRD__e4aXERcYDf46ZhG-jW1axNPbRYcQf_FQD6jqp-A0taFaHJ6tBjCEoPabZ8c5FL6qwrJEQp9zdxhSDkCZOIdwVQ99Up7lCPacIWJERc_Jmt8HXjUxUDliaZjMghJR7eHEXrJn2vYfgwCfbisIP1daIMEH6CLK4iglgRrXwTMtprqsgRd3ARkM5h9K77VapprxrpjhVdMI94qZTaGIjlkjVAIcYY327e1-p18-1HMio2qoxAktmdLG3JP16UmEbs3VEfa8jBkDmUJ0dPJSFiG2Zqot8VfyKNYR2gJZ3O9Z23ZBWwVByFokz5ddpXxV5osZoKivQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb299e65f.mp4?token=kth5iwE4G94tRD__e4aXERcYDf46ZhG-jW1axNPbRYcQf_FQD6jqp-A0taFaHJ6tBjCEoPabZ8c5FL6qwrJEQp9zdxhSDkCZOIdwVQ99Up7lCPacIWJERc_Jmt8HXjUxUDliaZjMghJR7eHEXrJn2vYfgwCfbisIP1daIMEH6CLK4iglgRrXwTMtprqsgRd3ARkM5h9K77VapprxrpjhVdMI94qZTaGIjlkjVAIcYY327e1-p18-1HMio2qoxAktmdLG3JP16UmEbs3VEfa8jBkDmUJ0dPJSFiG2Zqot8VfyKNYR2gJZ3O9Z23ZBWwVByFokz5ddpXxV5osZoKivQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
لحظه شکستن پای اسماعیل کونه بازیکن کانادا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133848" target="_blank">📅 10:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔸
🔸
اوسمار و حدادی به زودی جلسه میزارن و راجب درخواست‌های اوسمار برای تمدید و نقل‌وانتقالات صحبت میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133847" target="_blank">📅 10:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133846" target="_blank">📅 10:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
مدیران باشگاه پرسپولیس هنوز به صورت رسمی برگه انتقال کسری طاهری را از روبین کازان دریافت نکرده‌اند اما انتظار دارند این موضوع تا 48 ساعت آینده رخ دهد و او به تیم پرسپولیس بپیوندد/ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133845" target="_blank">📅 10:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133844" target="_blank">📅 09:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
نتایج شب گذشته جام جهانی 2026:
🇶🇦
قطر ۱ - ۱ سوئیس
🇨🇭
🇧🇷
برزیل ۱ - ۱ مراکش
🇲🇦
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند ۱ - ۰ هائیتی
🇭🇹
🇦🇺
استرالیا ۲ - ۰ ترکیه
🇹🇷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133843" target="_blank">📅 09:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A757qLKqVNOel__nWf1neD1xPBJGpn1JBFtiDqn8b3AluRLqxR18QvPaHve7kGS2HiKlIy8I170VfkplPNd5zcp9xGhfgoTTvoKsHGTil3OIo475Gw74_s-K7-NYoAY6QXi1ENs-fvQGeMk5gkQ9W0DJtSZ4jsyKFIc5sr1gmiSe1M4714PfaJiUfPkd3xHtPIAiaQQrNfSNR3wnw-XfmGDbxqmtwQ_U8RicS22w9_FW7r-1mOCUBskHzufOtmIRWNnGOFh6L7PLDDXvgE0SY9qHKOWUW5HaxFiJnbSpa3-Kr2AW0-4d45gm5LthtSS_aIk6VC2wv0xEBA9fFdv4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/133841" target="_blank">📅 09:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj4iqMnJwCZxiXYbK_WQFcCu9AHNaMPpmrvlFaHTw6z10cK00BZEfRhX3Fe9ZjzWHjZSD68jmB91x3jV28VLF3OBrSFt77oOlGTDVBOU8rnlCJqMUPMaPu-pMR5TqvDzoWQNAuA4IqLlJLVMebCGs6cV3n5PrFzsKEViFrPNeyyfGzoTRbFekRv3CMEHFh3zVVoJMAwXSlg-FjHT31cjOUYcsIrSqL98NK_NEjdoc_Yn-zIVkdv4Mr-_7mOaOs-yMeNMbeN0mcCayGAOUmy8vfNqQfCtkXCWOv421bOVE8TtPyGkoUUYEv48_JwiPBZkjYxo7waCcbN2tJcm5YEj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه A جام‌جهانی ۲۰۲۶
[
مکزیک
🇲🇽
🆚
🇰🇷
کره‌جنوبی
]
⏰
بامداد جمعه ساعت ۰۴:۳۰
🏟
استادیوم
آکرون
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/133840" target="_blank">📅 01:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
کسری طاهری با قراردادی یک ساله و قرضی از روبین کازان به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/133839" target="_blank">📅 01:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133838">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/166bff416e.mp4?token=sArildA3xxuaI4wVo8rigoXBAuefhRf8GWOR3CNO09AwEPiFZVuAUs2zF9oG7vjXMsCSS0rRXMdlFeYLFTEjFPyCJ-xG6TFdjSGeI4iLC09Dp7EWmPS_NUxQutzDW9SJz_qOrAdUZJcI0DE47yDvYg7GdzmRM1OBePMmEgawAFOclpPyF77Ev0je4fv0PN-RFXDW_pGV6oxmbIhTNhTRG-tzV1pzEHV4pZWhBjwgKrWxYyhYOgem2T_84W8CGtNio4I8W8HPeYGbgvE5OP6w2xFvHwwYJb4TZrxV3k0GWVJVARVsyCFbrrbc9zBgogP1pdHRMuxcZKkL9KAMca3YlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/166bff416e.mp4?token=sArildA3xxuaI4wVo8rigoXBAuefhRf8GWOR3CNO09AwEPiFZVuAUs2zF9oG7vjXMsCSS0rRXMdlFeYLFTEjFPyCJ-xG6TFdjSGeI4iLC09Dp7EWmPS_NUxQutzDW9SJz_qOrAdUZJcI0DE47yDvYg7GdzmRM1OBePMmEgawAFOclpPyF77Ev0je4fv0PN-RFXDW_pGV6oxmbIhTNhTRG-tzV1pzEHV4pZWhBjwgKrWxYyhYOgem2T_84W8CGtNio4I8W8HPeYGbgvE5OP6w2xFvHwwYJb4TZrxV3k0GWVJVARVsyCFbrrbc9zBgogP1pdHRMuxcZKkL9KAMca3YlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مازیار زارع:
✅
پس از مصاحبه‌ام علیه داوری فینال جام حذفی، علاوه بر اینکه حق تیم‌مان خورده شده بود، ۲ میلیارد هم جریمه‌ام کردند!
🔴
هرکار دیگری می‌کردم، دیه‌اش کمتر بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/133838" target="_blank">📅 00:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
فاکس نیوز به نقل از مقام کاخ سفید: مراسم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
🔴
این توافق هم اکنون لازم‌الاجرا شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/133837" target="_blank">📅 00:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
تسنیم: اوسمار تخفیف نداده و تا شنبه تکلیفش مشخص میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/133836" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyW9b2xDQb0Fo1uqMNkyE4tBqd4v0YjySjh2_vKPaDRlLyVzyvMiWvC4XjyZSNKtmfWY1Qeap5KTZsoM6E6p3bsL2e1F1yoaWWDcvLHS2d5OPyhdxJtBw4wr4Yh17Lysj75190p8gf6XbKwylXqTAnrD2mgBFtet-DFSYhFqpxfLxCYuvFlDP7gG51cGPwu19ppxGoSgxtpMXM9hTHNvRBVNBMB_SRMfBzV6gkSeFWozeSVxJ3WQ-vpm-Q_o77DwOoRkSRxEwIeBVKbfDrwJgSuSltYh5YjhwaEuBUR5VZaUTTeFoY8PuQfTSfheQLGGcZrFcEiEOK_YSL7c6kSQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
روزهای خوش در 36 سالگی!
🇮🇷
فیفا، رامین رضاییان را به‌عنوان خلاق‌ترین بازیکن دور نخست مرحله گروهی جام جهانی ۲۰۲۶ انتخاب کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/133835" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/133834" target="_blank">📅 22:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
اوسمار برای توافق جدایی پول زیادی می‌خواد!
🔴
اوسمار توی تایلند زیر ۵۰۰ هزار دلار می‌گرفت، وقتی برگشت پرسپولیس رقمش رفت بالای یه میلیون که همون موقعم بابتش باشگاه رو زیر سوال بردن.
❗️
حالا خبرنگار آنا می‌گه اوسمار یه میلیون و هفتصد هزار دلار می‌خواد! پرسپولیسم…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/133833" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133832">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qii4zcLb-UVqJz1qY3UrdoWMhlyUuHpI2swCAohRCYBaM2SnMf3KXHPUmC-Pa8P5Wi1UNVItLcm8ynhnGtPcL89VvT3Yw6JS9DaIhLztoGSz5aq5zwpzrFTyg7PE4mr8T7snnOO4XnkUo4WffLA_1o5omr1SQBsi3NXpxZoVm6qC7Br9jPawnC51IOvwHLn1yEYPH3Jgm20I0nzTrkRis7nJBJRt6sxxKTSfX273ThZlFfwVLRX1RDVBpwHRRXoq34T_0_s5Hf5DTa6weL6ckufd0WO6BHEdGiJieR1Cde-gs-eoCIoKTM_MGGftod0tPsZ9aBqdKo9VNM-RbDtEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
الهیار صیادمنش در تست های پزشکی لخ پوزنان لهستان شرکت کرد تا به زودی هم تیمی علی قلی‌زاده شود!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/133832" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔸
🔸
اوسمار و حدادی به زودی جلسه میزارن و راجب درخواست‌های اوسمار برای تمدید و نقل‌وانتقالات صحبت میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133831" target="_blank">📅 22:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3VdkgKVPU3kUEd5rwziiJzOwt-xtgtxY5V-BlS4Q1Bn0DEGozh3G73_VA4A_1wc7m0bCbcpbkTZeSXe-8EcxmqYRUebYa9r9tqw_zZUvC0Qy0EWzNlg5IzzjLKgL0GRPqySFI3mTuySPAOsDgV_IQvf-Lno-2MyWB0iUj5XGDB1bC2wwCKE6R-kso8fb8v1LQDtx6_UJAoqgO-Hgd6IIXvrVoa2aX3BMrAih-6fwFxtAoufaPQ9BMW1w04Jeg4qcPqn6LN5gnNihJfj3nkltZpmGeMKD9fTlq1dKWNVcaMKxLPJjCDWfn_xh_Fw6J1xulb8AJDnBSTGl-BKCVHdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133830" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38845ba49a.mp4?token=D6ZrZ_nJpmVfm4gHm84HGOLvZUgiTyQmQqmneaCPsjyq61r-Lsmb3gsEXKr4OJcUztJ-1nrmDViJeuk6nUpmF631n8nz1qXColXQuX9Zk52LydTevC3UadtKHpUtYw3gtwqpjHJost4aCUedvMjTcetY4EVPfxopgTzPLXn2BMlQlN9onwaa9zTHgCv-MIuamdmnWXCh_5fYJMqlDfz1_YZzT510vZnL-IHcKYQobMroQa-uZd0OV3VE6vQwKLv282IbVZhH9VRt9D1LNyZE1V0LW_t-Szi5Jj_dgL7x2GWg3Gpa15Yo9fTydTmWx9Lf2qVGxdJ92bT6ysXEcJU20g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38845ba49a.mp4?token=D6ZrZ_nJpmVfm4gHm84HGOLvZUgiTyQmQqmneaCPsjyq61r-Lsmb3gsEXKr4OJcUztJ-1nrmDViJeuk6nUpmF631n8nz1qXColXQuX9Zk52LydTevC3UadtKHpUtYw3gtwqpjHJost4aCUedvMjTcetY4EVPfxopgTzPLXn2BMlQlN9onwaa9zTHgCv-MIuamdmnWXCh_5fYJMqlDfz1_YZzT510vZnL-IHcKYQobMroQa-uZd0OV3VE6vQwKLv282IbVZhH9VRt9D1LNyZE1V0LW_t-Szi5Jj_dgL7x2GWg3Gpa15Yo9fTydTmWx9Lf2qVGxdJ92bT6ysXEcJU20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133829" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/133828" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
فاکس نیوز به نقل از مقام کاخ سفید: مراسم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
🔴
این توافق هم اکنون لازم‌الاجرا شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133827" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6ECQuqauhw2h_LgNiescr3ep69Cr5JwveVVvA7ddBKVQlm8VSry08vQfPcQ68J6B7B-q0nNuS63sSVhHmrgcutOFQDOIcJCy624jJV2i1CMNV86EvcW8K6bSyC50lyqkGG-uIGXIdBRAMF4_UiX0R93T11hpeStKX0K6UwVncXiHWr-U9nec3KaM5X3oZ7xa_bMg9czj1GAWhsgIi1Rc4azNAnhSTJiljPp5WQtfxF5y52lcUyQYctR8N5XL1naiwQSSkiqyUa8N2TgK3RrAVqaSwwz4mMZR2h-hzg86Fexhah7kgif5Xu5IqgMm1lapqjTFJFSTQ-b4Xf34wH4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اوستون اورونوف و ایگور سرگیف اولین خارجی‌های تاریخ پرسپولیس هستند که در حین عضویت در این تیم در جام‌جهانی بازی کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133826" target="_blank">📅 21:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133825">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
خبر ورزشی : اسکوچیچ از پرسپولیس در خواسته قرداد یک میلیون و هشتصد هزار دلاری داشته و ظاهرا حاضر شده ۱۰۰ هزار دلار تخفیف بدهد و هپچنین مقایسه با پیشنهاد استقلال  این مربی قیمت دستیارانش رو کاهش داده
🔴
🔴
و در صورت عقد قرداد با پرسپولیس سه مربی اروپایی به ایران…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133825" target="_blank">📅 21:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
حبیب کاشانی: برای حضور در پرسپولیس با من صحبتی نشده است/  برخی می‌خواهند خودشان بیایند اسم ما را مطرح می‌کنند
🔴
با من صحبتی در مورد پرسپولیس نشده است و دنبال سمت مدیرعاملی هم در این باشگاه نبودم.
🔴
پرسپولیس باشگاه بزرگی است. من با همه علائقم پیگیر باشگاه و نتایج تیم هستم.
🔴
نه صبحتی با من شده و نه من پیگیر بودم.
🔴
برای پرسپولیس آرزوی موفقیت دارم. برخی نام ما را به رسانه‌ها می‌دهند درحالی که هدف دارند و شاید افرادی به دنبال این سمت هستند و با مطرح کردن نام دیگران و استفاده از نام دیگران فضا را برای آمدن خودشان مهیا کنند.
🔴
این‌ها شبیه بازی است و صحبت بیشتری نمی کنم و امیدوارم پرسپولیس به آرامش و روزهای خوب خودش برگردد.
🤩
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133824" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPY7UsMCs-tFGW2agSfFLiFNGke_LDdQVt6W_e98ykhPJoJ4As5R6TsuZjhV4_9WhAV5bPRFpJ1_toPzSh5X19YCwF_vLKScFPkId6T9F993o73-2O4i5cRk-_omgZ8anckgpwm1UlumMxAkYaIECUm8G-dyWvqADxScYr1ruPyKbudQYaEiDSLOP29BxDKQ5lR2QRPRgLir2mu_pBL_3RoWzWc6z6-0UdkBwcrsKzYz3lgrsP6-2YTIrZgYcKDDrXjtEjgS5N2mLGKgo5QZfCfzp4QVqWLl-hNN0K4sZ7VbyL-bF1i3JfK_Fm7SwZL1kyiCF9Lj-s0LdVmqzIogUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه B جام‌جهانی ۲۰۲۶
[
کانادا
🇨🇦
🆚
🇶🇦
قطر
]
⏰
بامداد جمعه ساعت ۰۱:۳۰
🏟
استادیوم
بی‌سی پلیس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133823" target="_blank">📅 20:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
حمید استیلی : با وحید هاشمیان صحبت کردم و ایشون گفتن که آقای انصاری بعد از تمرین گفتن که دیگه نمیتونیم در خدمتتون باشیم
🔹
ناراحت بود از این مسئله اعتقاد داشت که فاصله امتیازی ما با تیم‌های دیگر خیلی زیاد نیست، پرسپولیس از صدر جدول سه امتیاز فاصله دارد و حتی…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133822" target="_blank">📅 19:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133821" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133820" target="_blank">📅 19:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
بازگشا: اطلاع رسانی لحظه‌ای نقل‌وانتقالات به سود باشگاه نیست صبوری کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133819" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
🚨
حبیب کاشانی مدیرعامل باشگاه پرسپولیس شد/ فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/133817" target="_blank">📅 16:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQA_IKu_pI3SyQMWw9b5RrPVMNQO0mpYd4CrXElfEipvbM5OtZYadBgghFD3h94I2C3Vf5gRpNWMy0eUplvoPIE_ZvZ-bAgzjdQYa6lYMG1sgnZy7Ci9NnkE0JnGmXkFC-04BDY5fXfKq9-fK_tC6cBtymuUC1nGuE-_eGpGMyOGLu_v1ik2AIlp1fGQ79McZ9sz5ebb5CIkb_ZPm3MuSq8v3SmzdZEefwslZK3nfs0XgZC-6VMIbqREzH960dJH7pKuCJZT3KVyPeuWjbSpa-C8anAlxOVIzk0ySnOQFjAk2xsfYsjcwM-ctnDIQhE49HPPHv-6fsXYPJX8lH1tsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصاویری که از محمد محبی در حال پاره کردن تصویر مهسا امینی و شعار زن، زندگی آزادی است، فیک و ساخته شده توسط هوش مصنوعی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/133816" target="_blank">📅 16:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HjYfDu_IZSSTlmrsfpL_5O77uSKyw8uDwlUCUd963xE9YXskst000lSV0ol_pbpre3wMopTuOskI6DUyMuOzt73LbVvnzPNb-lNbkErR-tmDyp7lzMeL7RG8V79WYGJjPqPX88edEnKtlKSRk-JXgC4Mk058UnX-61VdcGtME5N9ca58VanWPh08kP1KDUIacGvHWNz5qH7eBLKwsFEXZlke-_C5tCRREmn5wXyPJOO2cMLoC9nVvL1XSkqzUos0pVe2yJdXJSCrKPF9Pl5AsPSuYTCuJ_AfBHgQbYF_y6ej-O4D20JnHHScF7mLOOOGP1BgNY7uuCGdeGeNYSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازگشا: اطلاع رسانی لحظه‌ای نقل‌وانتقالات به سود باشگاه نیست صبوری کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133815" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
خداداد عزیزی که ارتباط نزدیکی با مدیران سهامدار عمده باشگاه پرسپولیس داره و بخاطر همکاری موفق با اسکوچیچ تو تراکتور، گفته زمینه حضورش تو پرسپولیس رو فراهم میکنه / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133814" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[💠🍃 ғᴀᴛᴇʜ ᴬʳᵗʷᵒʳᵏ ]</strong></div>
<div class="tg-text">یادمه کریم باقری رو ترنسفر کرد و گفتش ابرام اسدی فقط پنج درصد با کریم اختلاف داره!!!!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133813" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaavrAIbaMJ0B-obdbj1kJpPNN_6GUrAxvI-UFCm_ALAOZK1CgwnZalfNDvJt-P4OaDXuRte1MFYFEOQvVUvAXMBKWVstUP3G7pMlBoNSsqz9EgM62qT9WS10M1wM5U6_2Acr3ZoMNwticYPcM1lFS9n3Wm-Nmb1qmTOkNEElozUfskMZUV19FwEBoOsSIixYmLhGefQTMEDnGERGI3HNKRjPwuB7USmbVSFgQIu6I1SYumMjPZDq5Khwvk8E2DRzKuK38i5fyJGsLks_Vudn_-tGf81VOTBBHuzZ9N4nsN-lmfKGBdlgP92VAr0jNUFugQotP2KnUZqwIn0I4J_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
🇨🇿
تو بازی امشب آفریقای جنوبی و جمهوری چک ، سه داور زن آمریکایی برای اولین‌بار در تاریخ، داور یک بازی فوتبال مردان میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133812" target="_blank">📅 15:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
🚨
حبیب کاشانی مدیرعامل باشگاه پرسپولیس شد/ فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133811" target="_blank">📅 15:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">یادمه استقلال جاسم کرار رو گرفته بود جانواریو مجتبی جباری برهانی خسرو حیدری این اقا اومد تو برنامه نود تک تک جملاتش یادمه گفتش کرار بمبه مگه؟ جباری جلوی  کریمی بمبه مگه؟ با یدونه خرید کریمی داشت پز میداد فتل بازارو جارو میکرد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133810" target="_blank">📅 15:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خداداد عزیزی
، سرپرست
حبیب کاشانی
، مدیرعامل
یهو
حمید استیلی
هم سرمربی کنید
یاد دهه هشتاد زنده بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133809" target="_blank">📅 15:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝒎𝒐𝒉𝒔𝒆𝒏</strong></div>
<div class="tg-text">به خاطر ۴۰ میلیون بدهی ۶ امتیاز ازمون کسر شد تو دوران این ادم</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133808" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from@M</strong></div>
<div class="tg-text">ارش برهانی تو باشگاه  پرسپولیس باهاش امضا نکرد رفت استقلال</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133807" target="_blank">📅 15:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
هوادار هم باهوشه هم حافظه خوبی داره، بخاطر همین نظرات مردم رو گذاشتم تا چشم گوش عزیزان باز بشه اگر دارن شیطنت میکنن….الله اعلم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133806" target="_blank">📅 15:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">کاشانی سیستمش اینطوریه که یدونه ستاره میاره با سن بالا اون زمان (علی کریمی) بقیه بازیکنای معمولی و دلالی اون زمان فشنگچی میثم بائو نورمحمدی و امثالهم رو کرد تو پاچه تیم سپاهان و استقلالم هرچی بازیکن تاپ و درجه یک بود جمع کردن تو تیمشون</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133805" target="_blank">📅 15:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhossein</strong></div>
<div class="tg-text">همین حبیب کاشانی تیم ملی امید رو داد دست عنایتی و نابودش کرد
بعد رفت سایپا و اونجا باند دلالی تشکیل داد و سایپا رو نابود کرد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133804" target="_blank">📅 15:14 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
