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
<img src="https://cdn4.telesco.pe/file/UibJvAdftkxWYNQsgq7kSKXEOcQQBc06qDqZXPf9OoDpB-mZ5I4ErEruzQdD3tTt1dfBnizZH8zSuhUclpOSTsyJtP42TjFcG9y9Jaanpqz2R7JHMztlHPGcOK59Bw62iWCMOABCOVXO5m95h-L6LsEPg-XpdELsaNE-ZSPdNcV0fwyi9asLZimtPzEwNLoDd0kclG_IqkbJjUXq_Z7Ze5V5dpcIU7OhpTUvcZlKZGs50ndmZnnMVncvS0nfd5GL46irIKK0YjzrTu6bIDUmt0CtE-Kc6I8jS-g7ruWnFY_YydbaYXSm34CcAQsqUp5Ih_28fthaFuLTgD99OMUrqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 196K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtVinMGsKbGZQr3wttHmVuNfOCfr0d2-uxIYydWdfT0mbvpOV5FDaUUy6uUzXKZ_ZBDF4Itk4dm4QSJRAS0YjqWHBa06dp3LelR5Ze8zF1yHorjRwNyIPPe_JEdz6RGma1Its8huIBWibppgqvqsfZRxQdB3AT1e1JnoHAZ1o8a58bAhBO_zGGHEIf-L72WRmMcaIdcJmSzYT0aGJU1Qwjg6ISSAyFGtXD7IK9ErrMrtTOlK8VTuLhpr1g0fajg4SA-O3U4eHjO4oCtzQjPe1N-nOCzLjoLXi8xHuRefuC1Ep40ywrX1EHT-QnWCMgbEtzl25iBgX8B3iA-z_FdeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3K · <a href="https://telegram.me/funhiphop/80300" target="_blank">📅 15:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuvUKFtNtTVrfH9RUG0j8k-tl-ZS3NvFlnVxEflMPsYMRsExYOLr5QoPNqVagNzcisEuZ80Ak9d0icykAeykkeGT0zslJcktu0wvFo7yrJwUQ1ErKtEYid1M0eOt4qWm7WYDInUYW52UbgD3K94CwXOrOdOwS1LSv8evCQge4LIO65cFv5wXQQBMRh69KFs5J1EZNuRTS049Jlz7QmCycV56xS9swAUhvfJWdiXixcLC7fmPF9X4H8QhlTB7uugGAk8n9qvbi_8rf4lcTMqD1PW8rGnAw5EaUEPpC-j8RkRbxu59YDelZRPrTWvGFGZOA3TMdjuo17gN-nH8o_OKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y95fZ3MjuSebcdmi89Arle7n9CrwgT9BySIIdz_v3sd9jvpV1JG7foWTouPquSshxpRp-8LFjPx3wVSxURDcql8AiOj0LWxrIrHvcNxhQYxJoFglvqoaYzrYe_d5QXrmPRkwQAiGNEaDUNWE9n74l62Vbuhz-SD9l_3nWqN00zKAvUvbTYLx_j3DUbN4DQ4CxKeHiNk2tPb5a1kdg5UpFoHKCE4zGvwZVpkUL-7MbtvcdcpuIze8bHqbC64hVWkm23LLEPlEvnVKl4Mtohjl-21fHL3fMxIX06bS9VTr9gmquI6iyNmWBTlXBVubCIE_phmTu8ty9YT954frcINk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://telegram.me/funhiphop/80298" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://telegram.me/funhiphop/80297" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://telegram.me/funhiphop/80296" target="_blank">📅 14:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الان سکته میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://telegram.me/funhiphop/80294" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://telegram.me/funhiphop/80293" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چه فشاری شد حاجی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://telegram.me/funhiphop/80292" target="_blank">📅 14:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOSpWlLr6rrsdIxnopqZPqwlc9Y3pFKnooz99yXMURH_ya2-Rvb-RagHIpr_bgchP3XKpS8RNQs8yLwWVyLpaNwxwRm_TqRtiAzq3bza6N0vUNF20Oblbk2rERf3M-uMH1ceP0zZFipY8tP6-Hm604t09_0hAYifRl-nmHEcUzZucsiebWZNH9dQhtHs7eGC-UD6hTPvZhMKO1uLoSICMp09_lKG5vGTaPwnDZvPirhCUWbtXFDRNhAazXIX47xbEqUHpQc3yz1uoQdKMXptoobBtIH42jSmtZF_ue2UCeGmtlhMMmwhhx0jFRq9AUAKyYwVPKnw3-cvHHKSkWkCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://telegram.me/funhiphop/80291" target="_blank">📅 14:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://telegram.me/funhiphop/80290" target="_blank">📅 13:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پسر دوش آب سرد بگیر
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://telegram.me/funhiphop/80289" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مامان عمو پورنگ درگذشت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://telegram.me/funhiphop/80288" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-text">امروز روز فلانه و کیرخر‌.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://telegram.me/funhiphop/80287" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار دوباره در جنوب برای ترور مجدد چرسی در جبران ترور ناموفق قبلی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://telegram.me/funhiphop/80286" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://telegram.me/funhiphop/80285" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://telegram.me/funhiphop/80284" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://telegram.me/funhiphop/80283" target="_blank">📅 12:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حالا ویناک که گوز کونی نیست ولی همه این سلبریتیایی که دارید ازشون دفاع میکنید وقتی ایران بودن خایمال بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://telegram.me/funhiphop/80280" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAQMfxVvvFga3itz7WRyQA11KSF2oxl2KPcWAAXynRzhjxAYkHumeDhjW3uoF_jdxgNBW00_h9dFzDTgDGUBMttzxY6_hYjm3MWOi_32NHSqviLpuOTOvxKbvXMGIeWqsMgkp5BOTDgdiMBdqC8uuh0PGhDiFVvp1wY0oBAo7p80jsCfyIkgDt8HkaCqRLjwcD_jI59_Xftf4wnXaFu0WDoL8ub_3kTDT_PvLeA7uesCrQrWV3vrNOnfP35Hz2rureXXRBUvMlt3Zt5UwKWjBQJBTVlQ-94aUw7dUTPilRdKLVB8i8gUPyvQlGOQXsFtm-BJMpopyqcRw2FgEJtOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD2uCV2qTfCYl3BGJiJ0TPwaG5WUSoLcVQbXNhp80Or2oPCZokIm3xFtFvX0bmc2lDrrh6W-YlGonlVVjYlA_PY60Jjw0JNMum1E-RDARKwhjkj29CvHn9B_uEZroblfIdvcf1lCn4ZGHCidFtp-8pnYP3T9DjIZlW6t9CNNZWkI2U0UNz9agQV3wdNJ2UPVPpc5D8xz8HzDb5L_QqttCIQkzCpuh5YyVWi7-COtF8CtgHwQOiumbpGdoBVsgbh9JlWyMDEWIVxX-vbKjeboVCyxFllW266ZL4XNRGtHla7jjWLXnsrQ1c8SupZqeseL27_KFBbc3zNR0GLyuNEh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qv_f_GhjiSwl1MFE3QTAfaiJH9IlzLhHumYM8BjWRiXNMbo8O1U8tNkO79w0q3CoaKbIjMKD8loaGq6O5g4_UO6RKeK5mTknNapyvTIm8kY4pyhcbeIhL0_IWy4_1JpgBL8FTd_qIsC-EiCyX0nUSU7YrTXXTqK7tPQdWNd6XgFPPEGS8IuDDo5c1NG9D-5dEEFpo4cZUiJEerJsaINBZm26JSgp2v2Jnlue4MAkcvvZP9FLF7E8oMzcUN5L0qlxCmbSp0IPrC3lNPoxnjxbUVk1LK7LUJNT01TAHe-p-xf5sD_aXAkcrp2gJLVAp2w7ETSUha2Zivu-_dJQ1RhqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sy1eIEN4X-xjDuAyiIVxbXJtBxxRT4UIOwjHmFrWhRIMr60PlbU5DfJ8wLkJWndsLm3NSAYU_TZFKPjCNvizuzK3ZWm10JgvZ6W2yUp8KiUFyV317DXyl-mPV28kk18134yoE6xFwlf2983SsBgXViZiYE4R0nHWLe44rKVVnCwznVjc8pCklTN6R4TQPqKpm0MFvdvBHNulR9kV0MsmQr0zqc5OUIl_-nowYPQPVYJW2AVNfQMAvmL0_LLzby74t6bmqK0GxJmLvO51DinZ_N6aAFDvhHcGjgVETT7SFpQ1BAYLYNOYQBhayFBDT5RR5qv9njgMpt1EDma9NLGWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_n2FHzlqhtxHjW4XmmbtV2tGdXaSY-NE2BAECJVyy_3YM0Q-xYaxit3bnkjNothE86eJj-HBMzLzVhlH6cVeNJP4cI3lVJR88c0QUBWPmW3KOAW3Q9zQVtQvXHlV-E_lt-XR8vQcyq1HLJGJXk1paK289xgS28uHCEAo7ONZcaye49LooqDLd8QW5gTGqjfcpQdtdWkmaFlubjOqjn02gVwyZX1_lWPtCGlkp_rxUvyaDJ8sSCZ-gzSjWHUtQHzYeVNB1qCiVy7DCF74qCW2zOu8UE9PXQWT13oLFIJ908ENrUP9P2ez4fcIkafk_SszYrgTNdzZ-9MKdzvXgeXlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویناک اینارم از ۴۰۱ گذاشته و میگه من اون موقع هم خایمال نبودم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://telegram.me/funhiphop/80275" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=TA9MHIVo_O6U15K0LzpvGz2-svtlaIBVk8d3YpoEMUWJNR8M--wo6W6mNgpFuXDsXQ5sfDfTZAuta3JiA1J-0TfY0v5dnkELkRAX3bYCcgl-l90i2k2e99eouUCBBnU5WUQme6DfpfKHxuGE_W2PJaCB2cfC2jci60cFLi4kl3H4gW6rOo7A4-VWZKcjfqHNAPkeJdGhmD8_TVOXt5uiRB0BQ7tk9A7G-lIQ66UB7570TBM9bLtaCJzNhFu1sJWG_392aO0KyHh8GrQmwHWuYMvK3zuuKdGkE74H64wqCa3-MUZgtQT3TAadAaJVXJP57WTSDhVVr6WvxYxoj58-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=TA9MHIVo_O6U15K0LzpvGz2-svtlaIBVk8d3YpoEMUWJNR8M--wo6W6mNgpFuXDsXQ5sfDfTZAuta3JiA1J-0TfY0v5dnkELkRAX3bYCcgl-l90i2k2e99eouUCBBnU5WUQme6DfpfKHxuGE_W2PJaCB2cfC2jci60cFLi4kl3H4gW6rOo7A4-VWZKcjfqHNAPkeJdGhmD8_TVOXt5uiRB0BQ7tk9A7G-lIQ66UB7570TBM9bLtaCJzNhFu1sJWG_392aO0KyHh8GrQmwHWuYMvK3zuuKdGkE74H64wqCa3-MUZgtQT3TAadAaJVXJP57WTSDhVVr6WvxYxoj58-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناک یه اجرا از دکی گذاشت چنلش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://telegram.me/funhiphop/80274" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmkZzcB6fZ66Baq9IrnLtmhxagW-IQZQOBmuU_QgKUw4ttOXfFq0VwrXH8jOjSD234XYCPdaBEfMpa0NYDJL_G0dTBhPGsl_tkfZ29CPrDuV9momKUOCQlG_7b-nkEsxIosaXZAc9UqGVjOkWdKZW1cjO3P0o4lobYV2ix0YBPQjLkPT6lg4mQJLAWBkTgT47kXhTCOGQZsTHywwGf8lKVdBcI1uEmGqitDRWMJaKnZFbtOKxhuoNibyBSV-VLz_Sd6Pv5XrjQo8eW_T_re_BdTuUNUqUycgJrYhxXKTv3s5A1Wm_XMuZ3egsIRgMdqsGKH5m1CGkbMmlzblhd887w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://telegram.me/funhiphop/80273" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80272">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEE8MAg0DMlMpnuKoY_6T4mFOi9d6oafkh5PQjV90Yw9WskxW2cX6z4ZU8ddpwuAI0eVOZg_rog0ZRWJIW0svCSpOG0luWG10gO6Up9J8qveplAxDZow3ZWliVEkByJ2OuJXZlK75-7xT4Cknx8JbbEykcREREPl0-mcFni7GsFFrqum7AAJ15nsRPWf98GclLmNWsJa53GFU4heG1g6vVs1e3KzbtsMCpR2tsXxOb71fuuubgRdb9ZrcQlSuUWSAMyqjUpVm3O5UmM-oXEI2v5QZ8S4A13brHqY5_XGDGlXWAfZbAhEDqo4eOrHftfEwQ7CtBIzE1ZrbZQjWACRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهر لیندزی گراهام جانشین او شد
فرماندار کارولینای جنوبی هنری مک مستر، خواهر لیندزی گراهام، دارلین گراهام را به عنوان جایگزین او ، سناتور این ایالت منصوب کرد.
با توجه به پیروزی لیندزی گراهام در انتخابات مقدماتی،خواهرش یک دوره شش ساله کامل در سنای آمریکا خواهد بود.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://telegram.me/funhiphop/80272" target="_blank">📅 10:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ دلقک از تنگه هرمز هم میخواد بیست درصد تعرفه بگیره.
سازمان دریانوردی بین المللی اومده گفته این نقض فاحش حقوق بشره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://telegram.me/funhiphop/80271" target="_blank">📅 08:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیل نیست خوب لانچرا رو کشیدن بیرونا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://telegram.me/funhiphop/80270" target="_blank">📅 04:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الان که شما خوابید آقا آرش بیداره و موج دوم حملات آمریکا به جنوب هم شروع شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://telegram.me/funhiphop/80269" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نفت شق کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://telegram.me/funhiphop/80268" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کنکوری های عزیز ایران بخوابید، کمک در راه نیست.
ترامپ: معتقدم دستیابی به توافق با ایران همچنان امکان‌پذیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://telegram.me/funhiphop/80267" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حالا که مجبورید امتحان بدید حداقل بخونید تا دوازده سال از عمرتون که اینطوری گذشت بگا نره و ی ثمره ای داشته باشه، با آرزوی موفقیت برای تک تک شما در امتحانات پیش رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://telegram.me/funhiphop/80266" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">من که میدونم این سری هم جنگ نمیشه ولی نمیگم که دانش آموزا همچنان امیدوار بمونن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://telegram.me/funhiphop/80265" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایرانم به رسم همیشه عربارو داره میکوبه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://telegram.me/funhiphop/80264" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آمریکا هم یاد گرفته ها
دیگه جنگنده بلند نمیکنه هزینه الکی داشته باشه
یدفه صدتا راکت شلیک میکنه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://telegram.me/funhiphop/80263" target="_blank">📅 01:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eldKauH6luAB3J3RbYzc6XmHb249sds5aHucif5L-HoYLI9aPRZ_UPmaJQwqX8RoAI4AVOXqwhmVcqclECWH1BoFibPPB8g376SutdePXLSz4TRJCinIFErgRI9F92MfohB3EHwhV7rrHC_KUrC1npmZCCfPJIr0dVu5BFF3Ng0k29tRL7PSe5IqT5B__3a9jGn7ptByxO9HY1v_Kk-2hblvAIb6Uk4bv9MCMOmJroj7EUTX6EXwf__sdN1Ub8y8juOkmxk3qaCO9xs35AYGfIgOjFn2_oI7ZqrsgAhKCJnDLSRu51FPbkr02usM2FUeMpraOApJyRjhCyK7dqXAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا موشک کم اورده داره لانچر پرت میکنه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://telegram.me/funhiphop/80262" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17049dea80.mp4?token=E9I1jrPLP6J8ovDJuW19FJP1WlckfdImDJI-b1iatcw4Txy6pQY1aghjV1quLbAHi6VLuy3DoBraywY6S3FwwMEVsPK21bqota1yXlQsiRtZBnGtsLuG73zk84Tjq9QsZKDsuCbpJKqrttUTKB9b2FgnvbR_vi0Ycn2fXLqWmi642tmKL8ZbxAkfFTL7ARfLsUqV_ScXIdKboHVf7v9vj9iBWdZtEG1rQyiAlCWegbYb7FjfSEoVuK2scZAw82fG7_0ASKJjkij59_8TCVmsoSK-x_2KJSHXk73wfwwtBGQ8jwBllION5kceQQJ3Sj-OtLFAiH0Dl1rVOdEviJP_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17049dea80.mp4?token=E9I1jrPLP6J8ovDJuW19FJP1WlckfdImDJI-b1iatcw4Txy6pQY1aghjV1quLbAHi6VLuy3DoBraywY6S3FwwMEVsPK21bqota1yXlQsiRtZBnGtsLuG73zk84Tjq9QsZKDsuCbpJKqrttUTKB9b2FgnvbR_vi0Ycn2fXLqWmi642tmKL8ZbxAkfFTL7ARfLsUqV_ScXIdKboHVf7v9vj9iBWdZtEG1rQyiAlCWegbYb7FjfSEoVuK2scZAw82fG7_0ASKJjkij59_8TCVmsoSK-x_2KJSHXk73wfwwtBGQ8jwBllION5kceQQJ3Sj-OtLFAiH0Dl1rVOdEviJP_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت حملات از جنگ ۴۰ روزه بیشتر نباشه کمتر نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://telegram.me/funhiphop/80261" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حداقل کشورو بسپارید به فلیک شاید فرجی شد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://telegram.me/funhiphop/80260" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جدی بعنوان کشوری که یدونه پدافند درست حسابی هم نداره بیش از حد کیرگوزی میکنید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/funhiphop/80259" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://telegram.me/funhiphop/80258" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheMojoMan</strong></div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://telegram.me/funhiphop/80257" target="_blank">📅 00:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه جنوب کشورید به هیچ وجه نزدیک اسکله و ساحل ها نشید، وضعیت خیلی کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://telegram.me/funhiphop/80256" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسم نمیارم، خط جنوبی کشور کامل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://telegram.me/funhiphop/80255" target="_blank">📅 00:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جم رو دارن میزنن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://telegram.me/funhiphop/80254" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مشهد زلزله شد، این جدیده</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://telegram.me/funhiphop/80253" target="_blank">📅 00:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAꭑır</strong></div>
<div class="tg-text">این‌که تکراریه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://telegram.me/funhiphop/80252" target="_blank">📅 00:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چندتا انفجار تو بندرعباس</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://telegram.me/funhiphop/80251" target="_blank">📅 00:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شروع شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://telegram.me/funhiphop/80250" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه لفظی بود که یه ابرقدرت هیچوقت بلوف نمیزنه، مرتیکه قمار باز تو معنای اونم رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://telegram.me/funhiphop/80249" target="_blank">📅 00:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://telegram.me/funhiphop/80248" target="_blank">📅 00:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: به ایرانی‌ ها اطلاع دهید که ما در راه هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://telegram.me/funhiphop/80247" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80246">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سلام پنج گیگ کانفیگ فروشی با قیمت باورنکردنی هفتاد و سه میلیون تومن، تخفیف ویژه  مناسب پنج خریدار اول.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://telegram.me/funhiphop/80246" target="_blank">📅 00:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80245">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حاجی پشمام این B2 که زدن قیمتش ۱ میلیارد دلاره.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://telegram.me/funhiphop/80245" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r12jiZWj3nh8L-Kwpu3NomJH-a-qLbuVw8dEuWnwQQsW08Oz7ryYXTplZ2BNOsgF773TmxyqWu73Nmw_WeesMa0W56LQdMyNxgkU2sBqs6ZxE7LtFYPl1OmHy6qb3-IWJFbr-CrJKfmdtBk6PO4ETKzjhPAEXZ42v3YKQQqwUFN2nnI0WV3aHT5EoMTVjpC9aVz4G4g_Z4aBRlyljNjJ0fbJSNXCuXbW3R8ulpxgbsRLiR-gMdKCdzYUguI6z-aoEjYrbcmST2yhcQZsGqXY6dym77dJf1dLrbzS19MsHuJ7MYtBUA1u-KKC_lMpxXzbkdI8zhdTvnwqOJxRwMAMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی انگار باز داره جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://telegram.me/funhiphop/80243" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای جنگنده هایی که تو تهران میشنوید مال خودیه، خایه نکنید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://telegram.me/funhiphop/80242" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد.
یادداشت تفاهم یک آزمون بود و ایران به آن پایبند نبود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/funhiphop/80241" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صدای جنگنده هایی که تو تهران میشنوید مال خودیه، خایه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://telegram.me/funhiphop/80240" target="_blank">📅 23:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به مرینو نگید کانته آخرین جام جهانیشه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://telegram.me/funhiphop/80238" target="_blank">📅 23:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اوه اوه بیبی اومد   ترامپ:  امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت.  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://telegram.me/funhiphop/80237" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عباس عراقچی:
رئیس جمهور امریکا کاملاً درست می‌گوید هر کسی که از عبور ایمن و محافظت‌شده کشتی‌های تجاری از تنگه هرمز اطمینان حاصل کند باید برای این خدمات  پاداش دریافت کند ایران همیشه و در آینده نیز نگهبان تنگه هرمز خواهد بود البته بیست درصد مبلغ بسیار زیادی است ما منصفانه عمل خواهیم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://telegram.me/funhiphop/80236" target="_blank">📅 23:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=jrRnvgwJYLHIihvXRWUHTF4Y4qePCAtFlx1-MmcDKNd-KOgrhOocYMWFcdmrn6JWEAsDVyeqNNir4c1apOX-AnwGXraJCmg319-lh17r0f381U7ifzjJjyR3vToBYkG9UtXnTz37CCaxjKexmslkUcgrpx4zGw_-_Q7ni0GFTRax6vF58wteukf1UlUpgIyOYFR5cS_xN7zbDEvTYSgxXfYrE-eX7utfdx1MQcKIJJusfXJYs8R-57jfbPHURaXedioU1ggxEdjZ--5Z4zifJfbTewj5KVanHq4OCJk-2ccL7Jm07tRKsB9UKb2cx8dlvU1Vfqwb72Q9USNcu-Y9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=jrRnvgwJYLHIihvXRWUHTF4Y4qePCAtFlx1-MmcDKNd-KOgrhOocYMWFcdmrn6JWEAsDVyeqNNir4c1apOX-AnwGXraJCmg319-lh17r0f381U7ifzjJjyR3vToBYkG9UtXnTz37CCaxjKexmslkUcgrpx4zGw_-_Q7ni0GFTRax6vF58wteukf1UlUpgIyOYFR5cS_xN7zbDEvTYSgxXfYrE-eX7utfdx1MQcKIJJusfXJYs8R-57jfbPHURaXedioU1ggxEdjZ--5Z4zifJfbTewj5KVanHq4OCJk-2ccL7Jm07tRKsB9UKb2cx8dlvU1Vfqwb72Q9USNcu-Y9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">براورد میشه رژیم داره بالای یه میلیون نفر برای جنگ زمینی با قوی ترین ارتش دنیا اماده میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://telegram.me/funhiphop/80235" target="_blank">📅 22:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بر اساس اطلاعات رسیده به فان هیپ هاپ، احتمال میرود پادگان 04 بیرجند مورد حمله قرار گرفته باشد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://telegram.me/funhiphop/80234" target="_blank">📅 22:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80232">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">همون همیشگی، جنوب ایران
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/funhiphop/80232" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80231">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دریپم مید این ایتالی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://telegram.me/funhiphop/80231" target="_blank">📅 22:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80230">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noE8XsDCdJBmS13ayDv2nNzMOVzksKLAiQF_uD9SqrxpwcfGPCXmZ3NTgHdz_j1WDj2PCaCMdkEFTlOSK3A-KS6mO-5WNPodI39RbDWUuLlx2ddbU2mMcrd7hzaP2b1hrkGYUWBbk7BDgIfNJRTODgE4PxkJ6zw8Ke52LcP_ssSPwFEiv4xVwdmuegJksCdu7HXvdhIHhO5AdnZ4AvLX3EPbgCKD04EinUoyjf_wFfj5NtDUShmaZSYFh6hY9nZadPtc10YIBawQ_NI7oP7Xue93iOah1vio2djPcPNxKou9A3rXKL_Ti44O70WpbIw03GzrbpPIcdB1K0DW2DaJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرطان حلزون گوش گرفتم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://telegram.me/funhiphop/80230" target="_blank">📅 20:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80229">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://telegram.me/funhiphop/80229" target="_blank">📅 20:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طبق تحلیل من با این محاصره ای که کردن تا بعد انتخابات میان دوره آمریکا خبری از جنگ تمام عیار نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://telegram.me/funhiphop/80228" target="_blank">📅 20:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from2METi2</strong></div>
<div class="tg-text">باحاله</div>
<div class="tg-footer">👁️ 16K · <a href="https://telegram.me/funhiphop/80227" target="_blank">📅 20:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80225">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 16K · <a href="https://telegram.me/funhiphop/80225" target="_blank">📅 20:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80224">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جمع کنید کازو کوزرو علی گرامی ترک داد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://telegram.me/funhiphop/80224" target="_blank">📅 20:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80223">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اوه اوه بیبی اومد
ترامپ:
امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://telegram.me/funhiphop/80223" target="_blank">📅 20:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80222">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل سر انکار هولوکاست از محمود احمدی نژاد کینه سنگین داره و دیده هر چقدر خودش تلاش کرده نتونسته ترورش کنه؛
الان به جاش تصمیم گرفتن اینقدر تو رسانه‌های مختلف درموردش شایعه پخش کنن و بگن آره این ۵۰ ساله جاسوس ماست، مکان حضرت آقا رو این لو داد، یه قدم مونده بود براش کودتا کنیم به قدرت برسونیمش و... که یه روز خبر بیاد خیلی اتفاقی دکتر احمدی‌نژاد تو نیم متر استخر غرق شده یا مثلا خیلی اتفاقی پاش لیز خورده از هلیکوپتر شخصیش پرت شده پایین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://telegram.me/funhiphop/80222" target="_blank">📅 20:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80221">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آقا مگه قرارمون نشد تا پایان جام جهانی، تفاهم‌نامه برقرار باشه همه‌چیز گل و بلبل باشه تا جام‌جهانی در آرامش و کاهش قیمت سوخت و اینا؟
مگه ما ایرانیا مسخره شماییم که این‌همه تحلیل و آنالیز سنگین و دقیق و پیشبینی مانوک پسند می‌کنیم و بعد همیشه سعی می‌کنید جوری کیرمون کنید که تنها خوشی و استعداد ذاتی ما رو کاملا زیر سوال ببرید؟
۴ ماهه تو این چنلم کلا ۴ تا پیشبینی کاملا منطقی کردم هر چهار بار بزرگترین کیر زندگیم رو خوردم خب الان کدومتون پاسخگوعه؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://telegram.me/funhiphop/80221" target="_blank">📅 19:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80220">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش تکان‌دهنده نیویورک تایمز در رابطه با جاسوس موصاد بودن محمود احمدی‌نژاد:
بر اساس این گزارش، احمدی‌نژاد در اوایل سال 2024 برای مذاکرات سری در بوداپست، پایتخت مجارستان، با مقامات اطلاعاتی اسرائیل دعوت شد. او به بهانه‌ی یک کنفرانس علمی به آنجا فراخوانده شد و طبق گزارش، دو بار در سال‌های 2024 و 2025 با مقامات موساد دیدار کرد. منابع آمریکایی و ایرانی به این روزنامه گفتند: "این بخشی از یک تلاش چند ساله اسرائیل برای پرورش احمدی‌نژاد به عنوان یک دارایی اطلاعاتی است، که در زمان مناسب، بتواند به رهبر جدید ایران منصوب شود." این در حالی است که احمدی‌نژاد، در دوران ریاست جمهوری خود، برنامه هسته‌ای ایران را تسریع کرد، خواستار نابودی اسرائیل شد و انکار هولوکاست را مطرح کرد.
در سال 2024، حتی ددی بارنع، رئیس موساد، شخصاً به مجارستان سفر کرد تا با احمدی‌نژاد ملاقات کند. موساد، این جلسات را به سازمان سیا (CIA) آمریکا اطلاع داد.
بر اساس گزارش، اسرائیل به طور پنهانی مبالغی را به احمدی‌نژاد پرداخت کرد و مقامات اطلاعاتی اسرائیل در چندین نوبت با او دیدار کردند.
این تلاش‌ها در اواخر فوریه امسال، در روزهای اول عملیات "غرش شیر"، به اوج خود رسید، زمانی که یک عملیات جسورانه برای انتقال احمدی‌نژاد به یک مرکز امن موساد، به عنوان بخشی از طرح سرنگونی رژیم، اجرا شد. این طرح شکست خورد.
در 28 فوریه، روز آغاز عملیات، یک حمله هوایی اسرائیل به محوطه اطراف خانه‌ی احمدی‌نژاد انجام شد و هدف آن ساختمان‌هایی بود که محافظان و خودروی زرهی او در آن قرار داشتند. پس از حمله، یک خودروی پژو مشکی به محل رسید و او را به سرعت از صحنه حادثه خارج کرد. رانندگان این خودرو، ماموران موساد بودند که احمدی‌نژاد را به یک خانه امن و مخفی در ایران منتقل کردند. با این حال، احمدی‌نژاد که از این عملیات نجات به وحشت افتاده بود، تصمیم گرفت خانه امن موساد را ترک کند، اما جزئیات این اتفاق هنوز مشخص نیست.
موساد به درخواست نیویورک تایمز برای اظهار نظر، پاسخی نداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://telegram.me/funhiphop/80220" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:
مجتبی مرده! به احتمال 90 درصد کشته شده.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://telegram.me/funhiphop/80219" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6fb756260.mp4?token=kIvaUZVx3IAS5M7FP0LGIKzV_UvxvtHnNssy1jLO5M_0eolM_gAslE8njjlXUm1kPkzgkfm9vL6uQaaB6s15xft-xn2w5GPh3SxO4RgyFvaN-Sc2UUY_HncLo9IE6Jq6NjrwtePnoH3HFD25JgX7h2HC8w8hE_Q-04uI_B0WiUVi7CLFWh9NZgHmWUNOtbW0Kti2EROthO_HiGtLaCcS4nb_s6OkbKE1KQNs9Y978bNYSmFbSt3go6b8VCQ1-iNUJ10nt4e2s7nHnPalYXw0cPKW4rSLgZ2QWKUtIhFke32YKeB3FtdBS0cv6wtBZqFnCMcS9wbpHHL2tTQdBuQ8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6fb756260.mp4?token=kIvaUZVx3IAS5M7FP0LGIKzV_UvxvtHnNssy1jLO5M_0eolM_gAslE8njjlXUm1kPkzgkfm9vL6uQaaB6s15xft-xn2w5GPh3SxO4RgyFvaN-Sc2UUY_HncLo9IE6Jq6NjrwtePnoH3HFD25JgX7h2HC8w8hE_Q-04uI_B0WiUVi7CLFWh9NZgHmWUNOtbW0Kti2EROthO_HiGtLaCcS4nb_s6OkbKE1KQNs9Y978bNYSmFbSt3go6b8VCQ1-iNUJ10nt4e2s7nHnPalYXw0cPKW4rSLgZ2QWKUtIhFke32YKeB3FtdBS0cv6wtBZqFnCMcS9wbpHHL2tTQdBuQ8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف دکی و ویناک انقد جذابه ترکای اونارو ول کردم کصشری که مرصاد داده رو دارم گوش میدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://telegram.me/funhiphop/80218" target="_blank">📅 19:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VlM2dA3f-Ad4xR-1qtnNNUv3Q-WaEbleyWeE5d6s9fcW1ibKImeg78XohSiZzEphFM8h2ea7M_bpPy7i22i3Yh8PZzW1iVrUmaH48NiNfijJ_kBlfMNrvm9gsNAxUcxOaDn0XVzadtT9iS3U6R85YpJwrVyMICZsti0WGBpkopwHLVIT4iv8IwxswdPQsEgoTgIic2vqZbugPz-7tfnK71hIPbnfE4ZHPPNQFVI4Bzj7G8V4jPU2mTiO4ZPUGB1ipduJeOhh4_-Q_d9WybyRIP-cwVSOlcGK_0tKYrFZ8AkJdqsTM4fTsyZxyMlFEH7XSNWjmvgq69L_gIucSbfQgcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VlM2dA3f-Ad4xR-1qtnNNUv3Q-WaEbleyWeE5d6s9fcW1ibKImeg78XohSiZzEphFM8h2ea7M_bpPy7i22i3Yh8PZzW1iVrUmaH48NiNfijJ_kBlfMNrvm9gsNAxUcxOaDn0XVzadtT9iS3U6R85YpJwrVyMICZsti0WGBpkopwHLVIT4iv8IwxswdPQsEgoTgIic2vqZbugPz-7tfnK71hIPbnfE4ZHPPNQFVI4Bzj7G8V4jPU2mTiO4ZPUGB1ipduJeOhh4_-Q_d9WybyRIP-cwVSOlcGK_0tKYrFZ8AkJdqsTM4fTsyZxyMlFEH7XSNWjmvgq69L_gIucSbfQgcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیزهای اختصاصی بت‌فوروارد، مرجع تحلیل مسابقات برای تصمیم‌گیری هوشمندانه
🎲
📈
در بت‌فوروارد، هر مسابقه با بررسی دقیق آمار، تحلیل عملکرد تیم‌ها، شرایط بازیکنان و مهم‌ترین داده‌های پیش از بازی به‌صورت تخصصی تحلیل می‌شود تا با دیدی کامل‌تر و اطلاعاتی دقیق‌تر، تصمیم‌گیری کنید.
📗
برای مشاهده آنالیز اختصاصی هر مسابقه، وارد وب‌سایت مجله بت‌فوروارد شوید، سپس نام تیم یا دیدار موردنظر خود را جستجو کنید.
👍
ورود به مجله بت‌فوروارد
کلیک کنید
mag.betforward.com
کلیک کنید
mag.betforward.com
🅰
g22
💻
@Mag4ward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://telegram.me/funhiphop/80217" target="_blank">📅 19:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80216">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: بیشتر رهبران ایران کشته شده‌اند. خامنه‌ای از بین رفته است و ۹۰٪ از پسرش از بین رفته است. ما آنها را از بین بردیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://telegram.me/funhiphop/80216" target="_blank">📅 18:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80215">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ محاصره رو دوباره برقرار کرد: تنگه هرمز باز است و خواهد ماند، با یا بدون ایران.  ما تحریم‌های ایران را مجدداً اعمال می‌کنیم، که این تحریم‌ها به این نام هستند زیرا فقط از کشتی‌ها یا مشتریان ایران جلوگیری می‌کنند تا وارد یا خارج شوند. سایر کشورها می‌توانند…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://telegram.me/funhiphop/80215" target="_blank">📅 18:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DarDtzdkpg1yPwMhfUloQyBcS01AwlBkDBq_rGzdTI4e0fHWZ5dm19RRZ7aSSfo3FD6QVPp9MxgEQ9iD8JO0LR41ZnQ-bU3pGPRhdbw1NS5zaO4JPdCXplNk3CY-UXA7JtOWS2s_m-FjpivhJ222miCyq8c3l4VRFDT0f43kOjpxSAaxg_vdcgBx8kNQGPyzojyb6700JNzEeNX7Wd_enCXi4MOyNVEK_bez8Bbbwad9tt4S0sCK9uDDE7kPvpDPuLsIkVTHhpKfbmEnf9eG-Q-lC-mnWsYJik3ZOKE-bQw5rwPUQg13NtlrWELhyO1tnxjPueh1Bp35mDAXtwA6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ محاصره رو دوباره برقرار کرد:
تنگه هرمز باز است و خواهد ماند، با یا بدون ایران.
ما تحریم‌های ایران را مجدداً اعمال می‌کنیم، که این تحریم‌ها به این نام هستند زیرا فقط از کشتی‌ها یا مشتریان ایران جلوگیری می‌کنند تا وارد یا خارج شوند. سایر کشورها می‌توانند به طور عادلانه و آزادانه از این تنگه استفاده کنند.
ایالات متحده آمریکا، از این لحظه به بعد، به عنوان "نگهبان تنگه هرمز" شناخته خواهد شد، اما به عنوان نگهبان و به عنوان یک اصل عادلانه، برای هرگونه هزینه لازم برای حفظ امنیت و ایمنی این بخش بسیار ناپایدار از جهان، مبلغی معادل 20 درصد از کل محموله‌های حمل شده، به این کشور پرداخت خواهد شد.
این فرآیند و تشکیلات بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://telegram.me/funhiphop/80214" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://telegram.me/funhiphop/80213" target="_blank">📅 17:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://telegram.me/funhiphop/80212" target="_blank">📅 16:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز ترامپ یه جوری سنگین تهدید کرد که بالاخره می‌شه با خیال راحت چسبا رو از رو شیشه‌ها کند و با جزئیات صحنه‌ی امضای توافق رو تصور کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://telegram.me/funhiphop/80211" target="_blank">📅 16:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://telegram.me/funhiphop/80210" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://telegram.me/funhiphop/80209" target="_blank">📅 16:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c80ff7fa.mp4?token=heEUjGSFg76yI2VoqVkk5OmLJ3ElwlF1BhzU4u44GTQtzWdRTLsYGKDGMh1bEj2673DByn1di-ItsyHQs7i1Bae0WlogkoYp9FRVtjjJliUQjWiiCwQSjs9B20a1iDHvfntBcCl_u4TGtXTDiKF2ogcGwXT3GJZHDJl3v44B3wBKWyv3-VUuRiNgHq9q8u6lYsJH0m-HexGCMLS_fxQnBFhtsftSQz7eiDkW_c5slqMNi0zVr8ydTisZZAMRVlvq5eu_Jst5jRmwoE_K3TeyxFxonttkcuVmShvYulgRV9Bo_iBgZ-EDbDJldnMW0TpsPEokF41egxi2Fpe2K2oRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c80ff7fa.mp4?token=heEUjGSFg76yI2VoqVkk5OmLJ3ElwlF1BhzU4u44GTQtzWdRTLsYGKDGMh1bEj2673DByn1di-ItsyHQs7i1Bae0WlogkoYp9FRVtjjJliUQjWiiCwQSjs9B20a1iDHvfntBcCl_u4TGtXTDiKF2ogcGwXT3GJZHDJl3v44B3wBKWyv3-VUuRiNgHq9q8u6lYsJH0m-HexGCMLS_fxQnBFhtsftSQz7eiDkW_c5slqMNi0zVr8ydTisZZAMRVlvq5eu_Jst5jRmwoE_K3TeyxFxonttkcuVmShvYulgRV9Bo_iBgZ-EDbDJldnMW0TpsPEokF41egxi2Fpe2K2oRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز اعتراضات رانندگان و حمله ماموران با گاز اشک آور و باتوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/funhiphop/80208" target="_blank">📅 16:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd12e51ec2.mp4?token=LIekWOeg2fu5ty7xMD_r_yobxFwa9yclzTVIOU4fHZUfXbw9wvIEiLEAzTnkXOodc4LpZ2gQSuENPIeWNktBl6rG74IolCNPw_ETAqeKlUq5ok9TsGaNXHNsFFVoHCwHLDRKcQw5OofBKWyUgkf6Etudh7JjGt5NlCidrGoGtjgY7SutI2YpTXepXhMHcTW0h-iUoW446USylKY9Gidnsi9ErO6_TK8vSQQoI9duvltffpJZWLw-roN52xjVo4ft5TrF7xiJB4ZjV8PD1Ujb7BHG1FCf4zRcM3kXRBPsJb0Kzf4ts0pteNejfqSutuek0slW-jgi3lyj3837ZueXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd12e51ec2.mp4?token=LIekWOeg2fu5ty7xMD_r_yobxFwa9yclzTVIOU4fHZUfXbw9wvIEiLEAzTnkXOodc4LpZ2gQSuENPIeWNktBl6rG74IolCNPw_ETAqeKlUq5ok9TsGaNXHNsFFVoHCwHLDRKcQw5OofBKWyUgkf6Etudh7JjGt5NlCidrGoGtjgY7SutI2YpTXepXhMHcTW0h-iUoW446USylKY9Gidnsi9ErO6_TK8vSQQoI9duvltffpJZWLw-roN52xjVo4ft5TrF7xiJB4ZjV8PD1Ujb7BHG1FCf4zRcM3kXRBPsJb0Kzf4ts0pteNejfqSutuek0slW-jgi3lyj3837ZueXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش زدن مادر فرودگاهو گاییدن کجا میخوای فرود بیای  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://telegram.me/funhiphop/80207" target="_blank">📅 16:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ای کصکشه تاجر
ترامپ: ما عوارضی را برای اسکورت کشتی‌ها در تنگه هرمز دریافت خواهیم کرد.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://telegram.me/funhiphop/80206" target="_blank">📅 15:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4GQPEizD4m2U4p2h9mLkyF6CEsi2SymLzAvIN746TjFauzhFOen5enttSGYj4F5xJajcrLL9Rfd4x8iAJlJh_nV3Y35_z8oxpLs8OyyUGdE3RBMqwcIjwo_OqlME0T-68VnQkuW8Pn5dFhZ7Jm3zgZhOpX75AfFAMJ7kSnP1esS10qZbWW_pLs10LtHNmKnNpMnad6E0Fprr0tFAITSTL4Dx2EavZ82E21u8WTaME1QaO0Y5KBVd7raOQo83oFHkx2OQV1Ja465S0zX-xJ6Pw5vyQ1kN0x6lGdmqZyc7zxA9gYlw0fW8I6zLSmfcXQFLo6xzCBk8Tpvn6moNDN7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت مرگ لیندسی گراهام پارگی آئورت بوده.  @Funhiphop | Reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://telegram.me/funhiphop/80205" target="_blank">📅 15:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چه عجب
دولت بریتانیا، سپاه پاسداران انقلاب اسلامی (IRGC) را به عنوان یک سازمان تروریستی معرفی کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://telegram.me/funhiphop/80204" target="_blank">📅 15:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جلیلی چه پولی داره خرج میکنه، کل تبلیغات فیلترشکن های رایگان شده بنر های تبلیغاتی جلیلی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://telegram.me/funhiphop/80203" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4e2nn_zweCw9zMsZHp4grhe8Bt-URNhLL8jnu7Q4FhzcPTYL2BUo7Vl_PMtAhtgs6qpfoTvKsNvPNvBZMNmMnUvNxpkalS8IoPOTs19l1BT-JP-rASxL3M5GON_73aWOXWYUr87ojTT302qBo6MLFl6TO6ij5d2Z9efOUg4Lj2XVMuaklXGTs7yPkQINQSgFccD5dX0GghqEgUoWCa-bcrFn7D_6zYo_gxqaUUffYe6qvAumw2exRQcedIle8iDsv_j_Eqp6D-gIezrHm5X5NHo711iVwizzVnBqBRX6Aeb60E8Cq6k8hCbwY9TD2yUEr6YBJlRIQ3w-dqZp4ty7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش زدن مادر فرودگاهو گاییدن کجا میخوای فرود بیای
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://telegram.me/funhiphop/80202" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امتحان امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://telegram.me/funhiphop/80201" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=Roc7SNpaxFe7C7lvl-ZVRwKq17kmwS9uMgG-phqdxeBij8xv0sxVrvdvoMLHqbqLm3g52FnaRekbpB8gZcQYTn8hHvXL4gNquSk0kj-Czfp-cCxU1y_-Ttu-WWM-mG81Dzt8W4NanjxrrJOA1s6spP3lCiE1VhihbYk0n5u-97BS33sW3JUKIsG0xPbg_ybwosOPM1bVsO6zyi5CPGiloRiRoKjRxDFNFb9mA9HjZIUoRxSHk7bBMY5_LUcvQhVoFOuglbXxs4vi1xaSvSPRkyIpNLMvOhe3Q-tMPWCshaBIyi7Anw-wkf9thNKbdTDmnHkRTHQfxteBcwmE_GjFxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=Roc7SNpaxFe7C7lvl-ZVRwKq17kmwS9uMgG-phqdxeBij8xv0sxVrvdvoMLHqbqLm3g52FnaRekbpB8gZcQYTn8hHvXL4gNquSk0kj-Czfp-cCxU1y_-Ttu-WWM-mG81Dzt8W4NanjxrrJOA1s6spP3lCiE1VhihbYk0n5u-97BS33sW3JUKIsG0xPbg_ybwosOPM1bVsO6zyi5CPGiloRiRoKjRxDFNFb9mA9HjZIUoRxSHk7bBMY5_LUcvQhVoFOuglbXxs4vi1xaSvSPRkyIpNLMvOhe3Q-tMPWCshaBIyi7Anw-wkf9thNKbdTDmnHkRTHQfxteBcwmE_GjFxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش رید به حرفی که یارو میخواست بزنه
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://telegram.me/funhiphop/80200" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIEXVNFvd9mEStACd_tnKSGDCO7V4VimAjJclYpXS1VcthFMZ3xoK9bvyNFbwBWjU-eb8-G3JDJNrJG09fkn2suM7Zm6RfKxRAPziVUtY_UP7oDF6iUUXAr0YNBZlhQ2h8zpH396J4a6g2HomA65KFAGXPVyKYQMfXfiKSHhqmwRUaFsEpCDfH1CdOpSFzVGNElvQS0qfpLLgjH4FE6SNES1UdWToJ-q9DZGOlujZpvuHSGauh7rbaCNFiFtdSpasKO7y4Yl4crUMmaDs0pFXgbiz-5neZvPiQXXYw1vZlaux2UJ81w3KFgVTHsNR43lBpMlW2eEe1Z147vHN9AgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فحش آزاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://telegram.me/funhiphop/80199" target="_blank">📅 13:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3wGRIdYkg_B3lBsW9Y9vzZBO5Rte0Z5fBAhA-x31zy85GC64f8q2FD6ul5QyEGnqzh5vPFjHFoypvMj3olIEA55qN8-ZxwX_NdIeNKq5BnU0v-UmOJ-VD7Evss8fL7yOhygBId-oLZ2V40_Yh6FjLoKXHV1jTlm5aAI652xZgtoxIAE5xztVOUAvBztk_NmPeedRS4bf11TDDcyjjTf4bFaZFTc1zh091QZxo1iMjDkC2zt6KarCUhAoB5IHwRcfG4wsg3925uuhGm1d2gRotz_unCnzxfinE1M2yimwbjUlsHvEKQfQF2l4lAwd60IUbjh5WdOysWZiHdHaQhDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا رضا مچتو گرفتم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://telegram.me/funhiphop/80198" target="_blank">📅 13:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://telegram.me/funhiphop/80197" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhamE3_NORWqaow1A5i8TTyQmrqjmne_LNRzHOk_xnqj5f5jB2RuNzkKvm--bjrDCdmNk6OqggaXDuvuyZI7Du56I00QgNpacClJiwyUUU_d4Qpzh2U8-HGMWCKnDI0tSs72GIBJ-C0H4j4oSnoF3YSGub1Kv_UjjOGQ-pMQf1pFkxEQDew-BUOtVXR9jFzM0nmUi4Kbg8LnKRaE3ByGLPJ9-2HCJ_2IS7UaqD6zrE5C_PKAJmwLDppBobzbHpKhv1z5k2oJpekMhLrKlnyjjSfH__N1WJRlgORmjxaK5wwtTm-DFzAkim6n-SlyDsYgtyrJISDK1LrQv-6Qi24cUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تلخ هادی چوپان...
💔
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 18K · <a href="https://telegram.me/funhiphop/80196" target="_blank">📅 11:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4J7FzzoBKCl3_4tKkN5mLpsOCf9hkn-G3TwwcknfQvUOYo607ittKt139EBEMGoXJeQr_rCayNRdaFOLFQvRvEfalpx8rP_0XOmtUJ671FntrrLWtPXK331zAhuI96O2jkyuxNMTTaoaxQ03teTJxVQLpQ4HtDxHI2nSWD5V3nnVkXKVDGXjkeVPs9cYfyBNa1-g0p1LkY8LdzUMpdVFF3NxuXnoBBXCnBeJgfpvndN6Fn_2jYcNP5sSHKWKC85zJJZsjiaOrOUJzUZGAxe8fG1I12Xuwf3Cp4XlGrKHGFznn-uvAGbu9RVsRpY7X0nK3TayekFPJJJndbUdNafkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم برا حمید سوخت پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://telegram.me/funhiphop/80195" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2Vpxc1j_HQLCsJfm4sMGeev1Iu0mTSfKhs0Sn3OMnPj1l2zYtzEfXxMn_7b05hUAtIbKGJbjBK21-2gkalKD0U1Bj7PxBZwXwceS_AYMsrDQSV2indeCT0Mwre-NzFPkl57tqa0RjUToeS60DDW9o7xRo93u0VJHeW787z6WU7d_fpULEkkXjjUJP5zwMOQu1HbVO7PhCpZaXXs9VDn_ojZeoH0nunQrNeDhfAj_uL2D8oNbUOht5PMH3EglJUUtnRkhBMNPryMQbBb8YvJpyNbNFz2WJJbTWEGYiTzUUZ3eNBU2BJG4APZXSN8tGFZcPDSu4ZId9z58lsBBra3Pk0VM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2Vpxc1j_HQLCsJfm4sMGeev1Iu0mTSfKhs0Sn3OMnPj1l2zYtzEfXxMn_7b05hUAtIbKGJbjBK21-2gkalKD0U1Bj7PxBZwXwceS_AYMsrDQSV2indeCT0Mwre-NzFPkl57tqa0RjUToeS60DDW9o7xRo93u0VJHeW787z6WU7d_fpULEkkXjjUJP5zwMOQu1HbVO7PhCpZaXXs9VDn_ojZeoH0nunQrNeDhfAj_uL2D8oNbUOht5PMH3EglJUUtnRkhBMNPryMQbBb8YvJpyNbNFz2WJJbTWEGYiTzUUZ3eNBU2BJG4APZXSN8tGFZcPDSu4ZId9z58lsBBra3Pk0VM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیزهای اختصاصی بت‌فوروارد، مرجع تحلیل مسابقات برای تصمیم‌گیری هوشمندانه
🎲
📈
در بت‌فوروارد، هر مسابقه با بررسی دقیق آمار، تحلیل عملکرد تیم‌ها، شرایط بازیکنان و مهم‌ترین داده‌های پیش از بازی به‌صورت تخصصی تحلیل می‌شود تا با دیدی کامل‌تر و اطلاعاتی دقیق‌تر، تصمیم‌گیری کنید.
📗
برای مشاهده آنالیز اختصاصی هر مسابقه، وارد وب‌سایت مجله بت‌فوروارد شوید، سپس نام تیم یا دیدار موردنظر خود را جستجو کنید.
👍
ورود به مجله بت‌فوروارد
کلیک کنید
mag.betforward.com
کلیک کنید
mag.betforward.com
🅰
r22
💻
@Mag4ward</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://telegram.me/funhiphop/80194" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علت مرگ لیندسی گراهام پارگی آئورت بوده.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 18K · <a href="https://telegram.me/funhiphop/80193" target="_blank">📅 11:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یامال بالاخره ۱۹ سالش شد</div>
<div class="tg-footer">👁️ 20K · <a href="https://telegram.me/funhiphop/80190" target="_blank">📅 03:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نه،تعویق نخورد امتحانت، بخواب ایرانی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://telegram.me/funhiphop/80189" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امشب با اختلاف سنگین ترین حملات از سوی امریکا رو شاهد بودیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://telegram.me/funhiphop/80188" target="_blank">📅 02:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سلام باز صدا پهپاد میاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://telegram.me/funhiphop/80187" target="_blank">📅 02:39 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
