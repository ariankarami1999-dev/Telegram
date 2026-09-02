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
<img src="https://cdn4.telesco.pe/file/HfJSe5UwFFZCVarDNV4cpzw61oFwxuhTFwli7f7-ySw-nr3JxE3ZFo_TqCwp8xTwdv7wFIvEVbrFe-Ja3-pQltjwFHhEEkrpde7phhDhm2aWcqRtnRRSTJjoQcnUmZ9p4jfV2w2bAf5lZ_WAhpujYwZ9vhpvB0Cv0UKHt3TWsJDA3LJiG8VZ-g6rAoQ5ZnPp05fv4mrXrfjNXvRI96Y4K-4VuuAu0CcmbLhZPPCR73GYTdFjBwgWSVElPig96_LljM3K2FDBglrE5XycboJEEnifvRPxGIf4ahhiZIc2JgJIhz0o3YS8DEzT9JHf0jIIeb0c3ylQ3pJqeS3sLhTcHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 05:36:47</div>
<hr>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaYTX-CIuf_P_CYMf4ts_xJdqoR6uuQWP8uv_G95JLmy_Fh3_eW0wkNpJc32RUC0EE8vqtOWtjgJVmqNjw7Xmcs92w4noXmJJRRPdLxOR48YSTPcBMhmtUPwWFV-f3F9lT40aNLzumdr4HY_RCKOIdleQlOFITLrOELvGD7a6x0DjRfUtDvlCTvkmxxW63XHHmZB-oqZpFHc4CEL2AgYG8II4aQzWX_vs0McgGxxTDSzpanhwpQqpwvv91LVggWCJThViIem42nIIhO2IrhBvCBC1as4BUsydShjCzymKvBHkIM59HHtU5GngjKsRqJMmWY7WhBq2h2cmfBVWUsNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAq5MXg1K5jaVN2kQBPzg4ga0mUkrB_G_dp-frdtAnn69-nKJAeQunOXQpd-dWeN3DD8sYAAACfiD1q6CCI1qO5UYmsUxVn7K4HPHpSYauZQd_5_KyEjCujwhgJ07CA2XDezs0WlW_YQyVZixkh8KC9a1Gc_3sbsOOLXT5dpoUSj-aDk47lMOT0uZZXkDwFJ3Fkx0gQuZEu9Tka3zlKOl4owHELr2rsyfOgozzO3AFkPe0qGZ7nT4IjD9P4scDKmwLlDs6CEPKkFdiww9vP52fQ5MIHEiui3EdMike13q8vY9U9NAoPhuii0HWN3F-IWu3NU8OiSyp5CeDWkS7XMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn5k3-aIGKPTSuZusKE6xRMbxPG5vLahUm9gcbBXsU-sIRQOLeKuZ68ts_HYEFyXPVuz3uPaSsPkSxduj_vxqH50EaY6Fqq2G_Xw_QO2DgieKnrZTmLHASQkYjSzZgmTnzxfZQVIfv_xqaad7Vh4m0im_Td61AlZVMlYuskZCOk60mWUmHOn08QJlcL-fz8LpWEc99rZgRoWHsCrcYogEGPb9HUfwrRZfI9JyyXKyKBbDZPZEtqR3NiIhYO53OwU1tN8of-IzCVctMM9csi84uVr7Oy__jFw2S644MLNeczT3D3vLQqaxveKyt_hb6Qj3CNHAup6_Nvjz-2XcP7Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj3kzBp9x3y0PFXVC41w62Xnw4RctO3xT0FElyKmB2uvPJkWu7dEUuHAArQDCj9wgi6IXNz6Eoxvd7fRlLFRRmmATsf-2f3x1zAw3HLqQcDx8H-QMQGD3OXml2xZvGkNBylISJXs_VZ30hg0jRMw8f1PvdXvkTeJMwpHP41JKJvKTJrsCUTbODHez1CC9RaohPZHhSOdMqk0mTuNg-RwFKqifmL7l1Sz8Z9Z6BO_64Cb9wpvi5TJxDLUQvcMM8f0Y4_482RJdCP7fmtU6JQQI2i75i1Lzw7ILEPlK6eHaINYjAfkTH5f6r5gNmJ1kDXCBW8FwgXBAq8QqehAHczO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNHdbLHA5R9necrRFIXm0YcUBz9vfu0NraiOHVwtpEujamxEDtWIk07orY6m_ZOt_SzSBYANpGn0wlfEXLU7zwooBzw4M6eWfjSYAJfrGaTJOiz3HKfQldsJG0lKKp43k1Gu7HlxOgMee1MwySj34HtY3nG9yhFWE-d5_sJLEnLZsbUYGYlrBNLH2wIyXcyRjr8W2eZWg13D-Oula01agTzWmAklGxCsXKZLZNnyfdHvRkGKp7Rp0ttv3oXTRibfn00Tunu0e_Cqlpo1axRYgt-pacS0fMDp8w-NUNXLtYh_8OXsHIGcz45N_VHqPeYYjWBGlqdTkCgvlvdePfSzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگید چرا دیگه به سجاد شاهی فحش نمیدی، دلیلش:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJcKJohPOpfUlnDpxFs-Ji2GiCzIsVdKIt6NnN0qYfROQLcoCM4Mvd-w9Q69VuIIOGCuZljdZ4U4m8AtPv5TkJgAcpsayWmhV4WiRt61MD5NsIB-evD9iq0w0T_aBL0BlMujkY093blAxgNEjORW3qrC76rsQVJ-97U550u2y_yAIqvlus1VkviYrBCJLjSJpWIJMsM8FtD1QjCOt0dYVCke97z9remrcXgZUiw9R6i7JWlhBgTJRmcYLBD27mif1fpMbzx1CQhAtax0gfOTyiuSzPjZmVUjTQ_4FwsoRdYmP3c4b-sl4VvmrY30D7Jg9N5OfaQ7BYxxAK3Ux4WP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82863" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgTYmoZYBJ5USQRhNos5VBBHcCgjtNWkjUvJjArn70HQ9CxEliQ80Pz7ylUPtMak2-7kZO8A3bvND2JuTe-8kOOyxrDASC1eT76YstOEqXNpWoLf6FYIfOa6gLHvnXpsbdOI6bawdfWd0rZMGFkYbVOayyaHKjgCUbUrSnQ04vjoq2GrkTQkr2aFR4sU4gEcpN1e-X_j7TNksvAaUgII79p1aEHGJfDDt60iCNV00p_zyzFNwuxuCiiBnzkpKhxYVYXfCd4_U65aHKXasEFrYsmja0NsuvSCRabyoas24Y05nl59BujnikBMNfRErN981VwSVJnQ8Ofh_9nM7LuA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpBaBgEp5ixkrGN598HXX56rcnkx-i-kTnUOeVeJbx1zsAwGDDFniUqoFKDtfkCGh1qlHB0tamff5Q9TC85tXVUDwaNIV7zRkGZU99A-enWs6BF2TW3kL9fA4mn2vF3WeXORrhdnp0vrYqeaQFrmQYYO-j02qvDzZtg-jahhPGoq3EnrwjCHI1LDynTclmudVeKH1tLQ6JrMF33zQi13PbIcUhL9seD96daIjxiuS-6bZqGhSEz0wsJlxqtzE_Zn-HU5m7HGzt1dTHZrpd-ViaIiU86LPF7DZT2gSMfQilXjIaz_P2jkw_refXb7y5q6bocqDVf6jNbfFuztewtRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAQ1eVnzehttRp4P_IOWZ8cApdZxgRDULu8zpLF7dT7_PEIWEH8CiUKM1smnKeEOydmk1EF8CEe7nPs72HPmqXfwDge6mig26tlc02_5qwt880j6759_GG742w7gSNNEFYxjiwH2GqaqwO25SlxwjllBCipkg_qlVPxWjdI6TBX_bx_p8HcA1-oQB-L0rQav1e_SJtHnYuVKhcYtvHYpbX1ra1X592nyCCGft2RJE68Z6PDMOijFskF0khXN0llEVNZ_Fl6GkKU-ADNiEt8Bfr2vOgiV0bX6d-NysCKhd-A_G1ITOMxm8kSz3XxCRjwryU8nhrDQvBkIYrW8ZDRCHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان چون این روزا قمیت دلار لحظه‌ای میره بالا و شما هم که دیگه براتون مهم نیست چون سِر شدید، هر ۱۰ هزار تومن افزایش اعلام قیمت جدید میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82856" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f513feec.mp4?token=h4Rx_35dQNOhZitcembhNAkjjoxV215kmTSgcq3FF6y1V4VgkWrqHsfaqHYwyGEh82VBrlAxDhUs2d8cdhi8RITv_YcTnPYchaCTr59uevkM8hVkHNg8C5BymLaaQgxApHrJDMEdv8m_v-rkCcXvxSbwqXquFrQeiREfpS2wWZDZlwEqUqbIRuTgE739lPRCg3PNbv1M79o5Buv0DtCYcQP6r4rnEagAYeupFGPfL_SiKc-31_ZeT-r38y3sMiU6NCeY8-PRsMP_b8XdI2RTuNMXxZXWMK0WB8QhHarwScu3oMJKNVnIA7__EDU3jR0gxp61cv9yUH1MsOb-tptImw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f513feec.mp4?token=h4Rx_35dQNOhZitcembhNAkjjoxV215kmTSgcq3FF6y1V4VgkWrqHsfaqHYwyGEh82VBrlAxDhUs2d8cdhi8RITv_YcTnPYchaCTr59uevkM8hVkHNg8C5BymLaaQgxApHrJDMEdv8m_v-rkCcXvxSbwqXquFrQeiREfpS2wWZDZlwEqUqbIRuTgE739lPRCg3PNbv1M79o5Buv0DtCYcQP6r4rnEagAYeupFGPfL_SiKc-31_ZeT-r38y3sMiU6NCeY8-PRsMP_b8XdI2RTuNMXxZXWMK0WB8QhHarwScu3oMJKNVnIA7__EDU3jR0gxp61cv9yUH1MsOb-tptImw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکار رو یادشونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82855" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به طور خیلی طبیعی یکی از دیگه مقامات نظامی آمریکا که میانه رو بود به دلیل اختلاف نظر با هگست که تندرو تره استعفا داد(اصلا هم مجبورش نکردن)
این استعفا ها قبل از شروع جنگ ۴۰روزه هم اتفاق افتاده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82854" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2eJyYtGj_mnyWz945tGYKaz0kD5MOlxIbvMf7DWo_hEVH3JCA2cIWrEW_h_W0l3i16j4rET5tC6LqHdFSjw8fyqX8_l30ks8GZT4ia3ygcMYjoeLXunyuhRhURwBA-_bmC1TDOX-whIa37GADb-BkGcMEzd1TfnmEjL23W7Wr-pkY1IvzTX9GZSYDNtaUEaUn4SyNtOPbEKMW8x7BoIkU0S5fnW0yJtnftQr245mt_QLR-Kkff_Wa_vG8oyo0VREDwC8G_kASiaDbY7slkTtbtMY8nrV36qo_QU_KSJTUalSc_QzOsZ-0STPrEoU99_cK8bbVyTgTBLDHsDUY2XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82853" target="_blank">📅 14:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82852">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=SWpy5hM_M5deNPpoyMEzk1avoGrw-J_lOE2ZnKE-3RE2fG_vXt9bdGXzxA26jRJht6w7lYg7Zx0JDYK7pxJuyuIGzR1HmSHFqRPWzF7LQwcKnhct4SPy_wcM9Uw72xr4nhaG4EzN6TGLCx9YeKcA0e5l0FV9Lpf2TAiffvYl8cqkZti-TuhvA72l2_Vx9A7ovQRB4pezkNWPDP8ks0YsKStuL8mZe2H5Dof5HjvQB5ELe7ngGnX2Sk5hL8bAFCwzgrS0hD8_-BUEknQV-DRpMSU3HzNo2ACh0polcOjzai0_97A4kreNxyLOFzFpNhBT9KuxAwFVcFLR68raVCf5oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=SWpy5hM_M5deNPpoyMEzk1avoGrw-J_lOE2ZnKE-3RE2fG_vXt9bdGXzxA26jRJht6w7lYg7Zx0JDYK7pxJuyuIGzR1HmSHFqRPWzF7LQwcKnhct4SPy_wcM9Uw72xr4nhaG4EzN6TGLCx9YeKcA0e5l0FV9Lpf2TAiffvYl8cqkZti-TuhvA72l2_Vx9A7ovQRB4pezkNWPDP8ks0YsKStuL8mZe2H5Dof5HjvQB5ELe7ngGnX2Sk5hL8bAFCwzgrS0hD8_-BUEknQV-DRpMSU3HzNo2ACh0polcOjzai0_97A4kreNxyLOFzFpNhBT9KuxAwFVcFLR68raVCf5oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده خدا در پاکستان داشته خودروی بدون راننده‌ای رو که خودش توسعه داده آزمایش می‌کرده که با ماشین پلیس تصادف میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82852" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82851" target="_blank">📅 14:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82850" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxVpiC22DvJl52GuMUy4it5H-2j9byHEEdFiyTwh-oXPDnv_jOKwNBczlWyuOFpRjByiR6-UCU7WYnmjSxWTYVwU4QhskJxi-KsO6fObe1ECfi8mnYT1Xn8POK9k6xw_Nn7q4oxZMmEOTmkffXowl8CpXxYqQ1KKl9HIYkIx4qbuUsNsOUvlE2wkkUTCgbuB9ha8UT2C-ac2PVomJL3GqlKjT3luEKjxydjDhBiiHqmpnNdKZUAUGzGmOUvsfqb3hHR5f-z8hTy0IZo5OD7sCtBw1fxjSlxnE18saEyS7pYIy8dsEtpF165YmV5jB8LsAkSPcybr8FLAV5-HX35prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82849" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMG0yhUilRuvpDQyn1jhl8lxuRGBjcHxLFUiudZxQW-hHE08HR58qa3vgQDzFLAh7KyvkpsQD9vOaQgdcgyih_7tCpYn0qhqn_RO2hZ8ZwMSqswozoEylQdPAm6FewR2j-JfQDxs6mEnJVx6A8ceFKxzjOu-_AjtzQN22AlDHa9P-jiqWMe3O5tiFDCeyYejXpgsp90uxqQt9aSFgagRMmKIfjXGazclelSA9_6OVj6HDLbARL2xAMpqo2JR4p98Z2utsKa1XWxGSTSbMooD4QPnS4lLX3kebaS2LiAnRTxU-t0nTfDmGOwrUMX6UcKCuxl2CpKbuQepeChbJHTxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من جای نخست‌وزیر کانادا بودم بعد از این توییت کل نیروهای نظامی کانادا رو منحل می‌کردم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82848" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=A-gPRMISeIqCy8syK7FMhT3oVlH5RlnFSlsjBQ8kOmjO8urzQkVtP46p7vcEl92dTHGtH--E7ez_jyfmo3saDCGOs42eLEARQdXJYu1ctNzk7MbGCCgNK0g9I6KvNDsMCDNHZQvrykuMd9ur8JbOZdodLgt6JubnVRTl4KHceeY-FJnu37YlNb1bNFZ4Nvgc5XukbshXEnfWv5AAeSCpUxDNWVkVdL5Cnexyj9bMWMt6s82gCTP1XKvrE87Y1TXgeZW1TZtnqdb_WLcVsoWvS_FSoeiJa7xAPsC0mKzE0einOPyukOb7MXNyHfjWqMyCYM1H61q220LhrmxY5NgmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=A-gPRMISeIqCy8syK7FMhT3oVlH5RlnFSlsjBQ8kOmjO8urzQkVtP46p7vcEl92dTHGtH--E7ez_jyfmo3saDCGOs42eLEARQdXJYu1ctNzk7MbGCCgNK0g9I6KvNDsMCDNHZQvrykuMd9ur8JbOZdodLgt6JubnVRTl4KHceeY-FJnu37YlNb1bNFZ4Nvgc5XukbshXEnfWv5AAeSCpUxDNWVkVdL5Cnexyj9bMWMt6s82gCTP1XKvrE87Y1TXgeZW1TZtnqdb_WLcVsoWvS_FSoeiJa7xAPsC0mKzE0einOPyukOb7MXNyHfjWqMyCYM1H61q220LhrmxY5NgmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری اعتراضی سنگین جهان پهلوان هادی چوپان در واکنش به حذف شدن از مسابقه ناعادلانه دشمنان و ناملایمتی مردم کوفه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82847" target="_blank">📅 12:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi13Jyv5bS_2oXcwQu5nPgx7eL33tAAIPDMUpNg0W8um8-ChRHQPuttBi5bHDHNCTVpP4J5hz7fxADBRlnLkk-D3HbgtKEj71opkOr4D24jpcGOb3lspAcq0QHxViAoS9ZzVPQfPDJYlq_E-SjKZFNrckaHAs_RkxBVuLRfQvp09iah1HFiwiyTF673JYwuEcTh6PYlbUew70dAw2dCkv1T5dIpLclDaCsP5E6OdxNe10qN88ywxgTl4w-cZy7e5rTKUD-_ATkh4naWYSMvnSsMBMSxdd9Nl-HJ1eEr6Q_-D6n9U28QOdVxYbIa7uhkirwsRnwVttAuny6j42wSctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhS3SPUEMUvBlEv78mUwXOeLXsoqpGKKXJXFxL3vax-bemn-SynLTfckTI2Yt2zNlC2sBD6nzApKsBliA9mAEx59GEfDn-KZXkkOBq1T2nZcx0OU2R6lUR3M4vWEWw3dJl3OySUAv8aC6234fjis7f-Sh1j6eeIg14lRRn3r99VPSlOTwLEjLy5uBqkRlMNADGGkvEE9V_oyhdaH3RE8d-mV31lZiGYTU2k5kPI4bEmjbNo8gh8xhBxChrIWTrcfyYNfmptkI1-E0x6MLW1EF03BuaSIq74c6nNUHAGamCIno9ESnHH04qTwCQkuGJlQhljoarE5UlvGlCt8WOiaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhawUKIKLB697h3TzRayDbTaQT7HCrcqvxm1oP9cgKOBNlNxaGttyYFdlpia00_zflk_aLWqCyUtYMrqBvbEZZj1NkWlol-_HFu6u5ja5PUSt-q4Ufw-_b-XYGz5h6WEyyNsnyRYkCMTfc57gg8WhjNXRdogz7LZtu8wZBiKVAz21RNQTeVbBvXJgDsitx7H6Ji-fqnfpue-bhm2x6dTQunP0wT4jaaJPzbzpy_qAUpPdBmAYHc_aT2944Vavk4NsSVVa2HiQVdvTTai00spX7_RfnxFmxojawXVoLkG-9VqqTj0DFfF3A-IDfwxEIn2ew_YA0eIp0O8OzKMlW8WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه ام اومد تو گلوم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82841" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUCOWZtLgt58Xhmi179qS9J8FPygrMb4C8NW7aqEw0TIXDuuryHXP516U2WEjGOaXaBb94GPncC3ctcYaHpVx3_AY8T02W9Zwp5hVs7JeJWdWVYe4lHgOEMEVbawNGo7ErMUd2JfUshbBepZBuAPlDadhet6hemNCujsezF81bnv1rEXNERF5GlMcFciqceabc6rJK4dokxJUIjOFhasPYZSkCiFgNUYpS3EMFK6_-CRXc3eiNHDK-1kNm9UurZFMmPllb9tuQBCIuN-RtRLbO1P6ioMAn1bk75hriDAmqoOuN6A8LoInpIVTCzRBGNi8wHiHCT6qa1OHwmkz01ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشه یه نفر بتونه انقدر اشتباه کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82840" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNdlI8aNVk8cBxOQU635xW51kIsP6HbZWb-7vBm2tw1LI8jMytX7D4fQtnhEaJ21ZjiGzy4d5UTWpc479eBW0DyinpNMSHxHeJQfPR-IUhc7-edP2I4V_IgubddYlit6a8OaJgA2tt2_ht0k2s0CFQScHDWneA3retWWPmOoN1cGKYET3Y2LL1PFOkK0Q7c4xAjJ4fuYY7Z32rx7-AuGV5mrCAuY0InROKZkTrtfYHTIUizJxEfoTFiJRrG3KdmWUQPuU5P4WQtMc5fGPh6X_9mUTTDYWJ8QlCgeDo_hVKoIGzmySCRcjoSuvchHonvRHVVVE-AeJYnQbujGw0Y-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این چیزا جی تی ای رو پی سی قراره دیر بیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82839" target="_blank">📅 23:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکیان در واکنش به تذکر رعایت پروتکل‌: بابا ول کن پروتکل رو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82838" target="_blank">📅 22:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پدافند جمهوری اسلامی یک فروند موشک به سمت جنگنده F-35 شلیک کرد، اما موشک توسط جنگنده دفع شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82837" target="_blank">📅 22:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcz-LGuc6xu2WZ0Qk4Nvjz8-tobnk9ELCQ4VQvnSxCOBCD85UN-rh0j_sS5q1pWG1rren5Bkm-GIVEvTk8lkrajRCiNktNcK2x94r6jcmjZYtkIreSdxrCJ6_6R2tKV2Jxii_nQlSqB7WcSl4MW6Exw63w8_h1IyLhOGucrjvP-lBOeCBmGmSYIJnGT-3u2tHcBjEbps906Xh62v0k-I9UuQgqZQlIVKiV6hkKuZykxpsBG4d3MZgrDMXTpSs2Fazpcw6vWDdnm0iaaYtIBGYPD3JK2UtHSpiO93jqnP5bcPsdFLimquv_LU10oYr8I8WBOc9GBfmhzSbWPytQhXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بیا تو چنلش بگو دکی پولمو بده بخندیم یکم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82836" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ گفته میخواد امشب جنوب رو بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82835" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSikKt2Qdu3ezlvR1iRewN9LaxviCl52Abqkm9U-ZtpqkEqRJut1FR-DUTEFQE5r6uAALygPLRbN3OOmL1iyMX7JzOCCrwPuRK9eWopZ0jA3erht_z9a02RBDYPOjuvI5iYD3L3oUZ73FFdoJjgCkmVGsbCn1lREdvA6CMDHztZ0K531lt1kTEzGg8I2Xrpc9PkqT1Bb8sU0DjvrqO-Fs6A1BbM3kh-q7-IevtuxGSUIzFkXMO65bz3UheJUz_vEsbhRkb0UfxVY3OLv2AWlb_HvIwfLkac9wVUuO7hQu7cINC9fRngw4aNtZNiJkIDq9JzuNftdk1n7b6lgy67djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82834" target="_blank">📅 20:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82833" target="_blank">📅 19:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دالر ۲۱۳
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82832" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1knRD9xqr81gT3AME3z0iozNcOinoBFX_c8rzvGhkhwJfLMXP5Bg7XdB5GfvrnnzuchlQy5Ffs-QmM08FVL2sFKJY6a9F_b1NRXpCQfADVfrSCz58n5xQ-JnD2spXHI3T5tnwZRTQhtmPyYMYV7Vzog7eDbVh_grdViBEqkejzcndf97XQb5bDun770IOmWWBjHILoi9eSozgB6Jokmh5RSNj6zL5hN6uCKLrVre5JBhQCy4RFWMQ3bp8LH20o1qyYQWiRPMXl056xdz8ZVtUkfKMYm4F-r-yIa2JqIS3M0XqlNr_vySyMUXsFaofePaRHfK9K5fG0dpyfanhSdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82831" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWcO8U6-TVsl8PcXk8sR_arhMcgo9ryWZ3cNftlPOXFOJ9S2oWHy9QrSZ3eQf3Xt_nv5k65rbzEVp7cPBZTKoFIqfaAX4v04zhFjc0a2V7x8ybeeGCYljd85rt1LIRh3PdMUyJCPUAnapnJyNE3drzyBFIwEI8_lJts87hEZbhjgFPoGkO95fy9cwuNXUUAl6GCy1PFRk7N8W0eDpmH_dhF9VgHrEhlA28HuewXJBEjEg_3pgSt0DO7rD28U-Y-4bnhphx1nmgdBkrJkI1zIBJv_digZS0e6wV1WtMhqIxQnY7LMrcagXQMeVLrPJabyYBmI_ciF9wH87KZMlZnr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخندم و رد میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82830" target="_blank">📅 18:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82829" target="_blank">📅 18:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82828" target="_blank">📅 18:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=SB5N35P11x9cccjBHuIs6C_GW8ER7HBvFamci8p8v8VaOKMS5WZ9fqHzzw7Kdg2sHy1EGzlXIRPr-oBl1yGnM5fKrmc82ubE8vzm3EYWBabp7W5brnajI0GbBOb2rrYSkYF49IR-NWsaDaqqU5nCny89AD7MnSEcSrgZayfN37nTAYDr9Qrl5QuxBOoBY8jq6mCagryMnQgY4nL4aTpJ7fXSC1DlpVdfU923M2AP0EjCYjBy1QC6FAETdmFOE2Ygk7wCTXvHEs3xQG0wzp_IKkDIEJZUiPH7TR2ZRHgipPGQg3krR0UZ-_yao9v1upvQDTmbnl0EygZttVgyc4WalQzRN5V7cZHJxDRePopekOkXooP8rDtKXX3VgQPVU3zuh8T3y5NwdrnUif-ucn-xtSeCDq8Vgtx9CUwfkkRuHWDRbTS98EEHLAE7OVClgwWwpgrJQrRPZxkex9vLZRiu_TL8EHkcFLOuSaLqKwXMuyT6PIUEGDjkmyN_EIkN-3WYnaZYuPrQSjVUnexnhqRLEuzStdcy_ct-N918-g3PtjJ8iE7cTULC9KMB5xubz2SkXpD70-BsRpA-nKZeOOTzNDo5R8OAfeYg6WKeL8I3TUTMLEYVInL1wBbHHn0AixompEZfsyWVa0hlPSEdfR1CcaMvNuYtxpbKNq_tk_GqBno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=SB5N35P11x9cccjBHuIs6C_GW8ER7HBvFamci8p8v8VaOKMS5WZ9fqHzzw7Kdg2sHy1EGzlXIRPr-oBl1yGnM5fKrmc82ubE8vzm3EYWBabp7W5brnajI0GbBOb2rrYSkYF49IR-NWsaDaqqU5nCny89AD7MnSEcSrgZayfN37nTAYDr9Qrl5QuxBOoBY8jq6mCagryMnQgY4nL4aTpJ7fXSC1DlpVdfU923M2AP0EjCYjBy1QC6FAETdmFOE2Ygk7wCTXvHEs3xQG0wzp_IKkDIEJZUiPH7TR2ZRHgipPGQg3krR0UZ-_yao9v1upvQDTmbnl0EygZttVgyc4WalQzRN5V7cZHJxDRePopekOkXooP8rDtKXX3VgQPVU3zuh8T3y5NwdrnUif-ucn-xtSeCDq8Vgtx9CUwfkkRuHWDRbTS98EEHLAE7OVClgwWwpgrJQrRPZxkex9vLZRiu_TL8EHkcFLOuSaLqKwXMuyT6PIUEGDjkmyN_EIkN-3WYnaZYuPrQSjVUnexnhqRLEuzStdcy_ct-N918-g3PtjJ8iE7cTULC9KMB5xubz2SkXpD70-BsRpA-nKZeOOTzNDo5R8OAfeYg6WKeL8I3TUTMLEYVInL1wBbHHn0AixompEZfsyWVa0hlPSEdfR1CcaMvNuYtxpbKNq_tk_GqBno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Send him back
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82827" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax8UpIazq-pOwWCy6sf_Nsi_lc32u813Hgiyw5MNr_S74cqbGyIpRDAmZeQDd9APLfo6aNDTWAqgBlhFgc5BbFyebHhNKoAlU2JO327AndxayXR7z7X7JBQZF4z8D3_8j48Q3-KXXGyoE16FxkNJfL_ueqINYjQZAsf3In6cRImKV8w3wVgR7SK3MsoCSqvxLD9AUBrUQ7nfOSipkcksBhAEuaFchaJJa6riWhbZQoW7jhQEaFATQicSlYvr22xF-CRTaoEymhjyIC9uRWu-MxjN9JHAbiTo2wd6NKU6BLpC3zgioD5-lxFQdt-nogdqb48z89Zur5aa7sB8cW6QrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g9
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82826" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuo2MMmDMDfa-om8Zv03ZTT-dqRZY0kT1WEU1OrkADuM2UD94hjtufLEbhNguFJp4NVaw4fFQ5FiU2fkx_DRbZbDVIh36hDZX5qhmuTLTKTXupAyTu9fS9mxHao725gSZ4D7f195WCZzzbGDlr4kzCzd3M18xlav7TaqXUseTAbrZ55SIjKYou6x3_XrV3bQBiSMVuluz5CdL6WLFuPtXvnX9OcH5MrsrJfS3JXl9s8i3DeI7zihJJwxKk5HJW97P_GuOEffHmff8iSpONvXOZINtwxWBbH7_8UgzJ4j4Dlbm9cbAnXFgpd7FIQSj5TuILCbLEnPkQ2UwyKY6nmfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش اون گوشیا رو بکنن تو کونتون که انقد تو خیابون از ملت عکس و فیلم نگیرید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82825" target="_blank">📅 17:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=Yvf2nUeZfMH2QYLT-LIYAyBvk_u5wk1CpYzq0BhveIOYlNQsP_ipRSpYflSCxJKDtVKlWSr-tGzX9PhtGLjyEBzq_2F8ZB8fQ5XOFWOfdAxr49oa-707D40vyEfu8DC6pXQzyTsQ1hLKGzrksrw2kU3XWoTrlX126v2gexihbK_BmLAZP6JurLmdMVdJYxsMfkoEuwLE_eCiHRh-BYe4zeohHjLPry7tLYJBrAKX4GsxdBu7fuQ6N2J16SMRo8Ex1wCnTKw27KIyn_ErUBmkMOJ7qfze3SYegVILMPbQKI3Y6t2EQ5E8v_A6FRezSlxcfVb1C8OP_hdIKhITmRjZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=Yvf2nUeZfMH2QYLT-LIYAyBvk_u5wk1CpYzq0BhveIOYlNQsP_ipRSpYflSCxJKDtVKlWSr-tGzX9PhtGLjyEBzq_2F8ZB8fQ5XOFWOfdAxr49oa-707D40vyEfu8DC6pXQzyTsQ1hLKGzrksrw2kU3XWoTrlX126v2gexihbK_BmLAZP6JurLmdMVdJYxsMfkoEuwLE_eCiHRh-BYe4zeohHjLPry7tLYJBrAKX4GsxdBu7fuQ6N2J16SMRo8Ex1wCnTKw27KIyn_ErUBmkMOJ7qfze3SYegVILMPbQKI3Y6t2EQ5E8v_A6FRezSlxcfVb1C8OP_hdIKhITmRjZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشآمد گویی فرشته حسینی به میهمانان شوهرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82824" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82822">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=gT845HqaIe4uF4lEEm5D5jNSF94JiTGz5k7N4UZOLFggShiyZol0yAbKbGIn8NSGAFAPLnO50ZjXQWCJgwrAc-4I1t2cpfFRyCaWFMembw8DMJ-WDweweE5-5j7yEnZV6HbIbxqjRzVncnyqJFdqtIH9swffxDxUbDesou8qOb1rEqDQ8TodOGjt4ri2qdf2pXyE-6h3YdHjdPdF_E0FVHFlyYrsa2XgG5IlX6buE2N7wAJjKMMJ-9QqRhxD3L_TlDQVaaKHMtYPZtfFZureAvKByObPn9Xigpky0hcKZNrw_3mUV9GpvXF2ZbCqt5s37X626rTfzX3oRcGYj4uy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=gT845HqaIe4uF4lEEm5D5jNSF94JiTGz5k7N4UZOLFggShiyZol0yAbKbGIn8NSGAFAPLnO50ZjXQWCJgwrAc-4I1t2cpfFRyCaWFMembw8DMJ-WDweweE5-5j7yEnZV6HbIbxqjRzVncnyqJFdqtIH9swffxDxUbDesou8qOb1rEqDQ8TodOGjt4ri2qdf2pXyE-6h3YdHjdPdF_E0FVHFlyYrsa2XgG5IlX6buE2N7wAJjKMMJ-9QqRhxD3L_TlDQVaaKHMtYPZtfFZureAvKByObPn9Xigpky0hcKZNrw_3mUV9GpvXF2ZbCqt5s37X626rTfzX3oRcGYj4uy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی جدیدا تو اینستاگرام ترند شده که مردم  میان میگن قیمت خریدشون چقدر بالا رفته و آخرش میگن: «من اصلاً ناراضی نیستم، چون اگه ناراضی باشم میشم عامل موساد؛ پس من خوشحالم!» بعد هم شروع میکنن به خندیدن یا رقصیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82822" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82821">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBDCUIBhuvi9YlPATw6a4Krb7yRtIoydbdHLf6Iw7V-F5mq2fAFP4IOiSW-oVw5BCXniIeIGc9rBTyaQDQ27J3WHY3cNfYVtzo7scJG2GlyTtqhRAmtdW02WY9tbdlvGvjS4PQsMt72yzQxLRnCEI_IZ1iWI-AeC8Lwvn7PzlGerHVMxrwKWeh3F-tAjCm3nt0xJqjn7kEXoZHMVYPYGtE310WFygdthnKtcd_RaMGvWEIizSc9vk73mhAaq_uk6a_Nfm4WVXJVMK-pyPXWpj_qZSHIbD2LcS21vBRS4p-b2TuoKhTp8ylZySVM7GLIhcxvg68PRUUuO_Xa3Sjfchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون لحظه واکنش پی اس جی که تصمیم گرفته امسال بخاطر تنوع سقوط کنه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82821" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82820">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVutIaeoB98qFT_fu3027kXig8AIOrfrpty9HsfIqzOdKUnscEtdlLRIgeg5mSL94kMbRQKGJOl_DTq-V8KQR9zQB9gxhcZ4VES31AvHwE7iGFZgjZXc-ZZXF1VGY3WqFxqydizp0dNesEA1yXMw-ilPTFcRcgDVuuSogPUyFY2sr3BIk4EHq40xSP5WKO2dQcQ1yz_yw3gJK2RPsPXuPYJ17PMA6QQAwNPg1PxcUVXiHEuf4nQTLTozwEmLneaabzf3tyuFhNYjKI_A9iQ54WRCRrjmpgjSCihlo9bNOBEEYhnlNszjxZp_br_jS5_Iz4fNI9Usk1e7h7l6ZlWimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوس دارم بدونم مالک این برند کیه و به کجا وصله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82820" target="_blank">📅 14:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82819">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">روبیو و ونس و امثالش کیر بسنت هم نمیشن حاجی، یماه نشده ترامپ ایرانو سپرده بهش فلجمون کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82819" target="_blank">📅 14:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82817">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbkBa3MdZbm2J0gXi07XU_sRNVlNaBs2BeTTeZMPGUPVlL75JV6cqQuE_gB6gCBZRAMJ5pHfg1UO0HHVE-Qs7vWoWMMtFSb17xARQhd0dFPiqoouDzbMG3B2UvEWp0QzmRfK0ygTr9U_Rm2S58sm5dB5GY1ZClVdDnYEJeU3klGJVsjImYLF0lQL_QAvCwvSEg750W-PAH1O74DdnarglwO-jRdWEYQYHSlfW_5iMnAbv5-cih57OHVsut6_ubdHbcPa2cjgEd1YRpE5VfxS5JVoo7b2JoIvNMWJnzzb16Kl36o2_KsRbPJifyc1SyUNgb7X3ObH04-swXxUKUGduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnEDy1cx9Tf8r6B1w0NpIBDQVQvOJ4XDWTeyUaAsM2N40-gJ-PGegB45MRL6ip_D9wyyNodY4O3F9816Z7eeKoxU8bAytXuScfC4yNGsEZroGpdvcs57pmoQehAERr3g9ChjuPaUzA2Uuhw1D8CEql_cemvUpINlCtDIXjOly0MkElxskDwd7Az8fsMWGKGpvo8Vi8qbr5xHgOuF29Hoi_pbgopPOUfx1L0CU-JKYErgBLVURi3Wy6yZSMwOIVwPTpUvWQNF5sYEo8HDtpEtK7RSXZ2jadNwD7LV9laiVUPQHj_QF835BjZcewA0hLxxVbxQlXuxP3LKXGVblh0YMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسایی که بیشترین فالور اینستاگرام رو دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82817" target="_blank">📅 13:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82816">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این گربه هایی که صب تا شب تو گپای رندوم میو میو میکنن بیان براشون گپ اختصاصی زدیم فقط اینجا میو کنن
https://t.me/+CAwWLYMxGAU5ODU0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82816" target="_blank">📅 12:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82815">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHPG5fEQzTPtl_5ta8tv8hVCDXcXhwbcsmdXzhSint6nVMtIVp6gtLcl0DEEjAPBv3wzKOPGS4Yl53TqWhLEk7BG4AjbGhkzx54bFvnEcJiNShA-AgWxcTa9LBWT9ZI0RNfmp0VNPPxbyPwmvGMeAfxIzCC7kbhd84kpPnLA2guLu948MMwqIrb76IWFZqXxkW9ztryKG18lEhX4edvWsX5BTO_eUwewhfvujGZqRh7T1RPsIGayaRQvQHyzYOT8wQTTM55VTBweFzQpNbiRPs89BUhvppGoCg-zNbdFQLYFKeqBDCMkOmdNUp3zbxnixN7x-U28HOuQqYs4ptYNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من به شما چجوری بگم این سلطان قیمتش با اف ۲۲ رپتور یکیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82815" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان عزیز جود خیلی هنر کنه میتونه با فرمین مقایسه بشه، انقد با پدری مقایسه اش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82814" target="_blank">📅 12:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS-cvyAV3I9rgpc-Qn2lsgTDybtRlUuWNRm0vKXu8lYFT19bKa4_qhmbDnpRxhMfUCSuf57aZfcXTooeknS-ZabDaRdZpGi0ZgAU-HwFwtW9D3oiBscwzmGBuPiR6CwSXPSB2pmC9DmpGc1az39vkn8rSXF44IltNrCMusSEhH8BJtLnZfD1JdSoE4XlfzAQs2AhiaMyL2H-2L5Ly5l2BJMCSqxEnWjWwKOPI04XW2ueL8R55AFvDo1hkAK0sE45bhIPryvf-k1se3_szUahRQaxuwChg0hhwXyeoYN02IBWQqpcJ-tIPGsym70s6IRjKuWhkT2z8Tv9xOzHAo_XeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میترسم از خونه برم بیرون بیگ شگی بیاد بگیرتم ببره باهام فیت ببنده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82813" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StcS9bd_3rbEj1RFwmyh1Pa_zTk9C1rx5x3jMeTNMc0OlV-_v4on3C_-JuU1Hr2pxa-thYSS0uMubxBPFVOD4tA9K5-C3M3NHv_JLsvnyrYNFy-85RtmHKwGL_xys9FhpJJHsaaR3C3L3_Z72Vq2pBwbI92G2kff6r3YHaFHW381GHwJpP5E49GbwY_rPS_RXh_tnZ3AX0pM9p3eWdhRA3Lnj6vYQ53hPUd1r2LUlz7zNc28rImfyWMJy9d_LvR76FIbCSUkUsf0JCpi0n9V5u_KKaLr517RAaCaCThDpWnDi6s8jKCQvaUo-MOZTd0C2EfHfqnbXa_2ywVCwC0hPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی این بنده خدا رو از دهه نود بکشه بیرون به زمان حال برگردونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82812" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82811">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8ZW9OEfIkVohJ4vPb3ERsFgHfwNjNL92d2qMxmqETzSgR_t7S2oHLVIn22qSkv-NAfrG6gugUnq1kOtetkQDZlYr3VyZTzIu2SNjb4o0SpEhupzpd_vGa72gdz8OpTs7rlyNmHt_N82WrGtK9KxqRjUVNOpAWNgSnBWyYw0XtBmLI4HpxAXWs-o_9fsuoaYPbBOe_Zo3LQTzesy1PnMn6CEWnZx6v3AuETEUcsZgdQ6hB35KKlRMv7Pzc-NC_Pibl2gBX6Pnk1oZosyq-5_x759RR4tEVwx3V9uiH3Aw_qi-AVmI8-AknUX7edGzi12qThM0l2j5BPzfM9QUULY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82811" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyoaU93alMbjiaikMrlhFNjyRRNmBQuPN-87eTsu1oAxGXGtHXzCK4Nk8QrzI3PuULBOH0MkgZJhJSAzcLAT2KshhbisUZV67qUWM996Jfg22LhF9le5m-Vt7s4nPDTJL3FT14JPnhjGcSm6haGfETdflB3Yn6mWSjdRv4yPFZWXBSG8cLD5Osh451SLJ--iC00M5fzkUbI5eXFdhfqJZwfwXH9GxIQbxGK6cu0AFo9yvwaf7PF0k07ExhN5_hB4bye8YJWXkncQTFIF3gDkyVwauMHimvty0nNajhla0yy9w9GDFdKQz1FqtLpto5PFBSRcJtye18GzoWPztjGP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید خانوم منظوری دارید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82810" target="_blank">📅 11:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eub1tsWjYyja4aqUzlTHdUOlivNFTPJdDNV7eZ2NZDnlrpwggd0u51VbR1352MgyHvnwAbA6xqgR4UWslqPaiXDuApdObWEGwW8NPegs8cYaSCbGkNMj0fe6Ku5PJ7FoOFNBHg2P-736VSTjmm7J8DtEm5svrYK5-_ITs7-lr_IwyHrQD9OWsr_kIcuHBtSOhXD4pj0rPXXp3MLSUDEV9DgoQQwdTf1X--hVBNzWaDRVuDh7ROSu7Bk9CRcN4sS82nAPTjwIwNqGZ9GdWLJCflMCv04aUXXEqIhhj-td2bVPTdnX6gZ9QMf80K8qFeYHYVzM10uUJZdGTak0vY5XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیلی که باعث میشه بتونم این مدل مو رو از استاد بپذیرم اینه که پسرش اوتیسم داشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82809" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">میگن تهران زلزله اومده، ما که حس نکردیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82808" target="_blank">📅 07:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82802">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجددا صدای تحویل ذرت و جو آمریکایی در لارک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82802" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82801">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#فوری
سازمان ملل:
این آخرین هشدار ما به تمامی کشورهای درگیر است. اگر دوباره دست به اقدام خصمانه علیه همدیگر بزنید به صورت شدید ترین حالت ممکن نگران خواهیم شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/82801" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82800">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اونایی که میدونن امشبم جنگ نمیشه ولی الکی وانمود میکنن جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82800" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82799">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تسنیم: حمله آمریکا به لارک ۲ کشته و ۲ زخمی داشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82799" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82798">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پرتابگرهای موشک کروز ضدکشتی سپاه پاسداران انقلاب اسلامی در لارک هدف قرار گرفتند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82798" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82797">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آمریکا پایگاه سپاه جزیره لارکو زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82797" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کوروش یه چنل دیلی زده همه رپرا رو توش جمع کرده
بعد یهو یادش اومده عه آرش سرطانو نیاوردم، رفته پیویش لینک بده دیده عه لست سینش لانگ تایم اگو عه باز یادش اومده اصلا زندانه طرف، پیش خودش گفته خب چیکار کنم حالا؟
بعد پاشده زنگ زده به زندان و صداشو ریکورد کرده گذاشته چنل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82796" target="_blank">📅 22:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82794">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">می‌خواستیم به ماشین ۲۰۶ برسیم
آخرش به دلار ۲۰۶ تومنی رسیدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82794" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACDlW90YyqGOWqpKbVgm8uq3CF2Nf4V3t2vjJFUgo_Wsf1JS25hh6CNohAVrvKn2i9CRLkUiu2-vpr-Vd-FKn_Fzaul37aEPhWotSZzycnZ72MNlRhBd5ypn5dIT86BeZsofiJhIK-x4cUHfBwGvDjfXAJq9dVVw-KgMeySxoR_HcYiV_YOWCjSmW0Mcukugq7dR5yREOeNrn63GYgM9ZcfM7gi4Jvu1QCy6QO3DGRzkdCXZE57eyqXF2mRUg_varoyYPJLiWEVmL9mBfeU3xJwE9O9uW_v0Z-NnmUd8nP6pjpuFzsFzDlgCSu7p_Qu1rEmOss0EKXBUch5pCwY0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82793" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82792">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gharibam Bahat</div>
  <div class="tg-doc-extra">Danial Moghaddam</div>
</div>
<a href="https://t.me/funhiphop/82792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82792" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82791">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clM9lJXFrouibTPsiPTtSwqaEWwlXatOg2Fy5NU2zo_BY3RYyagXiw5KFPKcbBjdrr0wo_fLHQ8B-FrGkaSkazsMEj5b1Ii5ewM4IsgzmyhT92W0Tds8oupShmU6wGcZx7B6RYZFevbMT17PFVnrdxhsCwLXGcYk_eO3dV8tHf8sTHGt4gGP6VZiI8RRWYmW0au_VGFrmmaEWHgZs0Q3g48LvWCNqdgPMwhbLhhDDtx7CrVlCxA-KTz-tjfI4n1Pb6HtSCkOBGVH-dHom2XzycrWAzhKXkCD799ky-txW-ep3lXImwc6CUkVVJHrsrWC2sr1hmh1A2ONQkdYWqOY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید دانیال مقدم به نام غریبم باهات
از آلبوم خط مقدم منتشر شد
https://t.me/danialmoghadam3</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82791" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82790">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82790" target="_blank">📅 20:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82789">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=DnZOVJUpXqwJBhhAvDbGLo8tosfLRRHyqS58YCX1mK7df1RaXTL1dreyhbxgX70W_krAx8kJVA7sqRx1-2ysTsX3zrUkL28fuA2-_Rjh3vQRakw6oG-mJa2A6f9qQ2aypBBmJlpM_j0Kbv2wmLTkjn7lvmlNkXFdMINR9VcayOtzyVOGTbXNwHfUiuQJapG7Z0w-ck9RLhAvvsbN0Jwzc5HaCsqfmXt-QbBXGoMhMhizqICWYf3nzl-jgDxAcguSLBYqg77nLA1wIqEXnjVXRsLy1ZPBu81olbiApkzXaaxtRs1SVk97D7Fu7Zz9mCbpeYx7zq4LPyiJhrmODKAyXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=DnZOVJUpXqwJBhhAvDbGLo8tosfLRRHyqS58YCX1mK7df1RaXTL1dreyhbxgX70W_krAx8kJVA7sqRx1-2ysTsX3zrUkL28fuA2-_Rjh3vQRakw6oG-mJa2A6f9qQ2aypBBmJlpM_j0Kbv2wmLTkjn7lvmlNkXFdMINR9VcayOtzyVOGTbXNwHfUiuQJapG7Z0w-ck9RLhAvvsbN0Jwzc5HaCsqfmXt-QbBXGoMhMhizqICWYf3nzl-jgDxAcguSLBYqg77nLA1wIqEXnjVXRsLy1ZPBu81olbiApkzXaaxtRs1SVk97D7Fu7Zz9mCbpeYx7zq4LPyiJhrmODKAyXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82789" target="_blank">📅 20:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82788">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=Ykaucxu1jm1oXJ-svPBzyIRq7S6IUp2A-kug--jDriCbCU6tNzpRCO5HM-477MCa-d1Y1rgFdltpAO23F2tnIqPpWEDhz09SUIQVY9qv1cwXZqlk-nVON3HBQrQK6utuaWqjgPgcOg0wOYzLLLRa2GI5Wch2u7ELdOWsQqaQQXyMsOtHwZUES6YJAt-RU8F-8VpTnCUXKQpPhCsLZwa-13ErVwgQZvpyBwEOXquZNvd3bm0V8dgCH-bDYqOydaQgm8mEa70EtomUMhCQdr-E8GyOQf54yeIbmjLT-6umLYiEmlBBGkwIq9UO7R2YIvrRSR1D_7P8gKhwmaqLbr5fiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=Ykaucxu1jm1oXJ-svPBzyIRq7S6IUp2A-kug--jDriCbCU6tNzpRCO5HM-477MCa-d1Y1rgFdltpAO23F2tnIqPpWEDhz09SUIQVY9qv1cwXZqlk-nVON3HBQrQK6utuaWqjgPgcOg0wOYzLLLRa2GI5Wch2u7ELdOWsQqaQQXyMsOtHwZUES6YJAt-RU8F-8VpTnCUXKQpPhCsLZwa-13ErVwgQZvpyBwEOXquZNvd3bm0V8dgCH-bDYqOydaQgm8mEa70EtomUMhCQdr-E8GyOQf54yeIbmjLT-6umLYiEmlBBGkwIq9UO7R2YIvrRSR1D_7P8gKhwmaqLbr5fiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور ارشد و جنایتکار و نادان آمریکایی، تد کروز:
من بارها از ترامپ و دولت او خواسته ام که به معترضان سلاح بدهند، تا مردم ایران بتوانند با کمک سلاح، کردها را مسلح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
هدف این نیست که سربازان آمریکایی وارد عمل شوند، بلکه هدف این است که مردم ایران این کار را انجام دهند.
تصمیم‌گیری درباره اینکه چه کسی در دولت ایران باشد، از وظایف ما نیست، اما وظیفه ما این است که بگوییم دولت ایران نباید توسط یک حاکم مذهبی افراطی اداره شود که از آمریکا متنفر است و تلاش می‌کند آمریکایی‌ها را به قتل برساند.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82788" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82787">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dknOQx8ojOAON3X_hfEDafjDCEhqP4V6ls9qLrA9XvnKp3rKw-VqKf97OQ4Pv5GvYwisubiWxHyAZURiEZcCY23uQ9CKPWtx_DBGNxmiAcBl4sCAQ-xh6935o5dqN6xHfp-EL-Riv2Ilcz8IuDs6-Ai997oMB5tHZmE82yEaQehbwugYQvQXvcNtVANlRheG584ieui_5EZf71FxhaL6rctNovlB0sdYbh59mG7fZwi5PGjlK2JplMMXCusBDkUxbe8gWxESowT4gvHTT2BPDoDN8GkNYBk1cPrqBVE4CF5y-C7wLoSa3elHudhUziyFi5ON-XPoTM4-UhT2LvjzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82787" target="_blank">📅 20:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82786">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzzKY-g_G2tNm8DeXrWVBZr_znDbaTH84FDrCk66KXNlIc5RD8icc6vZ3P-fKhl7KWikqIZ-raNUwzeee33KcsY6bi0Q--o_YR80ImSkvSP5PjV9GoCG2vo_IFJ0CMA1LtC8I8lMCzHEd7z66u8Wyl3XCBHrF6fgSkC9ABaVRlkue0PNascO5_jZ2J2S_v_5CDLNWCE_rhkzKg_zYK3i3SiGgjhTqaAYMlFpsQTn6l_DAkqsefPnkyRMribua3hwDy8gytPvnp85cdE_8dYi0c6hYg2T9rUD1e4zIBx3B_gNMq-fldA1cQjRE8DYoGUDeTXkBBdJQgDNcrkiuE8Bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه  مشتی حداقل الکی میگفتی میخوام برم مسافرت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82786" target="_blank">📅 20:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M14du9pZhIS5eQOwNl28TuGa1Gd9mSrjrfleiiFqIrovoLyKigwZ5C_lflPp52MlrRYRIVaah37aOiurNA3EmDUkMOBPEFOfD3WVcmhYLOanjuBavTLd7FuV7UFpSPMtYL3n9wldelkYV9Clb9ia07BINRfaZ1nCoQkw9k40cu9JAci_6ETLZK6IuLcGMi8gAN0o2Xs9I_VwF00hoGMwsxAPv26m64FFrg2oCL_7-uKHS244DuY9ICgIZKo-PxkdAr6YEhmxhwfRVF_TE5hN1YWL0CcHnK8LHjusAb59OLF9XojRDbxR__jkaPXGoxH2eD2IVsEAiFGw6zmh0006yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-BVT9ziLOpcYl5Gq6wI-lVvB0qcmC8DS5fA_nUwm244oWoonv_h-aU-im72vQgqlxMTqmKgTUSLRzaxQH-GAYWXSvOdlxYYytM0rxjZPUnuFKM10thG1h__7WA5Fkk9plfc7Cm5fip2dhB_AdEKnPZZZHMhYRt3JuFw61NI-dlKLxtWJRa8qeNaRp59v0ePx4cVs66yJ9Id4dWPlFMuyFxm3L2jpj2sap2hL5j65ANaGNSTRMUoJIiByfVlDYz0tg_5HvKjeKH1KBRVLNpRoGv-gDUzTAvqqprLraqNtSFPFY3yXl8NDW0L6FNcTklwZ8KAl81Mm38paiBuBgld1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظارشون اینه مردم فتوسنتز بکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82784" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82783">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvid3ARQogd63x83A_g6eDcbPYybX-tSg_87F7vzyn_Q4HlgE80UZkvHTVBliSLl4wBhPuwR7cRQF9YonylHbMQ1gPJu51LL_F0dHptzkGy2yMZERgdpZl2WCuuBTGDs_dC_LRUFsLUQCqjHPgfpndABz0Zc_4sI6i6cyF_DUo5iRquFWI08iK0pn2C5hIPZT1CJMN05L9Cw-q7OhiMBdp-5mzQEYEXU2LKAboNAtmU_4LXPxFCSLtgSM4VPg9oPfGwKEHE7FVcujn3d7KO61G44MBsK96QsxctqhPtyuRgER8ha5lxj1IAqPp4pKjh5p186o7fJ2-KydZpD0BvQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرگوسن فک کنم تهش تو همون الترافورد بیفته بمیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82783" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMsU3L1nLWpVwWe618k5fKrJGhCXOR0GFDLxcKDfcNzT24xdOfj4GP4mCxoopldrPsyxFEXAkoyMt7dL_zfiIH2Pm8xKDIk71vVonR6fwbDJOrPr3Lm3yEoMy2d0ZvknSqaqmzwmtzX6CzLEYVoXH0Qm5PnrgSEXqsDoioOKXDocSbwSL-h9N5Euad7JQ4DC71Y-lmLqUl5_UWLr-itOeL7jYz9EQE4xzCzxSE4NNXniVQFbnVzsDCHyLoxw6b7gArK_MNMpGxNHq8WvjY1K6i__SqTVabGvsnBsVQY4AhWEkgJoi21NgBNna9AOS9kNN0MQbLyktHgSaMcUXEpPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFOmV6rSHZvEjwOzCSQPULTA-wYIH3qqfNpMHQ-mtGaMcF-MwKzLDwZ48851OY_NqSwLCsp2nYhVF-SEeZYtUn84EgeXbi7Gqo_xGLjKE7Ei2-V3v9V4_mP72viWqXgDNsxYkEMUd7oSbKyXH_wVjsBAGgHqlmHGTHGYC7rBM56_9J9MMEs2-CfCszTo4ubwu4gcJHanPRZcBloIylaEJ-Bl7V3A_rDCUpxd8q0bZw-UJ7pqzW4z73z-8vt2Bd_NpdrU6u1yeWGaf1lyFLOXsaTkOaDdKUINBjuKATfHdcr4fakD8lkQtGCXAje1BFSWNyahtvRi_n8ry_lKwBmlYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی انگار نه انگار که یه مملکتو بگا داده و الانم تو یکی از امنیتی ترین زندانای آمریکاس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82781" target="_blank">📅 19:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82778">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کی میخواد این فصل جلوی رئالو بگیره</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82778" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انقدر گفتن تحریما تاثیر نداره
اولین تاثیرو روی رپرا گذاشت، همشون دارن بلاگر میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82775" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjHe0-itg1NUfDT8eBpVp8SUuY5oDo3Y7sDz4eTHhTPfPWFunsYK48Vz5rW-k66eTQ2o2foN_smTiRdcUtTiUckSUZ1rj05fW61HaGxqrcUZnV6kGRagyECA7uBgcXFI7ifEpes7J8ckUfJjAidHIsgovg872sZkKyg28ir8Td-RAJWjMoeclqktkkb7gDAJIUu99myQRmaro3OQUK_ss9kLYUHlwTvgOLZW9lC1o_7PCML0eEAQAvzW2f7EZTChGS36qEr0KpHzzcPQ3OSJji82SekKYcbOG5JvnVoBHdU5_jfsytY8OJ6VfivSmZ_2cmqUKHuNZ53UyYi097aR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژابی بال و این حرفا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82774" target="_blank">📅 18:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdamV4EFrEF5uaysSeVRB4yvoCn2d2UKE26Bjz1d7dW1fq5G_76jWQmFFnRAG5mOKh-2noFscnsXuSi-KzcHmv289WitJ9aqMBfGI-pyGNdA-obmUD71cH5rDp7oPseRghANWiedJtWSrmGl86T1-pRk7InUtX78kl9uYbeHJcR5Z5kS4U_hh0H4paEnwoMc1FKzDb5tLWvVtCaRMcs83zlC45uHW5AuyJnTzE_z28hc310T-OASAYRvnIIgYjVdT-4DKf2yX3dVlQ8wLE49HmA3zG1TlckrW8wQXA1tLgD4Xs5AkCZ-T5gH7Q2Nfrs3USzpsvr1_6fDaS1gNF-4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال داره انجام آزمون تافل برای ایرانی ها متوقف بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82773" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بیگ شگی بود خودش ویدیو میگرفت میگفت بیا پستش میکرد، کپشن میزد پول رپ پارت ۷۲۷۱۸
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82771" target="_blank">📅 17:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82770" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
