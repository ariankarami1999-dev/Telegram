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
<img src="https://cdn4.telesco.pe/file/Lh2ZfdS_BIKon-QQ00dD-TgNJX8MTFZN1MVu-fsgQf_qG0-Yio5zzQk68bkMqxR84btW2krSeC96M0s9pv2TS5YtlIqbw9fk--ZVIG5uxGvO8gYanDUNOj7t2lPqKFlKZgWHa_pWDN6L9VvW-QZY-Gh68znR8ZwjmfNmUob6f9lUSxixI4-fpcrN7K1GbYC8bgcMDTinLa4U24DtOHkY1RF-InqnJHnk7YY64cGJxJDKgI3Pi3-2zzV-90fZFLiQ05fKr84uWEJT6euu8wdJvkqFaoRmCUJAQSzsNG0UjHo_wGM_y7E7fGOPPVyMaLgFSlwzvyFxUu49C4R5SP6W-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 16:56:40</div>
<hr>

<div class="tg-post" id="msg-81952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/funhiphop/81952" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مگه اپلود تو اپارات نیم بها نبود چرا طول کشید انقد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/funhiphop/81951" target="_blank">📅 16:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/81950" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm8KiK15NuZrRc1n05q4KVagUrT-RfjYMRCzXHPIgURsLQO8bOmtstoaknUTbq5Z-RthbY5mtDd6Jz0zt_3XL88eD4gjuQ5sadHvNlwYijQ_JNFjCwvdxHdnnZsjCMW19eBaiDZ0LogF-uAxrozwOifWlsrYHANiPXYtbe7NEKJNql5CptkNxJosQ2RKdFRudit7eUHHIOcQCv3jr3cQm000-9BXpui8vsE9qbVeDvhIw7tKjIjt0QfD_uYGtP9WcxVB78EwTu0Sba_iDQLlZTGJfsCNbEoeXv9-pRyK6m-cYsVgW2KlJu6HJWEm9sjk0zEOXPVn7re0zjYWX270pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
لینک حمایت از ارتیست
هست چرا یوتوب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/81949" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/81948" target="_blank">📅 15:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/81947" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCFRCdKh2w4Bl8DSe9wIcjiL0jUDNW53VttyP82FqApKPjIgRY2uVsAfRLbnWONv0tSR4PPCMTpgjSfBH2gXKlJ4hGyAT5kUaB7aXcMtEAovYW1Vt3F_kCYRTIFFTetEhGA5Qo_N65C31_cKhUG6OyQG7tZ2IVjt2AVMDAJV_LlhsrFHFnqYYe6PMQDLKCY42XIC8FI5F23FcxMFCGo3E0VSwcYYVDY2nskLT2TXbi1Y-fF3XPCKRMxV40g84Vj3rotZ_R_KNQxHFzUxVnpDn21ezDjlrgYP4tWjLQ2m8vMv9FZLwhDlGpWTIVvKzCnGea65lbSNCwZUG5qyUC1IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریود شدی کسکش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/81946" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKXeNHnQ2NP_zjqcGacd8h42JBrXFrxpOrNNF2hzXori6PtZrc6ZS7DaaQM-QNsUqSyIWox5V8lkX1QCWMbIxBNgP6gI1pQy8uc5wvnKQVhtrL67o-3a9JG1b5NiyEq5PMStpPoyoN9831EZD3TzNoZRghe4WmwWfRu6hD7LZnOqZ0StkDo86lDdAl7fgisi0KAudzqYvt3Cn5DDiE-Gq4K9gLFHmxXV0cMWLGGGr0rWLbnQs9VwK3tJQai5ooD4L4YZUrmKM-vQaZZqmgoY8OL2G8aCjtS5djq825_QIi9rlCbF8xnuDZ-OJkTQVYWRIixeeZC_z9wj-nqys57ZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81945" target="_blank">📅 14:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبر اومده بابای مسی فوت کرده ولی هر چی چک کردم خبر مرگ مولرو جایی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81944" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">صبر
صبر یعنی واکنش در بهترین فرصت
نه در اولین فرصت
پوری دوباره اینو گذاشته چنلش
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81943" target="_blank">📅 14:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=Y6apdCxM8j16ST_zT-iNo9_ymZaLsI6A5aclFhVYgKAdfUEyLgIhZVw7I87dXeVCjQCygqqzDViRSxRrXRj6eCDzEJRWywSaITlUY2eU7nPFOJQ9X7sXoh-IGmGWk1SkJVerP_X3FA_7zImMFGF_mX4gv0SWEopAmKmp9q75XYRPWlhFU3ONwa3K8TYOUiYV--UTzH5Yg6uDiHyGSKXs2mPiVBvZRlHFFiCDFKfBDbT2tlq0L9WXbp5bNNvXiKcPB9KJkgH33vOql_fjKGhexLIpwqUXXf2tyINrSvjs9AohzvgXIjKf457u3RWVDCOjKO0T39LLG6yWAJMpGXyfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=Y6apdCxM8j16ST_zT-iNo9_ymZaLsI6A5aclFhVYgKAdfUEyLgIhZVw7I87dXeVCjQCygqqzDViRSxRrXRj6eCDzEJRWywSaITlUY2eU7nPFOJQ9X7sXoh-IGmGWk1SkJVerP_X3FA_7zImMFGF_mX4gv0SWEopAmKmp9q75XYRPWlhFU3ONwa3K8TYOUiYV--UTzH5Yg6uDiHyGSKXs2mPiVBvZRlHFFiCDFKfBDbT2tlq0L9WXbp5bNNvXiKcPB9KJkgH33vOql_fjKGhexLIpwqUXXf2tyINrSvjs9AohzvgXIjKf457u3RWVDCOjKO0T39LLG6yWAJMpGXyfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هههههخخخخخقخخبخی۷خخخخخخیهیهییهیخخخخخ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81942" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag830o1Qpif_bT3WsDfhVolgPLPFmgzSXDeR8HQJ1IuGkG-WfrrkYjBrsmW9UTM_GaJZGAo5pGI5N6jIy3mrRLgQkpdVK_E10YQ1jgdqpd9q1zqev_mR1dNM9uGjYzriBboTPnTE4jCa0DgzJGjyUF9eZ5EkaMigC1pEdrR5BlPS_q5NwA87NTCQSJ3hMEIjWWzOlsptXsvkOS0asHiH-gVxX6dw83uAzxoSqTsW--r7s6b_GYv86qSbkcVYYYjOdSGRdpBybeijyamskA_hojcfwi-ia67W_rrp844xTRwAvtepF2GQX2S1z6TNj_loDp7qqWG-xVW0b1xP3yJ28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81941" target="_blank">📅 12:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVRpSUA9eWxOOTR6NoeulP0hsjvSijoL1jFXx_TVgSxEL46sQHzdZXUr9ZJz4d-A_j15YVMdOeap9VDB2EE0M9lMaYTiaQbOFl58Cdr6_FjIV7JxkvknIkGfRdYn6RMkPzDQw3jmugeJjok5Qk1SMSklJYykw3pYQG9G0O-sx7TQmjL11Oa8bSOq_tx47D1DnynMdVlwHgYKFCvBAV4sekMOgJfrnI0KAht8_LB8Jx24qEdyB29yb7BqMvN2sWTNR67pXLDUixQS0p--wwWbBirfGVsK3zUpy_b_ySC_6WJ1_ofdZd8ySiAaKJ0GiFMNPCBkVSNYkAkrUk7PUHFXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81940" target="_blank">📅 12:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTkg_YkzV5n-xrrPTMKyW9875BHbzs4jf3YwiKkp0wbOkT_61wItG9eJFWHG6lSwaOZwRxqON-sn6KcTDwyre7XNB_ji08ryOLWhwOkN9hNgqVRTaUvCZFqfBR0G7oDIHPWUv5bWwqLq3NPiE-u0NiHXhEl0X2PLT9GUkukUoyzdjVz12S0vKLvvXpEaKdqanONmjm-70W4dTZ2g3QRtSBnim-zF9hpqnkjJMNfeLNk1ji1rbv_4TIUWveu5dr3SgWaFvrEunBXq_sED1rfzQS5Z8Sv1wpMgSNCroZtzO9_Nr4mLZ28sX9Vm_-v3WltiXspWupcwdepfDrp5BVoOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه قضائیه: همه اموال منقول و غیرمنقول ساعدی‌نیا مصادره می‌شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81939" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpZKRJjGek4yBZwSauJk5VPrjH5H-PBFLwpvjZBu4DYXraTQDzCb9dCh2uqExOC-jJnUi1hdagOjKqs35lLrirkBNZVUcBbsY7FDulkBVpcm1vhDwcAN3pIpeU4DhgmaxLmBzLwBufGXYysaaOKp6qgORmltCOtOg5XtYHfzfxFHqvK0zCpsd_bw69dbaOa3tSBebdBM_E1f1OQH9lM7DV2kj5tmjsRy3oknsC607LIEiDBo7D8YHGULHwMJvinZbA6PGLnQxTbEbQW1lAeVAachAInve3fLDImmzPKTTDnHyeuoBySET8N3uxCyY_kU3od8DG4mHzKyrE638KU3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۱۸:۳۰
🏟
ورزشگاه گاملا اولوی، سوئد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، پنج برد و سه تساوی کسب کرده و در دو بازی شکست خورده است.
✅
منچستر یونایتد در ۱۰
دیدار اخیر خود، هفت برد و یک تساوی کسب کرده و در دو بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۲ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۹ گل در هر بازی بوده است.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r17
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81938" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYaKfRdbbGRpONpZ79aEjirh8GgMSAjpftRQ1YkmgwVp1-jWdd-AtN-gdeyA9QC7MmFK7BK0jWkI9g8egJVrD6dtbyM_wnK4cEAN-qy8QJDOyqi0OEPROsLjki-xGWE8mIujGPPDcLeGlmOUJvRRwQpLYduJ2myUDlFA6037ya5gwLQ_-Vi81um4tUatizv573GNQlNn7mOOaJcwqL-YGMZlff9AYw1DuAI5WFf7nZY0V0eL2d81hHji-v3RE8rcvCZ-eBZMpuIGoTgpNbzGoXaHiFJWfgGrgifAI9lLv0-2FQLidSPogeEhHB7x1bgRVEr-SHUdi4nm5epIke4i-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک لیست و فیتای آلبوم خلسه که به زودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81937" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6Jddy1NHMnl2aPjGoh5kxbxYwuPjPRrRyufk-ZpGQMjg5K_UCfJtlFOOJ2PADELSjCfS4DOCjOwLiDGv5Otp7lMcV3fJbIJxK7JP3_-s4ban4tQU344pP5Q0zGehb6TJOeT9GQCRjwB3X9n78BzA-hiIMVzU2rnD250neSfcbFX8Tl5vsK5bn_jEPwMIf_0FsNsKi4-jh0cC0U4hqegkIkkMuq5mL--aoIWhv1i1kipVldyF4kf5ccj6uULuSSqs9y7Zl_gK5E6g9zq8d1kIKC_IFtddkUGCE89aNqZe_MiqadgjIdPi3_VdREgS-nBeu2yFlbl7nNTlelU1vLLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها حالتی که ممکنه پرز لحظه اخر رودری رو با ۱۵۰ میلیون یورو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81936" target="_blank">📅 10:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81934" target="_blank">📅 01:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حاجی بارسا چرا این فصل اینطوری شده تو یروز بازیکن میخره تو یروز میده میره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81932" target="_blank">📅 01:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81929">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gL3U7LwsoV5S2w95vyrb_pVldTZEFtPcWQ1_K_voXRFiDDn4_y_VQDJQJpwuXi8Lg52W1Aa7k5CFRYIzN8YvhQ1FjEpNaY7HTqshv0k_qPuP3oKHqFIdng9uNbqqMOMBFAnyfcRja9c1dk-Gnn8i-9WtbbIIWfOsNXOPYC29waQwXjeKeXN6CNDZkyzb17IwcwnDY3o5o6pd4MIPow3uKTV26MfOl1U2ASTN5GydyRjlv7THq4Xp_VtgS5mOCLmDnh_E5qTqU3TSKfLenvcv2kuO0nlGOviN6YSPevSpMvitfnnyZ7suKsKHc08fbsJIKYghHFR1pQfFtzgnnwkWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnX05-D1EzMp6g6b0ZuF0fUTPYdg4mgqmRJxN82-W-cylfUG-GpsMsMaDpN0LnyAXgKXxfQvh6cUItSu6DCwGh08Lx3tdU8Ct76MHwh9jkZtFE6rWk3CvlD7YzZwJvEtZjflzwqsZY9vSlfN4hPCGvwASp1tZgA5iXglkA5g2usObBI7q9YqU3R9UEJsgX3OHyCu3NbW2_VpQK6YiyVQZblGgt5CRxGq-LOAwDMhbASeIpRFDipdIr0lHhkHMCpKTF5H0l9295UGc41WFRNIweL-0FcKEjKQL-VVp2KURnWifs1X3ei3xBD9RfWdYEby95a3PWdxrFjkBJUIt-S_9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رودری هیچ پیجی تو فضای مجازی نداره، حالا فنای بارسا رفتن سرچ کردن رودریگو و رو اولین پیجی که اومده بالا کلیک کردن رفتن تو کامنتاش دارن اومدنش به بارسا رو خوشآمد میگن
حالا پیج کیه؟ اولیویا رودریگو خواننده که پارسال اسپانسر بارسا برای الکلاسیکو بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81929" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81928">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=GZ4spSUlaXlBAyG4dUlZzv0W9CDHB01Yct2DQeZDFXKbceelL0tbyrj4K2D4ETCT4m0a3NYGGsDupeM_DrudBHdH9sOBRdBzxtWb9smcVDpq9qlAz3C09lRsPzvyDPpO-fi-ReM6-Z2h-s7r8EA3z0LUjQB3U2i4PciHW_EKkaj4-siUrFc3i2bb2HDfGFu97doGInA6oVAEnee7VRpIwhWFgH0JRu25iXmAkM9KknL5pH103TxsglOwRpn9AuIlFxpJpQEssvOa9TcUtov4vb2Ew36q2mSf9TNqtn4ZvbdwNZa_n798rlebDxQmxKXaZwbK1OJwSm1qX5AUVbDWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=GZ4spSUlaXlBAyG4dUlZzv0W9CDHB01Yct2DQeZDFXKbceelL0tbyrj4K2D4ETCT4m0a3NYGGsDupeM_DrudBHdH9sOBRdBzxtWb9smcVDpq9qlAz3C09lRsPzvyDPpO-fi-ReM6-Z2h-s7r8EA3z0LUjQB3U2i4PciHW_EKkaj4-siUrFc3i2bb2HDfGFu97doGInA6oVAEnee7VRpIwhWFgH0JRu25iXmAkM9KknL5pH103TxsglOwRpn9AuIlFxpJpQEssvOa9TcUtov4vb2Ew36q2mSf9TNqtn4ZvbdwNZa_n798rlebDxQmxKXaZwbK1OJwSm1qX5AUVbDWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر جور به قضیه نگاه کنی خدایی این یعنی تعویق دیگه.
ترامپ کنفرانس خبری خودش رو لغو کرد و به خبرنگار گفت هر چه زودتر اینجا رو ترک کنید ممنون می‌شم چون ما یه جنگ داریم که باید پیش ببریمش و برا همین باید زودتر از اینجا برم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81928" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81927">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_mYlm86r-XuNgdJvk_OlPraQDKoeFb1oICQSpx_AGm0-zV39i4TtDx6PCOIV7g3xlEGuSzUWypcAyMrO7ZeyYcdFJVI84og8sx9SpEZiwe-T25l74UVp6RzNHh_CQeXmRgAdIR0ePe-4QfQmaWwiUMFXLVqHrbhllKv0mAwtkmWUC-ZbaWXYdHt0SRDrra8rf9e1VcI-mY0BKoiK2bOZMyjrJs2wM9UZ15loHYCduSURFesXVuGDmOR9Vc-JXw65Ea1YSvUVVH08T2rRFdNIpr-UaLGy1_8c12zQTE_D5pzE41zdHW--qk1gFECOGIWNBncjpBnoiFOs6cC8fipjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رندوم ترین عکسی که امشب میتونید ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81927" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81926">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امشب میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81926" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81925">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81925" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81924">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81924" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81923">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81923" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81922">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdWbtde-voOTGYcHQax7Qq5lBEoA4x3nbiDIiMFuAhX_PKfUg3jR-XPPf-57OVe8eHsaiVCDj5p0jPO8n0MhhF18Z2faJyyXe6SK9HASxsL-JH-FmTFtqoTa52MKXlaDz5lTo3fp6J4VQ2SglDh0lKZV8WzeHYCIC6V7LO5OZMAlhYQeVP_ihARNGa0INBwbyubMuD5rcVh8w3eabYEOF0fC1HBpOSWpUu6BDTqYRXvuXhNA8mGwOmciHOMwW2P4l0jmSwYqRI8q_q_L-1Zz93ZhkGKxLv8xnidJLxxKthbAudYL4wlS22W_7pMZiaoQ9gZHII6GdvrDt_gcxNjHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل البوم دکی هم بزودی منتشر میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81922" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81921">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwIKKIiANoB6YdglXEPw68yleoTHwofoVs2CVui7YH7UgciF4kBnp4P8TIXW0UkatXVgVFQO4UBwp0pcVQopAd9ckiw79L8W1uOAviNAWDATCtd4SO1-C0PxDIOjl8tEgtbLB4FcA_zwQ2k9z4nfJFRfp8N3112AOyuD4a6beQTZS6FlTTub2JZHCt68BpNie5YpcZJYoAWQKrKL9uTh86z9cyXca4N5_egoCAEs6HTrt7GJYZUJBWHXYsmvih90NR3jwB_z2iG4zQP51vQCOR5h_Z42eyq86iLbYvfMgSWRxKUdxivey2CwCQObCIVCE0_ZNTaU-UTRLejgc9zfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دکی از نامه ای که مادرش براش فرستاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81921" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81920">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL5wMX5srZ78NnWzgvMCR0G4PyDs-PgNImmUcbedNujLkcRWegzmWZwntV90SglbFwfrGnIYETsPRUahcKm-3z0hImWJ35DPh9i7xaKDGsFcHFM6wTEr2KSojgb34YUIG_kE9dkuTBU0aIsb2bMKm9Jp2B2mpPjUsn4D26NwAbBc4wuuSRYcAPlsfE1ZOhOfVsMFMBF1WnTwNngxKWk_arHkBCaJcBqIehLqimbNZjzF2TGzsXxaJLlGEKqJ2Y6q83AZ0EojFeCLFqh_e2UWM6rFrJ6ULi8RX9OG2eyhU8vNzpC34F6jEhfrKfXJeYnLI7sHgVPNrLCcO_U4M7rHwFEtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL5wMX5srZ78NnWzgvMCR0G4PyDs-PgNImmUcbedNujLkcRWegzmWZwntV90SglbFwfrGnIYETsPRUahcKm-3z0hImWJ35DPh9i7xaKDGsFcHFM6wTEr2KSojgb34YUIG_kE9dkuTBU0aIsb2bMKm9Jp2B2mpPjUsn4D26NwAbBc4wuuSRYcAPlsfE1ZOhOfVsMFMBF1WnTwNngxKWk_arHkBCaJcBqIehLqimbNZjzF2TGzsXxaJLlGEKqJ2Y6q83AZ0EojFeCLFqh_e2UWM6rFrJ6ULi8RX9OG2eyhU8vNzpC34F6jEhfrKfXJeYnLI7sHgVPNrLCcO_U4M7rHwFEtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز جمعه شد
زاکانی، شهردار تهران: تنگه هرمز در صورتی باز میشه که تحریم‌ها لغو و آمریکا غرامت جنگی ما رو پرداخت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81920" target="_blank">📅 21:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSupport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPTmKtsHG8AVGvraPdYinn7el3zCn65sxyQeGg49MoK0M_Ggxjce0Ga9oHPkMJSMPu9iOfWK0bRnQxw1ZKfnzQUW7J8QMwSmEZbHBP-U2VGdw6y-mkglPateu_y4wqIe-SSNSwwD6Ih9LFimpangW9aEmv9j1X3LjVGT4FVVKiq1O36Wjle74SS8ujNe7Pm454vScxnRLYTcsTicGxBQOLAS8Wn3ks1XAUwxpXUQD-CoW94sITnPvG0WDO2cv1ahky_83ggAKEDlqX-PaRGemWmvtp3PEVZD4jx6hcefhEaS6ywqwzmWB87oBG3V4xgahsJwqgL839rCviqHO-mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اول تست کن بعد خرید کن
🏳
50 گیگ مولتی لوکیشن
🌍
کاربر نامحدود یک ماهه 105/000
⭐
⚙️
میتونید وقتی که لینک اشتراکتونو به کسی دادید که راضی نیستید در کسری از ثانیه تغییرش بدین و از دسترس همه به جز خودتون خارج شه
🕓
💬
پشتیبانی ۲۴ساعته
🤖
آیدی ربات خرید:
@SirenNetwork_bot
🏳️
آیدی کانال:
@Siren2rey</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81919" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سوپر جام اسپانیا این فصل بجای عربستان قراره تو ترکیه برگزار بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81918" target="_blank">📅 20:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81917">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6g0mYgl1cgb9cEO_VukWDEGwhog2P68_cnxxoymSqgJ46WFYhGJHnDYbZ4DkOHEwp97J4FoouQ3iLl4Ara7mdbbphIBrsvboAIx0hhuERIu6AVkP-Lx8WwnrUWf0ksGFQuHORIHXUkL55hAo0xv-25dGvfavd1ocWXupq_7b2AVUu2qLKmizVUbqxezxefnupVYD_Yz7kI6rR-W1NQESIPFK-QnI357A2WSnXQLMVxsx3VyZQ1tsWAlsyU5NvqeCsAU70CEz5g8T9fvzYI39VYNedIqjugWya2hoas6LSIuc3LeZ6ke1YHaSn3HUmoK2QKazggRXKrcTkMnrR5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش این چه رفتاریه با نعمت خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81917" target="_blank">📅 20:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=Pimz_cKXlL9O_xHlfoQBJsPolToMPmq0y5lLeuiXe8SiOlzT54PyJCsMouOLd5_teLakwKRFN6vmT-Z3tz5LrwnNXO69qg4-69uLV4Z6lqh7p7NDCefnHFTarTTeKg1W-fFohOKARjEz_SqemDefvvKX45uk6H8_DyiNU618gcx-hv9U1p7z4FZOly3dYPHXVN4Kw27-tQEvQTSjg4YxLXAj9FYdDHrlN8Lhx1YNOJKaSv5CDP2dK578QkwFsYbH0FcaTlZqeEsf3sXQs6KOO6UPJwk8vUeDfQdhu83h1ML0kPDlGrePMmFVRHyIPo9baihjdRZxM_JlkZGO-NIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=Pimz_cKXlL9O_xHlfoQBJsPolToMPmq0y5lLeuiXe8SiOlzT54PyJCsMouOLd5_teLakwKRFN6vmT-Z3tz5LrwnNXO69qg4-69uLV4Z6lqh7p7NDCefnHFTarTTeKg1W-fFohOKARjEz_SqemDefvvKX45uk6H8_DyiNU618gcx-hv9U1p7z4FZOly3dYPHXVN4Kw27-tQEvQTSjg4YxLXAj9FYdDHrlN8Lhx1YNOJKaSv5CDP2dK578QkwFsYbH0FcaTlZqeEsf3sXQs6KOO6UPJwk8vUeDfQdhu83h1ML0kPDlGrePMmFVRHyIPo9baihjdRZxM_JlkZGO-NIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادمهر عقیلی، قطعه‌ی معروفِ گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81916" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMlYyA4nd7YSZmAms2_xHMrWwROY_1n4-12qCLXwg29IAYkPqFZ3mXICqFvMyaDwKPdhrQdMqPOGsNTNPtn3AE1LfPVa9MoDfN8DpdUBzFQ_kOUdp3VB3R5-LNBg4QwksEzKA5AikJJv7GmB3YaSnKuMi6k2oiqjq4Xr4ZoL34frL3yIFU2sxX15ncFuA830xKrmL2ndG2i-QLLFIgINiqthL_gKMgpj29JQlsb2yYspdU2joY5VmYJGnHeKwPNd_gGzNfJMPbpvb7cucnMDV5IqILW6knsQJSNf07uyCDstk-msJ4rz0sA2hvCqTNJQyKP-FeUfKAQBqWNfwyFPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دی ماه تا الان ۹۰۸ نفر اعدام شدن، یعنی هر ۶ ساعت ینفر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81915" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOdEQdQiHdd4G5DiBi-vreHbyGWng6NHTlD1hWCPKcl-ME0NMywSs3_LXF3nK8y1yoCTzMTXl-lo45s0K6qe1ib33xjWCGEiRDi5VSSVRzwExM9NhNly9B7gKA8rG9CIpExZHblKwnpOynMv7jJMovimsa-_eo4xvg36_0KVmYWgTaiahobN1_dFP0WygQ5wlAGL_AMILK7BPuyREs9jbNs_ZguvMAb5LJChHERKYNg42hsxlLEC-t5FGAd0auOGutwOMS-dfRmz9w2PvRi_YIHP9y1i66G_KLxUege2Ab_500WkSM58gLlPJ9jhpviirzYgEq9pgEY13C4DQlIx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g16
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81914" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امروز سالروز درگذشت فریدون فرخزاده
فریدون اوایل مرداد ۷۱ تو خونه‌ش تو بن آلمان به شکل وحشتناکی با چاقو کشته شد و جسدش ۱۶ مرداد پیدا شد.
بعد از ۳۴ سال هنوز پرونده‌ش به نتیجه قطعی نرسیده و هنوزم یکی از جنجالی‌ترین پرونده‌های ترور مخالفان جمهوری اسلامی تو خارج از ایرانه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81913" target="_blank">📅 19:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igINhkTUiAbrOLELe88NmNcNhGV7dFMHkpajoGxX0PCmdmWpD7ndSyV82At6s9YxmWr0aC50SP11mmHo1iIw-mbVlCrWtbDWyQQxftfxFCJOXQjhaPUhJ_5wGARxlRrc5VoMwn8pWM5to8r-GHm6yPGgXdqBD-BJJEvKek0PZh82VLyXX0AQ7zk2Hyxu3EvNbLxQ6SzU3vVTFrm2QR8Joig4mp7qUtSIkMtmPZjejd1ZOwS3oFxhGzb8EFBhvzbqT2eXoGdPUPY1fiKVQkwUXY8wlSoxpNBO4szp58l9BketQ5x4_2iIi7sRH1Y1EJRQw5BuTZGZg8Vlbd-W88yjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH2scaeFtLq0aCgBdWXl60UYwmwNqqIWVU2AklEbdG8QD10jhMM5x5BiunWcWH7a08-YJ6hXwQxl1KpR-C6vZFu54OHwZM5RxDnZY5tvaFOm5Dd6YgSk4jwOquLfUTsuuBhOkIQPgaEj3mJLvvRyjGe8fugjV78HK_-5128fDvP7VIvnBha0XBgpsx9dVI66g7I7YM4f153KpAQkFpISyrMcINXp-CTSd81P3nJ3WC12hhg-c3rGIPfYN8fsn4jNBBO55oVCK67QHXPeu-AKpMtBt1-xbD_vAGhny5W8rnvX8e5S_iF4T6SUyR3O-3F4gaqnahyxB2gNrcKiLo1t4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81910" target="_blank">📅 18:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptnldNaz6V2GR5_ZXQeO5-2_IRvdZNKidexBpKkq02OBUmjdeaqiupd5LePpVeE7IveNNymOISfQy4ye9jQNOx0mee_f7CI1_QADWf9UoAsv8bUSHBxdaibeD5U_EfyqoiHj_Qtm__5-VuY4P5ywaqa07hLF3tYJ3WosNpzpVzLu2eiwlj10f6x7hiAm9-xe5GFDCOO9KkY_U7oOKnLkyuwY3jxf70YTNPlfUlcqUoc-ziGjfTK0Vh802XSzBbdt1V3DXEajNIEgDwjwN3_qDCKFi4S0N1kfZZM0ZaYguxg0LPcZeB4-CI2WK9AGlMc0ezBrfbHzvu8atvSzxTL2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIPG6AqfnfMkalin12AE_kQ20ZC0NJlHSH0x2MnEOFh3GI8e0tNGQBAs2SBcpez9qRZmttmumXvIN6gIS0RigiaqhBY39rUzPtmWDVtcUeJRYttwQGKETqZbbUwuc6-ErRwtJCjITVeq8H6OGWHDQhY3E2tSrGDSXYqQAl3jBi-hPs3Li0WG9GIwzC6uqLz3zKdpspEqyyfJro_8F2a3F2n0U_RudqKgrHN0RrXgzx_aRF9RET1OJhfUAjbXNsmYCovdxbF8mQJ-uMxhneOCUFbnhgtdMLzAUN4jsXFL9dmo2KJC1VjDS_l4UphmYQQZyKfky4naB9BSxO_JFuB-dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/funhiphop/81907" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVKuaAU5E0xnnZg1N3ssaGHuS7wHR6j_QcYhjvQaf4WSak6nVMpRoghrJuFfkiCZGoTS6u2YAPKeXzo0LaIDJVpomGVh7wUbIL_UM90ucFWc809D7Y1Snh-l6Cotx7G01QooutywiMEqH3XUHZlGe4iwgOldS_OkFG-EGaktNuH5wANai7XmP7kyrhuRNEUia3wkH6MxupFRAdZs5ktyYCo2KNHuC8xFnDrSlxpi_jTuNJi8dmrhn_qpAoHvimmnaxME9hrjaDx-iJAE8em8y1M1eEPH6uioMIlAF80TF13X9Uz8_Rr4kgeOsk2OcfHw5GBimh5hW9vP9uvytcX4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبونم لال زبونم لال یسری منابع میگن حال رهبر معظم انقلاب وخیمه و هر لحظه ممکنه فوت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81906" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrQ0CXmC1MW-R0cZb-6m6C-Oww1cKCjwCyCH-Xpt_cpZDfuJ4seCOq-53nJX_n0wSW5JK_GNssvltsSzm4UcvcojXHdesAFcljUwhg4q9MTpmpj3_q1ep5RTnUvWXDlmzsmpjrgDgXCeJVb0e3wnWyKV0g-lFaKbPh6LPbGWitQov3q3kfV6TyxliwrjW2LFRXz9U7G-BDulGZoftbIuq51XHD6NahE_C2_5iM757MjbG_kqQd_UUgS6Q2MMAj9wY0fOHqNtELWeOae-1v36uLZ2M1dNTjhZkI1D--71ftOXQaOE6_edwTDr46wyXZ0Zn-A9aJ6VItoy7fkCL1ve7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیارش خونه ما عزیزم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81905" target="_blank">📅 16:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">همه این خبرا برای اینه که ویناک طلبش از دکی رو یادش بره، لطفا چنین اخباری را نشر ندهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81904" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عربستان، ترکیه و پاکستان یه توافقنامه دفاعی امضا کردن که هرکی به یکیشون حمله کنه، اون دو کشور دیگه باید برای حمایت از متحدشون به جنگ علیه کشور مهاجم بپیوندن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81903" target="_blank">📅 14:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqeZ-QsT3ZcsqAm5ci2M8Qo4X2OctL9Nnm0BiF85vGt2zLpKyLP-x0qK8IjdoTat9Alf8Vr4ScO1QI7_0tbv3JdkjhiR_qA3IX689KaN5LDDBBxdIUslL2Hzz6Unn_8Kq3ZgBLpTQRV8qc1viRewGVVBDx84UwbrPTmgBzdL3d3uhD3j1sbxLSMZirTUs75GdWBgaC9oHopercigGzw9W1tN7IKpDmbuYUC1HXdbp1mivot4P7lM2WCpsuO4JH5e_CX6O-7XDD5Ov-JAZS7dWJJ7IzdoWkrfGE6z7BqQFGqEiPEtDotB3L4RFVdlev9jxW7rrxTWT5xl7y6dOukX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من از خوندن اخبار خسته شدم اگه بخوان بزنن روز میشه همه میفهمیم دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81902" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgHv3g7mlEcZW_wfI2y08cfoemW0sb0MKolxt_4bI1mRp5NWBCDrypQosEAlOWn2i2x40v7Hf-VDQr9k8w9qSHiLNhP_84bcQ8y_Mb3JLM6BJy2i8s1YtYRwicyv5FHxVga4fo_uUIqiJsOlJ_47X72iGFrcsPH1qmer8i8KGetjnTDYfn334kYCVLo70OyC0v9ju9R82UMOimjA9qmgOsgvfrSzVKY7PjApVq3bSFWknl1rLH5qZzOyzW8a09TynvYsv4SerZn041ychQD6IMpAVHgFgFMw2Gzfxh2nca4RWsPIJiIroBIpe-6bGZW4bVwtMM7ZqMGyQuAHypfQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81901" target="_blank">📅 12:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCUTK-BlNYxYDhdKF-x5fVD3gZhwtZoWjpzxbvsmDjlcCgMCyC9b_sXxoom3t1JWU_qrkCr7uZszdOcCo_LMkgoWSWzEBhqsKAdsSSz3pmTCDq48lcKMnF0tn_vvFNmddwh2bPWC3hhpfV5L-KL7NGXz2jwZD5pYduN0LpsXySrmZA_g-OLSpXEKLSDqTTA4j7y_OX11myAokQLXhen3QKaJTPuAPdlK5XBAtKluOuB-Ns-xhizxIUMqobc724cMUtbTr1d4AG7onstMWs8hWgVxB4Nnc6-y6bJzqOTetTRBvwSNnhUtn7W35-kv-NoToeKwL2B_pkaYYCz0yfyfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81900" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXpcoPyga0ewRzl3ZnHlV_iPc7XcFBguWtXx6hBxgxf9liFISUL66M5D417IweU_ep5I4tvh-DLFjiKyBlWmcUMn7PnehGIb5XYwpS2OKz7azAlSj0BsSdhd0NHIheS8rIUyS6RUGNYFsdr5qiQar2XQPqiFsdHEzYsjLOBm4hQgZp7FP0F3n03TLQpGXcqe7OS60lnA5qj5KFZ0TOt-yXR99Y8P0ydtVyOuKiDL4-jiv5MIUgzP1f4-Op_szElPPta9ticksfVyT6mS433AWywfQzq43jyZD66aEJdNxtUY2XAYeUH6EMdWXlIFS0MutBOQz-eV0UJTkjibmrDlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r16
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81899" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">متاسفانه ویلسون یه تماس تلفنی با پیشرو داشته و اینم نتیجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81898" target="_blank">📅 11:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هر بار حرفای ترامپو میخونم دژاوو میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81897" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIE9osizuU38Dh2B-xeK5gsc-F7IWKXzSE0-SMlRHXiO2AlcH8UCa63rvvDVMME0i2UfTMXGsbsvVyOpH81CyN5bxlN7oFbhbEp4KX5HfZADdm0cC_EzAGnhBE65eBOuyBo9V2nrXyYo_nsA3fHZeTAWkQVN1drP1Ej2HuLgzZjttRfQHSxy4Umf_hEqJxQkMNGpbw1FGGzhQFTi5ArssZcTggoVtEb_uPkpG8Rb8mSeXgYcqPgeBdKgoK_xXWCoYfKKJvsOQ-yUyzYlreQR88YKDCVC3XI4rziNLFqHoYADiLKReISrHwOVO7ZfNIKjmBnTQTsQ-doioLpxSPCVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.  @FunHipHop | artin</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81896" target="_blank">📅 10:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkSNRArMuhuDNPwGdXS3alteS0pMZhxBkHu87Zh-xX4ASCLZqHkw03pgdXG_QlzAD2qo_LCtg9Ovy1OiQLZJUtIfQlFyGSPov0w6h7Q1PYBQgaVYtpSdJxZr3PMQjygf0bCNvMR2_H8v-YNVE5LrXspuIQgTB2SPG_guspNDy9nFxLiMO-HF8z_jGgNEdsDSIcQJXoz7pGodMshoPDtcGr9OmHkNufQ5cX3pQDXaKV-FHFCTq0x3Z1hAJumzsS_KyMhgQLxwLcEpcZbcUaIV7i5iPni7Y6h-wgJFFECh-RarKrmBCxPHtHoDwMdopGJCfqAbaAA_EZsPN3Z2Wmr-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد 26 ساله که با لباس عزرائیل از پشت‌بوم بیمارستان به بیمارها زل می‌زد، توسط پلیس گونی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81895" target="_blank">📅 02:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری از رومانو:
بارسا و رودری به توافق رسیدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81894" target="_blank">📅 02:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81893">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB009LeyXh_dMVy325wrLcRwNSuSpl_Vc707NoS_Z-G-g0SO2JQDbCZfJql_FP2UQQmhpmw2MTQxvt8_BSDPJtWY3se-MAH9cOT3k7UuAStaDhh4TxQpgFRGvomJOahYPVH4F4bq-65axvjz3chiwbBk5rKxrV4O52YCXEqJs7UyUpMEOuHURniK2z6pQD9GkO-t9_kV7MCZ7I_IavPBgqhyKL5_ysUNtPrylsNPeMYlANZLO_wdwAIi_4qC2MkXIe9VqSaxrgEKGU6-RmyFAFyzo06u1u4sMiisaPkDWGSgtz2vq91yRWt5S2SZxA2L-tRl6ety4FevWPpR-l3QSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موفق شو دیگه بیناموس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81893" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81892">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diNHosxXEZj-grwW2PdI4XzKoQiV4hc5DWV4AhRTDvy2MJJhCiWZMlmo-gIaTPaJ8lLpRuRMml2Q6FatHInI2SCDzFXI3Lp3tvSbxH3fkAnV_OOcg8spTjyrnmLbRf7DSAwZw6vDdpYVBhFYc9gX0xOO_1obN_0Hfy4r0VKAda772drk9yv1ZJcoCTO3eCt7GhOeKbpafQUKvGgZmlYDEudS4aMLoYsm1zfWbjFwcZ7KeeewjOMB8OjDQChWv_kfsPtZa6i39eC0TD4haPKHtEs001tti8gh08M9Gg3XOUoDIoZ5HqOHlqkjVAj9R4GDNMgXJJw98B7RzZpMvGWCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده نفرین نکن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81892" target="_blank">📅 01:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81891">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وینیسیوس تا 2032 با رئال تمدید کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81891" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81890">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم دکی بدهی محمودو صاف کرده دیگه صداش در نمیاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81890" target="_blank">📅 00:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNq_PwbQAFWvvXDf6uxfKwUIjwMpW6w4rhiqJ9sdfdGY9mKhG1m4_5kQBIg-DjZR7khQ-DvRPPasqO3N5cLKJQfGz4V1FMvuFOozy5qgk0l1atzEZ_Vn9E1eO57T52acfXsgD8YRGzgYN2qcIc8VvJr1i0sE4-6z5ayZaaqv58pq_klTQVEv1YjfZ9qknBswAcmEHuqQoIRBgErqO4B7PaE0hoSJLB7laaFLk1CVTfzbZwLAR6oatvsbRkBA5GypnK5bju-mry9x8nURvmCMJd0GE49D7NHzrStCaV_P7jxvK06PQHP2S5geVcZ1dYOmfW-QpjhNrimvmWbAZWJebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjz-4pWvQ_ptnNXij4uHrxY3WFB9V4aZkIpA9FUk7g4TLetGHM33E9bakO9LIuTPvXdNiJznISvItgJL4hxEl0RiyRsiRfjSEUOwV-HvF5lDdWBP6ItyR3i6WFODcbXBfrh0A9JmQxDjKSveyuXNaNoR5_8pfVE8sNY_jBaIp-SAwoL_zPRxx1sKywfhcF5yTxq9UF2YziNkQJ2NEg3F5RRNay3alDHFCVcpwisQZlB3xpKfFRBFXlYJUOna3i7lT9eMruC7EnOo0dzF11NyZBlMlPRg06MWSLZs_r7bhHQciVfrVOKeLvgfnROrmrmd43O2r3ppk8Hf4w_2iEsbqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=XnL0fCV3YCwTqH9DO6FbadN9FKq2vfeStzzFcqTIoguVVUsN2K0eqrUY7_JplZC6zvCQGbYwzIwKqY5gI76-IwD9pYPQPCrjAYECe9KkT1Kp01aV-OVcAooXGAB2-qfTNfowcJUtrdA4RTbIc74_YSUMcauHSAA8GKv29Bhl7GXu6VT41ImMx29oPWS97VdK2WmVxVP1vwYVEpuOSuTzGcx_BmZWysESWwMg9B8Puv4D53Np9XaEXb5cJpgNROBtsXjnFdsuFk5ymrQmj9AIcfIIHOTuJuNdHuu7mQ4NroAtwQaR0dqf1mH4teLBbi7eSechcISqpN6awr4WoeDwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=XnL0fCV3YCwTqH9DO6FbadN9FKq2vfeStzzFcqTIoguVVUsN2K0eqrUY7_JplZC6zvCQGbYwzIwKqY5gI76-IwD9pYPQPCrjAYECe9KkT1Kp01aV-OVcAooXGAB2-qfTNfowcJUtrdA4RTbIc74_YSUMcauHSAA8GKv29Bhl7GXu6VT41ImMx29oPWS97VdK2WmVxVP1vwYVEpuOSuTzGcx_BmZWysESWwMg9B8Puv4D53Np9XaEXb5cJpgNROBtsXjnFdsuFk5ymrQmj9AIcfIIHOTuJuNdHuu7mQ4NroAtwQaR0dqf1mH4teLBbi7eSechcISqpN6awr4WoeDwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81886" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YC54SCOfFUTZd5Ig80H_0szdI0E48HFUr56sUceamY4AxbmmQ5TcvVsqG_LFHMZssSP-9OnHwQ3IrdBsZshR2ss822ygeLufOhwvnL_lKZwYoEwlGO2J6Rn4W1ssx_5UojolFBJ3Rf_eSG0tRjoTKGAbf6wvlQyFLnfhJC4nCWqbNlnAnSF9j8TS9EHiemcG-jvvXJI1SOV_VU1PwiCh3K0xYnT6XRcaNZFXgVDXqw4Su9c-NJj4aPbazGcATdgBMo-VmIhuWSZRuBI_QZg8Y9Q_RE9wx0bzHqUJA25_JJGVR3G3aqOZ4JhWLDFG9ns1k3_EXyJw0LyDq75MdeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.  ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81885" target="_blank">📅 21:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfEsZOW73_q4Qk7wLerlkWD6KyvYQTMMYjwOJe-5qJK4iQviJxtHEQzxlCfUyEDWjPcWbjcwtQzEQwvDtafk_A7Xe2S5AwcA8Cq4f53VW6r7dr-nI3vrrDh3J4wuoMVyCUYucS-uTlzpA-xfW2RHx31147A5CrJhpa7uhZBt-O1K3yD9aoRauKuYYb-w3CZMEMatRCmZS6Yud4s8pUr2qeungPXkgrMhb7zm-v3xn6G7pJIhYMr27pS6a8_Qgq64yZS4H5YKjwWPIln3eHqKhYqdu4szxbxA6p90tWQYyL1pvy09rBuOinBR2f7SLadhqAeiHIy7tt1IBRqBtV2MDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت کردن رو از کاظم تو انتخاب هم تیمی یاد بگیرید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81884" target="_blank">📅 21:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81883">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81883" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hs6VhXn_mCHiXJpM7bqxEiAG3Z0lfWcuXmzyZ_y_0CQPq1cqip-ScfoxCVMCxqrYQB5heWQkKfLBrjsMnr34xeaChLMV5x-rzW52qTBrahP1fi-u2sIuRMk9GH6fMPz3e1a3QmsCQdrJ_g70cMqGpRj6MJSAyVJ-nWpq2ndnUXJRX_d_ovwAxCJna-4yqnCjB1sIkYkdXdblgRPCIeA-dSgd46PP8CmmekCFrQT8FEuecls5hbNqTLL5HbOxhdoZGrprWA6-RsdMMo7tEZKiNREtSDr27Pn0lZUvH1E6VrwnRShkFLyOciJIVpz2pHp06nNdTJJcVqrD-kOt5b768g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81882" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81881">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=bZM94YFXeqdubRj_GB5tITLtDGmk2EnNmE-t7FE3xHfi8Y-yhIcFxjI52iuY4A5ZGMwKtSpYxnzro76qimFLEYzBqC_1nh9MIDbnLCuPBKlJndRUb7SKGJkLqDQ6U3H_yBPO9UA6BpBRr35YVVUv4bYw8fF8GRtLNS7InF2d7kAyxTQXcvWG5zF0POnHFMXc9tVQqy2fQf4WN9hkEEmGyFsR2wy9n07qKxoZRtkEHfVSb8hpZDiZOM0kdlCP9Z4iDI-IANr5SqT-wPgTEMDyDhdvK5odt7yH1RcDzfQWg7fGHu3NRThrx8BF4vsd3nE1Uj0rMOe31XaqelmMRK6mAXubIvtUr3ieTHOddTBBaf6veFk62AFzx2eW8s9VtOzMBt5I3MnDnvvQe9uOoAgKe4jVtBWYDG4sHmRGG9hdq0nQMYQ2au9KxB-18P3Ii1zMnHT8duXMXD8CjqocGwBWT0URcNsBFM8XqsA8YwTdQXVkKcUc9ens0U-95hu99PjgzcnNAjH-rzjl228yuDTvYmxtZSvYHqD8SXM8DFaTbnDKMKY_-zeVo9hH5pjF8cVHr5KDMxtDJMYwDZCTy0BTcXbjK88azNb53rhQTxvYa5MB3d3u377C_5JxY1Hd7W8hko-0jpK3_voNR9DgpGloqbRQpNVw5wSgI6AA_d8-qdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=bZM94YFXeqdubRj_GB5tITLtDGmk2EnNmE-t7FE3xHfi8Y-yhIcFxjI52iuY4A5ZGMwKtSpYxnzro76qimFLEYzBqC_1nh9MIDbnLCuPBKlJndRUb7SKGJkLqDQ6U3H_yBPO9UA6BpBRr35YVVUv4bYw8fF8GRtLNS7InF2d7kAyxTQXcvWG5zF0POnHFMXc9tVQqy2fQf4WN9hkEEmGyFsR2wy9n07qKxoZRtkEHfVSb8hpZDiZOM0kdlCP9Z4iDI-IANr5SqT-wPgTEMDyDhdvK5odt7yH1RcDzfQWg7fGHu3NRThrx8BF4vsd3nE1Uj0rMOe31XaqelmMRK6mAXubIvtUr3ieTHOddTBBaf6veFk62AFzx2eW8s9VtOzMBt5I3MnDnvvQe9uOoAgKe4jVtBWYDG4sHmRGG9hdq0nQMYQ2au9KxB-18P3Ii1zMnHT8duXMXD8CjqocGwBWT0URcNsBFM8XqsA8YwTdQXVkKcUc9ens0U-95hu99PjgzcnNAjH-rzjl228yuDTvYmxtZSvYHqD8SXM8DFaTbnDKMKY_-zeVo9hH5pjF8cVHr5KDMxtDJMYwDZCTy0BTcXbjK88azNb53rhQTxvYa5MB3d3u377C_5JxY1Hd7W8hko-0jpK3_voNR9DgpGloqbRQpNVw5wSgI6AA_d8-qdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط بیگ شگی میتونه وسط تکست های عاشقانه به کسی که براش عاشقانه نوشته دیس بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81881" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJSMUS-FK2sWUEaOJoHBJ3k3zdvjIm8Ek4ARUUZ-pdU7Y7yG7sxqL-tTU4S9n1D1UX7G6dw3irv2w8qJcyddHeAgmMPcFDVK4Ffh-QU1ttVWU22_Bn5ajN39FkAmQ4TKPRPvTjJMDQaOOis0swhrvnObMWsSqFy1hXBDRFYz6bfips_GwakGeX2t1JjjJt2sWw79vtfRbFS0YkA_Szv16FI9hP1E5kUep6HmnKiKfqAca3rHGeU0k_LXWwGV_IYvCV8uU8V1XJ_0ZewLTsD7mmNbJExbKLWN_WM4PDbh5RhpNDxTzLNhZLN4Lo-VDG4LakA-g9tuFbbgoNgeOxZJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنریا تارگریان هم همینو میگفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81880" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHzIZgXWA0AkTFrsKX4YZU41eylbTlYmtKmY1_z8u4euDxWYRIuBVYnaOZ6wnW_bdHuZBv82mw8Lb24VZT0kpQey_zT8NUDVVTzjYY1X1Y7ZACd7EYeKQ9QLSLgTFB-__BWanHTuB2srYZUd5men4ac9amA9xKsq4_HsYrsNVq97c_kZB_ychLHGo53mqfC6hbRl_qJijpgYENm0n50AKv5hoU-0Og7Ixeq7lSCsGGYqO6kkxoLPA2ekoYZ5oJ6vj_lEmq5LxybrfJeVU8KiCuaYyQl96TbZmuOYEEMPkGGV4paA2AQxNadNnZRWPErWA5ItSXIuecu2_8YLlrLMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g15
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81879" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل مثل همیشه داره جنوب لبنان رو میزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81878" target="_blank">📅 18:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بارسا هنوز ۱۰ میلیون یورو به سیتی بدهکاره از ۲۰۲۳ که فران تورس رو خریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81877" target="_blank">📅 18:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhwo8td2vq0cEjZNLMiDWO5ISsoVqkdkyUe10P0UiJjl5G6vDs-Fs893jVEaJmA1T3psFaxgAI2v2IR-dS3yGVz15heYZyjQDzIUlDjc1-qcsvCziSlRRf_rLe9YWapESAH2TfynxNKuRruW1gYILzjrlYc5CZMPHr-XRp_Q5ZmFOGvpy8oq933NeWxMhJ5GNGjrC14U0RBqxkNABaFeAQZNP6DSUeeomZqyZjS_M8Feu4IiGvyJfcQNH6v_PmgN2JXpsBiYVBaVt7tp7ROHMSPNN9IGoX5TZpdUHONe235TS4gsgr_N4G0o8PmY02l6FPqC4YFloUcT2DvKhFraPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس بچگی دیامونده،
بازیکنی که با رفتن به رئال به تیم دوران کودکی خودش خیانت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81876" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یوهان کرایوف میگه
اگه کسی برای انتخاب کردن رئال مردد بود بهتره که نیاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81874" target="_blank">📅 17:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
چیزی نیست اسپویل از گزارش بازی الکلاسیکو این فصله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81873" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ماجرای فروش دریای خزر به روسیه چیه؟
دریای خزر در ابتدا در اختیار شوروی و ایران بوده است
پس از فروپاشی شوروی این دریا با ۵ کشور (ایران، روسیه، آذربایجان، قزاقستان و ترکمنستان) مرز آبی پیدا کرد که ایران اعلام کرد هر کشور ۲۰ درصد از آن را در اختیار داشته باشد اما ۴ کشور دیگر قبول نکردند و درخواست داشتند هر کشور به اندازه مرز آبی خود از خزر بهره ببرند که در این صورت سهم ایران ۱۱ الی ۱۳ درصد می‌شد
ایران هیچوقت این تقسیم را به رسمیت نشناخت ولیکن نتوانست بیشتر از همان ۱۳ درصد به خزر تسلط پیدا کند، حال شایعاتی منتشر می‌شد که مسئولین ایرانی ۱۳ درصد را پذیرفته اند و در مجلس قصد دارند آن را به صورت رسمی تصویب کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81872" target="_blank">📅 17:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA87sgsK5BI5YnHjcDZlApZ3MZys9G3-p_6coSLJaZmY5R-ShbQ4W-QvlFJOqdeRhAXUJZNQh_s1AT4lABGA_yDNRkl4JgvaWt6nkTnBmW7po8BjH12BMPOLRfEVvJrcOSRiHoR7nMII1LoOlok8_LAJ6G7tX_NE7kuyjxogAXbLHj4GoTmkhYm8Thhc-0beYYr_MxNqX1Pi-ZuSjkUTN5e5XU8W2UcxeMRkJQccsGqGeerUXBoX8iRc2rHfHLaA_x9xwvE5f8jKjM5NLu_q-gGXFDDWoVZx1rnugrMhLQ5dUhxV197B_6mEUa16Hg_3kv6xNwdaBV0sNWh6Ld0D9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان پیوند کلیه در افغانستان رو ممنوع اعلام کرده
گفته چون از یه بدن دیگه یچیزی میزارن تو یه بدن دیگه مثل رابطه جنسیه پس حرامه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81870" target="_blank">📅 17:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آمریکا ساخت یه ناو جنگی کلاس ترامپ رو شروع کرده که ارزش تقریبی‌اش قراره ۲۴ تا ۳۰میلیارد دلار باشه و هزینه کلی توسعه این پروژه ۲۷۵میلیارد دلاره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81869" target="_blank">📅 16:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بارسا نوک و دفاع لازم داره بعد لاشورتا رودری میگیره</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81868" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سیتی گفته رودری رو به بارسا ۶۰ میلیون هم میده ولی به رئال زیر ۸۰ تا نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81867" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81866" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81865" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiCyTYftpXepEMjwwVver1bDZ9PcyOZyDameq7ti3vyz154fIkkhC4EpW0ssZtnRmG96GwdMjxEENCasOzHKQduVWn3CdQUPKQ3MhYmHbvGAndJKqcBeBvE4MsnC2UoveboJNdwNZWV6Ye4ILkyl3TmxYNtsVEXSJpBhItmqJIZp0Ms3ZmsVhX98fcIqGF1fyFUlWBi52DX-rJE7yemFit_epnondZ3SjEPlm-6eUQDVpmuuyK7tPgTlY2ahwybBX-V_4CnJfHQYOb24GgidDDsTKsHMNu4fI90RAKc94Zl9cdNoiCBclGWqyRcQHhhdaEEbC5S2eeL1-uReW5VNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای رکورد ری اکشن توت فرنگیو بزنید حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81864" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erPUSy6tRMoJq0lbcjhzye6aohjOzSdk6JCuPyxlIHYCx9SqxeU_48PXKd5beohu5Gze4eG4nosik5Hsu0XSlpalFWZobDkpbX8TKZeULteeIcdBPnBUiOyVvkoyXEjq_H79aWHeA1QvTqhsbs24UegRQCMaHrzaRmS9MffboNCkd3fSodn_2sbRxhmpRKIfVuG2gvzd_XS6MniWnabHH6i5i46wAAZwqn9AYSLW7f3bSucM2cgBNEFl_rsNyaVeo5NSniwefpFowKpPvCjNV5Q3A5Z8l9RA-U6xf-y1bhAKjBWpmQlE9ZGtVHPUKbiQsuV6ugQoTeGHKWGzc7wDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری آهنگسازا هستن که بیت هاشونو تو یسری برنامه ها میزارن برای فروش و نامحدود انسان هم میتونن با پرداخت یه مبلغی از بیته استفاده کنن و روش بخونن، اینام همین حرکتو زدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81862" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ما خودمون میخوایم از ایران فرار کنیم اونوقت اسپید گفته اوضاع خاورمیانه آروم بشه میخواد بیاد ایران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81861" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یکی اون وسط گیر داده بود به یکیشون میگفت نه این هندی نیست ایرانیه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81860" target="_blank">📅 15:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHscQ7cjCjXlAv8NWI67ihK0-fqKBp29IdXj5eRZakx3glgTpU7iYim3RM7XNhlFwhYfzYT6cWOaQkGTN2c1giperkYsrcTb1NTj2cjo295hwprXDmwRMpArnhFRNCmRvYhuHLu5dxZHG5GUCtYFc3d8eY7qe0ZUpmGvFC_qxtmQrIe41YeVbBATE-nNXx6JO40UTVYXgbn6_b8e7BGQOcS_3vhU7lhv5NzKLjAUCw_hABpGv5drhAqstc5oQvll_rhYAbaZEvjzoJXQd6FwP3SPWKR-_36cpp3xXot-2s0Jn0lDQajEmlGpfkhch0AOwx3zUXL8aWgjfwAgMEnaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.
ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81855" target="_blank">📅 14:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiwFFwlJHhrl600WWDmk06TiysFhiY4jZEOFZF_Y43rbbbGz5sRA7B1nMM0l7bWlu_kxgx9BXk2LNhLbeuTphyISSVTpibPAaIVuk1Q4cL6AuElD7bYy4Q3C7Agthp942svthG8hvpyXneIp5OwF72x_lfnxCThTZCesDLfYyH0Ba4ZM2ySvMOBucmocxO3vgLkyKalU4DoYTT65odG0MI5JezxUtfKx6NzzWhksAPawkOZKR8CNf-QFK1xVBOsK4Ul-psM3dRBtPjkXVVd2iatdj02DDBjs97dAPbtOq86HAb8w4o4JSGA30etfklj1cJ7BNmHvWP16dJinosk9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین چه خپلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81854" target="_blank">📅 13:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ساعتی پیش یمن یه نفتکش سعودی رو با کیر یکی کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81853" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsuehhPSlv6N0FApOKroIOJNfvZ9JtcVBAPOKrTs6NtqTDXcbxVNuDcXhUAtuRQIlW5-4KS9QQkXO0eJdg-3qsrGtZ_s8ALGV05QkVpCfzUppGh1cKdFuGF-DWBbsCRJOWJafe7Xqk4r2-XUfFAI9vave2CcXpXtf3-fnAvvKb3kEVkBJSO00NWeAz5CxQIawI_bMj1bWvBDvWCo1GjfLWayO-77DwYj9hX-VY-u2zjyQ93fH9YexekNLSuVBBWw6dV2wXvWXZ4G73DSmhIsNp4j5MKKFaz5Djj9fcUx4sdDXrsnjMYbK6wwlShpUYak42Q2omlOr2AomwEVLjgKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا به نام I dont Give a Fu*k(IDGAF) منتشر شد
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81852" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هفت خط لوله نفتی در کشورای اطراف ایران در حال توسعه است که بزرگترین سرمایه گذاراش آمریکا و چین هستن، این خطوط جایگزین اصلی آبراهه هایی مثل تنگه هرمزن که ایران فکر میکنه آمریکا رو باهاش درگیر کرده
پرتقال فروشو که پیدا کردید، بگردید دنبال چوب جادویی ببینید واقعا رفته تو کون کی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81851" target="_blank">📅 11:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگه حوصلتون سر رفته بیاید کصشرای ویلسون راجع به شاهین نجفیو گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81850" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187d19388c.mp4?token=SX2d_x11CUqs1UcjcD5RSbgT5Ufn6se5QznCm9_xW9BYo8Km1ID-AAkbnEirfSKYIKS4XvGwD43_2om8K0WFg0vr0f_7kNNQ2PXP04mVPu0Te0ZPbqmySeWFV0FJRKeZ-rshOQyiylVO4Bv6Y7lpS0h7FknpD0JnrcOjn7eujclYSMdos1B9H_q4p0fC6KsmC86iSobDZHDuQr_gDgGwyVBjKz5mixzToVbuuXuOkRbr4r57SNYwC_HjMXDX7zyVlTr1suoowIN9KZaMW8L51HarG1kEv2YR0dDN8wqH2NZhJbFQ1QznhoyWyDyZxdWXgV0mq8hg6SqfhnHfbZALdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187d19388c.mp4?token=SX2d_x11CUqs1UcjcD5RSbgT5Ufn6se5QznCm9_xW9BYo8Km1ID-AAkbnEirfSKYIKS4XvGwD43_2om8K0WFg0vr0f_7kNNQ2PXP04mVPu0Te0ZPbqmySeWFV0FJRKeZ-rshOQyiylVO4Bv6Y7lpS0h7FknpD0JnrcOjn7eujclYSMdos1B9H_q4p0fC6KsmC86iSobDZHDuQr_gDgGwyVBjKz5mixzToVbuuXuOkRbr4r57SNYwC_HjMXDX7zyVlTr1suoowIN9KZaMW8L51HarG1kEv2YR0dDN8wqH2NZhJbFQ1QznhoyWyDyZxdWXgV0mq8hg6SqfhnHfbZALdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چقدر میتونه این ویدیو براتون خنده دار باشه ولی من باهاش فرشو گاز گرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81849" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv8P4Bp497rV9ZdAP6bADOnplf1BJWEJcSQkwx1NAD1BCfnWpxbrn3lKFJGaIesnmR7XkIUSX1_D12MtvW5TbxOlDrchvGpheT1lGrHftiAlLQAj3ZWShQWM1ezRDOaP-KANpO_6slKjDBL8tiZQUlOvJLa34BaBQtDK0bCHyBZs6fwv9xYQ7Au8wDthLy6cIfZZF4PpWcpRcqC0bdeZf6r5iqx9J7oE0ObYzoHNfgR7HyN8f3EU_0-pif5J9HXPkrR4xZ5jCMbCrzwY-16KLqCasH_m4fihLD2d1-tMxEdx_VJAEgKBQpjYlsF1jzZPWR9jKCJkX7gJsM5BH9TeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81848" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جی.دی ونس:
در حکومت ایران افرادی هستند که می‌خواهند جنگ را پایان دهند و تندروهایی هم هستند که خواهان ادامه آن می‌باشند.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81847" target="_blank">📅 11:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK3g4Wwm0E3C9gkRZXGmETFKbC7O0cROXpUFJlk1qcoN2ISeCJ1mU4EYhKDjoFFfUCDULEDsCEDwd_oho4yYWRTSoKNDVpggmnvLgS7CFQKyABhd4cn2u92u7wQZLLTf7xmsrEYQNvJmprY2EgvmoPIaquXAEQ_ix4eQjMnOveXK3NP6FnSCRDqI0SsGnQzQgPnwJD3m8OwKBuZuJPJWQLAKpvS0fHy0OJjPrOL3qFpxUv5FdKOBGGg2wgEbDZd_AqC4zDgyCNxrMLZ1VvhVOJ5zhZqFqBL8uLNOEbXBC_Vzb02unj9n4ssoXtmGhlNhnHwzFol2Osl-H8sdZHJvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81846" target="_blank">📅 11:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBVdFDt4Q3V68g4UPBmmhEy4G-HaWe1bLXJ6l8rHyE4YKIgBc_-qYYZHtKsZy-f11EW70J9aJHREzGdU0BG-nNTBMlMc5DqUTgLbjb3TiIj6bKyLWIekSFb7L7IX2PurVDggf5cXRZ_Me0A9p0je6C0cXzHgfzGCATE1rpVkfSAaaqO_gHdvwl7dTYqrqBz_E2bOxfuFjjChXrF-LZnoc805MBnZMZCSbyY7LeWHKKLQQgraZy-lroEgM0VqB1s2D1kxOBCKRCgC8s0p8uWv9d5ubjnBwgxRgSRhplAMsC7i1RdT3N4PuEMfOK5ZtGNBNrOTkwWFdiz6pDcgI3lKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81844" target="_blank">📅 08:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81843" target="_blank">📅 02:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حصین درحال فحاشی به فدایی و مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81842" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp9KfgYnOxWVHSedNW7JjLWSJYdd6vb17mUBTJFcf_5pE5CBc5eJsQpC3mIwOAQkdk5l3AGDrB7IZEmN-1KwCHinI0VZBPG3RSje4xABhF9C4gNM25739HDEUiNoIyfld7w1SNVK5HLlN65RUl9EfTNXs2ykBmE6agP_3dz18PDKcCVLsZbg5nzSMj91Ei1HcJDl4mCg9ZoVJpX_TttPKN8LhQbwKdkY9QR2GICz9tr_5LyFuZ4scTAU_CDNZ2vqRcvZ16niC-syt_9BgVTYjvdI3qefzcmfe5SXd19-wYONe8Gr4-z97fNTLqwcnVdimBM8hiYlHaIoBx5gNnFYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپدیت جدید اینستاگرام که میتونید ببینید کی انفالتون کرده، هم دیگه رو تو چه تاریخی فالو کردید و حتی چه پست هایی از هم رو لایک کردید و چه کامنتی برای هم گذاشتید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81841" target="_blank">📅 01:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbcDU57-6dvwl4IPamLr_1JMF5A08oN1iwwofAKBuO2nYvARcQZ1kPrpYwdI3tGpc0wm1C13RP6BcKIv-GPu32lq14uceMw4HmoXH8bcZeqLRUcDdlgTar-nbPZW7dDmpUT2jiiP9b4MkGAm2SULP3jGUp3OW81aff6rE8yRhS258SAgr5Ie0G2DbkYGOtHfThP0Nz-PGlczc05HkOo3GQdW-CfSMoOUzi0LYeFmYauacHw05RO5byUQH8smfvI-tEmMNAEykU5kWgykQ_0OirR_QltBWklJlwqKAvTogL-QGRRnTiMtSIOHw8MDOdmWhZkd9mQZZhRwBvwFlWmN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
ادمینِ اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی من رو معمولا می‌تونی تو خونه مامانت پیدا کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81840" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سهام شله با کون خورد زمین
ارسنال 3 تا از بتیس خورده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81839" target="_blank">📅 23:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNkVBTBgr418N37eNiTDt-jNUYYwvsDrrS1bOydRoC-htJ8ivd6a63BhxAybJ8Pn1lB-AIpOPhoMvRqWNeBYubuuHSFxTlZ70iGAW4DLYblFGa_trugeX1HihwggQlszDkbhPddCGjWGzFqvL_-dVWxOsSTTeQfLFoY4_62_LJ4XMyyY5JXqm379m90jE4ascXoZCTzw_Q-tk-9Ee0PvIHf2LU8X4v-kJbAyBMshTs8ztU6BYQ-VlDPht7AEqN4BTFr52gM79wyjWy2fVsL8F5JZHLS-PEhgsoYDzL0zVj5eF-bE_-MbSkHrX-J-Z_p8Zy3i_jjiYnVFmTef_0wSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81838" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81837" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT2rjctHDikRqfTKhpNL5I64Yv4GHow0dgfHddYBtOZDkCv-litC3bGFABAr4rEbQgSZ-Qjra55IE9fMvincyTw3_iXcTKThJ8Pa5W2-oBgomOSsyJWXO3-J-1APt9kKfZMH8vdPVKUTkrUk0frZrJhbt3mnyrp2BPw_f47bUQ-PIRIsuWAEO1NEfrNppoNWghWeYUe6tmadEyIO6qdqUdX5QaX6197UlQQQ52KohIcM-fbvdYRfYoEDEjdJtPgGx5RUnsIJyNmVBM5NrCgE6OJlMvzhK6vaR8hKH6kmU-QIJ_oqicbAUjAfUhfYDRxnmpifm_oT0NJRs1eVkfsFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81836" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اخر نفهمیدیم ساواک خوبه یا بد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81835" target="_blank">📅 20:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbf5tVBVAqhzSV0p-2_KHNEEBk6tF9ja0H5Y4bEIhV4QivuOMyumQTmQfddOsNMPfIEiY8LeBWcZmnRfgdZFk18-vTtvQEs-zEFrGFcNFkntqB9v3tB1M-Z6IYA5d0g29eQUsdJKOtYuj9TRskDfdBbDFE_1ZqdRPhyBM4LgO8Xjn4cZES3krMD-einJf9IM_c7F_wU199Wx9cUvikgkSEPTwSW24DDRtTevaI96tlfj30a6Aa-9Nry1CiAk16XyT4o9RqFNj31oJ6ZLJSGLmq8vcOd_efz61BxGGaxoXrGHUiRpsQR0UE28B3yb2K6l7PwgMPrbYeYQ8R3_zLF2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس قشنگ معلومه چندسال منتظر این لحظه بود یه آتو از مهدیار و فدایی گیر بیاره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81834" target="_blank">📅 19:55 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
