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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-16699">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SBoxxx/16699" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16698">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">«مسیر ترامپ»: وعده ساخت از سال ۲۰۲۶  وزارت امور خارجه ارمنستان سرانجام زمان‌بندی مشخصی برای پروژه TRIPP اعلام کرد که به «مسیر ترامپ» معروف شده است.  طبق اعلام وزارتخانه در پاسخ به درخواست کتبی SputnikARM، فاز عملیاتی پروژه از سال ۲۰۲۶ آغاز می‌شود.   راستی،…</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SBoxxx/16698" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abCM1U8oqoKzHwwKb2iDeVj5RncgyZgyy8IokUdBR0q7TgDygv2KvqfB3EniH2ZEim0o5l5lRwKcNDTmxgxvlcXcsxXdDpWo3qlLKlTOIosc5axuAqDKC4yqx1ztkAsbzIBw4v2T5bVkVoqVtQb93Rq94vLQ0lRNVcbdyNnndAQZZ02izU-oivLYeVhFGEYv1kp6-eoRhVgHZ_6ZKFU1ztqRLcru6zWbY75Ue9BT4bj-Vlo1K3SePdHb8U4vWEtRrf3rr4ZNbcHVPbnv71Tmj2W5cxS6Cheg20AsCrhLe_-TEyitFSYgyMc4txsR_EAeJhB5lwr895WhVheuB-Uhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/16697" target="_blank">📅 17:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایالات متحده طبق یک نسخه غیررسمی از تفاهم‌نامه، متعهد شده است نیروهای نظامی خود را از مناطق اطراف ایران خارج کند.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/16696" target="_blank">📅 16:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.   این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16695" target="_blank">📅 14:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
  <div class="tg-doc-extra">162.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/16694" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه
مقاله Israel Hayom
درباره علل ناکامی عملیات نظامی آمریکا و اسرائیل ضد ایران</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16694" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nArV3gVGtpkbq-5Hqw7mCmDbfSc94dGKG6kHmKWng_FjoyD2Vo5azt-w0v91oZuZL90SJ0bK9Y73uC6YZwZavwD_S8M9C7J_mjNnxzSIUJWl2G1BAhfIxNlX_0T9oW9xZQzqJFLYCvI1FyZayih0uQ3UDiZgzHmpFrAOQKWGX-3-GuD90RPD0ladd7jQYxawiWpAwN4JPMSJGrHSW_QxHhRvBcMk5qMRzaPbCwXTGWAptsBchUrDzPZlwMqYplBTynmODG_dI2s79B9Swwo6dl_meLfHaJB7Q8ywninQ4GKshtz94ebHPEvgpKOFvSdvQERag9jv3ojMrLSnU1cq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گوشه ای از قدردانی کاربران روبیکا نسبت به مسعودپزشکیان پس از بازگشایی اینترنت بین الملل:</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16693" target="_blank">📅 12:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کره جنوبی قوانین ترانزیت نفت خام ایالات متحده را تسهیل می‌کند  آژانس گمرکی کره جنوبی دوشنبه اعلام کرد که رویه های قانونی واردات نفت خام ایالات متحده که از طریق کشورهای ثالث به کره جنوبی ارسال می‌شود را تسهیل می‌کند تا همچنان واجد شرایط بهره‌مندی از مزایای…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16692" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16691" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3ahSC7vliI4zVff7HezD49N-aCV2AO1o7dlo1dW0xyV-0wIlHTN9t-YBixC1kzNecd1AsqbHJipxkh3DpS2MpqWNCRvpYbd8Iv4rYrqvs7WTtlF_Kt8AQ5u1I1Bi490DLNYsTZwzeJ0CIUDMnC8uef_qYzIHSBgUdVAY3qkorYY1-QJlsIRuJ-RB5M7BrjMLMlfHwt3Rx48vnHZ3eV72qHrTNiPGepOWOyiAHSiIOZdhsva7e3LFqRLZhqiJ--ycr5O6yQz5WYc1GCzJeaVVn0Zbt-JYPPODLrzkyGP_7fCjmKKsI2ucFQIPnb8v_cn2uTS2kpAokP5igAOmM6o8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.
این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر رهبری مسجد و خطبه‌های نماز جمعه را فراهم می‌کند</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/16690" target="_blank">📅 09:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpznZ0PJv8I88cyAnqQnJGuwHC65B3qQq9Y1n4JGPz8PHlHZyoS3kREVyrqfU8n1ejoH-boy-iDcZFy17Ku3kh5utRRLuHxl0RN8BZqCFowQHaWKh9NRkqZPPwc_azJvkk8N7djehMhnhUBO2jHcxm9fpWBaDVt0Vv-McluTOcczc4HpxS2dXkbDYsTJnjYXjQ5HFgWU_WRxOlIFDKE51wUKO5pyOGhs66mVu4NZufbJta7NaEphIrJLQbyx4tSJGFRiuWkGRAUuJbSfog05sAaUDO-ANpZzuSSieNSBbxWCEXWGy62-JUV-vvXyFY4swrmcRgv8lLqPG1-KdQATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه در حال بررسی محدودیت صادرات گازوئیل و سوخت جت است، زیرا نرخ پالایش به پایین‌ترین سطح چند ساله در پی حملات فزاینده اوکراین رسیده است.
به شرکت‌های نفتی توصیه شده فروش فرآورده‌های نفتی به بازارهای خارجی را محدود کنند. تصمیم برای ممنوعیت صادرات گازوئیل و سوخت جت در مراحل پیشرفته است اما تاریخ آن هنوز تعیین نشده است</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/16689" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANiJz_TMv_776ncPFx3qIJWl9XE5cbdC3opPtNECaQ6MVQ6s1mV6H3V7RMOOfZoae9_EWeL3QKgoBVq746tO6u_1jkD9JQ-sW3YicWSxzh89hNWJsbVDiBgJpM_m09FRwKmJRauCAoQXBgbZyTcBPDg0wOIr719GsKdhCazSozWGznCzK91GamQW9xLIW0rWyWygiF7iFAefT98adovbGyCI42bpYmMKvcGq7EmusfK87PlNd7LKwQOueUMamxbQQxPvTt834_eWSUThCeGevrFyKYkaZuB5Ts_JkJ9Uuj53lBqNLGiuGueVp2CArdGEj79mMAzgQAmbeN8n_2_axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از درگیری‌های چند شب گذشته در تنگه هرمز و اطراف آن، احتمال ازسرگیری سریع ترافیک عادی در این آبراه حیاتی در بازار شرط‌بندی پلی‌مارکت کاهش یافته است.
اکنون معامله‌گران احتمال بازگشت ترافیک به حالت عادی تا پایان ژوئن را تنها ۴۲ درصد پیش‌بینی می‌کنند</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/16688" target="_blank">📅 06:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe37KNf3E9S9X8otHncLS975qaxzbNh-QTg36IJLbsHHUAO8HsQdJ8ISty64Uq4TUNEFPKADNcs0OBhKWmeOenfW-Bp3gs_CUZb9DxrCT5OuLFw4REDsXRiOruFMwwxUH12mZTISpJRBekc4dBUD8ixy_EZwurdm1Sm7I6tI8WiIrWdUb2P863nFoMPhtJv6d8lXmDibluBad6CpXs-fUioXg7rqLjtHHuYazHY3PTF6OJlGUJPt5VgvV7twGeHzCdRDcVNQa3-Nc2kcIb6Axf3yCwBmQ5BoaWOWymZ1RRCA0aWuK7705ErhYuZqLJY82eHL13dOPgasJf8sst-PaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/16687" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/16686" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZU8axwjJWuHbzyI3_OXXujUE7XWUOMjVjp8Dwv1YMvV2f_xLtfjNPgry8mMrpGGUvow6kpu0q663FUKRRjGGJa27i8ktaQOpJdGfIIz7ZjKCOMB7Thk6zEwZJxVteAuYDYSie7H_Eaqn6X5PdMHuF7dp_ATSW6JWv9kPJhym2kTXGIFD50wI2rkpNbe1k6rt9-6eQYjZt_FUBMmvPvDlcw5rpx2ZD8k4pTpwhwE3A7CNHKiNq2Xl_aWrHLdseMWsEIMoaJLSZacqEZ0jEDo1whaQ1DvGZmVklJpUNJB3UM2Y1mM0ft165PBgaZwuqFq5KyfRiICp6KkMafCOxhYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه پدافندی کوتاه‌برد ایرانی «مجید» در رژه نظامی ارمنستان در ایروان به نمایش درآمد.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/16685" target="_blank">📅 22:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=GmqthPQDbz_A_EcyxL0wsQj4HuF9qcbko61QjiayqfG5J9YyQtVTtvfR48cmqwSxfGoXwC51f94oEzqHFRTxrB1ezus3B-1hZv84PCte_Muv5mYN4URwkmg32HjW1vVWMjN4_I1dMjct8rvEBYiZFv31Jf4xfwF4P3owAuuknzuC697mmgNbyQ8bkiQZIcs1o3eP1qW7bAzscFbjXC3rzBEISosWJkOvAaVgfkBIqhxbExOXTUD4WSHkl14LdmIvzjzgkFASLbM7sPld9Zlu8Q8vnnocf9Mk7Tfcm5RBMxSvHSg-Fljc1f3udH0SQwv8MYwaZ4HcYcmo69pDKxky4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=GmqthPQDbz_A_EcyxL0wsQj4HuF9qcbko61QjiayqfG5J9YyQtVTtvfR48cmqwSxfGoXwC51f94oEzqHFRTxrB1ezus3B-1hZv84PCte_Muv5mYN4URwkmg32HjW1vVWMjN4_I1dMjct8rvEBYiZFv31Jf4xfwF4P3owAuuknzuC697mmgNbyQ8bkiQZIcs1o3eP1qW7bAzscFbjXC3rzBEISosWJkOvAaVgfkBIqhxbExOXTUD4WSHkl14LdmIvzjzgkFASLbM7sPld9Zlu8Q8vnnocf9Mk7Tfcm5RBMxSvHSg-Fljc1f3udH0SQwv8MYwaZ4HcYcmo69pDKxky4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/16684" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
فضای دیجیتال ایران ، پس از تجربه طولانی ترین خاموشی سراسری اینترنت تاریخ مدرن جهان ، از امروز به صورت تدریجی درحال برگشت به حالت قبل و فیلترینگ مدیریت شده است</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/16683" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/16682" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/16681" target="_blank">📅 19:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16680" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب نت دارد وصل می‌شود و اساتید بزرگی به جمع ما بازمیگردند
سبحان الله!</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/16679" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند. @TasnimNews</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/16678" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری تسنیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=BES_4Bd7jHWUh_Qnnb1a2VwFniHEhgib2uHhxkNDJslzAlhurgfS0vnHS_3SkQh0jtkgjmdYXp0UQLwtebH1-2_It-W8Bayak4dGaGRp1pRs1XQ4i0A6MvU-pYiUufmb-NPD6UfLghcruvlMNU3rIPgQFpB28baTFgvcXh8ojDfSuHEiFOhUPaW07OpKsiPxZ_tGbk8y94QfACjchxVmUGdsKonkGGSS1i_LbKatarVpZmKp5ZlPhvy_-LSNRaouIHoLx0MHv9q195t-HN58P_-Kt9CBu-7ztz5wc2aTcQvZOPfxva2BHpOpFM4kvsvLWhD_P7b5yd4lv_c4sR577Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=BES_4Bd7jHWUh_Qnnb1a2VwFniHEhgib2uHhxkNDJslzAlhurgfS0vnHS_3SkQh0jtkgjmdYXp0UQLwtebH1-2_It-W8Bayak4dGaGRp1pRs1XQ4i0A6MvU-pYiUufmb-NPD6UfLghcruvlMNU3rIPgQFpB28baTFgvcXh8ojDfSuHEiFOhUPaW07OpKsiPxZ_tGbk8y94QfACjchxVmUGdsKonkGGSS1i_LbKatarVpZmKp5ZlPhvy_-LSNRaouIHoLx0MHv9q195t-HN58P_-Kt9CBu-7ztz5wc2aTcQvZOPfxva2BHpOpFM4kvsvLWhD_P7b5yd4lv_c4sR577Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند.
@TasnimNews</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/16677" target="_blank">📅 16:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nM_u_xqpHn0HwjGhyyqczDYe3MruF5RCqFaCwzY3gUy9meyFkMPs5WYNc57xwi7UOOl1ZWAuXiTB_2Ok_NMD1f1xTrDXlDx7DLYgIaUAh39QV1iY2NXe2zLbmpvVzcZS8KCKfnigGw0RMppOtt6BD2PFZShNQ1r5GsovcUpvWlwymmSfzul9IRFk-Jhm3w3uAViIkxRsdNtrtHdQdh30wRH4gyaaqtuvNjMM1G28hCegpzV0gi_6gpOyAliGHlKSyOVFt0pBYdiEDdSnwZu60WrfSSiczE0YrBCpUD3frNItLQR-ha-lDd9ExJUomwvw1cjtq7ypB9TYsLNsin9wmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/16676" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/16675" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IceeP2Slnj1Hr9kbRWcNKcrTQttAN95gIuAssuaFshWYrIOIXUxvHBZTgz_jnQED43IaQwxIZaJgCLiXqxYOII2jbKiCJN4V4qNt4T0fTyQvTDI0bvbnt4EV7vuLku-KZaLD15I4aTRyN07roP0H9cPTFIGgjbemYpzZQO-EtvotID_Z0XGNJ6eeV3EAqm-svX4gJe68oVAQ1LZZm1owdLYnlySyTmAIzOi_jxjx2tne9CdiSbq8QiSs6fbsCsgkAf9OJrl2XY92iMRAsE7SqWyGoNyMAbcD5xjzxNCSz2947ipL57fXo3hL9P8tG925wN-hLD7JWHoDNBqh3QhG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/16674" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/16673" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMsd51U_CPzxySX2LCdjl43R9qTHnLgLZ1jNmQCQkEEBF03h67D3AJhy0xBVXDUi1lrkKF4AH3sWZZ9Z4BkYDCo0AUJkwQr7pnnOC_k1I5g2H6WvxgJO4dvxp-21fw5qHCdSx_4ZXGjTzsQpYLCKQJysc6D46aOAzg8h5xyNmjt-H-rtXTFq87kX7vlRs6nf85WZxfyNwmNXoY33ae2sy1aVa9tY1UvVhvEkY_GZW5PCV-Cg5SmEKLYC_OrYos0u9Z2l3xczcos5iijTqlQOzZURWLDUtXbGtCwiaMT9OyWtRht809_Kb-_Z-3O4YRc0gLVScCJSEwc_N8mbD9Rnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کوتاه روابط عمومی سپاه از درگیری‌های روز گذشته در تنگه هرمز
🔻
ارتش تروریستی آمریکا در منطقه خلیج‌فارس در ادامه ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای دفاع از حریم…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/16672" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153170738b.mp4?token=odibX11-bCtj98URIrRLwqnj0Hh0ANCQVIjszVyboSSes6u5xTVC-8fB7L8NRCCFwTyQ9T1DutaHdWu3CfTow-G22a05h0GnIOzmmgTip5nfQeEh3nPzzQVKDmj74Bt9qNuMSESaw53Zo4pCadiqXiGW2orBc1s5ME5HLdjfDZY1UhPhw3AD58cekw8G1RXV4Yu1twceR8cBDRBwxglfZETN2T7DitfPKrwhsqj_Ls8wGK8ymAFhfg897ZpPCESacYXqEDzFTduuQY4PzLoeFnIhcLkZ5hPhzvy0bp6lvAbWqVhSuc_5tX7rCbbKSRsb5iM7VREDvb84NZHz8uVzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153170738b.mp4?token=odibX11-bCtj98URIrRLwqnj0Hh0ANCQVIjszVyboSSes6u5xTVC-8fB7L8NRCCFwTyQ9T1DutaHdWu3CfTow-G22a05h0GnIOzmmgTip5nfQeEh3nPzzQVKDmj74Bt9qNuMSESaw53Zo4pCadiqXiGW2orBc1s5ME5HLdjfDZY1UhPhw3AD58cekw8G1RXV4Yu1twceR8cBDRBwxglfZETN2T7DitfPKrwhsqj_Ls8wGK8ymAFhfg897ZpPCESacYXqEDzFTduuQY4PzLoeFnIhcLkZ5hPhzvy0bp6lvAbWqVhSuc_5tX7rCbbKSRsb5iM7VREDvb84NZHz8uVzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرامزاده پول بده نیست بیخودی امید نداشته باشید</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/16670" target="_blank">📅 14:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16669" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.P</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=iaB3D-CEJqR0gefn7P-ck8vaNJ4YVtG-DEND6oQof4tyTWjgWXq-zlIXJ42MwQaxdBzKAoR9XioQiI61jrGA128EtZeMtsl_BmUkuc2tG2-rChg2ESKLULrDFdzGQG5x1NaNI50rIwypRgSCo6pLqqvY_m6gf2oGGEsdYAlmjc8GRrmOe9paB8sNCoiRMYbYS7AxCaGA3GsHeysLsAMmcV4zIOcadBZq-t5sPRsLhK7sft7KxVsNp-ZHoYbfBFYLWPDUDRqfN4Gr9Bnz0N3iYt_zGb_RuqtdkhO93S9TyZIXtwB0TtShCdiCunDrrEnCKhkO2oZ8tGbaixxxF1xmmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=iaB3D-CEJqR0gefn7P-ck8vaNJ4YVtG-DEND6oQof4tyTWjgWXq-zlIXJ42MwQaxdBzKAoR9XioQiI61jrGA128EtZeMtsl_BmUkuc2tG2-rChg2ESKLULrDFdzGQG5x1NaNI50rIwypRgSCo6pLqqvY_m6gf2oGGEsdYAlmjc8GRrmOe9paB8sNCoiRMYbYS7AxCaGA3GsHeysLsAMmcV4zIOcadBZq-t5sPRsLhK7sft7KxVsNp-ZHoYbfBFYLWPDUDRqfN4Gr9Bnz0N3iYt_zGb_RuqtdkhO93S9TyZIXtwB0TtShCdiCunDrrEnCKhkO2oZ8tGbaixxxF1xmmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16668" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnFjNV55gPA-FZ_DbwizblLCoJu63H19gbWCkZ4cSBYrE43mrqjL9IJEUD52Pc9geuA__K1gXroWazF_bu61pSaSRhoNWf38b1GTkAOerOy6uoGTBZucMJlqILZaor7mbDbn-Y31ex4oIHovpE5URh1I7PKl-bikniWUGLl_SedcfW_DEpgaPY-IyPyRWEtfrRXZMNU7cpVeEOq-LOg6sEi2YT2qsiAGa3H1rkHwvhUNUTP3rXnRdlNmkl_m-dJFAXkEeZsKuAKu5k9J3BiORbvZuzeFrL5UGKZGLUiWYPNq3e8pYlXy6SfKiGuvG_xlZjmR_rECxCJSQkKTuzZtwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ مثل این بستنی فروش های قرمساق استانبول است که پول را میگیرند و اسکل هم میکنند و آخر بستنی را هم نمیدهند</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/16667" target="_blank">📅 13:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd1YgemTj57bnB_UfhCN-CxjjRaVaij2Xd2Xq4uXEaMjGo97HhRBk6_4fbE7dl9YjUTtOA9bnqJK8zbdyVC3BBvtltGXH5_fnqAPA1szemlcHBj4r51NkYeWkNJv1C68hyWteRmJHkRrg64RshlxB5ZRzgU_rQ8YphCXBwZsC8qE17ofsqSFR0wCXKWFHsgzm65OIG09LJ-bX5QqbAUUhQo_xHR1l7ou_yxaaFm9gSBlh70zj8wRLIGXCrtphxLRjCeU_ia8IQZrRyK4VcKbuYA85ZKtdd0sJoDoe-i34d5kzd76VgGaDUPcdkN1JkO4t8HNSURxnYl6eo1rwnyEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!   بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16666" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16665" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کم کم دارد نت وصل می شود!  نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/16664" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF-xT8BXp0k4EpqUgxlcqBYbaG2aKp7Z7THMA7uIbmgG0bQyIUr40AtYIBsPfyQltZ8uO6tAAiBdC5egM3rJBLA1EPgZbbXjl38kzqOsl-6dIjhu-XroxnJM2y4h_lpbWRrc09-7ayhye4N0pOfelVporA69MRZma-rsB8DAAqzXrZM7KQtfrjtAUAlvtHfdbGiVuay8qe1mjjvWk1RNB5FnCr5e_7D_ISKVzZWFRZoQHzNVVpAbRtkztRZI-zHwHFmBJDFzks8jInNe90j4ubaLtuBEIlWzbPdL0e-Rj3-FTiKueWcDuN4XsNQ0mNBlt0rUT7QYkdNZIoHG9LQH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
پاپ
:
هوش مصنوعی همانند سلاح هسته ای ابزار سلطه و مرگ است</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/16663" target="_blank">📅 12:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کم کم دارد نت وصل می شود!
نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/16662" target="_blank">📅 11:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سبحان الله این چه وضعیتی است!  یک انفجار روی می‌دهد تا خبر انفجار قبلی را منتشر کنند!</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/16661" target="_blank">📅 11:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتش اسرائیل آغاز بسیج سربازان خود را برای تشدید عملیات‌هایش در لبنان کرده است.
نیروهای نظامی از سربازانی که در روزهای اخیر مرخص شده‌اند خواسته‌اند تا فوراً به خدمت وظیفه عمومی بپیوندند.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16660" target="_blank">📅 10:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خاصیت موج  4 همین وضعیت ابهام و سردرگمی است.   مثلاً دو هفته پیش ما تقریباً تا آستانه ایجاد یک فاجعه هسته ای با زدن نیروگاه امارات رفتیم، یا آمریکایی ها پریشب قایق های موشک انداز تندرو و پایگاه پدافندی را زدند، ولی باز هم نه تنها می گویند آتش بس نقض  نشده…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/16659" target="_blank">📅 09:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فکر کنم موج B از ۴ هستیم  از توجه شما به این موضوع سپاسگزارم</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/16658" target="_blank">📅 09:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار الجزیره نوشت ابتدا سپاه پاسداران به یک کشتی در خلیج فارس حمله کرده و سپس جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را هدف حمله قرار دادند و چند نفرشان را کشتند.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/16657" target="_blank">📅 08:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3mIRuk65LOevSDLjiLMoFgze1JvZ_ESipiWdKSi2YCbxCK3UPLKMMJvPeq0fDSEzx55ogtzHeqk9cAyi8LbuV8Qv2En6JOweb91gTF9-Na_IHy5NiM36piEMRGw4jPIQSG51M_z993QpXFuXCA5h8ta6N3qYhYs_YGt3uF1IqB4owSyEeQq_E8OOmybL3hPM91rLAVXMuqR-Tdcs9R6-0O9z2BzT5EV1iL4y1T3RPS5Uzg6VSYtEu7U5nTTm5Ay3IBOLxMxPcAjQ7E7304AB1NxWVoKne2-MlhiciwvRpr7NodycLitUJDLdgJxUz91VeMjOc3GL67xu41kgvGsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت های متفاوت مقامات ایرانی و آمریکایی  از روند مذاکرات از دیدگاه موسسه مطالعات جنگ</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/16656" target="_blank">📅 08:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این مجری را خیلی دوست دارم؛  اولا با وجودی که نصف شب رفته یک خیابان خلوت تاریک، ولی لحنش جوری است که انگار دارد فینال جام جهانی را لایو گزارش می‌کند! خصوصا آنجا که اشاره می‌کند به «موتوری که هم اکنون از پشت من رد شد….»  ثانیا در هر اجرا، تقریبا ۱۶ بار اشاره…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16655" target="_blank">📅 08:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وضعیت بندرعباس آرام و عادی است
🔹
استانداری بندرعباس در حال بررسی منشا صدا در این استان است.  @TasnimNews</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/16654" target="_blank">📅 08:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16653" target="_blank">📅 07:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew0SphGqhLp8dyCThfdSxJMiAfd2SpC_2wnmDefbuBKrnzyZwM1Qs_tYNAkR0VMTJrZwZGNI83uwZZSphSHCQuhlldbjjzqERHDSrqRfiCVYdslBYZlAXMDY9cc0aCOdz85HWCOb2hFuJRssR3CFJ8HBHgZ4y3VX6sRGv2nwSjXMqDwZN6Urf8VxNquUMOI9RmA39VxFSLVk-sQT0cS4rawKI2VcVgX6aIwM2CcK9_npzm7ab5OTjj0Y03jxLU4wEX7ewHMZZJt4T2rufh2kWXtx4GVuQllGaAM3rXsvPiJ6Bcb03iswHkIl84bwr9SRQbLTBYkJn9e7l7ILyt26Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ننگ بر سازشکار!</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/16652" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شما خونه تون مورچه داره ؟!</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16651" target="_blank">📅 01:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار الجزیره نوشت ابتدا سپاه پاسداران به یک کشتی در خلیج فارس حمله کرده و سپس جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را هدف حمله قرار دادند و چند نفرشان را کشتند.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/16650" target="_blank">📅 01:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل عملیات «پیکان آتش» را ضد حزب‌الله تصویب کرد.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/16649" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/16648" target="_blank">📅 01:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سبحان الله این چه وضعیتی است!
یک انفجار روی می‌دهد تا خبر انفجار قبلی را منتشر کنند!</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/16647" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هدف قرار گرفتن قایق‌های سپاه مربوط به ۴۸ ساعت گذشته بوده است
‌
خبر هدف قرار گرفتن دو قایق تندروی نیروی دریایی سپاه مربوط به ۴۸ ساعت گذشته است و انتشار آن به دلیل جلوگیری از فشار بر روند مذاکرات به تعویق افتاده بود.
طبق این گزارش، این حادثه ارتباطی با انفجارهای اخیر در بندرعباس یا جاسک ندارد.
تاکنون مقام‌های رسمی ایران و آمریکا جزئیات مستقلی درباره این ادعا منتشر نکرده‌اند.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/16646" target="_blank">📅 01:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری مهر:  منشا صدای انفجار شرق بندرعباس بود/ اوضاع کاملا عادی است
🔹
دقایقی پیش صدای چند انفجار  در شهر بندرعباس شنیده شد.
🔹
پیگیری خبرنگار مهر، حاکی از آن است، که منشا از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/16645" target="_blank">📅 00:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/16644" target="_blank">📅 00:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارهای مهیب در اطراف تنگه هرمز شنیده شد</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16643" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به نظرم استاد رسایی هم از گشایش فضای مجازی سود بیشتری خواهندبرد تا اینکه
در بله و ایتا اینطوری از عالم واقع بی خبر
باشند.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16642" target="_blank">📅 21:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-9OGRWlfPSvG_odcDFaep0VQ04qnUY6A14dOm5uenNWmMa0vMVEQ-hD5JNuxlD0LMyIS34UZEptj2UWJX9nCq4PjSvDFkLWhUPemzR87bf_h4TBFcJwMDn7l8buVydJqK5eIMTR7x0Gki8MJcwy3osunf2dNaqjD7MrlLd9uSDj0asDGMakMV5LgTOVgLGn59G1ubjIYXZQ6HK18a29oT31VzvVB9rYRAZSP-O3s3ZsE3ifk47Ks35ePFrq-4wTUNTmY59ueqkx_IxdTAF3xqHAC9fy-8aJ0f9-r5f1ycVzaKRzBNH6oZoB985bZJMm2DD-dyax6AdWQ__6QOouDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
مصوبه بازگشایی اینترنت ، دقایقی قبل با تایید مسعود پزشکیان جهت اجرا به وزارت ارتباطات ابلاغ شد</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16641" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
اعتراض نتانیاهو به دو بند از توافق ایران و آمریکا
🔹
نتانیاهو جلسه‌ای در مورد توافق احتمالی آمریکا و ایران برگزار کرد.
🔹
به گفته شبکه تلویزیونی کان اسرائیل، نتانیاهو به ترامپ گفته است که نگران دو بند از این توافق است.
🔹
یکی از بندها مربوط به آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16640" target="_blank">📅 21:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🛑
در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی ، اتصال مجدد اینترنت بین‌الملل به رای گذاشته شد که با 9 رای موافق و 3 رای مخالف تصویب و برای امضای نهایی به پزشکیان ارسال شد</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16639" target="_blank">📅 21:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در جنگ ما با اسرائیل بیشترین آسیب را عربها دیدند!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/16638" target="_blank">📅 18:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گویا قطری ها پذیرفته اند که به جای ترامپ، بخشی از پول بلوکه شده ایران را بدهند و سپس خودشان با آمریکا تسویه کنند.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16637" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Negotiations with the Islamic Republic of Iran are proceeding nicely! It will only be a Great Deal for all or, no Deal at all — Back to the Battlefront and shooting, but bigger and stronger than ever before — And nobody wants that! During my discussions on…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/16636" target="_blank">📅 18:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">Negotiations with the Islamic Republic of Iran are proceeding nicely! It will only be a Great Deal for all or, no Deal at all — Back to the Battlefront and shooting, but bigger and stronger than ever before — And nobody wants that! During my discussions on Saturday with President Mohammed bin Salman Al Saud, of Saudi Arabia, Mohammed bin Zayed Al Nahyan, of The United Arab Emirates, Emir Tamim bin Hamad bin Khalifa Al Thani, Prime Minister Mohammed bin Abdulrahman bin Jassim bin Jaber Al Thani, and Minister Ali al-Thawadi, of Qatar, Field Marshal Syed Asim Munir Ahmed Shah, of Pakistan, President Recep Tayyip Erdoğan, of Türkiye, President Abdel Fattah El-Sisi, of Egypt, King Abdullah II, of Jordan, and King Hamad bin Isa Al Khalifa, of Bahrain, I stated that, after all the work done by the United States to try and pull this very complex puzzle together,  it should be mandatory that all of these Countries, at a minimum, simultaneously, sign onto the Abraham Accords. Those Countries discussed are Saudi Arabia, The United Arab Emirates (already a Member!), Qatar, Pakistan, Türkiye, Egypt, Jordan, and Bahrain (already a Member!). It may be possible that one or two have a reason for not doing so, and that will be accepted, but most should be ready, willing, and able to make this Settlement with Iran a far more Historic Event than it would, otherwise, be. The Abraham Accords have proven to be, for the Countries involved (The United Arab Emirates, Bahrain, Morocco, Sudan, and Kazakhstan), a Financial, Economic, and Social BOOM, even during this time of Conflict and War, with the current Members never even suggesting leaving, or taking so much as even a pause. The reason for this is that the Abraham Accords have been great for them, and will be even better for everybody, and bring true Power, Strength, and Peace to the Middle East for the first time in 5,000 years. It will be a Document respected like no other that has ever been signed, anywhere in the World. Its level of Importance and Prestige will be unparalleled! It should start with the immediate signing by Saudi Arabia and Qatar, and everybody else should follow suit. If they don’t, they should not be part of this Deal in that it shows bad intention. In speaking to numerous of the Great Leaders mentioned above, they would be honored, as soon as our Document is signed, to have the Islamic Republic of Iran as part of the Abraham Accords. Wow, now that would be something special! This will be the most important Deal that any of these Great, but always in Conflict Countries, will ever sign. Nothing in the past, or in the future, will surpass it. Therefore, I am mandatorily requesting that all Countries immediately sign the Abraham Accords, and that, if Iran signs its Agreement with me, as President of the United States of America, it would be an Honor to have them also be part of this unparalleled World Coalition. The Middle East would be United, Powerful, and Economically Strong, like perhaps no other area, anywhere in the World! By copy of this TRUTH, I am asking my Representatives to begin, and successfully complete, the process of signing these Countries into the already Historic Abraham Accords. Thank you for your attention to this matter!
DONALD J. TRUMP
PRESIDENT OF THE UNITED STATES OF AMERICA</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16635" target="_blank">📅 18:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdaHEpeJ16MWOzLahxfGFW_IJ3b68LkcEmogalTCCZRBKJZaJxR9b-GSSZH6uRaPBGepR9E_qwREfwbK9vi7bfwo4X_ndRtpKCawvpjTOyfiW-iqFQ7hfikzcIFfoM-dVaPd5LE3YYdmlGLks-ZZP7ACHPHIkM-AI-q4vdLzKMBtWexHXiwwYEqHXubPNr45X_PfuiFHeCK6lNICQl5ohW3rWSgAsI0Kaxqj6J1LxRiMGMEr5fpGw_RAWk7dgO9-g0SbaULexJ5-DFlo_Hw2-eppcg5eO3LJ4joW9DS8-FwhojCaGssmpUe1OXxYOz9umXeYF_KNtiAmdZCaAMnvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16634" target="_blank">📅 18:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وال استریت ژورنال اعلام کرد مذاکرات بین واشنگتن و تهران سر مسائل آزاد شدن مبالغ مسدود شده و تحویل اورانیوم ها به بن بست رسید</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16633" target="_blank">📅 18:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!
بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16632" target="_blank">📅 18:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من
پیشتر گفته بودم
که ما ایرانیان اساسا نوادگان ابراهیم نیستیم که بخواهیم به پیمانش بپیوندیم!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16631" target="_blank">📅 17:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:   از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند، یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16630" target="_blank">📅 17:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:
از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند،
یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ توافقی در کار نخواهد بود و به جنگ بسیار بزرگ خواهیم رفت.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16629" target="_blank">📅 17:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🛑
در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی ، اتصال مجدد اینترنت بین‌الملل به رای گذاشته شد که با 9 رای موافق و 3 رای مخالف تصویب و برای امضای نهایی به پزشکیان ارسال شد</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16628" target="_blank">📅 16:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">در منطقه بانو پاکستان درگیری‌های سنگینی درگرفت و نیروهای امنیتی پاکستان و شبه‌نظامیان طرفدار دولت با جنگجویان طالبان پاکستان درگیر شدند.   گزارش‌ها حاکی از تخریب یک خودروی زرهی پلیس است و چندین نفر از پرسنل پلیس کشته و برخی دیگر اسیر شدند.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16626" target="_blank">📅 15:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5d3riGqGnU96RyEM3WQUO03x2IILspcLFMi4il7tuNj9elge8GwaZJb7gnJ-g-fw0qByMmjcqPd4vRi4lNfkZRrJ5C68ZYZDGKQaaFmBYwgg83fCu3O2C0hBdrTWX7VKAqAP5rwDnN6CbP7JKb0-dwUh8OE-FgreE0YSX3VaAvWnV74XkTwx0bs9LGCQdEtzF4hYddi7DUiHjTX-QJM3OZTCkbljY8nKpU1HL5zya_OW2xg6DpVd7zFRE9FuafiMqZrUhSY29OKD9lsn86DqxrxzChRhUnRrko1Up1kwiQXymmF2aWS21XmTjsFder7pvvX3CCtTf8iAwK2Y3l8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16625" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku-JXAmdZZTDsR54a4fKk9zOAGoJrpTNGTEucVI05qcl10lnKS87QI1RnXYAB3li72sIdYf4f9MYyy9CKqZ0nfGw82IgkvkvEVZ0JGtHdO8kkUgtT34lNUiWs3vTiRHGTTyyWRjMbAqxAKMExDZzQ4kw8Y3KNCrt5w08iw9NODAx2zDDoMGQi2hEDCXd2z7zhyWP_OHBmfBfagYzXWcDdYkT3Hgj-Um14sX6eG_Sii5ZYw0MGcImuoOg7rXho5PEzIu93L60aaGJhYsNF5qj31UvCHw6raKwl8kBhnkcd0ocM9Z7XVNSrJdPozA4NlfhXHNCZPeecF_KQltvvnKl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!   حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16624" target="_blank">📅 15:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK-zULJ0344hDBgaDvJcgCh98BNjzj_zg-2VwXyXUATZLParyLQ9RSWtwzD5jj7m9V9XV-Secdet1b2EDCZ9pBkKBkp7tHYT6FTMmGOzLLuhXGBXkSTYN7q6j-Xa_rCehEO6yraBDiXCfIfsnHS11x_NP9WuNi71EOCR35YkKokAx1a3Iebxw4qxe6BgAuh1LbSHE6ch-2DFvu0Y2iKUOU5rneVoP22t2zotVsM8iEd5tVXS07-y91iWh3lvtiTDAnWGMoCbQ4020OGQ2TJOWdK0igLIUoEOj5qOg4xMFsMJvZj2jwxOY5DPyI-LBjgmGJ20TF4pJhD5FVdfaHGUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16623" target="_blank">📅 11:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16622" target="_blank">📅 11:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16621" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت امور خارجه ایران:  «اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.  سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16620" target="_blank">📅 11:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت امور خارجه ایران:
«اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16619" target="_blank">📅 11:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق متدی که پیشتر گفتیم سوزانده!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16618" target="_blank">📅 09:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق
متدی که پیشتر گفتیم
سوزانده!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/16617" target="_blank">📅 08:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!
حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/16616" target="_blank">📅 08:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK44jF5CEZyeLTLLTls1gR7ghGaty8MZpaIqdtH3xi2UuWrTXklQ176RwjQePFFdSczUV3QotptzcxZ-jS1jcCnWZXB975GbAyp6XSs2e1PiCNjvI7L2zC8RgGU4KNJotAaNUGNihZfO3Zz7lYCWk9AY5zsil0Gdxzpnewja0DpQkvx6YgOMKyYH52ihrHxnBSi3WAR-VK86Bns3zJJ7AFybZGwPdkaZY-gu4B2jckVPf2BusS9OBzOdNvabyboYR7vvPjqKy60oko3aaktXuIxt7q_UoyVx-h0oleP1NT9jG6bDrNW6qafB8vKln8Vvj4w9ssdCs3EBAZZKCoRwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه هرمز تحت کنترل ایران باقی می‌ماند با وجود ادعای ترامپ - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/16615" target="_blank">📅 08:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ حاضر نیست هزینه خرید اشتراک هوش مصنوعی پرمیوم را بدهد آن وقت میلیاردها دلار پول بلوکه شده ایران را بدون دریافت تضمینهای لازم آزاد کند؟!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/16614" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgDsrMI0cbVQW1Ht3pigZlS4n_AfxFnlscl2QXq-ByphZmIJQegE6mEVmqTC7zumY9P3vcgsz_yt5JBrSkOIAjx71aZJIoc3U9Vfv9vA3hphH7VZrXhKGrSkKz7IMx5nW13Z1I0AYaMRBPgT0l59Gs7WmORSV0dpysrHeOO83jUp35yCy6jtOis5AB03EF3cIr-bu8RR1TaR84mlMe1cEE3_3wKyI792XvcD3rOm6eOczghPiJJDeeflNCq1X29dgqOk7A0yppvpimUHOJ1gVt6MiIE7uNXx-J19aY3yuOS83t25zishK48HCmB912C6zopNHuk-LqmX4vhiv0naPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ !</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/16613" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اسرائیل تنها.pdf</div>
  <div class="tg-doc-extra">347.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/16612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16612" target="_blank">📅 22:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzLgPiXsk-BOe0ncHMEh-W86A3USpQtbZDdJ8y82eZzQBRCJyLqKHJ-nxHHUsnr0JmKbzIUBWKbc0TAAaYZpXQbXdnc7z44rlo_tZLm_M9tkcCKB6aL0imCahTVOi0BBWRbcUcwV2o4cm40ye0tWO_-ANl2aNcJNAOCqlKob5s5Dc75fLnqUKmJbN7yUmNYSGPHZMkpExLVp1uooteU5-geYLA_lFdPPVCZexo6J0lee33YfwGSqGxhsGhBGR-s4omGC30AQvHeAglKDqF2zVfku6C_f-37UUtD9zPKylo3aa_CEW0FCKc7-pLF2djBS6NWT_GNxBaFIz3lfjh4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16611" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=K_KJtzr_XryJ39Bts09BCX3enugB9sNTmuOmxUxaP3CmI-BD_Y67FUcydB4kHWvJE2aa4vT7XqL8jjl1S1GVScVwh-U_-viAVH6bzMyw8IsLs5jjd09ys4Q2VWm2e6kNCbowIRXZKInqHbii4xKIJSzRKb4OA8-qOZG_PpMioxRPnG_KnhdbSSu6bgYqRUz0yHIMvtOvdqiUJy4zksET-TtAvcPwe1ymVC27tPhvDDEhjTY-5DAkH5jfNZ2jE-PjhzFWDmg_2NIQd3pMSm0IgdMOVlZ8LRv1Rfh4H963SPU-S0vIJVeY0wuSJT_dZNeFpFgh_9-m61yyZrJ1gcxvjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=K_KJtzr_XryJ39Bts09BCX3enugB9sNTmuOmxUxaP3CmI-BD_Y67FUcydB4kHWvJE2aa4vT7XqL8jjl1S1GVScVwh-U_-viAVH6bzMyw8IsLs5jjd09ys4Q2VWm2e6kNCbowIRXZKInqHbii4xKIJSzRKb4OA8-qOZG_PpMioxRPnG_KnhdbSSu6bgYqRUz0yHIMvtOvdqiUJy4zksET-TtAvcPwe1ymVC27tPhvDDEhjTY-5DAkH5jfNZ2jE-PjhzFWDmg_2NIQd3pMSm0IgdMOVlZ8LRv1Rfh4H963SPU-S0vIJVeY0wuSJT_dZNeFpFgh_9-m61yyZrJ1gcxvjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا توافق در حال ولی خب شدن است...</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16610" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ
:
اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مثل معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و راهی واضح و باز به سمت سلاح هسته‌ای داد. معامله ما کاملاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره نشده است. پس به بازندگان گوش ندهید که درباره چیزی که هیچ نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من باید سال‌ها پیش این مشکل را حل می‌کردند، من معامله‌های بد نمی‌کنم!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16609" target="_blank">📅 21:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGAifvsXey59myliVt0Uz2LelYN_vY94vBl21D5U1boXBzH_0091K_qEs32IOWuhZO_v-rspzfhkyeI27joOWJ1vbYGpSOK8hGyHMf0XzslbYCbF28yPfaH4iUjz8Lk5qnyg85PRfma5MwVJHoFNScdcH2zdC_vuhQfrQbc0_GL_qEfC3I3C4VF0fswSLN7sXTXtuI40xmD2xvXhVkHXzxv_duV80GqIa-Q7KhrHCgDt_NFqjEH6-gKAdNOaoUBFrWHykXE1yh6ZtLvUYh50DvDLTFYXJVkc8otjLx6cLZGkRdWDH0l15oqdzMjuTIMVoFeL2AbWDUSrzD5oG84Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16608" target="_blank">📅 21:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uthlhmiPVU6Xc2t3MEbNPXqugScUpERPS9q9EdgBJYz1nMQzqvlcdYKYt3iCJENSt1pqBv-tb9-_a3jihY_uml6H_jm4NzNmVW37VzpgUdwpMSOVEegdgEkLe299z6B2HxSgi_Bq8poQhAG5K_T5-w-urWU5gwPgxdUEKJkqzt0C_Pv3Za_Q4ADUg3CXzrAKisSsnrUoaBt5XYQNsi_WeQgyGbDOVOZelZG8L40V9mdLf0O2G80AnSiz8B9Pta1b8Ph7OGTc79u8gNEfr_cQH_gY80fape1M7sDgZ-r8wyzX_L_AiAeVg1nakzbjsVPw3uOyGIV-T-nsXL9XTTKU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16607" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16606" target="_blank">📅 21:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«ما آماده‌ایم تا بلافاصله به درگیری‌های شدید بازگردیم تا حکومت  ایران را تضعیف کنیم».</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16605" target="_blank">📅 20:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16604" target="_blank">📅 18:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">-طبق گزارش آکسیوس، یک مقام ارشد در دولت ترامپ اعلام کرد که امضای توافق امروز مورد انتظار نیست و هنوز چندین جزئیات باید حل و فصل شود. هنوز در مورد برخی جزئیات رفت و برگشت وجود دارد، برخی کلمات که برای ما مهم هستند و برخی کلمات که برای آنها مهم است،»
این مقام ادعا کرد که سیستم ایرانی در پیکربندی فعلی خود به سرعت حرکت نمی‌کند و برای طی کردن تمام تأییدیه‌های لازم، چند روز طول خواهد کشید تا توافق نهایی شود.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16603" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16602" target="_blank">📅 18:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دونالد ترامپ در تروث سوشال:
یکی از بدترین قراردادهایی که کشور ما هرگز منعقد کرد، توافق هسته‌ای با ایران بود که توسط باراک حسین اوباما و آماتوران رده‌بندی شده در دولت اوباما ارائه و به وجود آمد.
این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. اما نه در مورد معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است - دقیقاً برعکس! مذاکرات به شیوه‌ای منظم و سازنده در حال پیشرفت است و من به نمایندگان خود اطلاع داده‌ام که در آن زمان که زمان به نفع ماست، به سرعت وارد معامله‌ای نشوند.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت و اثر باقی خواهد ماند. هر دو طرف باید زمان خود را بگیرند و آن را درست انجام دهند. نباید خطایی رخ دهد! روابط ما با ایران به یک رابطه بسیار حرفه‌ای‌تر و پربارتر تبدیل می‌شود.
با این حال، آن‌ها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه یا تهیه کنند. من می‌خواهم تاکنون از تمام کشورهای خاورمیانه بابت حمایت و همکاری آن‌ها تشکر کنم که با پیوستن آن‌ها به ملت‌های توافق‌نامه‌های تاریخی ابراهیم، بیشتر تقویت و تقویت خواهد شد و چه کسی می‌داند، شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16601" target="_blank">📅 18:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.  به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16600" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSirus</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMX-eUKboZqCGhlB7g5nGyUaNa3QWAmKn6EY_MYGSY11DXm8NKC4Fd4OZaiFfiEel3lgWTcj8fqtad-Eczcy4wT-c8Wx-_nRoebzd7kd5m4FhBsYephKmrjyEzQVsiplqOuFREKMKMrB45PYJkT3U1f7XqRi2jIfPixddmcyW9b6lPoNh3Y2n9VIAkyiR3EixRQdWhd6H6cN3bSV6CRvHrSKXl3Ov4FGM5RlSHHE-S-OIkXv95KQ3mGHelAEjJvihr4Q-pxf2ABOYcxnqiqoUmkgM-lZPK2WHDvpHLCi8ZKGRdgmD0_Zbx-yjLOMCuG88SA5Y1LR3nI6IDraCRSpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر چقدر مظلوم بود و هست، چند سال پیش رفتم و هنوز آثار جنگ با صدام باقی بود!
یاد تکاوران ارتش و نیروهای مردمی گرامی
و یاد زنده یاد سرگرد خلبان محمود اسکندری و کابین عقبش ستوان اکبر زمانی که با انهدام پل اروند عقبه لجستیکی صدام رو قطع کرد و مهمترین نقش در آزادی خرمشهر داشت؛
خرمشهر را خدای محمود اسکندری آزاد کرد...</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16599" target="_blank">📅 15:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مسئول اسرائیلی:   ترامپ به نتانیاهو گفت که توافق نهایی با ایران منجر به خلع سلاح برنامه هسته‌ای و حذف تمام اورانیوم غنی‌شده خواهد شد</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16598" target="_blank">📅 15:14 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
