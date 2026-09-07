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
<img src="https://cdn4.telesco.pe/file/NLRxiNNJBocQNzHtAzunIrEE9LkykRZvy2Sl_ZdG-VO4V0edKexSBP7ls4IWFEuEKtCMUTYMHZZuvJoWOke0OSaiXDKRRTdF386sTuZS6qN4DeWWdkpQGm5UuZozkXd7AuFTvHXt3d6sVqHKzBSlIwryPoBW-Ni6I3iXlEkZl6DQGyzAx4Pe0VfxLplOrInh9Z1b8gMjHEMEc0cYBLpoLk7ivneQg-AmazSElzDYbFd0b05trXfhbybkNl3HpZ2K1ffIZvo0knLt11C4LXniCcA_cOs4u6jKaBU6fQUeEH1sVzb7ntoU7MMMWwWyzx3X6cBS_SjfUCnpS9c0X7unhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 02:24:48</div>
<hr>

<div class="tg-post" id="msg-460798">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/farsna/460798" target="_blank">📅 02:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_nQ_Kafdngh6Sw17perPOV6aRv82OJlasiJ7LR5wL_qEATKVJ8Z8fYg_tjCNmZVjCEu7sHUYXI2zM3RWoxkdcyZo809uunRz_KAQCdwK0PijFQJYwek104lyHIWFt7cLCNtcgflbGfHyRRBB6hz8ik_WmPmjSa8gC8GPEqUI5GbJHZ2KzUda-3yY0DLX2jIl_4LjfSxnEZP7jmMX6d9UBBuDQ2litKd3DNjkJFKXL46Ot3F8LbbgIhAhQS8pFwyoO4zh75fmYKrR83873MfeXpON7A-agtS7cvSaPbE-2OzgLysuibr3OUFpX5tBOSJi6Z1E1x0EArEHNetak7E2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQ8vzfioO7fNfFwe-1h-71kdXvsRzzqg-BXC89DWAAkutjgP8xTrHV9y1ueUomiL1_jefbVlUPK-plsxItyzcT4efJWbt4rAkLbzmT6i_a8sWIWQGZZ8ISrVtfAYJw5mLiqVnKNEOGaYxNu8saLNmKR-uArKE2a4VBnlyzZGUGqEueQK2ZkHbOvv3pi7vh-by1tpvZo8DfCGNBK38otEqVvAHXrNI-PDHXPa4gNf67M6y496IpMOzvswRPbTBfyqL2QQizW5RxNu7hZpJjOrH0jnChQb1xG_7m8embDRyzEgtHRk1IJpIbsqKBWbTBhqQCFs8L9w0bjx1-WkUjdfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhPJqW-MxWSGs74SY_YU305gXBJ3xM9pAvacANaCvmne1sMtoUrjVwFvUpGe6lHw5bmvant5IXVk14iBw97wJrx15V-Qkh93l9kXV39s372MZIcO7hWA08qs-Mu7PjjVkKGzwYosQj_JOMWDKCBteubyszJpjoyWHMtDpdMWGx0QJkER0LC2oSuf0uf00NPFL2DCDaXyvYdSoHHlFqSpkN7g1SV8ugtMy_5UrNp1OVwT6CuK5vvjTByleuPJThV6KCxHV0VHD4BFdvMM130Zy-JLMguFE8mVEJq0jhdfiBICMPNaTkIlSNAhPTaEb461SrSNHoyUYuFp4Y-OHtGFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpkZd6vvJBfuOin2kbkKE_7fmiT0flKYuh3nOHMFXgt5-98ZtNNE3MZPJSIFyaibexUq9ZDvgIx8tQxCoh0kfI6PAhzXHJNImM3tU3nYVLZfYn6MOsIXA4JNRinw3RKBoHbKr8Pl18lOyH-Faw4EHR_ZSIi9hTvTxzXRirPEQJ2Kd-0qIGxUIZzgxHqAgsd89yLi-OZO3agQU34Hk2cu-X-7j2YtkDWXR8LzsuWVaGCokD80IEMHulPnUwhQJFMoLq8qLhLqYI3Ah7J0zjmHNXTooRCyh87wPd8qG-BwIqngFd6o6OR-KhqZ_aQ8aVkov4P7mLziUJsG8fqnQTnaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nywRlr55aG9v41ZbmF6726Iv5ukkI3YcBmIOzKiA9hY_5yuWkiDnOkPjXY-7jIfV5nW8LPVoEyXjZRlcsFV4l4eATm3OM8UZA9WZUbGz5aConUWt7u_sLOWx_GiyrPPQW3iXHg_XdfogA0imk6_VuwWvq5ROfJvX3epfx1YoDP2T5XSwOQVynLZ0_jsB2yotx3pxNcI2hg3l8qLZossC-KLdowQpP466sbhY2kJ5Q3bNUNc38BvYBUZVzEnitaJhg8WvHx2avjB4gm0wr1vOc9jefWvX8I-vqZZ7CnSuh7hxh7MLIFCW32eXM-4AU-u1s5WMDQOoIJU8EcC9AwbXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYW27jlO-swUfBFUCPORIogYVs4Bp3Le1AMp9-WRIGD8Sk2SVKg01WdYxPiOJ8HVgmBCsUR0uVMgMsvlKQU3hqm8LXPWRswk2sMMloI_lAH0FlZExT3HOwLCVPj-yS_UTVYFHGz0e3Ivk00V7zp0ZWquWGTuMRjBRReERTCJxe_sy612P2Aq5sUFrb0StLeyzfJ-qpuQsom-cfKUcqiVo5Q_ZrPQdBnAOMmc8whT15tNW1BwMTC1Ztovq_8-Ig3fR845jIXrd7YdouSwc-0CHSjS-BFWHeRz96XwdHFebXBSdhxfq-h67XiohIXxFHYPQdbU1pgPuntxxBugvpjA4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۷ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/farsna/460792" target="_blank">📅 02:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460782">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Evry_tCKFhOUbkD1x6Zl8xnHxKhex2-Pe7A-boC2Q7jI52JGMJVG4EzfWQ5wbWg5sD0V_qlzdxEfTT0tCnw7oUv2dEKmowXbzkCbiNBKihyoAXLPuiDYY999kmO5OrfkbHOsbXelvJ5EjXW9oXcRcshRguVr1s4TpQVxhaHZ2H1GjCDUHuMgvIYeRN-zsf7VsjOgLgwNa6P_5GrypsNnqBCgJ4iecgjBkoqsOt0_Y_DzQTrmfuR0Au3zABaHyI1_2QLuuvxkIKS-JifnV_qWRO3kbhrLFWUVmNlVdOeFvkQ-vkdzvx0dhzXSUtcJ2CSXwMGOpF3PqouPI9mA-VLYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uH_UvHkeL9zBKiib9orLZMq-3gu0L50v4Y0il7grVpZjl9IqH7XR-gVOgydcbEoyc6PRygiUUV_EHKosCe7aaVvSFJkSTy1U-YZAp7sPQGbjYLtDm17mHg8HGS0PnmR9Wz6haiPMiVz3F_OTZV99ixPO_uwF-3cYy529JXfJRdZ0xz2wKg2XLl0g7ICYsxDyNLg8dvj2Lt_8pT9phZnPLM2vPh_g1wSeNA0Yl5GrBmBhya_iEnBraOcY2wgJGbET0QWkzvMZRfKnFTynSxp5g7ht3FBKZWKVAtFoS3gSVTo3MLbqlIXNbdFIjH0eGN8wE1wKdLNgBJiDmsn3e59TXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSaRW8fu6NOnXqpLM-FgsqVdbGHWfGFqQmDqJBwPW0f8C933VG14aB0w0RdwXnzdJ16rya0nF5V7iACizrs2x_9L4D-yNE0BCz3Ec4dqGs0-BHxVgWd7vqGgyLepcy1VRTjsmBQnIzz1Wt7RWZPuOQ4CDGTIbuIlEoynYO6_APDjgmrLmzT2hg4OGp4IzXCquAu-gEJ2ArEjAwa_CQlRoHUFVrSVOxG2fstKgMmv8bw88XuxI2J30eW2s1tfCQimKC-PKaLwKgM3553s4xlVC_5X4JOsJJbmsgy5dLzW-7UAVr0NRB9ww0HRmFmWFaYKukNNwcinRC9GmTSsBqGlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdsbqvl0bHqCGh74MRqJ4bm2W7GRHjdQAhmX8NHjqe8REeFyarTBghZq8hoTpBYRVCZrJEFjdIbNQX-XNS_QavuGkr_nO7uE7n6gBS0vKGcz3BsgeGaDrRRdlTcVt-Tuhb6o_s-a4_iKZGk3Erhpgsz7olXmI67lqNe3CoQ_us-iwRh41ReNU0nTHGT9vEnTav5YztiZ_a3XgiBNP9KIQomUrzXoWI3F7ZQCua0ON62vxpVGkYNtEUUY2Hq0iKlVwXxLiDP64TpXo49nyVc-vWHM1x7NceOp1v05aKlpTk6cREQaJ904bHqJfF2OlEZk7jpQA38tzHIPd_b9ED3bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SesZeH3sJ_P76yFcDd0TJfOhYZ0DDSR_M3IkHj9Ik-DDTSoV2K9he_wgJXPHKsezGqfriMUQi-FUqlh31Z7s9ut-yXPypNwQYS3jyOl7y75uwmzfSR3ugLzhxHelEx8_Hh7n7NaNGQ0fj9oR-y2YMBWtJfFibzab33_-HhlfXt09KBdWsnws9vV7Ar7TKEC2oPFxU78ZlHP9JvESB72JdNqYxrbw4Q4GlLRhUsOq8Ms0v8FEuI0UBbl6c1jLwcdSIrOffBP9mZndnVouDcE-_Tp0GbazD5BtX3Tes0Egp-U50iajRUsuufxXi56Lj6-FBEeLGB87TSTtxjvVdXsHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWtyBxDYE6i7YLhCDfGEzqTkGmexl_SiRyeb6OVFoVJEtPMiHVKXcwpFEEqFl-nBiZRIFGPAftgRnaf3f5z2AKBCLEjl0BNT6GXBfbbVYVvkDlky9zZ7bPXBs83oxduTNnUUK3yAuQl07fSkcNHQFOXaGG_GuDo5EG3VqU-bCFZx_Ka04BnTnxGuIyaqfGeqh6siDUqAwdmPH9yMiD_bmnUId7Bhbzb4B0egR3Thi63eOatFXB6TTvDgdyOxtSeBuZl-M5VUopAAzaLBZ7t1ZAZOfDUETlFaP7KfN1P1kePwEagt4SLdtMBn9GBd7snglmWU8W0o1uaok4n8i0QhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txjesPwApvU5fKAx5-SeHZiW3TPcp27hLBoHRQkXiDatbIgekdqLDh1kUgUkCHGAOjaPWI1odeYNWGwdWQYUx2eL94VbwHF3nA9OeUv7umioUjY2_oQl6QqXbpEAz6S00TQmqDxGiBaFATqtlBTaMkx7OZETQbuwbTGGG6vZec9D_PafseRZ1UdesLEqgAXrXD84rEn--Lj8soOW2qXFF6ODF1eNwX1lamkbFrlJhzuZ9BWq_yh81HUzFfXK6gOsqI4X4vTYrA5Rf3JpE_C8u8-REstRC2rASkTBhCx2vaYdgHSl8kecxx-S5SOlcHzbjWbXVhlD21CQxA34Y-fy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4IR2oq19w6_MN2aD1nPd7DqXnu4NhdvBeQca4LT-SDlEmmSMgKt0ABhrrlLHNMpk1Y5Zu86UCX_YIUiHSeS0KejCVyRqQq5MQ06Zm23Z9l40GYE-0DQ4dA23ZAA8RT6tDjyfMO9MWYAkRxb78ZJ8YfafbWZ6zy8IEasKVFz0pn77Hk1W6mUtw0Wget60JCd1xIyTnnPh83rY7W-4XI0txBPY63djUL_Bwq46FXSHqTdTjFo9x3DtP5Ef_oZuYYiV3Cmc-yUlHFK2wluotmlssiUY0MHZRUU3hqCsORvpdvG2j8qW7driNo0Yqo6k-VPHPq5OIuLbe-Vr_sKvQxcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUgT5tu7mnxPG1hjOO6lSzw_VKC9M5b7xZ4qmc3Chydjk1RNbamZhg8NZcdmva7Vxxudi0lLzqYRrAaVTPqOOhTEi0YSPzwsE1TGsuJPsNq1sSnedRs1yhY8vTDwZs9CJ8evpTY51S-zw3SUf1zSxGFRDrHP5j4Cu6_ru7auf9FqX9THZzztQPzud3Lel_z1SfEdVZkgxyNDwYFEq0xN91gX5lHqudDwFendtrbiQrtnhraiAJhmPpu2_QslAoGGtI0__cw5XVo_uwalReQQ-r5-4Vj-t1z_Q4srldIdou0JHbRrw5vHAaWTIkeYy4mpES68WXX638RMrqFQxMWJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRbqBkAAvdOFiK1mbFNxSxzQAVDYnWIPKKub9b--h-Y9Dy6lnioTblgRe4U9cbwO9bC5uDp7hTr0ki5t-WT15SS6hzc2hkGHPe-MBGxEasD5UA5ulk38y7qb_7UWem9Q5YA3Y3X99DgyxLiK0dbnj5dseIcMZfc5sUXHngt_Ns24tz-HtCozG0dmmdkEzqydjNuw-SLVSI5k4ZT5bAIswuW8yXwmcBZI5fLu-AfwUbULGQalokRtrgbJ5hdga-8Sje4VuwntYPEWOlrkUKOB3n8xxZknOW7B2AiXEY9T2aBg3GrG0J0ySAnsxxkltSapwu3mBydIa68oQujBVk_j7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/farsna/460782" target="_blank">📅 02:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460781">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/460781" target="_blank">📅 01:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460780">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef62f58031.mp4?token=vn848j7XmA5mF6TpEABG0aEIg050EkPrMFwtmXl3SrBcBAyWMRQMqxiQ6DfIdgCK63pJT7Xy7kK-Oikw-YZPZdw1tAwMPntIUlbBZ95WEeu4Mmi_ROexcPJx-xHAql6S16eET97QPlShW8ny6nVhVWxiV2AD1UZ3VF3itJY1eEECxS6YPFvu4oDqnXdAlUq48orCcLmdhUIrhcl876j77vdcPbhn_wRw3fk9YwUAbDk3Qz5qryT9HkgyOvHoSbdoZ_bDzsh1voIfog8LvorCC2penVgiM_p6F3OZZbPzQRWoshGP7gx2wKRa0Kf-N3c1G-rIeKOGGRlNfAhItPlZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef62f58031.mp4?token=vn848j7XmA5mF6TpEABG0aEIg050EkPrMFwtmXl3SrBcBAyWMRQMqxiQ6DfIdgCK63pJT7Xy7kK-Oikw-YZPZdw1tAwMPntIUlbBZ95WEeu4Mmi_ROexcPJx-xHAql6S16eET97QPlShW8ny6nVhVWxiV2AD1UZ3VF3itJY1eEECxS6YPFvu4oDqnXdAlUq48orCcLmdhUIrhcl876j77vdcPbhn_wRw3fk9YwUAbDk3Qz5qryT9HkgyOvHoSbdoZ_bDzsh1voIfog8LvorCC2penVgiM_p6F3OZZbPzQRWoshGP7gx2wKRa0Kf-N3c1G-rIeKOGGRlNfAhItPlZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل گل‌گهر منکر شد: هیچ فحاشی‌ای از سمت عالیشاه نبود @Farsna</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/460780" target="_blank">📅 01:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460779">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca35906779.mp4?token=Yfz6BREP8Yo_iRkU84erE9OIKg5VRDQCuAmEdxUCnxNeFkLmJFDSm-J3S5A2y4LLKRmGuwYaZ3O0Y1nf4lPZH0vDw3DMDHc4Me9A6eN_Dc5Guk0sbn8mcMuVaFkPb_9SKcIR6d4iZ_348M9_KXRJsZZsDM3qFIp6iX7OUGRFhM9jgzpPoTThXcIFH_qhhf0dQrpkQr3v-s6B_ViVvEOwsaej-t9Zt--bwLcT9ubfNvBIx8VLmQwdVfOI7rKH0H26Lr-mP357SU9o52JYfTlzysNi_DlIJSCWyS26JL-N_93fDjsQPb84cVk__EpbOMMSaNRVAnxYZFV9qvT7jIHEoB3pdR6kHacIcs_hNSZTVWGL3AlokmyKT2SnmYtIRvxQWd__g0zk44rWgpfS_uqksKqQmUQM2tTlj1k7w7_Um64aq4TjkbJtHhbnxh6YVasQ5vMJiwaWV15kOdsvzQGD6qGPKdcW20eUO-vhoN4iZfNcDiDTXAMcNx89JL9fiw9G3sPb5hGiqPBCGMR5moY--YGXCIkdqylTBqhIp1EPQPVEBIOfEcq11j7NErPWiUKWDjuuIgeLXa5FWOfhRW_z1GzNyjUYB4faR8fdGc1Oo1UfJ_rjK3oNEhQtJXYSk1l6CeqT3RxkGiC1g5PoDq9FBhmDhUPXPq7WgHFfjQqyDQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca35906779.mp4?token=Yfz6BREP8Yo_iRkU84erE9OIKg5VRDQCuAmEdxUCnxNeFkLmJFDSm-J3S5A2y4LLKRmGuwYaZ3O0Y1nf4lPZH0vDw3DMDHc4Me9A6eN_Dc5Guk0sbn8mcMuVaFkPb_9SKcIR6d4iZ_348M9_KXRJsZZsDM3qFIp6iX7OUGRFhM9jgzpPoTThXcIFH_qhhf0dQrpkQr3v-s6B_ViVvEOwsaej-t9Zt--bwLcT9ubfNvBIx8VLmQwdVfOI7rKH0H26Lr-mP357SU9o52JYfTlzysNi_DlIJSCWyS26JL-N_93fDjsQPb84cVk__EpbOMMSaNRVAnxYZFV9qvT7jIHEoB3pdR6kHacIcs_hNSZTVWGL3AlokmyKT2SnmYtIRvxQWd__g0zk44rWgpfS_uqksKqQmUQM2tTlj1k7w7_Um64aq4TjkbJtHhbnxh6YVasQ5vMJiwaWV15kOdsvzQGD6qGPKdcW20eUO-vhoN4iZfNcDiDTXAMcNx89JL9fiw9G3sPb5hGiqPBCGMR5moY--YGXCIkdqylTBqhIp1EPQPVEBIOfEcq11j7NErPWiUKWDjuuIgeLXa5FWOfhRW_z1GzNyjUYB4faR8fdGc1Oo1UfJ_rjK3oNEhQtJXYSk1l6CeqT3RxkGiC1g5PoDq9FBhmDhUPXPq7WgHFfjQqyDQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌های مداوم شبکۀ تهاجمی دشمن، چگونه کور شدند؟
🔹
هربار که یک پهپاد پیشرفتۀ دشمن در آسمان ایران از بین می‌رفت، مسئله تنها نابودی یک وسیلۀ چند میلیون دلاری نبود؛ بخشی از زنجیرۀ شناسایی و هدف‌یابی دشمن بود که از کار می‌افتاد!
📝
برشی از برنامۀ تلویزیونی «عملیات…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/460779" target="_blank">📅 01:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460778">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP0YZbkZgDM0IcEY-nnDJpUdrtENQj-niBV3rLbAThf8GsskUGn3-N8zTqKLeSOAeL3kPjVFSzSg_tyiUBZlaWmrbbnUPp8raOZ2cG8kgzih09BRBQNXvXbyxKt-zj9j1KX9DsyDiAvwSkodWRn_1GEMgYNBoCvL0OZS5dwG7iPEUbhQILKvp1xbDuJ6IU5LnYGf7o9QaQdHgfrBQBTrvCl7O51XmoOtX1tX_9RIfk3cs4i9WMzPGL046Q4lDygZt0wkBnzCtNE7y2lYnJ5wPu4u7OhOdx0PC_NE78dTGC6PLnd_9EPGeUMfTqxb6G1SdRD-pZzkSVYxzSwhfwsOqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای عالی امنیت ملی: جنگ اقتصادی با ایجاد منطقۀ ممنوعۀ دریایی در سراسر خلیج فارس تا محدودۀ محاصره پاسخ داده خواهد شد
🔹
سرلشکر محسن رضایی: در روزهای اخیر، واشنگتن از موشک‌های جدید ایران هشدار واضحی دریافت کرده است.
🔹
موضع عملیاتی علیه کشتی‌ها و پایگاه‌های نظامی آمریکا، مورد بازنگری اساسی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/460778" target="_blank">📅 01:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460777">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161ec79cf3.mp4?token=ox7YoHrsc2vhtewO-p4GZCCGNchi7lK1xN-gB6V7OH-dKbitbcZ1zipwqmdmFjyZtRTztlvxv14Sdq5mzjYVza8laXvkTGD5oVgI7uoMSO4LyttiRKinEue7rx1JHQkt1aq1wWJ89YsLdMauitFste9xdn22eQXGvw2YUhgEJ-2f28molrSAuAJ-o6n0gbckC3Z27YEUEstBwenqfELVOuCOxYx3mXDlleyAnnDSWERLb7AZNPSICb7VpLDnTs9FhB3-3At5aGFVd5HCOlLjixXq_pt3whO5wRx4aDIlUMrka1PzAIzOY23ucvjCbYyvmmw67dnSVn9eMyaKc8gOcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161ec79cf3.mp4?token=ox7YoHrsc2vhtewO-p4GZCCGNchi7lK1xN-gB6V7OH-dKbitbcZ1zipwqmdmFjyZtRTztlvxv14Sdq5mzjYVza8laXvkTGD5oVgI7uoMSO4LyttiRKinEue7rx1JHQkt1aq1wWJ89YsLdMauitFste9xdn22eQXGvw2YUhgEJ-2f28molrSAuAJ-o6n0gbckC3Z27YEUEstBwenqfELVOuCOxYx3mXDlleyAnnDSWERLb7AZNPSICb7VpLDnTs9FhB3-3At5aGFVd5HCOlLjixXq_pt3whO5wRx4aDIlUMrka1PzAIzOY23ucvjCbYyvmmw67dnSVn9eMyaKc8gOcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل گل‌گهر: چه کسی گفته نباید ویس خداداد پخش می‌شد؟ اصلا چرا [چنین حرف‌هایی] باید گفته می‌شد؟ فرار رو به جلو نکنید.  @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/460777" target="_blank">📅 01:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش رژیم صهیونیستی از آغاز عملیات گسترده در اردوگاه شعفاط و شهرک عناتا واقع در شرق قدس اشغالی خبر داد.
🔸
دقایقی پیش، برخی منابع از حملۀ وحشیانه اشغالگران صهیونیست به این دو منطقه خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/460776" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
تصاویری از حملۀ هوایی عربستان به یک زندان در استان الجوف یمن
🔹
به گفتۀ منابع یمنی ۳۵ زندانی همچنان زیر آوار هستند. @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/460775" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460774">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b379af196d.mp4?token=umqEE10qSgyc_8e0_9pU1fbz3xHtU0i-h193AvUP1BxfCYwOdDLgxndR7hwRp76qSJUqKrXyp4a4L4kbaQ1wxK9yJF_ul1vmMFYgfjRSYxBcv0IQtjbx7KreL9oQwFdm4azfX76ITPwEZ3rVVuNFVL5OL80w6eZMSOmgVSut54N-_RDKSpN8wtRT23Hd5S-StyIoP2k99uAHd0gjZck_t7Jc8PR5J-_dS2NKexeU-1Z2u5dW_4tC_OvMeNNRqnlTGIHAlclP6aj0z8USCbezm8i6hzxsPZ9VMKvrpZht6-MZjTQYIYMloNr-cOwHi6nDtFYNWgSYGBNnu8ddiqEYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b379af196d.mp4?token=umqEE10qSgyc_8e0_9pU1fbz3xHtU0i-h193AvUP1BxfCYwOdDLgxndR7hwRp76qSJUqKrXyp4a4L4kbaQ1wxK9yJF_ul1vmMFYgfjRSYxBcv0IQtjbx7KreL9oQwFdm4azfX76ITPwEZ3rVVuNFVL5OL80w6eZMSOmgVSut54N-_RDKSpN8wtRT23Hd5S-StyIoP2k99uAHd0gjZck_t7Jc8PR5J-_dS2NKexeU-1Z2u5dW_4tC_OvMeNNRqnlTGIHAlclP6aj0z8USCbezm8i6hzxsPZ9VMKvrpZht6-MZjTQYIYMloNr-cOwHi6nDtFYNWgSYGBNnu8ddiqEYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل تراکتور: کسی حق نداشت ویس خداداد را ضبط و پخش کند. ویس را دادند به شبکه‌های معاند، اول آنها پخش کردند  @Sportfars</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/460774" target="_blank">📅 01:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460773">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvsP3GDN8VPZxkYvebgqHcRMI_b68O4hIuXiCRt6Vnm21oUvVHp0PHefttKobQgvbFqd58OtgUitXqZakrosbwyqO22rPmqq7Z8oHimxLxDXRU89ESAd9yI-8uYEqysWEzaT0Mqi9LaySiGsWyTQR6Lrx7NevH7GgDHN7-ysz5h4diX_P0GPqX1_GYxHVJeMJA8tZoz55IWeMtuJUqDKmzWhPaIT-Kof6dWmKlQsISGtlVPWw7XLbEwTl19qNuRxiZnV3zRPW3NN-DNbU12-PBW_XNvkvhrVFY9NiE6NXfDusU3V4UTdz-EpAr1OJbduaP_0SZRae-FcH1Tp9hexOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تاجرنیا دربارۀ اعلام قهرمان فصل گذشته لیگ برتر: برای احقاق حق استقلال نه کوتاه می‌آییم نه خسته می‌شویم. از مسئولان سازمان لیگ و فدراسیون می‌خواهیم به حق عمل کنند.
🔸
پیش‌‌از‌این، سخنگوی سازمان لیگ از بررسی مجدد درخواست استقلال برای دریافت جام قهرمانی فصل گذشتۀ لیگ برتر در هیئت‌رئیسه فدراسیون خبر داده بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/460773" target="_blank">📅 01:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460772">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fec0611a6.mp4?token=XXU3UFyJv6EcckHfXL3RjhejOCjgSD1PZqpgfQZbqRDSMkZ1vmWwS1Rugig3Bn0b3IIkiejTDCkIQcBz-RXiURKCvnMvK5_oujQP-rMDw0RI2DgSj_JT53Fd8_Wa4AXahpOkDqiM89rC0AFHtcWU-bWxMa-sWxwD7jPUzOtVw9bPNPB-ClAG8ikHttMKS8PLUnnl66rrFNCxHguvLC9Dkwpqtwbx56_nil9zVThrUDhb7Oc18k7tYsqA-CU-IWfDKMWwkZMiUphX_gEmx_ydf_X8iJvTrVy-t9i5ks2540wGj8s1KAF8ZBkDz9kylL3vzosjmQk4qSRwHDAizIyJegsOtLvXnZaMo4hrSTaMQEynoL_zeWS7fK3JxmfRM6u1-QI6HLgcOEkPBELysjI7sOHeN-bEzKbd-UOr2wGw0EoUlhF1SY_JvbG75BS1hclnLKfqQdmbdjThWb4X8YgLjdHpUOenfYxIGHVPVTUHape0lIHv3Mo8KFLowtLYC-FXZ6yFFymGKuzSvk7qSYCvQjGvAiEQVNM47FgDlbEiYQfDH-UTxz4FDiVK7D2DSOr93RG80v7FtHS_tn54Qt1jr9MCkyk32qFSufArB1jgFtG5oINbgTlJVzbmP8IsZvLSJ8VB8zX_6G3YLipzJThXv9crSR9kMZM0BqE_YNDhIHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fec0611a6.mp4?token=XXU3UFyJv6EcckHfXL3RjhejOCjgSD1PZqpgfQZbqRDSMkZ1vmWwS1Rugig3Bn0b3IIkiejTDCkIQcBz-RXiURKCvnMvK5_oujQP-rMDw0RI2DgSj_JT53Fd8_Wa4AXahpOkDqiM89rC0AFHtcWU-bWxMa-sWxwD7jPUzOtVw9bPNPB-ClAG8ikHttMKS8PLUnnl66rrFNCxHguvLC9Dkwpqtwbx56_nil9zVThrUDhb7Oc18k7tYsqA-CU-IWfDKMWwkZMiUphX_gEmx_ydf_X8iJvTrVy-t9i5ks2540wGj8s1KAF8ZBkDz9kylL3vzosjmQk4qSRwHDAizIyJegsOtLvXnZaMo4hrSTaMQEynoL_zeWS7fK3JxmfRM6u1-QI6HLgcOEkPBELysjI7sOHeN-bEzKbd-UOr2wGw0EoUlhF1SY_JvbG75BS1hclnLKfqQdmbdjThWb4X8YgLjdHpUOenfYxIGHVPVTUHape0lIHv3Mo8KFLowtLYC-FXZ6yFFymGKuzSvk7qSYCvQjGvAiEQVNM47FgDlbEiYQfDH-UTxz4FDiVK7D2DSOr93RG80v7FtHS_tn54Qt1jr9MCkyk32qFSufArB1jgFtG5oINbgTlJVzbmP8IsZvLSJ8VB8zX_6G3YLipzJThXv9crSR9kMZM0BqE_YNDhIHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارزانترین پرندۀ ایرانی، گرانترین هواپیمای آمریکایی را نابود کرد
🔹
انهدام آواکس ای‌۳ تنها یک موفقیت تاکتیکی نبود، بلکه نقطهۀ عطفی در معادلات دفاع هوایی منطقه به شمار می‌رود.
📝
برشی از برنامۀ تلویزیونی «عملیات شکار چشم عقاب»  @Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/460772" target="_blank">📅 01:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiZJR-RSskvzi5K-jDWRCXYtrmqQH_DyGIL7f5keZNyktNqUlsAlwLW8ZRMIyAzLks31irDw4Wkif7Zgvd1TXPstVsy4D8F5BWxUuQw7sT4BQTaDI8k4cc9KGx3AK4QYmEo6Mxckt3jAb2rgJJR81IejPrJIuehUK4LJVyPfcbefbBGyumG6pKRClNkvSRznLKE_hl0S--sYXAPAdqouW61jfRcb0k8fwX8E8n1rc39pXeNWEiRjTWlLje_MFC9deXvc-wNEOQHxV8g_YmXJBgmEN3BZGy8nzQbOFt2py86mjZL53klbnJ2KSQ-Gig-zw8gJFOV9sRTOGqF8DHG2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت مقاومت عراق از عملیات‌های یمن علیه سعودی
🔹
کتائب حزب‌الله در بیانیه‌ای گفت: پس از تجاوز فجیع به مقر نیروهای الحشدالشعبی در عراق، خاندان حاکم بر شبه‌جزیرۀ عربستان به جنایات خود علیه مردم یمن ادامه می‌دهد و به سلسله جنایات صهیونیستی-آمریکایی علیه ملت‌های مخالف سلطۀ آمریکا در منطقه می‌افزاید.
🔹
این اقدامات وحشیانه تنها عزم مردم یمن را برای ادامۀ مسیر مقاومت، عزم آنها برای بازپس‌گیری حقوق خود و ارادۀ تزلزل‌ناپذیر آنها برای شکستن محاصرۀ ناعادلانۀ سعودی‌ها افزایش می‌دهد.
🔹
کتائب حزب‌الله ضمن تاکید بر همبستگی کامل با مردم یمن در دفاع مشروع از سرزمینشان تصریح کرد، پایداری آنها که در خطوط مقدم رویارویی و عزت علیه رژیم سعودی و مزدوران آن مستقر هستند، ستایش می‌کنیم.
🔹
فرزندانی که به جهانیان ثابت کرده‌اند ارادۀ مردم از هواپیماها و موشک‌ها قوی‌تر است و عدالت، هر چقدر هم که مدت‌ها در انتظار باشد، به یاری خدا ناگزیر پیروز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/460771" target="_blank">📅 00:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
مدیرعامل تراکتور: کسی حق نداشت ویس خداداد را ضبط و پخش کند. ویس را دادند به شبکه‌های معاند، اول آنها پخش کردند
@Sportfars</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/460770" target="_blank">📅 00:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b452ef8b35.mp4?token=tkaa6CDBl4V1SHOngDCgnemf2wQuErHie2ZXN0S3-NBh2qW9yZmMSy4GI0F1q3WgkUS8KirIaMTd23cQlQYnvOFOWPWLjv1sZ12U5-gwYub5SNBwIoZ9oKQ0vfLbSqxG68Rzxy3XAu4khSCdrnRhIVb63Ke5Dz1oP6hs4IWFVj-a_RqGXm-z2G1gaCphXJvaduA2uOkfRwWI4HUBsiuXsEc_9MKpKUvWjKoPO5kc5h0UyOYYAZAKzZzfdqHIZknKE9f1oZOa9RVpOXqs3YZZB9k9PKbU3K9jb74EQFiy6NfWYRcEqvevTf29u0-RtKF8-k1Z52TAm_Ld92MOEL2fZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b452ef8b35.mp4?token=tkaa6CDBl4V1SHOngDCgnemf2wQuErHie2ZXN0S3-NBh2qW9yZmMSy4GI0F1q3WgkUS8KirIaMTd23cQlQYnvOFOWPWLjv1sZ12U5-gwYub5SNBwIoZ9oKQ0vfLbSqxG68Rzxy3XAu4khSCdrnRhIVb63Ke5Dz1oP6hs4IWFVj-a_RqGXm-z2G1gaCphXJvaduA2uOkfRwWI4HUBsiuXsEc_9MKpKUvWjKoPO5kc5h0UyOYYAZAKzZzfdqHIZknKE9f1oZOa9RVpOXqs3YZZB9k9PKbU3K9jb74EQFiy6NfWYRcEqvevTf29u0-RtKF8-k1Z52TAm_Ld92MOEL2fZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارزانترین پرندۀ ایرانی، گرانترین هواپیمای آمریکایی را نابود کرد
🔹
انهدام آواکس ای‌۳ تنها یک موفقیت تاکتیکی نبود، بلکه نقطهۀ عطفی در معادلات دفاع هوایی منطقه به شمار می‌رود.
📝
برشی از برنامۀ تلویزیونی «عملیات شکار چشم عقاب»
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/460769" target="_blank">📅 00:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fno5x9qwCExRUeHVUIjXEEKkqrVZaWjaTb9xysaPD_rJ-Sk5AlA5rqHVXryY2VoA2jowqWMNIkzeHtKjXnyXtj2ThIGD4wlnKMzGFnYb-FprKC2AUrRbqDx3AL1TQwJiyHAC7Jp1MAnNQyqTK-iaKwdi12SDdidbjU3_TxCwnetLPEIkklJZ7OdUbHC78J6EckHOrgmIslZ6iVqzFu0NK6OAfRrYGYvWDIcbCZQn478XUyMxFxmjKUnOuMfYigbGhlNXxZKQVY1H6rO85V0jXUJ2Rl59vPK2Yndi-2AZ5h4d-b1T80Fp31d_D80z-CctQQXISZUQbdFV8NIBC6uvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۵ خبر خوب از ایران؛ از بازگشت پروازها تا جهش صادرات و درمان
🔹
همه خبرهای خوب قرار نیست در تیترهای بزرگ دیده شوند؛ گاهی یک پرواز که دوباره برقرار می‌شود، روستایی که به آب پایدار می‌رسد یا بیماری که با یک فناوری تازه درمان می‌شود، بخشی از تصویری بزرگ‌تر از…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/460768" target="_blank">📅 00:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA_pwtflcCEYJcbp1hRDQzhwjvgQMW2C2HpcLBkEDaTCpYQX1DQdWrpewWZV3lv1_T15kfkg9CyOl8NYzQMZZKO_KBgRDW-CKr5QFvkDiI-WzNmvGqCtIq6nN3koKtMZGRP3-KKr7j0aAuert8lJ8JBC0TVRPG7yt7BJTOERRBU93nkISZTe34xuW6yX6ILYiYo4BnLi91SoyaI1dagKRjsJi4DPmSDq79knrJlR7_6HxBeCbQAW0KtOje7A1_gVvi6DMiBRfRwelVEJgVJDnbIwoQYDbxbGOU6nTKAxjrdeqRoWzXdmYLdBUUuq8ZdhWO8FGo9ud3MdRFd0VogBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: بیانیۀ وزرای خارجه و دارایی کانادا در حمایت از جنگ اقتصادی آمريکا علیه ایران، همدستی در قانون‌شکنی و تحریف واقعیت‌ها است
🔸
سخنگوی وزارت خارجه کشورمان به بیانیۀ مشترک وزرای امور خارجه و دارایی کانادا در همراهی با اقدامات مداخله‌جویانه و جنگ اقتصادی آمریکا علیه ایران واکنش نشان داد.
🔹
اسماعیل بقائی نوشت: درست در همان روزی که رئیس‌جمهور آمریکا با بی‌حرمتی به حاکمیت و استقلال کانادا، کل این کشور را به‌عنوان بخشی از قلمروی آمریکا نقاشی کرد، وزرای امور خارجه و دارایی کانادا تصمیم می‌گیرند باز هم در مسیر باج‌دهی به همسایه قلدر قدم بردارند؛ این بار از طریق لگدپراکنی به سمت ایران از طریق صدور بیانیه‌ای که سراسر تحریف واقعیت‌ها است.
🔹
اما کانادا باید متوجه باشد که نمی‌تواند هم خود را منادی «صلح و امنیت»، «آزادی کشتیرانی» و «حقوق بین‌الملل» معرفی کند و هم از تجاوز نظامی آمریکا و اقدامات غیرقانونی و مداخله‌جویانه آن در منطقه ما حمایت کند.
🔹
اگر مسئله واقعاً آزادی کشتیرانی است، چرا کانادا، که خود طعم بدعهدی آمریکا را چشیده و می‌داند امضاهای آمریکا با مداد انجام می‌شوند، به جای مطالبه توقف جنگ و رفع عوامل تشدیدکننده بحران، از تجاوز نظامی و تروریسم اقتصادی آمریکا حمایت می‌کند؟
🔹
این، نه دیپلماسی است و نه نشانه حکمرانی مسئولانه، بلکه نشانه سردرگمی راهبردی و تسلیم در برابر قلدری است؛ انتخابی که حتی خود کانادا را هم بیشتر در معرض تعرض‌ها و باج‌خواهی‌های آمریکا قرار خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/460767" target="_blank">📅 00:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
اصلاح قیمت بنزین از ساعت ۲۴ امشب
🔹
مدیرعامل پخش فرآورده‌های نفتی: در نرخ‌های اول و دوم بنزین هیچ تغییری نداریم.
🔹
تنها نرخ سوم بنزین که کارت جایگاه است از ۵ هزار به ۱۰ هزار تومان تغییر می‌کند.
🔹
سهمیه‌های اول و دوم ۸۵ درصد نیاز خودروهای شخصی و موتورسیکلت‌ها…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/460766" target="_blank">📅 00:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe3d013a2.mp4?token=UWfWo11p3k-3SD73xauPMzfVwUShCY_zXy4RtxmHAxcRU0jyogReQuQ--tmwnyDDn1kdo-mS9HOem_TdP7EoB949yRd2P_KBImgFi-K-CfuG9A0F63QXeOhtZcQ6fvr_uzYK4-Ug8PR_tSXfogP4OOBbfZ2A2lHcG5-RovNcEitptk1mdr80sOD4a3EKSCout-f3-DWhNhF726iym-WwquRd5q-_SEMnUSB1xyOFgwjglFeQ90PCC8L7LI0Eyf4HZMz_HsHhOcibfr8e1IWb8xniLJCQSQoa7OXgiBCkj1pYWV4ujgM9NkuXrISkpc1LGSeKc5oe2AewV0mj-WEkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe3d013a2.mp4?token=UWfWo11p3k-3SD73xauPMzfVwUShCY_zXy4RtxmHAxcRU0jyogReQuQ--tmwnyDDn1kdo-mS9HOem_TdP7EoB949yRd2P_KBImgFi-K-CfuG9A0F63QXeOhtZcQ6fvr_uzYK4-Ug8PR_tSXfogP4OOBbfZ2A2lHcG5-RovNcEitptk1mdr80sOD4a3EKSCout-f3-DWhNhF726iym-WwquRd5q-_SEMnUSB1xyOFgwjglFeQ90PCC8L7LI0Eyf4HZMz_HsHhOcibfr8e1IWb8xniLJCQSQoa7OXgiBCkj1pYWV4ujgM9NkuXrISkpc1LGSeKc5oe2AewV0mj-WEkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان شهدا میزبان اولین شب گرامیداشت شهدای ۱۷ شهریور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/460765" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyEgEPiDbyOMnNnNqGc0KCP4-i6vgEBYHTFTve79Ax9Ql_qLDdf0lca-0XXibm8fX-TMS1xYxrBWH1bQ55GAWsUPOfGnJWNFZ8Jq3xNdAzSU3OgIUk5Rcbim4MZxejqF81Oq9-E4h1hpldamt9tddSPDW522w-uDjlAVp6YZWmYhhv1vUMYx-lYjQr8_yxALM9TNcb0tYPWla-tFJUsxOcE2VuR1HaeqQwpGwcQEouZyxc8nR7l6xO78292R0M47ZecOUF8a9O5w-eGDADfpr9RdCGpCoX9slwi932jaFu5NTXFtHxL9yyZaymiL4JNRIXatkej-SWkSLSzb2XtmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سازمان ملل نسبت به طرح اسرائیل برای آواربرداری در غزه
🔹
گزارشگر ویژه سازمان ملل هشدار داد که هرگونه عملیات آواربرداری در نوار غزه ممکن است به نابودی شواهدی منجر شود که می‌توانند برای تحقیق درباره جنایت‌های فجیع اسرائیل ارزشمند باشند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/460764" target="_blank">📅 23:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f51c78457.mp4?token=f29h4qbxvsLyi7mMhKTsUS2NSLBrqPdOUuaKtQ_si09fpbd3NyGjy1w6f7_6PuTL6VkyZqEV87mqLWLHafyNWyn6XD5MxGXplFzDcY_apqtQO95gwnZVZVMGveCV4astuVQ8MSgXDb5hMpQdZrh3QZI5pSKtAQItt4PRDyEjZQvlUU7ICYksNgWVjcHIa2TXAlSmTXLNvIkZ-TuwXwl2r_wOxR1vqXTkb5644_rrVtXpQWTvl6ZiQimyvBN4kKXR5mdj1ZkyNBT8Dm8AT5hcMZawyfS5irGxYOKDfrDyg7dQgDO7SNLP4B12gymwgm_RTzVzl0pp08YMDElle2riWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f51c78457.mp4?token=f29h4qbxvsLyi7mMhKTsUS2NSLBrqPdOUuaKtQ_si09fpbd3NyGjy1w6f7_6PuTL6VkyZqEV87mqLWLHafyNWyn6XD5MxGXplFzDcY_apqtQO95gwnZVZVMGveCV4astuVQ8MSgXDb5hMpQdZrh3QZI5pSKtAQItt4PRDyEjZQvlUU7ICYksNgWVjcHIa2TXAlSmTXLNvIkZ-TuwXwl2r_wOxR1vqXTkb5644_rrVtXpQWTvl6ZiQimyvBN4kKXR5mdj1ZkyNBT8Dm8AT5hcMZawyfS5irGxYOKDfrDyg7dQgDO7SNLP4B12gymwgm_RTzVzl0pp08YMDElle2riWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کنندهٔ آمریکایی را داریم
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/460763" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460762">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613b4cd993.mp4?token=oHkNEo7F8EhhoTmrwRso0Mndm2aqc3-OHcWwQR19D1oVPUqvRMm_QcLU0-W1mMBaWj-SOii-Z6-hhynQBgtIgl01lhfECO6PZnqiW7D1rYoVTY7Mu4LMFgMQ3rsVRbtomEYw9yAy5c1L_humGj9iTxIBPJ13ghyqmEoMfULOfa5J_49jRkIZL8FkOADYCZ4o03A7-QfRy7XP-1MDBMa-hjKOentcqWXEdrNivHadt7Lv5ep9YDD_6K7na7ggplBlFGxot9lhZlvAe-5qemugDVDmOnCusFUJz9sqqRXVetlsS8AUO197KHw_yz5q3hfS7bvHVixDuZ--PekX3y9eOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613b4cd993.mp4?token=oHkNEo7F8EhhoTmrwRso0Mndm2aqc3-OHcWwQR19D1oVPUqvRMm_QcLU0-W1mMBaWj-SOii-Z6-hhynQBgtIgl01lhfECO6PZnqiW7D1rYoVTY7Mu4LMFgMQ3rsVRbtomEYw9yAy5c1L_humGj9iTxIBPJ13ghyqmEoMfULOfa5J_49jRkIZL8FkOADYCZ4o03A7-QfRy7XP-1MDBMa-hjKOentcqWXEdrNivHadt7Lv5ep9YDD_6K7na7ggplBlFGxot9lhZlvAe-5qemugDVDmOnCusFUJz9sqqRXVetlsS8AUO197KHw_yz5q3hfS7bvHVixDuZ--PekX3y9eOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران میهمان امشب حماسهٔ مردم رشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/460762" target="_blank">📅 23:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سارق حرفه‌ای موتورسیکلت در دام پلیس بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/460761" target="_blank">📅 23:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گردهمایی مجلس باحضور همۀ نمایندگان
🔹
سخنگوی هیئت‌رئیسۀ مجلس: گردهمایی حضوری نمایندگان مجلس با حضور بیش از ۲۰۰ نفر از نمایندگان برگزار شد.
🔹
در این نشست، حدود ۱۰ نماینده به قید قرعه انتخاب شدند و دیدگاه‌ها و مسائل موردنظر خود را مطرح کردند.
🔹
قالیباف نیز در ادامه درباره مسائل مهم ملی و منطقه‌ای نکاتی را مطرح و تبیین کرد.
🔹
مسائل روز کشور در حوزه‌های ملی، منطقه‌ای، بین‌المللی و معیشتی از محورهای این نشست بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/460760" target="_blank">📅 22:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانهٔ مردم بیارجمندِ سمنان به ایستگاه ۱۹۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/460759" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترویج دموکراسی به سبک ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/460758" target="_blank">📅 22:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc-GTrYqz2Qdt4qJea3bHlhQzKDCI5FGiRuFC5vJ8MxmOyhnHhTAfr5WWq9z3u2IqZwzTtZRs119Dvc8BXxIW5QExQv1Og_bGUb6MtT9h33xDRULz1H5Mbi436ZmNen8l3BXowrFokijS-7GvHJMjE7o2lPYbM4GVDcaoMzi-hsIWAQjHNeuz7t3AZfxXxBqaB8yjgVjpHGfAVaSr5JnzS1-px21USwAz2jmT7rifkXM9r0eDAPQghiRvNjipIn58mxeIMP-tOGn73aEVE2CxjN5YynN7OIL2o-0cRMLc11MWLuBPdV-bILQJ-A5SozULJETWuZZ3WnVDqYBnNKIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/460757" target="_blank">📅 22:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWW06DQfv2X8PuAu7FsBq4deTl-1CWD73m9gWVuQr3NPxMOHVuW6IV8VvloBETQSsWtvGZXZbQbENtxYVihnLAFgpEvhRNfOJo3V94CuIdqC12t5PFLNWp_YrVyuIKjALYNe_GJbxIXLl7r1jGmw8BIq6Rwc8o4lfrqqcfvovk1BDQYgiXby_Ivfpw-XjEndBGktyyt-0eZ_z66DRrIaPHGqLkqY1NtIbmvpSzQIrJh-QCjcyCg_-VJnqN4xIQhh83K2BQzoZDHMvLdbKjLcWlW74F2aM5FctiWcJZvVenT2gJenBtIAAHend4mJLzRZnAHheKxlUyjkqub_nlqhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دبیرکل نجبای عراق به آمریکا: بعد از ۳۰ سپتامبر، سربازانتان سالم برنمی‌گردند
🔹
شیخ اکرم الکعبی: اگر یک سرباز آمریکایی بعد از  ۳۰ سپتامبر در عراق باقی بماند، اجازه نخواهیم داد سالم به خانه بازگردد و تنها اجساد آن‌ها از عراق خارج می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/460756" target="_blank">📅 22:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌های ایستادگی مراغه به ۱۹۱ رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/460755" target="_blank">📅 22:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460753">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5p36dzdVBnvhCQH-GJuiacYzpSpDK8jkRA8gphPG1V1o8MUNu1H4OMJuqOiGGxpkGqmG7UE6eLIuPbfnyhvLB4goWY7zfARPrgBLN3nYTPkNkJDxQPSpOP-_gofixRfmxEVSAmKo2b4Wcxu72aWXHQpRM0iAHM2QIXrjuE4eUrdZxrHK-u6bVVk_I4QHmibxso1fsotJ6OiKGULcIJ7BURacTtiAt2vsL5gBkiCYgi1T1pCk_ELBYr1EMkvQlWw3ktjYf_0_F8UAMmTZ7O-egA_uaU7P6g-0mfN1axRW3vOJnsqq3VdRtb99gqhlLHuHkAat_j-KPtsKIpH7mKufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ابزار قرار است کارهای روزانه‌تان را پیگیری کند
🔹
دیجیتال‌ترندز: متا درحال توسعهٔ نسلی از دستیارهای هوش مصنوعی است که قرار نیست فقط به پرسش‌های کاربران پاسخ دهند.
🔹
بلکه می‌توانند هدفی را دریافت کنند، مراحل لازم برای رسیدن به آن را تشخیص دهند و بخشی از کار را به‌صورت خودکار انجام دهند.
🔹
پروژهٔ «میوز» یکی از مهم‌ترین تلاش‌های متا در همین مسیر است؛ مسیری که می‌تواند نحوهٔ استفاده روزمره از دستیارهای هوشمند را تغییر دهد.
🔹
تصور کنید صبح، به‌جای این‌که فهرستی طولانی از کارهای روزانه را یکی‌یکی بررسی کنید، فقط به دستیار هوش مصنوعی بگویید امروز چه کارهایی باید انجام شوند.
🔹
در مدل موردنظر متا، هوش مصنوعی می‌تواند این درخواست را به چند وظیفه کوچک‌تر تقسیم کند، اطلاعات موردنیاز را جمع‌آوری کند و برای اجرای مراحل مختلف از ابزارهای دیجیتال کمک بگیرد.
🔹
در چنین شرایطی، دستیار از یک چت‌بات پاسخ‌گو به یک «عامل هوش مصنوعی» تبدیل می‌شود که هدف را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/460753" target="_blank">📅 22:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460752">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ هم نتوانست تولید دارو را متوقف کند
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/460752" target="_blank">📅 22:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460751">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnSD3jtg-z8nVXYBnp3nbAjyKdeJggzL2AZRKLEmwZi4ofV39O9nr2lhCfwY6aY-Xv2Q88hAJHFG3CqODoPvTPlfzaoRChLCLWDDyTC4zObvY9FXxwMLcmBnNjO5ut5IwfBlvaI9nBnY33GNXkv_8MrrpUptxq18aGqWLQB1V8thaBfqEBFXsHTLzy3c_DLmdA__LbZwjEnf5dtxM2gKVPhA8q6gmclrfUeZIIneg1H-l6R10bFNKAH_16Iagw6nO0rj5UBSkh4yQDhGlOuqGiR2exfmrkMcgPn9NcxvfqOvoUL85mmyR45dVtoWthoLdVpTrHGqvKmz8ArMZK9w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان ارز‌بری خودروهای داخلی اعلام شد
🔹
تولید هر خودرو در ایران‌خودرو حداقل سه‌هزار دلار و در سایپا دست‌کم ۲۵۰۰ دلار ارزبری دارد.یعنی برای تولید هر خودروی داخلی، حداقل ۵۰۰ میلیون تومان منابع ارزی مصرف می‌شود.
🔹
در سال‌های گذشته وابستگی به واردات قطعات های‌تک پاشنه‌آشیل خودروسازی بوده است.
🔹
بازوی کارشناسی مجلس می‌گوید تا زمانی که زنجیره ارزش قطعه‌سازی تکمیل نشود، شعار تعمیق ساخت داخل روی کاغذ می‌ماند و جهش ارز مستقیماً قیمت کارخانه را بالا می‌کشد.
🔹
حالا بررسی جزئیات آماری نشان می‌دهد تارا اتوماتیک ۴۵۰۰ دلار، شاهین پلاس ۵ هزار دلار و ری‌را ۶ هزار دلار ارز می‌بلعند.
🔹
این ارزبری در محصولی مونتاژی مانند هایما X7 به بیش از ۱۶ هزار دلار می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/460751" target="_blank">📅 22:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460750">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رفع مشکل اپلیکیشن خبرگزاری فارس
🔹
مشکل دسترسی به اپلیکیشن فارس که در روزهای گذشته به دلیل تحریم‌های جدید آمریکا ایجاد شده بود، با تلاش تیم فنی برطرف شد.
🔸
هم‌اکنون کاربران می‌توانند با به‌روزرسانی آخرین نسخهٔ اپلیکیشن از طریق
سایت رسمی فارس
یا
کافه‌بازار
و
مایکت
، به صورت پایدار از خدمات آن استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/460750" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460749">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ جانباز؛ از میدان جنگ تا امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460749" target="_blank">📅 21:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460748">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار متناقض ترامپ از نفت عبوری از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460748" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460747">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف دولت از افزایش نرخ سوم بنزین چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460747" target="_blank">📅 21:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460745">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام مسکن تهران یک میلیارد تومان شد
🔹
با اعلام مدیرعامل بانک مسکن، مبلغ وام مسکن به‌ازای هر نفر افزایش پیدا کرد.
🔹
تهران:  یک میلیارد تومان به‌ازای هر نفر
🔹
شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان
🔹
سایر شهرها: ۶۰۰ میلیون تومان
🔸
یعنی زوجین در تهران مجموعا ۲ میلیارد تومان برای خرید مسکن دریافت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460745" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا ۱۹۰ خسته می‌شویم از شمردن؛ اما از حضور هرگز
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/460744" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrwKtOiFY_QSQZOT_3tQyaDaLBn35jmZGHTuetf545UPptIPpzujH5L2aPG6xxmgBR1vaJysBUE8y0IQPa7MTg9wjXhORc4B-vou8CvQWoAtB0c-ZySpOmKOy0_IeDM1Rte8WMgt2ZjX23xwfPUlgUE5S7dV8jqR5bwS8cEzJi2Z5KSEI65LzLswYUM1qcXAPIGNGeWk5fIM-iYJQJRpOn_BLSaWE0zuRlBhg2ZN3WvU0Vq8CpjFcdSShBYHcDOMgtnMzYIFH0-T_VOa6FiRFgvNGBIR2nLUZDkPhlrljxLZfEixEggqFIT0jbkz2rXZeH7sZQhlgwBC0MFKzQJD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور پیشین لبنان: مقاومت تنها راه مقابله با اسرائیل است
🔹
امیل لحود در پیام تسلیتی خطاب به خانواده‌های شهدای جنوب لبنان نوشت: تاسف‌بار است که تقریباً هر هفته ناچاریم همین سخنان را تکرار کنیم، در حالی که غرب نظاره‌گر است؛ به‌ ویژه آمریکا که قرار است ضامن آتش‌بس باشد، اما این توافق‌ها همچنان روی کاغذ باقی مانده‌اند.
🔹
از زمانی که پای میز مذاکره با این دشمن نشستیم، آنها همچنان به تجاوزات خود ادامه داده‌اند؛ تجاوزاتی که علاوه بر حملات علیه غیرنظامیان، شامل سوزاندن زمین‌ها و تخریب و با خاک یکسان کردن روستاها بوده است.
🔹
این دشمن به توسعه‌طلبی خود پایان نداده و نخواهد داد، زیرا جز منطق قدرت را باور ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460743" target="_blank">📅 21:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/460742" target="_blank">📅 21:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90e3e6478.mp4?token=DKwBnlTC3b3nwAR2Uvqo8_YVuZK34gbnfY3up05k2FAGOYFZS51KtW2Fli_5sZlKKUDHDjqABil6ah03BhSQz05ZoApnwg33zGKynMx59Ia4uK_27TJqKGSQ1kBsWTbLLZTtVAy-79Zp9oz_BZI24TidhSnbfnfpEMrDVvViDKQemn4dNX0zl5jdF-rP1CvSh3RLmu7-LQxW5jNO95Pzh_2VFpeLrnd_eaUXY4TPw4IDP5-3wM0XHO_GXl1bP082DiIqP46oSxEAUgZt-8g1wRoXZXXR5ils__lM9na_0-mIinBYTD56Kz4ak_ijoh30pSLl_p1dNB24-vkUF1pWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90e3e6478.mp4?token=DKwBnlTC3b3nwAR2Uvqo8_YVuZK34gbnfY3up05k2FAGOYFZS51KtW2Fli_5sZlKKUDHDjqABil6ah03BhSQz05ZoApnwg33zGKynMx59Ia4uK_27TJqKGSQ1kBsWTbLLZTtVAy-79Zp9oz_BZI24TidhSnbfnfpEMrDVvViDKQemn4dNX0zl5jdF-rP1CvSh3RLmu7-LQxW5jNO95Pzh_2VFpeLrnd_eaUXY4TPw4IDP5-3wM0XHO_GXl1bP082DiIqP46oSxEAUgZt-8g1wRoXZXXR5ils__lM9na_0-mIinBYTD56Kz4ak_ijoh30pSLl_p1dNB24-vkUF1pWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار متناقض آمرکا از نفت عبوری از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/460741" target="_blank">📅 21:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzayaKFkFrBj1ZMli-vDPNtJdci-QqRpBLo3NDyKd3faGx2FPL9gykjJdOTyn0J7h6cGood2DP7Aa9OYIx4d9OWyPZl4gCWGJ0K7jhjt4J0oR5HPuohi-4YVucm2J4gPidJbXs54of2B1gnb97wukaC459zqjzNtACfuTChIJYOc4tbzTDhs31_sDX6WTHMNFgzb_TdicwkwY8zTVVxeF06X6k30jrzDRPfxjrz2eN1r_ST35omfBTDQueARmvjRmZwH47pKnTZRIHNhpSD3nAtAR6_lH23hbKq5SZf3xU5ArgAa1c5sMURWle57O1gpTz7QX06spnwEIvP_v8DpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم پرسپولیس به ذوب‌آهن توسط شهرآبادی در دقیقۀ ۶۴
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460739" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de63667a28.mp4?token=R6zgRkVqvSLb6u9E70YKS831HoxhvLgZTr95ABtk4nhE97KKFkHWe0M2wKYJhZ3NS_ejtyqi-NC7uIzBUSAa9J4w2eEwKKPXqTRVreHpC9fMHJoOsNCrfGmaHNZSUFx26L8zY95YTNXa9f43qZzlVFY4prENdXGN09f_VDROBZ-wVbN4yjjtgNpz21u5IkbmdVdNL1XOjKe1ed6fAX-SrcWbJQLjvvFB7o6NpX4quHOSdF7XNLGSaG6tKC5FXC2SLKo5kZNqzlpWsNzL4o62727kBCd_Iw1C8jmWBTiqMwGmoFnCN61n-paSKfS7aMjUmKoRHTd4BTRr02wf671Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de63667a28.mp4?token=R6zgRkVqvSLb6u9E70YKS831HoxhvLgZTr95ABtk4nhE97KKFkHWe0M2wKYJhZ3NS_ejtyqi-NC7uIzBUSAa9J4w2eEwKKPXqTRVreHpC9fMHJoOsNCrfGmaHNZSUFx26L8zY95YTNXa9f43qZzlVFY4prENdXGN09f_VDROBZ-wVbN4yjjtgNpz21u5IkbmdVdNL1XOjKe1ed6fAX-SrcWbJQLjvvFB7o6NpX4quHOSdF7XNLGSaG6tKC5FXC2SLKo5kZNqzlpWsNzL4o62727kBCd_Iw1C8jmWBTiqMwGmoFnCN61n-paSKfS7aMjUmKoRHTd4BTRr02wf671Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/460738" target="_blank">📅 20:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PLaRo2orHOsjJfOarZSA5Ptyh5r9kmju68hJiQ1ecK5ZvxdhNzB8ZkYRYtlIzwIp3mvr7FdKyoR5DoZ2iD_EnR7HHYlr4mS3EwPQo4EFGZum0rtB_bf-mgpqJHCfrxZVhOdUJZvmQuU4GhEfEd7QvR94Bjy-AiO_b7RatJGZsjepnVHLjaCTSqzm2WzBRm98YMWHb-p7iIJAF4QefzH7Z9G1mwK3yVsvMd_DagDyAs-UBNu1JUU73Xxz5EpReCJvIHBJrgisoozuYbP2MeUdrWhPA7Uium7RgEZ9tuf3cmQyW3Rcw7ErmpsJpSicUuLxvwnyeIn0B1zCJpaDZQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: تاوان جنگ‌افروزی اسرائیل علیه ایران را همۀ جهان می‌دهد
🔹
تا زمانی که گره تنگۀ هرمز باز نشود روند افزایشی قیمت‌ها در جهان ادامه خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/460737" target="_blank">📅 20:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46bf1f598.mp4?token=Y881rCTrA_g5cufJznbO3buwJ6QlnQsmS0a0XZFruhq96KcBa8va3kv5hsfha1WKBoL_tGs2TdSAuRWA6PNy3vwRsaqdGHcbS0H5FmLiEu2yhLSAgvJBUmFteaBddcx9ZtSUXCqP8czuzibckLGHzDHgoqJpY9uauuwKK_vLYVGgiTVkQQZYJvsZkShpfGqw6jq0TrXCx6lO1TgXJN9TYIAHaQPy3vnti52v6wC7OewN50DPlMAxQ5oOujbN2e-8q5gzw-uk3Gqp-xIEURZ-zfoIvJr7OvmY4LYZDg3hoOoXu0si7K4SPMdc16ggRlrbPyuj1zA159LUmTFyTkl9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46bf1f598.mp4?token=Y881rCTrA_g5cufJznbO3buwJ6QlnQsmS0a0XZFruhq96KcBa8va3kv5hsfha1WKBoL_tGs2TdSAuRWA6PNy3vwRsaqdGHcbS0H5FmLiEu2yhLSAgvJBUmFteaBddcx9ZtSUXCqP8czuzibckLGHzDHgoqJpY9uauuwKK_vLYVGgiTVkQQZYJvsZkShpfGqw6jq0TrXCx6lO1TgXJN9TYIAHaQPy3vnti52v6wC7OewN50DPlMAxQ5oOujbN2e-8q5gzw-uk3Gqp-xIEURZ-zfoIvJr7OvmY4LYZDg3hoOoXu0si7K4SPMdc16ggRlrbPyuj1zA159LUmTFyTkl9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/460736" target="_blank">📅 20:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74acdb12.mp4?token=pEmbUHF2lWxY85IKIQeJxd1WSBwzKeBMDrwbOU_Ccu-i6GOcyBWJRkirxZnCGL5cT1XqQzihCt_FXUrCFI6EUy11_w72CuTB-7oBmeDJ3j3GqVHojOAjsAZR1FZForVBwOpnF5f0Nynrbeuxn7Tw1f3NiWMVGXceCmHgx51cf_pSW1iVrFC--T-8IHTEy1vE26tHMEh77U7xvrAaIQsl2WHFk9k-8O8dftlrhxTGgxsirHuqwkg9eZ-Z6rB4F_Bk3wPwFwE5a7K1Ot-JQFbUy0pDXU1wz148f1OO6egg_UDA77Y6FS6FS_e-y_PkwHKg_-pkMOWe4WIKlxhmhinVmDyBXcqiaPkrqss0UITzvzp4k6AeIyZOeydLqGYIr8TAcv5WCbhBlY3u-ejk3sPSJaWTx4UFbubB7MsEWFdCFuYyzJwxoIuuP1POfhUEcF7zr3ckQQclAaq7ne6UGgt4a1G_PG_aQiHJyS0yoMhHi5N_wk7g4xQq7Oc4lC4WuOZVLf6Fv_7vyTB8bHVhm0fE7hLxfrXTU1hkmgWWJepZz2fXUv0ZCwB17WBop3GnxuZdQepcH_-KuJxhOMfOkrP7qvy1efvaWAm7FDLuTfxGJNnQmNIRvxjcpTr-PWTMKXGShIVkvMl1rT2ZJWGHdhOMMOpEUm46fxExpVIY8vXcpoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74acdb12.mp4?token=pEmbUHF2lWxY85IKIQeJxd1WSBwzKeBMDrwbOU_Ccu-i6GOcyBWJRkirxZnCGL5cT1XqQzihCt_FXUrCFI6EUy11_w72CuTB-7oBmeDJ3j3GqVHojOAjsAZR1FZForVBwOpnF5f0Nynrbeuxn7Tw1f3NiWMVGXceCmHgx51cf_pSW1iVrFC--T-8IHTEy1vE26tHMEh77U7xvrAaIQsl2WHFk9k-8O8dftlrhxTGgxsirHuqwkg9eZ-Z6rB4F_Bk3wPwFwE5a7K1Ot-JQFbUy0pDXU1wz148f1OO6egg_UDA77Y6FS6FS_e-y_PkwHKg_-pkMOWe4WIKlxhmhinVmDyBXcqiaPkrqss0UITzvzp4k6AeIyZOeydLqGYIr8TAcv5WCbhBlY3u-ejk3sPSJaWTx4UFbubB7MsEWFdCFuYyzJwxoIuuP1POfhUEcF7zr3ckQQclAaq7ne6UGgt4a1G_PG_aQiHJyS0yoMhHi5N_wk7g4xQq7Oc4lC4WuOZVLf6Fv_7vyTB8bHVhm0fE7hLxfrXTU1hkmgWWJepZz2fXUv0ZCwB17WBop3GnxuZdQepcH_-KuJxhOMfOkrP7qvy1efvaWAm7FDLuTfxGJNnQmNIRvxjcpTr-PWTMKXGShIVkvMl1rT2ZJWGHdhOMMOpEUm46fxExpVIY8vXcpoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: برنامهٔ اصلاح ساختار بنزین بر این اساس است که یارانهٔ واردات به‌تدریج حذف شود
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/460735" target="_blank">📅 20:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXMfcPdARbDLr_1VPs8FqwSzJS-FGIJ8r1gnsHoNoOCfxZx_SRbOBwyjw5p3Dt3j2qzCu_peloUozfRdi43PAY_jsAl_8Qrtb30SOR1SstrtPmD2gV5fZ7-bQvPx4LHYFuhd4VXlWmPjWdp3SYuwceBPf1vRLTQ1aXTdpvv_Qi-svnZuzMxk-bVYr1K8WHByBUFE-12bAxndzSOxYGeGRqrAzO7ZAvyQ4KUxZ_49d0BGe9xtyCxHcrtI0wwxzFr2yIYq-TJ_gQieD5tEWpV0v22NPUcwNz-Gx8IVwT-KO0JPoIrz07RbB0vVWx4GSiOk8gxgRSu9rw8gfxRkRa4ZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش هرمز قیمت گاز اروپا را به بالاترین سطح ۳ ساله برد
🔹
قیمت گاز طبیعی در اروپا در آغاز معاملات هفتهٔ جاری با افزایش چشمگیری همراه شد و به نزدیکی مرز ۹۰۰ دلار در هر ۱۰۰۰ متر مکعب رسید.
🔹
تشدید تنش‌های نظامی میان آمریکا و ایران در منطقهٔ خلیج فارس و نگرانی از اختلال در مسیر انتقال انرژی از تنگهٔ هرمز، عامل اصلی این جهش قیمتی عنوان شده است.
🔹
براساس داده‌های بورس لندن (ICE)، قراردادهای آتی گاز هلند (TTF) برای تحویل در ماه اکتبر، امروز با رشد ۳.۳ درصدی نسبت به قیمت پایانی جلسهٔ قبل، در سطح ۸۹۲.۸ دلار در هر ۱۰۰۰ متر مکعب معامله شد.
🔹
این قراردادها روز خود را با افزایش ۳.۵ درصدی و قیمت ۸۹۴.۶ دلاری آغاز کرده بودند و در ساعاتی از معاملات امروز حتی به بیش از ۸۷ دلار در هر مگاوات‌ساعت (معادل حدود ۹۰۰ دلار در هر ۱۰۰۰ متر مکعب) نیز رسیدند؛ این بالاترین سطح قیمت از دسامبر ۲۰۲۲ (دی ۱۴۰۱) محسوب می‌شود.
🔹
تنش‌های نظامی آخر هفتهٔ میان آمریکا و ایران که به حملات متقابل به نفتکش‌ها در آب‌های اطراف ایران انجامید، نگرانی‌ها را دربارهٔ امنیت تأمین انرژی از غرب آسیا به شدت افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/460734" target="_blank">📅 20:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d269b74f.mp4?token=L1JZVnTUg-zhOi4nR0Hpg-bzjaJGdZHHiF85msS_ihpbWH7TWwtzz_I3dhDwv8O9WocG5KbP9miMTKPY7h9mIbHFy2WtiZzho10xZi3cDR3OJ_oQ6QlEyLyI7RXxvNCkzYTkBDvihTYIbtalzDmobmWCxFMdACmKMlYdNsxAJKcQ6Ikw4A8zv-ZsJLGaU4gocSlaaRKH2bCr5DtNFkPy56pPa1a1BSv0UF9Bcl65UUktJuZvvbgemTTlUAPQTYkS48cj9BU5J4bgHXs6LBZAGxTLuVqMk5mMUvFYVddK8RIFmgqgV2_sJ3DEJglJlvJ3sMVxX5dh1TaniBDwYdD4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d269b74f.mp4?token=L1JZVnTUg-zhOi4nR0Hpg-bzjaJGdZHHiF85msS_ihpbWH7TWwtzz_I3dhDwv8O9WocG5KbP9miMTKPY7h9mIbHFy2WtiZzho10xZi3cDR3OJ_oQ6QlEyLyI7RXxvNCkzYTkBDvihTYIbtalzDmobmWCxFMdACmKMlYdNsxAJKcQ6Ikw4A8zv-ZsJLGaU4gocSlaaRKH2bCr5DtNFkPy56pPa1a1BSv0UF9Bcl65UUktJuZvvbgemTTlUAPQTYkS48cj9BU5J4bgHXs6LBZAGxTLuVqMk5mMUvFYVddK8RIFmgqgV2_sJ3DEJglJlvJ3sMVxX5dh1TaniBDwYdD4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
⚽️
پرسپولیس ۱ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/460733" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlWdUD01YW_ns0TSOwPUzubigF0Ti0s1tlbpROACxkI701sP-Wihor2i3dsaNAn1NrCyUns0VoJVXsxk7i2QvAe2s4wlfjsHFnj9GPdqAWueLdBRMgjLcumX3O5n8Y4_5KVP5-MDAzAZwYwlUrnSJN3maREZShVNL05Ha5AN9dISQpuY1wuja46D2Fe_MDCtcdOi4oiqpPrpYUhAcUvWCpUso9NRE_bZXMcx_174M9NZ2YP2Pbya3pR3D98SDJRXHgPXIQErgYHnPBqABQmNAonGQwMd-smBDmhpyFb4Z7A_2_lCur6PFq8ZYQG7sm1mYwpfcv-55lgImeDiHISipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت قضایی عالیشاه از خداداد
⚽️
در پی اتفاقات و حواشی شب گذشتۀ دیدار تراکتور و گل‌گهر، امید عالیشاه در نظر دارد از خداداد عزیزی، به‌دلیل فحاشی‌های صورت‌گرفته شکایت کند.
⚽️
گفته می‌شود فیلم و فایل صوتی مربوط به اتفاقات رخ‌داده نیز وجود دارد و عالیشاه قصد…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460732" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e3566765.mp4?token=jCEvFGK-W9dzRgU_SFyn6SZkxtHXPSSdaauWe6DRj3icrSyKABeJB8AESaYegUDlFVMrOYkxS0GN-gUy5bfjFy-1unFNxX5PMIzAt-7EXON0vL1o7NHvTAM_YKu3IcF-SA8Hy8cqEk1pJ5bSMh8ZCfWDphR7fwnRUWdGZrEF9gZCLhWTRp53Wdm1HM-_894qjd1N3ma_IKHFOQWR7H1-P8clJrKrU3AwoBN9nfFPZ9n3KBDqohYIwT3IS5A9VGgpKZWfvCa9OflPdznQK4tcSebL_g0u9SAKNTrKewqKNL5Z4K1bPpWCYhSL5mQh8MsZkt0qkXX-71-olHW5G-_WdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e3566765.mp4?token=jCEvFGK-W9dzRgU_SFyn6SZkxtHXPSSdaauWe6DRj3icrSyKABeJB8AESaYegUDlFVMrOYkxS0GN-gUy5bfjFy-1unFNxX5PMIzAt-7EXON0vL1o7NHvTAM_YKu3IcF-SA8Hy8cqEk1pJ5bSMh8ZCfWDphR7fwnRUWdGZrEF9gZCLhWTRp53Wdm1HM-_894qjd1N3ma_IKHFOQWR7H1-P8clJrKrU3AwoBN9nfFPZ9n3KBDqohYIwT3IS5A9VGgpKZWfvCa9OflPdznQK4tcSebL_g0u9SAKNTrKewqKNL5Z4K1bPpWCYhSL5mQh8MsZkt0qkXX-71-olHW5G-_WdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: مردم ضرورت برخی تصمیمات را درک می‌کنند
🔹
امروز پس‌از اعلام قیمت جدید نرخ سوم بنزین، صف جایگاه‌ها خلوت بود.
🔹
این نشانۀ فهیم‌بودن ملت ایران است. @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/460731" target="_blank">📅 20:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fd6c268e.mp4?token=TXhNRjIbmsWeg5-0bowAeRjSgZM5OYCc2RAFi0Ayzfl74qdd5-PjHfCEt7GGM7rHV7y-5JrAgFND754L1pRoQc7XC7zlwuFBHldcvZ5HcIJvb-KyWRwVvgEE3l8qG8AzT6ojd-WHQiBsbUtX0Xxv8GXeSW-5lFe_3cDlnBjk4k7k-8NozibLY-6EDiLjXKFkBCExaHB7wRuDj8jvHTDNIpVVvPTjdLu3xqeKmPZaiLO_c3NuABOyJScyxrfPD7J8BTe1VLVl8bjM0XwRI727Mn6gxVpeB_iweBuo5dnOynrtfBkQc7dRbfrL1cdtuCJoK3avxDr28REHmDgCf0leiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fd6c268e.mp4?token=TXhNRjIbmsWeg5-0bowAeRjSgZM5OYCc2RAFi0Ayzfl74qdd5-PjHfCEt7GGM7rHV7y-5JrAgFND754L1pRoQc7XC7zlwuFBHldcvZ5HcIJvb-KyWRwVvgEE3l8qG8AzT6ojd-WHQiBsbUtX0Xxv8GXeSW-5lFe_3cDlnBjk4k7k-8NozibLY-6EDiLjXKFkBCExaHB7wRuDj8jvHTDNIpVVvPTjdLu3xqeKmPZaiLO_c3NuABOyJScyxrfPD7J8BTe1VLVl8bjM0XwRI727Mn6gxVpeB_iweBuo5dnOynrtfBkQc7dRbfrL1cdtuCJoK3avxDr28REHmDgCf0leiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سود نامتعارف خودروهای مونتاژی
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/460730" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کنوانسیون خزر و زنگزور دو لبۀ قیچی علیه ایران
🔹
مدت‌هاست ترکیه و آذربایجان با چراغ سبز آمریکا، کریدور زنگزور و کریدور میانی را پیش می‌برند تا منافع ایران را از معادلات ترانزیت اوراسیا حذف کنند و با بازگشت کنوانسیون خزر به مجلس، میدان نبرد ژئوپلیتیک و تجاری…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460728" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjr4GZzArdp_b2V0qQp89qI5tbHYi7kLn5hMzlLm5St7iQBIMWVDWPfDtKMFPifjS4M4kjkHuVqZokkra0nB4cYz1PU8JBtENJF7lGPZKeJQZfhwk0mVTFG_3xxrLkKlrKpq-ZFIgOeMgFrkHmJdkBP3FEinktNlLw_GbWqTX0v3nUJGgnY19Wp-o3aIDElJc8ZRDs3pYw6iQczRjCGMxC_KsxqiirbH_oBE6bZHLjNZY4IcnoTc6VUnW6msonLzOI6bygh9oLggp7vOiZIzAuSU-ChQnDX99DkN_KX-ObO1nQQ-yDGbct9XrmNdRIPoM3maFBRTq4wLFjSYwnr5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چوب حراج ژاپن به اوراق قرضه آمریکا
🔹
بلومبرگ: آمریکا نگران بازدهی اوراق قرضه بلندمدت است حالا در این میان توکیو احتمالا برای مداخلهٔ بی‌سابقه در بازار ارز، اوراق بهادار خزانه‌داری آمریکا را فروخته است. بازده اوراق قرضه آمریکا اکنون در بالاترین سطح ۱۹ سال گذشته قرار دارد.
🔸
یک ماه پیش، وزیر خزانه‌داری آمریکا برای نجات ین ژاپن از سقوط حاضر شد دلارپاشی سنگینی در اقتصاد این کشور انجام دهد تا توکیو اوراق قرضه واشنگتن را نفروشد چراکه این اقدام یعنی افزایش بازدهی اوراق قرضه ۱۰ ساله آمریکا که تورم‌زاست.
🔹
حالا آمارهای ذخایر ارزی وزارت داریی خزانه‌داری ژاپن امروز منتشر شده، نشان می‌دهد که اوراق بهادار خارجی که ۷۰ درصد آن اوراق آمریکاست در پایان ماه آگوست نسبت به ماه قبل، رکورد ۸۷.۸ میلیارد دلار کاهش یافته است و این کاهش تقریبا با حجم مداخلهٔ اخیر ژاپن برای حمایت از ین برابری می‌کند.
@Farsna - Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/460727" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b39c9b653.mp4?token=KcaPaMAApLrWOeUYGPbAolWcfpjmuYfFbE_c6fYSxrjqB4xXS6_I_U5_Apif9dV3S2xiWKvEOTLpOByky_Uow_EqbxWMNiEmL-WldLfWJmKC5TCqIRgwSzybpsQoH8-0XjAnIsn2gk80saJU0nYBf37xUMaIQIBtw3hdx8Vqksq7KnaUJTwS9uZosVq0OssnFk2M_VnGrrH7MvACPgaO0LTxo7J_uVb-HwVp5w7A4uSO-zKHrupuA0xriN2UVcopPFtWKRxp9zwOZz4Ort9Fv71UY6gWmAwFedfqtBTGmY7AFiKa_uxQL170N7_JYJTtb6bnPX0gOus9y4khabDspg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b39c9b653.mp4?token=KcaPaMAApLrWOeUYGPbAolWcfpjmuYfFbE_c6fYSxrjqB4xXS6_I_U5_Apif9dV3S2xiWKvEOTLpOByky_Uow_EqbxWMNiEmL-WldLfWJmKC5TCqIRgwSzybpsQoH8-0XjAnIsn2gk80saJU0nYBf37xUMaIQIBtw3hdx8Vqksq7KnaUJTwS9uZosVq0OssnFk2M_VnGrrH7MvACPgaO0LTxo7J_uVb-HwVp5w7A4uSO-zKHrupuA0xriN2UVcopPFtWKRxp9zwOZz4Ort9Fv71UY6gWmAwFedfqtBTGmY7AFiKa_uxQL170N7_JYJTtb6bnPX0gOus9y4khabDspg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
⚽️
پرسپولیس ۱ - ۰ ذوب‌آهن
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/460726" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPDVJV-_NaU2e3NnwX0BKrLOw8evDJsBm_b-nM1FeM8732dYlUMEZszQiWbtuFUbKqcIxqghDWk-bmO2RZhrAeiofFgwZjrNpkUKGlQ1y_GpiTUH1yTau-mAeh4p3VmkJp5vQZSY-zbsg34m_rem9gbAGzb_Jdtpx0M9vHSfLAugTJvG4ekTV0CDP31dbjZlFCTsAsyMGhB5XQFJ6VbdnsDHjnXmgq-SXLQ_tXkmxi4jaML2a4pQED-Su6_X3Vjpq2E0Qh_8eTqbpXNdwrvgmh6_f-b9jJF8IuXS4AgHeRMse1fUILNEDSib45VriUlqqXJaKIPeDQP64kHOqQt3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساقط‌شدن ۳ پهپاد عربستان در ۲۴ ساعت گذشته توسط یمن
🔹
سخنگوی نیروهای مسلح یمن از ساقط‌کردن یک پهپاد وینگ لونگ ۲ ارتش عربستان در یمن خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/460725" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f06863f5.mp4?token=gaci01jtqfOwmjGuMTerGtln2Lr99UYCVrNYO7A2aNrZfNAR5kuZF7ajRQPe9mfKlRsBGWRmnf0wLX4NZusD4XpQRzBy_xx7pBuXuTikNhYMKx8-xYATa0e8wZLBznifxEaJpalglNPCZgsCjP58_Zg9XSaIOIx6M6Enu6VTRmcb5Kwcepa0PC4VwL9ouDmgScF3YxNUkDqXLVPGvftvynh7LxK2T57S0Pkghj2N1rGPKx7DkSAtJVJ57wxVYGjofQhFr9lJ2I7aXWY7zHvavFOejOqO4Qvqo27PwRdcHNla4uGX6H7o6Tha-nI3P9DpT9XE0DNtYbsS7B_5Or5sAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f06863f5.mp4?token=gaci01jtqfOwmjGuMTerGtln2Lr99UYCVrNYO7A2aNrZfNAR5kuZF7ajRQPe9mfKlRsBGWRmnf0wLX4NZusD4XpQRzBy_xx7pBuXuTikNhYMKx8-xYATa0e8wZLBznifxEaJpalglNPCZgsCjP58_Zg9XSaIOIx6M6Enu6VTRmcb5Kwcepa0PC4VwL9ouDmgScF3YxNUkDqXLVPGvftvynh7LxK2T57S0Pkghj2N1rGPKx7DkSAtJVJ57wxVYGjofQhFr9lJ2I7aXWY7zHvavFOejOqO4Qvqo27PwRdcHNla4uGX6H7o6Tha-nI3P9DpT9XE0DNtYbsS7B_5Or5sAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پسر‌بچهٔ مهمان برنامهٔ محفل ستاره‌ها به آرزویش رسید!
🔹
اقدام جالب فرماندهٔ سپاه گلستان بعد از دیدن آرزوی جالب پسربچهٔ گلستانی
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/460724" target="_blank">📅 19:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
*ببینید/ توانمندی درآمدی شهرداری، پیشران پروژه‌های شهری/ مسئولان شهرداری تهران، از دغدغه خدمت به شهروندان در شرایط جنگی می‌گویند*</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/460723" target="_blank">📅 19:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJvbvdxzGzwDbSZY7lNdeIzgRMjSQwXyQTyKLmjAssROr8YHZQ9NNDQhTUoR8Cpzp6Zt9SVMbBZBTDYZL683dz6vWzKC-c2bJu3MqKlck1XqTAQt60QYQKJRp8rImU20RdbacC-nWa-5wQJLX6yuq3vY3bazHmaDLSuCmfnssAR2S2GkTSLSWBGCJsDT1ejh76T60UiM0Ku8BkqagsogZJLjsxhvMJ8Kwx68IgAA7kkhYMi3PZA1lg3tnGvde0hcI0ZMvy78LkpExvoxsR9U7i9GW2qJ64EPJlFt-XoL4hfSeaaRp-jnBD_Npfk7b9d7lhZjh0jN8CnXDu7KXEc78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
با کفش ملی،برنده شو!
❗️
جشنواره بازگشت به مدرسه فروشگاه های کفش ملی شروع شد.
✨
تا 50٪ تخفیف
🎁
قرعه کشی: PS5+دوچرخه+120میلیون
📍
خرید حضوری از 220 فروشگاه کفش ملی سراسر کشور
خرید اینترنتی و چهار قسطه از :
🌐
mellishoes.ir</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/460722" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/460721" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLySZALY5XX8Zr5sEd6Z9YIaUaSwrgywYQebyvv8Zz2-4QyQsCRrkMOORoC1wXYobZoHX2GxB3yVwVeWA49kpG7skXIYvGgenLSwUx5Q_oYxnhzVu7tQAQEFZRhPpeJWUjJtzW4rXaSvjYqIusdIdpBf-v95ONARFrodp6SU5EzCXzuxnJ7tAmIKcXwCCTyRMotxfrRkfW23B7aXnBOP6Uh3TeAq5hBrSYjTFMObaZ7jvxMBej1V-RTteKEZOt9F6devaRkUkpVNSSi9zYqcHImgO3S0Lllb6dgL-jBpPsC9y76ikCNUZkeYdhK8NBjxET5kVdAAvXqqi8C1Qmiw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایزمن زیر موشک ایران و تحریم جهانی فروپاشید
🔹
گزارش جدید رسانه‌های عبری نشان می‌دهد مهم‌ترین مرکز علمی-راهبردی اسرائیل در آستانۀ ورشکستگی و فروپاشی کامل قرار دارد.
🔹
یکی از دلایل این ورشکستگی، تحریم موسسات اسرائیلی توسط محققان بین‌المللی است.
🔹
همچنین کمک‌های مالی اروپا به محققان اسرائیلی هم ۶۷ درصد کاهش یافته است.
🔹
در کنار تحریم‌های علمی، حملات موشکی ایران به مؤسسه وایزمن در جریان جنگ ۱۲ روزه، ضربه‌ای جبران‌ناپذیر به این مرکز علمی وارد کرده است.
🔸
رئیس شورای علمی وایزمن گفته ۲ موشک ایران که به این مرکز برخورد کرده، بیش از ۵۰ آزمایشگاه و تجهیزات تحقیقاتی را به طور کامل نابود کرده است.
🔸
او گفته خسارت مالی این حمله بین ۴۰۰ تا ۵۴۰ میلیون دلار برآورد شده و حدود ۹۰ درصد از ساختمان‌های موسسه در این حمله دچار خسارت شده‌اند.
🔹
این حملات، وایزمن را برای نخستین‌بار در تاریخ خود از فهرست ۱۰۰ مرکز علمی برتر جهان خارج کرده و به رتبه ۱۱۱ سقوط داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/460720" target="_blank">📅 19:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4el1qVV5thAkuvfjx38a0if2SB3pHsUHFC-4t_Bzv8Rkzq5dlxmqDshx4Tnz4tA4ocN6iYB7M1EgMYC31dHWj2fqg1HmcPtg4W5Npa2AuVxQHm1FTRm7CbOn9FflFuWFkBI0O9QDxLj5dvoG7QrshP15BsUzHeGc6_DnM9cImDq7wmHBW5PWBoHhKjGOz4tD1Jk_NDyKnhZgNlIMWCRMNvBIeIOt_Fy_xhl36h-HSkGgy84zhlYFa1hWT9kepxwIFMHYQZ64R47r5nhQxAJLNqfxXTo8vjQshvHEyUtUZgWC46EkWy5DKGDPyEzh_vr8FIaL28c2XypgOTvK1qVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpBVp36Y3TvDD1sK6dFkyla7Hi5chXAdGCrAc8HJIcWo_Dn50VsndJXJFVc5ZmxIm2FUoNLOpysQotrpeYFmwyzRo4J7uP-686zLi6PtyK6FMsiEfrHkcV85_Nv9N4Zl_V8HarlUswsH3QmVnFChoWzm6zgUvuDidCnbicY0n3xV-25b-j9__7RTIhgYRskSPbUVsZvvJxoQHCJHrNLZTVqwy35OyvbSJAERjIFsjHJ1HpTKnMIsJqXzhSN2N1la2cfIkJW_rFxjTy9HlQQRUCzjj3jTjshnsJQSCW2SEuYekbw93L_cjgnkX1ojWgx2W73J95jTW6X0gmTWtiB9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMD9zGPcsfpPFqEVPGufsqBz9WK0yRiQFyETiwp3kPxS0ObQyHDQBxXYnpSglplqLANltSJqq3MVZhOhgiqiqYj6CUjFUFEwve2DplhVwfKm3X3kiw6aEkRJAtT1CqacreVTYX80zdxDwfme-iUpPYhJcyNPGLJN0ogRteTUV-RvvU0w-deBfR2JtsX0FNNfQi9AWFSvXut1uvaYLwDXdQJyMNmjhzH9LDWT-TGnpanVD_9y83nvDy31JjMV71x-mb0y8ChxnmrE4na0RACmOC-_oVxdO4cIW88z9Yl0ea3tr_gj-6AkmmvXmqRUtKZDVeZP4r2zGDgC2padXtWt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bn585_pz3vhgqR1ncBqlrSPCW30KkT5T1o478M0YTz_fCjVsffSjCtlwXBZ3jASUixHpXzPNcjuHbedu4Ct2JCrlW8I5DInAKpxmF7qY5ULXXS-R-pFLtRKzUepz7zXRNP7816z5U8c1jKW5dq0YUtBJC9H9YrQyxj6t_UHZEHFNdweRuT_YKdTjN3i4FInEu_ymTRvCip1RWBau1f-Kfe2DzqiTtrJ3wkof-rNN9WOt2F7_EDefmFeZl3aQqJvaX81ko8lyLMcTDpLmM6N3uzCnAdoMbeiDPsqnLsu1pGWIu7207jLNOHLQ1LZXcGIgL_kP_mlw6sVdbmYveNi_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TV3gP6uvJoRvKmUsGCrXgXRwwdc05Gts_luziHXQIIBdfcqdV9OkU4TqJRzJkINRoE1z3rmGsL6B_nk50mck_j3wiKs9w3_2jh9kk3ki0d6WSJU-Ykr7VPSWao7eImastrfs1jXQPZ3P1ZvYgoLJuFNGEztWjh1lh3a6KZheu9KI9_yq80ueJawIQr4kyrqO9UD1PhZMPz_efsV3x458RYwvTYN1e7tHGJLYb5h7qbjve5pn-QtEBcbscTBxRC4M5xb8Y-NyxH8GCuuP0E90xUnjO2PnGeCfB9fqrqixXJKNdyj8oJ5q580wtWQPLZ7qa9tfQihNJrcwJIOMZImKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSMYvXgsIdlslwXAHj0Uk45Jup9rC0E0pMbz4SMNPHdcqq2QnFYz8ql1KFUDuIiFFw-tMtQPoQx-QEiBasIhQ3GIfWFAgZe3Wue5BBypkaWK7OVMeIq3YnEUPPwBIG9hqA3URunkCjgfZ46g1YgUyqeTxWLZ2M5jkbXeQ1YMZHawFzLx5o3xp_a3vw4F58s6dQlZ82fVKm7UYWaU6UF5i8r9ywtV_sWt9ky9_zjpaYCJK7vgWragriX2uFOVqg4F2zkjuAmYua2ZwO2IHM8plKTJix5vpM9yFMJiwz2XpEn9gOY_vmY2MaF4R0EVt7jf0RspHB5XypQtawe79fGzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maugZH5BdZ1Kh7Y7pn1dOYdYZJZVTbZR4qsOruez0UQYaCxIbPnD-q3oQOK06MnOO9LIFv12_ZjyrUv1myJhLAp6M5eyy6p9zrXZS7pRXegdcv_VtDCcdghBmxRx8_p4sTKlJAqjP7uFsCEc4LustFLBw2XuBNDPA4HUO7MdE_jYverctWJU5iEplC17IVcxolR88dUXiLxT_NgFyaLG9NsCY80HNtl4Wqmo9IF2USIr3FkxhlGGg2JSgJMMAe-RYrfiVXpkUyI4LJ53AAy7OvmhM_ZaLQ1jeODIDo4sd4oOJhMCtE_y0CvxxVvutu6JjJGTL3GjX408gu7pByFmvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن پسته‌چینی در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/460713" target="_blank">📅 19:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02cc1840b5.mp4?token=Pd340Xm-DRgjUt22AbR0lSeeHXW_hX_LLRTxUQj20GAUKJvTq9SMjxHhxjUkVdndpcRIKfWw6P3QE7aN-ny-qvBncdf2SSplrtxDeu4J7MJZquxiv7fbmCQkXT2qhWg7RD9sow5J9VnLt9NR6EHxkEpEsUI7YfkK7gA3y0z8YEVZoMZgfbhXUuUfqfQ6JL9ESbwFMrEx0cdqmU5K0w6fj9xRjhDtYK8XTlPr-sQrQe4uB8RDzhhccMWJ92f4A5ztwYuX-VyQPoysudc-6mSrvVkXgaexKHhI4V1WySFGBD7Q0gVl613hK4fW0x_xM-j-lGxOchjmXZL10NU38NPaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02cc1840b5.mp4?token=Pd340Xm-DRgjUt22AbR0lSeeHXW_hX_LLRTxUQj20GAUKJvTq9SMjxHhxjUkVdndpcRIKfWw6P3QE7aN-ny-qvBncdf2SSplrtxDeu4J7MJZquxiv7fbmCQkXT2qhWg7RD9sow5J9VnLt9NR6EHxkEpEsUI7YfkK7gA3y0z8YEVZoMZgfbhXUuUfqfQ6JL9ESbwFMrEx0cdqmU5K0w6fj9xRjhDtYK8XTlPr-sQrQe4uB8RDzhhccMWJ92f4A5ztwYuX-VyQPoysudc-6mSrvVkXgaexKHhI4V1WySFGBD7Q0gVl613hK4fW0x_xM-j-lGxOchjmXZL10NU38NPaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکارهای پلیس فتا برای جلوگیری از کپی شدن کارت بانکی توسط کلاهبرداران
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/460712" target="_blank">📅 19:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6ucUfsdHR_7DpAkXSmnqbWMjYXwChlMYTsDHKwnrlPW3KVAsBqIKWEb99QzgsDKBi5W4DMrbmE3TCaeHBdtG1jG9L2Qzz3w3obz5zsxYfiRe9oYxrZyuKoZEE0zGwhVC7ZwWMyefMH-V5nSiy8dbDNOIYD6eYIzPnNP1Ty09jbC2f9QdcjeoPd3xEeLWvH0geuI368zMc6PSs8ndqmtb7ER81xZbLfJ73FCrNkkhO0ePJy62NBDvAOU4fWryXJV_g7HWYsJisH1i6ubWIftaeKD8uvajp5kRBng0fb-OSPkwdWvWeyYCvfBvpLJ_h4L2uHrq5XzOzn94UrZFqAXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت امید مادران شارژ شد
🔹
معاون وزیر رفاه: مرحلۀ پنجم کارت امید مادران شارژ شد و مشمولان می‌توانند اقلام مورد نیاز خود را خریداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/460711" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQNr-NzVdmZM772--hZA7S5ecBQ6ED-VsdWwfYZe5Bl63-p8fVK_lcgW352dHjtsGTYJiPomL59yzhafhzdsWbwQ-ffbz7kKOJvBalthyguH2fmVUl47UZMAOwggjccVzlneUKQeHX_tm786WCVxUjPJxtZRrguAoSZd47zGqCBINJ79RB92xXhiD-T3A27YbaPqxpbfiJzSXQ9M9uyyz0sMqKGa0i9uayE0f3LgIuCyiUCt_LfzP-gF4h-Huzm8ZVThKHyWQEp0l70CEu2wWFE28FSFYS-i6T4HyrD2pStVHtf54DK8gHanSli--5IsFgcaFlXROAZX4Zy-ImGK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: تاوان جنگ‌افروزی اسرائیل علیه ایران را همۀ جهان می‌دهد
🔹
تا زمانی که گره تنگۀ هرمز باز نشود روند افزایشی قیمت‌ها در جهان ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/460710" target="_blank">📅 18:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSuD1_9x2l9eFDLnrH0KpRktwFCScjJj-vhnLRt2vsgo76Uj5rjdhH6YF2tymU7fHc7fqRe92njhuZjTSRGpWmssgrYytAxGyQ2TCv2CFCVAvoBOfl4_BoOdV4iubGLEIn9PtTwZtX7fmYMSwGRNUUYGKJPl3jtTldmTgnh70Z_uxXjxPIWvZBiqsASL3DARXOaL7lsT1YgSz6bA-4VXrWr0dfyZNYLXlpqqvElEMQTj89uk9qG_BSYAWjpiQP7g8rhTMlyz3zAYdlEWKsdG4FoK-qpkKf2r82b9Nr7SoVdkmCLCCdVKj3Hh-VfZViPb3BsFrsKzCj_gs92bgWCChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: روحانی به‌دنبال بازگشت به صحنه با دوقطبی‌سازی است
🔹
معاون پیگیری‌های ویژۀ دفتر رئیس‌جمهور شهید: حسن روحانی به‌عنوان نامحبوب‌ترین رئیس‌جمهور تاریخ ایران شناخته می‌شود که کمترین میزان مقبولیت در بین سیاسیون را در بین مردم دارد و از سوی مردم طرد شده است.…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/460709" target="_blank">📅 18:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df16f61f4.mp4?token=TviSMtFB6onGVN3j0sWwMIkOsihJbjB2pQ1cchs2MIpCmQbFQeeMl92FTHV8_I-r5kRxR9MYHJzXnt-Aql2aBphSvzoA4e-QTWofBVQITD8mtEUFwWuMBhoxIu4nmSt7JRqTCd80c7LOoS8yh-y-MeLyj-A8qTtFn0cN4WNi_m-WKfjjYrExKDVSF4z3Er17H9pV2bwtMx2zmEj_gyLI4qb9pmHYv9hczCu0463_F_94CWLjEFBm1akXtU_RhxdIgTCd70gehDBQCdWzw5Ni2GlYiXuFX9rHzCkj-VoqfQyjtNR57i5fzowtzv8l1Zftx42R5ukYOb88wGI_Bkol_YphuD7lAUykuIWdsug8pZSgTrkdKATpkjKWGcHwl6xVxshVfRBcjDJjKQBMtwOulKgpoZysblV2w3pnAsjutBVf927gcf76_Lcc5iqGl-LFv1iJ_wz7qUr-GTuC-9qBtwk9OlpNB_sGdHThw1VcJ00-HkjuOBWleGIe8BGc08mQrJuxZTy44lp05IRMLcF7JyVlWCLgaJMC3I8a1XfFFGVoJfQmhG1Uu0BJ_ScN4GxWBTg-glPGLRsKz98EX-wj5Hp5bRcCTE-ww_YJscMsuwHbSk0OSgAVY56RJP3awFR_aUKD4r7xiOmHRvGy-RYx2wcm-gjUilhe9U81y_Sotiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df16f61f4.mp4?token=TviSMtFB6onGVN3j0sWwMIkOsihJbjB2pQ1cchs2MIpCmQbFQeeMl92FTHV8_I-r5kRxR9MYHJzXnt-Aql2aBphSvzoA4e-QTWofBVQITD8mtEUFwWuMBhoxIu4nmSt7JRqTCd80c7LOoS8yh-y-MeLyj-A8qTtFn0cN4WNi_m-WKfjjYrExKDVSF4z3Er17H9pV2bwtMx2zmEj_gyLI4qb9pmHYv9hczCu0463_F_94CWLjEFBm1akXtU_RhxdIgTCd70gehDBQCdWzw5Ni2GlYiXuFX9rHzCkj-VoqfQyjtNR57i5fzowtzv8l1Zftx42R5ukYOb88wGI_Bkol_YphuD7lAUykuIWdsug8pZSgTrkdKATpkjKWGcHwl6xVxshVfRBcjDJjKQBMtwOulKgpoZysblV2w3pnAsjutBVf927gcf76_Lcc5iqGl-LFv1iJ_wz7qUr-GTuC-9qBtwk9OlpNB_sGdHThw1VcJ00-HkjuOBWleGIe8BGc08mQrJuxZTy44lp05IRMLcF7JyVlWCLgaJMC3I8a1XfFFGVoJfQmhG1Uu0BJ_ScN4GxWBTg-glPGLRsKz98EX-wj5Hp5bRcCTE-ww_YJscMsuwHbSk0OSgAVY56RJP3awFR_aUKD4r7xiOmHRvGy-RYx2wcm-gjUilhe9U81y_Sotiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: سعودی برای جنایت علیه مردم یمن مجازات می‌شود
🔹
تجاوزات بی‌وقفه علیه یمن همچنان ادامه دارد و دشمن سعودی تشدید تنش را با انجام حملات هوایی و ارتکاب جنایاتی مانند کشتار در الجوف و تجهیز مزدوران خود به انواع سلاح‌ها ادامه می‌دهد.
🔹
تجاوزات…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/460708" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQLXz4KEWijWoovuX3KqZkA8IB3TJh9opzro1zs1z4kQ1yqbc9EM1Hn3uwhQyGv5QI_7f5Mj3bo8z0acFaykj-MKH2kEj3CbxWWSAFlonJ8hyX6YPBgqaUTJy9N0PFebUQ96TypTMUsz7iAqKX1S0hX4PG7nD9NFC8Ga7jsC7uMY5H4VJXZ46LdFFQfbn4CS3hYBLDdbjiokOEn6QThBNxeXsg_i0O8VQ7fKz5R-HKvCrzskx5YryZ9v1DSZ5Ij_8Y8XRlj0yHHojQvkD9GwTXH_RrGh-KaNeYQXdDSgSmfJAeuFUzsbQkVtGjw59febkCqUc3I9VWXUpfj8l3yIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان توقف ۵ ماهۀ واردات موبایل
🔹
پس از ۵ ماه توقف، سامانۀ ثبت سفارش تلفن همراه فعالیت خود را از سر گرفت و درهایش را به روی واردکنندگان گوشی تلفن همراه باز کرد.
🔸
از ابتدای امسال یک میلیون تلفن همراه به کشور وارد شده؛ درحالی‌که در مدت مشابه سال قبل بیش از ۳ میلیون گوشی وارد کشور شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460707" target="_blank">📅 18:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRYNfunlhqbI2xTIzRjMEbTnseLeAx1SMmGDy4G6fmy2x9F7GOKHZw5TW16f4TgM1O_JXS1DxwmK8Og-0SToiwW1zXQV6t5m60mOL5zvAtPegTLmLwQxHB6ZIaXVnHCX82AEDiLwZIo05LVFgDj1mXpx7SdEquGdqj1RSKE14FsER_tLr-pul5bOpW9n6I7V2vfGRpXQqHOFSge6BYp09jWOcrta_erqAf6lCyjzcxPk3POg1a3r7Tf0o_QHKgvQx6I4ZjfdKs9WqIBNWmnktP4URscVc-fvu3i-zXKZS5_pMGxiusTfdxkuHlC0Pj9k7QtE7rKroaiMVZsoMNGgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خاطرۀ سردار علی فضلی از حضور رهبر معظم انقلاب در جبهۀ دفاع مقدس ۸ ساله
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/460706" target="_blank">📅 18:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHw1uxGUGA12_DyyO2fMxd6gJ0EcA6zFjd6_5KuJACvf7zAP7IW3zSWbQo77s2Vu1ONkK7l3ETsXlKay3ib8unkqmUbU27-kx33KO5KGoHCIW4pslLZhQ7JDZiRnlQqPZzNyKypf9e_IY7tglzde97Bcy_mk4qPpmGmS5zcGpd2lmjatG01Id6bsItbAPfE2fFIwF--Ec8sGCW5vqCT7h28w12TYdyTLzWA9LLZD9gCgvU9Fs3aB2cWWunNQV3Eojfcu1hk3eA5nge35QY_AHZ8BAkddKBvZTiVpmvDuiWNiz-TR8IrUoOjkNxIk_otoxoBZTGUjo0DUl-bggJdAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: سعودی برای جنایت علیه مردم یمن مجازات می‌شود
🔹
تجاوزات بی‌وقفه علیه یمن همچنان ادامه دارد و دشمن سعودی تشدید تنش را با انجام حملات هوایی و ارتکاب جنایاتی مانند کشتار در الجوف و تجهیز مزدوران خود به انواع سلاح‌ها ادامه می‌دهد.
🔹
تجاوزات مستمر سعودی علیه یمن بدون پاسخ و مجازات نخواهد ماند، و دشمن سعودی باید عواقب جنایات خود علیه مردم یمن را بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/460705" target="_blank">📅 18:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908dd4af2d.mp4?token=OHHLOEo14EVv8RJhcGmH-6uWWObiesF4kS4igIFf9mBuHdHp7yvyMBtHouyQPnDFUTMmSlSCeXmjdAxsPl457ENgnhUNZfKFf2m7zh8OCaJayRN6IEcF7PJMRtxl-Vv6Q75TNrxOgl7Jm66qOAw2562-8krR-RdmGjyjxNzT7TIOmlvtc_wPzY71KSocd_AxpaFSiTW3_Hv2fJODCZM-MxascfRwgcw9wgJn-a9LugI8l7UZNixo4U1p8OzdYW6fzIDxD22Zpmt_CgEOwY41IJ3HxsjLMTiZFIq2U2F2CmKsbTwOcwvtjQATtd0D7bM8dR7br2gHL_WFyv9D7vI8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908dd4af2d.mp4?token=OHHLOEo14EVv8RJhcGmH-6uWWObiesF4kS4igIFf9mBuHdHp7yvyMBtHouyQPnDFUTMmSlSCeXmjdAxsPl457ENgnhUNZfKFf2m7zh8OCaJayRN6IEcF7PJMRtxl-Vv6Q75TNrxOgl7Jm66qOAw2562-8krR-RdmGjyjxNzT7TIOmlvtc_wPzY71KSocd_AxpaFSiTW3_Hv2fJODCZM-MxascfRwgcw9wgJn-a9LugI8l7UZNixo4U1p8OzdYW6fzIDxD22Zpmt_CgEOwY41IJ3HxsjLMTiZFIq2U2F2CmKsbTwOcwvtjQATtd0D7bM8dR7br2gHL_WFyv9D7vI8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامۀ چندسالۀ آمریکا در مرزهای شمالی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/460704" target="_blank">📅 18:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKWUzCv3kLtK-L1SUrhFJgMR_JbwgW7iDGlE_7u6ui6ZxT-JU1r-xHZYIKxXEJrhPDxApIfMPXkpcL5dbc8l1EHokjBEVKEJJuF1tpQ83NXDL3SmmRkFEgJL7HoZCXbMtuohAiAOBFcoDaQIxexcYQIOOv-Ly2PV-VpDKE2o7Zj3gIrfLwWkUceqJngITwKojev2O0cKPIyWYjGHy78OwfZVZR680yxZER118TV3onmMwnUvzktamcauiJ2QiPbIa0_MH59El5xqn9g_APAX7XizjLnxAt8XYueoQPaZ6JzHrNPr-JSeeYed0EYH98u387KlFVHAwSC75jB7z2C-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال نتیجۀ شکایت پرسپولیس را می‌داند
🔹
با وجود اضافه‌شدن شکایت‌ باشگاه‌های پرسپولیس و آلومینیوم به دلیل استفاده از یاسر آسانی، باشگاه استقلال همچنان قویاً معتقد است که این پرونده سرانجامی برای شاکیان نخواهد داشت.
🔹
طبق پیگیری‌ها از منابع مطلع، باشگاه استقلال و تیم حقوقی آن از به نتیجه نرسیدن شکایت پرسپولیس و دیگر باشگاه‌ها در کمیته‌های نظارتی فدراسیون فوتبال اطمینان کامل دارد.
🔹
به‌علاوه استقلالی‌ها معتقدند باتوجه‌به شواهد و مدارک موجود در صورت کشیده‌شدن کار به دادگاه CAS نیز این باشگاه آمادگی کامل برای ارائه دفاعیات لازم برای اثبات قانونی‌بودن بازی‌کردن آسانی را خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/460703" target="_blank">📅 18:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کمین رزمندۀ حزب‌الله در مسیر اشغالگران، ۲ نظامی اسرائیلی زخمی شدند
🔹
ارتش صهیونیستی: یک رزمندۀ حزب‌الله امروز از داخل یک ساختمان در منطقۀ شقیف به سمت نظامیان ویژۀ اسرائیلی از تیپ گولانی تیراندازی کرده که در جریان آن ۲ نظامی زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460702" target="_blank">📅 17:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAg9hYdR3_T2lPOl-SEa8xPpK0IsLLCiJt3YGKYoNPEwFhfyfS4IFG5t20s0fXxxlpaPk5iwipmHyALw3vRqw6eq_zWylZEwednkeSVflvwDLpGi7k90MAIUKkQo6j2qPwQLiPWRPNrurVWSYOwi4cOd9FkZleqBojIubKJhwCuTZT5vroO1reD_fvK2sMrXQNYi8F6jje2slYrkmZw96bHxdKv6KkyqShDQCuQjuP9HmQkJpvVsRAOgkgqQ3iz9RhNNEgmFhiKG2G-8h1nzeNNLBgBJ1emWX-8F9dnhJJfJPtXFIQRQI5pVUi_HXBmihP-NeWxzCrCrt-kGMWjw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHRbFg_OLx5I0JdI_RLIVvTX-Msp3vp90hmhs9rDmOpUtSP7A3Z7hMxfHPuGmCntrAsVvqUEC3SdavKcAghbiPSxJNf__-M3Ka4aN5wJMB4Fa5-PYXJ0NjaAyqQmrPMF9TRblc00fKKYTdAN5IKrHJdR5vAyJ_1QnEw1IEvX-isrHxeOo1xJiszWB5XXon9LCTLolsmN437rAsrFOOZ6o09Wpt8jKuLDiGBYyjp-9M6vPtVG7ESDbQxqITBfwxI8C8d1eYJvjimAXEvaH2JG715b2fbaexWZPNfM4PcVs8tTV8R3ay48OLIfHTdKBhLSPCMncZTTmH4334CtdierGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسۀ بررسی همکاری پیشکسوتان سازندگی در بازسازی زیرساخت‌ها آسیب‌دیده
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460700" target="_blank">📅 17:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe85c09791.mp4?token=dXoB40jGAeazCCF12K7ncXn7lawThw7yaJ0IamMyeyqFRjRWKECAOSpYFENViwDS-iZzAX0Q1VVV32ZLCRb5wDZzpOWD39oJneZ_TqjxIdYDJy0_Fec0ECRNHxyBW_iGWXfkozt0hthKABTWDbugQ36Iz-XW080m1vlfSsMwc27CdPswmshmtVHL496MXYb5wMkkC4ykZ7VlbcUFYaRdRgvvbND9e6UN9ZWI6j0pYOGgqoTyBFxuqbwtZn_p33gypHZTovnqkJHgRcQ-8IUj8WVFmlmSXOFtHkFrP62112w9-972UZ19IlHeuSOzn8wxFHZt9T612aeTQAo3UBV6Dqu53nvFs2Y36NRUVuYvQWUfMFqf77o_w4K3FqJAP7t-a3Sfjn9KHjb5P2vvyVDosAPb_TcwCd5CFrIYUt9SyXEKOCeirXtI_aOoYmDpbowdcXIF6Dniqz31ZNvFaaf9WCHbuqw3yXaR5rz_S3QUsSZWS0EimAk_rWbSQcorqq3JSZnEba9el9OvHxnCpwCqg7XaG117OmZWxfPb2lHu8BNKGax-ERYlgdgEXsxZWHvtdoUbcL5yRg_psfsU1GFVH7ItHz7ilh_ovUj6x_crGg3YS0Z4iPUc6LzylZAp1fjvtgSSZhIPQQxsRYEzVG-ZgFdjr5X6Y3E_XHN0RfInIQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe85c09791.mp4?token=dXoB40jGAeazCCF12K7ncXn7lawThw7yaJ0IamMyeyqFRjRWKECAOSpYFENViwDS-iZzAX0Q1VVV32ZLCRb5wDZzpOWD39oJneZ_TqjxIdYDJy0_Fec0ECRNHxyBW_iGWXfkozt0hthKABTWDbugQ36Iz-XW080m1vlfSsMwc27CdPswmshmtVHL496MXYb5wMkkC4ykZ7VlbcUFYaRdRgvvbND9e6UN9ZWI6j0pYOGgqoTyBFxuqbwtZn_p33gypHZTovnqkJHgRcQ-8IUj8WVFmlmSXOFtHkFrP62112w9-972UZ19IlHeuSOzn8wxFHZt9T612aeTQAo3UBV6Dqu53nvFs2Y36NRUVuYvQWUfMFqf77o_w4K3FqJAP7t-a3Sfjn9KHjb5P2vvyVDosAPb_TcwCd5CFrIYUt9SyXEKOCeirXtI_aOoYmDpbowdcXIF6Dniqz31ZNvFaaf9WCHbuqw3yXaR5rz_S3QUsSZWS0EimAk_rWbSQcorqq3JSZnEba9el9OvHxnCpwCqg7XaG117OmZWxfPb2lHu8BNKGax-ERYlgdgEXsxZWHvtdoUbcL5yRg_psfsU1GFVH7ItHz7ilh_ovUj6x_crGg3YS0Z4iPUc6LzylZAp1fjvtgSSZhIPQQxsRYEzVG-ZgFdjr5X6Y3E_XHN0RfInIQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملۀ موشکی یمنی‌ها به کاروان تجهیزات نظامی مزدوران سعودی در اردوگاه الودعیه
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460699" target="_blank">📅 17:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5ebc0865.mp4?token=Wa_R_G0twlWhdvVxis2a-NnGp9lKA4raCWIJGhJhVjit1pb01mPuIV3G3E4yZgVhDskiTAXD-0wvxDpaGg8hihtxmEqgs7KRPbxsN-JukQFDH5YmkB1kU0YaHJsD70C_5h0W2Xnu9SGFTJvRQgoGEtrhMZo1381GFgd8cGMm5jwAGxVa7VtpHttUJMjpntJxsH2AaXGyOhjXTUIdkbYTY7AnZwlr4ifoi5-bdoKz03DojgmDkxz9fSpX-mVd1UmCrgX8kv40pKAS9Ifysm7OXAq_-OtEBW5RwO1wWdUiMo-SiiMcmwEUbsSX-c11L5CUcGqNk0oupv2GF47WNhnN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5ebc0865.mp4?token=Wa_R_G0twlWhdvVxis2a-NnGp9lKA4raCWIJGhJhVjit1pb01mPuIV3G3E4yZgVhDskiTAXD-0wvxDpaGg8hihtxmEqgs7KRPbxsN-JukQFDH5YmkB1kU0YaHJsD70C_5h0W2Xnu9SGFTJvRQgoGEtrhMZo1381GFgd8cGMm5jwAGxVa7VtpHttUJMjpntJxsH2AaXGyOhjXTUIdkbYTY7AnZwlr4ifoi5-bdoKz03DojgmDkxz9fSpX-mVd1UmCrgX8kv40pKAS9Ifysm7OXAq_-OtEBW5RwO1wWdUiMo-SiiMcmwEUbsSX-c11L5CUcGqNk0oupv2GF47WNhnN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت نفتکشی که در خارگ هدف گرفته شد
🔹
براساس بررسی‌های فارس، عملیات اطفای حریق نفتکشی که روز شنبه در حوالی جزیرهٔ خارگ هدف حملهٔ آمریکا قرار گرفته بود به‌پایان رسیده است.
🔹
همهٔ خدمهٔ کشتی نیز در سلامت کامل به‌سر می‌برند و این حادثه تا این لحظه منجر به نشت نفت نشده است.
🔹
امروز گروه‌های مختلف برای بررسی وضعیت این نفتکش به محل حادثه اعزام شده‌اند تا برای جابه‌جایی کشتی تصمیم‌گیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460698" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ6LjWLssCW-4t5JZdbauztkcigmIxmo2XsRPN6l2cv8eQ6orzgpZq6lgfUmUdKmBkfn5CQNxFrdJL4rngTt2GUGKcnTtBfbId3DPvjthSv6HAZE3khUBisrSFMwcmjBNFI3JdVrB5Qod_o990qecO4kifNOqN3QdKJjcLOEjiEv3DqLm16Guas24kNUs6lTnSLHAi6X8erzxoGwjB_OB-4dm0Uf7VK7VWsWKMP6ZUHu08H9GVjRECG0LHxJprSFHPxwsd5lVmfpFe0Yc9-Ny2lXZiQsx7lELtzv71jsNakctValTUw1ppTQTmryOQLbGLWs4cx98bdemT_AnLw_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دست رد دیوان‌عالی کشور به سینۀ متهمان چای دبش
🔹
رئیس دیوان‌عالی کشور: درخواست اعادۀ دادرسی بیش از ۳۰ نفر از محکومان پروندۀ چای دبش، از جمله ۲ وزیر اسبق، رد شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/460697" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b99b0a2d.mp4?token=P0KPRB6kkgnAg9X-opTPImNHkZNn7uuiBNiG_0rTwtdDmAojyz1ZpYXO7ilCldSV0uAZPUPYl7ngNnCKpkTDOnUFFepp2isI4Ys3Sq__86VVeOaNcDGcaekRPktn3tAU0TZVbx6XOOOxILWL1TjEgqF53IoWoPmet-rOvKb9mnvyh-BEW7I2fQjj8sp7RaaJm6NVHTZ7bdOs9WAP1QcrTjj9m54Cn2QxzgJiBacc1tsThbV6ZgHmLqpRG79bM-PZMP31He_muiZFIoaKj1qtKSOlLyMFlsH83NlPsqnWruYnc4Guj8QDL4hy2027q2QFP25SbsLGSq8wBfdvMD9zxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b99b0a2d.mp4?token=P0KPRB6kkgnAg9X-opTPImNHkZNn7uuiBNiG_0rTwtdDmAojyz1ZpYXO7ilCldSV0uAZPUPYl7ngNnCKpkTDOnUFFepp2isI4Ys3Sq__86VVeOaNcDGcaekRPktn3tAU0TZVbx6XOOOxILWL1TjEgqF53IoWoPmet-rOvKb9mnvyh-BEW7I2fQjj8sp7RaaJm6NVHTZ7bdOs9WAP1QcrTjj9m54Cn2QxzgJiBacc1tsThbV6ZgHmLqpRG79bM-PZMP31He_muiZFIoaKj1qtKSOlLyMFlsH83NlPsqnWruYnc4Guj8QDL4hy2027q2QFP25SbsLGSq8wBfdvMD9zxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: وحدت‌شکنی از هر طیف و گروهی خیانت و جرم است
🔹
از هر طیف، سلیقه، جناح و تفکری، صدایی بلند شود و عملی سر زند که وحدت‌شکن باشد و تصویر مقتدرانهٔ ایران در اذهان جهانیان را مخدوش و تضعیف کند، بی‌انصافی، خیانت، جرم و گناه است.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/460696" target="_blank">📅 16:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaec964408.mp4?token=G5a7a8mRkXoxlq2bE9LFi_c8PwWsO8_VXwUJ1Ym3-uaxs16cbc_85ClflUgSPRppjDwGquX2mBxNy1Kgbpqru5jtj73B60Nec7ZWjjqlnaqUVdOPr1m46u5IUIvgHsFLkeE1yKLYPXbJmBPB3auZJOzc4n41ob-fheiocN-lREId1H1E4aYkXVEeyPqyCYu4AHNQMlPaaCMsVSYDiEkoWFPyGuoKR3OvQ2vnB9Btp0E-1mB88UeVwgI8XDKITWLJ3i0EuaIHFf4rEjCYwSwef9gz2jzbQm4W00C3U2hu7Dfybl__q2Jviw373aJdhPTTf4XTOwjwT7mYfi-9AKV5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaec964408.mp4?token=G5a7a8mRkXoxlq2bE9LFi_c8PwWsO8_VXwUJ1Ym3-uaxs16cbc_85ClflUgSPRppjDwGquX2mBxNy1Kgbpqru5jtj73B60Nec7ZWjjqlnaqUVdOPr1m46u5IUIvgHsFLkeE1yKLYPXbJmBPB3auZJOzc4n41ob-fheiocN-lREId1H1E4aYkXVEeyPqyCYu4AHNQMlPaaCMsVSYDiEkoWFPyGuoKR3OvQ2vnB9Btp0E-1mB88UeVwgI8XDKITWLJ3i0EuaIHFf4rEjCYwSwef9gz2jzbQm4W00C3U2hu7Dfybl__q2Jviw373aJdhPTTf4XTOwjwT7mYfi-9AKV5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز دادگاه حادثۀ تروریستی خاش زاهدان
🔹
آمریکا از طریق گروهک تروریستی جیش‌الظلم در غروب ۲۴ بهمن ۱۳۹۷ اتوبوس حامل تعدادی از نیروهای سپاه پاسداران را پس از اتمام مأموریت مرزبانی و در حال بازگشت به خانه، مورد حمله‌ انتحاری قرار داد که منجر به شهادت ۲۷ نفر و زخمی…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/460695" target="_blank">📅 16:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ca05586f.mp4?token=R091Z19PkM9_KD0AOa3FChRsgBgGU07X3Ud3Xjdd5xavuYixaXLKbvws1hOqH1jwuqOPHTuZn6o2ialrFO7wpGQZxlPl_pzcVFw4L70CHWHzUy0uUlrzpSDivz_ODVDa2RoCfkBDOJzxZfhRNOppjv164FG84sKrDvj9QyH7RKCez1qaUOFqLdVjBvZxcqg3xnYKqGP-qBxT9fs5icRnUhhBsj1qsu3NxCfspZSmGgRwF25puhIAp8UyycfqcdiFm9GY0z1hQW2_mO81rrDWt04V_bQFZ6aNUbckOgAu0lPa9k_TWNwpsIxo3UHev43NBCb6A8r68m-2tCiqiy1C5UyyQyYEwmHaZQVLvGayRg41Y72hhiXNj1H-_4dNN4t9Qc10hLiVw6YiYmASQ3IK13gN2EtvqjlEdIqXdjR0pSYPbeA8eu5CA6EmnFzMQn-uD_a8VhzeF0S6f2sGpXYIDap_yEZLWXn41OF0C_jWp_buItofQK2A0mRp-CO4vra_7spmAp79aAjfrBEeKMpPH38zqOA200x8yOb78A5pPOKJx9fufoWAI68KLEJiDSZXTwBhvMXOZ1TKS2rGdDy4-7ryUiNqvs4uPnI0ptia9GYfh1WonCGeiIEJKYG07GUTL2Ohc084lijzqWJIadbIzEoZYnMGKli1MW94QTbVO6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ca05586f.mp4?token=R091Z19PkM9_KD0AOa3FChRsgBgGU07X3Ud3Xjdd5xavuYixaXLKbvws1hOqH1jwuqOPHTuZn6o2ialrFO7wpGQZxlPl_pzcVFw4L70CHWHzUy0uUlrzpSDivz_ODVDa2RoCfkBDOJzxZfhRNOppjv164FG84sKrDvj9QyH7RKCez1qaUOFqLdVjBvZxcqg3xnYKqGP-qBxT9fs5icRnUhhBsj1qsu3NxCfspZSmGgRwF25puhIAp8UyycfqcdiFm9GY0z1hQW2_mO81rrDWt04V_bQFZ6aNUbckOgAu0lPa9k_TWNwpsIxo3UHev43NBCb6A8r68m-2tCiqiy1C5UyyQyYEwmHaZQVLvGayRg41Y72hhiXNj1H-_4dNN4t9Qc10hLiVw6YiYmASQ3IK13gN2EtvqjlEdIqXdjR0pSYPbeA8eu5CA6EmnFzMQn-uD_a8VhzeF0S6f2sGpXYIDap_yEZLWXn41OF0C_jWp_buItofQK2A0mRp-CO4vra_7spmAp79aAjfrBEeKMpPH38zqOA200x8yOb78A5pPOKJx9fufoWAI68KLEJiDSZXTwBhvMXOZ1TKS2rGdDy4-7ryUiNqvs4uPnI0ptia9GYfh1WonCGeiIEJKYG07GUTL2Ohc084lijzqWJIadbIzEoZYnMGKli1MW94QTbVO6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمله‌ای که رهبر شهید هنگام اعطای حکم فرماندهی به سردار شهید تنگسیری گفته بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460694" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68324108a9.mp4?token=lnw3LN-Wb9gaIFR7leyEyI7hHe5BJbVLgbr4cvgfQIDW7fzBHOyLChh7ZEz5ZgMTYhNpJov4BMRruccqcKcPE8Mp7o6Treo70Ee9mg2G91Jn8vEEorvaKaUcjBHAZbD_UYgcf9GVem9xqcfcyc6Q6ofA47IQLg05tkwi9MBlvx-R4wivvuitLsRerAMZP1TpthMMRzwgkUobUvYUBCNMXzJCSIOGzdDd8X-tVMvDfhxfahO67mkWjgKId22ougE4SADWDWb-qQWb7suyx9Ap3apjkEuHbBE_s-rsG3VYPJroM3wxdDCQC9zUpBsiKMcEQcSPERQNaJ_WxC5RuRrAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68324108a9.mp4?token=lnw3LN-Wb9gaIFR7leyEyI7hHe5BJbVLgbr4cvgfQIDW7fzBHOyLChh7ZEz5ZgMTYhNpJov4BMRruccqcKcPE8Mp7o6Treo70Ee9mg2G91Jn8vEEorvaKaUcjBHAZbD_UYgcf9GVem9xqcfcyc6Q6ofA47IQLg05tkwi9MBlvx-R4wivvuitLsRerAMZP1TpthMMRzwgkUobUvYUBCNMXzJCSIOGzdDd8X-tVMvDfhxfahO67mkWjgKId22ougE4SADWDWb-qQWb7suyx9Ap3apjkEuHbBE_s-rsG3VYPJroM3wxdDCQC9zUpBsiKMcEQcSPERQNaJ_WxC5RuRrAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ مجروح شدن خبرنگار المنار در حملۀ هوایی اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460693" target="_blank">📅 16:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7v8t6uL8se1F8rWQ3JonnCTa1_iuRsujuu1lUKhJu_DYN5zkQEJKm6ALmeqDwOGZPA_8t51ji2HATaJXFC18g4iKh3YnrPTDn-OQeQRChixVm0FDOJ7ureQoVfpyqMap9M8qNCbYIY5WpIyzlSRfs9zuVlM2QK8081vMEZt-tBD5cXeA13RrGKDJknfn9M4bwM0y_7vouW3NF5KU4wKUJYD5vPyYWBaZiZCUwKXQQqoTZnZf4JMr1BTw6boV2EsBE80Ky_el0N_BViSgdW0ZhwH4AfcazCNjzyfLLuQ3ge5fuP7ORKYdymcWeJWSh7svpju3cNuSZ6wzniScXyqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ وزیر روی زمین ماند
🔹
با وجود اعلام رسمی وزیر نیرو برای پایان خاموشی‌های برنامه‌ریزی‌شده، گزارش‌ها حاکی از آن است که در برخی نقاط کشور، قطعی برق همچنان تا ۲ نوبت در روز ادامه دارد؛ در برخی مناطق نیز این خاموشی‌ها به‌صورت برنامه‌ریزی‌نشده و بدون اطلاع…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460692" target="_blank">📅 16:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duqkXm0zRtL2wS8bxFeP74DQyMT0xPdN7-Se_iL-iWLH3dyyy2YqwZ1ymD7TrxKRC8FyokmhFVpbmmJTLEfHJGyNJ07aXLaIbUXL5BDtHjFPOldvw6TUt0jIfacVXZam7pulbdGRZU7JtRaQ5jU77NoQrXIS4pgARaton0XHm93Jy7pQtEH0bo3WEeqbrSAqoaIJfrCZrbN64zqe5ZUETZu6f0DBDDF9eEru-lNZp7xKaHNTe4x9BZ6FR_RmtXAKbmRcwdVOlbiPUBUD2QRtrvsxtbknDcPujWxhAuHOX-jo7zBBuqIvurBKQ7CoWrc8JViC4ThtzZVO7gI3WvxBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدی: نقطهٔ پایان مصونیت در تنگهٔ هرمز «خصب عمان» است
🔹
معاون سیاسی نیروی دریایی سپاه: عبور ایمن از کریدور آمریکایی در جنوب تنگهٔ هرمز عملاً امکان‌پذیر نیست و شناوری که وارد این کریدور شود، پس‌از رسیدن به محدودهٔ خصب عمان دیگر از خطر اصابت مصون نخواهد بود.
🔹
نیروی دریایی سپاه در خلیج فارس، تنگهٔ هرمز و دریای عمان، با اشراف اطلاعاتی و عملیاتی کامل تحرکات شناورها را لحظه‌به‌لحظه رصد می‌کند.
🔹
تمامی کشتی‌هایی که قصد عبور ایمن از تنگهٔ هرمز را دارند، باید از کریدور تعیین‌شده از سوی ایران استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460691" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3FAC-visSDzMgudMgIJolSVfOUJWvaJl0hsZvYay3cB4KLIcjWQ6Tx2v5m_h0rF9pDRcf9P03AewB5iDQUo63FwJtUmSV4owyEMgyXgcf3QPNMf-TlXwl8WUwHWCfPWPay1Jj1tdMcuBsx5nW3ncGbFSVQQBGUnrPTQKyk1RfJzWUmHYCLkValcHpDxpYsrHhPeTT2s_bwbYIZwTQzp2py3Nm-Ft70oEvXCMNdGk2w_kOZKI2au5P8J0uTJBdrlZMypm8_YuYtB1-2s3DYm3kLkjkmuz2t2KwKbzBL62TnKetXY3kdSk1pjhOo2tkvP50ZiswXCvgsDCPM0aMPPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای روحانی، دوگانۀ اصلی، «مقاومت و تسلیم» است نه چیز دیگر
🔹
اظهارات حسن روحانی دربارۀ اینکه آیا مردم حاضرند «۲۰ سال دیگر» با قدرت‌های بزرگ بجنگند، با انتقاداتی مواجه شده. منتقدان می‌گویند پیش از طرح چنین دوگانه‌ای، باید دربارۀ تجربه ۸ سال اعتماد به غرب، مذاکره…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460690" target="_blank">📅 15:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر کار: معوقات فروردین بازنشستگان از امشب براساس حروف الفبا واریز می‌شود
🔹
میدری: هر شب ۲ همت براساس حروف الفبا به‌حساب بازنشستگان واریز می‌شود.از بازنشستگان عذرخواهی می‌کنم که همواره پرداخت‌ها با تأخیر مواجه بوده است.
🔹
درصورتی‌که از اوراق گام استقبال…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460689" target="_blank">📅 15:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ کسب‌وکارتون رو به فرصت‌های بیشتر وصل کنید!
✨
💫
با «شهرآسا» بانک شهر، فعالیت پذیرندگان می‌تونه مزایای بیشتری برای کسب‌وکارشون به همراه داشته باشه؛ از تسهیلات و جوایز ویژه گرفته تا امتیاز و قرعه‌کشی ماهانه.
💳
با اتصال پایانه فروشگاهی یا درگاه پرداخت اینترنتی به حساب بانک شهر، از مزایای ویژه شهرآسا بهره‌مند شوید:
🔸
تا ۷ برابر میانگین حساب دریافت تسهیلات تا سقف ۱۰۰ میلیارد ریال
🔸
جوایز نقدی و هدایای ویژه اصناف
🔸
تجهیزات جانبی ویژه
🔸
تقدیر از پذیرندگان برتر
🎯
به ازای هر ۱۰ میلیون ریال تراکنش در ماه، یک امتیاز کسب کنید و شانس خود را برای برنده‌شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
یعنی اینجا، فعالیت بیشتر می‌تونه فرصت‌های بیشتری براتون بسازه.
🚀</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/460688" target="_blank">📅 15:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21401f4c23.mp4?token=c6QWE9k_XgRlqMSzEr-UBpqrbLkNCmDDUy7xjo04Wdjoa2OOpvlYv_oMWKbLmvt_zFdKkJKHAqw0Qt28ZR2kgAWY-BsRKDHV8hI5T0IEOttoOnbHhoKrSf2ZY1nId-U14PSboIWQbhBEGOpFXS7EpGLTemSHGi7ukZjeiD0O-h8kRvGg3nIhLQwWcDsf__kf0CwwrrOkf3GudLIZhBskRhjPjQHV_uDceuOCNcw7e5FTwUjhxk7uFDSaDgyzw0CD80KB1RvsQCj0HeOOHztgzfrYsp7wB7jwSc-ks58pO8ORu5dNKN103Cy19dp4EpJ3acyFPV1cXhC6I7nx8a8lMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21401f4c23.mp4?token=c6QWE9k_XgRlqMSzEr-UBpqrbLkNCmDDUy7xjo04Wdjoa2OOpvlYv_oMWKbLmvt_zFdKkJKHAqw0Qt28ZR2kgAWY-BsRKDHV8hI5T0IEOttoOnbHhoKrSf2ZY1nId-U14PSboIWQbhBEGOpFXS7EpGLTemSHGi7ukZjeiD0O-h8kRvGg3nIhLQwWcDsf__kf0CwwrrOkf3GudLIZhBskRhjPjQHV_uDceuOCNcw7e5FTwUjhxk7uFDSaDgyzw0CD80KB1RvsQCj0HeOOHztgzfrYsp7wB7jwSc-ks58pO8ORu5dNKN103Cy19dp4EpJ3acyFPV1cXhC6I7nx8a8lMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوت آغاز هیجان زده شد!
🏁
«فرا‌لیگ» دوباره شروع شد
⚽️
از لیگ برتر ایران تا جذاب‌ترین بازی‌های انگلیس و اسپانیا؛
📲
نئوبانک «فرا‌رفاه» رو نصب کن و وارد فرالیگ شو؛ نتایج بازی‌ها رو پیش‌بینی کن و با هر حدس درست، امتیاز جمع کن.
🎉
به مناسبت ۶۶ سالگی بانک رفاه، هر ماه ۶۶ شرکت‌کننده ی برتر فرا‌لیگ از هر لیگ، برنده جوایز نقدی خواهند شد.
🎁
در پایان هر لیگ جوایز ارزنده ای به شرکت کنندگان برتر تعلق میگیره
🔹
"فرا‌لیگِ فرارفاه؛ میدون رقابت فوتبالی‌ها برای جوایز میلیاردی"
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/460687" target="_blank">📅 15:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/460686" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c185f8a03.mp4?token=KrCXrqHlc_K5RtsisQ_duq6u-_iGSwFl4ERUNiWh6wrD3cbUt-sN05sk0CZ2HCD7jWBS-H5TVUtmrUi_30yTEoBrMNOKUrAEoNoy-z7d6Ckrqepg2iN2McuIg8mf7X9ueUd9cycjvCaic8yqdzcLVM4Ecsz3jxI5iPgQSme_h8fuGOMp4fYNj7oyQHe1kufQo8pYhAaLsValjLr0iiND28RZ7FlGD9EJnIJs20FruTwQNQEMnxZWRScYtsokLStNdxEVkm0aDiI3cKwVwLXquPgdpzy1b-iBmSVtl5d56A7zzb0maRbqrp8K6KIIlJC0HuKZyG5DirYIKCJtWzX2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c185f8a03.mp4?token=KrCXrqHlc_K5RtsisQ_duq6u-_iGSwFl4ERUNiWh6wrD3cbUt-sN05sk0CZ2HCD7jWBS-H5TVUtmrUi_30yTEoBrMNOKUrAEoNoy-z7d6Ckrqepg2iN2McuIg8mf7X9ueUd9cycjvCaic8yqdzcLVM4Ecsz3jxI5iPgQSme_h8fuGOMp4fYNj7oyQHe1kufQo8pYhAaLsValjLr0iiND28RZ7FlGD9EJnIJs20FruTwQNQEMnxZWRScYtsokLStNdxEVkm0aDiI3cKwVwLXquPgdpzy1b-iBmSVtl5d56A7zzb0maRbqrp8K6KIIlJC0HuKZyG5DirYIKCJtWzX2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/460685" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4414a580ef.mp4?token=qNtEZ2zA3ibfu284xJL41fCilFR2vSaAovEX21zH6Sx3JkxPdCus5CzLKHUl2WajMHSOAyNGsGrMir7dmO4BRXZw6WYo2jygQSHnYCW6xmL4LdMZQe7X3YXzmdKE6QTjKRsiSq4Ji56syd_Rc5unMpMQyJBXBTLwypjhQM-_fLtw-_V5PMesYnawcNwTbsmWJQqZiEQl72BbE_fz70y36b7w3kn_whCunaOJsq_4CLFrKYIg_mswnIQun2NBDaEMC4gYJpe7lmjSvdJzaHbDurGF20HtKuETxg0kGwJuzZmTHOQqUoPC8hzzGFjaxIf4wpgBGZCxotfwxtvV3IGbiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4414a580ef.mp4?token=qNtEZ2zA3ibfu284xJL41fCilFR2vSaAovEX21zH6Sx3JkxPdCus5CzLKHUl2WajMHSOAyNGsGrMir7dmO4BRXZw6WYo2jygQSHnYCW6xmL4LdMZQe7X3YXzmdKE6QTjKRsiSq4Ji56syd_Rc5unMpMQyJBXBTLwypjhQM-_fLtw-_V5PMesYnawcNwTbsmWJQqZiEQl72BbE_fz70y36b7w3kn_whCunaOJsq_4CLFrKYIg_mswnIQun2NBDaEMC4gYJpe7lmjSvdJzaHbDurGF20HtKuETxg0kGwJuzZmTHOQqUoPC8hzzGFjaxIf4wpgBGZCxotfwxtvV3IGbiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌ها همچنان از آرزوهای برباد رفته‌شان می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/460683" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c445b6b71.mp4?token=JlDmpIvJDz1kYFHtFJKfpWgYiz07C3hGin3H_2WqowpKLskKn-7ZvFpusxmZKvqk3yvP-OgORhIBaXr61fIq6DsAdDrmDGSfmh7SH4fuj5GsJnXzEBSws2s0KXzsL00q7dcgKEFQaR9R7To7SFJdEfGqdQrgB5IOqZT5lLqSqoAhX-JEu2_fGObbBf4MHF8YtFZnM_CQZ8GdXCQEK-TKAXqTbkNFjJOEtHK7T0AK_iuX2rAMVDqiHy5p2vfHpEZiPHfVMWWxdQJcCtdGHr4h9lYi7Lmra1GgRjaFTTuG4lUnwg6B4hlKfBGTHyCq81RBne2vHIoJPhXVCrMu60YBYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c445b6b71.mp4?token=JlDmpIvJDz1kYFHtFJKfpWgYiz07C3hGin3H_2WqowpKLskKn-7ZvFpusxmZKvqk3yvP-OgORhIBaXr61fIq6DsAdDrmDGSfmh7SH4fuj5GsJnXzEBSws2s0KXzsL00q7dcgKEFQaR9R7To7SFJdEfGqdQrgB5IOqZT5lLqSqoAhX-JEu2_fGObbBf4MHF8YtFZnM_CQZ8GdXCQEK-TKAXqTbkNFjJOEtHK7T0AK_iuX2rAMVDqiHy5p2vfHpEZiPHfVMWWxdQJcCtdGHr4h9lYi7Lmra1GgRjaFTTuG4lUnwg6B4hlKfBGTHyCq81RBne2vHIoJPhXVCrMu60YBYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگاران خارجی برای انعکاس جنایت‌های آمریکا به سیریک و میناب رفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/460682" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
این مردم ۱۹۰ شب است که در میدان‌ها حماسه به‌پا کرده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/460681" target="_blank">📅 15:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e5181b6f.mp4?token=hYaM5q-FpKl9J5EtNksllw1t1sda0iM7ONqfNI0dghdwEZp6JB1IymZRVwu2BiHfHeaCSYd82MUQtHuw4JshIidhQjBqeBpZfIsaPFvcuv-3_0qMOXpCjWE7xkb-5KNYCdV5aD1EjsAC9DWKG4K5cBYIu5NTokR8oaUOLy5jTuNUSDqcucZ0zipJyCwBscwjpdpVS4ZAc9vvA0gjCIWG6GndFIl609isR33NfsmPSlRy1JfyR7I_xgzOJHMkjzUTBMMKXvI4A3AduxIpdwsK8mp7Tp9y43y2jmkRu3uxpQAcrvHSzaJwNA5ik10c-rcO5Bzd-PGjlfoyK0ucV3DPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e5181b6f.mp4?token=hYaM5q-FpKl9J5EtNksllw1t1sda0iM7ONqfNI0dghdwEZp6JB1IymZRVwu2BiHfHeaCSYd82MUQtHuw4JshIidhQjBqeBpZfIsaPFvcuv-3_0qMOXpCjWE7xkb-5KNYCdV5aD1EjsAC9DWKG4K5cBYIu5NTokR8oaUOLy5jTuNUSDqcucZ0zipJyCwBscwjpdpVS4ZAc9vvA0gjCIWG6GndFIl609isR33NfsmPSlRy1JfyR7I_xgzOJHMkjzUTBMMKXvI4A3AduxIpdwsK8mp7Tp9y43y2jmkRu3uxpQAcrvHSzaJwNA5ik10c-rcO5Bzd-PGjlfoyK0ucV3DPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزلۀ سیاسی در آلمان؛ پیروزی چشمگیر راست‌های افراطی در انتخابات ایالتی
🔹
برای اولین‌بار از زمان جنگ جهانی دوم و سقوط نازی‌ها، یک حزب راست‌گرای افراطی در انتخابات آلمان به یک پیروزی مهم دست یافت.
🔹
برآوردهای جدید حاکی از آن است، حزب راست افراطی آلترناتیو برای…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460680" target="_blank">📅 14:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای آتش‌سوزی در یکی از تأسیسات آرامکو واقع در ینبع را تأیید می‌کند
🔹
این آتش‌سوزی در حوالی یک مخزن سوخت اتفاق افتاده و تصاویر توسط ماهوارهٔ Sentinel-2L ثبت شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/460679" target="_blank">📅 14:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471897a3ba.mp4?token=vOwGnKb0bBbRQIG-nw6opDTHJJvgn3DJTnEztBRsPgp1Xj6DAuAVzn8H_oR-Qv-5M2-PMsdCnOhehsMeRp8ZsC9ibt9gTWHqZ1jtbodjTrkw8NlTUX2z9asp_jUhL7wy8gSO3gk2xyVhO8mn_5bRad2tiQOUqWg0YmXoNl740MTJWkUXgen9SmjwKMX3i1zq4lnuP5KM2SGgUwd3pZdhHf1c_tBASS7_wvC3S8q9K3Lac66j7wVYm2R9-5W3OpVRSiM7m8g5j1PJUnUF6sOnasC3UZ4fHszcTO55ckyf1d-vA_MbvawO-N9zuukFtD6GQAxqQTYVldK9N3t8LQERfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471897a3ba.mp4?token=vOwGnKb0bBbRQIG-nw6opDTHJJvgn3DJTnEztBRsPgp1Xj6DAuAVzn8H_oR-Qv-5M2-PMsdCnOhehsMeRp8ZsC9ibt9gTWHqZ1jtbodjTrkw8NlTUX2z9asp_jUhL7wy8gSO3gk2xyVhO8mn_5bRad2tiQOUqWg0YmXoNl740MTJWkUXgen9SmjwKMX3i1zq4lnuP5KM2SGgUwd3pZdhHf1c_tBASS7_wvC3S8q9K3Lac66j7wVYm2R9-5W3OpVRSiM7m8g5j1PJUnUF6sOnasC3UZ4fHszcTO55ckyf1d-vA_MbvawO-N9zuukFtD6GQAxqQTYVldK9N3t8LQERfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی خطاب به ویتکاف: بیشتر به اینجا بیایید تا اوکراینی‌ها بتوانند بیشتر زنده بمانند
🔹
رئیس‌جمهور اوکراین پس‌از گفت‌و‌گوی امروزش با ویتکاف و کوشنر، نمایندگان ترامپ، از پایان دور نخست مذاکرات با هیئت آمریکایی خبر داد.
🔹
زلنسکی در پیامی که خطاب به فرستادگان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460678" target="_blank">📅 14:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04260caec9.mp4?token=nlb9Ybb3ehmuS_mr5gK_vc8CsprvrPyiHL6awmi0TmR0rp05TFnPSkta7HETaE_DDUsWIhuwCLO_uWvu9q60SPSWbUJd1bWYM-K0HWwXs-roCEQOLyZQXFMoMh7kZK2ojmvhSAlSXiSUXLWn91lqYI3WvP7jfY66GOAyiWmagNe29quuvEwv3CExUAGRTDeqJsMMwEANQEGIGUjDjIgT_XCpSzdOvnJRwR-SigRysurx0WCTtUSSrVPiSMLafxdiNwPfOR2zbSZRP3TCnaXl4Fh5TZ3wXHfehB-1tIyN9mZrcbYd3KE8tIogIAu0ZvG7bWFA_mgLfT1as_COK307YkD_iSOH03anNSJdV3pshX4SGeMehk7PAPCTUxat7lGe6E9SPGkmdLsKx4H9W5ER42icyikOjQRWhTREl858W1eVsnuS5slZi5FKUD7H0SjQ5zMH3nEKJcZgt-PvGjWUh-OcDKPoZbQl3wG6W22hAd00qdRBJocLU20HTnaUL2C9b1AAqOwpnCXPhmbPsQlyx-l8G2P3z6zYGDz3ZmZqD8Zp8zcGUt2jb3btCyppsrZtXD1gHQv3GCqdrpFTR_f9eOlCCqQDKZZfd66lL7chdYDN9VQX02pCMcEQFsuCk1I_kRLKQ4__xGjAFHpCdpM0OVKrRuv1omgtq2n5OvRljFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04260caec9.mp4?token=nlb9Ybb3ehmuS_mr5gK_vc8CsprvrPyiHL6awmi0TmR0rp05TFnPSkta7HETaE_DDUsWIhuwCLO_uWvu9q60SPSWbUJd1bWYM-K0HWwXs-roCEQOLyZQXFMoMh7kZK2ojmvhSAlSXiSUXLWn91lqYI3WvP7jfY66GOAyiWmagNe29quuvEwv3CExUAGRTDeqJsMMwEANQEGIGUjDjIgT_XCpSzdOvnJRwR-SigRysurx0WCTtUSSrVPiSMLafxdiNwPfOR2zbSZRP3TCnaXl4Fh5TZ3wXHfehB-1tIyN9mZrcbYd3KE8tIogIAu0ZvG7bWFA_mgLfT1as_COK307YkD_iSOH03anNSJdV3pshX4SGeMehk7PAPCTUxat7lGe6E9SPGkmdLsKx4H9W5ER42icyikOjQRWhTREl858W1eVsnuS5slZi5FKUD7H0SjQ5zMH3nEKJcZgt-PvGjWUh-OcDKPoZbQl3wG6W22hAd00qdRBJocLU20HTnaUL2C9b1AAqOwpnCXPhmbPsQlyx-l8G2P3z6zYGDz3ZmZqD8Zp8zcGUt2jb3btCyppsrZtXD1gHQv3GCqdrpFTR_f9eOlCCqQDKZZfd66lL7chdYDN9VQX02pCMcEQFsuCk1I_kRLKQ4__xGjAFHpCdpM0OVKrRuv1omgtq2n5OvRljFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در همایش افتتاح ۷۹۴۷ طرح خانوادهٔ ارتباطات
🔹
رئیس‌جمهور: اگر باایمان و اراده بایستیم دشمن نمی‌تواند مانع رشد ما شود؛ ما میتوانیم همهٔ مشکلات را به همدلی، همراهی، انسجام و وحدت حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/460677" target="_blank">📅 14:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcBZScg0I5kExWiww1BKEROmIldlRLCUD4QyCgQZjtKMDj0IuSI7mjjui1eO8apWkerb4v1ekTBgKsG0g2iDg6DP2kljJVf3YkH-NiXNoXdKh0eJKwAbGxw3jslTIy1Xb9j6-2QT0XgMBY5l6csz0npGwPMBJYtXMAfmKRcu-lXsKonjaiK7cqLcS6-5S9UFaOu5bbjPebp03DwSnjLgopWrfgAwlli5l2mHucGct-Dy_LpsnelcUXcgH2p46CmnBs2knyKdHMRPeXBmUIvaqvzlu3HFPQ2H4FTLaNqBiICQ3ct5sVmECofaJGi9zZ_yI7MghFqE7UOi5HVDZH0i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری و بین‌شهری نیز باید مورد توجه دستگاه‌ها قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/460676" target="_blank">📅 14:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌ نکردۀ جنگ در بوشهر
🔹
فرماندار بوشهر: فردا از ساعت ۹ تا ۱۲ ظهر خنثی‌سازی و انهدام مهمات عمل‌نکردۀ باقی‌مانده از جنگ در حوالی پایگاه هوایی بوشهر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/460675" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGqZ_UaFvn6M5y6Q4u0UvvKtWsgaScX5D2Gw7sJosWtRPAlHcno9xp8Hw2Pp890B99ss9V3X2wG-WN6iD18k_LCWevr3YFlUSPw-3Jw28UefB9SDojuNrrZJ3CG0Nvf9y4sbcf5yD-rEnhi3HbkkEkfzPfDl9u5qcqA7FSXcd4ydxUW7KEBhWZkJWArMcut8TwVyHWpKGVXia7oHqVcjoFI53jQOuZ_sxN0e4agMlgh6slapiueNr0XebJOHKGcwQImUasKew4cyNng1wSuHr8S9jsAnaiakARL24jij0tmyCcM1krhN9okCiEhPe_LEAx0-Cr-FuFc0EWqUDO_tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی دریایی ارتش: می‌توانیم دشمن را در هر نقطه‌ای زمین‌گیر کنیم
🔹
دشمن امروز ابتکارهای عملیاتی نیروهای مسلح ایران اسلامی به‌شدت نگران است و با توجه به پیشرفت‌های حاصل شده، در صورت لزوم می‌توانیم دشمن را در هر نقطه‌ای زمین‌گیر کنیم.
🔹
غافل‌گیری دشمن در مأموریت‌های مختلف، به‌گونه‌ای بوده که توان عملیاتی برخی از ناوهای متخاصم را برای مدتی طولانی مختل کرده است.
🔹
مأموریت اصلی ما این است که اجازه ندهیم دشمن به اهداف خود برسد و در این مسیر موفق خواهیم بود، چراکه تحرکات دشمن به‌صورت لحظه‌ای رصد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/460674" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d21b4626.mp4?token=GtKyYeQrDoCpGEWaRRYoDdCXekOZcJdjNgHvicC71mgH58E2toN21984tGCg_pTz_MyI15WbB08_QDjcniuphlDx3zf6CxEFOAC3pzNkKzrCWeDXdYiO2HPqiDzEBrPP4luhKmRLM3I1onGEZgArsAwcEznekhOvNlAPSbLUHrFd4yOyOyiFdCf_U5JUlq2TscwDNCpA1fFKkL8X9mChNVMcHLOzbThGSXIkvji4BMjMEXk-adKBayZTgng5tRaRB0ftEQVTplGrw5y4Qda3VvwPhqBPiVIAGQo8NgQlokkbn_Ot_y4RBXsNxUIZZM_VQt5vggIDCSYrROuDl8HKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d21b4626.mp4?token=GtKyYeQrDoCpGEWaRRYoDdCXekOZcJdjNgHvicC71mgH58E2toN21984tGCg_pTz_MyI15WbB08_QDjcniuphlDx3zf6CxEFOAC3pzNkKzrCWeDXdYiO2HPqiDzEBrPP4luhKmRLM3I1onGEZgArsAwcEznekhOvNlAPSbLUHrFd4yOyOyiFdCf_U5JUlq2TscwDNCpA1fFKkL8X9mChNVMcHLOzbThGSXIkvji4BMjMEXk-adKBayZTgng5tRaRB0ftEQVTplGrw5y4Qda3VvwPhqBPiVIAGQo8NgQlokkbn_Ot_y4RBXsNxUIZZM_VQt5vggIDCSYrROuDl8HKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رشد ۸۵ میلیون دلاری حجم معاملات ارز تجاری
🔹
حجم معاملات بازار ارز تجاری از ۴۶ میلیون دلار در فروردین به ۱۳۱ میلیون دلار در شهریور رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/460673" target="_blank">📅 14:27 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
