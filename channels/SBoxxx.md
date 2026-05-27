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
<img src="https://cdn4.telesco.pe/file/Qul-IUKSHQzVR9xHYOjdS1pGcJokP3VU2SoB-5tA8GLtdjlGf3nzjY5FDo01fColjofmSNHygbWr20Tf0cihC6YuA18-5d1VNosAp2bsNfBFn8LQlR_YiqKnzYqkvbmLOXCdf3M_BJLityrw6wenEQpXj_-2pnglbpNMYuk9Z03tYoVJLdsxnfpW-gr8yLwphuyEdCdV1OdAOFjBVxPqg6XJdt_kB8FAWIKSrc3Y7hOVYqWLP4HQbERN5WSjfMInmTGR2DBUr9AmGvK1Kkf-zWCQ2bUNsE412UnwdxF2Vvpvg5UIywH58J_YFQUo1crZxY-0SCvGrCb5fjJRNq8jXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpznZ0PJv8I88cyAnqQnJGuwHC65B3qQq9Y1n4JGPz8PHlHZyoS3kREVyrqfU8n1ejoH-boy-iDcZFy17Ku3kh5utRRLuHxl0RN8BZqCFowQHaWKh9NRkqZPPwc_azJvkk8N7djehMhnhUBO2jHcxm9fpWBaDVt0Vv-McluTOcczc4HpxS2dXkbDYsTJnjYXjQ5HFgWU_WRxOlIFDKE51wUKO5pyOGhs66mVu4NZufbJta7NaEphIrJLQbyx4tSJGFRiuWkGRAUuJbSfog05sAaUDO-ANpZzuSSieNSBbxWCEXWGy62-JUV-vvXyFY4swrmcRgv8lLqPG1-KdQATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه در حال بررسی محدودیت صادرات گازوئیل و سوخت جت است، زیرا نرخ پالایش به پایین‌ترین سطح چند ساله در پی حملات فزاینده اوکراین رسیده است.
به شرکت‌های نفتی توصیه شده فروش فرآورده‌های نفتی به بازارهای خارجی را محدود کنند. تصمیم برای ممنوعیت صادرات گازوئیل و سوخت جت در مراحل پیشرفته است اما تاریخ آن هنوز تعیین نشده است</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SBoxxx/16689" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANiJz_TMv_776ncPFx3qIJWl9XE5cbdC3opPtNECaQ6MVQ6s1mV6H3V7RMOOfZoae9_EWeL3QKgoBVq746tO6u_1jkD9JQ-sW3YicWSxzh89hNWJsbVDiBgJpM_m09FRwKmJRauCAoQXBgbZyTcBPDg0wOIr719GsKdhCazSozWGznCzK91GamQW9xLIW0rWyWygiF7iFAefT98adovbGyCI42bpYmMKvcGq7EmusfK87PlNd7LKwQOueUMamxbQQxPvTt834_eWSUThCeGevrFyKYkaZuB5Ts_JkJ9Uuj53lBqNLGiuGueVp2CArdGEj79mMAzgQAmbeN8n_2_axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از درگیری‌های چند شب گذشته در تنگه هرمز و اطراف آن، احتمال ازسرگیری سریع ترافیک عادی در این آبراه حیاتی در بازار شرط‌بندی پلی‌مارکت کاهش یافته است.
اکنون معامله‌گران احتمال بازگشت ترافیک به حالت عادی تا پایان ژوئن را تنها ۴۲ درصد پیش‌بینی می‌کنند</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SBoxxx/16688" target="_blank">📅 06:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe37KNf3E9S9X8otHncLS975qaxzbNh-QTg36IJLbsHHUAO8HsQdJ8ISty64Uq4TUNEFPKADNcs0OBhKWmeOenfW-Bp3gs_CUZb9DxrCT5OuLFw4REDsXRiOruFMwwxUH12mZTISpJRBekc4dBUD8ixy_EZwurdm1Sm7I6tI8WiIrWdUb2P863nFoMPhtJv6d8lXmDibluBad6CpXs-fUioXg7rqLjtHHuYazHY3PTF6OJlGUJPt5VgvV7twGeHzCdRDcVNQa3-Nc2kcIb6Axf3yCwBmQ5BoaWOWymZ1RRCA0aWuK7705ErhYuZqLJY82eHL13dOPgasJf8sst-PaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16687" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/16686" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZU8axwjJWuHbzyI3_OXXujUE7XWUOMjVjp8Dwv1YMvV2f_xLtfjNPgry8mMrpGGUvow6kpu0q663FUKRRjGGJa27i8ktaQOpJdGfIIz7ZjKCOMB7Thk6zEwZJxVteAuYDYSie7H_Eaqn6X5PdMHuF7dp_ATSW6JWv9kPJhym2kTXGIFD50wI2rkpNbe1k6rt9-6eQYjZt_FUBMmvPvDlcw5rpx2ZD8k4pTpwhwE3A7CNHKiNq2Xl_aWrHLdseMWsEIMoaJLSZacqEZ0jEDo1whaQ1DvGZmVklJpUNJB3UM2Y1mM0ft165PBgaZwuqFq5KyfRiICp6KkMafCOxhYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه پدافندی کوتاه‌برد ایرانی «مجید» در رژه نظامی ارمنستان در ایروان به نمایش درآمد.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/16685" target="_blank">📅 22:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=GmqthPQDbz_A_EcyxL0wsQj4HuF9qcbko61QjiayqfG5J9YyQtVTtvfR48cmqwSxfGoXwC51f94oEzqHFRTxrB1ezus3B-1hZv84PCte_Muv5mYN4URwkmg32HjW1vVWMjN4_I1dMjct8rvEBYiZFv31Jf4xfwF4P3owAuuknzuC697mmgNbyQ8bkiQZIcs1o3eP1qW7bAzscFbjXC3rzBEISosWJkOvAaVgfkBIqhxbExOXTUD4WSHkl14LdmIvzjzgkFASLbM7sPld9Zlu8Q8vnnocf9Mk7Tfcm5RBMxSvHSg-Fljc1f3udH0SQwv8MYwaZ4HcYcmo69pDKxky4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=GmqthPQDbz_A_EcyxL0wsQj4HuF9qcbko61QjiayqfG5J9YyQtVTtvfR48cmqwSxfGoXwC51f94oEzqHFRTxrB1ezus3B-1hZv84PCte_Muv5mYN4URwkmg32HjW1vVWMjN4_I1dMjct8rvEBYiZFv31Jf4xfwF4P3owAuuknzuC697mmgNbyQ8bkiQZIcs1o3eP1qW7bAzscFbjXC3rzBEISosWJkOvAaVgfkBIqhxbExOXTUD4WSHkl14LdmIvzjzgkFASLbM7sPld9Zlu8Q8vnnocf9Mk7Tfcm5RBMxSvHSg-Fljc1f3udH0SQwv8MYwaZ4HcYcmo69pDKxky4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/16684" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭕️
فضای دیجیتال ایران ، پس از تجربه طولانی ترین خاموشی سراسری اینترنت تاریخ مدرن جهان ، از امروز به صورت تدریجی درحال برگشت به حالت قبل و فیلترینگ مدیریت شده است</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/16683" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/16682" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62edae59af.mp4?token=ClhRQ3l-PvrzbTQPcOnXfCJqVyY1Ha5thco_Vd0QU33forXFM0sa4nNm23DpIFx3fmJSkp6a4y7cwsMpu6i8NBm-t2jZOJyKWEKz2YkYs4VbMwwYQ63lUcuhstVBJlsiR0WxcCoEbZ2AYLXRa4SZz-IW1hI9wRtpIh3gPuH3vvUyRNJ7YcDm0uDnF7OPf_LNeaU6IsLNb-GhJkLR5zBN9Z0DsdLEL9yuXl-Jc2EqLX9UYGVLVrI5dIZwIveg7Ywkaq44HWUxMURU3vhxJvp3VFZS246aGk5EkQ4frTfVcrU-DV_Y4UZ5Zo4MU64X2BrWLLcZAM_NqROGJzQLubld7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62edae59af.mp4?token=ClhRQ3l-PvrzbTQPcOnXfCJqVyY1Ha5thco_Vd0QU33forXFM0sa4nNm23DpIFx3fmJSkp6a4y7cwsMpu6i8NBm-t2jZOJyKWEKz2YkYs4VbMwwYQ63lUcuhstVBJlsiR0WxcCoEbZ2AYLXRa4SZz-IW1hI9wRtpIh3gPuH3vvUyRNJ7YcDm0uDnF7OPf_LNeaU6IsLNb-GhJkLR5zBN9Z0DsdLEL9yuXl-Jc2EqLX9UYGVLVrI5dIZwIveg7Ywkaq44HWUxMURU3vhxJvp3VFZS246aGk5EkQ4frTfVcrU-DV_Y4UZ5Zo4MU64X2BrWLLcZAM_NqROGJzQLubld7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙌
@TweetyChannel
| علیچی</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/16681" target="_blank">📅 19:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/16680" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خب نت دارد وصل می‌شود و اساتید بزرگی به جمع ما بازمیگردند
سبحان الله!</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16679" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند. @TasnimNews</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/16678" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری تسنیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=XptpNKAuHbEAVKM3oZuiXQUyp44SSSJ1fEf_a-yyxDTwJdHZX5t7ODECt5XHmSOAfyJtLwxvM12YqjN6Cg4MUAXy7DrPfb1xiK0_dwto1nH6QqhxQEk45G1MTxt9IrxcsfmYEsKqxlFycCfluSOEF_ZuNo7qADDSRUva-v9QiT8izWWXL4pwhKmyaG5lS0GqTy2f_k2IvUaLYL_NxhTKvYe5yqipj6ReNhlDG5gLFBAP42VS5uUalBabdDjJa87tBcw7zB_35HuEmvr-xPb7eMAmPDrIG3E5xVelN9mA_fo6sKVGVhtl6c89MvdayC1D8KAz0RIbttryNwIfpj93vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=XptpNKAuHbEAVKM3oZuiXQUyp44SSSJ1fEf_a-yyxDTwJdHZX5t7ODECt5XHmSOAfyJtLwxvM12YqjN6Cg4MUAXy7DrPfb1xiK0_dwto1nH6QqhxQEk45G1MTxt9IrxcsfmYEsKqxlFycCfluSOEF_ZuNo7qADDSRUva-v9QiT8izWWXL4pwhKmyaG5lS0GqTy2f_k2IvUaLYL_NxhTKvYe5yqipj6ReNhlDG5gLFBAP42VS5uUalBabdDjJa87tBcw7zB_35HuEmvr-xPb7eMAmPDrIG3E5xVelN9mA_fo6sKVGVhtl6c89MvdayC1D8KAz0RIbttryNwIfpj93vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند.
@TasnimNews</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/16677" target="_blank">📅 16:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNrTw87_FWE1KU5YwpCh0jzep5gjH483xsxdC0-WT4kMET3JzJ6caCqNCsaK_g_ZZDz_0LO3_oCj8X-FFCBtUTYCaOtqeOk0x5gyjM38jQEZzEl7BLUiBz6Sv_D3Rm_TeQM74GVC9rPswv7nwMjiq2vkccsoeT8kirr_2YDv5opLrQNYBxwOfNR550fKHx0Vyi5afuvVCDn3a4ZzRzkb5PGahdUJcOvH-yWI37PSh4VjTOx27DEo2q-ldGfeuNl2t1X96dN2Bw2f1m8uOAe-E0y2vMGGkN035xheYhVUBBG7wZZrJ1yejaAQuLtQ1O6Q9erJRW-KJQzb5Lt2hTt0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/16676" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16675" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4anDh1rpHeBcPBYvVBRxYTGyeuX1QdG27kNTeYo-jxXy_sA0W1BQuZKaGtVtndgvVLTHOX8OoJI0nDm7naf_aDFLSacUQ1w0PWhCfLtxFOjY1mVUgA1N-PaLz-5g_oL8BlXCl8QDfRMDoBQ1ul7x8DWzl5e4aOKOZ0ijS3RYQZdQ7djnEKxZtKVUfnfFLyMtzHWu36_b86bxm3gz7Ay6dpR3Gag9CODuzbwF-WBcRc4Uuj31l0aLqHqEVdTcw7hr2AD3krgS_SIzfKAMfllx0uca3iiG4F31aURFFJFfarcBYE_vFFA7_jRLw539pg_0j8LIljmlNejhCV-W9I1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/16674" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16673" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuqLcJ73ry3ds9fbk5ykrKwQp7t2UTGD2OPiq7qQ8A9Drzwj3SHHZqxRKQ25pGvUCpspxoWKeKJlX7pvdDArxX7ZGlawCDmPDJSkfb_IGsd5qWB5xoZjxkSYXg369tOov6npLg6h4CwF8UJM4thCch_V3EVQFUFmYyMlD2BfGsenQOyCOJs5WJkHrxZ4FgqwmO4hHDXqlH_CJwF7Y42AHsVlOA25O8y-jJ6r91dlQhh21Jx5huqc2n5azblP_kq1xa4tdf6JCs4TojMhIEGlluuoEwiF8zjdy8-SEso969cyjijd9gG_spdhrms2vIiawVhZLedCQSeFZ62EI5j8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کوتاه روابط عمومی سپاه از درگیری‌های روز گذشته در تنگه هرمز
🔻
ارتش تروریستی آمریکا در منطقه خلیج‌فارس در ادامه ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای دفاع از حریم…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16672" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153170738b.mp4?token=ao1GIKpK8cgBdkfHar91JGw6NQPIpwkltl1L0t7MnkylWmnCzT2qsOcMVaXWJGJuZue9OdHrFXuGBCwyMG890PgXntrrShWQ33XnONEG6d6hWF9NESSLYFkOULslp2g4s_-q3JZQpVtkWqetFnhHjZjPm3u9LhSWOXgeNxZg0XkOrFgSDvolzWsMwseLM2b6qbO-V4obyNTLXoScgvsqIzLqBy1gesT3DBCtmx4Tcr81Ze7iGnFf-lRnRHJDJDEzwrECiXHDbuLx7xKYFTQcnfcK9-UahzetMk1TpiqaK7B9d-KICjf0i2ibndUboXly68M90eKsgimSQAdY9ioU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153170738b.mp4?token=ao1GIKpK8cgBdkfHar91JGw6NQPIpwkltl1L0t7MnkylWmnCzT2qsOcMVaXWJGJuZue9OdHrFXuGBCwyMG890PgXntrrShWQ33XnONEG6d6hWF9NESSLYFkOULslp2g4s_-q3JZQpVtkWqetFnhHjZjPm3u9LhSWOXgeNxZg0XkOrFgSDvolzWsMwseLM2b6qbO-V4obyNTLXoScgvsqIzLqBy1gesT3DBCtmx4Tcr81Ze7iGnFf-lRnRHJDJDEzwrECiXHDbuLx7xKYFTQcnfcK9-UahzetMk1TpiqaK7B9d-KICjf0i2ibndUboXly68M90eKsgimSQAdY9ioU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرامزاده پول بده نیست بیخودی امید نداشته باشید</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16670" target="_blank">📅 14:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16669" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.P</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=SWlHkNnSozeFv3f-agfwtuW9NVT5Bk_aMA7m0It2LzyaBPS22jYWGucOmZqfqTfQd4vKDqnVBijk8J04-zySH3eB-7XPzJVG-TeW_g0lrJWg9THwC6tVH2W3Xl2BqBVAYQaWDjAa2VBk9EFDlINjxcDTm5Nk4UFwtETYWMmMmDxOQSV9I5YGFD5XLC5ct15eXEJxsH5uMo9DP7SZUCBykrx5wt9goxmz1Odo77Ra1VbWW9ShFap3KXzvuul56hF6a5xHlUTTmn-ckb4TSA3CC32nFUW2nKvzbuwQLMFG7zCj3mFCvV731X5zbxL3SX4CrTV3xZgEgqZcL8jNSKRsEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=SWlHkNnSozeFv3f-agfwtuW9NVT5Bk_aMA7m0It2LzyaBPS22jYWGucOmZqfqTfQd4vKDqnVBijk8J04-zySH3eB-7XPzJVG-TeW_g0lrJWg9THwC6tVH2W3Xl2BqBVAYQaWDjAa2VBk9EFDlINjxcDTm5Nk4UFwtETYWMmMmDxOQSV9I5YGFD5XLC5ct15eXEJxsH5uMo9DP7SZUCBykrx5wt9goxmz1Odo77Ra1VbWW9ShFap3KXzvuul56hF6a5xHlUTTmn-ckb4TSA3CC32nFUW2nKvzbuwQLMFG7zCj3mFCvV731X5zbxL3SX4CrTV3xZgEgqZcL8jNSKRsEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16668" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL2lSr5cHp6LPxOu4BOfgYa1o3iK5HLGYLFHyAWtvayT3qNjoPNI_DMUd1662-_lbKO4K9lfakGyUpfexeNwzMqi66P42LHPNdMJ9lhhULeLUqnGHxKnwaSV7fsTvOkycK3A9hJ5_PqNPzUrw3v8JEdw-nTOy2GojfLce4YSKgHsXUdMFQ_mgbC6Wwtz0yw6Lkr4qaO-EAWaKAtwWLVgfoZA4J6GinKLLSmdl_2hnp3J-AKwqlkQN5f82Av1Y0k9xr4oXqK8H_ZGmnOhXG9JOy1Tcyn9ilLW1mZS07PFFfSvt5dqjMPoXK8BgP_DEvRP9FxR_t5l7yTrWu_gU0s4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ مثل این بستنی فروش های قرمساق استانبول است که پول را میگیرند و اسکل هم میکنند و آخر بستنی را هم نمیدهند</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16667" target="_blank">📅 13:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eElucIwv7TPyb5dZ5AdZKW99DfFdLPRbC8oyFmXCWPe-sAL5AmODpu_yt6z0AQV_l9w2moord_nF9iXKZ2E5UFqYie9rBDIKm5P4dIH1hl55mU2ByzX8hK7NQfuJmxn68tK9rLGNV7RarlTRDc_NnAIxUpF5CmNyvaW1pPzCoInmxtbrkmp58-9gGWe0L-fVkiQynKq17z-qTRoRedWkEzHCmlypa5xEUx5NiQ-EXoK0feQG4tJybuLFv5XGriHgAOs6ycH1KjLS8tUU_yXJ-3-ByL_Q29H77enTasx2ychJLUOzygt6oYTEXUa0VX-WxVPZ8VooQU-I1FWJYwIISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!   بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16666" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16665" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کم کم دارد نت وصل می شود!  نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16664" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFbvzq0dBJMJiJutHfwE6tCaqAu7S2zpiF3KJzfpWQe-OHbb4Gm0alLUDxZBnzV3hur5tWFa9yMjIAYA0ym3RSsNsfEsS0MbUwwie9L9fO62ztXulERGUnAskBQXuh842xw7uyVGCPFAs4OpTKJ93AHe8mP5EHcXwIaJd-xELf0rhXxRN7TKYLofGewKkDM_HAKx0Yn6q2A4jJD6mcKLjZ3da5Vc_l-IbiRBFYjSGtLP-rcgvPLKcBNvREjllM_lVnGHUf_hXv1tFlUTjhficNxG8OFctu96dp1eZd4SSF5lPvcbe73NmPjVOgSAPJwmOT9Mrx2-2VB6UnRrriNscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
پاپ
:
هوش مصنوعی همانند سلاح هسته ای ابزار سلطه و مرگ است</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16663" target="_blank">📅 12:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کم کم دارد نت وصل می شود!
نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16662" target="_blank">📅 11:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سبحان الله این چه وضعیتی است!  یک انفجار روی می‌دهد تا خبر انفجار قبلی را منتشر کنند!</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16661" target="_blank">📅 11:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش اسرائیل آغاز بسیج سربازان خود را برای تشدید عملیات‌هایش در لبنان کرده است.
نیروهای نظامی از سربازانی که در روزهای اخیر مرخص شده‌اند خواسته‌اند تا فوراً به خدمت وظیفه عمومی بپیوندند.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16660" target="_blank">📅 10:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خاصیت موج  4 همین وضعیت ابهام و سردرگمی است.   مثلاً دو هفته پیش ما تقریباً تا آستانه ایجاد یک فاجعه هسته ای با زدن نیروگاه امارات رفتیم، یا آمریکایی ها پریشب قایق های موشک انداز تندرو و پایگاه پدافندی را زدند، ولی باز هم نه تنها می گویند آتش بس نقض  نشده…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16659" target="_blank">📅 09:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فکر کنم موج B از ۴ هستیم  از توجه شما به این موضوع سپاسگزارم</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16658" target="_blank">📅 09:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرنگار الجزیره نوشت ابتدا سپاه پاسداران به یک کشتی در خلیج فارس حمله کرده و سپس جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را هدف حمله قرار دادند و چند نفرشان را کشتند.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16657" target="_blank">📅 08:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3mIRuk65LOevSDLjiLMoFgze1JvZ_ESipiWdKSi2YCbxCK3UPLKMMJvPeq0fDSEzx55ogtzHeqk9cAyi8LbuV8Qv2En6JOweb91gTF9-Na_IHy5NiM36piEMRGw4jPIQSG51M_z993QpXFuXCA5h8ta6N3qYhYs_YGt3uF1IqB4owSyEeQq_E8OOmybL3hPM91rLAVXMuqR-Tdcs9R6-0O9z2BzT5EV1iL4y1T3RPS5Uzg6VSYtEu7U5nTTm5Ay3IBOLxMxPcAjQ7E7304AB1NxWVoKne2-MlhiciwvRpr7NodycLitUJDLdgJxUz91VeMjOc3GL67xu41kgvGsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت های متفاوت مقامات ایرانی و آمریکایی  از روند مذاکرات از دیدگاه موسسه مطالعات جنگ</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/16656" target="_blank">📅 08:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این مجری را خیلی دوست دارم؛  اولا با وجودی که نصف شب رفته یک خیابان خلوت تاریک، ولی لحنش جوری است که انگار دارد فینال جام جهانی را لایو گزارش می‌کند! خصوصا آنجا که اشاره می‌کند به «موتوری که هم اکنون از پشت من رد شد….»  ثانیا در هر اجرا، تقریبا ۱۶ بار اشاره…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16655" target="_blank">📅 08:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وضعیت بندرعباس آرام و عادی است
🔹
استانداری بندرعباس در حال بررسی منشا صدا در این استان است.  @TasnimNews</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16654" target="_blank">📅 08:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری تسنیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee94b5ab44.mp4?token=HV4Xtr8myl6uXIlUDgd85Qqh36GMic3Lb1zBHOG9PrE6tV5gQtRgvPPiiyvkLYlGeDbsss0kh8sdLDr9moncopNv0qHFlXN8LX9UCx-HCd9mq2tnhBoGUmF_ELSCpeEP2vvAmojvDnNKTO1ae2FnuqmZcD65Zx017K7d2nuvd9AtkXBoTIlvpyEhrFHiyw8QYsRHztGVwolkut8YQFsETfdrni8LpTFD7eZ9Lw6nypoV2iaL3MZ0f-GD1r9-l-8-1xxiHstHYIKOLfbSDVabTdQbgJmCCywMev35pLAYmd5hRPaRUCHJrnuEW8Cad8H5biXr4Z7rwgt5wsmOYnhGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee94b5ab44.mp4?token=HV4Xtr8myl6uXIlUDgd85Qqh36GMic3Lb1zBHOG9PrE6tV5gQtRgvPPiiyvkLYlGeDbsss0kh8sdLDr9moncopNv0qHFlXN8LX9UCx-HCd9mq2tnhBoGUmF_ELSCpeEP2vvAmojvDnNKTO1ae2FnuqmZcD65Zx017K7d2nuvd9AtkXBoTIlvpyEhrFHiyw8QYsRHztGVwolkut8YQFsETfdrni8LpTFD7eZ9Lw6nypoV2iaL3MZ0f-GD1r9-l-8-1xxiHstHYIKOLfbSDVabTdQbgJmCCywMev35pLAYmd5hRPaRUCHJrnuEW8Cad8H5biXr4Z7rwgt5wsmOYnhGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بندرعباس آرام و عادی است
🔹
استانداری بندرعباس در حال بررسی منشا صدا در این استان است.
@TasnimNews</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16653" target="_blank">📅 07:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njWIzD0PB-Cz0FKuIqzWKVD2EWR0_dSwHDJaPDvPryrl5SvPXiTXmRYOlnDxonxgaLRcXgTPsbcRRhvvEc9Of8gn_bpYfrbL2Hv9fkGO4JEVyJhyyCrK9I-qxpn2sAN4Yi8SiChs5bO576sCxPzc8NOYm-6MaSinkj8dkU9ad9bfL_TguTq3vmaZF-GAqb2YiXXR-uLeMoNhK6ee2mx9ZZmbbiZWY_kXYtkNv_EpeD9QmSngSAxaJmr5HZk5qLhEU0G6DNxP8eP7Hs-2kwsB_95PL6JjHu2UfgA03Gd4XJXggE64yCDi5D6ri3-Q94N6K5ZrbryHIcfvxUHgWaHysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ننگ بر سازشکار!</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/16652" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شما خونه تون مورچه داره ؟!</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16651" target="_blank">📅 01:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرنگار الجزیره نوشت ابتدا سپاه پاسداران به یک کشتی در خلیج فارس حمله کرده و سپس جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را هدف حمله قرار دادند و چند نفرشان را کشتند.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16650" target="_blank">📅 01:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسرائیل عملیات «پیکان آتش» را ضد حزب‌الله تصویب کرد.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16649" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/16648" target="_blank">📅 01:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سبحان الله این چه وضعیتی است!
یک انفجار روی می‌دهد تا خبر انفجار قبلی را منتشر کنند!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/16647" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هدف قرار گرفتن قایق‌های سپاه مربوط به ۴۸ ساعت گذشته بوده است
‌
خبر هدف قرار گرفتن دو قایق تندروی نیروی دریایی سپاه مربوط به ۴۸ ساعت گذشته است و انتشار آن به دلیل جلوگیری از فشار بر روند مذاکرات به تعویق افتاده بود.
طبق این گزارش، این حادثه ارتباطی با انفجارهای اخیر در بندرعباس یا جاسک ندارد.
تاکنون مقام‌های رسمی ایران و آمریکا جزئیات مستقلی درباره این ادعا منتشر نکرده‌اند.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/16646" target="_blank">📅 01:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری مهر:  منشا صدای انفجار شرق بندرعباس بود/ اوضاع کاملا عادی است
🔹
دقایقی پیش صدای چند انفجار  در شهر بندرعباس شنیده شد.
🔹
پیگیری خبرنگار مهر، حاکی از آن است، که منشا از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16645" target="_blank">📅 00:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری مهر:
منشا صدای انفجار شرق بندرعباس بود/ اوضاع کاملا عادی است
🔹
دقایقی پیش صدای چند انفجار  در شهر بندرعباس شنیده شد.
🔹
پیگیری خبرنگار مهر، حاکی از آن است، که منشا از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت پدافند در این شهر خبر داده اند.
🔹
اوضاع شهر، کاملاً تحت کنترل است و جای هیچگونه نگرانی برای مردم شریف بندرعباس نیست.
🔹
هموطنان عزیز توجه داشته باشند به شایعات منتشر شده در فضای مجازی توجه نکرده و اخبار را صرفا از رسانه های رسمی دنبال کنند.
🔹
هنوز منابع رسمی در این خصوص اظهار نظری نکرده اند.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16644" target="_blank">📅 00:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارهای مهیب در اطراف تنگه هرمز شنیده شد</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16643" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به نظرم استاد رسایی هم از گشایش فضای مجازی سود بیشتری خواهندبرد تا اینکه
در بله و ایتا اینطوری از عالم واقع بی خبر
باشند.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16642" target="_blank">📅 21:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsLKVLcb0y3N6pBZzBnEdYafubSvxMja3pMtOZapd2miyV6gx7Q6YXT7F1ro1jvQD2ftKZB2MSA3-jsEtD5iQjaFPdYakDyj5jcsgwAX4U7kWByOouit9q_p12XIrotu6-aUE1IxAqOfALMRfLj35nTasaHS5WE8FeBrjD26jLCbiNAjq_xkvpZeg6jQLejrMwnAOhiRFeUB6rgJNbKBOsfhA-AxinyHEmpvBGrYdO-Ku6Xy3a5LorHxcC883Hfu85FjREbW8kBPHwoCcFH06QBxDS7zUmt-WjJWg40TwjoDz7wq6sdHxY9Lnfe6le9T3XBN1Qtqz3T0qrh8y4BRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
مصوبه بازگشایی اینترنت ، دقایقی قبل با تایید مسعود پزشکیان جهت اجرا به وزارت ارتباطات ابلاغ شد</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/16641" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
اعتراض نتانیاهو به دو بند از توافق ایران و آمریکا
🔹
نتانیاهو جلسه‌ای در مورد توافق احتمالی آمریکا و ایران برگزار کرد.
🔹
به گفته شبکه تلویزیونی کان اسرائیل، نتانیاهو به ترامپ گفته است که نگران دو بند از این توافق است.
🔹
یکی از بندها مربوط به آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16640" target="_blank">📅 21:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🛑
در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی ، اتصال مجدد اینترنت بین‌الملل به رای گذاشته شد که با 9 رای موافق و 3 رای مخالف تصویب و برای امضای نهایی به پزشکیان ارسال شد</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16639" target="_blank">📅 21:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در جنگ ما با اسرائیل بیشترین آسیب را عربها دیدند!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16638" target="_blank">📅 18:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گویا قطری ها پذیرفته اند که به جای ترامپ، بخشی از پول بلوکه شده ایران را بدهند و سپس خودشان با آمریکا تسویه کنند.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16637" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Negotiations with the Islamic Republic of Iran are proceeding nicely! It will only be a Great Deal for all or, no Deal at all — Back to the Battlefront and shooting, but bigger and stronger than ever before — And nobody wants that! During my discussions on…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16636" target="_blank">📅 18:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">Negotiations with the Islamic Republic of Iran are proceeding nicely! It will only be a Great Deal for all or, no Deal at all — Back to the Battlefront and shooting, but bigger and stronger than ever before — And nobody wants that! During my discussions on Saturday with President Mohammed bin Salman Al Saud, of Saudi Arabia, Mohammed bin Zayed Al Nahyan, of The United Arab Emirates, Emir Tamim bin Hamad bin Khalifa Al Thani, Prime Minister Mohammed bin Abdulrahman bin Jassim bin Jaber Al Thani, and Minister Ali al-Thawadi, of Qatar, Field Marshal Syed Asim Munir Ahmed Shah, of Pakistan, President Recep Tayyip Erdoğan, of Türkiye, President Abdel Fattah El-Sisi, of Egypt, King Abdullah II, of Jordan, and King Hamad bin Isa Al Khalifa, of Bahrain, I stated that, after all the work done by the United States to try and pull this very complex puzzle together,  it should be mandatory that all of these Countries, at a minimum, simultaneously, sign onto the Abraham Accords. Those Countries discussed are Saudi Arabia, The United Arab Emirates (already a Member!), Qatar, Pakistan, Türkiye, Egypt, Jordan, and Bahrain (already a Member!). It may be possible that one or two have a reason for not doing so, and that will be accepted, but most should be ready, willing, and able to make this Settlement with Iran a far more Historic Event than it would, otherwise, be. The Abraham Accords have proven to be, for the Countries involved (The United Arab Emirates, Bahrain, Morocco, Sudan, and Kazakhstan), a Financial, Economic, and Social BOOM, even during this time of Conflict and War, with the current Members never even suggesting leaving, or taking so much as even a pause. The reason for this is that the Abraham Accords have been great for them, and will be even better for everybody, and bring true Power, Strength, and Peace to the Middle East for the first time in 5,000 years. It will be a Document respected like no other that has ever been signed, anywhere in the World. Its level of Importance and Prestige will be unparalleled! It should start with the immediate signing by Saudi Arabia and Qatar, and everybody else should follow suit. If they don’t, they should not be part of this Deal in that it shows bad intention. In speaking to numerous of the Great Leaders mentioned above, they would be honored, as soon as our Document is signed, to have the Islamic Republic of Iran as part of the Abraham Accords. Wow, now that would be something special! This will be the most important Deal that any of these Great, but always in Conflict Countries, will ever sign. Nothing in the past, or in the future, will surpass it. Therefore, I am mandatorily requesting that all Countries immediately sign the Abraham Accords, and that, if Iran signs its Agreement with me, as President of the United States of America, it would be an Honor to have them also be part of this unparalleled World Coalition. The Middle East would be United, Powerful, and Economically Strong, like perhaps no other area, anywhere in the World! By copy of this TRUTH, I am asking my Representatives to begin, and successfully complete, the process of signing these Countries into the already Historic Abraham Accords. Thank you for your attention to this matter!
DONALD J. TRUMP
PRESIDENT OF THE UNITED STATES OF AMERICA</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16635" target="_blank">📅 18:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyLukqZiDQ_Kk7ypvQCK4F-i58qnhAVS85nn2jVwAoL9eEnaaBWtL-3VEDyeKUFyZZHvkQFZsBZ2UvZXKOKs_sjeg8jnO5K0khpDnxP-CXroUScsMMDpTe-PxsibJmOHVd0p4cu88cYjZ4uBAuC3SAdmfM25JsycSM1kCSBZfOc-KXmdgkG1oEVIy79Dv7vl-rmaK30oRojknWU8yYJnOm7MQkCJ-vqMyF8LeK35V7v2SNRiiTFb1Jq6pn2L8R1m1qxYplH-sJxLLWAT7TCKQiUAsw_VqUj991XU7CkbsPoI9OISWPjWwpAVdEbxD41yEYil3ruhreLJhwdLRHv3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16634" target="_blank">📅 18:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وال استریت ژورنال اعلام کرد مذاکرات بین واشنگتن و تهران سر مسائل آزاد شدن مبالغ مسدود شده و تحویل اورانیوم ها به بن بست رسید</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16633" target="_blank">📅 18:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!
بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16632" target="_blank">📅 18:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من
پیشتر گفته بودم
که ما ایرانیان اساسا نوادگان ابراهیم نیستیم که بخواهیم به پیمانش بپیوندیم!</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16631" target="_blank">📅 17:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:   از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند، یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16630" target="_blank">📅 17:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند،
یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ توافقی در کار نخواهد بود و به جنگ بسیار بزرگ خواهیم رفت.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16629" target="_blank">📅 17:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🛑
در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی ، اتصال مجدد اینترنت بین‌الملل به رای گذاشته شد که با 9 رای موافق و 3 رای مخالف تصویب و برای امضای نهایی به پزشکیان ارسال شد</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16628" target="_blank">📅 16:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در منطقه بانو پاکستان درگیری‌های سنگینی درگرفت و نیروهای امنیتی پاکستان و شبه‌نظامیان طرفدار دولت با جنگجویان طالبان پاکستان درگیر شدند.   گزارش‌ها حاکی از تخریب یک خودروی زرهی پلیس است و چندین نفر از پرسنل پلیس کشته و برخی دیگر اسیر شدند.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16626" target="_blank">📅 15:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk4SGfOCA3p4gM7FvHxNZCgfJfl0VF2Jhjl8hhpZmsR-n4N2dN8z-LMsT9G3EDpARqJE6_PCglq7cxqyWG2hvbssP0IUosBp7qgvTmM5yHKr3vK8wZstWKAa2AaiBij8MXQT4wjP58KoKcocQPtU1spbFc122-qbOdjsK3VzFF2Tr4Iu_PNJaouvjzPs88jCPCvNgXRQLTNWyRLt3EWKUOvCar1arIqUp_M_qM9PHe3v6iKbo-C-Lgp358omH9rDwZXxtS7D5UFF3sDhpb-BIKbugXsTNNsJLkqvsIu7A2Oh1cBSHlCnuwQOJodOGpgoSKWJy8XajWdJjvkbBszYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16625" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZZkznUF12_6BsMzi3-gEIqFJOlqGJrygYxZXlcLYtOdZO5q2A2gkUyRFrC07BuQV4shHjibmCqd30vGgcXCJR5Vmi3tB-tDCsdtf_-RAwOAdDuJ9yIQJDUSzR5OaFtErJcvxE8a-dcgqCEgJnDK9prH-I5SjySYx094AumGGysFpvvaOFNh-SUaa8c_YqsuP1f85WuxKRbNqvKo4iR3Yo4D22ROCowlIb1fDMme4KmyqZ-v2vPMnKNmIam3q12Af9aei7-_mELN8g5-cH6HC0-ftJrzX2dfJRhqN7sM0qKsBnACdZtV6OmCxjhKY3fOXJ5HNCguYv2VfM3wtVXtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!   حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16624" target="_blank">📅 15:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4HqDHrbRqyXlqKOWlO4in5zg3M03g6IFMtXKpz4O6rqFK0ZIoc7gGgiareCaUcQAIZxoVtx3rzhlu-sJ0HNp7ELktq5b0H44GJiCH5zVStCu6sQsxqcAoogUIwqGcc5H6QCLpjljI65ShAalHbPB5mrlGto08ddGRAkp8N4dUu1On_pzOyVopNCBQx01-lWjNIWh1Oj13sSsdYBKc99U5IDIP0rE3c-DUG79yqklv7BhzuLM-RHub_uXLjLlszWoZWWib9ChcTk8yWjj-TQCSiClCxwO_SeYWRAzKdYEnDFErduunyrD4V20rDrvkpF3aO_ncxBL10Njv_E2HUJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16623" target="_blank">📅 11:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16622" target="_blank">📅 11:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16621" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت امور خارجه ایران:  «اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.  سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16620" target="_blank">📅 11:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت امور خارجه ایران:
«اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16619" target="_blank">📅 11:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق متدی که پیشتر گفتیم سوزانده!</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16618" target="_blank">📅 09:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق
متدی که پیشتر گفتیم
سوزانده!</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/16617" target="_blank">📅 08:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!
حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/16616" target="_blank">📅 08:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK44jF5CEZyeLTLLTls1gR7ghGaty8MZpaIqdtH3xi2UuWrTXklQ176RwjQePFFdSczUV3QotptzcxZ-jS1jcCnWZXB975GbAyp6XSs2e1PiCNjvI7L2zC8RgGU4KNJotAaNUGNihZfO3Zz7lYCWk9AY5zsil0Gdxzpnewja0DpQkvx6YgOMKyYH52ihrHxnBSi3WAR-VK86Bns3zJJ7AFybZGwPdkaZY-gu4B2jckVPf2BusS9OBzOdNvabyboYR7vvPjqKy60oko3aaktXuIxt7q_UoyVx-h0oleP1NT9jG6bDrNW6qafB8vKln8Vvj4w9ssdCs3EBAZZKCoRwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه هرمز تحت کنترل ایران باقی می‌ماند با وجود ادعای ترامپ - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16615" target="_blank">📅 08:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ حاضر نیست هزینه خرید اشتراک هوش مصنوعی پرمیوم را بدهد آن وقت میلیاردها دلار پول بلوکه شده ایران را بدون دریافت تضمینهای لازم آزاد کند؟!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/16614" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgDsrMI0cbVQW1Ht3pigZlS4n_AfxFnlscl2QXq-ByphZmIJQegE6mEVmqTC7zumY9P3vcgsz_yt5JBrSkOIAjx71aZJIoc3U9Vfv9vA3hphH7VZrXhKGrSkKz7IMx5nW13Z1I0AYaMRBPgT0l59Gs7WmORSV0dpysrHeOO83jUp35yCy6jtOis5AB03EF3cIr-bu8RR1TaR84mlMe1cEE3_3wKyI792XvcD3rOm6eOczghPiJJDeeflNCq1X29dgqOk7A0yppvpimUHOJ1gVt6MiIE7uNXx-J19aY3yuOS83t25zishK48HCmB912C6zopNHuk-LqmX4vhiv0naPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ !</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/16613" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اسرائیل تنها.pdf</div>
  <div class="tg-doc-extra">347.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/16612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16612" target="_blank">📅 22:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzLgPiXsk-BOe0ncHMEh-W86A3USpQtbZDdJ8y82eZzQBRCJyLqKHJ-nxHHUsnr0JmKbzIUBWKbc0TAAaYZpXQbXdnc7z44rlo_tZLm_M9tkcCKB6aL0imCahTVOi0BBWRbcUcwV2o4cm40ye0tWO_-ANl2aNcJNAOCqlKob5s5Dc75fLnqUKmJbN7yUmNYSGPHZMkpExLVp1uooteU5-geYLA_lFdPPVCZexo6J0lee33YfwGSqGxhsGhBGR-s4omGC30AQvHeAglKDqF2zVfku6C_f-37UUtD9zPKylo3aa_CEW0FCKc7-pLF2djBS6NWT_GNxBaFIz3lfjh4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16611" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=K_KJtzr_XryJ39Bts09BCX3enugB9sNTmuOmxUxaP3CmI-BD_Y67FUcydB4kHWvJE2aa4vT7XqL8jjl1S1GVScVwh-U_-viAVH6bzMyw8IsLs5jjd09ys4Q2VWm2e6kNCbowIRXZKInqHbii4xKIJSzRKb4OA8-qOZG_PpMioxRPnG_KnhdbSSu6bgYqRUz0yHIMvtOvdqiUJy4zksET-TtAvcPwe1ymVC27tPhvDDEhjTY-5DAkH5jfNZ2jE-PjhzFWDmg_2NIQd3pMSm0IgdMOVlZ8LRv1Rfh4H963SPU-S0vIJVeY0wuSJT_dZNeFpFgh_9-m61yyZrJ1gcxvjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=K_KJtzr_XryJ39Bts09BCX3enugB9sNTmuOmxUxaP3CmI-BD_Y67FUcydB4kHWvJE2aa4vT7XqL8jjl1S1GVScVwh-U_-viAVH6bzMyw8IsLs5jjd09ys4Q2VWm2e6kNCbowIRXZKInqHbii4xKIJSzRKb4OA8-qOZG_PpMioxRPnG_KnhdbSSu6bgYqRUz0yHIMvtOvdqiUJy4zksET-TtAvcPwe1ymVC27tPhvDDEhjTY-5DAkH5jfNZ2jE-PjhzFWDmg_2NIQd3pMSm0IgdMOVlZ8LRv1Rfh4H963SPU-S0vIJVeY0wuSJT_dZNeFpFgh_9-m61yyZrJ1gcxvjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا توافق در حال ولی خب شدن است...</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16610" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ
:
اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مثل معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و راهی واضح و باز به سمت سلاح هسته‌ای داد. معامله ما کاملاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره نشده است. پس به بازندگان گوش ندهید که درباره چیزی که هیچ نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من باید سال‌ها پیش این مشکل را حل می‌کردند، من معامله‌های بد نمی‌کنم!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16609" target="_blank">📅 21:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGAifvsXey59myliVt0Uz2LelYN_vY94vBl21D5U1boXBzH_0091K_qEs32IOWuhZO_v-rspzfhkyeI27joOWJ1vbYGpSOK8hGyHMf0XzslbYCbF28yPfaH4iUjz8Lk5qnyg85PRfma5MwVJHoFNScdcH2zdC_vuhQfrQbc0_GL_qEfC3I3C4VF0fswSLN7sXTXtuI40xmD2xvXhVkHXzxv_duV80GqIa-Q7KhrHCgDt_NFqjEH6-gKAdNOaoUBFrWHykXE1yh6ZtLvUYh50DvDLTFYXJVkc8otjLx6cLZGkRdWDH0l15oqdzMjuTIMVoFeL2AbWDUSrzD5oG84Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16608" target="_blank">📅 21:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uthlhmiPVU6Xc2t3MEbNPXqugScUpERPS9q9EdgBJYz1nMQzqvlcdYKYt3iCJENSt1pqBv-tb9-_a3jihY_uml6H_jm4NzNmVW37VzpgUdwpMSOVEegdgEkLe299z6B2HxSgi_Bq8poQhAG5K_T5-w-urWU5gwPgxdUEKJkqzt0C_Pv3Za_Q4ADUg3CXzrAKisSsnrUoaBt5XYQNsi_WeQgyGbDOVOZelZG8L40V9mdLf0O2G80AnSiz8B9Pta1b8Ph7OGTc79u8gNEfr_cQH_gY80fape1M7sDgZ-r8wyzX_L_AiAeVg1nakzbjsVPw3uOyGIV-T-nsXL9XTTKU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16607" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16606" target="_blank">📅 21:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«ما آماده‌ایم تا بلافاصله به درگیری‌های شدید بازگردیم تا حکومت  ایران را تضعیف کنیم».</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16605" target="_blank">📅 20:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=o-ichGy_mcDBDwPCZYS08qlbdUzHdym9NRN5LMol5_n6PN4d2EPQP55cY-IYW5bwm3kqN3Yi08jxp3gtVLtdu1xBJaGFo-4W1_38E2QKrMIo_mq25bpDSZLXf-hPHbbDU113eFnVFljbFSH2eM7bi3gRYaOLnEV8CjMBXmWX5gRxTFGERDi3VD_W20FFUdh7Ke48ZKv33vQzx8HojWUFDVVZXbWw3jydOtMJW9gTvlEhfqr5etH6fo1oTrB-y6HjhSwVEiMLhf85VDrickeiC8C70jEjZfuO0u3sWRyjogCBo4LJxwaQ8u_lXMBN8jLK7whqYEXGY_ZdgtRN9b5wsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=o-ichGy_mcDBDwPCZYS08qlbdUzHdym9NRN5LMol5_n6PN4d2EPQP55cY-IYW5bwm3kqN3Yi08jxp3gtVLtdu1xBJaGFo-4W1_38E2QKrMIo_mq25bpDSZLXf-hPHbbDU113eFnVFljbFSH2eM7bi3gRYaOLnEV8CjMBXmWX5gRxTFGERDi3VD_W20FFUdh7Ke48ZKv33vQzx8HojWUFDVVZXbWw3jydOtMJW9gTvlEhfqr5etH6fo1oTrB-y6HjhSwVEiMLhf85VDrickeiC8C70jEjZfuO0u3sWRyjogCBo4LJxwaQ8u_lXMBN8jLK7whqYEXGY_ZdgtRN9b5wsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
ولادیمیر پوتین جزئیات جدیدی درباره عملکرد موشک "اورشنیک" روسیه اعلام کرد:
🔶
کلاهک این موشک به دمای ۴۰۰۰ درجه سانتی‌گراد می‌رسد که آن را به سلاحی با تخریب بالا تبدیل می‌کند.
🔶
هر چیزی که در منطقه انفجار باشد، به ذرات ابتدایی تجزیه شده و عملاً به گرد و غبار…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16604" target="_blank">📅 18:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">-طبق گزارش آکسیوس، یک مقام ارشد در دولت ترامپ اعلام کرد که امضای توافق امروز مورد انتظار نیست و هنوز چندین جزئیات باید حل و فصل شود. هنوز در مورد برخی جزئیات رفت و برگشت وجود دارد، برخی کلمات که برای ما مهم هستند و برخی کلمات که برای آنها مهم است،»
این مقام ادعا کرد که سیستم ایرانی در پیکربندی فعلی خود به سرعت حرکت نمی‌کند و برای طی کردن تمام تأییدیه‌های لازم، چند روز طول خواهد کشید تا توافق نهایی شود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16603" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یادداشت تفاهم آمریکا و ایران، طبق Axios:
تمدید آتش‌بس به مدت ۶۰ روز
عدم دریافت عوارض ایرانی در تنگه هرمز
ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد
آمریکا پس از برآورده شدن این خواسته‌ها توسط ایران، محاصره خود را پایان می‌دهد
آمریکا برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد
تعهد ایران به هرگز دنبال کردن سلاح‌های هسته‌ای
ایران متعهد می‌شود مذاکراتی درباره تعلیق کامل برنامه غنی‌سازی هسته‌ای و حذف ذخایر اورانیوم غنی‌شده خود برگزار کند
آمریکا متعهد می‌شود مذاکراتی برای رفع تدریجی تحریم‌ها علیه ایران و بحث درباره دارایی‌های مسدود شده ایران برگزار کند
آمریکا هیچ نیرویی را از اطراف ایران خارج نخواهد کرد.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16602" target="_blank">📅 18:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دونالد ترامپ در تروث سوشال:
یکی از بدترین قراردادهایی که کشور ما هرگز منعقد کرد، توافق هسته‌ای با ایران بود که توسط باراک حسین اوباما و آماتوران رده‌بندی شده در دولت اوباما ارائه و به وجود آمد.
این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. اما نه در مورد معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است - دقیقاً برعکس! مذاکرات به شیوه‌ای منظم و سازنده در حال پیشرفت است و من به نمایندگان خود اطلاع داده‌ام که در آن زمان که زمان به نفع ماست، به سرعت وارد معامله‌ای نشوند.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت و اثر باقی خواهد ماند. هر دو طرف باید زمان خود را بگیرند و آن را درست انجام دهند. نباید خطایی رخ دهد! روابط ما با ایران به یک رابطه بسیار حرفه‌ای‌تر و پربارتر تبدیل می‌شود.
با این حال، آن‌ها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه یا تهیه کنند. من می‌خواهم تاکنون از تمام کشورهای خاورمیانه بابت حمایت و همکاری آن‌ها تشکر کنم که با پیوستن آن‌ها به ملت‌های توافق‌نامه‌های تاریخی ابراهیم، بیشتر تقویت و تقویت خواهد شد و چه کسی می‌داند، شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16601" target="_blank">📅 18:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.  به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16600" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSirus</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAkl89-azhSh037B_oeiKRjUctmRgPnlccCqYY0knPJ2g_Ig72VAXgG2wAGSK8a_GDIkY4Cq16kVt4V_2WQUH65Ei1orxo5n4Hn2_klu-mPR775AU75tLaG5juLfWD6zWq03CWJ2Tu0KRdoQb947KJRuJq_A2kwT6onCZwh55_tY5LeloXpSem5oWN6p_xfQrUBS6JMBjUMentmlZPNVjBHX8ojsReiK7cNZmcAr3MgRE4UXbZMJojn829xoq5_JpyCRBTpEeVoumczWo_ZXSlo7v5rBab3H_TDx5BiGFjYA_Wv0D_274zuYkG9h9LKfy_t5PL7AWh_rTrpXl9QqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر چقدر مظلوم بود و هست، چند سال پیش رفتم و هنوز آثار جنگ با صدام باقی بود!
یاد تکاوران ارتش و نیروهای مردمی گرامی
و یاد زنده یاد سرگرد خلبان محمود اسکندری و کابین عقبش ستوان اکبر زمانی که با انهدام پل اروند عقبه لجستیکی صدام رو قطع کرد و مهمترین نقش در آزادی خرمشهر داشت؛
خرمشهر را خدای محمود اسکندری آزاد کرد...</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16599" target="_blank">📅 15:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسئول اسرائیلی:   ترامپ به نتانیاهو گفت که توافق نهایی با ایران منجر به خلع سلاح برنامه هسته‌ای و حذف تمام اورانیوم غنی‌شده خواهد شد</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16598" target="_blank">📅 15:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16597" target="_blank">📅 15:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16596" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16595" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.
به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق یک مکانیزم آزاد سازد، اما اکنون از هرگونه پرداخت از پیش خودداری می‌کند.
تسنیم هم گفته  که اگر مانع‌تراشی ایالات متحده ادامه یابد، هیچ تفاهم‌نامه‌ای امضا نخواهد شد.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16594" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر حادثه تیراندازی چند هفته پیش در آن سالن را هم حساب کنیم، ترامپ دو‌ بار خودش مورد سوقصد قرار گرفته و یک بار هم افشاگری درباره ترور دخترش مطرح شده!</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16593" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16592" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16591">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
اعتراض نتانیاهو به دو بند از توافق ایران و آمریکا
🔹
نتانیاهو جلسه‌ای در مورد توافق احتمالی آمریکا و ایران برگزار کرد.
🔹
به گفته شبکه تلویزیونی کان اسرائیل، نتانیاهو به ترامپ گفته است که نگران دو بند از این توافق است.
🔹
یکی از بندها مربوط به آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16591" target="_blank">📅 14:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDFhPzajbscn8sd0z7iHb5CyTtNvbqc_HzGzchnAD6j8iGhiU4r5G9rRsYsJBL9jx_R8SM7yTadsWTxUg0jeM1rgQDl9P3h2RQQ7LijzE6Q54qazQV3Ezg0u6sCSuanxbRq5uBLFUN8cAzD5D41vmsUQS0PhYUBvrI8Fo73T5F5kwEaO24m4ACFGlDshBrDfhy17_kpR5b3CaS-tXH0fnQ2f3q_7eCSm_CfsRu-aAHFAmJRAYG2YWHZCNojev876jNOHmGvGSLp00CqIBdBgKvHns-_XMGyttNz5PAJFrOnVfdHEYP2VoCp_SzNwJCofDfBykR9Pd8ur3hPTfhHc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16590" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16589" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک مقام ارشد ایرانی روز یکشنبه به رویترز گفت که تهران با انتقال ذخایر اورانیوم غنی‌شده با خلوص بالا به خارج از کشور موافقت نکرده است.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16588" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
