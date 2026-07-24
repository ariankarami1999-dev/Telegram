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
<img src="https://cdn4.telesco.pe/file/Gf-rcMXVJCuJnToOVVPNLAmNjJSvA1hmiwYb9mSv0eVxf7Qr0_jNEphKMHC5HJNQzFwzapeYW4y9zuHV9fq6uG68iNHQpvLk5WI61fO7RSFcKVWjEbGdsbVt1AMnlrD4gD9GGYxCMpRLaUor2MoGvEGQt8aspUL7wuV854xx1blxUl0rhPz29zpcUWo624d3vHdIcCOvvWnbAUrvjejJJEONMyjRIDqDmlwaWwuSJz-vUHgkFpsqFPTKJnswimYrrrAIZTI9XtWnN_DBtxi8GYTma8q-E0C8mhSrwadkIBwQXJbO0OloL0qG8VLtI02WJOpYEWmIP8OWQl8D_ndj3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 207K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-81198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromِ</strong></div>
<div class="tg-text">تخم داری تو یوتیوب مقایسه کن</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/81198" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEoieOia8Hl3Kk4hHakC-qL0nDz-zGNFxJAUWMIRkhrZNrvUJUUWN4uGWicNvORe7hCYz90gKy3fYQiJJI9IhDHGBBf4PxaaNvtwOooLvAh7NN7vVilfEvEKoicRmSLZpimp4uAhXLhe8zHCiJMRSS-4rrChlfp7YoO5RiX2U9De_Y6zOYUBIkbqmMnlNqROD_-dZw_mRLVDIv9MVZAtfeRdBg-tt4W-fVgKDVk_fcX3UYjmR_lgRmJIeXPtxxJNlB6wGFHj3Tbg4CkhEvgtfM2N_8GtYVrMbAYMfWra8Z2xCao9-s0qvhBoa4nlPo9ADb1P_O4YyLHZemTjrFXXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از مقایسه رونالدو و مسی توی جام‌جهانی که خیلی درخواست کرده بودید.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/funhiphop/81197" target="_blank">📅 18:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGdKFh1TdIbr9XosifJ5WLH4146CeqhzRF25wkr8UHhfYRIInSoBKQA4XX1ArosdjG1yrnDkYfCyZQcQ1nzJmr1Nd3D_eBaNNSG1pSBWdw9qrZkAIMOpu63BgnmD0k_JVMumsbdOEx2ZEbaKOaE4S7LsipMD-g5YY42OuF8EtSdi6_WOzjQzQ84xQuEf45gGH1b_MIYI6dN4uYN9QkGMcwMOZy9ja1kJeUUreBMutGzxKygOHm1-Wjcifz4-ik5Fbao4hPHHxARAQ0yuzmp6_9mlIEjh0_a_230IwrtFc-HK5xJhSNKsCkTU3Iki1ADuvwBFr1dsOOcwUN9kEnlv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRHJsZUU-U-ZWY2RFgx6XxDEMywiA4FAZpoz4745AvkrVbJj4qZDp-ufHdtP00oe2bOyjyUki1yCcHbxe-gcSASMOERF1W3X8ApOETb-W_hdX3ipwLby0IoeaU_cv2JkTpMccl44_DT3Ok3Al6RITK0uFsnKcomkkX7J9NKEcBdCIHE6D1VAUT5BgpXJGheR3dWX4u6UOcLZ3IKM9OkkPFEdJ5Nfiw-lCP8HtQiegJNbnEXE_cTvb6hpZ-dqpSaGS3zw80nYf2lDvARDMrdpMfot0HmofJ0Pwd3EBGxxU_g5TFYsxPfOq6tbxt4M8NHgyiClI9Y8Di8i43AMArD76g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مورد علاقه رامین رضاییان
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/81195" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81194">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQwT6G8nFKqLa-WbLiLSEjEgZ2qO6B1PEUQx7l6F0-QXM2WM7dIWeB5RILU_N-BMudd9n-vsxxqWRIDheSCwPKG_2u3PELNTF_NOZEgIz-hWN5FJlbcGosU9uO7QcdqM0bB5-ojGkgGDNKNuuAkUUMMrWkM6JoG3Azr4zeNIgkvqvFbIIX_eLYx3Q9L8DCILU7alpkph6knaxdb6i_Xmwr1Hpx1riQ4JTlPsAYngUPVLabG-_vfs4ZDhAWTlzzT9santKMsbc6AgyFZoxyTupVT2-_LBJy1AMpr5tzpp15uDlmBaYJnMOhbF0xaI478M1SFdcXzhl9By4IClcBfh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
روزنبورگ
🇳🇴
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۱۹:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
منچستر یونایتد در ۳ بازی اخیر خود مساوی نکرده است.
✅
روزنبورگ ۳ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۸ گل در هر بازی بوده است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r2
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/81194" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۰۲۱کید داداش بخدا ما بخوایم یو‌کی گوش بدیم انتخاب های خیلی فراوونی داریم، چه اصراری داری انگلیسی دریل میخونی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/81193" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8VCiAZk333r37-4L_11Sv49oSEoBic2zF6NQO3jWBwFTOPmZ5td-kQ57dqzU6JgJK-9sZboecXeGa7E5qhZeqBSNwAK9QM7bPXyntIVBYGH8ADs5lh9ybW4cshr91TGjcnm6fUXFmXMlgnHqXbSPIyCfzKF_UKHoI1PVw9KKM0TtleVbI0OtY_QqVn19hiEAdBLP-9Mb_Dp-mVHfQZBcPwHTx90mry24DHdIWg69jQrhgGjqtTVTKJLU2otX4xfp7dNt0U08fvbxEvN7N4JlV8gcFAQt6r1uDNmQ-BBLLnQXtwN4Numv3kBS74sKp_cDhj0z4Un1WiSZuSif0OEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/funhiphop/81192" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81191">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8nTBEAKUtm7cKkxvpLpdvzl4YFO4caXF-0u1bC3qrQRMXRSHZpdEaDSLOBvJZ1zYADPI3PaBBkYJqYQyeNicTjEhpa3YElPRpbRNAkfXClySPLVMfLRp2tJRf8xjfl52Hxevq74HEC_S5G1GCCFYnoujohR7rDItlGePDnylQxPJbxzcrmou3xbBEvzgD099i7p2ADSpJrh3BsB6hh-93QbDPwysLiZovgvtTYCNeJpPReOaIVGl_VBSz91mmbYFGHhzOPdA8MbkJZaYXpectw3PKUe6RWwnuNULUi0ruXpXkbGI4p_OzKevJmVG413smXeqUmbAjyljj2-9ZqRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین عکس جام جهانی 2026 از نگاه هواداران فان هیپ هاپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/81191" target="_blank">📅 17:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81190">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suqBJYGCMyBpEgwIU-DyBSn9oie7NMl0BKuBHhFuwR3lvQndVbriYtFdcmeiHLRWRzBy4R4rRpYjHI4ctaeloNy3Kt_4gpSCcrMBCO7Ggptk-i3aYVJI7nKMUntG7-ncSaD0Tlits83NBBO9L400vwsBfyWMT4rJsjmHzaVtdaGAUompajoZAwIQ1hN1Z_7YNYSZpc3kin3oCSYXtKLJsyqp2kz6UL7cYiKU0gsT6EXwonllO5Hqgx6us531azfOSWbvzKB6klzQrH-ze8hOaAV4tGRTCh3cr6mfk5XFmh-UcFZuAYzbRvfZZKIWwEfs2mR_hZny011PGRKu9OZfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/funhiphop/81190" target="_blank">📅 17:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81189">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj6-w0LeCQxtNsnTkvJeZ85rWJVp9lJhqhn2RK4L4YQFHijIv02GMoVQPR7QbHFJEw2FYGQbYurAcAsMPkP_9_PcL1EMTMrx-9o4ExWZS007x0QShrUiV-XfDCxm8XB8Qh7YySq4DXNAPWE1ozjuOfHfgI-hTCFjH7Tm2d6xUs9vhDeWEbv7bkhPTbbTA7O_iLQYsPPh9zFyvKUcb2rdCqJtb2F-F_t7MIaVY8bWOitMxnI3T5EDdf6yoU9ZqWYDOLKz1wjh4kjR9AlfisV_I2eWjC5upe6MbrNAY1RFb6H8aXM2sYK86CQb3P2w8de8AaKu7YSm1Aq1ccWbO_WDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/81189" target="_blank">📅 16:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frR6UhI0YDp4cCHCLt9vKTX0MVA_nWMIFNZZ8ReO0fvlQOudU5COgGSWHRjsY0oRlJwG5tlSy6IABp7IuO-lxgKyh4ocN4UoPKhaCc2SugM15V0Xajn0w_6p_9mNPcvWm2tJ5pMy4inJxYC8r7RQYg33-T6LMC3TpTZczRXG-BhkDIO0t-yMF0IWiuRxWW0bwdFAHEQ3ckJHn261LR8vRKO8s0cZr58ZAmVMGkzmNVDHONeNkxAXFAZWF9jRT5mmKHmoCEVFHQrIKfcwxwoQf9JYgeN7oquiTkdUkQe8Yqlrz-c7Pp5flrfir1Aoj7Il0PsxsrAPDCrCTCHmxpV2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس آمریکا تقریبا مثل قبل از شروع جنگ ۴۰ روزه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/81188" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXrMxG1XPJRDnoCRR2XYebirIBqGbI-_7NJ0FMfbkzU_UBlJmtL4aZ6aj-HH52ivIXzflQrmn-M0W7e2hyM_e0iBND_PWuMqUBNhMji6WkVVTfWLaI7MkW7Oi0LoztCu4-O56jr8x2V-FsugwKkiDelroZr7YXWRXKVIwtInSXjeb7Wc4VQqYUUdl_Y5SIX2rsh7O2xYHWpXT4LoGSdwH7He2zb79dARMxsPFtkI6axhRkBIR85-xI5Bj3WuWEus8UaSbkYlDbsmp4Cc5bMKt4KtfdJGRuB4JLt9pcRXJzSDrD7TwNV-vuHijr273K9cfZjdaD91I5VFdnXC9NL4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81187" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اختلال تنگه هرمز قیمت نوشابه رژیمی تو کشور هند و بالا برده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81186" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقایقی پیش ادامین فان هیپ هاپ از من خواستند فورا فان هیپ هاپ را ترک کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81185" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81182">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81182" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81181">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9BJQ2SyySbWmD5ZlrkBITx5rGklKsWdjghVqJNXaVDrY2S8TpDwg1px1_5hhbQlpOHyNFjqzbzYyvJ5oHQIM1GRugljsd1fIf2tFBG_TndE95m3XMq2uCYIACNUEjMGGBdUCCjrvSSBjT65ntDtvfpKJ7SJNgrs0oHteolO5jFMdN6VvjusH_WB3OmBEjuFfBFrdUdQO9KqcBB6SaVuFRt_gwDpQI0Hu1q3gFRvX86wgvmOXoei8W8YgzPFaSbE2H99hrkLTavwQn3gPr3nMKVpHbU9zxwXLrD1HpEG8qSzBTT8jnM9quglU1MGF2f1P3Z4KjB-rFR-2XUulI4PcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81181" target="_blank">📅 14:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=t22gOw2XdMk6dgzfPqlZH58p6zFshySG1n_EBqnrJ2JhYaHT28j31a3Snpd0nb9Gl97GF-zWhPtNMTFUnsKzhCwok3hhuyzqXtjGixSlZFo7c0SH9Li5bRSX4-zuxcCKA587S6YAS2Xvh5CKQsHDaqqw9ELtK0ExZTDrjvg60GR7xOYGV_MTudcHuBxgjgnsd6zY34GMusaRotq3hvBzLXHOA2tPkkOJwQ0uEwoGM42yKC0b-tMC2L74IpBb97F4-DSVx70qcT6P0satFdbbUtwjRftTaNjMsZouszZDYvP9HMHlpvZ33OSUPk1sirakfjuRW6W6VGehbOTJALK0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=t22gOw2XdMk6dgzfPqlZH58p6zFshySG1n_EBqnrJ2JhYaHT28j31a3Snpd0nb9Gl97GF-zWhPtNMTFUnsKzhCwok3hhuyzqXtjGixSlZFo7c0SH9Li5bRSX4-zuxcCKA587S6YAS2Xvh5CKQsHDaqqw9ELtK0ExZTDrjvg60GR7xOYGV_MTudcHuBxgjgnsd6zY34GMusaRotq3hvBzLXHOA2tPkkOJwQ0uEwoGM42yKC0b-tMC2L74IpBb97F4-DSVx70qcT6P0satFdbbUtwjRftTaNjMsZouszZDYvP9HMHlpvZ33OSUPk1sirakfjuRW6W6VGehbOTJALK0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان میناب در صدا و سیما.
)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81180" target="_blank">📅 13:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید گفت که ایالات متحده یک برنامه دقیق برای سرنگونی رژیم ایران دارد.
«اطلاعاتی به دست من رسیده که بسیاری از افراد از آن بی‌خبرند، و من می‌توانم با اطمینان بگویم که ایالات متحده برنامه‌ای برای شکست دادن رژیم در ایران دارد. کارشناسان بسیار متعجب خواهند شد و سپس خواهند گفت که همیشه این را می‌دانستند. به سادگی، به آنچه اتفاق می‌افتد، توجه کنید.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81179" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tomPRArODosDOxiqifRkFLTdwucoFBOFLNDJscNOwoHdC8P9SAw4MV_aZnsxCD5jcNlewXpUEUPPyjYzYxiw3IAfXKlPd5HIzWk3oRyXHI1K1PlYxQCwwGyXCzQFeqS1xIc8MZb1XAStdHnAhPA9u4mdziOzUKEBYvQ3DVbG5tsaC47-JslEGB0UtB0-NoJ0gpqxU2iHAiUj9pNIEZPharrkiuIpoyvGKqWyFlk_t-aV5iIglY5CSW1RCRR9xaTtKHiJydd8AeieMJKjInq_38xuuOKncC7azLn-ARCSaK961HxcY3Dm4eMxRmjZejmuWxfDnTpJQD8R8BVgI1qLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81177">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6aEtH8JPtsn_SBVZ3mUxYIErEiySaa7YtTjFSIW4J2EjtfvkAh_A47aOVYGYXbW2-oTyXhu8RK_z2SV43TLaJVfEypAik3d19olkNJ9heLXaYMQXZNiMOLGWZ1Usv0RA5UYNXSitVDm54h6O9QzMfgglP4QaTz0ftrJDLbC6eAqcWEQMtU-L6Pyd42E_zuRGUWfK6dOFi4Daz6e-o5pi6Z3uvoEZyeVVL3U5FIdSa3jNqWP1SAvrpYDuN24ebNr32xAXba94CxFTc3zzb-CKs9hWYK51sSdM9lXhs2H1vx4GEfkliMZOrsnnVKqcw7IEcWDSS9c9pWswJjiNVWG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
روزنبورگ
🇳🇴
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۱۹:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
منچستر یونایتد در ۳ بازی اخیر خود مساوی نکرده است.
✅
روزنبورگ ۳ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۸ گل در هر بازی بوده است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r2
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81177" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L01mCkXKIyYObbyiILUnGs4VXuB_1FfMSgPt_CLhdYZ4vHWYZSgy1j9MPVsl7snTIgMCFUfAS0sNQqsI6z1FGsntijG_aKd2hv-I2tMwUWgFm3UIFUa5Vyw7s72VsgD_RiU6jg4CS0DRloY9QU0p87kZiGHwcG4lWG0bByIND7PDr9ou4lrVGN1R6cxZCiln-s1L31wklpBhMq8rQIGOippUgFvy3Zmlb40v1FrzG0-Xq4ox2j-6_vd4dlvnlh-gd-ttGFQwrEmy63qeSO5jKKgE-auAHRvya7NAA2C7KJTNGVRI03CLm-42TPINvBVNmeXmuR5OBsnTetZiS2SwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حملات امشب آمریکا هم تموم شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81175" target="_blank">📅 05:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فیروز آباد فارس صدای انفجار شنیده شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وای
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81170" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بندرعباسم زدن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81169" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اهواز جر خورد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81168" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81167" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81166" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81165" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=vtwJENieN6GHz6jkUs2-43AzqyVro1r0FJp7MclhEItUCcXQKmbIh9cI9hJ8IoV87wSX7vno8XAnaYk0lmavUBkHdVtLAjcFr-gK5q2qP7EFar4qYZKFWu3T2TcrdwGu0GCXNPgHByaan9iasnbAPJ0ILT6qfJcyNv5tm0KvRmz2iYsxS6J5DIKhUXExWzTsLW7yctYd_W4wKpB365VCwvAqsj58yTsOvIxLuRrTG5m3P-xL-pOGru5LwyvHyJc5uJfwHloo2Dr9JBGPNm9qlfe4a5uzah2q9necFC3UNq0h1dWyWh387zKf7TgYbSWNph4nxuCxqc3WBNKDPiUlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=vtwJENieN6GHz6jkUs2-43AzqyVro1r0FJp7MclhEItUCcXQKmbIh9cI9hJ8IoV87wSX7vno8XAnaYk0lmavUBkHdVtLAjcFr-gK5q2qP7EFar4qYZKFWu3T2TcrdwGu0GCXNPgHByaan9iasnbAPJ0ILT6qfJcyNv5tm0KvRmz2iYsxS6J5DIKhUXExWzTsLW7yctYd_W4wKpB365VCwvAqsj58yTsOvIxLuRrTG5m3P-xL-pOGru5LwyvHyJc5uJfwHloo2Dr9JBGPNm9qlfe4a5uzah2q9necFC3UNq0h1dWyWh387zKf7TgYbSWNph4nxuCxqc3WBNKDPiUlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس: یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، در حال سقوط است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81164" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بمولا این یکی یعنی تعویق.
ترامپ به آکسیوس: جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81163" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ گفته ایران از این به بعد هر کشتی که تو تنگه هرمز بترکونه، خسارتشو از پولای بلوکه شده اش ورمیداریم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81162" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw4u_xOf6ct9zzBuXIGabC6bv4erVGDQl4a0n9AyEWSuKXdJyWKV9feqUNp77KDQD82wOIqs-3XKR-VxfFBmslVjDlovIENF8pif7yeEDJ3nht07FiYHiKpqX32NKr0uHLIP_mIsjZ78sGUUGwT2ABLz5U7b00KzAFCKu0FdyN6jzd2b2uDLv6OUI8-mCi6dkKQRBVd00id388yRl5vhzWYxipSXYpI__n1qWJoEfIe6Jjq9vu3-Rx5zcAIRq41AdJI1BHLSj2ly7NSfe1GhMUwNo55xWerCkGQnXe3R5kVjV2FUZo79jOuA91PLO3geloWgQFF0YVJSvtXbyNZ4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4V8NFFNLzzsjTvCSNfcL59ymU23OXrCexeLMB6q1lCHo6YloRz8BgTGYjwFL11yCVDdfAfMU_BZZiDVzOu1cmTh7VXJ63PkdeU34XO_iGwxfF_zYBxbN8JLt0Ci7vNZtwUKNw39tMefn-F2cvXU7baYAlK9hP2R6fJWyRZdilGp9YkTACXhYJp_2YGHRQVcJfaqAhLvgge_v6s0T3XHWIG6f2aoS5xabT6cp6qyC2iLA752l3GTCypSWig3XxiwPpoHA_J9mDu_RJ4diInP_DSnGRLHjbHa2aGFdHWLwO-3Khk83pOSjluIAF74LPuUq_UgnLHZ-LYdwJo2-xsH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه چند دقیقه پیش حمله کرد به کویت و مدعیه تونسته یکی از رادار های تاد رو بزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81154" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امروز تولد 33 سالگی نوید افکاری بود، تولدش تو آسمونا مبارک، روحش شاد و یادش جاویدان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: ایران میخواهد از طریق مسیر دیپلماتیک به کار ادامه دهد اما به نظرم هنوز آماده نیستند و باید بیشتر تحت فشار قرار بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81151" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یارو اومد گفت هر کشتی بزنید یه زیرساخت جنوب میزنم گوش نکردید نتیجه اش رو دارید میبینید، الانم گفته هر کشتی یه زیرساخت تهران بازم دارید کار خودتونو میکنید، وطن پرستای زیرساختی نظری ندارن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5dmSyYXFetQJux9MmsOCVdl04Znmj1vXgCwtdF-e-At-rn3aocGxKJjcsquus_HXl-TgO5Q9VrZ2xTsD65dYGl1bJ5M-NR1OjwdehqDygPOT4Z9peBMJiqZTJ6tMkcwYQNezR-0oEgBMWdAyyYo9B1nemMIBdTB9Yqpeucy9tqnHZHOzu0FxTGVw3yAhekOQlp4SqAPzvea6_8vx5-xiMarMigxKly38hAMSl9bnSkxgMHG4N-a8ErtLHrzt238mWIQSt6-uZ9TAyfy8ER50Rsiip93n_p51KBzjvR1-9GgVkFg_Vx39gAhrhqWEDq3_GrTNYGpcz19OyIRWzEKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRKOt_SkqoIpBzoWBKHgGQJMtvTML_DTqWWx6mrcxCxTgHMkYGtsxNq5o9Dg_wHgHYU7pJDB-mqbSe-B_8BQoCuzZOmote3rT4GfcKJrdvDryG-lZiImNYSIqk65gB50_rHA237AKytG83XV3qddZ4bieTPaZSAhnOtxqo67SrjzQRBRkN3--UJAjfa1f-TXRZnNednmzXmFQkqH3uVhy1DBRFi2qzf5IKLM8r3Y_--Y1sRdixZyz6DQLFWsI_w-aqGi4k8Rv2vx1px54sa1WNBODPBspCR07HkVIsm3EJIb2FTeNYg2qpRzenre1KgLxj-TkDFT4w9XeVQhxvJkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo1mj88rusKepi3pIMf4nmRpaIGJybPKj7JijcMlnasIw4cuzx7M_x8kx9WypadBRhO3nJUVnGr3k1cXaRkHI6dCprhnuwX5H_rQf2d1JuZc-Gi9UTRxN2TF-cCmCOEfc19tg20vmlFWiin9Ge2ek5rFZ6ap6lxFwjEM_5FSCn1GW94p6h_Olg6tqLy7Bh43muIP96BzlAaWesN71Ckf-6ntM08GZ9-YdZGByBbdlEdhZA2_v4FqDko6guwLyX8pOkEbwSrRi3QrW95NudKgC3-wpyvHpsIDItzDK39wDu-vnakuJTdI7RgLMVW2urFbN8cVZaWRO7I1pjF8OZPb1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG8I9TU-FjfHcQK8Pn0iLnj-9_bDucbsypFC-6vKb9CwVmtd1m1ZjEYEdFAu6ThlTwaIWHFgz2rT52dK8I0veIm4JiBZYixTv89XaMJ2qphOsAzSqTD-hyMJqisDdYfb9IXvtFl0kqPmiqeZYAN_9uyYECyA5890bk-dTldAoGWOL9-KG5xMcwDr2jLXmd479Uv7d55BAEcjiNivb8VLnDfC4xY9wOffjq5ogB3Tt_smzzSXW1QbyN1WsT7Z6csUhPjUNV7JjvCd29pn_7k_Ddm6BlQfJPuodRo1gkcRNPVC6InJDhUiNr6_jUrI2DILF2J-T8HusXMnsMVmba45Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ایسین به اسم دارک منتشر شد.
📷
YouTube
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81143" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وضعیت خزانه کشور.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81142" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDKgwXEqhN8u06-B_VfdvqoD0oeI5lWy2L2VDkf8K9qeXSgXDqIO3IA9cbAt6DQLs90O9ZbtCxqQSosoT3ZFEN8S6jyZ9esKkeSaqmLAI8c54YbS4_usg6sAq6sBFS7HZV5pNpFafrQlGfaZlyXE1y1-3Stjg7VT7C8_9O7ZCfGgE8-Hn5qoXWsuJGPUH7o3ZI5BISDELRXdw3DDbJaWer5U-DSv8RPQk4aoqE6dpMkVZeYIXVYuD8Y9Ut1ZN188HBNcwVsH8_xgwNG0VvIIhUAYjgx12QuUGf1lsRxuHwmY4yZPq9mO18ifQqe4gC3TKlY5aBYZLn2AUgK24vj9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDoVidxHHiyJaS5pumG_FS8IEPNssEh0Dcljcz5bSCMZ1vmcR6nOM3g8ZCkVJMoFVL7Z1CegQ_1TMnqoZPMvn143tXZFQEkjlh7eW2JbsTXvG2L0B1qK0cEUQ2PmttrUB8rVtubhVWvSB3emAdYLkpkXvE8VXmmv9RainnNRM-VG2mOt0Xk4jOJ_ctxAAPlKiaRz6NK0lIUPMGB7PztWgEdZ5ATL53mqjfP18pVgd04KDfXJBQXhZY3vx-_W9lgxXGvrfoVsHyPFSa27MrZxukshJ5N1MeR6Sknh0JnMzCQPrlZjgdOBjFQHbqVUl9HNqJFRU36jc1Wjggb5ccMHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید کنار بیناموسا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81140" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6LN_fnIIpKJ93Du9B4IaATmOGnAjhvgYdXQYTGq4tDwmUmVCcWfkc_FDY5yDBym6eAxswSh6nXZj2AvE76iltvMPhmL_s14jRJPM_SiOklWDuPxpW8JviXplH9L_81JD20xkyUyhv2ah0g5C0yJSGMeA1D6sOtmc8bbBSZnFhA5hrDs8xRM8YUzCa49yarvJZHsTcVfAsUIQDk_4cdJ9FFbXdgeoiVFsW1tk0DhnzeqDNTN_pXQMtDq_chNd64TIX6e39dPCic7kDvsB3aKgAlb9psgLVSQzZZf0wIZMhdFfcQX7YuZQqpWkpNNw7E_W25GqH4TOhLHPIl0uuSZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81139" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81138">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس:
ایران آخرین پیشنهاد صلح ارائه شده توسط میانجی‌ها را رد کرده است.
میانجیگران تمام تلاش خود را برای همکاری با طرفین ایرانی به کار می‌گیرند، اما ایرانی‌ها همکاری لازم را نشان نمی‌دهند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81138" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده کنست اسرائیل و عضو حزب حاکم لیکود جوری که انگار از دهنش در رفت گفت:
ما در حال نزدیک شدن به یک حمله علیه ایران هستیم، شاید حتی این آخر هفته.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81137" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسما و شرعا توافق شد آقا
ترام به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم.
حمله‌ای بزرگ‌تر از هر چیزی که قبلاً رخ داده است.
من نزدیک به اتخاذ یک تصمیم بزرگ هستم، آنها هنوز به اندازه کافی درد نکشیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81136" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRNrCMak24yWikmijiq3rhhSvBn7adJcrfYELVweddTI7h6-jkfIofo1IA-OYiXNWs2xGB4xKtaQdOGoYXstJqSrWMESbsVfHGFO_JbK3q6Vcp8nGrEhLH-pDL_ZzYfrXFbKbHh-9gro_b0yNpMAkm8-mdm13psNW38wd7Xxy2biSAP4xi5g8X42tBWZc_gpSuq7yUs_Ny5wZbeV13YEyy_6GcKNL0ZcMv2G86nTn7Y5YE5LFyFF6fh6w2aAS_64tRSSwlwI1EhMe0AzVZtWRZoHAYA063nbHaDOVz3reC9MKaptfLxlS_cBqtbQ1sTWUydFYfhYYPuKRxN-ABusaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwY7qL_uaL53Gcc-b79lJxg-prPQVzhE3Ju-IULpMDouGEC801lPUkNzdfpRA4he5uaem-sg2Zhw1drK-s3sTnjsvv8756lzT1O0VHv4VnAyhvNeuBRs0f-aM1KriIufNlnPjoDmiAO-SGAjnOMt13pzs5Ht6lAwMFiZ_mTj-dGAN5lWS1XaHVkLprR7-LGPHgXDWTngvHz2eWaxITGavFypoajOPPpeCaMEOvFG7C8PUNajudGwCn_I0D5tOk_RQPCWL7dzz6bjSFEx0C7GtJjV3Fql-qbrEnMeGTXlMYuh0SdiA6u-aPdWhxIMa_v4bzIb502Jb8-OyPnUoFxFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه صهیونیستی جروزالم پست:
موساد گفته این افراد زیر نظر وزارت اطلاعات ایران و با همکاری سپاه پاسداران انقلاب اسلامی قصد ورود به اسرائیل برای کشتن مقامات ارشد اسرائیلی و انتقام گرفتن رو داشتن که دستگیر شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81133" target="_blank">📅 18:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=qKRHXPyefsUxEUldhMU3rN11g0I4Awuihex-0DPexNydA78JELU-gcBuy6PiKKpcH60zsVCRQ4B2OuCbZ9MYocYkUuMg7m718pKuA4jI4eMa9MdjBqz6V3VhNYSM1GVUXn_hIb_fh6O2mtFgAtDQa2MUw_PPJWfVvd2auKrtH5LOdKfbh4k7d7MI0htNWvubPRSWN-bnR6SEJNzaq2TkYeunhRb6RdajQxZJws5SRvbQmw6l3icYyQegey1T5eJqq_LTt_7L7BsfnQ0DdHEjtfTJuYyj-U4_m7TQNn_aS6ICXHarvUNOumpLAc7WPK8pHiqg8dFSBCfeo7FgB9SgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=qKRHXPyefsUxEUldhMU3rN11g0I4Awuihex-0DPexNydA78JELU-gcBuy6PiKKpcH60zsVCRQ4B2OuCbZ9MYocYkUuMg7m718pKuA4jI4eMa9MdjBqz6V3VhNYSM1GVUXn_hIb_fh6O2mtFgAtDQa2MUw_PPJWfVvd2auKrtH5LOdKfbh4k7d7MI0htNWvubPRSWN-bnR6SEJNzaq2TkYeunhRb6RdajQxZJws5SRvbQmw6l3icYyQegey1T5eJqq_LTt_7L7BsfnQ0DdHEjtfTJuYyj-U4_m7TQNn_aS6ICXHarvUNOumpLAc7WPK8pHiqg8dFSBCfeo7FgB9SgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5-jntYoaFl9GQsyboUQhX6bFQg4uuuwuSNuJpf6kgCjLTUuUKLBeYwVZRYgHlw-ru0sAAbOU-5fqrCWjDPvzIdOpzO05Oqt0oq9s-ZVSAD9BOzLGdfuqSqHynjrCtT-57C8hZndWTf47_DTY0MzCqB0WyC7bcm70RXgCa-XzVO55NYJpYI3kpEhQgAUwwgkOmW0Pt4NnRl6-rqlut45sbCGXQ6SH-vo9CiaIeV6ZEVFIpyD7TQRQtzMytOInjXls0J-0KucJOkgbvmW_x5awh4MX6YUOV7_odB5ChGmQpay5vRrZy9CLvRbDk7MPz3UPiccC1RXcmZEpNVIcQ_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81131" target="_blank">📅 18:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81129" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=tJIiTrsRWl4M0yPxlxTCctnScLNwfEStNRO4GWAU2bbY7VP0DUyLxqkebaJ-jDR_9q5GCAkBnMqprMWcrN9KEBlUZxcIJm8yBuMVw-XrUlYCC4iNpTlSHiodasCp7OsnQGxc-Z-IQCKZ3rf6AzdG0IeWJ27_BR2Upe03MXSeP2UhTwBw4rhpODruWxBrQrK8jAY6HtBVhh3HgOJWtAI3-BPwpnrgCYdqptONoiR2t12dOTn_evSuGks4d6GsUhyyk72glJuyGpFPTnmq2yBvDk0rPfavPAzW2RcSy6FpxOlC9JkdOXw69qCc_IRXZVjf4SGBc0e-HE3J3E84LCH3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=tJIiTrsRWl4M0yPxlxTCctnScLNwfEStNRO4GWAU2bbY7VP0DUyLxqkebaJ-jDR_9q5GCAkBnMqprMWcrN9KEBlUZxcIJm8yBuMVw-XrUlYCC4iNpTlSHiodasCp7OsnQGxc-Z-IQCKZ3rf6AzdG0IeWJ27_BR2Upe03MXSeP2UhTwBw4rhpODruWxBrQrK8jAY6HtBVhh3HgOJWtAI3-BPwpnrgCYdqptONoiR2t12dOTn_evSuGks4d6GsUhyyk72glJuyGpFPTnmq2yBvDk0rPfavPAzW2RcSy6FpxOlC9JkdOXw69qCc_IRXZVjf4SGBc0e-HE3J3E84LCH3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81128" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=vKXTm-zzAcOGiheKNv18ptxMgcrEXzQDSOO7u7-s6fmUGr2xnMwJugL78qyRoG945T87GlcVbOO_VEQkg3_n2qtxd7VhvKbcdL-klsFyfQAiJKzU4aXgbPamlcJW4hX_SO7LieT56euvmSKxHw8kn54PK4B9mriI70M3KUZoItlTyimr0iYzajHuRXvI-4CHXwh0qhK7glm3EIqO3yVEqduUy-Z3_smskCZOtTDVGWVcTQEq_gOF5zxBV3ZF138W6ov3rwmgJksp-5dHxhU-thlrp7MVl4fIw7AwfBhsVKEeaP7GGyA9SNJv1vFe4-xtZK0Y95bAvvC1nZ0xu30s_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=vKXTm-zzAcOGiheKNv18ptxMgcrEXzQDSOO7u7-s6fmUGr2xnMwJugL78qyRoG945T87GlcVbOO_VEQkg3_n2qtxd7VhvKbcdL-klsFyfQAiJKzU4aXgbPamlcJW4hX_SO7LieT56euvmSKxHw8kn54PK4B9mriI70M3KUZoItlTyimr0iYzajHuRXvI-4CHXwh0qhK7glm3EIqO3yVEqduUy-Z3_smskCZOtTDVGWVcTQEq_gOF5zxBV3ZF138W6ov3rwmgJksp-5dHxhU-thlrp7MVl4fIw7AwfBhsVKEeaP7GGyA9SNJv1vFe4-xtZK0Y95bAvvC1nZ0xu30s_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای شهریاری
❤️
💋
💘
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81127" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81126" target="_blank">📅 16:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaUOMDBdnuxIf_gLKjP-lP8jrMuIyG8ZBEWqGkh-O8EDWQF0wFFW8RzmGcGrSVA641lGRgEOFkSfyyEGmb1fG58k5Vcjdf5fY7603hYc_icTJUOkESYx3m4464T24ZbPE2A0-OaRZQIgDHHfpbYfrI_nedYUBDr6_tN5f3IAtPrFEnrkHu8CdwnraT0M8hwYCaZkH5AV9TVwQvnbqla8UkpDTT0UmG_h2UuGxhhZetVvrZqQDm0O_u1XkJQMwAocKDbNmMdXyKI6J35g4Etn-Rffvzq56-cQRqASlZj7uV_kNdaeucgGN2E3GdKiSF72DLVTBMbjy9FWwKE0jZxLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81125" target="_blank">📅 16:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امباپه هم دستور داد کارکنان سفارت فرانسه تو تهران تخلیه بشه و کارکنانش خارج بشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81124" target="_blank">📅 15:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.  همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81123" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSlUAZrubDt2cmsUjRhxPh4N4gKpmUTJg8dy953GB7_P-17EVcb8UPD0bs0rgGPD4ZnNAUV9Xqp-R0XV6CcUmYI8EY9wVjzHjFfdWa397LI69_zksqHib8jIXxXepDLGz2BEQV-VRVu6F68jD2GSzc_HfmjdGjW0h0jzwLl0Fq8ELAxCzc4Ny6FM2LwP7Ch-3nTS9l-HwVuhxpAWthZ7Oi8FSSqF6AhfQ-6besUxCTulh2wg03krAUre-RwfKgnsaOE5i9gX2tnabWE_DS64yLyLafqW4xHLtqFhTNs9XCR0a5iKFPtaYHZ6iad6pXKRXAuzW1LwWGWGyzz8DEejuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81122" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY6cn11ONE4Z-oXEG5X-Jbc3OYSeAULGGpoqfFf3bTYk5avW5AG3ms2BUmAGBchRzpgIECwuBT_BwbGWZ_pl031MMcUuHivtxmWAnyEEP4B6vNIC6h8YVEteYmwIuKG89GfJYDO21h-rRLKmTYxi8bM4WkoffRZFPqwyVXMsPquuqAN0EUV_dr2xF6mMLId1j6hiloTG3VKFRHnn8niBNaAOMh7nfHw2EHHWmIk7YMAXUNWcyRDr_4D0WF_noNxARIeB58l0lgYELXN7Jq51Y_Uq_oRYcftgulAWdICQRX9Z3yYh_kMQUfhBk2Qd2uOhyADFqJwI0LXRO-RM0ilMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتای اینتر
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
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81121" target="_blank">📅 14:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmNgwe3FOfYTO1yfu6ADxpqr-q_V05eM-IZ_FWPD7t8L5Ukz2MTV7Th6TV4qvqhocKsrX8sJDhUk-WW0vMsyA68MN6fuM_3CHdu4JUS51Xt85jbkpmL2viyDHopV3QGgxcSyqBt99kYC-Y5ajKB0jAaS4EIQNpfHq_m1l_S7TyJar4UuagqkLHlu7BWu-wcWZgPI_TQI8gLpuwfmHzSiQiKL0mvABmLyqIh1m9uk-NgRB8Dp_oSH6hKoyrJJ73eVtW4FtpXLDE_-3dXMw0MXT8wqYmgmIRhA6IbdrpMsQ-FEWzCtHSbTQ9o7AB8OcuyxQVm_wgXYewhKEItV_FNzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv0pve7JkNemyfdqpoS2dgWYbPa23pJh5ME5Kl-d43ZwGm0XHrmdDX8PwmEhC1c-U5xA_n4d59KLPlJgI7IV7OnbxQrqW-QjjU6FHbp_HorA_jWpRbdMh8mChtzfjb2SaoEBeKKJTyKnMBbnLL1Q2bETd9bmp9CjmtHxAEnx4jqbk0jFWu5Bc_jZ0f6ULiRr0Rl9qt8vCnI7c2zvjO6fuivaJic9OnzDh3Xop8o6kU0SSgoXOj1n3aToTjLaO-r3p2c3Y2C-_Fwrx43LNGvVhbybZkdATBiTuftLIM03iCz6IHUbGmgBdGtyPVS3L6A62uP4JmeoI9wF0m-WEWacUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت دوم رئال مادرید چقد کیریه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81119" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9KRK-HpdranqVTJZZTXXJQh6dA9tl8TL9mLRkn9wt6EqxH26YW6swOy-v3FmSC9TbmTjrHKbSDtE94zYuUagMh6As3zqwKKcemBo_IsZWctY2KQIY9ABE-B74ZHyb93eKO9bZB8LXiRI9UheV9jGN0-F0os5_aM4G4ZSc9OHTRjQDN7_DJXX-Gcc1QYGoNlPSgrVGfRHKBAK3BpdpFnJAO4J7bMLGGs0GkTgd7oWG-eNIMfzZWyocudG8qE-axR4CP7VvjpUtussId8_yMZhwK_bf8Gcs8If4b_vD-jogx_xIYI9FJ7D70uydYra4T1d_rCBgOeXwmVScqYFwsNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81118" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPP19QntL2qEhxaTxcNs95kh_W-wihbQMOUp--B2KJ2Fo7O8rMAa5BS_aY-zItLZ71HCWzKaISJAkt085N0m9essuu0IDVfNnj2tg_sFohFJgPJhhMpQF6EVaGSlsfdILHbumkpgXdmQnoC3LE8f2a65F-jglWlvW4GEtMTdlkC7cT00sLfHkmcgTXdSlH8Avyy_kY_HWxesycvzZ7QAfaWVSP8OEMmcRSASt1WaOjGQ6_LX2mdWY9mYN4d4uKsfPgpG5uIIHjeH74mLOrLQ9eisYHdBsSxSX-gRp2gudpOkNsuyuGlqIQYnVeoWSePv6HJB4SrPzVDbtwKN0dsUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت ها مانند ابر میگذرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81116" target="_blank">📅 13:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKSAGto4EkkqUZEC-WxDhh_NSPjYXDhJMd2UP8QiX6D9qjjxRCpR61Sr6TuihAepIZxt2NDZPbr3NOatu6kbX481MFYb666Fb7PJrLqDuXJTSysjf4_wBkFT9Dnac0ifOinlyOx917i6PtNk6nyhR_L7v1Ct28B62s2OAxnuUfNf4lzndU007jqoHSv6BpzllIc_-PsV5Vd5Bjgvono0vVrZKaTtjB3QhA16org2OxTGEQgOv5nTGBCoiSxP9FxK85y3hUD6PuCjf9o4BgGuDBLe6ZwgwznO1anxUcxlKhkgCu8NvYYulfylIGpe98QwQPoRU7sVNVoO4lGGqrLtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN3lldZLh-oSIcIRKn1eL8gHiCSWpnFW5pkwj5-Rr2D42im5X_mS_W7QRJkCbmo5AFAad_tf7ZTFY_ajqT0xlfg316T-DIiKFjbpdh3RZj_0GUPkqpFlqlesa6CR7GeJnpTgHdAvVOe5XqEzF8xFU3ffKSG21jXjs86nHg1X1ZXdNAYyO4ICYITeUguhcmv5_car7vQwJ5LVunyHgEKTKvE4PCRVdgmHVauUmDSHAXt3HJEodJRPhiR1o99GPQiEj1vGN4U0Gtew8N9RNFVAgZ3gz9pz0lGliBY-YRcVzO_XPJmCpxPe4_GkjOHE93e8wYwlwCVshye5bICBX2IUrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک بچش به دنیا اومد، اسمشو گذاشت کندریک.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81113" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdkfsRtWUgto5iEE3Fi6Fw9aPSC1Vyk-6Am1rMHa1bKv4pUQurn0_o_0LwzpJuFObhqrCPJFiGnmG4OKjjNOatLlnOzYhFwGue2ikW9ggyltDfBr-9cN2dVBC_16rSiYKAISXg2ncLVuyj6PY_7uA28_WnNbClLnitim5Lav594TnVxUQQWuyVDsT3YR2XBT_ACw1hTSIuVKjgf03UjrNPvZhCtxZ_Q5lK1bBq4HX9_Og7B4VJyO1Rv2ONv5rn3UQDf9MD0wtPObgshbZ8GXn7ZY0VljvDC4Kw7xJRnRdXnnxWF7mt1WhPpEAUcqZLDhtmm98OxOS-jJv1Tr4nxF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا در کنار جوادسیوس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81112" target="_blank">📅 13:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81111" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TscJEyqzdnJ9LoLjyVxds0xDtjjK5d0mSCcp7izrJtnjblecOjAELKpGi6H4wOye4d_bhXNrJTaIGDoInBz5DMCJyl8NS0xM5Bsnm5dcFZ_jkovSAPB474qHrTlr9OFpwPUs79OPgwWe_VmnUvFH0XznDL-puTcPV2P6agR2QgHmOtb6Qf8Ii6CVHGVZEuncojoNLPYeQigwLSrol4r38_O_RuDc0-v_ak20c6K6kU07xqJNsqFowLY_r9-fwczMdR8qNubCOz9hAyZ5SwEjlPMO6bT1uDECg3NpTKBZzRcAbsoIHDcVjtgcnnKPg7dUP8bY4JRwsKEL0dY74B_iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81110" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrTKzY4KWCuqACDph5Cbv_2rfSk0DJAph1wSObz-FiXnYE0dfqpUHfdswgtOLbHRuXbzwgSqmDVT7vWD5ILXR6sRMPxmjGf3a812CRHgzF4lQP-O_BDOVkNjJM6DCVjQ8i01BcvxeMy79NzZTlgX8fMUg2SNFS_x4_bbVC3wcagLZFb3lELfv8oW_uINwZ-ZpDYOu7hdkfYx6HOnA_V9u2lQ3lfp1qEdal7zmE7lAxQL2PpVSQKL-v8M72T-Huq9u3kugzTSf1Ap3fostQ-qi-CCweoSgr-LC7AWTiG-dLnlO4pSUPbp8afCTQLQk9wakEZQTL8KuuV20q1RfY2Jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.
همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81109" target="_blank">📅 12:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مارکو روبیو:
عراقچی می‌گه سیاست اونها چشم دربرابر چشمه؛ درحالی که من معتقدم سیاست ترامب، سر در برابر چشمه، اونها بهای سنگینی رو پرداخت خواهد کرد.
هر شب بهشون ضربه می‌زنیم و این ضربه‌ها قراره هرشب قوی‌تر از شب قبل بشن تا جایی که ممکنه به یک درگیری گسترده منجر بشن، این اوضاع تا جایی ادامه پیدا می‌کنه که اونا عاقل بشن و بخوان معامله‌ی خوبی انجام بدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81107" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ازونجایی که فارس بیانیه ای از رادان پخش نکرده پس قطعا ترور نشده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81106" target="_blank">📅 11:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up8m3EIBmkbIXl3uB8-_CHUsLpyqal64u7RtjdKhNuUS-YarGucFu0_MNgz22Ef5DfrLJONennB0YzQoay0CeiDFQmnTykpcYImvb9nThtWQOV3wlAqdTXOZpMW1KYPDQ2ajnbt7pRl6bnRz5I4-rPIJciX0cBYfNC-slHrtogGl2AJ8hnial-oGLaD_t6Avf1tnGuSe3-iHOvdWTIOJ9b88-cQD0ma--8kfUnMHQDCwMD1NuS0uWCmEQtc0V8kksPbJtu2qh8DpjNgMDdcoFfbznWyprMcENSRoxrAsBW5BNwl-C2ipTq6DdowS3ZPUDfppzzNmM4VbShgcp84pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقم میدونستی ایران نباید هسته ای داشته باشه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81105" target="_blank">📅 10:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=HTh1BoKtAUFksERq3PYAtDStCOyZOkn6g1gsRnGqwJD2iWdHjWnfvl3sdBGBRgZiBPBpw-84u-tCESdo1B0d87Kum_DTDFsDDJ4Ta2G8-9RWuXfDLjwOMlX_jtH_SfMCdSEF3ry2meMETMzYC7TsLWXrt-2IGtOfXHg7fz3eulogGQ_IeBmX2zpIrt9GaRcAGJlq2Atfl7VRp9L4YdtL2eWW7iyOXaqI8CTz38MEAqb-m1CDjJuaOUIlsA11EkslQvUwWsoS2IjMwJ_fx-s8y0IjY8j3YRGwyjLbKKAkuudKwsNWyNvhLQt5wRuRN-rmP3VuG7UQnZQyGO-6sXw6Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=HTh1BoKtAUFksERq3PYAtDStCOyZOkn6g1gsRnGqwJD2iWdHjWnfvl3sdBGBRgZiBPBpw-84u-tCESdo1B0d87Kum_DTDFsDDJ4Ta2G8-9RWuXfDLjwOMlX_jtH_SfMCdSEF3ry2meMETMzYC7TsLWXrt-2IGtOfXHg7fz3eulogGQ_IeBmX2zpIrt9GaRcAGJlq2Atfl7VRp9L4YdtL2eWW7iyOXaqI8CTz38MEAqb-m1CDjJuaOUIlsA11EkslQvUwWsoS2IjMwJ_fx-s8y0IjY8j3YRGwyjLbKKAkuudKwsNWyNvhLQt5wRuRN-rmP3VuG7UQnZQyGO-6sXw6Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی مربوط به حمله شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81104" target="_blank">📅 04:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X94G4iz0cceOI-TgmzXEM0LhieVDhu9j0wwczuKD3JUBpYWo5ebZ_T7sK9lqTmMFexQZzl2zKx7c6DCFSmKMWbKFopnr7R_2Mn_EIFUALRklGcYiGFheeCDoXZc6jEvRYO20kIwptkpPDfiF0mulFG-SkmQqx8G0qxFMutzetJKTwpIolkkMREFTGBfjJHwx6TJZnuSJjj2CFGEEfUkLFfl2l9xv0NM-vlL3QXWVfgZzaPww5ej8XrYWZF1Pk2UJSzdpQNgMA19EF6QMXyibCBS-9caR2LClkFeOhKd31K0ifMzeyGBvA4uaQpZcBh4GxSnkltl55BBu8tfxEo8QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس امروز از رادان تو شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81103" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81102" target="_blank">📅 04:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6b0zH7fM6DcB8YPAjr9dsMjAF_luGolj_SvFLaZ-WSgLO_9rGmo2K2UCfUDtwltCL52vwJ8nHn8GzA-yYFjY0CwOsBOpPQ2sXcPClJBeOImPYEudEFYHCx3QiZZnHP1Jb-2ERNDxPURMi8mP75MJGO_dmGcUO3qJaJ8rmKUh5XWaH7NW_Pc9esObAGGygQKgRmTsoOGL7RAsJ6H9lHLxPUVSxZfn9ba5CzOFXXHEGT3zu1ee5vz8iAVJwto6125HU3gfUyaGITApSaUvHhj_Nd49IurbPEaWJ5aUxVUzFWyXA2MS7vZzd5RPBGJ9k2-FGEBmgrQ23Biyqb0KMuRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه
پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81101" target="_blank">📅 04:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیدار شید فک کنم رادانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81100" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کرمانشاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81099" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=qQVJ56NBOJKZOC9Xu6PFCY2wABtKgq3cs_wm8j8tyCv-9J7leXXy70XeWVi-_Rm5K-bLQl0_fUwYWkkwSb1g0QFVxgKlJC05FQzIT0RGRwJvuKucEQrbSljLjBKc59y2Hj9u0U5UUYDQwasf8AIOwXcDwir57r6xb19pdmeFW_6NUORSPuqHf_VX-7NR-MaXCwPvB1atLG5XNoYrlmFXctINekE7GKHUr6nzRvZHOHTxTc_ng0KSzC5Z1RMWRPWSd1zTqQ70OEkIAt5rqmOsJa-igiXtLElQsmeX0EKOwOaPgtcIuK85fuuQWuK5fSLVXOsDPYE7nQnKk68gFbm1qA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=qQVJ56NBOJKZOC9Xu6PFCY2wABtKgq3cs_wm8j8tyCv-9J7leXXy70XeWVi-_Rm5K-bLQl0_fUwYWkkwSb1g0QFVxgKlJC05FQzIT0RGRwJvuKucEQrbSljLjBKc59y2Hj9u0U5UUYDQwasf8AIOwXcDwir57r6xb19pdmeFW_6NUORSPuqHf_VX-7NR-MaXCwPvB1atLG5XNoYrlmFXctINekE7GKHUr6nzRvZHOHTxTc_ng0KSzC5Z1RMWRPWSd1zTqQ70OEkIAt5rqmOsJa-igiXtLElQsmeX0EKOwOaPgtcIuK85fuuQWuK5fSLVXOsDPYE7nQnKk68gFbm1qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردا:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81097" target="_blank">📅 02:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9SKV_v5TalEzSiwwE0ugK7LdUYg6vmwuMt6wa9sYrhViyBbqd8Q26reAS8GcFRiH-UDjTuzv5v9CC6-ARRzQzwYnPyCWUtZDAowyDqmK88WBlNzIbexR0zjwBcSeJejh0x3hnKVzXweXCr4sz6QTKM7bNrhGOTck8Gb3Oq23r7xLbWC6A85l7QLa6__0SmLvUP4lvl95bV3BYN7zqaQIlvXqXO4lIjrzQbgjk_8xk01IHjC0BJqNHcQeboTDvkHX-IIJjgRfJBfrr-OwfhE7imK2q8oN0ZPb7jj1dHiyIxpapyTplf6FaqaxMVnn9KaBeWn0ZBXg9krSL2jRUlp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه ۹۵ میلیارد دلاری تامین هزینه جنگ با ایران را تصویب کرد.
پ.ن: به گفته امریکا حنگ 40 روزه براشون تقریبا 38 میلیارد دلار هزینه داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81096" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سیریک
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81095" target="_blank">📅 01:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پرواز جنگنده های نسل 66 کوثر بالا سر تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81094" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctQ-aZYAm5SjCB57p9efD0u1Gt7uLpEKhdhidOWw94qzgj9KHmfg9Ow7CKqet78FD1Rm6BMAPdVO3A6ANYkzSQVm-utCaG-RDrZQAi1qiNZxV6H5IyXnyhv6PBy8RcBKcrzUl4s-ozs2YykhJLo7Wi6L61f9VDYG8exzzzwzVOYcfJ2afj1mvkY-glicMfqI0dnPqYT6w5CCeSxUUf0hBqJvlP9ZF8J9BWRHzoS2Qva6jdCGSRKI72uj4j0_hpLcC7AqLSxwc_iWmj0bCFRrlkF7gxnl1hTqHm4EmZB4xI65xt2-Lvbqplo7RRk5ZExPFlsljQCg7g7FYPXnYhEFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق مقررات جدید چین، استفاده از برنامه های هوش مصنوعی عاشقانه برای افراد زیر سن قانونی ممنوع اعلام شد
دلیل نگرانی سیاستمدارن چینی این بود که شاید افراد وابسته‌ی ربات شوند و تمایل به ازدواج رو از دست بدند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81093" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81092" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار در ماهشهر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81091" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81090" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81089" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کان نیوز:
ایالات متحده به اسرائیل اطلاع داده است که قصد دارد در روزهای آینده حملات خود را تشدید کند، از جمله اینکه برای اولین بار در این عملیات، از بمب‌افکن‌های سنگین استفاده خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81088" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81087" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj0LRvBQlwT0VtPr5iZSFJiqsW88dU1W7Qz8QZSIF1IhJHiDAc8mt8RO_fglFndTRTuC84o02mA1Ye3RDKJRU-TErcOhXPWMXTmtuuPxgV7XHCSexT_X5Fcr4ukjxV4pJr1f6qElvvduSpOE_CjC-kQx-CMiMrJDnX-5JMvfHKxmlH9JVArn_0D5FddSW-d7EvbHy5N34ZWKwttBKb4De3JY19a7g7Ud_xwHOSkXxvlV8fPCJvJ74veseuxG5wmGWTMg9boy7eK8uQi75QXpROnGhwu3tSwe1W9Rnhr0qvugn4j8Q2mIDRvLbg2AZKoWo54fy57RINI2rt_e9VQlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81086" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eByWR2uBr7Hk6tFJ1P1IlNJjiILTrNnxSUA8VtuAK-R0_gEmgpygBRu4kgMfEqlW3FoYoFFuE3uoS4YEw3u2ouERM8tIxNAq1URf3Yk1Yb1AMrBN3ESsIWWUFgWOuaKTMJD2PCifLDEAEg3VyFAYAa-qGR3vEIvKTqHzLnXYyTg63OTT9weI25Psoc9dvAZv2o6G39I5m_hZFY_6LwZ13o1EYqqgujIGfZKFUoOUvMl_mF3UliDLOdZoGgFKHMpwrzKd8M3fXJPaQYqnc4CmQ7AbvRYhaeS4cAfBgW4DeaujNazwcZZ57TBqQaWkp2MHfMaDyBYHWL81BXhjZlIxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار جان پس اون پلا و نیروگاه‌هایی که کودک‌کشان تا الان زدن چی؟
اونا جزء تست رایگان ۷ روزه حساب می‌شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81084" target="_blank">📅 22:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS6y5J0BFVrnvEO2RKj4CxarpMka9MWCqm6vwDhvy0ucARF4cdIBJhyFOR1q7Pj9iya3QqAHzVQms_G7_n6uguXB1jy_mDSqvNHH82A0UoAtoysM9KTMnMIU_7OkAycVJ3syoaU9ODVC1jQ_Za4kLgFW4u5GPTsK0SGlF5672L7MHd91vf2DYhBZrcPIIEusZWn0wKsiMwclQyrP3n7rtMNQ8UHNDJNwt0U-q3p0zE-j4rrXMgIcnsAdX3s46jcVV0ZEzy3LnSFQ8x-RAf_LBEHDGq2jz5WHt7jgRGSv-GXDx5n-fooncmWLKtJHAlSpuxCNEPf67fkJgfP4imdBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نخوابید خیر نیست مثل اینکه
انگلیس سفارتشو تو ایران بست و کارکناش رو هم کامل از ایران خارج کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81083" target="_blank">📅 22:40 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
