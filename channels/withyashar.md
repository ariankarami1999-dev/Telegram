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
<img src="https://cdn4.telesco.pe/file/l7i9ShEMNxBpgF5QfIDjY2GJ8E4-CrRHYdXhD6W7H2qcODg70tjYTb_ySlYrcSauwIQqrSxr2mgZJ2UZzT6uzGqeE9EnZfglvQenhakBlSk-s-kk9Kzo5wpIN9w00-rM2C3g3TPRxoKExwM7bCnXaC2Msu5uISbr8TxpwUKfgxlhtirqYV-203aBhEruTcDz0h68o-7T4Bf8MgZewvH5_aDu_Tunpee0sDRpAQIl9j5zghqa6OeX5No4Idq4mqOoDzutWO-TSpUt9VnVL5JqToxyZaEjK2-TBaPIV3ejCMQj4iC9gtWZP7BPnPnWUah09wLw75tgMKJhZ2ApIGirlQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 407K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 17:24:51</div>
<hr>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad58b44d3.mp4?token=IYCK5dYPVAkurTWwe_8o56LaPyX3UXGR5A-H1LmzSVLLTOK_v_sW_9YdzXzFhvFFci6cGoDPz8R2KrOU_otsE7tXTBtYETjzn7Ou3n0bg2pfOzugyVy3fwH92YDk2TTvyKRAlIZQzUq2O-sx0ewretZASvlna2Mk663Vg7LfC7-F2c5zrXSIAb82SvYcpYv_3ZqNPHr1HJ7LUyZ8R8daY_JEUBs5v8F2aGzCqaORviyZ4HkcR0lWk6vu1lPoIQu1jr99LWEnUIi9Dpm-fgdS-0bzENRTbczal83CQOPgvc4u-9J65dC-RAQ7V3NPL7Us0NvQtYm9K40xEUvtn6MTug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad58b44d3.mp4?token=IYCK5dYPVAkurTWwe_8o56LaPyX3UXGR5A-H1LmzSVLLTOK_v_sW_9YdzXzFhvFFci6cGoDPz8R2KrOU_otsE7tXTBtYETjzn7Ou3n0bg2pfOzugyVy3fwH92YDk2TTvyKRAlIZQzUq2O-sx0ewretZASvlna2Mk663Vg7LfC7-F2c5zrXSIAb82SvYcpYv_3ZqNPHr1HJ7LUyZ8R8daY_JEUBs5v8F2aGzCqaORviyZ4HkcR0lWk6vu1lPoIQu1jr99LWEnUIi9Dpm-fgdS-0bzENRTbczal83CQOPgvc4u-9J65dC-RAQ7V3NPL7Us0NvQtYm9K40xEUvtn6MTug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سوریه یک کامیون حامل خیار که به سمت مرز لبنان در حال حرکت بود را توقیف کرده است و درون آن چندین قبضه گلوله و موشک ضد زره کورنت پیدا کردن
@WarRoom</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/18739" target="_blank">📅 16:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">در منطقه بندر کویت، صدای چندین انفجار شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/18738" target="_blank">📅 15:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b511507b37.mp4?token=bbMD2i89497YDcIJdxCNWC9JLTK6FQ7DlHnIsoI-ZC0_NdwnNYKhMvnIRtMbz_ovrV76IOQAnZK-K4EveX-8T_5XWfgr3GDxppksAA5f4DOMuae-8AldxUrEVW2LHyKxpxR6kAoKRNcimA7rc0kgjERUkQ6t_IoLUrDIgPnMH0QvxmY5pHQui_xe-y31AUq9ltOCW8iL8zYoPdf8Sb9M8B5Acdbavc4eMztjvpxNU5Od6EsTmc3bryZYjKhWyPlBapwIxhDfMj4RvPgJcHNXlsF0ngRzaLKuLfGgcgKjCE3fdLxR1q9hmsxxIfMbAE5muajqOcg6RnVUD8NneLYHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b511507b37.mp4?token=bbMD2i89497YDcIJdxCNWC9JLTK6FQ7DlHnIsoI-ZC0_NdwnNYKhMvnIRtMbz_ovrV76IOQAnZK-K4EveX-8T_5XWfgr3GDxppksAA5f4DOMuae-8AldxUrEVW2LHyKxpxR6kAoKRNcimA7rc0kgjERUkQ6t_IoLUrDIgPnMH0QvxmY5pHQui_xe-y31AUq9ltOCW8iL8zYoPdf8Sb9M8B5Acdbavc4eMztjvpxNU5Od6EsTmc3bryZYjKhWyPlBapwIxhDfMj4RvPgJcHNXlsF0ngRzaLKuLfGgcgKjCE3fdLxR1q9hmsxxIfMbAE5muajqOcg6RnVUD8NneLYHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
🤣</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/18737" target="_blank">📅 15:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بحرین رو دارن میزنند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18735" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ممدانی در مورد سفر نتانیاهو به نیویورک: "جای او در دادگاه لاهه است ، ما در حال انجام مذاکراتی هستیم تا دستگیری او را محقق کنیم."
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18734" target="_blank">📅 15:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایرنا: در جریان عملیات عمرانی نزدیک بیمارستان دی در میدان ونک تهران، بر اثر ترک در انشعاب لوله ی گاز ، انفجار رخ داده
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18733" target="_blank">📅 14:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی وزارت بهداشت ایران: در حملات آمریکا طی سه هفته گذشته، ۵۰ نفر جونشون رو از دست داده و ۵۰۰ نفر مجروح شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18732" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee2040af6.mp4?token=e1N2TZWIgSeuSwNXOJI1PQukjjaMguRGSKxLBWRobe_mbuSpGFOKdJNezDxENLN74uhEc5_rQ51E_95fnnu4iC-_GWSjGbwbACNp55NyayeYMUBYLKVANIC7uDoq_oqbcBPJp4gL8pSAtL994EXz_B-zmksorES1w4hNv5Lq9jp9AO7ecbbtOPAf6UkSXwcqGOmn89t8_XqTdS0B5R-j4KxxdlppIWTBehrRH74st0A8T7FVTkeadoSOGoXD0hj6iMG2UKyU6fuSuCGoQAI6It6qMjpseBaApQzxFcMR2X3k6wpYacdFfxwnumTnj10h9MTXXIdR0KDt6OWHNhCvWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee2040af6.mp4?token=e1N2TZWIgSeuSwNXOJI1PQukjjaMguRGSKxLBWRobe_mbuSpGFOKdJNezDxENLN74uhEc5_rQ51E_95fnnu4iC-_GWSjGbwbACNp55NyayeYMUBYLKVANIC7uDoq_oqbcBPJp4gL8pSAtL994EXz_B-zmksorES1w4hNv5Lq9jp9AO7ecbbtOPAf6UkSXwcqGOmn89t8_XqTdS0B5R-j4KxxdlppIWTBehrRH74st0A8T7FVTkeadoSOGoXD0hj6iMG2UKyU6fuSuCGoQAI6It6qMjpseBaApQzxFcMR2X3k6wpYacdFfxwnumTnj10h9MTXXIdR0KDt6OWHNhCvWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸ موشک در آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18731" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qgj6U18QdT_Np0xZTWB3VHh49VKbHQcofU-YbY4gi-erbhd6Is0HLVfWXpSvoJ9VygTLW11pILC8WG8qL9QPQ0WDF8swM2ohhTC4QjRkhG6q1Thnuzkk9ftnZjd4jTNWNWfYMOcX9WEPl1hxxGCWVtJt7zbYwlOqGPTZWczdfqu1P2DdOuperXSdc-mlOG9pPPi_nXv5q7en5aibY0IyLA8PlOMiRpQ_K5FFufAoBYIHqwkiQUKzrf-8zKZL6PlwLelQ9_4bnKNmkdt4Z-HVHVObN0MaYhhRtpxkUkvTXWL8JOofwpK5TDqixfeATDKu7-RzoPY7_2TsE9PeOzIi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب ۳ موشک جدید از ‌امیدیه
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18730" target="_blank">📅 14:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الحدث از قول یک مقام آمریکایی:
رژیم ایران بیش از هر زمان دیگری در معرض یک انقلاب داخلی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18729" target="_blank">📅 14:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وای نت: 10 هواپیمای سوخت رسان دیگر آمریکایی تا امشب وارد اسرائیل خواهند شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18728" target="_blank">📅 14:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رسانه های عربی ارز قول یک مقام ارشد ایرانی: «موجتبی خامنه‌ای تا پایان جنگ در انظار عمومی ظاهر نخواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18727" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">معاریو: اسرائیل و ایالات متحده، سطح آمادگی خود را برای از سرگیری جنگ علیه ایران افزایش دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18726" target="_blank">📅 14:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKmMMq7ydrwt3uFNY5f5dz-uWUfglVGDWKgsOkU5uGxMVqqT2D2MFHTXGeGTjZTIMQcbgha-GP6pRQo6H489HXWGvWlUSvaErQ_9ahGQIKBIvUuyLXzFisaIEW7Mzm2P6cGfxqEo2ZwiMCPGJNGMAKiASThUW2UMUMJybq4Pi6p5OeP9O4utO8eLOXXyhjwIx5ny5urDnpVagGPXEKonEsRL1yyr1nlIJbcEu-FP1okweOnUeKs6YlxpPNn9gSwhPOae4pFNtdcI8OKvn9qsgwxa035pulDyCvsEvLLXCppn7GQ1VBWfjgcqK1lT9QAMlU_qxAwzD6mDpeFSFfWlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت موشکی خمین ,کوه انگشت لیس , بین خمین و گلپایگان
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18725" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسانه های آمریکایی: ارتش آمریکا همچنان داره تجهیزات و جنگنده های بیشتری به خاورمیانه میفرسته که این نشون دهنده گسترش ث و طولانی بودن جنگ علیه ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18724" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد هواپیماهای سوخت‌رسان ارتش آمریکا امروز وارد اسرائیل شدند اما هواپیماها در فرودگاه بن‌گوریون فرود نیامدند، بلکه در پایگاه‌های هوایی نظامی داخل اسرائیل مستقر شدند، این اقدام برای حفظ روند پروازهای غیرنظامی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18723" target="_blank">📅 13:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدای آژیر در اردن به صدا در آمد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18722" target="_blank">📅 13:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16b0742bf.mp4?token=BF7kdWA1yp1V__aTKeaykeBKWutY7HPekJrcDH8iST5-Nr91W1S-sGXPimZnegSE78tl3HXodcKVhbItmfauaAtkCzB4Vj4ptEhZMlM4H4Gsi52y_4EF0JJUFRfFLu3dtYEiz2BbSbU7u43Rg0Q6N6cgY9Hs_7rKz0gdc7LNjGJQLVUr2J59FN4Xs4pPqHRRMH2pRDIqmTFHqsJ4Qv8vYMKlHkEOXBYbfENKJ9_xETHbE9lhxWcLCLl4lv_IZAFvmgAf_-FlzppDrn0HvpU-S0-OF5QEDgMHbeIlOWpwLgIIaSRkDkB8MlKyoGHTar1_F5VsN0LOFSYY5hMpy_ok3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16b0742bf.mp4?token=BF7kdWA1yp1V__aTKeaykeBKWutY7HPekJrcDH8iST5-Nr91W1S-sGXPimZnegSE78tl3HXodcKVhbItmfauaAtkCzB4Vj4ptEhZMlM4H4Gsi52y_4EF0JJUFRfFLu3dtYEiz2BbSbU7u43Rg0Q6N6cgY9Hs_7rKz0gdc7LNjGJQLVUr2J59FN4Xs4pPqHRRMH2pRDIqmTFHqsJ4Qv8vYMKlHkEOXBYbfENKJ9_xETHbE9lhxWcLCLl4lv_IZAFvmgAf_-FlzppDrn0HvpU-S0-OF5QEDgMHbeIlOWpwLgIIaSRkDkB8MlKyoGHTar1_F5VsN0LOFSYY5hMpy_ok3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک آسمان تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18721" target="_blank">📅 13:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3560da63b1.mp4?token=mlydXUc64suRu-rpIsU1wJg6CkREA7Fqc-0gaBGrmLqkVmtbk0eA1ELSGt0HZ8PjASnnTEFjviGbs4Bk2nXR80v3nmnf8kFO4HV3VFyT-U4ZImC-12f4oblDkpHlw_Xllm2mP0VlxwekhHUS_aVjNlgiQRGqlg9YcnoWZXMV0O2kp8PPfxREMOietqo4KeFVS47ly93oR4YkILGNqEFSIZNA0kMpTH8bScAQQ3RrV5N_4pT6uC61-XlClqa_hV3Nkp1qWCTFAHpLWxXXuCEkgTg0Qg4iCPiU3RR9o9A-pKn2Aj_6bQ-sZZSbYhOuHz01a6_5H6AHpBMqDcfRMD7LLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3560da63b1.mp4?token=mlydXUc64suRu-rpIsU1wJg6CkREA7Fqc-0gaBGrmLqkVmtbk0eA1ELSGt0HZ8PjASnnTEFjviGbs4Bk2nXR80v3nmnf8kFO4HV3VFyT-U4ZImC-12f4oblDkpHlw_Xllm2mP0VlxwekhHUS_aVjNlgiQRGqlg9YcnoWZXMV0O2kp8PPfxREMOietqo4KeFVS47ly93oR4YkILGNqEFSIZNA0kMpTH8bScAQQ3RrV5N_4pT6uC61-XlClqa_hV3Nkp1qWCTFAHpLWxXXuCEkgTg0Qg4iCPiU3RR9o9A-pKn2Aj_6bQ-sZZSbYhOuHz01a6_5H6AHpBMqDcfRMD7LLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک آسمان ابهر
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18720" target="_blank">📅 13:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1HVWzAx0HnfzhGC66rHrDLaBhpxcMWAH31yep_4Xi7_e03Rw2cJ9W-taMCu-XZ0WRS8UOrIo8slN1A7oDiKhh7JcWQp8mA24vH5yA1JDejFOHf7EpaRNZtUtnlIXuH_OmR2040KNE6wT7H3FeDXiu15PdgUNCHKU_gf9tLpBjTIXuP5fLPL6vbmdRRpGO91jPBQsOaBBLOYUOIQImuawEONiG736vaPm_PtKVEf0SNjrbFaBTeyHRD22ci1a_942DbfXL1ctrM20WWBc1gGKqbrNa5ujfSy-n3W3coNn6Qh6LMY10XSWurlimrwxkEQyYz--Y-OHsPWVouQeRK_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک دو موشک از خمین/الیگودرز
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18719" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2573443feb.mp4?token=flgjtgzBL1nhJtfZQLGWw7rQduLoZProHwM90DsMqay86OQawqjfQ4Lh4HPCCrCki6d7n285CKC1NaNsplw7HP8IF8vT3KwIa2xid6jI_bXkx4-ZY8WLO_JKlt_KLCOy0uT0BnjSNrvuLLopJ6B899xa1P_Z9Giab1R6EQVfJgNWBvjxHGny4FUmMsFT21-xC2wjQwjHfVPndkPFTfyMkcBenfF-PxeA_gT3frtZ75IYWKLvU9QOMdg_v8_dWmKJOYS-BcPF5k-A_GjnWFFYNRqOAIfuxcn8O3IVRDvY-5SLWFX5CQjfaU1YORbOT_XzUnwpupkP1NU8jOXQ8yR3lL01322DWLiU7nQIBnMa6UvYT9IQ01iWyDm4iCNnw9a1RXnng_-DMx_3Mvae9bB9DYJ-XLvfWvgfylnRCStHWeeNQYrt-MT-Cq92047xjFMgRKEWpjwUVrQ3p46tf5isDs-PV2plWonOv4M6UYbg3lsXhooRAVo18zF0hp-zxeem0wzSIPsvxRBKdJ28_wtRH0YWcC6LUFwfKTTWS5dnSLX9ZmvfjxlX0ZcuOYJmytDs4JphbmR-G5ove7MQlTElcPzGqp0LOWNYtm4A3neQ5zLX91QTXJEjz4Jco3EATZfz4Y_JSivoXJhOPvcKw1HGEoh8KTA0RhBQsTdoZk5sOuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2573443feb.mp4?token=flgjtgzBL1nhJtfZQLGWw7rQduLoZProHwM90DsMqay86OQawqjfQ4Lh4HPCCrCki6d7n285CKC1NaNsplw7HP8IF8vT3KwIa2xid6jI_bXkx4-ZY8WLO_JKlt_KLCOy0uT0BnjSNrvuLLopJ6B899xa1P_Z9Giab1R6EQVfJgNWBvjxHGny4FUmMsFT21-xC2wjQwjHfVPndkPFTfyMkcBenfF-PxeA_gT3frtZ75IYWKLvU9QOMdg_v8_dWmKJOYS-BcPF5k-A_GjnWFFYNRqOAIfuxcn8O3IVRDvY-5SLWFX5CQjfaU1YORbOT_XzUnwpupkP1NU8jOXQ8yR3lL01322DWLiU7nQIBnMa6UvYT9IQ01iWyDm4iCNnw9a1RXnng_-DMx_3Mvae9bB9DYJ-XLvfWvgfylnRCStHWeeNQYrt-MT-Cq92047xjFMgRKEWpjwUVrQ3p46tf5isDs-PV2plWonOv4M6UYbg3lsXhooRAVo18zF0hp-zxeem0wzSIPsvxRBKdJ28_wtRH0YWcC6LUFwfKTTWS5dnSLX9ZmvfjxlX0ZcuOYJmytDs4JphbmR-G5ove7MQlTElcPzGqp0LOWNYtm4A3neQ5zLX91QTXJEjz4Jco3EATZfz4Y_JSivoXJhOPvcKw1HGEoh8KTA0RhBQsTdoZk5sOuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش و تحلیل سی ان ان از حملات جدید امریکا
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18718" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaNaYTrFui57azdoHTrwPzjD7Q5yIPim4oOBNu98YDDj6tVXhLINpa6o-xBd9Op-79UPHl65IxSM7LQHISSJfI0rz2LfM8J1krmXazjpiT7TkTcDEa0JdR_owi5-3dWgHITtC71O5cFsrhlAHdgvgeKFBPa37upbunRBcTVhGqu6jC65KPc-4Z08bYoO2ksJR48WX_6I-v--asyd3pJE1TUkC2xaaloli9XIqm-ZCq6yOtEeKfq27NHABlzzUHEdAHtD5iG5qNbOpFTS-H3b628uq_V6PXWozX5e38JSXHMdGzZWBDhRWXqcYgM3zPYHO-PRZvoW_YV8DnmPWgk0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین آپدیت نقشه جاده‌های مسدود شده‌ در نزدیکی تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18717" target="_blank">📅 11:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd0OCTX9rKi1oX7_iO4ZrMQ2XMxgEeM4kixARFeD5mUiNg8ET4Rgau2iGbA2yqQgLKl_87UhNexoWyvWaSPHQkSez6FZ-RKYM607kpHMKDo4XrEA9IWUYS_cDsH22ipjv8oz24RzTd1_QqbAmHmD5_INRcOZ2IN74KNx6NyPzpZmgPalsqbFylusGM14cKUlDQSqbmwOiI8ayzED2n7IqhvW37QDHjitS7WkmPZCv1HOfC_EBFPGjHwnUcsIpiQLrcRNsMvJsQE24qkAHMKu3LEiquxgf9rRsN8k7Dds_G3gxvdBY-ZlEBturJYCzIyzGFxbTkzC7ckR0JbYSNlekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی الان : اصفهان سمت سپاهان شهر, مقر سپاه(فکر میکنم کنترل شده باشه)
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18716" target="_blank">📅 11:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">محسن کج بند : اگر حملات ایالات متحده در دو تا سه روز آینده ادامه یابد، نیروهای مسلح جمهوری اسلامی از مرحله بازدارندگی و پاسخگویی فراتر رفته و وارد فاز «تهاجم و نابودی کامل» خواهند شد، به طوری که پایگاه‌ها و سربازان ایالات متحده فراتر از مرزهای سیاسی تعقیب…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18715" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d53dfc1b1.mp4?token=JUnR6ZbrcNxBe3BLre0F_EMG8q5yNJuMfYV_plBVpYFAPl9Yjn9_8czNDlWW3Bhi4gdgW7D7WJ8BZCFmt12eUaZLeaD8XYPWWDEZKhHSveLPdqtiOgpNR6NpwstGs49sxGgBrooHgCfkl6zIkZdu7gczXnMLLcie3KJJStnxM-y2SHP-JbBZNSamwYP47YGocprA3Jv8pIGs1v4iA_SmqEIkjuxA4WrNf6EhnRB5ctjBaganrpP_CY6i6oRxLifx3MNSACoIHkYn9Y1AJByewrJqMWHQNiKctMRdtF_k8LNqMX3K1ZSP7a0TR5sPi_9o_5E7S8i41pYoFBIA6PnXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d53dfc1b1.mp4?token=JUnR6ZbrcNxBe3BLre0F_EMG8q5yNJuMfYV_plBVpYFAPl9Yjn9_8czNDlWW3Bhi4gdgW7D7WJ8BZCFmt12eUaZLeaD8XYPWWDEZKhHSveLPdqtiOgpNR6NpwstGs49sxGgBrooHgCfkl6zIkZdu7gczXnMLLcie3KJJStnxM-y2SHP-JbBZNSamwYP47YGocprA3Jv8pIGs1v4iA_SmqEIkjuxA4WrNf6EhnRB5ctjBaganrpP_CY6i6oRxLifx3MNSACoIHkYn9Y1AJByewrJqMWHQNiKctMRdtF_k8LNqMX3K1ZSP7a0TR5sPi_9o_5E7S8i41pYoFBIA6PnXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس دعا میکنیم
🙌🏾
🇮🇷
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18714" target="_blank">📅 11:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNcBo9jch3HdCCaNQK-Bfx-AqPgqxDHXM9P4kQB1SHsU2rPSLDIhSRuLpzyOIqM8Q_ClQSp_gqCgrh3T-_nx6ibVTiCLnbMPb2Cnwo9AGg5n75RikenHL_MmOZwDj6mty5MzJ2doBwVxVzqU69WHDvbzFXxy0JDywrSYILQRWNLpK-lwLBtNs9ipc03cuP37IoBIWy5lw3jYmmgmUaJ9uYWRj7Iyoy1JaPxoB85p2PJKojyZH39YoxzJRMKZhsN0U5l7IuFHb_EwAaHxfNKAk71LiBM1BI9nM1-YZI_ZSlH-rqcugMI-3hDdhwrVFVBr_tEAcP6tq2PNK8rpMiYnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که تا این لحظه تایید شدند دیشب مورد حمله آمریکا قرار گرفته شده
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18713" target="_blank">📅 10:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb828f5c9.mp4?token=ayUbFrKxkIzxiAKH-fkEdjMZN_rJzCtCFVgpEbcIedG1CXB4BtGRc55tw6TPpP2U0IGIJ9u7Fts3MaEeDfqGiqDQqCyB4KCfi7S3DX1erBa7zBNzGTr_3hPrabbFK-d2UOOBfRMrlX2NI1g3f__IuSuIw9e_J-9q0D_m9TYZDnZ-3XfV8bQZajMeVXzoFBSbosWOlj1IK9hDwLPKMUJAUq3eGc-x8TuohHuOfVRfZ0bLvkcFQy80__A1x-n35FbOHxiO5fJqZV2PJraWdULEKf7dd32lCrbc2AVhv96dcnxJGjeqvYOYZ3qKqdh9jh-q-8SnS9z3rt-M6-aQe9aA9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb828f5c9.mp4?token=ayUbFrKxkIzxiAKH-fkEdjMZN_rJzCtCFVgpEbcIedG1CXB4BtGRc55tw6TPpP2U0IGIJ9u7Fts3MaEeDfqGiqDQqCyB4KCfi7S3DX1erBa7zBNzGTr_3hPrabbFK-d2UOOBfRMrlX2NI1g3f__IuSuIw9e_J-9q0D_m9TYZDnZ-3XfV8bQZajMeVXzoFBSbosWOlj1IK9hDwLPKMUJAUq3eGc-x8TuohHuOfVRfZ0bLvkcFQy80__A1x-n35FbOHxiO5fJqZV2PJraWdULEKf7dd32lCrbc2AVhv96dcnxJGjeqvYOYZ3qKqdh9jh-q-8SnS9z3rt-M6-aQe9aA9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حملات شب گذشته آمریکا، تونل میرزایی نیز هدف قرار گرفت و گفته می‌شود دو دهانه این تونل مسدود شده است. این تونل در محور اصلی بندرعباس به کرمان، یزد و تهران قرار دارد و یکی از مهم‌ترین مسیرهای زمینی انتقال کالا از بندر شهید رجایی، بزرگ‌ترین بندر کانتینری ایران،…</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18712" target="_blank">📅 10:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شرکت آب و فاضلاب هرمزگان:
آب‌شیرین‌کن بونجی در غرب شهرستان جاسک مورد حمله قرار گرفت  در این حمله، ایستگاه پمپاژ برداشت آب خام از دریا و هم‌چنین ترانس برق مربوط به آب‌شیرین‌کن بونجی با ظرفیت تولید ۳۱۵۰ مترمکعب در شبانه‌روز به طور کامل تخریب شده است.
@WarRoom
شرکت برق کویت:
یک حمله جدید صبح امروز به یک ایستگاه برق و تاسیسات شیرین‌سازی آب ما انجام شد.</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18711" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش انفجار در بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18710" target="_blank">📅 09:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در حملات شب گذشته آمریکا، تونل میرزایی نیز هدف قرار گرفت و گفته می‌شود دو دهانه این تونل مسدود شده است. این تونل در محور اصلی بندرعباس به کرمان، یزد و تهران قرار دارد و یکی از مهم‌ترین مسیرهای زمینی انتقال کالا از بندر شهید رجایی، بزرگ‌ترین بندر کانتینری ایران، به مناطق مرکزی کشور به شمار می‌رود. در صورت تداوم انسداد این مسیر، بخشی از شبکه لجستیکی و حمل‌ونقل جاده‌ای میان بندرعباس و مرکز ایران با اختلال و افزایش زمان جابه‌جایی کالا مواجه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18709" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آلارم کویت به صدا در آمد و پدافند درگیر شده
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18708" target="_blank">📅 08:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18706">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULBy4Bmniv4wMwSmkvOi_5JuM5j-VAh_hTjyYvd740yV19gKhGbAVzUon7oD3Iaizmf216GPyNhpm-RxUN_ftq8eRobGzEAJ3MF9cVjjrt11O_9hQDf7sNV5pFG5qvr95x-joSAmU4-y3EOX2wta4S7vPCjoPO1uUJgDvSkQArhYPC6U2ME4jOsHKR_u_7T3B37aqlkR8NTC73gFAGEYEd45ioobeMHydUwSxuLkeNX43MWlPiLM-faiLpC0SHglZincloKHxoZgrJvj1NLVBS-ZHwvotjtdZWg-nBV_qdHrXnsN8QsZB1J9bEVqxUoOxaMdjuhdmoaEzpz7pA_i1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viIcy9B-D5G4PsdMyZlOv-pI-_JOQG3qMpPLU3p4NeFNEdXc16TH-JaHM7yh8gFui7ckK31t4Ic7nbdOLk0DV4ejjUufIATCu5ogdoFTn4QSX8lMKn99kgej_ITtFZY_GC-ucqFp8CQ00CjyaYCyGHiUio2IPR2o_zWz5YOXm8FjGinSycIOfvspoBZBp-gdwl_EILrONjZvpJJ-EHx82-ziJ0Ct7aj1qE4TXmRI5RcCXgWBEApfX8UPT7Fb_mSB4nk5EQGYJ5iEQe_h3VpHbUUg7vakQPdeaOgTr6TjpzFcmh_PNMiZKrzCMzgTtY3FWRcv86O8IuVSxU8GZBDPyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دقایقی پیش پرتاب ۳ موشک بالستیک از ‌امیدیه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18706" target="_blank">📅 08:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18705">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2931a5ca35.mp4?token=qFuPupc5h0q7qHQw78GqCfqTWg9Wxn0ez2YiGvQkz4XNow2bbyu9bJYy9klrhty9rG0tcpThky6aaKjotadQ0uspcAkFntDu3g8bNGZq1UhcftSzPKhA2Tomej1HPYUQq9XUZHaqJg5EgCsYSsRh05IQ8cPDzmxIHX8wiPdZrgjbyucTUxeZ3GPrQu02tE63V6Ah05spWXHu5eDoXrzFbJIE6TS-1R1hrh0P4t4sAr4Ii2Dp2TQQ5aUcN_FBtJrmYh-t15DIHIBpOOC-gy5T0YLn_3RafBQg4ts5vW6iwtmiZoQrIt1FXk9YU4tASAKYVFIobeup89qozuGczs-hZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2931a5ca35.mp4?token=qFuPupc5h0q7qHQw78GqCfqTWg9Wxn0ez2YiGvQkz4XNow2bbyu9bJYy9klrhty9rG0tcpThky6aaKjotadQ0uspcAkFntDu3g8bNGZq1UhcftSzPKhA2Tomej1HPYUQq9XUZHaqJg5EgCsYSsRh05IQ8cPDzmxIHX8wiPdZrgjbyucTUxeZ3GPrQu02tE63V6Ah05spWXHu5eDoXrzFbJIE6TS-1R1hrh0P4t4sAr4Ii2Dp2TQQ5aUcN_FBtJrmYh-t15DIHIBpOOC-gy5T0YLn_3RafBQg4ts5vW6iwtmiZoQrIt1FXk9YU4tASAKYVFIobeup89qozuGczs-hZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی
هفتمین شب متوالی
حملات علیه ایران را در
۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا (ET) (۰۵:۰۰ بامداد ۱۸ ژوئیه به وقت تهران)
به پایان رساندند.
سنتکام اعلام کرد در این عملیات،
مراکز دیده‌بانی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی
ایران هدف قرار گرفت. به گفته این فرماندهی، نیروهای آمریکایی از
جنگنده‌ها، پهپادها، ناوهای جنگی
و دیگر تجهیزات نظامی در این حملات استفاده کردند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18705" target="_blank">📅 08:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">در ساعت ۰۴:۴۴، نقطه‌ای در حوالی جاسک هدف حمله آمریکا قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18704" target="_blank">📅 04:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5fRqMk4J5GQDvZE_faqzOK9qNfKOxX0sw2nmicyioI9fFBJ0ha-BjSSFcp-FB2-7564IrGCY06G0jH0IfjqJPmdlvGhsbttMlfkXqwVi8DklKUtQAHnLBx6LK-2VaOEXW4POVC2WQvCkeOebr1jCUJbkBiPzWF6yQr8swsawWU9CDEXvqisdLYrMq8IqMpNsjyx_IMyfe29QAXjyoeuY3IGZpOX60-N1SSqFpYbMrlHbwOP7eWzf4W1Isj60H3cbEEdSPQdsbUWwJGM1hskD0xRM2UzZeSPze501Y12C6Gau9NRHbeloKUlF-C4jbrUMMKfG5hw1jg2lhjVYQbpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده های فلایت رادار نشان میدهد هواپیمای E-3 آواکس هشت ساعت و نیم است که مشغول عملیات در خلیج فارس است
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18703" target="_blank">📅 04:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بندر رو باز زدن
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18702" target="_blank">📅 04:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18701" target="_blank">📅 04:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18700">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پرتاب موشک از تبریز/ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18700" target="_blank">📅 04:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار در غرب بندر جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18699" target="_blank">📅 04:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بندر ۲ تا ۲ نونه دیگه زد پیچید بیرون بر
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18698" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18697" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">روستای گیگین ۲ گیگ زدن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18696" target="_blank">📅 03:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18695" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18694" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بندر ۲ تا ۲ نونه زد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18693" target="_blank">📅 03:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه: دو فروند کشتی نفتکش متخلف با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر شدند! @WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18692" target="_blank">📅 03:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بر اساس گزارش‌های بومی، مناطق هدف قرارگرفته در حملات امشب به یزد عبارت‌اند از:
۱. صنایع دفاع
۲. آماد و پشتیبانی سپاه
۳. سایت موشکی
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18691" target="_blank">📅 03:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18690" target="_blank">📅 03:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18689" target="_blank">📅 03:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18688" target="_blank">📅 03:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18687">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پایان سشن مارکت نیویورک
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18687" target="_blank">📅 03:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18686">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18686" target="_blank">📅 03:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجار اهواز</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18683" target="_blank">📅 03:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجار در جزیره خارک
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18682" target="_blank">📅 03:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار جزیره لارک
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18680" target="_blank">📅 03:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18679" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من هستم</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18678" target="_blank">📅 02:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏خبرنگار اکسیوس از قول مقام آمریکایی :
در تشدید تنش بسیار بزرگی،دقایقی پیش ایران برای اولین بار در 3 ماه گذشته به سمت عربستان سعودی موشک بالستیک شلیک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18677" target="_blank">📅 02:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18676" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار امیدیه خوزستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18675" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرتاب موشک از الیگودرز لرستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18674" target="_blank">📅 02:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله به پایگاه شاهزاده سلطان عربستان
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18673" target="_blank">📅 02:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d28e68968.mp4?token=I2JwrZdqbm6xT_MRqHrcOzEaZ9nd0X_3YKKmYVE1oOjynIOh3k17uhJC1jTd8TM1cGPRpYT4TWpreMBF8da76WUzCNH2k9AByZDkg_p4gBZO7_JkxE_sQ-kCZ8Ih3Iu3zF3qBasxDBDFZZJP0X5EKgffQAtFwChbzVFimfPsLNYgnTnihiLEtDFrJlQn-GgtbTt1ORTb8VOrJEMh6XNh-3Is2M5wPDfI_TaxEULN1k0VkatyJiIv29fL24oyomg1-HOXpg-Q-3TAVbv57U2RzjFGMKwFmS4v7hTnI3fCwQb4rbPuKeCMgjlwdD0Q4F63DsLKL2OoNTfHJDEvXp4HYo4R7TBG69-hRR1Sl5e6VSymbstroMmZb2kybTvm4RdR-qPLcuokzFS2pacg8XSQYpi2lD97Wq2KO-ZgvNx5-3Sd_41aUjix_w7pMeSxa_0Ty5naXpgoNsCz2NVTQuXbvpQ1OXTpOwph5t2N8dFIiQTx1RutosMm2jMCBBStdtmxp40xOBH03kEChVCEmAhfw_dfaKXkAwzX_krPqB-1EfJnC9eVMY8YKusvTHX_z2N97fzi_nfUDtSF0RJSczVVYED_gJmaVOSsjeyKiJ8WSI-Hmb_I8dvhPrD1_a2rowdHb6TGyQ3Qows4gcUk50RBBHCb5XN5DvJMq31zSO7jO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d28e68968.mp4?token=I2JwrZdqbm6xT_MRqHrcOzEaZ9nd0X_3YKKmYVE1oOjynIOh3k17uhJC1jTd8TM1cGPRpYT4TWpreMBF8da76WUzCNH2k9AByZDkg_p4gBZO7_JkxE_sQ-kCZ8Ih3Iu3zF3qBasxDBDFZZJP0X5EKgffQAtFwChbzVFimfPsLNYgnTnihiLEtDFrJlQn-GgtbTt1ORTb8VOrJEMh6XNh-3Is2M5wPDfI_TaxEULN1k0VkatyJiIv29fL24oyomg1-HOXpg-Q-3TAVbv57U2RzjFGMKwFmS4v7hTnI3fCwQb4rbPuKeCMgjlwdD0Q4F63DsLKL2OoNTfHJDEvXp4HYo4R7TBG69-hRR1Sl5e6VSymbstroMmZb2kybTvm4RdR-qPLcuokzFS2pacg8XSQYpi2lD97Wq2KO-ZgvNx5-3Sd_41aUjix_w7pMeSxa_0Ty5naXpgoNsCz2NVTQuXbvpQ1OXTpOwph5t2N8dFIiQTx1RutosMm2jMCBBStdtmxp40xOBH03kEChVCEmAhfw_dfaKXkAwzX_krPqB-1EfJnC9eVMY8YKusvTHX_z2N97fzi_nfUDtSF0RJSczVVYED_gJmaVOSsjeyKiJ8WSI-Hmb_I8dvhPrD1_a2rowdHb6TGyQ3Qows4gcUk50RBBHCb5XN5DvJMq31zSO7jO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18672" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پل دو راهی‌ میناب
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18671" target="_blank">📅 02:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18670">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خرم آباد لرستان چند انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18670" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18669">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">از ‌تبریز موشک زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18669" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پل رودان هم اکنون  @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18668" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a919a8cfe.mp4?token=t3jxqBTrarGE3qPCIEVQHm0jqg4BkOXuX37EEOq3BZ0LmSWKNBpD__NYghmf7UdTDp_VGzJ7hKABc8EK-Hvc_8ucPKsYGZWTV_dsN1hjzuQ5s4_QMhIVnaeB2ZvLQ2zqcvgvTFdUmrOs4PAma1c2Nm2v8VHtka9ntdHU6zAtpkNhI3i2iWfAZp-QvIIlGsq0BKCs-y9Gqd4WX536hOkw1zLauXkRN0Jf8SkJ30Ql6ZRUl20xbW2SQbo0t3a63CqByYtMDyooMOOFjaDb_NqBgDamFhJIwEsmU9DlpExvpMWec38j4Vxi5toTSJaOxIWNjO9j890Y9-sdC3cfAPjI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a919a8cfe.mp4?token=t3jxqBTrarGE3qPCIEVQHm0jqg4BkOXuX37EEOq3BZ0LmSWKNBpD__NYghmf7UdTDp_VGzJ7hKABc8EK-Hvc_8ucPKsYGZWTV_dsN1hjzuQ5s4_QMhIVnaeB2ZvLQ2zqcvgvTFdUmrOs4PAma1c2Nm2v8VHtka9ntdHU6zAtpkNhI3i2iWfAZp-QvIIlGsq0BKCs-y9Gqd4WX536hOkw1zLauXkRN0Jf8SkJ30Ql6ZRUl20xbW2SQbo0t3a63CqByYtMDyooMOOFjaDb_NqBgDamFhJIwEsmU9DlpExvpMWec38j4Vxi5toTSJaOxIWNjO9j890Y9-sdC3cfAPjI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل رودان هم اکنون
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18667" target="_blank">📅 02:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجار در کوار - استان فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18666" target="_blank">📅 02:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چغادک بوشهر انفجاررررر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18665" target="_blank">📅 02:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فارس: آمریکا امشب سه پل و تونل دیگه رو توی استان هرمزگان هدف قرار داد @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18664" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فارس: آمریکا امشب سه پل و تونل دیگه رو توی استان هرمزگان هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18663" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارهای سنگین در بنادر بوشهر و کنگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18662" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps_13FduD9x-eTQwtCg8VRz_hgQAn9I0ncst1xjjl_utm-h-gMtugVsAeGca5y1EHHwtRcrk0RJbio0rB7BRXGVUcNd22vTgCZ4J_ACGXkrp318tadaF6090IsrZCcKhLWvl6QLP-io9kSBC1zNy9nTyCzDH4vqacGwEQp3z8xYbNFTE_Kf6gqipDN36RkCX1GlJcmD_-B3ZTYCXUSj84cHAnzaxbkpyNGkQuu-SJpQnUOWAIFq_t5JwU49YGNDqKvrxhFX9AqLeVoa_ziIWjTwaOWhRiM_oR_Ra2Z0a5z1uLrG2-bsak1-5vCT9EIG6K--A2m5q6inIVq4haBc3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پل مسیر بندرعباس -رودان هدف قرار گرفته شد
.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18661" target="_blank">📅 01:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18660" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c70d8d934.mp4?token=A3vz5Z8rKpXLL8lQ-FDBdhwivpw54MDbHVtCQtNjQ_liV09AwtT8KIhYT_aGBlTQqoA6SuHuEjYj66I3tzPb-WVN7PoujmmhpSuSSmypK1IoZGoJmxp3wo8PHMzCKUaLf0j7L8pZaoUh1jN5BoOMV1T_n8aAgz9jHKOHBJiWXhP1bof1D724wHYyoswF77KJt7n4BoBehRySsOeBkz50NVkpZcJ-ZDyyA_mRgZpFmGNgRYf37ZKWd3McAUBdW1JA1CO5SPj0hYwQyroDE-B28dyGw0-BzoWSUgZBVQuBB0fz28nGKsTX6aGGWVT_QPa-zI7vJlX22VLEPCMBVyLXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c70d8d934.mp4?token=A3vz5Z8rKpXLL8lQ-FDBdhwivpw54MDbHVtCQtNjQ_liV09AwtT8KIhYT_aGBlTQqoA6SuHuEjYj66I3tzPb-WVN7PoujmmhpSuSSmypK1IoZGoJmxp3wo8PHMzCKUaLf0j7L8pZaoUh1jN5BoOMV1T_n8aAgz9jHKOHBJiWXhP1bof1D724wHYyoswF77KJt7n4BoBehRySsOeBkz50NVkpZcJ-ZDyyA_mRgZpFmGNgRYf37ZKWd3McAUBdW1JA1CO5SPj0hYwQyroDE-B28dyGw0-BzoWSUgZBVQuBB0fz28nGKsTX6aGGWVT_QPa-zI7vJlX22VLEPCMBVyLXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان هوشیار هستند، زیرا ایالات متحده محاصره دریایی علیه ایران را به شدت اجرا می‌کند. در طول سه روز اول اجرای مجدد این تحریم‌ها، نیروهای آمریکایی مسیر ۴ کشتی تجاری را تغییر دادند، یکی را از کار انداختند و یکی را توقیف کردند تا از رعایت کامل تحریم‌ها اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18659" target="_blank">📅 01:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8643b5df0d.mp4?token=F2OLwNJ4-QerkEnf08EAzXiR3c2HzrvzKWQlP_heKbmWRsviuyieb_DnyjNiFaMntA_0TtJSTg3PRyS1ZTsCqK9Rn3BLJV8d8yT_jVxqPSFiuwzzxVTt10onHchg26IlL-T5a-doeUXbut-W8mvYDrBqrdTGMlZaVkv7PyMvFRMye6qpaYmx1kd8WcBsJz4CEDMHPlqiGHEAdMHF_l5DStsAx26vW9dM3GTwcRbxk4xUjLF6GrcN-XN58Z7mhBL4Bvx0vMJ2yjDETKy-A7CRdlv6I8CZDpiiSXSZ5J9GFuBKYDg_nvKFm_xonL_VqWMgxVWCKuLf_AYPE2B56HoZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8643b5df0d.mp4?token=F2OLwNJ4-QerkEnf08EAzXiR3c2HzrvzKWQlP_heKbmWRsviuyieb_DnyjNiFaMntA_0TtJSTg3PRyS1ZTsCqK9Rn3BLJV8d8yT_jVxqPSFiuwzzxVTt10onHchg26IlL-T5a-doeUXbut-W8mvYDrBqrdTGMlZaVkv7PyMvFRMye6qpaYmx1kd8WcBsJz4CEDMHPlqiGHEAdMHF_l5DStsAx26vW9dM3GTwcRbxk4xUjLF6GrcN-XN58Z7mhBL4Bvx0vMJ2yjDETKy-A7CRdlv6I8CZDpiiSXSZ5J9GFuBKYDg_nvKFm_xonL_VqWMgxVWCKuLf_AYPE2B56HoZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس برج رادیویی رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18658" target="_blank">📅 01:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18657">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18657" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا «پل صراط» رو زد
🚨
🚨
🚨
دیگه نه بهشت میریم نه جهنم ، همین جا میمونیم
😂
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18656" target="_blank">📅 01:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار جدید لار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18655" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سپاه: دو فروند کشتی نفتکش متخلف با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر شدند!
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18654" target="_blank">📅 01:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آماد و پشتیبانی سپاه یزدو زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18653" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه F-35B  STOVL در
سه‌راه پلنگ صورتی
روی حالت هاورینگ ایستاده و یک بندری سفارش داده منتظر است
@WarRoom
🌭</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18652" target="_blank">📅 01:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جنگنده ها هم ارتفاع پایین اومدن خیال راحت بندر رو میکوبن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18651" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حملات به یزد و بندر عباس ادامه داره @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18650" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملات به یزد و بندر عباس ادامه داره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18649" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تسنیم: حمله  آمریکا به مناطقی در لار و داراب
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18648" target="_blank">📅 01:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بندرعباس  ۳ تا انفجار سنگین الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18647" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جاده اندیمشک - اهواز الان زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18646" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صدای‌ انفجار سنگین الان در کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18645" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بندر عباس ۲ تا پشت هم الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18644" target="_blank">📅 00:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667848bf1.mp4?token=uyEDCWbPvVoP8NBUZpdxwApsYd9guozk8Vd2lBmPwbdBD4OeKeEJQZxT5b952xCS6Tqm7PLCcvYtOe-xdqpME-7GaNge-ryGVv4xNBAyrllSkhRkoxnTc_5H6O1Cfn0CIYMS2pJggSK79_VF0FMCkaP3btgfgTApAzFWH1YCDortc_oIp8lGAY0crX0y4qnPDhWs-hcEkTrx1rXCNiwUe9-9uQ9SJd1x0piRz5W-Fn0QvOHpSxdAl2JHb_QRDrGkotpSGY-GDYq3fslx5-h_zq5dz0f4GdPNz3Xf_hlQRxXXRpI-YvbigqoH3_1iKADQ8Ynl7JKIuX8GzSTD58xxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667848bf1.mp4?token=uyEDCWbPvVoP8NBUZpdxwApsYd9guozk8Vd2lBmPwbdBD4OeKeEJQZxT5b952xCS6Tqm7PLCcvYtOe-xdqpME-7GaNge-ryGVv4xNBAyrllSkhRkoxnTc_5H6O1Cfn0CIYMS2pJggSK79_VF0FMCkaP3btgfgTApAzFWH1YCDortc_oIp8lGAY0crX0y4qnPDhWs-hcEkTrx1rXCNiwUe9-9uQ9SJd1x0piRz5W-Fn0QvOHpSxdAl2JHb_QRDrGkotpSGY-GDYq3fslx5-h_zq5dz0f4GdPNz3Xf_hlQRxXXRpI-YvbigqoH3_1iKADQ8Ynl7JKIuX8GzSTD58xxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یزد
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18643" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اهواز و زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18642" target="_blank">📅 00:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18641" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18640" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یزد یدونه سنگین زد الان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18639" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18638" target="_blank">📅 00:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه سلامی کنم به مهراد جم که تو چنله
😁
داداش شهرتو زدن</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18637" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چندین انفجار جم در استان بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18636" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بندر عباس صدای انفجارررر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18635" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
