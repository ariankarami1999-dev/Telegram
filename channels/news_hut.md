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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 12:13:28</div>
<hr>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BVlUA8Eam1yHTSz_ICmqDPmEgeNDAuVTbcqU3xLvmMo-rAMwg15KwNGxj0j9zVAkn-D6vh5NRH0Lu84vf7pDNsQwiwcY52lTuihzV5rOfM9Izol8L1rGOSsbmQqtpuH-q9X5eo2Kim62cwNFW08Yf1-tFKSPTKEtwdCvrLB1-CoQXvx4ZEVuSZUDql7WdXiNoHTfoZLxBAXXpuNdYQPHV2ASdP7eBuRsvJLLEAzdlIZILw6BKsq-UalyEoqXd52jTFCcQHrN8QoOsaKvgNhoOgb5FuMTjHrjBZXaOcRttLUy4eAKvcbuu7RCbeW8g8CFHp2xjMm4sfpCx7tl4gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMeNRZMKmdsZb_ExCKl6Z2pgucjKdIrzC23aVd7Lg16ipJiIaZaxsHWfJpHoMiI5r1HTj71c4fddEKV46XKX4_5G8TGRHw0MKS1rbp-B9SmSyk2kvcilc8pZLJMAILJNFmfLC7Dg-p02ZWev8YZtvghFI9YTE2KE0o23DxQ-CiclCaHWpYuGyUvi3ZTMQYtMPM3lSBBkTPTGZgKm2olFKYxy22ZDjVbw0FxDkG8kZu0CNvZBPUQnQXZYVhPp-cEMsrwaDKm4qdl5PWpNX5_nViHd9PO2wDcOFEXH9cPqwNaPNiNnX-W7xEPJIpPcVRBSgsLXQD6Xb5jraEcBDr0mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXlHzIOtycVEuzMaSyfjhTQ_k0vkOM397zePhw6u_lbEw6m_jlTRAiLMkW-D9VTW5GEG1xUnCnowrGUGD2tMzz9STfNzbX42lNPsmMi68hMJKTVIbk6NhNETndSaLzKQXjhbjf6z7ifIIoK__uSrTELnJWfK0ljB9qoIOLGfgDxIWKJcym1Zk8nSpEFTlR43HVfa2EIfmt9zYbo45PCVlqMoTit3RcaJvsG0fLU4e90Sb_vs_005FEDk9SHz9fEh6cYO-LowPT6dJQmSH3nWVmlF8bxRjbJAldcRtheadU8V56BLy0L7tKgOpSO5C5l-f0hGK_0DCIVQTGi--i5SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAHwWZcGQk9bTEPIAfKPO3pOndfQQwHEouwbOs6WPYwahNTkINmELN1cbqQaE7BT8UbCMaAS3wMzWBhNo8rZQjVR3BVuzRNCPNKEuRb7hB0OHc4-lI5_g3NSpLcHRjQqhXnjIuyQpRGwzpQK4z7RTeoOYr0hM91kIHzhLrVH6ugo05QGxZ2mjgDH5Ahw4D1NAPiJS_mOnvHIiNFoliLQmPRBCdX5NIYG50M7LHzlFRGJSdrbV23MK27soloafsPzsgtaPQcL9NMl3nSMC7Gs6lwAova0R-1gvYuxAqyiz0Axqj2GQyWgkp8KTZgxTzO_NaiHZ2ALJCDIRZMp38aBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el8YWblstOLTJChyvfOcg93SjeaCVsL_hZRF93qlInHSjDF0fptgLupC8aPPGy--pvq4yMMNt3TVLZajI_6yt_-wk-NSATPV6TWcYhXswi46Nme-BZADsVxVaJ5XdJmABjXGfI50wRV9gKeYt7j-u2Jb_4utMKk83udfpY1dQdtGJtlvwHNqnPSA2gWHSnWKtjErk3QV5W8ZMiINvrZOj5rv_6AUE6t-7frPqi4hNne08EXa3qIqSu9klgShUCuTGPWNpvurBVXik2LBuRJ3xzUXjbGOOyEmGh2LFyOeILZNsUw640yF2G5gX2vyEz5cXqKxTru8ZTpFDCLKl6zcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4uTcxfBc32O5E4ovfMEV48s-U0QFHiUX6aMXqb2qzTZa_mEeOhYCz_5_XIybc8hwMwHTjH2-1H0ajk6tOXt3Tec2iNxxKxpehJy5L_CZWRNNSHohzfLp8UEVFk3CdZZOOiQ9gOCfoNtRvwbuMant9GigFICOf31d73Y0dAM2yNv6-Ws2VGa5lZGhaCzNXFxXapAAHoAPuc9fQyMi6xZYGEL3IITyyZONuxrV793sFNzD0i9VKDHU8skrau22kuYM8QGFcwiMsyKauyEtiaL1Rk5fd86mekrjAu5TVQH4U_CZYUgCQIiyyTM5D4TCut0Jm-yHgGMZNEPgvUdMUEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HknV2wLCJujUnJVmpYoZ0Cdk2P2e6ApZeryo-x0Wig7eu1a_8DzdIvNuZiq8n5DCPujmVn01O1X5Q8SVn1qzgxKkHfHp13eN2Ft0OntLkunNGHeuSk32EaTGB8VgonZJBELeKNnfLzogCfGqYA0d38skzHzMDfp-zLxwzIaydse9YmHnIRzNqfBBxNoqAcozvxw40z7eBPH4LjBlp-guxd5a-QhkLAmi1YSHnjTwMeiyt9znTYnq52aC27OIh-ZOm0u73a5zSNBow4h85VWWCuD-mocDW2Ad_0_Ut0WxqnNhwQGZZhJEwvxZ9ajXiHj3s6z6TtyvL1rOYr_4EpjSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfd_Q6YNJP1grjpJv5GKYLKv2JcpWdEfV1g-3V7WNoatHRXzM8PF6IsVM3OYuTbgzNHVbD-eKE3FcTDZCAN-DLM1_bN0g7HCeLPraSarEtyRdiVLlCVptpqAtzV4dBamRp9T4LG2XmS7bJN6erHaxbWt2EeoZcczktfqUrqibUGoJysfYqS6tB299qXg8UpcOL53MOf71XeH_E1Qy1IZNZOrSlnJN_CW65AMCqxvq2MeBeKpWPm46CuBzSdj-uXYOCVbjs9z997NmcmPoCD1KUDhw-7rEAoiPU1ky35lCxnN_24AMn6nHj8SySwgnHeDQ8DZEkKPKgn48-dUPWewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld_XHD-1Tx6e-hHC2j1Wn4orUZ2s2nX3uzqOkzLTu7gac-AZC1wbuhCbpMiNYgeWG2f_gKP5v9bqsx_iHg9Vb6i16L9iNEjQnr68-lAB6IlxbaNekjNdD7Zwe_kchic7zdUqKHf5k-p-JS5EBI0O25MVD9jTQneQQcEz31gZ2i8Rtm9DvKeaJsJaMe5iwWzF0_xaoN-wAD-lCMmlQ0_7O0cQ6LiTf8kUcjCsV86qZodepeXLLHy6HMJV_JPmxQ1qEmTpdWpLNBXstkto7Puyo9GbwlQsPHsLKfkF44e6vhgqugjyTdyNZaDsbsOKhqhXCeHAHr4slDXtH2YJhXeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM-LWNTjnmcyuKiYgL5dsoS4G-ezxUb2ZLdLJk-UR5GEP2PWjbVRMnEKk5zuvCfulzlh-3xWBhi6eRS495rLoJEUUQb8kHDOEG9fXF4l59RkpNvvI8q95Ya-tmpo8ZU2wR8RvAztmFYmglnTDZpgrpg4uy0wRI4eDSsPL1rx6w5Lw3s6wFidrT5I3iUOM0Hjmaf3X3iqI9A-tXbegRRpF5KCoASuwgZqOr4BldazmQaLDSQDPP8AU-O4pWClKgTIkjMxU_Pkg2PJlPNeRw7TLerShNKE5ziFP99Nv2IyKZjrpl_OBQYp-re-eQ1HuNZoS9gOs699yISU9uC7EWXxsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=U678mtnjpYhnDxITe_nlWXbxOpzsBA2MfWjzwuqUZsoEpbxbZ4s4cr5mymMZ3OxeTMCiQMYHC3Qa5ykrzI5kxgWdKfe10-nHAbDqlL5SYIPAkux87QuRM_bzkorGEUIm2kIwjrySaw1ogmptoewXLW2oifP9HLYWTRSVn6UQmL40zk6WSCM2uj8XROnt5XfWEb_kefglsTyHqYHkhxv_cQ8DLMkWX2cFvITonm4dFf-BM__vdekZ-54ax6kNrCd_Y6HLOQEjsMcSPZFcI568P4fpW91sTDDPpKj3Nx9_ufrXwG1xFOq_S-ivEdhCLEsjuZGPlnZTvZFCeNRR1Tuu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=U678mtnjpYhnDxITe_nlWXbxOpzsBA2MfWjzwuqUZsoEpbxbZ4s4cr5mymMZ3OxeTMCiQMYHC3Qa5ykrzI5kxgWdKfe10-nHAbDqlL5SYIPAkux87QuRM_bzkorGEUIm2kIwjrySaw1ogmptoewXLW2oifP9HLYWTRSVn6UQmL40zk6WSCM2uj8XROnt5XfWEb_kefglsTyHqYHkhxv_cQ8DLMkWX2cFvITonm4dFf-BM__vdekZ-54ax6kNrCd_Y6HLOQEjsMcSPZFcI568P4fpW91sTDDPpKj3Nx9_ufrXwG1xFOq_S-ivEdhCLEsjuZGPlnZTvZFCeNRR1Tuu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل شهید میرزایی که متصل کننده بندرعباس به شهر حاجی‌آباد بود، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_96pDYZGhZR0ITprECR3ImzDL78_ua437n8LpgrZTMdTmQm0kJXWDej3KN1q2Gm7zWgkAeu0vAqKAH0lpRdAVQNAi_CCWHoZ367EZ2qPuitPg5dM13FU0ICzgTKZgi8qwcQpxPEgEony4KoKgaXK2TShe4cyMU-yo3rNNM9vedYJcV_BMXgnJBlRZkRywfrO4zN1VUCOsGdC3ZqYyfWBECdyHvUslpPtojMNHelIG7v8xBCxZVnpDYXCDKYEpDDtmLrgeBxIMTctQEFW7TMSFbwTbX-G435LTLfZKh1KXTJ2EzIiP8NMSY7m28-vkgTAGCMRc8Zxh1nmbA2yW9Urw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvkmt0_TMWg8rsDElOiwNohIXRSROaSvufFjHaiHfn7DIpLMndd9LKrCNPUJNxUyKvQIHWcrQ_XKgipXogJ8g2eXHj101_j62lx3Nj-lIk44gSdihueI_v5Ka8vsB5jHgkaC4v1FqmaLEy49bcFjrnIBaIN1HTH4SwRp7DipNbT9usbtSCnu0pl6g_CcBajJ2OPFAYxEVqYs1QF7HYMgIS1rZ3Q-JlVKTVorHOdSBYfhlo7-oAz-i_5MBLHUktMu2RvS0ADXTBx9swtF--_UEEJRBUnbFgZkxjPFIt6scW5Wfur3VaylYUPGjSQRPm8vu40MV8Xt40Uug_7TFgYvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdujzBKrPQ-ebTwAzXCI55txLFvdyQtktHJcXwTIV_YwLYgVk9070Y2MOo6duk4aC5RYRIy4DSf2JKsdRAfhgZHhWje7tGkfGlo-rK2-X6mCteJZA1CcbDPRcnNh0rL1QhiTBL4TuwokaVzyNmrgDl5Dqdnxvy-7CvHZgxVMciJp5G9MdXt-K2Ice7K3HE6TS7Dwenku-fm68of_EwCzdcxVS2GYRkHgv0QpriIKpCq0d2F8IGZx9Ta0qLChvS20YzWHBTueuNjpFIR5_CktCL_ZeQsTkO2XbvnVP5UPAAP8R1BWpvAeC9-WfOh2EbuHZ4JTp3NTvSlXkkIs8MRHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKBbY5FZTcTIu2NAf1k6IfOSagNZrk_ZmJZ51LIMN-sU2xg2RR2sAanDMPWoAHJj3oovHqlvS1S-EzE-bU1AiRepAvsK3oprN9B3AJkeuYK9_TQ3p87gNatZOl4AuxaZYJx6JqhIoKIENGOvgCMx3RFE1qI_Dju0-LHUvRhFr4QsABn6r0GeaeExxYab18vPRUPXyALdzI04GQUyOmtfhyRa2S-pqIBgfV6IKAvH6rVdm-OFbaxDh-vMy5105CGT7VGsArM1FzPRQ-1TFZur4TDKC50RkjdLbAJvnfGjs8J--gUcJMxX_h3A06b4_WJTIvgvmBC-cL2Z1ClnV_KK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTi1Un8zG7pcYrgVVfVy0HWHvAfdN0ZQt0YODXDh3c4GikPRQZ3QgD7u9ZVCgXi5MXPxFMlQfj28VpEC8_cVhcZCePotzq4TJGQw_uHO-4w1C3FbRFYHjjfCt6tTk5YmU5kHdX_ryQW4CD6mtlFq379ZJtun4DyY9hangYfW1BcUGohCcf3vDLuWXDypvWlgnB6KOJb-boHAvCGSYVxK_48TtEBCbBo5PNDzQWUnSx-7ISnZHuM9toUkj6nRCBeLIUIW59Zn52feUgeqBNho-Gwesp2yQnGDuZBo731ZGgGidcelEsPRa4_Ip163vB9R1p_wwdIaCbJrFZlOOy4EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJajQlr3Sk9vaQeP3K7Tak0AZWIMk8N2Tthjm67wHOgBkvVtc-HR_3PCvrzDSniVDG5WT5niektMuxvZXw_Twxl8a1VxcTTKyk4aJJX6ClCHFcixlaFqfnzStr_L87Wp_vccEWGj97gIhJQCE7zY0ApctX3bfOcpcxDoIQf9qM7ZERnvl3kqaqMGxzkLWzLF9saIdc0Fm4UBIwhV8p8_4eLTi0y4SxV_DtA1QkobguNsWRuG398GQPQC4V0A0wQrP9nx7TCaJb1gs2mPfy-pkvogzIaM6licTJ_aYJG377P_WNBgOou668rbQicYqxoH2G1nOSqXSInEckJVXe4U6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XctzEDdrJg468ZfVp0qpA5_RHVvGR1xwf0NoCxtXxIoBomdmtmJQOWTeujULquoRTBxTP-3CYxZChHoNHPFfnpsl80cm24BjBckL8gFbGQi1pQBR0-CJe8zy5TVKzA996qmIk6POmdx88E_T-fwOtFt90GItiJNDEJagNM-LnuXiZXOn8sRPJGAX_NQcWTqyzsI106UNBUQG2SBEegTQS0lENBUUPIoy9vpOAUSsxgXiX96iSUdljCaGYE5Lw8Vys3YGAuXJD8YrwSWdnmrCHkNSQaYS94_I0tAERTnWwEDdeKWFEknQqFDyg6INi4Kx3zNiyUs0r7ShVdc8rMJDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3W7DmsGszEBUF5UKh5lY2YU4dmtU0YyZHPu9TVs7MLq2c_Npa44oCZEJlS-RYruPiZIsw3tdhfTjajmTKDAyT3JVtDqyCUNjLDjUtQlH83fMaOR5u4QIl6mFzsMsVVnDg1zksCTYKyoLDMmgduFaCamIykRhm9vB2FRk--mFeMcZP57sqCHtgR5wX7sljMk9Ll32Ze8gxn8vA1yTFKlfksb3zA6NrXGjDNNDSzbY6JOZ2UYlhSf3pJuos06wTlDx-NoORP2HPyS7vOE_KS46TrwWDit589I9gcYlqStSk6TcOV8imcqBVPUpKs3epFIk8cXjlWVPkxw-4G8aBzieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VphKW7QLjPAk0ooEMwgmunBLsdJHNidxoCWhBpLSW89FmwdfV27uSH3EhGOZsHlsNzUr2aWahC2_kZMrlZUMhu3PGrYyXip8-lAaNNWuOsink_fNMBxzbYdxi7ZorW2sqg9FxZsjFHRw0WQtLzZk2jpcXDHdMZrpqeR6BgmRaznkgVNkbD7Gt8hEfV5HDLxBReefKtKthMLfov7AaixB8gwl-LgM44ayarm8H2JAfvEtGF9WeSLMtsj3dagxdyZGi4fm6M0rnIe27ZVU_tVkrY0RI8fyl0m5lqz2wyCtJuUEU-Jxx7b9xGGINb4RA75IW0B89zmqcgQ8sTFdIn6_Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4t4x9zkxi_uwEUcFdeK-xe9r6a9KhTbvgnLSjNxOzIaGYHTZ4sslYYW56AfDKdjpUqNWwuJkVEcjKqHF3TgZl7rAzLj-EK6f1atZ5q3uD2ewuTrEsbmbg9qRSWEuIafFcfy3qnHOn-B_8H78fab-RaXuxOBUOGq-zzs2G-4F-40rFu0POJICAwPhH6i2DFNxgKxlhuIWAL5fbkWA_5q-O-aB3vHNEUHXDY0_vwmMGLSSCIh5Wazm_fpcEIiJ9vvqqKPhK7U41j0D6WeZJt_ErR5eWvCEG559Q6-y_pjXA8FyRjvyJfGM9o_HlvmzJUMArkaGUGqw51En9QI5s_FtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=RHpm7ipjyfLbdNfpce33EnTCXChd8hEsGwxc39h3-2KFPJbPox_wGkX2StNdl4SXOqnb6wYCRhhsfbhmK0cSDtJkCQ9HRVveUMZi7r-Ge37_zdTFSGC04lK5MCdxqNwopnrDR2eK5F3x9acxWzpE_q7js7BOoohPvzhbloC_YinFKZARNDp6vKfPQ_jy2MYyeEdLRtYJOOqgKs-L7I4BPhp4xlr1NMHl4lOxYa_xTLcr1FfHGXgE6BlmvRrpzVhvBRWHv9HKC2LB_cSxc46wpDpWyOaTJRJUUeEMpF_cvHSn11CutMfqktg812Ho5feOLHtOHYXn9foubh8BEe5OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=RHpm7ipjyfLbdNfpce33EnTCXChd8hEsGwxc39h3-2KFPJbPox_wGkX2StNdl4SXOqnb6wYCRhhsfbhmK0cSDtJkCQ9HRVveUMZi7r-Ge37_zdTFSGC04lK5MCdxqNwopnrDR2eK5F3x9acxWzpE_q7js7BOoohPvzhbloC_YinFKZARNDp6vKfPQ_jy2MYyeEdLRtYJOOqgKs-L7I4BPhp4xlr1NMHl4lOxYa_xTLcr1FfHGXgE6BlmvRrpzVhvBRWHv9HKC2LB_cSxc46wpDpWyOaTJRJUUeEMpF_cvHSn11CutMfqktg812Ho5feOLHtOHYXn9foubh8BEe5OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=tflfj1sfnuSFnW_Q2CJCAruvhM9AezFEYTcHRPDFpiQKG9-vG2Q5VbJwHUzh7ze4_3p85bV_TZD9IDnb4KdEylkbNgZX9VoOsVjOU4w6isfel4_SWdyRlNb7MetQjg-a1icQMRXb1nwXJoCk2Vc-q041tNR2gQdDrP0NRT_E2545L8wISlhoalpXn5IueopVyrC7WNZDEQOveIJImJaSzp07Z1Ju_T-xnUh9rUSPw_mmw8hDltIzi7455bMH4UqtudkdFgbWl63hZ53LUZujd32HWK2Jb6pdLwa25t1K2YHWZBFjW9RrgY5ajr7xu8Jreh2ngxLS3WdbFcQjF5jeOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=tflfj1sfnuSFnW_Q2CJCAruvhM9AezFEYTcHRPDFpiQKG9-vG2Q5VbJwHUzh7ze4_3p85bV_TZD9IDnb4KdEylkbNgZX9VoOsVjOU4w6isfel4_SWdyRlNb7MetQjg-a1icQMRXb1nwXJoCk2Vc-q041tNR2gQdDrP0NRT_E2545L8wISlhoalpXn5IueopVyrC7WNZDEQOveIJImJaSzp07Z1Ju_T-xnUh9rUSPw_mmw8hDltIzi7455bMH4UqtudkdFgbWl63hZ53LUZujd32HWK2Jb6pdLwa25t1K2YHWZBFjW9RrgY5ajr7xu8Jreh2ngxLS3WdbFcQjF5jeOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=KZmPAMu4EVxosU7B3nV-XJghT17-MIWBk-zJ1-Cpe-Ewf0n4N1B_FuSAeOYkNXErGK7QgJHLRzrXmHeU7LP7htVtGxlC8hXWplMkNK61kpOewmqImxTNTuSjhFTx1NeYWijqJJQbDFcNy3lWNzmrFe_HDwfP6DriBs2FFzgS_vOngTix5bCS5yEr77lgdYaU2SSQYHjM95kD2H06f4k-DSd0wXEdvEP3WcTZoNc5ta2-IyAmInmbk4ZtrXXqKI1fYIcIBPIemE_X8RAFE8n9MNjexUViztudjADYZmOJeKYe66dn1yV5SQnaQlppk0dNQRVCN67eVfAd-WFA-9oQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=KZmPAMu4EVxosU7B3nV-XJghT17-MIWBk-zJ1-Cpe-Ewf0n4N1B_FuSAeOYkNXErGK7QgJHLRzrXmHeU7LP7htVtGxlC8hXWplMkNK61kpOewmqImxTNTuSjhFTx1NeYWijqJJQbDFcNy3lWNzmrFe_HDwfP6DriBs2FFzgS_vOngTix5bCS5yEr77lgdYaU2SSQYHjM95kD2H06f4k-DSd0wXEdvEP3WcTZoNc5ta2-IyAmInmbk4ZtrXXqKI1fYIcIBPIemE_X8RAFE8n9MNjexUViztudjADYZmOJeKYe66dn1yV5SQnaQlppk0dNQRVCN67eVfAd-WFA-9oQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZL8fXf9MwS-K3NRHY7QwXqjFOxyJuEXPWSTbqVtH_h-mOSq30yxS25WYWq3MFiLe0CID52RlTTd8xVeoBcZHejWwkkD7nUkWSA0tOY8rtnMEe3nUDPFNa61DNoO5vTi9LK_8vWt6ZIkBjfGosw-whTFd21xNjCbaaBZZMNms0ucZx9EACCoJQBh2vAlAt9RmyRRzpJb5sJkfJ8EWshTQedXHJZMt4I332CqPRCnnc5abRYNtFN6XCCdq9v_kmDxXOjqnzK7E0s_ZGs8Kz9EHOGfsCsfokIvN4-_oqzinsRoUlgv9seY4KtzlFGLq9FxA51xhE_JDHDJLBo7z830Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HftnfSSMsJg0my09wnU_gWoj7YBKJi9n6gqk6UAlK1HsYH6a8WqcYugE7Vdbah6Br_byWkbzWttbFST7NoFV2Xv3GtFWE1kicBoxVCGDP4_Wyw5F6c60oBcTXquTq6n_O84Ej9Ldo4IWzfgMyy9E06MdISQlYST4TadhWEEfPTnn8QRg3iDldk5TCSSjmK_vmiEsCB-EnZtBj-2sDblVQ3dPtEowZrI2LQ3dMbxxsT2wasakQLwGaRkiPxTQd90hPbeMEFEb7mSZxNOivIHTUY_fgYXbCNoM1ZuRqmty35b8LkjJ8Aond3hK7aJMNXGA3nUHlPN2IDfYUqJWDA7W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5SpthHiUKkyl_1yXcKj9u2x1xmXQJuKRsQvZ7AC7R6hItuwYGuDqKEftMMn5jCUwfEQcPC8279o0VjWdN1Ls9anijyVLLYDujdAGWrFhE6Ue3fjU4IWhThZHgel3UW4Gd8GwZvUea3L7Iz1yR0ZBWlvsX0vR0nQ7sJ6--vx1gTCOCwu-OZ4dZFJmLlFdTwYchnauU482KI6-VtRiAusZ29qIry4J7BSltezzV-5sl6uDxjGhcWRi58Hg2EY3l6GuYBticEmkeJKtReDk8oswdn3PC8K06LlYtCKTjzj4dAYwJ-SqKAYoqpIonUjJzDpvV21ZjmSqSReyXfqF2u1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qMem_kZwdJqm0HtKb_yMhbmIaiAB7vjohn3oGnIQpQiz1xhjWIxCSiIsqqm6c9iUkwRCK_TJm31mIvFc2k_HJOZJRspnl6LtlZ8LrQ8Q5i5ElKMQavhQBxFBxpwIuIFX2v2gxbhsEVhys2xtuwhMoI7AXVRQ8zJX7I5aDPYP0bp6bTJGdRE2GDpf6uJZmajMB4We8saGlnb9F4daSy4e4mgXrEVManro_diexU9g74NovwrnQjdwZwUM-abf7OyF1fQS5Wt5suC6DwHqtZ4Dz_pjNCCjwWzT3VzeU8dOP0pIZC7hxuQVEM_aDpABp5yuFc8EL-zMc-0Ox0yAtfDZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qMem_kZwdJqm0HtKb_yMhbmIaiAB7vjohn3oGnIQpQiz1xhjWIxCSiIsqqm6c9iUkwRCK_TJm31mIvFc2k_HJOZJRspnl6LtlZ8LrQ8Q5i5ElKMQavhQBxFBxpwIuIFX2v2gxbhsEVhys2xtuwhMoI7AXVRQ8zJX7I5aDPYP0bp6bTJGdRE2GDpf6uJZmajMB4We8saGlnb9F4daSy4e4mgXrEVManro_diexU9g74NovwrnQjdwZwUM-abf7OyF1fQS5Wt5suC6DwHqtZ4Dz_pjNCCjwWzT3VzeU8dOP0pIZC7hxuQVEM_aDpABp5yuFc8EL-zMc-0Ox0yAtfDZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=SZrLWwo1h0LdWz7FuH7J07nmXty3XV0ZuPHMU5OxxwF85HctSn2So4IW0Zkjum1yplG1u_qFc7a9pd8_NmXN0VMDMDghjq0t0rfmPWmKjosbIBh3_AnGMf8ugejwWj2dch60wj7MMz1b8yU4tCFDtGDXAWgOhA9B4sNifPJq9aGQ4CvpLufvz8OnhV8sHGn_tWty6YTCAW57T_b6wryuqqwz1Z6BjAxIl8hn6-KI1SXzyzh04RjEwoRauDQQMyGqxro86a6iW8XA1OpH8AdFai7O5sGdOfKvWplGYSp6PqEM_ziyXVvJeAOYonkcSpkNEMot19v95JDaoGyaobO4Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=SZrLWwo1h0LdWz7FuH7J07nmXty3XV0ZuPHMU5OxxwF85HctSn2So4IW0Zkjum1yplG1u_qFc7a9pd8_NmXN0VMDMDghjq0t0rfmPWmKjosbIBh3_AnGMf8ugejwWj2dch60wj7MMz1b8yU4tCFDtGDXAWgOhA9B4sNifPJq9aGQ4CvpLufvz8OnhV8sHGn_tWty6YTCAW57T_b6wryuqqwz1Z6BjAxIl8hn6-KI1SXzyzh04RjEwoRauDQQMyGqxro86a6iW8XA1OpH8AdFai7O5sGdOfKvWplGYSp6PqEM_ziyXVvJeAOYonkcSpkNEMot19v95JDaoGyaobO4Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFhHyFYGDM8vZjVKC58lI4HkQ0Mc_0FkMPZtvKqSH-qX2nK1LiJ-V5llcydDcqjnNE4jYHzAxOhlxF-7wRbpQjQv9hr8H9Um0xJIA0k24voMVeOJZ2ubyO3Li8ITk3Vq3tchRWdh-7RT9RJL-3GBYmZ2AWpazQVS5t1UgnXkdMMKJcCQvaqZ31wVWtIuxv17wA9aaMyfsLgCWLJtKRmYPeNDbTjqOJbr8J4QbZYMiLnJv4BaW7JWkR98GDfDqrvJu9C9Z-Vn6KKtZgUFvoj9bEOvvNWeYmiK12sK61DOzgsygriz78vy_djTbEMmWdbSAzu5n89LDuF03wR3yA5Hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwJndx98Hsh3xsKSo6RVg9rVXkKRQFF6VFKLZ19QCnEi-V56AIY26Tu1wyKcjbRTjSQtQeXm_khge3CnAn6NLORInNyPMrRpT5ioRjcFsXw5JDpQr2tlg2DoR7ZvajEm9F0K5OkM70Ce4-vcqNv8TPKehzI5QSAot3w5s2YCuZBKXITnlBaxC6pz-5krDJMWwGiwqhEvZEj0tGHcr9VQxjbN37c6EmhNUa69DXPH7w1IgMXb1SyD8ptoHgE3v8A0jZNeKi_J6rcHTtlRZlJICeUz-0PjdBCz7MQZDeTxNoMJr2JmS60ZyS_BoZDCk5luE_fYTNJywf6uAObXfgWD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=ub7SQOYWMQ6V2xo4XLOLv0pWYIOof9dlM66MYs3C8T25dG--d4hdnOHoFgl07EKUFRTNEzHfE9lloNhmVBC91mNHnnFL_oxLKziLHSyTo1IS_Xkws4-omHbGC3oX20AfpJASBniLs1_Ch6BtbXOMTcuaP2adRDxPw9UJ6azakCEUiSM2sl0_RTnwALMt34zvJecUJd8J3_4H2oxEETf69wNX-UFsOK45RSYcftp7xNilJjJgMb1NW1eYaTs4UuxtbHthOk7wxLCz4SX_Q8-FyD583PysuiN4MFXhuYYCzP6wekok7nSwTTe9RdQte-qW_ky31tPv3sLpKqiV1gh4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=ub7SQOYWMQ6V2xo4XLOLv0pWYIOof9dlM66MYs3C8T25dG--d4hdnOHoFgl07EKUFRTNEzHfE9lloNhmVBC91mNHnnFL_oxLKziLHSyTo1IS_Xkws4-omHbGC3oX20AfpJASBniLs1_Ch6BtbXOMTcuaP2adRDxPw9UJ6azakCEUiSM2sl0_RTnwALMt34zvJecUJd8J3_4H2oxEETf69wNX-UFsOK45RSYcftp7xNilJjJgMb1NW1eYaTs4UuxtbHthOk7wxLCz4SX_Q8-FyD583PysuiN4MFXhuYYCzP6wekok7nSwTTe9RdQte-qW_ky31tPv3sLpKqiV1gh4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=CN8UnLnEAMBrO6b2Jh-osjp99BgbOLR6gbSRJ3tdX8Vx3CLRASjScCGrvlroYqmwZnyOELDFN5tkI2phbSbzhJzp6isX8RIwydkQwHj7hlXVHpRg4CIoXgEwujBqB10cCWPfmPwlEikkan5wssIQ3tC1DgZVuUrQdraIs66xdvj_-0uJo3dTo8563B1ZaP4LMTGTy0XsIq6N6AG9RVWznJu6Tx18He5CmMlYIMsbFNi88cnIBETpsGU2nlcFcs32yzojzVYywYJH3duTDA2XjhENUeiDts435Gge_L0tkLAiAgmVyYecLfmoaCp-nbPldNHsP8ZQYXhrUXgaEb1eTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=CN8UnLnEAMBrO6b2Jh-osjp99BgbOLR6gbSRJ3tdX8Vx3CLRASjScCGrvlroYqmwZnyOELDFN5tkI2phbSbzhJzp6isX8RIwydkQwHj7hlXVHpRg4CIoXgEwujBqB10cCWPfmPwlEikkan5wssIQ3tC1DgZVuUrQdraIs66xdvj_-0uJo3dTo8563B1ZaP4LMTGTy0XsIq6N6AG9RVWznJu6Tx18He5CmMlYIMsbFNi88cnIBETpsGU2nlcFcs32yzojzVYywYJH3duTDA2XjhENUeiDts435Gge_L0tkLAiAgmVyYecLfmoaCp-nbPldNHsP8ZQYXhrUXgaEb1eTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJTazUqxtpDBzIzKksJhL3Lo_kgmfsirOhEJX5hYLn0uv_Nz_qQrZybYx8B2iKZmQOhz4Gr_KBxZhk2_X5zhIK9GufXocdnom11zT6JYKaxovPvnfxKIRR6TYMBFym-NJLRE1PeesKpfwpGVMVri2pPiWZoUXS7Oh-fzi8C46XRg7xQwAESwfEN09Cqs_6PTvSyhcPCHXrjBR0CViGbTz3NFmCUJ3V4yoffmzc1QfrislW686sAHA8ppR5zUCBXG3tGKf2RVvwr1JpWuRGsMXyWSgRSuZT__7m1ZD4L9DPg_rMfqt6wxgeQ8gR_dqXpEuj6-qqlXLffMMbylZS89WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwYcG2ecROhuBkjYRvbrYNJdl-LE0pjA1d7vIKJUsjkqi32HVNcV4R57_thaL-jsLW2POyCKY-ThlmFeNY2eHq7wFFls-hNdhOCggM6xnsCvcRDOjwoeS2U7ME_aza7Gk3sNsyhUOjLxkk5Y-6lwpLy94CIuFiDSQfSLslPkepQsa7kjT0qV5pDxn-4VLj2O1RUBrXGFRY5qDbuxS9P0HkDHwjLYGsW2oxKyU4sFnCCLcwyS6j3yBr_QiRsczGkjbFRXnfOt24lTeURlux7HSbDLzZcu-b0eZUaz9NAdUAKl9a9XzMzMRNL8n-oQclZ7wywzEm6il9vhKcvq0VBO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=Apcc5dutoplExyXHo07gw9tUjcY84pIhI8zaCSjFT7NAf8IxTXEmVyA_qmAqkjoWUXDQHZkujeGgutEyR8eZllDY8dnJ7WftwRrOWBgXD_mTJbOb8H7T1Bu_69M-fFmAGyT3VaFV_RlFVGlrpuh7BzGLEQW4XK35_E7-memia3G0Zr4KEA-y8V2PeEXDquK1dDmtWvBUyJRqZoX6KtPZ9hrxqMCKx9Zy0eP0336fsIVdlOpfso-YbWhjZs3nhdNm8XYtuBxh7mteLE3dnwbuGMk4uXKxRNkOSVbv1zH839MLGxjx6kszt0B-Lt9HP1RNif_jmkQPQZ2kx0YiA46EBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=Apcc5dutoplExyXHo07gw9tUjcY84pIhI8zaCSjFT7NAf8IxTXEmVyA_qmAqkjoWUXDQHZkujeGgutEyR8eZllDY8dnJ7WftwRrOWBgXD_mTJbOb8H7T1Bu_69M-fFmAGyT3VaFV_RlFVGlrpuh7BzGLEQW4XK35_E7-memia3G0Zr4KEA-y8V2PeEXDquK1dDmtWvBUyJRqZoX6KtPZ9hrxqMCKx9Zy0eP0336fsIVdlOpfso-YbWhjZs3nhdNm8XYtuBxh7mteLE3dnwbuGMk4uXKxRNkOSVbv1zH839MLGxjx6kszt0B-Lt9HP1RNif_jmkQPQZ2kx0YiA46EBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=ki6W-x-YRoxrrnZg6oPntTzfWcLZzGZB7GopVEenRQ3610U3h_Uv6fF7oCxhBWyNCuu1gxZDMyQQbsR9TJ1dekpzIzTgMA743-1_bskLEjyw05ddsUDL9JPdR2ubIcA7MNu62Qjw7B1k1Y-A5Pe12D7YbTu69LWx3e1pvWxU0cRqRA2SrGbK7s5VQmK0UYtBj6_BSlmrs6ZQXcRPfCsmFeokwuaV_J8DTSWGoRMAMFPH52rVfHajmiJe9J-7je8U8JsQm_0gRvcoFCMKm0Vs0sAI37ooemvDvLff4ok5K1CiKP0J5Vtl8i_j3LPF2_m1SdMfebiQorEH5e56ukWHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=ki6W-x-YRoxrrnZg6oPntTzfWcLZzGZB7GopVEenRQ3610U3h_Uv6fF7oCxhBWyNCuu1gxZDMyQQbsR9TJ1dekpzIzTgMA743-1_bskLEjyw05ddsUDL9JPdR2ubIcA7MNu62Qjw7B1k1Y-A5Pe12D7YbTu69LWx3e1pvWxU0cRqRA2SrGbK7s5VQmK0UYtBj6_BSlmrs6ZQXcRPfCsmFeokwuaV_J8DTSWGoRMAMFPH52rVfHajmiJe9J-7je8U8JsQm_0gRvcoFCMKm0Vs0sAI37ooemvDvLff4ok5K1CiKP0J5Vtl8i_j3LPF2_m1SdMfebiQorEH5e56ukWHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=ELCS0_ITjYmewo_8hNr6T6Bt5QzdPgRWpk654RFZWZGi-mKZ7Jjen8PvNMX82Y_U2TvfF4BivSzNKLoe0_-huwn4nGAU5baPBKlTRSWKuzK5X78KPbYYq0A7R56ia3zNpsN3UI-CpY8ojV0UZb0LVYf3yAimk2u1SsqZffVLFtSfwoGATRYdx9laN_lA5VFOzACKsTvlreqZGj7wTVeyN20vw4DETp-qX2YmjLwhU92_vcyqd0zGsT2_c-Bn7OS-tTFV52i9NGqgwJ5gtfv15Tnh3SSlhZu5rbpQg3diWmDd99PH6lKEnBEXjw03IXaAqzG33XdswJ8CkOD0EbHtdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=ELCS0_ITjYmewo_8hNr6T6Bt5QzdPgRWpk654RFZWZGi-mKZ7Jjen8PvNMX82Y_U2TvfF4BivSzNKLoe0_-huwn4nGAU5baPBKlTRSWKuzK5X78KPbYYq0A7R56ia3zNpsN3UI-CpY8ojV0UZb0LVYf3yAimk2u1SsqZffVLFtSfwoGATRYdx9laN_lA5VFOzACKsTvlreqZGj7wTVeyN20vw4DETp-qX2YmjLwhU92_vcyqd0zGsT2_c-Bn7OS-tTFV52i9NGqgwJ5gtfv15Tnh3SSlhZu5rbpQg3diWmDd99PH6lKEnBEXjw03IXaAqzG33XdswJ8CkOD0EbHtdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_mOLSckOXIchnTE1KoYJHuXxXuNYfTPpXI65DPO6bzRvaHlKPXsJImfniSNyEKwcZM-ACWU0ylBe65X8e1hDbLnwwB1G_bjn1-emHy-1y1jUsWt8V8cqCJ8qFWL2UQIc-3hrwSoNOmj1e7yZJk0VuucMwx4t3lakjVieLKtbuPuSXRZes1KN0Jp-QkxoZxo7ZIEirVh_akpYDyl44Fe8gEU2f2kdj_mO_urRUvQ78jUrDcLuzPvE_f361-6VFPnK8fnnwWeXyqcCQnHPz1yGyB5NJtA-xA1ALGR9eOBADJAI9yL7I9PMeiFN9CF9x3CqpV5fVhWwFuLXX91LgEDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfCHKTKA7q7rqs1BYt6B0_qSgG7WeKQCZDpLSh2A3xtNsVdGyK6Jkzhu99QwJYjpngyvBUJIs7n48MUFkrmG6kIvnC7ObA7v4KNfaeIVS--HD3Hh4jYhvSrQqz48ZozAeyNV5JgVCN8epykd1aWR6Zc33x-UAOAzpMSussOfd9N0S1YYSD8QGVnL1_PN-luUmMB0OPFhromf5g7xqyLMXaxdp6NnmvaTuyKoiU_kEo8-ssP5rDrn2ly6R_7pEwPVO6h16CF0bBDjqsM3OebV_OpHGgDaHsRcKSPj4W10BRRw3wlMfgB2fIToK11I7VsvJujB_2a7PSCgg2_n_X21-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWjvWJS5dJJsQO2fAxUkYYA_EMppTmLACIwPqVPjOsXh7Oh4d9k0pWNuOagVE_z6M_GR7CfqQcxQ4DR4algnryg_FYE3J0MNVEyggPy7IXTILacT_baR4zGRFc8SL5icMdO_WpIhZbUMaRPsZ5qzNc5zojIqH-Kmsen2pGHkcT3ZWI7JM7F7RYGXvLFGLLskwE_A-Vzl7wIdukgUy2TixDTCV99yJRAAUuO7NVDlulDrcZNPV7UuEeUBEazp_oqZ2y_GwOMrPYvqBvITtMcvq97iyZe06PlEYQAzr_aFxi0mjkYkjJ9APx_Aow86XyaHhNXHC8Z6LxtGm6Bgw0kgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdFrDGig7w8nL3RbFmD3MeFjj2rFtca9wqq7zWj1FMbi-2is3peUi0zwWELi5aXd_0bgrkuTWyDydKKs3paVXJmu9WJYH4XWTF81EW5M4-9VicTEt-tnLDAnGvEFloDwNWEeFDm1mXoLhRwy5S_9tV7K2c5GMzUpFt273bRI1O8mN-xroe5UU9165wSmRtBLVdw4GndksY668jrW2VjrOUXJufcxaNnC4fSjGQBFSm8knOOaidti5cVWKT1dbHZMcMJgyKrRjZaXSfiBxiFeAqY6Cycx8_RnfsRjE7orw05ekjG6KsxumyCuGKHmAe6RF8zAe5Nt0M5vx3CcWk0Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsIp34KFP8iLkr6yCU5E7Q-INC5tDpTrxQKoNkDgJ0vijctbzbqte_TG6LpKdezDdqV4WkgXATh502PxLiwZSnX9wjWY6LUs_hqdh8OBhgB9iZi6mtczpIPM148ACyAVCGliTh1rcdlmwgescB0aIZzf294SQo-NMOxTX4X_GDXMdWWx-jPIdGUIPK_mh4WuAURZ1mqf22DieeUtZrsHYT-KRpIrhaPaiOgwiBg39eZ_FLw5E4-WwEo8UV3I2HSioN3vTJNh0nM5XTSmHmsYsB-sdvZQf6Mz3cKzC3j_BMcTC3f5zIkacoSvPzLlzMgjvW12daQKlCZgWDxhI0NwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=ehaxjH_L9syGWtolnH08SQgMYE-3FFEaFDM22nLTPBvG9yomm8PzHp4atn77yFaMB76fEFksfuIYYZzXXSDSwtlFTN7t3zfd3LeJ2xEURBsfaApSseudLntLItTwMT6vDJDx8mRMxWU5133jktQvxmhzqlAaWl6a3DSoN9ikMzFBjXYU5VUi0PjlFDDrAIyR0r8Nf_pFfIwSDFH_UY7wU1OVMNTXic04c8DcuqTJ23SuQF50-ZbymgXZ_3rB3s3NySSLkRcH_qZGKL_KMdchrev5o46sXMJMtlJSnzs-uZxVapopb82_DYjHFHWB0LGOisGyveJahTJ_IY9cbEX4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=ehaxjH_L9syGWtolnH08SQgMYE-3FFEaFDM22nLTPBvG9yomm8PzHp4atn77yFaMB76fEFksfuIYYZzXXSDSwtlFTN7t3zfd3LeJ2xEURBsfaApSseudLntLItTwMT6vDJDx8mRMxWU5133jktQvxmhzqlAaWl6a3DSoN9ikMzFBjXYU5VUi0PjlFDDrAIyR0r8Nf_pFfIwSDFH_UY7wU1OVMNTXic04c8DcuqTJ23SuQF50-ZbymgXZ_3rB3s3NySSLkRcH_qZGKL_KMdchrev5o46sXMJMtlJSnzs-uZxVapopb82_DYjHFHWB0LGOisGyveJahTJ_IY9cbEX4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyGEAJWnoVQNulGA4u4l4na3XQl5qIC4djoEffb7e0SdWY21tpcFOcKZMjYVgybRQavyO_Gr5onVEFcr2qKxfIZPf7QTWY0qilt5kquBoJB4jwbzU-sc1YdOiCvvWfKCphw5I0nPX1kRQNTPaYY9EeVUs8jl8ossEB0kDtI5dhvjsRDPdganyuYb8zNaf8mPKycfL06--JAzlry-J4ZXsNAuCzC4NyNw12TuGq270m_suTYbZXK19nQueaTmSu7tN5Ec8AoH7ipGQEEbZ3MsYM8aGxo5LoSDCGgdh586kr3eVp5_wZNP43lloOa6tTZsF8Z5RHH0ak9Pew-TZ-5dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=lk4j8dWM4BN1nHD-yQZ0_Tl-KNJXxruaxDfa5yY-2t7Y3QZf3pv0Wur92KIq1xRrpMIvHzlTcYg_X_EuXLbYqROa-yTE6kmYJAGOeaPnCGgfx46sQorTdskLfquuYT1taDAMIeSJLETLXXpKiedECYKQNs6Fy2Yhneeru0XKfL8dsOEvctkU4KhEciIaMNDMy2_dSFjmWoQeZyGpUNtwcf0MZiTFVj_rvwWGXtoS0tEUMafOr6hu8S8Ayht_EB7WapnjR47UsQMLxqGtXSCGilWQ5FqS0p1o79_rvtZQWinw9IvQQ5VQNZe_lag1puS_iNLPmE-CWEGC8mHmhQAqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=lk4j8dWM4BN1nHD-yQZ0_Tl-KNJXxruaxDfa5yY-2t7Y3QZf3pv0Wur92KIq1xRrpMIvHzlTcYg_X_EuXLbYqROa-yTE6kmYJAGOeaPnCGgfx46sQorTdskLfquuYT1taDAMIeSJLETLXXpKiedECYKQNs6Fy2Yhneeru0XKfL8dsOEvctkU4KhEciIaMNDMy2_dSFjmWoQeZyGpUNtwcf0MZiTFVj_rvwWGXtoS0tEUMafOr6hu8S8Ayht_EB7WapnjR47UsQMLxqGtXSCGilWQ5FqS0p1o79_rvtZQWinw9IvQQ5VQNZe_lag1puS_iNLPmE-CWEGC8mHmhQAqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=QDCjAS_THOcWEfPePk0GtfBjnz3x-uqWPP70YoG7MLjY4MQv9SRV9o5w79PfwWh0_vRDjXycjKfema92FHVvyxrqub9S4K6p7PP1pFtvGnKctt7p8gn-VGSyMUJqikykbhIwJHIL_q5bFI_TBdGyEb5FtDBP3qY52j7-_z8Y_iPWRT-5uTm-pYsLZhEJduM1jglJPuERqDi6X8OFf1L4SIHWmvWc5CigF_RPW-sIWZV-gOtsMBL119SPKtqITFwELoPb1gIz3CFnQDuZWaBtJKtx4V9m5kqwDGcvLGzL4LjLQXivLlpPbm2ATv-lpVJxRwoWA0PcTFlcbqA3fnT4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=QDCjAS_THOcWEfPePk0GtfBjnz3x-uqWPP70YoG7MLjY4MQv9SRV9o5w79PfwWh0_vRDjXycjKfema92FHVvyxrqub9S4K6p7PP1pFtvGnKctt7p8gn-VGSyMUJqikykbhIwJHIL_q5bFI_TBdGyEb5FtDBP3qY52j7-_z8Y_iPWRT-5uTm-pYsLZhEJduM1jglJPuERqDi6X8OFf1L4SIHWmvWc5CigF_RPW-sIWZV-gOtsMBL119SPKtqITFwELoPb1gIz3CFnQDuZWaBtJKtx4V9m5kqwDGcvLGzL4LjLQXivLlpPbm2ATv-lpVJxRwoWA0PcTFlcbqA3fnT4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXQfjIWzsLCOUNP0SqVhXNLt9LStM9_XA4sef5f6U18xKSe-UD4RNwaeXoUsO9xVyNJE-cYa9FuoUywfVXHGXAk9RobwgdecDBiAU_P0p03-WlmYYnMvpvSuFVh1iNNZKqA3qB3G7LWV4Ja81WpKFVqXqgBWE7Rw_xK2hVqw9aU3Uge2I2pn7cDe0N8f5HKconBiDaYoTVdFo6DCL2YvpDH7b7kr0KBOoiJ4Jj0zU9CGDxRwKQ7atZajbfuIMiBAiyv4VIt3G9p7U4cUAnuivzTT0PTg3dlRzPnpiK41usvYKtmPPsVF_1v-Kx0Msr10WDCUgOim-6GQKPsvCE9Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDlzwB-85ZMqP-F111ovxn-4T9CKcUeWWzwU81pOinkmcZrta4bO3scuWm0Umxi6hiAeLj7GlRipheXnkkbnqJpGJVv7qb531v5cUzSh_2g8DY1hqu_UhuOLsvW1VyYtmbMOOLrR66omsuy52b1Jleo2NmauqilhB1Fxgj8jPvm8dugUD3HRK53zjErUGif-yaz7DJG20Ju1wOmO73JmuC6C2esodP2u6Mm6OqycONa7lywdHobp8WXOoiJqoF19PTl7wPo-3FBAYF8PtUMIoNpBzu0F0noai1HGV7n36bH1krPZTQgVnJCw-0G8z4YiX7U3WTP5wVj_ZuzmT_vRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usnv2-7rUG_sU4iiBV452mQuxv6l2qWIsiUTFxju6-tlZ9u2LuwiAoGERYCEn89kUtpY3CPFK9x-f8ekhFm5dXrJIRG5OKTPyQY9prXYTHaF--6ZzoFXmHOoAWsVTDekwpKVemucSNLQAkAG_lstumjgme18ayCughqEVSwURFbEEFABRBzKE_2uRD0rCAtVoP0FuVgbmU2nmyZOm7QpKKaxIbqgP1_iZjRBmpNGCQYYVQd37KHMFNrvQP5xg9mHgwJs7nGU576mQV_MmUcNBVLFLb6SfdNFdujtHFiZhBPCsOEVjDtpER9FToBf1LW4hVrSCLT5UVD--E8xCtN9OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LW2xS-oe20BNQfqN4mKlIKTezpKkzRMgvn3DOpUD7Cj5-jdUhuS8EGJzUEtaqfBP30JIdjdyEHsFDixHM-cZL_sEZnPzSY4OJMONuqWts2JLEY_8rQuoF1Bg1vndUpKWTCkhGVJF6jz7Vv18AjBCI_60zLkN0pf-ePp1ug8Q_ua5suWxJxw5R8dWN0SofLUeW0i7zA32o1Ku5Hxo6DwoJZYCVNMNrd4CTLE3W8JpSEyEdEIB028SuKO5Yv1JbSrkckdDUksUMRMA-coOxIpuAo08LndqlrJUyuvo8h9LCFKDe-FreN1wfBU0yAAj9hoGCi_ncXU57wTcqdoDDdT1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-JG-EiN90M-3ij9xkLmKesGCiyqe-xbzI7uvwZz0Et75p08BL-RIu-fUYmDPYn4T_dSjRqoYG6sAlRgbQXSQQ8BVkWLWbm0lAvT8p8bWNKqNo16vpDE4oLyrjLtr926Vgqtuiq-1Wf6BK2o9lFuA1LNb9ltbTq-1Vgp5h2UbEprNma9HuBJQJMpLUlMR2yh46TxCvcRrsR_s54144F1-saDuQyNprxhp5naGncWa8_o9h7cpvbgXmkcuT7bQ0T83dHY3F-1TQ1icapoKE-eS387VVP43YproKtscn1tM8tRBbEzsmlkLH6yd-VFST69YNRJaBfx2954Ca3yx84lzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=LB3X7b8KEtEegLHDXA6ZFujxr24l24grYRmOVoSHPAmvXPxRf0J0SdtSGRNE0y6VS9_F57Di8YTtXiU5MwCaciXM9zAw1QAcnnJbiLFC1dVzS7rzVeHBs27fEcXW0DvSRJ1pJik9q5Uv0A61LztKZu3q6Yq3s1wd0ya0c83DA0TkoOI1iVwY1qqSVkwmN7PC6YOb6XLQJbn-QQXH8bAQdP-gUT0iH52lj93F5WjiYbqZYjyXI8UxMOeQ7TlK-2uOs_KxasbW7ElsBj8Jn5HWKhIs8ExOyXrkhuBYJ36oynv8poLxbSJdykmYNSIC5PxekPc2sO7jUmHgNli3KL83dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=LB3X7b8KEtEegLHDXA6ZFujxr24l24grYRmOVoSHPAmvXPxRf0J0SdtSGRNE0y6VS9_F57Di8YTtXiU5MwCaciXM9zAw1QAcnnJbiLFC1dVzS7rzVeHBs27fEcXW0DvSRJ1pJik9q5Uv0A61LztKZu3q6Yq3s1wd0ya0c83DA0TkoOI1iVwY1qqSVkwmN7PC6YOb6XLQJbn-QQXH8bAQdP-gUT0iH52lj93F5WjiYbqZYjyXI8UxMOeQ7TlK-2uOs_KxasbW7ElsBj8Jn5HWKhIs8ExOyXrkhuBYJ36oynv8poLxbSJdykmYNSIC5PxekPc2sO7jUmHgNli3KL83dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enjBvQKUwzQgdTckzpeLtPgoLpIqeA5kMDu7JicpF2XskfR8So7bXAhKskjMkH2EbGzA0OkyoNdODPelPHRYrcrNgIstsKRO-53WNFir2JvmU0YqcCKoWnj80ErsRUObsk6QQUinMBJsD-KLxqnsO_br4_frmkgEQPdbiwOG8B1qCitLPBH7uQDgytViccHG-pQ0iP2OWRgJJmuKbjgsaYE-zwASMsOKwWWFe3lUJA6fMVs_Xk7hYdxakEee8-68rw6BFYaSPkNusjC2AyrGYUsccAgUa_aa1lwkfF0ySJzSc66y_tbPci3Q1DiSMehCFoliIUaIOzKlks1YA41wKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=MPSnCYIpF8sBTQ1J4ATdkLyBQYvCVMvSHa-tvPjjVTpycEOm3OATE0eGyEAh5s2OIdKZfImSOvHXLFdRGKH3_Vfyjn8hxQxwVfMZpKi8wy_Y5KpAmhmBRJRov6z2sILP-yLfffs24UkO3tv8t4ZX5Iy1FAUUI1ofAjWoy8rV0EZgLxg2DdW-iObMNqBCLh8jYvoI4C-IiyWuWeD1f8DzoCfMq1vmo1oVi5_ZSWK74izI_6qHkg7ni_GoykMA3GLDK6_i91vpIX6MJTiMIlDbUQfKNsG1rPgtnEnlsGSNUYyjP3UtCsuPy6ekS4AMLMGpVZtX3-lUDiwehgJaLBVhCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=MPSnCYIpF8sBTQ1J4ATdkLyBQYvCVMvSHa-tvPjjVTpycEOm3OATE0eGyEAh5s2OIdKZfImSOvHXLFdRGKH3_Vfyjn8hxQxwVfMZpKi8wy_Y5KpAmhmBRJRov6z2sILP-yLfffs24UkO3tv8t4ZX5Iy1FAUUI1ofAjWoy8rV0EZgLxg2DdW-iObMNqBCLh8jYvoI4C-IiyWuWeD1f8DzoCfMq1vmo1oVi5_ZSWK74izI_6qHkg7ni_GoykMA3GLDK6_i91vpIX6MJTiMIlDbUQfKNsG1rPgtnEnlsGSNUYyjP3UtCsuPy6ekS4AMLMGpVZtX3-lUDiwehgJaLBVhCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=Q5za_SeqxJaB5-lQ9ZMOK7yRj0zojCEFKvsEhJ_GCLRIhtkapBtgeejZNeND9ITRrTOhqlzw1c_i4MTSJCJ82xhkdKAs9_5klHxm5zXQEagpvaXUY-PNpogD4d_8VnsXsGUeAfZMfdpuKMLLVUx4GArfvykJb2FbwKkReb16X80boH-a8mLEAFQPBbyICg_E8sXclTpXMKnLq2EYkS2YRAcoQpxbvz6jrs_tXaEQC2UDjpcBKH31mKT8PDZH7u10yCDqaMtuK7-INWaGw9pioTl0dhfHEsHPDMoLUExBbiDTnC-bW1pnYjWg0idypb16S5fOfq6uxgUoYGYV3x52IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=Q5za_SeqxJaB5-lQ9ZMOK7yRj0zojCEFKvsEhJ_GCLRIhtkapBtgeejZNeND9ITRrTOhqlzw1c_i4MTSJCJ82xhkdKAs9_5klHxm5zXQEagpvaXUY-PNpogD4d_8VnsXsGUeAfZMfdpuKMLLVUx4GArfvykJb2FbwKkReb16X80boH-a8mLEAFQPBbyICg_E8sXclTpXMKnLq2EYkS2YRAcoQpxbvz6jrs_tXaEQC2UDjpcBKH31mKT8PDZH7u10yCDqaMtuK7-INWaGw9pioTl0dhfHEsHPDMoLUExBbiDTnC-bW1pnYjWg0idypb16S5fOfq6uxgUoYGYV3x52IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TB_og1_5mgFsWCNlfUAUxjOGGyJPaMCZBtohL8JSabWeskwk9uZ9Ywxo9pdE9ABYObvt-ZmhHtuM8heoJnUzqD46RbEqc27ANiOqPRrSHYAx0hngURH4ZVLtn_Ecfgte0YNBSwuvQIHsH-DyYnPsRAhvVb9jYLkzgNlQbzduxJo5T0CL5L74YWKVSlNCJN9RkfyfkkSsWQeTKqc7Nq2RtKBCdB4T47o8y0GAIbj0AqvaKx2gF8-Z4xa4HT2zmOsWsXUelQ1usM2zPO3O0hYrSYSMhLCWC3A9r_godQJ0tvMvjN_NEXMBVklQ0LW1wsrVNEAypfdP-LWPTzdi2l2yyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=DaagyQ_nI5mZYXjf_JLoFN9H92z5nqKfFaC836ie-VVfqqp_u-YJknHAnisQnlLjjtSwaUtZqAKGXzifN2GM1DbcpXUbgnExtkwLSgHDH21-AsHqka9XzKPN7PnHUQX0VolGKqABBfSO_qw6q0d8wYvcH2X1EeKSS37w2WtLtGRj6vLhVgc8x0Hx4cqSGpABJbH6bXSCBJIGfdmvFuqXpPb91BTUBhNlfpR5UFp7EHeBjFUKRVEkC7HrQSubfwcO3J9qgoO0qvHwh5n7lbmH8s2o0dQ0Q8p_1_3DqdNj4ko0rlkyoNmTpGk6CxUmuXGsJr85qcKkSHprcHvnE2sS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=DaagyQ_nI5mZYXjf_JLoFN9H92z5nqKfFaC836ie-VVfqqp_u-YJknHAnisQnlLjjtSwaUtZqAKGXzifN2GM1DbcpXUbgnExtkwLSgHDH21-AsHqka9XzKPN7PnHUQX0VolGKqABBfSO_qw6q0d8wYvcH2X1EeKSS37w2WtLtGRj6vLhVgc8x0Hx4cqSGpABJbH6bXSCBJIGfdmvFuqXpPb91BTUBhNlfpR5UFp7EHeBjFUKRVEkC7HrQSubfwcO3J9qgoO0qvHwh5n7lbmH8s2o0dQ0Q8p_1_3DqdNj4ko0rlkyoNmTpGk6CxUmuXGsJr85qcKkSHprcHvnE2sS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWdbd5s48jhWp39jxNmHg5TCrfb_QXnPQZdF4Oc30eRM1fPo6HNCQsX2fqzdns-1TYRW_j2skXDP1f7e_6bip-tohZt0hlsVQBR3CcIXN8ZYPRYfd1IvCStyhBgTQ3IN3l2E5iCkQf9K_YWBG1KQ2oEeie-bF6BKX5Rg1FOvEMmQYGlj52bskJ_8blAsQYuZHMIVafRi266NMrJ0UtTJ3qDeyPnkDeKjd1RDXoiB7XtOFFu_hFkCC62frEZMC-X2tB7wpuHzX8Iyt7DjdfmlnbIXN9uPEjGNLqtsJUPjvSc2ly8RiXwgukgZ1lWpjFhl-LUQYacuUFrn3eQ-QYGRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
