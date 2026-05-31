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
<img src="https://cdn4.telesco.pe/file/OaS3uoQ9MA3zcDhwryMZ7vZ9wwqovitJoW-SLG8y2uQoxCx6VpDv6WskDf2vJt-Kxl7Gbx3nuCUcjS0GvsUez4gGK-3rzXRDOYWfYJaSCem6AubDqD7Vme9DsBw3qa2qo3XPM686ntk7XeRRspD7tVGgNeOkjNMLqDm3cZaDeoEydfYkq6eHA8aF3zxVnAKGtSJ3WNeiaREpsavvqpCp2oWatBfsAkTRsErDX1KqFg3MWWLNW7Le6gt7uksJphxWuXAONDvRBy6asIKWoY2jV2MyW0ABhgQ8fGM2zHryQe5tC2e8WqPbe2fzb1F6IPU5T6l8qZKT8DB0zR-DwzV4pQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=FeM0dpG5xP6nmvd4uQygcutB8VNADPOvNncLjV-ikfTtolV6fYrzw_5xaDFed7QRssCZuDMGqr5CQg02tc4wvpdP7IBw9fpTPdcPIgD78Un2_ga8Wnbnl4wzlXP1hPHvFeQ-U34Z09OWLdsFx0j4jpQn22ZO7yYgLUFHN2GhtWMHti1AwAlF5nLkRReVQsbKn9APhh24FqJOEvDX6iMdp8azi5Np_PqPIrtxdVwbFoLzUCT8ZsJVXu1q3fQLORQWVhFIX-4oCVMaJu1emEv2QBEPJgGRMzqYtjL1B53e4Qi19hGYbZEuCoGxVl9YjyVFfiCl39jyDyjQvJZlhcBkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=FeM0dpG5xP6nmvd4uQygcutB8VNADPOvNncLjV-ikfTtolV6fYrzw_5xaDFed7QRssCZuDMGqr5CQg02tc4wvpdP7IBw9fpTPdcPIgD78Un2_ga8Wnbnl4wzlXP1hPHvFeQ-U34Z09OWLdsFx0j4jpQn22ZO7yYgLUFHN2GhtWMHti1AwAlF5nLkRReVQsbKn9APhh24FqJOEvDX6iMdp8azi5Np_PqPIrtxdVwbFoLzUCT8ZsJVXu1q3fQLORQWVhFIX-4oCVMaJu1emEv2QBEPJgGRMzqYtjL1B53e4Qi19hGYbZEuCoGxVl9YjyVFfiCl39jyDyjQvJZlhcBkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوس بازی‌های قبل ازدواج لامین‌یامال و دوس‌دخترش که در فضای مجازی وایرال شده. فک کنید ده روزه دیگه بازی داره زیدش هم اینجوری میذاره دهنش
🙁
😔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/90551" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEjC5g-VbbfK7Z27_N2dzxZQOodhGCVm7fdRLU9AoTajvWyH4JE31PAQomcaPfe78om9kN0-4MnziYiUgvtb4J24lDExOPq9en79oV41Mvtf8qy6lsBfj8yMIadwKuPR9PDi1qViT0aYbYS-1eUQC7v5oeg9SIzVjBkwJU7pzIl3hlaW-wtyHYZWT2aseoay-a0ZQ-Is2QpIu5NQf1oR5sJq1C2GAofkOID9jRMAPm5WU8zgSkUvVxi12nDkc9TeRDsJYFN7hVp_wgIDjY2fMSWn6HuXQM7IQd4nz978NPAk0ugb-fZ8dsQd5uRxQrEKDNhAb4pHZ_FACDcmm6v1WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ روزنامه‌ اکیپ فرانسه مدعی شد که ناصرالخلیفی به مارکینیوش پیشنهاد داده که بعد از جام‌جهانی به تیم الدحیل قطر ملحق شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/Futball180TV/90550" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHLft1j3pHXjwKpdfhFMpSzTZP4_kWNZeOquJbr4bOtuXcRuLSHib1APDrKYI2NHCsUlAAiLugX_FE--b-iTs4TfGm08Evxo1og6f8rfeIQixAZV7sFOjcomTB_QlkU3O9yHf8_ol6981REk1bnWsjI9dX5gRHcl_VDe-NOrT56NCAD5gh76gow5V1ZqBOAcmdqYId5xg_H5qL9WevzHsM2mNf_KWF6Ev69pjUvfjgBrsI5O-wKo9TVYihqgyvORBLaTc0M8z4d9fScmwzJteP37bqSL0MojEZMUoKQDTLUN5hg5wc0Lo6L1GibyHlb-KBkgyhXLs9EasioNxwZpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبال آقای امباپه رو مشاهده می‌کنید:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/90549" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4b2a728b.mp4?token=FPt82SFJQURFnBi7KNcLyQjbe2WxqNVhJerOwhlfzaG91xbmPii4ROavzwYcwtxggHXaHKyyRdA1v84xFWmvbu3qPQsRRtWo4ppOmvysEXMwxM7eAEoK2j8ngRp4Aj5dEVSYsDPAecI_AsTX2KVTUpoxkYL9WsAHUXQrCkN1oVV0AFzEeXN4OiRSCpqZVGwA4a2p_i_j53CX99BOWRoQerezeqi0pLN0VsxBhkUM35ik28d9dURAHuGHCwsJF1wTTaLgLpLs_xDz4mVxFkAPRf1GEbp4XvlzrXQD_PyWQMYqZRiNBkmFD200r7hglXxEYdksTlqzXTBtfsMESbJYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4b2a728b.mp4?token=FPt82SFJQURFnBi7KNcLyQjbe2WxqNVhJerOwhlfzaG91xbmPii4ROavzwYcwtxggHXaHKyyRdA1v84xFWmvbu3qPQsRRtWo4ppOmvysEXMwxM7eAEoK2j8ngRp4Aj5dEVSYsDPAecI_AsTX2KVTUpoxkYL9WsAHUXQrCkN1oVV0AFzEeXN4OiRSCpqZVGwA4a2p_i_j53CX99BOWRoQerezeqi0pLN0VsxBhkUM35ik28d9dURAHuGHCwsJF1wTTaLgLpLs_xDz4mVxFkAPRf1GEbp4XvlzrXQD_PyWQMYqZRiNBkmFD200r7hglXxEYdksTlqzXTBtfsMESbJYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از خیابون‌های فرانسه، هوادارا داشتن فینال چمپیونزلیگ رو از تلویزیون نگاه میکردن؛
بعد یه هوادارِ لاشی درست موقع پنالتی زدن گابریل، تلویزیون رو سریع خاموش کرد
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90548" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskmWuqm72wFhKsdUy13R4kTyiSttYTZ73ez1TrR_ARfnN-5oiFLqWk77i6wGog9G5utzI-pHstQXcUxKmFYXoodfa8_Xr5QwN-Lxhh9FcHDaG02rijzEfEVXpBRmLpD7e9920MvoCKEuWaTqNqM8Tt6cuzLF6cNaZC4LWHHsBPYetdseUiJtPx2erLA7A0J8xLbC41Tt-zBMPVLP9nTXSM0j_LGugS_pGWrEADLoQ-2K9kdh1_NG5nnQuBMei68gN6o_8yj5hsXFvUqXthryRCQEsF8jENhMR1wFXvQpuREwYVcwUKbx96n8Bgs5HLMtNq8ksULGR50Zvu71O13uU6Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskmWuqm72wFhKsdUy13R4kTyiSttYTZ73ez1TrR_ARfnN-5oiFLqWk77i6wGog9G5utzI-pHstQXcUxKmFYXoodfa8_Xr5QwN-Lxhh9FcHDaG02rijzEfEVXpBRmLpD7e9920MvoCKEuWaTqNqM8Tt6cuzLF6cNaZC4LWHHsBPYetdseUiJtPx2erLA7A0J8xLbC41Tt-zBMPVLP9nTXSM0j_LGugS_pGWrEADLoQ-2K9kdh1_NG5nnQuBMei68gN6o_8yj5hsXFvUqXthryRCQEsF8jENhMR1wFXvQpuREwYVcwUKbx96n8Bgs5HLMtNq8ksULGR50Zvu71O13uU6Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکا اومده یه ویدیو گذاشته از اقدامات سریع در حین فینال دیشب و جمع‌آوری صحنه کنسرت قبل شروع بازی در کمتر از ۲ دقیقه
حالا این سرعت رو مقایسه کنید با پریمیرلیگ جذاب ایران که خدا میدونه همین‌رو چقدر طولش میدن تا جمع کنن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90547" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👀
لحظه دیوانه‌وار قهرمانی پاری‌سن‌ژرمن در ورزشگاه خانگی در پاریس؛ دقیقا استارت آشوب دیشب تو پاریس از همین جا بوده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/90546" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO8uqxLzCnV3FLmph8c8F8BkNVaCx2GKvYG-yZvkZdIW2pFL0lf7UClKkQ94YU6odWn1lCLJlJ2xzY9NxnhPxBkWuWQtwT8qYl2XihdAGGdTrgKOOL1-c5alM3jz2X0zoTvc0SgcuLnhbruowgbwC_dOOym8WIo1yE4NfdXOqN5h6gc2UtNiRjxEKhBaMx220LbVIc2l0tW-a7kjjx5eQlXIWxmdbaa-m7IDCF_eGIAPVGX4MF3l8dlBSIjrPQXuKl01JRg2vyfvinxVjEomP34LbyU89VDg7HV6RtXB4hjD6Hh-ZqHS83kaTDVugcN2zjsUTkNP57RQiVRQx3FrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرکاپ اروپا
استون ویلا Vs پاریسن ژرمن
22 مرداد
آر‌ بی آرنا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/90545" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=USNOIbCWKDsFiq6pOFpM5789jAViSo2ePYoyRs_rMQ9Ufm2lo4V1BZMEcR4rIhr6__gft6ChAIGZZS1u4Ly5L6a7_jg4Eiv7gDqAlEQupvucReDKq5trwFxewpHIEj1Vi6IbnmiNOcA1snnUZuoz2N90ZLO-OQuoEeQYEYaJNUnLFpd0dfMl97kLP-78-I-NGtEQEatgh7KfUy3wSOiSGyXjbETkiUi-5rAoydd-htH0Vk_fG27nYYVmlVsizdxRlW1OUdoYLOnHiDtNle0le_vXVSO7h84d4vM8WQXOhqFudDTmj85s8ekma_MBYOmInDWN7bVlkR4gfZKUhfB-NIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=USNOIbCWKDsFiq6pOFpM5789jAViSo2ePYoyRs_rMQ9Ufm2lo4V1BZMEcR4rIhr6__gft6ChAIGZZS1u4Ly5L6a7_jg4Eiv7gDqAlEQupvucReDKq5trwFxewpHIEj1Vi6IbnmiNOcA1snnUZuoz2N90ZLO-OQuoEeQYEYaJNUnLFpd0dfMl97kLP-78-I-NGtEQEatgh7KfUy3wSOiSGyXjbETkiUi-5rAoydd-htH0Vk_fG27nYYVmlVsizdxRlW1OUdoYLOnHiDtNle0le_vXVSO7h84d4vM8WQXOhqFudDTmj85s8ekma_MBYOmInDWN7bVlkR4gfZKUhfB-NIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو هم تو فضای مجازی دست به دست میشه از این بلاگری که قبل خراب شدن پنالتی دیشب گابریل، میگه توپ گل نشده و پاریس قهرمان شده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90544" target="_blank">📅 11:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔵
عاشقانه‌های بازیکنان psg با زن و بچه هاشون بعد فینال دیشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90543" target="_blank">📅 11:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=ha0pvnrbVxMIQAETNkIiWPl_gwbTZt36BaRaI_EI-2d7bWKwHUnNz8xhPa5i3rupD-npWy9qa-4kXnzVRnV1QCVkJWxVqXFDPx3E_-_ysnuJ8NIzfEp-x49wMvR7UB9tIKr6JRfJkVoVW1Fp36W5j2adFTP04y2tz1HOrW15M6vTuR5uYmnGkVc3FlucugPxstI6UcjtjcQeWiq7zd0irT_jIBysB3S3sGGqFzYNznaTSbXWRJIRzeHvqICV9CRjQ08-eUXuhqFUIAXc_--kY0T6uFU7v6aUHGrFXu4-fjxTfAwDrXEFTlOvgg6ngZP9FI54NVflvngkNaU9CWjiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=ha0pvnrbVxMIQAETNkIiWPl_gwbTZt36BaRaI_EI-2d7bWKwHUnNz8xhPa5i3rupD-npWy9qa-4kXnzVRnV1QCVkJWxVqXFDPx3E_-_ysnuJ8NIzfEp-x49wMvR7UB9tIKr6JRfJkVoVW1Fp36W5j2adFTP04y2tz1HOrW15M6vTuR5uYmnGkVc3FlucugPxstI6UcjtjcQeWiq7zd0irT_jIBysB3S3sGGqFzYNznaTSbXWRJIRzeHvqICV9CRjQ08-eUXuhqFUIAXc_--kY0T6uFU7v6aUHGrFXu4-fjxTfAwDrXEFTlOvgg6ngZP9FI54NVflvngkNaU9CWjiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های انگلیسی از این واکنش دیشب رایا وسط پنالتی‌ها پشماشون ریخته و عملا گفتن این گلر کسخل مسخل از کجا آوردید که قبل زدن ضربه شیرجه میزنه
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90542" target="_blank">📅 11:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=o_qWvkqM7jZNL5z0z2lSlfI4hxk2YQhrspn4H1hBwwvD_TvodlU0_DO3hFhpmFSXAkvHjQb335H9foalY6Bvkn1PinS4ylbI6ZJpSBOUiyhLmssqNzB8BHKE-fRydsaQ28j3gfguy64LydmicSHR746E93FStko6tPdzGjdhDmqFPRj46b0w-qtnxP2Wd5KLng8QuKh3ha1UbEqzh9l9o7csJL-DNPr6iksADUQBxAe5zFcQkgM_AVl3h_wArSFPo8uvaYQ6xwbz9JA8VGRNEf7PCDZjFGRC3YmQ6DAZtvfojKWSnoPCJ2yQVm_4qBV8HErUHRng5hckVX9xPCgqUjrSXUEvW4_axCvpSyB7ler8RR_IffEGpxTvBoNbLq6JrjKIFYUSIPsQ4kmcpfV_HPcAQJzSJQb9SIFbtdMWw-gP_GgFN3pQG6zJE1V27XTMQvNph1dtW4u0VQadRJg-Y1lJyvwRK1v0nZzFX2p9eYWZptAiw_Ww3Ibd_qlei_nfOdn7um_pTIkhDp0s0L4O9UQK7OMAZqNIuq60yV_cGqsDra3VUgTZd_Sz7ooKyrmxThLt9z5_lczNTBk941ohFxE8XixxJf7UlfJ8wq2KpKznPFwAUpiruigzWBiFP-KoqhzPlE1zLPMw92S9CwttejLk043-3R3vK6EB3oMDr30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=o_qWvkqM7jZNL5z0z2lSlfI4hxk2YQhrspn4H1hBwwvD_TvodlU0_DO3hFhpmFSXAkvHjQb335H9foalY6Bvkn1PinS4ylbI6ZJpSBOUiyhLmssqNzB8BHKE-fRydsaQ28j3gfguy64LydmicSHR746E93FStko6tPdzGjdhDmqFPRj46b0w-qtnxP2Wd5KLng8QuKh3ha1UbEqzh9l9o7csJL-DNPr6iksADUQBxAe5zFcQkgM_AVl3h_wArSFPo8uvaYQ6xwbz9JA8VGRNEf7PCDZjFGRC3YmQ6DAZtvfojKWSnoPCJ2yQVm_4qBV8HErUHRng5hckVX9xPCgqUjrSXUEvW4_axCvpSyB7ler8RR_IffEGpxTvBoNbLq6JrjKIFYUSIPsQ4kmcpfV_HPcAQJzSJQb9SIFbtdMWw-gP_GgFN3pQG6zJE1V27XTMQvNph1dtW4u0VQadRJg-Y1lJyvwRK1v0nZzFX2p9eYWZptAiw_Ww3Ibd_qlei_nfOdn7um_pTIkhDp0s0L4O9UQK7OMAZqNIuq60yV_cGqsDra3VUgTZd_Sz7ooKyrmxThLt9z5_lczNTBk941ohFxE8XixxJf7UlfJ8wq2KpKznPFwAUpiruigzWBiFP-KoqhzPlE1zLPMw92S9CwttejLk043-3R3vK6EB3oMDr30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیچی‌برگردون‌های پشم‌ریزون پریمیرلیگ در سالیان اخیر؛ واقعا هرگلش یه پوشکاشه
😮‍💨
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90541" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضدحال عجیب و غریب به تماشاگران سر صحنه پنالتی آخر دیشب گابریل
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/Futball180TV/90540" target="_blank">📅 10:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLdFWotBQldN8n_r-1kSgMmHX9MIUdivu-qWVaAlsH8F-W6hVrOFSMN3q29sGbns6k0YiKnURv2m8S8T2pjKrDER_CUnGXWKvWh1Ngcb-qlrK70ULTofUTwxC_DbaM1klg2IPYa3Pbh8wJ_FukZAPuG2ZMVmn6CKbXp6sGrlKzFThCKQOcisdXIXfN2HKDeTDUXMRobPHwaGgX0JeY0bTtsLNlsTOZLiSs3EDkZgyoc_mJax8uf0OWlwxdm4TQfQkMTdUvZT7rIJROwqzPUj7oXma_yj-GQRCrD_m7IVIIS3kothoqB63MFjP5TZNZBNU77T7U_A-Xc7QZrWMAEeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رافائل لیائو هم این وسط اعلام کرد که دوران بازی در میلان تموم شده و تابستون جدا میشه.
مقصد احتمالی: پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/90539" target="_blank">📅 10:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مسابقات پایه ایران، یه گلر وقتی تیمش جلو بود اینجوری برا حریف کری میخوند که در نهایت ...
خودتون ببینید عاقبت گنده‌گوزی چی میشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/90538" target="_blank">📅 10:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
برندگان جایزه پوشکاش در ده سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90537" target="_blank">📅 09:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که اینروزا اتلتیکو بجای آلوارز به بارسا داده:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/90536" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوتی‌بازی مارکینیوش و دلداری دادن به هموطنش گابریل بعد خراب کردن پنالتی
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/90535" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاریس دو سه تا دیگه قهرمانی چمپیونزلیگ بیاره از اون شهر فقط یه خاطره میمونه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/90534" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90533" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiXklXdLj0e4THvjj_OIz_7YBNAaQ1WeV6dnf7XCI8oQ1Xk5yOaPE0HMFhaPAggzrfU6W6hTnKLGPvnPn1bmKb_wnaQX4txqlr6Mp-dAJLGPsod8x8elKwkzrloIbuBNgr4WJWiKtQmE3-betw4QC6aiPemJsgBmAsg3uCwWk1t_RMPPQvqLUBemsk4e1WfGstbliPc6SVYtXCvxSJx2_Gw1Iudytlo0gFQRRwJl5ZOcD42JmKVS7Vl4GDZ-_cI_aQFewVLWxR0xVtX2x7SyUSJ4kLSPN7RYfRs_Y4Xoyv1CrtGFtf1vh2XxZ2r01rOJ_WCICmc5ryEYZa4LMy4qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90532" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbXtmMHiUwlaTyvGqyfA6oqEYU1ms7C_Dh_mB-eGZOdcIGslSD0dJ4eOOVTPj8fNxT_0DuzoBhZF2qGQ6OuvAhkXiZlrveMOWAkbRfm6bbY0GcBSgXpP2C3g5zW8ctDLWGeuCjW8AoIQCYdXqAtMQVcVlY19wxLkNfeMMivz7hd1M9kpRYndu3QL9lTkX9ls3SGuCHsmuE33pmho64sFgVT2yASvYnTAg3E37oKje2qLhjNdXz_DJbjre6P1nVuXVbMsUhoSPVS3sOjmTlv96HXZWJxLXg2q4OaJd8qHEr55_BMJQZXbrVK0d-Cgo4q1na1GK2RroKxDZYWkUkazcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEooXv4bGZQk6VC8ADlhm1mMNPsCmG9pKxrV5wBvcZKGD-zpTYElK6WOwcWNv3N5yDNMm0zcnAfG29KjviX8KUfITBrEJBOzbhIpM7Z6R-O_AMmFyz51twMeUb9_RYzty7EW-YNP7wyp4Pru-Tqhwr6-jAvABSZK0Dfio87zHKJW2LLRsjnTayVm10sa4Bw2ZFSX8SJGpSNU4YBcLJRbUoHNObsJrsaVJhasTeZcOxiY3QgYppDsqBz2NugSAtySf51E29JqosakMxwsLYrQ6M9TRzye9a8FEF41mSqmY_u_VoieXcPEww78nSUtGY9ErSWxtA6Zxb9EoMw8CSLY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEFF6tiFu00JTRKSY0w5Z7_isn02kpNQTEq6tyof-Hd3tqeKELBnx9QbsOqwQXXh6Vjg5kfGs7CJPaEaLYLQAtffBhKF21UNTVO85d1CLNVNOo3o2vTA-cNomcfw4EmEnQJicYR-LzDxMgEWo4HSLSNwSJ1NI8Q41Enaur-lvXlAIuFfPpVKocjAfExXgXuJee9yRHiU2MZOQs8EszTE__pYszfETHQYM96cnjl1dbJ7W4c1QYfnuukwp4tgDNSZ9_QIE8FjKifCRXOXHBTgU2wxLIlEK75Mcqc6iL4oPRMQHshyzgA3ov50EHxzLfXGg0_SPOl1_9tx_bb8qooXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست کریستال پالاس برای ترول آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90527" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz7Bfe45kBsvH0QRnb5Hu4anpCBu6l1uROrqoulN-asZYRtYr_WOLXoWM9WDwm7KElkg3PxADiZvjj1vuB9B1Qs7Cc6hXvL5XBXkwivRcvFrAe4TgyLoZw71QttQ-qalTYjZDtixvSHPKL9_M3y4Khtg8W-V-37M02KS4Llkmpgs967q70zWsRngl5f3D-U1EphjngnYOo1zGaeHLHIOSHEZ_KssNOKzHLHEldJxTisSeflQ6EoSH7ha9EiGsp1m2ksrGq6sHxXX5-r6uYm7qOySvAMbr-cpC0LFHgnvV8EC0Mo6f_hg_PcakZfUvBDzh85fKcSI1FiTR8XRxkZWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا:
می‌خواهم به پاریس سن ژرمن تبریک بگویم، به ویژه لوئیس انریکه. آنها بهترین تیم جهان هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90525" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDUKIyR4akDESRIa4Jn7stYsyejDS55iqPEW3s9slEZgHN5ouR6uQT1NGc-xGcvVGQ6dJAl0PKAhKna3dAjJQ06TfoSSpIaRCoUHyoxFESYeTFCWL2oA8-0keV4CWJ3of-BQFOVItALEYxJLgU5rPlnprbnGvtYo6Ol3WTrQwjmjI_S6LFqbBwjARP18PyrTaM9cM2ZlUyvuKuRYpBAZtl2VvI2L_PaZSHpzQEhM_xupUcnqgd6YQM5xUGYqr3rNR9gMLiNPEWi1HSyJw_OWwIn0u33yf7qSokeDQZz4nB1rza9cuX_GlEFEvReUtN6mk1MOOZIxC4hdEofMczXuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چلسی بعد از باخت آرسنال : به لندن بیاید و از این جام بازدید کنید
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90524" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUKwGwyUay_TNZYUh5SwDB7frAlAEP0cfnbmiUxSHwaIb1InBg3P1BREMVH1-gBIwXisMccLb-o_YxxsNLtKbznKoDJnPPlJGtMcc1PzdMaBWQbg017vsQlr5pAiLHZrWL0T3BloFYV_JON7gU7gyMHUlPOCVMb7XKa0y7xhTHQElZoZIQb2JlP8KmubS2LEJFnStVkaYzdI-HzfZK4n7vydcVRuw7CJ1qDT_DoQU-b-_BYy0nc7bu3veagk5KX7QEL5mCzj6lfYO7r6nnP7TDGYo1NmUXKMns9aRD-atJM63kzsx-CVwJi20fkb12deuWTVfljZo0L4JUFewjIE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxW1SyfsabYk9C239zdHP5rT7--fdaMP8P4SpmvB9uPk35R08S8onrGl7pmd-qEnvW5RNVXcImwC39nKb77fixKHaXgplq0Ni1k4xkKvGZqM_ueKxvEQdJm3aHyojaUjoCq8Tc3Kpxt09BQ7NIWeMVVr3nbEbN3GcCNe36hCqzDmHZBjMOkfw2bnUi3iBXk1Cnm3TaenV17bgo7qk_9D9Pp-25LoQ5mlemLq0QH6CJkQ0y7joh28SZhQHN9jTfMS2JnptomMr2C1D0IxnS8BlizVzzEwD9avntEXl6Q61shOgnNdgi2Ln2LIj5RYKuiEqPeNfiiTcuAo5RdSbCkLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QF0gRPgZ3_iGY62BU2NtVtRhzT-EsoJdLrDOWuSfhpDs8A77_IUUbuEXLjh5gwsnu_VTJo38kveqDvb61FvOJog3heJuv2IbhUyRYuzSEBGWZTiQbdvGMHaZWXRBUVJHbWMXN5LsdvaC9DEXWgs1Nqzxdkc3IdJqrF8OspoabljGygDLJN2bX_gr8SebNprW1w41cZVK9490DW8PDYUWj1c1hIuZZW8eSCVwxPb0HBwZRsGHyJqwkxWTs_WYQg2Yw4-034E60oKomY_gz_FabXN4RsFwsyHfHKam5959TEhRSYlWsEjInIotz6Pws_uq6tI-EiJ6MVuWGDIMI8Nhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VScfe9IOJw_3zPjSedJjb0bwJMv_qs5m9CewOlshfM8GAHY1oWUGIINhUduXJEt93-CzkJSXEJTlOtdplnuRcV8_4LzO-GAIGRzAsMDeLNjSiDKSZht8-rIVAHwCil_dqVxk44EOFbG6JXjXBply6EOeYclkno0gHUgm4UKZ0XeWjSIYA19eMT5EBTb7MjPwxLUVt4GGCKXhL1YavwHh-Ucsakqqx_CP5GpxnqMNQxO62kMtnf9GBSzi0KgI56SrH06Byn_HEDKO11vC14AvNAYNNpKM0YEn0eFYnYY_ojMOO8BmTzbtk3bPqoPv8_aHqfHcheGwsUBZoIJ-CY_vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzZVn9UCo6BFVKN1yx5YzUVfK8AdXbh9aKnstKxrrvTWeaBYFJvYLO1kTAeKa3fwPZ2W8sl-AsaaWGQ5GzuiSkSSDji7HuO0V1DhbhNtZ1_lSGPbjm8tt5XYpKwV4LwAuohNxjohxR-TrZOn4s2ojXGYW_XcREGzKihw0WBpfELQbfCL2FjEpZusKqPCMi4tF-weD6kFGONKSsztTrYnu_XMUCWly6EkAgWCLon5qA6ucUW60IsmoOWf6CCFnw5_jtRkd1YRVOP_1cPFowDuMXnFZlmhUNxTeaF2tfsVSj-x4Ttbm3wMafnKTrfOddARd9-LqHuhI1gttR4Mn2uHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQuH2_ub59R146xfuGdKC-FlabE90m-H4NFA-_mF3Lsp9YPY3gYCQUmvjTKTKMi27DFfCmg9KaI3K4bLYO8TTiUW251LC-XamfsEcTYjsvdFyCDseD-IIiO1wEw7oMcpKjeDz8MX1n7jq8fsqSk5f2ursbFQSU1jhChVHq84XbgZ7SDn_983pSX11YGBBUVaXVSJMwcCAWLVjmqYFGico67s0mw9S-cYzGwNprfQos9oyIfq7pVv4mIS8WTlQeizjsjmypvo6Xn0Ts9qVzfB23DAUUQZwqw31F5uPrw6BS9Rq__vOUUxz7QIH3FHehw49f8ey3WXTtKVWsxA83tNEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از جشن قهرمانی پاریسی ها پس از دبل قهرمانی در اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90518" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عجیب ولی باور نکردنی!
امباپه دو سال بعد از ترک پاریس: 0 جام
پاریس بعد از ترک امباپه: ۲ چمپ(بماند باقی جام ها!!)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90517" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elthntzkPkCnSkCqR1dKc3njDAhPO6h5074f5wnbcUfJKr4fv_KWWmRGb76c49tB8O6j5Yxd_0Tyk8Ys4HinUELOHBtJ89LSzJ5sWWQRFofbRubsDmDsIZ7lUiVIgg4o5-XPVIbo2EyYVyPMaEjq1h9s335w9SiyYi3t7ITGHDipgB8gOQTxU_2rN2nnuH5w-5dHb__qIm8aHS-Rz_WuCbMWgJQ6PGgaimP_xUf2mCLQQCN18jH8xMBhU6A2krvHAlaeGaUYj_ZKiZIdh11AXoVJeNZzxTCZgFgnPxhZ07qynwcvwgZ7f6I22GBFNPgJNRCU-duKztnb1DIrmYCUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90516" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پاریس دومین سی ال متوالی رو کسب کرد و باز آرسنال ناکام در کسب قهرمانی سی ال
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90515" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تمامممممممممم</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90514" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گابریلللل زد بیرونننننن</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90513" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زد بیرونننن</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90512" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگه آرسنال نزنه تمومه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90511" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگل برالدو هم زد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90510" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگل مارتینلییی</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90509" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجیبه صداسیما تاخیری نداره</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90508" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگلگل حکیمی هم زد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90507" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگل رایس زددد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90506" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رایا پنالتی نونو مندز رو گرفتتتت</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90505" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رایا گرفتتتتت</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90504" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ازه زد بیروننننن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90503" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوئه گلگل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90502" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گیوکرش هم گلش کرد</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/90501" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">راموس اولی رو گل کرد</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90500" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازی آرسنال پاریس به ضربات پنالتی رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90499" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز خبر اومد چشمی جام جهانی رو بدلیل مصدومیت از دست داد ولی چشمی امروز در تمرینات تیم ملی شرکت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90498" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90497" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDBl6DlbbQbn_Az4IZ9ZeQw5V5RFPb1GKH__xybD1kRRqdwh_wuz4UPPC73lJ_1iJUKPzgX4PmnicEv9rzb3m6oNgpmZZ9aTeowkqu7V5e-CPhGyCaslcjfbjv1rz0vyY7ucpXAG_EOeYZQbNLgbYvxXYDOlOta4fj0K-rYlBWsTANQhkVGV0i0qVLG9J4Lum_69vHkMMPBqYbJ28JiZZdpCd9aiTjZGnj1jGDspHlxxhi87OejEFTSY3iXodSS6NxUCdfsGBMXPgzhfb27KJbNmb7-O2Ety5d4mMP6VuMyTYmkgr3EmfI2tihQgpw3aLOfmZ9stHw81wGrTNzJ6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید یاسر آسانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90496" target="_blank">📅 21:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موقعیت های مشکوک به پنالتی جذاب تر از خود بازی بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/90495" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پایان ۹۰ دقیقه
پاریس ۱_۱ آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90494" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=iTY9Sogl_0tof0S3nJRoMf0KrHT106Kb4UZAgMqUffRdD2StAalgQi3DT42uMTiHwjz6qKf-n_g_qRXd6ozmWf01GycHgrdrDzmn9YPbZq1IOuGAmfC0S0il59x-isexkYbv_lEhwlFDGUNnkyRHahAkSQ-_oZSuOORsLfGqtyCrcA_v4JNPWjvw-AKAId0K8HIp9fbE1in61uwnSA-_61lJSwyZxLTp0to2DO6AgUzbmjiOORTqC-T9IQK1iNOPPXon9TaRe--JdhbrcafpVkyqtuEHsM1c4NQu-xX-CQuPIlD3ZL0hG1wjpHuL0YHZX1JoCgtBmZUq29slP83yVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=iTY9Sogl_0tof0S3nJRoMf0KrHT106Kb4UZAgMqUffRdD2StAalgQi3DT42uMTiHwjz6qKf-n_g_qRXd6ozmWf01GycHgrdrDzmn9YPbZq1IOuGAmfC0S0il59x-isexkYbv_lEhwlFDGUNnkyRHahAkSQ-_oZSuOORsLfGqtyCrcA_v4JNPWjvw-AKAId0K8HIp9fbE1in61uwnSA-_61lJSwyZxLTp0to2DO6AgUzbmjiOORTqC-T9IQK1iNOPPXon9TaRe--JdhbrcafpVkyqtuEHsM1c4NQu-xX-CQuPIlD3ZL0hG1wjpHuL0YHZX1JoCgtBmZUq29slP83yVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به آرسنال توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90493" target="_blank">📅 21:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگللگگلگل برای پاریس توسط دمبله از روی نقطه پنالتییی</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90492" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایان نیمه اول| آرسنال 1_0 پاریس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/90491" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چییی خراب کرد پاریسسسس</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90490" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez0T0Fi0LXf1c5OiN5IiQA6EN9MQ5nLq6nU36BbOWHcE2_Fj674ZD272kCvcqvTObe00aMQVltYRsRXW5yTTTC0ueyqdWu9Lm6-HHfp4n9vaHkl14f5MGiL90tE4qkhZCw3S8HA3mUooQqUgNwvD0vvbfmHtjTUYRF7d90qOrNhxot3k-3EMS6oEoC_gzy-T-cxJcoLzu37k7VXJTRWsMsXy-PwX8YXWAdJDFlS6A4xUIt2w9rhHQ8D5PXN9H56T7ftITjNYK4klRWwa9eSCrMOMuBqhgMbKm3wdMCyL6gNxiRazGEflsH_08g5np-cd0ji64aMsAHdl3K_z3upedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرنه اسلوت گزینه اصلی مربیگری میلان در فصل آینده است!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/90489" target="_blank">📅 20:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRK4O5-d0iU8jEkmjldD_FJgapJ6Lxoi7Dg5qgJCntX_Zhu6K8olycpgRC8YJ_bzqLs7Cr3vfpOiRXZfLbyyZMP0jRhHnVpin97CaZHzVuBADCNWY4pdAsMHoqAbvxoPkZrKJd5Q_WyMijDekIbjnY3ofG3o4ItWMF2M0GF3Ti6uaFUlP0ss9HfrdUxy3tYaw6yhpyAr_mgyMCeCCEfyiN3-JSY_4FS5K9aVlIUv-mSM4x_TrrjJcvwnkEfsGN7B-WcZ2a4Qp_L23PCIr-eSiHJYhMQ1_GR7acSeP_VKW-r_qHfsbm-1DW65rVqz-5wPgUyHTLkfwR0T-2C1mrkEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90488" target="_blank">📅 19:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90487" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpTB0yvqufqEeatUf5ru9e17L-E28qTQ1H8jUYh0v4tvUIiUh1wR83tw-gw5ji1HlvoGPbE0m_FXWdKH740vBUNSFMjksrxEEj2IlhJjLqqF47KrEC8ypZ41ppAlkUwW-2F-4bubNr2szyLjAOZO2SUer1xorLmPoU0Qj7JgC9rsDmF-hOTi3iwRxEX5dX_Cn868R_pwd_UpxTnX-bY8RsOuf58nnnn2KeOB92AkpGeflvj7hRn8oAroiFq_Mj-LCVUG0BEk7N1WtyCYl0Uer6snBFFvU1LdbrdlJvyJr7J6k87qkkjpI2DLO3-he-VNSlcunjXE-0LTfBmamodOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/90486" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anrnjENCv3929zXxziTkpqUwBf_I9-T7cOFNlNAtaZRcWtwUj-q6SPiXFXggQoyBNfoanFfafEUa6RDqKw2epXj5u5E4voU3hFJlK5dgvHTvFd_FmEATB2-CdhIjhawnPB0KW4zncAL-Bx6w6mf_Jn9lYduy9jopU6JRFHgZF73Cpn0i9GBxaUPfzlnHDyIq-ZibSq1TlBa-w3AjJGauA4tskfsFwl_ULi0pVfK_CY2SjSlUdFt_C8Q496m5OIS3UmvIKLvGRHeQm-Qt39XUS9WHdsiQNB4B64y_C8naR29M47560xHtFG474JqYbeYGwI5c6W32pH5wAkcAcduLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/90485" target="_blank">📅 19:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71e697023e.mp4?token=CoNcTP4UOGjcqCPuB8RS1FKDh6508VMLMUeF_xCTbzZuBuvgl7oJHPCcwhX5KnJKNNCZLWQUE57a_Mfsf4n5HCpmIexc2czHeApzXrf-XCw0LTOF4TsUivpcIxSZuI0XpEmUr8h5oZYdlUsIGMeHhYCap1f1SzBB31T593fR_nRKpLTZf9CDpHA42iXP9xjUCROyd7OtVPnGo8ieKYOr87PQ67cCoAtgG3TrMF388SKzd94Fvum7L2AyKRiwnWuzs4-gnGhGI2aepfabBUtWuSpLUvExfx8o_qCa2R_6YWtwfpef_jZtUSfBikU-0piu3NEDlGaCuztb5eblIy41xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71e697023e.mp4?token=CoNcTP4UOGjcqCPuB8RS1FKDh6508VMLMUeF_xCTbzZuBuvgl7oJHPCcwhX5KnJKNNCZLWQUE57a_Mfsf4n5HCpmIexc2czHeApzXrf-XCw0LTOF4TsUivpcIxSZuI0XpEmUr8h5oZYdlUsIGMeHhYCap1f1SzBB31T593fR_nRKpLTZf9CDpHA42iXP9xjUCROyd7OtVPnGo8ieKYOr87PQ67cCoAtgG3TrMF388SKzd94Fvum7L2AyKRiwnWuzs4-gnGhGI2aepfabBUtWuSpLUvExfx8o_qCa2R_6YWtwfpef_jZtUSfBikU-0piu3NEDlGaCuztb5eblIy41xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال به پاری‌سن‌ژرمن توسط هاورتز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90484" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سوپرررررررگلللللل کای هاورتززززززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90483" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آرسنااااااللللللل
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/90482" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگللگگلگلگلگلگلگل اوپوپوپوووللللل</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/90481" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYLXt1EH_6Nap38RcCPqKyGvKktW4EtSuWrkKMxYma3ohd3THDZg3sA26av0jfPL2xZyqH9nAXpT99Om_x124AqZ5v05O5mzWEsAW_Uf1p6zB6IgfhitggqTBURt3nlBpdjmGtkgmyN3EKTttZTwxGaheyxRQXfHLhh7aW0yLCyqwWJPeKI_kC9C19Vnz7dCLSHo0veSxFvRjXztlvIMPEEfY8EYye_rYbJSNGDjazh3DshIWs165RIwkcIkE7r7wPGG93w_0zcbtrnMHlmi2lxkTK-H3-4-aILXpgJcGkJa0_a6_lpJhOqBbttR451Sub0A2N49X81MZ4QkummGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی یک هوادار آرسنالی از پیشبینیش از بازی امشب سی ال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90480" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrCB1euOxUjgwVP1-F1G_pzVTnof7wdoQl4kCBg0CXbOE1k364_O2xXFRru8qDsoO-NrahA3VXE7-HhB2OtThYQ5ug0i2awIhy9zwLFFCJBXctK0yUqYDH3nb7IxFSuzZDZ5n6PVQdW3baMbzRQ-UV8m0TcNXje0jf-ddag84YhPmQA3jqDcyGEpWvSsW5i3NnuP4aSrj7XMZagj1vclMzb3xrkTT3vH6HZnDvLfZH4ae0pe9b78sAdpasEx5wn3Vuz2RHnerR0RFsLfLONiqnaCDSgT0aaNO60ekmY86PslvlnipXr9RyyOi0Yfg7ZMN_B4HtD9QarpwwE2Y2xveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUfwYJmLXYmPil_-MiOBZlpjGz09x3hYpBmCX-Rw7R4h2QaPBq5I2zg5BGB1poxFmjk1LG5tJjPcDFG63jr7JsHfFR2eNCdT0Br5wuylX8dbqJte1XvEQlbuJ3kP1ZVldyIKDPcoASTkw9eBGTrhAxJHcKJEAvASxUhlfcVK-VSItVyGUqlwGvz03d1r1Hc2nE5IrrGPwlKWnFWMAqRP1LdAoSq1nRgdaTR_7Olhe-YJKv8EdDB55uhr-EfAdzXWMSQhxYISRr7Qxgmwp9UBiMaDh9ialMxBfczegb4upCIUoUg19ie8lzL1QCE4NiR1jcRXLWjP9svOt_BbLO0jhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmPFGtNEP7-L7VziRdFgBtgmbJOm3oIfQRbTvs_RTQssqqT9-BxV-R8wAytbpAaRAYdeA_KJJHsqMBMXLNR5K1UxnIXaeqwsBTNvuYaXeX2ZP_v9NZROtWJWQmL3IInedSc3Jaun7LNMM_4bJJ7j4_eSCn3gz4tzjTEkv3044HY_VwcL4RKdFQ65ZyeSStAfp-YEFj0ayAQEvGtjm4ae79NC-QUGkZtumOAe13I1GPZnW0FPcLa28s-kC8EwfWS99lsh0-_XjI2bTBXa00Es4VdRi0Fih59ERea_kLoI8e021h2U-ia0N4Djeoo2V_o0iSMvctsWHM4Ko8CwShbKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WU5Kh3tvasg7DUOCkeAEupYTPtcfD4Nqu-3X2CLQL5goLMx_GWRQza-YhNGeUFV15XLKHmvGwcWZ8rLZDol2u5MRnDQpm5KSXZ4mF-cPQom8EoOgiqPhW-rLS1eRidXnDeCu9wX8w3D33xmKE2S-38YaurDjB9U4HMrSfOlKVlU9gi4OLzqUQ7BNRX-DpP1ADWTBoXVPvimmLeyAhT6Cse5SyH7gcy3zv8TcH45oYlvSRQ_RzbEb9LVKJD75OUoNpVhS0jMKL_Ey5JFI6lWOYHT3UApfo7YlvEEcL6fWIDCEm5--AL9E8mayIOcgJ60AGCKQZAQ-K2D81uZx-lIWTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYTsBAZzauZOt5n0OQVBjMM5xnO9fj7msqcdMSVBidsS6mmuDn1Wq6VmSMFh0MZSA9OCebO0fy4fotoYyqUeQN13otVK5VXC_UxGgmVbzhOx4rJ__DUaY1eqha-B-0SYv6f03w5JbuL_XMpn0HM2BpYqEZY7fOxazSlrgx7lkZop3cw92lQC6C6VnNOPI7irQvysfVTpaLMb3ksOQbMrkNkytCCPos8f4q5rcIZM00HWRv3CG3hwJluIJzElSqFmcpwyHgfvn-yew2scMbNiQpIUp-8_HVBn6rHJOMEvBCRCkT3yL-9bpDmbLGle9mNYBHTIkUjCrm7dXUOHgfNlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYhfjVyR85_1yiTNAQvEZa_CRhSVyQjw-rHYTmmNoqkc25kjRG-pyPqzzk-LZew65pqCgsAmtW83Ct1ZFlBbtpDGf0ayXbalQS1SO5oHbJsa5lN70s1AH-8EuTUcqWiReZMiOWxAHpfP73U33BrBoBBwF1bgdBtYwGZGUtknu2WMYpVRaBsmJUuGZDXvaBTf05JA187gOtYSR6D-Wv2RIW8ioKSMi0A9weMaI56L92p7nczKzcPvrx3R4YbRHjQ3_BgyHmJMDEgn5xdEb3OYPcMNK9G31sveZwk-MMeyQya2eVfhBqRVeVCtFT4IvJUa0k51qfBQVtDDVWFCjvEowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=cltjS5648alQyhFltPUdsvBw2krRg7cx-WUulYePdP1U5sRgr80Cu6T0Grvfbb3YEAn2uuKlVAxNrfWx6KsU0d2CODnc21jrCTQbvXAYr34jVC5Ccp8tt9g84foozb-YZajlfvmp9abcDGSt5mTsNMesuxVQTLKr_gCYSm3UOF9K0AyQn6KxH05UbC95KA5DBIBwaeODLqjovmxrdsI7bIoJiET8Tqp5VmvKW5LggpWWKagdbs4jvflOT44H3DguCDD-giEJnhZspZriBI-ypEdDTay_gbdnU-g-i0SNJl2NLrvE-MxLA2pJ5pRO1mxjyHzCkYUbFChcpP6IVABozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=cltjS5648alQyhFltPUdsvBw2krRg7cx-WUulYePdP1U5sRgr80Cu6T0Grvfbb3YEAn2uuKlVAxNrfWx6KsU0d2CODnc21jrCTQbvXAYr34jVC5Ccp8tt9g84foozb-YZajlfvmp9abcDGSt5mTsNMesuxVQTLKr_gCYSm3UOF9K0AyQn6KxH05UbC95KA5DBIBwaeODLqjovmxrdsI7bIoJiET8Tqp5VmvKW5LggpWWKagdbs4jvflOT44H3DguCDD-giEJnhZspZriBI-ypEdDTay_gbdnU-g-i0SNJl2NLrvE-MxLA2pJ5pRO1mxjyHzCkYUbFChcpP6IVABozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaLtjinBqxFpy996k7tE1G_Kslgb0qXAmfhuh0itTpH-_1ODY7tH6leYh-8fCUBO671wWtABMLIu4Re-51q0LIZH0HqJIujh6-07Oqize84fRWZRhSXgXnf7FqEGp7hQkOqCMdb66w_NOfVDNZvqk-c_F7bhQxHT5QKsfABbO1zvg9fBak_OdkTqWCxwyYD6mqPlL15kjSeOQwu4DBVROaiyPeKQtftou2v76CO8Bdh3BWkqtxIJToOUDNdoNa9121A-sUbUNFJoNl2QeNUSofhz788uVdyUsEb-sdUNuWB4h2qfbIZz6e7HP1WA8IPQ-AgoFRT-DlvLZ21uhqXtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=lRl1-1uVd12xbjdAwWxeWeKd2Vuu3nqaWGUZ4KeZxdn0OnNuNVhMIaKYMXrKNyAyIpgtrRrM2y0VDkgLNbYJnt6uzjOzyUMT9eJhfTJQT-q_NSEf54Pz75xvsBom5K3-cT3aBFcSezd38MJe2UjpX4cWR9c3-NecF2H99o_9sKjrHoRyzI0mFSz6cw46TaYhX7Nf0d6jKjzXf_ejlxVifG5DEmG3gv1AhBFNxVZtMZn-GkN4Mdnlgs-tmLCxzXSCeYRTJ8bPMfWdMI7lB1YabYuxRgt9D30QIVYZNeNLtnHwPSa58mxAMaDfhhZzXxzGDqX1H45YCXdGx1Y8ensyaKjlX-niGFn0XtDd1uKUgTQRuAuJ4CvlvJ1qr4LUV7uhH6LlxMAh6ssDoLKQ14Eoy3Tdq86IZJNlc3D0j-NKpQUYWAVtQ2wFv8HHfDfXiLq4JByhSfRIrzln519JRAdrd7EBIR6i035JrygR_NHzFOEFHbBNzsEjBqH_1trND-2fEbplv7TfagYV7_BELizlaySvZniyfn9K44wxNX1Jj5o05d10XOdqDbe1shmYS5LaGxqKYoh_H6vo_b7D2Km5vzomtVwjbpVlq_HZgttxQPfqbmkab2iepWBAN3g-QxLI1OyPX-iKrZIp5govEuCNv5vzBsKZxV-vSc4vXtyiLwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=lRl1-1uVd12xbjdAwWxeWeKd2Vuu3nqaWGUZ4KeZxdn0OnNuNVhMIaKYMXrKNyAyIpgtrRrM2y0VDkgLNbYJnt6uzjOzyUMT9eJhfTJQT-q_NSEf54Pz75xvsBom5K3-cT3aBFcSezd38MJe2UjpX4cWR9c3-NecF2H99o_9sKjrHoRyzI0mFSz6cw46TaYhX7Nf0d6jKjzXf_ejlxVifG5DEmG3gv1AhBFNxVZtMZn-GkN4Mdnlgs-tmLCxzXSCeYRTJ8bPMfWdMI7lB1YabYuxRgt9D30QIVYZNeNLtnHwPSa58mxAMaDfhhZzXxzGDqX1H45YCXdGx1Y8ensyaKjlX-niGFn0XtDd1uKUgTQRuAuJ4CvlvJ1qr4LUV7uhH6LlxMAh6ssDoLKQ14Eoy3Tdq86IZJNlc3D0j-NKpQUYWAVtQ2wFv8HHfDfXiLq4JByhSfRIrzln519JRAdrd7EBIR6i035JrygR_NHzFOEFHbBNzsEjBqH_1trND-2fEbplv7TfagYV7_BELizlaySvZniyfn9K44wxNX1Jj5o05d10XOdqDbe1shmYS5LaGxqKYoh_H6vo_b7D2Km5vzomtVwjbpVlq_HZgttxQPfqbmkab2iepWBAN3g-QxLI1OyPX-iKrZIp5govEuCNv5vzBsKZxV-vSc4vXtyiLwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=Cg0HeHT6nf4a0YgZdFx3SbXCACYjvh-Lr0r3vnpaEwFwG8TD7BHHnFnOhFZWFmnyG7EPubP-4YMuOzNa1J4oWnJza_hVGXtE9gixDogY68EfnRuBaPOEEFeCahFvmex5X6y6tGeL34Dv-94Y0ziT2NRo7h0CwMaL9UXpRRpdOFt9t-96ki8YgzMzaiUcugevjByl9DMsLEFpXMsAEbjugLrwatfC2zRt1QJ3f3e-RyuJM-5MvoAO1irziqPzCCRN73PMDiWw17fuUTcsnaNHlFh13syMefpXD7Yy_gJ09CrtaAiHoocttkbZCZe9nGqy_6wBZtM7H_KOsjYDtmIvtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=Cg0HeHT6nf4a0YgZdFx3SbXCACYjvh-Lr0r3vnpaEwFwG8TD7BHHnFnOhFZWFmnyG7EPubP-4YMuOzNa1J4oWnJza_hVGXtE9gixDogY68EfnRuBaPOEEFeCahFvmex5X6y6tGeL34Dv-94Y0ziT2NRo7h0CwMaL9UXpRRpdOFt9t-96ki8YgzMzaiUcugevjByl9DMsLEFpXMsAEbjugLrwatfC2zRt1QJ3f3e-RyuJM-5MvoAO1irziqPzCCRN73PMDiWw17fuUTcsnaNHlFh13syMefpXD7Yy_gJ09CrtaAiHoocttkbZCZe9nGqy_6wBZtM7H_KOsjYDtmIvtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIP_s0lRM9HS_Y3C7TQF4gb3pD6wVQHKXiUearWTj2AYGNZmGp8RFayDAL9leZWh4h_8xEy_N2iMOLkiNAz99m5cAqTsxezfXBFwEj1WhfIFO3-qpAb50Z97udB_L75AD-0sCrShPXfPz2j7xfqzLu5Ya2BDTDzp640BQeHIKYsdWZoKpmAzX0x1QxmVVNlV-oCSyHW8YIqbodA3ETTitysXnYkrhElPP4EjZfpvB2MsH92xNXdTA5Kvi0OVe6J0ezwylj0GO8BcfuGvxhfOkOh8ewqBlsxBGx4qYUokZJGyJKwIGhyShzmBsxyEarsvBizPT3k4xUrTPqv_-2lW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEDA54U7U3RtmgA5036EGHfwSdfn6uoR-O8t3pvO94YhVtYHt-c97I1fRA6sIx7o6nNDctvsquBj_W3LNUkHQUspP6RuyEY6FUlgsLSVY6hUBzz3lnMYrllpqfakb_u4cwa2sJOa6fHxg0OmzQxUUU6M1e6WQNrWYqZSWQJyH_UAe9MWrHOboeaGKr2KX2XLHR4F-p_bcFdCTaB_Eo9tOD3EM34WG7tN5qH14q6truU0DGBogOSPT8CTjGudROC2HJc4w6QsgkboHTFZNG26NS5ncqPYVsWh_KfBOJ8NmIKMWO8Mn1CTw6XiG_gv_M5sFO-iddj16EROgO_2Wdmr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj7xacZ7uzDEWQCWy-Gab8nhpPxgoPttbDcs5pxWAeOT5MllTgrROapR_WGHWQ_2CPe1HP9G_EEEwe9dNv7cgnJ-iVmQfpaOr4rxL48yG7W0PkkxJWebexGhWqwa1-7Cg5q-BPFYc9EU8YK3bW8ZhcTKMUKv4NByDLMxpK5MF47L4uQUKkZy9bruyhqzW2V3IveoFukUqTj8drYe8oI0YDX8ybTo_VH2V6ymBd21_LK9Z-pbrHHPWYrX4JWrYRxQSlWYIZpPRMGOHzeKFWlkUiG746CFmn0J0DpwdysAh1YV4Uq3qcMgtWVCJ_zrLWyMew_LtXNcMH9Syws0MYfjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m74Xzt11-quieD78MNv-hhdNXwTZZM70h0NE-0A8jbNEJ4Se_PH7O2PwcrlBrRRZ_Shwc8Xd4beJu57_mcGdHVolrR70aEa8zMJUdHqWKwxwIqfHkGyawcfi_zb4kNqX3yrPwMDdnmDwcNq9soaZGk8wz44q3nrYjYxJLfdWP8VynplHiu7xgITP9T5oW5b_PNpFFN_RK815g0ET7uat4_Mqy5knErl0tm9CmBNMGStP70B4YRo6Ma7EvW7f6nQTnQuY1G_8aLys989vKKRFhwoii-4mXIISAUhEoz1JSAdh5SsRzcpgFep2b75u01O7vxk4BIY-nEplPxiVVLR_jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=YPFeNYIZuX_HgOPAgTlMu0-CCTl3ETV-qq1KJnjlXYFrdyqy7UkqGN6SfmmQWyWcsgr3sVDH2vJsQbkslN_Ic8Y2IkABwi6LAOVX1TeHzc_rWj0rxuVoCp_1sg7ED-fhGRUIaV1myhV4iB_NkA9oe3DkIc71QW29ZXSp1erArU1u50HvRYjTEZ8cwcr-WduNoJx1wRWlir12ESESBjVoSCBmZo_-MdRZtyEBZmF-XvGM6qSkniMoOU2KrA_R1u9ok2EkpnMcQhAz_bB6HZfMzrLqX6rr0YlrUbN1WlEv3Uz5_gSu02V8MLM0I8Xqu9x1oSbzfiMsTZ59QuTItMCXcHFd1zfDF8slO8n6Pbh4LzxOFqWAOBlfiN_Z0EKB5Eu9qBOicxDM8NKKHbOGNveMw1NvH0nQOY2bFHkve9DV0zXKCy0Jyq3XRQAVci2p4lDz6Js4-4tuqew4gifOFLfNJYsgsclESM37aTMDRn5hSsRhXKRomhNgimadW_QQ5CEWo3T94-8dfvKog0bBqhGrqvU46fqowJfEoZUNqw_4aFtRBCFVofDX-uQGAcDZVCuG3jdHix3OfYkt6i3N3GQn9tHeaY2d0XDp4sOzyUwnSwvlokNQhH_CjblLlfbnQxTjHviIpl4BhaWUOnEMwKitoLxqCLWWhz0eENBlZl7Q4LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=YPFeNYIZuX_HgOPAgTlMu0-CCTl3ETV-qq1KJnjlXYFrdyqy7UkqGN6SfmmQWyWcsgr3sVDH2vJsQbkslN_Ic8Y2IkABwi6LAOVX1TeHzc_rWj0rxuVoCp_1sg7ED-fhGRUIaV1myhV4iB_NkA9oe3DkIc71QW29ZXSp1erArU1u50HvRYjTEZ8cwcr-WduNoJx1wRWlir12ESESBjVoSCBmZo_-MdRZtyEBZmF-XvGM6qSkniMoOU2KrA_R1u9ok2EkpnMcQhAz_bB6HZfMzrLqX6rr0YlrUbN1WlEv3Uz5_gSu02V8MLM0I8Xqu9x1oSbzfiMsTZ59QuTItMCXcHFd1zfDF8slO8n6Pbh4LzxOFqWAOBlfiN_Z0EKB5Eu9qBOicxDM8NKKHbOGNveMw1NvH0nQOY2bFHkve9DV0zXKCy0Jyq3XRQAVci2p4lDz6Js4-4tuqew4gifOFLfNJYsgsclESM37aTMDRn5hSsRhXKRomhNgimadW_QQ5CEWo3T94-8dfvKog0bBqhGrqvU46fqowJfEoZUNqw_4aFtRBCFVofDX-uQGAcDZVCuG3jdHix3OfYkt6i3N3GQn9tHeaY2d0XDp4sOzyUwnSwvlokNQhH_CjblLlfbnQxTjHviIpl4BhaWUOnEMwKitoLxqCLWWhz0eENBlZl7Q4LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIP6MoR52L1_AOKO_C3-9C5F_5VgIQBKzE_p9ucFQ5gROAcYT90a7DPFrcI1VXcERWYBVkyWKCeGb2AHXfXbCbzjFgF83DGzHj3r_gEoJU8--6sTvzHvbuRPu1xFFrdwK4iUCj9UwAk33g8vqoD76xO52Raieft-aU2plqJXg_9wmjXotzPupwUpl-1Njl5653AruDrQdf0voh-J2WmJ3-jZHvNlYWIbgf_knEFdGFyykOkaRgOZmouCKpL3xKSJBt8YaCLFObjC9TBK4FJB2qOX0O2yAJ-qnaLSud-QkbCiw96kwzGnSThyymGoISA8KXgC2pTyFxbgRA-4yu17CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توییت جدید باشگاه کادیز اسپانیا
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90461" target="_blank">📅 14:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBmvOaRyy0hPZiZSjUUX_XFGUs-RPygPeh7b-pb373MUTVEoEQIAubhO63k76dWFVJdygpx_zBVsu7EOPL669DS3NSHq_ky1-mqRvv1CTph3wpwpVuGNO2MatcQd_NPlv60PG54az8YkSw9MZzTFuS6U9k2qni8eA9UAQDN8c5Pc8Q00-npE1kcVu_CcKvhtQ71Es5wYT9MT8wDXuKysEqLYVaxeGKRS8irsCvbFl9xrKHAyzK2TpNvzZ5Uzv__wLUb769FN0MRW2KvpAHCdIT---Cya6oTEyNiLoq0ENUddjB3-rI3pAeQ-zczCkPdkXgEBKEPV7A1-OF3mhR1GuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فوق‌العاده داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان اروپا؛ رایا در صورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90460" target="_blank">📅 14:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmZ5Q9gC2jx4MXxf-6I7WYDcSlIiGjvxvQIXExwaE2IrAz2Obo3SX3B3u1KA4E6MsmdGrGhgovHueS7qvr8WzIyWLG91JmgkWOH91HeTroMzDitTKXB3XXHUOdZwwAN8Ix37163HdgcBjByBDEK-ibTm0Q2n0a7HfAmwh-VM-W6bFI8Iz_y1vMO3aYKBaaSh-ypkqy-iygNeL7jlW1CNU8-rguOHWyzfYFrfqae03ubpPcZv3on2KDCNvVw5IMYJHh6Ail2TJei1W2lJuAwGi8RzKZUHYKgrgDtQLuapFwZU5hiQI8WDsmOAK-X4IIwwXOZcBGmnO4CS7wu5jFkWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4JdDEcDiln7UoEE4aVPXQmllu_KsgQyaj2gWR2fBGl1wdpcjNaRo1osJTNS6Uoy-3YK_9m5i6c5n82yHtqmgxd0viWnXk8xb2Qi3ZcN1bZRTm8RWcHMMdKVrd67-GUFgThvCDyRh7XB8b-22_JRw2AxIvgrdHMsce6cG2X2DMpi8CgsXpoPKyC9V1yjHGZgaBzD16rr_C-bra-CPUyFxU-mmmtKEobheq92Xih31jKEsk0-Bf56wAxTzY39qXapp99w65aNivw4zDis6FGQPktxzKpyXbUg_HlgEpuHr1L9XSd0ooBEXbvp6a5r1LYMw4b27thogG1rrsMWYK42fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAALF8JTdwUDm4aaKTQlSY9tSWWjrKx-rI94axgoz2UTw50sZoJORhLdj63nXLQaOm7u5-i8NY1lhH4h15XRXov9LSAiV2QkVKNnlXAFdMNUKazp3d6HJWAz7hYZppnCWcyANdlMowvJNj_tv7SthajPR1XVNIR42ocQ059bMokUIeckWn1L-gS07HV1t5QWHbHflndUBaH5cA3d5I8yXthRITZkrmL48jUIepQwFqnQbdXqMaf8Ie6D4Havejxb89X_xGt2lsuNI2NDGsKdmIBShxskQVCXHTxXV-gKmmp1qcZthUKvfEeD4pJrvUYWRIEYCpiHNJnsgbFFwo-MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF51iUa_dA5xnMj6u-WQhARkEESuiwA8IVJYlmVMkAIKzF7xVWFfRjVR5YCRrgQO4BKZkCQ5Qj3pnKnEa3PGAmQnjTUZ-Vmeb1iSuVc2mu_rY_k0QyCBf1zuTFzzb9JeGQdCenmFaeOsyYiQZfmKD3Q81FQkM-gwCHGsfk3FY4qLlgExR4_Rohl2HZVW34-8INuNUUoAHZiSXir7xhfpEbH5KjYBpocDV-GOBiC0xrBgrZfHgaO7oPRqa56ZE3Fy4rdG08utu4G4RV4nqLFsco1bg8hxvNA6QG-tbxjzi7Q6xtifQEZ16KrAvEoER1ILgb5kmU42bzcJ-dRDgk1i1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj_s7gvbEStufC9xl4x-NqWbiBM5qoUenX5zeQAoD1QxTXN1qsR2h7oe-l4SRg_5Xsfv3kkeL8Yex7GPZ4bSWczFdjWJNE3Rx1GYPQHJbFMWGLR6RsN1crcFlpSVUoIWig-luuxXYq8UpUeUinCeKgYGtZYdQO8-rM_O_-QzHDTcdyh8dkAUx_BqiJ3HcY8L-IaBSlmnjaoNxgy1yfkQOKn1XVWBWq_drqaG1WtkFob4eB3Q7xX0EVuRjowdG4yy9fnisLdaq0PTis3w5NQZH1i7jEEUvRHIhHakY4iVb0DtMobyNeV4RWHVzlWjgjohBO7d_6NCwuh2QVOpHjsJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3EYMJnkKY9X4pEBBD6juknAYY5BAnLsGx_eJ23q9RrqGJ2P8e_06C5GpPf3Kre8_RsE5eNf0KeQ596NlcM6FQiy_JJdqLhmeXRdklzPJr11t2S4FwDjQ-H0Vw_NWmBsK1F-4e9JQkk12PXMTgc_-Wn9CljfndqCVNbequ_As3d6OCddjnh_HdcDhSIq_hEcTxJpA82WMIdBu676DLeuaLSf5XzQeEpWrBzMP229FEOF_BfJnVxnjXXU2Rmd7_hJL_Yk-ANc8l0yo9IVQ1BcukpGwO8R25j-fUh6uP5xLhnTyZ5PndtF6cvtmZstJWwB4Ck1hkSpNDMrUsmRZyLo5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrJmhKZ5JWMIyVI_o4CNc-XprRYQJtzUlIkYmLJWU1-6YsidMqgZLPqMl6BP94TZA5nn1ZQQAFgiV9DFOmA5LPcM9oqSh9DRtFkITvlXKa1S_Ujr6DlH-lVEatpk9NzPFgV4WNmLJAEWBkzLaV6d4FrA1u_XSHp59yVEsNu5du2McwYnyM2_OG3uUMwP6Dcd8-_Z_aApjYy7LrCO_gMFd-IRKqmaKumbgJO_A5n7ghecVsNNm2gznjKXHZ9h3H8_xXZo9ZW5vTChyRKKOwD7o1Vujw-33ZALYE_WN_Dyv_0d8tafM2vsrKRjG_Nd2OvueC3O444HtS-KQTFMQV5beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=DYjmyJZvfpARXQRV-vBIhdQaZa2mi8o380Ea766PfDFB1T_63pIEfGPENqaom_97u6YQ2imPyPZzxrf4LKKcTHqFN67n8veEOZ4O7QTNJ2luWavWE8QTpE32I_pKSPJQNL2U31iDidzyLj4DVKoueBVdibIboUgi3ajN9aWM3pFDSoyheCW2AMgWsjrMZFt-YlrKRei-meUrRv7e8Ns0xqKWY-tj-X9BEhAIVv8RPGiJW7NePOh2I6K8wvS0xP15gxgfsbtcikCbt0sCOAWtZGmoBhF06xmdUl2aIhZBf0IE8N9Xt2fiqWbe5ma-idDU5nwJXBCvpDEGpDG64GrSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=DYjmyJZvfpARXQRV-vBIhdQaZa2mi8o380Ea766PfDFB1T_63pIEfGPENqaom_97u6YQ2imPyPZzxrf4LKKcTHqFN67n8veEOZ4O7QTNJ2luWavWE8QTpE32I_pKSPJQNL2U31iDidzyLj4DVKoueBVdibIboUgi3ajN9aWM3pFDSoyheCW2AMgWsjrMZFt-YlrKRei-meUrRv7e8Ns0xqKWY-tj-X9BEhAIVv8RPGiJW7NePOh2I6K8wvS0xP15gxgfsbtcikCbt0sCOAWtZGmoBhF06xmdUl2aIhZBf0IE8N9Xt2fiqWbe5ma-idDU5nwJXBCvpDEGpDG64GrSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=NorGiDbk0K_70Ga-IIY43e9MjEQ7heKU_zKDlKjlkvxOFJUc_dCAFHAWMX22FEy9a-52U3sP19bMpmUIzM2PPZppxnlzXGcg5-Mjf0iwq21Z56XXImthbYjEbYPwvH8NXASeBgV8UZNMejlUOWIUPPgQNNmtMvukXTHrcM6wz9ULZ0lWPLypqGeA0YHICSuI-U96P_z5tjGwT14eHGil31h59IDFjGkKBe7ZdTc2OZvo9Dk1mxgFNev5W23muDiLvGvW6yOb00Z31IFG_PMYs90s9ij4--55_o0v0bfzqAAYlwcbEUcjSywZ3iWxDCUW-C6F-_av5lYNsHvcL6zoLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=NorGiDbk0K_70Ga-IIY43e9MjEQ7heKU_zKDlKjlkvxOFJUc_dCAFHAWMX22FEy9a-52U3sP19bMpmUIzM2PPZppxnlzXGcg5-Mjf0iwq21Z56XXImthbYjEbYPwvH8NXASeBgV8UZNMejlUOWIUPPgQNNmtMvukXTHrcM6wz9ULZ0lWPLypqGeA0YHICSuI-U96P_z5tjGwT14eHGil31h59IDFjGkKBe7ZdTc2OZvo9Dk1mxgFNev5W23muDiLvGvW6yOb00Z31IFG_PMYs90s9ij4--55_o0v0bfzqAAYlwcbEUcjSywZ3iWxDCUW-C6F-_av5lYNsHvcL6zoLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=nBzR2o-NY4-TvRbuwD9cuXSRi5r2egmBt-MifHCVFzIj8Evg8XAiYRP_laKZM268S5aENd6HEYlxNJdWZTyvNdTocOAQG_EOcY7MpicOdJ2X1YgjIRPmToV7vUKa3hdEW1x1-_6GgtDuQID8CeXb7dupmdIjTqkENGmlYEs1wa_Hi0gWqNyepE8TctIpUFQ2fcvrlE7dlFalpfX1Ppe5gjcC31ZJG1b6DTjJM6Y-tp25_vaRb3H00-Ah6gMws4pL2mYLIaSMd-NKbIIK2op-Sy4UqySYZ8qUQZK56DMoL0qDJfN3AE3UcdzuybDhTgpc8qtY3kytBmfoMZID11a0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=nBzR2o-NY4-TvRbuwD9cuXSRi5r2egmBt-MifHCVFzIj8Evg8XAiYRP_laKZM268S5aENd6HEYlxNJdWZTyvNdTocOAQG_EOcY7MpicOdJ2X1YgjIRPmToV7vUKa3hdEW1x1-_6GgtDuQID8CeXb7dupmdIjTqkENGmlYEs1wa_Hi0gWqNyepE8TctIpUFQ2fcvrlE7dlFalpfX1Ppe5gjcC31ZJG1b6DTjJM6Y-tp25_vaRb3H00-Ah6gMws4pL2mYLIaSMd-NKbIIK2op-Sy4UqySYZ8qUQZK56DMoL0qDJfN3AE3UcdzuybDhTgpc8qtY3kytBmfoMZID11a0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=HPlZCclzaIqWhPmmuDMeos3lvS52c4BwVcIBBhhJhbTCyiV1tVXIZYCA7PX4d_59EMWJj4-XpTJFDGl8jgFsPev0LyT5w9Hbaa9VlYhrDIw1VJD35dMnoHW2tgohnntvafbEdI21o5C0Oz42HZCpRQkK-vmr_6AUlfDAw4EUg17BaS31HduwfOZdYi6knGisW8ZDP6zB8JPgU-8nneil2SfteabXsEsZLJAhytuClx5WPZUKHpZsE78HO7BMAHM0GdNfeGZUf60S9GpRCGYoNboxUjx0gBrDlQEsl_WMdOw6CuRYXSOs3TFOjey3NjkF6i18pGIWJERy9W8Io1YZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=HPlZCclzaIqWhPmmuDMeos3lvS52c4BwVcIBBhhJhbTCyiV1tVXIZYCA7PX4d_59EMWJj4-XpTJFDGl8jgFsPev0LyT5w9Hbaa9VlYhrDIw1VJD35dMnoHW2tgohnntvafbEdI21o5C0Oz42HZCpRQkK-vmr_6AUlfDAw4EUg17BaS31HduwfOZdYi6knGisW8ZDP6zB8JPgU-8nneil2SfteabXsEsZLJAhytuClx5WPZUKHpZsE78HO7BMAHM0GdNfeGZUf60S9GpRCGYoNboxUjx0gBrDlQEsl_WMdOw6CuRYXSOs3TFOjey3NjkF6i18pGIWJERy9W8Io1YZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLZTl5BPCfptmxQzS2Ws05JxrdrEMv-4lZUNfhGkNLNVATuktdvdHng-jjAc8EtiDHLcaDOcJylsHq7N2XW5_-B7LIt_X0lUBF49BgvLfqzYgOIvAs-262f3oHVqKCjAouCzdmf1adG5UmIkJ9O7nzOSCDRHKVRtee5aDmZ_vwL8gAIbiF77PZtRyGZ6TBWcdxviGa5kwCrDpnyHzS156f__zdZGoBdx46Tv_gJp4iSyAF8nGAxlY9Xj4TGLJhOCL7aBeo0TONMwHDTQBDfyCO_6QMlaM0Gg5XcvOF61GgbgDXt5XSbxGYtE5kS-tiMm1I3_fq39zXAkKGAt18KZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRqyBaIk6mgrKCMqEjIgmdOzzrY2Ai3yOnon-d-qABAps3UrR1PUZ5V2MXKPtVB1HA5fzgEqB8EBXLgS5cT9Av1UZnQDVWiI94JeGoftQ5vEcgI69qjhglh_0Bb036oyhzy5HwPKyUk3KGaVcu5V6e99kyhpYmP1VkiQTMyFsOmSogvMVjIcXPt6Fr4vYP1F_8fmvw_ItO2yE_oEh-gAS2Ur0PYhbya314JNPR5XU2vPmHJwB2rToGpBQIh1hHxeayRap0IzOvOoMPdFxBD3LfAggCn7YzruadR_yiWGU4J4Jyghyl58YX5MkbF2l5VzEgxFItXnKWHFLWQzt_PKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
