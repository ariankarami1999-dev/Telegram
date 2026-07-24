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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 22:23:15</div>
<hr>

<div class="tg-post" id="msg-81204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=lWLiia7Yfag-pFHTSvEXgNWpqlB8moWWgVY0e8Gglq34uCWLA9EmOsm5kjl9oboxgYj_PzqsSdIF2appmBVBWhWzJqIRNaXmEFsBeL6JkWP6Sh1jirpfZvM2I6fP54w6W3kLglIJIJDdeG7lIQHoXeLWFZDrdxE2ovkP_xtyKL3XbIftCMEx9o-JVxWVRU4dEjJndWzFIRfLr8dvuNYEbeM0cgOlnBV6Whrn-AfQXQnak2WZwmmV7nToilZkMpxx6gO7Ekc9nkhTAXPXYv8ligsN0nVVx9HAwU29aUjMWWOg4UMVV0gzQG4OZWzVG5yYmC_pyADfi58gV12pV4Sabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=lWLiia7Yfag-pFHTSvEXgNWpqlB8moWWgVY0e8Gglq34uCWLA9EmOsm5kjl9oboxgYj_PzqsSdIF2appmBVBWhWzJqIRNaXmEFsBeL6JkWP6Sh1jirpfZvM2I6fP54w6W3kLglIJIJDdeG7lIQHoXeLWFZDrdxE2ovkP_xtyKL3XbIftCMEx9o-JVxWVRU4dEjJndWzFIRfLr8dvuNYEbeM0cgOlnBV6Whrn-AfQXQnak2WZwmmV7nToilZkMpxx6gO7Ekc9nkhTAXPXYv8ligsN0nVVx9HAwU29aUjMWWOg4UMVV0gzQG4OZWzVG5yYmC_pyADfi58gV12pV4Sabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین صحبت های مرحوم در مورد وضعیت مملکت هم ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/81204" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=sER7dlJF2HMAiRCGV-VsAM0pLrh1FU56bPEIIO0-uW0K-pr_ULZETfIUFeUDvqcqs52ouPRzam6UJQEstfcnJiLTr3Rv6m14GBYKKme-uoC3qCllyoD5WTSW-TdmK34KWtKXP1Ka42aFo6xK9aadB7x5Wb4VdSR0l4vNiiybnCuvu-3z6_JMtsk6R7Cih5CGfbpVy6cJKMCAZOe02P4NJOgYr0_gZVRDGCGr2EsKl9ngktrh8z_qEu5pL2rmSkPISHMSRPBx_13lCKm1mf10OVxhS35f6zszW_r6vdEG1zQrAA9j3zLa2MPtz6gr4DgasDRkffd7n-0jc6t5MVPYfaF5zOAzZLskq6YMfAnJsAWtzv9Le3Pnos9nEl4x0EPmDfJdZDPfk8zs4_IKN-WAbSeKxKChRHqqNHKWc9DSqVXcbQ-4PP8_IlREpOoTQf5rwQgqyhJSqG_goVRNXM2-vGwJa9FKVdt1vCQ08SstyCeoc0fbp8Kwr1R98TP0k5YfXqUEV5bSAl6uQyX4i_l_QbTAuKOyIDCtKLqLJDh8txZf1J7svRv8cGpX2PW7_n4GzyOfu5R70PwPvIM0lJLtpbsAE4xMQgyzTxeVfe6fKvF3312pXCRIE9ClezW0MHurwmrk1R5GAw-tAK6J5zWAF-8jjLjzV1mFevewTiKbD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=sER7dlJF2HMAiRCGV-VsAM0pLrh1FU56bPEIIO0-uW0K-pr_ULZETfIUFeUDvqcqs52ouPRzam6UJQEstfcnJiLTr3Rv6m14GBYKKme-uoC3qCllyoD5WTSW-TdmK34KWtKXP1Ka42aFo6xK9aadB7x5Wb4VdSR0l4vNiiybnCuvu-3z6_JMtsk6R7Cih5CGfbpVy6cJKMCAZOe02P4NJOgYr0_gZVRDGCGr2EsKl9ngktrh8z_qEu5pL2rmSkPISHMSRPBx_13lCKm1mf10OVxhS35f6zszW_r6vdEG1zQrAA9j3zLa2MPtz6gr4DgasDRkffd7n-0jc6t5MVPYfaF5zOAzZLskq6YMfAnJsAWtzv9Le3Pnos9nEl4x0EPmDfJdZDPfk8zs4_IKN-WAbSeKxKChRHqqNHKWc9DSqVXcbQ-4PP8_IlREpOoTQf5rwQgqyhJSqG_goVRNXM2-vGwJa9FKVdt1vCQ08SstyCeoc0fbp8Kwr1R98TP0k5YfXqUEV5bSAl6uQyX4i_l_QbTAuKOyIDCtKLqLJDh8txZf1J7svRv8cGpX2PW7_n4GzyOfu5R70PwPvIM0lJLtpbsAE4xMQgyzTxeVfe6fKvF3312pXCRIE9ClezW0MHurwmrk1R5GAw-tAK6J5zWAF-8jjLjzV1mFevewTiKbD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنده خدا حتی وقتی اعصابش خورد بود هم ملت رو میخندوند
روحش شاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/81203" target="_blank">📅 21:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اکبر عبدی درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/81202" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ2lLJT-FVRE7bcczoiDjoiOcmjraPhs2NhjT-TU_gELy1cff4EmB9-tC6C2qZHCdFc0JtljBqgMfi4_mTQDE1uWhKVuMYECqIAkQE6PEDHvzjzcYYjyVVxe2KiJ5ElSFQa0WQc_-B9qWH8P6X_qGMN9wd7V5cb5S1c8t1tdnoaJ4BYjiP3sCCD_nVVRuWIwr5jk2iaEe06995d-Qdg59sEGpVTK1iUu5DCxN4XEDW5MDRtWyG62gPLi-geDV6Nm7Ldhm6n0nmZwPB1VB_Ww5BMlqbko5mJsBLmGGBT9pZZi6fYh1y6KbZp6CJgvaa6OTayfBb7gqR6Kh8bhSHEjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم این چه سمیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/funhiphop/81201" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تنگه رو مفت بدیم بررررره؟
مال ننته بدیم بررررره؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/81200" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoJ6uqUQ74p7h9IhOxbrrZQssSb1KvaCylcnRBlPNUeYKK_zw_p0Koht79wgrbbye6sGE_-RYAbti8A5KwmFMuwD4Jmey6AIhIoucwHwHQBffMN2dem5vhI-Q_TwzqjSXlp9rc3m6DuBE4l6mR8-J9v3pL9pssyundpZCo7PFg_ZwNL_yY0D9qPYHhh6y2Ago4twJUe4fAxI3lgsm3r5-saoWqkK0GxCirsEqyIwYIYwjsyGPIJOUXvTHyHiRdpaFfueczK_7SqBRSXlkupNPCYHdthQ2nF0XGc2BPbOszjKT8nR-4FcOPIrUDqQ38kOOh5ssqgE9cn1fhOejol0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این مقایسه ها که خیلی دوست دارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81199" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromِ</strong></div>
<div class="tg-text">تخم داری تو یوتیوب مقایسه کن</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81198" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEoieOia8Hl3Kk4hHakC-qL0nDz-zGNFxJAUWMIRkhrZNrvUJUUWN4uGWicNvORe7hCYz90gKy3fYQiJJI9IhDHGBBf4PxaaNvtwOooLvAh7NN7vVilfEvEKoicRmSLZpimp4uAhXLhe8zHCiJMRSS-4rrChlfp7YoO5RiX2U9De_Y6zOYUBIkbqmMnlNqROD_-dZw_mRLVDIv9MVZAtfeRdBg-tt4W-fVgKDVk_fcX3UYjmR_lgRmJIeXPtxxJNlB6wGFHj3Tbg4CkhEvgtfM2N_8GtYVrMbAYMfWra8Z2xCao9-s0qvhBoa4nlPo9ADb1P_O4YyLHZemTjrFXXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از مقایسه رونالدو و مسی توی جام‌جهانی که خیلی درخواست کرده بودید.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81197" target="_blank">📅 18:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGdKFh1TdIbr9XosifJ5WLH4146CeqhzRF25wkr8UHhfYRIInSoBKQA4XX1ArosdjG1yrnDkYfCyZQcQ1nzJmr1Nd3D_eBaNNSG1pSBWdw9qrZkAIMOpu63BgnmD0k_JVMumsbdOEx2ZEbaKOaE4S7LsipMD-g5YY42OuF8EtSdi6_WOzjQzQ84xQuEf45gGH1b_MIYI6dN4uYN9QkGMcwMOZy9ja1kJeUUreBMutGzxKygOHm1-Wjcifz4-ik5Fbao4hPHHxARAQ0yuzmp6_9mlIEjh0_a_230IwrtFc-HK5xJhSNKsCkTU3Iki1ADuvwBFr1dsOOcwUN9kEnlv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRHJsZUU-U-ZWY2RFgx6XxDEMywiA4FAZpoz4745AvkrVbJj4qZDp-ufHdtP00oe2bOyjyUki1yCcHbxe-gcSASMOERF1W3X8ApOETb-W_hdX3ipwLby0IoeaU_cv2JkTpMccl44_DT3Ok3Al6RITK0uFsnKcomkkX7J9NKEcBdCIHE6D1VAUT5BgpXJGheR3dWX4u6UOcLZ3IKM9OkkPFEdJ5Nfiw-lCP8HtQiegJNbnEXE_cTvb6hpZ-dqpSaGS3zw80nYf2lDvARDMrdpMfot0HmofJ0Pwd3EBGxxU_g5TFYsxPfOq6tbxt4M8NHgyiClI9Y8Di8i43AMArD76g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مورد علاقه رامین رضاییان
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81195" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81194">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81194" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۰۲۱کید داداش بخدا ما بخوایم یو‌کی گوش بدیم انتخاب های خیلی فراوونی داریم، چه اصراری داری انگلیسی دریل میخونی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81193" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8VCiAZk333r37-4L_11Sv49oSEoBic2zF6NQO3jWBwFTOPmZ5td-kQ57dqzU6JgJK-9sZboecXeGa7E5qhZeqBSNwAK9QM7bPXyntIVBYGH8ADs5lh9ybW4cshr91TGjcnm6fUXFmXMlgnHqXbSPIyCfzKF_UKHoI1PVw9KKM0TtleVbI0OtY_QqVn19hiEAdBLP-9Mb_Dp-mVHfQZBcPwHTx90mry24DHdIWg69jQrhgGjqtTVTKJLU2otX4xfp7dNt0U08fvbxEvN7N4JlV8gcFAQt6r1uDNmQ-BBLLnQXtwN4Numv3kBS74sKp_cDhj0z4Un1WiSZuSif0OEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81192" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8nTBEAKUtm7cKkxvpLpdvzl4YFO4caXF-0u1bC3qrQRMXRSHZpdEaDSLOBvJZ1zYADPI3PaBBkYJqYQyeNicTjEhpa3YElPRpbRNAkfXClySPLVMfLRp2tJRf8xjfl52Hxevq74HEC_S5G1GCCFYnoujohR7rDItlGePDnylQxPJbxzcrmou3xbBEvzgD099i7p2ADSpJrh3BsB6hh-93QbDPwysLiZovgvtTYCNeJpPReOaIVGl_VBSz91mmbYFGHhzOPdA8MbkJZaYXpectw3PKUe6RWwnuNULUi0ruXpXkbGI4p_OzKevJmVG413smXeqUmbAjyljj2-9ZqRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین عکس جام جهانی 2026 از نگاه هواداران فان هیپ هاپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81191" target="_blank">📅 17:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suqBJYGCMyBpEgwIU-DyBSn9oie7NMl0BKuBHhFuwR3lvQndVbriYtFdcmeiHLRWRzBy4R4rRpYjHI4ctaeloNy3Kt_4gpSCcrMBCO7Ggptk-i3aYVJI7nKMUntG7-ncSaD0Tlits83NBBO9L400vwsBfyWMT4rJsjmHzaVtdaGAUompajoZAwIQ1hN1Z_7YNYSZpc3kin3oCSYXtKLJsyqp2kz6UL7cYiKU0gsT6EXwonllO5Hqgx6us531azfOSWbvzKB6klzQrH-ze8hOaAV4tGRTCh3cr6mfk5XFmh-UcFZuAYzbRvfZZKIWwEfs2mR_hZny011PGRKu9OZfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81190" target="_blank">📅 17:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj6-w0LeCQxtNsnTkvJeZ85rWJVp9lJhqhn2RK4L4YQFHijIv02GMoVQPR7QbHFJEw2FYGQbYurAcAsMPkP_9_PcL1EMTMrx-9o4ExWZS007x0QShrUiV-XfDCxm8XB8Qh7YySq4DXNAPWE1ozjuOfHfgI-hTCFjH7Tm2d6xUs9vhDeWEbv7bkhPTbbTA7O_iLQYsPPh9zFyvKUcb2rdCqJtb2F-F_t7MIaVY8bWOitMxnI3T5EDdf6yoU9ZqWYDOLKz1wjh4kjR9AlfisV_I2eWjC5upe6MbrNAY1RFb6H8aXM2sYK86CQb3P2w8de8AaKu7YSm1Aq1ccWbO_WDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81189" target="_blank">📅 16:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frR6UhI0YDp4cCHCLt9vKTX0MVA_nWMIFNZZ8ReO0fvlQOudU5COgGSWHRjsY0oRlJwG5tlSy6IABp7IuO-lxgKyh4ocN4UoPKhaCc2SugM15V0Xajn0w_6p_9mNPcvWm2tJ5pMy4inJxYC8r7RQYg33-T6LMC3TpTZczRXG-BhkDIO0t-yMF0IWiuRxWW0bwdFAHEQ3ckJHn261LR8vRKO8s0cZr58ZAmVMGkzmNVDHONeNkxAXFAZWF9jRT5mmKHmoCEVFHQrIKfcwxwoQf9JYgeN7oquiTkdUkQe8Yqlrz-c7Pp5flrfir1Aoj7Il0PsxsrAPDCrCTCHmxpV2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس آمریکا تقریبا مثل قبل از شروع جنگ ۴۰ روزه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81188" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXrMxG1XPJRDnoCRR2XYebirIBqGbI-_7NJ0FMfbkzU_UBlJmtL4aZ6aj-HH52ivIXzflQrmn-M0W7e2hyM_e0iBND_PWuMqUBNhMji6WkVVTfWLaI7MkW7Oi0LoztCu4-O56jr8x2V-FsugwKkiDelroZr7YXWRXKVIwtInSXjeb7Wc4VQqYUUdl_Y5SIX2rsh7O2xYHWpXT4LoGSdwH7He2zb79dARMxsPFtkI6axhRkBIR85-xI5Bj3WuWEus8UaSbkYlDbsmp4Cc5bMKt4KtfdJGRuB4JLt9pcRXJzSDrD7TwNV-vuHijr273K9cfZjdaD91I5VFdnXC9NL4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81187" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اختلال تنگه هرمز قیمت نوشابه رژیمی تو کشور هند و بالا برده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81186" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دقایقی پیش ادامین فان هیپ هاپ از من خواستند فورا فان هیپ هاپ را ترک کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81185" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81182" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9BJQ2SyySbWmD5ZlrkBITx5rGklKsWdjghVqJNXaVDrY2S8TpDwg1px1_5hhbQlpOHyNFjqzbzYyvJ5oHQIM1GRugljsd1fIf2tFBG_TndE95m3XMq2uCYIACNUEjMGGBdUCCjrvSSBjT65ntDtvfpKJ7SJNgrs0oHteolO5jFMdN6VvjusH_WB3OmBEjuFfBFrdUdQO9KqcBB6SaVuFRt_gwDpQI0Hu1q3gFRvX86wgvmOXoei8W8YgzPFaSbE2H99hrkLTavwQn3gPr3nMKVpHbU9zxwXLrD1HpEG8qSzBTT8jnM9quglU1MGF2f1P3Z4KjB-rFR-2XUulI4PcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81181" target="_blank">📅 14:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81180" target="_blank">📅 13:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید گفت که ایالات متحده یک برنامه دقیق برای سرنگونی رژیم ایران دارد.
«اطلاعاتی به دست من رسیده که بسیاری از افراد از آن بی‌خبرند، و من می‌توانم با اطمینان بگویم که ایالات متحده برنامه‌ای برای شکست دادن رژیم در ایران دارد. کارشناسان بسیار متعجب خواهند شد و سپس خواهند گفت که همیشه این را می‌دانستند. به سادگی، به آنچه اتفاق می‌افتد، توجه کنید.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81179" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tomPRArODosDOxiqifRkFLTdwucoFBOFLNDJscNOwoHdC8P9SAw4MV_aZnsxCD5jcNlewXpUEUPPyjYzYxiw3IAfXKlPd5HIzWk3oRyXHI1K1PlYxQCwwGyXCzQFeqS1xIc8MZb1XAStdHnAhPA9u4mdziOzUKEBYvQ3DVbG5tsaC47-JslEGB0UtB0-NoJ0gpqxU2iHAiUj9pNIEZPharrkiuIpoyvGKqWyFlk_t-aV5iIglY5CSW1RCRR9xaTtKHiJydd8AeieMJKjInq_38xuuOKncC7azLn-ARCSaK961HxcY3Dm4eMxRmjZejmuWxfDnTpJQD8R8BVgI1qLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81177">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81177" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L01mCkXKIyYObbyiILUnGs4VXuB_1FfMSgPt_CLhdYZ4vHWYZSgy1j9MPVsl7snTIgMCFUfAS0sNQqsI6z1FGsntijG_aKd2hv-I2tMwUWgFm3UIFUa5Vyw7s72VsgD_RiU6jg4CS0DRloY9QU0p87kZiGHwcG4lWG0bByIND7PDr9ou4lrVGN1R6cxZCiln-s1L31wklpBhMq8rQIGOippUgFvy3Zmlb40v1FrzG0-Xq4ox2j-6_vd4dlvnlh-gd-ttGFQwrEmy63qeSO5jKKgE-auAHRvya7NAA2C7KJTNGVRI03CLm-42TPINvBVNmeXmuR5OBsnTetZiS2SwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حملات امشب آمریکا هم تموم شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81175" target="_blank">📅 05:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فیروز آباد فارس صدای انفجار شنیده شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وای
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81170" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بندرعباسم زدن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81169" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اهواز جر خورد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81168" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81167" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81166" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81165" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81164" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بمولا این یکی یعنی تعویق.
ترامپ به آکسیوس: جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81163" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ گفته ایران از این به بعد هر کشتی که تو تنگه هرمز بترکونه، خسارتشو از پولای بلوکه شده اش ورمیداریم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81162" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw4u_xOf6ct9zzBuXIGabC6bv4erVGDQl4a0n9AyEWSuKXdJyWKV9feqUNp77KDQD82wOIqs-3XKR-VxfFBmslVjDlovIENF8pif7yeEDJ3nht07FiYHiKpqX32NKr0uHLIP_mIsjZ78sGUUGwT2ABLz5U7b00KzAFCKu0FdyN6jzd2b2uDLv6OUI8-mCi6dkKQRBVd00id388yRl5vhzWYxipSXYpI__n1qWJoEfIe6Jjq9vu3-Rx5zcAIRq41AdJI1BHLSj2ly7NSfe1GhMUwNo55xWerCkGQnXe3R5kVjV2FUZo79jOuA91PLO3geloWgQFF0YVJSvtXbyNZ4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4V8NFFNLzzsjTvCSNfcL59ymU23OXrCexeLMB6q1lCHo6YloRz8BgTGYjwFL11yCVDdfAfMU_BZZiDVzOu1cmTh7VXJ63PkdeU34XO_iGwxfF_zYBxbN8JLt0Ci7vNZtwUKNw39tMefn-F2cvXU7baYAlK9hP2R6fJWyRZdilGp9YkTACXhYJp_2YGHRQVcJfaqAhLvgge_v6s0T3XHWIG6f2aoS5xabT6cp6qyC2iLA752l3GTCypSWig3XxiwPpoHA_J9mDu_RJ4diInP_DSnGRLHjbHa2aGFdHWLwO-3Khk83pOSjluIAF74LPuUq_UgnLHZ-LYdwJo2-xsH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سپاه چند دقیقه پیش حمله کرد به کویت و مدعیه تونسته یکی از رادار های تاد رو بزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81154" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز تولد 33 سالگی نوید افکاری بود، تولدش تو آسمونا مبارک، روحش شاد و یادش جاویدان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: ایران میخواهد از طریق مسیر دیپلماتیک به کار ادامه دهد اما به نظرم هنوز آماده نیستند و باید بیشتر تحت فشار قرار بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81151" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یارو اومد گفت هر کشتی بزنید یه زیرساخت جنوب میزنم گوش نکردید نتیجه اش رو دارید میبینید، الانم گفته هر کشتی یه زیرساخت تهران بازم دارید کار خودتونو میکنید، وطن پرستای زیرساختی نظری ندارن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivMx_3bg3a07ehLZegX5sYWCnNaFj7yNhGrT0zGs2dh7-lVjw53hz3qFvsEoTtJxZn28K5JvpATQeA3p0ubKDNdr4nMXmjNvr_ppWzhv9VgBYly3yD69rbT6Ahh3Xj9pdeJKNlWlJ4V529qZ3MkENM2Nbv-JrX1a_Wk3kngdvidW09pIxhkLM99BFlFe4EEYTgKyvw0J2dlbyL3qYWuUzCym9_j0TyKcPTUlHTrfBC9ylV6ZIZhIrbTJJdr-_dXiFFA9Hw1ibzrnmbQ4BA44PjvQ0RwfEZfCS60se1-X4HnAPJsmxSAxj8R7nnrlOLlEWoOBfTo_kXvU568dwe7G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrLWxnhzLk45ArIPWDLWs02BC7G3k4SSCujVyzrIlebV8a2RrByfVeE2SMkMZ5FlqYl35GZv-40Zu6E1w0i8uUwQcL3MogJw9L9CJIebKOmTKtKzSMndcKb35K-xrt1Oxc9gelYsu8Do0VS1FUkpUynIGdnA_saEAbgze9529871T8_BPvf5aEnJqMc15TEQPeiLkQC7ThSJslIlbDwCPo3X7EwRJbcdGtAFIOY7JFsqsOQL5O_aSfA0VbwOCo7IsBQxxg48q4Hxc0WXKltc4b3vqki6Dokg7NlLNsNmcYsiioUZD5yAZ4rG9CDn-ImWPJikugx-ODk--LHX4wOULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVLCPkK0-X8DkVJeTvdvae678L1x8XMNH1zAL8j0WJMV04KxtjRf_X8p8J1B6BC1jPXJD0DPT8O1lzZA057SpDVgiX6clVSXuzakiqQv99udKUF5aGFMLtWbmuCs_mVruHjZIiSD0AB3vEJTr5ifB95jEue4sUtfyhvVBNVQ4ID55XAlwJXiD9yu2dwXjHpwzQL5356dpsA_65hOyrZ1jTc1qkzSzEUCWsgeARgQn-Ph4h2ocGPj_MusUACLR_j9fHIvokUjr6M3hl87OJiR3CsVhMh7TeBxyNHiWfkfyVjJjE687KCcp5iRBYVRW-XYHX9u4Z8oOT5I-OqqrU_pBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVRm8wj9CpfggdgkPiQG7B_MmSg-ZtKFsCDUpv-2rJheT2NjqleyfO5ptEzxkXoZBMidtjESJ86Xi1fRRNcqLXRuLsa0AV_JGncitkPdG3UsG2tP_q_9L0XzabEAfJyQZRPDVskbTF6hBRWAnRhxSj_35y1F04KostzOgqaFkEVDoIAW1evwBvjGhndU7AEXSrWF7SIISthXKPmlir624kWKccv60e96SeHvdytvXLDeLmeP2hB5oN8SBOGEn6THyvWYJMLsQ7OOpsVyh7dMAg2iqZnElAFIEoxpNdsTocmSA3v8Amtw5r-rzHW3UQduH4gWK4BERwIQ9_9NujUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ایسین به اسم دارک منتشر شد.
📷
YouTube
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81143" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وضعیت خزانه کشور.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81142" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix6JR9DEpKAdnxyKKL5L_psq_uXIt7LhGcv_UZ4jZSwEWK62aLMr3O9JQzR0mUbCY-kLDMPKQuI-iyozVPothdPcbM72JUJq3Xs8duzS6rZuZt53IB8JlsdmQJavRw103nquvm6ceA_M-EgHQCVHxLON8P2mwZcgACOPNcSo_ECZT2vze0X70jHunUYzMjClepHYtu0Ynu_zTQEdY0CBf5JETTJCmlU1AMmNsAzXVPmleffsR1NTPhNUXBOuHKv96BI18pE9cRWS9XBchWktMIDWC50AzHq-hLw2_kaasVx4CsQylowzKl2ZJlGz6W_2lBWJEzMZYctzAQS1W9LxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfamumvYmzD_Uk6Cpr03bqXY7Z3t_QrClUvIc04YraKZWz9L6oswUIHJ_59ckPJs0C3bib7g46ciSyOrSr8ZhOv0Xmqr1yHEglEoJWPx1CbObX2te1Nn0uwk7s3s5wkVLY0Z0a1FhRQFsET12Ja6m_ZIOhOuT3IWDtRID08xSO7boEzNtu19Qqi1CMOJbkIQDIq3rJLMXnUAZ-nBk_ZSherzZ4gMmTV6LkW_WfBCvNVyh5gLmsXJmO0NKGfkV4XCHmlL7cRAzbwNz7O58V_9jpkdcuZISYA3Kcp7qw74jt-QtLzpdFOPu0F7e0pUWzj1fMZTSOKAIDqa0T40y8xHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید کنار بیناموسا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81140" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvraLam_0kGkAbnOvvlru1wuR2HShIfwJzg30wXPXW5LtkI5wfKR24wpcGL3zneMKPgCIBLYI9hK9xOAB9fGY-bVFEgbHfNMvw_cuAGBD_7tKvOwZwi70DUBopXVbERGSC3WRDf8PhDUisj2Bgk5zuECArrIWeq9GfPpeqLTJ4jBJTmIV8Jqjs-p86sK1_yxc-6moLxXu0sHWD1L10_7ZZnaMQhHVoQBuXx--coKh40hxv6agXidrWgzGSAPzThdGspL-ucW2dVq8MymTJKvHttjaMEvdc5leL5QSED7GNhjXtltacIzm61dN5fBxvyZJCHVzzw7T_SX4WSNcTY7Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81139" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آکسیوس:
ایران آخرین پیشنهاد صلح ارائه شده توسط میانجی‌ها را رد کرده است.
میانجیگران تمام تلاش خود را برای همکاری با طرفین ایرانی به کار می‌گیرند، اما ایرانی‌ها همکاری لازم را نشان نمی‌دهند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81138" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=bNnUMWxEF-IYqeC3i06RWVH1haA8G4PCK-oOgm4QaSYg4TFBq5zOIo510l_9o5OYg_yJYNTZpt5quA94TElFTBwtLplCbREImHH8Lra2YZIQpqc6rNn6HWohe29Nxy83qjypYE2fWS0qen6oNjdUO4119gTlKk5vmgNZcaUk_4S0TcDM6GjLLqXQSYkLcOIf5niA6RhghJ6rZqqNOaFxD-1slbFk2DpNRQnJ8cMNEMB4tLVbbVXuaHeAW616TuUFxBkwuxXFM5FXBazo8dbaWxzBnvNdVapFobLIJzsQD6uA1T-stz_Ds6mpBCOVzqOpGvZCwMyU4h2sNOYGFa-VCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=bNnUMWxEF-IYqeC3i06RWVH1haA8G4PCK-oOgm4QaSYg4TFBq5zOIo510l_9o5OYg_yJYNTZpt5quA94TElFTBwtLplCbREImHH8Lra2YZIQpqc6rNn6HWohe29Nxy83qjypYE2fWS0qen6oNjdUO4119gTlKk5vmgNZcaUk_4S0TcDM6GjLLqXQSYkLcOIf5niA6RhghJ6rZqqNOaFxD-1slbFk2DpNRQnJ8cMNEMB4tLVbbVXuaHeAW616TuUFxBkwuxXFM5FXBazo8dbaWxzBnvNdVapFobLIJzsQD6uA1T-stz_Ds6mpBCOVzqOpGvZCwMyU4h2sNOYGFa-VCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده کنست اسرائیل و عضو حزب حاکم لیکود جوری که انگار از دهنش در رفت گفت:
ما در حال نزدیک شدن به یک حمله علیه ایران هستیم، شاید حتی این آخر هفته.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81137" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسما و شرعا توافق شد آقا
ترام به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم.
حمله‌ای بزرگ‌تر از هر چیزی که قبلاً رخ داده است.
من نزدیک به اتخاذ یک تصمیم بزرگ هستم، آنها هنوز به اندازه کافی درد نکشیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81136" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRNrCMak24yWikmijiq3rhhSvBn7adJcrfYELVweddTI7h6-jkfIofo1IA-OYiXNWs2xGB4xKtaQdOGoYXstJqSrWMESbsVfHGFO_JbK3q6Vcp8nGrEhLH-pDL_ZzYfrXFbKbHh-9gro_b0yNpMAkm8-mdm13psNW38wd7Xxy2biSAP4xi5g8X42tBWZc_gpSuq7yUs_Ny5wZbeV13YEyy_6GcKNL0ZcMv2G86nTn7Y5YE5LFyFF6fh6w2aAS_64tRSSwlwI1EhMe0AzVZtWRZoHAYA063nbHaDOVz3reC9MKaptfLxlS_cBqtbQ1sTWUydFYfhYYPuKRxN-ABusaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwY7qL_uaL53Gcc-b79lJxg-prPQVzhE3Ju-IULpMDouGEC801lPUkNzdfpRA4he5uaem-sg2Zhw1drK-s3sTnjsvv8756lzT1O0VHv4VnAyhvNeuBRs0f-aM1KriIufNlnPjoDmiAO-SGAjnOMt13pzs5Ht6lAwMFiZ_mTj-dGAN5lWS1XaHVkLprR7-LGPHgXDWTngvHz2eWaxITGavFypoajOPPpeCaMEOvFG7C8PUNajudGwCn_I0D5tOk_RQPCWL7dzz6bjSFEx0C7GtJjV3Fql-qbrEnMeGTXlMYuh0SdiA6u-aPdWhxIMa_v4bzIb502Jb8-OyPnUoFxFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه صهیونیستی جروزالم پست:
موساد گفته این افراد زیر نظر وزارت اطلاعات ایران و با همکاری سپاه پاسداران انقلاب اسلامی قصد ورود به اسرائیل برای کشتن مقامات ارشد اسرائیلی و انتقام گرفتن رو داشتن که دستگیر شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81133" target="_blank">📅 18:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=E_0wpoVqkyxy3nhrcVFCYDtcjKG5VNwdldZXoVKI-Y5_pDvl4Ha1-ZC4CRiwxRmhMVRz03uQIGmehBPzr8syiEAKmGkSxMUYgFA6QrT5iJg6490wktQzHnk5sXLvqEjYI4bBUuQu-2cU7PTD5UEf9Nxl5RezRGJ1erk08kOXFqDuq9tOwFf70chf4r_wSLJz6BNx1AQCipxZtHVncVoqfENmIXnE6jDdsr3Rtym9OcYi9jl_a021f_Chk7PxGu-DncSrHcYEvcLGh4lzyBuoIV5rAObOqEluAzH97GGk6v9gwZIlJ4lGCVDDts-tQkVgSGZ-QFxDVj7TYJmp2UBbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=E_0wpoVqkyxy3nhrcVFCYDtcjKG5VNwdldZXoVKI-Y5_pDvl4Ha1-ZC4CRiwxRmhMVRz03uQIGmehBPzr8syiEAKmGkSxMUYgFA6QrT5iJg6490wktQzHnk5sXLvqEjYI4bBUuQu-2cU7PTD5UEf9Nxl5RezRGJ1erk08kOXFqDuq9tOwFf70chf4r_wSLJz6BNx1AQCipxZtHVncVoqfENmIXnE6jDdsr3Rtym9OcYi9jl_a021f_Chk7PxGu-DncSrHcYEvcLGh4lzyBuoIV5rAObOqEluAzH97GGk6v9gwZIlJ4lGCVDDts-tQkVgSGZ-QFxDVj7TYJmp2UBbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5-jntYoaFl9GQsyboUQhX6bFQg4uuuwuSNuJpf6kgCjLTUuUKLBeYwVZRYgHlw-ru0sAAbOU-5fqrCWjDPvzIdOpzO05Oqt0oq9s-ZVSAD9BOzLGdfuqSqHynjrCtT-57C8hZndWTf47_DTY0MzCqB0WyC7bcm70RXgCa-XzVO55NYJpYI3kpEhQgAUwwgkOmW0Pt4NnRl6-rqlut45sbCGXQ6SH-vo9CiaIeV6ZEVFIpyD7TQRQtzMytOInjXls0J-0KucJOkgbvmW_x5awh4MX6YUOV7_odB5ChGmQpay5vRrZy9CLvRbDk7MPz3UPiccC1RXcmZEpNVIcQ_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81131" target="_blank">📅 18:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81129" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=hmAild0lUJv0lNGWltxd7V4PNf4Gh2IpCHh2nR0vR-gvxNUukGDl-0cLT9wjbKb8iQBiZljXpEA3ag7s4FfYSLu3l8Af8RP-UtenuxOuM3jX-38OTqEyExF1oiMZ201dJAJDwfe3briS0RzLWQALsFUE6maIuwVqo8RDJSLMFqnBQ0hCS4V-5eqWdKs5F9yO8jUsDj8tI93SErzwtlNo2f1fCi_7SrzUd_BwuxR5sAZlstKzFg5sUC2ekbGhB1rUDPfl7VRC92CQxk_RY66-8g3O_M5WYNJJDdYl9Whb3YT9-jAu7nLvw12XKeSxQur-vZ1fpQWl17RnRx3VdelfJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=hmAild0lUJv0lNGWltxd7V4PNf4Gh2IpCHh2nR0vR-gvxNUukGDl-0cLT9wjbKb8iQBiZljXpEA3ag7s4FfYSLu3l8Af8RP-UtenuxOuM3jX-38OTqEyExF1oiMZ201dJAJDwfe3briS0RzLWQALsFUE6maIuwVqo8RDJSLMFqnBQ0hCS4V-5eqWdKs5F9yO8jUsDj8tI93SErzwtlNo2f1fCi_7SrzUd_BwuxR5sAZlstKzFg5sUC2ekbGhB1rUDPfl7VRC92CQxk_RY66-8g3O_M5WYNJJDdYl9Whb3YT9-jAu7nLvw12XKeSxQur-vZ1fpQWl17RnRx3VdelfJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81128" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81127">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81127" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81126" target="_blank">📅 16:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaUOMDBdnuxIf_gLKjP-lP8jrMuIyG8ZBEWqGkh-O8EDWQF0wFFW8RzmGcGrSVA641lGRgEOFkSfyyEGmb1fG58k5Vcjdf5fY7603hYc_icTJUOkESYx3m4464T24ZbPE2A0-OaRZQIgDHHfpbYfrI_nedYUBDr6_tN5f3IAtPrFEnrkHu8CdwnraT0M8hwYCaZkH5AV9TVwQvnbqla8UkpDTT0UmG_h2UuGxhhZetVvrZqQDm0O_u1XkJQMwAocKDbNmMdXyKI6J35g4Etn-Rffvzq56-cQRqASlZj7uV_kNdaeucgGN2E3GdKiSF72DLVTBMbjy9FWwKE0jZxLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81125" target="_blank">📅 16:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امباپه هم دستور داد کارکنان سفارت فرانسه تو تهران تخلیه بشه و کارکنانش خارج بشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81124" target="_blank">📅 15:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.  همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81123" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSlUAZrubDt2cmsUjRhxPh4N4gKpmUTJg8dy953GB7_P-17EVcb8UPD0bs0rgGPD4ZnNAUV9Xqp-R0XV6CcUmYI8EY9wVjzHjFfdWa397LI69_zksqHib8jIXxXepDLGz2BEQV-VRVu6F68jD2GSzc_HfmjdGjW0h0jzwLl0Fq8ELAxCzc4Ny6FM2LwP7Ch-3nTS9l-HwVuhxpAWthZ7Oi8FSSqF6AhfQ-6besUxCTulh2wg03krAUre-RwfKgnsaOE5i9gX2tnabWE_DS64yLyLafqW4xHLtqFhTNs9XCR0a5iKFPtaYHZ6iad6pXKRXAuzW1LwWGWGyzz8DEejuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81122" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmLZRQwyyloUUQ5QOhiASnlro9vWacyjZF1hKBm-CeC2VI5eYImlUnegsYpBeeFlNOUJ5cighBdRtkMPqQjTu5sqQnEzHICpdZTM8WBWFBapUipPGOglZFml90JjR2cBQ0y2UsOCef63PtEqMwcp7WvAGb3X0iS3vTTkYpjKWTlhxGhuKDYRGXoV5fPbzHjKCRwmMNMTXcRInhvINC0TQXM_J4Tn6AVf61cJ7SgdgoFp1624xkRzL-gG43Y1jqhSDIJjJQdl4LoxpDxxYHIACcdk8FYu9abGw_VW32lBP776tfncuoFNj0jITHPsfX4ccKLCDYwl1_8J1PkLbxviLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81121" target="_blank">📅 14:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF4EEQOeV6OmI8RDt47TF2B0zVZCfBKwcZqYgzWuAmDNpDAEUOmSH0uKDyeswk2lnllrhla16wEJcI03x2Vre4XRlXCyAKfj69SIsGVrfhSEphBycQ2DxwBYzw0lZQuo9Da0IIFxuWKvdrUCbgjtZOQF_tApuz-QExDO2LEPer0RGUGMmb6s4TqfFXBkLAdAohU0VrjdzwuCK38JqZaGpQQxA04yidKLV1Q2GGHWg1MtxPFJeJlM7NtyDA1NIoVFvs2ZCMtAhw_am7W0XpSHpISMEysg4O9fXnTq-6-lSw0P-0JrlDH2RItpJx8cbz1PFJM7ovffeeHmqycOn0X_Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81118" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1c-EHB7tBKe5oHz2fS9MDXjphlJPmfzl1qKYicY1_0ytOnciY6YaD4Bo34bcGI4DPhBQ4uNdA2SH7cWxAZSN6ICbbgIWuZiY_WHasMEQHQfrnx_3H2xZN1zhzdougArQyyOv37foLEp71MV_0UJtF0YEqPL3nNJr5_l5fetWbUdOhFMW6ZqYhrU_cAux1_W3mjrIPNtaX3mbrMe0wCxfvoQ9Fgpr2G0-aMaObSy-LEY3i8aE804O82YGDWlR1ayAQFINCxfRwg1jSM1u66jCTsaLyRu0yWd0FbCQCS1-Bzdb0tyDlZL4cMhj0qRnoopaKrFtBhtcyC-52iIksxnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت ها مانند ابر میگذرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81116" target="_blank">📅 13:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKSAGto4EkkqUZEC-WxDhh_NSPjYXDhJMd2UP8QiX6D9qjjxRCpR61Sr6TuihAepIZxt2NDZPbr3NOatu6kbX481MFYb666Fb7PJrLqDuXJTSysjf4_wBkFT9Dnac0ifOinlyOx917i6PtNk6nyhR_L7v1Ct28B62s2OAxnuUfNf4lzndU007jqoHSv6BpzllIc_-PsV5Vd5Bjgvono0vVrZKaTtjB3QhA16org2OxTGEQgOv5nTGBCoiSxP9FxK85y3hUD6PuCjf9o4BgGuDBLe6ZwgwznO1anxUcxlKhkgCu8NvYYulfylIGpe98QwQPoRU7sVNVoO4lGGqrLtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGHYx9N0zcmiGIR3bhhISAamk92_UHCLJzaNx5MCo82YjPp4DGSevvuECHPjy9pIIRspVHDWjAhSM_vn_x6qM0MazGZq_LQhOBQmta26ceiQKr6WyAbzRfcNN0GUZewZguPGNRU3Esr7Yh1HfFhXYaFjvJGmWk8Nrvm-zVzPYMBR5eiGZpxlQOsDpPe9iVJOm6rZ1eav3dBJLsRfCmXHTHQsiIYZv7irsDLtq9GC3qJmxGnVV3O5cJYUouPrHpl4JtgelJ7uQmhb5TQl0oHrpInJA_jHqB0kWjjal2BHrZ5ioDXOkyux3kDV8uxLnhyxEni9OF-o8ha1cPEJC5rR1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک بچش به دنیا اومد، اسمشو گذاشت کندریک.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81113" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv2tzHaAX8aPLNcna-ubAQjTDSZyt3DDpmJM-03lSvi3_w39hpv23586M3-XpVziAvf1PWjSTI1dgiUB2ZptxlHzHfQx-JrBMZi4Tc9QbQRhAgqlHypd6qNqB5pdVaORzsFRTUMm8pYIJkdX3sxTi1vz8OAVHN3fNYUIKr_BHawWIoCGgs6TZV9fIPZpcvpp1EPOiRAV-zek5X4QihpogrwqY0nfLFC86jagrUkUl9iIIW_EyVGZuIQEyN50WNvmNQSN3x1MKQEkZvUqICLkNVWUpSe-3gvlfE9pgEyoSb6WcPPCy0UzRYd6HxyPuDdG_PeCrtWi7KLyQKJEMJy8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا در کنار جوادسیوس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81112" target="_blank">📅 13:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81111" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH7gLZTMrgzEqgh-lD10TNAi5biByc3IHPujLVHL9GNp_chMlgxEkS29TeK8f_jPl5qlFQIKlniODDYK1opRMVs9ZhCxCESjCc_jbx4-vTCENnJB0PWZKDsEuftiFKgN_oTUppWJntL1pD7yz6h2Fi_1YBGEVsq0xl3bAoBBC51UbSKmVSxLCHozjvAK_Hh_dEe26iohCr7EI11ec4W8LBx8CPOu8GKFLB0bZhCdN0caO6E0XEuDFBq8I4n0jmnlv7f0KYydbOdPQpa6VaVKOjJ_kekb12CktfkjONf34u48jcCckVtTnnX5dEsCa2nB7HIg-2pYkAIElhoHTNFEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81110" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUXRgyr1BcRL7G87ecVraMZdYHm9ZFwEPcj8Y13RoPayy1Xpbj6K3No-ZQk3a8jZrE4q9PAS38yJW-Kcu3TZ8ECSqWZt9JB_n-ZveRW2MFDaAjna9WElop17X4xk8yUiFU7eUSsDPrRzE_YjXUbGBoQy1hRmaTWUPVFUK1QwkDvGrHjBxFxhMRErfCO4V1ePQ4LYAQmRKYLRtoMeB_zrmarjllzw0Wr8W-xdLcV2GifXHFIfD1kMkbHL1vReYHBQlnaJvq2WMIrG6DT4m_4XB9mSXVUAb5XdHCZlsSCVlaww9wcZx4krlgaTCzC2pICEdNFZ_aIZa2-z7OYE_NQfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.
همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81109" target="_blank">📅 12:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارکو روبیو:
عراقچی می‌گه سیاست اونها چشم دربرابر چشمه؛ درحالی که من معتقدم سیاست ترامب، سر در برابر چشمه، اونها بهای سنگینی رو پرداخت خواهد کرد.
هر شب بهشون ضربه می‌زنیم و این ضربه‌ها قراره هرشب قوی‌تر از شب قبل بشن تا جایی که ممکنه به یک درگیری گسترده منجر بشن، این اوضاع تا جایی ادامه پیدا می‌کنه که اونا عاقل بشن و بخوان معامله‌ی خوبی انجام بدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81107" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ازونجایی که فارس بیانیه ای از رادان پخش نکرده پس قطعا ترور نشده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81106" target="_blank">📅 11:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObAJSZrW8415K6kvjLsFbm6ZhRvnYvNijmjHzrzw-_RWN6kqTXH9ZN03sJNe4qbZH8beYeWQt9KtoUuq2MJ64WXgNfzSNEui2WVbJiLO9uN1lRVny0H71ir2aPC_4KhbSIisJf3t9s7YieXIQygu1laQfXDJ1SygNOMQnasUvLHKNaAgLZ_Yqlzr9lx1wUvy2YP34kFfZ_rysTURDv5FEohKmhlMO6DGZL2bSOcSTtFqtUKKO6iRNPeqws48Ef5zuki4lpqSjyKLllE_PgQkrzWf79bIgzR0RS6tcwQsVALyKdicqoIKkWbxncJIpVN8rhD0hfXVQ1iloKBWysCUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقم میدونستی ایران نباید هسته ای داشته باشه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81105" target="_blank">📅 10:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=PNXvj9sX2c-hXwXMoVVtOCs_q_aH0FTYEmL7kOPa_ZNPcaJje4Cto8qZyhstL8b2IH3beWmf50A3xNEJWjs2yD_piO910IrSd1gdfLLMZkwp8cfmyH9hzsiyI0981O2ZDQX_h60p9Y-OTaHZobvwBQpgC_-53CKIwHACOsSYDWJCVIdCPRiMuDQy9JdKCtXgqiQNieDU7I4eqIV1oXuMTXpgVHAt7nvnDsH81v2m5YN1re-_owdjwGV-SsuacQ4qgpdIxgsFiILvKS0EW-IpziQtP5H-4RjFHWHvxcaHTNWdbjg4R1Ft_Vuzcws7S01EC81Z0RijdMmhb6M_4uQeAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=PNXvj9sX2c-hXwXMoVVtOCs_q_aH0FTYEmL7kOPa_ZNPcaJje4Cto8qZyhstL8b2IH3beWmf50A3xNEJWjs2yD_piO910IrSd1gdfLLMZkwp8cfmyH9hzsiyI0981O2ZDQX_h60p9Y-OTaHZobvwBQpgC_-53CKIwHACOsSYDWJCVIdCPRiMuDQy9JdKCtXgqiQNieDU7I4eqIV1oXuMTXpgVHAt7nvnDsH81v2m5YN1re-_owdjwGV-SsuacQ4qgpdIxgsFiILvKS0EW-IpziQtP5H-4RjFHWHvxcaHTNWdbjg4R1Ft_Vuzcws7S01EC81Z0RijdMmhb6M_4uQeAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی مربوط به حمله شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81104" target="_blank">📅 04:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X94G4iz0cceOI-TgmzXEM0LhieVDhu9j0wwczuKD3JUBpYWo5ebZ_T7sK9lqTmMFexQZzl2zKx7c6DCFSmKMWbKFopnr7R_2Mn_EIFUALRklGcYiGFheeCDoXZc6jEvRYO20kIwptkpPDfiF0mulFG-SkmQqx8G0qxFMutzetJKTwpIolkkMREFTGBfjJHwx6TJZnuSJjj2CFGEEfUkLFfl2l9xv0NM-vlL3QXWVfgZzaPww5ej8XrYWZF1Pk2UJSzdpQNgMA19EF6QMXyibCBS-9caR2LClkFeOhKd31K0ifMzeyGBvA4uaQpZcBh4GxSnkltl55BBu8tfxEo8QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس امروز از رادان تو شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81103" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81102" target="_blank">📅 04:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNe4mh9KhlGmOFW28BovhKEX8pZJ6DWZayZgPh2WeN_VpHBWvwRM_ihsmFR_Q1W-YNC4h3DpuYlKhhoV3j2s26W_6k_4dS-8nHoo52vx9yi-m1UuV74ht21XngHmOFZ9VA4x7KLl44wfQLplY5GQIkgvyzIEsZbotB3swpwRK_1ZF2xMCoyf17ncXlRDpF0NULIFVpPguE63hhNoePntXDK_RAawazos2sMJcQFEVbe5oSlh8YKxksYvhfHNoUc49rl8xfNPBHlde6p1XvYiq9cgF5FrIxDTGDGs2q_NiyHN_9KSYnHjHR8d-BkB-0fYs846HVm99ncaQRswHmTgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه
پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81101" target="_blank">📅 04:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیدار شید فک کنم رادانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81100" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کرمانشاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81099" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=kUc_5-4-cP8OOos8F0QRgXfV5UVmPhyuxJnqq95CyNXwfkepovz2Ln1domMN92TTTszj6aeUqa-5JfZxMbhyJ_jrEquFhdZJvGwhEv1ODU3Zr4hM29wjd65jLMS7rVcyPOb1YvZcjEaXem6n2IgrZxGps9AvLhz1rO_Mb4ZMjLwxVf5qe7yxyyu3en1g-tnlOHbYwS5xiB-SUfeh7NaTCdaSf94_qqiDWJJsA3_w1tdXYGFRM5pZ2tWyG0VigYblFEsn4Rh9GaPRD47lp4c5xOLN0rM5d0ik9zlhagpwTa7Uuj-fJdjm0-OYAJ4azGg-0l7ng7gAIfdmdkcC96Kksg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=kUc_5-4-cP8OOos8F0QRgXfV5UVmPhyuxJnqq95CyNXwfkepovz2Ln1domMN92TTTszj6aeUqa-5JfZxMbhyJ_jrEquFhdZJvGwhEv1ODU3Zr4hM29wjd65jLMS7rVcyPOb1YvZcjEaXem6n2IgrZxGps9AvLhz1rO_Mb4ZMjLwxVf5qe7yxyyu3en1g-tnlOHbYwS5xiB-SUfeh7NaTCdaSf94_qqiDWJJsA3_w1tdXYGFRM5pZ2tWyG0VigYblFEsn4Rh9GaPRD47lp4c5xOLN0rM5d0ik9zlhagpwTa7Uuj-fJdjm0-OYAJ4azGg-0l7ng7gAIfdmdkcC96Kksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردا:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81097" target="_blank">📅 02:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj2RgtGmNsoFkqyjDhn0rSBN2MmTdd_MLgn0GZmd-LGW8GCk6c4th7Djta-IU3tNGlUsK4CkxGLJvtWa2bzUQVXs9rnaWDEgY_OXToaxtw4h0FBrFbY9w2ye8GOv982CAV5GKGadFyi675UM5iTdxCQ1N_0aT130ndtadZ7xe41xCxLtqQ6svXqtlMLTsvR1UHNOGReX_yFV88p0PWzvQMs9Yim9mfy7aeEdXNch7TRkMN2l1btIaE06yNbH3Q0oeH-nxi1Nc2N8SlFzheNJ2SWRAIkIsxXpEi8V2I5BvmSusgCWt2TYBOSBvis2SjOisa3dNUMVtxoJRk3juPGr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه ۹۵ میلیارد دلاری تامین هزینه جنگ با ایران را تصویب کرد.
پ.ن: به گفته امریکا حنگ 40 روزه براشون تقریبا 38 میلیارد دلار هزینه داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81096" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سیریک
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81095" target="_blank">📅 01:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرواز جنگنده های نسل 66 کوثر بالا سر تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81094" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK3mitaKL2tEWUtWIGQtttYEN-eEqgoeX5hig673FYNRJjwjH4nLVZvpWazWInZKO7pNV66ENH9RJ3dPbCeWE0Kwywh7-AfEpeObKfMBXeNbaQG9g69VtEBEldsclmYoRmJ-DeLxh1arLClqvtJ_HAay_747VI7ZKcWDkkKnYcvfN9Xzc-WnsrBWiUoCBfjF94IDnit4keNvMTJsi_k6WPIMYz6-2inE7_RO7rcR03NdETqmbHX4DQzYtIgSXbJVQkLR4yAPhU3cQtMaDDcjHmgxC5hGWddIh0pfNvKhyFMjzhjo7RL8e-zPdenllWLjkjLSRIgLn8KfUi-u8sh7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق مقررات جدید چین، استفاده از برنامه های هوش مصنوعی عاشقانه برای افراد زیر سن قانونی ممنوع اعلام شد
دلیل نگرانی سیاستمدارن چینی این بود که شاید افراد وابسته‌ی ربات شوند و تمایل به ازدواج رو از دست بدند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81093" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81092" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار در ماهشهر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81091" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81090" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
