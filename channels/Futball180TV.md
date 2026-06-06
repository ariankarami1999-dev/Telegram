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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 209K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 14:32:04</div>
<hr>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:  صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.  و حالا فکر می‌کنند بعضی نام‌های جدید…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/91160" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucRu9PiUlbXc0-ziElXKWzG6Rw5Lak-ZgABv1CuQGDrjXD99sYOnIGwoKhiVPiINT_Yld0EpaGa0ch_9-U8adADm_i46HkKOwjXuhIGd8OgkLLGupe-hKPqatJm2tk3iWcggfAv0ccVVEyRFuZyv9Ha11P77nXUSLmAbVaJ5BNj0HccgEqY-blgG_D2w4JPTZvM8h-GayvOx6vbBvNXkpzdD_BGbUPufwU29KOtqXoQznLHE6tjU85IFIDakm6_bM8wWG-8gE7hGaj9Uwgn92Qiis-otuBCbisJaekuVJtj0otR14U-1ZLk-bCvBG8Wq8NyW4rupP9LhSFiMMf-9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:
صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.
و حالا فکر می‌کنند بعضی نام‌های جدید ناگهان آن‌ها را قادر می‌سازد تا با بارسلونا مقابله کنند؟ حتی اگر ژوزه مورینیو خودش برگردد، مشکل خیلی عمیق‌تر از این‌هاست.
اگر بارسلونا پروژه‌اش را کامل کند و بازیکنانی که واقعاً نیاز دارد را بیاورد، رقابت بسیار سخت‌تر از آن چیزی خواهد شد که بعضی‌ها تصور می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/91159" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
تیم ملی پاراگوئه هم به این شکل سکسی بدرقه شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/91158" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gweyh3Z90BKMXbTKR67bd1RhtU5h1rNmRbVd-ZpVa-ITykvYjV5eqhiA-QkGfKiEnkB-wZGqyz69EC3-TDo6751PTV5XdNcJEtB8y7r6sZ38EmC3hfBzGx0v4cbQrmUKd0aBiWmEfpww9nAwI7jSMTvaQ5z_EdWSm9WcqyI1SZL-GHc4sg-_MIhKKmcJzPCK23Ju2ePzI1G5jSqqTKPsikyp-_waqFKzjJ1am_jvGYf34WaGcRysC70bQFfi8IbojgJcztubYFwqDjCZhGPOF8lTI8g-IEnnX370_fB-EL-UeH8f93SBDu0-L9FIE1ilTpz7did4IErvftKrf5fBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دلیتا تو جام جهانی مجری خواهد بود
🍆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/91157" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtYwfClyNmiwoTtxPI6dZvr-xa2Sod1IszwQ2bqzLA_men7X-UOWKq6eRmB3PrAKS1urSCOBCmv2CPDVibdMOR3hJePalSBnp2C7rSmacAc5fmxSGM_M3mdBplmqYQ4Mu7gb20VuoPGhvdwMdbgL5yQKAwSavOGXW-Hgp4gq6VSf4XYRn_ZLT0Dpy_CDSOvZJ7kgaaiWCAVSHxp6OnPElF_xbsxFCAGosKpw4v-S_h0tH3u383Uq0S9tWWp5iRq5iOJYAMO8_Jifa40HkqIKmPIu08bpaCiyP4UW5yQSD4OPYTmFztpAylDR5x43wnRlsoiJTRlNpC-mMt3yGRIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 سال مثل برق و باد گذشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/91156" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdGE1EeWGNck2qT6dCx8Wb7r2NFchTNSD_hFn2BpbWXsNGyy-k_uC_U6pDxjVvdeQuxL0W8aMJcA8vALVtJCiZ1Er4ZXeLKap8q4tuEG1AvH5JgyXBQ7Ih0mSqWUsPREcbWKVDR0DmwqNGLw8yQNySET3sYb9fcBtECKyf25iEPaqaZzOI80JiVO8nJuwLuGeRHI8qbO7CoBHxWodRfn3Xarr0UpUaLAMuY0hj885NzfVbIAaglmij2PbAK5-onj6D0c1b8GhE4zFbWaxNqcI7kXwA6ktuPLYBa0cMmUwDQmQe90JVokQVWbz2CW8f0q7D2QzVUGnRBU0_YHViU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYVW3ryfu07r8xL8OjLcQJkK89BLE9dAUram6keVba9k2Pd1cNeegqmJUZTpNPHn5SJNhhqgFsfu47qQ3ZNVIjM0ZcVMP3q47pfcrtTSGrvqkfW59-cFz-3lMkpfk7QD_eejtaH4A9Hre7GXDziJaRBGAAbqrgCJohcSUJmJ3ZsBCnaXfp3xP6WtrNZoyuduLUhJT8Dveh3i_YC5wJFdSAt1SlPLWb-zd-JEm2gW6nBe1Kw-5STbkmV-nYM3uUTTnodtXmHeRXUKGTIMA6iOfrZJIwoZrDC-8m31JuQ_edTQn3XUIHtk80XI55CCH-b2nkcc6ijwk6fOFxdzVq9Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZImLL07aXPRlUhilaMQJNN5EfpsBtH1UH483p3OKj8L-F2HluR9bplFcPjEjQTCpb3as4uGUFc2bGd_Fvw8urE4n1GJvOg11LsLm1cKn0GcOi4nW36QZ0Ak3PMuvSv96wN1b4n3yHXE9HJsUMQ4YwigUVz1Ywr6FQiZebsrmFVQU5c40-nkJ591BCpHvcIcGHyJgpB67nPLjfvjXSjoY8mZsY2cLE-VSPSudkG0vRMSVsxbdBLoRSzQ4yaLPqo0ZFRWCCZo6gdojR43X1qr1mVkuuOjvL4KBe-blWOPEtKgomEx_NGvES9ufvO8Z8bwBnP-opFNe7tjXqFb62qGbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDAIOHYnCcuDGA8ZWc7w85Y84ReJoo7VKfAWM056aeFrZD0J7hXZGevHBcJW5JVCFv26Zc940csCzePng9blq8WIjK_UDap-JwXw43H5MEyGi23eZy-a_Rn5UgQqROG3u9XbMWSGdlrZq_0aTIrlRaNyihb3GPYgdmoDCp2TTqRb9MQ29Wm-fLrsTIXCb22z3BGWuSbVwx-5RzsOJtEJpCVHs2IlCLrU0N1b1FsY27QaFU1hHfmKOa0RhFmd0-XsSLlaqWq9xzA-H0KQrhUcqvBkalKtpa5rSpE7l84FHZMUWtRYzBQo3KJzKHcxQx1cwyWu_WD-a_Hs8Nx1rmh0cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🤯
مادلین رایت هستن که بعد از خداحافظی از فوتبال تو سال ۲۰۲۲، به طور کلی وارد OnlyFans شد و درآمد سالانش از حدود ۷۰۰۰ دلار به ۱ میلیون دلار رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/91152" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ePsXRWeo0WxxqsLN3Umh3mJ35cEh5zF6XJEhA37nmqHh9ElzqOHo64kIIpo32LNSGUA55gI3NPUT-wqoL1GuGt6_spa1OuT9akWj-TUiEYVkThb71pbYjdivs2kZFkQ5F2-kNqmaG-XLu4SKiVUX61ofMoEwIBuAiLwX4GsttV9OI2SwO2Q6fHXOp4xmHMhluYyxK0BloDRFUyUTBEVe_1DeCwsqQrNuvh_jSlnu9YPBsDO2K6H-rUrbFG2QD3V2X1mbc_C-Nxin1-VpilexOiG7EsTBksFvL6kGVQj5do4TUCHSm1F8uTIYggxdSWYOiq1lejZayFywxzYdT3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/91151" target="_blank">📅 13:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
موسی‌جنپو بازیکن استقلال قراردادش رو فسخ کرد و یه پرونده جدید به لطف علی تاجرنیا برای این‌تیم در فیفا باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/91150" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J64Aa2ddxYMNZhhbzlwdSNs58y4zk85aVEPCgZfVXYRhHtoAGKIBdwit0YhI9pE0UT5oO6azu7QW4dileGA9cCFeMdD3IR7HGSwOuZbudoMbApyzp8Qe99jgxBFFpdgDZsH-PCZEoWWhQ-1WUGZuMFXICXNbadiBod3-KcbcpQ9f4ouwp47gsM8GnrIJ_obEAlw9ytjpnNf-845xbo5WEk9jSAMND-P_3WfYfrXgg8um7eTZoqcXdv7mlng9c38VYiLgIz8XGtx1iUfb8ukCpuZlhXnS5aOyU2PjJk2q9GPZX4bKYGcdpWNDqcS0NFYHNZ99fvVqOblZGhXJI424DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از ترانسفرمارکت، یامال و هالند با ۲۰۰ میلیون یورو باارزش‌ترین بازیکنان جهان هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/91149" target="_blank">📅 13:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
#فووووووری
#اختصاصی_فوتبال‌180
؛
🔵
ابوالفضل جلالی در لیست خروج باشگاه استقلال قرار گرفت و فصل‌آینده جایی در آبی‌پوشان نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/91148" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H3m9WiWezbWX9cNSaDjJWj6rkLRlE-56PpTmRTG2OKVQqX-VBY9gfBPurx7PcAwZ1CKD3DygrNt8yqNKIknfJ9rrk7dWUqLd99MmFjKR108_fb8eXvAFYxuwvrFMIS6uDm2sUZ8ivFFjMn47x-GNdpxRaHLYzVXOgJ_KHE-O0KInm1URuTAaI4-BL1QzSEWDC5CvfpcRguT_qO19VF3rNf-UpDPi6lV5hjI36vbJXLDuSJJG0J33rtIjPQmj1YKiFqEo_UEvyzxyTtT0LkaHzRJhtCfAdsRbJZioTC1-v8yNVdElkz0iwdxM92oDXZ34wuWuii_TLb-bBI_lEMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇩🇪
اولیور کان مدیر تیم‌فوتبال بایرن‌مونیخ:
🎙
اولیسه باید از خودش بپرسد چه می‌خواهد، رئال مادرید او را در گذشته غرق می‌کند و به بهانه اینکه ما در گذشته بهتر بودیم فریبش می‌دهد، مجموعه‌ای از افتخارات و جام‌های قدیمی، اما بایرن مونیخ آینده را به او می‌دهد.
🎙
رئال مادرید باید دست از زندگی کردن بر اساس افتخارات قدیمی بردارد و تلاش کند در آینده پیروز شود. در گذشته نام رئال مادرید بزرگ‌ترین بازیکنان فوتبال جهان را جذب می‌کرد، اما اکنون اینطور نیست و آنها هر تابستان باید بنشینند و بازیکنی را برای پیوستن به تیم قانع کنند، ما گذشته آنها را نداریم و آنها آینده ما را ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/91147" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
وزارت خارجه آمریکا:
فقط برای افراد ضروری از جمله بازیکنان و کادرفنی تیم ملی ایران ویزا صادر کردیم و افراد اضافی جایی در آمریکا ندارند و نباید از امکانات ما استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/91146" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiOM5CL92d9Oz6OcClQqPxDDmmHPKdKgXqX62Hejl4ojrkpneyRhvfgkSAXxFtR3C0msvAckvFBg_4ii0oatbSWBSzGPiGKXxu69sx5LKc5K2ZBhxLJzciPy-b8TZYaXnIGUwJiTffSQtEpn_B8h-pea5lZsLNMw6LTkBDYCQ_g0_ApLcTwexpyzD8c6zz54uhDeyJIaG87WV0J5qG25J3uL_BDpaIFFhKp7Yf5js_Yk_4i87wiC15-YzId-VKC46Nbe_xC_of8zEfle6fOgqXEGwf0rop30E3GCcsFOwxnXCQRo1xBCHDi6RzDBDhjds5mj_rmhC3axnbdVZ54Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی مختصر تیم‌های گروه A جام‌جهانی
🇲🇽
مکزیک:
لقب: El Tri (سه رنگ)
سرمربی: خاویر آگیره
ستاره اصلی: سانتیاگو خیمنز (مهاجم میلان)
تعداد حضور: ۱۸ دوره (یکی از باقوام‌ترین تیم‌های تاریخ مسابقات)
بهترین مقام: صعود به یک‌چهارم نهایی در سال‌های ۱۹۷۰ و ۱۹۸۶ (هر دو بار در زمان میزبانی خودشان)
دوره قبل (۲۰۲۲): حذف تلخ در مرحله گروهی (پایان رکوردی که ۷ دوره متوالی از گروه صعود می‌کردند)
نحوه صعود: به عنوان یکی از سه میزبان مشترک مسابقات (در کنار آمریکا و کانادا)، بدون شرکت در بازی‌های انتخابی به صورت مستقیم صعود کرد.
وضعیت فعلی: آن‌ها بعد از تغییرات پیاپی روی نیمکت، دوباره به خاویر آگیره باسابقه اعتماد کرده‌اند. با داشتن امتیاز میزبانی و بازی در ورزشگاه مخوف «آزتکا»، فشار و البته پتانسیل زیادی برای صدرنشینی در این گروه دارند.
﻿
🇰🇷
کره‌جنوبی
لقب: جنگجویان تائه‌گوک / تایگرهای آسیا
سرمربی: میونگ-بو هونگ
ستاره اصلی: سون هیونگ-مین (کاپیتان و ستاره سابق تاتنهام) و لی کانگ-این (ستاره پاری‌سن‌ژرمن)
تعداد حضور: ۱۲ دوره (رکورددار بیشترین حضور در میان تیم‌های آسیایی)
بهترین مقام: مقام چهارم جهان در جام جهانی ۲۰۰۲ (به عنوان میزبان مشترک)
دوره قبل (۲۰۲۲): صعود دراماتیک از گروه و حذف در مرحله یک‌هشتم نهایی مقابل برزیل.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در مرحله سوم انتخابی جام جهانی در قاره آسیا
وضعیت فعلی: کره جنوبی ترکیبی از با تجربه‌های باکیفیت در اروپا (مثل کیم مین-جائه در بایرن مونیخ) و جوانان نسل جدید دارد. آن‌ها به نظم تاکتیکی شدید و سرعت بالا در انتقال توپ معروف هستند و مدعی جدی صعود از این گروه به شمار می‌روند.
🇨🇿
جمهوری چک
سرمربی: میروسلاو کوبک
ستاره اصلی: توماس سوچک (هافبک و رهبر وستهم) و پاتریک شیک (مهاجم لورکوزن)
تعداد حضور: ۱۰ دوره (با احتساب دوران چکسلواکی سابق) / این دومین حضور آن‌ها به عنوان کشور مستقل «جمهوری چک» پس از سال ۲۰۰۶ است.
بهترین مقام: دو عنوان نایب‌قهرمانی جهان در سال‌های ۱۹۳۴ و ۱۹۶۲ (در دوران چکسلواکی).
دوره قبل (۲۰۲۲): غایب بودند (نتوانستند جواز حضور را کسب کنند).
نحوه صعود: پس از ناکامی در صعود مستقیم، از طریق مسیر سخت پلی‌آف اروپا (UEFA) موفق شدند بلیت حضور در این جام جهانی را رزرو کنند.
🇿🇦
﻿آفریقای‌جنوبی
لقب: Bafana Bafana (پسران)
سرمربی: هوگو بروس(مربی باسابقه بلژیکی)
ستاره اصلی: لایل فاستر (مهاجم باشگاه برنلی انگلیس)
تعداد حضور: ۴ دوره (پیش از این در سال‌های ۱۹۹۸، ۲۰۰۲ و ۲۰۱۰ حضور داشتند).
بهترین مقام: حضور در مرحله گروهی (آن‌ها تا به حال موفق به صعود از گروه خود نشده‌اند).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: صعود به عنوان یکی از تیم‌های برتر منطقه آفریقا (CAF) پس از یک ماراتن انتخابی فشرده در قاره سیاه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/91145" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA_UVDOLhS0zeR_LSSLTXXQ1kdpEtZ7oSODeRLpI-WKTxok0dQhd0jQGtwfLy-td0KWwbQGPU02DmYQ2cfPNFSbxaLrNZppy2Mzqnqi7FcR39mySSB0oT5gLQqVk9RreIe4KxxKsgEiONEL_isiUnQmXiOjneA3S3zirdHTmAkzaNP9YD-rzVcbXAKP4nd5gySSJTNjjl6t8_WQYdkw7-oshBdBgknI-C-kMQGp9P8fBEBuPr_O9ApTR0MSOlrT_QXiWyfFjgqlmfHZvsOV0r3VfnRnp7rsp4KZH4URAgvD0TNA-NuJ54_ZqPrTeh8B9QWEFGZ2qq64JpF3oQSCqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاکا: «من علاقه‌ای ندارم که فرزندانم بدونن که روزی بهترین بازیکن جهان بوده‌ام. فقط می‌خواهم مرا بهترین پدر جهان بدانند»
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/91144" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-e4yDA_cPSsig_65DdXqlTpHsZQgFnWBTWRwn-Fdl1Z6gxnXWhdGOS9MloSUwbqMOo2EBt_X9qVE2LNPLK1776xWGA4fHaFTwmyfNdIRfI41UE9K21UpTcgg41M5qWYhT_3NnPv8dJucTHXWMVUGUzbDROSh8t9-JA_f1rWIjRyWN7UVPxZMMBFVPZYcOMzjNol8FKbd2TQkCWRhopd6EeoXm7KAab8srpxJpKZarPKJc9dCiNcxsIyte-i_W_ndXmq7POQj1i6nracO--vfxIX59IK9HaaRafhskO4r07WbYgTc6lcKGWOKuDabnSLtG-5iga5RISrE_gQzq-LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7pDwI8WWoPYCEEQIBGE3Iq2haXU_JHWMCWHkDh2MbY8I2n08al61wVmOfhSPVtWiTtHCyAxWUpgxBvw7-dIt74k8hjzydW1g_vE2KmIlK-6QYDQySIV7XpNyCDE3uVrF49prlWP96VnP5rC_oc5vxLgJH43ONv2aeLKZiAY2UR4PlSd8IwYMkcJ-yXtjvTquCDow600X32WuFScwVfixwaBt2bQ_VYFmXy-MYwyudHYAJFZTQo2UH4AkM9Jm4JOsrJJMO7JHuPotwT8Qn3HZ2TsvmdsPz5FxZAC5BL9cjGXdXwpQUWhrS6XMldu5vumVw9hlRMZCNtVdPSHqNuPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UJLu7vL_BVfqH5u3qACaIFrA6czAH4glnu1bj9QJUZ0YS3cnFy99ZzqTZnBjxb8ps5qhFNWy-1bt_pO8H4ne8-ZypxjCH2yw1KKWSL8okhuYS71LzMB-bsC1yZWHRXz7mbbClH2u9XG734eJPPNvM3GlKm6_yfh8DswPcu9yP0qVXVGcthGhfTZZB_Ip1W5K_U9-iUZLOZj2KDCJ61uHeD9IV2WBQxuJNkYkvB4fVPnIhRcKPh80KYqujgZ7z84H12BeNvZzvOcivAnBlTAiYxkZP7BpUx8yaspCsk-jcZX0s8uZGwjPfOdsE2fYw3q-wJQAWf-MYWEllEw_Shpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت لیگ پایه استان اصفهان: پیشنهاد میشه اگر افسردگی شدید دارید و مدتیه نخدیدید این ویدیو رو تماشا کنین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91132" target="_blank">📅 11:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعی از هوادارای پرسپولیس صبح شنبه رفتن جلو فدراسیون و از مهدی‌تاج میخوان این تیم رو به آسیا بفرسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91131" target="_blank">📅 10:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn0BXD-xp1B-n3TAnhWVwp5eE0zUZMnRXz_HF5YLUEYOOpiTqMcRRKJd25ebxBd2rTjUQI_LD5yYjxxJ7W5GxW17_9IkFMnV4rNXOFNVGq33LvO6rpGyWymREeWm8ZlPTyFBRO-xnMSoC9oen41ao8Gg9YNmXem0OmBQDIH_kfpw1i7lkqMk81mEuAYw0M5q22LGS0Jbm9PUHc-hKZcsB8hUfKwtuAqcPMQFXhzwK59H5kfzzGzO6BblwqA_DdDEUzZwt-kro8fWbkZQqvZq1E2D0FZku9y3-SqBrA5MggzIj0UsxbjbT2xCRnvuMkiQMVUGaqTUFUgIrVllqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری
؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91130" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91129" target="_blank">📅 10:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss6T0DR7HiJ8fWqTqeqdvlWXnwzZlf5oAsPlgYMOFHtylEYStfYwD_dduJgY0SgIM5ruustZkQkUG5_ogICLtNy1QP2vCFyRkBUGB4SSSyWwogayPrTgqRn7HmryBbSsemN3rSN2ZF2TkgKAakoZolI_1a5PcaRnAGuCvz74L9NqbpkocLnfAe0ahwEn_cs64W0CPXi6W9MOe14iyOq7M5BGtU19bM44kxH4hIdf0FG_GVu7bZ6qzg8-7vwwU7ASfoKlrIEOIYLZvd65MPHIJgJ_5CJLHEZp_0ITEoyGUmEH5Y-jdgZGPMqgQk_8MuUaMt7G4QQsVc5PMI6H6K-gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری
؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91128" target="_blank">📅 10:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91127" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زور این دوست عزیزمون از هالک ایرانی بیشتره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91126" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
‼️
پشت پرده اخراج شبانه و غیرقانونی علی دایی و دادکان توسط محمود احمدی‌نژاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91125" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1Fj-KR3eOvkO-X11__cNhS4rzG0d7VATK6SCJV0AjCKQMvWzy3vn7a8nmiGIBO1lGBG4xrMwwiSlsNHs1-mWcWgHfZre42BZKkL5KOnvfgoMCzcXpDTwVkvUP5SZ4e1cxXNb7VUimjP6dIAokKAj7qA4GpV813vpT7GJDzYrmn_GHRXi-nAo4wR4jejkwXmHQF-iZl-pZY0aJ4a669vqJ29_CS6-ncWe-xHsNv43-iM_0gFC0n6vCOKsPDIr6QtYBYliJdVc31vJ0Ny4S5rv4t-fxUIh_o3b7ZbY1AOk7hxdDHaZ9BB93Vcx5KZog-idtOTjx-O5g72102v9jQVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfsMXgnJWi7nGlYMQP-nGNtR9qBh6xLBFnYYI1KpVs3gwD3nW_eQGWErzFkKkfLLHl7T0aysCFo-Em_LC-NDFhuT0pwBas0-FEQHWBbOUIbiE4Z4YI3qI7S_6oJCmImPCcYE8h7EtRuT7SoDNelveProXCKLDi8TweUFGQJp45fc00kqGWJ_Xd1FdFQhHHCtd-iy6Bem_jbW8_1oQKWoX8i-SZEXZOt1x4jOdQqpUKEpyR_2tgYcTYgmATomseLQgzeyG3mOuU-CcjOZrZEn1SmAhekkqlS2CHqKBjm0YADog-gTSAbhdzZV3E_4PvoX60wC-ih2nC5H7E3IB0WP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3j5TMGdgCAhV2Pv5o7GDLoVu_gB8cxON0Nya6yURXDi3kCx0arzpAN_mSvrAedHmTHifmVSjXmNEDKkfc45479lIukioekiW-j8ZGwoqmIqa9do_nGgLWnh8bGpJ1XUzeuizmAL8htx_g2k8emeWGJMQrIdzhCX2GsJyfodLuUvZM2H6YHg-cGdoKkCRf8jjxl8ZvePp17Rweh_2NTUK8fWk7G9be5lYGpv1NT4UgCu9NCiSxplf2q9suY9vosLxMksmtC9MuT8-GVHYgAqNSA1xqP7iAsQkldKlP8N2D4qfLMeLGtxOoWhw07YOeBIGYjlk87tsdp5DnCB142jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKempgzb4IDdo-lCOAhO0-JMj8DOsbKlTs3_Rx1R0uotfaTASr_Zond7_aHkptTkIuEOygx3stIIubNgOoPs6NXy0jYMvz8EzF9wu3Jvaf987sEm0AV-VLDikcig7JUm614cm__CRrJO-w-FPld7BR0rCnM3VqjVc_OpblYxwhfsKPog8JNN8zz4u-HFQkscq1vvOeJ6imFAs3nVoEqFDbbqehIXcZelZtDAM9A2PboQTwE2iTrqqN_T2Rr5S-8mKl6D-Y9UBS4LV4J-D7HGjH4p7sj7YVLCN7JMNZckgjCgj8F18Md9_U1Wu9cP6tp06V3i3TfZPhlkEHlptzsZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktG8yM56tM07r-KrhT0mvzu1K2zogyYISs829eHMKG57zvUZledcWcs0Y_JhOfY7P7xQz5vI09K5w4AAvsMLC2N7mBXDs66RppN9hVr4tk-TjK8RPl6xx5NKsMv2j3c6jznY7nBv_n-VyB3Nw9MLNAsCgDj6Nx-HMy0VEXmIvLtIh7czBz7XjPw9nW_fX7ZWKn2dC5M38zPF465Umt-JhuLzyyvbP2VS2dRK37JFKdWGiI1BkVbKPAjhyoS7_ColyYJ4ccaKnP9h6CvQxSEaF7__QWQo0eQ_LkSaYE_QZKIlE4FyV-f0OzgJKug0PgogyFgwtWTptfjPM9rx5zdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_2P8bSu1dgqGwGJBYUZiCLRR3bktI4wGbIUmdA_lFTj3Gg7AEa8RUQozy0N4UcQk_GgioR1e3nQeOD4joczZqNiLbROyCNKnmcunTaaFPmHt9qH_fdLMuxi9QtBde-rPTo3tIFGpcHIeMUZPbjQekZAnNzAIln7ocw9M6DtTbUEdgFLk8-22wghDaAKDWpbh7nqQcq3amB8TPFDf29zAJc5uUvPq0kYReSqqxtzccpFStlDCcxruNiVX9NBIT82PO7kFJ0xSbaf1Yn8o5mnQLUg4LRvlOrC2g0OX7v937MGgvR_d0iVHPnq7sUnB_7PCt6DBxjM6UT0PRFVVNuzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjCLtEjhx9MES5c_jSZ-DspolCpiUQ98xoSqWZvsEmbBAkYHDWwjjNzhT5JiznB_iDVuqcJSR2taqRWkYphHlO-pe0nsImXgqPehTazCnyFaeu-aofyNeuGo8BH8-fxdhvIg4r3nCC7yOgLZJyzK21o3HDJhvX_MQs52zmJ6yocwhQ2mzDgy1tEgqFkQuO7CHvmjDc_t2sGWgERUR0aFaZ0g3ShPHdHxVn9T5oucwa1VsAxY4VXS-_JtO_BaUGbzqbJzuPHrF-ECphP0NNFA8cB5pfxoid01IzgbSsJ4gs43j6gM0mI0vdTUqa80wzxxrKgbPIJ1ML2ftXaTwuBNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpIL_1pEqEhyp084TeXTYSC98kwhvEDzruKmqlonaKbbLaGbMAWyoimqyjyVRtVy6VCRUeTcDPDt1qejOkQEQMHFjE7S7OCdkmskb43OLTy4fqsA1aIOShSMJ_7e874fitTTYHvmI-XALCT_PPt9NBfWIocHcAEemliIUaTV-3ioGlDZZFcq0zB2F1rP5WJLfRxwoT7lfXazYu8rbHhSUrMLCBfR1KkjytfCtBsyvAq63MKlC9dRJ1t1e8VPfb_ptYHapgcpgH-EPI_nfh5LSNhTOAskuOSk2tVMrJM6LV4u49gkkXvklbAqO8ZKSenFwPypDHNxbrSAQ55rlQsW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارل 18 ساله به دلیل پارگی عضلانی جام جهانی رو از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91106" target="_blank">📅 01:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KnvF7uEZORIc5CHKe8ywUJ8skTEeHyWkbn7ZnU80WujqYI6wHROu2otj60Dtz3OzmwZyQ9LmYA_yEvAkHMaBWbRYn5zVNwncQtBhYyR08YZAMvMrQDVptxZ7OFE6IgROBCUQdRMwWa0j2emNT88kY68hXjIariglvd_h10B25owj1sCqcpcjVH8UGY2zSx-wXVNKQSmkO05vUTPtXeNE_mfM0hnt_LcjERj-_8A0CjLgRhCNZZEcFf9MluJXEAqJSDmf1-8BQVRV9yFxJPGJicSv8HGPXb_KOYVKM4iALCe8S0aWa5qGAqDbntiFkGDJDdxzkA05VLat0itLrORCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری از رومانو: لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91105" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فوووووووری از رومانو:
لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91104" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMqhqjn4wId8418VU6GousgiGEp2zuleRRmp4pWFkUqUcMQ6mhQIxNgUV4RNzycXTbTNi1goUjOO5hS8oqgBiKTdyPXw3ffLvdHvQncM_KLELPC_OIfIbTJW5OOL1L5gKjetS0CD7hkR8oCn_URwn2Kjxfq1o6eoCQbl0-qoBXsAdB1HQPCjey_Z_kUAqvDCT8PeT2mirQOZf57Q52fmHPCQmL_0u01KDU4cQZcla0K96WBF2BgemHBHARB3vlTLIlzSgLzXYFI4iCgJSBmgXo4GWpK6_5A7gYJgaaYDA2nZaGAQcd2agZ0v2YJ6upL08r3oT515QWTJErhlTZqCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب مایکل اولیسه به یک هوادار رئال که ازش خواسته به رئال بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91103" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">First dance
❤️
Last dance
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91102" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5rluRmqOEQyXoyurpaFvOK9ZImLrh9BfsaE0acYpwEmXh_4VqRD7jLrESNEUsAG19MMoEebzllLConGAXdMajli0sHFl0NLJgmfot_38iQiFxRQk3vTd4ykF7ozm3jH-dr5LWxvq4m3s0RPphROiK_VXwjsogmSDvQYldoGR-1faM5iFbbidB-av7CKUTJZfiaLbhsQ4-trPtwU3WkxJ0rc49J_GfUkHWz_pTQHUzaANE-j8kfGc7cadNw3621NAI0yg-DGLBrihaFXceBth54h3WFaQiPHtulw4Sdyt1rvuxdnfAElWqw9pqSSeNcmgrGJedDLWmT2hsSjShJs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CneoCr4oz0gBih6dXfr6dHxbrH0ym0_Ltr0EA_vqZLH9KIFUNXjHXucCHH5hpHWvnTKNmY2kK6l3BovYdtVh3DN75sIzX82CmUaRxlViqEO0pKA66x55S9pYDPlT5Kh4y7uVtHu7OIgyImzSBSlUCAYCLBVwcZH6ji-e49oxWaIdZ6UvHbQG2m0yIa-ZdOnkDEhk8aTK0Xq2asp8GgvkGbW3VWyo3h0JMC78kSz5FZzZWIZ0kx8-bnMH83_xsImLx2pxQWo0Zw4QLETLQ1xRLg3-x39E7ffNrsJxtcF04RrSGM4H9l_DMO-lkOeTCYDd8f1Vac_bKsjPEVaGw5Cfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_cocnUdCQhxyTZTRd1wYRJCTvq0KLzdl4Pll1rXHmkk8toPNp6Ba1igWs3oeXKq3hDkmFybmYzhZXsmPsu1JSL0AhxA-mWGn6Aa01n84QyP0slfmeAnik6714kZ3AgOYrMLU544MaPpAaAMFdI1n8M5IfIpoVp7XdUZSwrqjJiUqFxlOliMZmqJ3RwQYBgjZmAuyxfQD1m7Zl3FGQxTlF-lwQ2wQN2XuGjpD3aqqN66evh9GxRqWVU9F0dZ6jiBCgZlbjz25tMn2sesB0H6OK37hqhN-b7j2IISoSO0dqhVrqTwfuOguNaIJ4Oo9Mf9A0bS6e4HuwKxXBTfQ1M9AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زید سابق و با کمالات وینیسیوس
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91099" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0bxqaoPsQUPyNLANGprHjzsfqd0pynZkuCvngPeG8JzTC7A06m5MmPOdCYzz0esjQXXTMRpRR2kcI9_WX2JbaK9nPl8VIvexB53azNB4n5utaBJ7sogpCUrb2QWcxCmgfkM4gt8NUt00y-zi2hOPDRpB8viQF49MhXGKo-p7oym95X93U793H2d-PhuISBXOd1uwGqorlJ0xQBFBHkg9ZnhTRDs6N9IwC_TtmXjQg_6irMnfldtG07aL2o56YZFlX16KrioCNnv3CloCdoYZcEGtUdlACSv38mkLuDFTje0XCoPYohbqNSnA9b-6Ar6J270Hzb5AUEbO_93K18TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال همینقدر میتونه بی رحم باشه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91098" target="_blank">📅 00:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvWWNsosJ8NpKzMF9rySwkw-GxBRGMdz4_xZap3kotaVEPY1IBEmxmpRgBG3oK1TO8lJfv7-6Mkct2xs0nga2kokChMlGxEGGSQ_rRCN_9XpYcZuDAbqJkt2VHiewp7poMYKZYwRCGE6PmAy64643lWicL-1xzELq_RIrnIr318lvfEAcKZexnK3Y_G264SniJiP888QcnhHtPACpapJ9ggajqbEu0kwceVQ1REYQdxiOnUEKUrHjl0q_oO4i1zIn0zRyWfDrVwa3YbzLS8MpSq_Zl4K2Fr1bMLG1nHJwTIRbj4IGehRqhzbj6_D3eLOzIY5MhtSmKwbAb9pptJW4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ بازیکن تیم ملی کلمبیا در عکسی که مجبور شدند قبل از رفتن به جام جهانی با رئیس‌جمهور بگیرند، لبخند نمی‌زند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91097" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91096" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNj1jpq7KBLdfItDmhBzwo1WlxaBqk5_oxuetzPAP_kh4mJW7xJpzTvMYPhNQ-2KQe8b9mff6V6_HW23p9diX3SZcEEj1yQWVKmLMnOubtLlIhyKoGOWI2O_XY1rhkdaE_hzHR2Ze4VGK0fkdnjbVlTI8iNojyVnt8Kby7KfTjl7kdpKEgJcz7YodDlHrEFxuo_4l6HOQM_Y1v3T_DjswkaPBaXa_uhqA5bWBxTCaJVZyb9G1s3FtcCHwsBAA2jVMcPP1zUMgoN6e77MCrTpPix3hTtVB9hFP0zebNHmwgO653Qktm2qCfl3NZtsJMXZz5-th_3DUP1SLdg6MZyebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIpvEj4WtYTtOstiBW7v7IMec8IV_36_QmRhnoRozE8NsH5sShwfhu2HrFnykxyLbwOixlVsh9kklkEz_-hY72QUeP_efenlYS1bWFkYPCeDZ1r7eJF23JJ7ZUT_L_36q55VFikntcJ_UKm1FEDLa3MwK8KQarYIa76zkF41vPfudD9ngqKXKkpRoa2NxbYdzayQQnxWHYAnznm_2NwTix7zEH6fYSnmmGVkVopvf3t2NerbJSViCJijpWO9vST0Ys-TBX79BNPDY2OOshWwI7dKsHRQ48W9aLdsF5hGIEenvGT528-D7loWjVwtSd40Z8e6nv3_SeVM6B6bHOopdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91094" target="_blank">📅 00:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91093" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOnDKfIvzhtN5kYUPXKSNx_KDfatM5D3h9g4SNosXl4GfshLkuFkKuQ2xE1woFGDe3n98wYD4JI-KbA6z5z71fdT7OhrgPuKSIuJGB_0AO36jjqPrdm1Z2AdMh15eZ4fLH16ELmkh8IERjqtWIreMUTuYhCivwtsiQC3bISoBUlnhAy1ide986ZJ_7RvUITPovbMAqLlxrO8TOXHpPEjjccSvuw89FLWzdfWrvXQBOgD3DBrp3eWfVwbJWMBuGSq2bFVsw7Y62BxXfRBsqxp3X7VwHoC7jSPsK_jtO0AhERjaH45wa8bt2GVkBIpkOK-WW6EdrTWM_HLq-2SmN_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار بهترین بازیکنای این فصل پنج لیگ معتبر اروپایی در این فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91091" target="_blank">📅 23:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP6WRaUrEuj6NPp-6o6cexq-UIrwY_LvPsLRzQ_rhVF2joBxdmVpqlqhfPzo0BiO1QswcCJPjEic5gaxkoQIQSZuvKfpUDZGp_ON7eKFZX_T1QV8dZ2_qr3dtVnYZL5acKJ_xOUoDTygjafBroy89bjUVlRfd5SJMsiDokYkZ1bbDEAExgYhMJWcVxyiTE9Sf_sGYl7WuOop3Y83f0KV3Ek1M9yCfiuefIXlssmOqYR__j9JFTB4ferKAg5it8YyWudTHeJYuHmvpkLWm5bvIkZDpMqS-cnoHcfs25WZSZNvbj24uwT4xwMMHcnzdwpWQgKQnZxwmFJfot3vYaJkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91090" target="_blank">📅 23:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎙
تاجرنیا:
آمادگی هر تصمیمی در خصوص لیگ برتر را داریم اما اینکه لیگ را نیمه کاره بگذاریم و قهرمان مشخص نشود این خلاف عدالت است!
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91089" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده:
امیدوارم فدراسیون پاداش بهتری از دوره قبلی (حواله ۱۰۰ میلیاردی ماشین) برامون درنظر گرفته باشه. ما همین حالا هم کار بزرگی انجام داده‌ایم
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91088" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=D_EBgmbyOljthJR6ZFOCR6IOO3rdjwmbhRL6s_HtX0_WPMy5BHG29ijg8jtcuOpoESfDCergpqsew2mr9UvqOckREH7pepII75FTzG7EOnNS6xJFAe2IfWCt3LBzJOVnxHSQEd3yQeQ_yHG9328mufGBF6ypjYeP2vbf1EFixzX-cNgAozPX3DKJAGMZ_MEyUugbXQ5twKZIE_HeD1xtvPwIhDk6QHVJAPjDs7Yqk2TDW_wcoGuzKRC4ZG8VGZSxi9P29t0keNoBzV0fAE3S1AzGKjf7rI8hJQwMkBIVtr7-999sP_QTtyyYk52h_MyY-5YiZYOjvMQvxMLa96lC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=D_EBgmbyOljthJR6ZFOCR6IOO3rdjwmbhRL6s_HtX0_WPMy5BHG29ijg8jtcuOpoESfDCergpqsew2mr9UvqOckREH7pepII75FTzG7EOnNS6xJFAe2IfWCt3LBzJOVnxHSQEd3yQeQ_yHG9328mufGBF6ypjYeP2vbf1EFixzX-cNgAozPX3DKJAGMZ_MEyUugbXQ5twKZIE_HeD1xtvPwIhDk6QHVJAPjDs7Yqk2TDW_wcoGuzKRC4ZG8VGZSxi9P29t0keNoBzV0fAE3S1AzGKjf7rI8hJQwMkBIVtr7-999sP_QTtyyYk52h_MyY-5YiZYOjvMQvxMLa96lC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی در تهران بعد از جنگ خرداد 405:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/91086" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNtgjoI5_hRyepjUn1stFLkpWQhCSjbzWZRgDVIbXG6DvgwWL_iDmjFltCTQfN5C0EmbPo2KoqYvThq4Wp9xCNZZZKCjucB51fjWTEHwNcOfsNvVjLVWE6y6wMY6tp088QByGU3KNR-yFviuugulbeINKpJ4iQhaPKMJ1qdKzpmwCs-qN1AKIkyNIBRFkDTBoVNzXULqmjmfPFpGNAcghP-a2FDWXwCNT6rSE__Gx1f5SC3gWl-DZTxOJiYj-M134WVy4bkv4ooYvpgjCDcJzj1tTbUKHGb-okeVpeL1utizSO9p6u0tPXaufMn24NqipstWC8CMlYeiB4-8ruOetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/91085" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91084" target="_blank">📅 23:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGBtkdv-VlQLCqo42BKCARb4vKt-4gzJ-_GgGbaWCm2Y4UTUkhYkZ6CuFYGwWc2T7XYAV1X_jupDLdm8F-vUrsKbUoOYzb-e1-KcERMfr-6LfySkmHezZD6eV6pOfzcHuGMZLDygcINp_4DfASkzatpqHYshzsxv5H5IjH9jv9wBGwPyNZlsEI-8da9_k-mRBY_wYmBhjU3YLRd9lQAo-TcnYPMa4V_QHm8vRN4sgiFrsspipXsnOWHhSsBPTeMs6RkqF6MxpvCK7bDEouFjIdUn_j42o4EeKELuQYh6d9fyLd6OnBUQw2Pc8nRMOpmUEXwe2s3YpsZpKbYQVeRQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب بازیکنایی که اصلیت فرانسوی دارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91083" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9xZOkFeVfj8hA53P3A_aVd6xWJK72tKUgE59M3DYc8q9ToyuY_R4DRSphejHRy3NkhLrqFTrUYhGvPzXUAwWZrYn_66S01h8WvzVhL3OOE3J9fJkEJjPH7ZpGK2cRWbts1Rg_iWq7Zq7NOLkiARb09P_YKijKjO5WGY9kJtN3iY5j-GGyAYFwFmJAHvZz4KLVCb7x5rfRfVKPEmNhinVbhlZCXt48lMC8ltQKO2T7RQDYE1g9O4mmxpTsTkjccueG6CbDD2BO4f-_txAgbU8meunJecm2hBf205Ig8cP9XXrTwWOXJdQ3NH3JG32-cM1eMd867-N95uDu7wesht4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه تماشاگران فینال چمپیونزلیگ 2026 با یه بازی رندوم از ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91082" target="_blank">📅 22:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-QQduZvDZjLtAPJZ2tBVez2rERTqi2ZHrmhKdl1h_1G8hbzLwfBVOAvfmBdk7EJFwJQRia9jROrAiaesPHpFlFZH5f_A4UWFIwbGrWuSuE_FSOK0yCOmTmhrC5BKl7uRxxyetw_C7dK_CrYFeoKlAsbbKz8flvThSMIOQRnVL1gvOkMgurZIkJvRiZywXgAmmO5DAQoWvD5FFwafCFFGAgmC28Lq1e52wFOtbYFnSmoZsUfQlkCmnWbXZm0LH2hMdI3SjdRcVeT9HFW4hjowx1AXmJEtrWnvztMF4LlHzF6FE_I1nQQV1mGO1j0nSg1YnoYRGIPUmU_hVFA1JEYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در ۱۰ دیدار اخیر خود، شش برد و یک تساوی کسب کرده و در سه بازی شکست خورده است.
✅
مصر در ۱۰ دیدار اخیر خود، پنج برد و چهار تساوی کسب کرده و در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر برزیل  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر مصر  ۱.۹ گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۱.۵ - ضریب : ۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91081" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRIHy6PoessbGiraM5lXtErrjovImjbgcB3GhjJ2Y6ARU4CXNCJzoJ_D1Ow4HAy_p4ilTowMc_hyF1gaPI8-Suof3X05Y1U0YHx-d72L5XCSitlQUjZvlPPFks2cCgkFuS1Swn6w3z2-G3PNuh647aKk7Oe5G2lgw9vf3H932OYtfGQJ5svz1YssDsjuvsaGob87E6cNO_w0jaarnt9atULS5Ggp1EWPsF438cqdhM2HeU0yRNGC42pnUa0w7Sx4aM1F7xvuAuMH-uHsGJZs2DTLDHgBoSYw4naM0zqaiBqNrBhsYvttVLL2hdE9b6d_Oj0vhrRo8azhPwOM3zDIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی: اصلا منطقی نیست که بگویم من اینجا رئیس هستم و دستور می‌دهم چون همیشه درباره تمام تصمیماتی که می‌گیرم با مسی صحبت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91080" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3J3NMcq43ShpfjvzvJtmbDtOAkb1QbFj-FM1GgEnz5uAMw1yhKvaohAG9dbbh4XuAzer3iREJ66IdJjWd7QuSqLZfi1SCmJiMr_eudw9yITn2beiqE-EREivkzKwcmAULg6J_B9UxqthPf85RUewwYEs4E-43wJuyMSd3rtNFPfSSqsxMHoc9JDT6LwiN5w1yn_OE4Bvp6Z0PzIxmOfsg5UGMueJxBKqu46rfOGzDiFTiAoa0wCN0abv9U1XQGBnofSTyYTOndk2t0VzlGOUMPf4SFLBjIjrXHJ-JBPGAISCB79EqCg5cdd4AyG9RQiOnREWOErC9TnN6yuku0G_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فعال در جام جهانی پیش‌رو:
◉ 13 گل — لیونل مسی
◉ 12 گل — کیلیان امباپه
◉ 8 گل — هری کین
◉ 8 گل — نیمار
◉ 8 گل — کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91079" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=sfsrQpcn9OCRt-JaEbodHJhCm_Ak5UjCy05ApPBJFBQAYaH09AXhZClO-baPFL3yStP2jx7WViNxzOo9cSaOHyDmK2etlu2Y_ecPXCl9Wz4mihKT1IuP2pQj9NxR2zoDm2glw-yWoOlqi9N8yANFrdADkxTsJCWXHQPPK7GM1d-cJ3rxjzUwRkAjoUGMHeRjxwdA2d3u1jWKMIM32xSdr3VIo-ikn3W2EzvuFkxeabS9_AC2I2cWE0hY7u_JE6rNB4BOMB5BWIx3W7-ALhjS1WHj6Z4S8WG8Mhq-XLdKONQA3ecLxWVAzpq0v43439sAvgoMkUCk_akTtbXU0ksT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=sfsrQpcn9OCRt-JaEbodHJhCm_Ak5UjCy05ApPBJFBQAYaH09AXhZClO-baPFL3yStP2jx7WViNxzOo9cSaOHyDmK2etlu2Y_ecPXCl9Wz4mihKT1IuP2pQj9NxR2zoDm2glw-yWoOlqi9N8yANFrdADkxTsJCWXHQPPK7GM1d-cJ3rxjzUwRkAjoUGMHeRjxwdA2d3u1jWKMIM32xSdr3VIo-ikn3W2EzvuFkxeabS9_AC2I2cWE0hY7u_JE6rNB4BOMB5BWIx3W7-ALhjS1WHj6Z4S8WG8Mhq-XLdKONQA3ecLxWVAzpq0v43439sAvgoMkUCk_akTtbXU0ksT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91078" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
رویترز : ویزای آمریکا برای ملی پوشان فوتبال ایران صادر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91077" target="_blank">📅 21:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNxYKnD6L6rscDF-O7Vd6ZLQ5B2n1VisKAvhVE1a4t3Za-euLnn9wcjPxelzQa8sDmCY5L_zKVnXGsBxUziKK_KeLub6p7VAEEKcSaIETXGyinZ5ZK3ZhYKdHBPC4bu4jQO2y-wbiDqh-0N6Ryn97eVrmh-zHdzrQ8loyge2LazeJfsAmImoU6HS--s6kBqWO3NC2sjq8GNt6fPwrkfEF3spbbUWKplzMahCL6xK9qzHoGgER0oG4hCrzN-oWBRVfYk4MrJ3EQ_RVYfw8HvzPkAqAVVbSQtUsLIvtj8X6uBPHSO4MnV0T8BciHSLQj1gb-JIlQ53UYDMVymKCuHWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک جام جهانی هستیم و این پرامپت جذاب مخصوص کساییه که میخوان همچین عکسایی با کیت تیم مورد علاقشون داشته باشن..
Ultra-realistic TV broadcast screenshot, identity preserved exactlyfrom reference image. Young woman sitting in the crowd ata(اسم تیم) home soccer match, filmed by a live broadcast camera.She is seated in stadium chairs, leaned back, looking off to the side with a surprised caught-on-camera expression. She wears a (اسم تیم) home jersey with jeans, casual match-day styling, relaxed pose one arm resting on the chair. The jersey should look like a normal full jersey, not a crop top, not rolled up, not tied. Around her are other fans in stadium seats, blurred. Keep the crowd mixed and natural. Add a scoreboard graphic in the top corner subtle broadcast compression, digital noise, bright stadium lighting, and imperfect live-TV framing Telephoto sports camera look, authentic televised soccer crowd shot, natural skin texture, no smoothing.4K.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91076" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
انریکه ریکلمه: بند فسخ قرارداد ارلینگ هالند کمتر از 180 میلیون یورو است ، اگر به عنوان رئیس رئال انتخاب شوم او به رئال مادرید خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91075" target="_blank">📅 20:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=BJIgnEHKhcvFX361jFU6okeY0-N9WhidWQhwmSUe7-kqBnSCGQzS-de7v6tthUdlgOFgNZXBjtnPDJUJMXkzny0RylJnbnQPYy5snuTlv-giJcnj1wKizff5-nSschi3UydF6FACpcWIqi_qCB1apzGvJhBCk4g5cxbPKDpyqv7oskbxkaV1yC37RXXLMpMcb5xpCbYMw5Rm4IbbJVZr5KCL6dvJdTCGCyGokFUOADUtRAuP68LFUqI7QuxhtHtNSwCoHozjf8nYzPsfKnnvD6Vm3mzeSrx5UKlCEzmVBD_fALSJ9PJdH3Winfw86p3VFej8cIy8Zxl9khoN-buCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=BJIgnEHKhcvFX361jFU6okeY0-N9WhidWQhwmSUe7-kqBnSCGQzS-de7v6tthUdlgOFgNZXBjtnPDJUJMXkzny0RylJnbnQPYy5snuTlv-giJcnj1wKizff5-nSschi3UydF6FACpcWIqi_qCB1apzGvJhBCk4g5cxbPKDpyqv7oskbxkaV1yC37RXXLMpMcb5xpCbYMw5Rm4IbbJVZr5KCL6dvJdTCGCyGokFUOADUtRAuP68LFUqI7QuxhtHtNSwCoHozjf8nYzPsfKnnvD6Vm3mzeSrx5UKlCEzmVBD_fALSJ9PJdH3Winfw86p3VFej8cIy8Zxl9khoN-buCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
وضعیتم اگه یه سال دیگه ایران بمونم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91074" target="_blank">📅 20:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL43-Qin0uaccOAnrg8ljb7nwt9q9u-6cDT10wl9p-_0lEnthV3Ll4B22DO5jO93Rhw29mIp_wnROaQ4eTyBy2oyT4OvbFlRT_P-i-ImfSqQVO_xU6nDL4pbNhfWxEsFJanC8aI9UV7CzkzHuS42QoNLfH_WkWFJARKYBrijbEkw2Wc4alLzifayk4BT_hVClUhhm4yUAjX_fvQ29FRGu07y5MuQRc3oloEH7xtuT9OS3Zs8ntwrCkorRoF-pIUfME5iF3bBSm6O9svQ-bnuGo_upfz82TR2mxipWewTI2FePfEpgtC71vdRu72gsxhsnXElCDQLuM75CYiZbAtp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNKUYynMF0C7swtmNo-tsGu38Ww7HID47W-sPvVu75f2nNfedjoFJw3QjlMAphOuyZni-ENvAN4qQN71LbBilwp_CCNPWAwqSckExl1POP5qaSS7kbV1VU1u1GB6hwGVsXWmpb2OhxluSRHom2qWK2-8VkYrj09zJkSDVTLgaCzNTLWw8FWfik8iiA63rYfpiKNlUQZlHavhzjW13pjrpUwzD1MZ9QYXQ9XNtPrCHozE05HGUJtT_08VjfDywB7yRpKqbUuBqL7sRHZPA7CcNbsow2QbjNQGKNcLJngDGon96B-QeCWA2oCqsD6Wula5Qgn8DdlxBD1XJLM25XgM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAKW9DWAMkaRIJoNzbsDlQcMu1iT9oOvfh3DDkGeaH4Q9MaJzNGdh6xtEX96ErJ4i5tDjYuteU1sE3dxooQfoJx7s0igZqEqTesW3BpsFYvFuwKtjrHwbqk5XKoDTGcwy-a6ho7BGMs5tgzeX3ellventb2EJ0iZUrTTFcZnmbiSRGQWPdCK1iID9kbqXmt8UwK9p7g3DHxm8lf1fyMsEUV4-YQPpR27DNoUGHRxrP4qaZuXlapmvdPGktiyQLXF0mBCN1Cb8nNjW14_U5Ffdt72KupJtIT3Uvgk5fk8j2ybm6I3utn1e7vSJbc_CMSQroWXvnI6oCrEMRTzcxOaWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzJ1ga53H389lH47OYbi1459jJoLFxDK0Vo7mOSNqLQgfRo0ijduG5Fe27sqQ4BJELr0J5f6diaxylrdI_mushFAI7rPMfY82YMuWqlCJBR2mz7zkj0LS1AgjnnNG9tQSoyu5LOmXJf5tUo5vKhOdpaP0yXigKaGwRRoV7JLzbEjKf9uYlCjjKgx4whV3MDfRmeG5X2nFr3tHPt7xSRE3_CNWCGNV5DsSgH5zEhmqfKZMmIzNWJ3JrDRn1bT0jt9x4JZS3SrFKSIFv3aWJlHun-VKnmiRVp0UUEYOQkzamje0r8jxIy8xGb5wShaGWLPpM9bf4w8vCrn4rXWIbSlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXRFjJatW8fq-A9QLKoh1tRs0-LEryA4W-TorPpw8H-rm8Nco1dDaQKuAChwm1_o_dA66Uny7fTkHMk9b12wGdyn-g8XHz95KsQtlYCbr4uGeIgNKq_c4AXBssKkOjD2qAnLXnPIYC1buL9Ic8cB9AT8h-NZH1RBEeuSgIxDQQ1DQ9fpZ58QXu39n2bUxHfyl4iIqa7aNTJRcHt2fby_jF4xtWq_akAjn8_fDDDNmb1KIlInux7dPna4LnpNmE9yfa7oyrJI7i9rpxnFSTVYOmTAWvkF2fRMiFKQ_8WzSZUu7xeMMWH7dzLZGhG774kUToDml_0s_-trqXSYynO-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egiucDCTQwvpFtUFEIETbJ-WCJ4NrB_vWHhe2XDO2Va7sMOu6Q91mzaaTT5-k5zZn9bwBtyJJt0MWij_U4zvJBPZyxhV88DHXTmJrDpaZYtaZ024d5W4UxhJAzbnMRcixW5yIbeEv2WIN_hqoB-5ZeBUNtYXQHGGDaWarNYlqt5VErEFSth-2M7x2V1LESvjmwid-Ei03FXgYSRsOehUT3XFRJw-qa2EH9VyZCXsGpPh3kpL1NaUQz3S_JTIUWY8Yf08FjV3DQ-aBgf3o1FxsKxZvcYsERM2gPK9Sjwy36ucxSmALMBkjTs-zGvGXUA9R7zIphMtwl_LpARfLF33oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzeNLiY8l1m1WOw9akbaOrIsdpa8uwWPLxCwbyr23X8CXhPORGQ00ZDfUxE2NSHeCeKCeVyi74zhQqeq8bz5qGv-YeO9LzOFzphCUSlJzEPcYbETYP0cm0ryoUVHD-EFxLHEEKasCvv6KpefvTEuTGl45nPRxIsiKCqND-jNKz5DEoi8HcWj2hYkMLwbEg0lN69dt0ObBf3ZQr9ttE-IqGEUhwX2UUvs9X7ezZaLLQXKOrW7WHQxjyF8flI-AKgQ6nbKhPlEC78POLgmWyxbixrhCoCvAGZEiJtLIX6YeVU4PsDFzJL0QdUUWlW6VBYFWCrohvcgDh5yyN4smrNZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8Ec2jsPyhb0t9YJPsSYbmrumPaTwt0ZDblIAHsV6Z7HnvPjbMiDeJbBtbWk0fe7JLVmXBk9HF3kYtbe6KHhUgGQCtJBYQ4TCnPg5q-EAzoik8A2yUy2PumX9TAFquQVLQp81zyDu03kgGbalyN2-QMSaX-_NlFljBpRxbLFFFhJhTx3lwoOzXvHSdzoH5aKrrU8kj9wc_MJFGUuBDdh-Nb-obTs9x2pWuFk95tyyd_UtuECnXa9iWTV7nnk8d8W0F58d0yV5RyHUR4XyBF5Zq_5lNY-Z2_u1gtYXfpuNofaRz88V1Gw1LSTapRxg2pMYK3fcTafc2W0ZRxKPGCZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_WA_GoDUVgHMPvrAI9quxItxLZ4e4RpdYMX-7Acqf2qwF-Vq59ksq-UX7Yx-z4pbba21LIHJMWGAa_EVLLwtobZJIKtAcnxrspCnU0OhXYRJ3MRfK91P9KUsj7op4ASnQlhYHVeEXhSXAZSsxUx7CjVJztfDtumuGSlQE8iJcSjiw2CHT9O-Pq5NaVZ2W2B7ygFdEgMtAr3wBlq9Xy04j64Einn3zEP7MzeMg6700gUSucPkjEW3o0-NSHU1wu1RlHUgFfrHewrRiWmRzNWs2k1YuByaIi8tieWwS4opuQH2-oFno8zxdXkOIyEPCW7erakYKFWg2ulNHk1Qobjmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNw2Z1MwHXLo0kHRe1aRNDC04Hu2ggV0wANWPgolbBsVr65g0NV2yrDxlA9lhcFF8weN50UN5xwVNRU69AAYxm8ph_9jNT4o2aGTOPLliXI-qOnBT1lnlIYHhZWpwnYnRTBe3_KEQfM__k_U7QKdGfz-F_qx_CIexkWCNktj2Dy_hn299dkfpBnd9zIET-zKvOsr0Ou0foHDjgyaEJd41BKknJuFXsIEY-yGON47f34xWki91CTHDYRtxthy1Ea1V1Sg4oULkV_-CP6eAt3ItGACjenhZfeLp76IcF0lF2LbgnxCemuwwql8Jjoz9erQ8dEhTfpmH08pkj2zKJdaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mncg_Z30a2iCd8O1iVKsND8EBAaIwIf3sMIqzuY0Ba4Ph4AqDYTHSNlOdaP4KsN8JIrlJnJ-DUgdwKwGH4GcEXWMOWVdmRr2c3LJv7g9pMdCS9QY7631x8Jt9LuEP4yDc-mYb2iPzytvOOiGCTlvsyneEoquK22i5jafUSrBskvK3vgYY6YyZW-LNIzi-bj2PRSffwxyDIejnHgXtxKWdcrfSOeRLEdqGpw53Pua0H1YFMLNKTyQtMHz62HCZ7SlTOEp_CaGM2VwWfVnH0YfZMZRInZS5UkNE3tI6RaYe6AnNQhklSWvMGpHbgSU23CpcSy43VoqPkPyxpJFxT9Fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gHF4o4YKnbX6zCraH7bUrIACTScNhMnHyOFPIjjr41AwYzO3s_Ql09Rj8RJZiMZ4genOtbf4BBnqAwpIDuSYwxzTcJIEISl45cBmIJ9XdFztMyLSMw4chHmKa-MX9_SMMVGTTlfGepIPuv4_qWzQr5Tv9bMNmEwakrnEA7n4_GYM5qIUcOcbbAkC_q6jEFpZiSmtluzNxRhPxi53_jEQP5mTB5L8x2PfULjN6vbewE_r-3TTLHHhlcRF9_0eGfbIH_zc-x_qShWQIrsk6U45ju1xPoKz59J0ZkSV6Jn4B2Bb5L0_TYdBor2M9_RGcu9LX2d_jwBh4hy7hp3Nc8mRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfvpGGT7jlcKdN6gW5rAAChVb61Kw6xyZROcg3_VaucF9RLMquoVarFQEy29AMYnIQwAcnzretcKQ5QiufivDgIThA5o7iVV0R47AAAMZUVID3iTYBCduIMEyeoNz_HuNYNZDuO0oKHOnAQSHtgu_TXCZqLHXC3HtKhrRVjb2iD2IcwsrBh0TeoHNK1IMfwAn758SUxnS7-2BQLAqJ2yRGf8kTYvh0yM0LaaGkAV6CjZfMU3wr9kgP8tJkyCdpwzR4QKxZmS0FXsI3Bnp-iNDWbd_HQhPYLD-Zzj5h09Zy8wzNujrcHJBpx6imTT3LM2t4xXJv90qRyJxSMmH5F_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ll60U1mpnGRp3ZUHwgVbtdXKgxV6tyz_kMKgYfVZ0rKs8NkTJ5PWWV_y7KAOcfhVvD_Cee_uBKu2KcfhQw7r21_LEOY3pM9-Jho-kwMO7U0X8eq_FzEQkLKnwNZATKXVkgkwxSXg6d5SC3UMZobWXqoQ7RsdDtG7RrvwB_EywP8Clevjz2UINL28c-PhfrzPBlccDBtvRulTWBhdtIP4d48IYU4JKg2poYnfJ0qbAGNwV0ZlsueW4EaA-6axG4vg8Er4lf8S1HNFECMGbwMk5voWm9Lhhehpm5or16FDbwJiTmtATijZgEP8GDc4D2950Ndh1gcqPc9SEFpxVkB_qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mT53t2P4gjEh__1EPxcMF2yx6CoJHtnbXKtGi-YIjk9mBhZJt0GyL-R7DaDJ9ItVENuJhiZKn77UsSFTI9W0s445YCOGeh2t9hYkxl8aEp0Yk5IkkTxlsaZJKE6WJAmppzXh-sWKtx6tazuM8PV5OC4Hx15A4071wIHNpYhlSvnUu8O63z3dDEx0vlt5BcJXg5CnSq121luWluBe0WTNXqj-g904MNfgFFMUT2EcQsWziG1erD3p2IJg9laDrAjM8Qu75b4d1WSXks6WLKK71jMZw38Xy0mHkb0GE-Fiv_GA8Al78KcUxA5Y2tv64KMfseZRDBMOPH72nhZvUpdNDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mT53t2P4gjEh__1EPxcMF2yx6CoJHtnbXKtGi-YIjk9mBhZJt0GyL-R7DaDJ9ItVENuJhiZKn77UsSFTI9W0s445YCOGeh2t9hYkxl8aEp0Yk5IkkTxlsaZJKE6WJAmppzXh-sWKtx6tazuM8PV5OC4Hx15A4071wIHNpYhlSvnUu8O63z3dDEx0vlt5BcJXg5CnSq121luWluBe0WTNXqj-g904MNfgFFMUT2EcQsWziG1erD3p2IJg9laDrAjM8Qu75b4d1WSXks6WLKK71jMZw38Xy0mHkb0GE-Fiv_GA8Al78KcUxA5Y2tv64KMfseZRDBMOPH72nhZvUpdNDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIcllzbRjDVoTR3ehCOM3ThNTRcRoB1Z8ZdrZa9xXtD4aeqUub8-_efQjY2gdYAPTVpBrYMfQ4M3sCIOE9mVypPYID2euppnK-AEQX4vvB06zTUee7JPkETReMN06ezKZOek1Yh1Wn-uAFKLiYwWQhtAbCoPUY9rd7lXNe1oAKP5Hc83JXdx6E-Gy79qG9eGKSCYhyjmOE2XIVW9F0K2IoEAa1kYL5Nf_qV5f9F_UGMhe5sSJGf4GSJ0PHtbCxYL_IeJ2isHwZ-96kAzyK6-70XSimzgSN5Lg9AiFeq5Vs7vw_7XjcYdvq47ngrueypt4Iw5rXL-pXeeKhrLDc0VIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE4pUY6UwSLThIfSo8qbv9qiaN7MjBUDrhR2klHh8ZI900ObQBAryE-LsTL4JHRjyVJlBry9rT-agtLDQjYYvtCdzGzBD21zXwi08P2okx43FfD4UnrVUWzjg6X8fYdZidJb9lNEe6iXE9o6JPc5AoNh-USoHIhcPqb4opUGQB_HZ-XUPiQZJM5h8NXdZ5vM-pUZnk9p0Pyxhvr6G9mR2s1-9Nd7tTR0vKIoBepMIAv8F8InlVoUtWkGY7G68fjT-s1nlNYTvk3QQDL35-DrsoZ4K51JJHyIeLWgYngD5TsEnk_ReKbE29rXoe43Nox8_hsTWiB6RQEx8UB79EAW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=RZQYJ-vKzVikX2GPC57EMDtN0ELul0Bs-8SvHaqFHbjj8KzmW3THDM6XIa7_UeN9N5qPI31P8HgxZrMPeqGRTW4itF0zUZtw8uZEqKKzGBvRPJvoBFLkn9WO3JpM4VVmh1PnhxVm__M0mB2Z12il8DGWozEeDZF45_PQy8z_U7WG0u_mGINiKQjBNcBIUS-ZzCoiZaY61Fo6jCoYDgnX66TY2UFtvbnG4xTxPe__F_DcWiKH20YBXaNwG_HMs__NoB8knopPLx1TZ7LG4dU0f1dopoCWWmdD_5DRhy4k-6VzznKSuOGs6nfOxRpW3K4AVZolwdbKhtF8s1BHp4CpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=RZQYJ-vKzVikX2GPC57EMDtN0ELul0Bs-8SvHaqFHbjj8KzmW3THDM6XIa7_UeN9N5qPI31P8HgxZrMPeqGRTW4itF0zUZtw8uZEqKKzGBvRPJvoBFLkn9WO3JpM4VVmh1PnhxVm__M0mB2Z12il8DGWozEeDZF45_PQy8z_U7WG0u_mGINiKQjBNcBIUS-ZzCoiZaY61Fo6jCoYDgnX66TY2UFtvbnG4xTxPe__F_DcWiKH20YBXaNwG_HMs__NoB8knopPLx1TZ7LG4dU0f1dopoCWWmdD_5DRhy4k-6VzznKSuOGs6nfOxRpW3K4AVZolwdbKhtF8s1BHp4CpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8C0nrR0RR3jQxO5x_8e0eZ4uGIlC6c8OX6uudbvn83U8hO5__DgZC2yJk6Za2OmALm3DvvH_RhcsSHbtPqHI2y6JkbM3Rt4OJ6KYcwNZY_tYFFO1EdyjYxA4iZeus7MW6t9uHwEKJOb2_M9Up-Ys3IL-eGXQv4P02s4gaeiQS5jNLSZFdLdTZe_HYslWR_lCeoSq8zC6gWDH1CQOjfb12lrKsepcAW2NCPv0i0XMPgKuPNdXiICY9woGp4e3OCLDDnj9iUjxQZ0_gYUoq2AIIG37fqG5nDSotYcK3gu9QurCeOHT4aVr0Wyi6a76oAQhFiss0mnrM4onMkUDxanJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=maDKdKIBXv4ky45BsK4DZOj-KTZukUkBLx6ZBpgRm70u9YCZqdzwrDBnaNM0TnZcAAEeIqiEL9Jhz3HbRM4celmMPGDrVbgeIt0xnYndpE-zrSZjT1Umznjh95R34ASmS3BuTXXBMrnQHbG8qKbjoVWEHDOsP9lhObIXtNBKSXuFhhyQ13G-PYtu8d5bBW65XQ5YCQEREw9_JaGJhOoC4oSXAHixOotS5rPJ80qio8IdK01OOosGefQd6uW0vFuxic9wshMvbMryoRkcJGXXVNxuQMU04ogS9AHjDQ0uGOnv-VnJsx1Iv5K7ksACLDXzDUisUWAMXG_qtZe9sJgXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=maDKdKIBXv4ky45BsK4DZOj-KTZukUkBLx6ZBpgRm70u9YCZqdzwrDBnaNM0TnZcAAEeIqiEL9Jhz3HbRM4celmMPGDrVbgeIt0xnYndpE-zrSZjT1Umznjh95R34ASmS3BuTXXBMrnQHbG8qKbjoVWEHDOsP9lhObIXtNBKSXuFhhyQ13G-PYtu8d5bBW65XQ5YCQEREw9_JaGJhOoC4oSXAHixOotS5rPJ80qio8IdK01OOosGefQd6uW0vFuxic9wshMvbMryoRkcJGXXVNxuQMU04ogS9AHjDQ0uGOnv-VnJsx1Iv5K7ksACLDXzDUisUWAMXG_qtZe9sJgXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXpZbUCMsX6kEbgeEAGT4FQzELgNwPsjS7386SHy7NetJmHyVhbLziN8CtcT2Cf0Aq_FvT7yo_6mwORj3oD5KhdcSmLdfS6Ryyokx9NC4YrN549qBgCw0Qtlsn2jdEgk147MdyLKg9GMULIEA7EQ7Bjs-ytpNoDzv4tsFUfga3pNMVBEVBEQs11rFiMG96dQPz_9S7zN3fTLnK0O8K8tqc3t3NYB7lxooawgjCB4G7p3Tdcv2qSZ7ABkgkg33tsSfx6FwktFr3CePWhS9UDvbHVorfSyOpGYOmYSi3Z-tDhrJMp800V_r-zhIBVxXTVZPgKg40nu0m8mSHBLTtSWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWiHPbo15xQoc1XZV3vO6DRD0c7bTro4H1iqOx_xYVYJkeBaotisKRlCMrFWxIS6WErnQhUI57WSzEYgt8GxxRYyZLs0SE4L6PbQEQTITjMVpl1-O5G7dFSw6CrPOqK_Sx27nkf095o6wAJHMMJDxZadZNSSEWfFxx4MoGAv7vKVCh-Wd0TRl8KYEsdNoUhqRZs_en2YK2nq7OlgSqzn7WHnQ8gEocEM-QkI-h4ASVLmYFJoYuDSO7utTMpIJelQsXawiVzeeTQQoUuN5pmTSI2EwPksV5LacL1a_C119PQe4MtJ568v2F7I0IbfIb42-t4qiazy7tvANqSKolUwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5rk76yeEhoHPg2Lx_4Vdn819SfRTsqQd79ootFXPf1l6MIv-9PClx5rGPTowovBpCrL3cstyPybR4XTzj9WjHEoVn5MZLgKnwL2YsCfpUJ5uB7Kh6Lw8oJsd7gSf2tF37Qy65hTray-xDyaNsy4EWC5PhacZBrp2X68M9cqhPOnXJn7P5R80oM2u7z_v_r_06OA_Ug2T-lOGs_Zoi2Dj7LoT6FxlLc2HtNebNYt0wjnIOt5BrTL_GMvfv_ZM0-fkL98Ikn1azsT3JkqoA8TGvrz_rdci2EqPCPgU1iZ52NuYPzV1dQ-VxKjrVEX-aHS3O_JAJCeQ9ISN2OBpdHJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-y6rO4_wBLVYL0FbFujl9kQlXAMKOKujG9vOMDCAu_VLMgjWqvAWsY3cGsop2m1lECIbzs4U0T4yykpVFhdFMI1-oYLbAAH5div_4_Tz-MMOp1hsl3vEaYO0VbTvIqnyhzriquJ33CL_Gum5dBgF5p9ACfVh_m-59-6PWL82cx0K_KWVa760R0vmdnn0JtA2wDxxg5mQEtjsAfkHVdIwZhAT1pt1_Zlji56BtLiDB7v-3UsPqT-Exn55krEmoR-8TX8_keTtO676h922PtdEJi9KcvahDM8T7Wd-S7a8RWdfu6l0BVpA3e1Q7JoFFdpxsh_gbFLKLQInmrWULRofg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmmJYz2asTKeHup7li_Y-K2zV2zT8igWt1-uiAubzPtvBrlClWHedy0-pfXA5m2Iskz8tkqAKCjtrJmdyhKUzrKRIyXooC7VbhCD-LvDbLgqsVS8KPcWFHTQjuq_w2G_YX1ECEXYOIcQTsALtipkEfOfF1dBb-yrrc_l7GfT40tlCeWyNVkIXm5uVBap4cetTCbX-274sxW2nzTFNjsvkVuG9nERzC372QyOqGtHloJXjUDrq4mlGF2quyZGNinFnY7dSZUxRTcfx6agzJ1ijsD05twWCKdRXyUNUi0WQOpaVvEEyXUwVNPOwridbJ5wjFvnIpJBL4et4znb1GHVM6Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmmJYz2asTKeHup7li_Y-K2zV2zT8igWt1-uiAubzPtvBrlClWHedy0-pfXA5m2Iskz8tkqAKCjtrJmdyhKUzrKRIyXooC7VbhCD-LvDbLgqsVS8KPcWFHTQjuq_w2G_YX1ECEXYOIcQTsALtipkEfOfF1dBb-yrrc_l7GfT40tlCeWyNVkIXm5uVBap4cetTCbX-274sxW2nzTFNjsvkVuG9nERzC372QyOqGtHloJXjUDrq4mlGF2quyZGNinFnY7dSZUxRTcfx6agzJ1ijsD05twWCKdRXyUNUi0WQOpaVvEEyXUwVNPOwridbJ5wjFvnIpJBL4et4znb1GHVM6Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هازارد، استعداد سوخته
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91042" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Wcf7Fu7PtYFYOeX3-RUNelCX0JukS_5w2gON_g6p31ZgLWZm3eF1MvU_-JCNXu0GkKzPsHhPosD1vQAgbUq3CJK-wWgi0vRL89HxnPxmZSb_7PgXNEsYShTEV1uAjMLwbOKYLsPAar9kjQ9q0rYPE2AgRhrQwqJ3WqOs--Msde8bqDj6fCaYhQbc9u3fLGAABoalWsAGNpVVSjwEf4gyGfwt_cx06CxdQkoHerv_czmp8qF7NVYGzIrzUgam2UbOepwDbpNtaQyfrJ7THECw8CDIgdQsrXd0IEq2OAdcSshV_vDcS2v-MnosPBoq392jeUKwxHgm2PIY1S9AN9LGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
یامال به عنوان بهترین بازیکن فصل لالیگا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91040" target="_blank">📅 16:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6KA3AeW9GancC4qUc56SYvrjwFArAdvwciaEPZNQ7uaPy2A7MP6OVpiL1XlGK6QGctxW3Ce9p4pDA-lI_WyMtasi5ekQUljOFQqiGvvDPV-N3O_-OpQ7PGEyKcfnhPjVihABY2eQ5dXbAZcLYajnm-wNNRaTRsnA0CjTjhYvRP3Jvo4T6Po6Z6boM7gWE1YueOTidQCZoXCxRdvN4RzuRpVt_tGe4I74ZLVdXpf4vQ1Ii2GyXLkqWAsWwYDzrbcCoVYMOlG-8Cp3IRjS-1qCYaJsk0SqgpKir4nbFveEyeCd902DP81ZpP4FrRnQkT6LH1dLMfyK8WyVjJ2XDURXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فووری
از اسپورت:
اوسیمن به بارسلونا پیشنهاد شده است با این حال فعلا جایی در برنامه‌های بارسلونا ندارد و اولویت آلوارز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91038" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC1OXlftNs5302TP-zVT15BeAboGcCfw9SJVudj2k8I14ElKIWjpA21ZKFjmXp8cpK9BANWKCQc2MiPWuNPzr1fVa0nRIjj3EKsuMCaQA220Yd6quCnwYcPnnWkHPmTs9kk6S_BHrf5i5oQFh0V0YCIRge_jSPimnVCOJVmL_fp7KFqn9DDTZ041_SBaZ9X9bcOBKS0Jj6EHbPFpGRdgYqXL3wZVBWEpbui4oQJFv9GHDWWKQsYJcaVdHcISJvZzOeZX9E0uUlHWh5qbfVMs6RWV7LEVvZEkSKpkVCuDfl7cCbWIhMaRbFFZgMS6lIoNlOBvwIZS73b0Cj69IAfA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه زمانی حس ناکافی بودن داشتی به این فکر کن که برای سقف برنابئو 600 میلیون یورو هزینه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91037" target="_blank">📅 16:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg6tWfm8MnBCz9i3WCErJRJV59oEqAuMjuLR534dErdtw0dR5w1quNHc7RGG-Ecd59eXPbj0qFehM2-k3Pw3_aJCureSsmGCjPoyJR9DPzeyAAph4FEoCXTXNcC0v6ACy0-bBcqx3KdsiVDPyXxy4Bg4lcfff5Dho-y9BI0IaEGRcIf5cZAIh-kBAstvYqual6yq1l0bYrQ3DupjGbveMOsr8j2nf0tEG9xoSrcULINyRD0Qvj39HmH4PceYx4RkGs-v4xnpUclAL5BkZXcLMezyMBpfItzMrGmcoPOS9AqoFmdV_quoSXFmpuYM8z--zkru8EYs3ZIs4-HqSj225g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل لیائو: من یک چالش جدید خارج از سری‌آ می‌خواهم. لیگ جزیره را با دقت زیادی دنبال می‌کنم. اگر فرصت بازی در آنجا یا لالیگا را داشته باشم، واقعاً خوشحال می‌شوم چون استعداد من در آنجا شکوفا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91035" target="_blank">📅 16:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01837206.mp4?token=JGdBIUVQxD254EzKbatObvkrJkuYwSwYu3DPxgLTJb25gooB3p4TwpF6xlCHS9He2oRGFsFjpWkV0izEC_urISxq1_nDvL1Cuy5r1oNt7Ii7qGWmhKk95b75hRS9oi0NC0TjjTNERSj5_v1CTk-CHI3nh_ckcewsyqcMJTXZzLI9RhuPdIlm4rDdHBCP1CHjwHHmlqd-e9UZ6AI3bal-HxhAI644I0pLYolWIibXtDqKh6c5XuOFY-aJr3QRUmCHeYvTT0-iqIecLq6qkwuyjYZd_x2je82RhTKC6ZG8dk97lFVyzjMmz6i_dpse_OPIC9r_oiW6zwCkbhUC7ViVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01837206.mp4?token=JGdBIUVQxD254EzKbatObvkrJkuYwSwYu3DPxgLTJb25gooB3p4TwpF6xlCHS9He2oRGFsFjpWkV0izEC_urISxq1_nDvL1Cuy5r1oNt7Ii7qGWmhKk95b75hRS9oi0NC0TjjTNERSj5_v1CTk-CHI3nh_ckcewsyqcMJTXZzLI9RhuPdIlm4rDdHBCP1CHjwHHmlqd-e9UZ6AI3bal-HxhAI644I0pLYolWIibXtDqKh6c5XuOFY-aJr3QRUmCHeYvTT0-iqIecLq6qkwuyjYZd_x2je82RhTKC6ZG8dk97lFVyzjMmz6i_dpse_OPIC9r_oiW6zwCkbhUC7ViVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
🇮🇷
یه هوادار مصری اومده به سمی‌ترین شکل ممکن ترکیب تیم‌ قلعه‌نویی رو برای جام‌جهانی گفته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91034" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txSy8nyX1cxgPYgteIaLGMnyBP7VVWS3l-PwuI015MSihmtFlxP4aXQphDVp7KigJTFpVi_VK2j5u0EYdgyJYHNjPWYThnTzK5mahR3EU3d9Hu6AWMQ8CIpTe7g1HsVKFNu-ceM3HUe5oGUOBCjIgCWZE4n5X3mKc8vDZ-s5oDntDks_GN_KB7TPrp4RIju_WprK9hNVLYJSMj2na-jivOi2oTVhpX9FyHPdHuy5W7Fs-5paBrURqOGO8GVpECnGF8PLtNHlFkGsonnEgRXmpyXy2DpmljjuKd8C0mgnqMxsWEG6ruUmdJ0WMG-vwC-E6ww3lG_u5eu9_aCndw41yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه لیونل مسی در جام جهانی 2026 پاس گل بده، به اولین و تنها بازیکنی تبدیل میشه که در 6 تورنمنت جام جهانی پاس گل داده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91033" target="_blank">📅 15:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUCD40Sin8e8sQYIzEk8cMd-GvzMhs3Kv_cnNpjyIbTj_te_lh7tF6P1QgSctRMYS8ofNqUoXq-W4o60vVXmEHWVqJ1MFS8CavLL1fILCGTLA-kr7Hw5RQhKqaHqVpokCnGmNAvzMOqyzJ_Vs0EAxNGtKsL-m4MHLTFlWoUeavYWdmEhshwvRBynrLza853fNJJLwaf39eKWyirDR_51V6J0XiOZ4-OG9hZbku_FZZLo9pTpwiBvul4UvoAuwNk4Tmktx2i59yS7lCifOMpzwx-f_7ixOcZO70UA9o7r4w3rNihii3WzjdlrCPtr5ydn9Kr_--a_zgZyPBJaQSYtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی: اندی رابرتسون رسما از لیورپول به تاتنهام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91032" target="_blank">📅 15:38 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
