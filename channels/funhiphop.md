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
<img src="https://cdn4.telesco.pe/file/UibJvAdftkxWYNQsgq7kSKXEOcQQBc06qDqZXPf9OoDpB-mZ5I4ErEruzQdD3tTt1dfBnizZH8zSuhUclpOSTsyJtP42TjFcG9y9Jaanpqz2R7JHMztlHPGcOK59Bw62iWCMOABCOVXO5m95h-L6LsEPg-XpdELsaNE-ZSPdNcV0fwyi9asLZimtPzEwNLoDd0kclG_IqkbJjUXq_Z7Ze5V5dpcIU7OhpTUvcZlKZGs50ndmZnnMVncvS0nfd5GL46irIKK0YjzrTu6bIDUmt0CtE-Kc6I8jS-g7ruWnFY_YydbaYXSm34CcAQsqUp5Ih_28fthaFuLTgD99OMUrqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 195K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Shahi</strong></div>
<div class="tg-text">سنگین بستم رو فرانسه</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/funhiphop/80358" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froma.r.m.27</strong></div>
<div class="tg-text">از وقتی شاهی گفت سوئگ دارم مایکل اولیسه یروز خوشم ندید</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/funhiphop/80357" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کیر یامال رفت بیرون</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/funhiphop/80356" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فنای رئال وقت دکل جوده</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/funhiphop/80355" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گریه امباپه ضریبش چنده ببندیم روش
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/80354" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مهندس فوتبال حضرت ژاوی هرناندز هم تو ورزشگاهه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/funhiphop/80353" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پاسکاری قشنگشون
امباپهههه
فرانسه برگشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/80352" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سومی رو هم زدن افساید شد</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/80351" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسپانیا واقعا شایسته قهرمانیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/80350" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسپانیا دومی</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/80349" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/80348" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مشخصه با کونده و اون یارو کونه نمیتونی ببری، اینارو دیگه منم میفهمم دشان مادرجنده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/80347" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تنها بازیکن خوب نیمه اول فرانسه ربیو بود که اونم تعویض شد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/80346" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فرانسه بدون سالیبا فینالم بره جلو کین و بلینگام ‌بگا میره</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/80345" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چه بتایی که امشب لوز میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/80344" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بابا کاگان کصکش چیکار باید بکنن اخراج کنی</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/80343" target="_blank">📅 23:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیکتاتور کارو در بیار، به این بچه کون نوزده ساله نشون بده رییس کیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/80342" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیکتاتور کارو در بیار، به این بچه کون نوزده ساله نشون بده رییس کیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/80341" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چه پرسی میکنن حاجی</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/80340" target="_blank">📅 23:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عجب فوتبالی بازی میکنه اسپانیا آدم کیف میکنه خداییش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/80339" target="_blank">📅 23:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرانسه از کون اورد</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/80338" target="_blank">📅 23:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فعلا بارسا 1 0 جلوئه</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/80337" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ربیو تنهایی زورش نمی‌رسه به هافبک‌ها اسپانیا</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/80336" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئال عجب دفاع خفنی گرفته، گزینه تعویضم نیست</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/80335" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سالیبا مصدوم شد</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/80334" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مانیان گرفت</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/80333" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مانیان گرفت</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/80332" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پنالتی برای اسپانیا روی هنرنمایی جواهر نو ظهور فوتبال
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/funhiphop/80329" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یامال کصکش
😂</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/funhiphop/80328" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😂
😂
😂
.</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/80327" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام آقا فرید همین الان اهواز رو زدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/80326" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرانسه هیچ حرفی برای گفتن نداره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/80325" target="_blank">📅 22:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بازی شروع شد، به امید فینال فرانسه انگلیس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/80324" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امشب اگه فرانسه برد نفری ی شارژ بیست تومنی ازتون میگیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/80323" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جنوب، همون همیشگیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/80322" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بارسایی بدبخت شدی
دیونگ چون جلو مراکش با مصدومیت بازی کرده رباط زانوش پاره شده و نصف فصلو از دست داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/80321" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر دنبال یه پلتفرم کامل برای فیلم، سریال، انیمه و انیمیشن هستی، وقتشه Meowvie رو امتحان کنی.
✨
امکانات Meowvie:
🎥
آرشیو گسترده فیلم، سریال، انیمه و انیمیشن
🤖
هوش مصنوعی اختصاصی برای پاسخ به سوالات و پیشنهاد محتوا
🌐
نسخه تحت وب (قابل استفاده روی iPhone، iPad و همه مرورگرها)
📱
اندروید
💻
ویندوز
🍎
macOS (Intel و Apple Silicon)
📺
Android TV
⚡
اگر فیلم یا سریال موردنظرت داخل آرشیو نبود، کافیه فقط درخواست ثبت کنی؛ پس از بررسی توسط پشتیبانی، در سریع‌ترین زمان ممکن (معمولاً تا ۳۰ دقیقه) به آرشیو اضافه می‌شود.
🇮🇷
حتی در صورت اختلال یا قطع اینترنت بین‌الملل، Meowvie برای کاربران داخل ایران در دسترس خواهد بود.
🔥
همین حالا می‌تونی وارد Meowvie بشی و تجربه‌اش کنی.
🔗
لینک دانلود و ورود:
meowvie.ir
@meowvie_ir</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/80320" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبر خوب برای دانش اموزا
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/80319" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طوری که بحرین رو زدن احتمالا امشب تهرانم میزنن</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/80318" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرانسه فقط حملش سوپره مگر نه خط هافبک و دفاع جالبی نداره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80317" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4xtt7SzQg5Ei08phixjJl5k-weNSvdFYrL2Zti2oe2FOBzBJlzx-G6IFtQXZFxIqyMqYEmLWSID_RnhEH21Ep8eXsBQuIXxOJhGD37hPPb5kV7GyEaIVQgAKYNNroMaTsyox1Q_acM_jPQaR8yiuQPjZs6gLBKXRk3fef68jRqevahojvWcvtNWobiY8j6QnPLns70fkllRBhulL8thrJ_XyAouPQOvkYcJWWo8JMFHOrnSNWlfwJHhsbh0rM-tddXBfsOSvgvPnSsVwToA-SdGfojeYm0r1aOHKZv_ymIBllxz-8OvHJrwolGovEubWeZA739z1nmeOr1eqEX-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80316" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9fyLB_Nx4l-AUQz7Ib-_tQiffZXXqh1rW5tHuR5yiABh2eFsndsBgc7FA2iJa-QzJb4A2a6LmtRpzym0chi6HSVAFKTwNMG_AP8JKNPRBRyg4Zz-5uW-Y8BliDCQIsxoYY6xi-c_Wh-CjFI62NL4mQjRJ1PcvX3cL5i02uCEZ1nEvCSg48EL1JgmzIEovRvn5K7WCnljIP2hpnF-U0UNmxKmD1pIYI7nrp27Tf26xUTFMMNVOSQ8wRN5MV-_Jtbdk1hmYDN2LkZpjWqmkJqfhJoxdPe001pGh-c78bURR9pGgAF392yzJmwRo2lblWozimcE7gzHiJt6r53ln7pAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کصمادرت با این ترکیب چیدنت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80315" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">داش میدونیم مادرت کونیه لازم نیس یادمون بندازی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80314" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80313" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=h5vS5v6eLQjZJ-SjtwECRmklYB9_sz9hR121wse2gFLDy6OF6aBhWDyx3DEMwt1NlF3upb7gokXk2KJWFtx3Wbr9vsSK_L8GFQopdui5Li31ttmfUbsdKpIwdZvD6Q-5PN0_GzfSgY8onFojik7LCiOLLVxQQ2tFfWWAQulJikoFvZakM9RjE6kMjpYS-1DIBwzZvXC2ol2ityokcm5QUyjUuq_wIb7ZJgf9GXr7ei0-wrWfSW0ABl7sHO4szbpdJ21sKzmgipzVjQdlDOvxPhkprpl_3LkNEOEOuJ5d3KTGUru2N5xcUwjbCOiNNW8QHhOGgdcHeBYUrQ1WolUytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=h5vS5v6eLQjZJ-SjtwECRmklYB9_sz9hR121wse2gFLDy6OF6aBhWDyx3DEMwt1NlF3upb7gokXk2KJWFtx3Wbr9vsSK_L8GFQopdui5Li31ttmfUbsdKpIwdZvD6Q-5PN0_GzfSgY8onFojik7LCiOLLVxQQ2tFfWWAQulJikoFvZakM9RjE6kMjpYS-1DIBwzZvXC2ol2ityokcm5QUyjUuq_wIb7ZJgf9GXr7ei0-wrWfSW0ABl7sHO4szbpdJ21sKzmgipzVjQdlDOvxPhkprpl_3LkNEOEOuJ5d3KTGUru2N5xcUwjbCOiNNW8QHhOGgdcHeBYUrQ1WolUytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین بد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80312" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmQhDe1S4YNIuNu-E2pk-KyZRmiFmNB_H3HW3fl_Onr7azgcXDn8a-VMWMLDiU_iEAAU3J2sBGGNOErX5dPfgas1qV0Kd3elQp69AQEhoXhmyz0ii3n7tqzX_7bp1p5QfnhH8kXK8pFIP0iida1RWnjyGO74R8rMLEtZVWlT4OVSevKRvFzTUfyRjS1_zzID9GDHbpHS9O5RORYl1isl7kvPxTrSBKhirKZq_mkowVP9DricYJit_daozowS7b2_jL2goY6Civ4i_KJYjqzRHjSs6ScoSEiWosLBTRbncZitKO_FaUPvXHG9l5fZdVMyKT6txoQnEzo1K8lGQGFwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80311" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هرچی دارید بزنید رو صعود اسپانیا به فینال جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80310" target="_blank">📅 19:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80309" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بنظرتون با پنج درصد شارژ میشه ۷۰ دقیقه دووم اورد؟</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80308" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=T5E-Iy9OHl7D1mgP1WpQw4cvaQKtC5sjgF6lUmolf1Q-T_SK5kK1SbEhgLQPolrhICpwMocI2VuIiiVHSAYo4_GBFBAAqUOuAMzKPfw_UL9hIVVKAOt-mnGT-y4fyUv0tE9VZ66MX5BWaekVxWcb8kZ2US6SP60iQztSjJX5L9uI-eifIB65JdwlFSsVnxWrKWT514nJsPiqFCddkK2FLl-GU2W4teynAhc3SHEiHyQKift38iWgUnNY46djARA_ctATMTqeJeTxD2URPN2qWG8qnI1YRJiUJg-KL-K-p2i9RTBWS0CPuTEXXsB4N3D6MjTqH1UyaGJP41MBafaIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=T5E-Iy9OHl7D1mgP1WpQw4cvaQKtC5sjgF6lUmolf1Q-T_SK5kK1SbEhgLQPolrhICpwMocI2VuIiiVHSAYo4_GBFBAAqUOuAMzKPfw_UL9hIVVKAOt-mnGT-y4fyUv0tE9VZ66MX5BWaekVxWcb8kZ2US6SP60iQztSjJX5L9uI-eifIB65JdwlFSsVnxWrKWT514nJsPiqFCddkK2FLl-GU2W4teynAhc3SHEiHyQKift38iWgUnNY46djARA_ctATMTqeJeTxD2URPN2qWG8qnI1YRJiUJg-KL-K-p2i9RTBWS0CPuTEXXsB4N3D6MjTqH1UyaGJP41MBafaIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش لطفا نخون دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80307" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگن پرستاران و کادر درمان در شیراز و یزد دست به اعتراض زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80306" target="_blank">📅 18:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKQwGXF53vTpKNWATkvolWXtk2HjCCN-QehWKOpr0cBwpdJ7aMyxoNFX-BZApHkDuEBkNakC24gbq-BYoQ9FHNcGCRQ7dP1eDSDaOfMxCN7qtUQpCyC4Df9UsUcqxDIZPvtjNbdLQPXMyM3cOCr98CkAALmZtcdVMRlS0LbtlMkkxgyOO6Uzk6BEQM9EUfYIHehOScdSTtHvuxTCz5IKDMobJbqeYNP81wcysUX2n_98tpARjK8mdMCDDrS5dlxtW8p1ye8orbrEy2IZZvoA_6mK25UlIBn6Eud63gCM-BwnDV1bL4TdoOkoOnYbSwVbwZbYmjyOr9tgXYgH7ns3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMikrGRCts2RV5C7G2IU_V8L7ZkBda1gJhKDZAXZvt3PoTRpKsUlHQWBzhKoN7rhUZCDiXKav_wKoVjQB7l11cqgzX54oyxx2dUpolevNxygL_FY3C5Bif2eVIW-3XQyvV9c_G6Upr4NX7YdXWMP7AyfjzzIyP2dFRLvt5g3d-9kqv9VIpN6uUUMQ8By6OcYLCLmyvlCjsqvM-qw22A4d66PpGpL6v6ZuTmJWaJulkyZDe9b6ua09SUniKnweNSUwGsjk5JzrSJiGM4k2InoYJ5Pl-RF4_IZ_NV-xjY7C2oPbmNESpnEaKdqF9AMyE-ovp2zHwSF8K6kuA5rKY9kvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنیفر لوپز ۵۶ ساله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80304" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDbX0VW51KHv2PMHZ3gAO0xFxOuFG0ajM1rkLg8eIvWL39KGpUKk0O3DlUN9uKvdm6nZDPu4ornbLe19T4hOfznuB_1I_n9Cue_a9RAg80tJm0jbjD1nmcXOrG3no4iLqh4J3Z90iZ1mD53wv0ZMNMBiRUCUkjsc6rCESouiIpS9pgEfiWEhSsOZE2FNIuGuWctjKK4x9cONAUAJw7ihBsawFunHCGpNF9M8YartrTxxMbkVrS3Ne0_D6CTZ9Q9Q1iBvcvvwOHxK6oZYygiarzgJZyhPly8OxZIFM9unY45MRbSHEsCqRU0Q0gny2CINwd2h0mQ6W0NzGwZQWx4Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g23
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/80303" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3vvYrIaUvvDiqITgceO-_Lm0ftpKk9Vwao8_U6ye6LrmiEk_aDGx5RcxTnpjIoL_Gx30RenpA8yixmXuibX6yuHom3RHO-nUtQLSolIqWZI_QhTKOOFxuSo4rM8nNsqxH4C9r_IR7BFff3Soh08P7SgEdzxzA4_xoCwDoW1J1n_oIpWVdnfIXYtw_oPjsLYimWUwuK0zD2atcR5VBhfaziH7rUQG5L5xfnIbw3q-zZRdjFVOZE0SzpZw-hJZJ9tT4bxykBrDbXqLoEaE1mmQf-yLcbHpx31ECqBO6NWTk5x23ksr_PaQ6s8u66SaeGSfutS_LriHFJuiPFiiInJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80302" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5BRKafxsV37m1bElCU5g8t8dx70CYOmSHz2ovAiEyUo3pXvoGyiO0NpiqTXKdmgVPSan84VVJSvmChKiMhLDGlroC3wZX0E_IgazEe-CjDS9LoCAJYgMeSdsRaVYiuq7ksHLr8mqHaeS2pY-EyMDr3kfaIqFPC5WbxFhNPGplu2YiR02Vt_7OObjXSiS31DWAOIUjxXlxeNyhUHH5Rzc_kaK-jraOjroH2blxfWqStD-T3SiwUmuNs5W-Qn3UJ5IDz9djqQ19bexV1MQqddlF6tVgBa5zAK6jBECCt5Bk3BDzfTcozygbkfWLwA81XDOQQZkjj-iIHEasKs6_fYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80301" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoQAVNKOG6WSx3XVnEkigBp3Sl1OOGlFEVJKZ5A8tgc5ofjfTHV3qleHU8EMzRO17oeAkTPC4CQWFUZSNoa2_Yw-r50WxhO3XRTPEXie3DtvVMvk_w68lvxV7wzt7sd0X1JQamp_aJgWz3eYzCiaIZ3QZIgRi-PzO3ErU7y86_Ca0IcDQ1uE7if3avKceMxIBlePvSMhD6FE2HGZ_znmjuCcEyWJjueag3zMFLpei-H713OkI29rxfxMIwv6J5kJVa7e52ZPzMCPPWfeDYt-CTW2yPceXPYeflAoPbRcTu8TuKRye7TrQ_9ERK6LsrXrjk08lfQTeS95lF7_OCz2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80300" target="_blank">📅 15:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNoSkY2AW70m5C9hp_8m4iPppYkpBBMlojTqQqJSmCwB4nYZYW9rSKVZI_TnGNkLicldt2S1cjvpxAs59O1MQRxss1xMVWVqEW9XqJiEg0s6KJF395p4uHZE84z7KxQy1_LaYxFzn-t_h53eI_nGg38axWuPDUyFoVL26WvKFK9dVrEWQB7-qFDIErvc5xKugRDbe255oEc0pwUe_AngUtyvXVLvZJHyjzsaVK1fxg566hb-PIh63f4dvlZNhaW5zwsGIL7KvWflIgFmEjRSWD2S9bAplALbQ7StjQfRfXYUNNQSqo5ISCTZiNEIqxOj7THeLbqFXcrEz5cM5OjxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkksotpNsPgvCRsD3gR1N4psT3V52H0aLwYTejciU_wM-zvsu1JsgJS9XJTKYKSMRdc4lAPMbyTJM5xO-VRinXuwpda5MAWrpSuLra6punmi5pc4LnjpgppKM6FZKFNyJbOuV0CQELkSdy7qdi5dJROYh3PoVrVhlUN5oNaA66fr6WlTZYd_HLatYuNIEjyRa81xMWznSfM9LGAEeNGKCjTy3-ggl8HhjsihmjxyIlqt9WRtpjQz-Tf4PBbEfE-gBtR1VK22pBWOHc45uRCzFfSHEwePCJE5MIRTPRP11kNaT-LQVS-8U0_IwMX_lE-rmq6Z6yfBctbEnePhDQD5Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80298" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80297" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80296">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80296" target="_blank">📅 14:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الان سکته میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80294" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80293" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چه فشاری شد حاجی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80292" target="_blank">📅 14:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH9loQHQsFxDUHvHcx5SBteNg4YoYefQHBzLD9-UNQKk0p3T-Mtjwhag4EkLx7_IjAfsgtd-ifjj746f-xhwPqkmiPwJ7_wPYbibiZ0XQ39tkQ7nI_KBWsrYHCbFW9Zyy04-nBe_Fl94mk8p46e3qMgK6CAamDUC9fbkEo5-k6UgrLp7ulFO9T9-1yd3Yv2wiFGWJDeOwJIQjSV-IRpcFQzyMXtY3Jugl-8wB9-L6A5bSqvKavYhHDg2nu_MbXvUqHbSZ-2Vs8PwcdIyIrwOoDNboBeJ-6vrdQPY0C770CcBzpDIDZGJTIFh5nr92UqExu4oXp8Dl4Dd94kZg5ACVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80291" target="_blank">📅 14:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80290" target="_blank">📅 13:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسر دوش آب سرد بگیر
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80289" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مامان عمو پورنگ درگذشت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80288" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-text">امروز روز فلانه و کیرخر‌.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80287" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار دوباره در جنوب برای ترور مجدد چرسی در جبران ترور ناموفق قبلی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80286" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80285" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80284" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80283" target="_blank">📅 12:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حالا ویناک که گوز کونی نیست ولی همه این سلبریتیایی که دارید ازشون دفاع میکنید وقتی ایران بودن خایمال بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80280" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfm7CEAeA0xys1yGs-FLexD42nKZGS-qHgR1yDAL0Il76RvB05N-rjqytwqPbJ57mM_B-XXYO3g_2lcHmBjX0ZpuhSMJ_KgizS0_XFLZI_OPO1aAOEaVWD9we76GdPs_lUmQXUy2FBFrk2oy4lrQD3e04tTtt9vcuS6HgiDpqwsZu5y7-bMvsqjiub2ts5rd_iViyvUmZul1eOvicmJimF1haVFw_FYv8e5RsctTk4S22cag8S6nWKw1yYJVXr4oyS6d_EdHP9sxyQ0BiSeKTx7Ju8zojecHnqZAuj5ZCZ0W6Gs8JgjlIZZHWehYeXBPvlGEiAPMYyp-Albx9Stteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElCd73wYr64sHwoKWJbOYDBAfP7q0LTaQrqlVPrMn42NijPd_hUrQFRos3k71oihISo0q5ziRyI_ilP3ldkopvDDZnG-_2b1H9ePocrqqu0Ndty8zWDiCftYwLdwQxJ5Qlr5cIK6VYU9Cm3xB6B-yzv4GPjJBm83IJt7l-KOlPCRkCHlZQVKFOw7RwzjWA1HEZadS9h0oCdFqN03TPcrm3xZ0DTvH1KvlK2T0N88MeaVQxL9CpVpDv_rbnThKoYlC_7b-FE4Z-vu4KhSKsqNa2w8vPctKLNh_dyrFKllXdzDPPnhMT-XXroJJ_vI-cY5EZt1iq-ynmDClyGpRayL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMt0TVEIJ4uri3bruGN328Tim060fUhO6zKugCQfuYCm4aPfs5qEkn_ds3lOp2LkGIS88W6-FZNyiFAAOeFPWpWbHYikvdrHSTBNdxSu01HvDXeoovpfmB5QWt9o8vHH98aWmixRfdlTunQI7g8N-iFFE8rB9qHoZ_nKZQ6wVvnjxKmzbGIIBJwyAKycvogI2d3ptWCOsk29_oUYiaRGsd_IaFrfvWVAjEwHU-fwnZ_zRjkqpLNAOgDEe8pC-Qfif0InkTjtnYfIDZHXb3DDJY3W4sLBy_LaPYKDzGo3l0MOsEv2gLRpQgeDUaTpUfBuNagtG5CAGmRXSSLwgISvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoMHPfXzeNY2H9-hm9082mvwa7E_OtLcgKRtwcS14S0VNybz8dGy2JdAvxm5Ow7BLzmGVUzkljwcigurg-_UEEcNUXcLyvvaaMM5QCpuPG4nw4h9IX6wUypdJCDMvYi40TL6IP7wNH03hOVG8H59xXkLQ_MzM0DJMKD8uPJNlgclP-ONGeT27kx0kl20AdbQKUKDnRWR7nLY_twOBP7zJQNMKLiUDLewt3hgf6m8501deGU7_Yzu5dnh933JRcn4JSt11TbhaShie001ZmdWHMZ2T6A44XW6BHdY5VijRL3xWsvoF-I1kirdLMJmrJO3t2zx6h0mKeoEVs7xbfYH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or8fveE8T485Kzlfi2A5x03fbuG9r7mrv8jPEI7c4C6pUuuVJpr8EEVPbSNpJNUkXuk7q8cWrqMg1auqvxeRx4s8HRMlI4DMbdi3brwZBUwD3QVd3duizUY9MwpMspe1OMBk3OVofn-q2bIF4Ct61qd8BFX-J4qrtco4b_s5vmaSpaaBR99nOis_xeoeV-4z5NO2LpvH_gdyBQYkwKThlNuOP4h4k3cymH8eC3bbQtVeWZ5fAcplhTFWWJkqUJw99HbcmqYIuoH_KkvWu2KLRnUvlqMZRB-FuFIszXgI79jfyYsvWoV3t0uJC-WVGFpNiqT21tMCOU7FjSRu4lvd_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویناک اینارم از ۴۰۱ گذاشته و میگه من اون موقع هم خایمال نبودم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80275" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=TA9MHIVo_O6U15K0LzpvGz2-svtlaIBVk8d3YpoEMUWJNR8M--wo6W6mNgpFuXDsXQ5sfDfTZAuta3JiA1J-0TfY0v5dnkELkRAX3bYCcgl-l90i2k2e99eouUCBBnU5WUQme6DfpfKHxuGE_W2PJaCB2cfC2jci60cFLi4kl3H4gW6rOo7A4-VWZKcjfqHNAPkeJdGhmD8_TVOXt5uiRB0BQ7tk9A7G-lIQ66UB7570TBM9bLtaCJzNhFu1sJWG_392aO0KyHh8GrQmwHWuYMvK3zuuKdGkE74H64wqCa3-MUZgtQT3TAadAaJVXJP57WTSDhVVr6WvxYxoj58-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=TA9MHIVo_O6U15K0LzpvGz2-svtlaIBVk8d3YpoEMUWJNR8M--wo6W6mNgpFuXDsXQ5sfDfTZAuta3JiA1J-0TfY0v5dnkELkRAX3bYCcgl-l90i2k2e99eouUCBBnU5WUQme6DfpfKHxuGE_W2PJaCB2cfC2jci60cFLi4kl3H4gW6rOo7A4-VWZKcjfqHNAPkeJdGhmD8_TVOXt5uiRB0BQ7tk9A7G-lIQ66UB7570TBM9bLtaCJzNhFu1sJWG_392aO0KyHh8GrQmwHWuYMvK3zuuKdGkE74H64wqCa3-MUZgtQT3TAadAaJVXJP57WTSDhVVr6WvxYxoj58-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناک یه اجرا از دکی گذاشت چنلش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80274" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMFyctzFhBy0AXzUIYdttQSC2PKTyOTe6krnbzhWLF_sys7pL6iZqetS-JYS_-spaYY4-FcFuoYy4fk40UWlo2Tu0XZfxvCCBqTF31yPNbU1_tZh0QSDBiR6BevRPmedo9BT7vcYj6gN8j1AcTOyPlkG5EkT32nCRpSzlk2J5o_V-nXYq7E4QonvKVja5h1kB5L0MPI4yZFfx8KvwVUR1Ty0TASstDMZVnBNeNUVp1yv8gU9SM_jcc2X5orjLrlYBkSWUqtibcRr8MsvThJuMFjwdhCaZ2QPsn18ydMKpPPHuFcWfkKlTX5N1VCYdStJalxJa1lWQJW5lkihp8stuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80273" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCeb0mGaKuq6BKGtQjxfxh899NCBVClFRxX3fv-hdgggRmewCJNBwVwx4iLEiGhuTWQyshYGssuZX3fJqRj-DpKTynVKcX9mQGWdahzwRfNzkHTKLVd6VP9AwMoi5VuFQfrQLV7YjLjf8Iz0lmhTG49XMFVKbedjdPcWbxFFY2t59kSQFX_4ptutBVC4l2wkUr22zC-cBtPjtca62Am5vQIeoCMwNpN72tzp--Zyki8Gb0aw1ZPg-oAwbDD_nTbuSwh7bSVOw0WGnvYwvHZzc3CzLe2-QITabW6iSSIy1i6a7oKxCpG62yaGhCMXgunpe9dW0i03gMBlEjhSwvDb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهر لیندزی گراهام جانشین او شد
فرماندار کارولینای جنوبی هنری مک مستر، خواهر لیندزی گراهام، دارلین گراهام را به عنوان جایگزین او ، سناتور این ایالت منصوب کرد.
با توجه به پیروزی لیندزی گراهام در انتخابات مقدماتی،خواهرش یک دوره شش ساله کامل در سنای آمریکا خواهد بود.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80272" target="_blank">📅 10:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ دلقک از تنگه هرمز هم میخواد بیست درصد تعرفه بگیره.
سازمان دریانوردی بین المللی اومده گفته این نقض فاحش حقوق بشره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80271" target="_blank">📅 08:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسرائیل نیست خوب لانچرا رو کشیدن بیرونا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80270" target="_blank">📅 04:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الان که شما خوابید آقا آرش بیداره و موج دوم حملات آمریکا به جنوب هم شروع شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80269" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نفت شق کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80268" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کنکوری های عزیز ایران بخوابید، کمک در راه نیست.
ترامپ: معتقدم دستیابی به توافق با ایران همچنان امکان‌پذیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/80267" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا که مجبورید امتحان بدید حداقل بخونید تا دوازده سال از عمرتون که اینطوری گذشت بگا نره و ی ثمره ای داشته باشه، با آرزوی موفقیت برای تک تک شما در امتحانات پیش رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80266" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">من که میدونم این سری هم جنگ نمیشه ولی نمیگم که دانش آموزا همچنان امیدوار بمونن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80265" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایرانم به رسم همیشه عربارو داره میکوبه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80264" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آمریکا هم یاد گرفته ها
دیگه جنگنده بلند نمیکنه هزینه الکی داشته باشه
یدفه صدتا راکت شلیک میکنه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80263" target="_blank">📅 01:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5gAtFiPrnjZNkZCE2fiS7y9nPQMzq1W2Dan4z9-O6zrWtdZcFQ0re78s9YgSN3AYWtC512yOXeYo3P8O03E3lSTYELMSoIl7ArYwf6XzX4L0ZVyB_fAbi5A8eDoBO3S0FKjRYrJZJdVlT5JPWWfOnvqgb16M9F1Zotmtl5qBJKeAO8IbOqQhQOounKzdeoqCClecHEvHx0ZqCkFBFXktHqtQ__YEw7kNO7oKbfyvRlZeZfUVoB7z85tqvSWm5Nqg2F_K9qAzAVxeCUv_pnv4sdL295q5zGkQmkx1_77yHaQeEIw3OT_kD-cpKl1CduM-YgR5LLfY7WepsEBfjkcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا موشک کم اورده داره لانچر پرت میکنه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80262" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17049dea80.mp4?token=Ir6NP1xgkXfGJng6wT7ChVJVs4VWmg5sS2CjJoII01AKLCHa7iB6mN1esFLtDulBF1c-M6dG8V598DM0ns5bRye2W1p6_dCihn_tzvNMeCYfwdlOz_hNwDeVeUSHsuwey77LtZnRk5o5b0jFvYe2J1yoMv50S7e6cHEVN-Ca5raxj0AlOC2BJl-anYs7Dp6vw6TIEeyst0nKD4nr_VqJVx2pBmITiSGMMHLIsgYiviQ31gyQ7Ngg-oVbQSD-dqsiDvt1mpQYmKVGA_zXWJ-o6VtXkmYcJ5dQ7MAlGDo-B31R_zu53ilijlNFx6g0sOml7oK0BaCToT4IfoRb5cc3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17049dea80.mp4?token=Ir6NP1xgkXfGJng6wT7ChVJVs4VWmg5sS2CjJoII01AKLCHa7iB6mN1esFLtDulBF1c-M6dG8V598DM0ns5bRye2W1p6_dCihn_tzvNMeCYfwdlOz_hNwDeVeUSHsuwey77LtZnRk5o5b0jFvYe2J1yoMv50S7e6cHEVN-Ca5raxj0AlOC2BJl-anYs7Dp6vw6TIEeyst0nKD4nr_VqJVx2pBmITiSGMMHLIsgYiviQ31gyQ7Ngg-oVbQSD-dqsiDvt1mpQYmKVGA_zXWJ-o6VtXkmYcJ5dQ7MAlGDo-B31R_zu53ilijlNFx6g0sOml7oK0BaCToT4IfoRb5cc3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت حملات از جنگ ۴۰ روزه بیشتر نباشه کمتر نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80261" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حداقل کشورو بسپارید به فلیک شاید فرجی شد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80260" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جدی بعنوان کشوری که یدونه پدافند درست حسابی هم نداره بیش از حد کیرگوزی میکنید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80259" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80258" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheMojoMan</strong></div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80257" target="_blank">📅 00:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگه جنوب کشورید به هیچ وجه نزدیک اسکله و ساحل ها نشید، وضعیت خیلی کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80256" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسم نمیارم، خط جنوبی کشور کامل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80255" target="_blank">📅 00:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جم رو دارن میزنن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80254" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مشهد زلزله شد، این جدیده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80253" target="_blank">📅 00:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAꭑır</strong></div>
<div class="tg-text">این‌که تکراریه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80252" target="_blank">📅 00:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چندتا انفجار تو بندرعباس</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80251" target="_blank">📅 00:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شروع شد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80250" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه لفظی بود که یه ابرقدرت هیچوقت بلوف نمیزنه، مرتیکه قمار باز تو معنای اونم رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80249" target="_blank">📅 00:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80248" target="_blank">📅 00:22 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
