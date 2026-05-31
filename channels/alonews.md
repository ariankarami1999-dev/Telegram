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
<img src="https://cdn4.telesco.pe/file/urFNX22FrJggyHxBjMD_j3Q5_l4L9NJN-jTYlsscJc-qppcgHVp1kf3V9evIbNGSonmr3J-lHWW7WWWJPuv4vu6zJqLDu7n1lIKqf-vbsYcUeeCrW0ij3gZOsWV_g2fyFuWfQrOtSHC7haPFQxeAc7-XfP2425_R3UDDia49UkIU45rnOZVgE3YO4mH8hsk8lhssIfPHktJY0CPN_AMNdoK9PeyJK1sAZyKaNtQMIDSugDIP8Fra94gsXNZZt3UYqo1_EW_8IQWbq5jKyaG0g0sn4CKZeRO6gWOeWtNZDUdc4QCVPIj_v0afBfT8_jM35yDv8dFJTZH3eUzfnS_ETA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 904K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 01:00:29</div>
<hr>

<div class="tg-post" id="msg-124067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_d7OLPo1IKrEacIxaPGHwbel2IT7jx6OeNGkCtU-JsRLcUEJf-w3zAGMgvn4CVjbv3Mm_Bm-anNYAXZ_7v9JJZzE5CBydXKgG-uh5ttYiKXo5LE73ynO73Romy3J7Tw6wloAZ8poqp3T_DeiFrJJFZqVGz86hkazhVt2Hm1KNSo3xzY1JXd4A20xNWcDLgqawlCBx027akIRvlbMEq9D_-XDJ037ZQyT_RBtU-utMOyJ4UILBHGjJOxXFrpwN2Mekorao0r33RPzD-dRFN249DqMAYItVTvYFsblhCrkAu9pFLl8uXhiterkH_4shN9rZT0z2ApjON5Gy-QwS9PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری ‌CNN اعلام کرد که ایران اکنون 50 ورودی از 69 ورودی تونلی را که توسط ایالات متحده آمریکا و اسرائیل در 18 تأسیسات موشکی زیرزمینی مورد اصابت قرار گرفته بود، باز کرده است
🔴
تصویر متعلق به یک پایگاه موشکی در دزفول است که چهار ورودی از پنج ورودی آن باز شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/124067" target="_blank">📅 00:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SGfKgFN0Po3sjzNOH1fLJiZPkfi9UOMKCJm15Dds72KjQ4VPyByYH_sp3ut_hiX_cQWPa_BTM2qro2vnDMEgZKezTHvXW8FaYPfzudQrd-ldG-sARYQrHrd5589fZFdqC4v3gYJu-apbP89wu-RbSfmen4jmKdf1u0PEQftVt0Y-cUXJ0YjWoxuyS4s5FM7NeIw9jixfqzVScUGx30bOIHgdM1fQvilhU30hfepphIbtKDMB6yd84Xmcdvmit5ShbcpR1gQrDRjl5RI6UIexacQ2ASK8G3qwD2GyHi2nPo67V47bz1lX9tWlr1uLXuQGF-gkv5A9gcRlG0h2QJFH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tz_9QT8D4bjy2nTfhXqzaIRAUbNDCNv3hVN_Daeyrkq1ms13nIH-RLzmYEMjz7weW2h6KeCebK0uJcJXTxA261RAkoLQB6ndL57FJfhtUx4BfqjsQRQ9ounVp7cACQn__R2OrvraHAVS3S41igk2krrYWaWmExIlIKCH-RVZb4VC7SZifa_v25D5G7dUvTLehj-6vXsAionEgp4-aQlXC98krZrPvX7wlYGL0F9Cr0oMkkU5TUxi1gihN1xWtCQiozp2-b7no_jx99bJH9e3ZDQyLVXaqId2nSX9yC-KoqORfhL_TJiSWiQK0lp8Jmd54-RGc_urNhAgxnt1XK1zhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رژه روز اسرائیل در نیویورک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/124065" target="_blank">📅 00:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26430ec32.mp4?token=XyBbNMg0k_juENm6SuKlZayb9Dw9KSIzwzmSkQm-yCzkSVIYhqu7U3PyzRZ1LLw7ir5VT4U1UqesX3WWnDWu7rApG1ZPmIrECwQUVNGvfYoaEUFSIZeoP5mlDLoTXNCnwCn5EWP2qktKf0F0lf24PInMaQ0hQRLVpTe9vIBG2JAP66HIhf-XRHr8-2llxritbPbS3H09WLVYGRO3BUgHjIdb_s6MX7iLNMkJhdE4Rv2cGHAYNPsI3gfn5WmCPZqRTYjRi48xRSafyJIFPJigaEysQejzq4Tk4UfbpZ0k3F4vkAItmZ12HKOUhXbZKLe94j28HSljMWKKAmHWMerOew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26430ec32.mp4?token=XyBbNMg0k_juENm6SuKlZayb9Dw9KSIzwzmSkQm-yCzkSVIYhqu7U3PyzRZ1LLw7ir5VT4U1UqesX3WWnDWu7rApG1ZPmIrECwQUVNGvfYoaEUFSIZeoP5mlDLoTXNCnwCn5EWP2qktKf0F0lf24PInMaQ0hQRLVpTe9vIBG2JAP66HIhf-XRHr8-2llxritbPbS3H09WLVYGRO3BUgHjIdb_s6MX7iLNMkJhdE4Rv2cGHAYNPsI3gfn5WmCPZqRTYjRi48xRSafyJIFPJigaEysQejzq4Tk4UfbpZ0k3F4vkAItmZ12HKOUhXbZKLe94j28HSljMWKKAmHWMerOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این 2 دقیقه رو حتما یه جا سیو کنین و یا بفرستین پیوی رفیقتون که گمش نکنین! هر بار این کلیپ رو باز کنین مو به تنتون سیخ میشه که طی این چند سال چه اتفاقی افتاده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/124064" target="_blank">📅 00:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d653bc80.mp4?token=B2MLw4E5u1xQjMt9NWNddwCDmtQUPgPkiOqT6h7iSRnpfVYUizhbASzsoL4dKx3nXUxMl7HmUc6PLs1qvFfwyKttH5biWi3K9iCI_ZUfZ_SDbyNw3XZqo_cpiz98EIwrnXRev0wnSRZH1c2OPxCgPUfnW7EvXSbYwGWbHa4UtodvhwdBE3zJqoo21enS3IsJ-NXxCc1n53BTL02qRe3pVRqUSXw3Wr-v5z_6R-JPSLISxvW5cmUAafzBmBdUXgSMAs7xBGVJRSU_a1f9-3cpWb3uSeSezCYgCcf5u6NM5BNZkwupwNiXo1rh3SMijOzdRtcuzWWPpcb6Jsp9b-LfKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d653bc80.mp4?token=B2MLw4E5u1xQjMt9NWNddwCDmtQUPgPkiOqT6h7iSRnpfVYUizhbASzsoL4dKx3nXUxMl7HmUc6PLs1qvFfwyKttH5biWi3K9iCI_ZUfZ_SDbyNw3XZqo_cpiz98EIwrnXRev0wnSRZH1c2OPxCgPUfnW7EvXSbYwGWbHa4UtodvhwdBE3zJqoo21enS3IsJ-NXxCc1n53BTL02qRe3pVRqUSXw3Wr-v5z_6R-JPSLISxvW5cmUAafzBmBdUXgSMAs7xBGVJRSU_a1f9-3cpWb3uSeSezCYgCcf5u6NM5BNZkwupwNiXo1rh3SMijOzdRtcuzWWPpcb6Jsp9b-LfKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسعود پیاهو، کسی که ویدیوی مرد نشسته مقابل موتوسواران یگان‌ویژه در خیابان جمهوری تهران را منتشر کرد، به ۱۰ سال زندان محکوم شد.
🔴
ویدیوی این مرد که در دومین روز اعتراضات دی‌ماه ۱۴۰۴ منتشر شد، به سرعت وایرال و به یکی از نمادهای اعتراضات تبدیل شد.
🤔
دم از عدل علی میزنن ولی به معاویه گفتن زکی
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/124063" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124062">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6v4tZACRPCJ_MqQOh2BE2WahPVH0hf4K2bFQMjNOTTV92L7icpguCNLiGD1JirTBlB9kcAh1lBCIHtqPDIlwbgAzhMHGkbSFRojbiLSd8za_bTB5EaOWN3Eck8Xs6Rfps2sy72BlS4r-Q88_TO2VBSh_Z3daTyjVATlsw4WvLtPFYHMiDipmjeLeHa88SM7CYf4yHzL5pjfx4aRSmjwngvScF3m5_P3X2tvYAkm2P_wUCo9Eb_cViq5XIgE1kqISdaOUTkagykTEXhG4K8RiHPK8Kkj-NNyTr54-HawUpQhyLMepwE9-dqw7-a5epK2FSwNpfflOuK3uQsnwTGqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله شدید عارف غلامی، بازیکن استقلال به محمدحسین میثاقی
@AloSport</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124062" target="_blank">📅 00:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124061">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نبیه بری، رئیس مجلس لبنان : اعلام کرده که خلع سلاح حزب‌الله را تضمین می‌کند و قول آن را می‌دهد اگر اسرائیلی‌ها حملاتشان را متوقف کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124061" target="_blank">📅 00:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyYvTlHT0LgNTtn3H5ifers6h_uXt_fFTvgncCsfWOD0ogA2Vf8ixj32aH8hTZsbpzimBGiLZ3DelhZXu-cFl5QnzAOsWPt2CsbwIQO-cQNKMChCk5VK9aaYWESxrRS6XbO9Q4nS2fn0_jwy2EZqQzpawUvGqwtH68Vq97R6moj7ZKdQ_L7q-a5y74Cld9zSOa7GYfuL3CVBg71l68J6nCyojJ3nkVmkGAXikc71k1zwNMN9oEbQ1Gj7t_FCF4CMPR7s3uCfPMXbWvBNAPdJZrwCwwpcjohSxjYScgaL6Ez1UYrBcgW59w5V7wz4hixIB0qTQf4f9W1NwO0eUXLl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد انتحاری به سمت روسیه پرتاب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124060" target="_blank">📅 00:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxv_IVMIrcQyyRKgk4lKQbKo0JUtto8mGfmVTsb7Fv4hnsG29sAmTRMjbQI67v7UrPVeS2w5WWP5aNm13UVzVBOxxPE5vLzuJbulKDnwsyzkWLfxdXQd-xYobBvgcF_NenO58GyHB21mAoFOtjKeaCxZNzyTEEvKJdJKiZDs35-wjl6ZxdleSN49Ci-MOposhANuIgl7XwHkPNzId6ZPdrs9ZZ2gzAG6dyXLBBsthctag8taHp_cFxTeo_utYTMdqStSqC-6tUATAnXUyBGswODQo7ezF92YR5ydNnhUGgmul4Cm3Ky9RnZQ9qaZDgotkhAmjjyTzktleMCLN9skUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124059" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه خبری المیادین گزارش داد صدای چند انفجار در مرکز منطقه کردستان عراق شنیده شده است.
🔴
هنوز علت انفجارها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124058" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTXVNW2SAjwyTHtBH6WRVOaosdaQMgg_khdDDvhQyX3DnZYeYxSzjjf3uQCpsSGljFUrKQSglQx07uSiRYGPp0eUNmsMSwrUN68F8Jg5qw0_TqYUjSR7aBlPgbKM0qY5Rw2AksJsr-Ck7F_TOS0wKNiVY4Q5ob8XgnNRMhgVfId4AI4B6-V2Zwwx19Mm8GwIY9S-faoToLSpHF3JwOgNr6x1uJMqb3bdU0c042sbvQcpIy8L2pUiFHxum8Vfw4t2gK6lSshU5a4e70H85C32cLn7LlJAce789o8DdiCpt0kMkV7gTBLqVjMEifUnz4VoDWN7jH5t1zEjeeVyiD7E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز: چهار نفتکش ایرانی با محموله ۷ میلیون بشکه‌ای ظاهراً به ایران بازگردانده شدند
🔴
بر اساس یک تحلیل تصویری، ۴ نفتکش شرکت ملی نفتکش ایران با مجموع ۷ میلیون بشکه نفت خام در ۲ تا ۳ روز گذشته ظاهراً برای خروج از آب‌های ایران حرکت کرده‌اند، اما به احتمال زیاد مسیرشان تغییر کرده و به داخل بازگشته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124057" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
انفجار گاز در مجتمع مسکونی فاز یک اندیشه با ۴ مصدوم؛ احتمال افزایش مصدومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124056" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ماکرون: ایران و آمریکا باید فورا به توافق برسند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124055" target="_blank">📅 23:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5SpUgCX4vw4-NfhOUpCwlsfo5orqC8FX7tbe0WzciNtRcpLmB2VRCCqzvEXRB5UnMqoQbOIGCL6p12WP8htTdTEAz2wwX9efModMnvvvt9kB57xWWsgIVq7SG1oTLj8_tKGONZd7Jd-r2qcVhzKN-73azafkSqdqtrE4V2k_MARAdbQZnld38ujmEtqchsrCQqKK5A_YBm33qpKN6o_WxLBag8noHOFs3k-FcM-pNb-z6PyFnrbTfnm2AOXWxQ7LGLW34L72rb13Bu7P7aKB0IjW2Om6kVX_DnE25Jj_k4bANT-Bx-5tqusXTvPge_zR2-MxW_1_ht1vcHu50XYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: سه ماه پس از آغاز جنگ ایران، تقریباً غیرممکن شده است که روحیه صعودی که بازارهای جهانی را برای دارایی‌های پرریسک هدایت می‌کند، کاهش یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124054" target="_blank">📅 23:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHPDzGBAXx6ZhwpARsHORZ3i3euFfGJ3XFZIJiRlRcOMiJ3Wvh971N9UUPpUYAHcGclFtL8CrGdQYglJMINwgaOq41kUCevLGrhVCEdu4g3gdrmWLYtHIv0hs8bmpZiiJzA_JO46cyflyTZv8PBXWBS0LoNYZqOa0oULg-L8F4XbuNXJ9QXHp0ldtlXIxyJwPDf1YXyt2pv7acSI857f3BiPVUP78rAVYElo8C4Ztt7JOiAqwuu5PIGlKXBExXyKmfZFhrcYuY9qeWsS-2A5187Ga2zehcxCdxgzrxcQdfJR0x9A841UxPuQBZkvrZ9e-S50u7l9L0uqHTiDMJ0kAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت تانکر های سوخت رسان آمریکایی در خلیج فارس
🔴
همچنین آواکس E3 نیز بلند شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124053" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124052">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خارجه آلمان: پیشروی مداوم ارتش اسرائیل در جنوب لبنان نگرانی عمیقی ایجاد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124052" target="_blank">📅 23:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124051">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: به ساعت صفر برسیم حتما نظامیان ما اقدام خواهند کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/124051" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124050">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: ما هیچ تعهدی در موضوع هسته‌ای در مقابل طرف آمریکایی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124050" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124049">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ایالات متحده شهروندان و شرکت‌های خود را از استفاده از خدمات ایران برای تأمین امنیت عبور از تنگه هرمز منع کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124049" target="_blank">📅 23:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه قطر: دولت قطر استمرار تجاوزات اسرائیل علیه لبنان و گسترش نفوذ زمینی آن در جنوب این کشور را محکوم می‌کند.
🔴
ما از جامعه بین‌المللی می‌خواهیم که مقامات اشغالگر اسرائیل را ملزم به توقف تجاوزات خود علیه لبنان کند.
🔴
ما بر موضع ثابت دولت قطر در قبال لبنان، وحدت، حاکمیت و تمامیت ارضی آن، و حمایت کامل ما از تمامی تلاشهایی که ثبات و شکوفایی لبنان را تقویت میکند، تأکید می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124048" target="_blank">📅 23:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3wirrJXcU_Beql_MUcYepdVjWP7RxzjZhRFxEKEsU3LxNZ7KXJxMqed320lhFuTpC_tiRSmQAddY_HvbwGpgq8UiDUvZeOXIwNvHOGS6BPUMOVWFfjBW_EMSdZV4Bx649AXANxP4IaXbhbAodwH9IYhdOpRBD8dGInr9YEjPgdtb2dD6-70m5e42yr5d6Pg5xCGy993qlYWz012C5I5Qu-6leRIsykEXqfnc2KoZa20idt3pNDXtfwErv8HHeL7WZ1cROJmY9Jzwmenh047eEU3KvypgshKOYZgDE1clDWU4og50NZX-E5jMr91JmbjeeQ1Wlv4KjNHQokBlywbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن افرز: «ایالات متحده با این فرض که قدرت آتش برتر و قابلیت‌های تکنولوژیکی‌اش می‌تواند یک پیروزی سریع را رقم بزند (و از تکرار باتلاق‌های گذشته جلوگیری کند)»، در ایران «به بن‌بست رسید».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124047" target="_blank">📅 23:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcio1xduzhbPHgp3j8fixlUBowbsOAJ1x0uX_hE5eyhyLex_PDIWEaAfWrNhgl4ChAaaOHtL1HVWSxoHqBRUMgLv2tz-FWVD7Az3et11aD7WxzROoVEOM2b4C8nMff2pt7xITrW2RHpOoCiknFqmTT4B_vaKCTYynIdRdgscfOwrhwpwfjPDKo2SRRLAX173x9m0jDCGSs5fP6YcHPkG2lteSD7L9w3NTL9rRpxxufZn-aGI7Duiy8tb5QcFY6y1EnNoIvvLdiGaYc16q8lzzPkwzJCKK44KWu1NIMVwSwU16y0paxuhfJfi_RMkIj0BZGi6qQJzZeW9Y7pldmoeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124046" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_QmhmLMeyjq9e_Z9sDtcY-0FQeDKGvSQ6n_npJ5vyFKHkHX2QhRF1HuG8rY8q98S1U9IHozYsvXsSXDrO6tbYt8TtSg2Xvc340a328_PgYPc2-zNruq7-6EIYM3-yvPrXwLnJFHFiur_HB9iRbN86-VypCZGxMsmZSQGSwowwacf2QvbAFqmVfgFnz5Jf7FjAL6CPM1IzyDkv_PwRLGYpG5d5pzMWJrycea1bcqDy8YiiKTCwHv2pDnMdtEeGFxG8u53MOMpREz2gmKeGINgACOdhZxTrK2RqEwMf4DtVy_9g82QwdIXb_PIBGTTQl2jkAig2kBEfrzG1-uCp3iWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124045" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qot7dal1QR3k0LkwA99N7qr6-NSueiryWwDkt5ke0lgFyOUvq33TsxlA6O6tkdl3taF50dFBHjavI8RhRZcAXIkT_PN1DfBP-7STl1urepw6OvtMPmr-IPoxFv6dzvlwTSDrtIUhJeMBTroM2AJEcSyCdK4kXWh9PRHB8oQbDhq2nudOM57NYDDitRRGKKhg-DyC_IjvSUqax6--eZDzIuYEn8a3sg0m_vxO7R3etpTO0D7FbOk3I4WBAczQJUtyyDlueojbwR3-qWNTP904QvXsuK2OTzoAmEwuqfaE7pmiloHbVvmdXIMBdbLDVT8Sona7qYlpZo9j7EYxDyNZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل به عرب‌ سلیم در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124044" target="_blank">📅 23:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc40eaf31.mp4?token=EItsxmUcWBPdAO81WeLu-cjgs78tBsrCxlVEGQMPLX9AyuPYDbgGHI9QAIDSnD0rfynXM5u4OhlI1XYewwHqBwpetgiLIgPOPrgqkwy6R7umUd2SH3MAlW12ECu3bcPxs7DXTgUS6V_2P0h7VvuQ8JU9fSHg-Lb_79v-XpAN2TN5fL6R-feMwOi9gKoRjSrbgKEmovzLlm4lsLGf7ILiydTZw5hZOnaoKHMqPOn1pJhu3_4KOFSGqoATNXIlJsZAT_10SL2Ai2Vm0EBBSVwbAM9R017z5txeeKENlrAd-uQJJu1p0-ZROfkrIC6HX-NPBeU9Y0qEao6XkxBEBnDtqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc40eaf31.mp4?token=EItsxmUcWBPdAO81WeLu-cjgs78tBsrCxlVEGQMPLX9AyuPYDbgGHI9QAIDSnD0rfynXM5u4OhlI1XYewwHqBwpetgiLIgPOPrgqkwy6R7umUd2SH3MAlW12ECu3bcPxs7DXTgUS6V_2P0h7VvuQ8JU9fSHg-Lb_79v-XpAN2TN5fL6R-feMwOi9gKoRjSrbgKEmovzLlm4lsLGf7ILiydTZw5hZOnaoKHMqPOn1pJhu3_4KOFSGqoATNXIlJsZAT_10SL2Ai2Vm0EBBSVwbAM9R017z5txeeKENlrAd-uQJJu1p0-ZROfkrIC6HX-NPBeU9Y0qEao6XkxBEBnDtqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی اصابت پهپاد انتحاری حزب‌الله لبنان به خوابگاه نظامیان اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/124043" target="_blank">📅 22:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d568308de.mp4?token=WMJ8y-G-LdEKVH2NLGsJAbLaAGv-Rka3L6Gf3c1lx8y0J3CeOE5FVBZ7SMmexITtjIOi8Kzu1pKHfla7RcuH77s7Z3oKQOtQDwN4obkBtjYYa3E-zpId58yIhC5Ie7pReMClhU2n-V4lo0zeeNUClRVUWjGBlRCxUmx_dpQwFT1Hj88564jr1gG1sWh56-BrTcWJWRGBRKxhzuointGTQ7X45lS6yERJm1R_jDpTrvTSYx-uKP89nQMTnBT6Pymr8noMIJcijUYbbocu5QaFuZ2V5PSTjMLBlYePOvUjx4aI1Hy27xnxGsuFoNKxKAjP540DH1Ux1j9IiwSjcFLdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d568308de.mp4?token=WMJ8y-G-LdEKVH2NLGsJAbLaAGv-Rka3L6Gf3c1lx8y0J3CeOE5FVBZ7SMmexITtjIOi8Kzu1pKHfla7RcuH77s7Z3oKQOtQDwN4obkBtjYYa3E-zpId58yIhC5Ie7pReMClhU2n-V4lo0zeeNUClRVUWjGBlRCxUmx_dpQwFT1Hj88564jr1gG1sWh56-BrTcWJWRGBRKxhzuointGTQ7X45lS6yERJm1R_jDpTrvTSYx-uKP89nQMTnBT6Pymr8noMIJcijUYbbocu5QaFuZ2V5PSTjMLBlYePOvUjx4aI1Hy27xnxGsuFoNKxKAjP540DH1Ux1j9IiwSjcFLdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر : من نماینده از جانب تمام اسرائیل هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124042" target="_blank">📅 22:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع آگاه: ایران اصلاحیه‌های جدید درباره متن تفاهم احتمالی اعمال خواهد کرد
🔴
تبادل متن‌ها ادامه دارد و ایران نیز قاعدتاً اصلاحیه‌های خود را درباره متن اعمال خواهد کرد و هنوز هیچ چیز نهایی نیست.
🔴
ملاک برای ایران متنی است که خودمان قبول داشته باشیم و اعمال اصلاحیه از ناحیه ترامپ به معنای پذیرش آنها توسط ایران نیست.
🔴
ایران برای وضعیت عدم تفاهم نیز کاملاً آمادگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124041" target="_blank">📅 22:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بانک مرکزی: رقم وام ازدواج مشابه سال ۱۴۰۴ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124040" target="_blank">📅 22:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ade6a1991.mp4?token=GF2bCRRt_AGEleAkCAroaxikj1aQDac00hccXqjDHWe_5w0jc9MIzIrWB-4Jpvn7YaFj6iZQLSDP1mOhYyDbQBNHFDwKbaNpoFOoswsoqk_mEgCoswd0vq6ZNGZbEkfmqOc3QlsvYxrBSPK9tozORMwGJwVkgvxKlkB5HIqI3Z6qj5Vj9LvWv5z2AFNO67QW1jbDNOkBA6Uu_QEdJYNOFkQBuvoURshWXZ-eZFqlLu-VywE1YOnAbT_cW9CLP0P2WOzgy285BiPsp14rmagYCMea-rjw6sEbTq0GxMPXuKJsAQwp6ydyR7KG5frFvSc1bK8WTEsJY97Q-SvFOSqsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ade6a1991.mp4?token=GF2bCRRt_AGEleAkCAroaxikj1aQDac00hccXqjDHWe_5w0jc9MIzIrWB-4Jpvn7YaFj6iZQLSDP1mOhYyDbQBNHFDwKbaNpoFOoswsoqk_mEgCoswd0vq6ZNGZbEkfmqOc3QlsvYxrBSPK9tozORMwGJwVkgvxKlkB5HIqI3Z6qj5Vj9LvWv5z2AFNO67QW1jbDNOkBA6Uu_QEdJYNOFkQBuvoURshWXZ-eZFqlLu-VywE1YOnAbT_cW9CLP0P2WOzgy285BiPsp14rmagYCMea-rjw6sEbTq0GxMPXuKJsAQwp6ydyR7KG5frFvSc1bK8WTEsJY97Q-SvFOSqsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:  نصرالله دیگر در میان ما نیست، و این تصادفی نیست. و هزاران عضو حزب‌الله دیگر در میان ما نیستند، و این تصادفی نیست.
🔴
و با این حال، این کافی نیست. ما پیروزی را به دست نیاورده‌ایم.
🔴
ما باید ادامه دهیم، و ادامه دهیم، و ادامه دهیم. ما نباید متوقف شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124039" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه با ترامپ تماس تلفنی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124038" target="_blank">📅 22:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حمله به کشتی حامل مس در تنگه هرمز
🔴
در پی درگیری‌های اخیر در تنگه هرمز، یک کشتی خارجی که حامل مس بود، مورد هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124037" target="_blank">📅 22:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام و توییتر (X) فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124036" target="_blank">📅 22:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=SmXtEw-LldJSyCyCVnPLRfgMXQmWZEbUEccF3_yYhmb3WwdYm7KSEEkcUyH6lpBoY2FNarZDSx2n6Bf9lNoSqav3OseO-HlKh17v03QvYiIS6swKQyfsd8y0KUPmVQxjG2vgw4cG5Oy-n6WBxRxzDLIqi9RWy_NJNT_yfkezj9pyQIgzmd2NapwZQinay6hlV0jhw-jRObCajTysHN88Nznsh6HOmF4vEV8s3bcWaHRCDukaCB5sCfb_orFslQF3OaQzi0pNIKY5bRwwc_9clt3xen0jTAVS4BS0UWXaQot4MWdJDt7c8iv2OfRlUhLEBFtoEUTSUbHXACl8VvG3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=SmXtEw-LldJSyCyCVnPLRfgMXQmWZEbUEccF3_yYhmb3WwdYm7KSEEkcUyH6lpBoY2FNarZDSx2n6Bf9lNoSqav3OseO-HlKh17v03QvYiIS6swKQyfsd8y0KUPmVQxjG2vgw4cG5Oy-n6WBxRxzDLIqi9RWy_NJNT_yfkezj9pyQIgzmd2NapwZQinay6hlV0jhw-jRObCajTysHN88Nznsh6HOmF4vEV8s3bcWaHRCDukaCB5sCfb_orFslQF3OaQzi0pNIKY5bRwwc_9clt3xen0jTAVS4BS0UWXaQot4MWdJDt7c8iv2OfRlUhLEBFtoEUTSUbHXACl8VvG3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد‌جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
🔴
من اصلأ هیچکاره ‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124035" target="_blank">📅 22:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124033" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYKEvbcjnQ4PqxXoOAWn-05BJ2n4UGdAxeL_Bia6BrXR_fcJNbLbvRKo-z_G7m77wads0Ip22jYWrtzWgQYR1WBB6dgW_YmGJloJ3kfnKTW-x9TKA04wMn2bqfklOoSRBTPBrG41RCrC_0SJtM-ckb5gil3eoe9tFh0qw1l6JG5XQpWFeS7T4CI0BF3A13jEfB0A5KZV_Lv4IktQ__2SDhKerwKOT720ib5b_UEGexCI8f8BMEj1BAn-kc8YIep38dvpV3d0GmIkcxrY2iLMhooxx2dLqurU3rzKDOR1JGvpfiFOk-c_385upe_Cr3S7po9m2jM02IjuFl39RVEprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124032" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر نیرو: شاهد کاهش ۱۰ تا ۱۵ درصدی مصرف آب توسط مردم‌ هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/124031" target="_blank">📅 22:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124030">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDn7BvXZmY_00QW4uM9J9AYXmWLbDgiznJ-zO8nTtAETaUU4FN5K75ic1I4_Nea-BwNoVGbPxD3irR3v8cXNDMbBQvwZwmRJ3-MkQ3wM0I-eGyf38UGKNYMBrcdvwa_qc4YPXjt7VRVxlhCZai37fGARcZkSt37ADUNg9CHVpY9e0bqNFZKFMLccxiyE0qHXezooa2MD9-2Ng6uWcBfVkLFeDtQ5uCptsd5903HGneumvC0toqXBmQv5VOH2rGCzvTBTPZGI1WI6572KvjsnM28bHwpkn-tPUyUSJbW1Z432YcBn_X38HPoZUyQ0HMW_r6YzVqvAjfRM-R5AIQZz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دادستانی بحرین، روز یکشنبه دهم خرداد ماه، اعلام کرد در چارچوب تحقیقات مربوط به آنچه «تشکیلات مرتبط با سپاه پاسداران ایران» خوانده شده، اموال و دارایی‌های اعضای این گروه توقیف و حساب‌های بانکی آنها مسدود شده است.
🔴
به گزارش رسانه‌های بحرینی، رئیس دادسرای جرایم تروریستی این کشور گفت تحقیقات نشان داده اعضای این تشکیلات به جمع‌آوری منابع مالی و انتقال بخشی از آن به خارج از بحرین اقدام کرده‌اند.
🔴
دادستانی بحرین افزود، در جریان بازرسی‌ها، اسناد و مدارکی مرتبط با فعالیت‌های مالی این گروه کشف شده و بر همین اساس دستور توقیف اموال و مسدودسازی حساب‌های بانکی افراد تحت تعقیب صادر شده است.
🔴
مقام‌های بحرینی همچنین اعلام کردند تحقیقات درباره این پرونده همچنان ادامه دارد و اقدامات قانونی علیه متهمان در دست پیگیری است.
🔴
بحرین پیش‌تر از بازداشت ده‌ها نفر در ارتباط با تشکیلاتی مرتبط با سپاه پاسداران ایران خبر داده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124030" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124029">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
زلنسکی: فکر می‌کنم امشب یا فردا شب از طرف روسیه یک حمله بزرگ با استفاده از پهپادها، موشکهای کروز و موشکهای بالستیک خواهیم داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/124029" target="_blank">📅 22:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124028">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnuCpEbZ-AVBNkuiBlQkOBAZv6RJbtLijUlyLxnKj_X9qNyxQWrZT-7TnUCOY-sLMn5z6yGTRIzMqOlSGvEWujaTb3GNdc1y_j1NCETwjwoMmE4WZgxCStZDdowz57ZSUlgfWLsiopIqvOd4OFx-SUcTnXM964KEF6hmUIM3Cy6W_MwvJ1WCDk_5QQFcYjJJlS-G2mCUsRbXNQ8LwwSAdgtx6xRBfw1zY2ecuqfcyPF19rE6PAwXD1uKiLm97TBrpwBhatkVo9KEsuyo6lUJmKltQje7jyiPjETNZlgxMJbU4VaYHXE4jC39TBx-BwknHptiFy8jBGTXVDLA1_m-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: دست ما روی ماشه قرار دارد و شگفتانه‌های جدیدی نیز در راه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124028" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124027">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💔
روز ۱۸ دی بهرام زاهدی ۴۲ ساله و مجتبی قربانی ۳۳ ساله بر سر کوچه‌ای در دروازه لاکان رشت ایستاده بودند و تنها تماشا می‌کردند که ناگهان هدف رگبار حرام زاده های عرزشی قرار گرفتند.
🤔
شما حرام زاده های عرزشی تروریست هایی هستید که این جنایت رو انجام دادید و از شما…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124027" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124026">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
به گزارش کانال ۱۲ اسرائیل، اسرائیل درخواست‌های رسمی خود را برای تأیید گسترش عملیات نظامی به بیروت، از جمله حملات هوایی احتمالی، به ایالات متحده ارائه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124026" target="_blank">📅 22:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
به گفته منابع محلی، حداقل دو جت جنگنده نیروی هوایی ایران در حال انجام تمرینات آموزشی معمول بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124025" target="_blank">📅 22:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124024">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پزشکیان در جلسه امروز دولت: یا با قدرت ادامه می‌دهم یا شهید می‌شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124024" target="_blank">📅 21:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124023">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
چین از یک الگوریتم جدید هوش مصنوعی برای هدایت دسته‌های پهپادی رونمایی کرده که ادعا می‌شود حتی در شرایط اخلال شدید الکترونیکی، قطع ارتباطات و محدود شدن دید نیز قادر به شناسایی و انهدام اهداف است
🔴
بر اساس ادعای پژوهشگران، این فناوری در شبیه‌سازی‌ها به «نرخ موفقیت ۱۰۰ درصدی» در انهدام اهداف دست یافته است؛ هرچند کارشناسان تأکید دارند عملکرد در میدان نبرد واقعی به دلیل عواملی مانند آب‌وهوا، فریب، آسیب‌دیدگی حسگرها و جنگ الکترونیک می‌تواند متفاوت باشد.
🔴
هدف اصلی این سامانه حفظ توان عملیاتی دسته‌های پهپادی در محیط‌های فاقد GPS و تحت اخلال شدید ارتباطی است؛ شرایطی که در جنگ‌های اخیر به‌ویژه در اوکراین به یکی از چالش‌های اصلی پهپادها تبدیل شده است.
🔴
این فناوری بخشی از رقابت فزاینده میان چین، آمریکا، روسیه و کشورهای عضو ناتو برای توسعه سامانه‌های رزمی خودمختار و دسته‌های پهپادی مبتنی بر هوش مصنوعی به شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/124023" target="_blank">📅 21:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124019">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/99a9772ea2.mp4?token=kMzFo1q_kw8iG-VgKiV2wFacuDZ3YghOclEBJ90DgzKiBKcHQCh1m-P5G6XybsKJW5sPlvWcVRkoPtfMONCm96-sdeTYkm9JDxo6SZXC7jXX1fcCPuYBdX-VkleQQ8iBUpXEVMyn1M-cdNi6Bwfv6M3KV711RAzksyHEwISOlAuvmDxAhzLN2AWNhNnTbLzIVmoye8w_HJHrjBiS8v_sR1eVvKT7Lg7GmcJyKkWp3EYCh8rvTcC164fK9SQ4R0TSP62s9tvy3vneTfo00x5YTL0okYu94URPSP1H_65xIFFTVU9DoPiJOJUPXrLtjVF5pUFzsLdZ80_C1GaZO0SbFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/99a9772ea2.mp4?token=kMzFo1q_kw8iG-VgKiV2wFacuDZ3YghOclEBJ90DgzKiBKcHQCh1m-P5G6XybsKJW5sPlvWcVRkoPtfMONCm96-sdeTYkm9JDxo6SZXC7jXX1fcCPuYBdX-VkleQQ8iBUpXEVMyn1M-cdNi6Bwfv6M3KV711RAzksyHEwISOlAuvmDxAhzLN2AWNhNnTbLzIVmoye8w_HJHrjBiS8v_sR1eVvKT7Lg7GmcJyKkWp3EYCh8rvTcC164fK9SQ4R0TSP62s9tvy3vneTfo00x5YTL0okYu94URPSP1H_65xIFFTVU9DoPiJOJUPXrLtjVF5pUFzsLdZ80_C1GaZO0SbFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جت جنگنده ناشناس نیروی هوایی بر فراز کرج، استان البرز، شمال ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124019" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124018">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دود مشاهده شده در اتوبان ستاری مربوط به حریق در انبار کالا بود
🔴
سخنگوی سازمان آتش نشانی: حریق مربوط به یک ساختمان دو طبقه بوده که در طبقه همکف آن پارکینگ را به انباری کالا تبدیل کرده بودند و دچار حریق شده بود.
🔴
این حادثه مصدومیت و تلفات جانی نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124018" target="_blank">📅 21:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124017">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش ها از پرواز جت های جنگی ارتش بر فراز آسمان تهران و کرج.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124017" target="_blank">📅 21:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124016">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
عراقچی: ویزای تیم ملی فوتبال ظرف یک تا دو روز آینده صادر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124016" target="_blank">📅 21:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124015">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو، در مورد گسترش حمله لبنان امشب تشکلیل جلسه میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/124015" target="_blank">📅 21:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124014">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d8007820.mp4?token=BLL28qWZFZ1PMs6sH-JKm4QGCZh4GCh2QcBebvwks3Rc1vtiArf4_U8ObNoUgsNkZwz9b92rGlB0rQyVYdLRRqh-C6Bkab2tTAVr9We0f0YRC3QEFFApdYP6yTBAQBdU3s8ID04MG_tZLaEYhcr5UQxX9itFZZ9AJv3OGsr_BQXh-VTKM1ZnXmc2gi1bnLC7aqsHUXjj935i-ww9YXPKE6quSBeZVf_tpGYyu0vMJM7OWhS7p3hRoqpPyYbCxYVCmjd_j_5N3KrbFr90TpiXzf9X3IbfHbnG8thpqWKXNphKRQ_mgIDjHJNA848D6lyQTBYd21GptbFdjcLzuHEsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d8007820.mp4?token=BLL28qWZFZ1PMs6sH-JKm4QGCZh4GCh2QcBebvwks3Rc1vtiArf4_U8ObNoUgsNkZwz9b92rGlB0rQyVYdLRRqh-C6Bkab2tTAVr9We0f0YRC3QEFFApdYP6yTBAQBdU3s8ID04MG_tZLaEYhcr5UQxX9itFZZ9AJv3OGsr_BQXh-VTKM1ZnXmc2gi1bnLC7aqsHUXjj935i-ww9YXPKE6quSBeZVf_tpGYyu0vMJM7OWhS7p3hRoqpPyYbCxYVCmjd_j_5N3KrbFr90TpiXzf9X3IbfHbnG8thpqWKXNphKRQ_mgIDjHJNA848D6lyQTBYd21GptbFdjcLzuHEsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: پیش‌بینیتون از نتایج تیم ملی تو جام جهانی چیه
🔴
پزشکیان: مهم نیس تلاششونو بکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/124014" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124013">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۵  عبری: گسترش عملیات اسرائیل در لبنان با هماهنگی دولت آمریکا انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124013" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124012">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50386848ef.mp4?token=OdhBO3PcRx5brXTEHcovCIxFQdBEAgUpxYzSHC1zxQ7NFlNhpbQVRdXdudrT5h70Hi6P5PtX6MPfqtFkqxg48j5nRY7LJCgU-T35rDePE3jIBNco_uUwaO7zBDNYWBTZKiz01u3UBNgT_xSZH_lxGNyLO-GZARBREVp1QrR0lJDLkJTrdcdmVoZMcx6ALF8KYRwiQcY-fFgKJx_0mdKaUMuX7RAycDVbrQg_Ej6VQlG8xx5cJKGNP7OaOcve-rRRlNh8ZMDMQsnSEZS3J2w5RQL16Fnr_arAz8EiFE1-LiLcVRz9imUqi1DDAI7lr2lN9G_zCjOJDFK7NyJGDCcfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50386848ef.mp4?token=OdhBO3PcRx5brXTEHcovCIxFQdBEAgUpxYzSHC1zxQ7NFlNhpbQVRdXdudrT5h70Hi6P5PtX6MPfqtFkqxg48j5nRY7LJCgU-T35rDePE3jIBNco_uUwaO7zBDNYWBTZKiz01u3UBNgT_xSZH_lxGNyLO-GZARBREVp1QrR0lJDLkJTrdcdmVoZMcx6ALF8KYRwiQcY-fFgKJx_0mdKaUMuX7RAycDVbrQg_Ej6VQlG8xx5cJKGNP7OaOcve-rRRlNh8ZMDMQsnSEZS3J2w5RQL16Fnr_arAz8EiFE1-LiLcVRz9imUqi1DDAI7lr2lN9G_zCjOJDFK7NyJGDCcfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
روز ۱۸ دی بهرام زاهدی ۴۲ ساله و مجتبی قربانی ۳۳ ساله بر سر کوچه‌ای در دروازه لاکان رشت ایستاده بودند و تنها تماشا می‌کردند که ناگهان هدف رگبار حرام زاده های عرزشی قرار گرفتند.
🤔
شما حرام زاده های عرزشی تروریست هایی هستید که این جنایت رو انجام دادید و از شما حرام زاده تر کسانی هستند که این اتفاقات را می‌بیند و همچنان از شما قاتلان حمایت می‌کند.
🔴
اگر آخرتی باشد قطعا شما در قعر جهنم هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/124012" target="_blank">📅 21:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124011">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عباس عراقچی: مذاکرات و تبادل پیام‌ها در جریان است، اما به نتیجه مشخصی نرسیده‌اند.
🔴
وی گزارش‌های فعلی را حدس و گمان دانست و گفت تا زمانی که قطعیت حاصل نشود، نباید به آن‌ها وزن داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/124011" target="_blank">📅 21:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124010">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سنتکام: از زمان آغاز محاصره دریایی ایران، ۱۱۸ کشتی تجاری را منحرف و ۵ کشتی را هم از کار انداخته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/124010" target="_blank">📅 21:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124009">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGbE8iLQfHRuLysOJSNV443vKtJsHIP126nYaH8bjc9ZbtsKOqkY2fYn7KJOPzgpFe-YgmXbN-mAx253R_tRVEeoa5koReCXAVM1mk9Nbc2ajZYMV99rAp7y5zTr8yJ8xGLlnf70PXHfn4ooB5VBEHzChDZivvdWkcNJH2EzNfSYrXOz2KRr4B1YSCosHCaJBe7suqXdM02FbRkzA_6wJMpWh7ELw75L7CKhNGyg0eksVivSoODN4CdKXMBrkOoH8qQZChNuQyXOkEXyhBsG-2ruQUPtEWkCgiIyyBeP_T-R4V2BR2MBFjRB9uw6_-AKbXTI349Tyi5CVWOogrZjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس‌جمهور: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/124009" target="_blank">📅 21:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124008">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ایران اینترنشنال: پزشکیان به خاطر تسلط کامل سپاه بر اداره کشور درخواست استعفا از سمت خودش رو داده.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/124008" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124007">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سنتکام: 118 کشتی تجاری رو برگردوندیم و 5تا رو هم توقیف کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124007" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124006">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgqcrRU_36AFp3R_NvmSeXiC_aT7Sxg72NSNWUeJho5rGmHS30qh-OBr69BKYNGxoTwJVywGNAaOf4NOjNf-zlIVhZMVBl5r366Chf_o6SdTrq0jnTCZqlr3JuYG4NzLSLNTyOR2HxZ6mlvdDsubP1Sp7yUfE3aK-RbDg4ffQWBnXso7TX7QNUAb4aoyEksHNXwVtUdKc97vNaiD3HePCCp49SpUoimkNP8thW8MRfgqHkd0nCNEdz0hvh5spXBiRZZkUgTaQbYqLOZmFA37xMFicZO_soFT5gUlrl3pGmYgsHsAeP2GNlKYitSRUbSLp9V3f6jF98xE9KrPgQHdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران اینترنشنال: پزشکیان به خاطر تسلط کامل سپاه بر اداره کشور درخواست استعفا از سمت خودش رو داده.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124006" target="_blank">📅 20:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124005">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNSi8G0sISZ1zhX5qFoN2QXB8CeZ6A1Afp3GjXCGkvthggYZqH0PQPnlQ5nAHuJF3rmbRUke-r9yhdLTzsg1pxmFhWmEjRaFg3tEx2-djQWGcE0aqAhNH1LDqWudPFB5eVOhja8dZMoGbjSHfzrhMyl4oWVdk5GNbB1LnRf3ypl1okzgQSuJaaOmGNbrwlgQeQT0xK0ZeFy6F73yWkJbIyyooOy_GY7jIrNPJts6nMNsg1692YDzCLH4mBKbHgxk7CWxMAM_I0LB56SoUFlomLEcNC1CFNZQqlL7hmZ_y6117GEAZ2OOwlSYjD8165wPk3LNgMhYv3MwVyhqjWzRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران اینترنشنال: پزشکیان به خاطر تسلط کامل سپاه بر اداره کشور درخواست استعفا از سمت خودش رو داده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/124005" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124004">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haCHkkNWpgzoq87RIjTz9GdOea8C6tkjhyVx3LXK4IqwRZGzM4HdUo3WYWFpYpDpPqOlzoATnw5NaKo2FKCOC2300qq62sRWL20kuhr-NLWhuTIwoxrUORakQUDDmHQRxuQAgpeV1WLwsIJJdCZXHWccg9oQstGmSnZyCptEm4SRPxpT83dRfbPFRYi_Ls5qzZw0TTXF7fnlDPqImT6-kLBkD-HLKNpBgwcQ69jtlSCIcDmdLmwzokam4TApWQ2piYEB368sWogNS8OD5bR19a-MYCIU2xeB9nB-c37bv4bfpYTCjus_ym_2KVQRvI0L7sfFxkFQNMrPMSvBh7XUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست:
منابع به واشنگتن پست مدعی شدند که مجتبی خامنه‌ای، رهبر ایران، هنوز به آخرین پیشنهادات ایالات متحده، از جمله تفاهم‌ نامه‌ای که در جریان مذاکرات اخیر مورد توافق قرار گرفت، پاسخی نداده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124004" target="_blank">📅 20:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124002">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7QZEeHoYXzjJOPiOJwK-C_JC70zxWIM893y3_x1ZMNG8NU0Qcu8KBQjvZ11Ht9DFDHLiSRyE1L7vEkSQriGCB-e1RsGsLJIUqv3wakpfWv5AKK-77wRblc_fW7IVDuctDP65cpPjftC_FYPPi4eLSLCNZgLX03tbHjUMehJpzXYsH3qmXZvo1ylwUjPxKUe-u-z-uX9OTdtkn9f_Y2ovK1d_1q-YM_AQPk2nzwCSXpEg7b7CFs5iq-OVB6BnAvQw-Gyuiw7lcy5Uclt2Zl7zAJcYbM7t5InIuD6Ad3TMwpBQ0s3WPLPs3P2nqAsnWy_v-6h1xqSN8ibeuFfiMfUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ پست نیوت گینگریچ را دوباره منتشر کرد که در آن می گوید ترامپ "در آستانه پیروزی تاریخی" در ایران است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124002" target="_blank">📅 20:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124001">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: فشارها بر ایران و جلوگیری از صادرات نفت از جزیره خارک ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124001" target="_blank">📅 20:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل دستور حملات گسترده در سراسر لبنان را در 24 ساعت آینده صادر کرده است،مردم دو شهر بزرگ نبطیه و صور در جنوب لبنان در حال تخلیه فوری می‌باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124000" target="_blank">📅 20:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbf3f64be.mp4?token=KGnbkMi23ioUrCIQ5RLaBHODP-O__BwNbEwuOTIL8nvlvslgC_GFslwVptmZ9x1ehH2lwBA7h8bs19gePlJf-a6STNjsemwJ2pziUGVorryzGqUgLIDaahkowAZrDLJz_okSdLD4R5HK9tlgDmltmghBD6_EnR5SeQCmxZya44et61xej86250THVt33JRp2agXwiLVUtdZMrM-gPSSgvd-fvJ2KJFg4dGsww6a1IRlCIQXwck1nctRhv6SYZ-dI1l1wt5ioIN4UFuZm__A1LcJfEl9eHFpA0HgOHAQ7rUot_6mc4ByLwiRxbl-KU0GJlWj5aGGA6Ua7XmljOxSj5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbf3f64be.mp4?token=KGnbkMi23ioUrCIQ5RLaBHODP-O__BwNbEwuOTIL8nvlvslgC_GFslwVptmZ9x1ehH2lwBA7h8bs19gePlJf-a6STNjsemwJ2pziUGVorryzGqUgLIDaahkowAZrDLJz_okSdLD4R5HK9tlgDmltmghBD6_EnR5SeQCmxZya44et61xej86250THVt33JRp2agXwiLVUtdZMrM-gPSSgvd-fvJ2KJFg4dGsww6a1IRlCIQXwck1nctRhv6SYZ-dI1l1wt5ioIN4UFuZm__A1LcJfEl9eHFpA0HgOHAQ7rUot_6mc4ByLwiRxbl-KU0GJlWj5aGGA6Ua7XmljOxSj5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بندر غزه هدف حمله هوایی قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/123998" target="_blank">📅 19:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر دفاع چین:
اگرحاکمیت چین بر تایوان نقض شود پایگاه های نظامی ایالات متحده در ژاپن و کره جنوبی به اهداف مشروع  تبدیل خواهد شد
🔴
پکن هیچ مداخله خارجی را نخواهد پذیرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123997" target="_blank">📅 19:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvkFt2W1uTzbVRFwQ2NFcXWjuIsRJYOWFWYNUh_LLQ4SmUnKhCE9HES864mC29G2G9Ir0QaB5fIZwFUuSCST0tokRiJofmkGffhzcl9LqG2sGK_xHnqTPsfI4tSUw18iOadWrNIb-OqlzWhWzx6Z30SuYVjFuI7LNmj24j-N2CIYk9l74XfkxQbfYIJdsjp8oE8WpQWvvp9rjKCSfQAY-vgw1UVOFPUQkdm7Poqzk168UR7oOqV-0xqyqD3lNWE5tIb2CQVdqsD67_JimEMoyp76eqzeUrYPiEoNCZn-Nq1z9UHAE6iqmMuTNkFiAU_MX2_IuLr1ldjtE_OzOTZCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی ایرانی به نام «IRGC TOLL COLLECT» در تنگه هرمز ظاهر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123996" target="_blank">📅 19:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
منبع آمریکایی به سی بی اس :
فعلاً برای رسیدن به توافق با ایران هیچ ضرب‌الاجل و زمان مشخصی تعیین نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123995" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU8qk_t8xBptDOZcXjCRecDU4K3KmCYNvlR8K2BmQFvJjh-ZEipKQh-yXrY37x6CGqai2U7EEXLdJgdu4nJ7-4Las2kKaFas0KN1-sh_NrrgBhNty5U0HNtvCwctP0QXKQZAgsafwB7kiyAiMBFZmXYs1MAHsud1ISJ7OTH2Xg1FAQhSXrec9yfBwsPruA6yaTjmyaJFIEu_dXMJSbANLk-3fCvtnUaUwX_GwqEzRD_c5L3txa87PB5PL55fe3n05ho-CGUY9xDUfML5ex8Bvhi8bAFibMGoxkmNahuLCkVB-nr_o4OCTK2gII5NNh3GBviiFx1MyP1ANX8VIimCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این تصویر که میبینید اولین جلسه مجلس شورای اسلامیه که فقط با حضور ۱۴ نماینده برگزار شده.
۱۸۷ نماینده به صورت آنلاین شرکت کردن و ۹۳ نماینده دیگه حتی به صورت آنلاین هم حاضر نشدن.
🔴
طرف نماینده شهرشه ولی حتی حوصله نداشته آنلاین شه بعد انتظار دارن دانش آموزا و دانشجوها هر روز به صورت مجازی تو کلاسا شرکت کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/123994" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/123993" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6zgeMLaZGLvS5deinV3Ybyw7HzCbdJ3oxWxHiy5LwpdeGddvKO94zwAxtqeEQC5vIRzp0hLK0x387l45yadG1Q-8em-fhTq7vTZzOb4he6FspCjNXtpWBUS4FxNef2JVsyOvGF2Yes2ysJsQHnH9-ULfFmYazhmAPkZhW6jt2MvVXo0cSsmOBn-Mr5PYzA8w-uK2vGfJSzilOj-EEiKDYVUsGNH46MocS0hAC6X3yI_IcVCqc093BVYAi492q3v5BcwnwPM51Gc6D6T73xkKbA3AdCH0bQMwbYnH5Dx_ICGP-9D9K0QKcyDRivjLe5h5wtoCYUkOvMDmaG_5R9TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/123992" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال 12 اسرائیل: حزب الله از صبح امروز بیش از 20 راکت به سمت شمال اسرائیل شلیک کرده است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123991" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انفجار مهیب در میانمار، دستکم ۵۵ کشته
🔴
در انفجار مهیب در انبار مواد منفجره در نامکام در میانمار، دستکم ۵۵ نفر کشته و بیش از ۶۰ نفر زخمی شدند.
🔴
از سرنوشت چندی نفر دیگر خبری در دست نیست .
🔴
در جریان این انفجار ۱۰۰ خانه آسیب دیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123990" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123989">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123989" target="_blank">📅 18:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=HVi0TucKzfUMTqn3Vur4CpXPvopzsSed0z-lNGf95w2lMEzaZU4_RiJM93pd55o_x5K38S9WABwct7En5FxHxkX3OO_F8U4Kg8hAWUEdNvfZtalylfSqChGgsEsyiFGgzpIOGwQyFmM-MQ73pdtOCZfosN6s3s2EV4-uwKODLxw0x4-wCHGs-rjNTUS5lgFRSh-pe4SYOuiL3uM7QyziU8EJigb_WmVJ9JxRN7KfIIpe8dbadbG6aK3VL1olfHksB2Q-JN9T2yg9PYB6KuOrUw30vpGbe0cSUpwTMsfA5a4XY387t9Go8WcAUt4sh-GATLESldLnrs4aE_zcxgFujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=HVi0TucKzfUMTqn3Vur4CpXPvopzsSed0z-lNGf95w2lMEzaZU4_RiJM93pd55o_x5K38S9WABwct7En5FxHxkX3OO_F8U4Kg8hAWUEdNvfZtalylfSqChGgsEsyiFGgzpIOGwQyFmM-MQ73pdtOCZfosN6s3s2EV4-uwKODLxw0x4-wCHGs-rjNTUS5lgFRSh-pe4SYOuiL3uM7QyziU8EJigb_WmVJ9JxRN7KfIIpe8dbadbG6aK3VL1olfHksB2Q-JN9T2yg9PYB6KuOrUw30vpGbe0cSUpwTMsfA5a4XY387t9Go8WcAUt4sh-GATLESldLnrs4aE_zcxgFujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت یک پهپاد حزب الله در داخل پایگاه نظامی ارتش اسرائیل در نزدیکی بیت هیل چندی پیش‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123988" target="_blank">📅 18:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123987">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حمله مجدد اوکراین به نیروگاه هسته‌ای زاپروژیا در روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123987" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123986">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e2d4b641.mp4?token=Px6Rtvmt2rxGeme07N4yB3yNoyBsnGNo84ftIxh2Xbuquc8GkYvB4po8LOCoXGhkxY2oHbxaE5gu28H6sngdko780eZk9VrlCPf-B--yCdg9n5sbXvucfFsa2L3cSBCKJg8M85qUZJ_JiulF_CbuNszr90UY8b6KknNgnBQaKtUVR6jstoKi6QBkdmTi6hYZv_lT_HMugKULT2Az8U4_yRwqAqzgShaEuTgYchOIlgC75zSp90gm_qhwRTjMzjU56_Le1H27Xk2js72BB2lQm5u28Fak7qE00B6-9xMJ_SN00LhcYhXI104cuU35oz1cV-dl9q3mIPAal9sUbgeXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e2d4b641.mp4?token=Px6Rtvmt2rxGeme07N4yB3yNoyBsnGNo84ftIxh2Xbuquc8GkYvB4po8LOCoXGhkxY2oHbxaE5gu28H6sngdko780eZk9VrlCPf-B--yCdg9n5sbXvucfFsa2L3cSBCKJg8M85qUZJ_JiulF_CbuNszr90UY8b6KknNgnBQaKtUVR6jstoKi6QBkdmTi6hYZv_lT_HMugKULT2Az8U4_yRwqAqzgShaEuTgYchOIlgC75zSp90gm_qhwRTjMzjU56_Le1H27Xk2js72BB2lQm5u28Fak7qE00B6-9xMJ_SN00LhcYhXI104cuU35oz1cV-dl9q3mIPAal9sUbgeXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی: از من به یادگار داشته باشید که در ژانویه، مجلس نمایندگان به دلیل جنگ ایران، ترامپ را استیضاح خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123986" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123985">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8b0f815b.mp4?token=h-68XiZGBuD79ApdVsKrseF7VJUFd95wyD5dRa9RoiyaoKxWR9pASJ2pCHlh81BjPJUSNgE7X41CtqZg_qIGPIgJ3_TfzGoLiDvnb3GW2uTSJOtmJ-MBO0W_L_iCmhx07aN948kNDB_v3jYQboJI2gzSkOXqQEy4WiE2k4EdCcFGurn6cI3gCjhF-BV_HNofy9gNhhmIz4DW-iB00pI4TSWAn3awu_zHsCG8EDO43ocKtROSon_Quj7NxBZGIoaL8Nb8UYEd6CzOIFor1GZOEmO-G2siS8fYmC-t0sYRuapEFkSfIbFzLJo6j20TlMakSltxuFsEWcmmzmtGxY1E5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8b0f815b.mp4?token=h-68XiZGBuD79ApdVsKrseF7VJUFd95wyD5dRa9RoiyaoKxWR9pASJ2pCHlh81BjPJUSNgE7X41CtqZg_qIGPIgJ3_TfzGoLiDvnb3GW2uTSJOtmJ-MBO0W_L_iCmhx07aN948kNDB_v3jYQboJI2gzSkOXqQEy4WiE2k4EdCcFGurn6cI3gCjhF-BV_HNofy9gNhhmIz4DW-iB00pI4TSWAn3awu_zHsCG8EDO43ocKtROSon_Quj7NxBZGIoaL8Nb8UYEd6CzOIFor1GZOEmO-G2siS8fYmC-t0sYRuapEFkSfIbFzLJo6j20TlMakSltxuFsEWcmmzmtGxY1E5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام زهره خاکسار ، دخترش که بر مزار مادرش میرقصد
🤔
برای ما مردم دیگر فقط مسئلهٔ اقتصاد و سیاست نیست؛ یک حساب تسویه نشدهٔ عمیق با حرام زاده های عرزشی است که تا ابد در ذهنمان مانده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123985" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123984">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرگزاری CBS: تغییراتی که ترامپ در متن تفاهم نامه داده جزئی نیست و قابل توجه است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123984" target="_blank">📅 18:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123983">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به شهرهای کفرسیر و شوکین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123983" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123982">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گروسی: حملات به تأسیسات هسته‌ای غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123982" target="_blank">📅 18:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123981">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سی ان ان: ایران ۷۰ درصد سایت‌های موشکی خود که بمباران شده بود را باز کرد
🔴
ترامپ نگرانی خود را از میزان سود مالی که ممکن است ایران در چارچوب توافق به دست آورد، ابراز کرد
🔴
ترامپ بر عبارت‌های سختگیرانه‌تری در مورد تعهدات هسته‌ای ایران و وعده‌هایش برای بازگشایی تنگه هرمز اصرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123981" target="_blank">📅 18:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123980">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB6R4pvqxEtwQNEp8yh5TjFd22debPqug1vidrkNAJ7SK2kf9u6Ma0oudLw54fFidiRJAefPOKN6OLKZNClfgGzrPks0qGvkKkr_M6qhQcoIy53za89THDfoYdFXkVCHQpIt2ko5EHnSNXvpsx0C4RnCKvM0dR9RTsYP6jZl8ZnulSqRPXK25CX5SwF-gwsSwPLcl4ijlJlh_Vv32dpkb_4KqExOlfEtyI4ilxB4eJ3rdg9y8xDg1yUdEPCdQ8op3j653SI-mIQs4cbusDo1aSfWrdmJyDDyhb0HqWrP3JS1Fdit85qQkJrnXknuWJ5Ddl8uuSt-6ZqkSbiZmAc4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین کمپین در خبرگزاری فارس با عنوان قطع داوطلبانه نت بین الملل!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123980" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123979">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز به نقل از یک منبع:
در حال حاضر هیچ ضرب‌الاجل یا چارچوب زمانی مشخصی برای دستیابی به توافق در مورد ایران وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123979" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پزشکیان: خدمات‌رسانی دولت در هر شرایطی ادامه خواهد داشت
🔴
دولت با تمام توان و ظرفیت خود مسیر خدمت به مردم را ادامه خواهد داد و ادارۀ امور کشور با قدرت و صلابت دنبال خواهد شد.
🔴
بخشی از مشکلات اقتصادی کشور ناشی از محدودیت‌های بیرونی و بخشی نیز ناشی از فشارهایی است که در نتیجه شرایط خاص کشور ایجاد شده است.
🔴
دولت و تمامی دستگاه‌های اجرایی با تمام توان در تلاش هستند تا کشور با کمترین هزینه و آسیب از این شرایط عبور کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123978" target="_blank">📅 18:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb7188e1b.mp4?token=ZI6l2QV9p5sO9IwHUGoeonXAe6t1pGa2hTupPEk1W1q5_ST10m4U_S3nhehAAoxvnM6KoCIc2cNUOSgtdNY706Pu38iUifyRo7g3dYogb_Ii6p1skjQKBvNyOEBiJBRSIi57NMlHNPy1G_ugyuugGpgHia0LEEjKIRWI-X0qy6_z_gysk21A-nccN7RVTPKMoN-dFv9bUR6E1DV9xQ49dpQ30leP_ml6M30QFd1Okzdm0NMqxsYk2ezVFLMDkbKCIclaqcrvvM57zxgs2G67-AvjEl8rZjbuK5ynBjafcjJB8gyoiMCGclp1RKMP5enun_H4UJjSD5H6tOyeMAsHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb7188e1b.mp4?token=ZI6l2QV9p5sO9IwHUGoeonXAe6t1pGa2hTupPEk1W1q5_ST10m4U_S3nhehAAoxvnM6KoCIc2cNUOSgtdNY706Pu38iUifyRo7g3dYogb_Ii6p1skjQKBvNyOEBiJBRSIi57NMlHNPy1G_ugyuugGpgHia0LEEjKIRWI-X0qy6_z_gysk21A-nccN7RVTPKMoN-dFv9bUR6E1DV9xQ49dpQ30leP_ml6M30QFd1Okzdm0NMqxsYk2ezVFLMDkbKCIclaqcrvvM57zxgs2G67-AvjEl8rZjbuK5ynBjafcjJB8gyoiMCGclp1RKMP5enun_H4UJjSD5H6tOyeMAsHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده اسکات بسنت درباره ایران
:
اطمینان از باز بودن تنگه هرمز، دریافت اورانیوم بسیار غنی‌شده، و اینکه ایران سلاح هسته‌ای نداشته باشد — این پایان دادن به کار است.
🔴
این اولین بار است که ایرانی‌ها در ۴۷ سال گذشته حاضر به بحث درباره نداشتن سلاح هسته‌ای شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123977" target="_blank">📅 18:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfAr7SamgXRogVOiVLpTFFofYY0LUNvRlDma-ENPHtZTzi5mtgfxTzi0aHqjt8jx70BvLgui81-IJRBXgR4Cop0phyhqUE7VOxUUY1Qg0sMYBh6VHoTytnEylzin190LahUUp4bRdEuXpov8oP-PhLxsvkKMoxO4tpA5Ha4nKfLlRLSdlwo_sZ-gXZ2Yczk50onNX3TRVgqchhEkj3FQjDvvRL7udNVm_y9KR6ouF70azFMvoxG6LFOqUMpvpfHFcyWbNzhooh0x62yplHf7JuV_Te7Md-EKa7lnPR-hAntCb235mEgpG94jbOk55ZWpx4q156Bw-pNAX542S4G8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123976" target="_blank">📅 18:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
منابع خبری مدعی حمله موشکی به حزب ضد «پاک» در کردستان عراق شدند.
🔴
یک مقام حزب آزادی کردستان به روداو گفت که روز یکشنبه  پایگاه مهم وابسته به این گروه مخالف ایران نزدیک اربیل هدف حمله موشکی قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123975" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شبکه LBCI لبنان: روبیو دو روز دیگر آتش‌بس فراگیر در لبنان را اعلام می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/123974" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDKF89a9LQkewfoCTr1bguZtqC9e1mdveYxAPuBynrVn2wNkiQQC9pJxayXrveZdeBZUmCZbnJSrATFfzHsLnLqNes5QDV1S2sDeQnisW32q5k9tI3ug5bPqbUQKxMpR2DwTAdFb1XGI2GYWnzfocJYn6kxNUSK02l-GsjE4NUhQfHn44quZ62oMM5JgBC08COlB48-IpH0CixqDF6BSgyuJmiH59du7Xy0ru4qsBer63u6oB_MNi4DKzL5JNTAScMyLAV5hzuXuRHndpHP3V2V6VnwOczDVsh8Rke1-B3cqe7RTIzseLQtY925e1ivN-JF6we1bVhmHGlX-ag1LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با کمال خرسندی اعلام می‌کنم که تام باراک، سفیر ایالات متحده در ترکیه، که عملکرد فوق‌العاده‌ای داشته است، به عنوان فرستاده ویژه ریاست جمهوری در سوریه و عراق منصوب خواهد شد، و ما همکاری استراتژیک خود را با هر دو دولت پیش خواهیم برد.
🔴
تام با حمایت کامل وزارت امور خارجه، سفیر ایالات متحده در ترکیه باقی خواهد ماند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123973" target="_blank">📅 17:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
حزب‌الله با پهپاد FPV مستقیم به کابین یه خودروی امدادی اسرائیلی حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123972" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123971">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سی‌بی‌اس: میانجی‌ها به مذاکرات توافق تهران-واشنگتن ادامه می‌دهند؛ ترامپ متن توافق را جمعه بازبینی کرد و آن را برای تأیید به ایران فرستاد، پاسخ هنوز در انتظار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123971" target="_blank">📅 17:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123970">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رویترز: جمع‌آوری سلاح توسط اهالی گرینلند از ترس حمله احتمالی آمریکا
🔴
برخی از اهالی گرینلند به رویترز گفته‌اند که برای مقابله با حمله احتمالی ایالات متحده، اقدام به جمع‌آوری اسلحه و مهمات کرده‌اند. یکی از مدیران معدن با یادآوری اینکه پسرش گفته بود برای آمادگی در برابر تهاجم قصد خرید مهمات دارد، به گریه افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123970" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت جنگ آمریکا قصد دارد در ماه ژوئن، برنامه‌های مشخصی برای خروج بخشی از نیروهای خود از اروپا را در بروکسل، مقر ناتو ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123969" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4vhXUnMBYSgjs0aI_4eCI0okfqgPs-lXyBkJ0warDZ2DVvqT1jhekl4P0OP_9GfCinqPLWyyd_NhjZqaGlFwtBgDzMTZmDKXV_oHEaLMkRwPD-6CSEZ1uYCApR4cLBTUokj7g0EiAH18bkoPjwPx0jqm436Zdz1Q97UBYOTlM50ujrYJsnFImoGyQ9GV0-2YyHT7s7QkummKd5F5We-p8xJJ9yj28fm23lj_2UUm01OlTBeNSVgjEpdPbO_BJx9atLJi9JBts4a4hbAUgNEbcC4TRB8-beOj3iAd5k256lgG2G3OVCOt6-_H6GIR3rcgFydbpthfqH8t7d9mvBAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho9a82KRXqbrhY2vljD74yVTqw2TXL0SouV_AW7qySDRaouywKZ6sN4bd8guKrKQuYsH0B8z7e_HDvIvb_IW6WIP1eiuNhccYUj0fw0qjslqUgtA_YAjQAmYTbG8Oq87jc5WQx8kwtJ6GSjh13qaxFSHwkzBD_xKu2370H1bguJpJHB5-NIRr_OACeN-o040Ll8XLhRyzQie3SF6UZJDzfTHIcwi41Tf8oaErh6n0zE5XnANLtFIVGrVLo0t0kUJ8JqwDcxMZl5WL-HqMbaJbpcRiP01pMzsOcvc9YJTvxGU3kDyyT6FKqIM5fPKIWb_224HWVNuSHrueFzoDhgMSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک راکت حزب‌الله بین منازل مسکونی در روستای مسیحی نشین رمیچ جنوب لبنان سقوط کرد. که تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123967" target="_blank">📅 17:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مدیر عامل پارس جنوبی: بازگشت سه سکوی فراساحلی میدان مشترک پارس جنوبی به مدار تولید
🔴
مدیرعامل شرکت نفت و گاز پارس از بازگشت سه سکوی فراساحلی میدان مشترک پارس جنوبی به مدار تولید پس از جنگ‌ تحمیلی سوم خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123966" target="_blank">📅 17:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf49usHZzjWyTkqKEDxxATwH0a6dFKsiBflkGX1I0Ewqt0ht1Mz7dDWhzDJcl7svvOwMylMFFxMEAoXDtuvPxANUpKLYzs3pdy8MAGqJ1T82QNdcUQdxfsi0u9F_qDSYlta4_TFkpamLJiR9MajOZd6OUcZT8D7hoKaipqi0ndGzHvgVgGHZ-ppmC8scE-Xzl_GSZQbrhx051efpgEZtet_tSY5Q6H0DJA-_dsaG4brY6Eo3c_iZNBzS0EIgR397BVPIRb6qpPykFXuFsbR6MENyVaneanMUJy6qYrVI92xDSe6MNkblbHLDj5L3fUdhjPVIRekXhWBqqdr3HQS1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: درخواست فرانسه برای نشست اضطراری شورای امنیت درباره لبنان
🔴
ژان نوئل بارو، وزیر امور خارجه فرانسه، اعلام کرد که در واکنش به عملیات نظامی جاری اسرائیل در لبنان، خواستار تشکیل جلسه اضطراری شورای امنیت سازمان ملل متحد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123965" target="_blank">📅 16:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قائم مقام معاونت راهبردی رئیس جمهور: تراکنش مالی وابسته به تنگه هرمز حدود ۲۰۰۰ میلیارد دلار در سال است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123964" target="_blank">📅 16:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bab239b5e.mp4?token=SXnRVwCEsHfo0FoNndeXOaZT0ugCWitfjJJGLU0R4kdUwEZz4J8DdkkZyz4iFSKW25OeigpAtZczlmopaZWvU0PUvHocvQaF2aVE8dbcfoC7F6Ouqfdef7YX19DttRROjKXjJyM6EvzIXwynpTiyHUOL6tnvUdGnZqvieKdHJ0Zc5BJK3ldrGxgzGZicuaRKBE4CR86KPIHdkmcDY-mO8GtmGAa-S7n0xR_kHKQcWitZU7Kz8xxohWn6unOrUS8IHXU7XMcOJMkaTpRgdnnLppJXTzFLev7n7OeAPBCwRP8t0iXi52fpuzmihs_Y5whTNWE3LiJVPGXMzgiv76RHZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bab239b5e.mp4?token=SXnRVwCEsHfo0FoNndeXOaZT0ugCWitfjJJGLU0R4kdUwEZz4J8DdkkZyz4iFSKW25OeigpAtZczlmopaZWvU0PUvHocvQaF2aVE8dbcfoC7F6Ouqfdef7YX19DttRROjKXjJyM6EvzIXwynpTiyHUOL6tnvUdGnZqvieKdHJ0Zc5BJK3ldrGxgzGZicuaRKBE4CR86KPIHdkmcDY-mO8GtmGAa-S7n0xR_kHKQcWitZU7Kz8xxohWn6unOrUS8IHXU7XMcOJMkaTpRgdnnLppJXTzFLev7n7OeAPBCwRP8t0iXi52fpuzmihs_Y5whTNWE3LiJVPGXMzgiv76RHZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز به طور مداوم حملات هوایی شدیدی را بر شهر صور در جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123958" target="_blank">📅 16:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال: سازمان ملل در حال ورشکستگی است، زیرا ایالات متحده و چین میلیاردها دلار را از این نهاد بین‌المللی خارج می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123957" target="_blank">📅 16:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عضو هیئت‌مدیره انجمن داروسازان :
کمبود کدئین به خاطر تحریم نیست، به خاطر محدود شدن تأمین تریاکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123956" target="_blank">📅 16:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: پرونده لبنان در صدر تعاملات مربوط به توافق بین تهران و واشنگتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123955" target="_blank">📅 16:28 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
