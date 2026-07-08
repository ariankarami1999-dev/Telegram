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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI_mTx9ahU6HEAXcF6f0dn0shyaBHmyrzxtwg-x5ENXYnsALH4ynIevsuZkhkvQyeVCJ-JIOB1BddumF7EdKP2MkHRMUnhT6whP3w1OLNQBfMi6-FGgm80wLwb1lSxg3rTg_4q-VXHZUXsdsX9Cro63V-Rfx5h8odc1bIYR3rWS1LiP8repImy43r5Ib0kbeH5AuASSCCRvj4rLpkXCvtbU0BVxCejU5VcHiEssvTtzo3Dtj9KRr0fUf5hbQrxx8SfN4eRXW7bujw2aRvezkvLMIOWzG-wud-taWdSnijG59_i6Uze1CwW8DRgW5MZPPBc5ehyO3aXFeD-RWodF6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP4q_76sVGT_ZoAZ1maLVECSgDr9_0zTVMdwnFaWpivMyxVuN4swUW055Kz_F5rd4k5R2wy-MbF2rl0T2ysGMlttDHLpPLk7dXxHUkgeZum3N5f5-qZ3DXaEZ1UpA5mlSKTVm_AF12QUnQl_ZE2AGeWfD_gq8P3c4TC0dafj_2y-2VOcusL4UxOZ6mkeOMruf05jUTey2qB07vRqaE4JlnSNRaXsMSX2bk_EKCnaM7mtmAtoMHJRM0f5I9GdKd5e78TwfkY4kVcyOR82ckf7kBrmS7SpOv8jEGnsh5dO-4sf2mhBpIwddJrIlwJxQqCJEWMTTEdeKPtaX2HfptX9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlIXDYc-EM-t8KD7BXJ4cAM5FsFCh_LQGsFUE2Ucbbppt6HwthmnxmXGsUMoYFf4WJmpFtZBUrR-3THhoFWOugzFG99ceXq2T2cQFiaqtzbQGJfW-2M2d_mjmd1TEF3k-qBB5QD_B-Zesk9jE6IuXb5-lWo2PkdXmizcP7N6ImvOlDaI1a6tjLTUDBaLV3MDatw8Z8UJl-A1BU6staUF16wNp1xSAGNo8XgNs1edUrOOHlTxcu6VFRrChtgR80rCKbURFfhSFIiTGtoxRRmkL90XewojZLwl6j5CN23w7UqzSb4CyqIdrjruP72_ZxZwjlVnd8dVpmWEoFtiGPF79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3RjaDhqtg8Wxu32_jJ2MEcsF2cTz9fLXBzyPdNG4mGOn0IB69MUE2jMZ_eqhx9S6w-T7ubZebmTI_-atRBrp-7PjJwTWBSds0Qf8w36cRvLS-9-PUXfBTTCCwBWgM1a8OQjbYvxrHEzgbsxaUQyWMGGj_FZ6K3VASdhgLXl6q_dlg13trpw97TvQXqlH-tzykvSBofJV3Q1n_-9yJtgzlXwD3x51atL4SQ-ekPf96u9cF7cgjo7TP-vetFREUY78S445QxC7qepdz38g4oVFc-gw8WklwzSlD1jwGAJd6P-No4uT1PJobVdNKes3rqC51TWBP-4haZ94IN-h5M7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQEuqUrnLkAVOOBUuxJl03pMe8gTR95BU3qrRALI15uKYhCoF7Ej5zyOKopTSmmIIt5ky9taMk40PDzSshuO44L3S306lFfzwUfNaCqJxEzW92w0aNkVQMLemt30GMPAM3K-GWZoyljWaF2Yt67_2E9TZCcRc2A8bU7lTszimDaq5u7lUP1oaAVCEagAIpJhaXR0UYKExjdRon9rqp0WGII3SHzB6Y63Le7L7wIuJL32pYudBVauiQNayQl6bfDJl3HR3-2tOu57AIje86RrSUkCmGMLLhVFr2H1Uvus3_KVR4-s2gLFZ3k0iBZS8F-BBUqTG9HifQL-UEIWhSGXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7-UOeWJA0yiz7x2kQLrm_yZ4xT69f70umKrUnpwnG1c6zeE3i0jcK6AZoyNiCTIyoakI0smZauYFB_K-etcG0e3--PuhYdQXkbRRejJ5peoKsVI_zhGjD1CedW43UyP0f6GKzB1kpqnta39mNzBfssz4Z3v2T8YNKKEUlR1ndXmn_0NjbLHezSon7UufzVVMbM91Fkmq8XMDxPY1Y9wZLx0A34mLj1J0TGTW-63XuXSGJJjf2mkIEevjqc22RswzZt-RnWRsaLlPhcNVvF8ERWm_Mg_ZT9M6DH5QixXupVrmFQqgEkB-Regf5OoN17EiQIajx2XxIYEUmkH0S8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btYw0NczwZYUmkYN74TbDUNn1kX4Mbb5DZjxSqjTpurx-e20-2yFgl6kssbV3BY2tcga5ULwlaxmP8r-gMyqjgy_aVGJ3qU1cGJnEBWJLOXLbyZtthZ0Za25HbBXlZlzKB-o4p26PuDLoxtctH4-8St1XmwPWM8R9km_DlO9MsjRdO8yvMUe2Hz4l9YYFA3B5sO1tE0tR7L6g151YVKdemRlsdnhCBRsMQazaUA3wtn7YLcoYmz9JVGgx6oOV2Fuy9GsvOIbBLtKUsLLZVHZMb8WL-sPDbd-e7-UKka4Vw7TwrBSnYs-mqHduQYlf5VcZRqKJX0lAlUm88wiCqMj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFgdaa2H-cf29WByl-aBmfAkGI4sqyuX4hqxp6p1ulpzWXdwSJY3WdLBWZDJqqFKIooUHyr558l-WkFcCmkwe4ncXdGwbl8dP-CGn6-fB83eq-zedBCX7KiG7V4eZjGNrqkJkdtDAFQg7mfwTR3aHwnnqdF4p7Xfcnhy1tMCjfk-0ZaWOWw998oNs0tjWmgwX_Hlda3lp0bx1Ge9ekCsljxwkmc5o4mRt7PtGs19AUZebULpYd3u-YgS-skWM1E6vxTUx7ZJW8Jb3FL1x5Ou2Lt8kkbLrkcd09N9cxZE1Hqz6CnnMfp9MO1IjYolfErrHzOzQQr1xbG8GKuof-iNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFu_i15RVbGem7uacHCSrGVxoNHbDWoG6wsFlmMhhZqjvrCLilWpwE_TPpoUSK4zjZcuh4JmHeLS0e8e1Ch4dg4JoKG5ITw9al3ng26zzjRbHTZkGLkuAYiaBrWlQk0ZSH0pv8gDVR52E06ANOnfgVGw8zNpLCfuT_bhGocYsgM1jGGaaDKiUfTO8mds0R3SjoyE3ddN4EaSACbRE0rRPqrJIlKaShXh_w22psmZZ4sG8dYWHewTU8_359gBGGC7D70FxHIWR7x1HJeUKGhDYcbveXIEaTrGzVJZCj_Pj-tYtuiLSaf1OD9N4FN_qftwkYKM1oAJgibh60zBXGpLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXQcSvENmcRPhUU5W6GIBgqZjSpPw4qlqUcKJD6Z6Nt2y-4xwDOwQVup0gTgurw9C86Q8juEmB2JpkaqzxayJNPUaZdXGI_r4-Il8jpNdCKfDhRcz1Mb9KhOGbEidyojrbwtqAhSvxZ7iwNh0rLaZ2XcjONvaD83sRGb_ew2LUok3zBzorzBxh5LeBrqCVoZwIw9mxTdmQG-CyZGQ4BxMSgezVzKlZO6rpWmwQRXUdjOgb7Z7CzwzRIYTRq9PWkGk0PdDzczShdahBsx_7c4AALEpOoittUQB3U1gXsjGoGICyMOsZgLIWWS2CTxSgLvc9x-wlCx51NZwxCbOt1raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmLEzLfq2Ffmo_v6i9vqP4YwALoqRb0NXmvdXVsd1rz7gFH9YyD7OJGu7W7qcRV5CFJXCTcBa2rtr3vN4eHjjbsZSBuCXq0Mwef2Bmgb8yamMVLcCApxsmtVkKj2q4JCUx1dAXTx_CAp04UEerL5YBq2aJ2gkujHjyPSM2OhfRwbbZAOheNvs4AF7dyOvDXHxCUkFnDAxovmsSiYgy1hE-b4zkeLdXi0mu64HCvzwBk9w8PixKvBMfiaOslLHLpvOg4FHTY0erfzyqhUjknRXNS47s74IafN8mo2IPJ_TUNxC7uLJ6mp5Qf-v2cPLEzGxga0xy8OMr08Z99TzOw8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL4FweE67FhSd_0ASIVCf4Y0o-RYIOcVBHSLD4D10THtu7C1qnNQ1oppj9yZGfEuKEdSy11qkywJznQ6CoYmlj-lthyAQDJ6BB-IfooIQEk2TdBxRhasw_CwTlaA1uHtkp0w4Myo8CT5MZTObbxxT7j6aRKpQulOKlOQV3boJmt7mWyxICohY3fXZDsxECrrro_x2MqAc_smGm6Km1t6jb--IR9vP6Of_1V5vnKqNpkXfIWZAzh7NFqCqs7xpNE5f9ZK_NX8QyKMLzqodvQgxikjEh1q_EOqlM7SfP686MXMOVT46rSfpFepEFFkiVnC79zWPsfiC4WOdxnRoqi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASoU7LVcxUUnkYHU4fIdcQSVpbsuUr8SUpaQIUi5cQMrunjmcm3x19owsI01gOrHdaouH_reyZoTlalN45bDLziVy5O1jVub04MbT8NRELWDtulN9X7x9EI5Y2l1ksskp6g4xGYzG2uYwKgjYB8gjTEBiunwTOr-G1JYd_oUbqQ2uGM8WBabd_7iJqQ-85dYBF6z-iJn1JggXMD_BeHa07-vnPLBob3QcTIl0xOJqL6xO85hgs5mrr6xAwjcV5B1oUiHDnEluWUnhDJNQ9fnaP5_M0Ud-LR19BdQJM_WL8suP0sZCc5DdqNpEGoP7BuW2LWyCj0M3EmsuSWzDqABgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9DIiwd0svz27YWzjkKRgQvQaseeU0v6xxjntDqr5XUtD-Y_1Yk8t5RvNxvpw72ARiqsZ4Nx6VDu-opeV6JivaN70GjUs4_uelvsX9JaUqy35iTlE-GS7VNdLIFGKID5k4LjJUqmzPElLj6tbQgcf8AarDkFfSOcp4jboV2gKmgEOaZzgKPc8nSGR-wvkhEr2oKUiy32R9LG-Y5j4ut8LIxohX_7P9IV6M8Luo2eBKT90NGc2WI8iAnXp2urUekgxymL4GaJy_X04BjJxFZowW5vAvVRPLxjyzqbpOmPdrazVL03RoB5J9scIKITDgQWtXj-Gi3FrYRgVMarm48K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1V2opBIAWxDbcJ4g3EJYZS8QkMzxKDp1MQNH-EzUFPoK2r3rHDqtzPpbrkP3iLj7Uuvrrx7lgF8VQG3bMEgB219UpFWbQZtKiH794SygQEUkky-fH-qjelayq1h9TblVicTL9MhSdDIgd2RIjVA8AfFzbr94dpYKxkc73fhB2l00c-dqXqO3BLKx9Cl24BpNVQzemMfrFWEh3eJRP6rl6nfFr-KC0-BxbYrG86S_IqYtN4YeVvWJUQQUKk1Eac6UQ0kr7jznXL82XOwWhzsAAXLdIT2RmD9q02RT_p1uBvZZUmPMhu8w1dskhdMxm4mqzhraU5KI4vl-9K78WvVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr0yR4aeKeOQURdfOiMGUokdIVCwaEsPryvsSKXU3TTG5RJ677R4szkTzJwQBn2cHojRJERvrY922Rpx427yKuMGOSbHT09kytSUFNEkBp7kBklGizEygHFcHEWJgM5Kg0EzNa3w92aVk_LIIXlyARNXXkVQ54ck_7ucY3aw8_LvEAuMiXGx3b4ZAgbvCYQaDwvBsAWN5P7UHGgDAIfVHgtXCfrZVoAmQwiKI7nW36fCe7kLYLOSh441UVNCrKfZHGPBs9FgTTP4d_ZqEnLnlq1yc7X13-0PFIa_KQGPRwSsAoYg2SDWc3bmxH5FHCEd3RxVchMAF5TApq92EHw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaLAh3IiAILndiyJe7PwEbDpE94c_J2XLsZCvdIzPQNEHPXtrH7fiU1Q07qk43mCOam_ylQOUzyAYr1azB8PMt1H7yNtACJT5z-WDnZQkWwD-CgPlHAz6Pu_nARwKGkCBUrpYrVsDNZk_yy02zC4jTULpAz-J7NFyvXOc3wG0r_AjpZvk7XZ-r73h1--9iFPkSojYszoARzewpbeKo3hyfylRsAmynxOkl8WvvUxaZf8XEAR8kJSYiCSGCekQW0dX0T_fVg3_0TYjbcONd9hu5sW4SvxeaYCQgUjJWj64QTaGFsTMXIYXscBLUyW3r02vIl7ht1ynWEwQezwf1W8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Bda7Hl8nl-sQFy3N62aHzVjlBhVgys9nzN7GGXbRljVM9n5nTJ22pFU-kLgDCs8e_A7bEI5b5ZVfEixg_p1S4g4Wd3aI8B_FTESbdfbriy2zaU2LqkJJsBwbQTtOIeKyRl2xiil0AdgAoWkT4I3b8Qeq2F3z35WZZq9GDBiDyq5GOj11SUe00PSzwpjbGuQeFAZ1ppPNNcUnox0IJeq0ESP5XJqr2bsIB0t11fQ_E-2mnWOL-Hecjyzgn89ySFi2sadbbCkdJaKZ1AvZDwAjzxzV6t7kfJb7N8_nMGCYdHFSaSHHi9X7OKsGMy0xdZTgaXs02oxd4iDc-bsGUTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CflROHh8yk50lUIQpeWZ7eSVcU7WN9XbHeFzvTKj_POWXCo4GxY-iriwiMPkpDsQ2no-0nxOYc-KtLxn5IQfz4b_e82fwqi8kL6eFIcivYYyp9cXZ5KHpWqEh2ktdexTwt0nWYfriKV9lMD6lF7WQq1Bp7QQoyYxXaWTpf5-BPILQ4nWI63dqu6IbNJxt_sh0e6zCcQGCrg44jAxXHO8y9cgFIUo-IY3RSQhVk7xYoj_3IM87XHXcibPn5r_XoX9cQLKflCMkxcTzdTgJEjD3aoBbRtoVJrKPaeSp6kNHqsYRGSX4U7_HvlBjaa1Wijy59YfGIzpojP9vaWO2NAucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXqdFlW1ukQPbxY8ntdc5mPsdqdN_qGBx6fdEjAr28VwvmJSBhbcGRW1gPFNF2sA-h8csyX64ZBI54CbIJQhCqgRkclGS0R40ehk-NEYvyJ-tTC_WvZx7tg7GsVi57J0Tp33KvWcGpzN4HmZscsacILzlLSzZSgGn2fNDVZkEKzrHiXPJkCDJka4rmU91UQJAZteOLeMrm-cg4TP-p3npqsSPoK8QT7UU3xDce4Zv6hXx2TrgKMjAG6DnEbQp1bS54lcnlB1-YGOQR0roOVtK3NIb43EEi6OSvRtpagjzUKJkjc_xCqGYu2CLOJV4POP9vFIH4lbryMd7RAnM3butw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN9R3x0_XmLkjkoN8z5a1sjEdSgBqS5SM8RkZDv8SSNLYk7AbQZ9pjnHa0sLWGi5P4KqMEKtdXoQmB55jAtYKuLPW0F4W8zzlzeaw8tA_IgGsO1cUMFHeQR3HkuvcsBzbzWz9xe3oLpOuIYk62pI_4SfPPJEg1D64OtgU41uH-733lgZp2r8yKJ8tXDQgsmq33LLMlr92JZ8Ch-OhQOKjk7_lUEfu3VDSSvMpy3V4QBns-Kcf2uish5cS2xJIpXXpGteub42lX-NYOkSCQP4hWD-MtWeqlpZoTcToFqA1Oen_V-KDz6pE-UrCv4YPrfjpz5moG4lf06kME_2pcYXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=JIkHPUwS6WkQyxFphQNkracnKzqEiar-7nRWwU7ky0bqcBmKe9UDW7ThF0pNBaeC3lQR9p596YgCgWNDHnp4XCF22be_x1LXA4cU3YuEYivXkB6gRvZlXflLB8nCpdL1PbTcPsXcPDRpHTGjx9zv5wOTL6TNAkzxyQJ_9GaEcn25SJ_OSDvQJ5jL3zV3WHtsUmqUnVSC-XPc3RBdHecJ18s1R5bIe6My9_dl-MZ6mn1_VrPqFo2L1HCM-69IOApoP9FA1nH58RNWQUttdH0uInxRJHYvsvt0tFgQOAIAhMsMHKD9A2IZjQ2-dv9t6Y4qyAHRT1uLOf8v9PX9pL_YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=JIkHPUwS6WkQyxFphQNkracnKzqEiar-7nRWwU7ky0bqcBmKe9UDW7ThF0pNBaeC3lQR9p596YgCgWNDHnp4XCF22be_x1LXA4cU3YuEYivXkB6gRvZlXflLB8nCpdL1PbTcPsXcPDRpHTGjx9zv5wOTL6TNAkzxyQJ_9GaEcn25SJ_OSDvQJ5jL3zV3WHtsUmqUnVSC-XPc3RBdHecJ18s1R5bIe6My9_dl-MZ6mn1_VrPqFo2L1HCM-69IOApoP9FA1nH58RNWQUttdH0uInxRJHYvsvt0tFgQOAIAhMsMHKD9A2IZjQ2-dv9t6Y4qyAHRT1uLOf8v9PX9pL_YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iewWcOqTFhH2_8-eWw_78rStPRB9CSQoUdUGCKnc1cbLWuZLKX80puC6ajeYOIPzkaIYyvBcJB0TJcGtYP1MGDkADL7sPO769ZG5upnWN0GsueWvoik8SAhX6_ZFSGyM7RdcKag-lqibJBcZtf3jkint0d_NAcoQ1di2AkGa3zJ6KjpmrJqcLRsS6UEkzouE6D3CHe5HqTpyosYSLyNUPWJO32miNQUmtfWbq2CNvDRhzw9_5nzcM9Iz9u_KQ4gYIaOGufT_-iL8GMcLqgbjGMd5BH8cr1Hurl4Md6R3NZMLLvw3Z7j2-UhlJ1PUe36Ndac5ec_WNUPdXslcjVkmqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtF6s-5LoplNOhL7tAYie8mrx9qIJnvdP-dfZZzNytPv8APWP44VTMJK8KMxTD7dioGPcWLhOfbops5AZ4-KdrC8XHGeiW0KRYHqsmWM6Jq77V-xrraLD2dhQN2PxHDHzg1MdqpPLMn5Zl6l3FA7Tub4hxvlU7BL8jDknAWTVCj3I8xDGyJxRfQeIfk5p9gMx6XtgFkap0YtKY6oTF2wt9Lbj3yuGJi3w3lwsTnDGE5EqPiz2sw_vJY8YiayI9mhqz9mYUw1RmZshHq70N7coJHnYbaG31rsapD3AbiXI37E7IK6FnKsM9FdbFc1RsFzaelJfNOiuAyzy1BdKgHhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=NOLPkKixYOmLvaoNk31szb53XBRYSWddsvEXLqFxHEJPumVOt2ju8k41C8i2zJ7CSpD1ad4A4B64sVe60VtU9U8XQrXq5_Edz3RASgO16EBQaQ8EOhIllwzgXAQVEmhnj464AXE6DWRUS-LPFajaA9GcNJT5K3UQYfQYMtgqpTf3AtbuIfVwOYBMBMm-aLtmUb72uuoUm2dN_kqYaEdn_b5QB6IcmQn6usxk8tY0iL26yv1CR4YPp6NZQmDuAKTiQEmlhV9CoGTYGdfwjHWq6im6n6LSPGJRS_c0H4dM-kQKOqUj6PzCbp4g_DDj_pMznmhp4ky-rfDJzmM1BXd8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=NOLPkKixYOmLvaoNk31szb53XBRYSWddsvEXLqFxHEJPumVOt2ju8k41C8i2zJ7CSpD1ad4A4B64sVe60VtU9U8XQrXq5_Edz3RASgO16EBQaQ8EOhIllwzgXAQVEmhnj464AXE6DWRUS-LPFajaA9GcNJT5K3UQYfQYMtgqpTf3AtbuIfVwOYBMBMm-aLtmUb72uuoUm2dN_kqYaEdn_b5QB6IcmQn6usxk8tY0iL26yv1CR4YPp6NZQmDuAKTiQEmlhV9CoGTYGdfwjHWq6im6n6LSPGJRS_c0H4dM-kQKOqUj6PzCbp4g_DDj_pMznmhp4ky-rfDJzmM1BXd8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=B5pFa77c-FXHjhj5RdYAkJgbpQXj5JXMs78RDE6OQRzPLSkH2ATGftIeuR1_dw8ns3ihLSLS-4nRA0hvRCZOiKBD3Q3_pjNv20y1L_7-LILp3fyo-2Q5q2pdCC2Wqa8QpplHn6SPO0FIN9ztB1mD_VmKK64e64WuC-zPHtvXBaQgEgFSPKV3XWM33vP_1i1NVwhlPAx5chIdsoyO2bQWSm8Psmoxo95Uy2efFsowyhQKK-o2eLvdHR59xzNu161kZ1UYsHUJZdz69xT_BaUyXJWAKrkT1FLjJCXd1cCGRPlwl0tV2JyzseDA0kzyjg21m-wz5xwbn4PIyDUVZY769A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=B5pFa77c-FXHjhj5RdYAkJgbpQXj5JXMs78RDE6OQRzPLSkH2ATGftIeuR1_dw8ns3ihLSLS-4nRA0hvRCZOiKBD3Q3_pjNv20y1L_7-LILp3fyo-2Q5q2pdCC2Wqa8QpplHn6SPO0FIN9ztB1mD_VmKK64e64WuC-zPHtvXBaQgEgFSPKV3XWM33vP_1i1NVwhlPAx5chIdsoyO2bQWSm8Psmoxo95Uy2efFsowyhQKK-o2eLvdHR59xzNu161kZ1UYsHUJZdz69xT_BaUyXJWAKrkT1FLjJCXd1cCGRPlwl0tV2JyzseDA0kzyjg21m-wz5xwbn4PIyDUVZY769A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsjke6TbdKyJqrAEfqhmXy5iEbg0qCW-fLi1GXXywRwrr54nAgrW6AKr0UrP5FMCdBeG_znmPwZcQxMu74eZstqM_MbsMkn7-GoFsM8WbFbiuVlEJLr2gknE8JitdCAZH1dbuKo0oDjGXsIDnXRajltASSp0F9sAwNy9FpEwOE4UbnCRvja-goxibU1U-grmwQMKRdujNr_aIBiyUGusj9jwbWOV5OxTZudCD08UffXHR3clxTmq-o1eW8Nb9K8NfCL7ezyNEvxNxnPw4eKKRSAr2wl0dBiM0kP8V1JVFgZEtevnks-_YzVgsUSAj5hoS-xt22EWSl5Lp9yd3i0Q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHDFH0PvptHyIoa5NpfFl2EmEcqUlJeDoEZxWxxvLvT1xdX1oKbvKzCV3VrSB2W8qJgYtFaIfnEnUBA6j0AnOv0oY5e03Z-lLLGyep9rU9bdFvEjOHOJr1synt6Wrm68rokATyXxg9qOudPgnl15euyly0iezSEGf32wzsUBcIXzfZ-iNIkQLtis5v17Eb8SnZ6FCdltUJrZ3aHfWGOBJ5FQAhkS-qkzSMe7lG3D2Bvt2-P0M5rvnu80z5g-vnqbJV_wk15zsNt97qlBbChCk3Jc4oZaEn_vBgSe8f2Fpz9Dhvr0Mt0SNZ5Xr1zL-g_0fzDzbuqArx41vIF69-CLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=Y-LSFAq_spOyieY8BP24-2WtpeE6P9xPrFWo_hvWk1SYe8s9qYTQ0IhxzmwsJcOqn4d0g0XGLZUCIsR1RhoyNvp3C-CTmtMlNUvT7Qjr89NIt9jBZ5DET11zRVu6mKVxT-vjlvqfdHPzQtNx-XDxlpAXuK9AZ9dQ_jG5N5omySNny7wIR_ZVQUmGPc0mar8YX_LHJARc6Rf9d_xZI-faaBXUOlj8Kml6P1OSebRDhpja7foadgZp3wDjV8d0Uof6CHF3X8In4fkf3u71yKE0gZp9Z8wbnGNSmp3fqEcSAr4IiyENXo-LwtGJoQ4P9bZyjZoCapblVJuL8U5W7RoiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=Y-LSFAq_spOyieY8BP24-2WtpeE6P9xPrFWo_hvWk1SYe8s9qYTQ0IhxzmwsJcOqn4d0g0XGLZUCIsR1RhoyNvp3C-CTmtMlNUvT7Qjr89NIt9jBZ5DET11zRVu6mKVxT-vjlvqfdHPzQtNx-XDxlpAXuK9AZ9dQ_jG5N5omySNny7wIR_ZVQUmGPc0mar8YX_LHJARc6Rf9d_xZI-faaBXUOlj8Kml6P1OSebRDhpja7foadgZp3wDjV8d0Uof6CHF3X8In4fkf3u71yKE0gZp9Z8wbnGNSmp3fqEcSAr4IiyENXo-LwtGJoQ4P9bZyjZoCapblVJuL8U5W7RoiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=CTK9YcVleR7k7a_o-KGWYsQ7ZhriuJF5SVcnBmJVRnj7uNRCTf_w6ANWljjgrLBL1M76Jy_F09O6gLiVsZIHAKEn2V498OSE0fZEFWQaO8u-A1SHpKQLaQ9bZPEvHaIhhyYOj2ytTmFZH6MTf4nMKZwK_1rx1A6PGSO00hiOeaChw78Ymo5ax-LK0Y9Q9neWxdloucBbHVnLZq-9TFCgys3h1BuQZvqn-GCRYRZuV7IO0FVb3rkUHPecTseHFaDPmrZWNuvATUI3Jo2oUjWK6Qv_wrxB96M098J-sfEX_H0sOZPzbpRjX0L0kPy85V4ounsxHoPetDyZydr58ZMFJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=CTK9YcVleR7k7a_o-KGWYsQ7ZhriuJF5SVcnBmJVRnj7uNRCTf_w6ANWljjgrLBL1M76Jy_F09O6gLiVsZIHAKEn2V498OSE0fZEFWQaO8u-A1SHpKQLaQ9bZPEvHaIhhyYOj2ytTmFZH6MTf4nMKZwK_1rx1A6PGSO00hiOeaChw78Ymo5ax-LK0Y9Q9neWxdloucBbHVnLZq-9TFCgys3h1BuQZvqn-GCRYRZuV7IO0FVb3rkUHPecTseHFaDPmrZWNuvATUI3Jo2oUjWK6Qv_wrxB96M098J-sfEX_H0sOZPzbpRjX0L0kPy85V4ounsxHoPetDyZydr58ZMFJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9Y-QTIPT9BXLY_QCWBTyxtNKcBdDRP_cloc_rz8B4yAYEqs1MTO9AfVnaQM_mypi-pWJCpeJ479FdpOWfWhasQmVVkAlhWaMZ-CPluxy3RUHnI0H28GsD71mNY3N83NpxqkiDXlz72ZWaz5A5IU0w6sDIbH_ES3awJ-4el63u07O6KsXgklhYdvBd0xlqfbm6RXiKI02ORBviAme5iSmDIG1sAeOSSustepOoS-Kj5Fa9d-dEt8Y14xNtvK03yz2NRbOF7J1ElNYNilYq_igZFmCeA9096Fln2DesPu0-qQs0eUNqG7t5hNMjtkS0iqukWnBHU5Z6seN2wmhcNT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX7dAYG-dlDXQb68RVbpFpRwV4pDji2Xfwxj6-j5WoutK3hVWr6Lk3RtUQ9l3BbPSdAG__LZwOqnxyicF32zQPecqac0Cv_dkPgvE7guW9OcFewnFLBFFJp-M2ZqqmghfZRdCyDiavvBbMUIzAcm4g7YM-8n_pkHVSwxeR1QPUN2G7TScnJalKecTnaCX_3_lT61YOKwSPNiaSbD5671hiYZSFvVgxcRxaayHrvWbgQnKPYOSae8LdGCDAxdZk46vElid4YrHGZonUjvbW24k_gH7bcw472Eu_4j7wa3Vg3ltWJk80DrF7Jb2EGAzePMqcTV8KvKnS0pMB6q5ygM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOlqbKgNDDvzYRo_7Axley75jK8_cQVvwf1RqZQDHnpwNiU-fY4gLlguSzSoebJv7812DWPsMKq81OPPkVYdjVrL-0FYUD7D6E0qb8FUfERsZthT4kAokLmQMKoJOSzobcrZSzBKUMRJltlcW44VTyFxXGeaT-PZ-JF_F_7auvTbatCXqnjTnNBk_1pioWcahW4hkb-5lXF_TEc301QtrufIXM2eOa6J1q1EWfjNslOf6BTJppyvjkc8URwYfWHid8fZg5yiJu5Wak_vgmYFFrFrhJAoSq4wcUUCp1UtWNN-VnEKItPnsqyxV8Kn5HVXYywdr8Fcq-dPcF8OV3zWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heVYEIUDEpOUfFEISIXDMJ-2-_CKgj7vOeXWZWwmqpl0z6VFEQa3RyP9WmjkXcWCugFpKMo7AXVKDnwhECd3VoE1p8Q6EFMjCFbYjfMTWDRfgO8HMlFedtU8v7BLjS0LdfPrJVyGOdZVSKdk3WtOoY9kH-EO18-S1LdiycCxqqeVNpi5D8ZDYBm9UMegWMOkeLlMkBcP1FyGcWIbDgrpdr4Xzqqfr98IQMr-YzisAiUY1Q_Kgs2vVLMhbKMtP4ndgUv_mxsy9lPnN0sZh5HIxo2SmryqVmko8BvmpNr4nmrPa5UfPiL0h3vKIRwbZz99dm22QDZzlyiQeDvC6-WP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOCUsrcmn0bPVqhZMHWYr0wWtJzlx3U8brVZS4-x1mwbNGDsCdSmOZ_gB8_6-m5WYyuiiHR3X0kg9p9AWrm1wkj1Sd3st9adEB5OjJm6aotrP1ZjzShe9WNbKNpdn55oNGBf0HnKPkfPTbqy_cRqJkLe_D6wwTGeQwbkmLgdZTwKrseWz-6_aoW0mDVmPSxE5pzIyyJNsD_qfOwugdh2_MUgLnWqHtqgJcDpZf8YT5mUYlMijsBZ6KCKYgDKHzjhvpijq12NgV-9e2977OfA9JLsTGVsZ9boezsLUJbP80hBjyU5jXNgY1ewIHJfAQoM1WhkgzlyIKPzjN9jsWioIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu2hqVPUqCFubgDGdulexKZoRcUlk35Api_M3GScQAL5GFoxw8XFdWZ90lonQrJ3T1KtGhbMeJPXq8DsBxangnJy2MyjiWBoovzRswJwlGmgT8GcFBdjnMjfKY3QSvRaVioIlMfc5KlnsV7ldEHxO1-WLeS8N_3qn1hl_CTzqzBy7OTKvsbBYzScWk56FgNuOF7KGS_30E0ByUiXQQjhFloGE0TgMaKm4eBjSbCu1Sx4TmoaETD8wNHEEH4VdqzBcnnIN_-ZGum6Xv9FZ758n5xJkkWreOMylcA823Ba-4D5gNay3WNbv4izuCRSfJB31E9_PfEjJa7zbKGkwq-O_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zox5I--32jKLKWFs45TBo4Ar1hrowjIUG3bc60JpoMb3I61jcA6b1J0Iu5STcsATMesvz1Bv7MGfaI_djFsjXepeWHcG68pPznyn_Td0VhmgBCDATzbNHgxp68OQxyHF-f7WYKBDuPINlPvq_5JSfDkobV1FvZl8kcmgnfxK_RfqPMdPtYkl5yc7fUm_ICsHDgWPv_QRZqMaO-k9BqDYRIvMxsp6EK9Jv4pbqL9ZUKx8dg_GTc7i0uxtuePnluptIOxWZyqyBjxbj7A2_mnv4i7VeD1oa_JkDaUamnL9-ZUOTZ9jXhEYmUiitUXSRV460WjBP4YmPDwNx-nZIBv1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw0EW8cnhpjEulKsLwdPv39CI9UVv2-qCturQ9sX5I1eLMbAcjQpgFAbWghwuFLMVSyZ2oymSl6s1iadEdALh1-0dDhIl4pmYyFApOrpfHXeeSFjWjUA-GKx7fsJziagTT5hqRSsoQr5t1iXq5IlkZYxLF6YU-K5G2X5zU2W_EsDM6ruhtgzqXKGq9abU8srbjEDy3UJ779vqD5UOFBD0FRWyME1wim41mn38aboKqmRSpYkntbU36yt5CwUaaQTM_VtJgochDrK1ZTa5OwiA6pt_MIApIzT249YAoNczQfyFrbQmMbYq4BDQh6SxXlan2oIgB7fBcCe31rrte3h8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=jYvX9Y3UH6T3FaCKesZlEgrrVoDj4e1EKAO76xrrYKb_UmATgruSTBTifd6toONOT64_3CB3J-sz5hHQUesHXMrz5YOJhAd4gA9FHAgNY4jheBeLrlZH9wKiKJT5y-6-wS0NgLuKQgjH0Um8pdN7VTMCVAX2akgQk6AVSxmxu47zXGaceHpxgYL6xf_V4nCZSLWUK_171PoKczlvGrbtBDrYJP87jwn3jEJaLflIAAA2KM1qCB99itXRRlYPBLmy9FwfPn-PSQaxuFmitfsaVOItZunfl6BN_MtmRlvR7APFKLUFFtjf7QH1lcOh4UTey1dSuOh_I8tK--49DWNxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=jYvX9Y3UH6T3FaCKesZlEgrrVoDj4e1EKAO76xrrYKb_UmATgruSTBTifd6toONOT64_3CB3J-sz5hHQUesHXMrz5YOJhAd4gA9FHAgNY4jheBeLrlZH9wKiKJT5y-6-wS0NgLuKQgjH0Um8pdN7VTMCVAX2akgQk6AVSxmxu47zXGaceHpxgYL6xf_V4nCZSLWUK_171PoKczlvGrbtBDrYJP87jwn3jEJaLflIAAA2KM1qCB99itXRRlYPBLmy9FwfPn-PSQaxuFmitfsaVOItZunfl6BN_MtmRlvR7APFKLUFFtjf7QH1lcOh4UTey1dSuOh_I8tK--49DWNxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=D94SFmCO5AL4k6BJsvX2BRX_3lVJhJUaThTkx4fEscx329MS9LEs9MYuVmJDAkzIvQG8VGpQca1PattDMRm847FAzyOy1H4vcSvQlurQxNARuA2OARSqv8s7e7phH4sSYYa2F_Vo85UzokqgqovghYtrFYT3_BantkeufQtfoeyLYuI7FLQlYayyiIU6zUesZBVbpcgfKglSgbhaK-yAJENyx_KDhBBQyf6q-L_Y-hYQhBLZY5asHHwPMbWTfzJ-S75ikHAiZIcewmtgZAsugFRzDn4-EvNJ3sGWDn-XYrhgAB8GtYxb6vCiUIq2hlfdKCeCgc1HGTjoSMW7hLuTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=D94SFmCO5AL4k6BJsvX2BRX_3lVJhJUaThTkx4fEscx329MS9LEs9MYuVmJDAkzIvQG8VGpQca1PattDMRm847FAzyOy1H4vcSvQlurQxNARuA2OARSqv8s7e7phH4sSYYa2F_Vo85UzokqgqovghYtrFYT3_BantkeufQtfoeyLYuI7FLQlYayyiIU6zUesZBVbpcgfKglSgbhaK-yAJENyx_KDhBBQyf6q-L_Y-hYQhBLZY5asHHwPMbWTfzJ-S75ikHAiZIcewmtgZAsugFRzDn4-EvNJ3sGWDn-XYrhgAB8GtYxb6vCiUIq2hlfdKCeCgc1HGTjoSMW7hLuTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trvo1mPzopqMC6_78unmTPuQMJiwGemlIo6jqpYaJyBKD-zTTRPwdGOE3Rbf73rH4hFkEO_Y8LP6uRu1QtJdK_hKfXQfOi3Pir6Pa8DbnlU_pLjF8gOs7gjUfQ7TICvbKAZcEum1430a6cqduEoLuHNWLYiX792CJdu5xfMMmoFtOOGy0xj3Tvb4aQ1pxddRTd1jtm_R1kIC0J77NKmOzni_UxsJpboVF4J87Dkfq8bzIxRRFv7abMGmgRofi3x7VixC0TSkhnbt1J4y5qolj26St_w6Y71HlmEIXfOteNv4OOHkGta4gjOt5SOXooq4nrFzveS13D9bvI3aVWlH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqPh8ujhgmZwEL6aWimJsyy19NEPo5Mu5ajVodtIiqku9oBmxYr1j9ZXhUwS0GaY7V8joVXCB9zpmw-2-1OniTQ8dwbFNdS04895nGLn7DK8_3nb3JzMKCwhCNe2Fp60gnldi0wNWRVYuEjhUFAfhZSNCxrD37VIKZ8B5MRVraF9fv2ksBzRu2jmtPiXCednersYno4FNJX4C77iMnjxtH2S6bPsCHGt-ShzjBUUOTH6AxkJV7Xb0RfRlilVwIOQBCb6KqAZLpttEiYl3LjlYdowFKrUIVL32_iHKIBWFlnl5pKUFm6LGO5nrbFw7N1faYPXUHeSC-tjsLfr8QtDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=YscnNAYop4i4cjZAiB8A107-kdFoQxsjVjdwMopcXxPm88t4nTGBczJXmY5oAAi0yw0jI3qmrNIjEivZJxmwcUIWFtdSq6p6t1aXfQVi4V5WtcCjQjXwajrNJ_Tn3Nb6YLjPIgdN46BNYPFpNTEnnXdvclpZg5_-6xgt89XJKA43ipiuy7d6NJoqbnzvE2VzMlIu1dFTLZ_d6Oo6Lut41EayvX4fN5_Q28PnenVIJwi2MZrWpWghwVZOPD-vDBLk6ObK11gKuyD_xfy5zQF-LdB8LLeXTcrvWVbGMNNNG9BiT7brCqdSSpgVWBOvceq5vW58JN_8c1cNJb2yJXYy9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=YscnNAYop4i4cjZAiB8A107-kdFoQxsjVjdwMopcXxPm88t4nTGBczJXmY5oAAi0yw0jI3qmrNIjEivZJxmwcUIWFtdSq6p6t1aXfQVi4V5WtcCjQjXwajrNJ_Tn3Nb6YLjPIgdN46BNYPFpNTEnnXdvclpZg5_-6xgt89XJKA43ipiuy7d6NJoqbnzvE2VzMlIu1dFTLZ_d6Oo6Lut41EayvX4fN5_Q28PnenVIJwi2MZrWpWghwVZOPD-vDBLk6ObK11gKuyD_xfy5zQF-LdB8LLeXTcrvWVbGMNNNG9BiT7brCqdSSpgVWBOvceq5vW58JN_8c1cNJb2yJXYy9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am303ZRc4HkxqDs1htZlarTMNsZL5aucj4GmOwLqELa8yp4Kyh4KAx06i_Vq7cYN2Y0xC56fzIVn88283NGmkA1Pe8SfLOeYuJ2f0mOK5m23uxLZ7Y81DiON5MyJa8-IUujTauO1kf6Fuxioiu7ZO7GOYlCnOHuh3FkIUbP1RTTJrwgu08QnAVmKO0BXitv0VKrCLFXM7u-1ql3Yl7Lddu21ZRGhl8zh80PRSOl_km0biT-bajxuUyHD3mqLY8Sn6O2kBgd05AuqWbFN0yghi0a9YWp8wAj_Ivk_2rbTa62fVHmU9SfYF1zROMgMFiSt7_lCyrb1VYP0SB_0XbUpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuBsiIhvU1LwZQc2tYxirSFf7lCvwmlBMcaGCkUkWdgtB8StlikuHQIBzJYnBqBtgJReO7flaimY_0gB16IE1bvUKbvxlGcsyYHpwUFS5DV5l6Dj4kkMP1CRQr5dzWvBDWhwfHns5UKuHFbqXt8y1wWeuxcq04vaNcVrD8dBndbfSoM41mBmxKTWJo-Gzm4QWmILOpl8y2-QK4GHl5H9rmdhYBQxY0FkD4-B6SkxL1BGvD6XzQjqOGYVcDO_DLBMC6PfeOKtDWXde2JnIAcfboU2EfMCG7_-_aXD2Gsl8LixsSmonqfTakxL5gcNP6SpBFCFhC5QUhMWVEDYyaL2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKWAEEGh2teEVofjrOtWO5fClMt-DC3R58LtsqK5gnE0DivNdElDepc2nvvX-_dFrgk1znvE8iAhMAMA4_xZ83-KBF3VwFFZERXK9jlL5BAmxY2ZZnI5bqPF3qJG-8iduYBmZolhzhJGeMjlwBdTdaawzQj31Esqi38exQVBrs9jLInC5x8Oe77FHICBQ6OcA60CghKJ8xTIGzjsDGtretBhJLa3LJcbpBMjarnVmdsKk3YMXxQ44eD9rs-Rrd1EGOm1B82UPn7Heq8aaE_4Vu7_sxNHCWpFY7TPYJnCUk1xzECjla84BNTSS4d48wAvmUpOvjU-hUsFc5QkzoB2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btxEOgKwt3wwmddErW72uR5HUfVqu6l1S0cMWP3bjZ78_Wlu-RUvrARJEP6Grnmdqf-RaEZjMzVNBRBwGIOR_DhnRpmbvpT0sprsp15Csy1Ebpox3hQZunDqVZGlC0_WeBfRHjwCqqPIjak0tgeWyXUe_S6WPQWDjLKzvqTX8o4yNWQr9wXW0wQOsw702nmc29QplKKscJFccxEhLj5t6NCWsslGwu8jCzH7GM6atFrsd-HQChLYBDrxufYKC4I_F3vjD48qWHDXRbj8haNfBjG3yIX5nXvHLAaqeERn02ZHSQgZZAakujq2EEiMYnm2WTck29DJyNoDjmDHsZZKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIDS0ch-lgM-6yM_Avj6tDYR_LWnLyH9Il3RKbYymcOiP0a5Ebc77AqbfAX8RMtH0U1gH20aUK9jEHlXkCY0NH-bhRIoWO8iozFaYYPC-zz7xUCnClIgdUvadP3gx3n1i3nj3qJxMzcll_rZZcZsdlfhakUkB8b2EPFm9tNN3rhtrvM6flTgmulzHLQ7p7-90qX7dIs5RH_54NJJxdKfL1dgN_5SWpCYNO1IDz_Hrxnt7BzrOz1eAIziZhxNJyUCgAPx95RIQe6k5oX-z3XD5clJ7Ap6ZtbwADjjj0p9DEM4IS47lV7SW2KRHp1b_ZJusf-U7F0kbfF62ngheDlWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR3w9MrOmdMkDDWfSK0qDe3xkkqD4Wsm_RqlbkNGiJG20KYdK7UyTNeb1c-92PZIWuKR151cR--YBVlhp4LKeOLiIBZuDBAbuXZM2C8TYyxsYgLMKONmqiwcoeuZcJO8lxgH23e5vvXtfillh3N2AaTzW0DtsE6sT6AgksCqqLJBnsT_Eh28iadtgc2xrgDq5z7RSgDoME9gnxTj_a4hrec5Utyis79YcfLyww4azXjwH74Nnw7Trm95dRNbo6PJ2FfAl4VmkBYHqeRygzqW53-znpt7bGrNeRRU7xtXjk0Cd-up9c5zf6IyuwQ32vB1cKzk-LaQR4HoUWeaxGDMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6u3btTOxMpoOHfSi17M4e2pEoEukJh2LGipWYpFEfxwl64mHotWNkjOkm131PFj-CHEgiFK80g4tB9YJc4koriZFKlu63KbHzoD9U0TA4UT6UssbdOQzZOe-U_cpv4Waz235c274GFpTZYc-i8hxMgxVYqEmKm7U_abcGwxCmVxgl4vFs43jvtC8_YXstO_71IEixhsi2C4NVcIkCFIzdMHslMK2HcEow-D5_OvlEwToVoV9tbC3X6JvrOLdFmqDpqCRMeAkgWlBJJa6EcT9Js9fWYyT8DOKOjXjxzWaZIJzESCSYd05MqJ2PccH9f3oAYCbip50YxsMQPeVHWgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwjzhsMXNbBRTIUJqG8pNYHhsq5czuWPvn1nIqbihDGU9RK_b_cnLfeqopSZ34vpEl7Bfk2DOJ87I5il9FDTSk7fwSvW0Z8Y5cX1nlix7WXBZa10qQyPfBqE6O6DJv88jEQ5z3VnTkJlk2b2-NlhQN719ZexfPIsuHSM6BpLLogvAt2ZSYGI5Q-aAJaDDsE9uNy_kpFReY6r-mgvpw4wYPD0dvphHeptmmIe2H45DWLg_rVyVLV7tMryWU5PYpRanQXU_y1du4FM8qIz-P5SuCoCn-_Ray30BNK4k3YqYy8p_KBUkmTI7pX-FYWAryBEE-syxBjYWK1UCDMZEeuuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWck60KdaiJFxSSHEexiVBSz-C9pP58OkW90nSHQgX3mkeikMLT6aG1gqMQu9Kw2xlREl6B31rzAYG_c7y4iYgovcNnOt3cNaa3D4zaKzNHbYdUbjm-8c4YJ_HfEQ_V0S7JciNo0QBGlH2n9kPMklmOReK6N_mO2TQV48tgqFmI0g7-TOOM-B3fJGq0ojl2CiXYWRfXDqfy3XQtFZrVCA8SuyBPjuy5YTzFt6EHG1e13z2griZDxcTQospx5c7JRSuPFnS6PNOBG6zrxJ3SuRBQVQ2O3JXHT37wfr8KLp2YDjr2LkPJIrqVzH3GZlIZYZHpsvRgCebS2_AVX5fGZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blFxLJPckmIsWnRSH-VG7_327KPhbWHvz_MmJcveEjFSOtlIjWz6i0Z_JDXvTl58lXSGxjpqaOVamRz2PxfW3fswl_TM4SLKllc8paOhKky1LEMTpBf7uXaeJn2wrBR7IvLj_276oP_f-5_PyLcvNFlHidNmk4N7HxOG5SdXdIiV9dyXccEYfKl0zvo-ucGZ_EauH3tEQV4FziyRsZKhnurHOSI1Rf5LwVjy49cSvt6fZofGmSmJFWcvYGz9OoBdySmzNuyTgNALkDhiankJBXBj37X-F9EttQ7beFZ0h6lIEQMG4AsubsL1yBp11ztrFhyd2eqWcBTktl36NhuamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-vf7W7PyRtbz7YpjjB46fB8EQ8IUp_E89VN6_BmEowi1BB78WfRQ7lcYEfenmiom8MiJgqGqLzm80rT69M378Qemj7V7fmbpT-3zQezcBZGSbladnj4CsBdXJj5qioto4jtLw6raArgUDfP4kzE7hDdU9eeAygJJJYTeEEXyR8tTlnEvV_wjADrw6cDLZV-qB1w5b5lGex9ESTaj1-lYChRxxryjmlwjDjzuc-4JYoSN-0-tk19ytKVbtgDbbQOw0YzK3HbaU_LmhZkdAiyJsMIse65lmXYAvSLr7euoR2E6qXx3aVoULfmctddNzvLVxFj_SPHgOKdSsrp5HC55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuTUAvEZHFQANIaZBa5HVl--QXtW2vbJIRqyNKQ1F3hmEErcvw6nvsFIJPCIV-k4zKtkZmUOG6bWjyCOVuDSeiBysfXF6myE945WSXAm8-VuQoXq2vI2_Hdgib2mqljbNVpQzR810QTl6br_soV2AtibBN7Zhb2VzVzvhGkE-ZIdfUoA42nrfv3ou7zxQAmD79MsVA0FYucdeByIVnkiIec3pPfKy2OYPUa8CYtgPAPMM8KK06-NtFr6VazOEpORDcO6EkAdgLH_I_7mO8KfWKHcyUMbKjh7VBQd89OiZSigpXwi-xexD8DYFhntZfEu0DC51ZO4UF4KP0I5a9pf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOayy8S9tSYaajIgwJZSkJONuyrdc6E6CB21xxJ3e5JGeAmNS5h5-2zJ6qimwQllPkiwQzJ3rXEuIbKzCHSgp-IBYBTokr5Y1j663eWIM1uHOmFhAWbaP9rd1TVjlmp2iJJK6Acwkgm8kqTp_n5Qn-CZHbusuAkVBAfoAxAlL1w2FOwqV3UbaaWzXVhA6X3Bb1OOb8rAGqAmnsNeJI1MULuui8YPW3t7C4c2TTBVFXcE3C1bZbjn5neItLV-Qwjbj1cSZASQE89mtwtKHzYDDdGHR2UV55nUvgLW2VozXgbkPgxYMWsPNISNWw1Om8Bo6BL8QeG3HdwZOsbDeQnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWQF3adt4r3vePINS5QYr67Ypi__w7gGlLzpSQu1A_-CJ9cBDHJJEWb4Su-JOtlO7FSKZZ7hCegdSRhEe3h9Xop4Q9Nk7Ap37JxIujHaUIBsUah_LWw4QtcBwt-_kDSoOG2q0wu6e2i9oxKZ4WPf5F9N8RKFma3rd2ofBmZm8Ek9Vihy29Jsm2VbXmgVdYx4Y4RcdtqJHkV7k77KOxhGOAW5KcyWe3YAp_0w5AyvtHwDmGsjTMi3JTLFQoH8lN4TX4NN5bUEnVHiP8cROuzj06NbW8Z4UOI1NIQm2tosOhe6r7lUzh928cfCgn_dnD-sYw-xQSBZ8SqCWgxkEYrZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ--lQAyNUl1sjnsryVMwYFT9-98G16YwZ6RwRFij-uJL6r8l_sg3BOQwWPeO0BdsnDWZSJTf8Sw3c1wxU3vamdYXkKpEgP_K423DehfUui9XGMB3DUsoevq-iioacZLZWqwrxuhOrPXjOBwvFdxb84fTKGJzyrzJxD5ChFP0f_fGzgI4asPiLe3iXuui-GY_g4zq0N6H1q9fu1H1dADOdRngKtj7JaQY5gEfy2w9aW3s-hqhJ1AeZ9dmKwOV-m7UtvkVBgmwNCRASBO4fh4tg77hHhxaOHNwJvSyQOJXVNAliBJu50SdQQJtHIoaV6GFGQbFqNDr7ZhqUFRZ-bF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW8j5B6OjG8IAfvxcERYRB-952xmKDCdVO62IcFw6GLurn6XkcDocbSRtQmF67HmA_pB7RcrtmIXUTqHuiLxaRVsaBo62K5dru1M6cEbWWx6z-T-Fr_bZsuLB_3fV04dPcIIiu8nL3okvbXciuJD4fKtNHD0RbG2CNtbDyhsadkQ8Z-jEwYW8AGXxn-ucuquyVQKcmm9a5eK43Gfeq_5H9BkOC-wtxa2IjWKfXja6Jvw53fb_TfNC2kKVzsjOEQlhP_Q6KkVNrCmJb9PPozVkl_n6_SnJJlkD6bXwGJ2M5-zypNTgDUI5f-VzvyAVaWisGcdVQfUEfzEa6-ra4Qrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpB75lS-E6Mgqk9wHAQ5QSV8UocjmU4gHWVmOwBa1EKEgP_D_pT21nzdQL0FG47Q03JFVpVh-m_OGptenzEyxNDtIVfU8oXhArfyD_fZX5Ln4kkoyXe0DCvWEcjdnSZgFnDXPbhzAcU4BO6CM0uREN_WzfrCjribSlEJwv7IvYFyw1_mvDuTTFiK7sQJKMrkj0DlYWNUCHSzFAcILOqzt8t5zULvbllEzHPyOeZVdzk37x-WTnoM61wQSTgV58EEAtjHwsGJNpBP2zEWKdWamKAdDORHAReB2VLXuyATSIptTwK4pVihI0PyzEMe44o5r6zOe9N5ftM7VUsBydXZZXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpB75lS-E6Mgqk9wHAQ5QSV8UocjmU4gHWVmOwBa1EKEgP_D_pT21nzdQL0FG47Q03JFVpVh-m_OGptenzEyxNDtIVfU8oXhArfyD_fZX5Ln4kkoyXe0DCvWEcjdnSZgFnDXPbhzAcU4BO6CM0uREN_WzfrCjribSlEJwv7IvYFyw1_mvDuTTFiK7sQJKMrkj0DlYWNUCHSzFAcILOqzt8t5zULvbllEzHPyOeZVdzk37x-WTnoM61wQSTgV58EEAtjHwsGJNpBP2zEWKdWamKAdDORHAReB2VLXuyATSIptTwK4pVihI0PyzEMe44o5r6zOe9N5ftM7VUsBydXZZXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHkiCGb63N8dD7_jW9hDHvWPgeQrmea8D1laONJnR0Nrc-GefUSU2pTWiw9rMu120bBuRoOODjtj519beg9bWrsDMs3JLOULhoMpXdpj7X6NqL5BWBZEYiFtVNHjbyBphi9mUzaSpXD1Mwn0CSLNvD7692ZUbFzFmxTq8WRN70WL4sw9PYafERb5F-anvcqSPfwZTobFAJEf3M1hFQYB3rCyPB5SMTJptBd1NJvp2Ciajx-Em4xmB4s3Sa8n_Ys4NS-obkSiATO0IvDmEXKp9MEXZ-fQRBDuBvjh4grvlu7Ooe_NTWK8pSihqY-deiK6ffyofeRMUf6zkt2OVkfJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZE3z0Ju8EHJ4qLo563hsvJlw4SWJLaeI7R78otp8oqp6y5-mq5sL9cd1kj_xFriHC3JypWfOjQYDHkNvSMpxShgT1MoqzYxBA9Nyo4e6glUbBOL0IzwtnhvMzPRAeHfIfDUO94JmYBkEVA8mz5M0kXojMv4TTu_GUHMnLi9-h0oyeRMyKhpJWBcUB7lWID-V811LXJZyYdsXPcBNI_pPCadAK59psOUMi4rF57iGoQA0s5prbdlVVIUTs3LmCvEdzSRQxFR3K8IglcmxyRRk_U_qpaBFLBUhGRw4FXoGAkSfIUTGEd84bE2_ZCz18GMfQxabXZQO6_8PBFhb7KX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRPbathoe15mqgF_8pq8ZbWebLB5XJ6a8-Em2K4OLnNKbYQHRAfRJI-ht5lS7xXbDBoBghFR8sufBoba-zBvyRzgSm-UZRE7e9lQ6n6_5fgOrblSiYmTRKAga03qqIsbg5NsD4ohFuCdrf3YPFUtwRdQoBERPmsfhS5aTfcqg3Kap_uikNV26cE72OyFwemM_b_iQhWRN82MEGgMCENlk4La98O-KgHs1xbdqxwp5afyC4boYAjeW7liO2a9o5m9amn6gnDxW7Sl22uNpbfjxRpeaioXIxmt8M58E2G-N8AW5KrusacPMYQkoQUtXhaRYDuhWhuh5trrHvpP6_hXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=O-bufJ1IjXL4QUvyrhlkr74Sk0__BjoPL4cabDK_CJ0FBmOJbHKW3EMK5izqhqPG849VIvqlUMGRYgwjZIflUHzLb1-46BNoxtIlR5fFwLv-4Kp4P6tN9YjeuaVcCHri4Uhm1MoR2wa6CVYJ3ujAokCrBiECqtVBaHLUuelQEw_J1FKyH62FY8pEhppOdOg7PUBbZi-TzNJ9gnWUx-3aPQhq0Y9QLxifosM3llm8D-a7qRFDdwV5EXX1qcmDfk70UGjvlpiTJBlvZN9gz66IhrHIkoKH9cKtSVMAkWbSUGuR8vH4TVa4hRjuzHaxQEQjNaNGxFCQRT2rmr8WKku6rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=O-bufJ1IjXL4QUvyrhlkr74Sk0__BjoPL4cabDK_CJ0FBmOJbHKW3EMK5izqhqPG849VIvqlUMGRYgwjZIflUHzLb1-46BNoxtIlR5fFwLv-4Kp4P6tN9YjeuaVcCHri4Uhm1MoR2wa6CVYJ3ujAokCrBiECqtVBaHLUuelQEw_J1FKyH62FY8pEhppOdOg7PUBbZi-TzNJ9gnWUx-3aPQhq0Y9QLxifosM3llm8D-a7qRFDdwV5EXX1qcmDfk70UGjvlpiTJBlvZN9gz66IhrHIkoKH9cKtSVMAkWbSUGuR8vH4TVa4hRjuzHaxQEQjNaNGxFCQRT2rmr8WKku6rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=kObc7WhKnAhlHOxki_eKbFGFHVI2b2XeniSBswKXb8V0mK52NbIIuK-n_MVN9yaBSFFID0CWNylojvOtn4l6IJDXbrgPvYxZSzrdLd6BwhD2p4-UFzSmdA_AsyYUCDJDO95D1aYD5KFrshdT2X6e5N61-8Yz_3AhroVHqvsH4yKqitIQF_N2MWu89YZb0rjdveGiklNic6WJtbK4bVWLu8GfpemIRaJ79knjDY2BPC-aU6FxU3E1V_Rko7S6eP74Vf78ZcRiK23MU7QsWcvEhP_BHJODyZiHwHAVEJalh6KgHAm3edMf9_c-gCuibyg5MsyFVV2V_8CH8o0uq6EXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=kObc7WhKnAhlHOxki_eKbFGFHVI2b2XeniSBswKXb8V0mK52NbIIuK-n_MVN9yaBSFFID0CWNylojvOtn4l6IJDXbrgPvYxZSzrdLd6BwhD2p4-UFzSmdA_AsyYUCDJDO95D1aYD5KFrshdT2X6e5N61-8Yz_3AhroVHqvsH4yKqitIQF_N2MWu89YZb0rjdveGiklNic6WJtbK4bVWLu8GfpemIRaJ79knjDY2BPC-aU6FxU3E1V_Rko7S6eP74Vf78ZcRiK23MU7QsWcvEhP_BHJODyZiHwHAVEJalh6KgHAm3edMf9_c-gCuibyg5MsyFVV2V_8CH8o0uq6EXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJXJe29tA-ILavzdeuDb3T7Q1t69vg097o1VZ9OPtpUeN4sqfx3MwzoI-bO4ymV0bTh5FxZmQDErBIe9tQ3RUTcxur_LlUtA-74-uR3QKT4GP1jGAshsB_2CeMLSOiwFKZV7helGjUfPIU1KA2coqgKVJpSX0krigh22efsrFmiXhcd1ploeaxWNlJwzI2zPCul2AKXwK35KR6MUJ3S4jRpdQj-TgVvBXnHFEsg4HHfrWwPWM0S4zd3SNoR8-AlkLY3iyaKJV_-MOLj8-4kj9lRITqmkAsSphcvVyBr7SLqXS6JN0_h7aYzQbRUJ4kJxg9PzgMgq_IwpyXGPL99FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjT6dcj-azbM9Ibd6BV3IUyL9lR1IQpKTFge9BhGdoguiWVyVY43eFHB5sZVr4gium1rRvCzLYnn-7VmRiaQ_xK-paX0n77wJ6tcyCeeS4PkjvVH8Wmkz4BYIalG641Q3E5kpjPWNdwa1-4kL17Le6m6MirsPb1Nt3pDkZN4t7OuTH9WgUCQWX5FHfuO7N70mqb8_4MPDVL3ey1WzMuKk4jBF8rMAXrFbVDneOz6naij_1NVWODGqY-ZTuiLaFBAeocfa1tfrmq2sL0ZojASPCrwv-mwQJp75BxWbO0etwuqe7iypP9LmqQKKXcFfTusvptt22FKfb9u75RKzhe3cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ceqr6ot2BsTJ-4NHczkcrBh1nHNlVXrcrn64tqn2wwKrOpYMxaPSCmQ7VrtHB8nNmU2Feuh6T7N-4u7WpdD8m1pjcMCK5Rfq3fpBNOIhDZBC0Xgp2DCLFUe1tFyPZq7ZvlsKGyP_q8t7ivdtPN_n5f_ilKySJXG9z3oo-n4UkxzYPpMEhv5OLC3SeMEZKnQhzge9legdBCM14D-8s5C2YZOq9n1hraZ5kQm8vc0EZr_aFcxqtisG5uCalnl8c8lvUJbgy8GFAGL0LWXZDdRWfFzCILYjO0G6XWXQx7GQFZDnfcPhgGb49e039HFd3BuKr6RumkZIjsqAmEoIbHg1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX8JK8OhoVNnboehYqPx6yEOcV-_OyYzJ3fMCrSzncLfNKrHXseuzyfwUYdmSMWFaZFoiwPAlu0bfWLVnPaB8PFrToGOOinZzc0eYOcs699Z6QMz-CJufdwyXlRFbdyH1KF5vfAMxogsta6KRkHjWR7x5EicnuV08nq6buM53ASdZ6jfSUK7XSNcGJkn6ihjXNIHEI56R472rey3wK4Q4-JEmLmJDQRvpRXc4UP2BxFD0rIlOLCzNfD-UKD7vL9H-Nez3Mh5erxf9O9g397nzn0POohqA1PgnpGOkmJVDefl7MEWpgZTz9Lo9GlnLeP16MFFNhuIGxYY0x0Y2ASWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOToikulDEJjuN2zfOzAB7D8BhUThLq8GgYDPbs4XsDwkYxs52hH61RCHfTcM13gDvCOa_unMMmZfqMazmCkRiNJJusW_LF1Y1lcrKhas27xER4fsG-AHcivqWv3rmp6he_CuBa0l5LowdSX3rLzqvv0i73-uhRSiGezEZuaECxipVVnnZyx2qQBkSP1BP-V7h3zB1y-d7r01DuQRlHD97ZCIm0Pw_f_T0OtyOBLDpDWbtjb83fn3poKLikDGZRkzEHXhJxzirbqi_72d9OTPTYHM6gXoU_pKUucrf5Yjh9gqcyyu2EyblR4tUwdGjYfsBWg2i1eASrLm4HIm-2K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnYEvwBTZFBiHjTPnZxFHLM6Ho6K-Oe0f0UACpL1y_o1yuwFC72zj2x-AxRqHDMDO9jtYVw6RicuijxXVI8xashWvYukLybhPbaCcYGMYsB82Bo4bwqawGoGCecC285s1OeEAbkV_U-_YRTvQXjz_8zC-yNFGeyPZBf4RzYqfxGFPoQ-KALwrk4LEc6DZ1nVA_VahMP-1WpJZNkmNKbhWIpgcO7cqIXAfSPMTrvJGo7fXcb9CkkjJyfoaqbVkMj5GOOA7Cgb82nBAbj7ZBhFt9fGmRXJNPyENM-tPJX_Ufq3bL-V5loAJgmeAgD1ZHBmoxxI3SIjNNWcrzvtEi2kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4gk6dXFInmDjsAp8piqULzLkYby0V80YUpN85Ve6tczEm9PJbeJ3yIU-Cb2aM51f1R5Pr51D8Ce3y6VYiJVTcWGk57HXarQC47xj78FespN0m1iwqIj0zfF8Ro5rkitEFHuafupNHWnfyHx1OetQ-9XKAw-OnFK1s3NIfNqfAlguvEnUcI5eTYUoeYftSrGMDQw3kyX0GquuQKrkA-V8jjmy9Vu112Rk6aRHgDySheo67QS_TSW07Aof1XhJ-Zt9E37cF5nD176cAlixqd55sznxc_Vbo_4gwW8lRaBPqZIDGkTizOiyEcO1Ui9UIWVkhm984QCtiSZjRUaczQPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWDIpbMmEI9bw2l9V_cfFsqo0N8gH_zJNyCw6UW7A9IsZqlQLZQCiytpRvlwox5dsXhYfgX9tG3ALi649gWAfb6cuvMecVMd9DGeNpfNHRf6sdOp8CyA9QerBXCPsStvSbxGgP98zRMn1vk4p5Uy0NFSH8n7cvC3DLDlly6SYY7Paut9oQTHWPBPWyfPmysZow62dwSIHPjuMEJYbg-pXm211QmhPIpXsXDEplMzpbGFBL-Ymuw628OP6UvAhEMwh8KvV3-HpCzC5iSJ9gPzsVmdhEWZOmT3yk3D_jC8JrMamNXasUxvmqjCfV0qqFnkpLhfyGijYU_HUtVmtLm6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzg8c_fdLZCTeDgctygY4C2EzJVqL9m_tGmavvtNqVCsHHE8sCrlwEvDX-lj645fVurJZM84sp6BPn8cbkAZnMgqYEBjV1Bt4iGiFOfhoBpNWlAUm6Ll3ArujnYc02QUXo3xsnNCkiWsLUefVaeSGzboMTb79WNIWwdWP38yBAi2ha2IRERyzYJ1i73k1PNg_INMRejAyL7Kh38eXfqSD1_1gFYxC5MSoHeWgAvz74LsKIsmIzhIO2EwmY9kfOUYq-fpykXPHiE0MAUa9rM3pcF4K_tJ1cyNreSuPkUYZDE88qUmV9AWUnTVyXp1U31X39wd60dYkjqdUzhA_wyj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBTrmIHCU0O3oHCoa4YwYBb-FS9R4RURaxU3nUbVcRfJLu6I8vfHssvsvNPaJEPqSMGvwypmbPEIcfuL-wh2gjsTnN819jQUHlGRuBEu6JpNGf8jrPSjuUfXvgWfpPTd_nGUTgkvGffO7mFhzR3gz2GPUiTrbi78z-Bt8ndgU58tENzhHBLEqfvEZHYdPNckb0kwr708XSSRB7hslyaA700QuZbgkaCAgau0nhgBe2fUuBs3951dXuu3Pxv-4aX62s4mC2zlDubCpN8juE5nQpDloqmIJ3Eo8UhUCsgn758T3z8Dhry2X_6K58qHlkSdWXUD3ZyxM-DMnjvf8mbs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2fDEeHJyWyiEu-XDeQGm_XJNfvaH3fSN06t1V3NZkdbOATnVScQQR95m30iJuoKlvPirMjBH4x3ccOSVsKmnamOpPVvUxkZmBwzGZVGbUXrfK_BA5-nqUs1v5ZllgpVy5phk5ylIl-qXbVJBmK8cK-AJhoE3vxC0UDoro4dR2h-D21psV9rE5BuFU1LQgZgkbJVdhz0E1oZHb6swLzydoAkqfVRHaSEowNqvVw_VLuWMjGGkRsxxPUfriGlFKDXMm8pMwpW7a9n1WvNhikPhThZTwqmkfUZvI5sb7aKosufTUmL130QuiBpdqq-VPLYhwcbevJKMmCeYFaGUQyACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITiMm2Fimyy_bi4jtD23fOvMP3BLz_mcfpSGiKTaj5A4_uxm7W4U73nHLAjqh_XFB6l0OrDukK_e0oWjNHm05I2-icOolleSrnYKkJBG_jL7CUdzHbhUkAGBRGTCVGNLbNi3JwyaZeb7JGP1lnq13dH4Auo0ZOcUqQmrl62LW15EoTtT7vmSE_bi1IOB2nnKe38h5uh32DIVo4gGe-jsKsRM3cLRHWkpOpCqOTFSEi7fO2SpnM-blgPxqxrK6W3HtqkIOUUYwO3sUDs30i6IKQ6o49mEe1YWXrKKMW88tEeLFK_aC6lHdJ4fYZhthv3IczHXiU5tzW1IAdwWPgMyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNMBWhHQbvpWQ7ZSy_8qrUzSc093TJwTw6uwlCFF4LwxMVpFX5j_XgQAm0ah8WuPLYAxTdN_jt5f2eQF7IgfqA740c-82WjrTP20lefnfhQLiBwK5oJYa6ea72RLzyxS4O1kbdkH_EDysB5yTJehYPDdVq8N-DRbfuujNHm5l5Uo8Tndy_GJXwImHgeH9N5ZyIAj6TIqakbQOy2GYBAefsA8HhUSGi462pdJcFKF5yLQmpbf-TbYPnT8a5Gv_1i3cV2wlz26VzjFOsj9Jbz3CBef-zd5nLd-cMAd_U4d75Fn9iP1NKw3X7MejdmlZ8LC2EazlMU73okskbrRFAYjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohoCMJ5STuysTEkSlfrzlPX5lY5SUbkdo8dEh3LJHT5_fcd1TDuvbUAQH5ENxqVHkeUWPSyjZ0kvv8eIlA7REDVOfE5Qsc8_VDhpS5nJpnjyqU6bkZJH6oPuF5fUpz927Z47ZaBAJ8m442QfaLrf2XG3jerD0MTpKO7dWmXyDAXIvvsZzGXYi_5oUFNH2hUxTO8znR_e7aOikePPS6AJjPMt631MGhn6VeHUZa6GU7CNodlOlXu0_kFtctlZ6ead6EKDO_-eTb7p_vHfkO4BSgsAwLOKA_1_7ybQg6-x7DQWrELucG9qCM3zyRrPE_I9MMXnDrfKbUdG-eN659b7Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2WV6LKOyBiQXNBDkapgT6dvUoxWjiSK9VIkerfNXedzj1eEsY6ugjt3yIHVT5Fo72hsW9GSHdhXcQqKRyBaRI8tzA2T93ijEwx7F7sM__AFIAjhzkSFLdZRfKzJr4ihU15Nh_LIW5Gctb9f1PLjsldjCC_pNghQ4PglBft6qt9364b-MbPG7h39nTQm0K-PuRQo_oiTECV33cIO1DR9XDRcSt4r-3Gw23AO96DL0zPNxMqcspiUsqd2HesL3X5U2iWHe10FxvP-aVplO00uG1rNwWC1kNxdKrGx6hpVgjknFV1vdD8N_UlIsrd5ZrX1V74mvfPSbHm_vFefl9tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKDHLe6rTksfl0qa3QtneF_z3iEnFRDlfxKbPsaGcQ-ZbBuBNZ2NsUt-usx7h6NzBJOtQQ4A9fRITJT4tQFJ6vLBbm9iVbiEr6wPqkwPMZ5Dswyij3mWnWUjDmVRzz4Cx0CNOpuakR7VwlwaImYCGjUjOqWRgIhumDqMt_0hoigjWRgGdwWEXH2QJBbM-hKNlqiDKXH-7BQveMmhdUEY_KrMX8wir8SiPEl85AyZYWGBeGVUn8DMGJBXELJryeeWQmEOah0j25nuKkpNQLJcX5uSrckY6hZh_hOuLcUAUJqb9_SSSw1vD21GO4BHM-B-RGR-a6ybAuC8XBdmoCv64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-qBdrV8kBGjDlFoo4dBLl564-87v9ZrvBMZPgR8attugzGKwVBFc2nikrdsD0ffAtbuz8rUR4hpSKtn2f3gEQrbC6Sik4ULehAMOlK7b2t9AyxIbse9muFWJ60be19GSWmqO1BI5kHuYnguMd2IpnY8eu_BQ0FbO0IJgvqtyG69_ZguRjZI9RXV8WGro14aLg4MpfbATsWmXzJTzip1WgvjJeYKkljR41LEDtIDP4BHGY84G2t7lhN1133FKzeeBm1cxhoxmP5qnangZ-3URIxjVUC-oiydW4Nz8rApse6Vtembk-uhctnXru7_abiqq40PDIQ8yOctIeNqlgYMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_NgVMrmE8qkSp7njggM2k_dQPByX1OPJZuGHv2uNp4lF43jfVilq27JnHZ14zDjz0KzvSnXfRe_kXv2G_HZvFwIVk_S3wW_V2OPOCPYYvpgtVuyFHm3BAcfjwxzls9e_u4skeERIeB0xxn_U0DF5qyPc2XbvERaxqpriSi64gbYBg1N-VI5Tkii9Jajs4xC1kBxXqZ0orQt_Gio3ABwJh_4v43BNY-tB-kX3V_B9qoSjLl5NcmIVxWzopfCLxVusMHZH9CUtSjZrArhyGu86P3op4EVuI7PAZcFk-JAJ6huZmIhX6QOHqcorklRu1kF2a1LQTTgzU9u92B7lnXeFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNsXjeEF3S27Ok5hRrMR3eFqwAKbU11evDDfHXUb2JGR880jlFdCnsPeqX8qY_w0MhptC40CDFA0CuLm44bajtoxB6UtEyV1V7KeQVLqdgiHkH-nTHheGSuh9OAXZv6I-CtN_YAjSO21XKy-Sl8qKA05Z0XexGccVnCgpWQHGFvqtQ81qbQ60oVjUgfsgSb3Pk6A2ddjPvrbR7yH2qrJK7SR0vUXf4Js3DG1XV1eQMUhiuU0AJubKMLYhwV8lbMIC4UOBX-AkDlrTNoxrhFmpD7NtLDBOCNvk8J3ZJHArQliwSubyHfPCeFDMjumo8BUW07MIzk-lPsxIyfowzldqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoaxXf4kfS2dNC1PWRCrZ8A6wAIU0ZTGx_XCp2J46FAUBDzOyK0Qkk2dcUn6bKhdYxZWqZ-maJG9wVCrk5920_2zkOwLrs1FfOgZAkO4wBCPjeLxuKh9wQuPDGQmFUqQSUmwZOHGAVDYHM6PP8bZlnQy2_tKRU4yKsspUUNjgUeUpZL1ERT_Y30X8-cjZzyq3jmkFW6cgZN8Ed3pyM1owbZuuBWjtveGnBpD5AW8uYo76BoibowTmQzErz_Cfx2hEJ3-7HCQOMKJD-B1YyXJQZvMp802bt4GOypkgf9XOARm5WjdZOadvmxSVN5l7zGjYGZRrGEOaKz0C4z3B_EUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJxwFX0v0UAz-oKuy3OwSLVhcRdQN0h6k_303EGb8zoQN1XkoS8angEE20fX6fD7MW4sesJ48AOHaKAeA84N0CzTV6oIznshC0HYEuV6u5Hf2f9STXuMRf_UmIhVLXjDd9WDD44llNZcDLr3L0hwUm0UGDeUStMho1ACvbxTsx2cO2xd6NUSheHgw2J6PTlZPg-BYQWzAieojPP63KSkFkZl5f8gO90Up2WeCAP6ZX9no9EmRH2O8HlrMwnOkXWTRa-i4Z1S_fKY73OgJA79ulUS5obq9Gn91jrFOtrUCAYRoev_yUfIKd8QVPpaa8LzKBNFUeJlV9OZtnKtOzO16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=eXaJoFI5U3eMM_1ulgRJuGwYDmF2rO7alCSpusUp32_LbgzoNJUwYp8QJd0YIzXPWSIAqSHzRBoxYIsgVe0G0yMt3rbinimIqSy2uI5K7MUa3j4DOuzF_Q_HSy0g1v5_Y-6k69SJahD-2Ql1d89e7Wqtvvdz21QZ4maIfuq3cPGISc5IVX_Aa2tuOCZX0JXUbIQvbr7gNkSnXJs73o2oP99g5BTGZUYmUmGk4pv2cYvaW2QzZu69FC2fFITreFx9su_Xoa1XNFJaIFzuXSQuGwEth4H4sqrIutlnOf11BZdtSXVLQIxbwTNKabHmmSiklAUCN7Vm0NcDK1dsRwj3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=eXaJoFI5U3eMM_1ulgRJuGwYDmF2rO7alCSpusUp32_LbgzoNJUwYp8QJd0YIzXPWSIAqSHzRBoxYIsgVe0G0yMt3rbinimIqSy2uI5K7MUa3j4DOuzF_Q_HSy0g1v5_Y-6k69SJahD-2Ql1d89e7Wqtvvdz21QZ4maIfuq3cPGISc5IVX_Aa2tuOCZX0JXUbIQvbr7gNkSnXJs73o2oP99g5BTGZUYmUmGk4pv2cYvaW2QzZu69FC2fFITreFx9su_Xoa1XNFJaIFzuXSQuGwEth4H4sqrIutlnOf11BZdtSXVLQIxbwTNKabHmmSiklAUCN7Vm0NcDK1dsRwj3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG9SPTKSfcQbVTRnmMdxyXXC0aaAZ5kjPYMm8uMdRtMbOsLEZsvqYsEthdh9pW1QU_3vB4HuTQU_4ezoE6wEAi1LH9oK5dd-ho-4d1KF-Cy-U99gdA-44GqfbRw_XA4dJrS0jj5yb6CicnS7Iy8oiAtk8Su5uDJ1ieRzknk1AxAl0QbSeMlwyCwf3xUMQMCU1S-lFFaAew5sLANKx_RxgyYkjY7FxPHnl7E5JtN6nVlQIQNXyrn1CCsIcKPIUpHYMhpMbCUxcQtlthcUfJ5pMdT5YctqCNV526fQ5kBnDl_vJbxtCF_FrCQxq_kbsq3Hxdl6kN9vDvlaacRtoa524Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9u4iYt5R_EXsnAU10UwLGeS-XLcmREMSF-tPno3_4ZG-cpf_uN-TdflbCs6lB9ouBTv_0Cv3riYg5-HZeqRoh7lDt4vKwmLumBsKeE5LYpzOmSzMvdEViuRr9-B08xssy-59ebfPxJUQF66y1dHJ_CQcH22Hi9tkShvaCO4maZwTnwuIQw8TKjKBvCHP1erny22Uc2i_G779ZnRjIT8SUE9U2VF40N_JXDok511PcpFyMRvFJI8hJCDKTBikRfTYEGNATn-NTuDMhnzbufnULIwVpChgoBM3dm729V4myl8Mb1gOLgafZVPUKR260DjHei7K2ApwsoiOGSH7WaGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd-_2mGSPnCaprEhBMX7TIpUYwg0_KPq6GOHYTBAAP16oegeny-sx_dJdLwerxzxd-LTaCseydF2jfJEqwQFSyJVCcZtb60_7BUZ2qQhzhlAJZ3qy-KgubD5Nh7jlUuQ2yy4dofW1pC-gNgVKibjSOLEnOXOZY0DXsPC_vfYEirHxhrP9RTnDeMcwpupB0r48_LEqSIIiA55e53FF_57Vw7mTruHZlzbLzsT2TcUQ5sP6gedpXqZJQUtiGI3kOOO_u11jrynqurxMFxlGQXIkXLt_9i49eSESx7rK0fAhDKq-imNpW-6821uC_3Est6QpvUuX2kAIuempU1bgJnt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiLrBkrM6pMb9RPcgJlxh2NGFIZYYffksktesmxAxikywRi03HT6HLyrKpwNl_MjQgJgrPqqq5K48dn2HZ6neNQb2vk66jH4VjuSxGb0Qza1HvnT77rraCfJD7KSMBGGLrNivCTBRorBfdgphv2pinY1UuuPItUwnLPj0hyKXhiOi8z09pXAFEPWG4xWapqLkfbzo7ePvkUzqmGGaiMLgHQho2fGhYhq-1tfVKIjcLfgKIvADP3p_Qa8rdyaPnoK_zmnmlEcCgLMN30XUBwaJqYsF6daPzSgMxuYI12S5ejJREJc2MsTPqfXN68lYU_f10rsltgDmrJWa4SzHNskTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJyeZYSqncwiBnfX4HNCpYHUKY-3fd9PCRUxxfC4vHATJJrzB0qquR5qEhEFh2ajam_6UNeIT0iWXmG4_LOQUE_Gj6D4LHx1edPJCWpm9fEPDDTaRBT_nomfLh3RKSvxAKrWVskNxp3lZmPChbCScWQzqVS98FNMvr786o_z6lA7kG69HIBtLJZnP4MH5wrNv-RvJZktwjsVd4XRoGbAryDK-LSfbV-_IygDzeGxRV1cE9yVx9qMZ5gvXHWQZenaG0eI2UAsEG9EwkSWdt8FIzhm0gUcRdWV9yoVNA534zdOWKqufZ6VobUP5EmDEsEsNusAYgTTBzNAigMOt3qfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0S09a4uMWXnNsLStBau0ToOavIh7Q6uGOLVHYV4uuPIDUN7PmxjTp5wPhIRsXWGvBwuvvmgWlA9Gce7kDpw4OYn4cu1HbogJYEhTdwn2MgyM84tgZElkUOgwmkuUvrCb8dWAG13ZZmDyEsR6QoboQuNRURsMxfehzu7VrwrdlMvhj3WJ8dJmQHDk-Kh19u5N9kwLlx97iPusjcCx8u-BUjup1wUpfwjwh6X-3cnOIWoJUi0lGVQi9FozHyqyKXeHSiQQDNJrv7r4ZjZ-_ruQzGlRLs3sDFrUOvcpsRKq_SIDxgd4f02dy39nQGKLzMEgj_UpNqWzprbm1niT5RWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU7nVVeWr7pvbEgBHBjb8j3K7zkLnEExNDKAzuEezwUTAoP4ZYTa0L-5UYYOpYxBLacvMzbVF167FnHAfyvi6hW5w3mzcnOlBCbdOUfHwU_CRfJwwF5lg2n1VwyIPMVTdxCbswWmGhj_uPCRcpDXj3787GeujTudvNtF-ooPgcSEKXpE7RaqqnSpgaxVqoWeWpb88b3vJuIuUvzNLEQ9wFSoyMR4h5UM8fy29SoZyDZIpJzHMJ-Fdg4nfI1ud-gl3I46u55KvWL_RFImTp4LkFmORN-pUlhcavSEILEDCL8ieaagrQ98S6WelhREuAurNHND7rtyWJ0qQS67eWK81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbx4p8_OoN18lldEs3d0BV3K3PfdnE4h4NXBEUmCuu4nvn1wLzRCwbmPYLWcliyYM576hA52Y06fX8F9_hYHF7nuh_91qZ1oVJ8ny6mSB1EoP4TvhTprCj3qpZ3dN5ob7I2x3pdMvnnhIH1anP6vKgV5db_IV9MfnPUz1TS67gEBL9XzlHLV9Laxj0NIeZptikvACUuHSJJCSR3k2I0Kl0JHtnvwdJJc5Piseil5JBh3kd5w9UZhmy5AR9p5nIPqq_d3oL9-qYhrEioMM_jDJMRdu5yaITCqI8-RZeEZfk8RrAsfXQ8Dv1mPk6ppZ5bYThd1_OYg_XZnMYDgDMrx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=qi642v1e4lUafME3gx_eM9b58iUsVcyWLYhRIcShm9BYdLnNo-PNV5hXHra9xusSo_hQGXd2k0Nd-A2i-GkL0tdn5Wg5_sBE_v23bNxD3ejFjUL0QRqmV6INBYCpvmWfI68rTFHofGeqbBE_SWIElCT_4I2HVIyvAT62qBRj4jlh6RnTZwFA7QfM83CyyDOe9uxZyAt7dLmLYXaUXncSsC_909mpLsbrcm0UAEQnDiGwAChV2NbNz9B2fn8kjHhewZhvyKna13CxSbzKdrkTm1Rc_KT4bb8qS3LqIOmEcaqOH9nxWjbEArkM5C3y_5F8BtV28-X3Jc6BRnuY9JtQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=qi642v1e4lUafME3gx_eM9b58iUsVcyWLYhRIcShm9BYdLnNo-PNV5hXHra9xusSo_hQGXd2k0Nd-A2i-GkL0tdn5Wg5_sBE_v23bNxD3ejFjUL0QRqmV6INBYCpvmWfI68rTFHofGeqbBE_SWIElCT_4I2HVIyvAT62qBRj4jlh6RnTZwFA7QfM83CyyDOe9uxZyAt7dLmLYXaUXncSsC_909mpLsbrcm0UAEQnDiGwAChV2NbNz9B2fn8kjHhewZhvyKna13CxSbzKdrkTm1Rc_KT4bb8qS3LqIOmEcaqOH9nxWjbEArkM5C3y_5F8BtV28-X3Jc6BRnuY9JtQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
