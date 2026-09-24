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
<img src="https://cdn4.telesco.pe/file/GzIBTwRN5nn2fclwzFCG9PFzy0nXuAg-OzoitXLlwznnnaGY2HoB-7T1X2kSC4I5_hA2sf-qDr-GJoe6EWZtnIoiEKPX1O2_0ZiuaCuF51pnEyvnUGtj10DKPjvi9PDg4cXswTwCFA_YS1RkdSHJzFqJ0ivpB0HcuHRZU12XuiEsr62pHr4JjgqIEWrrFNL9kLzBYzWk1ZMf5GkiDBATox4DvuDXeYs-caUR4S9zB4SameMFDyRHiZXrWkkDQ2U-vvVjKT9PChJ6LYQgCKPZiW8z_eouCd8c_J9juYBfbEG8sWbjfS_1DfD58-0iWKIlnIZPDgnrCbWCovSHNZOr9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-692674">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6a98c029f.mp4?token=RKoGyDtwVlHVkovmn_qHlUwM7sc8v5NoHHzQAphjgdUZwOZ4mYXdBjar2wjCl8h2zKpdRDl3g7xNA9FnDIld9B1PhYQi9J61hCqInRwUiX-T4LnmEAX6DoYq8nEB-0HBEOyWqOvbHolZgBuOfVbQkkAP0x__zVm-DLhTbg_WC8X-0zv1n_2dpLJAeqOyPzfKxwJH_yBiSjhVXIcqnyJ2Jk7q6OM7rDo5RfHsI8ue8BWYDBIKeXuFboAC1-SZpLqGxeCDDQ3CoF363_WP3aVWgihvK8IA63VbOw4eVFu3hJ1A_0vS3stXNVqoiVqJbDOWXP29oQWQ5oSjqqGumUnIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6a98c029f.mp4?token=RKoGyDtwVlHVkovmn_qHlUwM7sc8v5NoHHzQAphjgdUZwOZ4mYXdBjar2wjCl8h2zKpdRDl3g7xNA9FnDIld9B1PhYQi9J61hCqInRwUiX-T4LnmEAX6DoYq8nEB-0HBEOyWqOvbHolZgBuOfVbQkkAP0x__zVm-DLhTbg_WC8X-0zv1n_2dpLJAeqOyPzfKxwJH_yBiSjhVXIcqnyJ2Jk7q6OM7rDo5RfHsI8ue8BWYDBIKeXuFboAC1-SZpLqGxeCDDQ3CoF363_WP3aVWgihvK8IA63VbOw4eVFu3hJ1A_0vS3stXNVqoiVqJbDOWXP29oQWQ5oSjqqGumUnIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونگی شکل‌گیری بارباپاپا برنامه کودک دهه شصتی‌ها
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/692674" target="_blank">📅 19:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692673">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b4b52775.mp4?token=iKtZpjA7u6qaH7Rt0xyb6ci5v5TFTWyGOBdg-GPlC0Dez7JjRMnSv6ghTaCAo-yYIScfib36ywLarZLxWiet6jhsiG-gTemhv-XWLJmOTTQuarJg7Y_QZ48K_G-PKDQ7zo_lyJVkcSeF-V1IF6uFSkI0wtink-7XPKilaWzcmlmT76ebA5F-UZg9Co0u_Om2sef9cYxHlVx4__uWWPF0H0MdfB7wqeQnfq2y7fB_u5GsmBh3AabsRIiqkkEBASZDsclmOExkPGeTodwkP6IN91_cY0hDYR-1IJnOgG5vXRHOHBJiuufYoJ8t5Dl-vNozfxkh2iAXe0DbhUyHSKfSk7pssxlk5GD3Yv4GlPi5KeLq_HL-HOoH-IWwd0xzXce3OR3UgDNT1soBOhZEhT-AiGdm4DodlyR_8_hWDh_1mgHlc_u7jy38Fc_1S6M6y9vCU7WEze0gi20qIsrdLBuRIYeyrqTfwShC6sHCBjiixgE1GlIFaiuwOIz0Ia6Sx7JU3XCHI-DzRf-HBqHd8rsFR_W5EuTwC2m3yBGpYhr34ZF1PPuXA9d6pAFOjBTsN_Sde_R9dZ1O7OmC-UUiDBJI36EFv_TFGqXtIg1FuZhN87PtjIuGLjAXtWUooRxv4Raxm-0cfhiccLBVtj68kI9o22thEqZIZemGjNSp2ohWC3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b4b52775.mp4?token=iKtZpjA7u6qaH7Rt0xyb6ci5v5TFTWyGOBdg-GPlC0Dez7JjRMnSv6ghTaCAo-yYIScfib36ywLarZLxWiet6jhsiG-gTemhv-XWLJmOTTQuarJg7Y_QZ48K_G-PKDQ7zo_lyJVkcSeF-V1IF6uFSkI0wtink-7XPKilaWzcmlmT76ebA5F-UZg9Co0u_Om2sef9cYxHlVx4__uWWPF0H0MdfB7wqeQnfq2y7fB_u5GsmBh3AabsRIiqkkEBASZDsclmOExkPGeTodwkP6IN91_cY0hDYR-1IJnOgG5vXRHOHBJiuufYoJ8t5Dl-vNozfxkh2iAXe0DbhUyHSKfSk7pssxlk5GD3Yv4GlPi5KeLq_HL-HOoH-IWwd0xzXce3OR3UgDNT1soBOhZEhT-AiGdm4DodlyR_8_hWDh_1mgHlc_u7jy38Fc_1S6M6y9vCU7WEze0gi20qIsrdLBuRIYeyrqTfwShC6sHCBjiixgE1GlIFaiuwOIz0Ia6Sx7JU3XCHI-DzRf-HBqHd8rsFR_W5EuTwC2m3yBGpYhr34ZF1PPuXA9d6pAFOjBTsN_Sde_R9dZ1O7OmC-UUiDBJI36EFv_TFGqXtIg1FuZhN87PtjIuGLjAXtWUooRxv4Raxm-0cfhiccLBVtj68kI9o22thEqZIZemGjNSp2ohWC3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلویزیون اینترنتی «خبرفوری» رسماً وارد مدار شد
🔹
«مدار» تلویزیون اینترنتی خبرفوری، همزمان با یازدهمین سال فعالیت این هلدینگ رسانه‌ای پس از پشت سر گذاشتن شش ماه فعالیت آزمایشی، رسماً وارد فاز عملیاتی شد.
🔹
تلویزیون اینترنتی «مدار» با تکیه بر استودیوهای تخصصی…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/692673" target="_blank">📅 19:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692672">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmyzEyKP09b1c6usbtqAmBogkE3_2RDgMpLO2uYn6JlW7ZTLch6gXRhVteZXfveuDa9kwR36eJ2dkiFTELj796OIY7qWzNP12HFKj-nGSDMuUduecHNqo9ayhXV7_ptKQFate4kwJK_XDCPP0JToOtg2Qk-BCq55V69-NNxWzV5x22qq_TR_0zjWC_GIBcFtCVlNLJG7xkyPyexXvMS-l60mhMhA7YA5PEqIznHQQC_mwMpjC5GmMtTYXfKk9_ALkh3fauec687XQ9dUoY6GrY1b2DXuPnxIAdZrRIEJ-qs77b1LQ7jJce25DZkquC85ISJKWvIla8xyBFsZyMroEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما اونجا بودیم...
🔹
این ویدیو مروری است بر برخی حوادث تلخ و شیرین که ۱۱سال است خبرفوری در روایت این اخبار کنار شماست...  گزارش کامل کارنامه ۱۱ سالگی خبرفوری را در سایت بخوانید
👇🏻
khabarfoori.com/fa/tiny/news-3247219</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/692672" target="_blank">📅 18:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692671">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
از ساعت ۲۴ شب گذشته کلیه پروازهای ایرلاین‌های ایرانی به امارات  نیز لغو شده است/ ایسنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/692671" target="_blank">📅 18:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692670">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoNOXwiaCvNss5V1KtvJperT8naqPFDPH9YizwhkB36ojmGmv4MPt0Q33l8G6yC3zY9n9rnoYlkojHGRf-ywJtFBbxDpV_3PkY-SaLkTBFlLY1MQtuD2NR45nmQ32SYs8pxR7PKNcytNpF25leiSQcqj0mF4g-eizBGEwx_YmxIQ7Gq0sbxWPW_kOm69PezaF1vZOusmufJUJtimGfCgHhG6VJwIO3jUMS8kXtJpYFwG0qAxAcQp7CCAaM3BuFSGdnhGtQBpCuwj5HMu6RtI1emHe-2WkS2iYZxZfjKwB9fh1MX-e53gt4e1s1J5csE_97E6_hEKthJAc5es6WMqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از نگاه مجله تی‌سی‌کندلر، محمدرضا گلزار به عنوان جذاب‌ترین مرد ایران در سال ۲۰۲۶ شناخته شد!
🔹
همچنین گلزار جزو ۱۰۰ مرد جذاب جهان در ۲۰۲۶ شناخته شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/692670" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e7535140.mp4?token=ue9UZSNkIHLU69xZiYi8TxSJ3olWzUQkz1n9WT2DS1u5vchCBhbW9uNZuILESzbOpi1niABeIWe4yq26N0dxT_RgvGY3s-HfiPAxshmt8cNbxLftSPXnPJb88N0tOpWjlm10PlqEmyATDldEgbf6cxBCRcEjw9oBPfUq3Q95g2LhuQoyqgm0flrOuXNDsmScCXGgnvL6AU4cO6r6B3vCHFdDDVxjT4TrhVSTFLBDvApzPS8Rs7HHAHfiocMkfCrjabpOr-jPLVRz5h_OuWaQJWI4llmKCU7bmqn-GMoebJ_2ztZaGhXxCR_Rg4-rXmO1tXhi0_9X4YNdjPRCJZxhPh2DCqtnCpqQTu_4NohEH6_3UU2hIrN_92GT-4mlKm6IDPvwKWrUKxTveKdJoRy3faWAH7Zt01i6lDjjOKgqrwjP3gQN1cuL3E7nAfCCybHL1F2vNvNVd9GPjnrky-THT99i8gOb5CuqNIQqt1UfPF7cNRmebpn1NoLrFfcp_hMSwevoWSB6XwxsCVfi3qY3zQq82LcK7R7Z6-pLVLckH1ltjXsCbfs-mnUfuQabLk-M5uBV90pYPJm1cuielRKLOdZBLjptIE4ci3Z6bVmyva_a29HB9VNNzugApS2EOSwddWuQkdMz18DciZsBxYPMPjgGBFRd6MApQn4gbMAs5Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e7535140.mp4?token=ue9UZSNkIHLU69xZiYi8TxSJ3olWzUQkz1n9WT2DS1u5vchCBhbW9uNZuILESzbOpi1niABeIWe4yq26N0dxT_RgvGY3s-HfiPAxshmt8cNbxLftSPXnPJb88N0tOpWjlm10PlqEmyATDldEgbf6cxBCRcEjw9oBPfUq3Q95g2LhuQoyqgm0flrOuXNDsmScCXGgnvL6AU4cO6r6B3vCHFdDDVxjT4TrhVSTFLBDvApzPS8Rs7HHAHfiocMkfCrjabpOr-jPLVRz5h_OuWaQJWI4llmKCU7bmqn-GMoebJ_2ztZaGhXxCR_Rg4-rXmO1tXhi0_9X4YNdjPRCJZxhPh2DCqtnCpqQTu_4NohEH6_3UU2hIrN_92GT-4mlKm6IDPvwKWrUKxTveKdJoRy3faWAH7Zt01i6lDjjOKgqrwjP3gQN1cuL3E7nAfCCybHL1F2vNvNVd9GPjnrky-THT99i8gOb5CuqNIQqt1UfPF7cNRmebpn1NoLrFfcp_hMSwevoWSB6XwxsCVfi3qY3zQq82LcK7R7Z6-pLVLckH1ltjXsCbfs-mnUfuQabLk-M5uBV90pYPJm1cuielRKLOdZBLjptIE4ci3Z6bVmyva_a29HB9VNNzugApS2EOSwddWuQkdMz18DciZsBxYPMPjgGBFRd6MApQn4gbMAs5Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرورت شفاف‌سازی دولت در ناترازی انرژی
سعید داغینه، مدیر مرکز توسعه پایدار انرژی:
🔹
دولت باید برنامه‌های خودش را کامل برای مردم توضیح دهد.
🔹
دولت باید سازوکارهای حمایتی را به مردم اعلام کند و به مردم ثابت کند که به آن‌ها پایبند است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/692669" target="_blank">📅 18:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09078affc8.mp4?token=DR4GW4VUwKIWfI717O7z21G-iloyTXwQg0lvOnucSnkJlSuNlJRAFsEE-cjBkpOsGGeCwX7NaCOn07StTA6ztnB1gS1id6iS2jlw1Uw0HGRELhm3OYn5Ox_eYQiC18umNATok-3LKavUpaGUpUdEhlo5ruv8gwX9gUVLdtJFhez50AWK-Hr7EsrAHvrAa3iGH5awUlEEW5MWyTHurbqXWKsZqBnqfjYFBlPPMnryky58dggBOTkPHMuK8aQ74PgzQxAWHkFPxSQ1u_uSVCOML_s7koB5w1xCK2PmCav-G2IWe61evIHjFeTVFxt8moEZEp1rHulQ5qJygeCnOy69aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09078affc8.mp4?token=DR4GW4VUwKIWfI717O7z21G-iloyTXwQg0lvOnucSnkJlSuNlJRAFsEE-cjBkpOsGGeCwX7NaCOn07StTA6ztnB1gS1id6iS2jlw1Uw0HGRELhm3OYn5Ox_eYQiC18umNATok-3LKavUpaGUpUdEhlo5ruv8gwX9gUVLdtJFhez50AWK-Hr7EsrAHvrAa3iGH5awUlEEW5MWyTHurbqXWKsZqBnqfjYFBlPPMnryky58dggBOTkPHMuK8aQ74PgzQxAWHkFPxSQ1u_uSVCOML_s7koB5w1xCK2PmCav-G2IWe61evIHjFeTVFxt8moEZEp1rHulQ5qJygeCnOy69aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخشی از سخنرانی معروف معمر قذافی، رهبر سابق لیبی در سازمان ملل سال ۲۰۰۹ و یکی از جنجالی‌ترین نطق‌ها در تاریخ این نهاد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/692668" target="_blank">📅 18:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bc15423.mp4?token=pnYAvzSUsYZYLzhsAHzu8Wu_WElXl_jbrANJTTVVboDASrucyQPJCUHOtR9E4TckUV8ZGGMia9yRRmPVBWzS2jh0RGmrjqsnIa28Zyg0gQvNUj8v5BsHV-BxXbkCrrN5QhNjuMx64rge_ZVRaSakfMW6FpWHJvgcCJ07kVvSEoaH-9lc4f298vvbqllDCLypaJjSX6zPSinLN1HECXr5BeXW0cO-2uVN8IM00ujI3-PHwG_FuSbbdSpnLTXbHqUK7MsiR9sC0qdvoI-r6i2XVpDYZhG3-pgIo5sbKIp8M8MA7NdRf556bUdlp3SUmO5NlaT4ygIpaY3VXONVut4g6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bc15423.mp4?token=pnYAvzSUsYZYLzhsAHzu8Wu_WElXl_jbrANJTTVVboDASrucyQPJCUHOtR9E4TckUV8ZGGMia9yRRmPVBWzS2jh0RGmrjqsnIa28Zyg0gQvNUj8v5BsHV-BxXbkCrrN5QhNjuMx64rge_ZVRaSakfMW6FpWHJvgcCJ07kVvSEoaH-9lc4f298vvbqllDCLypaJjSX6zPSinLN1HECXr5BeXW0cO-2uVN8IM00ujI3-PHwG_FuSbbdSpnLTXbHqUK7MsiR9sC0qdvoI-r6i2XVpDYZhG3-pgIo5sbKIp8M8MA7NdRf556bUdlp3SUmO5NlaT4ygIpaY3VXONVut4g6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدیه رئیس‌جمهور چین به ترامپ؛ دو پاندا بنام‌های «پینگ‌پینگ» و «فوشوانگ» راهی آمریکا می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/692667" target="_blank">📅 18:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivVMJ3OJgpU5rkXpjYCduojUCz_zm7AIaQkq7CqP04uC7IqVU3r-2lKv4TIemwZg8GaF4b2wx44_Zh5qjbzLv9TjNHhBZttb0gMdNL0EL5ULK48wMyCQKtrKQ7BCjzCc4jX6hfLNjEKS2ZYT4gKL_npzzXtusYmCLGjnKiX27fflzvIM995RdVAAkBqdprdH2S-UYiStjDFjWq9CImrZMc4PLDxpVdci13iQpYEHaAeo0Bi2AfsaZ04tmcw59rmduapQAg9qwuPYMp2r8m3lVS50OeDZjQsbaBTJ1xNv4DWMD-ENYuKOq60mK2hJb9v1JQe70yyQLIl5BP4nxZBnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c93JntV34dJGnwt1uL5VWlvAMuwqb1uL4d9xJBiVzmkMyVTWXxtB40oits9Tgx63lmzkXJNDHRVfC6MIoVnn7dZailcj1vBoc3bnyFt-OdV4d9OpkMZ5oQkBlF0JTtvWsJqlmXdsohRhqCvaZciKEIQD3ZPLOiSbEa-B0MujaMlxd_F1EMOGrXZ3eK1NnRCMKJHX_El3Jk8t8SdoKRjd9-gKE86PoPyvkv8QHQKr0OyzZwhuhfujvX8jRkUOhU3Vw9ouJSeipFuu1OO42v1aPk1c31RvgBL-hGMnU_9Bv6LwVCM2myo4_4XkLZAxUn4rs74IKLHLqrJzNhufVLwnMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هدیه جالب عمو قناد به یک موتورسوار؛ فردی که دیشب او را در محدوده انقلاب سوار موتور کرده بود، امروز به دعوت عمو قناد به منزلش رفت و یک کلاه کاسکت هدیه گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692665" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: منابع ارزی مورد نیاز برای تامین دارو از همان ابتدا توسط بانک مرکزی کنار گذاشته شده و ارز دارو همچنان ترجیحی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/692664" target="_blank">📅 18:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1d2bccb4.mp4?token=MAnHoenPNOpxFXJNg838CZrqsENyJhNSdrr1iEK8EWr1iq2aB8LJyd590Z85LUTGYtxdGPOkaamgQ524SRPlFF_Sxg1vgcRknRcJkASW9-t5KgEEK-sxXjCqVf14caxTkTL32fLqpsd47MuUjeEpONrXyij8lLag1NZXinQgbR1cSHuFQjFu67j69qqL9BJ8jlOKrWNvTCIpJiRbUEs7rPlPt9jnQFrOtTdtmGr-TExj3N7mR_OyrtRk-s2xIB1eiGEigCwMa1AmFXu5_R4UdTqIU8DQYNmwEjXYMV2KQmPg0gjnsZWawACtD_EZrm9-RJUQ2pM3g1gthL4vKq-r2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1d2bccb4.mp4?token=MAnHoenPNOpxFXJNg838CZrqsENyJhNSdrr1iEK8EWr1iq2aB8LJyd590Z85LUTGYtxdGPOkaamgQ524SRPlFF_Sxg1vgcRknRcJkASW9-t5KgEEK-sxXjCqVf14caxTkTL32fLqpsd47MuUjeEpONrXyij8lLag1NZXinQgbR1cSHuFQjFu67j69qqL9BJ8jlOKrWNvTCIpJiRbUEs7rPlPt9jnQFrOtTdtmGr-TExj3N7mR_OyrtRk-s2xIB1eiGEigCwMa1AmFXu5_R4UdTqIU8DQYNmwEjXYMV2KQmPg0gjnsZWawACtD_EZrm9-RJUQ2pM3g1gthL4vKq-r2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این اصطلاحات بامزه انگلیسی می‌تونی جذاب‌تر صحبت کنی #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/692663" target="_blank">📅 18:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBmrXMbL445by7MDG_AOa_keDUiB2Ukkre7zLEY_a5j2HrNKsVPSZ3y4t2KKMyfvdZ6H_CFwZh-tndWGxLZDwzY4fSQNaH5lMeeycbdDJP7OCrVulfbpwDDSzL5YS7MZyUL-zuQyLpZppGqW0VrDlwCr74eqR8M8T0LZhc_0Cr_-3LtDvrvh76le9foH4M27_gr4jgX3_BgoHNS2y5_a9KZz0e05uT_Qj-uRhS3ARRq9LhfsEW5Vo_gZdtUjTT73EEsQwOAnWNQeoPgzR56U6TVI7KFIuIpaAnfXJD4AEPyTUkKqL-u6BI_jhgzbwBbvBrzxXdea2Tbyxc5hgWwfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ خودشیفته در تروث سوشیال با انتشار تصویرش کنار شی، رئیس جمهور چین: فقط ترامپ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/692662" target="_blank">📅 18:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اصغر فرهادی برگزیده جشنواره جاده ابریشم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/692661" target="_blank">📅 18:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قیمت واکسن آنفلوانزا ۲ میلیون و ۱۸۵ هزار تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692660" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96639117a6.mp4?token=ayIF8JI3YKPWdCR4j2w9oqX43f6cBDMSr78l7cHWtmGtKmp7uBUjPWQOO2m73X3-JCwVJQsKQdATHAWqsMo-Wp6Fp_cfmgZy7lFp4u3PQPRNTdeO0mjGqZyu0oLuvTM7L30z-kMHZ-E5t0cJGkiRsZM2ui1SI1R3h-DMPmqbWQOxL9Jh8yO7h54Y5-4oyPI4dShG_OzZiR_5bfTnOV5OcFv3xT8XUbI3TnPBxv-Ug9WWY4lou824oPITUDhUW807pq8zYE2MtRlQJ-yzmaVRPZm9cg8nZ0UGRORNQuiNaLJveD_sj6HDITGbNnzbSYsl_ZgNhowQn17u1QjcMpxAWx8zhTcFLKhlhtWsfj2fuyEwaTNU0tWbHqBzZQL2yil8nzCTzl_w6mDCuvhIkqVNjIepQqWIsPp7xTe8SHurprm5OE--75c35U1vhH1lurm-docEASnYWG8L1fligzUDPYggpSSG_cfFVMMDASWICQT9B2e8B2Ii0e3qS-urBLg0QDOScNjeCV5GFiqv30cb0B7fhxoGybH0MCQOP7UL-Noi5VRXyjldvtFZjcAIqpVaXe_q9Ticv3EC-YvT8URrunr85UQ8coECDn1RM-4R6CV4l5LbEtVXlZ3rSUqm3iGGZumkY4jW74SWA5-Z7NloNzu0TLeVDmJRygetnJ5Bmw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96639117a6.mp4?token=ayIF8JI3YKPWdCR4j2w9oqX43f6cBDMSr78l7cHWtmGtKmp7uBUjPWQOO2m73X3-JCwVJQsKQdATHAWqsMo-Wp6Fp_cfmgZy7lFp4u3PQPRNTdeO0mjGqZyu0oLuvTM7L30z-kMHZ-E5t0cJGkiRsZM2ui1SI1R3h-DMPmqbWQOxL9Jh8yO7h54Y5-4oyPI4dShG_OzZiR_5bfTnOV5OcFv3xT8XUbI3TnPBxv-Ug9WWY4lou824oPITUDhUW807pq8zYE2MtRlQJ-yzmaVRPZm9cg8nZ0UGRORNQuiNaLJveD_sj6HDITGbNnzbSYsl_ZgNhowQn17u1QjcMpxAWx8zhTcFLKhlhtWsfj2fuyEwaTNU0tWbHqBzZQL2yil8nzCTzl_w6mDCuvhIkqVNjIepQqWIsPp7xTe8SHurprm5OE--75c35U1vhH1lurm-docEASnYWG8L1fligzUDPYggpSSG_cfFVMMDASWICQT9B2e8B2Ii0e3qS-urBLg0QDOScNjeCV5GFiqv30cb0B7fhxoGybH0MCQOP7UL-Noi5VRXyjldvtFZjcAIqpVaXe_q9Ticv3EC-YvT8URrunr85UQ8coECDn1RM-4R6CV4l5LbEtVXlZ3rSUqm3iGGZumkY4jW74SWA5-Z7NloNzu0TLeVDmJRygetnJ5Bmw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظرفیت نیروگاهی ایران از ابتدای انقلاب ۱۲ برابر شده؟
🔹
‌به‌گفته وزیر نیرو، ظرفیت نیروگاهی ایران از ابتدای انقلاب تا سال ۱۴۰۵ بیش از ۱۲ برابر شده است.
🔹
در این گزارش، با استفاده از آمار و داده‌های موجود، به بررسی صحت این موضوع پرداختیم و روند افزایش ظرفیت نیروگاهی کشور در این بازه زمانی را بررسی کردیم.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/692659" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fa435b47.mp4?token=FZpA-WF4PzBfyKvRWxZL20F8DhCV11WRsL9b7K-NWaNBQ4kl8_sN3nA1IuDgj6nhqOxHDcINbdrSa_LuSdAw8bkN4iWXSWu34ISNz-EWhxM7E6PmLKT-gWj2o8Am2GR6jjSAKj7E7pR4ocPePr87GE52PSN_mrJ9SvY6pAQoIbX7ePWET4d1wiy0MWOqmt-VeF8xrpvvYE6xviny7ZCs7O2g6ccT-9mGDiU67GDpxJ03VIVFq281uq8007_IUBi5voO3x2OlhnWwO6a7AASNs0Yml7Tt3T2EgSoONo_-7AKTzL52jJnal-cGQNPXT5XC5enIHHPoWprnHhaJGxBvyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fa435b47.mp4?token=FZpA-WF4PzBfyKvRWxZL20F8DhCV11WRsL9b7K-NWaNBQ4kl8_sN3nA1IuDgj6nhqOxHDcINbdrSa_LuSdAw8bkN4iWXSWu34ISNz-EWhxM7E6PmLKT-gWj2o8Am2GR6jjSAKj7E7pR4ocPePr87GE52PSN_mrJ9SvY6pAQoIbX7ePWET4d1wiy0MWOqmt-VeF8xrpvvYE6xviny7ZCs7O2g6ccT-9mGDiU67GDpxJ03VIVFq281uq8007_IUBi5voO3x2OlhnWwO6a7AASNs0Yml7Tt3T2EgSoONo_-7AKTzL52jJnal-cGQNPXT5XC5enIHHPoWprnHhaJGxBvyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری تماشایی از تلاش ایمپالاها برای نجات از تعقیب یوزپلنگ
🐆
🦌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/692658" target="_blank">📅 17:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKzyeUj81XT9sFOQ4BI604xWBeHof_LXjlrK3SKrWPcZ74DWgZKOlTYPdrRaBQ_81O7gE5hoNgEl1MqTH1TfApUFZIMMS7gd69EkAf5oyJSAHWAepUJpvoA5qKVrqFqyWDmCwPDxwICTgG5tf8WjPzOUn0httUOR-sQwT4-C8z-K2U8nZIoOy9gRV0RBHdyxlFB_KBibgLlEMW40UOtE6rpvA-XW0jUOnin3T0SsHJ_VpIZTcu2hbkXON-umqVN8r-lvpsbY9VNZgg9azbIEFmQxSXcTH63sy3-NShwQL4X-s43IQ21FSFHN6UeUekXeCsUtV491_dCR2jO28fdEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویداد تجلیل از کسب‌وکارهای خلاق حامی بانوان ۷ مهر برگزار می‌شود
🔹
رویداد «تجلیل از کسب‌وکارهای خلاق حامی بانوان» با هدف شناسایی، معرفی و حمایت از مجموعه‌های اثرگذار در توانمندسازی و اشتغال‌آفرینی بانوان، روز ۷ مهرماه ۱۴۰۵ برگزار می‌شود؛ هم‌زمان فرآیند داوری و ارزیابی کسب‌وکارهای ثبت‌نام‌شده در این رویداد در جریان است.
به گزارش روابط عمومی موسسه کمک به توسعه فرهنگ و هنر؛ این رویداد با همکاری صندوق پژوهش و فناوری صنایع خلاق و مؤسسه کمک به توسعه فرهنگ و هنر برگزار می‌شود و بر معرفی کسب‌وکارهایی تمرکز دارد که در ارتقای جایگاه بانوان در حوزه‌های اقتصادی، اجتماعی و فرهنگی نقش مؤثری ایفا کرده‌اند.
در این رویداد پارک ملی علوم و فناوری های نرم و صنایع فرهنگی، تپسل، تپسی،  بازار ، با سلام، کارگزاری دال و دانشگاه علم و فرهنگ مشارکت دارند.
فراخوان ثبت‌نام این رویداد پیش‌تر منتشر و مهلت آن تا ۲۵ مردادماه ۱۴۰۵ تمدید شده بود. اکنون، پس از پایان ثبت‌نام، اطلاعات و مستندات ارسال‌شده از سوی مجموعه‌ها وارد مرحله ارزیابی و داوری شده است.
بیش از ۱۳۰ طرح به دبیرخانه رویداد تجلیل از کسب و کارهای خلاق حامی بانوان ارسال شده که از این میزان حوزه های صنایع دستی، گردشگری و میراث فرهنگی، سلامت، غذا و محیط زیست، مد و پوشاک و آموزش بیشترین سهم را دارند، در این رویداد از ۶ کسب و کار خلاق تجلیل خواهد شد.
کسب‌وکارهای تحت مدیریت بانوان، مجموعه‌هایی که بخش قابل‌توجهی از نیروی انسانی آن‌ها را زنان تشکیل می‌دهند، کسب‌وکارهای فعال در حوزه اشتغال و توانمندسازی بانوان و همچنین برندهایی که محصولات و خدماتشان به‌طور مستقیم با نیازهای زنان مرتبط است، در این فراخوان امکان حضور داشتند.
محورهای اصلی این رویداد شامل نوآوری، تاب‌آوری در شرایط بحران و پسابحران، اشتغال‌آفرینی، نوآوری اجتماعی و توانمندسازی اعلام شده است.
گفتنی است؛ کسب‌وکارهای منتخب پس از بررسی مستندات، برای بهره‌مندی از حمایت‌ها و فرصت‌های پیش‌بینی‌شده در رویداد معرفی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692657" target="_blank">📅 17:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692656">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q98IvYH6smJE_nAXN0gEkiiwZXbhyWOWScItUMNtNs-L54FD6ZcoST6a6mS_tnA1_XTTObJ8SvtlPyPdRUSswF56mvuIAOP_CRO9rqQyRlTx8oV9yzUNQd9EcM6W8f9R3Fjtin7qB5imL-yzrfzcwkmXRJ8Rcogs1vSWUOw9C_ag9zilv0FH0hMGTMQqd1s3KB5cTMzCT67jaFs5LOaDOtj1Tthmzb7LWb4YOpQh0e5YlrT_YP4Mjiwg89CaEvKWaPO7wm8qRWNft0SP_uTGhxTCklxZyfeflKGOeeLTfltUpRRpK1q_Zchua5nsYiu697ah68KoiQHys2rap41v7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از استقبال ترامپ از رئیس‌جمهور چین   ترامپ:
🔹
قرار است با رئیس‌جمهور چین درباره ایران و موضوعات مختلف دیگری گفت‌وگو کند. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/692656" target="_blank">📅 17:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شبکه ۱۲ عبری: به دلیل ملاحظات و الزامات امنیتی، هواپیمای حامل بنیامین نتانیاهو در یکی از فرودگاه‌های نظامی و دورافتاده آمریکا به زمین نشست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/692655" target="_blank">📅 17:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7462972e.mp4?token=GRMOdVPzCh9PLLlQym_qYv9sgTBFNDZfyIYTTHDvqZVkfk3mw89cWOcMYJmZBVS7iWP6yo7dsw_wHFv5Oxngu76zKHvSxL8pZH6F3Dj38n3o9CsHvT8t6ETKFldJkz8gBzjSu52b1fzMCgTCD5Q4s-doCVm_BVvog3Ml2dpVB2PEZsatXMD31s4U_IJb2G6NSQhYMQyOCAUVX5CLuut9JhD2LVTNuRp29trUYJ9Q_B7Bx74-FrGyY2B3Rq6F5RpC6nxLZnwVdRBZckwlCK4XKYo3Ga_MInfVzDqwUPF7GBTfQTRUpGH1or-O9kePItQxX7GlQ4tzAIXtj1tsG47N2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7462972e.mp4?token=GRMOdVPzCh9PLLlQym_qYv9sgTBFNDZfyIYTTHDvqZVkfk3mw89cWOcMYJmZBVS7iWP6yo7dsw_wHFv5Oxngu76zKHvSxL8pZH6F3Dj38n3o9CsHvT8t6ETKFldJkz8gBzjSu52b1fzMCgTCD5Q4s-doCVm_BVvog3Ml2dpVB2PEZsatXMD31s4U_IJb2G6NSQhYMQyOCAUVX5CLuut9JhD2LVTNuRp29trUYJ9Q_B7Bx74-FrGyY2B3Rq6F5RpC6nxLZnwVdRBZckwlCK4XKYo3Ga_MInfVzDqwUPF7GBTfQTRUpGH1or-O9kePItQxX7GlQ4tzAIXtj1tsG47N2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط پژو با دو سرنشین در زاینده‌رود
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/692654" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سرلشکر وحیدی با اشاره به سخنرانی پزشکیان: «از جنگ نمی‌ترسیم» ندای بلند و استوار ملت ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/692653" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9312a799.mp4?token=M4Is8jKAF54qZN7J23aAhD3A4C5Z0mIiPs57EYCOk6_PUZENl5w1yo8e1_xksb8V40p9TqIJYmw_31gHWP_RhuaIL_FZAGpsI-el8ap-6EKp2Tt-SZHOM-vERRPD_E9AD5PJck6StHdQ7uz_7YzotcPZcBBkfD_TwJKdmtNls8b8OWBJxISt7X37CKl2-C8Q9mf2G4Tj1NtjGuJr8JAfrUVE20cS2nntnN0D54A9oxVCSFZeGl6f9Y60PQCuLW0NXrEqfBhT6l1POSMXs4x0vpq5H9VYT2b4LRc-73emxTrEwR9s01cja_6KgTFC7-bBQ2kcI-E-tnHNpG9dye4SeUB2oq4wFkJeNTVZFKAv2PmKItjfBwkYsJ3kf8f58TLG6VdoQRKv_I31FzKZmvVmb38gT7w2n3y2ctz4hTni5T5GPhrDYDZNt2JWTy4d6YadWmqKcXunAOLTXDyk2TIwO11sUYMwyI48bo5ZCwS-f3uNO6JnntmVfIRzVr2G-bQt0-i2SlfHuIyXN7KCka9Rz_iKad7y49mFdyOKTrzXugG3Vrmz6wqT0ICt4t8PJLF9B_iaqsXRlWiuQ358Z2HEmeet4wC3JihiH_vizh_u3XaLagv0Zpy3RyOdF1s62ZF8ggPAJ0oQsvEEQwan0uI9bswM31RJJ4ODR8bn7xO1xsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9312a799.mp4?token=M4Is8jKAF54qZN7J23aAhD3A4C5Z0mIiPs57EYCOk6_PUZENl5w1yo8e1_xksb8V40p9TqIJYmw_31gHWP_RhuaIL_FZAGpsI-el8ap-6EKp2Tt-SZHOM-vERRPD_E9AD5PJck6StHdQ7uz_7YzotcPZcBBkfD_TwJKdmtNls8b8OWBJxISt7X37CKl2-C8Q9mf2G4Tj1NtjGuJr8JAfrUVE20cS2nntnN0D54A9oxVCSFZeGl6f9Y60PQCuLW0NXrEqfBhT6l1POSMXs4x0vpq5H9VYT2b4LRc-73emxTrEwR9s01cja_6KgTFC7-bBQ2kcI-E-tnHNpG9dye4SeUB2oq4wFkJeNTVZFKAv2PmKItjfBwkYsJ3kf8f58TLG6VdoQRKv_I31FzKZmvVmb38gT7w2n3y2ctz4hTni5T5GPhrDYDZNt2JWTy4d6YadWmqKcXunAOLTXDyk2TIwO11sUYMwyI48bo5ZCwS-f3uNO6JnntmVfIRzVr2G-bQt0-i2SlfHuIyXN7KCka9Rz_iKad7y49mFdyOKTrzXugG3Vrmz6wqT0ICt4t8PJLF9B_iaqsXRlWiuQ358Z2HEmeet4wC3JihiH_vizh_u3XaLagv0Zpy3RyOdF1s62ZF8ggPAJ0oQsvEEQwan0uI9bswM31RJJ4ODR8bn7xO1xsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت تماشایی معراج؛ ناکامی رقیب آلمانی!
🔹
حرکت ورزشکار ایرانی مورد توجه کاربران قرار گرفت و ورزشکار آلمانی با وجود تلاش فراوان نتوانست آن را اجرا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692651" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b3fe3135.mp4?token=WPt0RXkc186bzK-v5aFZX3O93gXhl6ThUWueomUHzdC5zwrfUPIYAxYTgq6O5BJ2UtX9QOTrYwAJAuODFJDi7deUEN02rOov_NFtIfpBTiqYJUGOYsIG1Z-dOaaVwykPVHHu9h82mReY2yZu7YAuYUGKAng_oH8UXI1_O0Qw09Q6ps9p_lOMSJwZsnHCIgQbTSt-H_TOb2ANZG8bF4NpvIs25YZScqovYxGO5GnPkgy_ER0gFrcT_DYfEtMUQzwid64Mk-owIkMzFBNA-7KGpsefpFFSw0LlJeA1Fb78S9nfPMrOMny83HpyW9pJAJH8sL9kyiSufhMNVVxrCq057A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b3fe3135.mp4?token=WPt0RXkc186bzK-v5aFZX3O93gXhl6ThUWueomUHzdC5zwrfUPIYAxYTgq6O5BJ2UtX9QOTrYwAJAuODFJDi7deUEN02rOov_NFtIfpBTiqYJUGOYsIG1Z-dOaaVwykPVHHu9h82mReY2yZu7YAuYUGKAng_oH8UXI1_O0Qw09Q6ps9p_lOMSJwZsnHCIgQbTSt-H_TOb2ANZG8bF4NpvIs25YZScqovYxGO5GnPkgy_ER0gFrcT_DYfEtMUQzwid64Mk-owIkMzFBNA-7KGpsefpFFSw0LlJeA1Fb78S9nfPMrOMny83HpyW9pJAJH8sL9kyiSufhMNVVxrCq057A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق
صمیمی به مدال برنز پرتاب دیسک رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692650" target="_blank">📅 16:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رأی‌گیری احتمالی سنا درباره قطعنامه پایان جنگ با ایران
رویترز:
🔹
سنای آمریکا ممکن است از امروز درباره قطعنامه‌ای رأی‌گیری کند که هدف آن الزام دونالد ترامپ به پایان دادن به جنگ با ایران، مگر با دریافت مجوز مشخص از کنگره، است این اقدام برای محدود کردن ادامه عملیات نظامی آمریکا علیه ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692649" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc442036c.mp4?token=EaSnMx-cNAE5C8vQCz_K8Zc7-4VATk_mk8xKRd_PnMDRXPxAU3Cg8RW-QkaD-xV12aTbZd6vHKK9xobwHPccPQLpiHlYORgwhx60pUaZ-7MUBmE7zE6_UYU3pXC2fcH_1f2xOEye3z8W5bR29jrqSjeAp9yK_kwdUWvR0p_agWJsaQe_uQbTrgty_pKH5dAD1K8HEByqR0kNbBpcHGsSy2dDDcRzfIY3cl6FUwzroFzoWawuNm-C_OpE54U7ahvqHfIB6L7mu0NkRjIXPPwuj4h5m_7fLRQ_4s85zi9-iG3zAYI5xja3QprzXNMLrjC6n2vp3iC0Bpb8bG-hEmev1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc442036c.mp4?token=EaSnMx-cNAE5C8vQCz_K8Zc7-4VATk_mk8xKRd_PnMDRXPxAU3Cg8RW-QkaD-xV12aTbZd6vHKK9xobwHPccPQLpiHlYORgwhx60pUaZ-7MUBmE7zE6_UYU3pXC2fcH_1f2xOEye3z8W5bR29jrqSjeAp9yK_kwdUWvR0p_agWJsaQe_uQbTrgty_pKH5dAD1K8HEByqR0kNbBpcHGsSy2dDDcRzfIY3cl6FUwzroFzoWawuNm-C_OpE54U7ahvqHfIB6L7mu0NkRjIXPPwuj4h5m_7fLRQ_4s85zi9-iG3zAYI5xja3QprzXNMLrjC6n2vp3iC0Bpb8bG-hEmev1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترافیکی که ۱۲ روز طول کشید؛ یکی از طولانی‌ترین راه‌بندان‌های تاریخ چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692648" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVsbgqpXxH7c5-Mm6BIcYQ9fs9YMNrDx8Iye67TTF9H2k8ZYz2P1abCWwMcqJa8PoWQbFuxBNAj9eixaU0WY69P6kbfcOR-L-hrMJci2I2Rl_Ki1fD55WM8WH6ch8yPYJDu_x-DrTJuUT10uDqw56MTV3BuaBpPJAb58ID49NH7r5GzOL9XwZsSgZf8wJLiQrpXDO4jMg94yG6uFSZs_xdhYdBrcIOLNFtIMa75O7g95RUKiHra1BBRBK6sg1Onnowx7Xrt3NbgIcv2a4pXPd5_XJcypADSfnTxt3m-8Nx7GDEHA3mcOGwctb8WIEv22t6jr2wycJcxREp5Np_Ok9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد شگفت‌انگیز مساجد در جهان
🔹
بررسی آمارها در سال ۲۰۲۶ نشان می‌دهد که تعداد مساجد در بسیاری از کشورها با سرعتی چشمگیر در حال افزایش است.
🔹
ثبت رشد ۳۱ برابری در آمریکا، ۴۰۰ برابری در بریتانیا و ۴۲ برابری در ژاپن، گویای تحولات معناداری در این کشورهاست.
@amarfact</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692647" target="_blank">📅 16:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ba325bef.mp4?token=YoHESdPr_W3IKlaRn9bL1ZlHZCJI-YQANoqJ2VQVEtyYq_aCytyPx69bRhUOBZTGAlfWuZcaNr5RP45V_cdTUtbuCsc5rlS9rM9UkGpFDZOps7QGg2UA7fE4FvsoWQ_4Skdq18MDv-lWTSU4bR9XjLgVmAf8zN9ZEjx7_KuSCXRbFBH95h9DU6nRmdaOUnh41NVHT2U2GxkkOliok4hNQPEVxWGXBNKw9fYHNFo4wvcLvIxg8M3yMhjZc_Hz3qXi5fM-IlERboJv2ywIb6anuOIjxakIQBYEIHJ185EwA-ppxowbwc43FEZ9awP6tCRwU10cj7YnjXpHn-4tE4g0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ba325bef.mp4?token=YoHESdPr_W3IKlaRn9bL1ZlHZCJI-YQANoqJ2VQVEtyYq_aCytyPx69bRhUOBZTGAlfWuZcaNr5RP45V_cdTUtbuCsc5rlS9rM9UkGpFDZOps7QGg2UA7fE4FvsoWQ_4Skdq18MDv-lWTSU4bR9XjLgVmAf8zN9ZEjx7_KuSCXRbFBH95h9DU6nRmdaOUnh41NVHT2U2GxkkOliok4hNQPEVxWGXBNKw9fYHNFo4wvcLvIxg8M3yMhjZc_Hz3qXi5fM-IlERboJv2ywIb6anuOIjxakIQBYEIHJ185EwA-ppxowbwc43FEZ9awP6tCRwU10cj7YnjXpHn-4tE4g0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کسب اولین مدال کاروان دو و میدانی ایران
🔹
در رقابت‌های پرتاب دیسک مردان، صادق صمیمی با قرار گرفتن در جایگاه سوم، مدال برنز این ماده را از آن خود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/692646" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8613c2cb15.mp4?token=nDYmp7qww6aUpAVXw1vfai8GfbI-EehP_XiLoCHnPf_FSqPJSS3lU1qFp6-5zYJDji5Rk_tTQXr0APmW9Uuw9RT45y7mRsiv_kTlRanUZds4yic05P0UTtRrYUgYEsoRPcW3PM3iscSFH7hfiRjQbMPLaG_-gtWXd61957i1zwsbZpznHK5XZbFZ7Udv_0E086_Mo-v29F-kago7Ov_DyF2NoaBoZ4Jc7ZYdKfa-mS-WkHHxL4htUvOLzxygubvIYh9VW38xSrVZoFUPI6ySN-hKd8cfVEd17IWyEgsYL4zfvBdIbLSrP_9aThyHH5YTL0rrZIR7Xy8KT1lOTk22yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8613c2cb15.mp4?token=nDYmp7qww6aUpAVXw1vfai8GfbI-EehP_XiLoCHnPf_FSqPJSS3lU1qFp6-5zYJDji5Rk_tTQXr0APmW9Uuw9RT45y7mRsiv_kTlRanUZds4yic05P0UTtRrYUgYEsoRPcW3PM3iscSFH7hfiRjQbMPLaG_-gtWXd61957i1zwsbZpznHK5XZbFZ7Udv_0E086_Mo-v29F-kago7Ov_DyF2NoaBoZ4Jc7ZYdKfa-mS-WkHHxL4htUvOLzxygubvIYh9VW38xSrVZoFUPI6ySN-hKd8cfVEd17IWyEgsYL4zfvBdIbLSrP_9aThyHH5YTL0rrZIR7Xy8KT1lOTk22yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باهنر: مشکلی با سرمایه‌گذاری آمریکا در ایران نداریم
🔹
این حرف که می‌گویند باید استقلال اقتصادی داشته باشیم را قبول ندارم
🔹
اینکه سیم خاردار دور کشور بکشیم و بگوییم ما به هیچ چیز خارجی ها نیاز نداریم، حرف بی ربطی است/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/692645" target="_blank">📅 16:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وزیر ورزش و جوانان: وام ازدواج افزایش پیدا می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/692644" target="_blank">📅 16:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPbQNCYWDlPTxJplWg8BToqkuVEOuM2KJbQpQqE6oWH98Jr3WS6PoM0a90FJ6RaA6uiGKvZo7KvdhWCgW05uf1-jhyZJ40IhEPdy42M01wmgJ42TpNdr3edI8FWzgdDx-AuzdMByx1Cz0RyYb4Yuz00G6LHtYHBbZewS-haOrMHRVrPhtWySH68wGP2t85EcpkS0KkuYT09zS2_-sHl_pwYGYcvfu17VIlmzTzHfjUfdEOTf70NCZxj8yupE1P_jSEhgFR9T9ME9Cjgg9a1SxrXNT8EAX8crgRNPvGvmf5a0XoDWAvrIwsrd9CX4dIQntzGBeeK14GgXbwcOuskVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنده دیپلماسی دیجیتال در سازمان ملل چه کسی بود؛ ترامپ یا پزشکیان؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692643" target="_blank">📅 16:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEcnr4PxE_Z3gXYSWGIXq1Xt9FfXUOsLg5oOonyOWcR96XpFKvjUCmRT8d7ebaakRLncwdUZkBJVuYZ0opjh5yQXpa_7wDdxs4eDcnXmtVG_T3d5RQWlLl76vtQt0KPfWEtt80d0RFp1DOFQolCqF7T0pH_n0tI_tG9fBP8nBY8Wd_Z6LkkajPA5B4fmubQPCjd-sQt125X0leaIH9QKYo8QwvH84stLTw2SME-YUoIESmd-ob0rgPjYeR0lcP29S6Agmkn4h5yVTkTLuwwp3f7r3W4rrMfYz-ZnbYIGihBa9DEMSdzDivuF4Dzi7HnxISkDou1RvhqKxMIe7kN0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/692640" target="_blank">📅 16:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b0f5d9c3.mp4?token=ma6FFxt1KqWOZuKx6xhp6fcyygGSPdSaq71RJRFwl7uj2WAUypFDAMcUdoWIX-HZnlRr75UlDdlxrpyruzLP8n9txQrwxmNtQqN5VQK83XRHplFCu_mrirUpQmGjz1QH75rrIoQEXd4JZMj5zOK0C4Pge1Io6TC9yoz1ggTNirJaC8j6nhmSnQ1ZVzfQAmVYAtroxoDlVf_ZmP3FI41wq3VTKroJzWTGVGUuwaM8q6q7tYLcvtU8T68KpxMJa26lAaAE5TreLlfF9xB9r-W03JdbPuTKlJUiVzIii0t53Tv2bEO7xTf4nLfqcdIGvXSdZf8BWnSSm633-6uZ9eZs8zt8DMJq3fSLwlzjMlAmAuClvrcRY6lebHpYGD4g-oAKfzs27z0apcJPuBnmQdBxkU_fX_pY7ubVdRC2mtZBSbnXG_Vp-0ZeLEFZShKRWAVIlTlU9MH4r4aaEouBNQznlLpX2yY9Of1lI6_8Hv5PY7qVR8iXZxqdSbn_fFBxS6hzlgZC-iVZnz0boTWyxxbc6WX1AL7zM1RrgEETNInTL7qWstvvGeR-i5u3pHid-zGtg4obux2L8Rm73DHVu7TjbtoQdEax5MZrW4F8Ox-5Ioja0g1MPOUZ3q28vnLq0MVGs08D7C3Wgxem3aNFDjowKTR0ffToGpIT9vW04nW1US8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b0f5d9c3.mp4?token=ma6FFxt1KqWOZuKx6xhp6fcyygGSPdSaq71RJRFwl7uj2WAUypFDAMcUdoWIX-HZnlRr75UlDdlxrpyruzLP8n9txQrwxmNtQqN5VQK83XRHplFCu_mrirUpQmGjz1QH75rrIoQEXd4JZMj5zOK0C4Pge1Io6TC9yoz1ggTNirJaC8j6nhmSnQ1ZVzfQAmVYAtroxoDlVf_ZmP3FI41wq3VTKroJzWTGVGUuwaM8q6q7tYLcvtU8T68KpxMJa26lAaAE5TreLlfF9xB9r-W03JdbPuTKlJUiVzIii0t53Tv2bEO7xTf4nLfqcdIGvXSdZf8BWnSSm633-6uZ9eZs8zt8DMJq3fSLwlzjMlAmAuClvrcRY6lebHpYGD4g-oAKfzs27z0apcJPuBnmQdBxkU_fX_pY7ubVdRC2mtZBSbnXG_Vp-0ZeLEFZShKRWAVIlTlU9MH4r4aaEouBNQznlLpX2yY9Of1lI6_8Hv5PY7qVR8iXZxqdSbn_fFBxS6hzlgZC-iVZnz0boTWyxxbc6WX1AL7zM1RrgEETNInTL7qWstvvGeR-i5u3pHid-zGtg4obux2L8Rm73DHVu7TjbtoQdEax5MZrW4F8Ox-5Ioja0g1MPOUZ3q28vnLq0MVGs08D7C3Wgxem3aNFDjowKTR0ffToGpIT9vW04nW1US8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چارت شخصی من برای مدیریت دخل و خرج زندگیم که پیشنهاد میکنم شما هم استفاده کنید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/692639" target="_blank">📅 16:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3118c6bdd.mp4?token=hfzx_1vhUMVdMN55H7Gk3vmaxEcLKOnsi7lDol5DnkIFAgLqmDVeHIsaIPpYx9D57loiHXse0l4_kYv2Mhnvx6BD9HoNEeSMHWjNdKRZCESoBGdc7xbmvCsGHHBdmahc46FBD6fJ31FRoCb8Bo9nUdUzxigNMjBNdEsNrlFU4_zohPw39XuF7vamzzlt6N7Jqsoc8IVg6qtBClVj20xLAiQuPUOyp8vAGCSMvcxedUe75ZMotLERYFsnRx6PC8qBFh7obUW4Q4hmJ1cdOVx4yplcCGawdp9Cdp3oCm7TOL09LTXCczGy64mQXAPdj6dQLJMHX2OPdFfqRXHasqPjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3118c6bdd.mp4?token=hfzx_1vhUMVdMN55H7Gk3vmaxEcLKOnsi7lDol5DnkIFAgLqmDVeHIsaIPpYx9D57loiHXse0l4_kYv2Mhnvx6BD9HoNEeSMHWjNdKRZCESoBGdc7xbmvCsGHHBdmahc46FBD6fJ31FRoCb8Bo9nUdUzxigNMjBNdEsNrlFU4_zohPw39XuF7vamzzlt6N7Jqsoc8IVg6qtBClVj20xLAiQuPUOyp8vAGCSMvcxedUe75ZMotLERYFsnRx6PC8qBFh7obUW4Q4hmJ1cdOVx4yplcCGawdp9Cdp3oCm7TOL09LTXCczGy64mQXAPdj6dQLJMHX2OPdFfqRXHasqPjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند جدید اینستاگرام؛ ترکیب آهنگ‌های فرانسوی با دیالوگ‌های ماندگار و سنگین سریال‌های ایرانی، ویدئوهایی متفاوت و طنزآمیز ساخته که مورد توجه کاربران قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/692632" target="_blank">📅 15:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مشاور عالی رهبری: مرحله بعدی جنگ احتمالی تا اقیانوس هند گسترش پیدا می‌کند. در هر حال ما از یمنی‌ها دفاع می‌کنیم. سرنوشت ایران و یمن سرنوشت مشترکی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692631" target="_blank">📅 15:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS5566stZqp0o_mMs5bFvUYjb0DOXTkSMe-CgX-B_GsYyVe1hxOuCA5WVN85GYFmRHXaiveoC8cLPbpaGu0VXw0-Ti_4dAazvKdn1zx_-69Z2OzYsyrQJGnEjuRtaOQoYkOLIWSDEUUD835atYJlYU10NSDRMI2r3z6G5MFOWRVXdQd_DTA-PPAOK-FTHbkjfVAgc9992UIpe5W6zGmgd4aPZpg1PxkJxF7GbxMY9YDyC1BaSEBpDC73AgKBPbIOrSXFSLEWZBblHD9xCLDEmEkQ3UFcGFsi8VbjppgErrr8cPszrm_GIGUC2F_ad17hhMVJzZ0TfzvzvVpauM2vQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین سربازان اسیرشده کره شمالی را به کره جنوبی منتقل کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692630" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692628">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سمینار آبِ ناب مزدافر مؤمنی قسمت دوم</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/akhbarefori/692628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آبِ ناب؛ قسمت دوم
سخنران: مزادفر مومنی
🔹
02:20 عملکرد خطرساز دولت‌ها برای تصفیه آب
🔹
08:09 کلر موجود در آب چه بر سر انسان می‌آورد؟
🔹
14:00 عامل اصلی پیر شدن چیست؟
🔹
23:00 عوارض بطری پلاستیکی آب معدنی برای بدن
🔹
33:00 کمک به ۴ بیزینس جهانی با عادی سازی خرید آب معدنی در دنیا
🔹
قسمت اول
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/692628" target="_blank">📅 15:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692627">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqVsJc6OA_UL6KEzLd9QRiILvg1005-KoXUpBr_q5o2JthmD2e-KNDVZzhRavfKRU457_0drfMyrLVbTLOwSCiLkm3lnEN9lXKkd1RsxyANt3LNE531cf2_dvm3uPIyYqtFwBJVjtdVfan8oEKj65kBJGd6kRLuLXkOIyvwAbRkH5gh44bHRyJZtW2ldxkbzl-Wrh2DnA5zectMsKKSpAU7LWTKIh8sEa1E2aaXRAIPMygRTc0HNfmtIERpbHbgaRh1UaF13Pcv23h0yIs7QaULHkdXyAsQtuMtcGIE4mfFTwrC69my0tsm7kLlvd328NvD_QJW6qrRG8743xb_tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست عجیب «بیرانوند» برای بررسی پرونده پزشکی‌اش در کمیسیون اعصاب و روان
🔹
دروازه‌بان شماره یک تیم ملی و تراکتور، با هدف تعویق خدمت سربازی خود، درخواست تشکیل کمیسیون پزشکی به سازمان نظام وظیفه داده است.
🔹
طبق پیگیری‌ها اولین درخواست بیرانوند، ارجاع پرونده…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/692627" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692626">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48eff4f5c9.mp4?token=Imihf-adFrwXz-YMFUSZIMr7wN2Qjtk4-I_dfyWEsbW-emrS9Lgx3BlxzqkX44wLnaoLsbKnm7Qf-hAqCToSwdl9Ga-iQV4HI15FB89J5pZMJop0lBW3kzX-iFkn85G5YsWIfSk1gSLrCfKG2Lt_xkXOVjbwIei6MkzQUcrhnvRk9YhxkzxHaOwm0f2WFjnMWDnh7Pn3xH-UxpJEic__4OOLYc0ggZdQZteHifYXTAXSLOWqw8ING1GW9UTTf9SauCizG094MQIqD-QtJ4jdfAeDTDM6rKDDlIWqG4S5qiIFDzvn2r-oc3Yt3FOo7OWOslTVqYBe9zZ07Oyes2iK5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48eff4f5c9.mp4?token=Imihf-adFrwXz-YMFUSZIMr7wN2Qjtk4-I_dfyWEsbW-emrS9Lgx3BlxzqkX44wLnaoLsbKnm7Qf-hAqCToSwdl9Ga-iQV4HI15FB89J5pZMJop0lBW3kzX-iFkn85G5YsWIfSk1gSLrCfKG2Lt_xkXOVjbwIei6MkzQUcrhnvRk9YhxkzxHaOwm0f2WFjnMWDnh7Pn3xH-UxpJEic__4OOLYc0ggZdQZteHifYXTAXSLOWqw8ING1GW9UTTf9SauCizG094MQIqD-QtJ4jdfAeDTDM6rKDDlIWqG4S5qiIFDzvn2r-oc3Yt3FOo7OWOslTVqYBe9zZ07Oyes2iK5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«جانفدا» یعنی آماده‌بودن
🔹
آموزش نظامی و امدادی، از امداد و نجات تا کار با اسلحه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/692626" target="_blank">📅 15:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/545b2f488a.mp4?token=Hpm-L1JtnJdit3MaTcK5ciYze1iHAcyAv7DuBHcU42Z6QOG-homWEtQOKLyfmiq6ObWnT8JaQYvKSD7CAtk7wZKW0AIeOipfvMy8qCopdWOgtWTqC5yi3ZJbyLDurbfOCvl7hJKFV-WLKPVlcdt1soffq2onvr2HDxrkqnnIMPrBriEDoSGoWUklwoPRXJVpkiVrW0GzkrqE727OskfizKF2mR27K7tiCiJHgCZuj_ls5awXiQU2Pkx_c5V-EXliF-TFpsqp3LDu6oa-YXHuDfh_1Frh_0TgTwBnloGalY-Yn3v1_f9eDtyn3EsaoV7C7fRk3dijLGkuVzy0FTiqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/545b2f488a.mp4?token=Hpm-L1JtnJdit3MaTcK5ciYze1iHAcyAv7DuBHcU42Z6QOG-homWEtQOKLyfmiq6ObWnT8JaQYvKSD7CAtk7wZKW0AIeOipfvMy8qCopdWOgtWTqC5yi3ZJbyLDurbfOCvl7hJKFV-WLKPVlcdt1soffq2onvr2HDxrkqnnIMPrBriEDoSGoWUklwoPRXJVpkiVrW0GzkrqE727OskfizKF2mR27K7tiCiJHgCZuj_ls5awXiQU2Pkx_c5V-EXliF-TFpsqp3LDu6oa-YXHuDfh_1Frh_0TgTwBnloGalY-Yn3v1_f9eDtyn3EsaoV7C7fRk3dijLGkuVzy0FTiqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رضا پهلوی در مصاحبه با فاکس نیوز، از دولت ترامپ درخواست کرده تا به بهانه تجهیز طرفدارانش به سلاح، پول‌های بلوکه شده ایران را در اختیار وی قرار دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692625" target="_blank">📅 15:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvMYufEkmsXZazME0gj9UrzoiPRSbU6Czsmfu3prafafk4P5xAcZ9yl-cXS6d_qmQwDEyawgk3tNMGD7YYkK9o5j9ksvDDSStrL9B1YJCqAvCVLuMNcHh1FktTRs3-KkEYjVGcRxRXQvN6qreK-d9HvwJAwMH8oFS5cRPmLOyboNwRdz3v_3K0A-Z_DWzr5RXDBPMkwSm4chErcsvfQjEBiX4Fz5jqEyGyTestmNe_UUw7lVE2EeYK9wVYJZfyd-aLvKhSXZwLPULUk8dKU6TGTtMv6pZTT1WUmKieTpIjTPCSu89SFMBuca_2DUqL7wGxHv-0oiPK2qVP-TiGaPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
مراسم بزرگداشت و ترحیم عالم ربانی حضرت آیت‌الله العظمی شبیری زنجانی از سوی نماینده ولی‌فقیه در خراسان رضوی، تولیت آستان قدس رضوی، شورای عالی حوزه و مرکز مدیریت حوزه علمیه خراسان برگزار می‌شود
📅
زمان: پنج‌شنبه ۲ مهرماه
⏰
ساعت: ۱۸:۳۰
🕌
مکان: حرم مطهر رضوی، رواق امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692624" target="_blank">📅 15:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6401f529ff.mp4?token=vttL5EOLztOTTLhs4FJwhRvto7SAu3GHYX4imnPMEC-JWBMl-Zrykfhe9RMzupTk1tVb9mNXCNvklh4Ss9w1VgQxk7v0Uneyhu6sJ0tDgNRNCEdgPwBUnyKAuJt0z3D_8fSAFPUDdubGJ0FpJv5g2Shwqo28f5772SD7gA3FRQZyW4ukrJoZr5cOQ8WzrRWVcley3D1R_DNDs22J_X6wxrobuzdP_1rwwvLBh8IyeGG2R2Q11ot2NLVUilZnwcuW5hVTCQUxynbTvk7NeIOiNeHqhTcFZ92qO2YyNVsU1fg5w7zaNRMLI7sT8mg_CXQpleOrL0vhNBwSF37V3-cfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6401f529ff.mp4?token=vttL5EOLztOTTLhs4FJwhRvto7SAu3GHYX4imnPMEC-JWBMl-Zrykfhe9RMzupTk1tVb9mNXCNvklh4Ss9w1VgQxk7v0Uneyhu6sJ0tDgNRNCEdgPwBUnyKAuJt0z3D_8fSAFPUDdubGJ0FpJv5g2Shwqo28f5772SD7gA3FRQZyW4ukrJoZr5cOQ8WzrRWVcley3D1R_DNDs22J_X6wxrobuzdP_1rwwvLBh8IyeGG2R2Q11ot2NLVUilZnwcuW5hVTCQUxynbTvk7NeIOiNeHqhTcFZ92qO2YyNVsU1fg5w7zaNRMLI7sT8mg_CXQpleOrL0vhNBwSF37V3-cfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا یک مرد با وجود شکستگی استخوان می‌تواند راه برود، اما یک سرماخوردگی ساده می‌تواند او را کاملاً از پا بیندازد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/692623" target="_blank">📅 15:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc95917c1.mp4?token=VAJWk0XeDBSj-GKHJKbuc1yLksOP58RJUNcwME9ZNltrzyQznOhYrI0Dxl8mYM_BXOfYYuRHfg1ZcwWECkbNB4-d-SK7aD89E1qDKZc49I-t3DGAJC1TKzn6S_X-F4Sj0w9T3049d3N1XwJWJZcoY2CJHMrDgg6Uz1NdsYWHGWUSZw4spYWs1fyS5X2HCgUqmsEKjTmVcQMezkZ9R2otRjqCrzjNj4X1l8TQCYKGHRHbyOw_mzJIgFnxIZofMVLU0zyfYNUY3FJZPFWMvFHUDYEy7VbnOBfVxik04w8Li_mLlDOMfuW-njXapfIJGIpcxkHspvi2sUXOl8fA3o0X2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc95917c1.mp4?token=VAJWk0XeDBSj-GKHJKbuc1yLksOP58RJUNcwME9ZNltrzyQznOhYrI0Dxl8mYM_BXOfYYuRHfg1ZcwWECkbNB4-d-SK7aD89E1qDKZc49I-t3DGAJC1TKzn6S_X-F4Sj0w9T3049d3N1XwJWJZcoY2CJHMrDgg6Uz1NdsYWHGWUSZw4spYWs1fyS5X2HCgUqmsEKjTmVcQMezkZ9R2otRjqCrzjNj4X1l8TQCYKGHRHbyOw_mzJIgFnxIZofMVLU0zyfYNUY3FJZPFWMvFHUDYEy7VbnOBfVxik04w8Li_mLlDOMfuW-njXapfIJGIpcxkHspvi2sUXOl8fA3o0X2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو مربوط به آتش‌سوزی واحد مسکونی در منطقه برف‌فروشان شیراز در شامگاه چهارشنبه
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/692622" target="_blank">📅 14:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c1daed18.mp4?token=u73koGneiQH6fZNqWaKR93eAqvxRWs745sVoGEaM8sVYU4Z2multRdFudnCn110ATkPu9ddb1HwuPNtXekbIIYLguCsdBiWR3kpjYVPaAPDFNN1qOlVmmVZL7al-B8I3-5SfjjjIUezQbI7_MFT0okPD1j0xHyI7b2BuxCcQGAKo5jKfxhxxUcVNjlbWC3zaDV30UUWfqPDd7cMmpqHgma2lhzrzWwJUz4KSimn5aEavbi6JgcfxI-tg17yVj7cdbMlhEQWhfZ9PJ56jTsIz9f2DvEzGtJTj0uEPdBeAAE7nX9s0RnsJv0YziICGC9Ty_0Z5HRXaQLdxyfiD2RLMFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c1daed18.mp4?token=u73koGneiQH6fZNqWaKR93eAqvxRWs745sVoGEaM8sVYU4Z2multRdFudnCn110ATkPu9ddb1HwuPNtXekbIIYLguCsdBiWR3kpjYVPaAPDFNN1qOlVmmVZL7al-B8I3-5SfjjjIUezQbI7_MFT0okPD1j0xHyI7b2BuxCcQGAKo5jKfxhxxUcVNjlbWC3zaDV30UUWfqPDd7cMmpqHgma2lhzrzWwJUz4KSimn5aEavbi6JgcfxI-tg17yVj7cdbMlhEQWhfZ9PJ56jTsIz9f2DvEzGtJTj0uEPdBeAAE7nX9s0RnsJv0YziICGC9Ty_0Z5HRXaQLdxyfiD2RLMFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین زمان مصرف هر ویتامین برای جذب و اثربخشی بیشتر
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692621" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام علیه ایران مخالفت کرده اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692620" target="_blank">📅 14:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692618">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOtbz3RyXmUJq7MowhNeASIGAnRlBN47EpFI7-xlxsL3H5S6LaS9bc6KjKOd487sB_I2Eosln8BvVPnApJDL6LD_FJke1islqEc-P5Jw8EyLto3LkOcqaiL2MHr51gqtX1-coDOaxpbyAayTZXelXx8O6swb6eKPshVSVwMqIzXkBjDTFquPg9abjmzRT6Ywo6dvTKculD8SP1GfvfVxHs4TWubwxwspuDAUpQS2sq_n3wJNwSaRdRAQySZgZ3JtCCiXy106285B66B0hZ8dbpk7jLuJkPA05Nw7yJYw5cX7oe3V-xywBDf2p93gbqwmd58hCqAiQhdRjkw8Ghm2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwDHBR_jP7okvVDjaTkMeGLCqBsLKCRDAXJChyPyAIz-ZAz2-EM8gsyj2YXlvQKRE7BRpvJD-5ta0_qkcAP6NWCcIvKZFYrLm9RK95YHahORTpOYaVarUFzl97FpsxqUtBuWxyocQOr2PKO_0uQU5wmy_VoSb2-TT_Kz5bJM6nPi5IvGt_6wUwtXYvZO_uPhlSfpnjxbAPqnlLdFinSrSJaah7gP7wac7ov3z8vSHIDImyPMzg0NSoY17GVTOb9bPSM3MrxQdv1vqDpVF8d3yRzvt0VpWjfyOwnmSiWtoILX19WW4HO4yiPn2nPN_eNKPXMYxSyLejKZxaHGKop22A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عربستان سعودی باری دیگر مدعی شد که آژیر خطر در مکه به صدا درآمده است/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692618" target="_blank">📅 14:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692617">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c617ec332.mp4?token=rdXV4u7CLHUrn3xl5QaeGlOn9te-t1Sta9Ils8Ptzmc8B4AQgqqVS__25cHAsKYwXKwwogDGBr8sBEf85Idr9EgaeOVn3j7dOs-eWLHEPO7UCtYomTEJYTh46MhFMrn4r-oBrV8QhWziEVusWYbtVf-FJEK09DDYQg9Ft-nRx8CYPoMT9VZDlszFHRLxCz5Y59Kib0jGaA07XZNBHxQben4zRYr00yuhFpUFoKBsjUuwCIhXqOoGqffT26w4E0BFOmsL25EDSvlCFGBsNW8b9jh19oa-BMtxdWYZx5ZmZ1tmjRwRrhpvIxD7FBeg8_6HDYrwtHGrepHRprm12RGGqKDWCW5wfyN4KIJwCEOiKMja6h4D0XQAi038KNSnUVxC76Mu9JaF_N5gRDWvGFXwSpZ6pszijWdFUP9R34DEg76HOJUuIoRAkviC2jH0jLGvx6sIvCK-xjjjuK5iGDa561PMgxzgdxXFhFEE-2T9MySW9PF9Drx0eqAUQqNmUrB1HyRFJ1d2IeUOa6aD2UQ1RduN2ZO9kJSDr0BK15jvJ71oN3jnFSg737T6QoJ5A66V3oxAsQ5U-IvW-49UwYpv5ifqA8if4fcITd29LDPV7f37NrQi62D7ABC_E0Ws9deykIzFNZz2h3GEYCg5o1uLm4HhIl3G6GnX1TEXp3e6RfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c617ec332.mp4?token=rdXV4u7CLHUrn3xl5QaeGlOn9te-t1Sta9Ils8Ptzmc8B4AQgqqVS__25cHAsKYwXKwwogDGBr8sBEf85Idr9EgaeOVn3j7dOs-eWLHEPO7UCtYomTEJYTh46MhFMrn4r-oBrV8QhWziEVusWYbtVf-FJEK09DDYQg9Ft-nRx8CYPoMT9VZDlszFHRLxCz5Y59Kib0jGaA07XZNBHxQben4zRYr00yuhFpUFoKBsjUuwCIhXqOoGqffT26w4E0BFOmsL25EDSvlCFGBsNW8b9jh19oa-BMtxdWYZx5ZmZ1tmjRwRrhpvIxD7FBeg8_6HDYrwtHGrepHRprm12RGGqKDWCW5wfyN4KIJwCEOiKMja6h4D0XQAi038KNSnUVxC76Mu9JaF_N5gRDWvGFXwSpZ6pszijWdFUP9R34DEg76HOJUuIoRAkviC2jH0jLGvx6sIvCK-xjjjuK5iGDa561PMgxzgdxXFhFEE-2T9MySW9PF9Drx0eqAUQqNmUrB1HyRFJ1d2IeUOa6aD2UQ1RduN2ZO9kJSDr0BK15jvJ71oN3jnFSg737T6QoJ5A66V3oxAsQ5U-IvW-49UwYpv5ifqA8if4fcITd29LDPV7f37NrQi62D7ABC_E0Ws9deykIzFNZz2h3GEYCg5o1uLm4HhIl3G6GnX1TEXp3e6RfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیریم. بازپس‌گیری بحرین رویای نیروهای مسلح است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692617" target="_blank">📅 14:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692616">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e60806c9f.mp4?token=T4fUAp7NZFgYMF0MvNYfBwicZIH452RWtJBDB8uGQJrnWrgc9bp6VKxfvjnP80eDbH2al4JkHM0J8pmgOa2KYSR2kXAqPuovnYa0rKbwiqcxAuljvqRzrlXGGm9m6lWKZJ6GzDEZrVn5lmntp1q8eJ6IQV2z6SvkoExGPeyM20QO7lUeVZpMi3mRprZlg95J-y8idILRiti6E_vHnvdYdmyMVccx_nqX_WOmnVcPoLwOSbdhn8iqbO4bFGq0MBD5uNZ1bSetlJixnGGcljGeWrY8sVTwW_JKpHbt33GpVx6iZfDbVIm9GV-aWxedFuUOsobc14c4PDYJHx15N6LKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e60806c9f.mp4?token=T4fUAp7NZFgYMF0MvNYfBwicZIH452RWtJBDB8uGQJrnWrgc9bp6VKxfvjnP80eDbH2al4JkHM0J8pmgOa2KYSR2kXAqPuovnYa0rKbwiqcxAuljvqRzrlXGGm9m6lWKZJ6GzDEZrVn5lmntp1q8eJ6IQV2z6SvkoExGPeyM20QO7lUeVZpMi3mRprZlg95J-y8idILRiti6E_vHnvdYdmyMVccx_nqX_WOmnVcPoLwOSbdhn8iqbO4bFGq0MBD5uNZ1bSetlJixnGGcljGeWrY8sVTwW_JKpHbt33GpVx6iZfDbVIm9GV-aWxedFuUOsobc14c4PDYJHx15N6LKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی بسنت: ایران دیر یا زود مجبور به پذیرش توافق خواهد شد
وزیر خزانه‌داری آمریکا:
🔹
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آنها در نهایت تسلیم خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/692616" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0da167082.mp4?token=rYVXZX9MNBmYNz1d3L_Ulcoz3ppnbzJx18nVR2z4OF-BJfp0_44TIteGxTrtYbV-XLPp4i3gUNb9AN6GomAZb2qE8BRG3A02dbz_aTnD1CKuAWdYsOQvM50yAZ4w74C7mJw2IUskAhhx_TCpB0XRMz_qyh0tECFVvhlIghLRmqnWUgeQk4OtgCMVEx1npUx08QtV03vgqV2Hx10KGIPE4s5Bzxrcw-F6xSqkWgRqo0HtTTiSWyYd5kojczpDXULWbpcSAXdC1YqFeII9svK2rY_md-DAY9KVab04Gdvzcx5om87rUU4B7GhTqtrMTpCkw5n6p_qQp8NZ9y5nQEiZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0da167082.mp4?token=rYVXZX9MNBmYNz1d3L_Ulcoz3ppnbzJx18nVR2z4OF-BJfp0_44TIteGxTrtYbV-XLPp4i3gUNb9AN6GomAZb2qE8BRG3A02dbz_aTnD1CKuAWdYsOQvM50yAZ4w74C7mJw2IUskAhhx_TCpB0XRMz_qyh0tECFVvhlIghLRmqnWUgeQk4OtgCMVEx1npUx08QtV03vgqV2Hx10KGIPE4s5Bzxrcw-F6xSqkWgRqo0HtTTiSWyYd5kojczpDXULWbpcSAXdC1YqFeII9svK2rY_md-DAY9KVab04Gdvzcx5om87rUU4B7GhTqtrMTpCkw5n6p_qQp8NZ9y5nQEiZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی که در بین کاربران عرب با این عنوان، پربازدید شده است: کاری که سران عرب در کشور خود جرأت انجامش را ندارند، دو رئیس جمهور ایران در قلب آمریکا انجام دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/692615" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7640f9a454.mp4?token=BVYIzDwqkaQnAl_WCILBCzCOmvRtE2ydwUPrkiSbuW4HuQI1U9uLaFOFKpi1PU2zlBvKt48tyHl8KpUfJL4NUDJfodJSo4hNHhBQGgAsOwyqdi9e-dWHOZn9zeqtJU1d72Lq7LoqTggbE78BJbWhFit1EyWWlOfT15AE2uNy84JVVTEdSD2-iZiSH_0sOYPWnz-lIe5VchzFrQRh4Cror2i2CmB9PY4_7zUPGI8nMR3YNr8uxPVotLjzSOFa2PmGqso40FKbD98ggiNNU6MOVSB0-OGSClEozmaBbGWDY4nEZd1NKcm7n3IUZWAg2f0yWJRmPNGw1fVFaBA41b5Qgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7640f9a454.mp4?token=BVYIzDwqkaQnAl_WCILBCzCOmvRtE2ydwUPrkiSbuW4HuQI1U9uLaFOFKpi1PU2zlBvKt48tyHl8KpUfJL4NUDJfodJSo4hNHhBQGgAsOwyqdi9e-dWHOZn9zeqtJU1d72Lq7LoqTggbE78BJbWhFit1EyWWlOfT15AE2uNy84JVVTEdSD2-iZiSH_0sOYPWnz-lIe5VchzFrQRh4Cror2i2CmB9PY4_7zUPGI8nMR3YNr8uxPVotLjzSOFa2PmGqso40FKbD98ggiNNU6MOVSB0-OGSClEozmaBbGWDY4nEZd1NKcm7n3IUZWAg2f0yWJRmPNGw1fVFaBA41b5Qgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقره ژیمناست ایران در بازی‌های آسیایی
🥈
🔹
آرمان خدایی در فینال خرک حلقه بازی‌های آسیایی با امتیاز ۱۴.۵۶۶ به مدال نقره رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/692614" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b7e8145c.mp4?token=Dkd3RHLqatFbzNdTiqNFt4UERJYA_D601LOpU4vKXatOiWHYlxMphtTJOxmenDG8LOpIWWuEkw9jrsDPs7DjJiVAr3Ou-sKxaRlw9BkV6VZVKkniVg21bkNLT7LdU3c8zU5z9s-x-irAhxh46beT-V_ObeWP5IG8ssllLBDm3jbpNRo38JEpwD6HOeF4GlCzEhMFCZcZLxFaqZtigEDl4LFgZNMCsBrLtx69nnaFkbqQa_f0-tgPTyN_OjzG7FojkfGDc405YmwDId-5XsX1BXe6ShGrhNrX8l3Lbjil-IlvdCjItzg7CKZwyJRqUxPKMRYRV12YPLe79APEnNhreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b7e8145c.mp4?token=Dkd3RHLqatFbzNdTiqNFt4UERJYA_D601LOpU4vKXatOiWHYlxMphtTJOxmenDG8LOpIWWuEkw9jrsDPs7DjJiVAr3Ou-sKxaRlw9BkV6VZVKkniVg21bkNLT7LdU3c8zU5z9s-x-irAhxh46beT-V_ObeWP5IG8ssllLBDm3jbpNRo38JEpwD6HOeF4GlCzEhMFCZcZLxFaqZtigEDl4LFgZNMCsBrLtx69nnaFkbqQa_f0-tgPTyN_OjzG7FojkfGDc405YmwDId-5XsX1BXe6ShGrhNrX8l3Lbjil-IlvdCjItzg7CKZwyJRqUxPKMRYRV12YPLe79APEnNhreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه این نکات رو نمی‌دونی، کت‌و‌شلوار نپوش! #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/692612" target="_blank">📅 14:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت  دستیار و مشاور عالی فرمانده معظم کل قوا:
🔹
جمهوری اسلامی ایران به‌طور کامل «تنگه هرمز» را مدیریت و کنترل خواهد کرد.
🔹
ما و عمان به یک سازوکار برای مدیریت تنگه هرمز رسیدیم اما آمریکایی‌ها در این زمینه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692611" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
رسانه‌های عربی از شنیده شدن صدای انفجار در شهر جده و طائف در عربستان خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/692610" target="_blank">📅 14:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت
دستیار و مشاور عالی فرمانده معظم کل قوا:
🔹
جمهوری اسلامی ایران به‌طور کامل «تنگه هرمز» را مدیریت و کنترل خواهد کرد.
🔹
ما و عمان به یک سازوکار برای مدیریت تنگه هرمز رسیدیم اما آمریکایی‌ها در این زمینه کارشکنی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692609" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTDs70ywhHJmrfmkoVRHjM9_svqMKpq0nKDA2L-Fz1eJpC2nkYMx0IaAht5Qxw0mcC-5s5Nsp_x-tjJYo1yoWI1EBwoDhpRE6Hhu7avE-3W92shfV61Tg9BIQXTgvV-CpicUG0UzLKTNaOT8Rc4mSFjLutOE7ulR9hIRZDyeKQRXPRCbXDIK_a7Cz2e9bRbPPf1lJLy5Ii8AMkxx9ZUvLoUeNJ4HbnqDWRUer-sKWHxOxt7yeMfImV4fiPX0tXN9cyh2AH7mpPizMS7huWU3wLUFfWf4xBOMDDP8r3M_akcWDH9fG7eCVwOLflb9GVNhlYHCfndppuv58w4dHWpuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همتی: انگلیس روغن ریخته را نذر امام‌زاده کرد
🔹
رئیس بانک مرکزی در خصوص اقدام دولت انگلیس برای تشدید محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور، در همراهی با سیاست اقتصادی آمریکا، گفت: این همان مصداق روغن ریخته نذر امام‌زاده کردن خودمان است.
🔹
به نظر می‌رسد خزانه‌داری آمریکا در فشار اقتصادی به ایران به آخر خط رسیده باشد و کشورهای مختلف نیز برای نشان دادن همراهی و تبعیت خود از آمریکا، فعالیت بانک‌هایی را که بعضاً سال‌هاست در چارچوب تحریم آمریکا هیچ‌گونه عملیات بانکی در ارتباط با ایران ندارند، برای خوش‌آمد آمریکا مجدداً محدود کرده‌اند.
🔹
البته خود ما نیز برنامه داشتیم که برای کاهش هزینه بانک‌های غیرفعال در خارج از کشور، محدودیت‌هایی را بر آنها اعمال کنیم./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/692608" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692607">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
رسانه‌های عربی از شنیده شدن صدای انفجار در شهر جده و طائف در عربستان خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/692607" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFErbUp_Cskq7tTdgkGYKLGiXRSo_TE8m-VWN5E_H0LmUzlWr55gML7bkQ0-L6kFXLjwzFBSzhpkqR88sW3ubH7f8stOKoH-QmHOBVJYB0B9StxMJ6JYf3_jQM52HYftNlVGUZYE9C3rDOUJR8TSzlUpyk9mLNKFHL9kQ96vzB393X896YUkLc2ehUYk7avIbxWwoIvk-CLM1shbYpeVSNPcdhA2d4amsTBTHx4tG6A3uGY1zA8yT5efNWcQQBc1zLoGn4KRdwtfZVhxTr_sV7uQ1QArSP3wNpK8mWBjBTLWozwSIljKpKVbHvP-VrvPOc2UZUunyN1yq15nbw6xCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنکینگ تیم‌های ملی پیش از آغاز فیفادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/692606" target="_blank">📅 13:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قیمت گازوئیل در اروپا رکورد بی‌سابقه‌ای را ثبت کرد
🔹
میانگین قیمت گازوئیل در اتحادیه اروپا به ۲.۲۳ یورو در هر لیتر رسید.
🔹
دانمارک و فنلاند با ۲.۵۶ یورو در هر لیتر، گران‌ترین قیمت را بین کشورها دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692605" target="_blank">📅 13:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oI9VNw8M2GibwialaXXZf-rYsiqQvm5FjL7fo6m_bSLcpmQ-D6ToyLpJCwzeFJYMN1jaHNcWtzxZ0weziwjnJzq3osW4W34n0hhpj_KSOmw88PwHhieTgVVt3TNSfguFCCukGB-hLcfNRx03R_G3HZ8goyuJeiZ2_T7w6gMKCvUy-4FZfgdY1jozgAijkBEVxekfUhr5IaR5m0zhVMGe4bOw5s90ugdhIxoP8AsUE4aHMCi9uj6sVuqXpX96BpCW7k3-jom9N7UfJRe-kEZ6l7Aa7PWIrQScBr1O8SvwCg-tih2GbBl3DBplGEJDOeF7FvzvLPKbE-1dWahqvmI5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCQbRj-ZVlUyehgI6Qm1w0Z4Cviea81ALbCnVijnN8OcnK6Bzk6TuuPEBfcZkp-bbLcWpVHC08uz4li8W6-DOHHambB0biKGVr3LUSW_vFw4sHXu5DCFBPx0L15i7dNZSeF8L1P00i8JW_-5V8Idhx717JolBocqS5Z4iKVMKoQPiYcEMS7E_esr71WOpMA2TV_AmlIodxUj4v27gVILBrK--w_Ky9Q4EWKUNYEevpk9F36MFtrRZtI3aG79b_bFe5tecBIHfvRUT8TL1bzAnt5ww2mJ81p0PI0aMPu4wuSbrSq9_fbE9Cg6DRMLAq3DUut5TKV4D3PTSVqVYAophw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صدای شنیده شده در آبادان به دلیل نقص فنی در پالایشگاه بوده و در حال برطرف شدن است/ صداوسیما   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/692603" target="_blank">📅 13:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue9eGJ3lCZurJOdqi_8Q2Dk321r6DnQv1u1iFo8nODvkHbSj2NZrS7L9RoQv0iUe82I_o5ecB5bvJ8tWUQ70l4S4CSKiuRiWWzRCpK6EPmWm-itNZzoje-TVqYnpkRK_r5GGuIt5ncqmVkPDnVwwEM0TPHzymeWsvyasjUasGbYUUIbBxv5UJ3HkLj2k_GzG5wM94vptlw4gkaM1lHESctaCnaEym-sb-55NCLCobrDgciDn-oxmVJa31HQ7zB652fvnZf6ZS55sIYS3LuOuoTXi9vToSMya5KaGSHA3NLT6n65CZeo_fB5X1s8d8A9NCFL_PYdCiwFrc64rMF99FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/692602" target="_blank">📅 13:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mNU4sSpriTAFxcV2OVmGNRIAFYNIoOzQIki-VssLEXoIBOTrX5vCjHWS36t7vjX8Rmq3UbdAV3KN0Jpz4WX_tB9B3RNv6o8qUdV5vVCYLNWU2aJONZ-x0ce841iNjKUg_oGtrtAVlMDCVGJJrzm-VGtUxZSF-Pm2nJjoZu2toi7l2t1ctIxpTQM3RRPSMlb_4b2XVjb1Zth5w32_yPRePO3NVsZB8BaWH311LtmZG6AOSgD4qQ0tTwS-ZstgzH30PkO_ETMbictARMSuYK5J4356VRMygCs_c4c4RImAUcJO4gnJOyImlM8hvVwyOiFA4ipbSOUOuzzEZ-_YsH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💼
Work Mate | دفتر کار همراه شما
همه‌چیز برای یک روز کاری منظم، داخل یک کیف حرفه‌ای.
از جلسه و محل کار تا سفر؛ وسایلت همیشه مرتب، در دسترس و آماده استفاده‌اند.
✨
⚡️
پاوربانک ۸۰۰۰ میلی‌آمپرساعت
🔌
دارای کابل
Type-C و iOS
📱
هولدر موبایل
📋
تخته شاسی
برای یادداشت و جلسات
💳
جای کارت و مدارک
🗂
نظم‌دهنده لوازم و وسایل روزمره
🎁
انتخابی کاربردی برای استفاده شخصی یا یک هدیه متفاوت و حرفه‌ای.
💰
قیمت: ۶,۴۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/692601" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
زاکربرگ از گجت «Muse Charm» رونمایی کرد
🔹
مارک زاکربرگ در رویداد Meta Connect از «Muse Charm» رونمایی کرد؛ گجتی کوچک با بدنه نیمه‌شفاف و نمایشگر تمام‌صفحه که امکان گفت‌وگو با دستیار هوش مصنوعی را بدون نیاز به گوشی فراهم می‌کند.
🔹
متا قصد دارد عرضه محدود این محصول را پیش از تعطیلات کریسمس آغاز کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/692600" target="_blank">📅 13:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به یاد ۱۶۸ غائب امروز مدرسه
🔹
امروز، به یاد کودکان مظلوم میناب ۱۱۰۰ بسته تحصیلی به مناسبت یازدهمین سالروز تأسیس «خبرفوری» آماده و برای ارسال به جنوب کشور راهی شد.
🎒
❤️
🔹
۱۱ سال همراهی بهانه‌ای شد تا این‌بار سهمی از این جشن را با کودکان جنوب ایران قسمت کنیم؛…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/akhbarefori/692598" target="_blank">📅 13:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بانک مرکزی: صدور چک‌های رمزدار از سه‌شنبه ۷ مهر ۱۴۰۵ ممنوع و پذیرش این چک‌ها در سامانه چکاوک نیز از اول دی‌ماه متوقف خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692597" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دلیل بازگشت پرواز تهران - دوشنبه به فرودگاه امام(ره) اعلام شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
به دلیل اینکه ترکمنستان مجوز عبور ایرلاین‌های ایرانی را از آسمان خود صادر نکرد، پرواز تهران - دوشنبه نتوانست در مقصد فرود آید و ناچار شد به فرودگاه امام خمینی(ره)…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/692596" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از مدیرعامل شرکت آرامکوی عربستان: هرگونه اختلال در تأمین یا فعالیت‌های شرکت آرامکو را می‌توانیم «ظرف چند روز» برطرف کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/692595" target="_blank">📅 13:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c42c31b18.mp4?token=DxK0gepkOmQaJUPPQjfO4LK3ryz1fwuyo-gtkt3pSWjhtAokZ-fgMvK255Fugkqfe3sThd33V_z39iCxwJecG74wB-Cu4wjBPTCfiKXBrC8YP3AuQ9WzEJg3L6tZTxN8MrjNBzctDIkztwXa-B7LcRAyoPLzjUAYBhVPX5iTGiz02RTUyL9LsibqzDqAxJKv64eL2Vwk01MbClHmL-qGEzkFfIvtS4Wlg8Wwf8kdiWJEIjYFXLpD7LnRBnFEhxtF-5KEFJpcoPEELNltLJ1I4JNvEECyGBeIyV4VixYOJjBljbxgjW3TYrNndLrY6IxYGTSbMP6Z1w45invAvXR6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c42c31b18.mp4?token=DxK0gepkOmQaJUPPQjfO4LK3ryz1fwuyo-gtkt3pSWjhtAokZ-fgMvK255Fugkqfe3sThd33V_z39iCxwJecG74wB-Cu4wjBPTCfiKXBrC8YP3AuQ9WzEJg3L6tZTxN8MrjNBzctDIkztwXa-B7LcRAyoPLzjUAYBhVPX5iTGiz02RTUyL9LsibqzDqAxJKv64eL2Vwk01MbClHmL-qGEzkFfIvtS4Wlg8Wwf8kdiWJEIjYFXLpD7LnRBnFEhxtF-5KEFJpcoPEELNltLJ1I4JNvEECyGBeIyV4VixYOJjBljbxgjW3TYrNndLrY6IxYGTSbMP6Z1w45invAvXR6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش چین نسبت به تحریم‌های هوایی آمریکا علیه ایران: از تحریم‌ها پیروی نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692594" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پروازهای ایران-تاجیکستان لغو شد؟
🔹
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692593" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b277e5e789.mp4?token=qozOkR6ct76zNfb6ou_Sd5C2xR0r1NpNEGPevjNqEoiWCdHaboPHbM_2n7O0IuqiyzHlEnR3mv21XXKNhNa_UPex2s0yJCOV7h-J5hmig0HMPoiopZi0q-6IJH5wEr5FZuBMfyUep3C2sG14t0gb30wskrExknjsIhEt32if17TKt1SfqSjl8Znsc1Kam4YQFwie2olZ_mANRrN5Cg7Rbygu8ZffPYwjDxMEzWWpPKnpK4Ckd8Xo3p3L_7mTxp_QiRYGcrNhPrshAW2YFi1WifHFlZFXS0wJFcXfgKDxdYxOP65_z4qvio5Wrqs2vPyDcIHryEARd3k1IYmLgdfVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b277e5e789.mp4?token=qozOkR6ct76zNfb6ou_Sd5C2xR0r1NpNEGPevjNqEoiWCdHaboPHbM_2n7O0IuqiyzHlEnR3mv21XXKNhNa_UPex2s0yJCOV7h-J5hmig0HMPoiopZi0q-6IJH5wEr5FZuBMfyUep3C2sG14t0gb30wskrExknjsIhEt32if17TKt1SfqSjl8Znsc1Kam4YQFwie2olZ_mANRrN5Cg7Rbygu8ZffPYwjDxMEzWWpPKnpK4Ckd8Xo3p3L_7mTxp_QiRYGcrNhPrshAW2YFi1WifHFlZFXS0wJFcXfgKDxdYxOP65_z4qvio5Wrqs2vPyDcIHryEARd3k1IYmLgdfVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
آتش‌سوزی در زیرساخت برق آمریکا
🔹
منابع محلی پورتوریکو گزارش داده‌اند که بیش از ۲۱۷ هزار مشترک در چند منطقه این کشور دچار قطعی برق شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/692592" target="_blank">📅 12:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OC1EEZ0EiPRdTNOXuwIqWNe-V-N1D6CvModd7dZxPQm3-fG5F5V_F8hagY93zxkQbdy_R1ejgZ64D1W7j6G2Z2Tua5BdY7H-dE3U1Z5mVQmlu-afEJpa0s-VxH3nrzgmVY7v8wd1POeOdmg2z3cSbBKtPbXirWTh-5ZRV5m4YPVZyHe4b2VtzV2JlWwF0RKJDnUN_NH4CMFk12lTp9WJUfpqLOWBOtVbc6KJyLTBMg6Ej1TwwobYnnNGBqncxHIPi2KBJgKboPq7X41X_SYV65s8lcXGnzbBQ-sxHe4P0GoJBWPMV7dXeHyYyuNMU50TLMI7EF1T40fek1H9jTswEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSSID2GsJEpGShst_74UamxlZQLpYBGj-rKjtdTvi1o_82quiR2kxtcZFgz1BPrOuTK9CDbrL01hOu7HqX2wlFqUMDBS48etkzifPB0OBVp9bMzRjbSODvPzRpHRb-knqIOdSEsmXuWf5t4Ysyvvv1lVDq5bsk42wpiSc8Kr6C3gTHf6Mibo0nQOIj54V8QGSt7cQk3vPoG8SZp96SnCB89WH6OqMnptc4iyCHwunkFUJ0bs3DtUysPCk7ZM5qc_YbqXnCO5mNa4FujcT_qYyXIdkHqbBYwvl2rqxd4w2c1hxJfv6jgaKGlv5rvbheqE2PmeuPys5awDxCInfbCywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvgDlCtjtNtQNnq6j3H5drmPOoK5tsqynGdtNABF8A7psJsb6HSrlyrpZaBNMQIOYjFPV1rEQs915DFDtT-AWWJYk0_iYw_yW43QDjJbV0dN_5ZddVGyf2rvQjFAoeXQ7DFpbKuMQsB6zN4ZBeCKFD56MRqP2L4nzfNhUuLGmKdhpyf88hUuxp-rdn8-VrmXpHo9mO_EGhQ_PJK3AyhZzL33OMLrvaGfeSHw3RCvr4PpwzkJVroR7ARd4AGQLD25wgPceFCZ0isPqOEvgis-MBPj03xySe3sT_wFriUVbdUfReBN3eNz4bEI_aXca2wevtnMpwHDqj4MOe_-2biqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmpz874tEJf_FFtRva7XpNHQTjZiFR555u7hhnhXUxZYKSdeu7kAABrhin7ACBt1rrwh4K7roj0ZrlIbThpVbTB38JQBdGInqzDsKcNVTd0BxVeNjWPPTB1KtGMfye-hKnmCgJoXnJtYLAe_Mj_lLxs7MUu9fxDOHQA5hdYoDdYOVFaYwwUVulJk-rWWTdsUgd_fOwKIEBqJ56lp3AObol20BAZ4bn2dDVtFBr1g3iejSaMNZxftmD9XB3EqsXjX2fYUQbAu_5bHUitkRE0mZCE_06U97h3VeexZ-x0SQqpdwSHYcQ25takexEydMWAx2vwHlaC5RwxclN6BpRS1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxgxBu6wERzwdwpTrOlxm5ykBwkejvJfaPOdRTzfScoIA3NjNSdlBepB8ZSdpVNHVcBkvGrU0hpcHHPBHNYUi70_e4oNegnro79ZDcybDCQDhA7pCVSj23P7f8HH1skelmS-wqdn1C0-xy-FNCLUlSeEqBNVnpgdjrzqwVb7Ntn2kbqnvjJi-m4AOlRgCKgEcgJp3fRRujM7B5rhWDIOXqRrBjYjoCPEBjXqLqJ9iheMSQRpkSbbiMySF6mvARSAB-pkh48J0crpBXHeA3hIUX5rM6gvnX5uoJeJxRfpSD21joZKJ5rTQJ4VmdXh-8ie0glbi9Gi1YIb7WU_MQevIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2BP6MsSKH_DjCq3wGsVepFG2PtgCvW0aNIu6HMC_Z9qob672kqUaU2bDokKW78d99H_Akm9TGm0HwqGTFxyEwexjV-QjJv3zUTLLJXTjEA9UZ0tor5bIT_k1OpnzkeGexvqniF7NAB3403jGYT6pBPK57HmYNrkIe-24lK3JKv5kJ_uFT0VvC6wTrQPGnVQrUX-EIAhQSfDwGfqtlNgTCSHbGO3mky6yFNhNtXnKGUBIvScrcqfEsWlB_gHPUAHXIyAE6OqyBULKbnPaYGah-KSotIShOGH7EdW6RvtJ9zOZljvUuFCAnmVbAAFf9mB2KCdWvhtosTZo6LAzXzoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQRLL3iTMYIxOSWzGc05khOOL4uWXpu4YDTAhLms8QNmoLCJjhHHr4eFwp74cJnhYL9V-Wn1mDs1h4-nQAfntb_0NGrfnjG2JG5Il4uKJwycaNf8VNnBNTJNgsVKTJ2Hpssr5dJ9BnlQCDvC2SuMgQhR8pHek4Ix72QlXCvyfVgcrmtscppmHIqiaEh82mtuw5_69738cpVY_D9HVgslZHXgLNwEclilm3x6kzFR64Kuif0VzSM8mS10vSwETFG2iiY9M6Xyol8jZ8oEJlkvwnwOoIzUt450JEPonyaRvgd4AQlRAOL7C3n4oNw3Yi8rQdaPed_Rjo0Ikaxz0JZn1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هفت ترکیب عالی با گردو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/692584" target="_blank">📅 12:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692579">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ygjUSEqC2kz6TFKSEZX9S9FVsx3QkdaLf86felyaVY77UKllkANZB-AebAoZLGOP968rdHuDIwhUzMdjedyGGG9uFUUVAAN6sDNXDJgjNEjIcT9MfFS-5uR9JnWSCJJbxF-OzwxETT_R3P9w4ON9tj2Bs4Q_ovU5vM8eKphDen64t4qn7OEX2-5Qr1mJGqLJz8fLEvB-r7taBdIjyPCy2aw2q3YO83a4EdF4VJXiao-vJk32FQYkv-mJvNSa5Q_fgtNN2zIpZkGvWoQzJC8Ejb6RdpGNV0v0KuyX8miISzlFiSI_jrMF0F0SMCUxBmESmIcU4iME2Ln6KWrNPZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQl_tfLJ7ug9VgCUXwajEvNSm0_5WgNr0QEWGovtdCgYw-_JXhD4f2Lj3__4uiFblh8dzyKKkJXnWejsW6DSSevJA9pqfb3cBwjKhGkT48oakHd8aUjIyT-YN2GAwU3lfXRVT_DkY4EUJ13aFpRRHV3B3dUT5tEF47vicvoli_y3r0tr9pDa33FrtFIt0Nwp4vWyCWOsOb61S5XyHv4yfg1jY3mMLDtfHNyJcWd3jRwNLln0vIf5N4C1Apiqe1CEKajNhrJKjN243FhtKn-YoE7yCpq7dtWBwuAAKVpv7SHnWhib428l8aAjEHrdxwxI1WP6RUGuE1oV8N3wUcY1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYnBi4UXcrzppI5nTO57wbIrJG8eCLFDthRWv_bSqOVhEcUwYCDY2HJpmDLGyFv_ps5i04NKPLaEoYTaIxNBAOIanG0RDoOeON4SrGeiW6vDXVc2dXeH7MKcaGgsIrNv_yDcpdO0zjjWTWTnTOOhH-UlMC6MsG-sNtiq6DgwcAv0BOLmuihvuqn0GKFaky66nSzx9TDh_nAnoPAYkcS4jUIefkj2McNJcWEVDW8vElk3d2jAyWIk1HjyLPn6Fiuze7W_M168QO3EMXHJ_rF_JcAOow4_JLeLa1lrpVDMBQ9KF1RAmmcQEMRf2DjgLwpjJlQjsHKcqfDDgCEqQZKPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSUebb1V2CL7ls7qMYtu8h_rLjwJp1yCPD9AIpWf0-ooU4PxSRwQhgv5EgBF9p54TJTxf5azh58x7C-ZEto4ObG4lG5Zet2N-39MHN2-IbozUSPmDx5b8Kg0EqV2gS_B21T-sHobwm50CKqgfB9Z7kpQ86Ek0mRf6ZS7sbZE00WJfB34AyhqPZuyLc22BPlDuT-LD6trmjt6r0JGiauEXoadoREhrhf_vya7YTt5XORjRHNAbDlxdX_ouQyGD2GDWplB_7sSeC5UwOXlV4sBNzc1eiLA3lyRFd4Fokc0AQTBxJbCxNQrd44KP0bS1WffnXmwsrQBCoJ-HHJodXIzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4l3U3EYhmIkGuv1RXZGjYpHHNazrO4v4mShyrbqCChT-UPmYaqz7BLzN4ekvDPrgQXZU5Dqhocm9fUoxU1MTofxFi00Mbx8NmYfZYv1Cd5AZvxUCZ6tJlAlKJolW1j8BIq3Cv4tdW8dQLU6DSuCM24gSCv24hcnjhyMGH7SoDguzMadcSK5DNJ0-gqLG7b12BHm2Hg8LFhekh-cygoIUzqjYCV_H4Bk02QZ07I7QSyl8PRhT1tTSmQdKBXHBuEC-o_zDMtFhImE1D_4uz7o89vOQUrDQeYox7YjqEsExXHaKsOfuE8BOj8QFwvboEi--y47xWnVruR2X0tvq1lyMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افتتاح چهار پروژه مهم راهداری در جنوب سیستان و بلوچستان با حضور وزیر راه و شهرسازی
🔹
همزمان با سفر وزیر راه و شهرسازی به استان سیستان و بلوچستان، چهار پروژه شاخص راهداری جنوب این استان با هدف ارتقاء و تقویت زیرساخت‌های ارتباطی، بهبود کیفیت راه‌ها و اتصال مناطق روستایی در جنوب استان سیستان و بلوچستان به بهره‌برداری رسید.
🔹
در این آئین، پروژه‌های زیرسازی و آسفالت ۱۲۸ کیلومتر و بازگشایی ۱۲۴ کیلومتر راه روستایی، روکش آسفالت ۲۰۵ کیلومتر راه اصلی، فرعی و روستایی و احداث چهار دستگاه پل بزرگ با اعتبار بالغ بر ۴۰۰۰ میلیارد تومان به بهره‌برداری رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692579" target="_blank">📅 12:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=RQURD87EECCyF0x1TmL2ftTehXxIUgGZWAt145ca7VRO1lG1Pc5sOiaWWj-ZfUgrd1LBzugEMUhoyI3EI7iVD_CKb1PBTF0CIU13KrQz3WZM07p_rJBfkA9VOgXKgkvWXxjonuk9SDGzI2kbepAbkzYYuEe8ee2wVaFNony1BkILTZm0fkc-CIW7iQGSBdTDZ8GUBi6oae8yCAodTeZ1ZyQFuyCKlj0glqsbf5qvA-iLN5giQXkPmw59bcA8ElW07i2HsPiy7RWHe7J54BEhoQ3JP2VlsRbd4XTIX4ogWasJNsEAYrXaXm1FZSMRJN9WZKZrutbBsDGb7UFlkXOfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=RQURD87EECCyF0x1TmL2ftTehXxIUgGZWAt145ca7VRO1lG1Pc5sOiaWWj-ZfUgrd1LBzugEMUhoyI3EI7iVD_CKb1PBTF0CIU13KrQz3WZM07p_rJBfkA9VOgXKgkvWXxjonuk9SDGzI2kbepAbkzYYuEe8ee2wVaFNony1BkILTZm0fkc-CIW7iQGSBdTDZ8GUBi6oae8yCAodTeZ1ZyQFuyCKlj0glqsbf5qvA-iLN5giQXkPmw59bcA8ElW07i2HsPiy7RWHe7J54BEhoQ3JP2VlsRbd4XTIX4ogWasJNsEAYrXaXm1FZSMRJN9WZKZrutbBsDGb7UFlkXOfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طالبان و پاکستان درگیر شدند
🔹
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔹
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/692571" target="_blank">📅 12:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09492e061.mp4?token=i2n4voteqe_FusjW1H6oiEkgV-LOEyhoWavOOHdXyUPR3Oe2IXC_fFi2iLtUC4R0T7YeufSpOhq-sRy4WO8itgY5dezDFPoAsO0j82erUtD2RoMWcKiN-GsiAzawO178mHuOMuW5cQgDbF8EltnIhyTwErlyxq5KChdPMu1mV6q7k8DUusU0J1lqwTJTCjCseIKqt_UjwgsLE6_Wq-xcOonuCdrKcW76LplOKG0EbP4dV2JR23VFEuWXL5ruyIf4x7FIVcwj03hw85HWUuQoD23eFaV6w1nZEFx4YURCZ55pGjRlsNYse2jy91TrHj7rDlDnDOHxuyvl50XATcJN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09492e061.mp4?token=i2n4voteqe_FusjW1H6oiEkgV-LOEyhoWavOOHdXyUPR3Oe2IXC_fFi2iLtUC4R0T7YeufSpOhq-sRy4WO8itgY5dezDFPoAsO0j82erUtD2RoMWcKiN-GsiAzawO178mHuOMuW5cQgDbF8EltnIhyTwErlyxq5KChdPMu1mV6q7k8DUusU0J1lqwTJTCjCseIKqt_UjwgsLE6_Wq-xcOonuCdrKcW76LplOKG0EbP4dV2JR23VFEuWXL5ruyIf4x7FIVcwj03hw85HWUuQoD23eFaV6w1nZEFx4YURCZ55pGjRlsNYse2jy91TrHj7rDlDnDOHxuyvl50XATcJN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب از تردد گله گوسفندان در یک بزرگراه در یکی از شهرهای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/692570" target="_blank">📅 12:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-4sR2wqPVYcASUoE9dy6Jle_tqYRI2xZ9TW_1w-z7vRlqe73B5d2Daj9DOtWF3KcT10sE8rcmJ5D5ZMkdWmDQp8S0MBs366YY4xT8yUtNASZc1IWiuQQaYC3x2Xs9wiMXQIT8eKPEfTUn8bMvnHLJSIdx8AIktDGcn0tAe3w0g6EDMsu8w17Gr3DXUYra9cpULqlnM_X30gFOFPlPw0a2poxsBLEUf5EJfdc7szNnZbjrik0PYT5p2yZaUkYBq9YjOFV7HHAlBEAvkdZ0EdjP9EujuLUh83L_KOPu1tRWDf7mukrobRcr0hYVUwkCIHRcPyi3hTQiBR3w9UgbcoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت از ۱۰۵ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/692569" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692564">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p51x1wDJ-NxwVzeN3F_nimt030vpwcj77VYbiDriXNXSZY3J-b9Lg79RcMpvTXvxyxe3yVt9bRNunKiDzXP2zDS3UwY524akQ3KJ2KJU4VRgAcOWnU9mJ8YITm3vLA5B8C3W9HhuGOWTh5gi9WFT_MwO9d5vWizSrY1To_nQfW0osJzBE2Xthrp38CVCSBsIU0LkyDKicRHatDZGhbfzAfAi-WZDz_9Uiwqz89Ojkxhx--XBaysA4qJYYRYkeW_V73N2D2m2Y4AhZ2GpqKHnAK0JWNjo3RJ_CQjR5mLrfVtu3ERClDe5mxJvK2PLFGVDux68VZk0TSsTzKrqKDQkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692564" target="_blank">📅 12:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e00a628a.mp4?token=DsX6-1HhqMNQb1PrO1HaP0wOxZlYgiT7W9jKMReveTNNJEV90y10LYyczazbinHiDQPSEK07ajVZB79iDueFHXBYhCX1iNYqa8sb4D-0HUpEOesDaFlLu2vOWtEjtvUEtGXr-8lyEP6A6Tw49uxYZyxnkitgfB2V-ft0nibEf1hwAv5QoOYLUMmkKIrZAkqiwxSEdR_EEM7Ad_KrkUU486T5y1d7VsfgmsOfpBfFqzYebJSKwRPFAbRyZNGDDaLc8h-IG_Y5_hkXoTYbmO_BGNwR51SpJYb3pqZPTkIDqcw0dxo5-JA4W943x4Ogt48pLk9s5JG-rlmWjh3vGv4TYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e00a628a.mp4?token=DsX6-1HhqMNQb1PrO1HaP0wOxZlYgiT7W9jKMReveTNNJEV90y10LYyczazbinHiDQPSEK07ajVZB79iDueFHXBYhCX1iNYqa8sb4D-0HUpEOesDaFlLu2vOWtEjtvUEtGXr-8lyEP6A6Tw49uxYZyxnkitgfB2V-ft0nibEf1hwAv5QoOYLUMmkKIrZAkqiwxSEdR_EEM7Ad_KrkUU486T5y1d7VsfgmsOfpBfFqzYebJSKwRPFAbRyZNGDDaLc8h-IG_Y5_hkXoTYbmO_BGNwR51SpJYb3pqZPTkIDqcw0dxo5-JA4W943x4Ogt48pLk9s5JG-rlmWjh3vGv4TYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به هر دلیلی با همسرتون بحث کردید، حق ندارید پای خانواده و ترومای‌ کودکیش رو وسط بکشید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692562" target="_blank">📅 12:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db64b5a4.mp4?token=LtSx-h8n1TO7sNjUg1DL2H5bGX41mNPdmQUcsw5nLrLQ1evLvXQRDU1UaRpm-2O0lDyXWfDrlACCTgXurVMNbUfPvcR97y0l28qU8RKsVx3JRvnQG7XwEKBb41aM3cgmITY4N3ZCZJwotqBSLxSFBm2GTUy2QMl8Sru4cbPOZ9asi3lvQE195wrve9yfZrYZwIpDzAypSJED5vSJgt40LUtEfl2Qj8iDi1feU6mO-x-wCjjmdhkKo1p_VcucrJ63bksZ3bxAzZkDrA5RS0HgyeF_n-d0RYhUX_EEcbMHcM0tNOXHPpHCGGfwYqY7dI-AufLUzAoP0iw4NoLcg7qFH3-2ozAwSDgsGW2R2Q6nW2F2UyAjPtHopKMiSDyGqVT6rOT_t0qZ0PDhAM6TpfhuKf-EuzYR8fptgVNP4-pMsxZ4vehgGkMBcFRFlTIy5ad7iL7aotYpFr3OKOgcfDl3YRA3W2TTJZP_Ot4ya5pXXFXW_ZZBIEUD3YQC-vvLwzLwNqqRIpX0qgfBANjuDNau94XrJ80_8_AydSvTqg35lvwrjIKOD9KrxiuxSUTmhJqk_rXZ1hIcbGSkQ2p1W4SPFAlfR-boxLqd1xzJpfbQufRd1zJO6QNGO2WkrHeDkvTPTijZGeI3xAHqBQArX6-V5uwVaQFQ1j3WCYt8mOu0QYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db64b5a4.mp4?token=LtSx-h8n1TO7sNjUg1DL2H5bGX41mNPdmQUcsw5nLrLQ1evLvXQRDU1UaRpm-2O0lDyXWfDrlACCTgXurVMNbUfPvcR97y0l28qU8RKsVx3JRvnQG7XwEKBb41aM3cgmITY4N3ZCZJwotqBSLxSFBm2GTUy2QMl8Sru4cbPOZ9asi3lvQE195wrve9yfZrYZwIpDzAypSJED5vSJgt40LUtEfl2Qj8iDi1feU6mO-x-wCjjmdhkKo1p_VcucrJ63bksZ3bxAzZkDrA5RS0HgyeF_n-d0RYhUX_EEcbMHcM0tNOXHPpHCGGfwYqY7dI-AufLUzAoP0iw4NoLcg7qFH3-2ozAwSDgsGW2R2Q6nW2F2UyAjPtHopKMiSDyGqVT6rOT_t0qZ0PDhAM6TpfhuKf-EuzYR8fptgVNP4-pMsxZ4vehgGkMBcFRFlTIy5ad7iL7aotYpFr3OKOgcfDl3YRA3W2TTJZP_Ot4ya5pXXFXW_ZZBIEUD3YQC-vvLwzLwNqqRIpX0qgfBANjuDNau94XrJ80_8_AydSvTqg35lvwrjIKOD9KrxiuxSUTmhJqk_rXZ1hIcbGSkQ2p1W4SPFAlfR-boxLqd1xzJpfbQufRd1zJO6QNGO2WkrHeDkvTPTijZGeI3xAHqBQArX6-V5uwVaQFQ1j3WCYt8mOu0QYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروازهای ایران-تاجیکستان لغو شد؟
🔹
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692558" target="_blank">📅 11:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ef4b9caf.mp4?token=BRaA9-z1lMZIRXFVUG-YO75jEX5AMfNII0RGB3fQwBLO18rbAdhvUvWzqj_4x1M4afdPchmD2Pme3JQ41-78A4bZSQjDwT2LcVE9yS4QV4AUaZ0lQ8q2ew2BniVhiH7JOj6j1rkBfkI77nMYFGH7BkulqGwqigALGE5WK7h-ZMWd7lGH2DoociUF2uf_lwvO92Kd9G2P6EMgCvgd74cWT_F4VKcxMlrcGfse2kW2Pj4pJrgOUJ5MKYUUegrc26tCQmIcaAapGYNwCmbDo4V0hloAa6ufDnSSJ_wIX_3LqTROgkD7aDbMZpTetrzm6LY_wasU9uJSTrk-6rwpHXBveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ef4b9caf.mp4?token=BRaA9-z1lMZIRXFVUG-YO75jEX5AMfNII0RGB3fQwBLO18rbAdhvUvWzqj_4x1M4afdPchmD2Pme3JQ41-78A4bZSQjDwT2LcVE9yS4QV4AUaZ0lQ8q2ew2BniVhiH7JOj6j1rkBfkI77nMYFGH7BkulqGwqigALGE5WK7h-ZMWd7lGH2DoociUF2uf_lwvO92Kd9G2P6EMgCvgd74cWT_F4VKcxMlrcGfse2kW2Pj4pJrgOUJ5MKYUUegrc26tCQmIcaAapGYNwCmbDo4V0hloAa6ufDnSSJ_wIX_3LqTROgkD7aDbMZpTetrzm6LY_wasU9uJSTrk-6rwpHXBveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دندان‌های عقل چرا باید کشیده شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692557" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNcWfqyTqLL-qMo1_P2IikeRJ7VZG8kxeGSZanYE5mKtrxpTjOCRekUmBTaL8XHuCVKNCLnl9NVnh_8hgDSl5mTGQMyLE3EaP9aRiCCrGbxcU1E9m4XUWGrw0GsDNz07JX_tswZpce9_46Ut73xtB1xbAAotElSr4DLILU5l4drU2Cdpf1-8QCt3d0LuoZIhjD7lwrNtQi5fIt6mdEL7k_VCcBdANVP9NqhgsMfMtzPXIn1vULG8kRspm9WaxxNSiCHWaqAuuMYwkcGWaL_rgrnQKJTj99cAC5nTxRU2OUXKAcqnDq7NP7lPUhSQWQVZawgkzgqiTQ66A94ul0D6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: پیام ایران از تریبون سازمان ملل روشن بود: دکترین دفاعی ایران تغییر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/692556" target="_blank">📅 11:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آکسیوس: مذاکرات ایران و آمریکا در نیویورک غیرمستقیم بود
🔹
آکسیوس گزارش داد مقام‌های ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل، حدود سه ساعت از طریق میانجی‌ها مذاکره کردند.
🔹
همزمان، یک مقام ارشد ایرانی به رویترز گفت تهران در صورت کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران، می‌تواند تنگه هرمز را ظرف یک هفته بازگشایی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/692555" target="_blank">📅 11:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f8034866.mp4?token=WLgEcJTp0jArIMC2iRNlk4FgDFm4TzeaaOuqLQz5lI7s01GdjgRo6g_uUjkhsHKQd4xzHzUUcAv4gpCXHh8Q8sCpjjWPmnYj99ai3JkRIFT0T5ICtThVKRmBpoJscGthfJIFCrmzHXoC6xIRnmHHhqOjlue2swb9Zfdg4buI3TlN1juodWD1C7M18X-14w95oAGFJaAb-0pN03I8x0T0peYZblBqnQXeCAcKtts8GrlvXygjjTfCclsmPoddA9ehhbJQKRFLKlZKONVCPu_y5gPDLSzjJsGG_NQ8hFdr6TnuLSUf2rlcbY096EKhfxBih68ZEDFzvmZKQ3OJUHnqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f8034866.mp4?token=WLgEcJTp0jArIMC2iRNlk4FgDFm4TzeaaOuqLQz5lI7s01GdjgRo6g_uUjkhsHKQd4xzHzUUcAv4gpCXHh8Q8sCpjjWPmnYj99ai3JkRIFT0T5ICtThVKRmBpoJscGthfJIFCrmzHXoC6xIRnmHHhqOjlue2swb9Zfdg4buI3TlN1juodWD1C7M18X-14w95oAGFJaAb-0pN03I8x0T0peYZblBqnQXeCAcKtts8GrlvXygjjTfCclsmPoddA9ehhbJQKRFLKlZKONVCPu_y5gPDLSzjJsGG_NQ8hFdr6TnuLSUf2rlcbY096EKhfxBih68ZEDFzvmZKQ3OJUHnqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف‌های تلخ شهرام قائدی: وظیفه بازیگر حضور در یک شو و ملق زدن نیست؛ ما مجبور می‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692554" target="_blank">📅 11:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbea335ba.mp4?token=Zt1idZeBVh8Bw4S7lM3UJMwnJK7EiqxIrw64BIEKssrV2ls17cnD0PRv_cDYg8vkuEYuyzYn6RMI1dHvLC_5_KtX0tEpn9cdai0oUSYEAgEziKzvxVql4tFdDOZPO7VqIgsDc7NlLjGTbmScAU8e8akIA4uLcvdi-sh6CVnpmX_a0h9bi5Wimn9pSY6S0a9w9wQ66rMVY17se9vu63-G39NItVEyZOmQ3vTkeklDwXjQj63mK0oH6XWpHyXmfbNfLeCgMp6Xumo5zpdNaKq8XnYxZkUu0LJs3cuDZNzL69Q4MHkLSNulQmBGmqQ53sQFVPlgSoLcmJcW9_aotRbYHqmR3uMj8Bw75sLtgcBhKHpBjTSD5B-wOWPxYUyMfxGqoeWoxXIHy4ZcaNJJRT1liaDZ_1O8ozKt_jmrvuwC3OImASEODdepf4e0S5Z_8HFxJTPL9DPg0-W4OP41uNn3yjyhVqNFIx6pS0xfKcLzlNLpKtLwo-4u95h_kZCXR5KNf7UF3XnyJq8LboAxMli5kyc3wvuW8BmQC5qXRN8FB24H782I1piil6WaqTstVNWCT1Z_GQmmtNK1cbj9fe7d5Rkm7XwaeA-Rdm4jT3Z7UJP9oUhxlyn8RjHfQI38cAavGshDnLoohCWE3qJKWhA3k8wuEdotoAJdpyAbH7HZCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbea335ba.mp4?token=Zt1idZeBVh8Bw4S7lM3UJMwnJK7EiqxIrw64BIEKssrV2ls17cnD0PRv_cDYg8vkuEYuyzYn6RMI1dHvLC_5_KtX0tEpn9cdai0oUSYEAgEziKzvxVql4tFdDOZPO7VqIgsDc7NlLjGTbmScAU8e8akIA4uLcvdi-sh6CVnpmX_a0h9bi5Wimn9pSY6S0a9w9wQ66rMVY17se9vu63-G39NItVEyZOmQ3vTkeklDwXjQj63mK0oH6XWpHyXmfbNfLeCgMp6Xumo5zpdNaKq8XnYxZkUu0LJs3cuDZNzL69Q4MHkLSNulQmBGmqQ53sQFVPlgSoLcmJcW9_aotRbYHqmR3uMj8Bw75sLtgcBhKHpBjTSD5B-wOWPxYUyMfxGqoeWoxXIHy4ZcaNJJRT1liaDZ_1O8ozKt_jmrvuwC3OImASEODdepf4e0S5Z_8HFxJTPL9DPg0-W4OP41uNn3yjyhVqNFIx6pS0xfKcLzlNLpKtLwo-4u95h_kZCXR5KNf7UF3XnyJq8LboAxMli5kyc3wvuW8BmQC5qXRN8FB24H782I1piil6WaqTstVNWCT1Z_GQmmtNK1cbj9fe7d5Rkm7XwaeA-Rdm4jT3Z7UJP9oUhxlyn8RjHfQI38cAavGshDnLoohCWE3qJKWhA3k8wuEdotoAJdpyAbH7HZCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌
عصبانیت رسانه‌های فارسی‌زبان خارج نشین از سخنرانی پزشکیان در سازمان ملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/692553" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJFWyZpr0kVB2VH7kh1Jn-NdgDEJMdOn-HyIeYvcFlLz7Fkk5NJckVfxtGEzeM-RozcS1zj25psFxeSiBSbtXEHgNuW9ZQCtedKx4wCUoodwsHEUcbRUrydobuQ5IpeOohR7IRBNVP0ltqGSzBT2GkVexfNMNV6_WGNrLOSBv98BRv4CHZ09JtB-UEBQU8bjGdo0mdBbpI6KIe0MXKOWAk6xLnx6pNr_M0cR5JTh0sAXhmyTtQyb4NQ4oMLYDHVN0xjSkguf0xzvhOkDLqj6IF199m1Kn7kVOtYYyFK1d75yAHFFa2SOH7PsFPQe4nl9w9wrDm7Wvu-BmOXPyEwACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هشدار: مراقب کلاهبرداران رمرارز در دنیای مجازی باشید!
🔹
رایج‌ترین کلاهبرداری‌های دنیای رمزارز را بشناسید تا طعمه شیادان نشوید.
🎥
برای مشاهده ویدئوی آموزشی و دسترسی به محتوای کامل، وارد
«مدار»
شوید:
https://t.me/+0AFRVmShGBMzNDc0
https://t.me/+0AFRVmShGBMzNDc0</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692552" target="_blank">📅 11:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmhNrP3XiueMX-4KUaShk-QbAyby2LzafDriDOYykRqpsnO7TrU-Fdp4usRuTKGzF341LrQIQKHdVGv3jg4CvOdeMJVCT8gHG-MVl-4EdUjEJRK_hYFfvNBLCWGetALwvG9qs4sVfLfqZ7pH5ZwbluwI12W2he3efJyX2LOcMcNU5ChLmXdd0WvaHA7XmUfajnlnlzUFmlE7T20hldvhooeaGkZ4-RxWnslfw9s6DDGKWsfLEUqfXs8YsmHmYH5rVYR-5ITPVId7IljTnRcp7X9jaJRJx4WYn1Po5mPPF9b-czhRJtIlCtH-yq1JnXdSRGMyRxXUwqWa3Mv-EqdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ ظریف به توهین‌های ترامپ علیه ایران و تمجید از صحبت‌های پزشکیان
🔹
«قلدر کل» اجلاس مجمع عمومی ملل متحد را با میدان جنگ عصر حجر اشتباه گرفت و تهدید کرد که مادر همه جنایات جنگی را با «نابود کردن» یک ملت مرتکب خواهد شد.
🔹
پزشکیان در پاسخ، سخنرانی از پیش آماده‌شده‌اش را کنار گذاشت تا به جهان بگوید: ایران همیشه آماده دیپلماسی است اما هرگز ایرانی‌ها را تهدید نکن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692551" target="_blank">📅 11:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ترامپ و نتانیاهو دیدار نمی‌کنند
🔹
تحلیلگران، علت این موضوع را نگرانی ترامپ از کاهش محبوبیت و ریزش آرای جمهوری‌خواهان عنوان کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692550" target="_blank">📅 11:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692549">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0bfPIR0dYmtahh4hWIo5NGsKjjoLmKWLsYrH-zXhOW-V_HvO675O73KuiHgwDFbma9L8ZdmGSRc8KBxqz-ff2EtXq7cR2MYkT5UL841WT1OOHqdx95kqdnuAKF4TNbM05IxW40PlqIyeOtdDHl80eMDLrRGnJZdjevtH2BobpuPMQpyPH9rXx9sY_48vaoV_lUS3TfoUYBklXmSRUOy7OkYDcabdgcig1McEd3Bw_Tr_63xZLoQSarGYRgUAb963S-fUguJaZJ606KSsp0MU3mZy_NY2Yt6hdsH32y-D1V8ukQFYJ-6nWqIPA_p5ZegtSQjZPHg2Br0ITYmED28hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/692549" target="_blank">📅 11:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692548">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه چهارم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692548" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه چهارم؛ جایگاه حقیقی
🔹
انسان باید از خداوند درخواست کند که او را در مدار «حق الهی» که آمیخته با رحمت و فضل پروردگار است، قرار دهد.
🔹
کسی که در نام
«الْحَقّ»
پروردگار قرار دارد، از لرزش و تردید آزاد است و تحت حمایت الهی قرار می‌گیرد.
🔹
انسان باید بیش از هر سخن یا تصمیمی، نام «الْحَقّ» را بر زبان آورد تا نیت و گفتار او از باطل و لجاجت پاک شود.
🔹
در دورانی که تشخیص درست از نادرست دشوار است، تمسک به نام مبارک الْحَقّ باعث شفافیت بصیرت و تشخیص منجی از دجال می‌شود.
🔹
بزرگترین خطر برای فرد حق‌جو، گرفتار شدن در «غرورِ حق‌جانبی» است.
🔹
مسیر حق روشن و بدون ابهام است؛ در حالی که باطل همیشه با دودلی و وسواس همراه است.
🔹
اگر انسان باور داشته باشد که مسیر زندگی‌اش تحت نظارت نام مبارک الشَّهید و بر مدار الْحَقّ است، حتی سختی‌ها را بخشی از فرآیند رسیدن به جایگاه درست خود می‌بیند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692548" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692547">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692547" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692546">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0685d6b2b5.mp4?token=WOV0lo2cKHEsPpXhN2KN8Z7redlS_dkWRoYuH2faCmkSt6x7PNC7IUXReF1nNAVMbxIwimoP0Oqvf6b3N4Xyu7Whc5klYb9yWvEaA2UE4Vmso8G1PnCWza8QmHzPyrx5dRqZEI9__Wl2gFI5bzE-iypwyJTrkMkdmsLwX2_m7CSmjUvETErVXyNQ7EKI-CMYrTxnqZ-moRfddFYkWmIB9OQqHDzClPO3LhhTDOIs66Xqd9Jb2NNvno30wVsLNp4VdJIX4hTKX2Z6DV-XAqjEAX5gDqY9GowCw6F_B0m6X93xkKpoCXfZ4e2N2xhbx5kKDQrHD6dlYIWlYxXr8JDTEpbV3XwuRaDdQ39ql49_Bj6iDLwBNQfUr_ohYX1woZ6NozgnIaTeQ5jods5rh5u9WaWYhmGwN6i5N2Wcf5D5VFaAqOoWtRKxI-ciG1AR193VyrC7PXXPfx7Gz3ZVqJhV-UPPuMuJpzDBLQWQeZHmjnBquECOQYDoKj2c-n5D5-T2CAB-EDnuNMwm8Mg-5XrTj3KBu1r38D_Nkj_ALVHr72v-xDkwrSRHtqLftBgwavpLSjVyBXq0rH_oeeFDg2PAND03nLPOLSmwN9Ey-USGCQa_QURsTpYCjI_UjtmyQBHv2QYvLOs76etOnMNmmov9qvxpLXOsC1ta5BWya6lpnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0685d6b2b5.mp4?token=WOV0lo2cKHEsPpXhN2KN8Z7redlS_dkWRoYuH2faCmkSt6x7PNC7IUXReF1nNAVMbxIwimoP0Oqvf6b3N4Xyu7Whc5klYb9yWvEaA2UE4Vmso8G1PnCWza8QmHzPyrx5dRqZEI9__Wl2gFI5bzE-iypwyJTrkMkdmsLwX2_m7CSmjUvETErVXyNQ7EKI-CMYrTxnqZ-moRfddFYkWmIB9OQqHDzClPO3LhhTDOIs66Xqd9Jb2NNvno30wVsLNp4VdJIX4hTKX2Z6DV-XAqjEAX5gDqY9GowCw6F_B0m6X93xkKpoCXfZ4e2N2xhbx5kKDQrHD6dlYIWlYxXr8JDTEpbV3XwuRaDdQ39ql49_Bj6iDLwBNQfUr_ohYX1woZ6NozgnIaTeQ5jods5rh5u9WaWYhmGwN6i5N2Wcf5D5VFaAqOoWtRKxI-ciG1AR193VyrC7PXXPfx7Gz3ZVqJhV-UPPuMuJpzDBLQWQeZHmjnBquECOQYDoKj2c-n5D5-T2CAB-EDnuNMwm8Mg-5XrTj3KBu1r38D_Nkj_ALVHr72v-xDkwrSRHtqLftBgwavpLSjVyBXq0rH_oeeFDg2PAND03nLPOLSmwN9Ey-USGCQa_QURsTpYCjI_UjtmyQBHv2QYvLOs76etOnMNmmov9qvxpLXOsC1ta5BWya6lpnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با آبیاری قطره‌ای دشت‌ها خشک‌تر شدند؟
کامران داوری، پژوهشگر محيط زيست:
🔹
در برنامه سوم توسعه گفتند راندمان آبیاری را ۲۵درصد بالا ببرید تا مصرف آب کم شود؛ با عجله آبیاری تحت‌فشار آوردند، اما غافل از اینکه راندمان بالا یعنی کاهش نفوذ آب به عمق زمین و توسعه سطح زیرکشت؛ راندمان بالا رفت، اما مصرف آبخوان‌ها بیشتر شد!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/692546" target="_blank">📅 11:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692544">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fheSDogYwddIHlAFMFxJF9Z5IwtintLvhJy84GhSsywJBZjly6yWapJJRMdVICPvb8AVWQt3W6zluZURVxla8WVrogb0_LtQ9jrcphIKlDW43d-QgrTT8w7QRmHxLd2gYIB1vpD80U7ixnqagmxovK5Evz7r18SMngPjAOOUJ77geXRaW-WIbA8a_Af3ZnOljM_YRRGw1nAdjur4CB1EhNzjn98vfgnttws4jxe_E3TkiGu20CkPq3uHlyjLupPoD_a_XB0THGr4GYBeAi261R4zMS7pfUds2NbTiaV_sEwRUXyVG0KsodAMA62KyOEaLaWW19DGoTxpvRoN1wSImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jE9IGTBZSXYvWAGRCQPlDObB_N6bP83WnxIwo_1WZVDCRn6ZGImPQIPMOIzcta-0upbGQHIOLUCXo00iWdCqi_7Ne4LD6pDUc5kvzOnZQQAd1rcVqbksXb_MO8B7FkMme2Ugr56RbiMTsJgY9pFA3rOQUcMtBWw8lvUxdL7jysL3zRNJTbECibePleJ1ZomL6QBTvvroSVPpGOfJFK7tjXr0L9vDtaEm-vNKpd6Oo8mf6SeAM4ZAJgBLNpViZ60WQ61qUZ55AWNXwnoFCtY2BNkjuDZ_Xcl144yuoA6tB5GQiQ8Zt4vatT0AyBiNJe0zA8X8bzRJoSRNqAZ7-TAsqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشاهده افراد مشکوک نزدیک محل اقامت نتانیاهو در نیویورک
🔹
پلیس نیویورک از مشاهده سه مرد ناشناس خبر داد که بامداد امروز از یک چاه فاضلاب در نزدیکی هتلی که نتانیاهو قرار است در آن اقامت داشته باشد، خارج شدند.
🔹
این افراد با دو خودرو از محل گریختند و پلیس اعلام کرد به‌دلیل حساسیت محل و برگزاری مجمع عمومی سازمان ملل، بررسی‌های امنیتی بیشتری با همکاری نهادهای فدرال در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692544" target="_blank">📅 10:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692543">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اسقاط ناوگان فرسوده در ۳ کلانشهر در اولویت قرار گرفت
🔹
تهران، مشهد و اصفهان در اولویت نوسازی ناوگان فرسوده قرار گرفتند؛ موتورسیکلت‌های فرسوده و تاکسی‌ها در اولویت هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/692543" target="_blank">📅 10:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692542">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون درمان وزیر بهداشت: افزایش تعرفه‌ها در بیمارستان‌های دولتی منتفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/692542" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692541">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
طلای جهانی از رشد بیشتر بازماند
🔹
قیمت طلای جهانی در معاملات پنجشنبه تغییر چندانی نداشت؛ هر اونس طلای نقدی با اندکی تغییر ۴۲۹۱ دلار و ۴۸ سنت معامله شد و طلای آتی آمریکا نیز با ۰.۲ درصد افزایش به ۴۳۲۶ دلار و ۳۰ سنت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/692541" target="_blank">📅 10:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBDVQhB5HJofOVwEaJ_CIjsrWQjuPgJ4fvhX_rV5xPb2ZvfQiBUs85eYm5Y_wfbD_XUk7saDcWP9jMn_9BWa7KQ6HlrPzUSHmVKy9pUoPHJjeZrmNjPGZZuSVM2pxl9EP6Aiwg489oLdv7DWRkWKFnVpNojV7s93X1QFUKdSGpxHaJHaGZTAIJk7Ntp2y78k0EZWI62ItOECYEIwigNWpT9nH4DVcYuNAmJ_5il8SA07jHZ7oNUs9X4AApLaw3p9eTohyB4-Cf412a3b5yWBIeEMfOiqqHVEIleWky73aZRiq3qjxcVrIl9kIQwRbIfp_aeOMO4oj7ls_jCbjQGBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا ۶ میلیون بشکه نفت ایران را دزدید
تانکرترکرز:
🔹
نزدیک به ۶ میلیون بشکه نفت خام ایران به ارزش ۶۰۰ میلیون دلار که پیش‌تر توقیف شده بود، به‌صورت بی‌سروصدا در حال عبور از اقیانوس اطلس به مقصد آمریکا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/692539" target="_blank">📅 10:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
با اين مرینیت مرغ، حتی اگر هر روز هم مرغ بخوری ازش خسته نمی‌شی
😋
مواد لازم:
🔹
ماست یونانی ۶ قاشق
🔹
سرکه بالزامیک ۳ قاشق
🔹
روغن زیتون ۵ قاشق
🔹
رب گوجه ۲ قاشق
🔹
سیر ۴ حبه
🔹
نمک و فلفل‌سیاه
🔹
پول بیبر و فلفل قرمز
🔹
پودر سیر و رزماری
🔹
ادویه‌کاری زردچوبه
🔹
تخم گشنیز…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/692538" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04b0043c.mp4?token=NJd28weoARVj7Y2LeKfMOgzGkGdN-WM0XOnTtmrPitoE0Lq_ikZUe01wqL-TSPSeiLg-jVbBs8WmBE6npXMmHomo9TI-4fY5t1smC265TaOKG110HawMLJKoXIjVOtYpmuzBdiUqInPi-RmTQYgrB5L6h5KD1VeY8DWPz80DKImGHpzOqAWeEhh_GIT-xbcOXKIXtDiucx7uDFY7epsAbJQGm4gYiCiMQXkE2urTZHF6esaIOdfz86Zr9FAbwRrsu0JptVxeWoQ-QOr2IgpDHg_CEsSHcLaOk9h-rBr82VCHKRySLu4YqNKf69QztabgYkQShc3Jm_CCNOeI7mvYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04b0043c.mp4?token=NJd28weoARVj7Y2LeKfMOgzGkGdN-WM0XOnTtmrPitoE0Lq_ikZUe01wqL-TSPSeiLg-jVbBs8WmBE6npXMmHomo9TI-4fY5t1smC265TaOKG110HawMLJKoXIjVOtYpmuzBdiUqInPi-RmTQYgrB5L6h5KD1VeY8DWPz80DKImGHpzOqAWeEhh_GIT-xbcOXKIXtDiucx7uDFY7epsAbJQGm4gYiCiMQXkE2urTZHF6esaIOdfz86Zr9FAbwRrsu0JptVxeWoQ-QOr2IgpDHg_CEsSHcLaOk9h-rBr82VCHKRySLu4YqNKf69QztabgYkQShc3Jm_CCNOeI7mvYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متا از عینک واقعیت مجازی جدیدش رونمایی کرد
🥽
🔹
متا از Meta VR Glasses رونمایی کرد؛ عینک واقعیت مجازی حدود ۱۰۰ گرمی که برای تماشای فیلم، سرگرمی و ارتباطات طراحی شده و به نمایشگر 5K با پشتیبانی از Dolby Vision و صدای Dolby Atmos مجهز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/692536" target="_blank">📅 09:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
صدای شنیده شده در آبادان به دلیل نقص فنی در پالایشگاه بوده و در حال برطرف شدن است/ صداوسیما
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692535" target="_blank">📅 09:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
حقوق کارگران چند روز کفاف زندگی را می‌دهد؟
رئیس اتحادیه پیشکسوتان جامعه کارگری:
🔹
افزایش دستمزد ابتدای سال تنها حدود ۲۳ روز پاسخگوی نیازهای کارگران بود، اما اکنون این میزان به کمتر از ۱۰ روز رسیده، بنابراین موضوع بازنگری در دستمزد کارگران ضروری به نظر می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/692534" target="_blank">📅 09:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a17886d44.mp4?token=Unz3EDMKAx5z7F8bExuLQWYXN-eGynT4T_3Lvs2AUMtmjazBHNWkeVn8MrdnHlZwP_ClZOczA3qSV4P66CIKH5Ml2WA3-MjNJlw5JmSajpJDUfFXh9G83DAX04ZYmOXwYhpoXtaRuoGDzHCcNz65BMgAUGmeIdAptJNArp5LC3quKntrflzcAr0Kp1c0I6-7sUp7uiVBNSJC2iDFyBx9bmGizOvIHippOQsQFkwXag9ourG2MfwPE1FkI0iUfwUquN21fu_3sr9ueStdEo8lpOxHSwHl2a1FgPUwnnI6UEH_uLZXqI8dBstIp8rWCsZhFiA_MabWHdxxDJkgmOo-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a17886d44.mp4?token=Unz3EDMKAx5z7F8bExuLQWYXN-eGynT4T_3Lvs2AUMtmjazBHNWkeVn8MrdnHlZwP_ClZOczA3qSV4P66CIKH5Ml2WA3-MjNJlw5JmSajpJDUfFXh9G83DAX04ZYmOXwYhpoXtaRuoGDzHCcNz65BMgAUGmeIdAptJNArp5LC3quKntrflzcAr0Kp1c0I6-7sUp7uiVBNSJC2iDFyBx9bmGizOvIHippOQsQFkwXag9ourG2MfwPE1FkI0iUfwUquN21fu_3sr9ueStdEo8lpOxHSwHl2a1FgPUwnnI6UEH_uLZXqI8dBstIp8rWCsZhFiA_MabWHdxxDJkgmOo-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر ارواح!
🔹
تصاویر عجیب از بخش تمام اتوماتیک بندر شانگهای چین.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/692533" target="_blank">📅 09:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
روز پُرمدال کاروان ایران
🥇
🥈
🔹
ورزشکاران ایران در رقابت‌های آسیایی موفق به کسب ۳ مدال طلا و ۴ مدال نقره شدند؛ فاطمه مجلل، کیمیا زارعی و زینب نوروزی و سهیل موسوی طلا گرفتند و سوگند سینکایی، شجاع پناهی، عرفان محرمی و تیم روئینگ چهار نفره زنان به مدال نقره…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/692532" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر صبح این ۵ حرکت رو در دو ست ۲۰تایی تکرار کن تا یک روز پر انرژی رو شروع کنی
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/692531" target="_blank">📅 09:07 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
