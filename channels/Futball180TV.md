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
<img src="https://cdn5.telesco.pe/file/LjwAqdJpD-VU8n7OPa7mlcD0QwIeaBwHB0IjWjKZCsDHbzNbEu_K4CrTJEjcAJo7AsvzpUh9dm8qxdG-gToMSxYMg2F8ZeEUQMHUsWRUt3k_7Bov4aIkRCEor0euJ04_q2ewuwskDBrTpYeiQuNwsAeEzJF4rNg9ymkuArw6UcQuKI1sPPmF0u1dpIGmWyWWxUSn7SLDM8elQSGae8iC3qLkbVjlblQH5yiMot0tstTn0pvieItc98um3UUN9pVByULKkwKBLlPt11-xnZ03gmZxHOQIyDmGtpw-XzomcKTHthc54qlYhxsmzDdJFJ8FLPwfiQqwapBvIt0eXfJeYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 441K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-104835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6HbXjYNXe4GVJwe0tjRfj-DvKoYSO9VmUKX0CMMi5GSg3o01O_vhvNrxE55cloV1x_lq3K3RuLEPPJvWrtbdrfggSzNPJp_Awle1F9lPjrJ1afPxjNUin6Yb89J3oC5RQZJCzcC9NMRpqdnUBm1F2-91SjiKPOddG5X0Ux0WHvRCaVGaxjVp3Wb5AxDwlpgUZwdalEkVUdC0RABhZCXBE-MlkU_XoT0u0_k9HwDbIssnL5VpDCwRh2QKJWr0sMoV9eEhr-TX7BTAfom-Q7M_ATgg_TZXPhcumRd420b_90ubrLxyKEMmUEUzMx-CjoKXpGeOZ3YmKzP5gzZF4e9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9zOeqSPy5L4TxzlHbF8t6SOrvgzbPzz3Zyh44ZAOXlwAZW0l-SfjZuMaTH11JohiBZE6bRiRLbO6sY0UUAgGqZYLcxheQzkQXWSF6v8c2Vh6VAk1EdxmW55hggcKMMYcYBuagkBm1sEF-P_mRFhlCuqFuGoxLX-UeX9Fmi6vDrmnc2EWl7KW4E4gNVJcCIclb1qeBB8RgsCwLMQ3M8ua-A0AZ-blfRHEc-CP_GTBbfjk43uxQpuGxOsnmxVr7NI8kXs4eeCrOBswHX21EG6VpM6tZ0kZAZgXyAd_zQij22p39IKFITSADnLm1nlIGHH5l8wO4CZxbNlcOJJs6O2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UddZEciMh34DGTzR3D3vbWpHTwWow7qTsim1mDiEXPfJmF3inGSypTJm0A5eJ_UUwsrl0Cia8wTvpvynesd90kFGXbXNDo7QyzBf41ePeRF7UwBLC448y8fG_phBrxmUyjaaBEmRSvGL1-3LhJDczqlfTFnxDIhwo-yo5R5_IQch_JEHhr_KGptRRTpoJryXjMxjQDRbw_pEl3lh9gzPWdcf7X3NoaVxbyAwFeKSECbeG1j9KZEhJCMjCTdDMoVMPaJgUR9AElpzr3y4QeCSpK3u2mkDFs6sV2ABphTeCwb91bhgArfPQoTzVowUMNCMLz7E7C4_t_jXSRKZJrbV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUdtwFrFDchY1B_gWvlbg1bmYdC_PQtz9o4_auXfABN9Opfa93J0hJQ6NPjryCNeUqeIyg7Txy0R7FE6KT__irkYJn_j9hrTeOQhZ63sKuw79KY8O5OIHAJEdztpPVicU8nSr6_hlkCQeIhaWPedY54nHgBT61LDrM17C_g9ncldtFH1-IDRhnFxO6dF40dlSJGftgAjc3Q_PIcbdf4KHKwMNLIJlznEYgSszoLfaUagyYOENs0VOdfC8HE_jKdGk4RjqGWONRIk4MHWZZt751GJ2g0WDd493vx-g-7Q4cn0WHgZr7g82L5AV9Ww5mCFRBUJgU6J9MJyKynmrOW94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEITWyTk_etaLlCJjOxMDK-Dvf-Uvk2PAtOETFRUcZsAu0S4MU7SnBju6wbQ62e5do9Hy-kVih_KiMWUWhNEyFPzT2hfYQL9EYvQPLFyNacGzXWZEYYOS6gSpc0Hu58pRNR61T-GoiM0OZzigWv6xoHSqyzMk5jLBEqTgDOL2qEJmYJJEkZY5-X9BtFSynQ9PfJxpSzECZibjvLUUPkyy-acQD2dP4uQ4pj1MJIop3zmwye3RQVMKLom7Fx0p6OqzwZjl-qFFy_EHZgtU2l7waDTED3mA0LcpKkddBkEyXXJ_ijFgeashYocsu3Tu4kbeLde1ihpHwVPr1lhhV7k6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZzeD-xgTg_9sN5HNVmSSakme3NHXTToSqVgz6-2bZwq2QEsTpkELk8kq-sLJCWPOmfVB_GY-H4iL0Y0WhjNk5pj2l1_V2nlVltkmsImBl5bHketlhilBuJ_a7OvkxjWeY0e1C_jejA4w64s6NlGLOIOKGQVgDCPevaPUo3k0o3qdxMPK3e77RPr1oEZxmPYXnW32-Y6EcX6MwmDKG2WGvzC5KMBAoEboR5-holRwvgL6ygaanT2oVw7ReTd49TSu3yDMtUxcct9Env8GdXFdwAj3Z6pId3oZdpoDv9ro_4kxRCkCOaarjK10zjXglQnzlSR_zN2GPQl50MljAWXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7U72L7uG7D3oLzoMYg5la5m1bvZSlOSBN4koNPPOfT8CL3xGAfBhLTHTrWIIyW_EXooZOryuuhTxCpKFEWbiHKvRzxcT2eDJraECYxQQByNFsKTbKK0meBUQ8u35p3pmEL5s_ZHR-VVFyinqaNfNebhuweCRRmBNQ7KOliPDG0mtxlBDWqd9zytBuyidP4vlZsEDlg1hbLsWbCIib9fl9jBeO7hD-H1yEet8Ko9Gh7dxsPLoSGTscb1QJM4o-UFC0_SUHB9fCZtTX7snMaAWlqnjqru0a_T0qftTOGQkFACG2yAOvqFtqt54RV7-GB2wqNNmqqnKSmklQGE9o3vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSUXx4OY2mtDE7bKQ1dOmsnpCO4GDwqXk4cb1A5VNWjki_hoK6OB8AXfRwLSheEnZER3Jr7RU2mC7bc1uoXe7GBu1ejD2gr2KjoMp69kftEMbqlqzYRTPh6HcJfLtPHhCljAUhWyPmyZNdcxlIIOZwpqLaHXp9j-tzjUVD6SV03scG3URvcokVoWkr8hUrQu-7PPw7KPOBRvamDwYd5fazNn0CW0-nKsSPDDdTNaxnnYeVe2c1tt7yXe2WFRgETx6CtnzszxzETRX30yOiFYzEy8gmrTXEcOA8xlhzxX254s0twjoVXk3xNzJHe54K7pCPx10P1Q9L-KJMFFPrtNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CioWENemK6LXcB0aZGYrh32-YwTgnRMYvE0vxkL7JDuSYrM-o76RajE8JuwuMHgxsvuzo-G_qrG5oQgrM0h6S8QEiVmnVEtwk2MNCr5KDXh1EOD-6jink2Msw84HR3q8uGxdoRL_bMXEng3VyJvKMtoUUkAEuXTgEzxlOQvCwF7iDE3udvg242Tn8_hBw7MrSNQJ-fcFAYUTwXWRXFWo4PPGaSZrtOUPztt6nWqiL8312fFXe5X7j2COcBuXzVcx-aF8jZ33GqwFRiGEaAKZbIKQ0fdaMKLqV_3tyiea43sjUpXGLc2lxPC43tSKNHhlf1FmU95XoKAnwXKMqjOWPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/Futball180TV/104835" target="_blank">📅 20:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikb8X7BdP4NHB3SbOhLU4IuwssjtUBcyozE67uMoEId_OuPcp3sZqEjNzjKeYvwFm4pTzQDrGoQYnKOc_PrkZiV81nvs9O2l4wMrPxP06KyhiMEwf1CFFCJNWUIbcf_8fY1w0rKLFvu-o6PANOZSngSYkeyOApI6hlG2Jb44DC9zrAKHlGnvsYEb9rwrf1RruWATjrhQgkb1NIl1bdBsD29Apm0-mYQW-dRd0qcjRFZiGTUcjupsrKvVfVq9dK3fs4WBELTZ9J9XysK5evP2MAw4CnY5_rnWcKbF4pd3-5RfIG4yw4grTvtXGPpI7mVlzGBHPESpzeVdQDa90sVwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید دو در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/104834" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP3Izc-VUJ-VXydNQ2HU0HwC5PRSOZ_weiHYmznm0tv4Df-2NkMVVDd8Z4D0qJPVFfkXd4XuU4lrPtjdklv54pGeZbvyOVFI_OWy1BE3ylyd48jXbvxgPpahUKMgeUXjuchlEPAjlWQBFBAFuqY32WWXoNikikSWfE9Et6JpW9lFL2NjXsvEOPfdttMZdcjAY9ZMiLpG2zYf0mAj-uO-iSrRvDfXcdWEPcDPZlJp63nURU9ODCT5veH1xZgmRiCBZIwwkVjNTVjnCJCr1Or-kBHhHHqdU8UFfDXZ5WOkT19ugA78WczkIROIR3izRzRx7OKffTSyjcIyR3c9zdEbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
دیدار یوستی مدیر بارسلونا با رئیس اتلتیکو مادرید در حاشیه مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/104833" target="_blank">📅 20:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnQ8EAhXfEYNl_nzB3EqAaeioT_IHUtp2l0m5swGpGKIYgr964I3gEnB0w4yq8_LHzTtxzaBn2IuOFbPu3HDczfNPJDAuZWq6MxfBSG8NuVH8I9tp3RgMnHeIuj19rsdC0nLREXap2Rojyct0x10EY9PM3HVOjQ3Q6eFJw1PlzO-JOWNnQyOgikQS8_yVrD_eGtzYOrQt3ROX8h3304g_VwUhIjhugRlvMxN1SJXajMiyEUjJAwlyO2vkPoalHIu9WK0238yB2sE1g_Klgavr9u9-EGwvs5VY3EaUmPVhqCrcOWCEgpAaUt-hCGBvguT664OqvQbPSgtkOpc2mGAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/104832" target="_blank">📅 20:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOZ2lP5c_AGB8NpbB-MI1xTpG_BPqN5bp21zIehj6wUua0hsaFbMdPjavZjvb9FYdhwavq8Har7nvcemcQCynr_qXlDwg0E1N2sOcKtsNRS2EqLygR-BeooZfPEvV1gQBQfZ-kTSn21_XIW13VoGgZ681VTQPJBFmEaERKTltZLjGfPLCPH7yXC_Rg9P19cavbfzkvDBYcA2Ph8_bV-cTP-zOLBwjHxT1hzTL8XIysiygheu06QgYZxBiVCuSmYa0x-izyvHVsg_Oku5Hi48Lab_FXFL_Mg5Qv5f5yDF69o1YmHYs_lgND2Rhd8xPoimKvvITW9jy_cevpFCon-PVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری
#رسمیییییی
برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/104830" target="_blank">📅 20:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liA23FDLqz1KYuj2UagVSAF_9-Ho3j51_gHsvqOxyiGo--poQC8knkHOMXgH92zXpZ3W167Z8P8TEs_ykUagQDHd_-plG-l8_j85oWad-MX5ttIMgoSXANcDS-9KztsnuiMtQ-gkazd7YHhx_G0F_3YnGFKoJERgQY52WKcJizxJiz_VsJbnot61kNKWDozsFzNttkqMH0gpvg3ITMpJOrD5VCgDjTajv50QNyB7MQIdQo5jNd8F4XM22f-oGd50gq7INX9nSdgEoJb7Wq377iEXf0iR67NzCQgsErgSdG-KUSvTW51DjP6n5pmT5y4OmY63rrrzI68nl4ruTLgF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇩🇪
بازی‌های بایرن‌مونیخ
اتلتیکومادرید و آرسنال رقبای سید یک باواریایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/104829" target="_blank">📅 20:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMzf9sxZcv_IMQZsX5sGUCn752nih-YYz_YP691wEBHvNcAPafoPlEwPN-QmtIK34G8q2XBXIuye1JY54qdhahZsGDJjfsd0iUX51tpGkdw7HEE1FBO6m0EiZTpCqY2kl7AT0pIO-eYhBzcDN8cXyvEtNBqXy-K1U6vWKVfokut1n8jRIGbYRmaKLKZCcjDrTFM4tHoUkaGHu0j7egbfQVF9MaRjOtUPHGyJLb5wPTPphfq56T2pjGyQuiM4J8VJcSzGSCZfiA18EM9EiExAQJXPQ7KIUgOO_KhmHDjQcCPeYtgZiuG9wMrOXdJasDuTn-90BMUqMeaSRM9Rf2ZMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برنامه مسابقات آرسنال
تقابل با رئال‌مادرید و بایرن‌مونیخ از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/104828" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrbTXXu0DlL_ZMNmjrnSzERVl7RGx9P3_pDryI83uWmVTQn2Z15unuQ1DJfPbJkM79wa-HPmn2FYJ8_BdhQdt_MC66BPUW00lArx1u3lAijdHyEWdb82YeyjSbD44TciCH8cfvr3PreFT0XA0GPFQymm5BDSgMCSjAAniI98qKx4aGiGNmgRF1wMWOF64fsZTc3Vh0ViqUvmiYmI53PjiKhrpaH7JBGT6kyMUZisNrgaFU81Uj-AqM-Ex5scS4UrmY9U1cB5TyeRwUjPOWmU04jzNd8Xh19mnbRosZP82w9DX4aMSAxh9CGNwyw0w2yDaGvKpFExnVQRAX5LKn4eTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات لیورپول
تقابل با اینتر و اتلتیکومادرید از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104827" target="_blank">📅 20:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jffh9BprqRpBnNyN04wSHrG06TzYblcznm38JHKVf9mzbEk_6cQrD2HH_cPbhmBgQQIxbCsBg96mQdDawzpSZBFqXp_7NtDP8PKm0HPb-Rw3w4gWEIebWGd4WqEsWs7hHwpVUQrQwYa5wg10GuzirC7Efm-FWlxWedKk6BAdCHzDiv-kb_d-jGlY43eQsxKT13SZagQheGa8j9AYOunOelvoqciMZmgufM4sisft4G3FmMw8weJU2oYaG1zLTfP7-wtDPIilkm_F3yrKs06IJHByuIBSeW0paVkmuKlwexlEPZzKXESrJIPofgOr4NVdC2PNsX20_O2tPeFL8kB5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇫🇷
برنامه مسابقات پاری‌سن‌ژرمن
🇪🇸
بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🇮🇹
رم
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇹🇷
گالاتاسرای
🇪🇸
ویارئال
🇮🇹
کومو
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104826" target="_blank">📅 20:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU0Oawwf8gde1Ic6j-7LJQXoI3QCgcdK9N24f9BdaCG9o-oU46YAsXSPUVNtIjgR6Pc8YRjuEN05phssiLzTIgieOx-pCCyOWgxGLQjr-s0b2ChALnv4lyETQssgXYwHj-tCEiq1ALJxtwxW9wI9Y1RbjAd_T2wIzdz9yL-GfbVgKWx8w2AmCIGeUVSNOYgupqrcmNLmY16d4J3rCtjRifJo7rbr3GCtfQ5BOzi4FPUesfg7ZE73UDGqaVk42N5417tqQK_qTaDDaIv22SlhbEnlM5epwvilmWnnE7r96Y_ofV0iJUfcCx_XLuGcrllKervW-HnuJjRJKjr0sSMETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏆
برنامه مسابقات اتلتیکومادرید
🇩🇪
بایرن مونیخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🇳🇱
ایندوهوفن
🇹🇷
فنرباخچه
🇳🇴
بودو
🇳🇴
وایکینگ
🇩🇪
اشتوتگارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104825" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/104824" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ileBGbQ5-5EHXuPzn2NVozik4WK8g3iRMyVeV54XSZJcM6sYw713T7dZxzhOMcHlsCGb7GPF4-aeeyFz8io1Q3Uor48hQOvsMJh1gk5O4c8zws-bSVhb2Taq25kdpBJCZk41gJ6icYJCwQVxW6KxdzA8OIVr6OCvF8JFbweirHq0KhEWug6kMWNMjXwvBS__xxJrHkGcLZ1TlwV3evDPJGkkRTk_GDy0PcjTDiGKhjHvuYvvHLlH_GgkGh3gBWusMThoeipQeYMoocTPANU-JS0gUdp6MEdM5hvdfNuo-AecPBg8mhRds52Xjj9RBjWaMLQSn3pEcLCVpU2xovuslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/104823" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpNDatCGVp29qdHXfdYv9dk0PKnnENebnnFQ6kNFS9F1HVT1s5Suoj4_5Ljv-LwSiypjQuQwutKHqsR5inwl35z7Ikyz0kqCV-KsRR_cjMhdfk2sA1fSJ-1_KHszxTY0eBgou_wBjZcIaPhT0i6GV1cqfYpgOcyReJBKdxAxlLUhcbk3d7Q7UTKZjg3qMjrK8d_F05XNK-fVC1J3GoWi_MWCp9ntj2lOo06NuqY2V8YcLUJ-j0N-81YlNjUOnGp0CQUGcv4MBhJo78MzJLB54CuGycqRgrpCvq6dD-07zrgq6f5Uh-jkRqYQZbFj5IsZYbWb8YYafXEkRMROLm-6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇮🇹
برنامه مسابقات اینتر
🇪🇸
رئال مادرید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🇧🇪
کلوب بروخه
🇩🇪
دورتموند
🇺🇦
شاختار
🇳🇱
فاینورد
🇩🇪
اشتوتگارت
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/104822" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/104821" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFo1E28_1C8lsURnnVqElIe3ZaZOsJEiJdQFZzAauMTCzOwtJ4ETc0JkZEvUM9Tnn0vbMKORqw-YgbWfw2SGgZFConn236z1zjhh918jtXcapXhhpAIDZHe_2rcSohru9tyxpxqUgBEY7YtvN3h7PNbm9dORV6zOiQtGLttClMDUacnx5hZiBJqY2cr8RXnF6nP6L5nE5aTvR4G24Sm-uIfaBwFRRPf8_BcxBFaO5SIFAQPDKYOyZpjGiyOX2YSdlpFn8ZRVSs9WC7VlP5D2kdxMHep8HkwnN66OAMUMyG4BJKXkntUX_vkNdqKopQARSbg-WnpdzcXrPlA-icLxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن
لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/104820" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXmhmD_IVeJh-ByK56Q_LdFrL_et9WNC8o8vDgVh-G8ECkYzm83vbB799Ic8Rqu6ju8-4JUI2NaooneRjNUHpZ8sgdsoHmJFqXBguHCSk1CMbxpKrMxbcUc4X4-Duy-4rlSE_s9Zw0aMXJJprbTa1i6Wfea39QiAnX6dR9wdeD-jUd2EPAlL_qKSfKQ8yRp4WYbtfaY1s4BVfo8vphjHJRvas_NJfoDCyE5soYSq0cAhKiykL7FQ1136m3QkpwUJxBIbyENrvdRsn1PUMvO2liX1TNO7-EYEetMMYyTBw5wp2mtbrUarwNzpiWp64P3sZoOEh1-HK2qp7Y3q5fwk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏆
برنامه مسابقات رئال‌مادرید
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇳🇱
آیندهوون
🇮🇹
رم
🇩🇪
لایپزیگ
🇺🇦
شاختار
🇦🇹
لاسک
🇬🇷
آتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/104819" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
رئال‌مادرید</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/104818" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🏆
معرفی تیم‌ها شرررروع شددددددد</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/104817" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/104816" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIumOR0O5zZ_vOa6-vBAKcZjYTALeHPbt0EKDslOb69ZHZAqHOssCc4AekPHJ_Gmr8RloD_eetTMvg6PovHuvsvcIkGY5JWDtXGVBqT0ruTEKZwhD7fm1-4kaWRHXgrenE-DK8QPq60VH_BKWbdy1e-1hpFOsnRKhm5xFvSoIj77UMBGGVScm03Eo-5vOJ-Dp4a6HCtidOWGVcCGiyIJ0yrDvUSVR6p9W6jqv0h-QDu33WUYslzatkbd-wg3t3bFR8q1n2g_W-INwDq5TQJ2PFQVjCakFBfJrw7QmL4dr1Mn0lvepBBR8YjBYF6Rf4BxOtxSGhMo4ixvfIGPQkOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
شررررروووووع شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/104815" target="_blank">📅 19:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⁉️
🇪🇺
سؤال مجری از دیوید ویا: احساس شما در لحظه‌ای که در سال 2011 با بارسلونا قهرمان لیگ قهرمانان اروپا شدید، چه بود؟ چه چیزی باعث درخشش بارسلونا در آن زمان شد؟
🗣️
🇪🇸
دیوید‌ ویا: در یک‌کلمه بخواهم بگویم لیونل‌مسی بود. همین برای یک‌تیم کافی‌ست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/104814" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seI7DVkFoE02R_HCoZbZ11SKY6LAq-ZOBucALGADL9QAclZ90wZ--isj79qz-YtUs61-S_uqcovp6MK4GLDim7PHZ9qMqpIPgDHABtyzn8rrgf99kpuU0rSd8hOM7XNcalUuUVRVS8FcFRnZ1pufQYr6RZGUbn-MOYNrH9oCHH3De5C2gcOW7jIzeMwPIZAT5nT5wAsTkVkjxgEJCMGGMcsSxsmbbBJ6gtzjC8mlp91ZrgIkCJg8ldUYkvbserTFMF0owqbbteW-rPADVM0EnBwY11jHc_NMoLPSc4oLMWjf8QzIjDKadlCyUhc2ryMtALy9sufn74TbBE2o9_faIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
‼️
یوفا اعلام کرد که از این به بعد، صحنه‌های مشابه خطای هند مارک پوبیل در بازی مقابل بارسلونا در فصل‌گذشته، به‌صورت دائمی از این فصل پنالتی اعلام خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/104813" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll_gHZRYfkiBQQ1xycTj41kBl2S-KStLDZm9vUz5hVgpufzvVRevbiLEh_Bnc3omUMYeS-4Aaq4sQusZXYlC-YTO2UnSO0IU8eyuQ_mVoGQyGrcAMvgtcwz92AJHb3H5cjbLx0-3SZk_-P6CJhpQcmWpn0TQ8l8yY-TEnTCUqLjZYL9naTxAnfY85zayxFIiy8TJqpAhwijkQt8FxQgy43L_BTk7nArmGlqU38830GVMQcxaZJq1N7oGQfFzCVgFAg70ogV46BcbjaGigC0qh-IdWZzKFReiw8a8sJlNmLeN5ZjRD4R_vrqxxQqaEZ6j01gAgkx7DAQa_UZ8ed9Bdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیری‌آنری هم این وسط یه جایزه گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/104812" target="_blank">📅 19:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYJ62_ZvxQh0oW0OaLu03OXpVU7as52bafJl-c-lI_efVfP6XTIAh73s1BPREy8OHVF8dY8wAhKUsz5dhbZMTPGxDDMIEaS3UpS8qtMApYLZufdreUBRBwz09QW9deUy8KboPrTCMNsr70Nak12eZGFVAOjdt7Yl4gqrSlFR68AjuMmoQ0KxvuPlveeWe3XMv1z4hPzlDe3r2UkJODCsceahKhHVqBKrGCxPgAjQU8eazeJn3aOcB01B06o6cXHcowDQokPcUtnfyHPD2Knkpckpwtsu-L3BAspm_eA_RrLd6HWpg4z32cv1-a29zMunlwdBh70j8Tcwwo_DWf1iYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇫🇷
مارکینیوش کاپیتان پاری‌سن‌ژرمن برنده جایزه سال از سوی رئیس یوفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/104811" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CugfP-U5v-Iz8h4ISHJVcZfIP04raWxi7-0O7QfndtJb9iSYUrk5aB9JsjeaRUjPs2AytruB_yMrEkG-gcXoLJhQMKIDMjS6Djvx62CBvXs2KdQtG76VaT0lAqUyCak4Sn_OK2eK4BT9B1OzuJ8J_xmkgp_m0TAqbM60fwz5j4px-OzFGH3ROvEAlGalMnxXLgy2NfGmlDWbolggSFdCW3kukLFD0PcacxW8E_jRXsJki7yVQ-HcYliF69JPsQrQEANtr_EjaI_kUILxSM_w9do50R_kNMG2cM8aC76Ki0HpAT4iLozAoJzsbtnMQRtrhsczd7R3YjFYc3xhgxlXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه‌کشی آغاز شد. با ما همراه باشید
❤️
🔥</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/104810" target="_blank">📅 19:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/104809" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=joLo_kNAhBzH18XzPRqT6Sc4a_vdjrKIEUdXGivk17qf-o4U9B8vOVRWYcQoXc2JTfJosoe8iJH5FiwOqvIVIYNS93CjfH2rWZaym3j15oBH0kFiDffmwqT02Kkh_MUvYQ4yci2NtDfwtr3x3GGZlZuUytvEEkPTHGlOXoCGVBfR1X8SAnKpGVsGsGtJMtX_FncQV6pbT32KxRPgrJ951ha6NnMkimuQWxKcoK4VW0xn7Nc_34b9VX42q5l7y-hNFczx92l3K5wh4vEC6VcLYwHbVU68Eh-etRuu_b4zVGtH3Vr3nPlelaHkEq06EqRDa6MBqbVvi8nGWhSGrH_nbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=joLo_kNAhBzH18XzPRqT6Sc4a_vdjrKIEUdXGivk17qf-o4U9B8vOVRWYcQoXc2JTfJosoe8iJH5FiwOqvIVIYNS93CjfH2rWZaym3j15oBH0kFiDffmwqT02Kkh_MUvYQ4yci2NtDfwtr3x3GGZlZuUytvEEkPTHGlOXoCGVBfR1X8SAnKpGVsGsGtJMtX_FncQV6pbT32KxRPgrJ951ha6NnMkimuQWxKcoK4VW0xn7Nc_34b9VX42q5l7y-hNFczx92l3K5wh4vEC6VcLYwHbVU68Eh-etRuu_b4zVGtH3Vr3nPlelaHkEq06EqRDa6MBqbVvi8nGWhSGrH_nbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
تنها ۲۰ دقیقه تا شروع قرعه‌کشی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/104808" target="_blank">📅 19:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNkflNxwF0GnuFEzLYbkgJmgoR9K1oU_1CQjN3HbLluubMD88jTTSxYs6iCILT_KoofaVf6kBOwzFaJf6njhEFXgaTsnqIaSmUZFHN6MVNVmvqGYgkTl5rtMhfAnEWXgtONvX0_dQHThkZfQvlQH2MKeMY3bBKiRvV9or1Ep6fVMMVBCfPgTTseEfyd_Apc8oVBuMLfMoT3BksZJs9p21AVRq2527bYmifB16MUG50f5_zDsVSR8x-qVoeqGSDAWG1MRVaTqvvwlplDQOrymPTBmvHLUUvSpclPm_ELmRXc5lN4lQzbwkvWk24L7hixD4zDSfYFNf0rshJcLHpcBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDC1TtqPIyn7mXikYREVw959ni8bwVg9jf9XkleGqPde8xNybQ8keA51WLgLAFgE84DoV7atDEx8iqNNPFWs50ErbvwLXcE8jvkER4vjGnI_Ud7B6gPHW_wPYhvmLfSDKqda_pZ-BhfVi9UsYTVlD77xAXTqQylKQptPk2M6EkHq5YwhJwvtp1Um13Xr1BA7BgAxNVBl7npAfeuYM6zDysKWswoFkYWXCRZ9Tk3_Z75fc7cfHBMxeFZQLVKyBED6ff47qo1ptu2owpT9T1ndPeg3W1SkPc5QY5_lgc8JcZ2p4Trrj2i-6B1HgEgdow7n8JhFSlIMzY0Halwwubp7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbOTjLttd3NTo6r6qKJYbfX5IWPoVE3AejH83GytXDZkl3UU2Td0Saq3SJsZ-AWk9iZJm9OsgsHsB9w8ZcGZhuOn9kJpg74gnToC4vbIgWW41KOPJYLaAEtSnem_ZiI5eyxdbZLc1sxqxFGeU7YM6EOBC2NgwJEZ7Y7gWSXYs-5vKdJQ3SgptYMN-T72gTG2gbbdJBLtORaJIopZNn2ycQbTz6nZWrWGtuu22qTJeOEyh8BYjTH0q66ngyt4hAyF2_no-q-teaJiraQN627YbT1RbRfiCNj0jy6WIoYkj8d3Bw8vDQcuxJYE5DZ3BU5fujyVAZot12Q_Rjbm-Kb0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxsPmn9eFp_TJjSngbW0hbMxDpICWLCr1N2V4FLfJ6SgMuPRIOdAiJNinwUxYd7JP4EsnkYeHgCjdgHptNuciq0CZphsMVisopsRMvGptL_jlbXgHTQBn-xpkf4uJ71Vgz55y--z34wvpjU83pgfB5VS_21d3KjVLJh7MT3wFPgVHuhAH3ngKd0UQenXdG2qjeWO_xW6mgV_xYPguu6L-pUxkuoE4VK5VUv8O9-4gM9cyV9nRg8oP5P76_EfgJNtWORpDtBhr9rE1XMRAKxXtzuZgHbwwyWDwUJ9LZujPks3QGk8hQa9YV6Jxussr4q-5LPH6U7FBDwoI_aQggmNHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/104804" target="_blank">📅 19:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVyvqyrXCAt7iGCXJck84AcQ8lcUAIvXifcIle_7rN6RQDnV1jjyEhftIlnOPvcTYeMz-EVCJGhOBpcdlAfK12uraH0IiHoZ9W9YsB_Z2h9auU9JJEWW4bmykPJ_H154FexUzpBnPkEVdmjUigHaPM-36HPIWuYnOHeCcn9fFH1sdl_bTjvy4TUQiw0y00k1_bMTLXJYjnK5wKUAS0aMFNjjIFDfN28fHaqtxv2HOLArpbJd_r22jhs_UJsJNjIDtTmpuOD9AOZKsnen0HcB09HJaXQ_1-J40vqAyMA_jri3OUBNMxB1vFwOFBF2TIDlCBQ1DGOX7P-Kjjw87M_AsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/104803" target="_blank">📅 19:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=hd4iSgXQN0KcuJns8AO9_98WXpjrilemgk9uRns8L55JkJ0hURTsrqgRQDck9qs8lFfmQgOyQmMA7d-ctL42Jtz3A7Hb5NsVoha7n7mlcAoiqhw92Lk3guUZK-_i3oK4V6SRLBzGcXr6B67tlfnsXtIKXu7VBT2fu-d-ytu6_OYebnHrNKZxakbn_QzL7xi6kMX_005Ii49VTsCFTc70fyMhk76YDFJ-s4ahn7vBLUkQW9mc1g2o0pjLIrKF0iOJus5rq5NhAqkb4Ncj-Pr7xVYDblZIKJepdUIflcgObcv_swbuxs8wzZxEFmS-x_8kEnnZYtHPllqlywd_fPRhtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=hd4iSgXQN0KcuJns8AO9_98WXpjrilemgk9uRns8L55JkJ0hURTsrqgRQDck9qs8lFfmQgOyQmMA7d-ctL42Jtz3A7Hb5NsVoha7n7mlcAoiqhw92Lk3guUZK-_i3oK4V6SRLBzGcXr6B67tlfnsXtIKXu7VBT2fu-d-ytu6_OYebnHrNKZxakbn_QzL7xi6kMX_005Ii49VTsCFTc70fyMhk76YDFJ-s4ahn7vBLUkQW9mc1g2o0pjLIrKF0iOJus5rq5NhAqkb4Ncj-Pr7xVYDblZIKJepdUIflcgObcv_swbuxs8wzZxEFmS-x_8kEnnZYtHPllqlywd_fPRhtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
آغاز جنجال در اهواز؛ به گفته هواداران استقلال، لیدرهای فولاد شدیدا آبی‌ها رو‌ برای حضور احتمالی در استادیوم در بازی فرداشب تهدید کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/104802" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
✍️
سامی‌مقبل روزنامه‌نگار انگلیسی:
🇪🇸
اتلتیکومادرید سه روز پیش به آلوارز گفته که بارسا سرش گِرده و از خیالش بیا بیرون
🇪🇸
آلوارز هم از طرفی گفته یا بارسا یا هیچکس به همین دلیل سه روزه خودشو به مریضی زده و تمرین نمیکنه
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال و اتلتیکو توافق خوبی…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/104801" target="_blank">📅 18:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=IYJ-marflOPFHG14ywafmDtzgkdI0-JE9lNGofqiMp0uM7X0cRYnV5rvlJtYMia5To2yNfqZ-s4iplVoGatH9KkaR6FpfV-2aE62WqLV3vI4OVkf0U84t3igoKp5-SEvadlQ3KiWUBsJWE2Q66ceQy7SAlMpPPPR9XxZNmgfHRoWr8FLjBr5h_E39otH6hxbGxPFvBfZquQMN_e1GR55taKOq63WKR3tBxxl8x0r0VuBpRz1wITGk-aBMaptSIu0lPh4a3g6tsf_3ZYdUUNNmRWUiv-m8OsC-SG6BnJMATk1a8279Wg-o8kShGi0tMOePZEu6cVbb9nJLRUFooOw7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=IYJ-marflOPFHG14ywafmDtzgkdI0-JE9lNGofqiMp0uM7X0cRYnV5rvlJtYMia5To2yNfqZ-s4iplVoGatH9KkaR6FpfV-2aE62WqLV3vI4OVkf0U84t3igoKp5-SEvadlQ3KiWUBsJWE2Q66ceQy7SAlMpPPPR9XxZNmgfHRoWr8FLjBr5h_E39otH6hxbGxPFvBfZquQMN_e1GR55taKOq63WKR3tBxxl8x0r0VuBpRz1wITGk-aBMaptSIu0lPh4a3g6tsf_3ZYdUUNNmRWUiv-m8OsC-SG6BnJMATk1a8279Wg-o8kShGi0tMOePZEu6cVbb9nJLRUFooOw7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختراع زبان جدید توسط علی‌منصور در الطلبه
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/104800" target="_blank">📅 18:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kche4CryXIYPJhJDBbhN4iFyDy9Tt7W0r_0xFI6QLrHd17z8hE3itoWFBzvuSP8kz00g6xz3UzB88fAHMFHk73Fq7qn31dLshnEe59fpzqkeZjMH9KjcLYop-MZxq9cCc8hJ-EWv9rYnDuR4qQuc8whojU5j7Xir8pHo2ByUfiAHuTZHDoc9o3f3DEhu8U0p5yayBrlPJI82wSzB9NAK_-KJOyz3IB74MphD3QwH_WgEsgttbFDDHu1DSphjGWtTrb6JVJOdhPuDR2m5eBrtuQgWEo8hWabnal2Rv_Wgp8vXnD1cnbGlSDyA_kQ8b0_yECVSfyYNgLSMoxXWT9amsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه رکورد پرتغال: رافائل لیائو با رد پیشنهاد گالاتاسرای به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/104799" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
از عجایبی که فقط در خاورمیانه میشه دید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/104798" target="_blank">📅 18:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBQqj-m8pU8OCQlB-fYuUB5WUIVHUgBreK2-wgrCm3jQjY5p0D50bg1EUA4mhP4Wsw9uDwSW5rOL5SKCk3YA2T5SBbWYuuIRwb0crYaQridIJ9N-WugYyQhGbTWdiyE8OT-fIUWB7gq0OA3LI32RxDcrZOq6FttKZPHVyNkYTOsPIJhAB_2weyLx4HOXV7KJHrEQ-VsvFkkE7CvYwtevMig8G5kzuwyjqvMP5NCZUUBVaq8z_Yc0_eawYycaFIkDEO539G9lHAULQsu8cmShgWO2ELOpWECip15Uk9QEkhumR-mZR-7MdJttpF2Y6i86696Cc2DGRUz3LBHa6npD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✍️
سامی‌مقبل روزنامه‌نگار انگلیسی
:
🇪🇸
اتلتیکومادرید سه روز پیش به آلوارز گفته که بارسا سرش گِرده و از خیالش بیا بیرون
🇪🇸
آلوارز هم از طرفی گفته یا بارسا یا هیچکس به همین دلیل سه روزه خودشو به مریضی زده و تمرین نمیکنه
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال و اتلتیکو توافق خوبی دارن و به محض دریافت چراغ سبز از بازیکن خیلی زود شاهد توافق‌نهایی دو باشگاه بر سر آلوارز هستیم اما بازیکن تا این لحظه شدیدا مقاومت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104797" target="_blank">📅 18:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=awwv1aH0Vu1VUhBiI_nFKihWj3kn_4X8RxetYjkHOeJuylq2VGRkoaF8wMisnodPZsFljmMicDBGN2G89h7dCyXkVuB9AXlCWiHpKsQFiCcZ2VagpbO5CBMzJ3Q27VNH7PPpKIe_WaYmiSFfoYluYoZ7m9OmDI_w9bBX-sFjEbqPunnSZmlAH9deAMNotf33X28aXxbqimVD-7MMGUNgyK-0lkEarZw0xbjutOpv6Px_wTBGunW9_tlBJNqZI5oeEGKyszWGyUYJ633PjcHwgBX9GovVswC6PlozEC1AOtJdCWvlO6-XbgSlQLHvVovyMDrDOh1AijMzpD8mev4Ljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=awwv1aH0Vu1VUhBiI_nFKihWj3kn_4X8RxetYjkHOeJuylq2VGRkoaF8wMisnodPZsFljmMicDBGN2G89h7dCyXkVuB9AXlCWiHpKsQFiCcZ2VagpbO5CBMzJ3Q27VNH7PPpKIe_WaYmiSFfoYluYoZ7m9OmDI_w9bBX-sFjEbqPunnSZmlAH9deAMNotf33X28aXxbqimVD-7MMGUNgyK-0lkEarZw0xbjutOpv6Px_wTBGunW9_tlBJNqZI5oeEGKyszWGyUYJ633PjcHwgBX9GovVswC6PlozEC1AOtJdCWvlO6-XbgSlQLHvVovyMDrDOh1AijMzpD8mev4Ljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104796" target="_blank">📅 18:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCxrC-gxFC_53Kg3dP2jGEtjeXtDeCjlq_qAOAci0FX0507lDwQZ-Fdtm1VSEGeeetVnuLfjiUEMQIOVZHIsA09bg2k_5irbt5pIb2MtKasGPwvRk_y-qLxXx9bUCWEctuZHYLyM8tVZfCk5QKr6Kq9AZL2itTveSdnmO_EvJQG6KdUL30GLgtLUkY09uhmL9NcZ7NC-svZaCj5aJ1DMPugXaYj9wIbjqWuB6Csll2KDz4dPrEAdUpb1rRAEovFdVQexFe5OeW6Jos1c9wgl9rBT8nGNhYfIzvCmwyMxcrx4REus2PvWIuoLttG6BwzpMf2dt7OFrbr5dD4pYReHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ عمر‌‌مرموش با عقد قراردادی قرضی با بند خرید اجباری به تاتنهام پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104795" target="_blank">📅 17:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQWC81339Jw9qoulfq4QPtYHcYBZIf7UMkWbk9rGvkBV5FX6Acb9m1xQfdiiP8tzpn1H1287dHB5x3zE_7jZaY5H7eUo-Jg-_oY96D1HInJs8Jt4hAh49j5GChuSiN40AUH48Ib4yzSutKCsrafC1i8q-WhJyU_YoT-Ac1RdkVl0ddZTlZfnLNLe0cLiKI-0xSv4oZiyNHVLwaPP5LZzMIIUx_6bSHd8EHs_PmRDNvfKpAImHP9bgw4oInWsoHUbpZsu9ll-YLF7b4PYKlREkrVZSmFwOaV_HaF7fOxh-4FSkHeZ73Fa3lROmRibHZxvJtuOXGiWOHN3g-ek8ox0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🟠
پوستر فولاد خوزستان با تصویر رامین‌ رضاییان برای دیدار‌ فرداشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104794" target="_blank">📅 17:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ-EqX3hEi3lFm3pC-b6Liyc3D5lsaOSE6ADa_-onT3SnxHytsrtRO8f-RYuoil35fyA4z8IbDjT3q5U3A3zluAYMR8oVV_Xzco16D82Pl8CBBq-AxcGCb_dCOMYJ2D6ME4Xr0PdyullBhsYnhVnvz-gMGIaKjrsOHzpyyPYu69sRrxxuC5MKvIuJjvPtNjrtgbcWClbDB_p-UlVWACMf3aLPq5FNJeeBpkKTlsuoypSm4t2IJwzmTdTgNOQdgHXPlnqDApcwzhAu1kXrCmqyMQMxBnWZDiyzynafuByXrf-X1Lvzh7NxXMmfTgGDS48NuZrmZ1hIZDFE1R7UML3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ عمر‌‌مرموش با عقد قراردادی قرضی با بند خرید اجباری به تاتنهام پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104793" target="_blank">📅 17:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmeEbpitN8ZLYGX3jelIm1JHc5-Tog14LUKUd_ojSABxGOHQRabSgpa00Ap4SyyuoU4073GV3_u74EoRoBqlVYouqPXsQnuPItPGAqlfX0kf_siv51nXfzELUx_aI-KRLyIhh8KOhKB__5XZFfn_AwyF-d72Pn4ksNbxeuNp-Xii2OFHdSfBuzk-tUc4ymYzh5WNy14P_neX1ExPkdoy5PqrAPuaqkn-4HS519IxgAjBxsjPHbTWX7NXwUc3ne2gNeEW6HckOn1p4za-c1GqF6HTFA9Pf1yXXf5hCnPQcVJVAJeFuJqT-AI0eonre3Ka17CXrNZ9bj9LogIFrWogwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✅
🇪🇺
سالن محل‌برگزاری قرعه‌کشی لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104792" target="_blank">📅 17:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3180f2f4cb.mp4?token=t-Nl9rDHOADi311S09IaYUslWSbAjLag8SBbITQg9RlYmZgTkl7g1jGaqT5hSaOmNE3qwfCn1N0yYfHCkkPagmnCMyeo7PZ6oRmuUvbpuam4XL3M0IH8_1NK8EW_1Ex6Hoyzr6hBX1PKFBHiMjV4xQsvNiGVpSHN5_R-GwRcO_Q0WkNpyzD5oQDrJym13IuoiVDm9U7reI22DIfsG2JVqAc-kUCRI1qRA5OfqkudTTS10KzuX7rxLrqltFVUJtoLlwZqcu9cDDVhaMPM7DoGiJH89uMVriXAHyrhLXDNlCXOEkZPtisbvgkvMXdWMZjdjY-K23agCnHWSb2_VY9hBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3180f2f4cb.mp4?token=t-Nl9rDHOADi311S09IaYUslWSbAjLag8SBbITQg9RlYmZgTkl7g1jGaqT5hSaOmNE3qwfCn1N0yYfHCkkPagmnCMyeo7PZ6oRmuUvbpuam4XL3M0IH8_1NK8EW_1Ex6Hoyzr6hBX1PKFBHiMjV4xQsvNiGVpSHN5_R-GwRcO_Q0WkNpyzD5oQDrJym13IuoiVDm9U7reI22DIfsG2JVqAc-kUCRI1qRA5OfqkudTTS10KzuX7rxLrqltFVUJtoLlwZqcu9cDDVhaMPM7DoGiJH89uMVriXAHyrhLXDNlCXOEkZPtisbvgkvMXdWMZjdjY-K23agCnHWSb2_VY9hBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکلات خاص در‌ ورزشگاه‌های ایران؛ ورود آقایان با شلوارک ممنوع!!
🚫
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104791" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104790">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3g6OC3W_MtTRxzZNdm-Y-lTWdroR0M7T3WoL1a6fiyOUeiFFKjtradPd8pkd4ixios28t6WmviarJzkp_GIJ3kpeezsk8HAknF0wiJ70VuaweLKtGy_sq-jJ96AjedCp2A__Ms3Knj09SYAkt-r8mra2RiOakQB_1ErEUxkWpZnQlTTJdx8DBOQjUvG17y456COQ87BA_dJiTTT5syROtyYn-le5rMS_N58bR5spWozSXF-gRze57E6CM3WmBdsAAb2d2HAuMFnsU59GJt7woiHMEh0UNJMzUpAEm4Vx8CDTPhVztqOF-hokl_szzfCArykSJu2tp3w1T0PJ7Vc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104790" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd2815717.mp4?token=luJKY4ON-8rD3QPtiAAgE9VjcXbZkfyGMVZ4ArlEfjQw1png3MGCI3R5nb7dCiVn0QOvYRt8YGBI9Fm2GvBLmpqG2EG3CyD6P9nG2Qrln993Kx-MMU7EPkeRnbDPGBmbw1A0aU0gS95qr9Q8YxOdvZI8fZeeSqU6gsY7xHMlY--WyP4sfaBXEWxOL9DUYsZ4aQWHGFZw0-VeUHmbMutsSaQ7bZ2apGOVa6pTrsBNaX0fPwpE0CZicEZNuF2chABoRM1e98xgcNW0K43ik_r2KNRZNVgv9R_D8eOlbcSelQtI9XHk4pOfiPt60dlwRD7_ProARBM_0P38bNnTJlW7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd2815717.mp4?token=luJKY4ON-8rD3QPtiAAgE9VjcXbZkfyGMVZ4ArlEfjQw1png3MGCI3R5nb7dCiVn0QOvYRt8YGBI9Fm2GvBLmpqG2EG3CyD6P9nG2Qrln993Kx-MMU7EPkeRnbDPGBmbw1A0aU0gS95qr9Q8YxOdvZI8fZeeSqU6gsY7xHMlY--WyP4sfaBXEWxOL9DUYsZ4aQWHGFZw0-VeUHmbMutsSaQ7bZ2apGOVa6pTrsBNaX0fPwpE0CZicEZNuF2chABoRM1e98xgcNW0K43ik_r2KNRZNVgv9R_D8eOlbcSelQtI9XHk4pOfiPt60dlwRD7_ProARBM_0P38bNnTJlW7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
طنز تلخ از وضعیت اقتصاد مملکت
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104789" target="_blank">📅 16:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104788">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2ffd8aad.mp4?token=Vp_2KE7sGa4mubv86vJBJTgLfeiHgLUzwG_qYQHnM9u7JsyShqiI-HUWiByvT_GarfykHn4hxwBfP2l2JG28AzhiW0T04dv1NDk5vRM84SlW-T2S6Hb4HtME6BdebonkZNXLpHeaaBLXirDVXmQ07-jJ7Yi22LhRqPb7zVVc9ZevMW2y586tzpFL2ptXWIJbv89CXIWoHUVYild7MApwGL0R50jjGqZNCOcUGU720F26N-3zTunhtVo8fyxDMHQFPhi_XqQhXbM_HfO_H_e4QHMTzsix01pvqtec2j_PkH6kjHDn1W1EP6GXnFvMVn7jKSkcUnjuM1A8EqnLnt8A6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2ffd8aad.mp4?token=Vp_2KE7sGa4mubv86vJBJTgLfeiHgLUzwG_qYQHnM9u7JsyShqiI-HUWiByvT_GarfykHn4hxwBfP2l2JG28AzhiW0T04dv1NDk5vRM84SlW-T2S6Hb4HtME6BdebonkZNXLpHeaaBLXirDVXmQ07-jJ7Yi22LhRqPb7zVVc9ZevMW2y586tzpFL2ptXWIJbv89CXIWoHUVYild7MApwGL0R50jjGqZNCOcUGU720F26N-3zTunhtVo8fyxDMHQFPhi_XqQhXbM_HfO_H_e4QHMTzsix01pvqtec2j_PkH6kjHDn1W1EP6GXnFvMVn7jKSkcUnjuM1A8EqnLnt8A6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماستانتانو در اولین بازی بعد جدایی از رئال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104788" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104787">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2544620852.mp4?token=KcteFYrIqzpBjZPpa9_gkcR2VAfWaIvu8GPlqYlF_HzMKujh0LeQAqpj_JX3GwP53pE7Z8kel8czTU0S2gDIkUlwkj42pckEBXame6MH1COA9DXh_r2xphfy_Kcix0Ohq3rIWfrG6kV7lxMJTCSIKA0zm6c4lyFSCrsBc8PO7syaG1jl6RjP8DZCnd6WWZoYmPBQm214s3b5BUiCu_JWlG3pM_1sBAKDorg44txFMKRl9vdvUVQTp7S6bPNdWvBEtaWOD3H6mp3AESo7IZ6BWrsLIaUN6IA2_A01o486gdiMSUt7O6D3GB-o29Z63mM4N_ksKPlsN3CAqfV1SK5LIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2544620852.mp4?token=KcteFYrIqzpBjZPpa9_gkcR2VAfWaIvu8GPlqYlF_HzMKujh0LeQAqpj_JX3GwP53pE7Z8kel8czTU0S2gDIkUlwkj42pckEBXame6MH1COA9DXh_r2xphfy_Kcix0Ohq3rIWfrG6kV7lxMJTCSIKA0zm6c4lyFSCrsBc8PO7syaG1jl6RjP8DZCnd6WWZoYmPBQm214s3b5BUiCu_JWlG3pM_1sBAKDorg44txFMKRl9vdvUVQTp7S6bPNdWvBEtaWOD3H6mp3AESo7IZ6BWrsLIaUN6IA2_A01o486gdiMSUt7O6D3GB-o29Z63mM4N_ksKPlsN3CAqfV1SK5LIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی که دیروز توی نپال اومده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104787" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104786">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ccdfab76.mp4?token=MwcexonuyEwP-jR_TiZsnOch_Sp3j7RYYzOGndyeIzM9vtJr_OqE7YaK3pEjOEfbIYRMQVE9hOKSaF5RKE0_2el18oEHYJ0ncnje03dBB8oW4bKcD7QVQTLczICbVV9pRBpMxtIrJaltsnfG2dZaUkN-8tPFnRNgQJ4qfb2phbMOG8iBoOX0tszNhsCSbsNec1v756QdrPqI17JJ5CklgfhLnskNWck-krdl23y23sV0NbJUpzn-U9LWUTzqKgZ4e-NJaboEPfsEcgedL4vOuPgYi36ZVRqDXm34uxeeOzzomznOby3__mre_T5FV0KTC2ZB-e6QKAuAxeFmttor8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ccdfab76.mp4?token=MwcexonuyEwP-jR_TiZsnOch_Sp3j7RYYzOGndyeIzM9vtJr_OqE7YaK3pEjOEfbIYRMQVE9hOKSaF5RKE0_2el18oEHYJ0ncnje03dBB8oW4bKcD7QVQTLczICbVV9pRBpMxtIrJaltsnfG2dZaUkN-8tPFnRNgQJ4qfb2phbMOG8iBoOX0tszNhsCSbsNec1v756QdrPqI17JJ5CklgfhLnskNWck-krdl23y23sV0NbJUpzn-U9LWUTzqKgZ4e-NJaboEPfsEcgedL4vOuPgYi36ZVRqDXm34uxeeOzzomznOby3__mre_T5FV0KTC2ZB-e6QKAuAxeFmttor8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
خولیان‌آلوارز در قفس آهنین خیل‌مارین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104786" target="_blank">📅 15:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZcxtAeyt4L1javC0cHR-Dk0dFF_7bY70H-GJxJ0I-MDdSdAvEhLGaxTx9BAqERPGwFtzYEHZrINIZqXRy2srmbiuJxu8xRJeVb-6t6nBnq8ipIwwMLZyDi1bpnbRBJgjJsp8b8ZkIYQDQuCt-nDiSe4bLaaR-keJ6FUzkK_bLSW-k78Z8uESyo1qAyIDL-mB07bJSkHMrv8272E_ks3YQU75gt1qz5ESEMKYb2fIgpxD6FKODyHBaz4E7RoQQeJPDBxnccRlt9WXxKpjhrWEMr5APBlNLqNKM6ueiN3qJ7vIIGopc4stdmGVSnMSs1SNFE4XSviNYF4B_e6ANBEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شماره بازیکنای بارسا تو فصل جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104785" target="_blank">📅 15:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEy-bqkG0ZLr3ktEq1nFNVg9m-Gk2ifBTLuZCw3KoQ8cMam_fwecOM1kOY1nO9OmG9eWUYw7LrSW96J1beU1G0hB5FAn2paVmFxN8IprKaAv_FheZOFT0o1Ou3b3KIfaGoBaBwc2UtLEB-ixVqUJgkfRTs6LBuOn0pfU5XHn2HlXNRPCyh_U9p-G7lzGTy-EdH4sQG1j6CMv9b2XgCfDS4TsQjPQ-ZpR7VnUPL51XpNbXMBePENq_MXySSrqcrkNvreCjn4gJws6OvklsdOo3B3QietzB6gmDuasOhSlzg0aAwiAXUAxdJcFvZVeNxGrhqxRfhhMpOWj33NENXIMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
سهراب بختیاری‌زاده بهترین شروع استقلال در تاریخ لیگ‌برتر رو به ثبت رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104784" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104783">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf1idu0qK1XSIFVcG1Yq_KVXbsP2lVTuDsnnGkwkCypOY-bbbEadgxqm6uDYnb_SDZbKOH4pTJvh7c-U4itrRQ7SVsd7efEWhv3x0ja2QiLUToNs7Shq4APrFUNWKLP1LhVGHDA7oCT5dX6HErp2gAGLBmmylFWBJzRPAauQ7h5LmMliTzksWUwn46qATZg29t5x4Tud3P880IMDZ0cgiW1fMgFHM_2mZufLCYdnc6nxPOEkyHP5fbBdBLtsPKWz6L9VBSZCGBuW9sD_r9hGivLvr0mbYwJYi1QPuQ8NfpHAXWKX6zkbQ4Jiw9VZtpr2ljRyLaW_ilqM9mHeZoOw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی امشب مقابل بیلبائو با حضور رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104783" target="_blank">📅 14:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104782">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ced5cf8b4.mp4?token=St4WYj-FhL3yAmNKBI44hlvELB1lEEv2sFwC9QkLiECaokMASwYitHm-N4ks5ea8G6u5x4p0RdLxCN9wiHTPStAsKpuio5-HuTv5Jx6wpBOi5Y1aZ1IL9w5hiPahFdp9mz8fBGBS-w6AurkV_Fy0EzilqMbSFCn0bl0a9BDXjQDnFAvnpgFjH7k-sqjVx8ULslplbq6y1NJWgkIQwwpaFFXK0Su-fm4dERnmlhp8KcWiy3kqxXfrKaCkD5TcZhSBVDOhiqe3fsZDI-tZ5gFIDRx1bjHUwA5A9af3jOBaFYZ01cqKy-SHPYBftvTSIa79MiTqbe9uDwiMGV8uwtyarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ced5cf8b4.mp4?token=St4WYj-FhL3yAmNKBI44hlvELB1lEEv2sFwC9QkLiECaokMASwYitHm-N4ks5ea8G6u5x4p0RdLxCN9wiHTPStAsKpuio5-HuTv5Jx6wpBOi5Y1aZ1IL9w5hiPahFdp9mz8fBGBS-w6AurkV_Fy0EzilqMbSFCn0bl0a9BDXjQDnFAvnpgFjH7k-sqjVx8ULslplbq6y1NJWgkIQwwpaFFXK0Su-fm4dERnmlhp8KcWiy3kqxXfrKaCkD5TcZhSBVDOhiqe3fsZDI-tZ5gFIDRx1bjHUwA5A9af3jOBaFYZ01cqKy-SHPYBftvTSIa79MiTqbe9uDwiMGV8uwtyarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
انگولو‌ کانته دوست‌داشتنی دیشب اینقدر بکیرش بود که وسط زد و خورد بازیکنای فنرباغچه و‌ لیون حاضر نشد و راهشو کشید رفت سمت رختکن
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104782" target="_blank">📅 14:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104781">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ72_kZeVtswVtfhhIf35u2PwZLPB8y-jGAJ-WgRI6nUQqytXU27tAWNJR5Eue02xrLLN5alO7GaceaKCtdMpgNFXm8j3XWdUHs52fxKp7t4SSbMzsGEohrsw6jpD-F6ZTCXlf-xiDT41KuOMT7J2-kIisw_ucvvWT_dABEDl8UZPRXYIPPQ5IlDx1ToJUdxjUjFw1VOloWf0jtwNlB8SWzemyejZUnL9D_0bl_rJwnobe-_fKIqYpQmuYcJG276epUeNAQl8rH1KoU13UttjiwB667des--veAtDt9nqrod1HS3elc6uwwzfKsesvbx_XuSvO-oZQdIjBOyQwB6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇺
🔻
ورزشگاه اسپاتیفای‌نیوکمپ‌گزینه اصلی یوفا‌ برای میزبانی فینال لیگ‌قهرمانان ۲۰۲۹ هست و حدود دو هفته دیگه به‌صورت رسمی اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104781" target="_blank">📅 14:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104780">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=DkFSlvvjcSONbJkdEQV936uFipwAnNDVlb3C8dUjBLIa-YDa9mR8h-UuDjZ-VPebAMfmrdCWHhDNzUKoSMsmEvX_TuIwjlXIGEEC9G1wswyIy3gkifieuoaEVuwrBIcSWAmIN2JrEqBLLeEx7vsK14H6NPwAejToW-xxcJyrWZhZXtKx3LXEixtwS6SvaOBru_hHmWTaXwG9csvR1UoF8tvOXNIYFVAV5mYqtaO4U7VX6HYDVALW469ceWA5FgngwN1W0V7xIUnBNOh3JHFhTKWwRgSUqxHAmYq2prF4sBm-0EHp7Kw7ijRRTSLBndnoYQd_gobcE2bviiZsXOgYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=DkFSlvvjcSONbJkdEQV936uFipwAnNDVlb3C8dUjBLIa-YDa9mR8h-UuDjZ-VPebAMfmrdCWHhDNzUKoSMsmEvX_TuIwjlXIGEEC9G1wswyIy3gkifieuoaEVuwrBIcSWAmIN2JrEqBLLeEx7vsK14H6NPwAejToW-xxcJyrWZhZXtKx3LXEixtwS6SvaOBru_hHmWTaXwG9csvR1UoF8tvOXNIYFVAV5mYqtaO4U7VX6HYDVALW469ceWA5FgngwN1W0V7xIUnBNOh3JHFhTKWwRgSUqxHAmYq2prF4sBm-0EHp7Kw7ijRRTSLBndnoYQd_gobcE2bviiZsXOgYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤡
تحلیل‌ عالی و‌ شنیدنی یکی از حامیان حکومت: ارزش دلار هر روز داره بالاتر میره و پول ما بی ارزش میشه، اما این به نفع ماست! اون فرد خارجی بیشتر محصولات مارو میخره، در نتیجه تولید بیشتر، بیکاری کمتر و تورم مهار میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104780" target="_blank">📅 14:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6a68d1e3.mp4?token=JOIMFcMpvuD0jImH7B1adS457KXn6h8sPPupXoEXBPUOSuPogd0d_MKAA1V_kTA3voFJPHoDZ6zpDd5uE7bK6F1_82ZeLRED1GGnptK4KJDq9UGGQzaBQy2-yv52dDYr-fNkI1jWhaELcGNE0_Rz0hHPalnr9EgdWl_exGhoQtNbXwdLHyj60VWSqArOASwNRBtosqjB4BYPXeEz7ZcHmjORIJnY8AHXqxmgKynlYq-Ss9IzED2_4tmWXg6lEXT8ScaebgFnWiRxO1hZd_uN10jSzwh2qv6k7x62O5tir1Wbwr7QAB8E9e5NlfdKHbmeBHgs0TrHphauV2oJUu-s4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6a68d1e3.mp4?token=JOIMFcMpvuD0jImH7B1adS457KXn6h8sPPupXoEXBPUOSuPogd0d_MKAA1V_kTA3voFJPHoDZ6zpDd5uE7bK6F1_82ZeLRED1GGnptK4KJDq9UGGQzaBQy2-yv52dDYr-fNkI1jWhaELcGNE0_Rz0hHPalnr9EgdWl_exGhoQtNbXwdLHyj60VWSqArOASwNRBtosqjB4BYPXeEz7ZcHmjORIJnY8AHXqxmgKynlYq-Ss9IzED2_4tmWXg6lEXT8ScaebgFnWiRxO1hZd_uN10jSzwh2qv6k7x62O5tir1Wbwr7QAB8E9e5NlfdKHbmeBHgs0TrHphauV2oJUu-s4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👍
بازیکنان لیل‌فرانسه این‌شکلی و‌ خوشکل با ایوب‌ بوعدی بازیکن جدید منچسترسیتی خداحافظی کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104779" target="_blank">📅 13:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104778">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGPjZoAppF1enXTG7GpkQL7y15wA7uWN7MmaNBPyoaltPbHrfcwprapUz5IoYChdCegftCFeadV_Mu1rfUzsTzcGqVpZ682Imvm4tGjSBLI0DxIfTc9CZQLzPbsbp_SksSg6ocKWnqiUjl1cNOu0drluHCRh2s0Qn1egDcNSbGiDS-dgamFVJT1sBU2h5021e1Midh1xFTM6PTnGviT1RWj9fTgsH9SyVxa1FteNTWAS9eXdiXbmWyTV-IQK9pqnh_oetpm-bT_J-zXZTe7PNZ62KnXbCIB8zBOBjQSfPgFXtzVxvBQvmlma4sLn1C8XG3qMotSfXv_nR3LvNH79OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ورزشگاه بصره عراق به عنوان میزبان بازی‌های استقلال در آسیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104778" target="_blank">📅 13:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104777">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh9OokFWzDRDmUle7w6SBfKEEI9WhuzfkncIHm0LYHO-luXo2l3KHthEw840Q0BuSjmSkubtOnC1qHuDRsHl2-KWkk3cpi78Txe4Gns5EpEOR1sFuHq1XCF7NLWiD2MIHbTCyErbMuitEJRxPABfaA0lQUIwjZvqyQ3mR5dQcvPj5JqHwI-YK2Kc17T2Xpw2RrWSiiaQKZyec-rwVr-9dRGpHiEIOy4pIJoOo0YY_wCItms-D1GHIYI-4u0kR9LakUs-9Yct11QQ3JTdV0CxQrCufaxpXfCDx-rcg8CnxIjYykt00mEoEJDA1CYK-bmBfAwRzZZK6FguIDruzMW5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
و
#رسمیییییی
؛
✅
لیواکوویچ سنگربان تیم‌ملی کرواسی با عقد قراردادی تا سال ۲۰۳۰ به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104777" target="_blank">📅 13:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104776">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfLf_t4drdqcFXuQyi_cDv-mMcwcG6c8pIbhUZY4Xf62SxQoiiOriGxQBlSoeuisD_s9r-H94oqxBkxmkJ0oNR5_WtbgnFQk2j9s4yGCvlzyCE_0qSre76214UrNXvggA65srWPTMNPvVY2QgtBPpfACYpdfDwSl87O1mA44zQkNJkG5jaEIWCS1N8gEbYXOtXslGsNKBw49uHA78wHErW_u_JTOfokHGT3DklWIuc4IrHwOBFZA1MaOJo2gFrtTOnyf8GmjsHqmysz93bURe6TpOE3lWREGXBKROCIHOKEzJH6AVQMOyZfLvwh-eJwit9rEywM_O_Xilv_gfRiEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خط‌حمله ۵۰۰ میلیون یورویی لیورپول
🇸🇪
الکساندر ایساک — 145 میلیون یورو
🇩🇪
فلوریان ویرتز— 136 میلیون یورو
🇫🇷
هوگو اکتیکه — 95 میلیون یورو
🇫🇷
بردلی‌بارکولا —  135میلیون یورو
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104776" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104775">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIZ6n-MgoWn0BB8GkqQG6Rijsne5feHcJiZkxUWubAyYcaN44xJ-YIvKNiX6DgvBZhWjf17tkxa7CjaDBJvn1QahFgwwQNwLTrcP5aWx5V1gd5YyNrJcGrFotkE2veBrWSrUElD7Z93yNPnfVkK6dWjBS497bG7_U-4Aguj3jsCn8r2XEwkbvwi38BQj8cA5xab0wvzDZ5-qUsiiyKej098ynB-7-SHG1fiKhDn17tE9uHr9AKCNA1wyPkR_mtraz3SlqxOuSstIpwdGePIK2wkker_UmsAkAXw1D1PEVaduBSOATMC0bxdRba1RAEMgmZ8Ty1Hj7hajwfiGjNxW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
اوسکار‌ناسی مدافع ۲۱ ساله گرانادا با عقد قراردادی به رئال‌مادرید پیوست. این بازیکن جوان قراره در تیم رئال کاستیا فعالیت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104775" target="_blank">📅 13:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104774">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODAI716qZbrnJV4X25HlUxp8xSIgBa1cjIzYBzwXQQwDNyrFJNLzm4gQr65wJ9fjfVvtiN0J3fAqq3oXBdvpY8G2ql91a3mRyCTUBJln8NJ5OjkLutS1IxVGpTaIv6UBpf8NpLY1quMU8XZ4fkkyO1EJgtedFWNwOgCJOpjHIq_JQBrffVk4ZfG-EQCQElNR1nLHqAQjwK2hNDsc6WUl76OvhAmrZlLhnq20Mk2SPZRIevb917nu1i2oz7fNL6dvasFk6zhPIWCe5vpYnayt1lFTOWK-Gs8Y4K8sTTNraU4Gmtw6pVzA-TroHB2hQeKOiVTExlvMLptqJiNIinQHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم سکسی فصل‌جاری منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104774" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecd32f7a0.mp4?token=GHItSyOsZWxCrAc2tyU6Q93DVLtkucg2_yRSRE1tdSdU09kvUsPO_HoTPuUpIn1CAqtwQTEscq5Tu_AC6buGjDak9eI-RXRdpXYSVBK0yeoyjUljgAsNYFCLh_-IKf1COg9cIpmS2IK4OyOtRDrcxHot2s0aqoyufJVnmFOQhUVwWbnAMbWCAJuhLAC8UZKZMLKfFpWHh33x_7fVhnSZ5uyGLuN47_9JhNYeU7htIoZkPwOAXJD4Wctn_x8Apv-1rYpoVVuDxeh72USJmbA9TWNJRlUG3eGpAjL7jUCp6VFcAg0k4Aq5GRqChq8Su0_GcQNFYpmo430kLKvcUeAu_r2KNhJRSFkkdeWzQV_ebMD4-n42-8kv02FIzuTFAT-ggTCZFrJAuJllcvVVY5LwL-A-lieNVOZ2_kVqQdEhI2MLxZObHR7xwP2Xa-eBNKQFXduOFMyYjGYTv1XiRikrEoeGoHLxZDnXpfeDR1yHQRXpWXgVu0ComVOnq4TYuYA3mi4dUjixaswG0fBCffImBp3t4xV9G4yM3AQCpAgPHgOAzOKY0Fn7n1qzFusV_Pfc5VjO2IqBq_wFnORBHYZKXVShS7CrArckAHlpHMyzoepP0inNuw5PgAyGkfHwfjf3PkweqNwIpMURecOb68aY598unNAVTRHF2urMWkdY1vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecd32f7a0.mp4?token=GHItSyOsZWxCrAc2tyU6Q93DVLtkucg2_yRSRE1tdSdU09kvUsPO_HoTPuUpIn1CAqtwQTEscq5Tu_AC6buGjDak9eI-RXRdpXYSVBK0yeoyjUljgAsNYFCLh_-IKf1COg9cIpmS2IK4OyOtRDrcxHot2s0aqoyufJVnmFOQhUVwWbnAMbWCAJuhLAC8UZKZMLKfFpWHh33x_7fVhnSZ5uyGLuN47_9JhNYeU7htIoZkPwOAXJD4Wctn_x8Apv-1rYpoVVuDxeh72USJmbA9TWNJRlUG3eGpAjL7jUCp6VFcAg0k4Aq5GRqChq8Su0_GcQNFYpmo430kLKvcUeAu_r2KNhJRSFkkdeWzQV_ebMD4-n42-8kv02FIzuTFAT-ggTCZFrJAuJllcvVVY5LwL-A-lieNVOZ2_kVqQdEhI2MLxZObHR7xwP2Xa-eBNKQFXduOFMyYjGYTv1XiRikrEoeGoHLxZDnXpfeDR1yHQRXpWXgVu0ComVOnq4TYuYA3mi4dUjixaswG0fBCffImBp3t4xV9G4yM3AQCpAgPHgOAzOKY0Fn7n1qzFusV_Pfc5VjO2IqBq_wFnORBHYZKXVShS7CrArckAHlpHMyzoepP0inNuw5PgAyGkfHwfjf3PkweqNwIpMURecOb68aY598unNAVTRHF2urMWkdY1vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ریشه اختلافات وحید رضایی و پیروز قربانی که باعث درگیری خشن در بازی اخیر آلومینیوم مقابل شمس‌آذر قزوین شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104773" target="_blank">📅 12:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec217fba.mp4?token=lw5qw4tCDaxHXSIKSWBJzwJiJaFo5V1eI7k_KQZ-Fi8i3tvs-Vz5r2MAm2Wez-VpNljGHOqSYEIPFnXJD5TB7swcMBS7KnB2PqNe_rpXTt6IcT-ZdIryDKkB0feV8tCEZ1p4gVGfniWAOs616hYTcbxuYkXb9vky49ZUmnOfpkyURrf1cy7aGji2R6BQbJUyzEYnM3urG1q5o7_ncTl2YdmemJ69RsYb9UehNyPtkrFfrmnNAfJUAgics_oLyMEVc0c33SWAtywTQPpFJ61GxWW3BaCLJwAXThntgtfaEtWlhlf5QEg8vhcV_28R3W1sy5oTk0ntbE4fkNY5QIZAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec217fba.mp4?token=lw5qw4tCDaxHXSIKSWBJzwJiJaFo5V1eI7k_KQZ-Fi8i3tvs-Vz5r2MAm2Wez-VpNljGHOqSYEIPFnXJD5TB7swcMBS7KnB2PqNe_rpXTt6IcT-ZdIryDKkB0feV8tCEZ1p4gVGfniWAOs616hYTcbxuYkXb9vky49ZUmnOfpkyURrf1cy7aGji2R6BQbJUyzEYnM3urG1q5o7_ncTl2YdmemJ69RsYb9UehNyPtkrFfrmnNAfJUAgics_oLyMEVc0c33SWAtywTQPpFJ61GxWW3BaCLJwAXThntgtfaEtWlhlf5QEg8vhcV_28R3W1sy5oTk0ntbE4fkNY5QIZAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
خبرنگار: امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣
🎙
ژوزه مورینیو: من ۴۰ گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104772" target="_blank">📅 12:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcRr1KnBpHRzGdPg7IVk-BazQjWJPVqzU7_XH4UOsQLVdJarwvlDSvWANWS4dT90fnJEKLqxeegbWgFly2RYT0is0mKERvhFqVx8lE9eLeVmTrisvUXYVgZYS8OX-0GcA26lS-ZO6Dw8F2EufClLpUkb4dTRZ53ECmoWgrvGLxI1QNPDDByybR1qoaPspWmb3qXwkVyReSga1R4f6lAcMvxRGd6THjtVS_ieeszXT-7-jAODvTyyhPJmICJE5EkkQ7hra0Mp3PDqcKVFCQdg_mavegmffo9aAwi3FiaMlBSbs_72tozRIJffUlAO6YxYPBMTNw1AJDZA-Zc5Diarng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
متئو‌ مورتو و دیوید اورنشتین: انتقال بارکولا به لیورپول با رقم ۱۰۰ میلیون پوند خالص به علاوه ۲۰ میلیون پوند پاداش نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104771" target="_blank">📅 12:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La8KTnJ55r7_fWSAUUXLJgx3js8SPdwKSfr67VwowO0DzjpoZuSgVWiwDry0c8eySNEpmgPkUSfKoIFrfIA4y7CgH18iGCCL2ulB9XM9Upn5QKmqs6iXZgEGUmj5-Rw2WF8UJ8CkOrp2sKwfsr_pg4mMTebjpiVX0AtHTbuUCUdq2e88fPkwNyc0dFzLD3JYr_amxl-x_ipzlwUNG2L1lCmdBDTZPTk7WSFuvDafhL7GUuc6WRvdduHlZDyfM2pKHzSj5Zt8VK0hnsK2KBRjEjgivxOwmajjQvqsxkwO2WuK94Gg1CZwTHhPtw2K8HI8mp19YvtPSaoMXBj3cGHCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
توییت جدید علی کریمی: دیگه از هیچ شخصی یا حزب سیاسی حمایت نمی‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104770" target="_blank">📅 11:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsAwOvn8iFlIaE6C-pyaMTVylxFWoe_f8U8x4Mb5iG4ywzhbVw5emizfcBi33oc_GAGJApJ8Cy7YI8_BX6hP0LQuWn751OlFGLKg3qbO5Fmw67ZE-q36oe3S3Zq5LOTA0fksYAMVyvBMAwy0tIAuQfu3ZcKxFIp3CNRc4P2x4zueLeJpF1Zw5bAHDw9KdFO9MK5saRqwFCXl1Rrbr_Y_JfpEuEBML035bKrdHrgCIt--WyPpr7Ter6cqDCIkIx6VmpT2nLc2LIxxCo_v4aMzjrsI0DD985pJZEYrDlQgovAB8xO6-XdWWiGEp6KODhFyZ-SElhLI6H9HUS1JtRdrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
#فوووووری از رومانو: مذاکرات لیورپول با پاریس برای جذب بارکولا در مراحل نهایی قرار داره و بزودی شاهد توافق نهایی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104769" target="_blank">📅 11:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0d739a4.mp4?token=AKqoGd-GKjsImkGBo_K0gK7uPj9cDZ9UETGFiN8iZfMeXz15f1dwGOb0dFuVH-0hp2vaPEMiTfXmUXWoALcNceYDdO-10zHuyzgEI5OzxG3RrDQ4jsEy3qenUtjXn8cKPNdcwMR26VBkYFgf49ig5CB5B1Ix9H90b5D89JI-7dY91ZOv5CNztlKUE7XYVDn3EGPNRLn4d-B9bmZZvC0P3rVEZAdqycWsntW9NSxSbeaUCC5D2AckKZNx61RjYRxgQu4RQFrtOtDLAyEyRJbiNFlL91-bpnmXIffI0mHsxUIRXYcBj4HfqfE6B2DHCLInUMRbnyPYC12jjuo2N81KCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0d739a4.mp4?token=AKqoGd-GKjsImkGBo_K0gK7uPj9cDZ9UETGFiN8iZfMeXz15f1dwGOb0dFuVH-0hp2vaPEMiTfXmUXWoALcNceYDdO-10zHuyzgEI5OzxG3RrDQ4jsEy3qenUtjXn8cKPNdcwMR26VBkYFgf49ig5CB5B1Ix9H90b5D89JI-7dY91ZOv5CNztlKUE7XYVDn3EGPNRLn4d-B9bmZZvC0P3rVEZAdqycWsntW9NSxSbeaUCC5D2AckKZNx61RjYRxgQu4RQFrtOtDLAyEyRJbiNFlL91-bpnmXIffI0mHsxUIRXYcBj4HfqfE6B2DHCLInUMRbnyPYC12jjuo2N81KCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
احمد الشرع، رئیس جمهور سوریه، نخستین تراکنش پرداخت با VisaCard را پس از حذف رسمی نام سوریه از فهرست کشورهای حامی تروریسم انجام داد.
❌
ایالات متحده آمریکا، سوریه را از فهرست کشورهای حامی تروریسم خارج کرد؛ ایران، کوبا و کره شمالی همچنان در این فهرست قرار دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104768" target="_blank">📅 11:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AspJZZjBqvhGn8_nqB0TcqG02JiWObF-bI_NzjT1mHZi1-dr2CZhDid7uZPjm3jxIz_of9E0m6yIcR9A1BJk-Lik7hDW8BUd7uWB4ibWSfyxXK5Vme9ZKlmh7ZXy0A4Bfuyt_ovCbm7TO3087Rcc-OZJmoWkeyZLlz2GxJG751TDdf5su8rl8-RaZuvX3IYX5ZPWjxD5eFYHas5ZPkHKhHbynx_a3DVhBiLIur84qX2Xq6EmOzltnT9Lp0upWuQM0X3q_qu9BtpK0LS2tiFYJXeTpgYwPDvsTutOigoSxhUZCrRiRHXvf3OtejMnTidi3VRskj9w_wrVdc0VaeWInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
خولیان آلوارز برای دومین روز متوالی در تمرینات اتلتیکو مادرید شرکت نکرده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104767" target="_blank">📅 11:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dom2pcu-QpVxsdatYa-pZER5_b5n6WAstAx-PNPHQSofMXQ4QqqtCVnJYDCYKbXvxNhpMhfaDT8DzxtKaiBSHXTs_-duGEix05cXfiOI4I-RfzrIlvXQs5YNd5HCAkhqwQk8c4u4WCvfRCupmrsQDJyqY7T5DNrTZBIMyzX41IqwBGVoaS2xQc5cRe78qpTMZFaR9leIH40_fRHu-k-nSI-nk94ztX5qG4iNTYTnQUoptHJ9e3E6NfUcRTMgRPN1ZBt-XyvhtSH_q3aY64XdFUrvY1Ec1Q4BPvZox_zbMBNjWN6AfdBvj-DHghWyaVs-D3m3xbus_-T1r57iezYYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم این‌فصل لیورپول رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104766" target="_blank">📅 11:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6f45b735.mp4?token=SplvrUjgi2AkrxOd0dUVjbMZqlH12LDkJbZSUFLR1dFZ3rIPmvCVZykFpHjxS1TJrcxfwJvWcXuji0JdMTPIvt86uuyxylm1NC4u_TiYkU5PYlO67pxv8FcfSCaZVIZ71zRqF6CLeHyTZtRgvOiMQDkUiDUkoZebntbiVGez1g4P4ISqDm6eVScq3XioQHe5wBAzXO7FLHiDkEiGHYaNk4K6I02EDy9gKwDTwXSaCweVANety1KlKXtrEwkKWX0aavoyBxRerPY5n2YDyWcoVJvV_NgR1wveK68smNakbyoQM-3oIGw7BU1rW-iAQN6zKpmEJkxNZZezbT4wkmfpFbT2zeDsWUS9fGcsAQ6BUTBqcVcTQ2q9wY1CArDPQCNExCAMO74_FAIAP7ZHl4SbDUwUCBDM9FhcmtQ7-zAUM4Hhpb7M93XPxHRHjMHviGouiJRf24EXiawvHWHFN5laNgkX_hTOTjxLk5ok87G-wtZCtJVVN3Tr8CeN5wpxDYrBVuwQWAELpmL9EeURpgAL57XHQEcDRQgGJNGdJA9yaJk8PGjdMmHbNE9Siykl1oCJQWwdgDEQknBKVa-TOq4X5f88oSpcE5yHO1Q4McEI2tzylkP8cBMHjnVlBXeDZ6MsGOv7nwAtFA0XZ9aZhXTvAUrgdouXX7rknyOawKPSVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6f45b735.mp4?token=SplvrUjgi2AkrxOd0dUVjbMZqlH12LDkJbZSUFLR1dFZ3rIPmvCVZykFpHjxS1TJrcxfwJvWcXuji0JdMTPIvt86uuyxylm1NC4u_TiYkU5PYlO67pxv8FcfSCaZVIZ71zRqF6CLeHyTZtRgvOiMQDkUiDUkoZebntbiVGez1g4P4ISqDm6eVScq3XioQHe5wBAzXO7FLHiDkEiGHYaNk4K6I02EDy9gKwDTwXSaCweVANety1KlKXtrEwkKWX0aavoyBxRerPY5n2YDyWcoVJvV_NgR1wveK68smNakbyoQM-3oIGw7BU1rW-iAQN6zKpmEJkxNZZezbT4wkmfpFbT2zeDsWUS9fGcsAQ6BUTBqcVcTQ2q9wY1CArDPQCNExCAMO74_FAIAP7ZHl4SbDUwUCBDM9FhcmtQ7-zAUM4Hhpb7M93XPxHRHjMHviGouiJRf24EXiawvHWHFN5laNgkX_hTOTjxLk5ok87G-wtZCtJVVN3Tr8CeN5wpxDYrBVuwQWAELpmL9EeURpgAL57XHQEcDRQgGJNGdJA9yaJk8PGjdMmHbNE9Siykl1oCJQWwdgDEQknBKVa-TOq4X5f88oSpcE5yHO1Q4McEI2tzylkP8cBMHjnVlBXeDZ6MsGOv7nwAtFA0XZ9aZhXTvAUrgdouXX7rknyOawKPSVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇫🇷
استارت‌درگیری‌های دیشب بازی فنرباغچه و‌ لیون بخاطر این‌حرکات عجیب گندوزی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104765" target="_blank">📅 11:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e643c8e93.mp4?token=omz0mUtW2skUnTTF4aNSt_nRI6WZvcv3JAImc4CGWG-VDY6DUkGv8YoGNv6B7RuqqizDPMaH778ySAsRK_pwrSKTTreRd0JL9i-KjhNRpJ-X7WwqsHKdZY6OMYODx5VKQyFx8SBOoIeJAykKHx4L2vfOnCQvJvxzxHJ-rPN5sL8A2HuU6xm7LVfAC867CA1rXDmand9Hwl1Pw2gHKHRd5_8GQHFzxQRegMdgwzAp9G9DG1r58kGmhvJYqEcV89I60yhMGhfqXU7F4RZq-lOFHCelD4RnwAmPGFjwlr--HjH_jEQiPS_fYhT_MV7f0q-MZBCJK7Pc9Oaza-_yL3tFclesMh4E81mEahP6xPfezUPnMhZT9WAsZglAQnxBP26BmAMI9lWQOm0eLtsvF2TpC9vK9VVFH56N7xoRC1IcGrFpdVfWnSaaXOtyU6gaoVc-8Dw19ulmZzWBhXFj5IYSfQOtQhEt805mAQ080Srel75iY5s5SbRgeh0q4Il4Zdc9A5DZDEKP90YI9Xp9NW5sL2X3Q0Ga5tUIakPnH-t9RKSEM5LB47yzuASdcpQ2EGKf6LiQaTiObK2IEUFEf8RR6em4TuIT3688HeyWoAZCCuUzR97AvV0wy83SqxOVpZ3C3xZID6hXX37IepngEuoNeYJ_uY7muyJVOyGu3-7XhBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e643c8e93.mp4?token=omz0mUtW2skUnTTF4aNSt_nRI6WZvcv3JAImc4CGWG-VDY6DUkGv8YoGNv6B7RuqqizDPMaH778ySAsRK_pwrSKTTreRd0JL9i-KjhNRpJ-X7WwqsHKdZY6OMYODx5VKQyFx8SBOoIeJAykKHx4L2vfOnCQvJvxzxHJ-rPN5sL8A2HuU6xm7LVfAC867CA1rXDmand9Hwl1Pw2gHKHRd5_8GQHFzxQRegMdgwzAp9G9DG1r58kGmhvJYqEcV89I60yhMGhfqXU7F4RZq-lOFHCelD4RnwAmPGFjwlr--HjH_jEQiPS_fYhT_MV7f0q-MZBCJK7Pc9Oaza-_yL3tFclesMh4E81mEahP6xPfezUPnMhZT9WAsZglAQnxBP26BmAMI9lWQOm0eLtsvF2TpC9vK9VVFH56N7xoRC1IcGrFpdVfWnSaaXOtyU6gaoVc-8Dw19ulmZzWBhXFj5IYSfQOtQhEt805mAQ080Srel75iY5s5SbRgeh0q4Il4Zdc9A5DZDEKP90YI9Xp9NW5sL2X3Q0Ga5tUIakPnH-t9RKSEM5LB47yzuASdcpQ2EGKf6LiQaTiObK2IEUFEf8RR6em4TuIT3688HeyWoAZCCuUzR97AvV0wy83SqxOVpZ3C3xZID6hXX37IepngEuoNeYJ_uY7muyJVOyGu3-7XhBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
ویدیو سمی از اسطوره‌ها در کنکور امسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104764" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
🇪🇺
🇹🇷
صحبت‌های گندوزی درباره جنجال‌های دیشب پس از برتری مقابل لیون و صعود به UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104763" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d032145636.mp4?token=OJVreZnDhVMwwWrKySwkuvjhW17FhY6E1wXb5ATUhVrkgNZdargD-vQhNiubN_MXEg-ksmeZ_3xo1M8ZAki9InAt7VdW1_tGN-G9HNy8jjgFmH-lX5GPMiyl_5goWb1OXikek4NuR4skVCSzvbIl1ykCJ4CGy6Ggn6HqhbGzViD5uzuLvlgySoCmzQWmav_t1CzRriszog23WjqObcad7mTPORCmWF-X_puMe131WXaOhmHcNAZXCE-TaDE8WzEDnq6gRSVXMbkVWXNT0apyfWmBIP8E6IQM9MX03VqbfxEibY2zitlHDIdq0BSkXLDHWQxq4i7kforfwHTI-tvYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d032145636.mp4?token=OJVreZnDhVMwwWrKySwkuvjhW17FhY6E1wXb5ATUhVrkgNZdargD-vQhNiubN_MXEg-ksmeZ_3xo1M8ZAki9InAt7VdW1_tGN-G9HNy8jjgFmH-lX5GPMiyl_5goWb1OXikek4NuR4skVCSzvbIl1ykCJ4CGy6Ggn6HqhbGzViD5uzuLvlgySoCmzQWmav_t1CzRriszog23WjqObcad7mTPORCmWF-X_puMe131WXaOhmHcNAZXCE-TaDE8WzEDnq6gRSVXMbkVWXNT0apyfWmBIP8E6IQM9MX03VqbfxEibY2zitlHDIdq0BSkXLDHWQxq4i7kforfwHTI-tvYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
شروع تماشای چهره ترسناک و بی رحمِ رئال مادریدِ مورینیو.
☠️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104762" target="_blank">📅 10:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOI5PgQKx-kiqVzkcvdn4UUymcMhxDy1FEdnurVyE6e7rsYKFghSQy8tyHcmBA2DmT4nmLZdTT5saJ4smyjtyc0kiUA6rK2xt1zZ04QYTY2KW0MEqoNY84VNN8sZ181sEJCQZdVqizNRBe5QH1ViZEL8X8uP4BI2OVMheiwmnEUau6jc-MyA4O2t45kDsEY1uMRSXXO2wAdN-O-FO84PY9XP6IKUBL-VYe4eLr2dxDQC9p3g-aVzsnF-As1lMJNW83kxbz-6koZkSkVZG1zI3NkegQwm1nUbWEu-dKttDhHfXTnLjkQkVuLEsBHyJc0sH5MpLL_FVdz_mvwMHQjMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
#فوووووری
از رومانو: مذاکرات لیورپول با پاریس برای جذب بارکولا در مراحل نهایی قرار داره و بزودی شاهد توافق نهایی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104761" target="_blank">📅 09:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cd3fb6e5.mp4?token=jz9QzQ1IH_sB-h51uVSyEyHxGAJDVvxA5wAp2ECUqhBq4UblQJWVtpQc5PwwO20J9J37wrWxGjgxOMLKJ1wPryh_qxysdxT7hN_uFwBtKVKv1ckRU_s1DQs_I56H2fkoon_Sd9CIABec7kUPKz6uFMGc2AGVa1gbRBZXd8SpA41F0yx_yHx2w39t3dFTIRYXdWQDfyMjSP-pXofrEiUO7Exbkfo7HGsa1SNzPt62VtK5fdo9MOAw-ynLHO2nHY3q5-OqbUHRZEvf891EHOBFO9slsVol08yWEEOfAajwJofjo072CjbJXnLQqaXIvYikeCGt77qS1_HlXhJtXlKKUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cd3fb6e5.mp4?token=jz9QzQ1IH_sB-h51uVSyEyHxGAJDVvxA5wAp2ECUqhBq4UblQJWVtpQc5PwwO20J9J37wrWxGjgxOMLKJ1wPryh_qxysdxT7hN_uFwBtKVKv1ckRU_s1DQs_I56H2fkoon_Sd9CIABec7kUPKz6uFMGc2AGVa1gbRBZXd8SpA41F0yx_yHx2w39t3dFTIRYXdWQDfyMjSP-pXofrEiUO7Exbkfo7HGsa1SNzPt62VtK5fdo9MOAw-ynLHO2nHY3q5-OqbUHRZEvf891EHOBFO9slsVol08yWEEOfAajwJofjo072CjbJXnLQqaXIvYikeCGt77qS1_HlXhJtXlKKUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عشق‌به خدمت مثل هدایت‌ممبینی دلقک!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104760" target="_blank">📅 09:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LakkwyUkiBODt9TsNZO9HauxLP69WNQ5og6ENvpUnXi7OQk2MzM_0fjAha4ARFpRzQidZ8Kld65_TVhJQEWrncrLGYunOJsdf3fOyR_IjE62st_gF53GJuPSqM3oqwUMyyP2OUhqx01zJfIHCH_2PNaPgZhwTmC4qPPe7BZWCbUeabnXTkKaMNx6OUHJWk6V9QDm8VCYkehXQruGq9s61PWlSxi-lW-fOeRJ2rGKoqBkCtHeixKcrImr440r_D2VNO5fAmibFPRrLHYHi3yGzQPDb8ZAWT1twZtP5v1zz7EJ2rNKnWAk76PkVeI4l8q1QSZz9kg5Yux2EIPXW63K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
تمامی فروش‌های سیتیزن‌ها در نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104759" target="_blank">📅 09:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJOB0DUtTmXqjAkpVQ0_sIas26F_qK6x4d9FDhbmA0Tr3VavKg0S1Px6LK7Bisgp5t9oYclRE8608wag2d_qrd_VBh0CMM8Gqjdlv2lewA5xbU5MeFVnqcDADlFOQg2ciKldKsDKMiLfbH4C0BU1ZpyxtgZRDWY7mrzz7VDyk78YyzATDi-KZp1BorbxPrHkntl6n4DUOiv541qVQb8lbIzoXFwz6qNrIP5dId8Z3vydlmbVGXPYYLEF7EvQj7M8BIQtZorsFaTF7l-8B3sa-r8wwpF-TNOJ0HPomxh3ucj1v8vWR__YY0CTposSxeMxjB-7ncxp6owvUOE4WtcZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه Tala Radio ( نزدیک به اتلتیکو ):
⚽️
روایت اتلتیکو اینه که در ماه مارچ به خولیان گفتن حاضرن دستمزدش رو بالا ببرن و جزو پردرآمدترین‌های تیمش کنن. در عین حال، اگر می‌خواست جدا بشه، باید تا ۲۰ ژوئن پیشنهاد نقدی ۱۵۰ میلیون یورویی می‌آورد.
❓
اما چرا ۲۰ ژوئن؟ چون سال جام جهانی بود و ارزش بازیکنان افزایش پیدا می‌کرد. اگر قرار بود اتلتیکو دیگه روی خولیان حساب نکنه، باید پول و برنامه لازم برای مشخص کردن خریدهای بعدی را در اختیار می‌داشت.
❌
هیچ پیشنهادی با این مبلغ نرسید و بعدا بارسلونا با پیشنهاد ۹۰ میلیون + ۱۰ میلیون یورو پاداش وارد شد که قرار بود طی ۶ قسط در ۶ سال پرداخت بشه.
❗️
اتلتیکو معتقده خولیان توسط ایجنتش و بارسلونا تحت تاثیر قرار گرفته و ازش سوءاستفاده شده؛ برای همین می‌خواد با تمام قدرت جلوی انتقالش به بارسلونا رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104758" target="_blank">📅 02:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFSS8DMlr1vL4C6FYthngrRWiP63nQHxnEy76wqG6X6fopI7qKLq8qMRHewu86DqVvp4XDzyP0d19Qw3SvkmjdhRuCh3SEMDAyheUHkyqUxLPUE1KudiAxUVhIzlg54JthjAOHwJwlBNqt49qMK7dfgwus8kYZ1FJRmelDfQMiP0_3JXrLzv-2hbLocrsf40-lv0xhqmTjFRPmYNUYoIZgZLe8sSKZdJqd6u-K4KbEepB2PbPSJZjGGLZXNAk8tmr29Nv04yXM5Dk5BoLMdsjFNnQ1e0t2dYR5pUMd471wLe11NsDupObhOmOeUPJoNwLmlwibwhBt3pAdfL78OhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📅
در چنین روزی سال 2021
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه منچستر یونایتد اعلام کرد که با کریستیانو رونالدو، اسطوره پرتغالی، از باشگاه یوونتوس قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104757" target="_blank">📅 02:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy3APomPMg_PmQRy99UQoGxXG0mKJewR1Z74lX_9_njxYVgG9aqjf3VN16Q0rINwLCboyomAqwb1T0FH_q31636JRYQWEiYcgr5663-KH8pZzhjAG-7zFZiA63F3ks_upfGTRE7r0H5eiYE_KYN6kuUd9aYixb02O64XVDA-WXTq4s8LbrGslvu-Pd0GR40y8PLFEgPSe9LafM4_12L6gjE6FMhEsmHSHH10CzRDGmWDiVufuKG9iJVXfFKWyClLTbTr_ktdeYdxdhH7ZFQW5hhonRnLGHiqJSjyqsA1oXROCEBX5VcBPMltTv6HjftRR3ZAmtZDFjfQdNQCN_jE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇮🇹
#فوووووری
از یاگیز خبرنگار ترکیه‌ای: باشگاه گالاتاسرای با میلان بر سر جذب رافائل لیائو‌ با رقم ۴۵ میلیون یورو به توافق نهایی رسید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104755" target="_blank">📅 01:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/secgCudmMUS0sukP9g-1vynmSwj_mtro3tjR0doJm4GytR8z-BONccC1JtbjZ5uOHSGDmqw8w4hIhBE60kZZQr8ycaqbI2cQ9mqIIU5TLyI8Da6m9VKr797wfYCc73qh4ecLZrxmG1dJO-aE4lFcQZE8GDUuLJgy0U-ZAXeb_f1ZfCxoP2VyQX3sfP-iobC9tdZs4wjTyzaKrMMdPpa4Lbh--ZYD3vttzM6zcVkjMglK0ACgt07JAQb_jnvYx5aTdq6HlqoYM6lBCOUIDgY7_3SW1tKszTlgb-MuSLFbe-ETpXTe94HVW-e9tAV-XEcYCKQlVZ7G-3uJ9scvdRlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری
و
#رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104754" target="_blank">📅 01:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwZ5rpITWwZEfezLcpbu-NeFsHa8V-AjXax_dgBQcEkJ0ggvzNKrcdwvfWkcLTNxKkA2xI4lo-UOJtwpnWq67Z4sJxSMx9H6WqUcHywuw85Lnd82pWEPW582ArJ-4OZvdca9Wy-P0zHNIO9qckltIwTjvD2pNDTVPh2pFjqQQJHOlgG7kXqVF0oXlSvKT3HF9gg1mI-RWtHNSF3H8sfhGyJ5DBiVr-X2mEba3ZhQ0DaHD4GFybKN3yzGbEhn1-BQQWknDZoFAyULC5RtJZ4o2ylkZuX3jibUsmoV0sCWGTrZDroOAPnfnhfsi2LE1h1eVU-D18cU22dU-qv5Umovbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🇫🇷
فنرباغچه تو فرانسه تونست جلو لیون برنده بشه و مجوز حضور در UCL رو بگیره. حالا وضعیت دعواهای بعد بازی رو ببینید
😐
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104753" target="_blank">📅 00:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogi6h5pASooi8B_9QVNioQBMBde8YQCR7XWEXytktfZrDQplE3aRoJk3O088JyeWFnbQkh3OY67Nn-m1anTJCtuG38s44aZ4Od2Uwdkl7oxUXGFKSvk9CYNCJwa289eFQ55EiBpuPErfoJh538vW3KhsthAWtK5q7CHqBjfFEgBOLQHyQQUD1YGGHbWkObWWZj02Bob6OpGGJY4mT4h779miYJB3rNFvKXkMNP6ZznpbUnIjVoBUeT24FNAYpHsssSVn8wp0yWMQdg9F0ZLSUgpbOzvEOd5W1GwDX9I7dCIwaB4C1ujdoFYHWiqkqetcQHhSIbsGrXWFRGN-k16AJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج دور سوم قرعه‌کشی کارابائو کاپ (جام‌اتحادیه) انگلیس؛ تیم‌های سمت چپ میزبانن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104752" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74ce22999.mp4?token=lIvY7xGefs-mcUymnWmUIFzoFP0FBvmpCfrrFcZX8Pu4XFdjSbgBOAUcSv_DGurhKhx1KNngf1L9_lTg2deMEGQLd-Hyap7CARpCzs9X9n7MQisQw8D47hCmgoAL6ygENq3o0195I8XzFV9pH6ptjclXfXC2iICDxLpmeDav_4BAXCIWzTUA9me4IoAtQgt6qeQvMrhbzS-sH8POThOVdQbU_yWd_aC7pQf3IOBHeS9sQNVv_ZHIrmKdBdoVSiMmkvRcrY92lQccSjLpH9dDwf4ipPst7LfbcxaMcTraB8CM_SQqVq2meyUcsmg9BnLU3_u0cBLSmX4WPm4-bciKMym07oJfMqAL0ierRfOFfCvBv1zGKT5p2uXjoIFhVGPT2G0V-txWZNd9Dqu_vs10rwa9UpHGDoS8La28Ji9vFA5JwIhMsJgJKTnAoAGQGfM61WDgWoqjL-WrFOADKnAEq_9WWGB0L5ZL7e1X0GJDjHJUiTomfUl7KjsoKnszsY7_1uaoDz68b4KJZ-CneurbDkpB6UCcoz2w3WCdxuom067CeKOCvYd0H6G0w0KsxUGbpCILRobxa5BiAUsC9Zrg2gTf8bRYz5bPr3lHgK3taPT0UHwiwL2Qg_TNScxu6PWbut5GStVJNxaRATBRftNhY2oNeExuqg8itBKOhuDdJYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74ce22999.mp4?token=lIvY7xGefs-mcUymnWmUIFzoFP0FBvmpCfrrFcZX8Pu4XFdjSbgBOAUcSv_DGurhKhx1KNngf1L9_lTg2deMEGQLd-Hyap7CARpCzs9X9n7MQisQw8D47hCmgoAL6ygENq3o0195I8XzFV9pH6ptjclXfXC2iICDxLpmeDav_4BAXCIWzTUA9me4IoAtQgt6qeQvMrhbzS-sH8POThOVdQbU_yWd_aC7pQf3IOBHeS9sQNVv_ZHIrmKdBdoVSiMmkvRcrY92lQccSjLpH9dDwf4ipPst7LfbcxaMcTraB8CM_SQqVq2meyUcsmg9BnLU3_u0cBLSmX4WPm4-bciKMym07oJfMqAL0ierRfOFfCvBv1zGKT5p2uXjoIFhVGPT2G0V-txWZNd9Dqu_vs10rwa9UpHGDoS8La28Ji9vFA5JwIhMsJgJKTnAoAGQGfM61WDgWoqjL-WrFOADKnAEq_9WWGB0L5ZL7e1X0GJDjHJUiTomfUl7KjsoKnszsY7_1uaoDz68b4KJZ-CneurbDkpB6UCcoz2w3WCdxuom067CeKOCvYd0H6G0w0KsxUGbpCILRobxa5BiAUsC9Zrg2gTf8bRYz5bPr3lHgK3taPT0UHwiwL2Qg_TNScxu6PWbut5GStVJNxaRATBRftNhY2oNeExuqg8itBKOhuDdJYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🇫🇷
فنرباغچه تو فرانسه تونست جلو لیون برنده بشه و مجوز حضور در UCL رو بگیره. حالا وضعیت دعواهای بعد بازی رو ببینید
😐
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104751" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALRnSRGFG01uGJBzplchPn7aRqU5z6dKIx3gy7BytfYjXqhyitw4SabxvEOT-NMJR0qoutNMLKWvQI3v0m9JpBSLLb_t8_wIp9M7IKY7cywwyD4Mg0YHGpf_Yo9-4xb9sRDJODSZ9f7kADvSxusqiloO3-BrTHxtmooclWYKhoM3C5Ry9WtXx5DkNKgmA3MGnRv50Fz84w7fOLcBcJBZg1802Zk6F_3PmPbrTBy79VXeZhobpi-41Jp3qZ-1qYGAj_KZ3NGo7qXlTwXYJ1d-tvYShB1BcwvoQaTqoLU8twdwoVYmqNw-DzvO8LZdLaUM1e2g2UeCHxQXjmjxUTRQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
🇪🇸
اروپا خایه‌کن که صاحبش داره میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104750" target="_blank">📅 00:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2024k42XRgXUpqkxykb-vlxVuaZ4tQvxyQ-4_pxBitEUZjRthhpJjU-OOpL-8mSmRYIsPo2SdJ2bgJ0ILgpx4vRF0vPm9PQO-wOz4tNVuAl6uqT8lozEjMs36uuRwKR9BosffXHmk5LOg-DPWXT6Ka47JHkrILP7BBih9WWRJ23CPeOLyoYXS65KW8FdQndTVdT2n5g07sY621wrivjOgqoPGEkcuQqrWmjU-nUJSmDjDDc96N6cTXLlW9CSw9GFLHESR3MkfeJdoR8UuxX3Y_eW0AbLfI0CcCP38F2QilAMaKFuogty1h4p-5FGcp7xk9UyYdXjxTftGneyyp6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🐐
📊
🇪🇸
عملکرد امباپه در رئال‌مادرید:
🏟️
[105] بازی.
⚽️
[89] گل
🔴
[12] پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104749" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD4ce4JGLN8ESTicv48HufKVNG6siGmFDWfhuD-qDIbm7hlNckCfSW0FSwHPpwyGIJ7BTXJXlqTlM4KNa4tsGeaRP4L4rFlYHczHiLPaTe_UnIRQy8R4uZCGut5pBmxjbYyEQJf_n5B7oQPm-AlFlTZHPhzAKbu5HMcC_JrxOglC4iUr_782JapiCLMD2G8CmdNSEBXj08Og6HBCpSRnMBoQKT-Plc9s5Tay-jBdr7PLbxEWmYVvEtGA_g5BVF7Lx7VoH3AfVD0wTU15_E4-r3bgybATtRPXdmi8cdSTeq-8oUkHUqrkXvtTcvXrcQ-xg15Xsvc_qjH0bgHWPDjlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌اول لالیگا؛ اولین ضربه قاطع در برنابئو؛ ژوزه با امباپه به آسمان پرواز کرد
🇪🇸
رئال‌مادرید
😀
-
😃
رئال‌سوسیه‌داد
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104748" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7653010aad.mp4?token=Y2P53MNA4vcxlXjvbKyL6e2Dai2lls9ShqiPZbG_ibCHgBjhnpFRQ5h5VQ5pz7XBB6ntVoeeGeUQWBmqJ3VlBzFmPRCMOdtR10I60bRh8WHB-RnCnOzu9rRfzbNLWZxASn4LvZj2eUR_cb4pM4x6qTLU1jBeCBP3IyLC1GEcC8VXjhzqyv_sJbA5PYIwZfR-DjjPxjiqMl2VU_BEmGephl-PcEXxjVR8bZogvPbIFZjankd0CDXMfrNq1CWJyp2Tv71yhhkOUdR-RwhJ7dmc2v5XmtG5C9AtrbsB_mliustXDdl1R4aUwj_wdClV3OQK0HkF5ki-CrNC06_rDi2BunjfRw4e8aqBHHJuYZjXPlAbHW_pPlWKAvSKm4qu45r4Vc1kHmndfSkrZaru0ntQMJHSGCFqNRkLxxP1aOKCQTc5TUp5XOQIOjYvRmeO5-1ZBud7qsYpk4G9QTVmmBcMjd6a3n7GVI0u00anrkejqVZcfi1ULFPXSDOhRwJFkGht1rjS_NIk6ESzM-kUKMvHpHlcnx7ZKBh1qOzOxW4E3-CnmMEGtzgOcyfUiU1SzonhZUDAALnrWnTyHnVfVYjhpqrHr0hNtpqafmoC9g4umNzKbKSnsCUjfAgFt5edJtdvGVCQsl1TC_ANqAgngoMpn2ieoYjiOR5uMq5jpl1U-Js" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7653010aad.mp4?token=Y2P53MNA4vcxlXjvbKyL6e2Dai2lls9ShqiPZbG_ibCHgBjhnpFRQ5h5VQ5pz7XBB6ntVoeeGeUQWBmqJ3VlBzFmPRCMOdtR10I60bRh8WHB-RnCnOzu9rRfzbNLWZxASn4LvZj2eUR_cb4pM4x6qTLU1jBeCBP3IyLC1GEcC8VXjhzqyv_sJbA5PYIwZfR-DjjPxjiqMl2VU_BEmGephl-PcEXxjVR8bZogvPbIFZjankd0CDXMfrNq1CWJyp2Tv71yhhkOUdR-RwhJ7dmc2v5XmtG5C9AtrbsB_mliustXDdl1R4aUwj_wdClV3OQK0HkF5ki-CrNC06_rDi2BunjfRw4e8aqBHHJuYZjXPlAbHW_pPlWKAvSKm4qu45r4Vc1kHmndfSkrZaru0ntQMJHSGCFqNRkLxxP1aOKCQTc5TUp5XOQIOjYvRmeO5-1ZBud7qsYpk4G9QTVmmBcMjd6a3n7GVI0u00anrkejqVZcfi1ULFPXSDOhRwJFkGht1rjS_NIk6ESzM-kUKMvHpHlcnx7ZKBh1qOzOxW4E3-CnmMEGtzgOcyfUiU1SzonhZUDAALnrWnTyHnVfVYjhpqrHr0hNtpqafmoC9g4umNzKbKSnsCUjfAgFt5edJtdvGVCQsl1TC_ANqAgngoMpn2ieoYjiOR5uMq5jpl1U-Js" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104745" target="_blank">📅 00:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c75ce2b54d.mp4?token=gHfEGLNqqaU-3uJrQ76HecJAUNS2JafBZFZ6b8sTsCXhNPkSzFGmfWui8LZgrcn4KlW4mJq_FZ7a5sgkHuGo17Zw9oyQv9ZOqx0oL1cDt4gcJd-8ylhyD15bs_GsN2PGT2J1uQsYfTjqzalTeyZyAo9uyVhRGj_4E7cNn-XsyNceMwZmAMG-PPn-rccrg7cBc5z3FYXkae9God0i9I7CpSV4buNI3LdCvO2Fi5VQwuVM-cfc5R_AQEWPMQKm2VtkmBTgxep-m_U5HhLXPLIxYV7tnWWBqXXVVfLLdU83O2_LGqKhH3K79Uckl68ZiEmVbQ2RTghII4ZTy85qDy90jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c75ce2b54d.mp4?token=gHfEGLNqqaU-3uJrQ76HecJAUNS2JafBZFZ6b8sTsCXhNPkSzFGmfWui8LZgrcn4KlW4mJq_FZ7a5sgkHuGo17Zw9oyQv9ZOqx0oL1cDt4gcJd-8ylhyD15bs_GsN2PGT2J1uQsYfTjqzalTeyZyAo9uyVhRGj_4E7cNn-XsyNceMwZmAMG-PPn-rccrg7cBc5z3FYXkae9God0i9I7CpSV4buNI3LdCvO2Fi5VQwuVM-cfc5R_AQEWPMQKm2VtkmBTgxep-m_U5HhLXPLIxYV7tnWWBqXXVVfLLdU83O2_LGqKhH3K79Uckl68ZiEmVbQ2RTghII4ZTy85qDy90jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104744" target="_blank">📅 00:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1714a1550.mp4?token=WmIK2ZiLQ64j5HqSk6PajMpHxi5rHs4Q3OLOLH0aNSQA7ccJDeoXfp9hI_A4ZNer1qXlxASQQt77xwds7Qi6XnFyiGLkSsHLQWv_R1wghjJZ3NCKeF0Mr14fxoonCddeynG5kzeNC0bkOIavJSNSkeJ_aMYXcdWt2cYZ4t8bLL3KVJWHAQMenkimT1krAJs7BXB3JX2wICmenNdbL1jWvoxcwlaOF9OppW14zqvX9nYb-RwUP1jKpt27oTNSPCdZeRoe9xzcv7HTG1fOhqKiBSWl8ZWwaVZ_vy-SCvt5h7CkaODbIvqJ37BUr2hTqakE81xtpq96HWp8qHg52i1uOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1714a1550.mp4?token=WmIK2ZiLQ64j5HqSk6PajMpHxi5rHs4Q3OLOLH0aNSQA7ccJDeoXfp9hI_A4ZNer1qXlxASQQt77xwds7Qi6XnFyiGLkSsHLQWv_R1wghjJZ3NCKeF0Mr14fxoonCddeynG5kzeNC0bkOIavJSNSkeJ_aMYXcdWt2cYZ4t8bLL3KVJWHAQMenkimT1krAJs7BXB3JX2wICmenNdbL1jWvoxcwlaOF9OppW14zqvX9nYb-RwUP1jKpt27oTNSPCdZeRoe9xzcv7HTG1fOhqKiBSWl8ZWwaVZ_vy-SCvt5h7CkaODbIvqJ37BUr2hTqakE81xtpq96HWp8qHg52i1uOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104743" target="_blank">📅 23:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/592c7db362.mp4?token=pFb9gckdHJiU1W5lyvIMGho1W-NvlXOhmgs2zJvUbBUb_KYyJoU28XNd3AEIzZKrKjfOeeXm5MmVFmnce2EyvkiJFdfNMpy1YFeaoHPAdtegB-2MpuhuLkmDfvqPGrDy1FSiTrxRydxssuH0Qd0rVBW_Bk8G4EK0DRG607pDDJIGNjFBQ7vEhqWTwjl6q1AW6JlolvaICdqLBL6NZv3eenCFh530wU6CGJOP3QwjQ4aEmMCHZcsNQ08KNhQRbbebjOWODtBFmo0ZPTtDWVElZhc4yVAG5jX41GQHcw9z2Px7KydKGlNjCLGts3aZDMjgknJb-_HguTiF175l64BnxQpAngQfmloFRl9qey0MIdBS3d_mp84dPOEEIS9J-0L6yz7eQH-5jV3p5FNYNpArF0K9kJ0z3eSL1Qwpx8O2H676X_3SGQH4lAHmkI-8-IC5NzGYe9uOy8K1I4MTQ-IHhTXN9L53-z7cFhB7qinORzzcjXIzfwqElYQhEsGDIfU2zOK1dXw2xBQZ6D_RimKgl-fpfY_A_GrFCIiTTVNpN0dPgeai-WZAQ5uZjh5Z3wgfB8tGsTLAc_3pABUBbIi8n01alWnWcAbpbupBdqw6Lh3X5oEf1YaUGPRv_om8Z3TTZpO4hGFmEjTqbrGpGjI7D59p01AmHb1E6nH6ymDSXH0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/592c7db362.mp4?token=pFb9gckdHJiU1W5lyvIMGho1W-NvlXOhmgs2zJvUbBUb_KYyJoU28XNd3AEIzZKrKjfOeeXm5MmVFmnce2EyvkiJFdfNMpy1YFeaoHPAdtegB-2MpuhuLkmDfvqPGrDy1FSiTrxRydxssuH0Qd0rVBW_Bk8G4EK0DRG607pDDJIGNjFBQ7vEhqWTwjl6q1AW6JlolvaICdqLBL6NZv3eenCFh530wU6CGJOP3QwjQ4aEmMCHZcsNQ08KNhQRbbebjOWODtBFmo0ZPTtDWVElZhc4yVAG5jX41GQHcw9z2Px7KydKGlNjCLGts3aZDMjgknJb-_HguTiF175l64BnxQpAngQfmloFRl9qey0MIdBS3d_mp84dPOEEIS9J-0L6yz7eQH-5jV3p5FNYNpArF0K9kJ0z3eSL1Qwpx8O2H676X_3SGQH4lAHmkI-8-IC5NzGYe9uOy8K1I4MTQ-IHhTXN9L53-z7cFhB7qinORzzcjXIzfwqElYQhEsGDIfU2zOK1dXw2xBQZ6D_RimKgl-fpfY_A_GrFCIiTTVNpN0dPgeai-WZAQ5uZjh5Z3wgfB8tGsTLAc_3pABUBbIi8n01alWnWcAbpbupBdqw6Lh3X5oEf1YaUGPRv_om8Z3TTZpO4hGFmEjTqbrGpGjI7D59p01AmHb1E6nH6ymDSXH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌تساوی سوسیه‌داد به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104742" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگل تساوی سوسیه‌داد!!!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104741" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=gsKMOPkf69-7X5vE2Nwgz_aHhRW74ga5BpED7H_NXP_HaNXSUYX6zV4Vv6355EjjOHwPow2r_7JdyRfwnEYayzWNDqdeviHfARQ5uyH4qUfHjOkY2UA-_FcF4s5wwWtVOgCqxuRYB6h_i4x8UvhNDzpqf6AZMBUI5iBa8NBadCxGifbDCwvpOPDcra-haUnmnQ_n-PkKX5lMZ0yKVhljq712FzHEQ_ISJIUABaEW3dULS2bcBLsOJIW3wP0Q00Po___X55-lNoq-cf9y6rcSkcrlIZecwsaIsMztiYSCeRi4RTBFXlrblNrX4HW4FFbQu72bHlvao0r-TsbTtZaCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=gsKMOPkf69-7X5vE2Nwgz_aHhRW74ga5BpED7H_NXP_HaNXSUYX6zV4Vv6355EjjOHwPow2r_7JdyRfwnEYayzWNDqdeviHfARQ5uyH4qUfHjOkY2UA-_FcF4s5wwWtVOgCqxuRYB6h_i4x8UvhNDzpqf6AZMBUI5iBa8NBadCxGifbDCwvpOPDcra-haUnmnQ_n-PkKX5lMZ0yKVhljq712FzHEQ_ISJIUABaEW3dULS2bcBLsOJIW3wP0Q00Po___X55-lNoq-cf9y6rcSkcrlIZecwsaIsMztiYSCeRi4RTBFXlrblNrX4HW4FFbQu72bHlvao0r-TsbTtZaCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104740" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104739">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امباپه یکی برای رئال زد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104739" target="_blank">📅 23:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAFSa9m1kvxUsld58_hE70rgT6sXAhrQAB7zX09vQw6GFSte2tDbeIw-sfGACD1uoDhW-mf-cFrfX5F8JP-DVa2Oj_uOoSua7BKZ8sHVwbHqFDBCD8tqEIFW5YVKTCkJHUXfB10F1MRnQwUJ-20OzS6a0IRIsOIRXwCk3LgQVWCTATeU3WY7zBdHSKepbU2BLHysaBRMfdkK0l_ckQjJ3kb8lhentsn7aDu6REUVcCxUwPvhR5dzRGHOlmCxA_JKy3JqCR8caLge5gjQU1XzlarHpYD6qNUPZ1H8JA1bdSWoCfil1qZw5fHreXFsBoA4UAl2mjOP-u0IaYs9Ks8sZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو: هیچ توافقی میان آرسنال و اتلتیکومادرید بر سر خولیان آلوارز وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104738" target="_blank">📅 22:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvOW_VHRQ7vlM8xCUsQBh87APjWq0nM_lDjMGBdMsHZWA-659A-d0bBSG5BTS2b8Az_LBxCIia8ij24bBv6VtDeg_IjCaO1T0gIJiWG9GUKtOFzeimXPLbCPgsf0OfosK8uu5vfFv9WXyluhTjX1J-AwzeBYBtzIxQzxkEAE0e3MSuxy3MM-U1wF0TxSnsyhx5o9N9hk-ParGdzM6IMxOa5-dVsoOKLvjDIXnjKEaF0CuZ0veb8EdE-jjY3IhhPVatfpKZIWZdo1EM_Fci4tol2WZaIC9AnkSN1Wnng6IZUvncSdRb6zkym1Nyv6PLc-aMEkJDa_gaBxffHrfG4PiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔵
🗞
#فوووووری
از رومانو؛ اولی واتکینز از استون‌ویلا به الهلال عربستان
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104737" target="_blank">📅 22:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی نیوکاسل از نیکو گونزالس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104736" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo_BMy8ewSgiwtuh04hRoz917DKNRxTwCaETb_p87epGTGhRFRW7glzlrx2n_C31v6XXFYQ4Vg_4GL8YHAYLdes7xMDvLp6KRSp0gUmUleFSKyIPnrt8aBoAbQhrruRY_8mk1uoE5Lcrcq5wRIjKXUPOCc6HrAcE1F2TvEM2q860WomZOTzBKL5N0Tv0bVg8kV9-E8PEoqqsXOPRjnhj_OCGeNmOML11dKZ56gooaj_OrZ-Fg8fvDMnMwCTqK25NRj-ZF0fFeDNngGFFg3FpcrTwBbwoXjLJ_zPitXd9QYvT0-3fSmuNd3ODVECFAtqOFfm2LX-CDZYojBhSdh33EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104735" target="_blank">📅 21:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c61000564.mp4?token=hq8y0UW2CXRT3YXhqTtvDiIdgkA954QQJAiJY-bY68cDDNHWXhLib2khm2rCdaXPZlp592mpohrwvcUbM23n9RW4b-neyfGqle-VNW73yWcQq7uVXp0NKokV5STFZNxlAx3Im7bgVRqsXSpke4HzOxjzx7_uc5NDoS-Bn9KtnKE3HhM5WXFR7rhIBbTpYXmYgi2K3tWCO4Te-IETjnhTffX2Z6uBhz3UYpKepr33I43clUbwi0iLeSLOYnyuU0V7IT0DcmVB9nJeLmGv44eZPv8qHnNeXbJdQhbDKL1NbTWEkyEbnaTUrN1L_qLgXE114PoDA6yXRJOxhf4DROKslw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c61000564.mp4?token=hq8y0UW2CXRT3YXhqTtvDiIdgkA954QQJAiJY-bY68cDDNHWXhLib2khm2rCdaXPZlp592mpohrwvcUbM23n9RW4b-neyfGqle-VNW73yWcQq7uVXp0NKokV5STFZNxlAx3Im7bgVRqsXSpke4HzOxjzx7_uc5NDoS-Bn9KtnKE3HhM5WXFR7rhIBbTpYXmYgi2K3tWCO4Te-IETjnhTffX2Z6uBhz3UYpKepr33I43clUbwi0iLeSLOYnyuU0V7IT0DcmVB9nJeLmGv44eZPv8qHnNeXbJdQhbDKL1NbTWEkyEbnaTUrN1L_qLgXE114PoDA6yXRJOxhf4DROKslw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جوری که رونالدو به گلر کسخل النصر دیشب داشت گلری کردن رو یاد میداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104734" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104733">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqcD3yqkmzy2BP1H7vGowdbiiURTRAmt5JOW1Sjxa-OpkwSdVtN6etTe_ZNfdwee9ZupsUpjSiCMfhC85gH5-KVzPi8dfB_4C8P6uoM1veW00xAM0kHKaJ8VYtx8-PavSmaKwEl6TUIQDCO_QwEtXu7YMKUnB4-OVdtvaYI1CuK2WLbC97JIaicuN0IeoYtano0MyQFDcwIgUyOL41cxvEP-qkJthE1FYsF1Y8HZq1OAqi2sdrUNGgHekg8g9h3ykKUQrKA-VXAhNGOZHswJ35ILLOErzrbZmZXkNOcV46OfKJ6Fptto6_GOcHp6acWGgm9YcuZOwTPq4KlkQK1g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل رئال سوسیه‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104733" target="_blank">📅 21:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و ژابی آلونسو که دوباره خوشحاله ...
🥲
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104732" target="_blank">📅 20:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
🇮🇷
عصبانیت و فریادهای محمد نوری سرمربی صنعت‌ نفت بعد شکست عجیب جلو فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104730" target="_blank">📅 20:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlrW4GuCEfaycnGsaHhNx461MkmCerSCI14dzk1zyzKVcqXgx6zCFh72r_LfkUqonZToQq-rk0Qrf9kK1AkNYGtrXUlmFK6CtEwXQ9LNd7jKPB8MEQEK7-3CGJIt-A0yNKQxlgHffFtoyPPFSk1nPjUXi8_2VKVa0z_zYe2s_0_gKMK4slDjX-j8NH_KEI8PKWsk89OS5AwFcAXIhcR6aWfIeE3PMOq23lDeldkC-pD_gCe_zL57b5kqdJH9Ca-qnET6PYhzqOzq6STPoG4aRPWSEYYrJv_iMEX1QJUSyIECSPjq_5nOrOt8qzzXbSCmPo72Nw1w8KDXruZIC3i0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک حساب کاربری که فقط اخبار مربوط به باشگاه اتلتیکو مادرید را منتشر می‌کند، گاهی اوقات منابع آن قابل اعتماد هستند:  جولیان به احتمال زیاد به آرسنال خواهد پیوست و به پیشنهاد این تیم موافقت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104729" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRSUwRUqVuf9sec-q7224pGi5ifTo54qg8uGvv7Eq6v_0_ClQjqUMXTf5vBr1XrRC2zcPJojtVwCRch0Op5buoMLdKCDMSPASs0iTsW8F_kqCLS2T1bm_GPAET-lUJthW_-mzErJFkAvk1qvFyQCgrpOS8syDXNGT1Zv5GIqndAXOheKARiTjFxyumVcX6WHscnDbGzgbY44dTFn53uCoDWPfV2pgFe7GL1HMCiATGlcT7Lz2AMMfppd0SQAialAB1zGvPkmtSrhhDRIVipMQPvrwEM1JQ4A_CXsJd8fqeNiDHu3jSu3S2ntPIIlHCqyWNV1yRPvaBpfXSkYko9JYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104728" target="_blank">📅 20:02 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
